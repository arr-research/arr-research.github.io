"""Finite analytic-formula consistency diagnostics, not universal proofs."""
import numpy as np,json
from scipy.linalg import expm
from pathlib import Path

def solution(H,tau,g,t):
 e,U=np.linalg.eigh(H);a=U.conj().T@tau@U;delta=e[:,None]-e[None,:];z=g+1j*delta;S=U@(g*(-np.expm1(-z*t))/z*a)@U.conj().T;V=expm(-1j*t*H);return np.exp(-g*t),V,S
rows=[]
for d in [2,3,4]:
 for mode in ['cyclic','missing','degenerate']:
  e=np.arange(d,dtype=float)**1.3
  if mode=='degenerate':e[1]=e[0]
  H=np.diag(e);v=np.ones(d,dtype=complex)
  if mode=='missing':v[1]=0
  v/=np.linalg.norm(v);tau=np.outer(v,v.conj());g=.7;t=1.2;l,V,S=solution(H,tau,g,t)
  I=np.eye(d);tr=I.reshape(-1,order='F').conj()[None,:];gen=-1j*(np.kron(I,H)-np.kron(H.T,I))+g*(tau.reshape(-1,order='F')[:,None]@tr-np.eye(d*d));E=expm(t*gen);err=0
  for a in range(d):
   for b in range(d):
    X=np.zeros((d,d),complex);X[a,b]=1;out=(E@X.reshape(-1,order='F')).reshape(d,d,order='F');pred=l*V@X@V.conj().T+np.trace(X)*S;err=max(err,float(np.max(abs(out-pred))))
  krylov=np.column_stack([np.linalg.matrix_power(H,k)@v for k in range(d)]);rk=np.linalg.matrix_rank(krylov,tol=1e-10);rs=np.linalg.matrix_rank(S,tol=1e-10);assert rk==rs and err<1e-12
  rows.append({'d':d,'mode':mode,'Krylov_rank':int(rk),'replacement_rank':int(rs),'solution_max_residual':err,'replacement_min':float(np.linalg.eigvalsh(S)[0])})
qubit=[]
for gt in [.2,np.log(2),1.3]:
 for w in [0,.4,2*np.pi,3*np.pi]:
  for theta in [0,.4,np.pi/2]:
   H=np.diag([w/2,-w/2]);v=np.array([np.cos(theta/2),np.sin(theta/2)]);tau=np.outer(v,v);l,V,S=solution(H,tau,gt,1);W=1-l;r=np.sqrt(W*W*np.cos(theta)**2+gt*gt*np.sin(theta)**2*(1+l*l-2*l*np.cos(w))/(gt*gt+w*w));a=(W-r)/2;assert abs(a-np.linalg.eigvalsh(S)[0])<1e-12
   qubit.append({'gt':float(gt),'wt':float(w),'theta':float(theta),'spectral_formula_residual':float(abs(a-np.linalg.eigvalsh(S)[0]))})
a=np.log(2);r2=a/(2*np.sqrt(a*a+4*np.pi*np.pi));r3=3*a/(2*np.sqrt(a*a+9*np.pi*np.pi));q2=.5/(1.5-r2);q3=.5/(1.5-r3);assert r3>r2 and q3>q2
out={'scope':'Nine generator/matrix-unit/Krylov checks and36 qubit formula diagnostics; finite floating consistency only','generator_cases':rows,'qubit_cases':qubit,'nonmonotone_example':{'lambda':.5,'theta':'pi/2','eta_2pi':float(q2),'eta_3pi':float(q3),'gap':float(q3-q2),'exact_proof':'r3>r2 follows8a²+27pi²>0, a=log2; no decimal certificate substituted'},'failures':0}
Path(__file__).with_name('CHECK955.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'generator_cases':len(rows),'qubit_cases':len(qubit),'nonmonotone_gap':q3-q2,'failures':0}))
