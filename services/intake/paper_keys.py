"""Account-free, paper-scoped bearer access. Raw keys never enter DB, URLs or logs."""
import hashlib
import json
import secrets
import os
import re
import subprocess
import tempfile
import click
from datetime import timedelta
from pathlib import Path
from werkzeug.datastructures import FileStorage

from flask import abort, flash, g, jsonify, redirect, render_template, request, session, url_for

EDITABLE = {'eligible', 'under_assessment', 'changes_requested', 'awaiting_independent_decision',
            'accepted_for_publication', 'published', 'quarantined'}
FIELDS = {'title': 500, 'authors': 1000, 'abstract': 5000, 'primary_subject': 200,
          'specific_topic': 200, 'source_disclosure': 5000, 'change_summary': 2000}


def digest(key):
    return hashlib.sha256(key.encode()).hexdigest()


def migrate(db):
    db.executescript('''
    CREATE TABLE IF NOT EXISTS paper_keys (
      id TEXT PRIMARY KEY, user_id INTEGER NOT NULL UNIQUE REFERENCES users(id),
      key_hash TEXT NOT NULL UNIQUE, generation INTEGER NOT NULL DEFAULT 1,
      created_at TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS paper_drafts (
      id TEXT PRIMARY KEY, paper_id TEXT NOT NULL REFERENCES paper_keys(id),
      parent_id TEXT REFERENCES submissions(id), data_json TEXT NOT NULL DEFAULT '{}',
      submitted_id TEXT UNIQUE REFERENCES submissions(id), created_at TEXT NOT NULL);
    CREATE UNIQUE INDEX IF NOT EXISTS one_open_paper_draft ON paper_drafts(paper_id)
      WHERE submitted_id IS NULL;
    ''')
    db.commit()


def install(app, a):
    def opened():
        return app.config['INTAKE_OPEN'] and (app.config['TESTING'] or app.extensions['editorial']['launch_approved']())

    def access():
        if hasattr(g, 'paper_access'):
            return g.paper_access
        saved = session.get('paper_access', {})
        g.paper_access = None
        if saved.get('expires', 0) > a.now().timestamp():
            g.paper_access = a.get_db().execute('''SELECT k.* FROM paper_keys k JOIN users u ON u.id=k.user_id
                WHERE k.id=? AND k.generation=? AND u.active=1''', (saved.get('id'), saved.get('generation'))).fetchone()
        return g.paper_access

    def require_key():
        key = access()
        if not key:
            abort(401, 'Open Manage my paper and enter your secret key.')
        g.paper_actor = key['user_id']
        return key

    def sign_in(row):
        # A paper key does not establish an account/editor session.
        session.pop('paper_pending_key_hash', None)
        session['paper_access'] = {'id': row['id'], 'generation': row['generation'],
                                   'expires': a.browser_expiry()}
        session.permanent = True
        g.pop('paper_access', None)

    def owns(row):
        key = access()
        allowed = bool(key and row['user_id'] == key['user_id'])
        if allowed:
            g.paper_actor = key['user_id']
        return allowed

    def key_owner(user_id):
        return a.get_db().execute('SELECT 1 FROM paper_keys WHERE user_id=?', (user_id,)).fetchone() is not None

    app.extensions['paper_keys'] = dict(access=access, owns=owns, owner=key_owner)

    @app.cli.command('paper-draft-sweep')
    def sweep():
        db = a.get_db()
        count = db.execute('DELETE FROM paper_drafts WHERE submitted_id IS NULL AND created_at<?',
                           (a.iso(a.now() - timedelta(days=90)),)).rowcount
        db.commit()
        click.echo(f'Expired private drafts: {count}')

    @app.context_processor
    def context():
        return {'paper_access': access(), 'paper_editable': EDITABLE}

    @app.route('/paper/new', methods=['GET', 'POST'])
    def paper_new():
        if not opened():
            return render_template('closed.html'), 503
        if request.method == 'GET':
            return render_template('paper-start.html', starting=True, draft=None,
                                   values={'primary_subject': request.args.get('subject', '')})
        a.require_csrf()
        a.enforce_rate('paper-create', 10, 86400)
        a.enforce_rate('paper-create-global', 500, 86400, 'all')
        if request.form.get('website'):
            abort(400)
        raw = 'AIRR-' + secrets.token_urlsafe(32)
        ident, draft_id = secrets.token_hex(16), secrets.token_hex(16)
        db = a.get_db()
        user = db.execute("INSERT INTO users(email,display_name,password_hash,role,active,created_at) VALUES(?,?,?,'depositor',1,?)",
                          ('paper-' + ident + '@accounts.invalid', 'Paper key holder', '!', a.iso()))
        db.execute('INSERT INTO paper_keys(id,user_id,key_hash,created_at) VALUES(?,?,?,?)', (ident, user.lastrowid, digest(raw), a.iso()))
        initial = {'primary_subject': request.form.get('subject', '')[:200]}
        db.execute('INSERT INTO paper_drafts(id,paper_id,data_json,created_at) VALUES(?,?,?,?)',
                   (draft_id, ident, json.dumps(initial), a.iso()))
        db.commit()
        sign_in(db.execute('SELECT * FROM paper_keys WHERE id=?', (ident,)).fetchone())
        if request.headers.get('X-Paper-Start') == '1':
            # Only an empty draft is created here. The selected PDF stays in the
            # browser until the author requests extraction or confirms sending.
            return jsonify(key=raw, draft_url=url_for('paper_draft', draft_id=draft_id))
        return render_template('paper-key.html', secret=raw, next_url=url_for('paper_draft', draft_id=draft_id))

    @app.route('/manage', methods=['GET', 'POST'])
    def paper_manage():
        if request.method == 'POST':
            a.require_csrf()
            a.enforce_rate('paper-login', 12, 900)
            raw = request.form.get('key', '').strip()[:128]
            row = a.get_db().execute('SELECT * FROM paper_keys WHERE key_hash=?', (digest(raw),)).fetchone()
            if not row:
                flash('That key was not recognised. Paste the complete key from your saved file.', 'error')
                return render_template('paper-manage.html'), 401
            sign_in(row)
            return redirect(url_for('paper_manage'))
        key = access()
        if not key:
            return render_template('paper-manage.html')
        db = a.get_db()
        rows = db.execute('SELECT * FROM submissions WHERE user_id=? ORDER BY revision_number DESC,created_at DESC', (key['user_id'],)).fetchall()
        draft = db.execute('SELECT * FROM paper_drafts WHERE paper_id=? AND submitted_id IS NULL', (key['id'],)).fetchone()
        return render_template('paper-panel.html', submissions=rows, draft=draft)

    @app.post('/paper/close')
    def paper_close():
        a.require_csrf()
        session.pop('paper_access', None)
        session.pop('paper_pending_key_hash', None)
        return redirect(url_for('paper_manage'))

    @app.post('/paper/extract')
    def paper_extract():
        """Optional suggestions only, after scanning. No external service receives the PDF."""
        a.require_csrf()
        key = require_key()
        if not opened():
            abort(503)
        a.enforce_rate('paper-extract', 20, 3600, key['id'])
        a.enforce_rate('paper-extract-ip', 40, 3600)
        upload = request.files.get('manuscript')
        if not upload:
            abort(400)
        with tempfile.TemporaryDirectory(prefix='draft-', dir=app.config['QUARANTINE']) as folder:
            path = Path(folder) / 'paper.pdf'
            size = 0
            with path.open('wb') as stream:
                os.chmod(path, 0o600)
                first = upload.stream.read(5)
                if first != b'%PDF-':
                    return jsonify(error='Choose a PDF, or fill in the details yourself.'), 400
                stream.write(first)
                size = 5
                while chunk := upload.stream.read(1024 * 1024):
                    size += len(chunk)
                    if size > a.MAX_PDF_BYTES:
                        abort(413)
                    stream.write(chunk)
            status, _ = a.scan_file(path)
            if status != 'clean':
                return jsonify(error='The PDF could not be cleared for extraction. You can enter the details manually.'), 422
            target = Path(folder) / 'text.txt'
            try:
                result = subprocess.run(['pdftotext', '-f', '1', '-l', '2', '-enc', 'UTF-8', str(path), str(target)],
                                        timeout=10, capture_output=True, check=False)
                if result.returncode or not target.exists() or target.stat().st_size > 200000:
                    raise ValueError('No usable text')
                text = target.read_text(encoding='utf-8')
            except (OSError, ValueError, subprocess.TimeoutExpired):
                return jsonify(error='Automatic extraction is unavailable for this PDF. Enter the title and abstract below.'), 422
            lines = [line.strip() for line in text.splitlines() if line.strip()]
            title = lines[0][:500] if lines else ''
            found = re.search(r'(?is)\babstract\b\s*[:.\n]?\s*(.*?)(?:\n\s*(?:keywords|1[.\s]+introduction|introduction)\b|\Z)', text)
            abstract = re.sub(r'\s+', ' ', found.group(1)).strip()[:5000] if found else ''
            return jsonify(title=title, abstract=abstract, notice='Suggestions only. Check them against your PDF; author names are never inferred.')

    @app.post('/paper/rotate')
    def paper_rotate():
        a.require_csrf()
        key = require_key()
        if request.form.get('confirm') != 'on':
            abort(400, 'Confirm that you want to replace the key.')
        a.enforce_rate('paper-rotate', 5, 3600, key['id'])
        raw = 'AIRR-' + secrets.token_urlsafe(32)
        session['paper_pending_key_hash'] = digest(raw)
        return render_template('paper-key.html', secret=raw, rotating=True)

    @app.post('/paper/activate-key')
    def paper_activate_key():
        a.require_csrf()
        key = require_key()
        raw = request.form.get('new_key', '')[:128]
        if request.form.get('saved') != 'on' or not secrets.compare_digest(digest(raw), session.get('paper_pending_key_hash', '')):
            abort(400, 'Save the replacement key before activating it.')
        db = a.get_db()
        changed = db.execute('UPDATE paper_keys SET key_hash=?,generation=generation+1 WHERE id=? AND generation=?',
                             (digest(raw), key['id'], key['generation'])).rowcount
        if changed != 1:
            db.rollback()
            abort(409, 'The key has changed. Open your paper again.')
        db.commit()
        session.pop('paper_pending_key_hash', None)
        sign_in(db.execute('SELECT * FROM paper_keys WHERE id=?', (key['id'],)).fetchone())
        a.audit('paper_key_rotated')
        flash('Replacement key activated. The previous key and its other sessions are now closed.', 'success')
        return redirect(url_for('paper_manage'))

    def draft_row(draft_id):
        key = require_key()
        row = a.get_db().execute('SELECT * FROM paper_drafts WHERE id=? AND paper_id=?', (draft_id, key['id'])).fetchone()
        if not row:
            abort(404)
        return row

    def form_data():
        values = {k: request.form.get(k, '').strip() for k in FIELDS}
        if any(len(values[k]) > n for k, n in FIELDS.items()):
            abort(400, 'One of the fields is too long.')
        values['secondary_subject'] = request.form.getlist('secondary_subject')[:2]
        values['operator_conflict'] = request.form.get('operator_conflict') == 'on'
        return values

    @app.route('/paper/draft/<draft_id>', methods=['GET', 'POST'])
    def paper_draft(draft_id):
        row = draft_row(draft_id)
        if row['submitted_id']:
            return redirect(url_for('author_view', submission_id=row['submitted_id']))
        values = json.loads(row['data_json'])
        if request.method == 'POST':
            a.require_csrf()
            if not opened():
                return render_template('closed.html'), 503
            values = form_data()
            db = a.get_db()
            db.execute('UPDATE paper_drafts SET data_json=? WHERE id=? AND submitted_id IS NULL', (json.dumps(values), draft_id))
            db.commit()
            if request.form.get('action') == 'save':
                if request.headers.get('X-Draft-Save') == '1':
                    return jsonify(saved=True)
                flash('Draft saved. You can return with your key. Select the PDF again when you are ready to send.', 'success')
                return redirect(url_for('paper_draft', draft_id=draft_id))
            try:
                if not values['title'] or len(values['abstract']) < 80:
                    raise ValueError('Add a title and an abstract of at least 80 characters.')
                if row['parent_id'] and not values['change_summary']:
                    raise ValueError('Briefly describe what changed in this version.')
                if not all(request.form.get(x) == 'on' for x in ('agreement', 'key_saved')):
                    raise ValueError('Save your key and confirm the submission conditions.')
                classification = a.validate_classification(values['primary_subject'], values['secondary_subject'], values['specific_topic'])
                upload = request.files.get('manuscript')
                reuse = row['parent_id'] and request.form.get('reuse_pdf') == 'on'
                if reuse and upload and upload.filename:
                    raise ValueError('Choose either a new PDF or reuse the previous PDF, not both.')
                if not reuse and (not upload or not upload.filename):
                    raise ValueError('Choose your paper PDF.')
                key = require_key()
                a.enforce_rate('paper-upload', 10, 86400, key['id'])
                a.enforce_rate('paper-upload-ip', 20, 86400)
                user = db.execute('SELECT * FROM users WHERE id=?', (key['user_id'],)).fetchone()

                def reserve(connection, case_id):
                    current = connection.execute('SELECT * FROM paper_drafts WHERE id=?', (draft_id,)).fetchone()
                    if current['submitted_id']:
                        abort(409, 'This draft was already sent. Open Manage my paper for its receipt.')
                    revision = 1
                    if row['parent_id']:
                        parent = connection.execute('SELECT * FROM submissions WHERE id=? AND user_id=?', (row['parent_id'], key['user_id'])).fetchone()
                        if not parent or parent['status'] not in EDITABLE:
                            abort(409, 'This version cannot currently be revised.')
                        if connection.execute('SELECT 1 FROM submissions WHERE parent_id=?', (parent['id'],)).fetchone():
                            abort(409, 'A newer version already exists. Open Manage my paper.')
                        revision = parent['revision_number'] + 1
                    connection.execute('UPDATE submissions SET parent_id=?,revision_number=? WHERE id=?', (row['parent_id'], revision, case_id))
                    connection.execute('UPDATE paper_drafts SET submitted_id=?,data_json=? WHERE id=?', (case_id, json.dumps(values), draft_id))
                    connection.execute('INSERT INTO audit_log(occurred_at,actor_user_id,event,submission_id,detail_json) VALUES(?,?,?,?,?)',
                                       (a.iso(), key['user_id'], 'paper_key_submission_confirmed', case_id,
                                        json.dumps({'policy': 'AIRR-PAPER-KEY-1.0', 'key_saved': True, 'agreement': True})))
                    if values['change_summary']:
                        connection.execute('INSERT INTO correspondence(submission_id,kind,body,created_at) VALUES(?,?,?,?)',
                                           (case_id, 'author_revision', values['change_summary'], a.iso()))

                from .storage import receive
                reused_stream = None
                try:
                    if reuse:
                        parent = db.execute('SELECT * FROM submissions WHERE id=? AND user_id=?', (row['parent_id'], key['user_id'])).fetchone()
                        path = Path(app.config['QUARANTINE']) / parent['stored_name'] if parent else None
                        if not parent or parent['scan_status'] != 'clean' or not path.is_file():
                            raise ValueError('The previous PDF is no longer available privately. Select a PDF to continue.')
                        reused_stream = path.open('rb')
                        upload = FileStorage(stream=reused_stream, filename=parent['original_filename'])
                    result = receive(app, a, upload, dict(user_id=user['id'], email=user['email'], display_name=user['display_name'],
                        title=values['title'], authors=values['authors'] or 'Anonymous', abstract=values['abstract'],
                        classification=classification, operator_conflict=values['operator_conflict'],
                        source_disclosure=values['source_disclosure'], publication_mode='anonymous' if not values['authors'] else 'standard'), reserve)
                finally:
                    if reused_stream:
                        reused_stream.close()
                session['receipt_submission_id'] = result['id']
                flash('PDF received privately. Your key opens this paper and all its versions.', 'success')
                return redirect(url_for('author_view', submission_id=result['id']))
            except ValueError as error:
                flash(str(error), 'error')
                return render_template('paper-draft.html', draft=row, values=values), 400
        return render_template('paper-draft.html', draft=row, values=values)

    @app.post('/paper/revise/<submission_id>')
    def paper_revise(submission_id):
        a.require_csrf()
        key = require_key()
        db = a.get_db()
        db.execute('BEGIN IMMEDIATE')
        row = db.execute('SELECT * FROM submissions WHERE id=? AND user_id=?', (submission_id, key['user_id'])).fetchone()
        if not row:
            abort(404)
        if row['status'] not in EDITABLE:
            abort(409, 'This version cannot currently be revised.')
        existing = db.execute('SELECT id FROM paper_drafts WHERE paper_id=? AND submitted_id IS NULL', (key['id'],)).fetchone()
        if existing:
            db.rollback()
            return redirect(url_for('paper_draft', draft_id=existing['id']))
        if db.execute('SELECT 1 FROM submissions WHERE parent_id=?', (submission_id,)).fetchone():
            abort(409, 'Choose the latest version in Manage my paper.')
        old = db.execute('SELECT data_json FROM paper_drafts WHERE submitted_id=?', (submission_id,)).fetchone()
        data = json.loads(old['data_json']) if old else {}
        data['change_summary'] = ''
        draft_id = secrets.token_hex(16)
        db.execute('INSERT INTO paper_drafts(id,paper_id,parent_id,data_json,created_at) VALUES(?,?,?,?,?)',
                   (draft_id, key['id'], submission_id, json.dumps(data), a.iso()))
        db.commit()
        return redirect(url_for('paper_draft', draft_id=draft_id))

    @app.post('/paper/delete-draft/<draft_id>')
    def paper_delete_draft(draft_id):
        a.require_csrf()
        row = draft_row(draft_id)
        if row['submitted_id'] or request.form.get('confirm') != 'on':
            abort(409)
        a.get_db().execute('DELETE FROM paper_drafts WHERE id=? AND submitted_id IS NULL', (draft_id,))
        a.get_db().commit()
        flash('Draft deleted.', 'success')
        return redirect(url_for('paper_manage'))

    @app.post('/paper/remove/<submission_id>')
    def paper_remove(submission_id):
        a.require_csrf()
        key = require_key()
        db = a.get_db()
        db.execute('BEGIN IMMEDIATE')
        row = db.execute('SELECT * FROM submissions WHERE id=? AND user_id=?', (submission_id, key['user_id'])).fetchone()
        if not row:
            abort(404)
        if request.form.get('confirm') != 'on' or row['status'] in {'legal_hold', 'appeal_pending', 'removed'}:
            abort(409, 'Confirm the request. A legal hold or pending appeal must be resolved first.')
        if row['public_release_url']:
            db.execute('INSERT INTO correspondence(submission_id,kind,body,created_at) VALUES(?,?,?,?)',
                       (submission_id, 'withdrawal_requested', 'The key holder requests withdrawal of this published version.', a.iso()))
            message = 'Withdrawal requested. AIRR must update the public archive; existing citations and downloaded copies may remain.'
        else:
            db.execute("UPDATE submissions SET status='withdrawn',delete_after=?,updated_at=? WHERE id=?",
                       (a.iso(a.now() + timedelta(days=7)), a.iso(), submission_id))
            db.execute('UPDATE paper_drafts SET data_json=\'{}\' WHERE submitted_id=?', (submission_id,))
            message = 'Private submission withdrawn. Its PDF is scheduled for deletion in 7 days.'
        db.commit()
        a.audit('paper_removal_requested', submission_id)
        flash(message, 'success')
        return redirect(url_for('paper_manage'))
