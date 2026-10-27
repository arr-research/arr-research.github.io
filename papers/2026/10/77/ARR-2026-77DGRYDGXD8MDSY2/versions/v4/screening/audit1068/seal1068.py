from pathlib import Path
import json,hashlib,datetime,shutil
P=Path(__file__).resolve().parent;D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_phase-tradeoff1068-audit')
assert P==Path(r'C:\Trabajo\airr\2026-10-27_phase-tradeoff1068-audit')
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def read(n):return json.loads((P/n).read_text(encoding='utf-8'))
def write(n,x):(P/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
for f in P.rglob('*.json'):json.loads(f.read_text(encoding='utf-8'))
before=read('INPUT_VERIFIED1068.json');after=read('INPUT_FINAL1068.json');assert before['packages']==after['packages']
assert len(read('REPLAY1068.json')['runs'])==3 and all(r['fields_identical_except_utc'] for r in read('REPLAY1068.json')['runs'])
assert read('SYMBOLIC1068.json')['passed'];assert len(read('AMBIENT1068.json')['cases'])==7
ic=read('INTERVAL1068.json');assert len(ic['cases'])==57 and ic['source_interval_cases_contained']==40
assert all(all(r['inside_original_intervals'].values()) for r in ic['cases'])
assert ic['adverse_all_1063_controls']==[2,3,4,5,6,7] and len(ic['adverse_original1066'])==9
for row in read('CONTROL_INDEX1068.json')['runs']:
 for f in [row['script']]+row['outputs']+row.get('dependencies',[])+row.get('failure_preserved',[]):assert (P/f).is_file(),f
for row in read('INCIDENTS1068.json')['incidents']:
 for f in row.get('preserved',[]):assert (P/f).is_file(),f
write('QUALITY1068.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'JSON_parse':True,'indexed_outputs_exist':True,'all_inputs_unchanged':True,'three_replays_equal_except_utc':True,'general_symbolics_complete':True,'ambient_cases':7,'integer_cases':57,'original_intervals_contained':40,'adverse1063':[2,3,4,5,6,7],'adverse1066_count':9,'initial_checker_failure_preserved':True,'scope':'Artifact consistency; finite controls are not universal proofs.'})
exclude={'MANIFEST1068.json','SHA256SUMS1068.txt','DELIVERY1068.json'};files=[]
for f in sorted(P.rglob('*')):
 if f.is_file() and f.name not in exclude:
  assert not f.is_symlink();files.append({'path':f.relative_to(P).as_posix(),'bytes':f.stat().st_size,'sha256':sha(f)})
write('MANIFEST1068.json',{'audit':'1068','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'C':str(P),'D':str(D),'payload_count':len(files),'files':files,'excluded_closure_files':sorted(exclude),'closure':'SHA256SUMS covers payloads and manifest. DELIVERY stores their hashes and is separately copied and checked. No self-referential hash.','scope':'Technical audit only, no manuscript score; original inputs unchanged; shared context and unattested independence.'})
checks=[(f['path'],f['sha256']) for f in files]+[('MANIFEST1068.json',sha(P/'MANIFEST1068.json'))]
(P/'SHA256SUMS1068.txt').write_text(''.join(h+'  '+name+'\n' for name,h in sorted(checks)),encoding='utf-8')
D.mkdir(parents=True,exist_ok=True)
for f in sorted(P.rglob('*')):
 if f.is_file() and f.name!='DELIVERY1068.json':
  dest=D/f.relative_to(P)
  if dest.exists():assert dest.read_bytes()==f.read_bytes(),str(dest)
  else:dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,dest)
for name,h in checks:assert sha(D/name)==h
assert (P/'SHA256SUMS1068.txt').read_bytes()==(D/'SHA256SUMS1068.txt').read_bytes()
delivery={'audit':'1068','C':str(P),'D':str(D),'payload_manifest_sums_C_D_verified':True,'total_file_count_including_receipt':len(files)+3,'report_sha256':sha(P/'AUDIT1068.txt'),'verdict_sha256':sha(P/'verdict1068.json'),'manifest_sha256':sha(P/'MANIFEST1068.json'),'sha256sums_sha256':sha(P/'SHA256SUMS1068.txt'),'input_manifests':{x['id']:x['manifest_sha256'] for x in after['packages']},'inputs_verified_before_after':True,'configuration':'RequestedAstraxhigh; effective identity/effort and independence unattested; reusedcontext/sharedfilesystem.','no_manuscript_or_score':True}
write('DELIVERY1068.json',delivery)
if (D/'DELIVERY1068.json').exists():assert (D/'DELIVERY1068.json').read_bytes()==(P/'DELIVERY1068.json').read_bytes()
else:shutil.copy2(P/'DELIVERY1068.json',D/'DELIVERY1068.json')
left={f.relative_to(P).as_posix():sha(f) for f in P.rglob('*') if f.is_file()};right={f.relative_to(D).as_posix():sha(f) for f in D.rglob('*') if f.is_file()}
assert left==right and len(left)==len(files)+3
print(json.dumps({**delivery,'all_files_C_D_identical':True,'total_bytes':sum(f.stat().st_size for f in P.rglob('*') if f.is_file()),'delivery_sha256':sha(P/'DELIVERY1068.json')},indent=2))
