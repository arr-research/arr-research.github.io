"""Replay exact public files in a separate writable copy, preserving downloads."""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,sys
import sympy,mpmath
ROOT=Path(__file__).resolve().parent
source=ROOT/'public-supplement'
work=ROOT/'public-replay'
work.mkdir(exist_ok=False)
names=['README.txt','requirements.txt','symbolic993.py','verify993.py','verify-certificates991.py',
       'PETZ-CERTIFICATE991.json','VARIANCE-CERTIFICATE991.json','SYMBOLIC993.json','VERIFY993.json','VERIFIED991.json']
for name in names:shutil.copy2(source/name,work/name)
assert sympy.__version__=='1.14.0' and mpmath.__version__=='1.3.0'
runs=[]
for script in ['symbolic993.py','verify993.py','verify-certificates991.py']:
    result=subprocess.run([sys.executable,script],cwd=work,capture_output=True,timeout=120)
    log=work/(script+'.run01.log')
    log.write_bytes(result.stdout+b'\nSTDERR:\n'+result.stderr)
    runs.append({'script':script,'exit_code':result.returncode,'log':str(log.relative_to(ROOT))})
    print(script,result.returncode,flush=True)
comparisons=[]
for name in ['SYMBOLIC993.json','VERIFY993.json','VERIFIED991.json']:
    original=(source/name).read_bytes()
    current=(work/name).read_bytes()
    comparisons.append({'name':name,'download_sha256':hashlib.sha256(original).hexdigest(),
                        'generated_sha256':hashlib.sha256(current).hexdigest(),
                        'same_json_value':json.loads(original)==json.loads(current),
                        'same_after_LF_normalization':original==current.replace(b'\r\n',b'\n')})
report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runs':runs,'outputs':comparisons,
        'runtime':{'python':sys.version,'sympy':sympy.__version__,'mpmath':mpmath.__version__},
        'scope':'Three public verifier scripts, executed once each in copied folder; no discovery optimizer or later-extension script run.'}
with (ROOT/'PUBLIC-REPLAY1006.json').open('x',encoding='utf-8') as f:json.dump(report,f,ensure_ascii=False,indent=2)
assert all(x['exit_code']==0 for x in runs)
assert all(x['same_json_value'] and x['same_after_LF_normalization'] for x in comparisons)
print('All public replays passed and reproduce the stored values.')
