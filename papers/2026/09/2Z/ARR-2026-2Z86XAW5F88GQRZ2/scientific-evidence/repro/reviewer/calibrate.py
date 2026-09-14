"""Calibration of the reviewer's tools: (1) T^n_r (own Fulton recursion) vs own LR (Jacobi-Trudi/Pieri) for n<=7;
(2) own LR vs author's lr.py/lr2.py on random triples; (3) hive LP vs Horn LP at random spectra d=5..9 and known values."""
import os; AUTHOR_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "author")); REVIEWER_DIR = os.path.dirname(os.path.abspath(__file__))  # repro: these replace absolute paths in the original review scripts
import sys, time, numpy as np, itertools
sys.path.insert(0, AUTHOR_DIR)
from horn_own import T, all_T, lr_own, part, Hive, horn_rows, kappa_horn, spec, rand_point
from lr import lr as lr_auth, strip
from lr2 import lr2 as lr2_auth

# (1) T^n_r membership <=> LR > 0 (Knutson-Tao saturation), n <= 7, all triples with the sum condition
t0 = time.time()
for n in range(2, 8):
    bad = 0; tested = 0
    for r in range(1, n):
        Tset = set(T(r, n))
        subs = list(itertools.combinations(range(1, n + 1), r))
        for I in subs:
            for J in subs:
                for K in subs:
                    if sum(I) + sum(J) != sum(K) + r * (r + 1) // 2: continue
                    tested += 1
                    c = lr_own(part(I), part(J), part(K))
                    if (c > 0) != ((I, J, K) in Tset): bad += 1
    print(f"n={n}: {tested} sum-condition triples, T<->LR>0 mismatches: {bad}  ({time.time()-t0:.0f}s)", flush=True)

# (2) own LR vs author's two implementations on random partitions
rng = np.random.default_rng(7); mism = 0; nz = 0
for _ in range(1500):
    lam = tuple(sorted(rng.integers(0, 5, size=3), reverse=True)); mu = tuple(sorted(rng.integers(0, 4, size=3), reverse=True))
    nu = tuple(sorted(rng.integers(0, 8, size=4), reverse=True))
    if sum(nu) != sum(lam) + sum(mu): continue
    c0 = lr_own(lam, mu, nu); c1 = lr_auth(lam, mu, nu); c2 = lr2_auth(strip(lam), strip(mu), strip(nu))
    nz += c0 > 0
    if not (c0 == c1 == c2): mism += 1; print("  LR mismatch", lam, mu, nu, c0, c1, c2)
print(f"LR cross-check: mismatches {mism}, nonzero cases {nz}")
# symmetry + a known value: c^{(3,2,1)}_{(2,1),(2,1)} = 2
print("c^(321)_(21)(21) =", lr_own((2, 1), (2, 1), (3, 2, 1)), "(expected 2)")

# (3) hive LP vs Horn LP; known values from the (m,2)/rank-onset papers (s = p/2 normalisation: kappa = sum s with gamma = lambda)
rows = {d: horn_rows(d) for d in range(4, 10)}
print("kappa_4(3,-1,-1,-1) Horn:", kappa_horn([3, -1, -1, -1], rows[4]).fun, " hive:", Hive(4).solve([3, -1, -1, -1])['val'], " (paper: 6)")
print("kappa_5(4,-1,-1,-1,-1):", kappa_horn([4, -1, -1, -1, -1], rows[5]).fun, Hive(5).solve([4, -1, -1, -1, -1])['val'], "(paper: 10)")
l7 = np.array([25, 18, 18, -10, -17, -17, -17]) / 7; l8 = np.array([25, 18, 18, 0, -10, -17, -17, -17]) / 7
print("kappa_7*7:", kappa_horn(l7, rows[7]).fun * 7, Hive(7).solve(l7)['val'] * 7, "(74)")
print("kappa_8*7:", kappa_horn(l8, rows[8]).fun * 7, Hive(8).solve(l8)['val'] * 7, "(73)")
for d in range(5, 10):
    Hv = Hive(d); worst = 0
    for i in range(60):
        x = np.sort(rng.normal(size=d))[::-1]; x -= x.mean()
        v1 = kappa_horn(x, rows[d]).fun; v2 = Hv.solve(x)['val']; worst = max(worst, abs(v1 - v2))
    print(f"d={d}: max|hive - Horn| over 60 random spectra = {worst:.2e}")
