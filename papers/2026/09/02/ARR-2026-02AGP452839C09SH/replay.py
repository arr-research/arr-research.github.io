"""Replay scientific checks in a disposable copy, preserving the deposit."""
from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess,sys,tempfile,time
ROOT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--fresh-lr',action='store_true');parser.add_argument('--report',type=Path);args=parser.parse_args()
checks=[('ternary_verify.py', 'ternary_certificate.json'), ('independent_ternary_review.py', 'independent_ternary_review.json')]
rows=[]
with tempfile.TemporaryDirectory(prefix='arr_cycle4_replay_') as tmp:
    scratch=Path(tmp);shutil.copytree(ROOT/'research',scratch/'research')
    for script,output in checks:
        extra=['--fresh-lr'] if args.fresh_lr and script=='review/independent_review.py' else []
        started=time.monotonic()
        proc=subprocess.run([sys.executable,script]+extra,cwd=scratch/'research',env={**os.environ,'PYTHONIOENCODING':'utf-8'},capture_output=True,text=True,encoding='utf-8')
        if proc.returncode:raise RuntimeError(proc.stdout+proc.stderr)
        data=json.loads((scratch/'research'/output).read_text(encoding='utf-8'))
        assert data['status']=='PASS'
        row={'script':script,'status':'PASS','seconds':time.monotonic()-started,'script_sha256':hashlib.sha256((ROOT/'research'/script).read_bytes()).hexdigest(),'summary':{k:v for k,v in data.items() if k in ['check_count','coefficient','integer_Horn_checks','lr_source','lr_cache_reason','LR_triples','geometry_subsets','POVM_outcomes']}}
        rows.append(row);print(json.dumps(row),flush=True)
report={'status':'PASS','checks':rows,'manuscript_sha256':hashlib.sha256((ROOT/'paper.md').read_bytes()).hexdigest(),'canonical_sha256':hashlib.sha256((ROOT/'paper.pdf').read_bytes()).hexdigest(),'scope':'Exact finite or symbolic checks; universal written arguments remain mathematical dependencies.'}
if args.report:args.report.resolve().write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
