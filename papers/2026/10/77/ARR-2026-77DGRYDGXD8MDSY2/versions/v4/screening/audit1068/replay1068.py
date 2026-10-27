"""Extract computational portions only; originals contain creation/sealing side effects."""
from pathlib import Path
import hashlib,json,subprocess,sys
P=Path(__file__).parent;rows=[]
settings=[('1063','2026-10-27_polynomial-phase1063','candidate1063.py','CHECK1063.json','mp.mp.dps=100',"shutil.copyfile(__file__"),('1064','2026-10-27_polynomial-phase1064-controls','interval1064.py','CONTROL1064.json',"src=Path(","shutil.copyfile(__file__"),('1066','2026-10-27_phase-tradeoff1066','tradeoff1066.py','CONTROL1066.json',"src=Path(","shutil.copyfile(__file__")]
for ident,folder,script,output,start,stop in settings:
 source=Path(r'C:\Trabajo\airr')/folder;raw=(source/script).read_text();begin=raw.index(start);end=raw.index(stop,begin);body=raw[begin:end]
 # 1066 places its output write and the copy on one line: retain only the completed write.
 body=body.rstrip().rstrip(';')+'\n'
 work=P/('replay'+ident);work.mkdir(exist_ok=True)
 imports='from pathlib import Path\nfrom fractions import Fraction\nimport datetime,hashlib,json,shutil\nimport mpmath as mp\nimport sympy as sp\nP=Path(__file__).parent\n'
 adapted=imports+body;(work/'compute.py').write_text(adapted,encoding='utf-8')
 run=subprocess.run([sys.executable,str(work/'compute.py')],capture_output=True,text=True,encoding='utf-8')
 (work/'stdout.txt').write_text(run.stdout,encoding='utf-8');(work/'stderr.txt').write_text(run.stderr,encoding='utf-8')
 record={'id':ident,'original_script_sha256':hashlib.sha256((source/script).read_bytes()).hexdigest(),'adapted_script_sha256':hashlib.sha256((work/'compute.py').read_bytes()).hexdigest(),'adaptation':'Imports and own output directory; extracted computation from start marker until first self-copy; proof generation, original mkdir, sealing and C/D copying omitted.','start_marker':start,'stop_marker':stop,'exit':run.returncode}
 rows.append(record);assert run.returncode==0,record
 expected=json.loads((source/output).read_text());actual=json.loads((work/output).read_text());record['source_utc']=expected.pop('utc');record['replay_utc']=actual.pop('utc');record['fields_identical_except_utc']=expected==actual
 assert expected==actual,ident
(P/'REPLAY1068.json').write_text(json.dumps({'scope':'Adapted computational replay, not unchanged-generator replay or independent proof.','runs':rows},indent=2)+'\n',encoding='utf-8');print(json.dumps(rows,indent=2))
