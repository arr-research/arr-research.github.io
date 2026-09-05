"""Replay for active_delay.md: symbolic identities and exact fixtures first.

Dependencies: SymPy and mpmath. No SDP solver or frequency grid is used here.
Numerical construction replays are explicitly supplementary, not exact proof.
Usage: python verify_active_delay.py
       python verify_active_delay.py --u 3 --v 1/3 --T 2 --construct
"""
from pathlib import Path
from fractions import Fraction
from math import isqrt
import argparse
import hashlib
import json
import sympy as sp
import mpmath as mp

HERE=Path(__file__).resolve().parent


def require(ok,message):
    if not ok:
        raise AssertionError(message)


def zero(expr,message):
    require(sp.factor(sp.cancel(expr))==0,message)


def symbolic_certificates():
    z,u,v,B,F=sp.symbols('z u v B F',real=True)
    t=(F*(v-u)/2-B)/(1+F)
    e=1/(2+F); k=1-e
    C=(1+F)*t*t+F*u*v
    detP=e*C-B*B-2*B*k*t-k*t*t
    zero(detP-F*(u-B)*(B+v)/(F+2),'residual determinant factorization')

    m,d,x,tau=sp.symbols('m d x tau',real=True)
    u=d-m; v=d+m; e=x/(1+x); k=1/(1+x)
    t=m+d*x; r=m+d/x; L2=d*d*(1-x)**2/x
    H=lambda z:(z-v)**2+L2
    Q=lambda z:k*(z-t)**2
    P=lambda z:e*(z-r)**2
    zero(Q(z)+P(z)-H(z),'active denominator decomposition')
    zero(Q(-u)-e*H(-u),'negative node equality')
    zero(Q(v)-e*H(v),'positive node equality')
    h=k*r+e*t
    zero(h-v-L2/d,'positive dual denominator identity')
    nu=e*(tau-t)/(h-tau); mu=1+nu
    lm=(v-t+nu*(r-t))/(u+v); lp=1-lm
    l0=lm*(u+t)**2+lp*(v-t)**2+nu*(r-t)**2
    aa,bb,cc=sp.symbols('aa bb cc')
    R=lambda z:aa*z*z+bb*z+cc
    zero(l0*aa-lm*R(-u)-lp*R(v)-nu*R(r)+mu*R(t),
         'universal active dual quadratic identity')
    zero(e*(-u*lm+v*lp)+nu*r-(e+nu)*tau,'dual first moment')
    beta=e*(lm*u*u+lp*v*v)+nu*r*r-(e+nu)*tau*tau
    HH=lambda z:z*z+bb*z+cc
    zero(e*(lm*HH(-u)+lp*HH(v))+nu*HH(r)-(e+nu)*HH(tau)-beta,
         'denominator support functional identity')
    zero(l0*k-(e+nu)*H(tau)-beta,'equality constant at optimizer')
    # Gives an algebraic check of the positivity step for lambda_+.
    zero(lp-(r+t-2*tau)/(2*(h-tau)),
         'lambda plus positivity factor')

    u,v,p,w=sp.symbols('u v p w',real=True)
    qs=w*w+v*v; L=p+w; tau=-p*v/w
    C=1+2*qs+2*p*w
    ideal=sp.groebner([p*p-w*w-v*v-1],p,w,v,u)
    def red(expr):
        num=sp.together(expr).as_numer_denom()[0]
        return sp.factor(ideal.reduce(sp.expand(num))[1])
    require(red(C-v*v-L*L)==0,'active upper ellipse value')
    require(red(v*v+(C-(1+2*qs))**2/(4*p*p)-qs)==0,'active cap equality')
    Htau=(tau-v)**2+L*L
    require(red(Htau-qs*L*L/(w*w))==0,'active ellipse support')
    N=2*(tau-v)*(u+tau)*(v-tau)-Htau*(v-u-2*tau)
    expected=L*L/(w*w)*((qs-2*v*v)*u-v*(qs+2*p*w))
    require(red(N-expected)==0,'exact transition sign identity')

    u,v,Y=sp.symbols('u v Y',real=True)
    K=u*u-u*v-v*v+1
    poly=(u-3*v)*(u+v)*Y*Y-4*v*v*K*Y+4*v**4*(u*u+1)
    zero(poly-(((u-v)*Y-2*u*v*v)**2-4*v*v*(1+Y)*(Y-v*v)),
         'transition polynomial with unsquared sign')
    zero(poly.subs(Y,2*v*v)+4*v**4*(1+v*v),'threshold root separation')
    dd=(u+v)/2; mm=(v-u)/2
    cinactive=-2*dd*dd*(dd*dd+mm*mm)
    cactive=2*v*v*dd*dd-3*dd**4
    zero(cactive-cinactive-dd*dd*(u-3*v)**2/4,'fourth order positivity penalty')

    # Explicit outer factor coefficients and polynomial lossless identity.
    B,Delta=sp.symbols('B Delta',real=True)
    h0=-B+sp.I*(1+Delta); h1=B+sp.I*(1-Delta)
    zero(h0*sp.conjugate(h0)-h1*sp.conjugate(h1)-4*Delta,'explicit outer factor')
    return {'residual_determinant':'PASS','active_decomposition':'PASS',
            'dual_quadratic_identity':'PASS','dual_positive_weight_factor':'PASS',
            'support_identity':'PASS','phase_boundary':'PASS',
            'threshold_polynomial':'PASS','asymptotic_penalty':'PASS','outer_factor':'PASS'}


def exact_rational_fixture(u,v,T,t,r,e,expected_active):
    u,v,T,t,r,e=map(sp.Rational,(u,v,T,t,r,e))
    k=1-e; p=(T+1/T)/2; q=(T-1/T)/2
    w=sp.sqrt(q*q-v*v); L=p+w
    require(w.is_Rational and L.is_Rational,'fixture radicals are rational')
    tau=-p*v/w; B=-v; C=v*v+L*L
    H=lambda s:s*s+2*B*s+C
    Q=lambda s:k*(s-t)**2
    P=lambda s:e*(s-r)**2
    s=sp.symbols('s')
    zero(Q(s)+P(s)-H(s),'fixture global nonnegative decomposition')
    zero(Q(-u)-e*H(-u),'fixture negative endpoint')
    zero(Q(v)-e*H(v),'fixture positive endpoint')
    zero(B*B+(C-(1+2*q*q))**2/(4*p*p)-q*q,'fixture exact cap')
    h=k*r+e*t; nu=e*(tau-t)/(h-tau); mu=1+nu
    lm=(v-t+nu*(r-t))/(u+v); lp=1-lm
    l0=lm*(u+t)**2+lp*(v-t)**2+nu*(r-t)**2
    require(lm>0 and lp>0 and l0>0 and mu>0,'exact positive dual weights')
    require((nu>0) if expected_active else (nu==0),'active or boundary multiplier')
    aa,bb,cc=sp.symbols('aa bb cc'); R=lambda s:aa*s*s+bb*s+cc
    zero(l0*aa-lm*R(-u)-lp*R(v)-nu*R(r)+mu*R(t),'fixture exact dual')
    Uc=v*(q*q+2*p*w)/(q*q-2*v*v)
    require((u>Uc) if expected_active else (u==Uc),'fixture phase comparison')
    peak_poly=(1-C)**2+4*B*B-(q/p)**2*(1+C)**2
    zero(peak_poly,'analytic peak equality, no grid')
    require(C-B*B>0,'strictly positive denominator')
    return {key:str(value) for key,value in {'u':u,'v':v,'T':T,'e':e,'B':B,'C':C,
            't':t,'r':r,'tau':tau,'nu':nu,'mu':mu,'lambda_minus':lm,
            'lambda_plus':lp,'lambda_0':l0,'U_c':Uc}.items()}


def sqrt_interval(value,digits=45):
    value=Fraction(value); scale=10**digits
    lo=isqrt(value.numerator*scale*scale//value.denominator)
    aa,bb=Fraction(lo,scale),Fraction(lo+1,scale)
    require(aa*aa<=value<=bb*bb,'rational square root enclosure')
    return aa,bb


def obstructed_fixture():
    # All bounds here are rational, with outward monotone operations.
    sqrt65=sqrt_interval(65)
    Ll,Lh=(15+sqrt65[0])/12,(15+sqrt65[1])/12
    length=Fraction(10,3)
    Rl=sqrt_interval(Ll*Ll+length*length)[0]
    Rh=sqrt_interval(Lh*Lh+length*length)[1]
    el,eh=(1-Lh/Rl)/2,(1-Ll/Rh)/2
    require(el>Fraction(2502579353269861041166,10**22), 'active error lower interval')
    require(eh<Fraction(2502579353269861041167,10**22), 'active error upper interval')
    sqrt10=sqrt_interval(10)
    Qcl,Qch=(8+sqrt10[0])/27,(8+sqrt10[1])/27
    require(Qch<Fraction(9,16),'T=2 strictly beyond threshold')
    tc=(sqrt_interval(1+Qcl)[0]+sqrt_interval(Qcl)[0],
        sqrt_interval(1+Qch)[1]+sqrt_interval(Qch)[1])
    # Exact isolation for the rejected old lower bound, now with separation.
    t=sp.symbols('t'); u=sp.Integer(3); v=sp.Rational(1,3)
    p=sp.Rational(5,4); q=sp.Rational(3,4)
    D=(u+t)*(v-t); Dp=sp.diff(D,t)
    left=2*t*D-(t*t+p*p)*Dp
    poly=sp.Poly(left*left-q*q*(t*t+p*p)*Dp*Dp,t).clear_denoms()[1].primitive()[1]
    lo,hi=sp.Rational(-760,1000),sp.Rational(-759,1000)
    require(poly.count_roots(lo,hi)==1,'old quartic branch count')
    matches=[(a,b) for ((a,b),mult) in poly.intervals(eps=sp.Rational(1,10**40)) if lo<a<b<hi]
    require(len(matches)==1,'old lower root refinement')
    aa,bb=map(Fraction,matches[0])
    # The original unsquared equation requires left and Dp to have the same sign.
    require(sp.diff(left,t).subs(t,sp.Rational(aa))>0 and
            sp.diff(left,t).subs(t,sp.Rational(bb))>0,
            'old quadratic left side increases throughout root interval')
    require(left.subs(t,sp.Rational(bb))<0 and Dp.subs(t,sp.Rational(aa))<0,
            'old lower bound root sign retained')
    rl=sqrt_interval(bb*bb+Fraction(25,16))[0]
    rh=sqrt_interval(aa*aa+Fraction(25,16))[1]
    Al,Ah=(rl+Fraction(3,4))**2,(rh+Fraction(3,4))**2
    Dl=(3+bb)*(Fraction(1,3)-bb); Dh=(3+aa)*(Fraction(1,3)-aa)
    Fl,Fh=Al/Dh,Ah/Dl
    oldel,oldeh=1/(2+Fh),1/(2+Fl)
    require(el>oldeh,'strict exact separation from unachievable lower certificate')
    return {'active_error_interval':[str(el),str(eh)],
            'active_error_decimal':[float(el),float(eh)],
            'threshold_q_squared':'(8+sqrt(10))/27',
            'threshold_T_interval':[str(z) for z in tc],
            'old_lower_polynomial':str(poly.as_expr()),
            'old_lower_root_interval':[str(aa),str(bb)],
            'old_lower_error_interval':[str(oldel),str(oldeh)],
            'strict_gap_lower_bound':str(el-oldeh)}


def number(value):
    if isinstance(value,str) and '/' in value:
        a,b=value.split('/'); return mp.mpf(a)/mp.mpf(b)
    return mp.mpf(value)


def construct(u0,v0,T0,dps=90):
    mp.mp.dps=dps
    u,v,T=map(number,(u0,v0,T0))
    require(u>0 and v>0 and T>=0,'model parameters')
    if T<1:
        a=1/mp.sqrt(2)
        return {'phase':'constant','e':mp.mpf('.5'),'completion_degree':0,
                'S_constant':[[a,-a],[a,a]],'peak':0,
                'instruction':'Use S_constant directly; the degree-one sharp completion does not apply.'}
    reflected=u<v
    if reflected: u,v=v,u
    p=(T+1/T)/2; q=(T-1/T)/2
    margin=None; active=False; boundary=False
    if q*q>2*v*v:
        w=mp.sqrt(q*q-v*v)
        margin=(q*q-2*v*v)*u-v*(q*q+2*p*w)
        scale=1+abs((q*q-2*v*v)*u)+abs(v*(q*q+2*p*w))
        boundary=abs(margin)<mp.power(10,-dps+12)*scale
        active=margin>0 and not boundary
    if active or boundary:
        L=p+w
        # Stable form: x=e/(1-e), avoiding subtraction at large T.
        RR=mp.sqrt(L*L+(u+v)**2)
        x=(u+v)**2/(RR+L)**2
        e=x/(1+x); k=1-e
        t=v-L*mp.sqrt(x); r=v+L/mp.sqrt(x)
        B=-v; C=v*v+L*L
        eta=mp.mpf(0); j=-e*r; ell=e*r*r
        tau=-p*v/w; h=k*r+e*t
        nu=e*(tau-t)/(h-tau)
        lm=(v-t+nu*(r-t))/(u+v); lp=1-lm
        l0=lm*(u+t)**2+lp*(v-t)**2+nu*(r-t)**2
        dual={'tau':tau,'nu':nu,'lambda_minus':lm,'lambda_plus':lp,'lambda_0':l0}
        phase='boundary' if boundary else 'active'
    else:
        if u==v: t=mp.mpf(0)
        else:
            low,high=(v-u)/2,mp.mpf(0)
            for _ in range(int(dps*3.5)+30):
                t=(low+high)/2
                rr=mp.sqrt(t*t+p*p)
                N=2*t*(u+t)*(v-t)-rr*(rr+q)*(v-u-2*t)
                if N<0: low=t
                else: high=t
            t=(low+high)/2
        rr=mp.sqrt(t*t+p*p)
        FF=(rr+q)**2/((u+t)*(v-t))
        e=1/(2+FF); k=1-e
        B=q*t/rr; C=1+2*q*q+2*p*p*q/rr
        j=B+k*t; ell=C-k*t*t
        detP=(1-2*e)*(u-B)*(B+v)
        require(detP>0,'inactive global residual positivity')
        eta=mp.sqrt(detP)/e
        dual={'old_lower_F':FF}; phase='inactive'
    if reflected:
        B=-B; t=-t; j=-j
        # eta's sign is immaterial. Reflecting this intensity preserves all claims.
    Delta=mp.sqrt(C-B*B)
    shift=j/e+1j*eta
    qz=[mp.sqrt(k)*(t+1j),mp.sqrt(k)*(-t+1j)]
    pz=[mp.sqrt(e)*(1j-shift),mp.sqrt(e)*(1j+shift)]
    hz=[-B+1j*(1+Delta),B+1j*(1-Delta)]
    peak=(abs(hz[0])+abs(hz[1]))/(abs(hz[0])-abs(hz[1]))
    return {'phase':phase,'e':e,'B':B,'C':C,'t':t,'j':j,'ell':ell,
            'eta':eta,'p_z':pz,'q_z':qz,'h_z':hz,'peak':peak,
            'completion_degree':1,'reflected':reflected,'canonical_dual':dual}


def jsonable(value):
    if isinstance(value,dict): return {k:jsonable(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [jsonable(z) for z in value]
    if isinstance(value,(mp.mpf,mp.mpc)): return mp.nstr(value,45)
    return value


def numerical_supplements():
    constants=[]
    for cap in ['0','0.5','0.999999']:
        result=construct('3','1/3',cap)
        matrix=mp.matrix(result['S_constant'])
        require(result['completion_degree']==0 and result['peak']==0,'constant cap below one')
        require(mp.norm(matrix.T*matrix-mp.eye(2))<mp.mpf('1e-80'),'constant router unitarity')
        require(abs(1-abs(matrix[1,0])**2-mp.mpf('.5'))<mp.mpf('1e-80'),
                'constant exceptional error')
        require(abs(1-abs(matrix[0,0])**2-mp.mpf('.5'))<mp.mpf('1e-80'),
                'constant repeated error')
        constants.append(cap)
    cases=[('2','1','1'),('3','1/3','1.1'),('3','1/3','2'),
           ('3','1/3','10'),('1399/180','9/20','2'),('165/28','9/20','2'),
           ('1/3','3','2'),('3','1','100'),('3.0001','1','1000'),
           ('0.5','0.1','2'),('10','0.1','10'),('10','10','2'),
           ('0.0001','0.000001','2'),('3000','1','2')]
    reports=[]
    for u,v,T in cases:
        result=construct(u,v,T)
        ee=result['e']; B=result['B']; C=result['C']; t=result['t']; k=1-ee
        H=lambda s:s*s+2*B*s+C
        errors=[ee,k*(-number(u)-t)**2/H(-number(u)),k*(number(v)-t)**2/H(number(v))]
        require(max(abs(z-ee) for z in errors)<mp.mpf('1e-65'),'constructed three node errors')
        require(abs(result['peak']/number(T)-1)<mp.mpf('1e-65'),'global analytic peak')
        require(result['eta']>=0,'global scalar residual positivity')
        def starpoly(a): return [mp.conj(a[1]),mp.conj(a[0])]
        def conv(a,b): return [a[0]*b[0],a[0]*b[1]+a[1]*b[0],a[1]*b[1]]
        pp=conv(result['p_z'],starpoly(result['p_z']))
        qq=conv(result['q_z'],starpoly(result['q_z']))
        hh=conv(result['h_z'],starpoly(result['h_z']))
        coefferr=max(abs(pp[i]+qq[i]-hh[i]) for i in range(3))
        require(coefferr<mp.mpf('1e-60'),'lossless polynomial identity')
        dual=result['canonical_dual']
        if result['phase']=='active':
            require(dual['nu']>0 and dual['lambda_minus']>0 and dual['lambda_plus']>0,
                    'numerical dual positivity')
        reports.append({'u':u,'v':v,'T':T,'phase':result['phase'],
                        'e':ee,'B':B,'C':C,'analytic_peak':result['peak'],
                        'polynomial_identity_residual':coefferr})
    # Deterministic parameter sweep checks classifier equivalence independently
    # of the active constructor, using the old quartic's unsquared stationary root.
    classified=0
    for u,v,T in [('1','1','2'),('2','1','100'),('3','1','1000'),('4','1','10'),
                  ('20','.01','1.01'),('20','.01','2'),('.5','.1','1.5'),
                  ('100','.1','1.2'),('100','.1','3')]:
        U,V,TT=map(number,(u,v,T)); p=(TT+1/TT)/2; q=(TT-1/TT)/2
        low,high=(V-U)/2,mp.mpf(0)
        for _ in range(320):
            z=(low+high)/2; rr=mp.sqrt(z*z+p*p)
            NN=2*z*(U+z)*(V-z)-rr*(rr+q)*(V-U-2*z)
            if NN<0: low=z
            else: high=z
        z=(low+high)/2; BB=q*z/mp.sqrt(z*z+p*p)
        result=construct(u,v,T)
        require((result['phase']=='active')==(BB<-V),'phase test versus old global positivity')
        classified+=1
    return {'constructor_cases':reports,'constant_cap_cases':constants,
            'phase_comparison_cases':classified}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--construct',action='store_true')
    parser.add_argument('--u',default='3'); parser.add_argument('--v',default='1/3')
    parser.add_argument('--T',default='2'); args=parser.parse_args()
    if args.construct:
        print(json.dumps(jsonable(construct(args.u,args.v,args.T)),indent=2)); return
    report={'status':'PASS','symbolic':symbolic_certificates(),
            'rational_active_fixture':exact_rational_fixture('1399/180','9/20','2','-103/100','221/80','16/41',True),
            'rational_transition_fixture':exact_rational_fixture('165/28','9/20','2','-15/16','35/12','9/25',False),
            'formerly_obstructed_example':obstructed_fixture(),
            'numerical_supplements':numerical_supplements(),
            'limitations':['The manuscript supplies the quantified proof and weight inequalities.',
                           'Symbolic and rational/radical checks are exact; mp cases are numerical supplements.',
                           'No conic solver or frequency-grid certificate is used in this replay.',
                           'Self-checking by the deriving agent is not independent review.']}
    report['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report['manuscript_sha256']=hashlib.sha256((HERE/'active_delay.md').read_bytes()).hexdigest()
    (HERE/'active_delay_certificate.json').write_text(json.dumps(jsonable(report),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','symbolic':len(report['symbolic']),
                      'rational_fixtures':2,'radical_obstruction_fixture':1,
                      'constructor_cases':len(report['numerical_supplements']['constructor_cases'])}))


if __name__=='__main__': main()
