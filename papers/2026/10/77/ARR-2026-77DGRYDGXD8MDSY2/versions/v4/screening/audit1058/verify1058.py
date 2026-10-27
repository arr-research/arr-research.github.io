from pathlib import Path
import hashlib,json,datetime,sys
P=Path(__file__).parent;c=Path(r'C:\Trabajo\airr\2026-10-27_bell-allnoise1057');d=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_bell-allnoise1057');mf='MANIFEST1057.json';raw=(d/mf).read_bytes();assert raw==(c/mf).read_bytes();h=hashlib.sha256(raw).hexdigest();files=[]
for x in json.loads(raw)['files']:
 f=d/x['path'];assert f.resolve().is_relative_to(d.resolve());b=f.read_bytes();assert b==(c/x['path']).read_bytes();assert hashlib.sha256(b).hexdigest()==x['sha256'] and len(b)==x['bytes'];files.append({**x,'C_D_identical':True})
listed={x['path'] for x in files}|{mf};extra={}
for label,base in [('C',c),('D',d)]:
 extra[label]=[{'path':f.relative_to(base).as_posix(),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'bytes':f.stat().st_size,'not_executed':True} for f in sorted(base.rglob('*')) if f.is_file() and f.relative_to(base).as_posix() not in listed]
phase=sys.argv[1] if len(sys.argv)>1 else 'before';out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':phase,'manifest_sha256':h,'manifest_external_hash_supplied_at_task_start':False,'C':str(c),'D':str(d),'files':files,'unlisted':extra,'all_manifest_files_verified_and_identical':True}
if phase=='after':
 before=json.loads((P/'INPUT_VERIFIED1058.json').read_text());assert all(before[k]==out[k] for k in ['manifest_sha256','files','unlisted'])
(P/('INPUT_FINAL1058.json' if phase=='after' else 'INPUT_VERIFIED1058.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
