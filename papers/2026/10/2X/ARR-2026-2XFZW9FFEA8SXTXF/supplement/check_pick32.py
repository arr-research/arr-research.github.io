"""Author diagnostics, not interval certification or proof of the general theorem."""
from pathlib import Path
import json,math,warnings
from datetime import datetime,timezone
import numpy as np
import sympy as s
import cvxpy as cp
from scipy.optimize import minimize

out=Path(__file__).resolve().parent/'pick-checks-32.json'
assert not out.exists(), 'Preserve historical output; run in a fresh copy.'
I=s.I
c,x,y,r=s.symbols('c x y r',real=True)
g0=(c+I)**2;g1=(x+I*y)**2
P=s.Matrix([[4*c,(g0-s.conjugate(g1))/I],[(g1-s.conjugate(g0))/I,4*x*y/(1-r*r)]])
detformula=16*c*x*y/(1-r*r)-s.expand_complex((g0-s.conjugate(g1))*s.conjugate(g0-s.conjugate(g1)))
assert s.simplify(P.det()-detformula)==0
a,b=s.symbols('a b',real=True)
gfirst=2*(c+I)*(a+I*b)
T=s.Matrix([[2*c,gfirst/(2*I)],[s.conjugate(gfirst/(2*I)),2*c]])
assert s.expand(T.det()-(4*c*c-(c*c+1)*(a*a+b*b)))==0

# Singular confluent kernel constructed from four boundary atoms.
z,w=s.symbols('z w')
atoms=[s.Integer(1),s.Integer(-1),I,-I]
weights=[s.Rational(1,10),s.Rational(2,10),s.Rational(3,10),s.Rational(4,10)]
h=sum(v*(1+t*z)/(1-t*z) for t,v in zip(atoms,weights))
hc=sum(v*(1+s.conjugate(t)*w)/(1-s.conjugate(t)*w) for t,v in zip(atoms,weights))
kernel=s.cancel((h+hc)/(1-z*w))
spec=[(s.Integer(0),0),(s.Integer(0),1),(-s.Rational(1,3),0),(I/4,0),(I/4,1)]
K=s.zeros(len(spec));Gram=s.zeros(len(spec))
for j,(zj,p) in enumerate(spec):
 for k,(zk,q) in enumerate(spec):
  K[j,k]=s.cancel(s.diff(kernel,z,p,w,q).subs({z:zj,w:s.conjugate(zk)})/(s.factorial(p)*s.factorial(q)))
  Gram[j,k]=s.cancel(2*sum(v*t**p/(1-t*zj)**(p+1)*s.conjugate(t**q/(1-t*zk)**(q+1)) for t,v in zip(atoms,weights)))
  assert s.cancel(K[j,k]-Gram[j,k])==0
assert K==K.conjugate().T
rank=K.rank();assert rank==4 and K.det()==0

# Rational example: residue identity at0 and -1/3 on polynomials.
R=3*(z+1/z)/2/(1+s.Rational(3,5)*(z+1/z)/2)+s.Rational(5,4)
res=[]
for k in range(8):
 val=s.residue(s.cancel(R*z**k/z),z,0)+s.residue(s.cancel(R*z**k/z),z,-s.Rational(1,3))
 expected=0 if k==0 else -s.Rational(25,4)*(-s.Rational(1,3))**k
 assert s.simplify(val-expected)==0
 res.append(str(val))

def toeplitz(coeff):
 n=len(coeff)-1
 return cp.bmat([[coeff[k-j] if k>=j else cp.conj(coeff[j-k]) for k in range(n+1)] for j in range(n+1)])
dualchecks=[]
for name,qseq in [('cosine',[1.5,0,0,0,0,0,0,0]),('mixed',[1.5,0.4+0.3j,-0.2j,0,0,0,0,0])]:
 for n in [1,2,4,8]:
  qv=np.array(qseq[:n],dtype=complex)
  m=cp.Variable(n,complex=True);av=cp.Variable()
  primal=cp.Problem(cp.Minimize(av),[toeplitz([1]+[m[k] for k in range(n)])>>0,toeplitz([av]+[1j*m[k]-qv[k] for k in range(n)])>>0])
  X=cp.Variable((n+1,n+1),hermitian=True);Y=cp.Variable((n+1,n+1),hermitian=True)
  fc=[sum(X[j,j+k] for j in range(n+1-k)) for k in range(1,n+1)]
  gc=[sum(Y[j,j+k] for j in range(n+1-k)) for k in range(1,n+1)]
  dual=cp.Problem(cp.Maximize(2*cp.real(sum(np.conj(qv[k])*gc[k] for k in range(n)))-cp.real(cp.trace(X))),[X>>0,Y>>0,cp.real(cp.trace(Y))==1]+[fc[k]-1j*gc[k]==0 for k in range(n)])
  with warnings.catch_warnings(record=True) as caught:
   primal.solve(solver='CLARABEL',tol_gap_abs=1e-8,tol_feas=1e-8,tol_gap_rel=1e-8,max_iter=300)
   dual.solve(solver='CLARABEL',tol_gap_abs=1e-8,tol_feas=1e-8,tol_gap_rel=1e-8,max_iter=300)
  dualchecks.append({'profile':name,'order':n,'primal':float(primal.value),'dual':float(dual.value),'difference':float(primal.value-dual.value),'primal_status':primal.status,'dual_status':dual.status,'warnings':[str(t.message) for t in caught]})

# Nonlinear constrained numerical exploration: no certified optimum or exact threshold.
C=25/4;rval=1/3
def objective(v): return v[0]-C*(1-v[2])
def constraint(v):
 cv,xv,yv=v
 return 16*cv*xv*yv/(1-rval*rval)-abs(complex(cv,1)**2-complex(xv,-yv)**2)**2
opt=[]
for cv in [0.1,0.3,0.7,1.0,2.0,5.0]:
 result=minimize(objective,[cv,cv,1.0],method='SLSQP',bounds=[(1e-7,30),(1e-7,30),(1e-7,10)],constraints=[{'type':'ineq','fun':constraint}],options={'maxiter':1000,'ftol':1e-12})
 opt.append({'start_c':cv,'success':bool(result.success),'message':str(result.message),'objective':float(-result.fun),'variables':result.x.tolist(),'constraint_residual':float(constraint(result.x))})

data={'created_at':datetime.now(timezone.utc).isoformat(),'scope':'Exact algebra checks and floating diagnostics only; not a certified optimizer or proof of the general theorem.','exact':{'one_harmonic_determinant':True,'two_node_determinant':True,'confluent_kernel_entries':25,'singular_kernel_rank':rank,'singular_kernel_dimension':5,'rational_residue_cases':8,'residue_values':res},'primal_dual':dualchecks,'rational_local_optimizer':opt}
out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps(data,indent=2))
