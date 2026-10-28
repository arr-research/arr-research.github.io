from pathlib import Path
import json,hashlib,sys,datetime
P=Path(r'C:\Trabajo\airr\2026-10-27_binary1093-audit');P.mkdir(exist_ok=True)
C=Path(r'C:\Trabajo\airr\2026-10-27_binary1092-barrier');D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_binary1092-barrier')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
expected='9e410927de5404ca42d96c92feb384662e514a4d6ee90418e5a275af0ed8b0a0'
assert sha(C/'MANIFEST1092.json')==sha(D/'MANIFEST1092.json')==expected
m=json.loads((C/'MANIFEST1092.json').read_text());rows=[]
for f in m['files']:
 a=C/f['path'];b=D/f['path'];assert sha(a)==sha(b)==f['sha256'];assert a.stat().st_size==b.stat().st_size==f['bytes'];rows.append(f)
assert sha(C/'PROOF1092.txt')=='c2303054b0859e4b9e5045761aee599c594d1932f2a8dfeb437f1b75f84b0150'
assert sorted(x.name for x in C.iterdir())==sorted(x.name for x in D.iterdir())==sorted(['MANIFEST1092.json']+[x['path'] for x in rows])
phase=sys.argv[1] if len(sys.argv)>1 else 'initial'
r={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':phase,'C':str(C),'D':str(D),'manifest_sha256':expected,'files':rows,'C_D_identical':True,'inventory_exact':True}
(P/('INPUT_'+phase.upper()+'1093.json')).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print('Verified',phase,len(rows)+1,'files C/D')
