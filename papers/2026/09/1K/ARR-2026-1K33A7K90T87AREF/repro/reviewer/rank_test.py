"""Exact test: is s = (3,5/2,3/2,1/2,0,0) Horn-feasible for lambda=(2,2,3/2,0,-5/2,-3) (m=3,z=1, G_3 chamber)?
If yes: an optimizer with rank 4 > m = 3 exists, and the optimum is not unique for m=3."""
from fractions import Fraction as Q
from my_horn import T, horn_lhs_s
import numpy as np
from scipy.optimize import linprog

def horn_ok(s, lam, verbose=False):
    d = len(lam); assert len(s) == d
    worst = None
    for r in range(1, d):
        for (I, J, K) in T(r, d):
            lhs = sum(s[i-1] for i in I if i < d) - sum(s[d-j] for j in J if j > 1)   # s_{d+1-j} has index d-j (0-based)
            rhs = sum(lam[k-1] for k in K)
            if lhs < rhs:
                if verbose: print("VIOLATED", I, J, K, lhs, rhs)
                return False
    return True

lam = [Q(2), Q(2), Q(3,2), Q(0), Q(-5,2), Q(-3)]
Phi = Q(15,2)
for s4 in [Q(0), Q(1,4), Q(1,2)]:
    s = [Q(7,2) - s4, Q(5,2), Q(3,2), s4, Q(0), Q(0)]
    print("s =", s, "sum =", sum(s), "Horn-feasible:", horn_ok(s, lam, verbose=True))

# LP: maximise s_4 subject to Horn feasibility, ordering, and sum s <= Phi (float, HiGHS)
def lp_max_coord(lam, coord, budget):
    d = len(lam); A = []; b = []
    for r in range(1, d):
        for (I, J, K) in T(r, d):
            row = np.zeros(d)
            for i in I:
                if i < d: row[i-1] += 1
            for j in J:
                if j > 1: row[d-j] -= 1
            A.append(-row); b.append(-float(sum(lam[k-1] for k in K)))
    for j in range(d-1):
        e = np.zeros(d); e[j] = -1; e[j+1] = 1; A.append(e); b.append(0.0)
    A.append(np.ones(d)); b.append(float(budget))
    c = np.zeros(d); c[coord-1] = -1
    bounds = [(0, None)]*(d-1) + [(0, 0)]
    res = linprog(c, A_ub=np.array(A), b_ub=np.array(b), bounds=bounds, method="highs")
    return res
res = lp_max_coord(lam, 4, Phi)
print("LP max s_4 at cost<=Phi:", -res.fun, "s =", np.round(res.x, 6), res.message)
res = lp_max_coord(lam, 1, Phi); print("LP max s_1:", -res.fun, np.round(res.x, 6))
c = np.zeros(6); 
