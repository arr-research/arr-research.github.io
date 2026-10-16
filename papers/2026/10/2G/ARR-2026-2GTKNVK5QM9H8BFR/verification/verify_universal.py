"""Deterministic finite checks. Numerical checks are not continuum proofs."""
from pathlib import Path
import itertools,math,json,time,sys
import numpy as np
import scipy.linalg as la
ROOT=Path(__file__).parent
sys.path.insert(0,str(ROOT))
from schur_checks import projectors,random_channel,choi,product_choi,dims,parts
rng=np.random.default_rng(45151026)
def add(p,q,scale=1):
 r=p.copy()
 for e,v in q.items():r[e]=r.get(e,0)+scale*v
 return r
def mul(p,q):
 r={}
 for e,v in p.items():
  for f,w in q.items():
   ef=tuple(a+b for a,b in zip(e,f));r[ef]=r.get(ef,0)+v*w
 return r
def power(p,a,k):
 r={(0,)*k:1}
 for _ in range(a):r=mul(r,p)
 return r
def detpoly(ks,rows=None,cols=None):
 d=len(ks[0]);k=len(ks);rows=list(range(d)) if rows is None else rows;cols=list(range(d)) if cols is None else cols
 r={}
 for perm in itertools.permutations(range(len(rows))):
  sign=(-1)**sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
  p={(0,)*k:sign}
  for i,j in enumerate(perm):
   q={tuple(int(b==a) for b in range(k)):K[rows[i],cols[j]] for a,K in enumerate(ks)}
   p=mul(p,q)
  r=add(r,p)
 return r
def gn(p):return sum(abs(v)**2*math.prod(math.factorial(x) for x in e) for e,v in p.items())
def gaussian_balanced(ks,n):
 d=len(ks[0]);k=len(ks);a,r=divmod(n,d)
 base=power(detpoly(ks),a,k)
 total=0.
 for rows in itertools.combinations(range(d),r):
  for cols in itertools.combinations(range(d),r):total+=gn(mul(base,detpoly(ks,rows,cols)))
 return float(total/(math.factorial(n)*math.comb(d,r)))
def cmat(ks):
 k=len(ks);C=np.zeros((k,k),complex)
 for a in range(k):
  C[a,a]=la.det(ks[a])
  for b in range(a):C[a,b]=C[b,a]=(la.det(ks[a]+ks[b])-C[a,a]-C[b,b])/2
 return C
def qubit_even(sig,a):
 coeff=np.zeros(a+1);coeff[0]=1.
 for s in sig:
  term=np.array([math.comb(2*j,j)*s**(2*j) for j in range(a+1)])
  coeff=np.convolve(coeff,term)[:a+1]
 return coeff[a]/math.comb(2*a,a)
def channels(d):
 E=np.eye(d)
 out=[('unitary',[E]),('depolarizing',[np.outer(E[i],E[j])/np.sqrt(d) for i in range(d) for j in range(d)]),('pure_replacer',[np.outer(E[0],E[j]) for j in range(d)])]
 for k in [2,3,4]:
  for j in range(3):out.append((f'random-k{k}-{j}',random_channel(d,k)))
 if d==2:
  for gamma in [.1,.5,.9]:out.append((f'amplitude-{gamma}',[np.diag([1,np.sqrt(1-gamma)]),np.array([[0,np.sqrt(gamma)],[0,0]])]))
 if d>=3:
  out.append(('werner_holevo',[(np.outer(E[i],E[j])-np.outer(E[j],E[i]))/np.sqrt(d-1) for i in range(d) for j in range(i+1,d)]))
 return out
def main():
 start=time.time();rows=[];worst=0.;qrows=[]
 for d,n in [(2,1),(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)]:
  ps=projectors(d,n);a,r=divmod(n,d);bal=(a+1,)*r+(a,)*(d-r)
  for name,ks in channels(d):
   A=product_choi(choi(ks),d,n)
   vals={str(lam):float(np.sum(D.T*A).real/(q*m)) for lam,q,m,D in ps}
   b=vals[str(bal)];g=gaussian_balanced(ks,n)
   err=abs(b-g);worst=max(worst,err)
   assert err<2e-10,(d,n,name,b,g)
   assert b<=min(vals.values())+2e-10,(d,n,name,vals)
   rows.append(dict(d=d,n=n,channel=name,sectors=vals,gaussian=g,error=err))
  print('direct Choi/Gaussian and balanced minimum',d,n,flush=True)
 Y=np.array([[0,-1j],[1j,0]]);YY=np.kron(Y,Y)
 for name,ks in channels(2):
  sig=la.svdvals(cmat(ks));delta=max(sig)
  rho=choi(ks)/2;ev,V=la.eigh(rho);sr=(V*np.sqrt(np.maximum(ev,0)))@V.conj().T
  H=sr@YY@rho.conj()@YY@sr;H=(H+H.conj().T)/2
  roots=np.sqrt(np.maximum(la.eigvalsh(H),0))[::-1]
  spinerr=max(abs(np.pad(sig,(0,4-len(sig)))-roots))
  assert spinerr<3e-8,(name,spinerr,sig,roots)
  for a in range(1,7):
   n=2*a;g=gaussian_balanced(ks,n);f=qubit_even(sig,a)
   assert abs(g-f)<2e-10
   N=math.comb(n+len(ks)-1,len(ks)-1)
   assert delta**n-2e-10<=g<=N*delta**n+2e-10
   qrows.append(dict(channel=name,n=n,delta=float(delta),gaussian=g,takagi=float(f),spin_flip_error=float(spinerr)))
 print('qubit exact polynomial moments complete',flush=True)
 # Exact rational normalized Schur inequality via character formula for integer x.
 from fractions import Fraction
 from schur_checks import char,cycles
 inequalities=0
 for d in [2,3,4]:
  for n in range(1,7):
   a,r=divmod(n,d);bal=(a+1,)*r+(a,)*(d-r)
   for x in [tuple(range(1,d+1)),(0,)+(1,)*(d-1),(1,)*d,(1,)*(d-1)+(5,)]:
    eb=math.prod(x)**a*sum(math.prod(x[j] for j in I) for I in itertools.combinations(range(d),r))
    target=Fraction(eb,math.comb(d,r))
    for lam in parts(n,d):
     q,_=dims(lam)
     schur=Fraction(sum(char(lam,cycles(p))*math.prod(sum(t**c for t in x) for c in cycles(p)) for p in itertools.permutations(range(n))),math.factorial(n))
     assert schur/q>=target
     inequalities+=1
 report=dict(seed=45151026,direct_checks=len(rows),max_error=worst,qubit_checks=len(qrows),exact_schur_inequalities=inequalities,seconds=time.time()-start,direct=rows,qubit=qrows,scope='Deterministic finite algebraic/numerical cross-checks; no proof-assistant verification or human peer review.')
 (ROOT/'verification-universal.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:v for k,v in report.items() if k not in ['direct','qubit']}),flush=True)
if __name__=='__main__':main()
