# Task (1): exact rational verification, d=2..40, degree <= 400.
# (a) c_{d,n} from the three-term definition (as in exp2_cp_fold.py);
# (b) closed form chat_{n+1} = (n+1-2d-2) W_n + d/(d-1) (n+1)(n+1+2d) C(2d-2+n, d-2),  W_n = sum_{k=d-1}^{d-1+n} C(2d-2+n,k)
#     with c_{d,n} = (d-1)/d * (d-1)!^2/(2d-1+n)! * chat_{n+1};
# (c) sign changes / n_d.
from fractions import Fraction as Fr
from math import comb, factorial
import sys, time
def coeffs_direct(d,N):
    a=[Fr(1)]
    for j in range(1,N+3): a.append(a[-1]/(d+j-1))
    c=[]
    for n in range(N+1):
        s=Fr(0)
        for i in range(n+2):
            j=n+1-i
            s+=a[i]*a[j]*(j-j*(j-1)+i*j)
        for i in range(n+1):
            s-=a[i]*a[n-i]/d
        c.append(s)
    return c
def chat(d,m):
    T1=2*d-3+m
    W=sum(comb(T1,k) for k in range(d-1,d-2+m+1))
    return Fr(m-2*d-2)*W+Fr(d,d-1)*m*(m+2*d)*comb(T1,d-2)
NMAX=400
t0=time.time()
allok=True
for d in range(2,41):
    cd=coeffs_direct(d,NMAX)
    ok=True
    for n in range(NMAX+1):
        pred=Fr(d-1,d)*Fr(factorial(d-1)**2,factorial(2*d-1+n))*chat(d,n+1)
        if pred!=cd[n]: ok=False; break
    sg=['+' if x>0 else ('-' if x<0 else '0') for x in cd]
    nz=[n for n in range(NMAX+1) if cd[n]!=0]
    changes=0; last=None
    for n in nz:
        s=sg[n]
        if last is not None and s!=last: changes+=1
        last=s
    lastneg=max((n for n in range(NMAX+1) if cd[n]<0),default=None)
    firstpos=next((n for n in range(NMAX+1) if cd[n]>0),None)
    zeros=[n for n in range(NMAX+1) if cd[n]==0]
    assert ok, (d,"closed-form mismatch")
    assert zeros==([0,1,2] if d==2 else [0,1]), (d,zeros)
    assert changes==(0 if d==2 else 1), (d,changes)
    assert lastneg==(None if d==2 else (2*d-1 if d in (3,4) else 2*d)), (d,lastneg)
    assert firstpos==(3 if d==2 else (2*d if d in (3,4) else 2*d+1)), (d,firstpos)
    allok&=ok
    print(f"d={d}: closed-form match={ok}; zero coeffs at n={zeros}; sign changes={changes}; last negative n_d={lastneg}; first positive={firstpos}; 2d={2*d}")
    sys.stdout.flush()
print("ALL closed-form matches:",allok,"time",round(time.time()-t0,1),"s")
