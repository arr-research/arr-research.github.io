import mpmath as mp
from math import comb
mp.mp.dps=40
def Qseq(d,t,K):
    a,b=d-2,0; x=2*t-1
    P=[mp.mpf(1), (a+1)+mp.mpf(a+b+2)/2*(x-1)]
    for n in range(1,K):
        c1=2*(n+1)*(n+a+b+1)*(2*n+a+b); c2=(2*n+a+b+1)*(a*a-b*b)
        c3=(2*n+a+b)*(2*n+a+b+1)*(2*n+a+b+2); c4=2*(n+a)*(n+b)*(2*n+a+b+2)
        P.append(((c2+c3*x)*P[n]-c4*P[n-1])/c1)
    return [P[k]/comb(k+d-2,k) for k in range(K+1)]
# cross-check recurrence vs mp.jacobi at interior points
for d,tt in ((4,mp.mpf(1)/16),(3,mp.mpf('0.3')),(6,mp.mpf('0.7'))):
    Q=Qseq(d,tt,60)
    err=max(abs(Q[k]-mp.jacobi(k,d-2,0,2*tt-1)/comb(k+d-2,k)) for k in range(0,61))
    print("recurrence vs mp.jacobi d=%d t=%s: max err %s"%(d,mp.nstr(tt,4),mp.nstr(err,5)))
worst=0; wk=None
for d in (3,4,5,6):
    for tt in [mp.mpf(i)/50 for i in range(0,50)]+[mp.mpf('0.99'),mp.mpf('0.999')]:
        Q=Qseq(d,tt,400)
        for k in range(0,401):
            bnd=(1-tt)**(-(d-2))/comb(k+d-2,k)
            r=abs(Q[k])/bnd
            if r>worst: worst=r; wk=(d,tt,k)
print("max |Q|/bound over d=3..6, t grid, k<=400:", mp.nstr(worst,15), "at", wk)
# check ratio is <1 strictly for t>0
worst2=0
for d in (3,4,5,6):
    for tt in [mp.mpf(i)/50 for i in range(1,50)]:
        Q=Qseq(d,tt,400)
        for k in range(1,401):
            r=abs(Q[k])/((1-tt)**(-(d-2))/comb(k+d-2,k)); worst2=max(worst2,r)
print("max ratio for t>0:", mp.nstr(worst2,10))
# thresholds
Q4=Qseq(4,mp.mpf(1)/16,20); print("-Q6:",mp.nstr(-Q4[6],10),"bound k=10:",mp.nstr((mp.mpf(16)/15)**2/comb(12,10),8),"k=11:",mp.nstr((mp.mpf(16)/15)**2/comb(13,11),8))
Q3=Qseq(3,mp.mpf(1)/9,20); print("-Q4(d3):",mp.nstr(-Q3[4],10),"bound k=13:",mp.nstr((mp.mpf(9)/8)/14,6),"k=14:",mp.nstr((mp.mpf(9)/8)/15,6))
