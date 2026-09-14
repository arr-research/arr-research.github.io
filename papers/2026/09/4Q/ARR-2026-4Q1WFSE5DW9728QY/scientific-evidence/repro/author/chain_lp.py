"""Feasibility of an n x n-block weighted-shift layering (layers of size <= nmax) as one LP over the spectra sigma^(t)
of S_t (generalisation of cycle2/work/A3_inertia_m3/layering_lp.py to nmax <= 5), plus the test 'is the level layering
of SOME form attaining kappa at the point (with up to two inserted zeros) chain-feasible?' at random points.
If forms_m{m}_n{n}_z{z}.json exists, all forms tied at kappa are tried (important at tie-heavy points); otherwise only the
dual form returned by the hive LP is tried.
Usage: python chain_lp.py "m,n,z;..." N [seed]"""
import sys, time, itertools, json, os, numpy as np
from scipy.optimize import linprog
from check_horn_lp import horn_t
from mn_tools import *

def horn_ineqs(n):
    return [(I, J, K) for r in range(1, n) for (I, J, K) in horn_t(r, n)]

def feasible(layers, nmax, tol=1e-9):
    """layers: list of lists of floats (negatives = -b's; zeros allowed). Layer 0 nonpositive, last layer nonnegative."""
    T = len(layers) - 1; nn = [len(L) for L in layers]
    assert all(1 <= k <= nmax for k in nn)
    nv = nmax * T
    def var(t, k): return (t - 1) * nmax + (k - 1)
    A_ub, b_ub, A_eq, b_eq = [], [], [], []
    bounds = [(0, None)] * nv
    for t in range(1, T + 1):
        for k in range(1, nmax):
            row = np.zeros(nv); row[var(t, k)] = -1; row[var(t, k + 1)] = 1; A_ub.append(row); b_ub.append(0.0)
        cap = min(nn[t - 1], nn[t])
        for k in range(cap + 1, nmax + 1): bounds[var(t, k)] = (0, 0)
    s1 = sorted([-x for x in layers[0]], reverse=True) + [0.0] * (nmax - nn[0])
    if any(x < -tol for x in s1): return False
    for k in range(1, nmax + 1):
        row = np.zeros(nv); row[var(1, k)] = 1; A_eq.append(row); b_eq.append(max(s1[k - 1], 0.0))
    for t in range(1, T):
        nt = nn[t]; beta = sorted([-x for x in layers[t]], reverse=True)
        row = np.zeros(nv)
        for k in range(1, nt + 1): row[var(t + 1, k)] += 1; row[var(t, k)] -= 1
        A_eq.append(row); b_eq.append(sum(beta))
        for I, J, K in horn_ineqs(nt):
            row = np.zeros(nv)
            for k in K: row[var(t + 1, k)] += 1
            for i in I: row[var(t, i)] -= 1
            A_ub.append(row); b_ub.append(sum(beta[j - 1] for j in J))
    sT = sorted(layers[T], reverse=True) + [0.0] * (nmax - nn[T])
    if any(x < -tol for x in sT): return False
    for k in range(1, nmax + 1):
        row = np.zeros(nv); row[var(T, k)] = 1; A_eq.append(row); b_eq.append(max(sT[k - 1], 0.0))
    res = linprog(np.zeros(nv), A_ub=np.array(A_ub), b_ub=np.array(b_ub) + tol, A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=bounds, method='highs')
    return res.status == 0

def numeric_layers(L, a, b):
    out = []
    for layer in L:
        out.append([a[i - 1] if k == 'a' else (-b[i - 1] if k == 'b' else 0.0) for k, i in layer])
    return out

def with_zeros(layers, nz, nmax):
    T = len(layers); slots = [t for t in range(T) if len(layers[t]) < nmax]
    out = []
    for combo in itertools.combinations_with_replacement(slots, nz):
        new = [list(L) for L in layers]; ok = True
        for t in combo:
            if len(new[t]) >= nmax: ok = False; break
            new[t].append(0.0)
        if ok: out.append(new)
    return out

def chain_ok(f, a, b, m, n, z):
    """Is the level layering of f (with up to two inserted zeros) chain-feasible at (a,b)? Returns (ok, nz, maxsize)."""
    L = level_layering(f, m, n); ms = max(len(x) for x in L); nmax = max(ms, n)
    if any(k == 'a' for k, _ in L[0]) or any(k == 'b' for k, _ in L[-1]) or any(len(x) == 0 for x in L):
        return False, None, ms
    base = numeric_layers(L, a, b)
    for nz in range(0, min(z, 2) + 1):
        for LL in with_zeros(base, nz, nmax):
            if feasible(LL, nmax): return True, nz, ms
    return False, None, ms

if __name__ == "__main__":
    cases = [tuple(int(x) for x in c.split(',')) for c in sys.argv[1].split(';')]
    N = int(sys.argv[2]); seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    for (m, n, z) in cases:
        d = m + n + z; t0 = time.time(); M = HiveLP(d); rng = np.random.default_rng(seed + 100 * m + 10 * n + z)
        fn = f"forms_m{m}_n{n}_z{z}.json"
        S = [tuple(json.loads(k)) for k in json.load(open(fn)) if not k.startswith('_')] if os.path.exists(fn) else None
        ok = 0; fail = {}; zeros_used = {}; sizes = {}; nonint = 0; tied_hist = {}
        for i in range(N):
            a, b = rand_ab(m, n, rng, LAWS[i % len(LAWS)]); lam = spec(a, b, z); r = M.solve(lam)
            if S is not None:
                cands = [f for f in S if abs(form_val(np.array(f, float), a, b) - r['val']) < 1e-8]
                if not cands: nonint += 1; continue
            else:
                f = canon(r['grad'], m, n, z); key = tuple(rat(x, 2000) for x in f)
                if any(k.denominator != 1 for k in key): nonint += 1; continue
                f = tuple(int(k) for k in key)
                if abs(form_val(np.array(f, float), a, b) - r['val']) > 1e-7: nonint += 1; continue
                cands = [f]
            tied_hist[len(cands)] = tied_hist.get(len(cands), 0) + 1
            found = False
            for f in cands:
                good, nz, ms = chain_ok(f, a, b, m, n, z)
                if good:
                    found = True; zeros_used[nz] = zeros_used.get(nz, 0) + 1; sizes[ms] = sizes.get(ms, 0) + 1; break
            if found: ok += 1
            else: fail[cands[0]] = fail.get(cands[0], 0) + 1
        print(f"(m,n,z)=({m},{n},{z}) d={d}: N={N}: some maximising form's level layering is chain-feasible at {ok}/{N - nonint} "
              f"(skipped: {nonint}; forms file: {'yes' if S else 'no'}); #tied forms histogram {dict(sorted(tied_hist.items()))}; zeros inserted {zeros_used}; "
              f"max layer size of the feasible layering {dict(sorted(sizes.items()))}; failures (first tied form): {fail}; {time.time()-t0:.0f}s", flush=True)
