"""Exact check: at a rational interior point of the chamber of the z=0-only form g0 (rationalised strict Chebyshev centre from
certs_m{m}_z0.json), g0 > max S(m,1) exactly, for m = 4,5,7,8. Since kappa_{m+3} >= g0 (exact certificate) and
kappa_{m+4} = max S(m,1) (Theorem 1), this proves kappa_{m+3}(lam) > kappa_{m+4}(lam + 0) at that point, hence on an open set."""
import json, sys
from fractions import Fraction as Q
import os; W = os.path.join(os.path.dirname(os.path.abspath(__file__)), "author")  # repro: was an absolute path to cycle2/work/A3_inertia_m3
extra = {4: (1,2,3,4,-2,-1), 5: (1,2,3,3,4,-2,-1), 7: (1,2,2,3,3,4,5,-2,-1), 8: (1,2,2,3,3,4,4,5,-2,-1)}
def val(f, a, b, m): return sum(Q(f[j])*a[j] for j in range(m)) + Q(f[m])*b[0] + Q(f[m+1])*b[1]
for m, g0 in extra.items():
    C = json.load(open(f"{W}/certs_m{m}_z0.json")); c = C[str(list(g0))]['centre']
    den = 600
    a = [Q(round(x*den), den) for x in c['a']]; b = [Q(round(x*den), den) for x in c['b']]
    # renormalise exactly to sum 1 keeping order
    a[-1] += 1 - sum(a); b[-1] += 1 - sum(b)
    assert all(a[j] >= a[j+1] for j in range(m-1)) and a[-1] > 0 and b[0] >= b[1] >= b[2] > 0
    S1 = [tuple(f) for f in json.load(open(f"{W}/closed_m{m}_z1.json"))]
    S0 = [tuple(f) for f in json.load(open(f"{W}/closed_m{m}_z0.json"))]
    v0 = val(g0, a, b, m); v1 = max(val(h, a, b, m) for h in S1); vmax0 = max(val(h, a, b, m) for h in S0)
    print(f"m={m}: point a={[str(x) for x in a]} b={[str(x) for x in b]}: g0={v0} = {float(v0):.6f}; max S(m,1)={v1} = {float(v1):.6f}; g0 - max S(m,1) = {v0-v1} ; g0 is max of S(m,0): {vmax0==v0}")
# also the m=4 padding example exactly
a=[Q(17,61)]*3+[Q(10,61)]; b=[Q(25,61),Q(18,61),Q(18,61)]
S1=[tuple(f) for f in json.load(open(f"{W}/closed_m4_z1.json"))]
print("padding example: g0 =", val(extra[4],a,b,4), " max S(4,1) =", max(val(h,a,b,4) for h in S1))
