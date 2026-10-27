from pathlib import Path
import json,hashlib,shutil,datetime
P=Path(__file__).resolve().parent
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_principal1044-audit')
assert P==Path(r'C:\Trabajo\airr\2026-10-27_principal1044-audit')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
final=json.loads((P/'INPUT_FINAL1044.json').read_text(encoding='utf-8'))
assert final['all_passed'] and final['phase']=='after'
assert sum(len(x['files']) for x in final['packages'])==21
assert not any(x['unlisted'] for x in final['packages'])
# Validate output JSON and the essential conclusions before sealing.
for f in P.rglob('*.json'):json.loads(f.read_text(encoding='utf-8'))
assert all(x['exit']==0 and x['output_byte_identical'] and x['output_json_identical'] for x in json.loads((P/'REPLAY1044.json').read_text()))
iv=json.loads((P/'INTEGER_INTERVAL1044.json').read_text())
assert len(iv['cases'])==4 and all(int(x['positive_gap']['lower_integer'])>0 and all(x['own_enclosures_inside_original_binary_intervals'].values()) for x in iv['cases'])
assert json.loads((P/'FULLMATRIX1044.json').read_text())['records'][-1]['passed']
excluded={'MANIFEST1044.json','SHA256SUMS1044.txt','DELIVERY1044.json'}
rows=[{'path':f.relative_to(P).as_posix(),'bytes':f.stat().st_size,'sha256':sha(f)} for f in sorted(P.rglob('*')) if f.is_file() and f.name not in excluded]
assert not any('FAILURE' in x['path'] for x in rows)
write(P/'MANIFEST1044.json',{'audit':'1044','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'algorithm':'SHA256','files':rows,'self_reference_exclusions':sorted(excluded),'input_verification':'INPUT_VERIFIED1044.json and INPUT_FINAL1044.json','copy_receipt':'DELIVERY1044.json'})
with_manifest=rows+[{'path':'MANIFEST1044.json','sha256':sha(P/'MANIFEST1044.json')}]
(P/'SHA256SUMS1044.txt').write_text(''.join(x['sha256']+'  '+x['path']+'\n' for x in sorted(with_manifest,key=lambda x:x['path'])),encoding='utf-8')
D.mkdir(parents=True,exist_ok=True)
for f in sorted(P.rglob('*')):
 if not f.is_file() or f.name=='DELIVERY1044.json':continue
 target=D/f.relative_to(P)
 assert target.resolve().is_relative_to(D.resolve())
 target.parent.mkdir(parents=True,exist_ok=True)
 if target.exists():assert target.read_bytes()==f.read_bytes(),str(target)
 else:shutil.copyfile(f,target)
files_c={f.relative_to(P).as_posix() for f in P.rglob('*') if f.is_file() and f.name!='DELIVERY1044.json'}
files_d={f.relative_to(D).as_posix() for f in D.rglob('*') if f.is_file() and f.name!='DELIVERY1044.json'}
assert files_c==files_d
for rel in files_c:assert (P/rel).read_bytes()==(D/rel).read_bytes()
receipt={'audit':'1044','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'C':str(P),'D':str(D),'payload_count':len(rows),'file_count_including_this_receipt':len(files_c)+1,'identical_filesets_and_bytes':True,'manifest_sha256':sha(P/'MANIFEST1044.json'),'report_sha256':sha(P/'AUDIT1044.txt'),'verdict_sha256':sha(P/'verdict1044.json'),'sums_sha256':sha(P/'SHA256SUMS1044.txt'),'inputs_C_D_verified_before_and_after':True,'receipt_self_hash_excluded':True}
write(P/'DELIVERY1044.json',receipt)
target=D/'DELIVERY1044.json'
if target.exists():assert target.read_bytes()==(P/'DELIVERY1044.json').read_bytes()
else:shutil.copyfile(P/'DELIVERY1044.json',target)
assert sha(P/'DELIVERY1044.json')==sha(target)
files_c={f.relative_to(P).as_posix() for f in P.rglob('*') if f.is_file()}
files_d={f.relative_to(D).as_posix() for f in D.rglob('*') if f.is_file()}
assert files_c==files_d and len(files_c)==receipt['file_count_including_this_receipt']
assert all(sha(P/rel)==sha(D/rel) for rel in files_c)
print(json.dumps({**receipt,'delivery_sha256':sha(P/'DELIVERY1044.json'),'total_bytes':sum((P/rel).stat().st_size for rel in files_c)},ensure_ascii=False,indent=2))
