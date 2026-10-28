from pathlib import Path
import json,hashlib,shutil,datetime
C=Path(r'C:\Trabajo\airr\2026-10-27_simplex1100-audit').resolve()
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_simplex1100-audit').resolve()
assert str(C)==r'C:\Trabajo\airr\2026-10-27_simplex1100-audit'
assert str(D)==r'D:\Proyectos\airr-investigacion\2026-10-27_simplex1100-audit'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def inventory(root):return {p.relative_to(root).as_posix():(p.stat().st_size,sha(p)) for p in root.rglob('*') if p.is_file()}
def checkinputs():
 receipt=json.loads((C/'INPUT_FINAL1100.json').read_text(encoding='utf-8'))
 for package in receipt['packages']:
  a,b=Path(package['C']),Path(package['D']);mf='MANIFEST'+package['id']+'.json'
  assert sha(a/mf)==sha(b/mf)==package['manifest_sha256']
  for row in package['files']:
   assert sha(a/row['path'])==sha(b/row['path'])==row['sha256']
  assert sorted(p.name for p in a.iterdir())==sorted(p.name for p in b.iterdir())==sorted([mf]+[row['path'] for row in package['files']])
checkinputs()
assert not D.exists(),'Refuse overwrite existingarchive'
excluded=['MANIFEST1100.json','SHA256SUMS1100.txt','CLOSURE1100.json']
files=[dict(path=k,bytes=v[0],sha256=v[1]) for k,v in sorted(inventory(C).items()) if k not in excluded]
mf={'task':'1100','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'payloads':len(files),'files':files,'excluded_metadata':excluded,'reason':'Manifest cannot hash itself; SHA256SUMS hashes manifest and payloads; closure records preclosure inventory and is checked identically on C/D after writing.','input_final_verification':'INPUT_FINAL1100.json'}
(C/'MANIFEST1100.json').write_text(json.dumps(mf,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
inv=inventory(C)
(C/'SHA256SUMS1100.txt').write_text(''.join(v[1]+'  '+k+'\n' for k,v in sorted(inv.items()) if k not in ['SHA256SUMS1100.txt','CLOSURE1100.json']),encoding='utf-8')
D.mkdir()
for p in C.rglob('*'):
 if p.is_file():
  dest=D/p.relative_to(C);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
before=inventory(C);assert before==inventory(D)
closure={'task':'1100','C':str(C),'D':str(D),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'preclosure_files':len(before),'final_files_including_this_receipt':len(before)+1,'all_preclosure_inventory_and_bytes_identical':True,'manifest_sha256':sha(C/'MANIFEST1100.json'),'report_sha256':sha(C/'AUDIT1100.txt'),'verdict_sha256':sha(C/'verdict1100.json'),'sha256sums_sha256':sha(C/'SHA256SUMS1100.txt'),'input_packages_unchanged_verified_again':True,'terminal_protocol':'After writing identical receipt bytes, archive1100.py asserts full recursive inventory and bytehash equality includingthisreceipt, thenrechecksallinputs and manifestpayloads before printing TERMINAL. No finalclaim beforethoseassertions.'}
raw=(json.dumps(closure,indent=2,ensure_ascii=False)+'\n').encode()
(C/'CLOSURE1100.json').write_bytes(raw);(D/'CLOSURE1100.json').write_bytes(raw)
final=inventory(C);assert final==inventory(D)
assert len(final)==len(before)+1
for row in files:assert final[row['path']]==(row['bytes'],row['sha256'])
checkinputs()
print(json.dumps({'status':'TERMINAL_VERIFIED','files':len(final),'bytes':sum(v[0] for v in final.values()),'manifest_payloads':len(files),'AUDIT1100_sha256':sha(C/'AUDIT1100.txt'),'verdict1100_sha256':sha(C/'verdict1100.json'),'MANIFEST1100_sha256':sha(C/'MANIFEST1100.json'),'SHA256SUMS1100_sha256':sha(C/'SHA256SUMS1100.txt'),'CLOSURE1100_sha256':sha(C/'CLOSURE1100.json'),'C_D_identical':True,'inputs_unchanged':True}))
