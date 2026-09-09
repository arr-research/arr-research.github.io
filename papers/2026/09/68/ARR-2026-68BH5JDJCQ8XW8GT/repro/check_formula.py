# Check: N_d = M M' - kappa M M'' + kappa M'^2 - M^2/d  (numerator of H = K' - kappa K'')
# vs the ODE-reduced form  Ntilde = (kappa-2d) M^2 + d(kappa-d+3) M + d(d-1),  N = ((d-1)/d) Ntilde/kappa
from fractions import Fraction as Fr
from math import comb
def series_M(d,N):
    a=[Fr(1)]
    for j in range(1,N+1): a.append(a[-1]/(d+j-1))
    return a
def mul(p,q,N):
    r=[Fr(0)]*(N+1)
    for i,x in enumerate(p):
        if x==0: continue
        for j,y in enumerate(q):
            if i+j>N: break
            r[i+j]+=x*y
    return r
def N_direct(d,N):
    a=series_M(d,N+2)
    M=a[:N+1]; M1=[(j+1)*a[j+1] for j in range(N+1)]; M2=[(j+1)*(j+2)*a[j+2] for j in range(N+1)]
    MM1=mul(M,M1,N); MM2=mul(M,M2,N); M1M1=mul(M1,M1,N); MM=mul(M,M,N)
    out=[]
    for n in range(N+1):
        v=MM1[n]-(MM2[n-1] if n>=1 else 0)+(M1M1[n-1] if n>=1 else 0)-MM[n]/d
        out.append(v)
    return out
def N_tilde(d,N):
    a=series_M(d,N+2); M=a[:N+2]; MM=mul(M,M,N+1)
    out=[]
    for n in range(N+2):
        v=(MM[n-1] if n>=1 else 0)-2*d*MM[n]+d*(a[n-1] if n>=1 else 0)+d*(3-d)*a[n]+(d*(d-1) if n==0 else 0)
        out.append(v)
    return out
def chat(d,n):
    # closed form (R3): chat_{d,n} = (n-2d-2) W_{n-1} + d/(d-1) n (n+2d) C(2d-3+n,d-2)
    T1=2*d-3+n
    W=sum(comb(T1,k) for k in range(d-1,d-2+n+1))
    return Fr(n-2*d-2)*W+Fr(d,d-1)*comb(T1,d-2)*n*(n+2*d)
allok=True
for d in range(2,13):
    N=60
    nd=N_direct(d,N); nt=N_tilde(d,N+1)
    # N = ((d-1)/d) Ntilde/kappa  => nd[n] == (d-1)/d * nt[n+1]
    ok1=all(nd[n]==Fr(d-1,d)*nt[n+1] for n in range(N+1))
    # nt[n] == (d-1)! (d-1)!/(2d-2+n)! * chat(n) ?
    from math import factorial as f
    ok2=all(nt[n]==Fr(f(d-1)**2, f(2*d-2+n))*chat(d,n) for n in range(N+1)) if d>=2 else None
    assert ok1 and ok2, (d,ok1,ok2)
    allok&=ok1 and ok2
    print(d, ok1, ok2, [str(x) for x in nd[:6]], [str(nt[n]) for n in range(6)])
print('ALL OK (N == (d-1)/d*Ntilde/kappa and closed form (R3)):',allok)
