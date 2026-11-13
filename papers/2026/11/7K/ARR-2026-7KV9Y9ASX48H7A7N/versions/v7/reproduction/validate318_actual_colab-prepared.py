"""Read-only validation of an actual returned production packet on owned Colab."""
import os,sys,json,zipfile,hashlib,time,resource
from pathlib import Path
root=Path('/content/tep318-actual-return-validation')
bundle=Path('/content/tep318-actual-return-inputs.zip')
if os.name!='posix' or not Path('/content').is_dir() or root.exists():raise RuntimeError('Fresh owned Colab required')
root.mkdir();start=time.perf_counter()
expected={'production.zip','source-manifest.json','validate_return318D.py','outer-report.json'}
expected|={n+ext for n in ('allocation','execution','download','release','backend-readback') for ext in ('.log','.stderr.log','.exit')}
with zipfile.ZipFile(bundle) as z:
    names=z.namelist()
    if len(names)!=len(set(names)) or set(names)!=expected:raise RuntimeError('Exact transport input set')
    for name in names:
        with (root/name).open('xb') as f:f.write(z.read(name))
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
if h(root/'validate_return318D.py')!='88c13dbd8fe535250754329eed9ac793c880b2873372d2aa7cf6986675fb30e8':raise RuntimeError('Validator pin')
if h(root/'source-manifest.json')!='ab5048598f630629f4c4ed7d9419508a2a85dc45d0202b24798492506be61fa4':raise RuntimeError('Source manifest pin')
sys.path.insert(0,str(root));import validate_return318D as v
result=v.validate(root/'production.zip',root,root/'source-manifest.json',[root/'uncreated-extraction',root/'uncreated-delivery',root/'uncreated-captures',root/'uncreated-parent.json'])
result.update(input_bundle_sha256=h(bundle),validator_sha256=h(root/'validate_return318D.py'),wall_seconds=time.perf_counter()-start,max_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,execution_environment='Owned Colab Linux',mathematical_test=False,visual_inspection=False,backend_inactivity='Parent must separately inspect actual production and this validation runtime readbacks')
with (root/'result.json').open('x',encoding='utf-8') as f:json.dump(result,f,indent=2)
print(json.dumps(result))
