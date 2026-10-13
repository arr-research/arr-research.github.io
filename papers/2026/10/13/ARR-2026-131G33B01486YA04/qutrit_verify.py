"""Exact checks for the two-rate qutrit witness. No numerical search is a proof."""
import json, pathlib, hashlib
import sympy as s

ROOT = pathlib.Path(__file__).parent
x, y, p, d, q, z, t, R = s.symbols('x y p d q z t R', real=True)
g = lambda r, u: s.sympify(r)**2/(s.sympify(r)**2+s.sympify(u)**2)
A = lambda r, u, v: (g(r,u)+g(r,v))/2
Delta=(1+x*x)*(16+x*x)*(1+y*y)*(16+y*y)*(16+(x+y)**2)
B=p**4+15*p**3+108*(p-s.Rational(46,27))**2+s.Rational(1904,27)
P=(5*p*p+48)*d*d+2*B*d+8*p*(p-2)**2*(p+1)*(p+16)
Pn=(5*q*q+48)*z*z+(2*q**4+10*q**3+216*q*q+1120*q+768)*z+64*q**4+1248*q**3+3744*q*q+2560*q
checks={}
def check(name, expression):
    value=s.factor(expression)
    assert value==0,(name,value)
    checks[name]=True
check('cleared rational identity',5-A(1,x,y)-9*A(4,x,y)+5*g(4,x+y)-5*P.subs({p:x*y,d:(x-y)**2})/(2*Delta))
check('axis asymptotic saturation identity',5-A(1,x,0)-9*A(4,x,0)+5*g(4,x)-15*x*x/(2*(1+x*x)*(16+x*x)))
check('opposite-sign polynomial representation',P.subs(d,z-4*p).subs(p,-q)-Pn)
check('positive quartic decomposition',B-(p**4+15*p**3+108*p*p-368*p+384))
for xx,yy in [(0,0),(s.sqrt(2),s.sqrt(2)),(-s.sqrt(2),-s.sqrt(2))]:
    check(f'equality at {xx},{yy}',P.subs({p:xx*yy,d:(xx-yy)**2}))
check('zero restriction with d=0',P.subs(d,0)-8*p*(p-2)**2*(p+1)*(p+16))
violation=t*(7-5*t)/((1+t)*(4+t))
check('semigroup violation',1/(1+t)+36/(4+t)-5/(1+t)-5-violation)
check('optimizing derivative',s.diff(violation,t)+4*(2*t-1)*(4*t+7)/((t+1)**2*(t+4)**2))
check('maximal violation',violation.subs(t,s.Rational(1,2))-s.Rational(1,3))
points=[(0,0,s.Rational(19,45)),(s.sqrt(2),s.sqrt(2),s.Rational(1,5)),(-s.sqrt(2),-s.sqrt(2),s.Rational(1,5)),(0,R,s.Rational(2,45)),(R,0,s.Rational(2,45)),(0,-R,s.Rational(2,45)),(-R,0,s.Rational(2,45))]
check('normalization',sum(w for u,v,w in points)-1)
features=[lambda u,v:A(1,u,v),lambda u,v:A(4,u,v),lambda u,v:g(4,u+v)]
actual=[s.factor(sum(w*f(u,v) for u,v,w in points)) for f in features]
expected=[s.Rational(29,45)+s.Rational(4,45)*g(1,R),s.Rational(13,15)+s.Rational(4,45)*g(4,R),s.Rational(31,45)+s.Rational(8,45)*g(4,R)]
for i in range(3):check(f'seven-point feature {i}',actual[i]-expected[i])
target=s.Matrix([s.Rational(2,3),s.Rational(8,9),s.Rational(2,3)])
limit=s.Matrix([s.limit(a,R,s.oo) for a in actual])
check('sharp distance supporting plane',(s.Matrix([[1,9,-5]])*target)[0]-5-15*s.Rational(1,45))
assert list(limit-target)==[-s.Rational(1,45),-s.Rational(1,45),s.Rational(1,45)]
checks['all coordinate limits and exact infimum']=True
check('finite R third error',actual[2]-target[2]-s.Rational(1,45)-s.Rational(128,45)/(16+R*R))
# Other errors are -e+(4/45)g_r, while third is e+(8/45)g_4;
# 0 <= g_1 <= g_4 <= 1, so third dominates both absolute errors.
check('monotone kernel difference',g(4,R)-g(1,R)-15*R*R/((16+R*R)*(1+R*R)))
assert s.Rational(13,15)<s.Rational(8,9)
checks['nonattainment equality-support obstruction']=True
nu,gamma=s.symbols('nu gamma',positive=True)
for k in [1,2]:check(f'single-rate alias k={k}',g(nu,k*s.sqrt(gamma*nu))-nu/(nu+k*k*gamma))
# Direct physical dephasing eigenvalues from the double commutator.
D=s.diag(0,1,2)
for j,k in [(0,1),(1,2),(0,2)]:
    E=s.zeros(3);E[j,k]=1
    out=-gamma*(D*(D*E-E*D)-(D*E-E*D)*D)
    assert out == -gamma*(j-k)**2*E
checks['Lindblad coherence rates']=True
v,h,u=s.symbols('v h u',positive=True)
check('population monotonicity derivative',s.diff(h*h/(v*v+h*h),v)+2*v*h*h/(v*v+h*h)**2)
check('robust witness coefficient',(1+9+5)*(2*s.sqrt(2)*u+2*u*u)-(30*s.sqrt(2)*u+30*u*u))
u_star=(2*s.sqrt(115)-15*s.sqrt(2))/30
check('population leakage threshold',30*s.sqrt(2)*u_star+30*u_star*u_star-s.Rational(1,3))
source=ROOT/'qutrit-paper.tex'
if not source.exists(): source=ROOT/'qutrit-candidate.tex'
report={'status':'PASS','exact_checks':len(checks),'checks':checks,
        'main_bound':'W <= 5','reference_value':'16/3',
        'selected_data_infimum':'1/45','infimum_attained':False,
        'proof_scope':'Static diagonal qutrit Hamiltonian ensembles; selected real statistics only',
        'robust_bound':'W <= 5 + 30 sqrt(2 delta) + 30 delta',
        'not_proved_by_script':['Priority','Analytic measure-theoretic proof of surrogate (see manuscript)','Optimality among every witness','Full-state distance'],
        'source_file':source.name,
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
(ROOT/'qutrit-verification.json').write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps(report,indent=2))
