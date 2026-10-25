from pathlib import Path
from itertools import product
import sympy as s
import json,time
r=Path(__file__).resolve().parent; start=time.time(); Q=s.Rational
words=list(product(range(3),repeat=3)); flat={w:i for i,w in enumerate(words)}
w=(-1+s.sqrt(3)*s.I)/2
def simp(x): return s.expand(x).simplify()
code=[s.SparseMatrix(27,1,{(flat[(t,(t+j)%3,(t+2*j)%3)],0):1 for t in range(3)}) for j in range(3)]
Hb={}
for k,l in product(range(3),repeat=2):
 out=s.zeros(27)
 for ii in range(27):
  if not code[k][ii]:continue
  for jj in range(27):
   if not code[l][jj]:continue
   fs=[]
   for u,v in zip(words[ii],words[jj]):
    f=s.eye(3)*int(u==v);f[u,v]-=Q(1,2);fs.append(f)
   out+=s.kronecker_product(*fs)/3
 Hb[k,l]=out
Ts={}
for charge,p in product(range(3),repeat=2):
 T=s.zeros(27,3)
 for j,t in product(range(3),repeat=2):
  T[flat[(t,(t+j)%3,(t+charge-j)%3)],j]=simp(w**((-p*t)%3))
 assert (T.H*T).applyfunc(simp)==3*s.eye(3)
 Ts[charge,p]=T
records=[]
for sector,T in Ts.items():
 blocks={key:(T.H*H*T/3).applyfunc(simp) for key,H in Hb.items()}
 # Exact invariant-sector relation on all nine logical matrix units.
 for key,H in Hb.items():assert (H*T-T*blocks[key]).applyfunc(simp)==s.zeros(27,3)
 commutative=all((A*B-B*A).applyfunc(simp)==s.zeros(3) for A in blocks.values() for B in blocks.values())
 if sector==(0,0):
  for (k,l),B in blocks.items():
   E=s.zeros(3);E[k,l]=1
   assert B==int(k==l)*s.eye(3)/2+E/8
 rec={'sector':sector,'image_commutative':commutative,'blocks':{str(key):[[str(v) for v in row] for row in B.tolist()] for key,B in blocks.items()}}
 records.append(rec)
 print(sector,commutative,flush=True)
out={'status':'PASS_EXACT_UNIVERSAL_H_SECTOR_REDUCTION','logical_matrix_units':9,'sectors':records,'all_cross_sector_actions_zero':True,'scope':'Exact linear map H for arbitrary logical operators only. Does not prove co-Choi signed comparison.','seconds':time.time()-start}
(r/'werner412-h-sector.json').write_text(json.dumps(out,indent=2)+'\n')
print('seconds',time.time()-start,flush=True)
