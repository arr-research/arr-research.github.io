from pathlib import Path
import subprocess,json,sys,shutil,hashlib
P=Path(__file__).parent;S=Path(r'C:\Trabajo\airr\2026-10-28_cq1152');rows=[]
for tag,script,outfile,expected in [('first','check-first1152.py','CONTROL1152.json','CONTROL-FIRST1152.json'),('current','check1152.py','CONTROL1152.json','CONTROL1152.json'),('exact','exact1152.py','EXACT1152.json','EXACT1152.json'),('adverse','negative1152.py','NEGATIVE1152.json','NEGATIVE1152.json')]:
 folder=P/('replay-'+tag);folder.mkdir(exist_ok=False);shutil.copyfile(S/script,folder/script)
 p=subprocess.run([sys.executable,'-B',str(folder/script)],cwd=folder,capture_output=True,text=True,timeout=90)
 (folder/'stdout.txt').write_text(p.stdout,encoding='utf-8');(folder/'stderr.txt').write_text(p.stderr,encoding='utf-8');assert p.returncode==0,p.stderr
 a=json.loads((folder/outfile).read_text());b=json.loads((S/expected).read_text());a.pop('utc');b.pop('utc');assert a==b
 rows.append({'tag':tag,'script_sha256':hashlib.sha256((folder/script).read_bytes()).hexdigest(),'match_excluding_utc':True,'cases':len(a['cases'])})
history=P/'input-history';history.mkdir()
for name in ['exact-first1152.py','exact-second1152.py','EXACT-STRUCTURAL-FAILURE1152.txt','INCIDENTS1152.json']:
 shutil.copyfile(S/name,history/name)
# Reproduce only bounded known structural failure; do not rerun the slow pseudoinverse algorithm.
p=subprocess.run([sys.executable,'-B',str(history/'exact-second1152.py')],cwd=history,capture_output=True,text=True,timeout=30)
(history/'structural-replay-stdout.txt').write_text(p.stdout,encoding='utf-8');(history/'structural-replay-stderr.txt').write_text(p.stderr,encoding='utf-8')
rows.append({'tag':'historical_structural_failure','returncode':p.returncode,'assertion_reproduced':'AssertionError' in p.stderr,'slow_pinv_replayed':False})
assert p.returncode!=0 and 'AssertionError' in p.stderr
(P/'REPLAY1157.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8');print(json.dumps(rows))
