import json,itertools,time
from pathlib import Path
import sympy as s
import numpy as np

R=Path(__file__).parent
t0=time.time()
x,y,z,a,b,c=s.symbols('x y z a b c')
I=s.eye(2)
P=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
A=[]
for i,j in [(0,1),(1,2),(2,0)]:
 q=s.zeros(3);q[i,j]=1;q[j,i]=-1;A.append(q)
D=[s.diag(*[int(k==j) for k in range(3)]) for j in range(3)]
AA=A+D;YY=P+[I,I,I];vv=[x,y,z,a,b,c]
H=sum((s.kronecker_product(q,v*Y) for q,Y,v in zip(AA,YY,vv)),s.zeros(6))
poly=s.Poly(H.det(method='domain-ge'),*vv)
S=a*b*c+a*y**2+b*z**2+c*x**2
assert s.expand(poly.as_expr()-(S+2*s.I*x*y*z)**2)==0
vertices=[(0,0,0,1,1,1),(2,0,0,0,0,1),(0,2,0,1,0,0),(0,0,2,0,1,0),(1,1,1,0,0,0)]
coef={str(v):str(poly.coeff_monomial(tuple(2*j for j in v))) for v in vertices}
assert all(poly.coeff_monomial(tuple(2*j for j in v))!=0 for v in vertices)
rows=s.Matrix([[1,0,1,2,0,0],[1,1,0,0,2,0],[0,1,1,0,0,2]])
rhs=s.Matrix([2,2,2]);bfs=set()
for inds in itertools.combinations(range(6),3):
 B=rows[:,inds]
 if B.det()==0:continue
 sol=B.inv()*rhs
 if min(sol)<0:continue
 q=[s.Integer(0)]*6
 for j,u in zip(inds,sol):q[j]=u
 bfs.add(tuple(q))
assert bfs==set(vertices),(bfs,vertices)
assert all(rows*s.Matrix(u)==s.Matrix([4,4,4]) for u in poly.monoms())
assert min(abs(poly.coeff_monomial(tuple(2*j for j in v))) for v in vertices)==1

# Numerical adversarial checks, not a proof of the theorem. Use arbitrary
# complex tuples, wide weight ranges and sizes not dividing the witness size.
rng=np.random.default_rng(20261016)
An=[np.array(q).astype(complex) for q in AA]
G=np.array([[np.trace(q.conj().T@r) for r in An] for q in An])
upper=float(np.linalg.eigvalsh(G).max()/3)
assert abs(upper-2/3)<1e-12
max_ratio=0.;cases=0
for m in [1,2,3,4,5,7]:
 for trial in range(40):
  logweights=rng.uniform(-8,3,6);weights=np.exp(logweights)
  Y=rng.normal(size=(6,m,m))+1j*rng.normal(size=(6,m,m))
  Y/=np.sqrt(np.sum(abs(Y)**2)/m)
  Hn=sum(np.kron(q,w*v) for q,w,v in zip(An,weights,Y))
  sign,ld=np.linalg.slogdet(Hn)
  obj=0 if sign==0 else np.exp(2*ld/(3*m))
  trop=np.exp(max(2*np.dot(v,logweights)/3 for v in vertices))
  max_ratio=max(max_ratio,obj/(upper*trop));cases+=1
  assert obj<=upper*trop*(1+1e-7)

fixed_witness_checks=[]
for trial in range(120):
 lw=rng.uniform(-15,5,6);xx,yy,zz,aa,bb,cc=np.exp(lw)
 ss=aa*bb*cc+aa*yy**2+bb*zz**2+cc*xx**2
 obj=(ss**2+4*(xx*yy*zz)**2)**(1/3)/6
 trop=float(np.exp(max(2*np.dot(v,lw)/3 for v in vertices)))
 assert obj>=trop/6*(1-1e-9)
 fixed_witness_checks.append(obj/(trop/6))

# Discrete phase Parseval: edge degrees <=4, diagonal degrees <=2;
# fix the last phase by homogeneity. Grid 5^3*3^2=1125 is exact.
monoms=poly.monoms();coeff=np.array([complex(v) for v in poly.coeffs()])
assert all(all(k<=bound for k,bound in zip(u,[4,4,4,2,2,2])) for u in monoms)
phases=np.array(list(itertools.product(range(5),range(5),range(5),range(3),range(3))))
angles=phases*np.array([2*np.pi/5]*3+[2*np.pi/3]*2)
phase_matrix=np.exp(1j*angles@np.array(monoms)[:,:5].T)
phase_checks=[]
for trial in range(10):
 lw=rng.uniform(-4,2,6);w=np.exp(lw)
 terms=coeff*np.exp(np.array(monoms)@lw)/216
 vals=phase_matrix@terms
 lhs=float(np.mean(abs(vals)**2));rhsval=float(np.sum(abs(terms)**2))
 assert np.isclose(lhs,rhsval,rtol=1e-10)
 obj=float(max(abs(vals))**(1/3))
 trop=float(np.exp(max(2*np.dot(v,lw)/3 for v in vertices)))
 assert obj>=trop/6*(1-1e-9)
 phase_checks.append(dict(lower_ratio=obj/(trop/6),parseval_relative_error=abs(lhs/rhsval-1)))

result=dict(status='PASS',scope='Exact example algebra plus numerical stress checks; not independent peer review',
 polynomial=str(poly.as_expr()),factorization='(abc+ay^2+bz^2+cx^2+2*i*x*y*z)^2',
 fixed_witness_cases=len(fixed_witness_checks),fixed_witness_min_lower_ratio=min(fixed_witness_checks),
 vertex_coefficients=coef,vertices=[list(map(int,v)) for v in bfs],
 normalized_energy=6,lower_constant='1/6',upper_constant='2/3',factor=4,
 random_cases=cases,max_upper_ratio=max_ratio,phase_menu_size=len(phases),phase_checks=phase_checks,
 elapsed_seconds=time.time()-t0)
(R/'candidate-checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
