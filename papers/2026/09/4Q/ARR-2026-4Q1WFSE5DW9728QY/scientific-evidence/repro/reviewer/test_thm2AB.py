"""Reviewer tests of Theorem 2A (path systems) and Theorem 2B (interlacing chain), own code.
2A: kappa_7 of (10,5,1,1,1; 13,5) (own LP); random aligned spikes: kappa == sum_i sum_j j a^{(i)}_j and the explicit
    weighted-shift C satisfies CC*-C*C = 2F.
2B: explicit C built from Lemma 3.4 (Golub v_i^2 formula) + diagonal continuation at random points of R_k, n=2,3,4;
    residual ||CC*-C*C-2F||, cost identity, rank, kappa (own LP) == cost(L_k).  Also: which k have nonempty R_k.
"""
import numpy as np, itertools
from myhorn import HornLP, spec
from test_thm1 import build_L, cost_of, tmap

rng = np.random.default_rng(7)

# ---------------- Theorem 2A ----------------
def check_2A_example():
    a = np.array([10, 5, 1, 1, 1.]); b = np.array([13, 5.])
    H = HornLP(7); kap = H.solve(spec(a, b))['val']
    print(f"2A: kappa_7((10,1,1,1;-13)+(5;-5)) = {kap:.9f}  (one-spike sum 19+5 = 24)")
    return kap

def path_shift_C(paths, d):
    """paths: list of lists of (index, value) in consecutive layers; weighted shift C with |w_j|^2 = -2 * partial sum."""
    C = np.zeros((d, d))
    for path in paths:
        ps = 0.0
        for j in range(1, len(path)):
            ps += path[j - 1][1]
            assert ps <= 1e-12, ("partial sum > 0", path)
            C[path[j][0], path[j - 1][0]] = np.sqrt(max(0.0, -2 * ps))
        assert abs(ps + path[-1][1]) < 1e-12, ("total != 0", path)
    return C

def random_aligned(m, n):
    for _ in range(500):
        u = tuple(int(x) for x in rng.integers(0, m, size=n)); u = tuple(x - min(u) for x in u)
        layers, T = build_L(u, m, n)
        if T is None or max(u) > T: continue
        a = np.sort(rng.exponential(size=m))[::-1]
        t = tmap(layers)
        # assign positives in each layer to alive paths (started at negatives in earlier layers) by a random bijection
        assign = {}   # a_j -> path index i (0-based)
        ok = True
        for uu in range(1, T + 1):
            alive = [i for i in range(n) if u[i] < uu]
            pos = [j for j in range(1, m + 1) if t[('a', j)] == uu]
            if len(pos) > len(alive): ok = False; break
            perm = rng.permutation(len(alive))[:len(pos)]
            for q, j in enumerate(pos): assign[j] = alive[perm[q]]
        if not ok: continue
        bsum = np.zeros(n)
        for j, i in assign.items(): bsum[i] += a[j - 1]
        if bsum.min() <= 0: continue
        # relabel negatives by sorted value so that b_1 >= ... >= b_n (Theorem 1 allows any schedule)
        order = np.argsort(-bsum); newidx = {int(order[r]): r for r in range(n)}
        b = bsum[order]; u2 = tuple(u[int(order[r])] for r in range(n))
        assign2 = {j: newidx[i] for j, i in assign.items()}
        P = a.sum()
        return a / P, b / P, u2, assign2, layers, T
    return None

def check_2A_random(m, n, N=20):
    d = m + n; H = HornLP(d); worst = 0; worst_res = 0; cnt = 0
    for _ in range(N):
        r = random_aligned(m, n)
        if r is None: continue
        a, b, u, assign, layers, T = r
        layers2, T2 = build_L(u, m, n)   # layering with relabelled schedule
        # formula
        val = 0.0
        for i in range(n):
            js = sorted(j for j, ii in assign.items() if ii == i)   # positives of path i, in layer order (= index order since ordered)
            val += sum((q + 1) * a[j - 1] for q, j in enumerate(js))
        c = cost_of(layers2, a, b); lam = spec(a, b); kap = H.solve(lam)['val']
        # explicit C: index of a_j is j-1, of -b_i is d-i (0-based)
        paths = []
        for i in range(n):
            js = sorted(j for j, ii in assign.items() if ii == i)
            paths.append([(d - (i + 1), -b[i])] + [(j - 1, a[j - 1]) for j in js])
        C = path_shift_C(paths, d); F = np.diag(lam)
        res = np.linalg.norm(C @ C.T - C.T @ C - 2 * F)
        worst = max(worst, abs(val - c), abs(c - kap), abs(0.5 * np.sum(C ** 2) - c)); worst_res = max(worst_res, res); cnt += 1
    print(f"2A: (m,n)=({m},{n}): {cnt} random aligned-spike points: max |formula-cost|,|cost-kappa|,|cost-||C||^2/2| = {worst:.1e}; max residual ||CC*-C*C-2F|| = {worst_res:.1e}")

# ---------------- Theorem 2B ----------------
def tau(a, k, n):
    m = len(a)
    return np.array([sum(a[j - 1] for j in range(k + i, m + 1, n)) for i in range(1, n + 1)])

def layering_Lk(m, n, k):
    L = [[('b', 1)]]
    for j in range(1, k): L.append([('a', j)])
    L.append([('a', k)] + [('b', i) for i in range(2, n + 1)])
    j = k + 1
    while j <= m:
        L.append([('a', jj) for jj in range(j, min(j + n, m + 1))]); j += n
    return L

def golub_v(dvec, sigma, s):
    """unit v with spec(diag(dvec) + s vv^*) = sigma (Lemma 3.4), dvec distinct."""
    N = len(dvec); v2 = np.zeros(N)
    for i in range(N):
        num = np.prod([sigma[j] - dvec[i] for j in range(N)])
        den = s * np.prod([dvec[j] - dvec[i] for j in range(N) if j != i])
        v2[i] = num / den
    assert v2.min() > -1e-12, ("negative v_i^2", v2)
    v = np.sqrt(np.maximum(v2, 0)); return v, v2

def build_C_2B(a, b, k, z=0):
    m = len(a); n = len(b); d = m + n + z
    L = layering_Lk(m, n, k); T = len(L) - 1
    idx = lambda x: (x[1] - 1) if x[0] == 'a' else (d - x[1])   # 0-based spectrum index
    lam = spec(a, b, z)
    C = np.zeros((d, d))
    Bp = b[1:].sum()
    # singleton phase: M_u = sqrt(2 tail_u) from layer u-1 to layer u, u=1..k-1 (all 1x1)
    for uu in range(1, k):
        tail = a[uu - 1:].sum() - Bp
        assert tail >= -1e-12
        C[idx(L[uu][0]), idx(L[uu - 1][0])] = np.sqrt(2 * max(tail, 0))
    # mixed layer k: S_k = s = A_k - B', R_k = s v v^* on Lambda_k, M_k = sqrt(2s) v (column) from the singleton layer k-1
    s = a[k - 1:].sum() - Bp; assert s >= -1e-12
    dvec = np.array([-a[k - 1]] + list(b[1:]))          # diag(D_k) with sign flipped: S_{k+1} = s vv^* + diag(-a_k, b_2..b_n)
    sigma = tau(a, k, n)
    v, v2 = golub_v(dvec, sigma, s)
    src = idx(L[k - 1][0]); slots_k = [idx(x) for x in L[k]]
    for q, sl in enumerate(slots_k): C[sl, src] = np.sqrt(2 * s) * v[q]
    Sk1 = s * np.outer(v, v) + np.diag(dvec)
    ev = np.sort(np.linalg.eigvalsh(Sk1))[::-1]
    assert np.allclose(ev, np.sort(sigma)[::-1], atol=1e-9), (ev, sigma)
    # M_{k+1}: Lambda_k -> Lambda_{k+1}: M^* M = 2 S_{k+1}, M M^* = 2 R_{k+1} = 2 diag(tau) on the slots of layer k+1
    w, W = np.linalg.eigh(Sk1); order = np.argsort(-w); w = w[order]; W = W[:, order]   # w = tau sorted desc
    slots_next = [idx(x) for x in L[k + 1]] if k + 1 <= T else []
    # slot i of layer k+1 carries tau_i (column i); eigenvalue w[i] = tau_i
    M = np.zeros((len(slots_next), n))
    for i in range(len(slots_next)):
        M[i, :] = np.sqrt(2 * max(w[i], 0)) * W[:, i].conj()
    for i, sl in enumerate(slots_next):
        for q, sk in enumerate(slots_k): C[sl, sk] = M[i, q]
    # pure phase: diagonal, column i of layer k+1+r -> column i of layer k+2+r with weight sqrt(2 tau^{(r+1)}_i)
    for r in range(0, T - k - 1):
        Lcur = L[k + 1 + r]; Lnext = L[k + 2 + r]
        for i in range(len(Lnext)):
            tau_r1 = sum(a[j - 1] for j in range(k + i + 1 + (r + 1) * n, m + 1, n))
            C[idx(Lnext[i]), idx(Lcur[i])] = np.sqrt(2 * max(tau_r1, 0))
    F = np.diag(lam)
    resid = np.linalg.norm(C @ C.T - C.T @ C - 2 * F)
    return C, resid, cost_of(L, a, b), L

def sample_Rk(m, n, k, tries=500):
    for _ in range(tries):
        a = np.sort(rng.exponential(size=m))[::-1]; a /= a.sum()
        t = tau(a, k, n)
        if not all(t[i] > t[i + 1] + 1e-9 for i in range(n - 1)): continue
        b = np.zeros(n)
        for i in range(2, n + 1):
            lo, hi = t[i - 1], t[i - 2]; b[i - 1] = lo + (hi - lo) * rng.uniform(0.05, 0.95)
        b[0] = 1 - b[1:].sum()
        if b[0] > b[1] and b[-1] > 0: return a, b
    return None, None

if __name__ == "__main__":
    check_2A_example()
    for (m, n) in [(4, 2), (5, 3), (6, 3), (6, 4), (5, 4)]:
        check_2A_random(m, n, 25)
    # 2B
    for (m, n, z) in [(5, 2, 0), (5, 3, 0), (6, 3, 1), (6, 4, 0), (7, 4, 0), (5, 4, 0)]:
        d = m + n + z; H = HornLP(d) if d <= 9 else None
        for k in range(1, m + 1):
            got = 0; worst_res = 0; worst_gap = 0; ranks = set()
            for _ in range(10):
                a, b = sample_Rk(m, n, k)
                if a is None: break
                C, resid, c, L = build_C_2B(a, b, k, z)
                kap = H.solve(spec(a, b, z))['val'] if H else np.nan
                worst_res = max(worst_res, resid); worst_gap = max(worst_gap, abs(c - kap), abs(0.5 * np.sum(C ** 2) - c)); got += 1
                ranks.add(int(np.linalg.matrix_rank(C, tol=1e-8)))
            if got == 0:
                print(f"2B (m,n,z)=({m},{n},{z}) k={k}: R_k has EMPTY interior in the stratum (tau_{n-1}(k)={tau(np.ones(m)/m,k,n)[n-2]:.3f} for flat a; k+n-1<=m is {k+n-1<=m})")
            else:
                print(f"2B (m,n,z)=({m},{n},{z}) k={k}: {got} points of R_k: max ||CC*-C*C-2F|| = {worst_res:.1e}; max |cost-kappa|,|cost-||C||^2/2| = {worst_gap:.1e}; rank C in {sorted(ranks)} (m={m})")
