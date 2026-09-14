"""Feasibility of a block-shift layering with layers of size <= 3, as one LP over the spectra sigma^(t) of S_t:
S_1 = -D_0;  spec R_t = spec S_t (same nonzero spectrum);  S_{t+1} = R_t - D_t >= 0  (Horn for n_t x n_t, n_t = |Lambda_t| <= 3);
R_T = D_T.  Layers: lists of floats (negative entries = -b's, zeros allowed).  Returns (feasible, sigmas)."""
import numpy as np, itertools
from scipy.optimize import linprog
from check_horn_lp import horn_t

def horn_ineqs(n):
    """Horn inequalities for n x n: list of (I,J,K), gamma_K <= alpha_I + beta_J, 1 <= r < n; plus trace equality handled separately."""
    out = []
    for r in range(1, n):
        for I, J, K in horn_t(r, n): out.append((I, J, K))
    return out

def cost(layers):
    tot = 0.0; Tr = 0.0
    for L in layers[:-1]:
        Tr -= sum(L); tot += Tr
    return tot

def layer_form(layers):
    """Level-structure check: returns the (w_i, v_j) description implicitly via cost; here just cost."""
    return cost(layers)

def feasible(layers, tol=1e-9, return_sigma=False):
    T = len(layers) - 1
    n = [len(L) for L in layers]
    assert all(1 <= k <= 3 for k in n)
    # variables: sigma^(t)_k for t=1..T, k=1..3  (index (t-1)*3 + (k-1))
    nv = 3 * T
    A_ub, b_ub, A_eq, b_eq = [], [], [], []
    def var(t, k): return (t - 1) * 3 + (k - 1)
    bounds = [(0, None)] * nv
    # ordering sigma_1 >= sigma_2 >= sigma_3 and rank caps: sigma^(t) lives on Lambda_{t-1} (S_t) and Lambda_t (R_t): rank <= min(n_{t-1}, n_t)
    for t in range(1, T + 1):
        for k in (1, 2):
            row = np.zeros(nv); row[var(t, k)] = -1; row[var(t, k + 1)] = 1; A_ub.append(row); b_ub.append(0.0)
        cap = min(n[t - 1], n[t])
        for k in range(cap + 1, 4): bounds[var(t, k)] = (0, 0)
    # S_1 = -D_0
    s1 = sorted([-x for x in layers[0]], reverse=True) + [0.0] * (3 - n[0])
    if any(x < -tol for x in s1): return (False, None) if return_sigma else False
    for k in range(1, 4):
        row = np.zeros(nv); row[var(1, k)] = 1; A_eq.append(row); b_eq.append(max(s1[k - 1], 0.0))
    # steps t=1..T-1: gamma = sigma^(t+1) (on Lambda_t, size n_t), alpha = sigma^(t) (first n_t entries), beta = sorted(-Lambda_t)
    for t in range(1, T):
        nt = n[t]; beta = sorted([-x for x in layers[t]], reverse=True)
        # trace: sum gamma = sum alpha + sum beta
        row = np.zeros(nv)
        for k in range(1, nt + 1): row[var(t + 1, k)] += 1; row[var(t, k)] -= 1
        A_eq.append(row); b_eq.append(sum(beta))
        for I, J, K in horn_ineqs(nt):
            row = np.zeros(nv)
            for k in K: row[var(t + 1, k)] += 1
            for i in I: row[var(t, i)] -= 1
            A_ub.append(row); b_ub.append(sum(beta[j - 1] for j in J))
    # terminal: sigma^(T) = sorted(Lambda_T) (all >= 0)
    sT = sorted(layers[T], reverse=True) + [0.0] * (3 - n[T])
    if any(x < -tol for x in sT): return (False, None) if return_sigma else False
    for k in range(1, 4):
        row = np.zeros(nv); row[var(T, k)] = 1; A_eq.append(row); b_eq.append(max(sT[k - 1], 0.0))
    res = linprog(np.zeros(nv), A_ub=np.array(A_ub), b_ub=np.array(b_ub) + tol, A_eq=np.array(A_eq), b_eq=np.array(b_eq), bounds=bounds, method='highs')
    ok = res.status == 0
    if return_sigma: return ok, (res.x.reshape(T, 3) if ok else None)
    return ok

def layering_of_form(f, a, b, m):
    """Layering (without zeros) from the level structure of the form f = (alpha_1..alpha_m, beta_1, beta_2)."""
    al = list(f[:m]); be = list(f[m:m + 2]) + [0]
    w3 = max(al); v = [w3 - x for x in al]; w = [x + w3 for x in be]
    T = max(w); lay = []
    for t in range(T, -1, -1):
        L = [-b[i] for i in range(3) if w[i] == t] + [a[j] for j in range(m) if v[j] == t]
        lay.append(L)
    return lay

def with_zeros(layers, nz):
    """All ways to insert nz zeros into layers (each layer keeps size <= 3); the first layer stays negative-only? (zeros allowed anywhere except we require last layer nonneg — fine)."""
    T = len(layers)
    slots = [t for t in range(T) if len(layers[t]) < 3]
    out = []
    for combo in itertools.combinations_with_replacement(slots, nz):
        new = [list(L) for L in layers]; ok = True
        for t in combo:
            if len(new[t]) >= 3: ok = False; break
            new[t].append(0.0)
        if ok: out.append(new)
    return out

if __name__ == "__main__":
    import sys, json
    from m3_complete import exposed_forms
    from m3_tools import radius, form_val
    from hive_core import HiveLP
    from m3_forms import spec_m3, rand_m3
    m, z, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); d = m + z + 3
    S = exposed_forms(m, z); M = HiveLP(d); rng = np.random.default_rng(9)
    print(f"m={m} z={z}: {len(S)} exposed forms")
    fail = {}; tot = 0; nz_used = {}
    for i in range(N):
        a, b = rand_m3(m, rng, law=['exp', 'unif', 'sq'][i % 3]); lam = spec_m3(a, b, z); kap = M.solve(lam)['val']
        vals = sorted(((form_val(np.array(g, float), a, b), g) for g in S), reverse=True)
        top = [g for v, g in vals if v > vals[0][0] - 1e-9]
        assert abs(vals[0][0] - kap) < 1e-7, (vals[0][0], kap)
        found = False
        for g in top:
            L0 = layering_of_form(g, a, b, m)
            assert abs(cost(L0) - vals[0][0]) < 1e-9
            for nz in range(0, min(z, 2) + 1):
                for L in with_zeros(L0, nz):
                    if feasible(L):
                        found = True; nz_used[nz] = nz_used.get(nz, 0) + 1; break
                if found: break
            if found: break
        tot += 1
        if not found:
            fail[tuple(top[0])] = fail.get(tuple(top[0]), 0) + 1
    print(f"  {tot} points: argmax layering feasible at {tot - sum(fail.values())}; zeros needed histogram {nz_used}; failures by form: {fail}")
