"""Portable replay of the seven declared core computations; never edit evidence originals."""
from pathlib import Path
import argparse,json,hashlib,shutil,subprocess,sys,datetime,os
ap=argparse.ArgumentParser();ap.add_argument('--workdir',required=True);args=ap.parse_args()
root=Path(__file__).resolve().parent;work=Path(args.workdir).resolve()
assert not work.exists(),'Choose a new empty work path; replay never deletes or overwrites it'
assert root not in work.parents and work!=root,'Work must be outside the evidence package'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
before={p.relative_to(root).as_posix():sha(p) for p in root.rglob('*') if p.is_file()}
work.mkdir(parents=True)
plans=[('1092','check1092.py','CONTROL1092.json'),('1096','check1096.py','CONTROL1096.json'),('1099','certify1099.py','CERTIFICATES1099.json'),('1101','measure1101.py','MEASUREMENT1101.json'),('1108','check1108.py',None),('1110','check1110.py','CONTROL1110.json'),('1113','full1113.py','FULLMATRIX1113.json')]
for id,_,_ in plans:shutil.copytree(root/'research'/id,work/id)
rewrites=[]
for id,filename,target in [('1099','certify1099.py',work/'1096'/'CONTROL1096.json'),('1113','full1113.py',work/'1110')]:
 p=work/id/filename;original=sha(p);lines=p.read_text().splitlines();found=[i for i,l in enumerate(lines) if l.startswith('source=Path(')];assert len(found)==1
 i=found[0];previous=lines[i];lines[i]='source=Path('+repr(target.as_posix())+')';p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
 rewrites.append({'id':id,'file':filename,'original_sha256':original,'executed_copy_sha256':sha(p),'changed_only_declared_dependency_path_line':True,'original_line':previous,'execution_line':lines[i]})
rows=[]
try:
 for id,filename,output in plans:
  env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1');r=subprocess.run([sys.executable,'-X','utf8','-B',str(work/id/filename)],cwd=work/id,env=env,capture_output=True,text=True,timeout=600)
  (work/f'stdout-{id}.txt').write_text(r.stdout,encoding='utf-8');(work/f'stderr-{id}.txt').write_text(r.stderr,encoding='utf-8')
  assert r.returncode==0,(id,r.returncode,r.stderr[-1000:])
  row={'id':id,'checker':filename,'exit':r.returncode,'output':output,'byte_exact_expected':None}
  if output:
   actual=work/id/output;expected=root/'research'/id/output;assert actual.read_bytes()==expected.read_bytes(),f'{id} output differs; preserve and inspect, do not change reference'
   row.update(byte_exact_expected=True,sha256=sha(actual))
  else:row['check']='48 exact rational stored-row assertions passed; no output file generator'
  rows.append(row)
 after={p.relative_to(root).as_posix():sha(p) for p in root.rglob('*') if p.is_file()};assert before==after,'Evidence package changed during replay'
 out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'pass','scope':'seven fixed core checkers, not all archived audit scripts, not universal proof or independent review','path_rewrites':rewrites,'package_files_unchanged':len(before),'rows':rows}
 (work/'REPLAY1124.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'status':'pass','checkers':len(rows),'six_generated_outputs_byte_exact':True,'receipt':str(work/'REPLAY1124.json')}))
except Exception as e:
 (work/'FAILURE1124.json').write_text(json.dumps({'error':repr(e),'completed':rows,'path_rewrites':rewrites},indent=2)+'\n',encoding='utf-8');raise
