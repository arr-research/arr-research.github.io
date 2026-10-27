from pathlib import Path
import json,hashlib,datetime,sys
P=Path(__file__).parent
packs=[('1033','2026-10-27_principal1033','4ddb0586a74f1178414546ae773aaa2b6cdff42f2a973b66a74c18f36f78f597'),('1035','2026-10-27_bkm1035','5b1c05e53dbbef4818ffecacb8edbc4b57322d1d5772e230477b2c796d90d719')]
rows=[]
for no,dirname,expected in packs:
 c=Path(r'C:\Trabajo\airr')/dirname;d=Path(r'D:\Proyectos\airr-investigacion')/dirname;raw=(d/('MANIFEST'+no+'.json')).read_bytes();assert raw==(c/('MANIFEST'+no+'.json')).read_bytes();assert hashlib.sha256(raw).hexdigest()==expected;files=[]
 for x in json.loads(raw)['files']:
  f=d/x['path'];assert f.resolve().is_relative_to(d.resolve());b=f.read_bytes();assert b==(c/x['path']).read_bytes();h=hashlib.sha256(b).hexdigest();assert h==x['sha256'] and len(b)==x['bytes'];files.append({'path':x['path'],'bytes':len(b),'sha256':h,'C_D_identical':True})
 cs={f.relative_to(c).as_posix() for f in c.rglob('*') if f.is_file()};ds={f.relative_to(d).as_posix() for f in d.rglob('*') if f.is_file()};assert cs==ds
 rows.append({'package':no,'C':str(c),'D':str(d),'manifest_sha256':expected,'files':files,'unlisted':sorted(ds-{x['path'] for x in files}-{'MANIFEST'+no+'.json'})})
phase=sys.argv[1] if len(sys.argv)>1 else 'before';out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':phase,'packages':rows,'all_passed':True}
(P/('INPUT_FINAL1044.json' if phase=='after' else 'INPUT_VERIFIED1044.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'phase':phase,'payloads':sum(len(x['files']) for x in rows),'all_C_D_identical':True,'all_hashes_match':True,'unlisted':[x['unlisted'] for x in rows]}))
