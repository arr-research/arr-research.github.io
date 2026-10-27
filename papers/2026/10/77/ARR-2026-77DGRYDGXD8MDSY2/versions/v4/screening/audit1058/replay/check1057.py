from pathlib import Path
from fractions import Fraction as F
import random,sympy as s,mpmath as m,json,datetime,importlib.util
C=Path(__file__).parent;rng=random.Random(1057);rows=[]
for n in [4,9,16,25]:
 for lam in [-F(1,n-1),F(-1,2*(n-1)),F(1,2),F(99,100)]:
  c=(1-lam)/n;b=lam+2*c;assert b>0 and lam+c>=0
  for k in range(12):
   raw=[rng.randrange(1,40) for _ in range(n)]
   if k%2:raw[0]=sum(raw[1:])+rng.randrange(1,40)
   rr=[F(x,sum(raw)) for x in raw];zz=[F(rng.randrange(-10,11)) for _ in range(n-1)];zz.append(-sum(zz))
   gap=sum(z*z/r for z,r in zip(zz,rr))/b-sum(z*z/(lam*r+c) for z,r in zip(zz,rr));assert gap>=0
   rows.append(dict(n=n,lambda_=str(lam),case=k,gap=str(gap),exact=True))
x,L,c=s.symbols('x L c');assert s.factor(s.diff((L*x+c)/(1-2*x),x)-(L+2*c)/(1-2*x)**2)==0
# Reuse the sealed1051 outward kernel, without modifying or running its top-level
# certificate campaign. Keep this dependency explicit rather than claim independence.
m.iv.dps=100
def iv(x):x=F(x);return m.iv.mpf(x.numerator)/x.denominator
def ell(d,p,e):
 a=d-1;q=a+e*e;A=1+(d*a-1)*p;FF=1+(d-1)*p
 tr=(A+FF*e*e)/(d*q);det=e*e*(1-p)*(1+(d*d-1)*p)/(d*d*q*q)
 z=m.iv.sqrt(iv(tr*tr-4*det));hi=(iv(tr)+z)/2;lo=iv(det)/hi
 return (m.iv.log(hi)-m.iv.log(lo))/z
intervals=[]
for d in [3,4]:
 e=F(1,10**30);theta=F(99,100);lam=F(1,2);ratio=iv(lam*lam)*ell(d,lam*theta,e)/ell(d,theta,e)
 benchmark=lam*lam/(lam+2*(1-lam)/(d*d));gap=ratio-iv(benchmark);assert gap.a>0
 intervals.append(dict(d=d,lambda_='1/2',e='1e-30',theta='99/100',phase='pi',ratio=str(ratio),all_Bell_benchmark=str(benchmark),gap=str(gap),exact_binary_endpoints={k:[[str(v) for v in x] for x in z._mpi_] for k,z in [('ratio',ratio),('gap',gap)]},scope='Outward100digit mpmath.iv check; dependent on the same kernel implementation, not independent audit or robustness evidence.'))
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),fisher_controls=rows,monotonicity_identity=True,positive_phase_intervals=intervals,finite_controls_not_universal_proof=True,audit_pending=True,no_score=True,poststart1054=True)
(C/'CHECK1057.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print('192 exact-rational all-noise Fisher controls and two positive-noise finitepi intervals pass; not audited.')
