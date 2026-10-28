from pathlib import Path
import hashlib,shutil,json,subprocess
P=Path(__file__).parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();runs=[]
specs=[('1110','2026-10-27_fixed1110','check1110.py','CONTROL1110.json',['integer_arithmetic1077.py']),('1113','2026-10-27_fixed1113-fullmatrix','full1113.py','FULLMATRIX1113.json',[]),('1108','2026-10-27_binary1108-boundary','check1108.py','CONTROL1108.json',['CONTROL1108.json'])]
for i,base,script,result,deps in specs:
 src=Path(r'C:\Trabajo\airr')/base;own=P/('replay'+i);own.mkdir(exist_ok=True)
 for f in [script]+deps:shutil.copyfile(src/f,own/f)
 p=subprocess.run([r'C:\Python312\python.exe','-B',str(own/script)],cwd=own,text=True,capture_output=True)
 (own/'stdout.txt').write_text(p.stdout,encoding='utf-8');(own/'stderr.txt').write_text(p.stderr,encoding='utf-8')
 row=dict(id=i,exit=p.returncode,script_sha256=sha(own/script),output_identical=(own/result).exists() and (own/result).read_bytes()==(src/result).read_bytes(),output_generated=(i!='1108'))
 runs.append(row);assert p.returncode==0 and row['output_identical']
(P/'REPLAY1115.json').write_text(json.dumps(dict(runs=runs,scope='Unmodified checkers inownfolders;1113reads frozen1110only;1108reads its copiedcontrol without generatingit.'),indent=2)+'\n',encoding='utf-8');print(json.dumps(runs))
