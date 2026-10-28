from pathlib import Path
import json,hashlib,datetime,sys
P=Path(r'C:\Trabajo\airr\2026-10-27_simplex1100-audit');P.mkdir(exist_ok=True)
specs=[('1096','2026-10-27_simplex1096','c3d1846c3291390de2e5d76f81a1538ce8a19ef1947c52122c8bb4f434d80b34'),('1099','2026-10-27_simplex1099-certificates','303ae24473ca2a0d163aa86ab42e7eee6365c17cfd5f69f628eb74f91e6a9686'),('1101','2026-10-27_simplex1101-measurement','2dbb209682c8cc39f2c618f504c36e3b8f2da81dc773913ed6aab93d815bb18d')]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();out=[]
for ident,name,expected in specs:
 C=Path(r'C:\Trabajo\airr')/name;D=Path(r'D:\Proyectos\airr-investigacion')/name;mf='MANIFEST'+ident+'.json'
 assert sha(C/mf)==sha(D/mf)==expected
 files=json.loads((C/mf).read_text())['files']
 for row in files:
  a=C/row['path'];b=D/row['path'];assert sha(a)==sha(b)==row['sha256'];assert a.stat().st_size==b.stat().st_size==row['bytes']
 assert sorted(x.name for x in C.iterdir())==sorted(x.name for x in D.iterdir())==sorted([mf]+[x['path'] for x in files])
 out.append({'id':ident,'C':str(C),'D':str(D),'manifest_sha256':expected,'files':files,'C_D_identical':True,'inventory_exact':True})
assert sha(Path(out[0]['C'])/'PROOF1096.txt')=='72afb9a1c90aa3009f13d4ab528b1ecae557a46abce33dc02e7df9d5ffd7251c'
phase=sys.argv[1] if len(sys.argv)>1 else 'initial';(P/('INPUT_'+phase.upper()+'1100.json')).write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':phase,'packages':out},indent=2)+'\n',encoding='utf-8');print('Verified',phase,sum(1+len(x['files']) for x in out),'files C/D')
