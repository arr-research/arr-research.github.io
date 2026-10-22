# Theorem 2 construction for K=3 with exact cone weights (Lemma 10):
# real nodes 1,2,3 (weights 2 each), pair nodes (1+i)/2 (weight 47), (1+3i)/2 (weight 7); Q=2.
import numpy as np, mpmath as mp, sympy as sp
mp.mp.dps=60
K=3; Q=2
reals=[1,2,3]; mre=[2,2,2]
pairs=[(mp.mpf(1)/2,mp.mpf(1)/2),(mp.mpf(1)/2,mp.mpf(3)/2)]; mpair=[47,7]
# exact check of A alpha0 = (0,3/2) with alpha0 = m/Q
z=lambda x,y: sp.Rational(x)+sp.I*sp.Rational(y)
def exact_moment(j):
    s=sum(sp.Rational(m,Q)*sp.Integer(r)**j for r,m in zip(reals,mre))
    s+=sum(sp.Rational(m,Q)*2*sp.re(sp.expand((sp.Rational(1,2)+sp.I*sp.Rational(b,2))**j)) for b,m in zip([1,3],mpair))
    return s
print("A alpha0 =",exact_moment(2),exact_moment(3),"(expected 0, 3/2)")
M=sum(mre)+2*sum(mpair)
S=sum(m*r for r,m in zip(reals,mre))+sum(m*2*x for (x,y),m in zip(pairs,mpair))
b3=mp.mpf(-3)/2
def solve(n):
    n=int(n)
    R=(mp.mpf(n)/(6*Q))**(mp.mpf(1)/3); eps=1/R
    # c_n = n-M mod 6, nearest to 2 S R
    target=2*S*R
    # nearest in class
    cands=[cc for cc in range(int(target)-6,int(target)+7) if (n-M-cc)%6==0]
    c=min(cands,key=lambda cc:abs(cc-target)); b=(n-M-c)//6
    t=c/R; u=b/R**3
    def eqs(x1,x2,x3):
        xi=[x1,x2,x3]
        d=lambda x: -x**2/(x-eps)
        e1=t/2+sum(m*d(x) for m,x in zip(mre,xi))+sum(m*2*mp.re(-(complex_(x,y))**2/(complex_(x,y)-eps)) for (x,y),m in zip(pairs,mpair))
        def Mj(j): return sum(m*x**j for m,x in zip(mre,xi))+sum(m*2*mp.re(complex_(x,y)**j) for (x,y),m in zip(pairs,mpair))
        e2=t*eps/4+Mj(2)
        e3=b3*u+t/8*eps**2+Mj(3)
        return [e1,e2,e3]
    sol=mp.findroot(eqs,(0.73,2.25,2.9))
    return n,R,c,b,[sol[i] for i in range(3)]
def complex_(x,y): return mp.mpc(x,y)
def build_roots_v(n):
    n,R,c,b,xi=solve(n)
    v_real=[R*x for x in xi]; v_pair=[R*mp.mpc(x,y) for (x,y) in pairs]
    return n,R,c,b,v_real,v_pair
def check_identities(n):
    n,R,c,b,vr,vp=build_roots_v(n)
    # base roots of B=(1+z)^4(1-z+z^2): reciprocals
    rB=[mp.mpf(1)/2]*4+[1/(1-mp.expjpi(mp.mpf(1)/3)),1/(1-mp.expjpi(-mp.mpf(1)/3))]
    def mom(j):
        s=b*sum(r**j for r in rB)+c*mp.mpf(1)/2**j
        s+=sum(m*v**j for m,v in zip(mre,vr))+sum(m*(v**j+mp.conj(v)**j) for m,v in zip(mpair,vp))
        return s
    lam0=b*3+c-sum(m*(1/(1-1/v)) for m,v in zip(mre,vr))-sum(m*2*mp.re(1/(1-1/v)) for m,v in zip(mpair,vp))
    return n,mp.re(mom(1)-lam0),mp.re(mom(2)),mp.re(mom(3)),[mp.nstr(v,8) for v in vr],R
def rho2(n):
    n,R,c,b,vr,vp=build_roots_v(n)
    # complex double data
    vr=[float(v) for v in vr]; vp=[complex(v) for v in vp]
    W=min(np.pi,25/float(n)**0.5); N=600001
    th=np.linspace(-W,W,N); zz=np.exp(1j*th); w=2j*np.sin(th/2)*np.exp(1j*th/2)
    sB=np.sin(th/2)**2
    # normalised log modulus of each group (squared modulus ratio), then half
    logsq=0*th
    # B: (1-s)^4 (1-4s)^2  -> squared modulus ratio
    logsq+= b*(4*np.log1p(-sB)+2*np.log1p(-4*sB))
    logsq+= c*np.log1p(-sB)
    for m,v in zip(mre,vr): logsq+= m*np.log(np.abs(1+v*w)**2)
    for m,v in zip(mpair,vp): logsq+= m*np.log(np.abs(1+v*w)**2*np.abs(1+np.conj(v)*w)**2)
    Pm2=np.exp(logsq)
    # F = -w^3 sum v_j^4/(1+v_j w)   (valid since sum v_j^2 = sum v_j^3 = 0, lambda = P'(1)/P(1))
    rB=[0.5]*4+[1/(1-np.exp(1j*np.pi/3)),1/(1-np.exp(-1j*np.pi/3))]
    Ssum=b*sum(r**4/(1+r*w) for r in rB)+c*0.5**4/(1+0.5*w)
    Ssum=Ssum+sum(m*v**4/(1+v*w) for m,v in zip(mre,vr))+sum(m*(v**4/(1+v*w)+np.conj(v)**4/(1+np.conj(v)*w)) for m,v in zip(mpair,vp))
    F=-w**3*Ssum
    num=np.trapezoid(np.abs(F)**2*Pm2,th); den=np.trapezoid(Pm2,th)
    return num/den,R
if __name__=="__main__":
    print("M =",M,"S =",S)
    print("n, sum v_j - P'(0), sum v^2, sum v^3 (exact identities), real nodes xi*R")
    for n in [10**9+7,10**12+9]:
        print(check_identities(n))
    print("n, R, rho^2, rho^2 n^(1/3) (K=3 predicts bounded)")
    for n in [10**9+7,10**10+9,10**11+3,10**12+9,10**15+11,10**18+3,10**21+9]:
        r,R=rho2(n); print(n,"%.1f"%R,"%.4e"%r,"%.3f"%(r*n**(1/3)))
