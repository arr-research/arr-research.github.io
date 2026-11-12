"""Metadata-only audit-packet writer: captures/hashes/local Git blobs only."""
from pathlib import Path
import hashlib,json,subprocess,shutil
W=Path(r'C:\Trabajo\the-eriksson-programme\solenoidal-layers275-20261112')
P=W/'_tmp/production289-a';M=Path(r'D:\Datos\the-eriksson-programme\autonomia\evidencia-289\production-a')
D=M.with_name('production-a-source-audit');S='9fb521efe3f758bd8c1a1cb22b76161c91d51fbc';paper=W/'papers/checkerboard-response'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v):
    with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(v,f,indent=2);f.write('\n')
C=D/'captures';C.mkdir(exist_ok=False);bindings=[]
def capture(src,rel):
    target=C/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,target)
    if src.read_bytes()!=target.read_bytes():raise ValueError('Raw capture differs')
    row={'origin':str(src),'capture':target.relative_to(D).as_posix(),'bytes':src.stat().st_size,'sha256':sha(src)};bindings.append(row);return row
operative=[]
for row in json.loads((P/'RUNNER-HASHES.json').read_bytes()):
    p=P/row['path'];m=M/row['path'];observed=capture(p,Path('runner')/row['path'])
    if observed['bytes']!=row['bytes'] or observed['sha256']!=row['sha256'] or p.read_bytes()!=m.read_bytes():raise ValueError('Frozen runner/mirror changed')
    operative.append(observed)
capture(P/'RUNNER-HASHES.json',Path('runner/RUNNER-HASHES.json'))
if sha(P/'RUNNER-HASHES.json')!='b0a97fd001710d1eb5c3d60790ce47449d1b299ecc7aed9e045369de822351ad' or (P/'RUNNER-HASHES.json').read_bytes()!=(M/'RUNNER-HASHES.json').read_bytes():raise ValueError('Raw manifest changed')
main=[]
for name in ['manuscript289A.tex','source-map289A.json','SOURCE-INPUTS.json','.gitattributes']:
    p=paper/name;row=capture(p,Path('source')/name)
    blob=subprocess.check_output(['git','-C',str(W),'show',S+':papers/checkerboard-response/'+name])
    if p.read_bytes()!=blob:raise ValueError('Frozen Git subject differs '+name)
    row['exact_frozen_Git_blob']=True;main.append(row)
inputs=[]
for r in json.loads((paper/'SOURCE-INPUTS.json').read_bytes())['files']:
    p=paper/r['path'];row=capture(p,Path('frozen-inputs')/r['path'])
    if row['bytes']!=r['bytes'] or row['sha256']!=r['raw_sha256']:raise ValueError('Frozen input differs')
    inputs.append(row)
mapped=[]
for key,r in json.loads((paper/'source-map289A.json').read_bytes())['accepted_sources'].items():
    p=paper/r['path'];row=capture(p,Path('mapped')/r['path']);row['key']=key
    blob=subprocess.check_output(['git','-C',str(W),'show',S+':papers/checkerboard-response/'+r['path']])
    if row['bytes']!=r['bytes'] or row['sha256']!=r['sha256'] or p.read_bytes()!=blob:raise ValueError('Mapped source differs')
    row['exact_frozen_Git_blob']=True;mapped.append(row)
capture(W/'docs/OPERATIONAL-GOVERNANCE-CHARTER.md',Path('governance/OPERATIONAL-GOVERNANCE-CHARTER.md'))
dump(D/'subject-verification.json',{'source':S,'actual_local_HEAD':subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD']).decode().strip(),'runner_manifest_sha256':sha(P/'RUNNER-HASHES.json'),'operative':operative,'main':main,'frozen_input_count':len(inputs),'frozen_inputs':inputs,'mapped_source_count':len(mapped),'mapped_sources':mapped,'gate_relay_present_at_final_capture':(P/'parent-authority-relay.json').exists(),'attempt_present_at_final_capture':(M/'attempt-a').exists(),'reviewed_code_executed':False,'runtime_inspected':False})
dump(D/'subject-bindings.json',bindings)
rows=[{'path':p.relative_to(D).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(D.rglob('*')) if p.is_file() and p.name!='raw-hashmanifest.json']
dump(D/'raw-hashmanifest.json',{'files':rows,'manifest_excludes_itself':True})
print(json.dumps({'full_report_sha256':sha(D/'full-report.txt'),'context_sha256':sha(D/'context.txt'),'raw_manifest_sha256':sha(D/'raw-hashmanifest.json'),'raw_members':len(rows),'frozen_input_count':len(inputs),'mapped_source_count':len(mapped)},indent=2))
