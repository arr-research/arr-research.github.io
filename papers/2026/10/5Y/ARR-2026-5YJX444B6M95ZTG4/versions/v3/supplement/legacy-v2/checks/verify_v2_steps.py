"""Exact/numeric checks of the steps written out in v2 (Prop 12, Cor 11)."""
import sympy as sp, numpy as np
from math import log, sqrt
# --- Prop 12: J'(1/2) closed form
h=lambda x:-x*sp.log(x)-(1-x)*sp.log(1-x)
Jp=h(sp.Rational(3,10))-h(sp.Rational(1,10))-sp.Rational(3,5)*sp.log(sp.Rational(3,2))
cf=sp.log(sp.Rational(2**6*3**9,7**7))/10
print("J'(1/2)-closed form:",sp.N(Jp-cf,40), " value",sp.N(Jp,15), " 2^6 3^9 =",2**6*3**9," 7^7 =",7**7)
# --- derivative of J in general, evaluated
p,a,b=sp.symbols('p a b',positive=True)
a_,b_=sp.Rational(1,10),sp.Rational(3,10); k_=1-a_-b_
t=a_+k_*p
J=h(p)+(1-p)*h(a_)+p*h(b_)-h(t)
print("J'(1/2) via sympy diff:",sp.N(sp.diff(J,p).subs(p,sp.Rational(1,2)),15))
# --- D_p sign interval: lambda^2=1/10
L=p*(1-p)/(t*(1-t)); lam2=sp.Rational(1,10)
D=sp.simplify(L*(lam2-L*k_**2))
print("D(1/2)=",sp.nsimplify(D.subs(p,sp.Rational(1,2))))
ineq=sp.simplify(lam2*t*(1-t)-k_**2*p*(1-p))   # D<0 <=> lam2 < L k^2 <=> lam2 t(1-t) < k^2 p(1-p)
print("poly:",sp.expand(ineq*(-1)), "roots:",[sp.N(r,10) for r in sp.solve(sp.Eq(ineq,0),p)], sp.solve(sp.Eq(ineq,0),p))
# --- Bayes identity: t_p(t)=p
pp,aa,bb=sp.symbols('pp aa bb',positive=True)
kk=1-aa-bb; tt=aa+kk*pp
ap=pp*bb/(1-tt); bp_=(1-pp)*aa/tt; kp=kk*pp*(1-pp)/(tt*(1-tt))
print("a_p+k_p t - p =",sp.simplify(ap+kp*tt-pp), " 1-a_p-b_p-k_p =",sp.simplify(1-ap-bp_-kp))
# chord = J
def hh(x): return -x*log(x)-(1-x)*log(1-x)
def num_check(av,bv,pv):
    kv=1-av-bv; tv=av+kv*pv
    apv=pv*bv/(1-tv); bpv=(1-pv)*av/tv
    chord=(1-tv)*hh(apv)+tv*hh(bpv)
    Jv=hh(pv)+(1-pv)*hh(av)+pv*hh(bv)-hh(tv)
    return chord-Jv
print("chord-J (several):",[num_check(.1,.3,x) for x in (.2,.5,.8)], num_check(.02,.3,.4))
# --- numerics: f_p(t) = convex envelope of e_p at t equals J(p) when D_p<=0 (p=0.6, lam2=.1); and flat Cor 11 identity
def g(u): 
    w=np.sqrt(np.maximum(0,1-4*u)); x=(1+w)/2
    x=np.clip(x,1e-300,1-1e-16); return np.where(w>=1,0,-x*np.log(x)-(1-x)*np.log1p(-x))
def env_at(av,bv,l2,pv,N=20000):
    kv=1-av-bv; tv=av+kv*pv; L=pv*(1-pv)/(tv*(1-tv))
    apv=pv*bv/(1-tv); kpv=L*kv; l2p=L*l2
    q=np.linspace(0,1,N+1); t2=apv+kpv*q; e=g(t2*(1-t2)-l2p*q*(1-q))
    hull=[]
    for i in range(N+1):
        while len(hull)>1:
            u,v=hull[-2:]
            if (e[v]-e[u])*(i-v)>=(e[i]-e[v])*(v-u): hull.pop()
            else: break
        hull.append(i)
    hx=q[hull]; hy=e[hull]
    return float(np.interp(tv,hx,hy)), tv
for pv in (.1,.3,.5,.6,.9):
    fv,tv=env_at(.1,.3,.1,pv)
    kv=.6; L=pv*(1-pv)/(tv*(1-tv)); Dp=L*(.1-L*kv*kv)
    av,bv=.1,.3
    Jv=hh(pv)+(1-pv)*hh(av)+pv*hh(bv)-hh(tv)
    print(f"p={pv} D_p={Dp:.4f} f_p(t)={fv:.9f} J={Jv:.9f} diff={fv-Jv:.2e}")
# Cor 11: a=.1,b=.3,x=.5 : f_p(t)=g((1-x)p(1-p)), max at p=1/2 equals h((1+sqrt(x))/2)
for pv in (.2,.5,.7):
    fv,tv=env_at(.1,.3,.5,pv)
    print(f"x=.5 p={pv}: f_p(t)={fv:.9f} g((1-x)p(1-p))={float(g((1-.5)*pv*(1-pv))):.9f}")
print("cost bits x=.5:", hh((1+sqrt(.5))/2)/log(2), " c(a,b)=",.6+2*.03-2*sqrt(.03*(.6+.03)))
