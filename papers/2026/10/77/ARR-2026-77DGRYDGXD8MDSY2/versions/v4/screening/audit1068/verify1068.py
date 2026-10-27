from pathlib import Path
import hashlib,json,datetime,sys
P=Path(__file__).parent;rows=[]
for ident,folder in [('1063','2026-10-27_polynomial-phase1063'),('1064','2026-10-27_polynomial-phase1064-controls'),('1066','2026-10-27_phase-tradeoff1066')]:
 c=Path(r'C:\Trabajo\airr')/folder;d=Path(r'D:\Proyectos\airr-investigacion')/folder;mf='MANIFEST'+ident+'.json';raw=(c/mf).read_bytes();assert raw==(d/mf).read_bytes();files=[]
 for f in json.loads(raw)['files']:
  path=c/f['path'];assert path.resolve().is_relative_to(c.resolve());b=path.read_bytes();assert b==(d/f['path']).read_bytes();assert len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256'];files.append(f)
 listed={f['path'] for f in files}|{mf};extras={}
 for tag,base in [('C',c),('D',d)]:
  extras[tag]=[{'path':f.relative_to(base).as_posix(),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'bytes':f.stat().st_size} for f in sorted(base.rglob('*')) if f.is_file() and f.relative_to(base).as_posix() not in listed]
 rows.append({'id':ident,'C':str(c),'D':str(d),'manifest_sha256':hashlib.sha256(raw).hexdigest(),'files':files,'unlisted':extras,'C_D_sealed_files_identical':True})
phase=sys.argv[1] if len(sys.argv)>1 else 'before';out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':phase,'external_manifest_hashes_supplied_at_start':False,'packages':rows}
if phase=='after':assert json.loads((P/'INPUT_VERIFIED1068.json').read_text())['packages']==rows
(P/('INPUT_FINAL1068.json' if phase=='after' else 'INPUT_VERIFIED1068.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
