from fractions import Fraction as Q
from pathlib import Path
from math import lcm
import json
import numpy as np
from scipy.optimize import linprog
from geometry import D
ROOT=Path(__file__).resolve().parent
a=(Q(33,40),)+(Q(7,160),)*4
b=(Q(7,20),)*2+(Q(1,10),)*3
lam=a+tuple(-x for x in reversed(b));triples=json.loads((ROOT/'horn_10.json').read_text())['triples']
rows=np.zeros((len(triples)+8,9),dtype=np.int64);rhs=[]
for t,(I,J,K) in enumerate(triples):
    for i in I:
        if i<10:rows[t,i-1]+=1
    for j in J:
        if j>1:rows[t,10-j]-=1
    rhs.append(sum(lam[k-1] for k in K))
for i in range(8):rows[len(triples)+i,i]=1;rows[len(triples)+i,i+1]=-1;rhs.append(Q(0))
unique,inverse=np.unique(rows,axis=0,return_inverse=True)
den=lcm(*(x.denominator for x in rhs));ri=np.array([int(x*den) for x in rhs],dtype=np.int64)
maximal=np.full(len(unique),-10**12,dtype=np.int64);np.maximum.at(maximal,inverse,ri)
sol=linprog(np.ones(9),A_ub=-unique.astype(float),b_ub=-maximal/den,bounds=(0,None),method='highs')
assert sol.success
s=tuple(Q(float(x)).limit_denominator(10**7) for x in sol.x)+(Q(0),)
common=lcm(den,*(x.denominator for x in s));si=np.array([int(x*common) for x in s[:-1]],dtype=np.int64)
assert min(rows@si-ri*(common//den))>=0
gap=Q(3)-sum(s)-Q(113,152)*D(a,b)
report={'a':a,'b':b,'s':s,'cost_upper':sum(s),'D':D(a,b),'stability_slack':gap}
(ROOT/'contact_midpoint.json').write_text(json.dumps(report,default=str,indent=2)+'\n')
print(report)
