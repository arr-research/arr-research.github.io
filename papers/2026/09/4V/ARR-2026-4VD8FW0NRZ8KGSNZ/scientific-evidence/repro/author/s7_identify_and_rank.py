# s7: (i) rank of the active-gradient matrix (5 x 7) at the refined optimum -> must be 4 (= intrinsic dof) so that,
#     with all KKT multipliers > 0, 0 lies in the interior of the convex hull of the projected gradients: strict local max.
#     (ii) PSLQ / findpoly attempts on gamma* and on the Gram entries (low-degree algebraic identification).
import mpmath as mp, json, sys
from s6_tie_refine_mp import bloch, spectrum, jac
mp.mp.dps = 40
SRC = sys.argv[1] if len(sys.argv) > 1 else 's6_refined.json'
ACT = [int(k) for k in sys.argv[2].split(',')] if len(sys.argv) > 2 else [5, 6, 8, 12, 18]
d = json.load(open(SRC))
p = [mp.mpf(x) for x in d['p']]
def Gk(pp):
    gg = spectrum(bloch(pp), max(ACT)); return [gg[k] for k in ACT]
JG = jac(Gk, p, len(ACT))
U, S, V = mp.svd_r(JG)
print("singular values of active-gradient matrix (5x7):", [mp.nstr(s, 6) for s in S])
gam = mp.mpf(d['gamma'])
print("gamma* =", mp.nstr(gam, 36))
for deg in (2, 3, 4, 6, 8):
    r = mp.findpoly(gam, deg, maxcoeff=10 ** 6)
    print(f"  findpoly(gamma*, deg<={deg}, coeff<=1e6):", r)
print("identify(gamma*):", mp.identify(gam, tol=mp.mpf(10) ** (-30)))
G = [[mp.mpf(x) for x in row] for row in d['G']]
for i in range(5):
    for j in range(i + 1, 5):
        r = mp.findpoly(G[i][j], 4, maxcoeff=10 ** 5)
        print(f"  G[{i}][{j}] = {mp.nstr(G[i][j], 25)}  findpoly deg<=4:", r)
# invariants: sums of powers of the Gram off-diagonal entries (O(3)-invariant, relabelling-invariant)
offs = [G[i][j] for i in range(5) for j in range(i + 1, 5)]
for m in (1, 2, 3, 4):
    sm = sum(x ** m for x in offs); print(f"  sum_{{i<j}} (n_i.n_j)^{m} = {mp.nstr(sm, 30)}  findpoly deg<=6:", mp.findpoly(sm, 6, maxcoeff=10 ** 6))
