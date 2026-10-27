from pathlib import Path
import argparse,datetime,hashlib,importlib.metadata,json,subprocess,sys,tempfile
ap=argparse.ArgumentParser();ap.add_argument('--workdir',type=Path,default=Path.cwd()/'proof-control-runs');ap.add_argument('--out',type=Path,default=Path.cwd()/'REPLAY1027.json');args=ap.parse_args()
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
manifest=json.loads((P/'MANIFEST1027.json').read_text())
for x in manifest['files']:
 p=P/x['path'];assert p.stat().st_size==x['bytes'] and sha(p)==x['sha256'],x['path']
origins=json.loads((P/'ORIGINS1027.json').read_text())['programs']
base=args.workdir.resolve();base.mkdir(parents=True,exist_ok=True)
work=Path(tempfile.mkdtemp(prefix='bounded-',dir=base)).resolve();work.relative_to(base)
import shutil
results=[]
for x in origins:
 target=work/x['script'];shutil.copyfile(P/x['script'],target)
 run=subprocess.run([sys.executable,'-X','utf8','-B',str(target)],cwd=work,capture_output=True)
 (work/(x['script']+'.stdout.txt')).write_bytes(run.stdout);(work/(x['script']+'.stderr.txt')).write_bytes(run.stderr)
 row=dict(script=x['script'],returncode=run.returncode,output=x['output'],matched_expected=False)
 output=work/x['output']
 if run.returncode==0 and output.exists():
  row['matched_expected']=json.loads(output.read_text())==json.loads((P/'expected'/x['output']).read_text())
  row['output_sha256']=sha(output)
 results.append(row)
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='Five fixed bounded proof checkers, not a discovery optimizer or computational campaign; no theorem/novelty/independence/grade certificate',workdir=str(work),python=sys.version,sympy=importlib.metadata.version('sympy'),original_manifest_sha256=sha(P/'MANIFEST1027.json'),all_passed=all(x['returncode']==0 and x['matched_expected'] for x in results),programs=results,all_attempts_preserved=True)
args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(all_passed=out['all_passed'],programs=len(results),receipt=str(args.out))))
if not out['all_passed']:sys.exit(1)
