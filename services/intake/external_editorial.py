"""Record explicit external founder instructions on an authenticated host.

No web session or human signature is simulated. Each operation requires a fresh,
exact-artifact human instruction; model recommendations alone never invoke it.
Only sole-author historical cases owned by the configured founder are supported.
"""
import hashlib
import json
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

import click
from flask import g


def install(app, a, case):
    def evidence(path, extra):
        raw = Path(path).read_bytes()
        if len(raw) > 20000:
            raise click.ClickException('Evidence exceeds 20 KB.')
        value = json.loads(raw)
        common = {'submission_id', 'manuscript_sha256', 'human_name',
                  'human_instruction', 'source_reference', 'recorded_at'}
        if not isinstance(value, dict) or set(value) != common | extra:
            raise click.ClickException('Exact external-instruction schema required.')
        for name, minimum in [('human_name', 3), ('human_instruction', 40), ('source_reference', 15)]:
            if not isinstance(value[name], str) or not minimum <= len(value[name].strip()) <= 6000:
                raise click.ClickException('Missing actual human evidence: ' + name)
        try:
            stamp = datetime.fromisoformat(value['recorded_at'].replace('Z', '+00:00'))
            if stamp.tzinfo is None or not a.now()-timedelta(days=7) <= stamp <= a.now():
                raise ValueError
        except (AttributeError, TypeError, ValueError):
            raise click.ClickException('Recent offset-aware evidence timestamp required.')
        return value, hashlib.sha256(raw).hexdigest()

    def guarded_case(value):
        db = a.get_db()
        actor = db.execute("SELECT * FROM users WHERE email=? AND role='operator' AND active=1 AND totp_secret IS NOT NULL", (app.config['OPERATOR_EMAIL'],)).fetchone()
        if not actor or value['human_name'] != actor['display_name']:
            raise click.ClickException('The actual configured MFA operator must be named.')
        g.user = actor
        row = case(value['submission_id'])
        binding = db.execute('SELECT binding_json FROM historical_revisions WHERE submission_id=?', (row['id'],)).fetchone()
        if not binding or row['authors'] != value['human_name'] or not app.extensions['editorial']['founder_may_decide'](row, actor):
            raise click.ClickException('Only the declared sole-author historical founder case qualifies.')
        if row['sha256'] != value['manuscript_sha256'] or row['scan_status'] != 'clean':
            raise click.ClickException('Exact clean manuscript required.')
        if hashlib.sha256((Path(app.config['QUARANTINE']) / row['stored_name']).read_bytes()).hexdigest() != row['sha256']:
            raise click.ClickException('Stored manuscript integrity mismatch.')
        if db.execute('SELECT 1 FROM appeals WHERE submission_id=?', (row['id'],)).fetchone():
            raise click.ClickException('Appeals require their separate independent workflow.')
        return db, actor, row

    @app.cli.command('record-external-founder-adjudication')
    @click.argument('evidence_file', type=click.Path(exists=True, dir_okay=False))
    def record_adjudication(evidence_file):
        """Preserve a minor report and record its evidenced external disposition."""
        value, digest = evidence(evidence_file, {'report_sha256', 'basis', 'resolution_evidence', 'all_objections_addressed'})
        db, actor, row = guarded_case(value)
        if row['status'] not in {'eligible', 'under_assessment', 'changes_requested', 'awaiting_independent_decision'}:
            raise click.ClickException('A current undecided case is required.')
        review = db.execute('SELECT * FROM model_reviews WHERE submission_id=? AND response_sha256=?', (row['id'], value['report_sha256'])).fetchone()
        if not review or review['recommendation'] != 'minor_revision' or review['unresolved_material_objections']:
            raise click.ClickException('This external route only handles a minor report with no unresolved material objections.')
        if value['all_objections_addressed'] is not True or any(not isinstance(value[k], str) or not n <= len(value[k].strip()) <= 6000 for k,n in [('basis',80),('resolution_evidence',40)]):
            raise click.ClickException('A claim-by-claim disposition and inspectable evidence are required.')
        note = 'Operator-recorded external human instruction; not a simulated web signature. Evidence SHA-256: ' + digest + '\n' + value['basis']
        try:
            result = db.execute('INSERT INTO adjudications(review_id,basis,evidence,signed_by,signed_at) VALUES(?,?,?,?,?)', (review['id'],note,value['resolution_evidence'],actor['id'],a.iso()))
            db.commit()
        except sqlite3.IntegrityError:
            db.rollback()
            raise click.ClickException('An existing adjudication cannot be replaced.')
        a.audit('review_adjudicated',row['id'],review_id=review['id'],method='operator_recorded_external_instruction',evidence=value,evidence_sha256=digest)
        click.echo(json.dumps({'submission_id':row['id'],'review_id':review['id'],'adjudication_id':result.lastrowid,'report_sha256':review['response_sha256'],'evidence_sha256':digest,'accepted':False,'published':False}))

    @app.cli.command('record-external-founder-decision')
    @click.argument('evidence_file', type=click.Path(exists=True, dir_okay=False))
    def record_decision(evidence_file):
        value, digest = evidence(evidence_file, {'decision', 'reason', 'report_sha256'})
        db, actor, row = guarded_case(value)
        if value['decision'] != 'accept' or not isinstance(value['reason'], str) or not 20 <= len(value['reason']) <= 200:
            raise click.ClickException('An explicit bounded human acceptance decision is required.')
        if row['status'] not in {'eligible', 'under_assessment', 'changes_requested', 'awaiting_independent_decision'}:
            raise click.ClickException('A current undecided case is required.')
        reports = db.execute('SELECT * FROM model_reviews WHERE submission_id=? ORDER BY id', (row['id'],)).fetchall()
        expected = sorted(r['response_sha256'] for r in reports)
        hashes = value['report_sha256']
        if not isinstance(hashes, list) or any(not isinstance(x,str) for x in hashes) or sorted(hashes) != expected or not expected:
            raise click.ClickException('The human decision must bind every recorded report.')
        if not row['ai_review_opt_in'] or not app.extensions['editorial']['can_accept'](row, reports):
            raise click.ClickException('The complete authorized model gate and objection dispositions are required.')
        note = 'Operator-recorded external human instruction; not a simulated web signature. Evidence SHA-256: ' + digest
        db.execute("UPDATE submissions SET status='accepted_for_publication',updated_at=?,decided_at=?,decision_by=?,decision_reason=?,decision_note=? WHERE id=?", (a.iso(),a.iso(),actor['id'],value['reason'],note,row['id']))
        db.commit()
        a.audit('editorial_decision',row['id'],action='accept',resulting_status='accepted_for_publication',reason=value['reason'],founder_author_editor=True,policy='AIRR-FOUNDER-1.0',method='operator_recorded_external_instruction',evidence=value,evidence_sha256=digest)
        app.extensions['editorial']['decided'](row['id'])
        click.echo(json.dumps({'submission_id':row['id'],'status':'accepted_for_publication','published':False,'evidence_sha256':digest}))

    @app.cli.command('record-external-founder-publication')
    @click.argument('evidence_file', type=click.Path(exists=True, dir_okay=False))
    def record_publication(evidence_file):
        value, digest = evidence(evidence_file, {'license', 'distribution_scope', 'rights_basis'})
        db, actor, row = guarded_case(value)
        if row['status'] != 'accepted_for_publication':
            raise click.ClickException('A separately recorded human acceptance is required first.')
        if value['license'] not in {'CC-BY-4.0','CC-BY-SA-4.0','CC0-1.0','LicenseRef-Author-Retained'}:
            raise click.ClickException('Unsupported manuscript license.')
        if value['distribution_scope'] != ['exact_manuscript','assessment_reports','associated_sources'] or not isinstance(value['rights_basis'],str) or not 80 <= len(value['rights_basis']) <= 2000:
            raise click.ClickException('Explicit exact-file distribution and rights evidence required.')
        if db.execute('SELECT 1 FROM publication_permissions WHERE submission_id=?',(row['id'],)).fetchone():
            raise click.ClickException('Existing public permission cannot be replaced.')
        db.execute('INSERT INTO publication_permissions VALUES(?,?,?,?)',(row['id'],row['sha256'],value['license'],a.iso()))
        db.commit()
        a.audit('publication_permission_recorded',row['id'],license=value['license'],sha256=row['sha256'],public_status='accepted',method='operator_recorded_external_instruction',evidence=value,evidence_sha256=digest)
        click.echo(json.dumps({'submission_id':row['id'],'publication_permission_recorded':True,'published':False,'evidence_sha256':digest}))
