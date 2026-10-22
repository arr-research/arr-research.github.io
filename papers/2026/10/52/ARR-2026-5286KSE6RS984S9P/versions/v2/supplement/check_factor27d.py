from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib
root=Path(__file__).parent;out=root/'factor-checks-27d.json'
if out.exists():raise SystemExit('Refusing overwrite')
z=s.symbols('z');I=s.I
def star(p,n):
 p=s.Poly(s.expand(p),z)
 return s.expand(sum(s.conjugate(p.nth(k))*z**(n-k) for k in range(n+1)))
def sqnorm(p):return s.simplify(sum(a*s.conjugate(a) for a in s.Poly(s.expand(p),z).all_coeffs()))
As=[1,z,z-s.Rational(1,3),z-I/2,(z-s.Rational(99,100))**2,z*(z+I/3)]
Qs=[(z-2)*(z-s.Rational(1,2)),(z-2*I)*(z-I/2),
    (z-1-I)*(z-(1+I)/2),
    ((z-2)*(z-s.Rational(1,2)))**2,
    (z-2*I)*(z-I/2)*(z+1)]
rows=[]
for A in As:
 A=s.expand(A);M=int(s.degree(A,z));Ast=star(A,M)
 for Q in Qs:
  Q=s.expand(Q);N=int(s.degree(Q,z));Qst=star(Q,N)
  eta=s.cancel(Q/Qst);assert not eta.has(z)
  assert s.simplify(eta*s.conjugate(eta))==1
  c=2+I;P=s.expand(c*A*Q);n=M+N;Pst=star(P,n)
  omega=s.simplify(c/s.conjugate(c)*eta)
  assert s.expand(P*Ast-omega*A*Pst)==0
  for lam in [0,s.Rational(n,2),s.Rational(n,2)+I/3]:
   R=s.expand(s.diff(P,z)-lam*P);Rst=star(R,n)
   H=s.expand(z*z*(s.diff(A,z)*Ast-A*s.diff(Ast,z))+(n*z-lam*z*z-s.conjugate(lam))*A*Ast)
   assert s.expand(z*z*A*Ast*R+omega*A*A*Rst-H*P)==0
   rho2=s.cancel(sqnorm(R)/sqnorm(P))
   lower2=s.Rational(n*n,8*256**M*(n+2*M+4)**(4*M+4))
   assert rho2>=lower2
   rows.append(dict(M=M,n=n,Q=str(Q),lambda_value=str(lam),rho_squared=str(rho2)))
T=s.symbols('T',positive=True)
P=1-z/T;lam=-1/T;R=s.expand(s.diff(P,z)-lam*P)
assert s.simplify(R+z/T**2)==0
assert s.simplify(sqnorm(R)/sqnorm(P)-1/(T**4*(1+1/T**2)))==0
data=dict(status='PASS',at=datetime.now(timezone.utc).isoformat(),
 script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exact_extended_factor_cases=len(rows),cases=rows,unrestricted_exterior_negative_control='exact symbolic identity',
 scope='Author exact identities and finite coefficient-norm checks for self-inversive cofactors with exterior roots; no independent proof audit or priority claim.')
out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:data[k] for k in ['status','exact_extended_factor_cases','unrestricted_exterior_negative_control']}))
