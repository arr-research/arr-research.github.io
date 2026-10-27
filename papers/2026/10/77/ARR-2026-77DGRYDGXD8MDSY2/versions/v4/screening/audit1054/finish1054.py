from pathlib import Path
import json,hashlib,shutil,datetime
P=Path(__file__).resolve().parent;D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_local-phase1054-audit')
assert P==Path(r'C:\Trabajo\airr\2026-10-27_local-phase1054-audit')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
before=json.loads((P/'INPUT_VERIFIED1054.json').read_text());after=json.loads((P/'INPUT_FINAL1054.json').read_text());assert before['all_passed'] and after['all_passed'] and after['phase']=='after';assert before['packages']==after['packages']
assert sum(len(x['files']) for x in after['packages'])==15
for f in P.rglob('*.json'):json.loads(f.read_text(encoding='utf-8'))
assert json.loads((P/'OWN1054.json').read_text())['records'][-1]['passed']
assert json.loads((P/'BELL1054.json').read_text())['all_passed']
assert all(x['exit']==0 and x['all_payload_fields_except_utc_equal'] for x in json.loads((P/'REPLAY1054.json').read_text()))
iv=json.loads((P/'INTEGER_INTERVAL1054.json').read_text());assert len(iv['cases'])==4 and all(int(x['gap']['lo_integer'])>0 and all(x['inside_original_binary_intervals'].values()) for x in iv['cases'])
from fractions import Fraction
assert Fraction(json.loads((P/'FALSIFIER1054.json').read_text())['positive_difference']['rational_endpoints'][0])>0
assert len(json.loads((P/'ADVERSE1054.json').read_text())['preserved_not_above_rows'])==14
assert (P/'OWN_FAILURE1054-first.json').exists() and (P/'OWN_FAILURE1054-second.json').exists()
exclude={'MANIFEST1054.json','SHA256SUMS1054.txt','DELIVERY1054.json'}
rows=[{'path':f.relative_to(P).as_posix(),'bytes':f.stat().st_size,'sha256':sha(f)} for f in sorted(P.rglob('*')) if f.is_file() and f.name not in exclude]
put(P/'MANIFEST1054.json',{'audit':'1054','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'algorithm':'SHA256','files':rows,'self_reference_exclusions':sorted(exclude),'errors_and_adverse_results_retained':True,'copy_receipt':'DELIVERY1054.json'})
with_manifest=rows+[{'path':'MANIFEST1054.json','sha256':sha(P/'MANIFEST1054.json')}]
(P/'SHA256SUMS1054.txt').write_text(''.join(x['sha256']+'  '+x['path']+'\n' for x in sorted(with_manifest,key=lambda x:x['path'])),encoding='utf-8')
D.mkdir(parents=True,exist_ok=True)
for f in sorted(P.rglob('*')):
 if not f.is_file() or f.name=='DELIVERY1054.json':continue
 target=D/f.relative_to(P);assert target.resolve().is_relative_to(D.resolve());target.parent.mkdir(parents=True,exist_ok=True)
 if target.exists():assert target.read_bytes()==f.read_bytes(),str(target)
 else:shutil.copyfile(f,target)
cs={f.relative_to(P).as_posix() for f in P.rglob('*') if f.is_file() and f.name!='DELIVERY1054.json'};ds={f.relative_to(D).as_posix() for f in D.rglob('*') if f.is_file() and f.name!='DELIVERY1054.json'};assert cs==ds and all(sha(P/f)==sha(D/f) for f in cs)
receipt={'audit':'1054','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'C':str(P),'D':str(D),'payload_count':len(rows),'file_count_including_receipt':len(cs)+1,'identical_audit_filesets_and_bytes':True,'manifest_sha256':sha(P/'MANIFEST1054.json'),'report_sha256':sha(P/'AUDIT1054.txt'),'verdict_sha256':sha(P/'verdict1054.json'),'sums_sha256':sha(P/'SHA256SUMS1054.txt'),'input17_manifest_files_verified_before_after':True,'input_C_only_unlisted_sealers_unchanged':True,'receipt_self_hash_excluded':True}
put(P/'DELIVERY1054.json',receipt)
target=D/'DELIVERY1054.json'
if target.exists():assert target.read_bytes()==(P/'DELIVERY1054.json').read_bytes()
else:shutil.copyfile(P/'DELIVERY1054.json',target)
cs={f.relative_to(P).as_posix() for f in P.rglob('*') if f.is_file()};ds={f.relative_to(D).as_posix() for f in D.rglob('*') if f.is_file()};assert cs==ds and len(cs)==receipt['file_count_including_receipt'] and all(sha(P/f)==sha(D/f) for f in cs)
print(json.dumps({**receipt,'delivery_sha256':sha(target),'total_bytes':sum((P/f).stat().st_size for f in cs)},indent=2,ensure_ascii=False))
