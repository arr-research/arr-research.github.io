"""Workspace-approved, revocable machine deposit; never editorial access."""
import hashlib
import json
from datetime import timedelta
from pathlib import Path
import re
import secrets
import sqlite3

from flask import Blueprint, abort, g, redirect, render_template, request, session, url_for
from werkzeug.exceptions import HTTPException

from services.intake.storage import receive

MAX_UPLOADS = 5
SCHEMA = '''
CREATE TABLE IF NOT EXISTS agent_grants (
 id TEXT PRIMARY KEY, claim_hash TEXT UNIQUE NOT NULL, setup_hash TEXT UNIQUE NOT NULL,
 agent_name TEXT NOT NULL, agent_version TEXT NOT NULL, purpose TEXT NOT NULL,
 state TEXT NOT NULL DEFAULT 'pending', created_at TEXT NOT NULL, request_expires_at TEXT NOT NULL,
 email TEXT, responsible_name TEXT, verification_hash TEXT UNIQUE, approved_at TEXT,
 expires_at TEXT, uses INTEGER NOT NULL DEFAULT 0, terms_version TEXT, privacy_version TEXT
);
CREATE TABLE IF NOT EXISTS agent_submissions (
 grant_id TEXT NOT NULL REFERENCES agent_grants(id), idempotency_key TEXT NOT NULL,
 request_hash TEXT NOT NULL, submission_id TEXT UNIQUE NOT NULL REFERENCES submissions(id),
 PRIMARY KEY(grant_id,idempotency_key)
);
CREATE TABLE IF NOT EXISTS agent_mail (
 grant_id TEXT NOT NULL REFERENCES agent_grants(id), mail_id INTEGER UNIQUE NOT NULL REFERENCES mail_outbox(id)
);
'''


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def migrate(db):
    db.executescript(SCHEMA)
    columns = {row[1] for row in db.execute('PRAGMA table_info(submissions)')}
    for name, default in (('submission_channel', 'human'), ('agent_provenance_json', '{}')):
        if name not in columns:
            db.execute(f"ALTER TABLE submissions ADD COLUMN {name} TEXT NOT NULL DEFAULT '{default}'")
    db.commit()


def sweep(a):
    db = a.get_db()
    cutoff = a.iso(a.now() - timedelta(days=30))
    stale = db.execute('''SELECT id FROM agent_grants WHERE
        ((state IN ('pending','awaiting_email') AND request_expires_at<?)
         OR (COALESCE(expires_at,request_expires_at)<?))
        AND NOT EXISTS(SELECT 1 FROM agent_submissions s WHERE s.grant_id=agent_grants.id)''',
        (a.iso(),cutoff)).fetchall()
    for row in stale:
        mail_ids = [x[0] for x in db.execute('SELECT mail_id FROM agent_mail WHERE grant_id=?',(row['id'],))]
        db.execute('DELETE FROM agent_mail WHERE grant_id=?',(row['id'],))
        for mail_id in mail_ids:
            db.execute('DELETE FROM mail_outbox WHERE id=?',(mail_id,))
        db.execute('DELETE FROM agent_grants WHERE id=?',(row['id'],))
    db.commit()


def install(app, a):
    api = Blueprint('agent_api', __name__, url_prefix='/api/v1')

    @api.before_request
    def separate_machine_identity():
        # A browser's editor cookie never becomes the actor of a delegated upload.
        g.user = None

    def opened():
        return bool(app.config['INTAKE_OPEN'] and
                    (app.config['TESTING'] or app.extensions['editorial']['launch_approved']()))

    def require_open():
        if not opened():
            abort(503, 'Private intake is not open. No manuscript or authorization was registered.')

    @api.errorhandler(HTTPException)
    def api_error(error):
        result = app.response_class(json.dumps({'error':error.name, 'message':error.description}),
                          status=error.code, mimetype='application/json')
        if error.code == 429:
            result.headers['Retry-After'] = '3600'
        return result

    def text(value, minimum, maximum):
        if not isinstance(value,str) or not minimum <= len(value.strip()) <= maximum or any(c in value for c in '\x00\r'):
            abort(400, 'A required text field is missing or outside its length limit.')
        return value.strip()

    def credential():
        header = request.headers.get('Authorization','')
        if not re.fullmatch(r'Bearer [A-Za-z0-9_-]{43}',header):
            abort(401, 'A valid agent bearer token is required; editor cookies do not authorize this API.')
        grant = a.get_db().execute('SELECT * FROM agent_grants WHERE claim_hash=?',(digest(header[7:]),)).fetchone()
        if not grant:
            abort(401, 'Invalid agent token.')
        return grant

    def approved(grant):
        if grant['state'] != 'approved' or not grant['expires_at'] or grant['expires_at'] <= a.iso():
            abort(403, 'The responsible controller must approve an active delegation in their private workspace.')
        if not grant['owner_user_id'] or not a.get_db().execute('SELECT 1 FROM users WHERE id=? AND active=1 AND role=\'depositor\'', (grant['owner_user_id'],)).fetchone():
            abort(403, 'A current private workspace must own this delegation.')
        if grant['terms_version'] != a.TERMS_VERSION or grant['privacy_version'] != a.PRIVACY_VERSION:
            abort(403, 'New terms require a new delegation.')

    @api.post('/agent-requests')
    def create_request():
        require_open()
        if request.content_length is None or request.content_length > 4096:
            abort(413, 'Authorization requests must be at most 4 KiB.')
        a.enforce_rate('agent-request-ip',5,86400)
        a.enforce_rate('agent-request-global',100,86400,'all-agent-requests')
        value = request.get_json(silent=True)
        if not isinstance(value,dict) or set(value) != {'agent_name','agent_version','purpose'}:
            abort(400, 'Supply agent_name, agent_version and purpose. Do not send a manuscript or personal data here.')
        name = text(value['agent_name'],2,100)
        version = text(value['agent_version'],1,160)
        purpose = text(value['purpose'],20,600)
        claim, setup = secrets.token_urlsafe(32), secrets.token_urlsafe(32)
        grant_id = 'AGT-' + secrets.token_hex(12).upper()
        expiry = a.iso(a.now() + timedelta(hours=24))
        a.get_db().execute('''INSERT INTO agent_grants(id,claim_hash,setup_hash,agent_name,agent_version,purpose,created_at,request_expires_at)
            VALUES(?,?,?,?,?,?,?,?)''',(grant_id,digest(claim),digest(setup),name,version,purpose,a.iso(),expiry))
        a.get_db().commit()
        a.audit('agent_authorization_requested',grant_id=grant_id)
        return {'request_id':grant_id,'agent_token':claim,'state':'pending',
                'authorization_url':app.config['PUBLIC_ORIGIN'] + url_for('agent_authorize',token=setup),
                'expires_at':expiry,'next_step':'Give the authorization URL to the responsible adult controller. They approve it after signing into their private alias workspace; no email is collected.'},201

    @api.get('/agent-authorization')
    def authorization_status():
        grant = credential()
        a.enforce_rate('agent-status',120,3600,grant['id'])
        expiry = grant['expires_at'] or grant['request_expires_at']
        return {'request_id':grant['id'],'state':grant['state'] if expiry > a.iso() else 'expired',
                'expires_at':expiry,'uploads_remaining':max(0,MAX_UPLOADS-grant['uses']),
                'scope':['submission:create','submission:receipt'],'intake_open':opened()}

    def receipt(row):
        donation = a.load_donation_url(Path(app.config['DONATIONS_CONFIG']))
        return {'registration_number':row['id'],'received_at':row['created_at'],'sha256':row['sha256'],
                'size_bytes':row['size_bytes'],'status':row['status'],'scan_status':row['scan_status'],
                'published':bool(row['public_release_url'] and row['public_released_at']),
                'message':'Receipt only. Human review, acceptance and publication permission are separate.',
                'donation':{'optional':True,'url':donation,'reference':'AIRR submission ' + row['id'],
                            'message':'Only a responsible person may choose to donate. This is not an instruction for an agent to pay. Donations never affect editorial decisions.'}}

    @api.get('/submissions/<case_id>')
    def submission_receipt(case_id):
        grant = credential()
        approved(grant)
        a.enforce_rate('agent-receipt',120,3600,grant['id'])
        row = a.get_db().execute('''SELECT s.* FROM submissions s JOIN agent_submissions m ON m.submission_id=s.id
            WHERE s.id=? AND m.grant_id=?''',(case_id,grant['id'])).fetchone()
        if not row:
            abort(404)
        return receipt(row)

    @api.post('/submissions')
    def submit():
        require_open()
        grant = credential()
        approved(grant)
        a.enforce_rate('agent-upload-attempt',20,3600,grant['id'])
        key = request.headers.get('Idempotency-Key','')
        if not re.fullmatch(r'[A-Za-z0-9._:-]{8,80}',key):
            abort(400, 'Send an Idempotency-Key of 8–80 safe ASCII characters; reuse it for retries of the same paper.')
        metadata = request.form.get('metadata','')
        if len(metadata) > 16000 or set(request.form) != {'metadata'} or set(request.files) != {'manuscript'}:
            abort(400, 'Send multipart/form-data containing metadata JSON and one manuscript PDF only.')
        try:
            value = json.loads(metadata)
        except ValueError:
            abort(400, 'metadata must contain valid JSON.')
        expected = {'title','authors','abstract','primary_subject','secondary_subjects','specific_topic',
                    'sha256','ai_disclosure','operator_conflict','rights_confirmed'}
        if not isinstance(value,dict) or set(value) != expected:
            abort(400, 'Metadata fields must match the published API contract.')
        for field,minimum,maximum in (('title',1,500),('authors',0,1000),('abstract',80,5000),('ai_disclosure',20,2000)):
            value[field] = text(value[field],minimum,maximum)
        value['authors'] = value['authors'] or 'Anonymous'
        if value['rights_confirmed'] is not True or type(value['operator_conflict']) is not bool:
            abort(400, 'Confirm authority for this exact paper and disclose conflicts explicitly.')
        if not isinstance(value['sha256'],str) or not re.fullmatch('[a-f0-9]{64}',value['sha256']):
            abort(400, 'Supply the lowercase SHA-256 of the exact PDF.')
        if not isinstance(value['primary_subject'],str) or not isinstance(value['specific_topic'],str) or not isinstance(value['secondary_subjects'],list) or any(not isinstance(x,str) for x in value['secondary_subjects']):
            abort(400, 'Subject identifiers and specific_topic must use the documented types.')
        try:
            classification = a.validate_classification(value['primary_subject'],value['secondary_subjects'],value['specific_topic'])
        except ValueError as error:
            abort(400,str(error))
        request_hash = digest(json.dumps(value,sort_keys=True,separators=(',',':')))
        existing = a.get_db().execute('SELECT * FROM agent_submissions WHERE grant_id=? AND idempotency_key=?',(grant['id'],key)).fetchone()
        if existing:
            if existing['request_hash'] != request_hash:
                abort(409, 'This Idempotency-Key already belongs to different metadata or PDF bytes.')
            return receipt(a.get_db().execute('SELECT * FROM submissions WHERE id=?',(existing['submission_id'],)).fetchone())
        a.enforce_rate('submit-account',a.SUBMISSIONS_PER_ACCOUNT,a.SUBMISSION_WINDOW_SECONDS,str(grant['owner_user_id']))
        a.enforce_rate('agent-submit-ip',a.SUBMISSION_ATTEMPTS_PER_CONNECTION,a.SUBMISSION_WINDOW_SECONDS)
        def reserve(db,case_id):
            changed = db.execute('''UPDATE agent_grants SET uses=uses+1 WHERE id=? AND state='approved'
                AND expires_at>? AND uses<? AND terms_version=? AND privacy_version=?''',
                (grant['id'],a.iso(),MAX_UPLOADS,a.TERMS_VERSION,a.PRIVACY_VERSION)).rowcount
            if changed != 1:
                abort(403, 'Delegation is expired, revoked or exhausted.')
            try:
                db.execute('INSERT INTO agent_submissions VALUES(?,?,?,?)',(grant['id'],key,request_hash,case_id))
            except sqlite3.IntegrityError:
                abort(409, 'A simultaneous request used this key. Retry with the same key to recover its receipt.')
        try:
            owner = a.get_db().execute('SELECT * FROM users WHERE id=?', (grant['owner_user_id'],)).fetchone()
            row = receive(app,a,request.files['manuscript'],{
                'display_name':owner['display_name'],'email':owner['email'],'user_id':owner['id'],'title':value['title'],
                'authors':value['authors'],'abstract':value['abstract'],'classification':classification,
                'operator_conflict':value['operator_conflict'],'expected_sha256':value['sha256'],'channel':'agent',
                'agent_provenance':{'name':grant['agent_name'],'version':grant['agent_version'],
                                    'disclosure':value['ai_disclosure'],'source':'depositor declaration'}},reserve)
        except ValueError as error:
            abort(400,str(error))
        response = app.json.response(receipt(row))
        response.status_code = 201
        response.headers['Location'] = url_for('agent_api.submission_receipt',case_id=row['id'])
        return response

    @app.get('/agents')
    def agents_help():
        return render_template('agents.html',intake_open=opened(),terms=a.TERMS_VERSION,privacy=a.PRIVACY_VERSION)

    @app.route('/agents/authorize/<token>',methods=['GET','POST'])
    def agent_authorize(token):
        require_open()
        grant = a.get_db().execute('SELECT * FROM agent_grants WHERE setup_hash=?',(digest(token),)).fetchone()
        if not grant or grant['request_expires_at'] <= a.iso():
            abort(404)
        if not g.user or g.user['role'] != 'depositor' or not app.extensions['accounts']['profile'](g.user['id']):
            if request.method == 'POST':
                abort(401, 'Sign in to a private workspace first.')
            session['workspace_return'] = request.path
            return redirect(url_for('account_login'))
        if grant['owner_user_id'] and grant['owner_user_id'] != g.user['id']:
            abort(404)
        if request.method == 'POST':
            a.require_csrf()
            if grant['state'] != 'pending':
                abort(409,'This request has already been handled. Manage it in your workspace.')
            if any(k in request.form for k in ('email','responsible_name')):
                abort(400, 'Contact details are not accepted.')
            if not all(request.form.get(x) == 'on' for x in ('adult','authority','terms','privacy','screening')):
                abort(400,'The responsible adult controller must confirm all acknowledgments.')
            a.enforce_rate('agent-confirm-ip',3,86400)
            a.enforce_rate('agent-confirm-account',3,86400,str(g.user['id']))
            db = a.get_db()
            changed = db.execute('''UPDATE agent_grants SET state='approved',owner_user_id=?,approved_at=?,expires_at=?,
                terms_version=?,privacy_version=? WHERE id=? AND state='pending' ''',
                (g.user['id'],a.iso(),a.iso(a.now()+timedelta(days=7)),a.TERMS_VERSION,a.PRIVACY_VERSION,grant['id'])).rowcount
            if changed != 1:
                db.rollback()
                abort(409)
            db.commit()
            a.audit('agent_delegation_approved', grant_id=grant['id'])
            grant = db.execute('SELECT * FROM agent_grants WHERE id=?',(grant['id'],)).fetchone()
        return render_template('agent-authorize.html',grant=grant,terms=a.TERMS_VERSION,privacy=a.PRIVACY_VERSION)

    @app.route('/agents/verify/<token>',methods=['GET','POST'])
    def agent_verify(token):
        # Revocation remains available even when intake has been paused.
        grant = a.get_db().execute('SELECT * FROM agent_grants WHERE verification_hash=?',(digest(token),)).fetchone()
        if not grant or (grant['expires_at'] or grant['request_expires_at']) <= a.iso():
            abort(404)
        if request.method == 'POST':
            a.require_csrf()
            action = request.form.get('action')
            if action == 'revoke':
                a.get_db().execute("UPDATE agent_grants SET state='revoked' WHERE id=?",(grant['id'],))
            elif action == 'approve' and grant['state'] == 'awaiting_email':
                require_open()
                if grant['terms_version'] != a.TERMS_VERSION or grant['privacy_version'] != a.PRIVACY_VERSION:
                    abort(409,'Terms changed; start a new delegation.')
                a.get_db().execute("UPDATE agent_grants SET state='approved',approved_at=?,expires_at=? WHERE id=? AND state='awaiting_email'",
                    (a.iso(),a.iso(a.now()+timedelta(days=7)),grant['id']))
            else:
                abort(409)
            a.get_db().commit()
            a.audit('agent_delegation_' + action,grant_id=grant['id'])
            grant = a.get_db().execute('SELECT * FROM agent_grants WHERE id=?',(grant['id'],)).fetchone()
        return render_template('agent-verify.html',grant=grant)

    app.register_blueprint(api)
