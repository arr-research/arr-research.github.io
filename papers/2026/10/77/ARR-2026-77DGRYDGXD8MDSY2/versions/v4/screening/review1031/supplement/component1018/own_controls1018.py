"""Audit controls: original full matrices, congruences, spectral resolvents.
These bounded tests do not establish the universal statement.
"""
from pathlib import Path
import json, sympy as sp, numpy as np
P=Path(__file__).parent
R=sp.Rational
def ptr(x,d,r):
 if isinstance(x,sp.MatrixBase): return sp.Matrix(r,r,lambda i,j:sum(x[a*r+i,a*r+j] for a in range(d)))
 return np.einsum('aiaj->ij',x.reshape(d,r,d,r))
def E(x,d,r):
 return sp.kronecker_product(sp.eye(d)/d,ptr(x,d,r)) if isinstance(x,sp.MatrixBase) else np.kron(np.eye(d)/d,ptr(x,d,r))
def write(name,obj): (P/name).write_text(json.dumps(obj,indent=2,default=lambda v:bool(v))+'\n',encoding='utf-8')
# Alternative 2x2 Sylvester inverse from Cayley-Hamilton, not solving entries.
d,e,p=sp.symbols('d e p',positive=True)
W=sp.Matrix([[1+(d-1)*p,d*p*e],[d*p*e,d*e*e]])/(d*d*(1+e*e))
T=sp.Matrix([[0,1],[1,2*e]])
Y=(T+W.det()*W.inv()*T*W.inv())/sp.trace(W)
G=sp.factor(sp.trace(T*Y))
expected=4*d*(1+e*e)*(d*d*e*e*p+d*d*p+d*e*e+d-p+1)/((d*p+1)*(d*e*e+d*p-p+1))
assert sp.simplify(W*Y+Y*W-2*T)==sp.zeros(2)
assert sp.factor(G-expected)==0
symbolic={'method':'Cayley-Hamilton inverse Y=(T+det(W)W^-1 T W^-1)/TrW','full_Sylvester_residual_zero':True,'displayed_G_matches':True,'G':str(G),'limit':str(sp.limit(G,e,0))}
structures=[]
for d0 in range(2,7):
 r=d0+1;n=d0*r;ee=R(2,7);cols=sp.zeros(n,d0);D=sp.zeros(n);blocks=[]
 for i in range(d0):
  a=i*r+i;b=((i+1)%d0)*r+d0;cols[a,i]=1;cols[b,i]=ee;blocks += [a,b]
  ci=1 if i==0 else -1 if i==1 else 0
  D[a,b]=D[b,a]=ci;D[b,b]=2*ee*ci
 sig=cols*cols.T/(d0*(1+ee*ee));B=E(sig,d0,r);Pr=d0*sig
 assert len(set(blocks))==2*d0 and n-len(blocks)==d0*(d0-1)
 assert cols.T*B.inv()*cols/(d0*(1+ee*ee))==(d0+1)*sp.eye(d0)
 assert ptr(D,d0,r)==sp.zeros(r) and sp.trace(sig)==1 and Pr*Pr==Pr
 assert (sp.eye(n)-Pr)*D*(sp.eye(n)-Pr)==sp.zeros(n)
 boundary=2*d0*sp.trace(D*D)-d0*sp.trace((Pr*D*Pr)**2)
 assert boundary==8*d0*(1+ee*ee)
 pp=-R(1,2*(d0*d0-1));S=(1-pp)*B+pp*sig
 predicted=W.subs({d:d0,e:ee,p:pp})
 residual=S.copy()
 for i in range(d0):
  ix=[i*r+i,((i+1)%d0)*r+d0]
  assert S.extract(ix,ix)==predicted
  for a in ix:
   for b in ix:residual[a,b]=0
 assert residual==sp.diag(*list(residual.diagonal()))
 assert all(residual[a,a]>0 for a in range(n) if a not in blocks)
 Q=sp.zeros(n);Q[blocks[0],blocks[0]]=Q[blocks[1],blocks[1]]=1
 assert Q*S==S*Q and sp.trace(Q*D)==2*ee
 structures.append({'d':d0,'R':r,'full_dimension':n,'passed':True,'boundary_SLD':str(boundary),'Tr_QD':str(sp.trace(Q*D))})
write('STRUCTURE1018.json',{'symbolic':symbolic,'full_matrices':structures})
# Random complex, genuinely noncommuting finite pairs, different ancillary sizes.
rng=np.random.default_rng(10181017)
def randstate(n):
 x=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));q=x@x.conj().T;return q/np.trace(q)
def herm(x):return (x+x.conj().T)/2
def maxwhite(x,B):
 v,u=np.linalg.eigh(B);w=(u/np.sqrt(v))@u.conj().T;return float(np.linalg.eigvalsh(herm(w@x@w))[-1])
def metric(s,z):
 v,u=np.linalg.eigh(s);zz=u.conj().T@z@u;return float(np.sum(2*np.abs(zz)**2/(v[:,None]+v[None,:])).real)
def kernel(a,b,z,s):
 v,u=np.linalg.eigh(a);w,t=np.linalg.eigh(b);zz=u.conj().T@z@t;return float(np.sum(np.abs(zz)**2/(v[:,None]+s*w[None,:])).real)
def petzspec(a,b,f):
 v,u=np.linalg.eigh(a);w,t=np.linalg.eigh(b);over=np.abs(u.conj().T@t)**2;return float(np.sum(over*w[None,:]*f(v[:,None]/w[None,:])).real)
rows=[];max_violation=-1.;max_residual=0.
for d0,r in [(2,1),(2,3),(2,5),(3,1),(3,3),(3,4),(4,2),(4,5),(5,3),(5,6)]:
 n=d0*r
 for repeat in range(10):
  kap=1.02+(d0-0.02)*(repeat+0.5)/10
  raw=randstate(n);B=E(raw,d0,r);q=maxwhite(raw,B);theta=min(.95,.8*(kap-1)/(q-1));sig=herm((1-theta)*B+theta*raw)
  z=herm(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)));z=z-E(z,d0,r);z/=np.linalg.norm(z)
  # Strict both-state budget by operator norm perturbation bound.
  slack=min(np.linalg.eigvalsh(sig)[0],np.linalg.eigvalsh(kap*B-sig)[0]);t=.4*slack
  rho=herm(sig+t*z);l=[-1/(d0*d0-1),-.5/(d0*d0-1),0.,.3,.75,1.][repeat%6]
  os=herm(l*sig+(1-l)*B);orr=herm(l*rho+(1-l)*B);bound=l*l*kap/(1+l*(kap-1))
  assert np.linalg.eigvalsh(rho)[0]>0 and maxwhite(rho,B)<kap+1e-11
  assert np.linalg.norm(ptr(rho,d0,r)-ptr(sig,d0,r))<1e-12
  sl=metric(os,l*z)/metric(sig,z);ks=[]
  for a in [0.,.013,.5,1.,7.,1000.]:ks.append(kernel(orr,os,l*z,a)/kernel(rho,sig,z,a))
  # Test orientation by comparing finite triangular spectral and Sylvester forms.
  tri=petzspec(rho,sig,lambda x:(x-1)**2/(x+1));direct=t*t*kernel(rho,sig,z,1.)
  err=abs(tri-direct)/max(direct,1e-300);max_residual=max(max_residual,err);assert err<1e-6
  # Quadratic endpoint R_sigma^-1 versus L_rho^-1 (both represented).
  endin=float(np.trace(z@z@np.linalg.inv(sig)).real);endout=float(np.trace((l*z)@(l*z)@np.linalg.inv(os)).real);endpoint=endout/endin
  violation=max([sl,endpoint]+ks)-bound;max_violation=max(max_violation,violation);assert violation<2e-11
  rows.append({'d':d0,'R':r,'kappa':kap,'lambda':l,'SLD':sl,'resolvent_ratios':ks,'quadratic_endpoint':endpoint,'upper':bound,'max_minus_upper':violation,'triangle_relative_crosscheck_error':err})
write('RANDOM1018.json',{'seed':10181017,'scope':'100 bounded numerical falsification attempts, not universal proof','cases':len(rows),'max_ratio_minus_upper':max_violation,'max_triangle_crosscheck_relative_error':max_residual,'rows':rows})
print(json.dumps({'structure':len(structures),'random':len(rows),'max_ratio_minus_upper':max_violation,'all_passed':True}))
