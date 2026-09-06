"""Separate internal checks: disk Poisson kernels and exact route fixtures.

Does not import the constructing verifier or numerical exploration.
"""
from pathlib import Path
from itertools import product
import hashlib
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
# Revision 1 source binding; original audited source: a4d59c248eab267df4fcf746f0fc493fa77853a27aed1ab6259986290a0bc2d2
# Mathematical checks unchanged; see CAMBIOS.md and the separate delta review.
# Publication-only front matter; accepted review source: 2e105f5027d0abdbd4cd0b97c971aea20a3b16d080eb5d0611a664637b78b886
EXPECTED='9a4d1a206d5a994c7d32f7ab1bdbd7786fe9cff00e13a8f146f4676c3873b8ad'
checks=[]


def check(label, truth, detail=None):
    if not bool(truth): raise AssertionError(label)
    checks.append({'label':label,'status':'PASS','detail':detail})


def zero(label, expression):
    check(label,s.simplify(s.expand_complex(expression))==0)


def feasible(V,Y,K,D):
    a=Y*Y-2*V+2*D
    b=Y*Y*K
    c=V*V+Y*Y*K*K-D*D
    return (Y>0 and V>K*K and a>=0 and c>=0 and a*c>=b*b)


def direct_disk_fixtures():
    # Roots chosen first, before the manuscript's V,Y,K parameters.
    # (real part, upper imaginary parts, half-gap squared, translation)
    rows=[(s.Integer(1),s.Integer(1),s.Integer(2),s.Integer(3),s.Rational(1,2)),
          (s.Integer(1),s.Integer(2),s.Integer(3),s.Integer(1),s.Rational(1,3)),
          (s.Integer(0),s.Integer(1),s.Integer(1),s.Rational(1,4),s.Integer(0))]
    records=[]
    for j,(r,e1,e2,D,m) in enumerate(rows):
        poles=(r+s.I*e1,-r+s.I*e2)
        V=r*r+e1*e2;Y=e1+e2;K=r*(e1-e2)/Y
        check(f'fixture {j}: polynomial positivity and stability',feasible(V,Y,K,D))
        alphas=[s.cancel((s.conjugate(beta)+m+s.I)/(s.conjugate(beta)+m-s.I))
                for beta in poles]
        for alpha in alphas:
            check(f'fixture {j}: determinant zero strictly in disk',s.simplify(alpha*s.conjugate(alpha))<1)
        a=Y*Y-2*V+2*D;b=Y*Y*K;c=V*V+Y*Y*K*K-D*D
        t=s.symbols('t',real=True)
        p=s.sqrt(a)*t+b/s.sqrt(a)+s.I*s.sqrt(c-b*b/a)
        q=t*t-D
        h=(t-poles[0])*(t-poles[1])
        M=s.Matrix([[p,-q],[q,s.conjugate(p)]])
        for sign in (-1,1):
            node=sign*s.sqrt(D)
            zero(f'fixture {j}: repeated-node q zero {sign}',q.subs(t,node))
            zero(f'fixture {j}: repeated-node amplitude {sign}',
                 (p*s.conjugate(p)-h*s.conjugate(h)).subs(t,node))
        check(f'fixture {j}: exceptional output at infinity',
              s.limit(p/h,t,s.oo)==0 and s.limit(q/h,t,s.oo)==1)
        # Rational boundary samples are checked exactly, not by a float tolerance.
        for coordinate in map(s.Rational,(-3,-1,0,1,2,4)):
            S=(M/h).subs(t,coordinate)
            for entry in (s.conjugate(S.T)*S-s.eye(2)):
                zero(f'fixture {j}: boundary unitarity at {coordinate}',entry)
            z=s.cancel((coordinate+m+s.I)/(coordinate+m-s.I))
            poisson=sum(s.cancel((1-alpha*s.conjugate(alpha))/
                                ((z-alpha)*s.conjugate(z-alpha))) for alpha in alphas)
            formula=Y*(1+(coordinate+m)**2)*(coordinate**2+2*K*coordinate+V)/(
                    (coordinate**2-V)**2+Y*Y*(coordinate+K)**2)
            zero(f'fixture {j}: direct disk Poisson delay at {coordinate}',poisson-formula)
        records.append({'V':str(V),'Y':str(Y),'K':str(K),'half_gap_squared':str(D),
                        'translation':str(m),'disk_zeros':list(map(str,alphas))})
    # Sign omission found during review would fail this negative control.
    check('negative Y is rejected despite nonnegative residual power',
          not feasible(s.Integer(3),s.Integer(-3),s.Rational(-1,3),s.Integer(3)))
    check('real denominator zero is rejected',
          not feasible(s.Integer(1),s.Integer(1),s.Integer(1),s.Integer(1)))
    check('acute constant-delay denominator is rejected by residual power',
          not feasible(s.Integer(1),s.Integer(2),s.Integer(0),s.Integer(4)))
    return records


def acute_peak():
    # The derivative gives a direct global proof without using the author's SOS.
    x=s.symbols('x',nonnegative=True)
    V=s.Rational(11,5);Y=4*s.sqrt(11)/5
    tau=Y*(x+1)*(x+V)/((x-V)**2+Y*Y*x)
    derivative=-40*s.sqrt(11)*(x-11)*(7*x+11)/(25*x*x+66*x+121)**2
    zero('acute fixture derivative factorization',s.diff(tau,x)-derivative)
    zero('acute fixture maximum value',tau.subs(x,11)-9/s.sqrt(11))
    check('acute fixture increasing before x=11',derivative.subs(x,1)>0)
    check('acute fixture decreasing after x=11',derivative.subs(x,12)<0)
    check('acute fixture infinity below peak',s.limit(tau,x,s.oo)<9/s.sqrt(11))
    check('acute fixture zero below peak',tau.subs(x,0)<9/s.sqrt(11))
    check('acute fixture strictly improves double-pole cap',9/s.sqrt(11)<2*s.sqrt(V))
    # Reconstruct the general cubic by differentiating the reduced stationary
    # value, instead of reading it from the proposed certificate.
    w=s.symbols('w',positive=True)
    reduced=(x+1)*(x+w)/(2*s.sqrt(x)*(x-w))
    numerator=s.factor(s.diff(reduced,x)*4*x**s.Rational(3,2)*(x-w)**2)
    cubic=x**3-(4*w+1)*x*x-(w*w+4*w)*x+w*w
    zero('stationary derivative independently recovers the cubic',numerator-cubic)


def fourier_geometry():
    # Algebraic overshoot formula in the paper's rational cotangent variables.
    u,v=s.symbols('u v',positive=True)
    norm=s.sqrt((1+u*u)*(1+v*v))
    cos_alpha=(u*v-1)/norm;cos_beta=(u*v+1)/norm
    zero('overshoot trigonometric denominator',cos_beta-cos_alpha-2/norm)
    zero('asymmetry equality obstruction',norm**2-(u*v+1)**2-(u-v)**2)
    examples=[]
    for up,vp in [(s.Rational(1,2),s.Rational(1,2)),(s.Integer(1),s.Integer(1)),
                  (s.Rational(3,2),s.Rational(3,2)),(s.Integer(2),s.Integer(1)),
                  (s.Rational(1,3),s.Rational(2,3))]:
        M=(s.sqrt((1+up*up)*(1+vp*vp))+abs(up*vp-1))/2
        eta=(M-1)/(M+1)
        gap=(s.sqrt(9+8*eta)-3)/2
        check(f'overshoot >=1 at {up},{vp}',s.simplify(M>=1))
        check(f'gap locus at {up},{vp}',bool(s.simplify(eta==0))==(up==vp and up<=1))
        zero(f'gap inversion at {up},{vp}',gap*gap+3*gap-2*eta)
        examples.append({'u':str(up),'v':str(vp),'M':str(M),'eta':str(eta),'gap':str(gap)})
    # Fourier moment step for arbitrary two zeros is checked as an identity.
    a,b=s.symbols('a b')
    check('second-moment identity',s.expand((a+b)**2-(a*a+b*b)-2*a*b)==0)
    return examples


def main():
    digest=hashlib.sha256((ROOT/'paper.md').read_bytes()).hexdigest()
    check('publication source hash is frozen',digest==EXPECTED,digest)
    fixtures=direct_disk_fixtures()
    acute_peak()
    gap=fourier_geometry()
    result={'status':'PASS','checks':checks,'check_count':len(checks),
            'reviewed_manuscript_sha256':digest,
            'reviewer_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'disk_fixtures':fixtures,'overshoot_fixtures':gap,
            'method':'Separate agent; no import of constructor verifier. Exact disk Poisson kernels, boundary matrices, derivative signs and algebraic overshoot.',
            'limitations':'Targeted exact checks and proof reading, not formal proof verification or a proof of unrestricted acute optimality.'}
    (Path(__file__).parent/'quantum_agent_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','check_count','reviewed_manuscript_sha256')},indent=2))


if __name__=='__main__':main()
