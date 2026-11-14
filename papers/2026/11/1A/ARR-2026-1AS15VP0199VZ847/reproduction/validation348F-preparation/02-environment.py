import platform, shutil, subprocess, sys, os, json
from datetime import datetime, timezone
require(platform.node()==OWNED_RUNTIME_NODE, 'Owned validation runtime changed')
probes=[]
for mode,args in [('normal',[]),('optimized',['-O'])]:
    argv=[sys.executable,*args,'-c','import sys;print(sys.flags.optimize)']
    child=subprocess.run(argv,capture_output=True,text=True,timeout=30)
    probes.append({'mode':mode,'argv':argv,'actual_exit':child.returncode,'stdout':child.stdout,'stderr':child.stderr})
obs={'observed_at':datetime.now(timezone.utc).isoformat(),'hostname':platform.node(),'platform':platform.platform(),
     'python':sys.version,'notebook_optimize':sys.flags.optimize,'PYTHONOPTIMIZE':os.environ.get('PYTHONOPTIMIZE'),'probes':probes}
with (ROOT/'environment.observation.json').open('x',encoding='utf-8') as stream:
    json.dump(obs,stream,indent=2);stream.write('\n')
print(json.dumps(obs))
require(obs['PYTHONOPTIMIZE'] is None and obs['notebook_optimize']==0 and
        all(p['actual_exit']==0 and p['stderr']=='' and p['stdout']==str(i)+'\n' for i,p in enumerate(probes)),
        'Environment modes invalid; preserve and stop')
