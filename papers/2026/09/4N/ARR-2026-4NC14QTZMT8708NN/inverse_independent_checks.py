"""Independent review of the final inverse, without importing its verifier.

The endpoint equations are solved afresh for the denominator. Exact Sturm
counts attack the cubic branch choice on a bounded rational parameter grid.
The arbitrary-parameter conclusions rely on the separately written proof review.
"""
from pathlib import Path
from itertools import product
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parent


def zero(expression):
    assert S.factor(S.cancel(expression)) == 0, expression


def symbolic_checks():
    z, y, m, d = S.symbols('z y m d', real=True)
    g = S.symbols('g', positive=True)
    B, C = S.symbols('B C')
    epsilon = 1/(g+1)
    t = m+y
    u, v = d-m, d+m
    Q = (1-epsilon)*(z-t)**2
    H = z*z+2*B*z+C
    solved = S.solve([(Q-epsilon*H).subs(z,-u),
                      (Q-epsilon*H).subs(z,v)],(B,C),dict=True)[0]
    B0, C0 = (S.factor(solved[x]) for x in (B,C))
    zero(B0+m+g*y)
    zero(C0-(m*m+2*g*m*y+g*y*y+(g-1)*d*d))
    H0 = H.subs(solved)
    zero(H0-g*(z-t)**2-(g-1)*(u+z)*(v-z))
    M = S.Matrix([[1,B0],[B0,C0]])
    P = S.Poly(H0-Q,z)
    residual_matrix = S.Matrix([[P.nth(2),P.nth(1)/2],
                                [P.nth(1)/2,P.nth(0)]])
    det = S.factor(M.det())
    zero(det-(g-1)*(d*d-g*y*y))
    zero(residual_matrix.det()-(g-1)/(g+1)*(d*d-g*g*y*y))
    N = S.trace(M)
    numerator = S.factor(2*S.diff(N,y)*det-N*S.diff(det,y))
    G = g*y**3-(1+m*m+(g+1)*d*d)*y-2*m*d*d
    zero(numerator+2*g*(g-1)*G)
    zero(G.subs(y,d/S.sqrt(g)) + d/S.sqrt(g)*(1+(m+d*S.sqrt(g))**2))
    active_C = S.factor(C0.subs(y,d/g))
    active_L2 = d*d*(g-1)**2/g
    zero(active_C-v*v-active_L2)
    zero(B0.subs(y,d/g)+v)
    active_L = d*(g-1)/S.sqrt(g)
    signed_w = (active_L2-1-v*v)/(2*active_L)
    zero(G.subs(y,d/g)-2*d*active_L/g*(signed_w-v*S.sqrt(g)))
    # First-cap comparison is obtained from the Rayleigh eigenvalue equation.
    e = S.symbols('e',real=True)
    lam = e/(1-2*e)
    poly = S.factor((lam*lam-(u*v-1)*lam-d*d)*(1-2*e)**2)
    zero(poly-(e*e-(u*v-1)*e*(1-2*e)-d*d*(1-2*e)**2))
    return {'denominator_solved_from_endpoint_equalities':str(H0),
            'residual_determinant':str(S.factor(residual_matrix.det())),
            'derivative_numerator':str(numerator),
            'identities':'PASS'}


def sturm_grid():
    y = S.symbols('y')
    gaps = [S.Rational(1,20),S.Rational(1,3),S.Integer(1),
            S.Integer(2),S.Integer(5),S.Integer(12)]
    rows = []
    for u0,v0,n in product(gaps,gaps,(2,3,4,7)):
        if u0<v0:
            continue
        u,v = u0,v0
        g=S.Integer(n*n); e=1/(g+1)
        d=(u+v)/2; m=(v-u)/2
        first=e*e-(u*v-1)*e*(1-2*e)-d*d*(1-2*e)**2
        if first>=0:
            continue
        cap=d/g; far=d/n
        G=S.Poly(g*y**3-(1+m*m+(g+1)*d*d)*y-2*m*d*d,y)
        if m==0:
            assert G.eval(0)==0
            assert G.count_roots(-far,far)==1
            phase='symmetric'
        else:
            assert G.eval(0)>0 and G.eval(far)<0
            assert G.count_roots(-far,0)==0
            assert G.count_roots(0,far)==1
            margin=G.eval(cap)
            phase='active' if margin>0 else ('boundary' if margin==0 else 'inactive')
            if margin<0:
                assert G.count_roots(0,cap)==1
            elif margin>0:
                assert G.count_roots(0,cap)==0
            else:
                assert G.eval(cap)==0
            if margin>=0:
                # In particular, the plus sign L=p+w is not an extraneous branch.
                L2=d*d*(g-1)**2/g
                assert L2>1+v*v
                assert u>3*v
        assert d*d*(g-1)**2/g>0
        rows.append({'u':str(u),'v':str(v),'g':str(g),'phase':phase})
    assert {'active','inactive','symmetric'} <= {row['phase'] for row in rows}
    return rows


def exact_fixtures():
    rows=[]
    y=S.symbols('y')
    for u,v,e,yy,bb,cc,peak,phase in [
        ('2','1','35/123','1/4','-9/70','223/70',
         '(sqrt(15529)+9*sqrt(53))/106','inactive'),
        ('1399/180','9/20','16/41','592/225','-9/20','29/8','2','active'),
        ('165/28','9/20','9/25','999/560','-9/20','29/8','2','boundary'),
        ('1','1','1/6','0','0','4','2','symmetric')]:
        u,v,e,yy,bb,cc = map(S.Rational,(u,v,e,yy,bb,cc))
        d=(u+v)/2; m=(v-u)/2; g=(1-e)/e
        G=S.Poly(g*y**3-(1+m*m+(g+1)*d*d)*y-2*m*d*d,y)
        B=-m-g*yy; C=m*m+2*g*m*yy+g*yy*yy+(g-1)*d*d
        zero(B-bb);zero(C-cc)
        if phase in ('inactive','symmetric'):
            zero(G.eval(yy))
            assert abs(yy)<d/g
        else:
            zero(yy-d/g)
            assert G.eval(yy)>0 if phase=='active' else G.eval(yy)==0
        pp=(1+C)/(2*S.sqrt(C-B*B))
        TT=pp+S.sqrt(pp*pp-1)
        zero(TT-S.sympify(peak))
        assert pp>1 and C-B*B>0
        rows.append({'u':str(u),'v':str(v),'epsilon':str(e),'phase':phase,
                     'B':str(B),'C':str(C),'minimum_delay':str(S.simplify(TT))})
    # Distinguish the correct transition root and the squared-error convention.
    Qc=(8+S.sqrt(10))/27
    zero(S.Rational(1,9)/Qc-(8-S.sqrt(10))/18)
    # The symmetric first-cap threshold is exactly 1/3, not sqrt(1/3).
    e1=S.Rational(1,3)
    for ee in [S.Rational(1,3)-S.Rational(1,10**30), e1,
               S.Rational(1,3)+S.Rational(1,10**30),S.Rational(1,2)]:
        first=ee*ee-(1-2*ee)**2
        assert S.sign(first)==S.sign(ee-e1)
    return rows


if __name__=='__main__':
    report={'status':'PASS','independence':'No import or execution of the deriving-agent verifier.',
            'symbolic':symbolic_checks(),'sturm_grid':sturm_grid(),
            'exact_fixtures':exact_fixtures()}
    report['hashes']={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                      for name in ('active_delay.md','verify_active_delay.py',Path(__file__).name)}
    (ROOT/'inverse_independent_checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':report['status'],'exact_sturm_cases':len(report['sturm_grid']),
                      'exact_fixtures':len(report['exact_fixtures'])}))
