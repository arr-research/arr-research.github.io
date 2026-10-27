from pathlib import Path
import json, hashlib, shutil, urllib.request, concurrent.futures
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parent
SRC=Path(r'C:\Trabajo\physmath-knowledge-tree\weyl-stability-20261024\integrations\research-radar\evidence\2026-10-27-contraction-supplement')
BASE='https://raw.githubusercontent.com/lluiseriksson/physmath-knowledge-tree/ce7f93cbdf6f28ea7342d7d63cb50c5755fe26fc/integrations/research-radar/evidence/2026-10-27-contraction-supplement/'
def sha(b): return hashlib.sha256(b).hexdigest()
def fetch(p):
    try:
        data=urllib.request.urlopen(BASE+p, timeout=45).read()
        return {'path':p,'bytes':len(data),'sha256':sha(data),'matches_local':data==(SRC/p).read_bytes()}
    except Exception as e: return {'path':p,'error':repr(e)}
manifest=json.loads((SRC/'MANIFEST1028.json').read_text(encoding='utf-8'))
checks=[]
for row in manifest['files']:
    p=row['path']; data=(SRC/p).read_bytes()
    checks.append({'path':p,'valid':len(data)==row['bytes'] and sha(data)==row['sha256']})
assert all(x['valid'] for x in checks)
dest=ROOT/'supplement'
assert not dest.exists()
shutil.copytree(SRC,dest)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    remote=list(pool.map(fetch,['MANIFEST1028.json']+[x['path'] for x in manifest['files']]))
receipt={'utc':datetime.now(timezone.utc).isoformat(),'source_commit':'ce7f93cbdf6f28ea7342d7d63cb50c5755fe26fc','local_manifest_sha256':sha((SRC/'MANIFEST1028.json').read_bytes()),'local_checks':checks,'remote_checks':remote,'all_remote_matched':all(x.get('matches_local',False) for x in remote),'scope':'Supplement manifest and listed payloads. Does not repeat the separate canonical-graph 65-file campaign.'}
(ROOT/'SUPPLEMENT-VERIFIED1031.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
rubric=Path(r'C:\Trabajo\airr-publicacion\reviewed-publications-20261026\docs\MODEL_ASSESSMENT_POLICY.md')
shutil.copy2(rubric,ROOT/'RUBRIC1031.md')
print(json.dumps({'local_payloads':len(checks),'remote_files':len(remote),'all_remote_matched':receipt['all_remote_matched'],'rubric_sha256':sha(rubric.read_bytes())}))
