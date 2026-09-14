# Independent d=3, N=5 search: maximise min_{2<=k<=K} g_k over 5 unit Bloch vectors with zero sum.
# Parametrisation: n1,n2,n3 free (spherical angles), s=n1+n2+n3, n4,5 = -s/2 +- v, v perp s, |v|^2 = 1-|s|^2/4, v angle psi.
import numpy as np, sys, time
from scipy.special import eval_jacobi
from scipy.optimize import minimize
from math import comb
K=400
binom=np.array([comb(k+1,k) for k in range(K+1)],float)
def sph(th,ph): return np.array([np.sin(th)*np.cos(ph),np.sin(th)*np.sin(ph),np.cos(th)])
def frame(p):
    n1,n2,n3=sph(p[0],p[1]),sph(p[2],p[3]),sph(p[4],p[5]); s=n1+n2+n3
    ss=s@s
    if ss>4: return None
    # orthonormal basis of s^perp
    a=np.array([1.,0,0]) if abs(s[0])<0.9*np.sqrt(ss+1e-300) or ss<1e-12 else np.array([0,1.,0])
    if ss<1e-14: e1=np.array([1.,0,0]); e2=np.array([0,1.,0])
    else:
        e1=a-(a@s)/ss*s; e1/=np.linalg.norm(e1); e2=np.cross(s/np.sqrt(ss),e1)
    r=np.sqrt(max(1-ss/4,0)); v=r*(np.cos(p[6])*e1+np.sin(p[6])*e2)
    return np.array([n1,n2,n3,-s/2+v,-s/2-v])
def gk(n):
    G=n@n.T; t=(2/9)*(1+G[np.triu_indices(5,1)])
    x=2*t-1
    ks=np.arange(K+1)
    P=np.array([eval_jacobi(ks,1,0,xi) for xi in x])  # 10 x (K+1)
    Q=P/binom
    g=(9/25)*(5+2*Q.sum(0))
    return g
def obj(p):
    n=frame(p)
    if n is None: return 10.0
    g=gk(n); return -g[2:].min()
rng=np.random.default_rng(int(sys.argv[1]) if len(sys.argv)>1 else 0)
NST=int(sys.argv[2]) if len(sys.argv)>2 else 12
best=[]; t0=time.time()
for st in range(NST):
    while True:
        p=np.concatenate([rng.uniform(0,np.pi,1),rng.uniform(0,2*np.pi,1),rng.uniform(0,np.pi,1),rng.uniform(0,2*np.pi,1),rng.uniform(0,np.pi,1),rng.uniform(0,2*np.pi,1),rng.uniform(0,2*np.pi,1)])
        if frame(p) is not None: break
    f=obj(p)
    for rnd in range(4):
        r=minimize(obj,p,method='Nelder-Mead',options={'xatol':1e-11,'fatol':1e-13,'maxiter':20000,'maxfev':40000,'adaptive':True}); p=r.x
        r=minimize(obj,p,method='Powell',options={'xtol':1e-11,'ftol':1e-13,'maxiter':5000}); p=r.x
    val=-obj(p); g=gk(frame(p)); act=np.argsort(g[2:])[:6]+2
    best.append(val); print(f"start {st}: gamma={val:.12f} active={[(int(k),round(float(g[k]),10)) for k in act]}  [{time.time()-t0:.0f}s]",flush=True)
print("sorted:",sorted(best,reverse=True))
