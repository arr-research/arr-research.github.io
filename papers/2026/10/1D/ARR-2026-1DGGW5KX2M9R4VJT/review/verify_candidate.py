"""Reviewer-owned diagnostics of the general capacity bridge candidate.
No claimed numerical proof of the asymptotic theorem or novelty.
Only relative output paths; deterministic seed; no author verifier imported.
"""
from pathlib import Path
from datetime import datetime, timezone
import numpy as np, json, math
BASE=Path(__file__).resolve().parent
rng=np.random.default_rng(20261017)
def hermitization(M):
 n=M.shape[0];Z=np.zeros((n,n),complex)
 return np.block([[Z,M],[M.conj().T,Z]])
def proper_coefficients(D,N):
 out=[]
 for B in D:
  for a in range(N):
   for b in range(N):
    E=np.zeros((N,N),complex);E[a,b]=1/np.sqrt(2*N)
    for phase in [1,1j]: out.append(hermitization(np.kron(B,phase*E)))
 return out
checks=[]
for ell in [1,2,3]:
 for N in [1,2,4]:
  for s in [1,3]:
   D=[rng.normal(size=(ell,ell))+1j*rng.normal(size=(ell,ell)) for _ in range(s)]
   coeff=proper_coefficients(D,N)
   V=np.stack([C.reshape(-1) for C in coeff],axis=1)
   v2=float(np.linalg.norm(V.conj().T@V,2))
   sigma2=float(np.linalg.norm(sum(C@C for C in coeff),2))
   a2=sum(np.linalg.norm(B,2)**2 for B in D)
   hs2=sum(np.linalg.norm(B,'fro')**2 for B in D)
   assert v2<=2*hs2/N*(1+1e-12)
   assert sigma2<=a2*(1+1e-12)
   Z=rng.normal(size=(2*ell,2*ell))+1j*rng.normal(size=(2*ell,2*ell))
   model=sum(C@np.kron(Z,np.eye(N))@C for C in coeff)
   zero=np.zeros((ell,ell),complex)
   target=np.block([[sum(B@Z[ell:,ell:]@B.conj().T for B in D),zero],
                    [zero,sum(B.conj().T@Z[:ell,:ell]@B for B in D)]])
   error=float(np.linalg.norm(model-np.kron(target,np.eye(N)),2))
   assert error<1e-10
   checks.append({'ell':ell,'N':N,'s':s,'v_squared':v2,'v_bound':2*hs2/N,
                  'sigma_squared':sigma2,'sigma_bound':a2,'covariance_recursion_error':error})
# Exact-energy asymptotics for a genuinely complex covariance and a fixed anchor.
A=[np.array([[1,1j],[0,0]],complex),np.array([[0,0],[1j,1]],complex)]
T=[np.array([[1,0],[0,2]],complex),np.array([[2,1j],[0,1]],complex)]
r=2;ET=sum(np.trace(t@t.conj().T).real/r for t in T)
T=[t/np.sqrt(ET) for t in T]
B=sum(np.kron(a,t) for a,t in zip(A,T)); assert abs(np.linalg.det(B))>1e-8
L=np.array([[1,1j],[.5,.25]],complex);L/=np.linalg.norm(L,'fro')
rho=.2;z=rho*np.exp(.7j)
energy=[]
for N in [8,32,96]:
 G=[(rng.normal(size=(N,N))+1j*rng.normal(size=(N,N)))/np.sqrt(2*N) for _ in range(2)]
 Y=[sum(L[i,j]*G[j] for j in range(2)) for i in range(2)]
 W=[np.kron(np.eye(r),Y[i])+z*np.kron(T[i],np.eye(N)) for i in range(2)]
 E=sum(np.trace(w@w.conj().T).real/(r*N) for w in W)
 direct=sum(np.kron(A[i],W[i]) for i in range(2))
 BJ=[sum(L[i,j]*A[i] for i in range(2)) for j in range(2)]
 affine=sum(np.kron(np.kron(bj,np.eye(r)),g) for bj,g in zip(BJ,G))+z*np.kron(B,np.eye(N))
 err=float(np.linalg.norm(direct-affine,'fro'));assert err<1e-10
 normalized=[w/np.sqrt(E) for w in W]
 assert abs(sum(np.trace(w@w.conj().T).real/(r*N) for w in normalized)-1)<1e-12
 energy.append({'N':N,'energy':E,'energy_limit':1+rho*rho,'pencil_identity_error':err})
# Concrete invalid-inference counterexample: all moments converge, norms bounded,
# and the least singular value is N^-1, yet the normalized log determinant tends -1.
negative=[]
for N in [100,1000,10000,1000000]:
 k=int(N/math.log(N));ell=-k*math.log(N)/N
 negative.append({'N':N,'small_singular_values':k,'s_min':1/N,
                  'first_moment':1-k/N+k/(N*N),'normalized_logdet':ell,
                  'limiting_measure_logdet':0})
assert negative[-1]['first_moment']>.92 and negative[-1]['normalized_logdet']<-.99
# Numerical check of Brown/Jensen phase mechanism in ordinary matrices.
phase=[]
for n in [2,3,5]:
 for case in range(5):
  H=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
  B=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))+3*np.eye(n)
  r=.2
  eig=np.linalg.eigvals(np.linalg.solve(B,H))
  mean_exact=np.linalg.slogdet(B)[1]/n+np.mean(np.log(np.maximum(abs(eig),r)))
  base=np.linalg.slogdet(H)[1]/n
  assert mean_exact>=base-1e-12
  vals=[np.linalg.slogdet(H+r*np.exp(2j*np.pi*t/1024)*B)[1]/n for t in range(1024)]
  assert max(vals)>=base-1e-12
  phase.append({'dimension':n,'base':float(base),'exact_circle_mean':float(mean_exact),'sampled_max':float(max(vals))})
R={'status':'PASS','completed_at':datetime.now(timezone.utc).isoformat(),
   'covariance_cases':checks,'energy_cases':energy,'phase_cases':phase,
   'negative_control_moments_plus_polynomial_minimum':negative,
   'limitations':['Finite diagnostics only; the proof uses cited asymptotic theorems.',
                  'The negative control refutes an inference about moment convergence, not the proposed capacity inequality.',
                  'Shared involved AI development context; no independent expert or formal verification.']}
(BASE/'independent-checks.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':'PASS','covariance_cases':len(checks),'phase_cases':len(phase),'energy_cases':len(energy),'maximum_covariance_error':max(c['covariance_recursion_error'] for c in checks)},ensure_ascii=False))
