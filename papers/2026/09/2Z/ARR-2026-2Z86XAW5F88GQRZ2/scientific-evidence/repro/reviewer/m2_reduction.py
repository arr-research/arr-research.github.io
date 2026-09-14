"""Task (g): exact symbolic check of the (m,2) reduction at b_3 = 0 and the one-spike reduction at b_2 = b_3 = 0, m = 4 (and 5):
max over S(m, z>=1) restricted to b_3 = 0 equals Phi_(m,2) = max(F_k, G_j) as piecewise-linear functions on the (m,2) stratum.
Method: (i) every (m,2) form, reduced modulo sum a = b_1 + b_2 to the (alpha, beta_1) coordinates, is an element of S(m)|_{b3=0};
(ii) for each (m,2) form phi, on its chamber {phi >= other (m,2) forms} intersect stratum, max_(exact LP, cdd gmp) (h - phi) <= 0 for
every h in S(m).  (i)+(ii) give max S = Phi identically.  Same for b_2 = b_3 = 0 with the one-spike form sum_j j a_j."""
import os; AUTHOR_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "author")); REVIEWER_DIR = os.path.dirname(os.path.abspath(__file__))  # repro: these replace absolute paths in the original review scripts
import sys, json, itertools
from fractions import Fraction as Q
import cdd.gmp as g
W = AUTHOR_DIR

def m2_forms(m):
    """(m,2) forms of Theorem A as coefficient vectors (alpha_1..alpha_m, beta_1, beta_2)."""
    out = {}
    for k in range(0, m):
        c = [(j - k) if j <= k else -(-(j - k) // 2) for j in range(1, m + 1)]   # ceil((j-k)/2) for j>=k
        out[f"F_{k}"] = tuple(c) + (k, 0)
    for j in range(1, m + 1, 2):
        c = [i // 2 for i in range(1, m + 1)]; c[j - 1] += 1
        if j + 1 <= m: c[j] -= 1
        out[f"G_{j}"] = tuple(c) + (0, 1)
    return out

def reduce_b2(v, m):
    """Eliminate b_2 via b_2 = sum a - b_1: (alpha, beta1, beta2) -> (alpha + beta2, beta1 - beta2, 0)."""
    t = v[m + 1]; return tuple(x + t for x in v[:m]) + (v[m] - t, 0)

def exact_max(obj, m, chamber_rows, mode):
    """max obj.x over the polytope: x = (a_1..a_m, b_1, b_2); mode 'm2': sum a = b1 + b2 = 1... use P=1: sum a = 1, b1 + b2 = 1, ordered;
    mode 'spike': sum a = 1, b1 = 1, b2 = 0. chamber_rows: extra rows (coef vector, >= 0)."""
    n = m + 2; rows = []; lin = []
    def R(const, coef): return [Q(const)] + [Q(c) for c in coef]
    rows.append(R(-1, [1] * m + [0, 0])); lin.append(len(rows) - 1)
    if mode == 'm2':
        rows.append(R(-1, [0] * m + [1, 1])); lin.append(len(rows) - 1)
        rows.append(R(0, [0] * m + [1, -1]))       # b1 >= b2
        rows.append(R(0, [0] * m + [0, 1]))        # b2 >= 0
    else:
        rows.append(R(-1, [0] * m + [1, 0])); lin.append(len(rows) - 1)
        rows.append(R(0, [0] * m + [0, 1])); lin.append(len(rows) - 1)
    for j in range(m - 1):
        c = [0] * n; c[j] = 1; c[j + 1] = -1; rows.append(R(0, c))
    c = [0] * n; c[m - 1] = 1; rows.append(R(0, c))
    for cr in chamber_rows: rows.append(R(0, cr))
    M = g.matrix_from_array(rows, lin_set=lin, rep_type=g.RepType.INEQUALITY)
    M.obj_type = g.LPObjType.MAX; M.obj_func = [Q(0)] + [Q(c) for c in obj]
    lp = g.linprog_from_matrix(M); g.linprog_solve(lp)
    if lp.status != g.LPStatusType.OPTIMAL: return None
    return lp.obj_value

for m in (4, 5):
    S = [tuple(f) for f in json.load(open(f"{W}/closed_m{m}_z1.json"))]
    Sred = set(reduce_b2(f, m) for f in S)
    Phi = m2_forms(m); Phired = {k: reduce_b2(v, m) for k, v in Phi.items()}
    inS = {k: (v in Sred) for k, v in Phired.items()}
    print(f"m={m}: (m,2) forms present in S(m)|_(b3=0) after reduction: {inS}")
    # (ii) chamber-wise domination
    worst = Q(0); bad = []
    for k, phi in Phired.items():
        chamber = [tuple(phi[j] - Phired[k2][j] for j in range(m + 2)) for k2 in Phired if k2 != k]
        # is the chamber nonempty (full check: max 0 feasible)?
        if exact_max([0] * (m + 2), m, chamber, 'm2') is None: print(f"   chamber of {k} empty"); continue
        for h in S:
            hr = reduce_b2(h, m); obj = [hr[j] - phi[j] for j in range(m + 2)]
            v = exact_max(obj, m, chamber, 'm2')
            if v > 0: bad.append((k, h, v))
            worst = max(worst, v)
    print(f"   exact max over chambers of (h - phi), h in S(m): {worst}  -> max S|_(b3=0) <= Phi everywhere: {worst <= 0}; violations: {bad}")
    # one-spike reduction b2 = b3 = 0: kappa = sum_j j a_j (b1 = sum a)
    spike = tuple(range(1, m + 1)) + (0, 0)
    present = any(tuple(f[j] + f[m] for j in range(m)) == tuple(range(1, m + 1)) for f in S)   # alpha_j + beta1 = j
    worst2 = Q(0)
    for h in S:
        obj = [h[j] - spike[j] for j in range(m)] + [h[m], h[m + 1]]
        v = exact_max(obj, m, [], 'spike'); worst2 = max(worst2, v)
    print(f"   one-spike form sum j a_j present in S: {present}; exact max of (h - spike) on the one-spike stratum: {worst2} -> equality: {present and worst2 <= 0}")
