"""Finite noncommuting input checks with an exactly summed infinite thermal tail.
No capacity optimizer, universal code, interval proof or novelty certificate.
"""
from pathlib import Path
import math,json,hashlib
import numpy as np
import mpmath as mp
r=Path(__file__).parent;rng=np.random.default_rng(583)
def ent(weights):
 w=np.asarray(weights,float)
 assert w.min(initial=0)>-1e-9
 w=w[w>1e-15]
 return float(-np.sum(w*np.log2(w)))
def se(x):return ent(np.linalg.eigvalsh((x+x.conj().T)/2))
def h(x):return ent([x,1-x])
def b(u,v):return (u+v)*h(u/(u+v)) if u+v else 0.
def g(E):return math.log2(E+1)+E*math.log2(1+1/E)
def tail_entropy(scale,start,E):
 if scale==0:return 0.
 logr=-math.log1p(1/E)/math.log(2);mass=math.exp(-start*math.log1p(1/E))
 return scale*mass*(-math.log2(scale/(E+1))-(start+E)*logr)
def smix(E,a):return ent([1-a+a/(E+1)])+tail_entropy(a,1,E)
records=[]
for E in (2.,8.,32.):
 for dim in (2,4,6):
  for lam in (.1,.4,.7,.9):
   for a in (0.,.07,.5,1.):
    z=rng.normal(size=(dim,dim))+1j*rng.normal(size=(dim,dim))
    rho=z@z.conj().T;rho/=np.trace(rho)
    mu=float(np.trace(np.diag(np.arange(dim))@rho).real)
    if mu>E:
     factor=E/mu;rho*=factor;rho[0,0]+=1-factor;mu=E
    vals,U=np.linalg.eigh(rho);sqrt=(U*np.sqrt(np.maximum(vals,0)))@U.conj().T
    psi=sqrt.T.reshape(-1);q=1-lam
    geo=np.exp(-np.arange(dim)*math.log1p(1/E))/(E+1)
    taun=a*geo;taun[0]+=1-a
    out=lam*rho+q*np.diag(taun)
    joint=lam*np.outer(psi,psi.conj())+q*np.kron(rho.T,np.diag(taun))
    Hr=se(rho);SB=se(out)+tail_entropy(q*a,dim,E)
    outside=q*a*math.exp(-dim*math.log1p(1/E))*Hr+tail_entropy(q*a,dim,E)
    SRB=se(joint)+outside
    I=Hr+SB-SRB
    F=lam*Hr+SB-q*smix(E,a)-h(lam)
    rem=I-F;err=q*float(np.trace(rho@rho@np.diag(taun)).real)
    upperF=2*lam*g(E)-b(lam,q*a)+q*h(a/(E+1))
    assert F<=upperF+5e-11
    assert -5e-11<=rem<=h(err)+5e-11
    assert I<=2*lam*Hr+5e-11
    d=g(E)-Hr;D=-Hr+math.log2(E+1)+mu*math.log2(1+1/E)
    largest=float(vals.max()) if mu<E else float(np.linalg.eigvalsh(rho).max())
    assert largest*math.log2(E+1)-h(largest)<=D+5e-11
    records.append(dict(E=E,dim=dim,lam=lam,a=a,F=F,global_F_upper=upperF,mutual_information=I,flag_remainder=rem,Fano_upper=h(err)))

mp.mp.dps=70
def mh(x):return -x*mp.log(x,2)-(1-x)*mp.log(1-x,2) if 0<x<1 else mp.mpf(0)
def mb(u,v):return (u+v)*mh(u/(u+v)) if u+v else mp.mpf(0)
thermal=[]
for E0 in (10,1000,1000000):
 E=mp.mpf(E0);p0=1/(E+1)
 for l0 in ('.1','.5','.9'):
  lam=mp.mpf(l0);q=1-lam
  for a0 in ('0','.0001','.1','.5','.9999','1'):
   a=mp.mpf(a0);v=(1-p0)*mb(lam,q*a)+mb(lam*p0,q*(1-a+a*p0))
   assert v<=mb(lam,q*a)+mb(lam*p0,q)+mp.mpf('1e-60')
   thermal.append(dict(E=E0,lam=l0,a=a0,branch_loss=str(v),limit=str(mb(lam,q*a)),error=str(v-mb(lam,q*a))))

tails=[]
for alpha in (1.1,1.5,2.,4.):
 for dim in (32,128,512):
  for rep in range(8):
   p=np.sort(rng.dirichlet(np.full(dim,.3)))[::-1];m=dim//4
   R=float(np.sum(p**alpha));t=(m+1)**(1-alpha)
   bound=1-max(R-t,0)**(1/alpha)
   actual=float(p[m:].sum());assert actual<=bound+1e-11
   tails.append(dict(alpha=alpha,dim=dim,tail=actual,upper=bound))

clipping=[]
for E in (10,1000,1000000):
 A=math.log2(E+1);G=g(E);m=int(E/math.log(E+1));L=math.log2(m+1)
 for B in (0,.2,1,A/2,A,G,G+1,100*G):
  target=min(1,B/A);lower=min(1,max(0,(B-1)/G));upper=min(1,B/L)
  assert 0<=target-lower<=(G-A+1)/G+1e-12
  assert 0<=upper-target<=1-L/A+1e-12
  clipping.append(dict(E=E,B=B,lower=lower,target=target,upper=upper))

doc=dict(status='PASS',scope='Finite floating/high-precision stress checks; not a capacity proof or optimizer',quantum_cases=len(records),thermal_cases=len(thermal),tail_cases=len(tails),clipping_cases=len(clipping),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),quantum=records,thermal=thermal,tails=tails,clipping=clipping)
(r/'checks583.json').write_text(json.dumps(doc,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in doc.items() if k not in ['quantum','thermal','tails','clipping']}))
