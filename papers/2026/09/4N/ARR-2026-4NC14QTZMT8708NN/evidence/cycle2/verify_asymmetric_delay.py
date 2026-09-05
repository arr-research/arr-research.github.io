"""Exact algebra and rational root certificates; no external writes or compilation.

The universal proof is asymmetric_delay.md. The finite replay does not replace it.
Dependencies: SymPy (and its mpmath dependency), Python standard library.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import isqrt
import hashlib
import json
import sympy as s
import mpmath as mp

HERE = Path(__file__).resolve().parent


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def symbolic_certificates():
    t,u,v,B,C,k=s.symbols("t u v B C k", real=True)
    y=s.symbols("y",real=True)
    aa,bb,cc=s.symbols("aa bb cc",real=True)
    R=lambda z:aa*z*z+bb*z+cc
    D=(u+t)*(v-t)
    lag=R(-u)/((u+v)*(u+t))+R(v)/((u+v)*(v-t))-R(t)/D
    require(s.factor(lag-aa)==0,"quadratic Lagrange certificate")
    H=lambda z:z*z+2*B*z+C
    A=H(t)
    crit=2*(t+B)*D-A*s.diff(D,t)
    require(s.factor(H(-u)*D-(D+A)*(u+t)**2+(u+t)*crit)==0,
            "negative endpoint stationarity identity")
    require(s.factor(H(v)*D-(D+A)*(v-t)**2-(v-t)*crit)==0,
            "positive endpoint stationarity identity")
    M=s.Matrix([[1,B],[B,C]])
    w=s.Matrix([1,-t])
    require(s.expand((M-k*w*w.T).det()-(M.det()-k*A))==0,
            "global residual power determinant")

    p,q,r=s.symbols("p q r",positive=True)
    ideal=s.groebner([p*p-q*q-1,r*r-t*t-p*p],p,r,q,t,B,C)
    def reduce(expr):
        num=s.together(expr).as_numer_denom()[0]
        return s.factor(ideal.reduce(s.expand(num))[1])
    Bt=q*t/r
    Ct=1+2*q*q+2*p*p*q/r
    At=(r+q)**2
    require(reduce(t*t+2*Bt*t+Ct-At)==0,"ellipse support value")
    require(reduce(Bt*Bt+(Ct-(1+2*q*q))**2/(4*p*p)-q*q)==0,
            "ellipse support lies on cap boundary")
    require(reduce((Ct-Bt*Bt)*r*r-At*p*p)==0,
            "sharpness determinant quotient")
    ellipse=B*B+(C-(1+2*q*q))**2/(4*p*p)-q*q
    # trace^2 - 4 det = eigenvalue gap squared
    ratio=(1-C)**2+4*B*B-(q/p)**2*(1+C)**2
    require(reduce(ratio-4*ellipse)==0,"peak cap ellipse equivalence")

    T=s.symbols("T",positive=True)
    pp=(T+1/T)/2
    require(s.simplify(pp**2-(1+T*T/2)/4-(T*T+2+2/T**2)/8)==0,
            "all-T positive-power sufficient bound")
    special=s.Rational(3)-s.sqrt(10)
    F1=(1+special**2)/((2+special)*(1-special))
    E1=1/(2+F1)
    expected=(s.sqrt(10)+1)/(2*s.sqrt(10)+4)
    require(s.simplify(E1-expected)==0,"T=1 exact asymmetric value")
    require(s.simplify(-special**2+6*special+1)==0,"T=1 critical root")

    # Independent rational antipodal example of Theorem B.
    ell=s.Rational(3,5)
    kap=s.Rational(0)
    error=(1+kap)/(2+ell+kap)
    require(error==s.Rational(5,13),"antipodal example")
    require(error>s.Rational(1,3),"geometric-mean extrapolation disproved")
    return {"lagrange_identity":"PASS","stationary_node_equalities":"PASS",
            "ellipse_cap_and_support":"PASS","residual_power_determinant":"PASS",
            "all_T_sufficient_bound":"PASS","T1_error_squared":str(expected),
            "counterexample_error_squared":"5/13", "incorrect_extrapolation":"1/3"}


def sqrt_interval(x, digits=24):
    x=Q(x)
    scale=10**digits
    lo=isqrt(x.numerator*scale*scale//x.denominator)
    a,b=Q(lo,scale),Q(lo+1,scale)
    require(a*a<=x<=b*b,"square-root rational enclosure")
    return a,b


def eval_bounds(u,v,T,lo,hi):
    """Rational outward bounds for a negative root to the right of D's vertex."""
    u,v,T,lo,hi=map(Q,(u,v,T,lo,hi))
    require((v-u)/2<lo<hi<0,"interval outside chosen monotone branch")
    p=(T+1/T)/2
    q=(T-1/T)/2
    rl,_=sqrt_interval(hi*hi+p*p)
    _,rh=sqrt_interval(lo*lo+p*p)
    Al,Ah=(rl+q)**2,(rh+q)**2
    Dl,Dh=(u+hi)*(v-hi),(u+lo)*(v-lo)
    Fl,Fh=Al/Dh,Ah/Dl
    el,eh=1/(2+Fh),1/(2+Fl)
    sharp_lo=hi*hi*(1+Fl)-p*p
    sharp_hi=lo*lo*(1+Fh)-p*p
    return {"F_interval":[Fl,Fh],"error_squared_interval":[el,eh],
            "sharpness_slack_interval":[sharp_lo,sharp_hi],
            "decimal_error_squared_interval":[float(el),float(eh)]}


def root_certificate(u,v,T,coarse,expect_sharp):
    t=s.symbols("t")
    u,v,T=map(s.Rational,(u,v,T))
    p,q=(T+1/T)/2,(T-1/T)/2
    D=(u+t)*(v-t)
    Dp=s.diff(D,t)
    L=2*t*D-(t*t+p*p)*Dp
    polynomial=s.Poly(L*L-q*q*(t*t+p*p)*Dp*Dp,t).clear_denoms()[1].primitive()[1]
    if polynomial.LC()<0:
        polynomial=-polynomial
    low,high=map(s.Rational,coarse)
    require(polynomial.count_roots(low,high)==1,"algebraic branch root count")
    # L and D' are both negative throughout each selected interval.
    require(s.diff(L,t).subs(t,low)>0 and s.diff(L,t).subs(t,high)>0,
            "L monotonicity on isolating interval")
    require(L.subs(t,high)<0 and Dp.subs(t,low)<0,"unsquared sign condition")
    intervals=polynomial.intervals(eps=s.Rational(1,10**16))
    matches=[(a,b) for ((a,b),multiplicity) in intervals if low<a<b<high]
    require(len(matches)==1,"refined branch selection")
    aa,bb=matches[0]
    bounds=eval_bounds(Q(u),Q(v),Q(T),Q(aa),Q(bb))
    if expect_sharp:
        require(bounds["sharpness_slack_interval"][1]<0,"expected global power positivity")
    else:
        require(bounds["sharpness_slack_interval"][0]>0,"expected nonattainment of lower bound")
    return {"u":str(u),"v":str(v),"T":str(T),
            "primitive_polynomial":str(polynomial.as_expr()),
            "isolating_interval":[str(aa),str(bb)],"root_count":1,
            "unsquared_sign":"L<0 and D'<0",
            "lower_bound_attained":expect_sharp,**bounds}


def numerical_constructor_replays():
    """High-precision supplements. They are not certificates of a circle supremum."""
    mp.mp.dps=70
    reports=[]
    for T0 in [1,mp.mpf(3)/2,2,3,10,100,1000]:
        T=mp.mpf(T0)
        p,q=(T+1/T)/2,(T-1/T)/2
        def N(t):
            r=mp.sqrt(t*t+p*p)
            return 2*t*(2+t)*(1-t)-r*(r+q)*(-1-2*t)
        lo,hi=mp.mpf(-.5),mp.mpf(0)
        for _ in range(220):
            mid=(lo+hi)/2
            if N(mid)<0:
                lo=mid
            else:
                hi=mid
        t=(lo+hi)/2
        r=mp.sqrt(t*t+p*p)
        B=q*t/r
        C=1+2*q*q+2*p*p*q/r
        F=(r+q)**2/((2+t)*(1-t))
        e=1/(2+F)
        kappa=1-e
        j=B+kappa*t
        k=C-kappa*t*t
        eta2=k/e-(j/e)**2
        require(eta2>0,"constructor has negative residual intensity")
        H=lambda z:z*z+2*B*z+C
        errors=[e,kappa*(-2-t)**2/H(-2),kappa*(1-t)**2/H(1)]
        spread=max(errors)-min(errors)
        require(spread<mp.mpf('1e-55'),"three active errors differ")
        gap=mp.sqrt((1-C)**2+4*B*B)
        peak=mp.sqrt((1+C+gap)/(1+C-gap))
        require(abs(peak/T-1)<mp.mpf('1e-55'),"global analytic peak mismatch")
        # Explicit z coefficients and exact spectral factor at numerical precision.
        qz=[mp.sqrt(kappa)*(t+1j),mp.sqrt(kappa)*(-t+1j)]
        shift=j/e+1j*mp.sqrt(eta2)
        pz=[mp.sqrt(e)*(1j-shift),mp.sqrt(e)*(1j+shift)]
        hmean=sum(abs(z)**2 for z in pz+qz)
        hcross=mp.conj(pz[0])*pz[1]+mp.conj(qz[0])*qz[1]
        h0=mp.sqrt((hmean+mp.sqrt(hmean*hmean-4*abs(hcross)**2))/2)
        h1=hcross/h0
        alpha=-mp.conj(h1/h0)
        determinant_peak=(1+abs(alpha))/(1-abs(alpha))
        require(abs(determinant_peak/T-1)<mp.mpf('1e-55'),"spectral factor peak mismatch")
        require(abs(h1)<h0,"spectral factor not outer")
        reports.append({"T":str(T),"t":mp.nstr(t,24),"error_squared":mp.nstr(e,24),
            "T_times_error":mp.nstr(T*mp.sqrt(e),24),
            "active_error_spread":mp.nstr(spread,5),
            "determinant_zero":str(alpha),"global_peak_from_Poisson":mp.nstr(determinant_peak,24)})
    return reports


def main():
    report={"status":"PASS","symbolic":symbolic_certificates(),
       "exact_T2_fixed_pattern":root_certificate(2,1,2,("-271/1000","-270/1000"),True),
       "exact_failed_sharpness_example":root_certificate(3,s.Rational(1,3),2,("-760/1000","-759/1000"),False),
       "numerical_constructor_supplements":numerical_constructor_replays(),
       "limitations":["Written proof supplies universal quantifiers and uniqueness.",
          "Root isolation and symbolic identities are exact; construction samples use 70-digit arithmetic.",
          "Peak delay is evaluated by an analytic global formula, not a frequency grid.",
          "No Lean formalization, external review, or literature-priority certificate."]}
    report["script_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report["proof_sha256"]=hashlib.sha256((HERE/"asymmetric_delay.md").read_bytes()).hexdigest()
    (HERE/"asymmetric_delay_certificate.json").write_text(json.dumps(report,indent=2,default=str)+"\n",encoding="utf-8")
    print(json.dumps({"status":"PASS","symbolic":"PASS","exact_root_certificates":2,
                      "constructor_supplements":len(report["numerical_constructor_supplements"])}))


if __name__=="__main__":
    main()
