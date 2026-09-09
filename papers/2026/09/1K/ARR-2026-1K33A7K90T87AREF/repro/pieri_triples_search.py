"""Two checks about the Pieri triples (Pi)_i of Lemma 4.3, using Fulton's recursive generator horn_t (d <= 9, ~20 s):
 (1) all Horn triples (I,J,K) in T^d_r (all r) whose s-form (2.2) equals s_{i-1} + s_{i+2} - s_{d-1} are listed; the
     Pieri triple is the only one whose right side is A_i = sum_{k=i}^{d-2} lambda_k, and its LR coefficient is 1;
 (2) the Horn LP (2.1) restricted to the Lidskii-Wielandt-type triples (I = K, J = (1..r)) and (J = K, I = (1..r)),
     which include all Weyl inequalities, is compared with the full Horn LP at G-chamber points for d = 6, 7 (float HiGHS):
     the restricted LP value is strictly smaller than Phi there, so a triple outside the Lidskii-Wielandt family is needed.
Run: python pieri_triples_search.py [dmax]   (default 9)."""
import sys, random
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import linprog
from check_horn_lp import horn_t
from lr import part, lr
from conj_formula import kappa_conj

def sform(I, J, d):
    v = [0] * (d + 1)
    for i in I:
        if i < d: v[i] += 1
    for j in J:
        if j > 1: v[d + 1 - j] -= 1
    return tuple(v[1:d])

def lw_type(I, J, K, r):
    full = tuple(range(1, r + 1))
    return (I == K and J == full) or (J == K and I == full)

def horn_lp(d, lam, triples):
    rows, rhs = [], []
    for I, J, K in triples:
        rows.append([-x for x in sform(I, J, d)]); rhs.append(-float(sum(lam[k - 1] for k in K)))
    for i in range(d - 2):
        row = [0] * (d - 1); row[i] = -1; row[i + 1] = 1; rows.append(row); rhs.append(0.0)
    res = linprog(np.ones(d - 1), A_ub=np.array(rows, float), b_ub=np.array(rhs), bounds=[(0, None)] * (d - 1), method="highs")
    assert res.success, res.message
    return res.fun

dmax = int(sys.argv[1]) if len(sys.argv) > 1 else 9
for d in range(6, dmax + 1):
    allT = [(r, t) for r in range(1, d) for t in horn_t(r, d)]
    for i in range(2, d - 2, 2):
        I0 = (i - 1,) + tuple(range(i + 1, d - 1)); J0 = tuple(range(1, d - i - 1)) + (d - i,); K0 = tuple(range(i, d - 1))
        target = sform(I0, J0, d)
        hits = [(r, I, J, K) for r, (I, J, K) in allT if sform(I, J, d) == target]
        assert (len(K0), I0, J0, K0) in hits and sum(1 for h in hits if h[3] == K0) == 1
        assert lr(part(I0), part(J0), part(K0)) == 1
        nlw = sum(1 for r, I, J, K in hits if lw_type(I, J, K, r))
        print(f"d={d} i={i}: {len(hits)} Horn triples share the s-form s_{i-1}+s_{i+2}-s_{d-1} ({nlw} of Lidskii-Wielandt type); "
              f"exactly one has right side A_{i} (the Pieri triple, LR coefficient 1); it is {'not ' if not lw_type(I0,J0,K0,len(K0)) else ''}of Lidskii-Wielandt type", flush=True)
    if d <= 7:
        full = [t for _, t in allT]; lw = [t for r, t in allT if lw_type(*t, r)]
        rng = random.Random(3)
        for m in range(3, d - 1):
            z = d - m - 2; worst = 0.0
            for _ in range(25):   # points in the G-chambers: b2 close to P/2, one dominant odd gap
                a = sorted([Q(rng.randint(1, 30), 6) for _ in range(m)], reverse=True)
                jstar = rng.choice(range(1, m + 1, 2))
                for t in range(jstar): a[t] = max(a[t], a[0])            # a_1 = ... = a_j* : gap g_j* dominant
                P = sum(a); b2 = P / 2 - Q(rng.randint(0, 5), 1000) * P; b1 = P - b2
                lam = a + [Q(0)] * z + [-b2, -b1]
                phi = float(kappa_conj(a, (b1, b2))); v_full = horn_lp(d, lam, full); v_lw = horn_lp(d, lam, lw)
                assert abs(v_full - phi) < 1e-8, (a, b2, v_full, phi)
                worst = max(worst, (phi - v_lw) / phi)
            print(f"d={d} m={m} z={z}: full Horn LP == Phi at 25 G-chamber points; Lidskii-Wielandt-only LP falls short by up to {100*worst:.1f}% of Phi", flush=True)
