from pathlib import Path
import sys,json,datetime,time
p=Path(__file__).parent;sys.path.insert(0,str(p/'reviewer'))
from chain_own import chamber_vertices_exact,layering,chain_feasible_exact,inst
m=9;S=[tuple(f) for f in json.loads((p/'author/closed_m9_z0.json').read_text())];total=0;t=time.time()
print('UTC',datetime.datetime.now(datetime.timezone.utc).isoformat(),flush=True)
for i,f in enumerate(S):
 V=chamber_vertices_exact(f,[h for h in S if h!=f],m);ch=layering(f,m);assert all(chain_feasible_exact(inst(ch,v[:m],v[m:])) for v in V);total+=len(V)
 print('m9 base chain',i+1,'of',len(S),'vertices',len(V),'cumulative',total,'elapsed',round(time.time()-t,1),flush=True)
assert total==969
print('PASS m9 all base chains; z1,z2 follow by unused zero padding and independently checked equal coefficient sets')
