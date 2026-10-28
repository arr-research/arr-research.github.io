"""Seal only audit1157, verify frozen input, archive identically C/D. No Git."""
from pathlib import Path
import json,hashlib,datetime,shutil,subprocess,sys
C=Path(__file__).resolve().parent
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-28_cq1157-audit')
assert str(C)==r'C:\Trabajo\airr\2026-10-28_cq1157-audit'
assert not D.exists(),'Do not overwrite an existing archive'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def snapshot(base):return [{'path':p.relative_to(base).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(base.rglob('*')) if p.is_file()]
def frozen():
 A=Path(r'C:\Trabajo\airr\2026-10-28_cq1152');B=Path(r'D:\Proyectos\airr-investigacion\2026-10-28_cq1152')
 assert snapshot(A)==snapshot(B)
 assert sha(A/'MANIFEST1152.json')=='3157deb948f01e9915bd124037765be5533c5ccd19f61597642f4d994279ec11'
 rows=json.loads((A/'MANIFEST1152.json').read_text())['files'];actual={r['path']:r for r in snapshot(A)}
 assert len(actual)==22
 for r in rows:assert actual[r['path']]==r
 return True
assert frozen()
subprocess.run([sys.executable,'-B',str(C/'verify1157.py'),'final'],check=True)
for p in C.rglob('*'):assert not p.is_symlink() and not p.is_junction(),str(p)
# Only regenerable local bytecode inside this exact audit directory is removed.
cache=C/'__pycache__'
if cache.exists():
 assert cache.resolve().parent==C and not cache.is_junction() and not cache.is_symlink()
 shutil.rmtree(cache)
for p in C.rglob('*.json'):json.loads(p.read_text(encoding='utf-8'))
exclude={'MANIFEST1157.json','MANIFEST1157.sha256','CLOSURE1157.json'}
assert not any((C/n).exists() for n in exclude)
payloads=snapshot(C)
manifest={'audit':'1157','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':payloads,'count':len(payloads),'bytes':sum(r['bytes'] for r in payloads),'excludes':sorted(exclude),'input_manifest_sha256':'3157deb948f01e9915bd124037765be5533c5ccd19f61597642f4d994279ec11','foreign_corpus':False}
put(C/'MANIFEST1157.json',manifest)
mh=sha(C/'MANIFEST1157.json');(C/'MANIFEST1157.sha256').write_text(mh+'  MANIFEST1157.json\n',encoding='ascii')
D.mkdir(parents=True,exist_ok=False)
for r in snapshot(C):
 src=C/r['path'];dst=D/r['path'];dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
assert snapshot(C)==snapshot(D)
assert frozen()
closure={'audit':'1157','status':'terminal','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'C':str(C),'D':str(D),'payload_count':len(payloads),'total_file_count_including_closure':len(snapshot(C))+1,'manifest_sha256':mh,'report_sha256':sha(C/'AUDIT1157.txt'),'verdict_sha256':sha(C/'verdict1157.json'),'frozen_input_files':22,'frozen_input_verified_after_copy':True,'payloads_and_manifest_C_D_identical':True,'closure_excluded_from_manifest_to_avoid_self_reference':True,'postwrite_check':'Closure copied byte-identically and entire inventories compared before terminal tool output.'}
put(C/'CLOSURE1157.json',closure);shutil.copyfile(C/'CLOSURE1157.json',D/'CLOSURE1157.json')
assert snapshot(C)==snapshot(D)
for r in payloads:assert sha(C/r['path'])==sha(D/r['path'])==r['sha256']
assert frozen()
print(json.dumps({**closure,'closure_sha256':sha(C/'CLOSURE1157.json'),'all_file_bytes':sum(r['bytes'] for r in snapshot(C)),'full_postwrite_C_D_equality':True},indent=2))
