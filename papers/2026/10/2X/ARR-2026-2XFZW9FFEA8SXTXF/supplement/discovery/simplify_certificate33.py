from pathlib import Path
from datetime import datetime,timezone
from functools import reduce
import json,sympy as s,math
b=Path(__file__).resolve().parent;out=b/'simplified-certificate-33.json';assert not out.exists()
records=json.loads((b/'certificate-search-33.json').read_text())['records']
raw=next(r for r in records if r.get('exact_positive_certificate'))
X,Y=s.symbols('X Y',real=True);t=s.Symbol('t');P=s.sympify(raw['positive_polynomial'],locals={'X':X,'Y':Y});degree=s.total_degree(P)
coeff=[s.expand(P).coeff(X,degree-k).coeff(Y,k) for k in range(degree+1)]
rho=X*X+Y*Y;H=rho+s.Rational(3,5)*(X*X-Y*Y);K=-s.Rational(3,4)*H+3*(X*X-Y*Y);f1=K*X-H*Y;f2=K*Y+H*X
def changes(seq):
 v=[int(s.sign(a)) for a in seq if a!=0]
 return sum(v[k]!=v[k-1] for k in range(1,len(v)))
def sturmdata(poly):
 chain=[s.Poly(p,t) for p in s.sturm(poly.as_expr(),t)]
 signs_plus=[int(s.sign(p.LC())) for p in chain]
 signs_minus=[int(s.sign(p.LC())*(-1)**p.degree()) for p in chain]
 return {'chain_degrees':[p.degree() for p in chain],'signs_minus_infinity':signs_minus,'signs_plus_infinity':signs_plus,'variations_minus':changes(signs_minus),'variations_plus':changes(signs_plus),'root_count':int(poly.count_roots(-s.oo,s.oo))}
trials=[]
for denominator in [100,1000,10000,100000,1000000,10000000]:
 ints=[int(round(c*denominator)) for c in coeff];div=reduce(math.gcd,[abs(c) for c in ints]);ints=[c//div for c in ints]
 PP=s.expand(sum(c*X**(degree-k)*Y**k for k,c in enumerate(ints)))
 LL=s.expand(-s.diff(PP,X)*f1-s.diff(PP,Y)*f2)
 p=s.Poly(PP.subs({X:t,Y:1}),t);l=s.Poly(LL.subs({X:t,Y:1}),t)
 pr=int(p.count_roots(-s.oo,s.oo));lr=int(l.count_roots(-s.oo,s.oo));success=pr==lr==0 and p.eval(0)>0 and l.eval(0)>0 and PP.subs({X:1,Y:0})>0 and LL.subs({X:1,Y:0})>0
 trials.append({'rounding_denominator':denominator,'P_roots':pr,'negative_lie_roots':lr,'exact_positive':bool(success)})
 if success:
  result={'degree':int(degree),'integer_coefficients_descending_X':ints,'P':str(PP),'negative_Lie':str(LL),'P_sturm':sturmdata(p),'negative_Lie_sturm':sturmdata(l),'P_at_01':str(p.eval(0)),'negative_Lie_at_01':str(l.eval(0)),'P_at_10':str(PP.subs({X:1,Y:0})),'negative_Lie_at_10':str(LL.subs({X:1,Y:0}))}
  break
else:raise AssertionError('No simplified exact certificate')
data={'created_at':datetime.now(timezone.utc).isoformat(),'scope':'Exact positive degree8 certificate at a=2; no assertion that degree8 is minimal. Trials that fail remain visible.','rounding_trials':trials,'certificate':result}
out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8');print(json.dumps(data,indent=2))
