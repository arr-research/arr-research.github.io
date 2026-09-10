"""Explicit host-authorized, single-artifact historical revision delegation.

No private parent case is created. The public catalogue is an operator-installed
snapshot, never an agent-supplied URL. Disabled unless configured explicitly.
"""
import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path
import re
import secrets
import uuid

import click
from flask import abort, g


def migrate(db):
    db.executescript('''
      CREATE TABLE IF NOT EXISTS historical_revision_grants (
        grant_id TEXT PRIMARY KEY REFERENCES agent_grants(id) ON DELETE CASCADE,
        binding_json TEXT NOT NULL, catalogue_sha256 TEXT NOT NULL,
        authorization_json TEXT NOT NULL, authorization_sha256 TEXT NOT NULL,
        authorized_by INTEGER NOT NULL REFERENCES users(id)
      );
      CREATE TABLE IF NOT EXISTS historical_revisions (
        submission_id TEXT PRIMARY KEY REFERENCES submissions(id),
        grant_id TEXT UNIQUE NOT NULL REFERENCES historical_revision_grants(grant_id),
        version_id TEXT UNIQUE NOT NULL, binding_json TEXT NOT NULL
      );
    ''')


def binding_for(db, grant_id):
    return db.execute('SELECT * FROM historical_revision_grants WHERE grant_id=?', (grant_id,)).fetchone()


def catalogue(app):
    if not app.config.get('HISTORICAL_REVISIONS_ENABLED'):
        raise ValueError('Historical revisions are disabled.')
    raw = Path(app.config['HISTORICAL_REVISION_CATALOGUE']).read_bytes()
    if len(raw) > 2_000_000:
        raise ValueError('Catalogue exceeds size limit.')
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def validate_binding(value, entries, author):
    required = {'paper_id','record_id','supersedes_version_id','parent_sha256',
                'version','version_id','sha256','changelog'}
    if not isinstance(value, dict) or set(value) != required:
        raise ValueError('Revision binding fields do not match the contract.')
    parent = entries.get(value['paper_id'])
    if not author or not parent or parent.get('authors') != [author]:
        raise ValueError('Catalogue must identify this as the configured operator sole-authored paper.')
    for new, old in [('record_id','record_id'),('supersedes_version_id','version_id'),('parent_sha256','canonical_sha256')]:
        if value[new] != parent[old]:
            raise ValueError('Public predecessor identity/hash mismatch.')
    if not re.fullmatch(r'v[1-9][0-9]*',parent['version']) or value['version'] != f"v{int(parent['version'][1:])+1}":
        raise ValueError('Revision must be the next public version.')
    if not isinstance(value['version_id'],str) or not value['version_id'].startswith('arr:version:'):
        raise ValueError('Invalid version ID.')
    uuid.UUID(value['version_id'].removeprefix('arr:version:'))
    if value['version_id'] == parent['version_id']:
        raise ValueError('A revision needs a new version ID.')
    if not re.fullmatch('[a-f0-9]{64}',value['sha256']) or value['sha256']==value['parent_sha256']:
        raise ValueError('A new exact PDF hash is required.')
    if not isinstance(value['changelog'],dict) or set(value['changelog']) != {'mathematics','scope','reproducibility','version','editorial'}:
        raise ValueError('Provide the five changelog categories.')
    if any(not isinstance(x,str) or not 5 <= len(x.strip()) <= 2000 for x in value['changelog'].values()):
        raise ValueError('Every changelog category needs a bounded explicit statement.')


def check_current(app, row):
    try:
        entries, digest = catalogue(app)
        value = json.loads(row['binding_json'])
        validate_binding(value, entries, app.config.get('HISTORICAL_OPERATOR_AUTHOR',''))
        if digest != row['catalogue_sha256']:
            raise ValueError('Catalogue changed; new authorization required.')
        return value
    except (ValueError, OSError, KeyError, TypeError):
        abort(409, 'Historical predecessor is unavailable or changed; no revision received.')


def install(app, a, require_open):
    @app.context_processor
    def revision_context():
        def historical_revision(submission_id):
            row=a.get_db().execute('SELECT binding_json FROM historical_revisions WHERE submission_id=?',(submission_id,)).fetchone()
            return json.loads(row['binding_json']) if row else None
        return {'historical_revision':historical_revision}

    @app.cli.command('authorize-historical-revision')
    @click.argument('evidence_file', type=click.Path(exists=True,dir_okay=False))
    def authorize(evidence_file):
        """Authenticated-host operation; output contains a one-time bearer secret."""
        require_open()
        raw = Path(evidence_file).read_bytes()
        if len(raw)>20000:
            raise click.ClickException('Evidence too large.')
        try:
            evidence=json.loads(raw)
            if set(evidence)!={'owner_user_id','agent_name','agent_version','binding','author_instruction','source_reference','recorded_at','scope','terms_version','privacy_version','operator_authorship_confirmed'}:
                raise ValueError('Evidence fields do not match the contract.')
            if evidence['scope']!=['revision:create','submission:receipt'] or evidence['operator_authorship_confirmed'] is not True:
                raise ValueError('Explicit limited scope and operator authorship attestation required.')
            for key, minimum in [('author_instruction',40),('source_reference',10),('agent_name',2),('agent_version',2)]:
                if not isinstance(evidence[key],str) or not minimum<=len(evidence[key])<=2000:
                    raise ValueError('Missing actual instruction/source or agent identity.')
            stamp=datetime.fromisoformat(evidence['recorded_at'])
            if stamp.tzinfo is None or stamp>a.now() or stamp<a.now()-timedelta(days=7):
                raise ValueError('Authorization evidence must be recent and offset-aware.')
            if evidence['terms_version']!=a.TERMS_VERSION or evidence['privacy_version']!=a.PRIVACY_VERSION:
                raise ValueError('Current deposit terms/privacy acknowledgment required.')
            entries, catalog_hash=catalogue(app)
            validate_binding(evidence['binding'],entries,app.config.get('HISTORICAL_OPERATOR_AUTHOR',''))
        except (ValueError,KeyError,TypeError,OSError) as error:
            raise click.ClickException(str(error)) from error
        db=a.get_db()
        actor=db.execute("SELECT * FROM users WHERE email=? AND role='operator' AND active=1 AND totp_secret IS NOT NULL",(app.config['OPERATOR_EMAIL'],)).fetchone()
        owner=db.execute("SELECT u.* FROM users u JOIN private_accounts p ON p.user_id=u.id WHERE u.id=? AND u.role='depositor' AND u.active=1",(evidence['owner_user_id'],)).fetchone()
        if not actor or not owner:
            raise click.ClickException('Active configured MFA operator and real private workspace required.')
        claim,setup=secrets.token_urlsafe(32),secrets.token_urlsafe(32)
        grant_id='AGT-'+secrets.token_hex(12).upper()
        expiry=a.iso(a.now()+timedelta(hours=24))
        binding=json.dumps(evidence['binding'],sort_keys=True)
        db.execute('INSERT INTO agent_grants(id,claim_hash,setup_hash,agent_name,agent_version,purpose,state,created_at,request_expires_at,approved_at,expires_at,terms_version,privacy_version,owner_user_id) VALUES(?,?,?,?,?,?,\'approved\',?,?,?,?,?,?,?)',
                   (grant_id,hashlib.sha256(claim.encode()).hexdigest(),hashlib.sha256(setup.encode()).hexdigest(),evidence['agent_name'],evidence['agent_version'],'One exact historical revision; external operator-recorded authorization.',a.iso(),expiry,a.iso(),expiry,a.TERMS_VERSION,a.PRIVACY_VERSION,owner['id']))
        evidence_hash=hashlib.sha256(raw).hexdigest()
        db.execute('INSERT INTO historical_revision_grants VALUES(?,?,?,?,?,?)',(grant_id,binding,catalog_hash,raw.decode(),evidence_hash,actor['id']))
        db.commit()
        g.user=actor
        a.audit('historical_revision_delegation_authorized',grant_id=grant_id,evidence_sha256=evidence_hash,scope=evidence['scope'],method='operator_recorded_external_instruction')
        click.echo(json.dumps({'request_id':grant_id,'agent_token':claim,'expires_at':expiry,'scope':evidence['scope'],'uploads_remaining':1}))
