from pathlib import Path
import json
import numpy as np
import sympy as s

root=Path(__file__).parent
x=s.symbols('x', real=True)
p=s.symbols('p', real=True)
h=-s.log(1-3*p+3*p*p)/2 # base change does not change -h''/h'
A=-s.diff(h,p,2)/s.diff(h,p)
assert s.simplify(A.subs(p,(1-x)/2)-2*(1-3*x*x)/(x*(1+3*x*x)))==0
B=lambda z:z*(1+3*z*z)/(1-3*z*z)
q=x*(1-x)
assert s.factor(B(x)+B(1-x)-(4-12*q-9*q*q)/((1-3*x*x)*(1-3*(1-x)**2)))==0
assert s.simplify(s.diff(B(x)/x,x)-12*x/(1-3*x*x)**2)==0
assert 4-12*s.Rational(1,4)-9*s.Rational(1,4)**2==s.Rational(7,16)
f=lambda z:1-3*z+3*z*z
assert f(s.Rational(1,10))**2-f(s.Rational(1,20))*f(s.Rational(3,20))==s.Rational(543,160000)
f4=lambda z:z**4+(1-z)**4
assert f4(s.Rational(1,4))**2-f4(s.Rational(1,5))*f4(s.Rational(3,10))==s.Rational(3457649,6400000000)
rng=np.random.default_rng(2026101710)
xx=rng.dirichlet(np.ones(3),size=100000)
aa=2*(1-3*xx**2)/(xx*(1+3*xx**2))
trace=aa[:,0]+aa[:,1]+2*aa[:,2]
disc=np.sqrt((aa[:,0]-aa[:,1])**2+4*aa[:,2]**2)
minimum_eigen=float(((trace-disc)/2).min())
assert minimum_eigen>0
H=lambda p:-.5*np.log2(1-3*p+3*p*p)
phi=lambda z:(3-np.sqrt(np.maximum(12*np.exp2(-2*z)-3,0)))/6
def graph(z):
    total=phi(z).sum(axis=1)
    return np.where(total<=.5,1,H(1-total))
a=rng.random((50000,2)); b=rng.random((50000,2)); t=rng.random((50000,1))
gaps=graph(t*a+(1-t)*b)-t[:,0]*graph(a)-(1-t[:,0])*graph(b)
assert gaps.min()>-3e-13
report={'status':'PASS','seed':2026101710,'exact_symbolic_identities':6,'boundary_curvature_cases':len(xx),'minimum_tangent_matrix_eigenvalue_numeric':minimum_eigen,'full_square_jensen_cases':len(a),'minimum_jensen_gap_numeric':float(gaps.min()),'scope':'Author-context supplementary diagnostics; not independent review, formal verification or priority certification.'}
(root/'minimality-diagnostics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
