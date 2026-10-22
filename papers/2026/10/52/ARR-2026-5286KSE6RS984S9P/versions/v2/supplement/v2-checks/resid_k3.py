import numpy as np, mpmath as mp, math, sys
from build_k3 import build, K
def roots_data(d):
    R=d['R']; ell=d['ell']; c=d['c']
    roots=[]  # (beta complex, multiplicity)
    roots.append((-1.0+0j, 4*ell+c))
    rp=np.exp(1j*np.pi/3)
    roots.append((rp,ell)); roots.append((rp.conjugate(),ell))
    for x,m in zip(d['xi'],d['mult'][:d['nreal']]):
        v=R*x; roots.append((complex(1-1/v),m))
    for p,m in zip(d['pairs'],d['mult'][d['nreal']:]):
        v=R*p; be=complex(1-1/v); roots.append((be,m)); roots.append((be.conjugate(),m))
    return roots
def exact_checks(d):
    R=d['R']; ell=d['ell']; c=d['c']
    rts=[(mp.mpf(-1),4*ell+c),(mp.exp(1j*mp.pi/3),ell),(mp.exp(-1j*mp.pi/3),ell)]
    for x,m in zip(d['xi'],d['mult'][:d['nreal']]): rts.append((1-1/(R*x),m))
    for p,m in zip(d['pairs'],d['mult'][d['nreal']:]):
        be=1-1/(R*p); rts+= [(be,m),(mp.conj(be),m)]
    S=lambda j: sum(m*(1/(1-b))**j for b,m in rts)
    Pp0=-sum(m/b for b,m in rts)
    return Pp0, S(1), [S(j) for j in range(2,K+1)]
def rho(d,Ngrid):
    roots=roots_data(d)
    n=d['n']
    lam=float(-sum(m/b for b,m in roots).real)
    # use mp-precision lam
    Pp0,S1,_=exact_checks(d)
    lam=float(Pp0.real)
    th=2*np.pi*np.arange(Ngrid)/Ngrid
    # chunk
    num=0.0; den=0.0; maxkap=0
    ch=1<<20
    for a in range(0,Ngrid,ch):
        t=th[a:a+ch]; z=np.exp(1j*t); s=np.sin(t/2)**2
        logG=np.zeros_like(t); Fv=-lam*np.ones_like(z)
        for b,m in roots:
            logG+=m*(np.log(np.abs(z-b))-np.log(abs(1-b)))
            Fv+=m/(z-b)
        G2=np.exp(2*logG)
        den+=G2.sum(); num+=(G2*np.abs(Fv)**2).sum()
        with np.errstate(divide='ignore',invalid='ignore'):
            k=np.where(s>0,-2*logG/(n*s),np.inf); maxkap=max(maxkap,0) 
            mk=np.min(k[s>0]) if (s>0).any() else np.inf
        maxkap=mk if a==0 else min(maxkap,mk)
    return math.sqrt(num/den), maxkap
if __name__=="__main__":
    for n in [10**4,10**5,10**6,10**7]:
        d=build(n)
        Pp0,S1,Sj=exact_checks(d)
        for N in (n+1+((-(n+1))%6==0)*0, ):
            pass
        N1=n+1
        while math.gcd(N1,6)!=1: N1+=1
        N2=N1+1
        while math.gcd(N2,6)!=1: N2+=1
        r1,kap=rho(d,N1); r2,_=rho(d,N2)
        print(n,'M',d['M'],'slope diff',mp.nstr(Pp0-S1,3),'S2..',[mp.nstr(abs(x),3) for x in Sj],'rho',r1,r2,'rho*n^(1/6)',r1*n**(1/6),'rho*n^{1/6*(K-2)}',r1*n**((K-2)/6),'min kappa',kap)
        sys.stdout.flush()
