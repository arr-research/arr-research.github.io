"""Exact controls of corrected hypotheses and comparisons, not a new search."""
from pathlib import Path
import datetime,json
import sympy as s
ROOT=Path(__file__).resolve().parent
u,e,l,r=s.symbols('u e l r',positive=True)
xi=u/(1+u)
support=s.factor(s.Rational(1,2)-xi/3)
kernel=s.factor(xi/6)
assert support.is_positive and kernel.is_positive
g=s.factor(8*e**2/support+8/(support+kernel))
assert s.simplify(s.limit(g,u,0,dir='+')-16*(1+e**2))==0
S=r**2/(l+(1-l)*r)+(1-r)/(1-l)
h=s.factor(1-1/S)
assert s.simplify(h-l*l*(1-r)/(l+(1-2*l)*r))==0
derivative=s.factor(s.diff(h,r))
assert s.simplify(derivative+l*l*(1-l)/(l+(1-2*l)*r)**2)==0
assert s.simplify(h.subs(r,0)-l)==0
gap=s.factor(3*l*l/(1+2*l)-l*l)
assert gap.subs(l,s.Rational(1,2))==s.Rational(1,8)
sigma=s.eye(4)/4
z=s.kronecker_product(s.eye(2)/2,s.diag(1,-1))
pt=lambda x:s.Matrix(2,2,lambda i,j:x[i,j]+x[2+i,2+j])
N=lambda x:l*x+(1-l)*s.kronecker_product(s.eye(2)/2,pt(x))
assert s.simplify(N(sigma)-sigma)==s.zeros(4)
assert s.simplify(N(z)-z)==s.zeros(4)
assert pt(z)!=s.zeros(2)
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'checks':[
  {'id':'C1','status':'pass','purpose':'Corrected0<xi<1 makes both eigenvalue classes positive; xi=u/(1+u),u>0.','support_eigenvalue':str(support),'kernel_eigenvalue':str(kernel),'regularized_metric_limit':str(s.limit(g,u,0,dir='+'))},
  {'id':'C2','status':'pass','purpose':'Scalar convex-representation formula, derivative and absent-identity endpoint.','h':str(h),'derivative':str(derivative),'h_at_r0':str(h.subs(r,0)),'condition':'Derivative strictly negative for0<lambda<1; q0=0 causes no zero output weight sincew0=lambda.'},
  {'id':'C3','status':'pass','purpose':'Ordinary versus complete depolarizing comparison.','gap':str(gap),'ordinary_half':'1/4','complete_half':'3/8'},
  {'id':'C4','status':'pass','purpose':'Explicit reference-only tangent yields unrestricted ratio1 but is excluded byTr_AZ=0.','sigma':'I4/4','tangent':'I2/2 tensor diag(1,-1)','partial_trace_nonzero':True,'SLD_ratio':1}
 ],'failures':0,'scope':'Four exact targeted controls. The universal upper and ordered triangular limits are assessed analytically; no universal claim is inferred from finite tests.'}
with (ROOT/'CONTROLS1006.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False,indent=2))
