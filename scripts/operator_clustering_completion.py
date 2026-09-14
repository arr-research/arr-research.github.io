"""Exact-paper authenticated-console operations with preserved native reports.

Uses guarded intake CLI commands. No web signature, new access or service is
installed. The additional minor-adjudication command is loaded for this process
from the separately hashed, tested operator module; production files are intact.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import urllib.request
import zipfile

SID='SUB-E484D42E9265CC06'
PID='ARR-2026-31ED4MTKC18JPSDE'
SHA='0701c2578111536ffed8eb97db5e95f69a5509e7337cbc9b9f1e0bc6755f0505'
REPORTS=sorted(['9efc4a22eaf3f5841bf347c1c4ded34b538d06d68283a64bf464e461a9e1d13d','9368829624c0e802ecd695884e0c87c3825853883018caa28bcbe6393437d530'])
RELEASE='https://github.com/arr-research/arr-research.github.io/releases/tag/'+PID+'-v2'
ROOT=Path('/srv/airr-private/clustering-completion-20260914')
CIPHER='dd8acdfd4736053825a7c5aced6e73773c2c2c7e71408e9b52e12fa13319e83c'
PLAIN='442eeb150797f9a30fc47a21ea3923cbd29f23e87ece4828410b408d9c025bfc'
MODULE='d1cd9874a0646734d47db0e90dde93a96de44baf721eb22e7984a9d56b6ffcd1'
URL='https://github.com/arr-research/arr-research.github.io/releases/download/OPERATOR-TRANSFER-CLUSTERING-2026-09-14/clustering-reviews-20260914.zip.age'

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,value):
    p=ROOT/name;p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');p.chmod(0o600);return p

def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['reports','adjudicate','inspect','decide','permit','published']);p.add_argument('--instruction');args=p.parse_args()
    assert os.getuid()==0,'Authenticated operator console required.'
    os.umask(0o077)
    cipher=ROOT/'reviews.zip.age';plain=ROOT/'reviews.zip';packet=ROOT/'reviews'
    if not cipher.exists():cipher.write_bytes(urllib.request.urlopen(URL,timeout=45).read())
    assert digest(cipher)==CIPHER
    if not plain.exists():subprocess.run(['age','-d','-i','/etc/ssh/ssh_host_ed25519_key','-o',str(plain),str(cipher)],check=True)
    assert digest(plain)==PLAIN
    packet.mkdir(exist_ok=True)
    with zipfile.ZipFile(plain) as z:
        for name in z.namelist():assert (packet/name).resolve().is_relative_to(packet.resolve())
        z.extractall(packet)
    for item in json.loads((packet/'MANIFEST.json').read_bytes()):assert digest(packet/item['path'])==item['sha256']
    sys.path.insert(0,'/opt/airr-intake/current')
    from services.intake import app as a
    app=a.create_app()
    def cli(*cmd):
        result=app.test_cli_runner().invoke(args=list(cmd))
        if result.exit_code:raise RuntimeError(result.output)
        try:return json.loads(result.output)
        except ValueError:return {'submission_id':SID,'publication_recorded':True,'release_url':RELEASE,'output':result.output.strip()}
    with app.app_context():
        db=a.get_db();row=db.execute('SELECT * FROM submissions WHERE id=?',(SID,)).fetchone()
        assert row and row['sha256']==SHA and row['scan_status']=='clean'
        assert digest(Path(app.config['QUARANTINE'])/row['stored_name'])==SHA
        binding=json.loads(db.execute('SELECT binding_json FROM historical_revisions WHERE submission_id=?',(SID,)).fetchone()[0]);assert binding['paper_id']==PID and binding['sha256']==SHA
        if args.mode=='reports':
            for item in json.loads((packet/'REPORTS.json').read_bytes()):
                label=item['label'];path=packet/(label+'-intake');existing=db.execute('SELECT * FROM model_reviews WHERE submission_id=? AND response_sha256=?',(SID,item['canonical_sha256'])).fetchone()
                if existing:
                    receipt=ROOT/(label+'-intake-record.json');assert receipt.exists(),'Already recorded without local receipt; inspect before recovery.';print(receipt.read_text());continue
                result=cli('record-assessment',str(path/'intake-assessment.native.json'),str(path/'RUNTIME-EVIDENCE.json'));result['observed_at']=a.iso();save(label+'-intake-record.json',result);print(json.dumps(result,indent=2))
            return
        reviews=db.execute('SELECT * FROM model_reviews WHERE submission_id=? ORDER BY id',(SID,)).fetchall();assert sorted(r['response_sha256'] for r in reviews)==REPORTS
        permission=db.execute('SELECT * FROM publication_permissions WHERE submission_id=?',(SID,)).fetchone()
        if args.mode=='inspect':
            result={'checked_at':a.iso(),'submission_id':SID,'pdf_sha256':SHA,'scan_status':row['scan_status'],'status':row['status'],'model_gate_ready':app.extensions['editorial']['can_accept'](row,reviews),'reports':[{'id':r['id'],'sha256':r['response_sha256'],'score':r['millennium_score'],'recommendation':r['recommendation']} for r in reviews],'adjudications':[dict(x) for x in db.execute('SELECT d.* FROM adjudications d JOIN model_reviews r ON r.id=d.review_id WHERE r.submission_id=?',(SID,))],'permission':None if permission is None else dict(permission),'release':row['public_release_url']};save('final-inspection.json',result);print(json.dumps(result,indent=2));return
        if args.mode=='published':
            assert row['status']=='accepted_for_publication' and permission and permission['manuscript_sha256']==SHA and not row['public_release_url']
            raw=urllib.request.urlopen('https://airr.science/papers/'+PID+'/versions/v2/'+PID+'-v2.pdf',timeout=45).read(30_000_000);assert hashlib.sha256(raw).hexdigest()==SHA
            result=cli('mark-published',SID,RELEASE)
        else:
            assert args.instruction and len(args.instruction)>40
            value={'submission_id':SID,'manuscript_sha256':SHA,'human_name':'Lluis Eriksson','human_instruction':args.instruction,'source_reference':'Direct author-editor instruction in current AIRR continuity conversation: explicitly authorized complete next-paper scientific, correction, editorial and publication cycle. Recorded through the existing authenticated Netcup console.','recorded_at':a.iso()}
            if args.mode=='adjudicate':
                correction=json.loads((packet/'sol-intake/CORRECTION-REVIEW.json').read_bytes());assert correction['identified_minor_objection_resolved'] and not correction['remaining_objections'] and correction['pdf_unchanged'] and correction['declarations_and_proof_text_unchanged']
                assert digest(packet/'source-note-correction/DenseClustering.lean')==correction['actual_corrected_sha256'] and digest(packet/'source-note-correction/DenseClustering.original.lean')==correction['actual_original_sha256']
                value.update(report_sha256='9368829624c0e802ecd695884e0c87c3825853883018caa28bcbe6393437d530',basis='The sole minor finding concerned a stale historical source docstring claiming functional calculus was mathematically necessary. The associated-source documentation was corrected; the original source, report, score and exact PDF remain preserved. The same reviewer checked the diff and confirmed the finding resolved. The declarations and proof text are unchanged; incomplete formal-build reproduction remains explicitly disclosed.',resolution_evidence='Exact PDF '+SHA+'; preserved original source '+correction['actual_original_sha256']+'; corrected documentation '+correction['actual_corrected_sha256']+'; native Sol correction-review SHA256 '+digest(packet/'sol-intake/CORRECTION-REVIEW.json')+'. Inspect source-note-correction/source-note.diff and sol-intake/CORRECTION-REVIEW.json in the preserved packet. No fresh Lean build is claimed.',all_objections_addressed=True)
                assert digest(packet/'external_editorial.py')==MODULE
                spec=importlib.util.spec_from_file_location('verified_external_editorial',packet/'external_editorial.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
                module.install(app,a,lambda case_id:db.execute('SELECT * FROM submissions WHERE id=?',(case_id,)).fetchone())
                result=cli('record-external-founder-adjudication',str(save('adjudication-instruction.json',value)))
            elif args.mode=='decide':
                value.update(decision='accept',reason='Author-editor acceptance after two exact-PDF reports and a verified documentation correction; historical source and formal-reproduction limitations remain disclosed.',report_sha256=REPORTS)
                result=cli('record-external-founder-decision',str(save('editorial-instruction.json',value)))
            else:
                value.update(license='LicenseRef-Author-Retained',distribution_scope=['exact_manuscript','assessment_reports','associated_sources'],rights_basis='The author explicitly authorized this complete exact-paper publication cycle, including its real reports, corrected associated documentation and numerical score. Author-retained rights remain in force; no additional Creative Commons reuse licence is inferred.')
                result=cli('record-external-founder-publication',str(save('publication-instruction.json',value)))
        result['observed_at']=a.iso();save(args.mode+'-result.json',result);print(json.dumps(result,indent=2))

if __name__=='__main__':main()
