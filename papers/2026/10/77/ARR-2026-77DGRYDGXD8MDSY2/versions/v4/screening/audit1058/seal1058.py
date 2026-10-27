"""Seal only this audit and archive an identical copy; never modify inputs."""
from pathlib import Path
import json,hashlib,datetime,shutil
P=Path(__file__).resolve().parent
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_bell-allnoise1058-audit')
assert P==Path(r'C:\Trabajo\airr\2026-10-27_bell-allnoise1058-audit')
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def read(name):return json.loads((P/name).read_text(encoding='utf-8'))
def write(name,obj):(P/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
for f in P.rglob('*.json'):json.loads(f.read_text(encoding='utf-8'))
before=read('INPUT_VERIFIED1058.json');after=read('INPUT_FINAL1058.json')
assert all(before[k]==after[k] for k in ['manifest_sha256','files','unlisted'])
assert read('REPLAY1058.json')['fields_equal_except_utc']
assert read('CONTROLS1058.json')['records'][-1]['passed']
assert len(read('BELL_CONTROLS1058.json')['cases'])==4
cert=read('INTEGER_INTERVAL1058.json');assert cert['both_positive_gaps'] and len(cert['cases'])==2
assert all(int(r['gap']['lo_integer'])>0 and all(r['inside_original_binary_intervals'].values()) for r in cert['cases'])
for row in read('CONTROL_INDEX1058.json')['runs']:
 for f in [row['script']]+row['outputs']+row.get('failure_preserved',[]):assert (P/f).is_file(),f
for row in read('INCIDENTS1058.json')['incidents']:
 for f in row.get('preserved',[])+row.get('receipts',[]):assert (P/f).is_file(),f
write('QUALITY1058.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'all_JSON_parse':True,'indexed_outputs_exist':True,'input_before_after_identical':True,'replay_match_except_utc':True,'own_controls_complete':True,'two_integer_certificates_strictly_positive_and_inside_original':True,'initial_failure_preserved':True,'scope':'Artifact consistency and evidence closure; not a universal mathematical proof.'})
exclude={'MANIFEST1058.json','SHA256SUMS1058.txt','DELIVERY1058.json'}
files=[]
for f in sorted(P.rglob('*')):
 if f.is_file() and f.name not in exclude:
  assert not f.is_symlink();files.append({'path':f.relative_to(P).as_posix(),'bytes':f.stat().st_size,'sha256':sha(f)})
manifest={'audit':'1058','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Own audit of1057; immutable originals, no foreign corpus.','C':str(P),'D':str(D),'payload_count':len(files),'excluded_closure_files':sorted(exclude),'files':files,'closure':'SHA256SUMS includes payloads and manifest. DELIVERY records manifest and sums hashes, then is copied and verified separately. No self-referential hash.'}
write('MANIFEST1058.json',manifest)
checks=[(f['path'],f['sha256']) for f in files]+[('MANIFEST1058.json',sha(P/'MANIFEST1058.json'))]
(P/'SHA256SUMS1058.txt').write_text(''.join(h+'  '+name+'\n' for name,h in sorted(checks)),encoding='utf-8')
D.mkdir(parents=True,exist_ok=True)
# Any preexisting divergent artifact aborts; nothing is removed or silently overwritten.
for f in sorted(P.rglob('*')):
 if f.is_file() and f.name!='DELIVERY1058.json':
  rel=f.relative_to(P);dest=D/rel
  if dest.exists():assert dest.read_bytes()==f.read_bytes(),str(dest)
  else:dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,dest)
for name,h in checks:assert sha(D/name)==h
assert (P/'SHA256SUMS1058.txt').read_bytes()==(D/'SHA256SUMS1058.txt').read_bytes()
delivery={'audit':'1058','C':str(P),'D':str(D),'payloads_and_manifest_and_sums_verified_C_D':True,'total_file_count_including_this_receipt':len(files)+3,'report_sha256':sha(P/'AUDIT1058.txt'),'verdict_sha256':sha(P/'verdict1058.json'),'manifest_sha256':sha(P/'MANIFEST1058.json'),'sha256sums_sha256':sha(P/'SHA256SUMS1058.txt'),'input_manifest_sha256':after['manifest_sha256'],'immutable_input_verified_before_and_after':True,'scope_note':'Requested Astra xhigh; effective identity/effort and independence unattested; shared prior context. No score or manuscript evaluation.'}
write('DELIVERY1058.json',delivery)
target=D/'DELIVERY1058.json'
if target.exists():assert target.read_bytes()==(P/'DELIVERY1058.json').read_bytes()
else:shutil.copy2(P/'DELIVERY1058.json',target)
left={f.relative_to(P).as_posix():sha(f) for f in P.rglob('*') if f.is_file()}
right={f.relative_to(D).as_posix():sha(f) for f in D.rglob('*') if f.is_file()}
assert left==right and len(left)==len(files)+3
print(json.dumps({**delivery,'all_files_C_D_identical':True,'total_bytes':sum(f.stat().st_size for f in P.rglob('*') if f.is_file()),'delivery_sha256':sha(P/'DELIVERY1058.json')},indent=2))
