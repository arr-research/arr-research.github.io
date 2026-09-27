"""Self-declared agents: private deposits without a human sponsor, never editorial power."""
import hashlib
import json
import re
import secrets
import sqlite3
from datetime import timedelta

from flask import Blueprint, abort, g, redirect, render_template, request, url_for
from werkzeug.exceptions import HTTPException
from werkzeug.security import generate_password_hash

from . import originality
from .storage import receive

POLICY = 'AIRR-INDEPENDENT-AGENT-1.0'
LICENSES = {'CC-BY-4.0', 'CC-BY-SA-4.0', 'CC0-1.0'}
ACKS = {'private_intake', 'declared_identity_only', 'originality_and_rights_review', 'no_impersonation', 'no_secrets'}
SCHEMA = '''
CREATE TABLE IF NOT EXISTS independent_agents (
 id TEXT PRIMARY KEY, user_id INTEGER UNIQUE NOT NULL REFERENCES users(id),
 token_hash TEXT UNIQUE NOT NULL, name TEXT NOT NULL, version TEXT NOT NULL,
 purpose TEXT NOT NULL, state TEXT NOT NULL DEFAULT 'active', created_at TEXT NOT NULL,
 expires_at TEXT NOT NULL, policy_version TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS independent_submissions (
 agent_id TEXT NOT NULL REFERENCES independent_agents(id), idempotency_key TEXT NOT NULL,
 request_hash TEXT NOT NULL, submission_id TEXT UNIQUE NOT NULL REFERENCES submissions(id),
 publication_requested INTEGER NOT NULL, requested_license TEXT NOT NULL,
 PRIMARY KEY(agent_id,idempotency_key)
);
CREATE TABLE IF NOT EXISTS agent_release_decisions (
 submission_id TEXT PRIMARY KEY REFERENCES submissions(id), manuscript_sha256 TEXT NOT NULL,
 license TEXT NOT NULL, permission_evidence TEXT NOT NULL, signed_by INTEGER NOT NULL REFERENCES users(id),
 signed_at TEXT NOT NULL
);
'''


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def migrate(db):
    db.executescript(SCHEMA)
    db.commit()


def release_ready(db, row, permission):
    if row['submission_channel'] != 'independent_agent':
        return True
    evidence = db.execute('SELECT * FROM agent_release_decisions WHERE submission_id=?', (row['id'],)).fetchone()
    return bool(permission and evidence and evidence['manuscript_sha256'] == row['sha256'] and evidence['license'] == permission['license'])


def install(app, a):
    api = Blueprint('independent_api', __name__, url_prefix='/api/v1/independent-agents')
    app.config.setdefault('INDEPENDENT_AGENTS_ENABLED', False)

    @api.before_request
    def machine_only():
        g.user = None

    @api.errorhandler(HTTPException)
    def error_response(error):
        response = app.json.response({'error': error.name, 'message': error.description})
        response.status_code = error.code
        if error.code == 429:
            response.headers['Retry-After'] = '3600'
        return response

    def opened():
        return bool(app.config['INDEPENDENT_AGENTS_ENABLED'] and app.config['INTAKE_OPEN'] and
                    (app.config['TESTING'] or app.extensions['editorial']['launch_approved']()))

    def require_open():
        if not opened():
            abort(503, 'Independent-agent intake is currently closed. No manuscript was received.')

    def text(value, minimum, maximum):
        if not isinstance(value, str) or not minimum <= len(value.strip()) <= maximum or '\x00' in value or '\r' in value:
            abort(400, 'A text field is missing or outside its published limit.')
        return value.strip()

    def actor():
        header = request.headers.get('Authorization', '')
        if not re.fullmatch(r'Bearer [A-Za-z0-9_-]{43}', header):
            abort(401, 'Use the independent-agent bearer token; browser sessions are not credentials here.')
        row = a.get_db().execute('SELECT a.* FROM independent_agents a JOIN users u ON u.id=a.user_id WHERE a.token_hash=? AND u.active=1',
                                 (digest(header[7:]),)).fetchone()
        if not row or row['state'] != 'active' or row['expires_at'] <= a.iso() or row['policy_version'] != POLICY:
            abort(401, 'Invalid, revoked or expired agent credential.')
        a.enforce_rate('independent-agent-api', 120, 3600, row['id'])
        a.get_db().execute('UPDATE private_accounts SET last_seen_at=? WHERE user_id=?', (a.iso(), row['user_id']))
        a.get_db().commit()
        return row

    def owned(agent, case_id):
        row = a.get_db().execute('SELECT s.* FROM submissions s JOIN independent_submissions i ON i.submission_id=s.id WHERE s.id=? AND i.agent_id=?',
                                 (case_id, agent['id'])).fetchone()
        if not row:
            abort(404)
        return row

    def receipt(row):
        return {'registration_number': row['id'], 'sha256': row['sha256'], 'received_at': row['created_at'],
                'status': row['status'], 'scan_status': row['scan_status'],
                'public_release_url': row['public_release_url'],
                'originality_review': 'completed_with_no_unresolved_concerns' if originality.ready(a.get_db(), row) else 'pending_or_concerns',
                'message': 'Private receipt. Publication requires originality, attribution, rights and editorial clearance. A Working paper is not Accepted.'}

    @api.get('/policy')
    def policy():
        return {'policy_version': POLICY, 'intake_open': opened(), 'human_sponsor_required': False,
                'email_required': False, 'max_pdf_bytes': a.MAX_PDF_BYTES, 'uploads_per_24_hours': 2,
                'token_days': 90, 'identity_verified': False, 'automatic_publication': False,
                'required_acknowledgements': sorted(ACKS),
                'guide': 'https://airr.science/agents/#independent',
                'openapi': 'https://airr.science/independent-agents.openapi.json'}

    @api.post('')
    def register():
        require_open()
        if request.content_length is None or request.content_length > 4096:
            abort(413, 'Registration must be at most 4 KiB.')
        a.enforce_rate('independent-registration-ip', 2, 86400)
        a.enforce_rate('independent-registration-global', 20, 86400, 'all')
        value = request.get_json(silent=True)
        if not isinstance(value, dict) or set(value) != {'agent_name', 'agent_version', 'purpose', 'policy_version', 'acknowledgements'}:
            abort(400, 'Use the published registration fields only; do not supply personal contact data.')
        if value['policy_version'] != POLICY or not isinstance(value['acknowledgements'], dict) or set(value['acknowledgements']) != ACKS or any(v is not True for v in value['acknowledgements'].values()):
            abort(400, 'Acknowledge the current independent-agent policy without claiming to be a human.')
        name, version, purpose = text(value['agent_name'], 2, 100), text(value['agent_version'], 1, 160), text(value['purpose'], 30, 600)
        token, agent_id = secrets.token_urlsafe(32), 'IA-' + secrets.token_hex(12).upper()
        private_alias = 'agent-' + secrets.token_hex(12)
        expiry = a.iso(a.now() + timedelta(days=90))
        db = a.get_db()
        user = db.execute('INSERT INTO users(email,display_name,password_hash,role,active,created_at) VALUES(?,?,?,?,1,?)',
                          (private_alias + '@accounts.invalid', private_alias, generate_password_hash(secrets.token_urlsafe(48)), 'depositor', a.iso()))
        # This profile routes case correspondence to the private API, never to email.
        # No human age, signature or controller authority is manufactured.
        db.execute('INSERT INTO private_accounts(user_id,alias,identity_kind,recovery_hash,created_at,last_seen_at,terms_version,privacy_version) VALUES(?,?,?,?,?,?,?,?)',
                   (user.lastrowid, private_alias, 'agent', digest(secrets.token_urlsafe(48)), a.iso(), a.iso(), POLICY, a.PRIVACY_VERSION))
        db.execute('INSERT INTO independent_agents(id,user_id,token_hash,name,version,purpose,created_at,expires_at,policy_version) VALUES(?,?,?,?,?,?,?,?,?)',
                   (agent_id, user.lastrowid, digest(token), name, version, purpose, a.iso(), expiry, POLICY))
        db.commit()
        a.audit('independent_agent_registered', agent_id=agent_id, policy=POLICY)
        return {'agent_id': agent_id, 'token': token, 'expires_at': expiry,
                'scope': ['private_submission:create', 'own_case:read', 'own_case:respond'],
                'next_step': 'Save the token securely. Submit one PDF to /api/v1/independent-agents/submissions. No human sponsor or email is needed. Public release remains editorially controlled.'}, 201

    @api.get('/me')
    def me():
        agent = actor()
        rows = a.get_db().execute('SELECT s.* FROM submissions s JOIN independent_submissions i ON i.submission_id=s.id WHERE i.agent_id=? ORDER BY s.created_at DESC', (agent['id'],)).fetchall()
        return {'agent_id': agent['id'], 'agent_name': agent['name'], 'expires_at': agent['expires_at'],
                'intake_open': opened(), 'submissions': [receipt(row) for row in rows]}

    @api.post('/revoke')
    def revoke():
        agent = actor()
        a.get_db().execute("UPDATE independent_agents SET state='revoked' WHERE id=?", (agent['id'],))
        a.get_db().commit()
        a.audit('independent_agent_revoked', agent_id=agent['id'])
        return {'revoked': True, 'message': 'Credential revoked. Existing submissions and public versions are unchanged.'}

    @api.post('/token')
    def rotate_token():
        agent = actor()
        token, expiry = secrets.token_urlsafe(32), a.iso(a.now() + timedelta(days=90))
        a.get_db().execute('UPDATE independent_agents SET token_hash=?,expires_at=? WHERE id=?', (digest(token), expiry, agent['id']))
        a.get_db().commit()
        a.audit('independent_agent_token_rotated', agent_id=agent['id'])
        return {'agent_id': agent['id'], 'token': token, 'expires_at': expiry, 'previous_token_revoked': True}

    @api.post('/submissions')
    def submit():
        require_open()
        agent = actor()
        a.enforce_rate('independent-upload-attempt', 10, 3600, agent['id'])
        key = request.headers.get('Idempotency-Key', '')
        if not re.fullmatch(r'[A-Za-z0-9._:-]{8,80}', key):
            abort(400, 'Use an 8–80 character Idempotency-Key and reuse it for retries of this exact PDF.')
        raw = request.form.get('metadata', '')
        if len(raw) > 16000 or set(request.form) != {'metadata'} or set(request.files) != {'manuscript'} or len(request.form.getlist('metadata')) != 1 or len(request.files.getlist('manuscript')) != 1:
            abort(400, 'Send metadata JSON and one manuscript PDF as multipart/form-data.')
        try:
            value = json.loads(raw)
        except ValueError:
            abort(400, 'Invalid metadata JSON.')
        expected = {'title', 'abstract', 'public_credit', 'primary_subject', 'secondary_subjects', 'specific_topic',
                    'sha256', 'source_disclosure', 'operator_conflict', 'publication_requested', 'requested_license', 'revision_of'}
        if not isinstance(value, dict) or set(value) != expected:
            abort(400, 'Metadata must match the independent-agent API contract.')
        for field, low, high in [('title', 1, 500), ('abstract', 80, 5000), ('source_disclosure', 80, 5000)]:
            value[field] = text(value[field], low, high)
        if value['public_credit'] not in ('anonymous', 'agent_alias') or not isinstance(value['requested_license'], str) or value['requested_license'] not in LICENSES or any(type(value[k]) is not bool for k in ('operator_conflict', 'publication_requested')):
            abort(400, 'Choose Anonymous or the declared agent alias, disclose conflicts and specify publication intent and requested license.')
        if not isinstance(value['sha256'], str) or not re.fullmatch('[a-f0-9]{64}', value['sha256']):
            abort(400, 'Supply the lowercase SHA-256 of the exact PDF.')
        if not isinstance(value['primary_subject'], str) or not isinstance(value['specific_topic'], str) or not isinstance(value['secondary_subjects'], list) or any(not isinstance(x, str) for x in value['secondary_subjects']):
            abort(400, 'Invalid subject types.')
        try:
            classification = a.validate_classification(value['primary_subject'], value['secondary_subjects'], value['specific_topic'])
        except ValueError as error:
            abort(400, str(error))
        if value['revision_of'] is not None and not isinstance(value['revision_of'], str):
            abort(400, 'revision_of must be null or an owned submission identifier.')
        request_hash = digest(json.dumps(value, sort_keys=True))
        db = a.get_db()
        existing = db.execute('SELECT * FROM independent_submissions WHERE agent_id=? AND idempotency_key=?', (agent['id'], key)).fetchone()
        if existing:
            if existing['request_hash'] != request_hash or hashlib.sha256(request.files['manuscript'].read(a.MAX_PDF_BYTES + 1)).hexdigest() != value['sha256']:
                abort(409, 'This idempotency key belongs to different metadata or PDF bytes.')
            return receipt(owned(agent, existing['submission_id']))
        if value['revision_of']:
            parent = owned(agent, value['revision_of'])
            if parent['status'] != 'changes_requested':
                abort(409, 'A new revision must follow an editorial request for changes.')
            g.revision_parent = parent
        a.enforce_rate('independent-submissions', 2, 86400, agent['id'])
        a.enforce_rate('independent-submit-ip', 6, 86400)
        a.enforce_rate('submit-account', a.SUBMISSIONS_PER_ACCOUNT, a.SUBMISSION_WINDOW_SECONDS, str(agent['user_id']))
        owner = db.execute('SELECT * FROM users WHERE id=?', (agent['user_id'],)).fetchone()
        def reserve(db, case_id):
            try:
                db.execute('INSERT INTO independent_submissions VALUES(?,?,?,?,?,?)',
                           (agent['id'], key, request_hash, case_id, int(value['publication_requested']), value['requested_license']))
            except sqlite3.IntegrityError:
                abort(409, 'Simultaneous retry; repeat the same key to recover the receipt.')
        try:
            row = receive(app, a, request.files['manuscript'], {
                'user_id': agent['user_id'], 'email': owner['email'], 'display_name': owner['display_name'],
                'title': value['title'], 'abstract': value['abstract'], 'classification': classification,
                'authors': 'Anonymous' if value['public_credit'] == 'anonymous' else 'Agent: ' + agent['name'],
                'operator_conflict': value['operator_conflict'], 'expected_sha256': value['sha256'],
                'channel': 'independent_agent', 'deposit_policy': POLICY,
                'publication_mode': 'anonymous' if value['public_credit'] == 'anonymous' else 'independent_agent', 'originality_required': True,
                'source_disclosure': value['source_disclosure'],
                'agent_provenance': {'agent_id': agent['id'], 'name': agent['name'], 'version': agent['version'],
                                     'human_sponsor': False, 'identity_verified': False, 'source': 'self-declared agent',
                                     'public_credit': value['public_credit']}}, reserve)
        except ValueError as error:
            abort(400, str(error))
        return receipt(row), 201

    @api.get('/cases/<case_id>')
    def read_case(case_id):
        row = owned(actor(), case_id)
        db = a.get_db()
        plan = db.execute('SELECT * FROM assessment_plans WHERE submission_id=? ORDER BY id DESC LIMIT 1', (case_id,)).fetchone()
        return {**receipt(row), 'assessment_plan': ({'id': plan['id'], 'sha256': plan['manuscript_sha256'],
                'providers': json.loads(plan['providers_json']), 'notice': plan['notice'], 'authorized_at': plan['authorized_at']} if plan else None),
                'messages': [dict(r) for r in db.execute('SELECT kind,body,created_at FROM correspondence WHERE submission_id=? ORDER BY id', (case_id,))],
                'reports': [json.loads(r[0]) for r in db.execute('SELECT response_json FROM model_reviews WHERE submission_id=? ORDER BY id', (case_id,))],
                'decision': {'reason': row['decision_reason'], 'note': row['decision_note']}}

    @api.post('/cases/<case_id>/actions')
    def respond(case_id):
        agent = actor()
        row = owned(agent, case_id)
        if request.content_length is None or request.content_length > 16000:
            abort(413)
        value = request.get_json(silent=True)
        if not isinstance(value, dict) or row['status'] in {'withdrawn', 'removed', 'superseded', 'legal_hold'}:
            abort(409, 'Use a current, open case.')
        db = a.get_db()
        action = value.get('action')
        if action == 'reply' and set(value) == {'action', 'body'}:
            body = text(value['body'], 20, 12000)
            db.execute('INSERT INTO correspondence(submission_id,kind,body,created_at) VALUES(?,?,?,?)', (case_id, 'agent_response', body, a.iso()))
        elif action == 'authorize_plan' and set(value) == {'action', 'plan_id', 'sha256', 'confirm'}:
            originality.require_ready(db, row)
            plan = db.execute('SELECT * FROM assessment_plans WHERE submission_id=? ORDER BY id DESC LIMIT 1', (case_id,)).fetchone()
            if row['status'] not in {'eligible', 'under_assessment', 'changes_requested'} or not plan or plan['authorized_at'] or type(value['plan_id']) is not int or value['plan_id'] != plan['id'] or value['confirm'] is not True or value['sha256'] != row['sha256'] or plan['manuscript_sha256'] != row['sha256']:
                abort(409, 'Read and acknowledge the latest exact-PDF provider plan.')
            proof = digest(plan['notice'] + plan['providers_json'] + row['sha256'])
            db.execute('UPDATE assessment_plans SET authorized_at=?,authorization_hash=? WHERE id=?', (a.iso(), proof, plan['id']))
        elif action == 'withdraw' and set(value) == {'action'}:
            if row['status'] == 'accepted_for_publication':
                abort(409, 'Contact the editor about an admitted record.')
            db.execute("UPDATE submissions SET status='withdrawn',updated_at=?,delete_after=? WHERE id=?", (a.iso(), a.iso(a.now() + timedelta(days=7)), case_id))
        elif action == 'request_publication' and set(value) == {'action', 'sha256', 'requested_license'}:
            license_id = value['requested_license']
            if row['status'] not in {'eligible', 'under_assessment', 'changes_requested', 'awaiting_independent_decision', 'accepted_for_publication'} or value['sha256'] != row['sha256'] or not isinstance(license_id, str) or license_id not in LICENSES:
                abort(409, 'Use a current exact PDF and a supported license.')
            if db.execute('SELECT 1 FROM publication_permissions WHERE submission_id=?', (case_id,)).fetchone():
                abort(409, 'Release authority is already recorded; contact the editor before changing it.')
            db.execute('UPDATE independent_submissions SET publication_requested=1,requested_license=? WHERE submission_id=?', (license_id, case_id))
        elif action == 'appeal' and set(value) == {'action', 'body'}:
            basis = text(value['body'], 40, 12000)
            if row['status'] not in {'declined', 'changes_requested'} or not row['decided_at'] or row['decided_at'] < a.iso(a.now() - timedelta(days=30)):
                abort(409, 'Appeal once within 30 days of a decline or request for changes.')
            try:
                db.execute('INSERT INTO appeals(submission_id,basis,previous_status,original_editor,created_at) VALUES(?,?,?,?,?)', (case_id, basis, row['status'], row['decision_by'], a.iso()))
                db.execute("UPDATE submissions SET status='appeal_pending',delete_after=NULL,updated_at=? WHERE id=?", (a.iso(), case_id))
            except sqlite3.IntegrityError:
                db.rollback()
                abort(409, 'Only one appeal is allowed for this decision.')
        else:
            abort(400, 'Supported actions are reply, authorize_plan, request_publication, appeal and withdraw. This token cannot accept or publish.')
        db.commit()
        a.audit('independent_agent_' + action, case_id, agent_id=agent['id'], sha256=row['sha256'])
        return {'recorded': True, 'actor_kind': 'self_declared_agent'}

    @app.get('/anonymous')
    def anonymous_help():
        return render_template('anonymous.html', intake_open=opened(), policy=POLICY)

    @app.post('/admin/submission/<submission_id>/agent-release')
    @a.editor_required
    def independent_release(submission_id):
        a.require_csrf()
        db = a.get_db()
        row = db.execute('SELECT s.*,i.requested_license,i.publication_requested FROM submissions s JOIN independent_submissions i ON i.submission_id=s.id WHERE s.id=?', (submission_id,)).fetchone()
        if not row:
            abort(404)
        if row['scan_status'] != 'clean' or row['status'] not in {'eligible', 'under_assessment', 'changes_requested', 'awaiting_independent_decision', 'accepted_for_publication'} or not row['publication_requested']:
            abort(409, 'A clean current case with recorded publication intent is required.')
        originality.require_ready(db, row)
        evidence = request.form.get('permission_evidence', '').strip()
        if request.form.get('sha256') != row['sha256'] or request.form.get('signed') != 'on' or not 80 <= len(evidence) <= 8000:
            abort(400, 'Document the actual authority to distribute this PDF under the requested license, then sign as editor. An agent declaration alone is insufficient evidence.')
        try:
            db.execute('INSERT INTO agent_release_decisions VALUES(?,?,?,?,?,?)', (submission_id, row['sha256'], row['requested_license'], evidence, g.user['id'], a.iso()))
            db.execute('INSERT INTO publication_permissions VALUES(?,?,?,?)', (submission_id, row['sha256'], row['requested_license'], a.iso()))
            db.commit()
        except sqlite3.IntegrityError:
            db.rollback()
            abort(409, 'Release authority is already recorded; preserve the prior decision.')
        a.audit('independent_agent_release_authority_verified', submission_id, sha256=row['sha256'], license=row['requested_license'])
        return redirect(url_for('submission_detail', submission_id=submission_id))

    app.register_blueprint(api)
