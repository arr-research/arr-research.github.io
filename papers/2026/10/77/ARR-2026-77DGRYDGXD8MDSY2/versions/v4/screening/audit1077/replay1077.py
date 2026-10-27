from pathlib import Path
import hashlib,json,subprocess,sys
P=Path(__file__).parent;rows=[]
for ident,folder,script,output,start in [('1070','2026-10-27_binary-measurement1070','measurement1070.py','CONTROL1070.json','src=Path('),('1073','2026-10-27_binary-ambient1073','ambient1073.py','AMBIENT1073.json','rows=[]')]:
 source=Path(r'C:\Trabajo\airr')/folder;raw=(source/script).read_text();a=raw.index(start);b=raw.index('shutil.copyfile(__file__',a);body=raw[a:b].rstrip().rstrip(';')+'\n';work=P/('replay'+ident);work.mkdir(exist_ok=True)
 adapted='from pathlib import Path\nfrom fractions import Fraction\nimport datetime,json,hashlib,shutil\nimport sympy as s\nP=Path(__file__).parent\n'+body
 (work/'compute.py').write_text(adapted,encoding='utf-8');run=subprocess.run([sys.executable,str(work/'compute.py')],capture_output=True,text=True,encoding='utf-8');(work/'stdout.txt').write_text(run.stdout,encoding='utf-8');(work/'stderr.txt').write_text(run.stderr,encoding='utf-8')
 rec={'id':ident,'original_script_sha256':hashlib.sha256((source/script).read_bytes()).hexdigest(),'adapted_sha256':hashlib.sha256((work/'compute.py').read_bytes()).hexdigest(),'adaptation':'Extracted computation only, own directory, omitted proof generation and original creation/sealing/copying.','start_marker':start,'exit':run.returncode};rows.append(rec);assert run.returncode==0,rec
 expected=json.loads((source/output).read_text());actual=json.loads((work/output).read_text());rec['source_utc']=expected.pop('utc');rec['replay_utc']=actual.pop('utc');rec['fields_identical_except_utc']=expected==actual;assert expected==actual
(P/'REPLAY1077.json').write_text(json.dumps({'runs':rows},indent=2)+'\n',encoding='utf-8');print(json.dumps(rows,indent=2))
