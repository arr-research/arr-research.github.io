"""Bounded original controls, run only in a fresh disposable directory."""
from pathlib import Path
import json,hashlib,sys,subprocess,shutil,argparse,datetime,os
ap=argparse.ArgumentParser();ap.add_argument('--workdir',required=True);args=ap.parse_args()
root=Path(__file__).resolve().parent;work=Path(args.workdir).resolve()
assert not work.exists() and root!=work and root not in work.parents
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
inventory=lambda p:{f.relative_to(p).as_posix():sha(f) for f in p.rglob('*') if f.is_file()}
before=inventory(root);work.mkdir(parents=True);rows=[];env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
def run(label,args,cwd,timeout):
 r=subprocess.run([sys.executable,'-X','utf8','-B']+list(map(str,args)),cwd=cwd,env=env,capture_output=True,timeout=timeout)
 (work/(label+'-stdout.txt')).write_bytes(r.stdout);(work/(label+'-stderr.txt')).write_bytes(r.stderr)
 assert r.returncode==0,(label,r.returncode,r.stderr[-1500:])
try:
 run('predecessor1147',[root/'predecessor1147/reproduce.py','--workdir',work/'legacy'],root,1200)
 old=json.loads((work/'legacy/REPLAY1147.json').read_bytes());assert old['status']=='pass' and old['checkers']==12
 rows.append({'scope':'predecessor1147','checkers':12,'status':'pass','receipt':'legacy/REPLAY1147.json','inherited_path_rewrites':old['total_dependency_path_lines_changed_in_execution_copies_only']})
 for label,script,out in [('exact','exact_own1157.py','EXACT_OWN1157.json'),('interval','interval_own1157.py','INTERVAL_OWN1157.json')]:
  folder=work/label;folder.mkdir();src=root/'research/1157'/script;shutil.copy2(src,folder/script)
  if label=='interval':shutil.copy2(root/'research/1157/integer_arithmetic1077.py',folder/'integer_arithmetic1077.py')
  assert sha(src)==sha(folder/script)
  run(label,[folder/script],folder,600)
  assert json.loads((folder/out).read_bytes())==json.loads((root/'research/1157'/out).read_bytes())
  rows.append({'scope':'CQ1157-'+label,'original_script_unchanged':True,'all_JSON_fields_match':True,'output':str(folder/out)})
 assert before==inventory(root),'Frozen input changed'
 result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'pass','rows':rows,'inputs_unchanged':len(before),'scope':'12 inherited checkers plus exact CQ geometry and seven integer interval controls; not every archived script; not independent arithmetic or a proof of general theorem'}
 (work/'REPLAY1167.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
except Exception as e:
 (work/'FAILURE1167.json').write_text(json.dumps({'error':repr(e),'completed':rows},indent=2)+'\n',encoding='utf-8');raise
