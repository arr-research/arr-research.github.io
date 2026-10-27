from pathlib import Path
import subprocess,sys,json,shutil,hashlib,datetime
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
jobs=[('replay/check1033.py','CHECK1033.json'),('replay/check1035.py','CHECK1035.json'),('replay/interval1035.py','INTERVAL1035.json'),('positivity1044.py','POSITIVITY1044.json'),('integer_intervals1044.py','INTEGER_INTERVAL1044.json')]
for srcname,out in jobs:
    src=ROOT/'audit1044'/srcname;dest=ROOT/'reproduction'/src.stem;dest.mkdir(parents=True,exist_ok=True);script=dest/src.name;shutil.copy2(src,script)
    r=subprocess.run([sys.executable,str(script)],capture_output=True,text=True)
    (dest/'stdout.txt').write_text(r.stdout,encoding='utf-8');(dest/'stderr.txt').write_text(r.stderr,encoding='utf-8')
    expected=ROOT/'audit1044'/('replay/'+out if srcname.startswith('replay/') else out)
    row={'script':str(script.relative_to(ROOT)),'sha256':sha(script),'returncode':r.returncode,'output_file':str((dest/out).relative_to(ROOT)),'output_byte_identical':r.returncode==0 and (dest/out).read_bytes()==expected.read_bytes(),'output_json_identical':r.returncode==0 and json.loads((dest/out).read_text())==json.loads(expected.read_text())}
    rows.append(row);(ROOT/'REPRODUCTION1048.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Byte-identical scripts reproduced in own copies.1044 independent implementation is shared evidence, not an independent reviewer.','jobs':rows,'all_completed':len(rows)==len(jobs),'all_passed':all(x['returncode']==0 and x['output_json_identical'] for x in rows)},indent=2)+'\n')
    print(json.dumps(row),flush=True)
    assert r.returncode==0 and row['output_json_identical']
