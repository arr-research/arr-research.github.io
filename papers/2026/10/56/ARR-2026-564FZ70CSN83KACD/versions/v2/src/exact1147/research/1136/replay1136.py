from pathlib import Path
import subprocess,sys,json,hashlib,shutil
W=Path(__file__).parent;S=Path(r'C:\Trabajo\airr\2026-10-27_support1134')
out=[]
for tag,script,expected in [('first','check1134_first.py','CONTROL-FIRST1134.json'),('corrected','check1134.py','CONTROL1134.json')]:
 folder=W/('replay-'+tag);folder.mkdir(exist_ok=False)
 shutil.copyfile(S/script,folder/script)
 p=subprocess.run([sys.executable,'-B',str(folder/script)],cwd=folder,text=True,capture_output=True)
 (folder/'stdout.txt').write_text(p.stdout,encoding='utf-8');(folder/'stderr.txt').write_text(p.stderr,encoding='utf-8')
 assert p.returncode==0,p.stderr
 actual=json.loads((folder/'CONTROL1134.json').read_text());original=json.loads((S/expected).read_text())
 actual.pop('utc');original.pop('utc');assert actual==original
 out.append({'tag':tag,'script_sha256':hashlib.sha256((folder/script).read_bytes()).hexdigest(),'semantic_match_excluding_utc':True,'cases':len(actual['cases']),'exit':p.returncode})
(W/'REPLAY1136.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
