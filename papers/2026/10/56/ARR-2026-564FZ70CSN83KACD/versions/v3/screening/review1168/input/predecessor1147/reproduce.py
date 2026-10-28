"""Bounded replay of declared current/predecessor controls on disposable copies."""
from pathlib import Path
import argparse,json,hashlib,shutil,subprocess,sys,datetime,os,platform
ap=argparse.ArgumentParser();ap.add_argument('--workdir',required=True);args=ap.parse_args();root=Path(__file__).resolve().parent;work=Path(args.workdir).resolve()
assert not work.exists(),'Choose a new work directory; no overwrite/delete is performed'
assert root!=work and root not in work.parents,'Execution must be outside the evidence package'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();before={p.relative_to(root).as_posix():sha(p) for p in root.rglob('*') if p.is_file()};work.mkdir(parents=True);rows=[];rewrites=[]
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
def run(label,script,cwd):
 r=subprocess.run([sys.executable,'-X','utf8','-B',str(script)],cwd=cwd,env=env,capture_output=True,text=True,timeout=600)
 (work/(label+'-stdout.txt')).write_text(r.stdout,encoding='utf-8');(work/(label+'-stderr.txt')).write_text(r.stderr,encoding='utf-8');assert r.returncode==0,(label,r.returncode,r.stderr[-1500:]);return r
try:
 # The original seven-checker runner remains byte-exact; its own two rewrites are logged there.
 r=subprocess.run([sys.executable,'-X','utf8','-B',str(root/'predecessor1127/reproduce.py'),'--workdir',str(work/'predecessor-replay')],env=env,capture_output=True,text=True,timeout=600)
 (work/'predecessor-stdout.txt').write_text(r.stdout,encoding='utf-8');(work/'predecessor-stderr.txt').write_text(r.stderr,encoding='utf-8');assert r.returncode==0,r.stderr[-1500:]
 legacy=json.loads((work/'predecessor-replay/REPLAY1124.json').read_text());assert legacy['status']=='pass' and len(legacy['rows'])==7;rows.append({'scope':'predecessor1127','checkers':7,'receipt':'predecessor-replay/REPLAY1124.json','six_generated_outputs_byte_exact':True,'48_exact_rational_assertions':True})
 for tag,filename,expected in [('first','check1134_first.py','CONTROL-FIRST1134.json'),('corrected','check1134.py','CONTROL1134.json')]:
  folder=work/('candidate1134-'+tag);folder.mkdir();src=root/'research/1134'/filename;shutil.copy2(src,folder/filename);assert sha(src)==sha(folder/filename);run('candidate1134-'+tag,folder/filename,folder)
  a=json.loads((folder/'CONTROL1134.json').read_text());b=json.loads((root/'research/1134'/expected).read_text());a.pop('utc',None);b.pop('utc',None);assert a==b,(tag,'semantic mismatch beyond regenerated utc');rows.append({'scope':'candidate1134-'+tag,'checkers':1,'original_script_unchanged':True,'12_original_cases_match_excluding_utc':True,'not_universal_or_interval_certificate':True})
 for label,filename,output in [('exact','exact1136.py','EXACT1136.json'),('interval','interval1136.py','INTERVAL1136.json'),('ambient','ambient1136.py','AMBIENT1136.json')]:
  folder=work/('audit1136-'+label);folder.mkdir();src=root/'research/1136'/filename;dst=folder/filename;shutil.copy2(src,dst)
  if label=='interval':
   lib=root/'research/1136/integer_arithmetic1136.py';assert sha(lib)=='6888e17a28c57aee3a7d99f21c10aad3ccc2115493ced999fcb97fd097fbb853';shutil.copy2(lib,folder/lib.name)
   original=dst.read_text();needle="src=Path(r'C:\\Trabajo\\airr\\2026-10-27_binary1077-audit\\integer_arithmetic1077.py')";assert original.count(needle)==1
   changed=original.replace(needle,"src=P/'integer_arithmetic1136.py'");dst.write_text(changed,encoding='utf-8')
   ol=original.splitlines();nl=changed.splitlines();changed_lines=[{'line':i+1,'original':a,'execution':b} for i,(a,b) in enumerate(zip(ol,nl)) if a!=b];assert len(ol)==len(nl) and len(changed_lines)==1
   rewrites.append({'file':filename,'original_sha256':sha(src),'executed_sha256':sha(dst),'changed_only_library_path':True,'lines':changed_lines})
  run('audit1136-'+label,dst,folder);actual=json.loads((folder/output).read_text());expected=json.loads((root/'research/1136'/output).read_text());assert actual==expected,(label,'output mismatch; do not alter reference')
  rows.append({'scope':'audit1136-'+label,'checkers':1,'all_JSON_scientific_fields_match':True,'same_original_parameters_and_cases':True,'output':output})
 after={p.relative_to(root).as_posix():sha(p) for p in root.rglob('*') if p.is_file()};assert before==after,'Input packet changed during replay'
 out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'pass','checkers':12,'input_files_unchanged':len(before),'scope':'bounded declared controls only, not all archived scripts or a universal proof/independent review','runtime':{'python':sys.version,'platform':platform.platform()},'inherited_path_rewrites':legacy['path_rewrites'],'additional_path_rewrites':rewrites,'total_dependency_path_lines_changed_in_execution_copies_only':3,'rows':rows}
 (work/'REPLAY1147.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'status':'pass','checkers':12,'inputs_unchanged':len(before),'only_dependency_rewrites':3,'receipt':str(work/'REPLAY1147.json')}))
except Exception as e:
 (work/'FAILURE1147.json').write_text(json.dumps({'error':repr(e),'completed':rows,'additional_rewrites':rewrites},indent=2)+'\n',encoding='utf-8');raise
