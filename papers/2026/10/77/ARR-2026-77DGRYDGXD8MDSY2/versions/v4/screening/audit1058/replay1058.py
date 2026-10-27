from pathlib import Path
import sys,subprocess,json,hashlib
P=Path(__file__).parent;R=P/'replay';R.mkdir(exist_ok=True);S=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_bell-allnoise1057');raw=(S/'check1057.py').read_bytes();(R/'check1057.py').write_bytes(raw)
p=subprocess.run([sys.executable,str(R/'check1057.py')],cwd=R,capture_output=True);(R/'stdout.txt').write_bytes(p.stdout);(R/'stderr.txt').write_bytes(p.stderr)
out={'script_sha256':hashlib.sha256(raw).hexdigest(),'exit':p.returncode}
if p.returncode==0:
 old=json.loads((S/'CHECK1057.json').read_text());new=json.loads((R/'CHECK1057.json').read_text());out['source_utc']=old.pop('utc');out['replay_utc']=new.pop('utc');out['fields_equal_except_utc']=old==new
(P/'REPLAY1058.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out));assert p.returncode==0 and out['fields_equal_except_utc']
