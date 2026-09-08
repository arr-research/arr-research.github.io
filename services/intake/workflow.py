"""Private editorial workflow. No route in this module publishes a manuscript."""
from __future__ import annotations

import base64
import hashlib
import io
import json
import secrets
import sqlite3
from datetime import datetime, timedelta
from email.message import EmailMessage
from pathlib import Path
from urllib.parse import quote

import click
import qrcode
from qrcode.image.svg import SvgPathFillImage
from flask import Response, abort, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash

SCHEMA = """
CREATE TABLE IF NOT EXISTS case_editors (
 submission_id TEXT NOT NULL REFERENCES submissions(id), user_id INTEGER NOT NULL REFERENCES users(id),
 assigned_by INTEGER NOT NULL REFERENCES users(id), assigned_at TEXT NOT NULL,
 PRIMARY KEY(submission_id,user_id)
);
CREATE TABLE IF NOT EXISTS access_links (
 token_hash TEXT PRIMARY KEY, submission_id TEXT NOT NULL REFERENCES submissions(id),
 expires_at TEXT NOT NULL, used_at TEXT
);
CREATE TABLE IF NOT EXISTS assessment_plans (
 id INTEGER PRIMARY KEY, submission_id TEXT NOT NULL REFERENCES submissions(id),
 manuscript_sha256 TEXT NOT NULL, providers_json TEXT NOT NULL, notice TEXT NOT NULL,
 created_by INTEGER NOT NULL REFERENCES users(id), created_at TEXT NOT NULL,
 authorized_at TEXT, authorization_hash TEXT
);
CREATE TABLE IF NOT EXISTS adjudications (
 id INTEGER PRIMARY KEY, review_id INTEGER NOT NULL REFERENCES model_reviews(id) ON DELETE CASCADE,
 basis TEXT NOT NULL, evidence TEXT NOT NULL, signed_by INTEGER NOT NULL REFERENCES users(id),
 signed_at TEXT NOT NULL, UNIQUE(review_id)
);
CREATE TABLE IF NOT EXISTS correspondence (
 id INTEGER PRIMARY KEY, submission_id TEXT NOT NULL REFERENCES submissions(id),
 kind TEXT NOT NULL, body TEXT NOT NULL, actor_user_id INTEGER REFERENCES users(id), created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS appeals (
 id INTEGER PRIMARY KEY, submission_id TEXT NOT NULL UNIQUE REFERENCES submissions(id),
 basis TEXT NOT NULL, previous_status TEXT NOT NULL, original_editor INTEGER NOT NULL REFERENCES users(id),
 created_at TEXT NOT NULL, resolved_by INTEGER REFERENCES users(id), resolved_at TEXT, resolution TEXT
);
CREATE TABLE IF NOT EXISTS publication_permissions (
 submission_id TEXT PRIMARY KEY REFERENCES submissions(id), manuscript_sha256 TEXT NOT NULL,
 license TEXT NOT NULL, authorized_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS mail_outbox (
 id INTEGER PRIMARY KEY, submission_id TEXT REFERENCES submissions(id), recipient TEXT NOT NULL,
 subject TEXT NOT NULL, body TEXT NOT NULL, state TEXT NOT NULL DEFAULT 'pending',
 created_at TEXT NOT NULL, sent_at TEXT, message_id TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS editor_invites (
 token_hash TEXT PRIMARY KEY, email TEXT NOT NULL, name TEXT NOT NULL,
 role TEXT NOT NULL CHECK(role IN ('operator','independent_editor')), expires_at TEXT NOT NULL, used_at TEXT
);
CREATE TABLE IF NOT EXISTS enrollments (
 token_hash TEXT PRIMARY KEY REFERENCES editor_invites(token_hash), session_hash TEXT NOT NULL,
 totp_secret TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS recovery_codes (
 user_id INTEGER NOT NULL REFERENCES users(id), code_hash TEXT NOT NULL UNIQUE, used_at TEXT
);
"""


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def authenticator_uri(email, secret):
    return 'otpauth://totp/' + quote('AIRR:' + email) + '?secret=' + secret + '&issuer=AIRR'


def migrate(db):
    db.executescript(SCHEMA)
    columns = {row[1] for row in db.execute("PRAGMA table_info(submissions)")}
    for name, definition in (("parent_id", "TEXT REFERENCES submissions(id)"),
                             ("revision_number", "INTEGER NOT NULL DEFAULT 1")):
        if name not in columns:
            db.execute(f"ALTER TABLE submissions ADD COLUMN {name} {definition}")
    db.commit()


def install(app, a):
    def launch_approved():
        try:
            approval = json.loads(Path(app.config['LAUNCH_APPROVAL_FILE']).read_text())
        except (OSError, ValueError):
            return False
        # Readiness for receiving is separate from authority to decide a
        # conflicted case. The per-case recusal and appeal guards remain below.
        if not isinstance(approval, dict) or approval.get('policy_version') != 'AIRR-PILOT-1.0':
            return False
        required = {'postal_contact', 'data_handling_review', 'storage_and_restore',
                    'https', 'operator_2fa', 'backup_schedule',
                    'monitoring', 'incident_procedure', 'end_to_end'}
        checks = approval.get('checks', {})
        evidence = approval.get('evidence', {})
        if not isinstance(checks, dict) or not isinstance(evidence, dict):
            return False
        if not all(checks.get(k) is True and isinstance(evidence.get(k), str) and evidence[k].strip() for k in required):
            return False
        source = approval.get('authorization_source')
        if approval.get('authorized_by') != app.config['OPERATOR_EMAIL'] or not isinstance(source, str) or not source.strip():
            return False
        try:
            authorized_at = datetime.fromisoformat(approval.get('authorized_at', ''))
            if authorized_at.tzinfo is None or authorized_at > a.now():
                return False
        except (ValueError, TypeError):
            return False
        return a.get_db().execute("SELECT 1 FROM users WHERE email=? AND role='operator' AND active=1 AND totp_secret IS NOT NULL",
                                  (approval['authorized_by'],)).fetchone() is not None

    def case(case_id):
        row = a.get_db().execute("SELECT s.*,u.email,u.display_name FROM submissions s JOIN users u ON u.id=s.user_id WHERE s.id=?", (case_id,)).fetchone()
        if not row:
            abort(404)
        return row

    def author_case(case_id):
        access = session.get("author_case") or {}
        if access.get("id") != case_id or access.get("expires", "") < a.iso():
            abort(404)
        return case(case_id)

    def current_plan(case_id):
        return a.get_db().execute("SELECT * FROM assessment_plans WHERE submission_id=? ORDER BY id DESC LIMIT 1", (case_id,)).fetchone()

    def enqueue(row, subject, body, access=True):
        db = a.get_db()
        if access:
            token = secrets.token_urlsafe(32)
            db.execute("INSERT INTO access_links VALUES(?,?,?,NULL)", (digest(token), row['id'], a.iso(a.now() + timedelta(days=7))))
            body += f"\n\nOpen your private case (single-use link, valid for 7 days):\n{app.config['PUBLIC_ORIGIN']}/case/access/{token}\n"
        db.execute("INSERT INTO mail_outbox(submission_id,recipient,subject,body,created_at,message_id) VALUES(?,?,?,?,?,?)",
                   (row['id'], row['email'], subject, body + "\n\nAIRR.SCIENCE\nContact: " + app.config['OPERATOR_EMAIL'], a.iso(), f"<{secrets.token_hex(24)}@airr.science>"))
        db.commit()

    def deliver(outbox_id):
        db = a.get_db()
        row = db.execute("SELECT * FROM mail_outbox WHERE id=?", (outbox_id,)).fetchone()
        if not row or row['state'] != 'pending':
            return False
        if not app.config['SMTP_HOST'] or not app.config['SMTP_FROM']:
            return False
        if db.execute("UPDATE mail_outbox SET state='sending' WHERE id=? AND state='pending'", (outbox_id,)).rowcount != 1:
            db.commit()
            return False
        db.commit()
        message = EmailMessage()
        message['Subject'] = row['subject'].replace('\r', ' ').replace('\n', ' ')
        message['From'] = 'AIRR.SCIENCE <' + app.config['SMTP_FROM'] + '>'
        message['To'] = row['recipient']
        message['Reply-To'] = app.config['OPERATOR_EMAIL']
        message['Message-ID'] = row['message_id']
        message.set_content(row['body'])
        ok = a.send_mail(message)
        # SMTP disconnect can be ambiguous. Do not silently retry and duplicate mail.
        db.execute("UPDATE mail_outbox SET state=?,sent_at=? WHERE id=?", ('sent' if ok else 'uncertain', a.iso() if ok else None, outbox_id))
        db.commit()
        a.audit('author_notification_sent' if ok else 'author_notification_uncertain', row['submission_id'], outbox_id=outbox_id)
        return ok

    @app.before_request
    def protect_workflow():
        if request.path.startswith('/admin/') and request.view_args and request.view_args.get('submission_id') and getattr(g, 'user', None) and g.user['role'] == 'independent_editor':
            assigned = a.get_db().execute('SELECT 1 FROM case_editors WHERE submission_id=? AND user_id=?', (request.view_args['submission_id'], g.user['id'])).fetchone()
            if not assigned:
                abort(404)
        if request.endpoint == 'submit':
            parent_id = request.values.get('revision_of')
            if parent_id:
                row = author_case(parent_id)
                if row['status'] != 'changes_requested':
                    abort(409, 'A revision must follow an editorial request for changes.')
                if request.method == 'POST' and request.form.get('email', '').strip().lower() != row['email'].lower():
                    abort(403)
                g.revision_parent = row
            elif not app.config['INTAKE_OPEN'] or (not app.config['TESTING'] and not launch_approved()):
                return render_template('closed.html'), 503
        if request.endpoint in {'record_model_review', 'decision'} and request.method == 'POST':
            row = case(request.view_args['submission_id'])
            if not getattr(g, 'user', None) or g.user['role'] not in {'operator', 'independent_editor'}:
                return None  # Existing authentication decorator handles it.
            if row['status'] in {'superseded', 'appeal_pending'}:
                abort(409, 'Use the current revision or the independent appeal procedure.')
            if request.endpoint == 'record_model_review':
                if row['scan_status'] != 'clean' or row['status'] not in {'eligible', 'under_assessment', 'changes_requested'}:
                    abort(409, 'Only a clean, open case can receive an assessment.')
                plan = current_plan(row['id'])
                if not plan or not plan['authorized_at']:
                    abort(409, 'The author must authorize the declared provider-specific plan first.')
                try:
                    report = json.loads(request.form.get('response_json', ''))
                    pair = (report.get('provider'), report.get('model_id'))
                except (ValueError, AttributeError):
                    abort(400)
                if pair not in {(x['provider'], x['model_id']) for x in json.loads(plan['providers_json'])}:
                    abort(409, 'This provider and model are not in the authorized assessment plan.')

    def can_accept(row, reviews):
        plan = current_plan(row['id'])
        if not plan or not plan['authorized_at'] or plan['manuscript_sha256'] != row['sha256']:
            return False
        expected = {(x['provider'], x['model_id']) for x in json.loads(plan['providers_json'])}
        actual = {(x['provider'], x['model_id']) for x in reviews}
        if not expected.issubset(actual):
            return False
        for review in reviews:
            if review['recommendation'] != 'accept' or review['unresolved_material_objections']:
                ruling = a.get_db().execute("SELECT * FROM adjudications WHERE review_id=?", (review['id'],)).fetchone()
                if not ruling:
                    return False
                if row['operator_conflict'] and a.get_db().execute("SELECT role FROM users WHERE id=?", (ruling['signed_by'],)).fetchone()[0] != 'independent_editor':
                    return False
        return True

    def received(case_id):
        db = a.get_db()
        parent = getattr(g, 'revision_parent', None)
        if parent:
            db.execute("UPDATE submissions SET parent_id=?,revision_number=? WHERE id=?", (parent['id'], parent['revision_number'] + 1, case_id))
            if case(case_id)['scan_status'] != 'infected':
                db.execute("UPDATE submissions SET status='superseded',updated_at=?,delete_after=? WHERE id=?", (a.iso(), a.iso(a.now() + timedelta(days=30)), parent['id']))
            db.commit()
            a.audit('revision_received', case_id, parent_id=parent['id'])
        row = case(case_id)
        if row['scan_status'] != 'infected':
            enqueue(row, f"AIRR submission registered: {case_id}",
                    f"Your private manuscript has been registered as {case_id}, revision {row['revision_number']}.\nRegistration is not acceptance or publication.\nManuscript SHA-256: {row['sha256']}\nSafety checks: {row['scan_status']}\nNo donation is required.")

    def decided(case_id):
        row = case(case_id)
        body = f"Case: {case_id}\nDecision: {row['status'].replace('_', ' ')}\nReason: {row['decision_reason']}\n\n{row['decision_note'] or ''}\n\nAcceptance does not publish the manuscript. You may appeal an editorial decision once within 30 days through the private case page. An independent editor handles appeals."
        enqueue(row, f"AIRR editorial decision: {case_id}", body)

    app.extensions['editorial'] = dict(can_accept=can_accept, received=received, decided=decided,
                                       enqueue=enqueue, deliver=deliver, launch_approved=launch_approved)

    @app.context_processor
    def workflow_context():
        def details(case_id):
            db = a.get_db()
            return dict(plan=current_plan(case_id),
                        available_editors=db.execute("SELECT id,display_name FROM users WHERE role='independent_editor' AND active=1").fetchall() if g.user and g.user['role']=='operator' else [],
                        assigned_editors=db.execute('SELECT u.display_name FROM case_editors c JOIN users u ON u.id=c.user_id WHERE c.submission_id=?', (case_id,)).fetchall(),
                        reports=db.execute('SELECT * FROM model_reviews WHERE submission_id=? ORDER BY id', (case_id,)).fetchall(),
                        messages=db.execute('SELECT * FROM correspondence WHERE submission_id=? ORDER BY id', (case_id,)).fetchall(),
                        mail=db.execute('SELECT id,state,created_at,sent_at,subject FROM mail_outbox WHERE submission_id=? ORDER BY id', (case_id,)).fetchall(),
                        rulings=db.execute('SELECT d.*,u.display_name FROM adjudications d JOIN users u ON u.id=d.signed_by JOIN model_reviews r ON r.id=d.review_id WHERE r.submission_id=?', (case_id,)).fetchall(),
                        appeal=db.execute('SELECT * FROM appeals WHERE submission_id=?', (case_id,)).fetchone(),
                        permission=db.execute('SELECT * FROM publication_permissions WHERE submission_id=?', (case_id,)).fetchone(),
                        children=db.execute('SELECT id,revision_number,status FROM submissions WHERE parent_id=?', (case_id,)).fetchall())
        return {'workflow_details': details}

    @app.post('/admin/submission/<submission_id>/assign-editor')
    @a.editor_required
    def assign_editor(submission_id):
        a.require_csrf()
        row = case(submission_id)
        if g.user['role'] != 'operator':
            abort(403)
        editor = a.get_db().execute("SELECT * FROM users WHERE id=? AND role='independent_editor' AND active=1", (request.form.get('editor_id'),)).fetchone()
        if not editor or editor['id'] == row['user_id'] or not request.form.get('unconflicted'):
            abort(400, 'Appoint an active, unconflicted editor other than the depositor.')
        a.get_db().execute('INSERT OR IGNORE INTO case_editors VALUES(?,?,?,?)', (submission_id, editor['id'], g.user['id'], a.iso()))
        a.get_db().commit()
        a.audit('independent_editor_assigned', submission_id, editor_id=editor['id'])
        return redirect(url_for('submission_detail', submission_id=submission_id))

    @app.post('/admin/submission/<submission_id>/plan')
    @a.editor_required
    def declare_plan(submission_id):
        a.require_csrf()
        row = case(submission_id)
        if row['scan_status'] != 'clean' or row['status'] not in {'eligible', 'under_assessment', 'changes_requested'}:
            abort(409)
        if a.get_db().execute('SELECT 1 FROM model_reviews WHERE submission_id=?', (submission_id,)).fetchone():
            abort(409, 'The declared round cannot be changed after reports have been recorded.')
        notice = request.form.get('notice', '').strip()
        try:
            providers = json.loads(request.form['providers']) if request.form.get('providers') else [
                {'provider': request.form.get(f'provider_{i}', '').strip(), 'model_id': request.form.get(f'model_{i}', '').strip()}
                for i in range(1, 4) if request.form.get(f'provider_{i}') or request.form.get(f'model_{i}')]
            if not isinstance(providers, list) or not 1 <= len(providers) <= 6:
                raise ValueError
            for item in providers:
                if set(item) != {'provider', 'model_id'} or any(not isinstance(v, str) or not 2 <= len(v.strip()) <= 160 for v in item.values()):
                    raise ValueError
            if len({(p['provider'], p['model_id']) for p in providers}) != len(providers):
                raise ValueError
        except (ValueError, TypeError):
            abort(400, 'Enter a list of exact provider and model_id pairs without duplicates.')
        if not 80 <= len(notice) <= 6000:
            abort(400, 'Explain the named services, confidentiality, retention and transfer safeguards (80–6000 characters).')
        db = a.get_db()
        db.execute('INSERT INTO assessment_plans(submission_id,manuscript_sha256,providers_json,notice,created_by,created_at) VALUES(?,?,?,?,?,?)',
                   (submission_id, row['sha256'], json.dumps(providers), notice, g.user['id'], a.iso()))
        db.commit()
        enqueue(row, f'AIRR assessment authorization: {submission_id}',
                f'Please review the proposed assessment services in your private case and authorize them before we transfer the manuscript.\n\n{notice}')
        a.audit('assessment_plan_declared', submission_id)
        flash('Plan recorded. The author authorization request is queued.', 'success')
        return redirect(url_for('submission_detail', submission_id=submission_id))

    @app.route('/case/access/<token>', methods=['GET', 'POST'])
    def case_access(token):
        if len(token) > 100:
            abort(404)
        row = a.get_db().execute('SELECT * FROM access_links WHERE token_hash=? AND used_at IS NULL AND expires_at>?', (digest(token), a.iso())).fetchone()
        if not row:
            abort(404, 'This link is expired or already used. Request a new link from AIRR.')
        if request.method == 'POST':
            a.require_csrf()
            db = a.get_db()
            if db.execute('UPDATE access_links SET used_at=? WHERE token_hash=? AND used_at IS NULL', (a.iso(), digest(token))).rowcount != 1:
                abort(409)
            db.commit()
            session.clear()
            session['author_case'] = {'id': row['submission_id'], 'expires': a.iso(a.now() + timedelta(hours=8))}
            return redirect(url_for('author_view', submission_id=row['submission_id']))
        return render_template('access.html')

    @app.route('/case/<submission_id>', methods=['GET', 'POST'])
    def author_view(submission_id):
        row = author_case(submission_id)
        db = a.get_db()
        if request.method == 'POST':
            a.require_csrf()
            a.enforce_rate('case-actions', 30, 3600)
            action = request.form.get('action')
            if action == 'authorize':
                plan = current_plan(submission_id)
                if row['status'] not in {'eligible', 'under_assessment', 'changes_requested'} or not plan or str(plan['id']) != request.form.get('plan_id') or not request.form.get('authorization'):
                    abort(409)
                if plan['authorized_at']:
                    abort(409)
                proof = digest(plan['notice'] + plan['providers_json'] + row['sha256'])
                db.execute('UPDATE assessment_plans SET authorized_at=?,authorization_hash=? WHERE id=?', (a.iso(), proof, plan['id']))
                db.commit()
                a.audit('provider_plan_authorized', submission_id, plan_id=plan['id'], proof=proof)
            elif action == 'reply':
                body = request.form.get('body', '').strip()
                if not 20 <= len(body) <= 12000 or row['status'] in {'withdrawn', 'removed', 'superseded'}:
                    abort(400)
                db.execute('INSERT INTO correspondence(submission_id,kind,body,created_at) VALUES(?,?,?,?)', (submission_id, 'author_response', body, a.iso()))
                db.commit()
                a.audit('author_response_received', submission_id)
            elif action == 'withdraw':
                if row['status'] in {'accepted_for_publication', 'legal_hold', 'removed', 'withdrawn', 'superseded'}:
                    abort(409)
                db.execute("UPDATE submissions SET status='withdrawn',updated_at=?,delete_after=? WHERE id=?", (a.iso(), a.iso(a.now() + timedelta(days=7)), submission_id))
                db.commit()
                a.audit('author_withdrawal', submission_id)
            elif action == 'appeal':
                basis = request.form.get('body', '').strip()
                if row['status'] not in {'declined', 'changes_requested'} or not row['decided_at'] or row['decided_at'] < a.iso(a.now() - timedelta(days=30)) or len(basis) < 40 or len(basis) > 12000:
                    abort(409)
                try:
                    db.execute('INSERT INTO appeals(submission_id,basis,previous_status,original_editor,created_at) VALUES(?,?,?,?,?)', (submission_id, basis, row['status'], row['decision_by'], a.iso()))
                    db.execute("UPDATE submissions SET status='appeal_pending',delete_after=NULL,updated_at=? WHERE id=?", (a.iso(), submission_id))
                    db.commit()
                except sqlite3.IntegrityError:
                    db.rollback()
                    abort(409, 'Only one appeal is allowed for this decision.')
                a.audit('appeal_received', submission_id)
            elif action == 'publication':
                license_id = request.form.get('license')
                if row['status'] != 'accepted_for_publication' or not request.form.get('publication_confirm') or license_id not in {'CC-BY-4.0', 'CC-BY-SA-4.0', 'CC0-1.0'}:
                    abort(409)
                try:
                    db.execute('INSERT INTO publication_permissions VALUES(?,?,?,?)', (submission_id, row['sha256'], license_id, a.iso()))
                    db.commit()
                except sqlite3.IntegrityError:
                    db.rollback()
                    abort(409, 'Publication permission is already recorded; contact AIRR for a correction.')
                a.audit('publication_permission_recorded', submission_id, license=license_id, sha256=row['sha256'])
            else:
                abort(400)
            flash('Your response has been recorded.', 'success')
            return redirect(url_for('author_view', submission_id=submission_id))
        return render_template('author-case.html', submission=row)

    @app.post('/admin/submission/<submission_id>/adjudicate/<int:review_id>')
    @a.editor_required
    def adjudicate(submission_id, review_id):
        a.require_csrf()
        row = case(submission_id)
        if row['status'] not in {'eligible', 'under_assessment', 'changes_requested', 'awaiting_independent_decision'} or row['user_id'] == g.user['id']:
            abort(409)
        if row['operator_conflict'] and g.user['role'] != 'independent_editor':
            abort(403, 'An independent editor must adjudicate this conflicted case.')
        review = a.get_db().execute('SELECT * FROM model_reviews WHERE id=? AND submission_id=?', (review_id, submission_id)).fetchone()
        basis, evidence = request.form.get('basis', '').strip(), request.form.get('evidence', '').strip()
        if not review or not 80 <= len(basis) <= 6000 or not 40 <= len(evidence) <= 6000 or not request.form.get('all_objections_addressed'):
            abort(400, 'A claim-by-claim basis and inspectable evidence are required.')
        try:
            a.get_db().execute('INSERT INTO adjudications(review_id,basis,evidence,signed_by,signed_at) VALUES(?,?,?,?,?)', (review_id, basis, evidence, g.user['id'], a.iso()))
            a.get_db().commit()
        except sqlite3.IntegrityError:
            a.get_db().rollback()
            abort(409, 'The signed adjudication cannot be overwritten.')
        a.audit('review_adjudicated', submission_id, review_id=review_id)
        return redirect(url_for('submission_detail', submission_id=submission_id))

    @app.post('/admin/submission/<submission_id>/appeal')
    @a.editor_required
    def resolve_appeal(submission_id):
        a.require_csrf()
        row = case(submission_id)
        appeal = a.get_db().execute('SELECT * FROM appeals WHERE submission_id=?', (submission_id,)).fetchone()
        if not appeal or appeal['resolved_at'] or row['status'] != 'appeal_pending':
            abort(409)
        if g.user['role'] != 'independent_editor' or g.user['id'] in {appeal['original_editor'], row['user_id']}:
            abort(403)
        resolution = request.form.get('resolution', '').strip()
        outcome = request.form.get('outcome')
        if len(resolution) < 80 or len(resolution) > 6000 or outcome not in {'uphold', 'reopen'}:
            abort(400)
        state = appeal['previous_status'] if outcome == 'uphold' else 'changes_requested'
        db = a.get_db()
        db.execute('UPDATE appeals SET resolved_by=?,resolved_at=?,resolution=? WHERE id=?', (g.user['id'], a.iso(), resolution, appeal['id']))
        db.execute('UPDATE submissions SET status=?,updated_at=?,delete_after=? WHERE id=?', (state, a.iso(), a.iso(a.now() + timedelta(days=30)) if state == 'declined' else None, submission_id))
        db.commit()
        enqueue(row, f'AIRR independent appeal decision: {submission_id}', f'Outcome: {outcome}\n\n{resolution}')
        a.audit('appeal_resolved', submission_id, outcome=outcome)
        return redirect(url_for('submission_detail', submission_id=submission_id))

    @app.post('/admin/submission/<submission_id>/notify')
    @a.editor_required
    def send_case_mail(submission_id):
        a.require_csrf()
        row = case(submission_id)
        if request.form.get('new_link'):
            enqueue(row, f'AIRR private case access: {submission_id}', 'Use the private case page to review updates, reply or exercise your submission rights.')
        pending = a.get_db().execute("SELECT id FROM mail_outbox WHERE submission_id=? AND state='pending' ORDER BY id", (submission_id,)).fetchall()
        results = [deliver(x['id']) for x in pending]
        flash('Messages sent.' if results and all(results) else 'Some messages could not be confirmed. Inspect the delivery state before retrying.', 'success' if results and all(results) else 'error')
        return redirect(url_for('submission_detail', submission_id=submission_id))

    @app.cli.command('send-pending-mail')
    def send_pending_mail():
        rows = a.get_db().execute("SELECT id FROM mail_outbox WHERE state='pending' ORDER BY id LIMIT 50").fetchall()
        failures = []
        for row in rows:
            sent = deliver(row['id'])
            click.echo(f"Message {row['id']}: {'sent' if sent else 'not confirmed'}")
            if not sent:
                failures.append(row['id'])
        if failures:
            raise click.ClickException('Some deliveries are unconfirmed; inspect the outbox before resending.')

    @app.cli.command('launch-status')
    def launch_status():
        click.echo(json.dumps({'public_switch': app.config['INTAKE_OPEN'], 'recorded_launch_checks': launch_approved()}))

    @app.cli.command('workflow-sweep')
    def workflow_sweep():
        db = a.get_db()
        db.execute('DELETE FROM access_links WHERE expires_at<?', (a.iso(),))
        db.execute('DELETE FROM enrollments WHERE token_hash IN (SELECT token_hash FROM editor_invites WHERE expires_at<? OR used_at IS NOT NULL)', (a.iso(),))
        db.execute('DELETE FROM editor_invites WHERE expires_at<?', (a.iso(),))
        # Completed notification bodies can contain bearer links and private replies.
        db.execute("UPDATE mail_outbox SET body='[erased after delivery retention]' WHERE state='sent' AND sent_at<?", (a.iso(a.now() - timedelta(days=7)),))
        db.commit()
        click.echo('Expired access/setup links and delivered message bodies swept.')

    @app.cli.command('invite-editor')
    @click.argument('email')
    @click.option('--name', required=True)
    @click.option('--role', type=click.Choice(['operator', 'independent_editor']), required=True)
    def invite_editor(email, name, role):
        email = email.lower().strip()
        if not a.valid_email(email) or a.get_db().execute('SELECT 1 FROM users WHERE email=? AND active=1', (email,)).fetchone():
            raise click.ClickException('Invalid email or an active account already exists. No credentials were changed.')
        token = secrets.token_urlsafe(32)
        a.get_db().execute('INSERT INTO editor_invites VALUES(?,?,?,?,?,NULL)', (digest(token), email, name, role, a.iso(a.now() + timedelta(hours=24))))
        a.get_db().commit()
        click.echo(app.config['PUBLIC_ORIGIN'] + '/editor/setup/' + token)

    @app.route('/editor/setup/<token>', methods=['GET', 'POST'])
    def editor_setup(token):
        db = a.get_db()
        hashed = digest(token)
        invite = db.execute('SELECT * FROM editor_invites WHERE token_hash=? AND used_at IS NULL AND expires_at>?', (hashed, a.iso())).fetchone()
        if not invite:
            abort(404)
        a.enforce_rate('editor-setup', 20, 3600)
        if not session.get('enrollment_session'):
            session['enrollment_session'] = secrets.token_urlsafe(32)
        binding = digest(session['enrollment_session'])
        pending = db.execute('SELECT * FROM enrollments WHERE token_hash=?', (hashed,)).fetchone()
        # Enrollment secrets stay in the server database, never in Flask's signed plaintext cookie.
        if not pending:
            secret = base64.b32encode(secrets.token_bytes(20)).decode().rstrip('=')
            db.execute('INSERT INTO enrollments VALUES(?,?,?,?)', (hashed, binding, secret, a.iso()))
            db.commit()
            pending = db.execute('SELECT * FROM enrollments WHERE token_hash=?', (hashed,)).fetchone()
        if pending['session_hash'] != binding:
            abort(409, 'Continue in the browser where setup began, or ask the operator to issue a fresh setup link.')
        if request.method == 'POST':
            a.require_csrf()
            password = request.form.get('password', '')
            if len(password) < 14 or password != request.form.get('confirm_password') or not a.verify_totp(pending['totp_secret'], request.form.get('totp', '')):
                flash('Use matching passwords of at least 14 characters and a valid authenticator code.', 'error')
            else:
                codes = [secrets.token_hex(8) for _ in range(8)]
                try:
                    db.execute('BEGIN IMMEDIATE')
                    if db.execute('UPDATE editor_invites SET used_at=? WHERE token_hash=? AND used_at IS NULL AND expires_at>?', (a.iso(), hashed, a.iso())).rowcount != 1:
                        raise sqlite3.IntegrityError('Invite already used')
                    if db.execute('SELECT 1 FROM users WHERE email=?', (invite['email'],)).fetchone():
                        raise sqlite3.IntegrityError('Account exists')
                    cursor = db.execute('INSERT INTO users(email,display_name,password_hash,role,totp_secret,created_at) VALUES(?,?,?,?,?,?)',
                                        (invite['email'], invite['name'], generate_password_hash(password), invite['role'], pending['totp_secret'], a.iso()))
                    db.executemany('INSERT INTO recovery_codes(user_id,code_hash) VALUES(?,?)', [(cursor.lastrowid, digest(code)) for code in codes])
                    db.execute('DELETE FROM enrollments WHERE token_hash=?', (hashed,))
                    db.commit()
                except sqlite3.IntegrityError:
                    db.rollback()
                    abort(409, 'This setup cannot replace existing credentials.')
                session.clear()
                a.audit('editor_enrolled')
                return render_template('recovery-codes.html', codes=codes)
        uri = authenticator_uri(invite['email'], pending['totp_secret'])
        return render_template('editor-setup.html', invite=invite, secret=pending['totp_secret'], otp_uri=uri, setup_token=token)

    @app.get('/editor/setup/<token>/qr.svg')
    def editor_setup_qr(token):
        # A link alone cannot retrieve the shared secret: setup is bound to its browser.
        binding = session.get('enrollment_session')
        if not binding:
            abort(404)
        pending = a.get_db().execute('''SELECT e.totp_secret,e.session_hash,i.email
            FROM enrollments e JOIN editor_invites i ON i.token_hash=e.token_hash
            WHERE i.token_hash=? AND i.used_at IS NULL AND i.expires_at>?''',
            (digest(token), a.iso())).fetchone()
        if not pending or not secrets.compare_digest(pending['session_hash'], digest(binding)):
            abort(404)
        uri = authenticator_uri(pending['email'], pending['totp_secret'])
        svg = qrcode.make(uri, image_factory=SvgPathFillImage, border=4).to_string()
        return Response(svg, mimetype='image/svg+xml')

    @app.post('/login/recovery')
    def recovery_login():
        a.require_csrf()
        a.enforce_rate('recovery-login', 5, 3600)
        email = request.form.get('email', '').strip().lower()
        a.enforce_rate('recovery-email', 5, 3600, email)
        user = a.get_db().execute("SELECT * FROM users WHERE email=? AND active=1 AND role IN ('operator','independent_editor')", (email,)).fetchone()
        if not user or not a.check_password_hash(user['password_hash'], request.form.get('password', '')):
            abort(403, 'Invalid recovery credentials.')
        code_hash = digest(request.form.get('recovery_code', '').strip().lower())
        db = a.get_db()
        if db.execute('UPDATE recovery_codes SET used_at=? WHERE user_id=? AND code_hash=? AND used_at IS NULL', (a.iso(), user['id'], code_hash)).rowcount != 1:
            db.rollback()
            abort(403, 'Invalid recovery credentials.')
        db.commit()
        session.clear()
        session['user_id'] = user['id']
        session.permanent = True
        a.audit('editor_recovery_login')
        flash('A one-use recovery code was consumed. Contact the operator to restore your authenticator through the recovery procedure.', 'warning')
        return redirect(url_for('dashboard'))

    @app.get('/admin/submission/<submission_id>/release-package')
    @a.editor_required
    def release_package(submission_id):
        row = case(submission_id)
        permission = a.get_db().execute('SELECT * FROM publication_permissions WHERE submission_id=?', (submission_id,)).fetchone()
        if row['status'] != 'accepted_for_publication' or not permission or permission['manuscript_sha256'] != row['sha256']:
            abort(409, 'Final acceptance and exact-version publication permission are both required.')
        # Export only the approved scholarly handoff. No email, bearer link, SMTP secret or private conversation.
        db = a.get_db()
        manifest = {'submission_id': row['id'], 'revision': row['revision_number'], 'sha256': row['sha256'],
                    'title': row['title'], 'authors': row['authors'], 'abstract': row['abstract'],
                    'classification': json.loads(row['classification_json']), 'license': permission['license'],
                    'submission_channel': row['submission_channel'], 'agent_provenance': json.loads(row['agent_provenance_json']),
                    'decision_reason': row['decision_reason'], 'decided_at': row['decided_at'],
                    'conflict_disclosed': bool(row['operator_conflict']),
                    'editor': db.execute('SELECT display_name FROM users WHERE id=?', (row['decision_by'],)).fetchone()[0],
                    'reports': [json.loads(x[0]) for x in db.execute('SELECT response_json FROM model_reviews WHERE submission_id=? ORDER BY id', (submission_id,))],
                    'adjudications': [dict(x) for x in db.execute('SELECT d.basis,d.evidence,d.signed_at,u.display_name AS editor,r.response_sha256 FROM adjudications d JOIN model_reviews r ON r.id=d.review_id JOIN users u ON u.id=d.signed_by WHERE r.submission_id=?', (submission_id,))]}
        a.audit('release_handoff_exported', submission_id)
        return a.send_file(io.BytesIO(json.dumps(manifest, ensure_ascii=False, indent=2).encode()), mimetype='application/json', as_attachment=True, download_name=submission_id + '-release-handoff.json')
