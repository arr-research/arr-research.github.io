"""Own terminal archive protocol, reused1115 lineage, refuses overwrite/reseal."""
from pathlib import Path
import ast,datetime,hashlib,json,shutil
C=Path(r'C:\Trabajo\airr\2026-10-27_support1136-audit').resolve()
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_support1136-audit').resolve()
assert str(C)==r'C:\Trabajo\airr\2026-10-27_support1136-audit'
assert str(D)==r'D:\Proyectos\airr-investigacion\2026-10-27_support1136-audit'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def inventory(root):
 assert not any(p.is_symlink() or p.is_junction() for p in root.rglob('*'))
 return {p.relative_to(root).as_posix():(p.stat().st_size,sha(p)) for p in root.rglob('*') if p.is_file()}
def inputs():
 r=json.loads((C/'INPUT_FINAL1136.json').read_text());a,b=Path(r['C']),Path(r['D']);mf='MANIFEST1134.json'
 assert sha(a/mf)==sha(b/mf)==r['manifest_sha256']
 for row in r['files']:
  assert sha(a/row['path'])==sha(b/row['path'])==row['sha256']
  assert (a/row['path']).stat().st_size==(b/row['path']).stat().st_size==row['bytes']
 expected=sorted([mf]+[v['path'] for v in r['files']])
 assert len(expected)==7
 assert sorted(p.name for p in a.iterdir())==sorted(p.name for p in b.iterdir())==expected
inputs();assert not D.exists(),'Refuse overwrite existing archive'
for p in C.rglob('*.json'):json.loads(p.read_text(encoding='utf-8-sig'))
for p in C.rglob('*.py'):ast.parse(p.read_text(encoding='utf-8-sig'),filename=str(p))
excluded=['MANIFEST1136.json','SHA256SUMS1136.txt','CLOSURE1136.json']
assert not any((C/name).exists() for name in excluded),'Refuse reseal'
files=[dict(path=k,bytes=v[0],sha256=v[1]) for k,v in sorted(inventory(C).items())]
manifest={'task':'1136','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'payloads':len(files),'files':files,'excluded_metadata':excluded,'reason':'Manifest cannot hash itself. SHA256SUMS includes payloads and manifest. Closure is verified byte-identical on C/D after writing.','input_final_verification':'INPUT_FINAL1136.json','configuration':'Requested GPT-6 Astra xhigh; effective identity/effort/independence unattested; shared context/filesystem.'}
(C/'MANIFEST1136.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
inv=inventory(C)
(C/'SHA256SUMS1136.txt').write_text(''.join(v[1]+'  '+k+'\n' for k,v in sorted(inv.items())),encoding='utf-8')
D.mkdir()
for p in C.rglob('*'):
 if p.is_file():
  dest=D/p.relative_to(C);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
before=inventory(C);assert before==inventory(D)
closure={'task':'1136','C':str(C),'D':str(D),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'preclosure_files':len(before),'final_files_including_this_receipt':len(before)+1,'all_preclosure_bytes_and_inventory_identical':True,'manifest_sha256':sha(C/'MANIFEST1136.json'),'report_sha256':sha(C/'AUDIT1136.txt'),'verdict_sha256':sha(C/'verdict1136.json'),'sha256sums_sha256':sha(C/'SHA256SUMS1136.txt'),'input_files_including_manifest':7,'inputs_unchanged_verified_again':True,'terminal_protocol':'After writing identical closure, script checks recursive C/D inventory and hashes, every manifest payload and all original input bytes again before TERMINAL_VERIFIED.'}
raw=(json.dumps(closure,indent=2,ensure_ascii=False)+'\n').encode('utf-8');(C/'CLOSURE1136.json').write_bytes(raw);(D/'CLOSURE1136.json').write_bytes(raw)
final=inventory(C);assert final==inventory(D) and len(final)==len(before)+1
for row in files:assert final[row['path']]==(row['bytes'],row['sha256'])
inputs()
print(json.dumps({'status':'TERMINAL_VERIFIED','files':len(final),'bytes':sum(v[0] for v in final.values()),'manifest_payloads':len(files),'C_D_identical':True,'inputs_unchanged':True,'AUDIT1136_sha256':sha(C/'AUDIT1136.txt'),'verdict1136_sha256':sha(C/'verdict1136.json'),'MANIFEST1136_sha256':sha(C/'MANIFEST1136.json'),'SHA256SUMS1136_sha256':sha(C/'SHA256SUMS1136.txt'),'CLOSURE1136_sha256':sha(C/'CLOSURE1136.json')},indent=2))
