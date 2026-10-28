from pathlib import Path
import json,subprocess,sys,shutil,hashlib
P=Path(__file__).parent;S=Path(r'C:\Trabajo\airr\2026-10-27_binary1092-barrier');D=P/'replay1092';D.mkdir(exist_ok=True)
shutil.copy2(S/'check1092.py',D/'check1092.py')
r=subprocess.run([sys.executable,str(D/'check1092.py')],capture_output=True,text=True,encoding='utf-8')
(D/'stdout.txt').write_text(r.stdout,encoding='utf-8');(D/'stderr.txt').write_text(r.stderr,encoding='utf-8')
assert r.returncode==0
assert (D/'CONTROL1092.json').read_bytes()==(S/'CONTROL1092.json').read_bytes()
(P/'REPLAY1093.json').write_text(json.dumps({'script_unchanged':True,'script_sha256':hashlib.sha256((D/'check1092.py').read_bytes()).hexdigest(),'exit':r.returncode,'output_byte_identical':True,'controls':7,'scope':'Original checker executed only in own copy; input immutable.'},indent=2)+'\n',encoding='utf-8')
print('7 original exact controls replayed byte-identically.')
