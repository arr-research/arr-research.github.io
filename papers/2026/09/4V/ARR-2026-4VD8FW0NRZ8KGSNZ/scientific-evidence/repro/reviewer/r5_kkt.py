# Independent KKT check at point B: gradients of g_k (k in ties) w.r.t. the 10 free coordinates of n1..n5 restricted to the
# constraint manifold (unit norms, zero sum), via mpmath finite differences at 30 digits on the 40-digit point.
import mpmath as mp, json, numpy as np
from math import comb
mp.mp.dps=30
import os  # REPRO: package-relative path to the author's data
W=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","author")+"/"
B=json.load(open(W+"s6_refined_B.json")); nB=np.array([[mp.mpf(c) for c in v] for v in B['n']],dtype=object)
ties=[4,8,9,12,16]; K=20
def Qseq(t,K):
    a,b=1,0; x=2*t-1
    P=[mp.mpf(1),(a+1)+mp.mpf(a+b+2)/2*(x-1)]
    for m in range(1,K):
        c1=2*(m+1)*(m+a+b+1)*(2*m+a+b); c2=(2*m+a+b+1)*(a*a-b*b)
        c3=(2*m+a+b)*(2*m+a+b+1)*(2*m+a+b+2); c4=2*(m+a)*(m+b)*(2*m+a+b+2)
        P.append(((c2+c3*x)*P[m]-c4*P[m-1])/c1)
    return [P[k]/comb(k+1,k) for k in range(K+1)]
def g_all(n):
    pairs=[(i,j) for i in range(5) for j in range(i+1,5)]
    ts=[mp.mpf(2)/9*(1+sum(n[i][c]*n[j][c] for c in range(3))) for i,j in pairs]
    Qs=[Qseq(t,K) for t in ts]
    return [mp.mpf(9)/25*(5+2*sum(Q[k] for Q in Qs)) for k in ties]
# ambient gradient (15 coords) by central differences
h=mp.mpf(10)**-12
grad=[]
for i in range(5):
    for c in range(3):
        np_=nB.copy(); nm=nB.copy(); np_[i][c]=nB[i][c]+h; nm[i][c]=nB[i][c]-h
        gp=g_all(np_); gm=g_all(nm); grad.append([(a-b)/(2*h) for a,b in zip(gp,gm)])
print("Precision: final gradient projection, SVD and least squares use NumPy binary64.")
G=np.array([[float(x) for x in row] for row in grad]).T   # 5 x 15
# constraint normals: unit norms (5) and zero sum (3)
C=np.zeros((8,15))
for i in range(5): C[i,3*i:3*i+3]=[float(x) for x in nB[i]]
for c in range(3): C[5+c,c::3]=1
# tangent space basis: null space of C (dim 15-8=7)
U,s,Vt=np.linalg.svd(C); T=Vt[8:].T   # 15 x 7
Gt=G@T  # 5 x 7 projected gradients
sv=np.linalg.svd(Gt,compute_uv=False); print("singular values of projected active gradients:",sv)
# multipliers: solve lam^T Gt = 0, sum lam = 1
A=np.vstack([Gt.T, np.ones((1,5))]); bvec=np.zeros(8); bvec[-1]=1
lam,res,rk,_=np.linalg.lstsq(A,bvec,rcond=None); print("lambda:",lam,"residual:",np.linalg.norm(A@lam-bvec))
# also verify: is 0 in interior? check min over random tangent directions of max_k (-grad_k . v) >0
rng=np.random.default_rng(0); worst=1e9
for _ in range(20000):
    v=rng.normal(size=7); v/=np.linalg.norm(v); worst=min(worst,-(Gt@v).min())
print("min over random unit tangent dirs of max_k(-dg_k/dv):",worst,"(sampled diagnostic only; not an all-directions proof; this tangent space includes rotations)")
# null-space check: SO(3) generators as tangent vectors
for ax in range(3):
    v=np.zeros(15)
    for i in range(5):
        nv=[float(x) for x in nB[i]]; e=np.zeros(3); e[ax]=1; v[3*i:3*i+3]=np.cross(e,nv)
    print("rotation generator axis",ax,"|G v| =",np.linalg.norm(G@v),"|C v|=",np.linalg.norm(C@v))
