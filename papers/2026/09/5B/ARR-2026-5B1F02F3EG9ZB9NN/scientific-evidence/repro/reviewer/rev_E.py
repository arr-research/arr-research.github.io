"""rev_E.py -- (E) kappa_6 22-form certificate: forms vs cycle-1 list, rays (pycddlib + own brute force), witnesses,
duals, coverage sampling, LP cross-check."""
import sys, os, time, itertools
from fractions import Fraction as Q
from math import gcd
import numpy as np
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # (repro copy: was the reviewer's scratchpad path)
from rev_lib import *
import cdd
AUTH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')  # (repro copy: was the author's working directory)
t0 = time.time()
C = load_json(os.path.join(AUTH, 'certs', 'kappa6_certificate.json'))
d = 6; n = 5
T = all_horn(6); assert len(T) == 522
forms = [tuple(Q(x) for x in ch['q']) for ch in C['chambers']]
extract11 = [(Q(7,6),Q(4,3),Q(3,2),Q(2,3),Q(-1,6)), (Q(3,2),Q(2),Q(1,2),Q(0),Q(-1,2)), (Q(5,6),Q(2,3),Q(3,2),Q(4,3),Q(1,6)),
             (Q(5,6),Q(5,3),Q(3,2),Q(1,3),Q(1,6)), (Q(3,2),Q(1),Q(3,2),Q(0),Q(-1,2)), (Q(1,2),Q(2),Q(1,2),Q(0),Q(1,2)),
             (Q(1),Q(2),Q(1),Q(0),Q(0)), (Q(11,6),Q(5,3),Q(1,2),Q(-2,3),Q(-5,6)), (Q(1,2),Q(2),Q(3,2),Q(0),Q(-1,2)),
             (Q(13,6),Q(4,3),Q(-1,2),Q(-4,3),Q(-7,6)), (Q(5,2),Q(0),Q(-3,2),Q(-2),Q(-3,2))]
ext22 = set(extract11) | set(tuple(reversed(q)) for q in extract11)
print("22 forms == extract 4.3 eleven + reversals:", set(forms) == ext22, len(set(forms)), len(ext22))

def lam_of(g):
    lam = [sum(g[j:]) for j in range(n)] + [Q(0)]
    m = sum(lam) / d
    return [x - m for x in lam]

def prim(v):
    den = 1
    for x in v: den = den * x.denominator // gcd(den, x.denominator)
    iv = [int(x * den) for x in v]; g = 0
    for x in iv: g = gcd(g, abs(x))
    return tuple(x // g for x in iv)

def rays_cdd(H):
    """Extreme rays of {g : h.g >= 0 for h in H} via pycddlib 3 (exact GMP rationals), H-rep rows [b, A] with b = 0."""
    import cdd.gmp as cg
    rows = [[Q(0)] + [Q(x) for x in h] for h in H]
    mat = cg.matrix_from_array(rows, rep_type=cg.RepType.INEQUALITY)
    poly = cg.polyhedron_from_matrix(mat); gen = cg.copy_generators(poly)
    out = []
    for row in gen.array:
        if row[0] == 0: out.append(prim([Q(x) for x in row[1:]]))
        else: raise RuntimeError('vertex other than origin?')
    return set(out)

def rays_brute(H):
    out = set()
    for sub in itertools.combinations(range(len(H)), n - 1):
        # null vector of the 4 rows
        M = [list(H[i]) for i in sub]
        # Gaussian elimination
        A = [row[:] for row in M]; piv = []; rr = 0
        for c in range(n):
            p = next((i for i in range(rr, len(A)) if A[i][c] != 0), None)
            if p is None: continue
            A[rr], A[p] = A[p], A[rr]; A[rr] = [x / A[rr][c] for x in A[rr]]
            for i in range(len(A)):
                if i != rr and A[i][c] != 0:
                    f = A[i][c]; A[i] = [x - f * y for x, y in zip(A[i], A[rr])]
            piv.append(c); rr += 1
        if rr != n - 1: continue
        free = [c for c in range(n) if c not in piv][0]
        v = [Q(0)] * n; v[free] = Q(1)
        for i, c in enumerate(piv): v[c] = -A[i][free]
        for cand in (v, [-x for x in v]):
            if all(sum(h[i] * cand[i] for i in range(n)) >= 0 for h in H): out.add(prim(cand))
    return out

def rank(rows):
    A = [list(map(Q, r)) for r in rows]; r = 0
    for c in range(len(A[0])):
        p = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]; A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        r += 1
    return r

def horn_row(I, J, K):
    """coefficients on s_1..s_5 (s_6 = 0) of sum_I s_i - sum_J s_{7-j}."""
    a = [Q(0)] * n
    for i in I:
        if i <= n: a[i - 1] += 1
    for j in J:
        if 7 - j <= n: a[7 - j - 1] -= 1
    return a
rows = [(horn_row(I, J, K), K) for (I, J, K) in T]
Tset = set(T)

def feasible(lam, s):
    if any(x < 0 for x in s) or any(s[k] < s[k + 1] for k in range(n - 1)): return False
    return all(sum(lam[k - 1] for k in K) <= sum(a[i] * s[i] for i in range(n)) for a, K in rows)

probs = []; total_rays = 0
for r, ch in enumerate(C['chambers']):
    q = forms[r]
    H = [tuple(Q(int(i == k)) for k in range(n)) for i in range(n)] + [tuple(q[i] - qj[i] for i in range(n)) for j, qj in enumerate(forms) if j != r]
    listed = set(tuple(x) for x in ch['rays'])
    rc = rays_cdd(H); rb = rays_brute(H)
    if not (listed == rc == rb): probs.append(f'chamber {r}: rays differ: listed {sorted(listed)} cdd {sorted(rc)} brute {sorted(rb)}')
    if rank(list(listed)) != n: probs.append(f'chamber {r}: not full-dimensional')
    for rho in listed:
        if not all(sum(h[i] * rho[i] for i in range(n)) >= 0 for h in H): probs.append(f'chamber {r}: listed ray outside chamber {rho}')
    # witnesses (in the order of ch['rays'])
    for rho, sw in zip(ch['rays'], ch['witness_s']):
        s = [Q(x) for x in sw]; lam = lam_of([Q(x) for x in rho])
        if len(s) != n or not feasible(lam, s): probs.append(f'chamber {r}: witness infeasible at {rho}')
        if sum(s) != sum(q[i] * rho[i] for i in range(n)): probs.append(f'chamber {r}: witness cost != q.rho at {rho}')
    # dual: sum_y y (sum_K lam_k) <= sum_y y a.s ; need sum_y y a + [z-part] <= 1 and lam-form == q.g
    coef = [Q(0)] * n; wK = [Q(0)] * d
    for I, J, K, v in ch['dual_y']:
        v = Q(v); tri = (tuple(I), tuple(J), tuple(K))
        if v < 0: probs.append(f'chamber {r}: y<0')
        if tri not in Tset: probs.append(f'chamber {r}: dual triple not in T^6 {tri}')
        a = horn_row(*tri)
        for i in range(n): coef[i] += v * a[i]
        for k in K: wK[k - 1] += v
    z = [Q(x) for x in ch['dual_z']]
    if len(z) != n - 1 or any(x < 0 for x in z): probs.append(f'chamber {r}: z')
    # s_k - s_{k+1} >= 0 with multiplier z_k >= 0:  sum y a.s = (coef - z-part).s where z-part.s = sum z_k (s_k - s_{k+1}) >= 0
    for k in range(n - 1): coef[k] += z[k]; coef[k + 1] -= z[k]
    if any(c > 1 for c in coef): probs.append(f'chamber {r}: dual coefficients exceed 1: {[str(c) for c in coef]}')
    # lam-form check on the 5 unit gap vectors
    for j in range(n):
        g = [Q(int(i == j)) for i in range(n)]; lam = lam_of(g)
        if sum(wK[k] * lam[k] for k in range(d)) != q[j]: probs.append(f'chamber {r}: lam-form != q at unit gap {j}')
    total_rays += len(listed)
print(f"chambers checked: {len(C['chambers'])}; total rays {total_rays}; problems: {probs if probs else 'NONE'}  [{time.time()-t0:.1f}s]", flush=True)

# coverage and numerical identity
rng = np.random.default_rng(5)
cnt_r = [0] * len(forms); ties = 0
for _ in range(100000):
    g = [Q(int(x)) for x in rng.integers(0, 50, size=n)]
    vals = [sum(q[i] * g[i] for i in range(n)) for q in forms]; m = max(vals)
    r = vals.index(m); cnt_r[r] += 1
    if sum(1 for v in vals if v == m) > 1: ties += 1
    assert all(sum((forms[r][i] - qj[i]) * g[i] for i in range(n)) >= 0 for qj in forms)   # g in C_r (tautology)
print(f"coverage sample 10^5 integer gap vectors: argmax counts per form {cnt_r}; ties {ties}")
worst = 0
for _ in range(3000):
    x = np.sort(rng.normal(size=d))[::-1]; x -= x.mean()
    g = [x[i] - x[i + 1] for i in range(n)]
    v, _ = horn_lp(list(x), T); f = max(sum(float(q[i]) * g[i] for i in range(n)) for q in forms)
    worst = max(worst, abs(v - f))
print(f"3000 random spectra: max |Horn LP - max of 22 forms| = {worst:.1e}  [{time.time()-t0:.1f}s]")
# also gap vectors with random zero pattern (boundary of the ordered cone)
worst = 0
for _ in range(2000):
    g = rng.exponential(size=n) * (rng.random(size=n) < 0.6)
    if g.sum() == 0: continue
    x = [g[j:].sum() for j in range(n)] + [0.0]; x = np.array(x) - np.mean(x)
    v, _ = horn_lp(list(x), T); f = max(sum(float(q[i]) * g[i] for i in range(n)) for q in forms)
    worst = max(worst, abs(v - f))
print(f"2000 random spectra with zero gaps: max |Horn LP - max of 22 forms| = {worst:.1e}  [{time.time()-t0:.1f}s]")
