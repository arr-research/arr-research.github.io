from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json
R=Path(__file__).resolve().parent;out=R/'checks-36a.json';assert not out.exists()
x,y,t=s.symbols('x y t',real=True);rho=x*x+y*y;Q=11*x*x+y*y
f=-x**5+16*x**3*y**2-3*x*y**4;g=x**4*y+20*x*x*y**3-y**5
V=Q**11/rho**10
loglie=s.cancel((s.diff(V,x)*f+s.diff(V,y)*g)/V)
# Central normalized derivative: -1-25 sin^2(phi)(1-cos(phi))/(6+5cos(phi)).
circle=s.factor(loglie/(2*rho**2))
expected=-1-25*(4*x*x*y*y/rho**2)*(1-(x*x-y*y)/rho)/(6+5*(x*x-y*y)/rho)
assert s.cancel(circle-expected)==0
assert s.expand((6+5*t)**2-11*(1-t*t)-(5+6*t)**2)==0
assert s.Rational(3025,11)==275 and 275<17**2
assert -1+s.Rational(1,20)*(1+17)==-s.Rational(1,10)
result={'at':datetime.now(timezone.utc).isoformat(),'central_log_derivative':str(circle),
 'common_numerator_degree':22,'common_denominator_degree':20,
 'robust_normalized_Lie_upper_bound':'-1/10','exact_symbolic_checks':True,
 'scope':'Finite identities only, no formal verification or grade.'}
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
