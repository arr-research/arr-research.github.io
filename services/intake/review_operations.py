"""Authenticated-host preparation tools; none can accept or publish a case.

The operator may record an explicit instruction obtained outside the web form.
Its exact text, source, timestamp, scope and hash are retained in the audit log.
This is labelled external authorization, never a simulated author web signature.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
from datetime import datetime
from pathlib import Path

import click
from flask import g


def install(app, a, case, current_plan):
    def operator():
        row = a.get_db().execute("SELECT * FROM users WHERE email=? AND role='operator' AND active=1 AND totp_secret IS NOT NULL", (app.config['OPERATOR_EMAIL'],)).fetchone()
        if not row:
            raise click.ClickException('No active configured operator with MFA exists.')
        g.user = row
        return row

    def read_json(path):
        raw = Path(path).read_bytes()
        if len(raw) > 128_000:
            raise click.ClickException('Evidence or report exceeds 128 KB.')
        return json.loads(raw), hashlib.sha256(raw).hexdigest()

    def open_case(case_id):
        row = case(case_id)
        if row['scan_status'] != 'clean' or row['status'] not in {'eligible','under_assessment','changes_requested','awaiting_independent_decision'}:
            raise click.ClickException('A clean, current private case is required.')
        pdf = Path(app.config['QUARANTINE']) / row['stored_name']
        if hashlib.sha256(pdf.read_bytes()).hexdigest() != row['sha256']:
            raise click.ClickException('Stored PDF does not match the locked hash.')
        return row

    @app.cli.command('prepare-founder-round')
    @click.argument('submission_id')
    @click.argument('authorization_file', type=click.Path(exists=True, dir_okay=False))
    @click.option('--request-changes', is_flag=True, help='Request a corrected revision; never accepts a case.')
    def prepare_founder_round(submission_id, authorization_file, request_changes):
        actor = operator()
        row = open_case(submission_id)
        value, evidence_hash = read_json(authorization_file)
        required = {'submission_id','manuscript_sha256','notice','author_instruction','source_reference','authorization_recorded_at','models','founder_authorship_basis'}
        if not isinstance(value, dict) or set(value) != required:
            raise click.ClickException('Authorization evidence fields do not match the documented schema.')
        if value['submission_id'] != row['id'] or value['manuscript_sha256'] != row['sha256']:
            raise click.ClickException('Authorization must bind this exact case and hash.')
        for key, minimum in [('notice',80),('author_instruction',20),('source_reference',10),('founder_authorship_basis',40)]:
            if not isinstance(value[key], str) or not minimum <= len(value[key].strip()) <= 6000:
                raise click.ClickException('Missing explicit instruction, source or authorship evidence: ' + key)
        try:
            stamp = datetime.fromisoformat(value['authorization_recorded_at'].replace('Z','+00:00'))
            if stamp.tzinfo is None or stamp > a.now():
                raise ValueError
        except (ValueError, TypeError, AttributeError):
            raise click.ClickException('An actual offset-aware authorization record time is required.')
        models = value['models']
        if not isinstance(models, list) or not 2 <= len(models) <= 6:
            raise click.ClickException('Declare two to six distinct models.')
        pairs = set()
        for item in models:
            if not isinstance(item, dict) or set(item) != {'provider','model_id'} or any(not isinstance(v,str) or not 2 <= len(v.strip()) <= 160 or v != v.strip() for v in item.values()):
                raise click.ClickException('Invalid provider/model identifier.')
            pairs.add((item['provider'], item['model_id']))
        if len(pairs) != len(models):
            raise click.ClickException('Duplicate models do not constitute distinct reviews.')
        db = a.get_db()
        if current_plan(submission_id) or db.execute('SELECT 1 FROM model_reviews WHERE submission_id=?', (submission_id,)).fetchone():
            raise click.ClickException('A plan already exists; do not replace a declared round.')
        if row['founder_authored'] and row['founder_declared_by'] != actor['id']:
            raise click.ClickException('Existing founder declaration has a different actor.')
        providers = json.dumps(models, sort_keys=True)
        db.execute('UPDATE submissions SET founder_authored=1,operator_conflict=1,founder_declared_by=?,founder_declared_at=COALESCE(founder_declared_at,?),ai_review_opt_in=1,updated_at=? WHERE id=?',
                   (actor['id'],a.iso(),a.iso(),submission_id))
        plan = db.execute('INSERT INTO assessment_plans(submission_id,manuscript_sha256,providers_json,notice,created_by,created_at,authorized_at,authorization_hash) VALUES(?,?,?,?,?,?,?,?)',
                         (submission_id,row['sha256'],providers,value['notice'],actor['id'],a.iso(),value['authorization_recorded_at'],evidence_hash))
        if request_changes:
            db.execute("UPDATE submissions SET status='changes_requested',decision_by=?,decided_at=?,decision_reason=?,decision_note=?,updated_at=? WHERE id=?",
                       (actor['id'],a.iso(),'Corrected revision requested by author',value['founder_authorship_basis'],a.iso(),submission_id))
        db.commit()
        a.audit('external_author_instruction_recorded', submission_id, evidence=value, evidence_sha256=evidence_hash, method='operator_recorded_external_instruction', plan_id=plan.lastrowid, requested_revision=bool(request_changes), policy='AIRR-FOUNDER-1.0')
        click.echo(json.dumps({'submission_id':submission_id,'plan_id':plan.lastrowid,'evidence_sha256':evidence_hash,'status':case(submission_id)['status'],'accepted':False}))

    @app.cli.command('record-assessment')
    @click.argument('report_file', type=click.Path(exists=True, dir_okay=False))
    @click.argument('runtime_evidence_file', type=click.Path(exists=True, dir_okay=False))
    def record_assessment(report_file, runtime_evidence_file):
        actor = operator()
        value, original_hash = read_json(report_file)
        if not isinstance(value,dict) or not isinstance(value.get('submission_id'),str):
            raise click.ClickException('Expected a structured report with a submission identifier.')
        row = open_case(value['submission_id'])
        errors = a.validate_model_review(value,row)
        if errors:
            raise click.ClickException('; '.join(errors))
        plan = current_plan(row['id'])
        pair = (value['provider'],value['model_id'])
        if not row['ai_review_opt_in'] or not plan or not plan['authorized_at'] or plan['manuscript_sha256'] != row['sha256'] or pair not in {(x['provider'],x['model_id']) for x in json.loads(plan['providers_json'])}:
            raise click.ClickException('The exact model and artifact need recorded author authorization.')
        evidence, evidence_hash = read_json(runtime_evidence_file)
        if not isinstance(evidence,dict) or evidence.get('provider') != value['provider'] or evidence.get('model_id') != value['model_id'] or evidence.get('report_sha256') != original_hash or not evidence.get('source_reference'):
            raise click.ClickException('Runtime evidence must identify the actual model, source and original report hash.')
        canonical = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        canonical_hash = hashlib.sha256(canonical.encode()).hexdigest()
        db = a.get_db()
        try:
            report = db.execute('INSERT INTO model_reviews(submission_id,provider,model_id,assessed_at,recommendation,millennium_score,overall_stars,unresolved_material_objections,response_json,response_sha256,recorded_by,recorded_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',
                       (row['id'],value['provider'],value['model_id'],value['assessed_at'],value['recommendation'],value['millennium_score'],value['overall_stars'],len(value['unresolved_material_objections']),canonical,canonical_hash,actor['id'],a.iso()))
            db.execute("UPDATE submissions SET status=CASE WHEN status='eligible' THEN 'under_assessment' ELSE status END,updated_at=? WHERE id=?",(a.iso(),row['id']))
            db.commit()
        except sqlite3.IntegrityError:
            db.rollback()
            raise click.ClickException('This exact response is already recorded; it cannot be replaced.')
        a.audit('frontier_model_review_recorded_external',row['id'],report_id=report.lastrowid,response_sha256=canonical_hash,original_response_sha256=original_hash,runtime_evidence=evidence,runtime_evidence_sha256=evidence_hash)
        reports = db.execute('SELECT * FROM model_reviews WHERE submission_id=? ORDER BY id',(row['id'],)).fetchall()
        click.echo(json.dumps({'submission_id':row['id'],'report_id':report.lastrowid,'response_sha256':canonical_hash,'reports':len(reports),'model_gate_ready':app.extensions['editorial']['can_accept'](case(row['id']),reports),'accepted':False}))
