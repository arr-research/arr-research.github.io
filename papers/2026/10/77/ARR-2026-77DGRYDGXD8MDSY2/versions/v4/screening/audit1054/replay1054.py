from pathlib import Path
import json,subprocess,hashlib,sys
P=Path(__file__).parent;out=P/'replay';out.mkdir(exist_ok=True)
tasks=[('2026-10-27_local-phase1051','check1051.py','CHECK1051.json'),('2026-10-27_local-phase1051','ambient1051.py','AMBIENT1051.json'),('2026-10-27_local-phase1051','interval1051.py','INTERVAL1051.json'),('2026-10-27_bell-benchmark1052','check1052.py','CHECK1052.json')]
rows=[]
for dirname,script,result in tasks:
 src=Path(r'D:\Proyectos\airr-investigacion')/dirname;raw=(src/script).read_bytes();(out/script).write_bytes(raw)
 r=subprocess.run([sys.executable,'-X','utf8',str(out/script)],cwd=out,capture_output=True)
 (out/(script+'.stdout')).write_bytes(r.stdout);(out/(script+'.stderr')).write_bytes(r.stderr)
 rec={'script':script,'sha256':hashlib.sha256(raw).hexdigest(),'exit':r.returncode}
 if r.returncode==0:
  old=json.loads((src/result).read_text());new=json.loads((out/result).read_text());rec['original_utc']=old.pop('utc',None);rec['replay_utc']=new.pop('utc',None);rec['all_payload_fields_except_utc_equal']=old==new
 rows.append(rec);(P/'REPLAY1054.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8');print(rec,flush=True)
 assert r.returncode==0 and rec['all_payload_fields_except_utc_equal']
