"""Finite diagnostics, not proofs of infinite-dimensional capacities."""
from pathlib import Path
import json, math, hashlib
import numpy as np
from scipy.linalg import null_space

root=Path(__file__).parent
rng=np.random.default_rng(572)
def entropy(p):
    p=np.asarray(p); p=p[p>0]
    return float(-np.sum(p*np.log2(p)))
def h(p): return entropy([p,1-p])
def b(l,d): return (l+d)*h(l/(l+d)) if l+d else 0.

interlacing=[]
for n in (8,16,32,48):
 for m in (1,2,4):
  for rep in range(5):
   e=np.sort(rng.uniform(0,100,n)); e[0]=0
   a=rng.normal(size=(m,n))+1j*rng.normal(size=(m,n))
   u=null_space(a)
   mu=np.linalg.eigvalsh(u.conj().T@(e[:,None]*u))
   violation=float(np.max(mu-e[m:]))
   assert violation<1e-10
   p=rng.dirichlet(np.ones(n-m))
   assert float(p@mu)<=float(p@e[m:])+1e-10
   interlacing.append(dict(n=n,m=m,upper_violation=violation))

# Independent finite diagonal-state calculation. The RB density consists
# of a rank-one perturbation on span{|jj>} and diagonal off-diagonal labels.
# Entropy cancellations below avoid allocating a d^2 by d^2 matrix.
flag=[]
for dim in (8,16,32,64):
 for lam in (.2,.5,.8):
  for a in (.1,.3,.7):
   mean=dim/6
   p=(mean/(mean+1))**np.arange(dim); p/=p.sum()
   tau=a*p; tau[0]+=1-a
   q=1-lam
   w=lam*p+q*tau
   hjb=h(lam)+lam*entropy(p)+q*entropy(tau)-entropy(w)
   block=lam*np.outer(np.sqrt(p),np.sqrt(p))+np.diag(q*p*tau)
   eig=np.linalg.eigvalsh(block)
   hjrb=-lam*math.log2(lam)+entropy(q*p*tau)-entropy(eig)
   actual=hjb-hjrb
   error=q*float(np.sum(p*p*tau))
   bound=(1-p[0])*b(lam,q*a)-h(q*p[0]**2)
   assert actual>=bound-2e-11
   assert hjrb<=h(error)+2e-11
   flag.append(dict(dim=dim,lam=lam,a=a,entropy_reset=entropy(tau),actual_loss=actual,derived_lower=bound,error=error))

report=dict(scope='Floating-point finite diagnostics only; analytical proofs and capacity theorems required',seed=572,interlacing_cases=len(interlacing),interlacing_max_violation=max(x['upper_violation'] for x in interlacing),flag_cases=len(flag),flag_min_lower_slack=min(x['actual_loss']-x['derived_lower'] for x in flag),cases=flag,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(root/'diagnostics572.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='cases'}))
