from pathlib import Path
import sympy as s,json
P=Path(__file__).parent;rows=[]
for d,e,th,z in [(2,s.Rational(1,2),s.Rational(3,4),-1),(3,s.Rational(2,5),s.Rational(5,6),-1),(4,s.Rational(3,7),s.Rational(7,9),-1),(3,s.Integer(2),s.Rational(2,3),s.Rational(3,5)-4*s.I/5)]:
 n=d*d;v=s.zeros(n,1);v[0]=e
 for j in range(1,d):v[j*d+j]=1
 q=d-1+e*e;r=s.diag(e*e,*([1]*(d-1)))/q;B=s.kronecker_product(s.eye(d)/d,r);S=(1-th)*B+th*v*v.T/q;U=s.diag(*([1]*d+[z]*(n-d)));rho=U*S*U.conjugate().T
 rows.append({'d':d,'phase':str(z),'raw_trace':str(s.trace(rho)),'structurally_equal_one':bool(s.trace(rho)==1),'simplified_trace':str(s.simplify(s.trace(rho))),'unitary_exact':all(s.simplify(x)==0 for x in U*U.conjugate().T-s.eye(n))})
assert all(r['simplified_trace']=='1' and r['unitary_exact'] for r in rows)
(P/'DIAGNOSIS1084.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8');print(json.dumps(rows,indent=2))
