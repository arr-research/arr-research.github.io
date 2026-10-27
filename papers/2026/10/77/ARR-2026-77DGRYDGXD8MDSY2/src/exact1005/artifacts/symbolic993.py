from pathlib import Path
import sympy as s,json
p=Path(__file__).parent;e,l=s.symbols('e l',positive=True);x,y,z=s.symbols('x y z',real=True)
W=s.Matrix([[1+l,2*l*e],[2*l*e,2*e*e]])/(4*(1+e*e))
Z=s.Matrix([[0,-1],[-1,-2*e]]);Y=s.Matrix([[x,y],[y,z]])
eq=W*Y+Y*W-2*Z
sol=s.solve([eq[0,0],eq[0,1],eq[1,1]],(x,y,z));YY=s.simplify(Y.subs(sol))
assert s.simplify(W*YY+YY*W-2*Z)==s.zeros(2)
gout=s.factor(2*l*l*s.trace(Z*YY));gin=16*(1+e*e)
ratio=s.factor(gout/gin);limit=s.factor(s.limit(ratio,e,0,dir='+'));target=3*l*l/(1+2*l)
assert s.simplify(limit-target)==0
gap=s.factor(target-ratio)
result=dict(scope='Exact2x2 Sylvester algebra for a rank2 ladder tangent. Boundary/faithful limit still requires analytic argument; not BKM/MI or priority claim.',output_block=[[str(a) for a in row] for row in W.tolist()],direction_block=[[str(a) for a in row] for row in Z.tolist()],input_metric=str(gin),output_metric=str(gout),ratio=str(ratio),limit=str(limit),gap=str(gap),lambda_half_limit=str(limit.subs(l,s.Rational(1,2))),sylvester_identity_verified=True)
(p/'SYMBOLIC993.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
