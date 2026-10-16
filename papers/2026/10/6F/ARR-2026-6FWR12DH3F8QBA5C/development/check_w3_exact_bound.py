"""Independent exact and numeric checks for the proposed uniform W3 bound.
The analytic proof is in w3-exact-bound-proof.txt; numerical checks are not proof.
"""
from pathlib import Path
import datetime, json
import numpy as np
import sympy as s

outdir=Path(__file__).resolve().parent
K=[]
for i,j in [(0,1),(0,2),(1,2)]:
    k=s.zeros(3); k[i,j]=1/s.sqrt(2); k[j,i]=-1/s.sqrt(2); K.append(k)
count=0
for i in range(3):
 for j in range(3):
  for k in range(3):
   for l in range(3):
    actual=s.trace(K[i].H*K[j]*K[k].H*K[l])
    expected=s.Rational(int(i==j and k==l)+int(i==l and j==k),4)
    assert s.simplify(actual-expected)==0
    count+=1

# Exact scalar majorant certificate: derivative factorization and contact values.
x=s.symbols('x',positive=True)
a=s.Rational(3,4); b=s.Integer(3)
c=s.Rational(16,81)*(s.log(4)-3)
q=s.log(a)+(x-a)/a+c*(x-a)**2
assert s.simplify(q.subs(x,a)-s.log(a))==0
assert s.simplify(s.expand_log(q.subs(x,b)-s.log(b),force=True))==0
assert s.simplify(s.diff(q-s.log(x),x)-(x-a)*(2*c*x+1/a)/x)==0
turn=-1/(2*a*c)
assert float(a)<float(turn)<float(b)
expected_q=s.log(a)+s.Rational(1,3)+c*s.Rational(9,16)
target_q=s.log(a)+s.log(4)/9
assert s.simplify(expected_q-target_q)==0

# Exact m=3 witness H=sum K_i tensor K_i.
h=sum((s.kronecker_product(k,k) for k in K),s.zeros(9))
gram=h.H*h
assert gram.eigenvals()=={s.Rational(1,4):8,s.Integer(1):1}
assert s.det(h)==-s.Rational(1,256)
assert sum((k.H*k for k in K),s.zeros(3))==s.eye(3)
assert sum((k*k.H for k in K),s.zeros(3))==s.eye(3)

# Manuscript's Levi-Civita ordering and its Pauli size-two witness.
kle=[K[2],-K[1],K[0]]
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
h2=sum((s.kronecker_product(k,y/s.sqrt(3)) for k,y in zip(kle,pauli)),s.zeros(6))
assert (h2.H*h2).eigenvals()=={s.Rational(2,3):2,s.Rational(1,6):4}
assert s.simplify(s.Abs(s.det(h2))-s.Rational(1,54))==0

# Random finite checks: all mixtures of unitaries satisfy both Gram constraints.
rng=np.random.default_rng(2026101604)
kn=[np.array(k,dtype=complex) for k in K]
numeric=[]
for m in [2,3,4,5,7,9]:
 for trial in range(5):
  p=rng.random(3); p/=p.sum()
  yy=[]
  for w in p:
   z=rng.normal(size=(m,m))+1j*rng.normal(size=(m,m))
   u=np.linalg.qr(z)[0]
   yy.append(np.sqrt(w)*u)
  hn=sum(np.kron(k,y) for k,y in zip(kn,yy))
  g=hn.conj().T@hn
  norm_error=max(0.,float(np.linalg.eigvalsh(g)[-1]-1))
  moment1_error=abs(np.trace(g).real/(3*m)-1/3)
  moment2_error=abs(np.trace(g@g).real/(3*m)-1/6)
  # Verify block-transpose formula independently of the trace-product identity.
  aa,bb,cc=yy
  v=np.concatenate([cc,-bb,aa],axis=1)
  pmat=v.conj().T@v
  pt=pmat.reshape(3,m,3,m).transpose(2,1,0,3).reshape(3*m,3*m)
  block_error=np.linalg.norm(g-(np.eye(3*m)-pt)/2)
  assert max(norm_error,moment1_error,moment2_error,block_error)<1e-11
  sign,ld=np.linalg.slogdet(hn)
  detroot=float(np.exp(2*ld/(3*m)))
  assert detroot <= 2**(2/9)/4+1e-12
  numeric.append({'m':m,'trial':trial,'moment1_error':moment1_error,
   'moment2_error':moment2_error,'block_identity_error':block_error,'detroot':detroot})

out={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'passed':True,'exact_K_trace_identities':count,'q_derivative_factorization':str((x-a)*(2*c*x+1/a)/x),
 'q_second_stationary_point':float(turn),'q_contacts':['3/4','3'],
 'm3_witness_squared_singular_values':{'1':1,'1/4':8},
 'm2_Pauli_squared_singular_values':{'2/3':2,'1/6':4},
 'm3_witness_determinant':'-1/256','uniform_bound_exact':'2^(2/9)/4',
 'uniform_bound_float':2**(2/9)/4,'numeric_cases':numeric,
 'scope':'Exact symbolic identities plus finite numerical checks; analytic proof is separate.'}
(outdir/'w3-exact-bound-checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='numeric_cases'},indent=2))
