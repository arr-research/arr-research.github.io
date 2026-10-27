from pathlib import Path
import json,hashlib,shutil,subprocess,datetime,sys
P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
jobs=[
 ('core1044','2026-10-27_principal1044-audit','asymptotic1044.py','ASYMPTOTIC1044.json'),
 ('bell1058','2026-10-27_bell-allnoise1058-audit','controls1058.py','CONTROLS1058.json'),
 ('scaling1068','2026-10-27_phase-tradeoff1068-audit','symbolic1068.py','SYMBOLIC1068.json'),
 ('binary1077','2026-10-27_binary1077-audit','symbolic1077.py','SYMBOLIC1077.json'),
 ('interval1077','2026-10-27_binary1077-audit','intervals1077.py','INTERVAL1077.json')]
records=[]
for key,folder,script,out in jobs:
 src=Path(r'D:\Proyectos\airr-investigacion')/folder;dest=P/'replay'/key;dest.mkdir(parents=True,exist_ok=False)
 raw=(src/script).read_text(encoding='utf-8');shutil.copy2(src/script,dest/script)
 change=None
 if key=='interval1077':
  shutil.copy2(src/'integer_arithmetic1077.py',dest/'integer_arithmetic1077.py')
  shutil.copy2(src/'replay1070/CONTROL1070.json',dest/'CONTROL1070.json')
  shutil.copy2(dest/script,dest/'intervals1077_original.py')
  old="Path(r'C:\\Trabajo\\airr\\2026-10-27_binary-measurement1070\\CONTROL1070.json')"
  assert old in raw
  (dest/script).write_text(raw.replace(old,"(P/'CONTROL1070.json')"),encoding='utf-8')
  change='Only external read path rebound to a verified audit1077 payload copy; arithmetic/cases unchanged.'
 cp=subprocess.run([sys.executable,'-X','utf8',str(dest/script)],cwd=dest,capture_output=True,text=True,encoding='utf-8',timeout=180)
 (dest/'stdout.txt').write_text(cp.stdout,encoding='utf-8');(dest/'stderr.txt').write_text(cp.stderr,encoding='utf-8')
 rec={'job':key,'original_path':str(src/script),'original_sha256':sha(src/script),'executed_sha256':sha(dest/script),'adaptation':change,'returncode':cp.returncode,'output':str((dest/out).relative_to(P))}
 if (dest/out).exists():
  rec['output_byte_identical']=sha(dest/out)==sha(src/out);rec['output_json_identical']=json.loads((dest/out).read_text(encoding='utf-8'))==json.loads((src/out).read_text(encoding='utf-8'))
 records.append(rec)
 (P/'REPLAY1084.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'jobs':records,'all_passed':all(r['returncode']==0 and r.get('output_json_identical',False) for r in records),'scope':'Bounded repeated component controls, shared code lineage, not independent proof or reviewer.'},indent=2)+'\n',encoding='utf-8')
 print(key,cp.returncode,rec.get('output_json_identical'),flush=True)
 assert cp.returncode==0 and rec['output_json_identical'],rec
