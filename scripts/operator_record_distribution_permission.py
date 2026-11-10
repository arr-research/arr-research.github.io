"""Record an actual editor-reported external distribution grant; never accepts a paper."""
import argparse
from datetime import datetime, timezone, timedelta
import hashlib
import json
from pathlib import Path
from flask import g
from services.intake.app import app, get_db, iso, audit

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('evidence')
parser.add_argument('--apply',action='store_true')
args=parser.parse_args()
raw=Path(args.evidence).read_bytes();value=json.loads(raw)
required={'submission_id','manuscript_sha256','operator_name','license','rights_confirmed','instruction','source_reference','recorded_at'}
if set(value)!=required or value['rights_confirmed'] is not True or value['license']!='LicenseRef-Author-Retained':
 raise SystemExit('Exact external distribution evidence with retained author rights required.')
time=datetime.fromisoformat(value['recorded_at'])
if time.tzinfo is None or not timedelta(0)<=datetime.now(timezone.utc)-time<timedelta(hours=24):
 raise SystemExit('Current, dated evidence required.')
if len(value['instruction'])<80 or len(value['source_reference'])<40:
 raise SystemExit('Preserve the actual instruction and source.')
with app.app_context():
 db=get_db();row=db.execute('SELECT * FROM submissions WHERE id=?',(value['submission_id'],)).fetchone()
 actor=db.execute("SELECT * FROM users WHERE email=? AND role='operator' AND active=1 AND totp_secret IS NOT NULL",(app.config['OPERATOR_EMAIL'],)).fetchone()
 if not row or not actor or actor['display_name']!=value['operator_name']:
  raise SystemExit('Existing exact case and configured MFA operator required.')
 if row['sha256']!=value['manuscript_sha256'] or row['scan_status']!='clean' or row['status'] not in {'eligible','under_assessment','changes_requested'} or row['other_operator_conflict'] or row['submission_channel']=='independent_agent':
  raise SystemExit('Clean current human case without unresolved operator conflicts required.')
 pdf=Path(app.config['QUARANTINE'])/row['stored_name']
 if hashlib.sha256(pdf.read_bytes()).hexdigest()!=row['sha256']:
  raise SystemExit('Stored PDF hash mismatch.')
 previous=db.execute('SELECT * FROM publication_permissions WHERE submission_id=?',(row['id'],)).fetchone()
 if previous and (previous['manuscript_sha256']!=row['sha256'] or previous['license']!=value['license']):
  raise SystemExit('Existing different permission cannot be replaced.')
 if args.apply and not previous:
  db.execute('INSERT INTO publication_permissions VALUES(?,?,?,?)',(row['id'],row['sha256'],value['license'],iso()));db.commit()
  g.user=actor
  audit('publication_permission_recorded',row['id'],sha256=row['sha256'],license=value['license'],method='editor_recorded_external_author_authorization',evidence=value,evidence_sha256=hashlib.sha256(raw).hexdigest(),public_status='working_paper')
 print(json.dumps({'submission_id':row['id'],'permission_recorded':bool(previous or args.apply),'already_recorded':bool(previous),'sha256':row['sha256'],'accepted':False,'published':False}))
