import mpmath as mp
from math import comb
mp.mp.dps=50
def Q(k,d,t): return mp.jacobi(k,d-2,0,2*t-1)/comb(k+d-2,k)
# d=4, t=1/16
t=mp.mpf(1)/16
vals=[(k,Q(k,4,t)) for k in range(2,401)]
kmin=min(vals,key=lambda p:p[1]); print("d=4 t=1/16: min Q over 2..400 at k=",kmin[0],mp.nstr(kmin[1],15))
print("second smallest:", sorted(vals,key=lambda p:p[1])[1][0], mp.nstr(sorted(vals,key=lambda p:p[1])[1][1],12))
print("all Q > -1/32:", all(v> -mp.mpf(1)/32 for k,v in vals), " all k!=6 Q > Q6:", all(v>kmin[1] for k,v in vals if k!=6))
# Lemma T bound check numerically
worst=0
for d in (3,4,5,6):
    for tt in [mp.mpf(i)/40 for i in range(0,40)]+[mp.mpf('0.99'),mp.mpf('0.999')]:
        for k in range(0,401):
            b=(1-tt)**(-(d-2))/comb(k+d-2,k)
            r=abs(Q(k,d,tt))/b
            worst=max(worst,r)
print("max |Q|/bound over d=3..6, t grid, k<=400:", mp.nstr(worst,12), "(must be <=1; =1 at t=0)")
# the d=4 tail threshold
for k in (10,11):
    print(k, "bound", mp.nstr((mp.mpf(16)/15)**2/comb(k+2,k),8), "-Q6=",mp.nstr(-kmin[1],8))
# d=3 threshold
t3=mp.mpf(1)/9
print("d=3 -Q4(1/9)=",mp.nstr(-Q(4,3,t3),10), "bounds k=13,14:", mp.nstr((mp.mpf(9)/8)/14,6), mp.nstr((mp.mpf(9)/8)/15,6))
