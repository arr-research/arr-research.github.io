from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib
root=Path(__file__).parent;out=root/'positive-checks-27c.json'
if out.exists():raise SystemExit('Refusing overwrite')
z=s.symbols('z');I=s.I
def star(p,m):
    p=s.Poly(s.expand(p),z)
    return s.expand(sum(s.conjugate(p.nth(k))*z**(m-k) for k in range(m+1)))
def sqnorm(p):
    return s.simplify(sum(c*s.conjugate(c) for c in s.Poly(s.expand(p),z).all_coeffs()))
patterns=[[],[0],[s.Rational(999,1000)],[I*s.Rational(999,1000)],
 [s.Rational(999,1000)]*2,[s.Rational(3,5)+I*s.Rational(4,5)*s.Rational(999,1000),0],
 [s.Rational(999,1000),-s.Rational(999,1000),I/2],[I*s.Rational(999,1000)]*3]
rows=[]
for roots in patterns:
    M=len(roots);A=s.expand(s.prod(z-b for b in roots));Ast=star(A,M)
    W=s.expand(z*z*(s.diff(A,z)*Ast-A*s.diff(Ast,z)))
    # C3 becomes the following polynomial identity after multiplication
    # by z^(M+1); this avoids floating-point circle sampling entirely.
    Kpoly=s.expand(sum((1-b*s.conjugate(b))*z*z*s.prod((z-c)*(1-s.conjugate(c)*z) for j,c in enumerate(roots) if j!=k) for k,b in enumerate(roots)))
    assert s.expand(W-Kpoly)==0
    for n in sorted(set([max(1,M),max(1,M+1),2*M+4])):
        for lam in [0,s.Rational(n,2),s.Rational(n,2)+I/1000,n*(1+I),-n*I]:
            H=s.expand(W+(n*z-lam*z*z-s.conjugate(lam))*A*Ast)
            h2=sqnorm(H)
            lower2=s.Rational(n*n,2*16**M)
            assert h2>=lower2
            rows.append(dict(M=M,n=n,lambda_value=str(lam),bound_ratio_squared=str(s.cancel(h2/lower2))))
data=dict(status='PASS',created_at=datetime.now(timezone.utc).isoformat(),
 script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exact_positive_kernel_identities=len(patterns),exact_H_bound_cases=len(rows),cases=rows,
 scope='Exact symbolic identity and finite rational H-norm inequalities, including n=M and near-boundary colliding roots. Does not verify Jensen for all roots or the full analytic theorem; no independent assessment.')
out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:data[k] for k in ['status','exact_positive_kernel_identities','exact_H_bound_cases']}))
