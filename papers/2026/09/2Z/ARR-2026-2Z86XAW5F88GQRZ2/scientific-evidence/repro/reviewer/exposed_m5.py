"""Task (e): exposedness of every listed form for m=5 (z=0 and z=1): own radius LP (max t: g - h >= t for all other h, on the
P=1 stratum with strict ordering margin), kappa at the centre by the own Horn LP (d=8) / hive LP (d=9), and argmax sampling."""
import os; AUTHOR_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "author")); REVIEWER_DIR = os.path.dirname(os.path.abspath(__file__))  # repro: these replace absolute paths in the original review scripts
import sys, json, numpy as np
from scipy.optimize import linprog
sys.path.insert(0, AUTHOR_DIR)
from horn_own import horn_rows, kappa_horn, Hive, spec, rand_point, form_val
W = AUTHOR_DIR

def radius(gf, others, m):
    n = m + 4; A = []; ub = []
    for h in others:
        row = np.zeros(n); row[:m] = np.array(h[:m]) - np.array(gf[:m]); row[m] = h[m] - gf[m]; row[m + 1] = h[m + 1] - gf[m + 1]; row[-1] = 1; A.append(row); ub.append(0)
    for j in range(m - 1):
        row = np.zeros(n); row[j] = -1; row[j + 1] = 1; row[-1] = 1; A.append(row); ub.append(0)
    row = np.zeros(n); row[m - 1] = -1; row[-1] = 1; A.append(row); ub.append(0)
    for j in range(2):
        row = np.zeros(n); row[m + j] = -1; row[m + j + 1] = 1; row[-1] = 1; A.append(row); ub.append(0)
    row = np.zeros(n); row[m + 2] = -1; row[-1] = 1; A.append(row); ub.append(0)
    Aeq = np.zeros((2, n)); Aeq[0, :m] = 1; Aeq[1, m:m + 3] = 1
    c = np.zeros(n); c[-1] = -1
    res = linprog(c, A_ub=np.array(A), b_ub=np.array(ub), A_eq=Aeq, b_eq=[1, 1], bounds=[(0, None)] * (m + 3) + [(None, 1)], method='highs')
    return -res.fun, res.x[:m], res.x[m:m + 3]

m = 5; rows8 = horn_rows(8); H9 = Hive(9)
for z in (0, 1):
    S = [tuple(f) for f in json.load(open(f"{W}/closed_m{m}_z{z}.json"))]; d = m + z + 3
    print(f"m=5 z={z}: {len(S)} forms")
    nexp = 0; minrad = 1
    for gf in S:
        t, a, b = radius(gf, [h for h in S if h != gf], m)
        kap = kappa_horn(spec(a, b, z), rows8).fun if z == 0 else H9.solve(spec(a, b, z))['val']
        ok = t > 1e-9 and abs(kap - form_val(gf, a, b)) < 1e-9
        nexp += ok; minrad = min(minrad, t)
        if not ok: print(f"   NOT exposed / not attained: {gf}: radius {t:.3e}, kappa-g = {kap - form_val(gf, a, b):.2e}")
    print(f"   exposed with kappa = g at the centre: {nexp}/{len(S)}; smallest chamber radius {minrad:.3e}")
    # sampling
    rng = np.random.default_rng(55); cnt = {gf: 0 for gf in S}; ties = 0
    for i in range(6000):
        a, b = rand_point(m, rng, law=i % 6)
        vals = sorted(((form_val(gf, a, b), gf) for gf in S), reverse=True)
        if vals[0][0] - vals[1][0] > 1e-9: cnt[vals[0][1]] += 1
        else: ties += 1
    never = [gf for gf in S if cnt[gf] == 0]
    print(f"   argmax sampling (6000 pts): forms never unique argmax: {len(never)} {never}; tie points {ties}")
    # also check: is the z=0 extra form valid at z=1? (validity = kappa_{z=1} >= g everywhere; test at its z=0 centre)
    if z == 0:
        g0 = (1, 2, 3, 3, 4, -2, -1); t, a, b = radius(g0, [h for h in S if h != g0], m)
        k8 = kappa_horn(spec(a, b, 0), rows8).fun; k9 = H9.solve(spec(a, b, 1))['val']
        print(f"   z=0 extra form {g0} at its chamber centre a={np.round(a,4)} b={np.round(b,4)}: g0={form_val(g0,a,b):.6f} kappa_8={k8:.6f} kappa_9={k9:.6f} (kappa_9 < g0 => invalid after padding: {k9 < form_val(g0,a,b) - 1e-9})")
