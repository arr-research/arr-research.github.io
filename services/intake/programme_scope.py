# SPDX-License-Identifier: AGPL-3.0-or-later
"""Append-only, host-recorded additions to an existing author programme's papers.

No controller endpoint can widen scope. Original instruction, token, licences,
contracts and child grants remain unchanged; no receipt or acceptance is created.
"""
from datetime import datetime, timedelta
import hashlib
import json
from pathlib import Path
import re

import click
from flask import g
from services.intake import historical_revisions as historical


def migrate(db):
    db.execute("""CREATE TABLE IF NOT EXISTS programme_scope_extensions (
      id INTEGER PRIMARY KEY,
      programme_id TEXT NOT NULL REFERENCES programme_delegations(id),
      evidence_json TEXT NOT NULL, evidence_sha256 TEXT NOT NULL,
      catalogue_sha256 TEXT NOT NULL,
      authorized_by INTEGER NOT NULL REFERENCES users(id), created_at TEXT NOT NULL,
      UNIQUE(programme_id,evidence_sha256))""")


def effective_evidence(db, programme, initial):
    # The original evidence is never rewritten or re-dated. A copy alone is used
    # for the bounded effective paper list; all other rights remain original.
    papers = set(initial['paper_ids'])
    if 'id' in programme.keys():
        for row in db.execute('SELECT evidence_json FROM programme_scope_extensions WHERE programme_id=? ORDER BY id', (programme['id'],)):
            extension = json.loads(row['evidence_json'])
            if extension['initial_instruction_sha256'] != programme['evidence_sha256']:
                raise ValueError('Programme extension has the wrong original instruction.')
            papers.update(extension['paper_ids'])
    if len(papers) > 100:
        raise ValueError('Effective existing-paper scope exceeds 100.')
    return {**initial, 'paper_ids': sorted(papers)}


def install(app, a, require_open, current):
    @app.cli.command('extend-programme-papers')
    @click.argument('evidence_file', type=click.Path(exists=True, dir_okay=False))
    def extend(evidence_file):
        """Existing authenticated host only; preserve the real extension instruction."""
        require_open()
        raw = Path(evidence_file).read_bytes()
        try:
            if len(raw) > 20000:
                raise ValueError('Extension evidence exceeds 20 KiB.')
            evidence = json.loads(raw)
            fields = {'programme_id','initial_instruction_sha256','paper_ids',
                      'author_instruction','source_reference','recorded_at',
                      'rights_confirmed','operator_authorship_confirmed'}
            if not isinstance(evidence, dict) or set(evidence) != fields:
                raise ValueError('Extension fields do not match the contract.')
            if not isinstance(evidence['programme_id'], str) or not re.fullmatch(r'PRG-[A-F0-9]{24}', evidence['programme_id']):
                raise ValueError('Existing programme ID required.')
            if not isinstance(evidence['initial_instruction_sha256'], str) or not re.fullmatch('[a-f0-9]{64}', evidence['initial_instruction_sha256']):
                raise ValueError('Exact original instruction hash required.')
            for key in ('rights_confirmed','operator_authorship_confirmed'):
                if evidence[key] is not True:
                    raise ValueError('Actual rights and sole-authorship attestation required.')
            for key,minimum,maximum in [('author_instruction',40,8000),('source_reference',10,2000)]:
                if not isinstance(evidence[key],str) or not minimum <= len(evidence[key].strip()) <= maximum:
                    raise ValueError('Preserve the actual instruction and source, not fresh assent.')
            stamp = datetime.fromisoformat(evidence['recorded_at'])
            if stamp.tzinfo is None or stamp > a.now() or stamp < a.now()-timedelta(days=7):
                raise ValueError('Use the recent actual extension instruction timestamp.')
            papers = evidence['paper_ids']
            if not isinstance(papers,list) or not 1 <= len(papers) <= 100 or any(not isinstance(p,str) or not re.fullmatch(r'ARR-\d{4}-[A-Z0-9]{16}',p) for p in papers) or len(set(papers)) != len(papers):
                raise ValueError('Explicit unique bounded paper IDs required.')
            db = a.get_db()
            db.execute('BEGIN IMMEDIATE')
            programme = db.execute('SELECT * FROM programme_delegations WHERE id=?',(evidence['programme_id'],)).fetchone()
            effective = current(app,a,programme)  # Includes revocation, owner, MFA and current contracts.
            if evidence['initial_instruction_sha256'] != programme['evidence_sha256']:
                raise ValueError('Original instruction hash mismatch.')
            actor = db.execute("SELECT * FROM users WHERE id=? AND email=? AND role='operator' AND active=1 AND totp_secret IS NOT NULL",(programme['authorized_by'],app.config['OPERATOR_EMAIL'])).fetchone()
            if not actor:
                raise ValueError('Original active configured MFA operator required.')
            entries,catalogue_hash = historical.catalogue(app)
            for paper in papers:
                parent = entries.get(paper)
                if not isinstance(parent,dict) or parent.get('authors') != [effective['author']]:
                    raise ValueError('Trusted catalogue must identify every added paper as sole-authored by the original author.')
            if len(set(effective['paper_ids']) | set(papers)) > 100:
                raise ValueError('Effective existing-paper scope exceeds 100.')
            digest = hashlib.sha256(raw).hexdigest()
            old = db.execute('SELECT id FROM programme_scope_extensions WHERE programme_id=? AND evidence_sha256=?',(programme['id'],digest)).fetchone()
            if not old:
                if set(papers) <= set(effective['paper_ids']):
                    raise ValueError('No new paper scope; reuse the original extension evidence for retries.')
                db.execute('INSERT INTO programme_scope_extensions(programme_id,evidence_json,evidence_sha256,catalogue_sha256,authorized_by,created_at) VALUES(?,?,?,?,?,?)',(programme['id'],raw.decode(),digest,catalogue_hash,actor['id'],a.iso()))
            db.commit()
        except (ValueError,TypeError,KeyError,UnicodeError,OSError) as error:
            a.get_db().rollback()
            raise click.ClickException(str(error)) from error
        except BaseException:
            a.get_db().rollback()
            raise
        g.user = actor
        if not old:
            a.audit('programme_paper_scope_extended',programme_id=programme['id'],initial_instruction_sha256=programme['evidence_sha256'],extension_instruction_sha256=digest,paper_ids=papers)
        click.echo(json.dumps({'programme_id':programme['id'],'initial_instruction_sha256':programme['evidence_sha256'],'extension_instruction_sha256':digest,'effective_paper_ids':sorted(set(effective['paper_ids'])|set(papers)),'original_instruction_unchanged':True,'already_recorded':bool(old),'grant_created':False,'published':False}))
