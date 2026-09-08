"""Private pseudonymous workspaces; no depositor contact address is collected."""
import hashlib
import re
import secrets
import sqlite3
from functools import wraps

from flask import abort, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

SCHEMA = '''
CREATE TABLE IF NOT EXISTS private_accounts (
 user_id INTEGER PRIMARY KEY REFERENCES users(id), alias TEXT NOT NULL UNIQUE COLLATE NOCASE,
 identity_kind TEXT NOT NULL CHECK(identity_kind IN ('human','agent')),
 recovery_hash TEXT NOT NULL, credential_version INTEGER NOT NULL DEFAULT 1,
 created_at TEXT NOT NULL, last_seen_at TEXT NOT NULL,
 terms_version TEXT NOT NULL, privacy_version TEXT NOT NULL
);
'''
DUMMY_HASH = generate_password_hash(secrets.token_urlsafe(32))


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def migrate(db):
    db.executescript(SCHEMA)
    columns = {r[1] for r in db.execute('PRAGMA table_info(agent_grants)')}
    if 'owner_user_id' not in columns:
        db.execute('ALTER TABLE agent_grants ADD COLUMN owner_user_id INTEGER REFERENCES users(id)')
    db.commit()


def profile(a, user_id):
    return a.get_db().execute('SELECT * FROM private_accounts WHERE user_id=?', (user_id,)).fetchone()


def install(app, a):
    def require_account(view):
        @wraps(view)
        def wrapped(*args, **kwargs):
            if not g.user or g.user['role'] != 'depositor' or not profile(a, g.user['id']):
                if request.method == 'POST':
                    abort(401, 'Sign in to your private workspace first.')
                return redirect(url_for('account_login'))
            return view(*args, **kwargs)
        return wrapped

    def opened():
        return bool(app.config['INTAKE_OPEN'] and (app.config['TESTING'] or
                    app.extensions['editorial']['launch_approved']()))

    def credentials():
        alias = request.form.get('alias', '').strip().lower()
        password = request.form.get('password', '')
        if not re.fullmatch(r'[a-z0-9][a-z0-9_-]{2,39}', alias):
            abort(400, 'Use an alias of 3–40 letters, numbers, hyphens or underscores. Do not use an email address.')
        if not 14 <= len(password) <= 256 or password != request.form.get('confirm_password'):
            abort(400, 'Use matching passwords of 14–256 characters.')
        return alias, password

    def signed_in(user_id, version):
        destination = session.get('workspace_return', '')
        session.clear()
        if re.fullmatch(r'/agents/authorize/[A-Za-z0-9_-]{43}', destination):
            session['workspace_return'] = destination
        session['user_id'] = user_id
        session['credential_version'] = version
        session.permanent = True
        g.user = a.get_db().execute('SELECT * FROM users WHERE id=?', (user_id,)).fetchone()

    @app.route('/account/register', methods=['GET', 'POST'])
    def account_register():
        if not opened():
            return render_template('closed.html'), 503
        if request.method == 'POST':
            a.require_csrf()
            a.enforce_rate('alias-register-ip', 3, 86400)
            a.enforce_rate('alias-register-global', 100, 86400, 'all')
            if request.form.get('website') or any(k in request.form for k in ('email', 'display_name')):
                abort(400, 'Do not supply personal contact details.')
            alias, password = credentials()
            kind = request.form.get('identity_kind')
            if kind not in ('human', 'agent') or not all(request.form.get(k) == 'on' for k in ('adult', 'authority', 'terms', 'privacy')):
                abort(400, 'Confirm the workspace type, responsible adult control and terms.')
            db = a.get_db()
            recovery = secrets.token_urlsafe(32)
            try:
                # Legacy users.email is NOT NULL. This random, non-deliverable
                # internal key is never requested from a user or sent as mail.
                user = db.execute('INSERT INTO users(email,display_name,password_hash,role,active,created_at) VALUES(?,?,?,?,1,?)',
                    ('workspace-' + secrets.token_hex(16) + '@accounts.invalid', alias,
                     generate_password_hash(password), 'depositor', a.iso()))
                db.execute('INSERT INTO private_accounts(user_id,alias,identity_kind,recovery_hash,created_at,last_seen_at,terms_version,privacy_version) VALUES(?,?,?,?,?,?,?,?)',
                    (user.lastrowid, alias, kind, digest(recovery), a.iso(), a.iso(), a.TERMS_VERSION, a.PRIVACY_VERSION))
                db.commit()
            except sqlite3.IntegrityError:
                db.rollback()
                flash('Choose a different alias.', 'error')
                return render_template('account.html', mode='register'), 409
            signed_in(user.lastrowid, 1)
            a.audit('private_workspace_created', identity_kind=kind)
            return render_template('account-recovery.html', alias=alias, recovery=recovery)
        return render_template('account.html', mode='register')

    @app.route('/account/login', methods=['GET', 'POST'])
    def account_login():
        if request.method == 'POST':
            a.require_csrf()
            a.enforce_rate('alias-login-ip', 8, 900)
            alias = request.form.get('alias', '').strip().lower()[:40]
            a.enforce_rate('alias-login-account', 20, 900, alias)
            row = a.get_db().execute('SELECT p.*,u.password_hash FROM private_accounts p JOIN users u ON u.id=p.user_id WHERE p.alias=? AND u.active=1 AND u.role=\'depositor\'', (alias,)).fetchone()
            password = request.form.get('password', '')
            valid = check_password_hash(row['password_hash'] if row else DUMMY_HASH, password[:256])
            if not row or len(password) > 256 or not valid:
                flash('Invalid alias or password.', 'error')
                return render_template('account.html', mode='login'), 401
            signed_in(row['user_id'], row['credential_version'])
            return redirect(session.pop('workspace_return', url_for('dashboard')))
        return render_template('account.html', mode='login')

    @app.route('/account/recover', methods=['GET', 'POST'])
    def account_recover():
        if request.method == 'POST':
            a.require_csrf()
            a.enforce_rate('alias-recover-ip', 5, 3600)
            alias, password = credentials()
            a.enforce_rate('alias-recover-account', 8, 3600, alias)
            code = request.form.get('recovery_code', '').strip()
            db = a.get_db()
            row = db.execute('SELECT p.* FROM private_accounts p JOIN users u ON u.id=p.user_id WHERE p.alias=? AND u.active=1', (alias,)).fetchone()
            if not row or not re.fullmatch(r'[A-Za-z0-9_-]{43}', code) or not secrets.compare_digest(row['recovery_hash'], digest(code)):
                abort(400, 'Invalid alias or recovery code.')
            replacement = secrets.token_urlsafe(32)
            changed = db.execute('UPDATE private_accounts SET recovery_hash=?,credential_version=credential_version+1 WHERE user_id=? AND recovery_hash=?',
                (digest(replacement), row['user_id'], digest(code))).rowcount
            if changed != 1:
                db.rollback()
                abort(409, 'This recovery code has already been used.')
            db.execute('UPDATE users SET password_hash=? WHERE id=?', (generate_password_hash(password), row['user_id']))
            db.execute("UPDATE agent_grants SET state='revoked' WHERE owner_user_id=?", (row['user_id'],))
            db.commit()
            signed_in(row['user_id'], row['credential_version'] + 1)
            a.audit('private_workspace_recovered')
            return render_template('account-recovery.html', alias=alias, recovery=replacement)
        return render_template('account.html', mode='recover')

    @app.get('/account')
    @require_account
    def account_settings():
        return render_template('account-settings.html', account=profile(a, g.user['id']),
            grants=a.get_db().execute('SELECT id,agent_name,state,expires_at FROM agent_grants WHERE owner_user_id=? ORDER BY created_at DESC', (g.user['id'],)).fetchall())

    @app.post('/account/password')
    @require_account
    def account_password():
        a.require_csrf()
        a.enforce_rate('alias-change-password', 5, 3600, str(g.user['id']))
        current = request.form.get('current_password', '')
        password = request.form.get('password', '')
        if len(current) > 256 or not check_password_hash(g.user['password_hash'], current):
            abort(400, 'Current password is incorrect.')
        if not 14 <= len(password) <= 256 or password != request.form.get('confirm_password'):
            abort(400, 'Use matching new passwords of 14–256 characters.')
        db = a.get_db()
        account = profile(a, g.user['id'])
        recovery = secrets.token_urlsafe(32)
        if db.execute('UPDATE users SET password_hash=? WHERE id=? AND password_hash=?',
            (generate_password_hash(password), g.user['id'], g.user['password_hash'])).rowcount != 1:
            db.rollback()
            abort(409, 'Credentials changed. Sign in again.')
        db.execute('UPDATE private_accounts SET recovery_hash=?,credential_version=credential_version+1 WHERE user_id=?', (digest(recovery), g.user['id']))
        db.execute("UPDATE agent_grants SET state='revoked' WHERE owner_user_id=?", (g.user['id'],))
        db.commit()
        signed_in(g.user['id'], account['credential_version'] + 1)
        a.audit('private_workspace_password_changed')
        return render_template('account-recovery.html', alias=account['alias'], recovery=recovery)

    @app.post('/account/grants/<grant_id>/revoke')
    @require_account
    def account_revoke_grant(grant_id):
        a.require_csrf()
        db = a.get_db()
        if db.execute("UPDATE agent_grants SET state='revoked' WHERE id=? AND owner_user_id=?", (grant_id, g.user['id'])).rowcount != 1:
            abort(404)
        db.commit()
        a.audit('agent_delegation_revoked', grant_id=grant_id)
        return redirect(url_for('account_settings'))

    @app.context_processor
    def account_context():
        return {'private_account': profile(a, g.user['id']) if g.user and g.user['role'] == 'depositor' else None,
                'is_web_account': lambda user_id: bool(profile(a, user_id))}

    app.extensions['accounts'] = {'require_account': require_account, 'profile': lambda user_id: profile(a, user_id)}
