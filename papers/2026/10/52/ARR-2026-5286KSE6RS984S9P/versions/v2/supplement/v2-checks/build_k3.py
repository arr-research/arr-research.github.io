import numpy as np, mpmath as mp, sys, math
mp.mp.dps=60
K=int(sys.argv[1]) if len(sys.argv)>1 else 3
# instance for K=3: reals (7/2,3),(2,2),(1/2,1); pair (1+7/2 i, 2)
INST={3:dict(reals=[(mp.mpf(7)/2,3),(mp.mpf(2),2),(mp.mpf(1)/2,1)],pairs=[(mp.mpc(1,mp.mpf(7)/2),2)])}
inst=INST[K]
b=[None,3,0,mp.mpf(-3)/2,mp.mpf(-3)/4,mp.mpf(9)/8,None]  # b_1..b_5
def bj(j): return 4*mp.mpf(2)**(-j)+2*mp.cos(j*mp.pi/3)
def Mj(x,j,real): return x**j if real else 2*(x**j).real
def dfun(x,eps,real):
    v=-x**2/(x-eps); return v if real else 2*v.real
def build(n):
    reals=inst['reals']; pairs=inst['pairs']
    M=sum(m for _,m in reals)+2*sum(m for _,m in pairs)
    zeta=[r for r,_ in reals]+[p for p,_ in pairs]
    mult=[m for _,m in reals]+[m for _,m in pairs]
    nreal=len(reals)
    S=sum(m*Mj(z,1,True) for z,m in reals)+sum(m*Mj(z,1,False) for z,m in pairs)
    M3=sum(m*Mj(z,3,True) for z,m in reals)+sum(m*Mj(z,3,False) for z,m in pairs)
    Q=mp.mpf(2)/3*M3
    R=(n/(6*Q))**(mp.mpf(1)/3); eps=1/R
    target=(n-M)%6
    c=int(mp.nint(2*S*R)); 
    # nearest integer in class
    best=None
    for cc in range(c-3,c+4):
        if cc%6==target: best=cc
    c=best; ell=(n-M-c)//6
    t=c/R; u=ell/R**3
    # unknowns: designated real nodes (first K real nodes) -- here K=3 and 3 reals
    xi=[r for r,_ in reals]
    def F(xv):
        xs=list(xv)+[p for p,_ in pairs]
        res=[]
        res.append(t/2+sum(m*dfun(x,eps,True) for x,m in zip(xv,mult[:nreal]))+sum(m*dfun(p,eps,False) for p,m in pairs))
        for j in range(2,K+1):
            bb=bj(j) if j>=3 else 0
            res.append(bb*u*eps**(j-3)+t*mp.mpf(2)**(-j)*eps**(j-1)+sum(m*Mj(x,j,True) for x,m in zip(xv,mult[:nreal]))+sum(m*Mj(p,j,False) for p,m in pairs))
        return res
    sol=mp.findroot(lambda *a:F(a), xi, tol=1e-40, maxsteps=50)
    xi=[sol[i] for i in range(nreal)]
    return dict(n=n,M=M,R=R,eps=eps,c=c,ell=ell,t=t,u=u,xi=xi,pairs=[p for p,_ in pairs],mult=mult,nreal=nreal,S=S,Q=Q,zeta=zeta,F=F)
if __name__=="__main__":
    for n in [10**4,10**5,10**6,10**7]:
        d=build(n)
        print(n,'R',mp.nstr(d['R'],6),'c',d['c'],'ell',d['ell'],'xi-zeta',[mp.nstr(x-z,5) for x,z in zip(d['xi'],d['zeta'])], 'resid',mp.nstr(max(abs(v) for v in d['F'](d['xi'])),3))
