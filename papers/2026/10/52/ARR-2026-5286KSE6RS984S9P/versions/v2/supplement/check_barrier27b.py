from pathlib import Path
from datetime import datetime, timezone
import sympy as s
import json, hashlib

root=Path(__file__).parent
out=root/'barrier-checks-27b.json'
if out.exists(): raise SystemExit('Refusing to overwrite a completed check')
z=s.symbols('z')
I=s.I
def norm2(p):
    return s.simplify(sum(c*s.conjugate(c) for c in s.Poly(s.expand(p),z).all_coeffs()))
def star(p,m):
    p=s.Poly(s.expand(p),z)
    return s.expand(sum(s.conjugate(p.nth(k))*z**(m-k) for k in range(m+1)))

# Exact arithmetic probes of the cancellation-sensitive H lower bound.
# Roots approach the boundary, collide, include0, and are not generally
# conjugate paired. This does NOT assert exhaustive or formal verification.
patterns=[[],[0],[s.Rational(999,1000)],[I*s.Rational(999,1000)],
          [s.Rational(999,1000)]*2,
          [s.Rational(3,5)+I*s.Rational(4,5)*s.Rational(999,1000),0],
          [s.Rational(999,1000),-s.Rational(999,1000),I/2],
          [I*s.Rational(999,1000)]*3]
rows=[]
for roots in patterns:
    m=len(roots)
    assert all(s.simplify(b*s.conjugate(b))<1 for b in roots)
    A=s.expand(s.prod(z-b for b in roots))
    Ast=star(A,m)
    W=s.expand(z*z*(s.diff(A,z)*Ast-A*s.diff(Ast,z)))
    w2=norm2(W)
    assert w2<=m*m*16**m
    for n in [max(1,4*m*4**m),max(4,16*m*4**m)]:
        for lam in [0,s.Rational(n,2),s.Rational(n,2)+I/1000,n*(1+I),-n*I]:
            J=n*z-lam*z*z-s.conjugate(lam)
            V=s.expand(J*A*Ast)
            H=s.expand(V+W)
            j2,h2=norm2(V),norm2(H)
            assert j2>=s.Rational(n*n,4)
            assert h2>=s.Rational(n*n,16)
            rows.append(dict(M=m,n=n,roots=[str(b) for b in roots],
                             lambda_value=str(lam),norm_H_squared=str(h2),
                             H_bound_ratio_squared=str(s.cancel(16*h2/(n*n)))))

# Exhaust the finite parity decomposition used in the new real-polynomial
# saturation corollary. This checks the integer selection, not the theorem.
parity_cases=0
for u in range(1,21):
    for v in range(0,11):
        for count in range(6*u+v+1):
            q=min(u,count//2); r=count-2*q
            assert 0<=q<=u and 0<=r<=4*u+v and r+2*q==count
            parity_cases+=1
data=dict(created_at=datetime.now(timezone.utc).isoformat(),
          script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          status='PASS',exact_H_bound_cases=len(rows),cases=rows,
          saturation_integer_cases=parity_cases,
          scope='Author checks in exact rational arithmetic; no full-polynomial H2 residuals computed here, no independent review or priority certification.')
out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:data[k] for k in ['status','exact_H_bound_cases','saturation_integer_cases']}))
