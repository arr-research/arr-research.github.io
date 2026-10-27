from pathlib import Path
import json,subprocess,sys,shutil,hashlib
P=Path(__file__).parent;spec=[('1096','2026-10-27_simplex1096','check1096.py','CONTROL1096.json'),('1099','2026-10-27_simplex1099-certificates','certify1099.py','CERTIFICATES1099.json'),('1101','2026-10-27_simplex1101-measurement','measure1101.py','MEASUREMENT1101.json')];rows=[]
for ident,name,script,out in spec:
 S=Path(r'C:\Trabajo\airr')/name;D=P/('replay'+ident);D.mkdir(exist_ok=True);shutil.copy2(S/script,D/script)
 if (S/'integer_arithmetic1077.py').exists():shutil.copy2(S/'integer_arithmetic1077.py',D/'integer_arithmetic1077.py')
 r=subprocess.run([sys.executable,'-B',str(D/script)],capture_output=True,text=True,encoding='utf-8');(D/'stdout.txt').write_text(r.stdout,encoding='utf-8');(D/'stderr.txt').write_text(r.stderr,encoding='utf-8')
 row={'id':ident,'script':script,'script_sha256':hashlib.sha256((D/script).read_bytes()).hexdigest(),'exit':r.returncode,'output_identical':r.returncode==0 and (S/out).read_bytes()==(D/out).read_bytes()};rows.append(row)
 (P/'REPLAY1100.json').write_text(json.dumps({'runs':rows,'scope':'Unmodified scripts copied to own separatefolders;1099 reads frozen1096 only. Originalsideeffects redirected by __file__.'},indent=2)+'\n',encoding='utf-8');assert row['exit']==0 and row['output_identical'],row
 print(ident,'byte-identical',flush=True)
