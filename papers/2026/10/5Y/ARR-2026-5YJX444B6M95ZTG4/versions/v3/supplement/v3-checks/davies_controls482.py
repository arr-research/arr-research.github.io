import json
from pathlib import Path
import numpy as np
import sympy as s
rng=np.random.default_rng(482)
U,V,K,b,e=s.symbols('U V K b e',positive=True)
u=U*V-K*K
A=s.Matrix([K*K/V,u/V,0,V])
B=s.Matrix([U,0,u/U,K*K/U])
C=s.Matrix([U,0,0,V])
wA=b*V/u;wB=e*U/u;wC=1-wA-wB
assert s.simplify(wA*A+wB*B+wC*C-s.Matrix([U-b,b,e,V-e]))==s.zeros(4,1)
assert s.simplify((U-b)*(V-e)-b*e-K*K-(u-b*V-e*U))==0
h0,h1=s.symbols('h0 h1',nonnegative=True)
assert s.simplify((h0*h0*(U-b))*(h1*h1*(V-e))-(h0*h0*b)*(h1*h1*e)-(h0*h1*K)**2-h0*h0*h1*h1*(u-b*V-e*U))==0

def pn(A,p):
 ev=np.maximum(np.linalg.eigvalsh((A+A.conj().T)/2),0)
 return ev.max() if p==np.inf else np.sum(ev**p)**(1/p)
def normalized(shape,p):
 X=rng.normal(size=shape)+1j*rng.normal(size=shape)
 return X/np.sqrt(pn(X@X.conj().T,p))
rows=[]
for p in [1.0,1.01,1.1,1.5,2.0,3.5,np.inf]:
 maxex=-1.;maxeq=0.;maxcontrol=-1.
 for trial in range(80):
  shape=[(2,3),(3,2),(3,3)][trial%3]
  X=normalized(shape,p);Y=normalized(shape,p)
  U0,U1=rng.uniform(.05,1.5,2);k=rng.uniform(0,1)*np.sqrt(U0*U1)
  scalar=np.array([[U0,k],[k,U1]])
  determinant=U0*U1-k*k
  if trial%4==0:w=np.array([0.,0.,1.])
  elif trial%4==1:w=np.array([1.,0.,0.])
  elif trial%4==2:w=np.array([0.,1.,0.])
  else:w=rng.dirichlet([1,1,1])
  vertices=np.array([[k*k/U1,determinant/U1,0,U1],
   [U0,0,determinant/U0,k*k/U0],[U0,0,0,U1]])
  alpha,beta,eta,delta=w@vertices
  T=np.block([[alpha*X@X.conj().T+beta*Y@Y.conj().T,k*X@Y.conj().T],
    [k*Y@X.conj().T,eta*X@X.conj().T+delta*Y@Y.conj().T]])
  excess=pn(T,p)-pn(scalar,p);maxex=max(maxex,float(excess))
  assert excess<2e-10,(p,trial,excess)
  rankone=np.zeros(shape,complex);rankone[0,0]=1
  E=np.kron(scalar,rankone@rankone.conj().T)
  maxeq=max(maxeq,float(abs(pn(E,p)-pn(scalar,p))))
  # Separate n=3 controlled-purification vertex, same rectangular blocks.
  Z=[normalized(shape,p) for _ in range(3)]
  W=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3));Q=W@W.conj().T;Q/=np.trace(Q)
  control=np.block([[Q[i,j]*Z[i]@Z[j].conj().T for j in range(3)] for i in range(3)])
  ce=pn(control,p)-pn(Q,p);maxcontrol=max(maxcontrol,float(ce))
  assert ce<2e-10,(p,trial,ce)
 rows.append({'order':str(p),'trials':80,'max_block_norm_excess':maxex,
  'rank_one_equality_residual':maxeq,'max_controlled_vertex_excess':maxcontrol})
out={'status':'symbolic_identities_and_bounded_numeric_controls_pass',
 'seed':482,'numpy':np.__version__,'sympy':s.__version__,'rows':rows,
 'exact_identities':['three-vertex coefficient reconstruction','gap half-plane','diagonal-filter gap'],
 'scope':'exact algebra plus floating point diagnostics, not a global proof or independent review',
 'candidate':'davies_norm481.md','manuscript_created':False,'importance_assessed':False}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
