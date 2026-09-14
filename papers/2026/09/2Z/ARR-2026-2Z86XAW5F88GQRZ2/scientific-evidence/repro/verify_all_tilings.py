from pathlib import Path
import sys,json,re
from fractions import Fraction as Q
W=Path(__file__).parent
sys.path.insert(0,str(W/'author'))
from lr import lr,part
from lr2 import lr2
from families2 import gen2
total=tiles=0
for p in sorted((W/'author').glob('certs_m*_z*.json')):
 m,z=map(int,re.search(r'certs_m(\d+)_z(\d+)',p.name).groups());d=m+z+3
 cert=json.loads(p.read_text());S=set(map(tuple,json.loads((W/f'author/closed_m{m}_z{0 if z==0 else 1}.json').read_text())))
 assert set(tuple(json.loads(f)) for f in cert)==S
 for f,c in cert.items():
  target=tuple(json.loads(f));sc=[0]*(d+1);rhs=[0]*(m+3)
  for t in c['tiles']:
   I,J,K=map(tuple,(t['I'],t['J'],t['K']));r=len(I)
   assert len(J)==len(K)==r and 1<=r<d
   assert all(tuple(sorted(set(a)))==a and min(a)>=1 and max(a)<=d for a in (I,J,K))
   assert sum(I)+sum(J)==sum(K)+r*(r+1)//2
   a,b=lr(part(I),part(J),part(K)),lr2(part(I),part(J),part(K));assert a==b and a>0
   for i in I:
    if i<d:sc[i]+=1
   for j in J:
    if j>1:sc[d+1-j]-=1
   for k in K:
    if k<=m:rhs[k-1]+=1
    elif k>m+z:rhs[m+d-k]-=1
   tiles+=1
  canon=tuple(x+rhs[m+2] for x in rhs[:m])+(rhs[m]-rhs[m+2],rhs[m+1]-rhs[m+2])
  assert canon==target and all(x<=1 for x in sc[1:d]),(p,target,canon,sc)
  total+=1
 print(p.name,'forms',len(cert),'exact PASS',flush=True)
print('TOTAL exact certificates',total,'tiles',tiles)
for m in range(3,10):
 sets=[set(map(tuple,json.loads((W/f'author/closed_m{m}_z{z if z!=2 or m!=3 else 1}.json').read_text()))) for z in (0,1,2)]
 assert sets[1]==sets[2] and sets[1]<=sets[0]
 assert set(gen2(m))==sets[1]
 print('set/family comparison',m,[len(s) for s in sets],'z0 extras',sets[0]-sets[1])
