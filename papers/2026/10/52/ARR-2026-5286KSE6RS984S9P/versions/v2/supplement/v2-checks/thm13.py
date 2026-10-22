import numpy as np, mpmath as mp, math, sys
mp.mp.dps=60
def params(n):
    n1=n-1; m,k=divmod(n1,34)
    v=mp.findroot(lambda v:v**3-mp.mpf(3)/2*v**2-mp.mpf(n1)/4, (n1/4.0)**(1/3.)+1)
    d=(v**2/(v-1)-mp.mpf(k)/2)/m; t=(-v**2-mp.mpf(k)/4)/m
    L=(51+d)/2; U=17-t
    X=(U*L+221+mp.sqrt((U*L-289)*(U*L-169)))/(30*U); Y=(L-15*X)/2
    a=1-X; c=1-Y
    return m,k,v,a,c
def check(n):
    m,k,v,a,c=params(n)
    beta=1-1/v
    # roots: circle quadratics 1-2az+z^2: e^{±i phi}, cos phi=a, mult 15m; c: mult 2m; -1 mult k; beta mult 1
    ph=mp.acos(a); pc=mp.acos(c)
    rts=[(mp.exp(1j*ph),15*m),(mp.exp(-1j*ph),15*m),(mp.exp(1j*pc),2*m),(mp.exp(-1j*pc),2*m),(mp.mpf(-1),k),(beta,1)]
    deg=sum(mm for _,mm in rts)
    S=lambda j: sum(mm*(1/(1-b))**j for b,mm in rts)
    Pp0=-sum(mm/b for b,mm in rts)
    return rts,deg,Pp0,[S(j) for j in range(1,5)],(m,k,v,a,c)
def rho(n,rts,Pp0,N):
    roots=[(complex(b),mm) for b,mm in rts]
    lam=float(Pp0.real)
    th=2*np.pi*np.arange(N)/N+0.0
    z=np.exp(1j*th)
    logG=np.zeros(N); F=-lam*np.ones(N,dtype=complex)
    for b,mm in roots:
        logG+=mm*(np.log(np.abs(z-b))-np.log(abs(1-b))); F+=mm/(z-b)
    G2=np.exp(2*logG)
    return math.sqrt(np.sum(G2*np.abs(F)**2)/np.sum(G2)), np.min(np.where(np.sin(th/2)**2>0,-2*logG/(n*np.sin(th/2)**2+1e-300),9))
if __name__=="__main__":
    for n in [10**4+1,10**5+3,10**6+7,10**7+11]:
        rts,deg,Pp0,S,(m,k,v,a,c)=check(n)
        N=n+1
        while N%2==0 or N%3==0 or N%5==0 or N%7==0: N+=1
        r,kap=rho(n,rts,Pp0,N)
        print(n,'deg',deg,'slopediff',mp.nstr(Pp0-S[0],3),'S2,S3',mp.nstr(abs(S[1]),3),mp.nstr(abs(S[2]),3),'a,c',mp.nstr(a,6),mp.nstr(c,6),'rho n^{1/6}',r*n**(1/6),'target',math.sqrt(15)/4**(4/3),'kappa',kap)
        sys.stdout.flush()
