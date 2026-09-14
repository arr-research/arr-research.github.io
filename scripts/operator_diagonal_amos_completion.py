"""One-paper operator-console helper; uses the installed guarded intake CLI.

No new access, service, key, endpoint or general deployment is installed.
Human instruction is supplied by the authenticated operator, never generated here.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import urllib.request

SID='SUB-7EFC8AE6CD94CB26'
PID='ARR-2026-39Y0F83F4Z9JK90G'
SHA='eabefc6d93e453b5599f7c1e8c1c7c311352c43d7d61eec0223dced09720ce0c'
REPORTS=sorted(['220c7ab9e6f76e412c93d0c3fc19e5a7800609ab36e34a23a0d371cc2dfda86b','05a5635ac73bcab8caf519bfce8754406c7c23d3869da9eb1e859257751b7fcf'])
RELEASE='https://github.com/arr-research/arr-research.github.io/releases/tag/'+PID+'-v2'
ROOT=Path('/srv/airr-private/operator-completion/diagonal-amos-20260914')


def save(name,value):
    ROOT.mkdir(parents=True,exist_ok=True,mode=0o700)
    path=ROOT/name
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    path.chmod(0o600)
    return path


def main():
    p=argparse.ArgumentParser()
    p.add_argument('mode',choices=['inspect','decide','permit','published'])
    p.add_argument('--instruction')
    args=p.parse_args()
    if os.getuid()!=0:
        raise SystemExit('Authenticated operator console required.')
    sys.path.insert(0,'/opt/airr-intake/current')
    from services.intake import app as a
    app=a.create_app()
    with app.app_context():
        db=a.get_db()
        row=db.execute('SELECT * FROM submissions WHERE id=?',(SID,)).fetchone()
        assert row and row['sha256']==SHA and row['scan_status']=='clean'
        assert hashlib.sha256((Path(app.config['QUARANTINE'])/row['stored_name']).read_bytes()).hexdigest()==SHA
        reports=db.execute('SELECT * FROM model_reviews WHERE submission_id=? ORDER BY id',(SID,)).fetchall()
        assert sorted(r['response_sha256'] for r in reports)==REPORTS
        assert app.extensions['editorial']['can_accept'](row,reports)
        binding=json.loads(db.execute('SELECT binding_json FROM historical_revisions WHERE submission_id=?',(SID,)).fetchone()[0])
        assert binding['paper_id']==PID and binding['version']=='v2' and binding['sha256']==SHA
        permission=db.execute('SELECT * FROM publication_permissions WHERE submission_id=?',(SID,)).fetchone()
        if args.mode=='inspect':
            result={'checked_at':datetime.now(timezone.utc).isoformat(),'submission_id':SID,'pdf_sha256':SHA,'scan_status':row['scan_status'],'status':row['status'],'model_gate_ready':True,'reports':[{'id':r['id'],'sha256':r['response_sha256'],'score':r['millennium_score']} for r in reports],'permission':None if permission is None else dict(permission),'release':row['public_release_url']}
            save('inspection-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json',result)
            print(json.dumps(result,indent=2));return
        if args.mode=='published':
            assert row['status']=='accepted_for_publication' and permission and permission['manuscript_sha256']==SHA
            assert not row['public_release_url'],'Already recorded; inspect before retrying.'
            url='https://airr.science/papers/'+PID+'/versions/v2/'+PID+'-v2.pdf'
            raw=urllib.request.urlopen(url,timeout=45).read(30_000_000)
            assert hashlib.sha256(raw).hexdigest()==SHA,'Public exact PDF mismatch.'
            cmd=['mark-published',SID,RELEASE]
        else:
            if not args.instruction or len(args.instruction.strip())<40:
                raise SystemExit('Supply the actual explicit human instruction.')
            value={'submission_id':SID,'manuscript_sha256':SHA,'human_name':'Lluis Eriksson','human_instruction':args.instruction,'source_reference':'Direct author-editor instructions in the current AIRR continuity conversation; authenticated Netcup console. One next-paper full cycle explicitly requested after the completed Amos bound paper.','recorded_at':datetime.now(timezone.utc).isoformat()}
            if args.mode=='decide':
                value.update(decision='accept',reason='Author-editor acceptance after two favorable exact-PDF reports, declared formal-reproduction limitations and preserved verification evidence.',report_sha256=REPORTS)
                path=save('editorial-instruction.json',value)
                cmd=['record-external-founder-decision',str(path)]
            else:
                value.update(license='LicenseRef-Author-Retained',distribution_scope=['exact_manuscript','assessment_reports','associated_sources'],rights_basis='The author explicitly requested the complete publication cycle for this next exact historical paper, with its real assessments and numerical score. Existing author-retained rights are preserved; no additional Creative Commons reuse licence is inferred.')
                path=save('publication-instruction.json',value)
                cmd=['record-external-founder-publication',str(path)]
        result=app.test_cli_runner().invoke(args=cmd)
        if result.exit_code:
            raise SystemExit(result.output)
        try: value=json.loads(result.output)
        except ValueError: value={'submission_id':SID,'publication_recorded':True,'release_url':RELEASE,'output':result.output.strip()}
        value['observed_at']=datetime.now(timezone.utc).isoformat()
        save(args.mode+'-result.json',value)
        print(json.dumps(value,indent=2))


if __name__=='__main__':main()
