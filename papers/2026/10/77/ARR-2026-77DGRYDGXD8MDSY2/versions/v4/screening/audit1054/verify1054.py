from pathlib import Path
import json,hashlib,datetime,sys
P=Path(__file__).parent
packs=[('1051','2026-10-27_local-phase1051','9aa6068ed7301229c4f467feeee0be0c16e89f286f1fbfeb647660fc49874532'),('1052','2026-10-27_bell-benchmark1052','9e5404f43294860288c3ad1bb79fd8a534732dc2de6bf9635ba2989aa18b5f7b')]
rows=[]
for no,name,h in packs:
 c=Path(r'C:\Trabajo\airr')/name;d=Path(r'D:\Proyectos\airr-investigacion')/name;mf='MANIFEST'+no+'.json';raw=(d/mf).read_bytes();assert raw==(c/mf).read_bytes() and hashlib.sha256(raw).hexdigest()==h
 files=[]
 for x in json.loads(raw)['files']:
  f=d/x['path'];assert f.resolve().is_relative_to(d.resolve());b=f.read_bytes();assert b==(c/x['path']).read_bytes();assert hashlib.sha256(b).hexdigest()==x['sha256'] and len(b)==x['bytes'];files.append({**x,'C_D_identical':True})
 cs={f.relative_to(c).as_posix() for f in c.rglob('*') if f.is_file()};ds={f.relative_to(d).as_posix() for f in d.rglob('*') if f.is_file()};listed={x['path'] for x in files}|{mf}
 extras={}
 for label,base,found in [('C',c,cs),('D',d,ds)]:
  extras[label]=[{'path':x,'bytes':(base/x).stat().st_size,'sha256':hashlib.sha256((base/x).read_bytes()).hexdigest(),'not_executed':True} for x in sorted(found-listed)]
 rows.append({'package':no,'C':str(c),'D':str(d),'manifest_sha256':h,'files':files,'unlisted':extras,'whole_folder_inventory_identical':cs==ds})
phase=sys.argv[1] if len(sys.argv)>1 else 'before';out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':phase,'packages':rows,'all_passed':True}
(P/('INPUT_FINAL1054.json' if phase=='after' else 'INPUT_VERIFIED1054.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'phase':phase,'payloads':sum(len(x['files']) for x in rows),'total_with_manifests':sum(len(x['files'])+1 for x in rows),'all_C_D_identical':True,'all_hashes_match':True}))
