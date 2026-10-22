# Numerical check of Theorem 11 (one interior zero): exact identities and rho^2 * n^{1/3}
import numpy as np, mpmath as mp
mp.mp.dps=50
def build(nn):
    n=mp.mpf(nn)
    v=mp.findroot(lambda v: v**3-1.5*v**2-(n-1)/4,(n/4)**(mp.mpf(1)/3)+1)
    m,k=divmod(nn-1,34)
    d=(v**2/(v-1)-mp.mpf(k)/2)/m; t=(-v**2-mp.mpf(k)/4)/m
    L=(51+d)/2; U=17-t
    X=(U*L+221+mp.sqrt((U*L-289)*(U*L-169)))/(30*U); Y=(L-15*X)/2
    return m,k,v,1-X,1-Y
def exact_identities(nn):
    m,k,v,a,c=build(nn)
    beta=1-1/v
    # reciprocal moments of all roots v_j=1/(1-beta_j)
    def mom(j):
        tot=m*15*2*mp.re(mp.mpf(1)/ (1-mp.expjpi(0))) if False else 0
        # roots of 1-2az+z^2: e^{+-i phi}, cos phi=a
        ph=mp.acos(a); pc=mp.acos(c)
        r=lambda p: 1/(1-mp.expj(p))
        s=15*m*(r(ph)**j+r(-ph)**j)+2*m*(r(pc)**j+r(-pc)**j)+k*mp.mpf(1)/2**j+v**j
        return mp.re(s)
    lam_P0=m*(-30*a-4*c)+k-1/beta   # P'(0)
    # P'(1)/P(1) = sum v_j
    return mom(1),lam_P0,mom(2),mom(3),(nn-1)/mp.mpf(2)+v
print("n, sum v_j - P'(0), sum v^2, sum v^3, lambda-((n-1)/2+v)")
for nn in [10**4+7,10**6+3,10**9+33]:
    s1,l0,s2,s3,l1=exact_identities(nn)
    print(nn,mp.nstr(s1-l0,3),mp.nstr(s2,3),mp.nstr(s3,3),mp.nstr(l0-l1,3))
def rho2(nn):
    m,k,v,a,c=build(nn)
    a=float(a);c=float(c);v=float(v);m=int(m);k=int(k);beta=1-1/v
    lam=m*(-30*a-4*c)+k-1/beta
    W=min(np.pi,25/np.sqrt(nn))
    N=400001
    th=np.linspace(-W,W,N)
    z=np.exp(1j*th)
    ga=1-2*a*z+z*z; gc=1-2*c*z+z*z; f=1-z/beta
    # normalized log-modulus relative to z=1
    ga1=2-2*a; gc1=2-2*c; f1=1-1/beta
    logP=m*(15*np.log(np.abs(ga/ga1))+2*np.log(np.abs(gc/gc1)))+k*np.log(np.abs((1+z)/2))+np.log(np.abs(f/f1))
    # P'/P - lam
    dl=m*(15*(-2*a+2*z)/ga+2*(-2*c+2*z)/gc)+k/(1+z)-(1/beta)/f
    F=dl-lam
    Pm=np.exp(logP)
    num=np.trapezoid(np.abs(F)**2*Pm**2,th); den=np.trapezoid(Pm**2,th)
    return num/den
print("n, rho^2, rho^2*n^(1/3), rho^2*n^(1/3)/(sanity)")
for nn in [10**4+7,10**5+3,10**6+3,10**7+3,10**9+33,10**12+1]:
    r=rho2(nn); print(nn,"%.4e"%r,"%.4f"%(r*nn**(1/3)))

# full-circle check (no window) and global/local/outer estimates, moderate n
def full(nn):
    m,k,v,a,c=build(nn)
    a=float(a);c=float(c);v=float(v);m=int(m);k=int(k);beta=1-1/v
    lam=m*(-30*a-4*c)+k-1/beta
    N=1<<22
    th=(np.arange(N)+0.5)*2*np.pi/N-np.pi
    z=np.exp(1j*th); s=np.sin(th/2)**2
    ga=1-2*a*z+z*z; gc=1-2*c*z+z*z; f=1-z/beta
    logP=m*(15*np.log(np.abs(ga/(2-2*a)))+2*np.log(np.abs(gc/(2-2*c))))+k*np.log(np.abs((1+z)/2))+np.log(np.abs(f/(1-1/beta)))
    dl=m*(15*(-2*a+2*z)/ga+2*(-2*c+2*z)/gc)+k/(1+z)-(1/beta)/f
    Pm=np.exp(logP)
    num=np.mean(np.abs(dl-lam)**2*Pm**2); den=np.mean(Pm**2)
    # global estimate: log|P/P1|^2 <= -c n s ?
    with np.errstate(divide='ignore'):
        ratio=np.max((2*logP)[s>0]/(nn*s[s>0]))
    return num/den, ratio
print("full circle rho^2 and max_theta 2log|P/P(1)|/(n s) (must be <= -c<0):")
for nn in [10**4+7,10**5+3]:
    print(nn,full(nn))

# Master estimate (Proposition A.5, K=3) evaluated with the explicit constants of the proof, versus quadrature
import math
def master_bound(nn):
    m,k,v,a,c=build(nn)
    a=float(a);c=float(c);v=float(v);m=int(m);k=int(k)
    # reciprocals of circle roots: 1/2 + i/2 cot(phi/2)
    def mod(cs):
        ph=math.acos(cs); return abs(0.5+0.5j/math.tan(ph/2))
    va,vc=mod(a),mod(c)
    S2=15*2*m*va**2+2*2*m*vc**2+k*0.25+v**2
    S4=15*2*m*va**4+2*2*m*vc**4+k*0.5**4+v**4
    V=max(va,vc,v); tau0=1/(2*V); tau1=min(tau0,S2**-0.5)
    T=-6*m-k+4*v*(v-1)
    Lam=2000*math.exp(3)*m+k+v; lam=(nn-1)/2+v
    first=2*S4**2*math.gamma(3.5)*(math.pi**2/abs(T))**3.5
    second=math.pi*(Lam+lam)**2*math.exp(-abs(T)*tau0**2/math.pi**2)
    return math.exp(4)/tau1*(first+second), first, second
print("n, master bound for rho^2, actual rho^2 (quadrature), bound*n^(1/3)")
for nn in [10**9+33,10**11+3,10**12+1]:
    b,f,s2=master_bound(nn); print(nn,"%.3e"%b,"%.3e"%rho2(nn),"%.3e"%(b*nn**(1/3)),"(outer term %.1e)"%s2)
