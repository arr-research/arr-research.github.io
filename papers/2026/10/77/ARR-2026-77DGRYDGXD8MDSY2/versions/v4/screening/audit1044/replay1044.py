from pathlib import Path
import subprocess,sys,json,hashlib
P=Path(__file__).parent;rows=[]
for pkg,name,out in [('2026-10-27_principal1033','check1033.py','CHECK1033.json'),('2026-10-27_bkm1035','check1035.py','CHECK1035.json'),('2026-10-27_bkm1035','interval1035.py','INTERVAL1035.json')]:
 src=Path(r'D:\Proyectos\airr-investigacion')/pkg;dest=P/'replay';dest.mkdir(exist_ok=True);f=dest/name;f.write_bytes((src/name).read_bytes());r=subprocess.run([sys.executable,str(f)],capture_output=True,text=True)
 (dest/(name+'.stdout.txt')).write_text(r.stdout,encoding='utf-8');(dest/(name+'.stderr.txt')).write_text(r.stderr,encoding='utf-8');row={'script':name,'original_and_executed_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'exit':r.returncode}
 if r.returncode==0:row.update(output_byte_identical=(dest/out).read_bytes()==(src/out).read_bytes(),output_json_identical=json.loads((dest/out).read_text())==json.loads((src/out).read_text()))
 rows.append(row);(P/'REPLAY1044.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8');assert r.returncode==0
print(json.dumps(rows))
