import numpy as np, mpmath as mp, math, sys
from build_k3 import build, K
from resid_k3 import roots_data, exact_checks
for n in [10**5,10**6,10**7]:
    d=build(n); roots=roots_data(d); R=float(d['R'])
    Pp0,S1,_=exact_checks(d); lam=float(Pp0.real)
    vs=[(1/(1-b),m) for b,m in roots]
    Sk=lambda k: sum(m*abs(v)**k for v,m in vs)
    Lam=Sk(K+1); sig2=Sk(2)
    N=n+1
    while math.gcd(N,6)!=1: N+=1
    th=2*np.pi*(np.arange(N)+0.5)/N  # shifted grid, avoid root hits
    # use symmetric half? fine
    s=np.sin(th/2)**2; z=np.exp(1j*th)
    logG=np.zeros_like(th); F=-lam*np.ones_like(z)
    for b,m in roots:
        logG+=m*(np.log(np.abs(z-b))-np.log(abs(1-b))); F+=m/(z-b)
    G2=np.exp(2*logG)
    w=np.abs(z-1)
    delta=1/ (2*max(abs(v) for v,_ in vs)/R)  # |v|<=R/(2 delta)
    inner=w<=delta/R
    # local bound: |F| <= 2 Lam |w|^K
    ratio=np.max(np.abs(F[inner])/(2*Lam*w[inner]**K))
    # g'' bound: compute numerically at theta=0 via second derivative of log|G|^2 
    h=1e-3/ math.sqrt(n)
    def g(t):
        zz=np.exp(1j*t); return 2*sum(m*(np.log(abs(zz-b))-np.log(abs(1-b))) for b,m in roots)
    g2=(g(h)-2*g(0.0+1e-30)+g(-h))/h**2 if False else None
    # curvature via analytic: g''(0) = -2 Re sum v^2 ... compute
    gpp0=2*sum(m*(-(v**2)*(1j)**2 + v*(-1)).real for v,m in vs)  # d2/dth2 Re? just report n-scale
    # outer arc: |P'/P(1)|^2 = |G|^2 |F+lam|^2
    outer=~inner
    Pp2=G2*np.abs(F+lam)**2
    kap=0.4
    with np.errstate(all='ignore'):
        lp=2*logG[outer]+2*np.log(np.abs(F[outer]+lam)+1e-300)+kap*n*s[outer]
    outer_ratio=np.exp(np.max(lp))/n**2
    E=np.min(-logG[s>0]*2/(n*s[s>0]))
    den=np.sum(G2[np.abs(th-np.pi*2*(th>np.pi))<=n**-0.5])*(2*np.pi/N)/(2*np.pi)
    print(n,'Lam/R^(K+1)',Lam/R**(K+1),'sig2/n',sig2/n,'local ratio |F|/(2 Lam |w|^K) max',ratio,'outer max |P\'|^2/P(1)^2 e^{.4 n s}/n^2',outer_ratio,'kappa_min',E,'den*sqrt(n)',den*math.sqrt(n))
