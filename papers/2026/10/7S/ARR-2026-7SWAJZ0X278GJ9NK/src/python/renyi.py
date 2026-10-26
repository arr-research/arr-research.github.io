from pathlib import Path
import numpy as np,math,json,hashlib,shutil,datetime
r=Path(__file__).parent
rng=np.random.default_rng(574)
def S(p,a):return math.log2(float(np.sum(p**a)))/(1-a)
tails=[]
for a in (.25,.5,.75):
 for n in (8,64,512):
  for rep in range(8):
   p=np.sort(rng.dirichlet(np.full(n,.2)))[::-1]
   m=max(1,n//4);R=float(np.sum(p**a))
   bound=a/(1-a)*R**(1/a)*m**(-(1-a)/a)
   actual=float(p[m:].sum());assert actual<=bound+1e-12
   tails.append(dict(a=a,n=n,tail=actual,bound=bound))
for a in (1.5,2.,4.):
 for n in (8,64,512):
  for rep in range(8):
   p=np.sort(rng.dirichlet(np.full(n,.2)))[::-1]
   bound=2**(-S(p,a));assert p[0]>=bound-1e-12
rows=[]
for a in (.25,.5,.75,1.5,2.,4.):
 for atom_complement in (.03,.15,.5):
  for E in (1e2,1e4,1e6,1e8):
   t=atom_complement;p0=1/(E+1);logr=-math.log1p(1/E)
   diffuse=t**a*p0**a*math.exp(a*logr)/(-math.expm1(a*logr))
   value=math.log2((1-t+t*p0)**a+diffuse)/(1-a)
   target=math.log2(E)+(a*math.log2(t)-math.log2(a))/(1-a) if a<1 else -a/(a-1)*math.log2(1-t)
   rows.append(dict(a=a,mass=t,E=E,entropy=value,asymptotic=target,error=value-target))
doc=dict(scope='Finite floating diagnostics of spectral estimates and geometric-series asymptotics, not capacity proof',tail_cases=len(tails),largest_eigenvalue_cases=72,asymptotic_cases=rows,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(r/'renyi-check574.json').write_text(json.dumps(doc,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status="PASS",tail_cases=len(tails),largest_eigenvalue_cases=72,asymptotic_cases=len(rows))))
