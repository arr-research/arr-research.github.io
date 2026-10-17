# SPDX-License-Identifier: Apache-2.0
"""Recompute both datasets in a temporary folder and compare every exact record."""
from pathlib import Path
import os,sys,json,subprocess,tempfile
R=Path(__file__).parent
def normalized(obj):return {k:v for k,v in obj.items() if k!='seconds'}
with tempfile.TemporaryDirectory(prefix='six-spin-',dir=R) as td:
    output=Path(td);env=os.environ.copy();env['AIRR_OUTPUT_DIR']=str(output);env['PYTHONDONTWRITEBYTECODE']='1'
    for script,result in [('verify_stable_blowups.py','stable-blowup-checks.json'),('construct_six_spin_examples.py','six-spin-positive-examples.json')]:
        process=subprocess.run([sys.executable,'-B',str(R/script)],env=env,cwd=R,capture_output=True,text=True,encoding='utf-8')
        if process.returncode:
            print(process.stdout);print(process.stderr,file=sys.stderr);raise SystemExit(process.returncode)
        expected=json.loads((R/'results'/result).read_text(encoding='utf-8'))
        actual=json.loads((output/result).read_text(encoding='utf-8'))
        assert normalized(expected)==normalized(actual),result
        print(json.dumps(dict(check=result,status='PASS_EXACT_REPRODUCTION')))
    print('PASS: 994 base characterizations; 360 stable bases; 720 blowup classifications and blocks; four complete positive six-spin Hessian certificates.')
