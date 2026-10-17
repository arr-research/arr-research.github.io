"""Independent finite-dimensional diagnostics for the 2026-10-17 manuscript.
No author verification code imported; these checks do not prove external asymptotic theorems.
"""
from pathlib import Path
import json, hashlib, math
import numpy as np
BASE=Path(__file__).resolve().parent
rng=np.random.default_rng(2026101702)
def hs_basis(n):
    out=[]
    for i in range(n):
        z=np.zeros((n,n),complex);z[i,i]=1;out.append(z)
    for i in range(n):
        for j in range(i+1,n):
            z=np.zeros((n,n),complex);z[i,j]=z[j,i]=1/math.sqrt(2);out.append(z)
            z=np.zeros((n,n),complex);z[i,j]=1j/math.sqrt(2);z[j,i]=-1j/math.sqrt(2);out.append(z)
    return np.array(out)
def op(a): return float(np.linalg.norm(a,2))
def herm(d):
    a=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d));return (a+a.conj().T)/2
cases=[]
for d in [1,2,3]:
 for m in [2,3,5]:
  for s in [1,3]:
   A=np.array([np.eye(d)]+[herm(d) for _ in range(s-1)])
   b=np.zeros(s);b[0]=1
   L=rng.normal(size=(s,s));L/=np.linalg.norm(L)
   B=np.einsum('ij,iab->jab',L,A)
   F=hs_basis(m)
   coeff=np.array([np.kron(B[j],F[p])/math.sqrt(m) for j in range(s) for p in range(m*m)])
   v0=op(sum(x@x for x in B))
   bv=np.stack([x.reshape(-1) for x in B],axis=1)
   g0=op(bv@bv.conj().T)
   cv=np.stack([x.reshape(-1) for x in coeff],axis=1)
   covnorm=op(cv@cv.conj().T)
   varnorm=op(sum(x@x for x in coeff))
   a2=sum(op(x)**2 for x in A)
   assert abs(covnorm-g0/m)<1e-9
   assert abs(varnorm-v0)<1e-9
   assert v0<=a2+1e-9 and g0<=d*a2+1e-9
   g=rng.normal(size=(s,m*m));G=np.einsum('jp,pab->jab',g,F)/math.sqrt(m)
   Y=np.einsum('ij,jab->iab',L,G)
   H=sum(np.kron(A[i],Y[i]) for i in range(s))
   eps=.17; E=sum(np.trace(y@y).real/m for y in Y); c=eps**2
   W=np.array([(Y[i]+1j*eps*b[i]*np.eye(m))/math.sqrt(E+c) for i in range(s)])
   energy=sum(np.trace(w@w.conj().T).real/m for w in W)
   normalerr=max(op(w@w.conj().T-w.conj().T@w) for w in W)
   J=float(np.mean(np.log(np.linalg.eigvalsh(H)**2+eps**2))-np.log(E+c))
   detJ=2*np.linalg.slogdet(sum(np.kron(A[i],W[i]) for i in range(s)))[1]/(d*m)
   assert abs(energy-1)<1e-10 and normalerr<1e-9 and abs(J-detJ)<1e-9
   inv=np.linalg.inv(H@H+eps**2*np.eye(d*m))
   grad1=np.array([np.trace(2*H@inv@t).real/(d*m) for t in coeff]).reshape(g.shape)
   grad2=2*(L.T@L)@g/(m*m*(E+c))
   grad=grad1-grad2
   Lip=(math.sqrt(g0/d)+1)/(m*eps)
   assert np.linalg.norm(grad)<=Lip*(1+1e-9)
   direction=rng.normal(size=g.shape);direction/=np.linalg.norm(direction)
   def objective(gg):
      HH=sum(z*t for z,t in zip(gg.reshape(-1),coeff))
      EE=np.sum(gg*((L.T@L)@gg))/(m*m)
      return np.mean(np.log(np.linalg.eigvalsh(HH)**2+eps**2))-np.log(EE+c)
   step=1e-6; fd=(objective(g+step*direction)-objective(g-step*direction))/(2*step)
   assert abs(fd-np.sum(grad*direction))<2e-6
   theta=.4; beta=1
   me=4*v0*g0*beta**4/theta**3; ee2=theta/(2*beta**2)
   loss1=v0*g0/(2*me*ee2**2)+math.log1p(ee2*beta**2)
   ms=32*v0*g0*beta**4/theta**3; es2=theta/(4*beta**2)
   loss2=v0*g0/(2*ms*es2**2)+math.log1p(es2*beta**2)
   assert loss1<theta and loss2<theta/2
   lip2=(math.sqrt(g0/d)+1/beta)**2/(ms**2*es2)
   exponent=(theta/2)**2/(2*lip2)
   stated=ms**2*theta**3/(32*(beta*math.sqrt(g0/d)+1)**2)
   assert abs(exponent-stated)<=1e-10*(1+abs(stated))
   cases.append(dict(d=d,m=m,s=s,covariance_error=abs(covnorm-g0/m),variance_error=abs(varnorm-v0),energy_error=abs(energy-1),normality_error=normalerr,objective_error=abs(J-detJ),gradient_error=abs(fd-np.sum(grad*direction)),gradient_to_bound=float(np.linalg.norm(grad)/Lip),existence_loss=loss1,sampling_loss=loss2))
# Exact anticommuting skew example lies outside the positive-span class.
S=[]
for i,j in [(0,1),(0,2),(1,2)]:
 z=np.zeros((3,3),complex);z[i,j]=1;z[j,i]=-1;S.append(z)
paulis=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1])]
anchor=sum(np.kron(a,y) for a,y in zip(S,paulis))
assert np.linalg.matrix_rank(anchor)==6
assert all(abs(np.trace(1j*a))==0 and np.allclose(1j*a,(1j*a).conj().T) for a in S)
result={'status':'PASS','seed':2026101702,'scope':'Finite-dimensional normalization, covariance, gradient, constants and example diagnostics only; not a proof of asymptotics or a Monte Carlo estimate of universal success probability. No author verifier read/imported.','cases':cases,'skew_anchor_min_singular':float(np.linalg.svd(anchor,compute_uv=False)[-1]),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(BASE/'polynomial-independent-checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'status':result['status'],'cases':len(cases),'max_gradient_error':max(x['gradient_error'] for x in cases),'max_objective_error':max(x['objective_error'] for x in cases),'skew_anchor_min_singular':result['skew_anchor_min_singular']}))
