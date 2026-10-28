from pathlib import Path
import json,hashlib,datetime,subprocess,sys,shutil
P=Path(__file__).resolve().parent;D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_binary1093-audit')
assert P==Path(r'C:\Trabajo\airr\2026-10-27_binary1093-audit')
assert not D.exists() and not (P/'MANIFEST1093.json').exists(), 'Never overwrite a sealed delivery.'
load=lambda n:json.loads((P/n).read_text(encoding='utf-8'))
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def write(n,v):(P/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
r=subprocess.run([sys.executable,str(P/'verify1093.py'),'final'],capture_output=True,text=True,encoding='utf-8');assert r.returncode==0,r.stderr
b=load('INPUT_INITIAL1093.json');a=load('INPUT_FINAL1093.json')
assert b['files']==a['files'] and b['manifest_sha256']==a['manifest_sha256']
assert a['C_D_identical'] and a['inventory_exact']
replay=load('REPLAY1093.json');assert replay['output_byte_identical'] and replay['script_unchanged'] and replay['controls']==7
exact=load('EXACT1093.json');assert exact['passed'] and len(exact['operator_controls'])==9 and exact['equality_gap_zero']
num=load('BOUNDED1093.json');assert num['operator_checks']==189 and len(num['states'])==27 and not num['violations'] and len(num['POVM_coherent_cases'])==2
fin=load('POVM_FINITE1093.json');assert fin['passed'] and fin['factorization_exact'] and fin['finite_Umegaki_old_guess_falsifier']['gap_certified_positive']
for run in load('CONTROL_INDEX1093.json')['runs']:
 for f in [run['script']]+run['outputs']+run.get('dependencies',[]):assert (P/f).is_file(),f
for f in P.rglob('*.json'):json.loads(f.read_text(encoding='utf-8'))
write('QUALITY1093.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'inputs_initial_final_identical':True,'inputs_C_D_inventory_identical':True,'original_exact_controls_replayed':7,'own_exact_operator_controls':9,'own_bounded_physical_states':27,'own_bounded_full_HS_checks':189,'own_coherent_POVM_cases':2,'own_exact_POVM_factorization_and_regularization':True,'Umegaki_old_guess_falsifier_certified':True,'mathematical_control_failures':0,'reading_incidents_preserved':3,'all_JSON_parse':True,'all_control_references_exist':True,'limitations':'Finitecontrols do not establish universaltheorem; sourceaccessfailures do not establishpriority.'})
excluded={'MANIFEST1093.json','SHA256SUMS1093.txt','DELIVERY1093.json'}
files=sorted(f for f in P.rglob('*') if f.is_file() and f.name not in excluded)
write('MANIFEST1093.json',{'audit':'1093','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'input_manifest_sha256':a['manifest_sha256'],'scope':'Single technicalfalsification audit, sharedcontext andfilesystem, effectiveconfiguration/independence unattested;no manuscript orgrade.','files':[{'path':f.relative_to(P).as_posix(),'bytes':f.stat().st_size,'sha256':sha(f)} for f in files],'exclusions':sorted(excluded),'exclusion_reason':'Avoid self-reference;SHA256SUMScoversmanifest;DELIVERYrecordskeyhashesandfinalcopyverification.'})
(P/'SHA256SUMS1093.txt').write_text(''.join(sha(f)+'  '+f.relative_to(P).as_posix()+'\n' for f in sorted(files+[P/'MANIFEST1093.json'])),encoding='utf-8')
D.mkdir(parents=False,exist_ok=False)
for f in sorted(P.rglob('*')):
 if f.is_file():
  target=D/f.relative_to(P);target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,target);assert sha(f)==sha(target)
hashes={n:sha(P/n) for n in ['AUDIT1093.txt','verdict1093.json','MANIFEST1093.json','SHA256SUMS1093.txt']}
write('DELIVERY1093.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'C':str(P),'D':str(D),'key_sha256':hashes,'input_manifest_sha256':a['manifest_sha256'],'C_D_copy_verified':True,'files_including_delivery':sum(f.is_file() for f in P.rglob('*'))+1,'shared_context':True,'effective_identity_and_independence_unattested':True})
shutil.copy2(P/'DELIVERY1093.json',D/'DELIVERY1093.json')
def inventory(p):return {f.relative_to(p).as_posix():sha(f) for f in p.rglob('*') if f.is_file()}
assert inventory(P)==inventory(D)
assert len(inventory(P))==load('DELIVERY1093.json')['files_including_delivery']
print(json.dumps({'files':len(inventory(P)),'bytes':sum(f.stat().st_size for f in P.rglob('*') if f.is_file()),'C_D_identical':True,'sha256':hashes},indent=2))
