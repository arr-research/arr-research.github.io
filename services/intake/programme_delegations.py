# SPDX-License-Identifier: AGPL-3.0-or-later
"""Revocable initial author instructions, with separate exact-PDF child grants.

The controller token cannot upload, edit cases, assess, accept or publish. It
can request one-use intake grants within its recorded author/programme scope.
"""
import base64
from datetime import datetime, timedelta
import hashlib
import hmac
import json
import os
from pathlib import Path
import re
import secrets

import click
from flask import abort, g, request

from services.intake import historical_revisions as historical


def migrate(db):
    db.executescript('''
      CREATE TABLE IF NOT EXISTS programme_delegations (
        id TEXT PRIMARY KEY, token_hash TEXT UNIQUE NOT NULL,
        owner_user_id INTEGER NOT NULL REFERENCES users(id),
        authorized_by INTEGER NOT NULL REFERENCES users(id),
        state TEXT NOT NULL, evidence_json TEXT NOT NULL,
        evidence_sha256 TEXT NOT NULL, created_at TEXT NOT NULL
      );
      CREATE TABLE IF NOT EXISTS programme_artifact_grants (
        grant_id TEXT PRIMARY KEY REFERENCES agent_grants(id) ON DELETE CASCADE,
        programme_id TEXT NOT NULL REFERENCES programme_delegations(id),
        request_sha256 TEXT NOT NULL, artifact_json TEXT NOT NULL,
        UNIQUE(programme_id,request_sha256)
      );
    ''')


def enabled(app):
    return app.config.get('PROGRAMME_DELEGATIONS_ENABLED',
                          os.environ.get('AIRR_PROGRAMME_DELEGATIONS_ENABLED') == '1')


def current(app, a, programme):
    if not enabled(app) or not programme or programme['state'] != 'active':
        abort(403, 'Programme delegation is unavailable or revoked.')
    evidence = json.loads(programme['evidence_json'])
    db = a.get_db()
    owner = db.execute("SELECT 1 FROM users u JOIN private_accounts p ON p.user_id=u.id WHERE u.id=? AND u.active=1 AND u.role='depositor' AND p.identity_kind='human'", (programme['owner_user_id'],)).fetchone()
    actor = db.execute("SELECT 1 FROM users WHERE id=? AND email=? AND active=1 AND role='operator' AND totp_secret IS NOT NULL", (programme['authorized_by'], app.config['OPERATOR_EMAIL'])).fetchone()
    if not owner or not actor or evidence['author'] != app.config.get('HISTORICAL_OPERATOR_AUTHOR'):
        abort(403, 'Original author workspace/operator is no longer active.')
    if evidence['terms_version'] != a.TERMS_VERSION or evidence['privacy_version'] != a.PRIVACY_VERSION:
        abort(403, 'Changed terms/privacy require an updated initial instruction.')
    return evidence


def artifact_for(db, grant_id):
    return db.execute('SELECT * FROM programme_artifact_grants WHERE grant_id=?', (grant_id,)).fetchone()


def check_child(app, a, grant_id, metadata=None):
    child = artifact_for(a.get_db(), grant_id)
    if child:
        programme = a.get_db().execute('SELECT * FROM programme_delegations WHERE id=?', (child['programme_id'],)).fetchone()
        evidence = current(app, a, programme)
        artifact = json.loads(child['artifact_json'])
        if metadata is not None and (metadata['sha256'] != artifact['sha256'] or metadata['authors'] != evidence['author'] or metadata['rights_confirmed'] is not True or metadata['operator_conflict'] is not True):
            abort(400, 'Exact PDF, sole author, rights and conflict must match programme authority.')
        return artifact
    return None


def install(app, a, api, require_open):
    @app.cli.command('authorize-programme')
    @click.argument('evidence_file', type=click.Path(exists=True, dir_okay=False))
    def authorize_programme(evidence_file):
        """Authenticated host only; stdout contains the controller secret once."""
        require_open()
        if not enabled(app):
            raise click.ClickException('Programme delegation is disabled.')
        raw = Path(evidence_file).read_bytes()
        try:
            if len(raw) > 20000:
                raise ValueError('Evidence too large.')
            evidence = json.loads(raw)
            fields = {'owner_user_id', 'programme', 'author', 'author_instruction',
                      'source_reference', 'recorded_at', 'terms_version', 'privacy_version',
                      'rights_confirmed', 'operator_authorship_confirmed', 'paper_ids',
                      'allow_new_submissions', 'pdf_license', 'metadata_license', 'publication_status'}
            if not isinstance(evidence, dict) or set(evidence) != fields:
                raise ValueError('Initial authority fields do not match the contract.')
            for key in ('rights_confirmed', 'operator_authorship_confirmed'):
                if evidence[key] is not True:
                    raise ValueError('Actual author rights and operator attestation required.')
            if type(evidence['allow_new_submissions']) is not bool:
                raise ValueError('Explicit new-submission scope required.')
            if not isinstance(evidence['paper_ids'], list) or len(evidence['paper_ids']) > 100 or any(not isinstance(p, str) or not re.fullmatch(r'ARR-\d{4}-[A-Z0-9]{16}', p) for p in evidence['paper_ids']):
                raise ValueError('Explicit bounded existing-paper scope required.')
            for key, minimum, maximum in [('programme', 3, 100), ('author', 3, 200), ('author_instruction', 40, 8000), ('source_reference', 10, 2000)]:
                if not isinstance(evidence[key], str) or not minimum <= len(evidence[key].strip()) <= maximum:
                    raise ValueError('Preserve actual initial instruction, source and identity.')
            stamp = datetime.fromisoformat(evidence['recorded_at'])
            if stamp.tzinfo is None or stamp > a.now() or stamp < a.now()-timedelta(days=7):
                raise ValueError('Record a recent actual initial instruction, not a renewed human assent.')
            release_scope = (evidence['pdf_license'], evidence['metadata_license'], evidence['publication_status'])
            if release_scope not in (('CC-BY-4.0', 'CC0-1.0', 'working_paper'), (None, None, 'private')):
                raise ValueError('Choose explicit CC-BY/CC0 Working-paper scope or private intake with null public licences.')
            db = a.get_db()
            actor = db.execute("SELECT id FROM users WHERE email=? AND role='operator' AND active=1 AND totp_secret IS NOT NULL", (app.config['OPERATOR_EMAIL'],)).fetchone()
            if not actor:
                raise ValueError('Active configured MFA operator required.')
            probe = {'state': 'active', 'evidence_json': raw.decode(), 'owner_user_id': evidence['owner_user_id'], 'authorized_by': actor['id']}
            current(app, a, probe)
        except (ValueError, TypeError, KeyError, UnicodeError) as error:
            raise click.ClickException(str(error)) from error
        identity = 'PRG-'+secrets.token_hex(12).upper()
        token = secrets.token_urlsafe(32)
        evidence_hash = hashlib.sha256(raw).hexdigest()
        db.execute('INSERT INTO programme_delegations VALUES(?,?,?,?,?,?,?,?)',
                   (identity, hashlib.sha256(token.encode()).hexdigest(), evidence['owner_user_id'], actor['id'], 'active', raw.decode(), evidence_hash, a.iso()))
        db.commit()
        g.user = db.execute('SELECT * FROM users WHERE id=?', (actor['id'],)).fetchone()
        a.audit('programme_delegation_authorized', programme_id=identity, evidence_sha256=evidence_hash)
        click.echo(json.dumps({'programme_id': identity, 'controller_token': token,
                              'scope': ['exact-intake-grant:create'], 'expires_at': None,
                              'revocable': True, 'human_instruction_sha256': evidence_hash}))

    @app.cli.command('revoke-programme')
    @click.argument('programme_id')
    def revoke_programme(programme_id):
        db = a.get_db()
        if db.execute("UPDATE programme_delegations SET state='revoked' WHERE id=?", (programme_id,)).rowcount != 1:
            raise click.ClickException('Unknown programme delegation.')
        db.execute("UPDATE agent_grants SET state='revoked' WHERE id IN (SELECT grant_id FROM programme_artifact_grants WHERE programme_id=?)", (programme_id,))
        db.commit()
        a.audit('programme_delegation_revoked', programme_id=programme_id)
        click.echo(json.dumps({'programme_id': programme_id, 'state': 'revoked'}))

    @api.post('/programme-artifact-grants')
    def issue_artifact():
        require_open()
        header = request.headers.get('Authorization', '')
        if not re.fullmatch(r'Bearer [A-Za-z0-9_-]{43}', header):
            abort(401, 'A programme controller token is required.')
        db = a.get_db()
        programme = db.execute('SELECT * FROM programme_delegations WHERE token_hash=?', (hashlib.sha256(header[7:].encode()).hexdigest(),)).fetchone()
        if not programme:
            abort(401, 'Invalid programme token.')
        evidence = current(app, a, programme)
        a.enforce_rate('programme-grant', 120, 3600, programme['id'])
        if request.content_length is None or request.content_length > 16000:
            abort(413, 'Artifact request exceeds 16 KiB.')
        value = request.get_json(silent=True)
        fields = {'sha256', 'kind', 'binding', 'agent_name', 'agent_version'}
        if not isinstance(value, dict) or set(value) not in (fields, fields | {'renew_expired_unused'}):
            abort(400, 'Supply exact hash, intake kind, binding and actual agent identity.')
        renew = value.pop('renew_expired_unused', False)
        if type(renew) is not bool:
            abort(400, 'Explicit unused-grant renewal flag must be boolean.')
        if not isinstance(value['sha256'], str) or not re.fullmatch('[a-f0-9]{64}', value['sha256']):
            abort(400, 'Exact lowercase PDF SHA-256 required.')
        for key in ('agent_name', 'agent_version'):
            if not isinstance(value[key], str) or not 2 <= len(value[key].strip()) <= 100:
                abort(400, 'Actual bounded agent identity required.')
        catalog_hash = None
        if value['kind'] == 'revision':
            try:
                entries, catalog_hash = historical.catalogue(app)
                historical.validate_binding(value['binding'], entries, evidence['author'])
                if value['binding']['paper_id'] not in evidence['paper_ids'] or value['binding']['sha256'] != value['sha256']:
                    raise ValueError('Revision lies outside initial programme scope.')
            except (ValueError, OSError, TypeError, KeyError) as error:
                abort(400, str(error))
        elif value['kind'] != 'submission' or not evidence['allow_new_submissions'] or value['binding'] is not None:
            abort(400, 'Intake kind is not authorized by initial instruction.')
        canonical = json.dumps(value, sort_keys=True, separators=(',', ':'))
        request_hash = hashlib.sha256(canonical.encode()).hexdigest()
        # Deterministic per request and bearer: response retries recover the SAME
        # secret without storing a plaintext token or silently renewing expiry.
        claim = base64.urlsafe_b64encode(hmac.new(header[7:].encode(), ('artifact:'+request_hash).encode(), hashlib.sha256).digest()).decode().rstrip('=')
        db.execute('BEGIN IMMEDIATE')
        try:
            current(app, a, db.execute('SELECT * FROM programme_delegations WHERE id=?', (programme['id'],)).fetchone())
            old = db.execute('SELECT g.* FROM agent_grants g JOIN programme_artifact_grants p ON p.grant_id=g.id WHERE p.programme_id=? AND p.request_sha256=?', (programme['id'], request_hash)).fetchone()
            if old:
                if old['state'] != 'approved':
                    abort(409, 'Existing exact grant is revoked; no renewal.')
                if old['expires_at'] <= a.iso():
                    used = db.execute('SELECT 1 FROM agent_submissions WHERE grant_id=?', (old['id'],)).fetchone()
                    if not renew or old['uses'] or used:
                        abort(409, 'Existing exact grant is expired; reconcile receipt before explicit unused-grant renewal.')
                    expiry = a.iso(a.now()+timedelta(hours=24))
                    db.execute('UPDATE agent_grants SET approved_at=?,expires_at=? WHERE id=?', (a.iso(), expiry, old['id']))
                    identity = old['id']
                else:
                    identity, expiry = old['id'], old['expires_at']
            else:
                prior = db.execute("SELECT 1 FROM programme_artifact_grants WHERE programme_id=? AND json_extract(artifact_json,'$.sha256')=?", (programme['id'], value['sha256'])).fetchone()
                received = db.execute('SELECT 1 FROM submissions WHERE user_id=? AND sha256=?', (programme['owner_user_id'], value['sha256'])).fetchone()
                if prior or received:
                    abort(409, 'Exact PDF already has a grant/case; reconcile original artifact, do not create a duplicate.')
                identity = 'AGT-'+secrets.token_hex(12).upper()
                expiry = a.iso(a.now()+timedelta(hours=24))
                db.execute("INSERT INTO agent_grants(id,claim_hash,setup_hash,agent_name,agent_version,purpose,state,created_at,request_expires_at,approved_at,expires_at,terms_version,privacy_version,owner_user_id) VALUES(?,?,?,?,?,?,'approved',?,?,?,?,?,?,?)", (identity, hashlib.sha256(claim.encode()).hexdigest(), hashlib.sha256(secrets.token_bytes(32)).hexdigest(), value['agent_name'], value['agent_version'], 'One exact PDF under initial programme author instruction.', a.iso(), expiry, a.iso(), expiry, a.TERMS_VERSION, a.PRIVACY_VERSION, programme['owner_user_id']))
                db.execute('INSERT INTO programme_artifact_grants VALUES(?,?,?,?)', (identity, programme['id'], request_hash, canonical))
                if value['kind'] == 'revision':
                    authorization = json.dumps({'method': 'standing_programme_instruction', 'programme_id': programme['id'], 'initial_instruction_sha256': programme['evidence_sha256'], 'initial_recorded_at': evidence['recorded_at'], 'artifact_recorded_at': a.iso()}, sort_keys=True)
                    db.execute('INSERT INTO historical_revision_grants VALUES(?,?,?,?,?,?)', (identity, json.dumps(value['binding'], sort_keys=True), catalog_hash, authorization, hashlib.sha256(authorization.encode()).hexdigest(), programme['authorized_by']))
            db.commit()
        except BaseException:
            db.rollback()
            raise
        a.audit('programme_artifact_grant_issued', programme_id=programme['id'], grant_id=identity, sha256=value['sha256'], explicit_unused_renewal=renew, initial_instruction_sha256=programme['evidence_sha256'])
        response = app.response_class(json.dumps({'request_id': identity, 'agent_token': claim, 'expires_at': expiry, 'uploads_remaining': max(0, 1-(old['uses'] if old else 0)), 'scope': ['revision:create' if value['kind'] == 'revision' else 'submission:create', 'submission:receipt'], 'programme_id': programme['id'], 'initial_instruction_sha256': programme['evidence_sha256']}), mimetype='application/json')
        response.headers['Cache-Control'] = 'no-store'
        return response
