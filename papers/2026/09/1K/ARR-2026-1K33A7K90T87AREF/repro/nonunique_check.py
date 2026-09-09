"""Exact (Fractions) Horn-feasibility of the one-parameter optimal families used in Theorem C' (non-uniqueness).
(1) m=3, z=1: lambda=(2,2,3/2,0,-5/2,-3); s(t)=(7/2-t,5/2,3/2,t,0,0), t in [0,1/2]; endpoints checked (convexity gives all t).
(2) m=4, z=0, open F_1 chamber: lambda=(a1,a2,a3,a4,-b2,-b1) with a=(4,3,2,1), b2=5/2 (E_3=2 < b2 < E_2=4);
    s(sigma)=(b1, A_2-sigma, sigma, a4, 0, 0) for sigma in [a3, min(a2, a3+a4, min(b2, A_2-b2))] = [2, 5/2]; endpoints checked."""
from fractions import Fraction as Q
from my_horn import T
def horn_ok(s, lam):
    d = len(lam)
    for r in range(1, d):
        for (I, J, K) in T(r, d):
            lhs = sum(s[i-1] for i in I if i < d) - sum(s[d-j] for j in J if j > 1)
            if lhs < sum(lam[k-1] for k in K): return (I, J, K)
    return None
lam = [Q(2), Q(2), Q(3,2), Q(0), Q(-5,2), Q(-3)]
for t in (Q(0), Q(1,2)):
    s = [Q(7,2)-t, Q(5,2), Q(3,2), t, Q(0), Q(0)]
    print("m=3 z=1 t=%s: s=%s sum=%s violated=%s" % (t, s, sum(s), horn_ok(s, lam)))
a = [Q(4), Q(3), Q(2), Q(1)]; b2 = Q(5,2); P = sum(a); b1 = P - b2
lam = a + [-b2, -b1]
F1 = b1 + (a[1]+a[2]+a[3]) + a[3]
print("m=4 z=0: lambda=%s, F_1=%s, E_3=%s<b2=%s<E_2=%s" % (lam, F1, a[2], b2, a[1]+a[3]))
for sig in (Q(2), Q(9,4), Q(5,2)):
    s = [b1, a[1]+a[2]+a[3]-sig, sig, a[3], Q(0), Q(0)]
    print("  sigma=%s: s=%s sum=%s violated=%s" % (sig, s, sum(s), horn_ok(s, lam)))
