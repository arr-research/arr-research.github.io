from pathlib import Path
import json,hashlib,shutil,datetime,subprocess,sys
P=Path(__file__).resolve().parent
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_binary1077-audit')
assert P==Path(r'C:\Trabajo\airr\2026-10-27_binary1077-audit')
assert not D.exists(), 'Archive already exists; never overwrite a sealed delivery.'
assert not (P/'MANIFEST1077.json').exists(), 'Already sealed.'
def load(n): return json.loads((P/n).read_text(encoding='utf-8'))
def digest(f): return hashlib.sha256(f.read_bytes()).hexdigest()
def write(n,v): (P/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
r=subprocess.run([sys.executable,str(P/'verify1077.py'),'after'],capture_output=True,text=True,encoding='utf-8')
assert r.returncode==0,r.stderr
before=load('INPUT_VERIFIED1077.json');after=load('INPUT_FINAL1077.json')
assert before['external_manifest_hashes_verified'] and after['external_manifest_hashes_verified']
assert before['packages']==after['packages']
replay=load('REPLAY1077.json')['runs'];assert len(replay)==2
assert all(x['exit']==0 and x['fields_identical_except_utc'] for x in replay)
assert load('SYMBOLIC1077.json')['passed']
a=load('AMBIENT1077.json')['cases'];assert len(a)==4
assert all(x['projector_eigenvector_construction'] and x['complement_mass_exact'] for x in a)
assert all(float(x['negative_affine_binary_transition_entry'])<0 for x in a)
i=load('INTERVAL1077.json');rows=i['cases'];assert len(rows)==57
assert i['original_cases_contained']==36 and len(i['original_adverse'])==12
assert all(x['strict_finite_DPI'] for x in rows)
original=[x for x in rows if x['family']=='original'];assert len(original)==36
assert all(all(x['contained_in_original'].values()) for x in original)
assert sum(x['negative'] for x in original)==12
for run in load('CONTROL_INDEX1077.json')['runs']:
 for f in [run['script']]+run['outputs']+run.get('dependencies',[]): assert (P/f).is_file(),f
for f in P.rglob('*.json'): json.loads(f.read_text(encoding='utf-8'))
write('QUALITY1077.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'input_before_after_identical':True,'input_C_D_identical':True,'replays_matching':2,'symbolic_passed':True,'own_full_ambient_cases':4,'integer_interval_cases':57,'original_cases_contained':36,'original_adverses_preserved':12,'strict_finite_DPI_all_cases':True,'all_control_references_resolve':True,'all_JSON_parsed':True,'limits':'Finite controls supplement algebraic/asymptotic arguments; no numerical proof of universal optimality or priority.'})
excluded={'MANIFEST1077.json','SHA256SUMS1077.txt','DELIVERY1077.json'}
files=sorted(f for f in P.rglob('*') if f.is_file() and f.name not in excluded)
payloads=[{'path':f.relative_to(P).as_posix(),'bytes':f.stat().st_size,'sha256':digest(f)} for f in files]
write('MANIFEST1077.json',{'audit':'1077','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Incremental technical audit of frozen1070/1073, no manuscript or grade. Shared context and filesystem; effective identity and independence unattested.','inputs':[{'id':x['id'],'manifest_sha256':x['manifest_sha256']} for x in before['packages']],'payloads':payloads,'exclusions':sorted(excluded),'reason':'No self-referential manifest hash; SHA256SUMS adds manifest, DELIVERY records final hashes and copy verification.'})
covered=files+[P/'MANIFEST1077.json']
(P/'SHA256SUMS1077.txt').write_text(''.join(digest(f)+'  '+f.relative_to(P).as_posix()+'\n' for f in sorted(covered)),encoding='utf-8')
D.mkdir(parents=False,exist_ok=False)
for f in sorted(P.rglob('*')):
 if f.is_file():
  target=D/f.relative_to(P);target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,target);assert digest(f)==digest(target)
keyhashes={n:digest(P/n) for n in ['AUDIT1077.txt','verdict1077.json','MANIFEST1077.json','SHA256SUMS1077.txt']}
write('DELIVERY1077.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'C':str(P),'D':str(D),'key_sha256':keyhashes,'input_hashes':[{'id':x['id'],'manifest_sha256':x['manifest_sha256']} for x in before['packages']],'identical_copy_verified':True,'total_files_including_delivery':sum(f.is_file() for f in P.rglob('*'))+1,'context_reused':True,'effective_identity_effort_independence_unattested':True})
shutil.copy2(P/'DELIVERY1077.json',D/'DELIVERY1077.json')
def inventory(root):return {f.relative_to(root).as_posix():digest(f) for f in root.rglob('*') if f.is_file()}
assert inventory(P)==inventory(D)
assert len(inventory(P))==load('DELIVERY1077.json')['total_files_including_delivery']
print(json.dumps({'files':len(inventory(P)),'bytes':sum(f.stat().st_size for f in P.rglob('*') if f.is_file()),'C_D_identical':True,'key_sha256':keyhashes},indent=2))
