"""Reproducible finite checks; these are not a formal proof of the theorems."""
from pathlib import Path
import numpy as np
import sympy as sp
import json,math,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1]
rng=np.random.default_rng(1702026)
def adj(z):return z.conj().T
def hn(d):
    z=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
    return (z+adj(z))/2
def basis(m):
    fs=[]
    for u in range(m):
        z=np.zeros((m,m),complex);z[u,u]=1;fs.append(z)
    for u in range(m):
        for v in range(u):
            z=np.zeros((m,m),complex);z[u,v]=z[v,u]=1/np.sqrt(2);fs.append(z)
            z=np.zeros((m,m),complex);z[u,v]=1j/np.sqrt(2);z[v,u]=-1j/np.sqrt(2);fs.append(z)
    return np.array(fs)
def tr(z):return np.trace(z)/len(z)
def op(z):return np.linalg.norm(z,2)
checks=[]
def ck(name,error,tol=2e-10,**kw):
    if not np.isfinite(error) or error>tol:raise AssertionError((name,error,tol))
    checks.append(dict(name=name,error=float(error),tolerance=tol,**kw))
for d in [2,3,4]:
  for m in [2,3,4]:
    for rep in range(3):
      s=3; A=np.array([np.eye(d),hn(d),hn(d)])
      L=rng.normal(size=(s,s));L/=np.linalg.norm(L)
      B=np.einsum('ij,iab->jab',L,A);F=basis(m)
      coeff=np.array([np.kron(b,f)/np.sqrt(m) for b in B for f in F])
      g0=op(B.reshape(s,-1)@adj(B.reshape(s,-1)))
      v0=op(sum(b@b for b in B))
      C=coeff.reshape(len(coeff),-1).T
      ck('covariance_norm',abs(op(adj(C)@C)-g0/m),d=d,m=m)
      ck('variance_norm',abs(op(sum(c@c for c in coeff))-v0),d=d,m=m)
      U=hn(d)
      lhs=sum(c@np.kron(U,np.eye(m))@c for c in coeff)
      rhs=np.kron(sum(b@U@b for b in B),np.eye(m))
      ck('free_counterpart_covariance',op(lhs-rhs),d=d,m=m)
      eps=.27;bvec=np.array([1.,0,0]);beta=1
      def objective(g):
          G=np.einsum('jp,pab->jab',g.reshape(s,m*m),F)/np.sqrt(m)
          Y=np.einsum('ij,jab->iab',L,G)
          H=sum(np.kron(aa,yy) for aa,yy in zip(A,Y))
          en=sum(tr(y@y).real for y in Y)
          val=np.log(np.linalg.eigvalsh(H)**2+eps**2).mean()-np.log(en+eps**2)
          return val,Y,H,en
      g=rng.normal(size=s*m*m);J,Y,H,en=objective(g)
      W=(Y+1j*eps*bvec[:,None,None]*np.eye(m))/np.sqrt(en+eps**2)
      pencil=sum(np.kron(aa,w) for aa,w in zip(A,W))
      logval=2*np.linalg.slogdet(pencil)[1]/(d*m)
      ck('energy_exact',abs(sum(tr(w@adj(w)).real for w in W)-1),d=d,m=m)
      ck('log_objective_identity',abs(logval-J),d=d,m=m)
      ck('normal_witness',max(op(w@adj(w)-adj(w)@w) for w in W),d=d,m=m)
      direction=rng.normal(size=g.size);direction/=np.linalg.norm(direction)
      deriv=(objective(g+1e-5*direction)[0]-objective(g-1e-5*direction)[0])/2e-5
      lip=(np.sqrt(g0/d)+1)/(m*eps)
      ck('directional_lipschitz_bound',max(0,abs(deriv)-lip),d=d,m=m)

# Exact singular scalar matrix space and invertible blow-up.
I=sp.I;x,y,z=sp.symbols('x y z')
K=[sp.Matrix([[0,1,0],[-1,0,0],[0,0,0]]),sp.Matrix([[0,0,1],[0,0,0],[-1,0,0]]),sp.Matrix([[0,0,0],[0,0,1],[0,-1,0]])]
pauli=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-I],[I,0]]),sp.diag(1,-1)]
scalar=sum((u*k for u,k in zip([x,y,z],K)),sp.zeros(3))
blowup=sum((sp.kronecker_product(k,p) for k,p in zip(K,pauli)),sp.zeros(6))
assert sp.expand(scalar.det())==0 and blowup.det()!=0
exact=dict(scalar_determinant=str(scalar.det()),blowup_determinant=str(sp.simplify(blowup.det())),traces=[str(k.trace()) for k in K])

# Parameter ledger, including small tolerances and large scales; no huge matrices built.
ledger=[]
for theta in [1,.8,.3,.1,.01,.001]:
  for beta in [.1,1,10,100]:
    for v0,g0 in [(1,1),(.03,4),(5,2),(10,100)]:
      m=max(2,math.ceil(4*v0*g0*beta**4/theta**3));eps2=theta/(2*beta**2)
      loss=v0*g0/(2*m*eps2**2)+math.log1p(eps2*beta**2)
      assert loss<=theta*(1+1e-13)
      m2=max(2,math.ceil(32*v0*g0*beta**4/theta**3));eps22=theta/(4*beta**2)
      loss2=v0*g0/(2*m2*eps22**2)+math.log1p(eps22*beta**2)
      assert loss2<=theta/2*(1+1e-13)
      ledger.append(dict(theta=theta,beta=beta,v0=v0,g0=g0,m=m,loss=loss,sampling_mean_loss=loss2))

# Complex, non-Hermitian Weyl coefficients; their balanced covariance has capacity 1.
# These stress cases are finite illustrations, not tests of asymptotic convergence.
stress=[]
for d in [3,4]:
  U=np.roll(np.eye(d),1,axis=0).astype(complex)
  V=np.diag(np.exp(2j*np.pi*np.arange(d)/d))
  As=[U,V,U@V];r=.13*np.exp(.72j)
  for n in [4,8,16,24]:
    vals=[]
    for rep in range(8):
      G=(rng.normal(size=(3,n,n))+1j*rng.normal(size=(3,n,n)))/np.sqrt(2*n)
      Ys=G/np.sqrt(3);Ys[0]+=r*np.eye(n)
      en=sum(tr(w@adj(w)).real for w in Ys)
      W=Ys/np.sqrt(en)
      H=sum(np.kron(a,w) for a,w in zip(As,W))
      vals.append(float(np.exp(2*np.linalg.slogdet(H)[1]/(d*n))))
      ck('general_energy_normalization',abs(sum(tr(w@adj(w)).real for w in W)-1),d=d,n=n)
    stress.append(dict(d=d,n=n,samples=len(vals),objective_min=min(vals),objective_mean=float(np.mean(vals)),objective_max=max(vals),unshifted_free_comparison=math.exp(-1)))
res=dict(status='PASS',checked_at=datetime.now(timezone.utc).isoformat(),seed=1702026,finite_identity_checks=len(checks),parameter_cases=len(ledger),complex_stress_samples=sum(x['samples'] for x in stress),exact_example=exact,checks=checks,parameter_ledger=ledger,stress_cases=stress,limitations='Finite identities and numerical illustrations only. No formal proof, no empirical certification of limits, novelty or importance.')
(R/'verification'/'results.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in res.items() if k not in ['checks','parameter_ledger','stress_cases']},indent=2))
