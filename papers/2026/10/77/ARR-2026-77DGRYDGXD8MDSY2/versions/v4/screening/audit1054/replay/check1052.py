from pathlib import Path
import sympy as s,json,datetime,random
from fractions import Fraction as F
C=Path(__file__).parent
x=s.symbols('x');phi=x*(1-x)/(1-2*x)
assert s.factor(s.diff(phi/x,x)-1/(1-2*x)**2)==0
# Exact-rational sum-zero controls, including one mass >1/2.
rng=random.Random(1052);rows=[]
for n in [4,9,16,25]:
 for k in range(20):
  raw=[rng.randrange(1,40) for _ in range(n)]
  if k%2:raw[0]=sum(raw[1:])+rng.randrange(1,40)
  total=sum(raw);r=[F(v,total) for v in raw]
  zz=[F(rng.randrange(-20,21)) for _ in range(n-1)];zz.append(-sum(zz))
  gap=sum(z*z/p-z*z/(1-p) for z,p in zip(zz,r));assert gap>=0
  rows.append(dict(n=n,case=k,max_probability=str(max(r)),fisher_gap=str(gap),exact=True))
# The local channel on the Bell probabilities is precisely complement averaging.
for n in [4,9,16]:
 K=(s.ones(n)-s.eye(n))/(n-1)
 for i in range(n):
  for j in range(i):assert sum(abs(v) for v in K[:,i]-K[:,j])/2==s.Rational(1,n-1)
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),controls=rows,phi_monotonicity_symbolic=True,Dobrushin_column_controls=True,scope='Finite exact controls are not the universal proof; see PROOF1052. Classical benchmark is prior machinery, not a novelty claim.',audit_pending=True,score=None)
(C/'CHECK1052.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print('80 exact-rational simplex controls and three Bell-kernel column checks pass.')
