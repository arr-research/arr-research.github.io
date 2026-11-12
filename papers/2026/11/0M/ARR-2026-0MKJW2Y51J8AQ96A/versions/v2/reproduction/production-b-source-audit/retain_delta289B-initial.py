"""Metadata-only exact-byte delta/capture; never runs reviewed scripts."""
from pathlib import Path
import json,hashlib,shutil,difflib,subprocess
W=Path(r'C:\Trabajo\the-eriksson-programme\solenoidal-layers275-20261112');A=W/'_tmp/production289-a';B=W/'_tmp/production289-b'
E=Path(r'D:\Datos\the-eriksson-programme\autonomia\evidencia-289');D=E/'production-b-source-audit';P=W/'papers/checkerboard-response';S='446124a566483e6f1a8d499d801ce60e0abbb9d8'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v):
    with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(v,f,indent=2);f.write('\n')
def cp(p,q):q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
rules=[('9fb521efe3f758bd8c1a1cb22b76161c91d51fbc',S),('90236127708dfc87bb553258a78299497e2e1112d4332126af8df5a29b36980b','579369eeb2940850a22265680e996ba97403d4523b95201f65bc69d79b605668'),('43315800ff2f76a0fb62b983b52bcc604007d8d7ad53223c64526b35a2b687fb','0c2afa8d1f889586df4530bf5819df5db5236a83cdbc0a22adeebbedd76bd1f4'),('manuscript289A','manuscript289B'),('source-map289A','source-map289B'),('tep289-build-a','tep289-build-b'),('production289-a','production289-b'),('production-a','production-b'),('attempt-a','attempt-b')]
result={'source':S,'allowed_rules':rules,'files':[]};C=D/'captures';C.mkdir(exist_ok=False)
for row in json.loads((B/'RUNNER-HASHES.json').read_bytes()):
    name=row['path'];a=(A/name).read_bytes();b=(B/name).read_bytes();pred=a
    for x,y in rules:pred=pred.replace(x.encode(),y.encode())
    if pred!=b or len(b)!=row['bytes'] or sha(B/name)!=row['sha256'] or b!=(E/'production-b'/name).read_bytes():raise ValueError('Exact delta/pin/mirror differs')
    cp(A/name,C/'A'/name);cp(B/name,C/'B'/name)
    diff=''.join(difflib.unified_diff(a.decode().splitlines(True),b.decode().splitlines(True),fromfile='A/'+name,tofile='B/'+name))
    with (C/('full-'+name+'.diff')).open('x',encoding='utf-8',newline='\n') as f:f.write(diff)
    result['files'].append({'path':name,'bytes':len(b),'sha256':sha(B/name),'exact_allowed_delta':True,'D_mirror_equal':True,'unchanged':a==b})
for folder,label in [(A,'A'),(B,'B')]:cp(folder/'RUNNER-HASHES.json',C/label/'RUNNER-HASHES.json')
if sha(B/'RUNNER-HASHES.json')!='a22e13ff799cbe532d2fe6fa322ecca914d2145f374e212e96ad6661fae0fcfb':raise ValueError('B manifest raw differs')
if (B/'RUNNER-HASHES.json').read_bytes()!=(E/'production-b/RUNNER-HASHES.json').read_bytes():raise ValueError('B manifest mirror differs')
shutil.copytree(E/'production-a-source-audit',D/'prior-complete-A-audit')
result['source_bindings']=[]
for n in ['manuscript289B.tex','source-map289B.json','SOURCE-INPUTS.json']:
    p=P/n;blob=subprocess.check_output(['git','-C',str(W),'show',S+':papers/checkerboard-response/'+n]);cp(p,C/'source'/n)
    if p.read_bytes()!=blob:raise ValueError('Frozen Git blob differs')
    result['source_bindings'].append({'path':n,'bytes':p.stat().st_size,'sha256':sha(p),'exact_frozen_Git_blob':True})
ma=json.loads((P/'source-map289A.json').read_bytes());mb=json.loads((P/'source-map289B.json').read_bytes())
if ma['accepted_sources']!=mb['accepted_sources'] or len(mb['accepted_sources'])!=8:raise ValueError('Mapped source delta')
for key,r in mb['accepted_sources'].items():
    p=P/r['path'];cp(p,C/'mapped'/r['path'])
    if p.stat().st_size!=r['bytes'] or sha(p)!=r['sha256']:raise ValueError('Mapped raw source differs')
inputs=json.loads((P/'SOURCE-INPUTS.json').read_bytes())['files']
for r in inputs:
    p=P/r['path']
    if p.stat().st_size!=r['bytes'] or sha(p)!=r['raw_sha256']:raise ValueError('Frozen input differs')
result.update(eight_mapped_sources_unchanged=True,all_mapped_sizes_hashes_match=True,frozen_input_count=len(inputs),all_frozen_inputs_match=True,actual_local_HEAD=subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD']).decode().strip(),B_relay_present=(B/'parent-authority-relay.json').exists(),B_attempt_present=(E/'production-b/attempt-b').exists(),reviewed_code_executed=False,runtime_inspected=False)
dump(D/'delta-and-subject-verification.json',result)
rows=[{'path':p.relative_to(D).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(D.rglob('*')) if p.is_file() and p.name!='raw-hashmanifest.json']
dump(D/'raw-hashmanifest.json',{'files':rows,'manifest_excludes_itself':True})
print(json.dumps({'full_report_sha256':sha(D/'full-report.txt'),'context_sha256':sha(D/'context.txt'),'raw_manifest_sha256':sha(D/'raw-hashmanifest.json'),'raw_members':len(rows),'A_report_sha256':sha(D/'prior-complete-A-audit/full-report.txt')},indent=2))
