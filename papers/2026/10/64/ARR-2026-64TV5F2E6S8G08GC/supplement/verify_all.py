# SPDX-License-Identifier: Apache-2.0
"""Reconstruct certificates in an isolated writable directory, then compare."""
from pathlib import Path
import json,sys,os,shutil,subprocess,tempfile
R=Path(__file__).resolve().parent
def norm(v):
 if isinstance(v,dict):return {k:norm(x) for k,x in v.items() if k not in ('seconds','elapsed_seconds')}
 if isinstance(v,list):return list(map(norm,v))
 return v
programs=[
 ('derive_initial_odd_block.py',['odd-initial-five-symbolic.json']),
 ('prove_odd_initial_large.py',['odd-initial-five-large-certificates.json']),
 ('certify_initial_odd_small.py',['odd-initial-small-certificates.json']),
 ('check_compression.py',['initial-compression-checks.json','seven-state-positive-target.json','compression-results.json']),
 ('verify_smaller_block_failures.py',['smaller-block-failures.json'])]
with tempfile.TemporaryDirectory(prefix='cycle-certificate-',dir=R) as tmp:
 T=Path(tmp)
 for p in R.iterdir():
  if p.is_file():shutil.copy2(p,T/p.name)
 env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
 for script,outputs in programs:
  result=subprocess.run([sys.executable,'-B',str(T/script)],cwd=T,env=env,text=True,encoding='utf-8',capture_output=True)
  if result.returncode:
   print(result.stdout);print(result.stderr,file=sys.stderr);raise SystemExit(result.returncode)
  for name in outputs:
   expected=json.loads((R/name).read_text(encoding='utf-8'));actual=json.loads((T/name).read_text(encoding='utf-8'))
   assert norm(actual)==norm(expected),'Exact mismatch: '+name
   print(json.dumps(dict(file=name,status='PASS_EXACT_REPRODUCTION')),flush=True)
 print('PASS: matrices, six sign certificates, eighteen infinite tails, 42 exceptions, eighteen k=2 cases, three compression checks and the full seven-state witness.',flush=True)
