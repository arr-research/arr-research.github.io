from pathlib import Path
import hashlib,json,datetime,sys
P=Path(__file__).parent;C=Path(r'C:\Trabajo\airr\2026-10-28_cq1152');D=Path(r'D:\Proyectos\airr-investigacion\2026-10-28_cq1152')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();h='3157deb948f01e9915bd124037765be5533c5ccd19f61597642f4d994279ec11'
assert sha(C/'MANIFEST1152.json')==sha(D/'MANIFEST1152.json')==h
files=json.loads((C/'MANIFEST1152.json').read_text())['files']
for r in files:
 assert sha(C/r['path'])==sha(D/r['path'])==r['sha256']
 assert (C/r['path']).stat().st_size==(D/r['path']).stat().st_size==r['bytes']
expected=sorted(['MANIFEST1152.json']+[r['path'] for r in files]);assert len(expected)==22
assert sorted(p.relative_to(C).as_posix() for p in C.rglob('*') if p.is_file())==sorted(p.relative_to(D).as_posix() for p in D.rglob('*') if p.is_file())==expected
phase=sys.argv[1] if len(sys.argv)>1 else 'final'
(P/('INPUT_'+phase.upper()+'1157.json')).write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':phase,'C':str(C),'D':str(D),'files':files,'manifest_sha256':h,'C_D_identical':True,'inventory_exact':True},indent=2)+'\n',encoding='utf-8')
print('Verified',phase,'22inputfiles C/D')
