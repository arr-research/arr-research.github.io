"""Independent active delay review; no import of the deriving agent's code.
Reconstruct dual weights by solving moment equations, and verify exact
rational active/boundary fixtures plus global polynomial completions.
"""
from pathlib import Path
import hashlib,json,time
import sympy as S
ROOT=Path(__file__).resolve().parent
def zero(x):assert S.factor(S.cancel(x))==0
def sharp(poly,z):
    coeff=[S.expand(poly).coeff(z,i) for i in range(2)]
    return S.conjugate(coeff[1])+S.conjugate(coeff[0])*z

def main():
    start=time.monotonic();z=S.symbols('z',real=True)
    y,L,v=S.symbols('y L v',positive=True);tau=S.symbols('tau',real=True)
    # tau is algebraically free here; its geometric sign is used in the proof.
    u=2*L*y/(1-y*y)-v;e=y*y/(1+y*y);k=1/(1+y*y)
    t=v-L*y;r=v+L/y
    lm,lp,nu=S.symbols('lm lp nu')
    solved=S.solve([
        lm+lp-1,
        lm*(-u-t)+lp*(v-t)+nu*(r-t),
        e*(-u*lm+v*lp)+nu*r-(e+nu)*tau],(lm,lp,nu),dict=True)[0]
    h=k*r+e*t
    zero(solved[nu]-e*(tau-t)/(h-tau))
    zero(solved[lp]-(r+t-2*tau)/(2*(h-tau)))
    lm0,lp0,nu0=(solved[a] for a in (lm,lp,nu));mu0=1+nu0
    l0=lm0*u*u+lp0*v*v+nu0*r*r-mu0*t*t
    A,B,C=S.symbols('A B C');poly=lambda w:A*w*w+B*w+C
    zero(l0*A-lm0*poly(-u)-lp0*poly(v)-nu0*poly(r)+mu0*poly(t))
    Q=lambda w:k*(w-t)**2;P=lambda w:e*(w-r)**2;H=lambda w:(w-v)**2+L*L
    zero(Q(z)+P(z)-H(z));zero(Q(-u)-e*H(-u));zero(Q(v)-e*H(v))
    beta=e*(lm0*u*u+lp0*v*v)+nu0*r*r-(e+nu0)*tau*tau
    zero(l0*k-(e+nu0)*H(tau)-beta)
    # Reconstruct the transition polynomial directly from the unsquared equation.
    U,V,Y=S.symbols('U V Y');K=U*U-U*V-V*V+1
    delta=((U-V)*Y-2*U*V*V)**2-4*V*V*(Y+1)*(Y-V*V)
    zero(delta-((U-3*V)*(U+V)*Y*Y-4*V*V*K*Y+4*V**4*(U*U+1)))
    zero(delta.subs(Y,2*V*V)+4*V**4*(1+V*V))
    # Independent expansion of the first two high-cap terms, using h=1/T.
    hh,d=S.symbols('h d',positive=True);vv=S.symbols('vv',positive=True)
    pp=(1/hh+hh)/2;qq=(1/hh-hh)/2
    ell=pp+S.sqrt(qq*qq-vv*vv)
    active=(1-ell/S.sqrt(ell*ell+4*d*d))/2
    expanded=S.series(active,hh,0,6).removeO()
    zero(expanded-d*d*hh*hh-(2*vv*vv*d*d-3*d**4)*hh**4)
    fixtures=[]
    for TT in [S.Rational(3,2),S.Integer(2),S.Integer(5)]:
        p=(TT+1/TT)/2;q=(TT-1/TT)/2
        for ratio in [S.Rational(1,5),S.Rational(1,4),S.Rational(1,3)]:
            v=q*2*ratio/(1+ratio*ratio);w=q*(1-ratio*ratio)/(1+ratio*ratio)
            assert w>v>0;L=p+w;tau=-p*v/w
            for phase,y in [('boundary',v/w),('active',(1+v/w)/2)]:
                u=2*L*y/(1-y*y)-v;e=y*y/(1+y*y);k=1-e
                t=v-L*y;r=v+L/y;h=k*r+e*t
                weights=S.solve([lm+lp-1,lm*(-u-t)+lp*(v-t)+nu*(r-t),e*(-u*lm+v*lp)+nu*r-(e+nu)*tau],(lm,lp,nu),dict=True)[0]
                assert weights[lm]>0 and weights[lp]>0 and weights[nu]>=0
                assert (weights[nu]>0)==(phase=='active')
                Uc=v*(q*q+2*p*w)/(q*q-2*v*v)
                assert (u==Uc) if phase=='boundary' else (u>Uc)
                qz=S.sqrt(k)*(S.I*(z+1)-t*(z-1))
                pz=S.sqrt(e)*(S.I*(z+1)-r*(z-1))
                hz=S.I*(z+1)+(-v-S.I*L)*(z-1)
                zero(pz*sharp(pz,z)+qz*sharp(qz,z)-hz*sharp(hz,z))
                h0=S.expand(hz).coeff(z,0);h1=S.expand(hz).coeff(z,1)
                zero(h0*S.conjugate(h0)-h1*S.conjugate(h1)-4*L)
                # Direct exact peak algebra, with no angular samples.
                CC=v*v+L*L
                zero((1-CC)**2+4*v*v-(q/p)**2*(1+CC)**2)
                assert CC-v*v>0
                fixtures.append(dict(phase=phase,T=str(TT),u=str(u),v=str(v),e=str(e),lambda_minus=str(weights[lm]),lambda_plus=str(weights[lp]),nu=str(weights[nu]),global_lossless_polynomial_identity=True,global_cap_equality=True))
    # Inactive symmetric fixtures exercise the positive-definite residual branch.
    inactive=[]
    for c,TT in [(S.Integer(1),S.Integer(1)),(S.Rational(2,3),S.Integer(2)),(S.Integer(3),S.Integer(5))]:
        e=c*c/(TT*TT+2*c*c);k=1-e
        qz=S.sqrt(k)*S.I*(z+1)
        pz=S.sqrt(e)*S.I*(z+1)+S.I*TT*(z-1)
        hz=S.I*(z+1)-S.I*TT*(z-1)
        zero(pz*sharp(pz,z)+qz*sharp(qz,z)-hz*sharp(hz,z))
        inactive.append(dict(c=str(c),T=str(TT),e=str(e),global_polynomial_identity=True))
    # Document the interface issue found in the original degree-zero return.
    aa=S.sqrt(S.Rational(1,2));wrong_det=S.det(S.Matrix([[aa,-aa*z],[aa,aa*z]]))
    zero(wrong_det-z)
    constant=S.Matrix([[aa,-aa],[aa,aa]]);zero(S.det(constant)-1)
    assert constant.conjugate().T*constant==S.eye(2)
    report=dict(status='PASS',elapsed_seconds=time.monotonic()-start,independence='No imports or executions of deriving-agent verifier. Dual weights solved from moment equations; rational hyperboloid fixtures generated independently.',universal_symbolic_checks=['dual weights from linear moments','universal quadratic identity','active global denominator decomposition','two endpoint equalities','positive lambda_plus factor','dual support equality constant','transition unsquared polynomial and root separation','active T^-2 and T^-4 expansion'],active_boundary_exact_fixtures=fixtures,inactive_exact_fixtures=inactive,constant_completion_regression=dict(original_degree_one_sharp_det='z',correct_constant_det='1',degree_zero_unitarity=True),source_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),ROOT/'active_delay.md',ROOT/'verify_active_delay.py']},limits=['Geometric inequalities and quantified classification are reviewed analytically in independent_review.md.','Classical degree-one Potapov structure imported.','Exact checks do not certify bibliographic priority or constitute a proof-assistant formalization.'])
    (ROOT/'independent_review_checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ['active_boundary_exact_fixtures','inactive_exact_fixtures','source_hashes','limits']},indent=2))
if __name__=='__main__':main()
