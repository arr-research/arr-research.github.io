from pathlib import Path
import hashlib,json,datetime,sys
P=Path(__file__).parent
specs=[('1110','2026-10-27_fixed1110','87e208b77f4718006224dc70087d049ade3fd844f44d1f6abd3a576711966749'),('1112','2026-10-27_fixed1112-prior','e48f5820911c6a3d10389dfed74950ca3c74e466c9ea0d2c7c094f88d0302578'),('1113','2026-10-27_fixed1113-fullmatrix','0bd4d52299b3ad1234bbe5539c06d9fc7716435f35e3237da00c77f89ed75e5a'),('1108','2026-10-27_binary1108-boundary','88911553c8448be83440ce5b59c5154d1dca0b800cc878de2ae07f0f17d8aa84')]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();out=[]
for i,name,h in specs:
 C=Path(r'C:\Trabajo\airr')/name;D=Path(r'D:\Proyectos\airr-investigacion')/name;mf='MANIFEST'+i+'.json'
 assert sha(C/mf)==sha(D/mf)==h
 files=json.loads((C/mf).read_text())['files']
 for r in files:
  assert sha(C/r['path'])==sha(D/r['path'])==r['sha256'];assert (C/r['path']).stat().st_size==(D/r['path']).stat().st_size==r['bytes']
 assert sorted(p.name for p in C.iterdir())==sorted(p.name for p in D.iterdir())==sorted([mf]+[r['path'] for r in files])
 out.append(dict(id=i,C=str(C),D=str(D),manifest_sha256=h,files=files,C_D_identical=True,inventory_exact=True))
phase=sys.argv[1] if len(sys.argv)>1 else 'initial'
(P/('INPUT_'+phase.upper()+'1115.json')).write_text(json.dumps(dict(phase=phase,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),packages=out),indent=2)+'\n',encoding='utf-8')
print('Verified',phase,sum(1+len(p['files']) for p in out),'files C/D')
