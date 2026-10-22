from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib
R=Path(__file__).parent;out=R/'fixed-count-checks-27.json'
if out.exists():raise SystemExit('Refusing overwrite')
z=s.symbols('z');I=s.I
def star(p,n):
 p=s.Poly(s.expand(p),z)
 return s.expand(sum(s.conjugate(p.nth(j))*z**(n-j) for j in range(n+1)))
rows=[]
for roots in [[],[0],[s.Rational(1,3)],[I/2],[s.Rational(1,3),I/2],[I/2,-I/2,0]]:
 A=s.prod(z-b for b in roots);M=len(roots);Ast=star(A,M)
 for circle in [[1],[-1,I],[I,-I,1],[-1,-1,I]]:
  Q=s.prod(z-b for b in circle);N=len(circle);Qst=star(Q,N)
  phase=s.simplify(Q/Qst);assert not phase.has(z)
  c=2+I;P=s.expand(c*A*Q);n=M+N;Pst=star(P,n)
  omega=s.simplify(c/s.conjugate(c)*phase)
  assert s.simplify(omega*s.conjugate(omega))==1
  assert s.expand(P*Ast-omega*A*Pst)==0
  for lam in [0,1,s.Rational(3,2)+I/3]:
   res=s.diff(P,z)-lam*P;rst=star(res,n)
   assert s.expand(z*z*s.diff(Pst,z)-n*z*Pst+rst+s.conjugate(lam)*Pst)==0
   H=s.expand(z*z*(s.diff(A,z)*Ast-A*s.diff(Ast,z))+(n*z-lam*z*z-s.conjugate(lam))*A*Ast)
   assert s.expand(z*z*A*Ast*res+omega*A*A*rst-H*P)==0
   assert s.degree(H,z)<=2*M+2
   rows.append(dict(M=M,n=n,lambda_value=str(lam),identity='exact'))
u=s.symbols('u')
for N in range(1,8):
 T=s.zeros(N+1)
 for j in range(N):T[j,j+1]=T[j+1,j]=s.Rational(1,2)
 vec=s.Matrix([s.chebyshevu(j,u) for j in range(N+1)])
 residual=T*vec-u*vec
 assert all(s.expand(t)==0 for t in residual[:-1])
 assert s.expand(residual[-1]+s.chebyshevu(N+1,u)/2)==0
data=dict(created_at=datetime.now(timezone.utc).isoformat(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),reciprocal_identity_cases=rows,case_count=len(rows),exact_path_recurrence_degrees=list(range(1,8)),status='PASS',initial_check_limitation='Sympy trigsimp did not reduce every trigonometric eigenvector residual to0; replaced by exact Chebyshev polynomial recurrence, preserving the intended analytic path identity.',scope='Exact symbolic identities and finite path recurrence cases; full inequalities and novelty require analytic audit.')
out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(status='PASS',cases=len(rows))))
