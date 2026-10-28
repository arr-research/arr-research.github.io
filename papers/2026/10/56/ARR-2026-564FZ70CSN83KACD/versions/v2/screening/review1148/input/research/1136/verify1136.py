from pathlib import Path
import hashlib,json,datetime,sys
W=Path(__file__).parent
C=Path(r'C:\Trabajo\airr\2026-10-27_support1134');D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_support1134')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
h='d0484d62d5e8f4de29736ad3734e2f9271d0e2c1d9026c9bdee4e3ec340fd67b'
assert sha(C/'MANIFEST1134.json')==sha(D/'MANIFEST1134.json')==h
files=json.loads((C/'MANIFEST1134.json').read_text())['files']
for r in files:
 assert sha(C/r['path'])==sha(D/r['path'])==r['sha256']
 assert (C/r['path']).stat().st_size==(D/r['path']).stat().st_size==r['bytes']
assert sorted(p.name for p in C.iterdir())==sorted(p.name for p in D.iterdir())==sorted(['MANIFEST1134.json']+[r['path'] for r in files])
phase=sys.argv[1] if len(sys.argv)>1 else 'final'
receipt={'phase':phase,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'C':str(C),'D':str(D),'manifest_sha256':h,'files':files,'C_D_identical':True,'inventory_exact':True}
(W/('INPUT_'+phase.upper()+'1136.json')).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print('Verified',phase,'seven input files C/D')
