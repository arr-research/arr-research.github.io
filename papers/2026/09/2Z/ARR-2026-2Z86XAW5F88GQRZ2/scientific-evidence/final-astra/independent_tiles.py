from pathlib import Path
from functools import lru_cache
import json,re,datetime
p=Path(__file__).parent
print('UTC',datetime.datetime.now(datetime.timezone.utc).isoformat(),flush=True)
@lru_cache(None)
def lr_cell(a,b,c):
 a=a+(0,)*(len(c)-len(a)); b=tuple(x for x in b if x)
 if sum(c)-sum(a)!=sum(b) or any(x>y for x,y in zip(a,c)):return 0
 cells=[(i,j) for i in range(len(c)) for j in range(c[i]-1,a[i]-1,-1)];filled={};used=[0]*len(b)
 def walk(k):
  if k==len(cells):return int(tuple(used)==b)
  i,j=cells[k];total=0
  for v in range(len(b)):
   if used[v]>=b[v] or (v and used[v]>=used[v-1]):continue
   if (i,j+1) in filled and v>filled[i,j+1]:continue
   if (i-1,j) in filled and v<=filled[i-1,j]:continue
   filled[i,j]=v;used[v]+=1;total+=walk(k+1);used[v]-=1;del filled[i,j]
  return total
 return walk(0)
part=lambda I:tuple(i-j for i,j in zip(I[::-1],range(len(I),0,-1)))
count=0
for f in sorted((p/'author').glob('certs_m*_z*.json')):
 m,z=map(int,re.search(r'm(\d+)_z(\d+)',f.name).groups());d=m+3+z
 for key,cert in json.loads(f.read_text()).items():
  co=[0]*(d-1);rhs=[0]*d
  for tile in cert['tiles']:
   I,J,K=[tuple(tile[k]) for k in ['I','J','K']];assert lr_cell(part(I),part(J),part(K))>0
   for i in I:
    if i<d:co[i-1]+=1
   for j in J:
    if j>1:co[d-j]-=1
   for k in K:rhs[k-1]+=1
  # lambda negative tail = -b3,-b2,-b1, eliminate b3
  beta=[-rhs[-1],-rhs[-2],-rhs[-3]]
  canonical=[rhs[i]+beta[2] for i in range(m)]+[beta[0]-beta[2],beta[1]-beta[2]]
  assert canonical==json.loads(key) and max(co)<=1;count+=1
 print(f.name,'PASS',flush=True)
print('PASS independent cell-tableau and integer certificate assembly',count,'certificates',lr_cell.cache_info(),flush=True)
