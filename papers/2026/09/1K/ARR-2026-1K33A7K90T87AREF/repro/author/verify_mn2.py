"""Exact verification of the inertia-(m,2) theorem for kappa_d, m <= MMAX (default 8), zero padding z in {0,1,2}.

Spectrum lambda = (a_1>=...>=a_m>0, 0^z, -b_2, -b_1), b_1>=b_2>0, sum a = b_1+b_2.  d = m+z+2.
kappa_d = min sum_{t<d} s_t over common spectra s of (CC*/2, C*C/2) with s_d = 0, Horn-feasible.

PART 1 (lower bound): for every form F_k, G_j an explicit list of Horn triples (weight 1 in s-units) is generated;
  we check (i) the Horn sum condition, (ii) c^{lam(K)}_{lam(I) lam(J)} >= 1 (LR tableau count; = Horn validity by
  Klyachko/Knutson-Tao; convention validated against Fulton's recursion for d<=7 in lr.py), (iii) membership in
  Fulton's T^d_r for d <= 8 directly, (iv) the summed left side has every s_t-coefficient <= 1 (so it is <= sum_t s_t),
  (v) the summed right side equals the form, as an exact linear function of (a, b).
PART 2 (upper bound): the 2x2-block weighted-shift layering of each form; exact interval recursion for feasibility;
  closed-form feasibility regions; coverage of the stratum; explicit float construction of C with residual check.
PART 3: chamber structure and reductions to d = 4, 5.
"""
from fractions import Fraction as Q
import itertools, random, math, sys
import numpy as np
from lr import lr, part, strip
from conj_formula import forms_mn2
from layer_chain import layerings, feasible, cost, forms as form_values, rand_stratum

MMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 8
ZS = (0, 1, 2)
random.seed(7)

# ---------- symbolic linear forms in variables a_1..a_m, b_1, b_2 (dict var->Q) ----------
def lam_vec(m, z):
    """lambda_k as linear forms, k = 1..d."""
    d = m + z + 2; L = []
    for k in range(1, d + 1):
        if k <= m: L.append({"a%d" % k: Q(1)})
        elif k <= m + z: L.append({})
        elif k == d - 1: L.append({"b2": Q(-1)})
        else: L.append({"b1": Q(-1)})
    return L

def add(f, g, c=1):
    h = dict(f)
    for k, v in g.items(): h[k] = h.get(k, 0) + c * v
    return {k: v for k, v in h.items() if v != 0}

def canon(f, m):
    """eliminate b2 = sum a - b1."""
    f = dict(f)
    if "b2" in f:
        c = f.pop("b2")
        for j in range(1, m + 1): f["a%d" % j] = f.get("a%d" % j, 0) + c
        f["b1"] = f.get("b1", 0) - c
    return {k: v for k, v in f.items() if v != 0}

def sform(I, J, d):
    lhs = {}
    for i in I:
        if i < d: lhs[i] = lhs.get(i, 0) + 1
    for j in J:
        if j > 1: lhs[d + 1 - j] = lhs.get(d + 1 - j, 0) - 1
    return {k: v for k, v in lhs.items() if v != 0}

# ---------- certificate triples ----------
def lidskii(K, d):            # J = (1..r): sum_K lam <= sum_K s - sum_{t=d-r+1}^{d-1} s_t
    r = len(K); return (tuple(K), tuple(range(1, r + 1)), tuple(K))
def weyl_neg(j, d):           # s_j >= b_j  (j = 1,2): I=(1..d-1), J=K=[d] minus {d+1-j}
    I = tuple(range(1, d)); J = tuple(x for x in range(1, d + 1) if x != d + 1 - j); return (I, J, J)
def pieri(i, d):              # even i: s_{i-1} + s_{i+2} - s_{d-1} >= sum_{k=i}^{d-2} lam_k
    I = (i - 1,) + tuple(range(i + 1, d - 1)); J = tuple(range(1, d - i - 1)) + (d - i,); K = tuple(range(i, d - 1))
    return (I, J, K)

def certificate(name, m, z):
    d = m + z + 2; T = []
    def pair_or_single(t):   # A_t via Lidskii K=(t..d-2) if t <= m-1, else s_m >= a_m
        if t <= m - 1: T.append(lidskii(range(t, d - 1), d))
        else: T.append(lidskii((m,), d))
    if name[0] == "F":
        k = int(name[1:])
        if k == 0:
            for t in range(1, m + 1, 2): pair_or_single(t)
        else:
            T.append(lidskii(range(1, d), d))                       # s_1 >= b_1
            for j in range(2, k + 1): T.append(lidskii(range(j, d), d))   # s_j >= A_j - b_2
            for t in range(k + 1, m + 1, 2): pair_or_single(t)
    else:
        j = int(name[1:])
        T.append(weyl_neg(2, d))                                     # s_2 >= b_2
        for i in range(2, j, 2): T.append(pieri(i, d))               # s_{i-1}+s_{i+2}-s_{d-1} >= A_i
        if j + 2 <= min(m, d - 2): T.append(lidskii((j,) + tuple(range(j + 2, d - 1)), d))   # s_j+s_{j+2}-s_{d-1} >= a_j + A_{j+2}
        else: T.append(lidskii((j,), d))                             # s_j >= a_j
        for t in range(j + 3, m + 1, 2): pair_or_single(t)
    return T

def check_certificates():
    from check_horn_lp import horn_t
    total = 0
    for m in range(2, MMAX + 1):
        for z in ZS:
            d = m + z + 2; L = lam_vec(m, z)
            for name, al, b1c, b2c in forms_mn2(m):
                tgt = {"a%d" % (j + 1): Q(al[j]) for j in range(m)}; tgt["b1"] = Q(b1c); tgt["b2"] = Q(b2c)
                target = canon(tgt, m)
                lhs_tot = {}; rhs_tot = {}
                for (I, J, K) in certificate(name, m, z):
                    r = len(I); assert len(J) == r == len(K)
                    assert sum(I) + sum(J) == sum(K) + r * (r + 1) // 2, (name, m, z, I, J, K)
                    assert lr(part(I), part(J), part(K)) >= 1, ("LR", name, m, z, I, J, K)
                    if d <= 8: assert (I, J, K) in set(horn_t(r, d)), ("Fulton", name, m, z, I, J, K)
                    lhs_tot = add(lhs_tot, sform(I, J, d))
                    for k in K: rhs_tot = add(rhs_tot, L[k - 1])
                    total += 1
                assert all(v <= 1 for v in lhs_tot.values()), (name, m, z, lhs_tot)
                assert canon(rhs_tot, m) == target, (name, m, z, canon(rhs_tot, m), target)
        print("PART1 m=%d: all forms certified for z in %s (triples so far %d)" % (m, ZS, total), flush=True)

# ---------- closed-form regions ----------
def E(a, i):  # a_i + a_{i+2} + ...
    return sum(a[i - 1::2]) if i <= len(a) else Q(0)
def gaps(a):
    m = len(a); aa = list(a) + [Q(0)]
    return {j: aa[j - 1] - aa[j] for j in range(1, m + 1, 2)}
def region(name, a, b):
    m = len(a); b2 = b[1]; g = gaps(a); gstar = max(g.values())
    if name == "F0": return E(a, 2) <= b2 <= E(a, 1) - gstar
    if name[0] == "F":
        k = int(name[1:]); return E(a, k + 2) <= b2 <= E(a, k + 1)
    j = int(name[1:]); return b2 >= E(a, 1) - g[j]

def sample_point(m, it):
    if it % 4 == 0: a, b = rand_stratum(m, random, den=random.choice([12, 30, 60, 97]))
    elif it % 4 == 1: a, _ = rand_stratum(m, random); b = (sum(a) / 2, sum(a) / 2)              # b1 = b2
    elif it % 4 == 2:
        a = [Q(1, m)] * m; s = sum(a); b2 = Q(random.randint(1, 50), 100) * s; b = (s - b2, b2)  # flat a
    else:
        a = sorted([Q(random.randint(1, 5), 5) for _ in range(m)], reverse=True); s = sum(a)   # ties in a
        b2 = Q(random.randint(1, 50), 100) * s; b = (s - b2, b2)
    a = [Q(x) for x in a]; b = (Q(b[0]), Q(b[1])); assert b[0] >= b[1] > 0 and sum(a) == b[0] + b[1]
    return a, b

def check_upper(m, N):
    for it in range(N):
        a, b = sample_point(m, it)
        lay = layerings(a, b); fv = form_values(a, b); mx = max(fv.values())
        feas = {n: feasible(lay[n]) for n in lay}
        for n in lay:
            assert cost(lay[n]) == fv[n]
            assert feas[n] == region(n, a, b), ("region mismatch", n, a, b, feas[n], region(n, a, b))
            if feas[n]: assert fv[n] == mx, ("feasible but not max", n, a, b)
        assert any(feas[n] for n in lay), ("no feasible layering", a, b)
        # chamber structure
        g = gaps(a); gstar = max(g.values()); jstar = [j for j in g if g[j] == gstar]
        if b[1] <= E(a, 2):
            kk = max(k for k in range(1, m) if E(a, k + 1) >= b[1]); assert fv["F%d" % kk] == mx, (a, b, kk)
        elif b[1] <= E(a, 1) - gstar: assert fv["F0"] == mx
        else: assert all(fv["G%d" % j] == mx for j in jstar)
    print("PART2 m=%d: %d exact points: feasible(layering X) <=> region(X); argmax layering feasible; chambers OK" % (m, N), flush=True)

# ---------- explicit matrix construction ----------
def construct_C(layers):
    """Float construction of C from a feasible layering (backward choice of sigma_2's, 2x2 rotations)."""
    lay = [[float(x) for x in L] for L in layers]; T = len(lay) - 1
    Tr = [None] * (T + 2); lo = [None] * (T + 2); hi = [None] * (T + 2)
    Tr[1] = -sum(lay[0]); lo[1] = hi[1] = (0.0 if len(lay[0]) == 1 else min(-x for x in lay[0]))
    for t in range(1, T):
        L = lay[t]
        if len(L) == 1: Tr[t + 1] = Tr[t] - L[0]; lo[t + 1] = hi[t + 1] = 0.0; continue
        d1, d2 = max(L), min(L)
        lo[t + 1] = max(0.0, lo[t] - d1); hi[t + 1] = min(hi[t] - d2, Tr[t] - d1 - lo[t], (Tr[t] - d1 - d2) / 2)
        Tr[t + 1] = Tr[t] - d1 - d2
    sig = [None] * (T + 2)
    LT = lay[T]; sig[T] = 0.0 if len(LT) == 1 else min(LT)
    for t in range(T - 1, 0, -1):
        L = lay[t]
        if len(L) == 1: sig[t] = 0.0; continue
        d1, d2 = max(L), min(L); tau = sig[t + 1]
        a_, b_ = max(lo[t], tau + d2), min(hi[t], Tr[t] - d1 - tau, tau + d1)
        assert a_ <= b_ + 1e-12, (t, a_, b_)
        sig[t] = (a_ + b_) / 2
    sizes = [len(L) for L in lay]; offs = np.cumsum([0] + sizes); n = offs[-1]
    C = np.zeros((n, n)); S = np.diag([-x for x in lay[0]])
    for t in range(1, T + 1):
        Lt = lay[t]; D = np.diag(Lt)
        s1, s2 = Tr[t] - sig[t], sig[t]
        if t == T: R = D.copy()
        elif len(Lt) == 1: R = np.array([[Tr[t]]])
        else:
            d1, d2 = max(Lt), min(Lt); tau1, tau2 = Tr[t + 1] - sig[t + 1], sig[t + 1]
            p = int(np.argmax(Lt)); q = 1 - p
            if abs(s1 - s2) < 1e-15 or abs(d1 - d2) < 1e-15: x = 0.5
            else: x = (tau1 * tau2 - (s2 - d1) * (s1 - d2)) / ((s1 - s2) * (d1 - d2))
            x = min(1.0, max(0.0, x)); c, s_ = math.sqrt(x), math.sqrt(1 - x)
            U = np.zeros((2, 2)); U[p, 0] = c; U[q, 0] = s_; U[p, 1] = -s_; U[q, 1] = c
            R = U @ np.diag([s1, s2]) @ U.T
        wR, VR = np.linalg.eigh(R); wS, VS = np.linalg.eigh(S)
        k = min(R.shape[0], S.shape[0])
        iR = np.argsort(-wR)[:k]; iS = np.argsort(-wS)[:k]
        assert np.allclose(np.sort(wR[iR]), np.sort(wS[iS]), atol=1e-9), (t, wR, wS)
        M = VR[:, iR] @ np.diag(np.sqrt(2 * np.maximum(wR[iR], 0))) @ VS[:, iS].T
        C[offs[t]:offs[t + 1], offs[t - 1]:offs[t]] = M
        S = R - D
    lam = np.concatenate([np.array(L) for L in lay])
    resid = np.linalg.norm(C @ C.T - C.T @ C - 2 * np.diag(lam))
    return C, resid, 0.5 * np.linalg.norm(C) ** 2

def check_construction(m, N):
    worst = 0.0
    for it in range(N):
        a, b = sample_point(m, it); lay = layerings(a, b); fv = form_values(a, b); mx = max(fv.values())
        for n in lay:
            if feasible(lay[n]):
                C, resid, c = construct_C(lay[n])
                worst = max(worst, resid, abs(c - float(mx)))
                assert np.linalg.matrix_rank(C, tol=1e-9) == m, (n, a, b, np.linalg.matrix_rank(C, tol=1e-9))
    print("PART2b m=%d: explicit C built at %d points: max residual ||CC*-C*C-2F||, |cost-Phi| = %.1e; rank C = m" % (m, N, worst), flush=True)

# ---------- reductions to d=4, d=5 ----------
def check_small_d():
    def f4(l):
        l1, l2, l3, l4 = l; return max(l1 - l3, l2 - l4, l1 - 2 * l2 - l3, l2 + 2 * l3 - l4)
    def f5(l):
        l1, l2, l3, l4, l5 = l
        return max(2*l1-2*l2-l3+l5, -l1+l3+2*l4-2*l5, l1-l3-l4, l2+l3-l5, l2-2*l3-l4, l2+2*l3-l4,
                   2*l1-l3+l5, -l1+l3-2*l5, l1+l2-l3, l3-l4-l5, l1+l3-l4, l2-l3-l5)
    for m, f in ((2, f4), (3, f5)):
        for it in range(3000):
            a, b = sample_point(m, it); lam = list(a) + [-b[1], -b[0]]
            assert f(lam) == max(form_values(a, b).values()), (m, a, b)
    print("PART3: Phi equals the published d=4 (3M Thm 3.1) and d=5 (37B Thm 3.1) formulas on 3000 exact stratum points each")
    for m in range(2, MMAX + 1):
        for it in range(200):
            a = sorted([Q(random.randint(1, 40), 40) for _ in range(m)], reverse=True)
            fv = form_values(a, (sum(a), Q(0))); assert max(fv.values()) == sum((j + 1) * a[j] for j in range(m)) == fv["F%d" % (m - 1)]
    print("PART3: one-spike limit b2 = 0 gives Phi = F_{m-1} = sum_j j a_j for m <= %d" % MMAX)

if __name__ == "__main__":
    check_certificates()
    for m in range(2, MMAX + 1): check_upper(m, 400)
    for m in range(2, MMAX + 1): check_construction(m, 60)
    check_small_d()
    print("ALL CHECKS PASSED")
