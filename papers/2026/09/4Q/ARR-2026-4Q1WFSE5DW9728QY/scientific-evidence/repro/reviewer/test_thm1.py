"""Reviewer test of Theorem 1 / Lemma 2.3 / Prop 2.4 with own code.
(1) Own construction of L(u) (Definition 2.1) for every schedule u in {0..m}^n, min u = 0 (including u_i > T, Remark 2.6).
(2) Own construction of the certificate tiles; exact (integer) checks: tile in own T^d_r, own LR == 1, sum condition,
    LHS coefficient identity (each s_t, t<=m, once; negatives only at d-n+1..d-1), RHS identity (sum of tile RHS = cost + sum of b's in layer T).
(3) 300 random points per stratum (3,3,0),(4,3,0),(4,4,0),(5,4,0): max_u cost(L(u)) <= kappa (own Horn LP); OL == OL_nondecreasing.
(4) Prop 2.4: kappa_4(1,1,-1,-1) by own LP and four-level formula; cost of {-b1,-b2}{a1}{a2}; the under-filled family in general.
"""
import itertools, numpy as np, time
from fractions import Fraction as Q
from myhorn import HornLP, horn_T, part, strip, lr_coeff, spec, kappa4

def build_L(u, m, n):
    """Definition 2.1. Returns (layers, T) with layers[t] = list of ('a',j)/('b',i). Positives in decreasing order,
    layer t>=1 gets exactly c_t = #{i: u_i < t} positives while positives remain.  Negatives with u_i > T are kept
    (Remark 2.6)."""
    Tmax = max(u); layers = [[] for _ in range(Tmax + 2)]
    for i, ui in enumerate(u): layers[ui].append(('b', i + 1))
    j = 1; t = 1; T = None
    while j <= m:
        if t >= len(layers): layers.append([])
        c = sum(1 for ui in u if ui < t)
        for _ in range(c):
            if j > m: break
            layers[t].append(('a', j)); j += 1
        if j > m: T = t
        t += 1
    while layers and not layers[-1]: layers.pop()
    return layers, T

def tmap(layers):
    t = {}
    for u, layer in enumerate(layers):
        for x in layer: t[x] = u
    return t

def cost_of(layers, a, b):
    t = tmap(layers)
    return sum(t[('a', j)] * a[j - 1] for j in range(1, len(a) + 1)) - sum(t[('b', i)] * b[i - 1] for i in range(1, len(b) + 1))

def certificate(u, m, n, z):
    """Tiles of Theorem 1 for schedule u (requires max u <= T). Returns list of (I,J,K) 1-based tuples."""
    d = m + n + z
    layers, T = build_L(u, m, n)
    assert max(u) <= T
    tiles = []
    # t_u = index of first positive in layers >= u
    for uu in range(1, T):
        pos = [j for j, ui in enumerate(u)]  # dummy
        tu = min(j for j in range(1, m + 1) if tmap(layers)[('a', j)] >= uu)
        Bu = {d + 1 - (i + 1) for i, ui in enumerate(u) if ui < uu}
        K = tuple(k for k in range(tu, d + 1) if k not in Bu)
        r = len(K); J = tuple(range(1, r + 1))
        tiles.append((K, J, K))
    tT = min(j for j in range(1, m + 1) if tmap(layers)[('a', j)] >= T)
    for j in range(tT, m + 1): tiles.append(((j,), (1,), (j,)))
    return tiles, layers, T

def check_certificate(u, m, n, z, Tsets):
    d = m + n + z
    tiles, layers, T = certificate(u, m, n, z)
    lhs = np.zeros(d, int)      # coefficient of s_1..s_{d-1} (index d unused; s_d = 0)
    rhs = np.zeros(d, int)      # coefficient of lambda_k
    for (I, J, K) in tiles:
        r = len(I)
        assert sum(I) + sum(J) == sum(K) + r * (r + 1) // 2
        key = (I, J, K)
        assert key in Tsets[r], ("tile not in own T^d_r", key)
        assert lr_coeff(part(I), part(J), part(K)) == 1, ("LR != 1", key)
        for i in I:
            if i < d: lhs[i - 1] += 1
        for j in J:
            if j > 1: lhs[d - j] -= 1
        for k in K: rhs[k - 1] += 1
    # LHS: s_t for t<=m coefficient exactly 1; t in (m, d-n] coefficient 0; t in [d-n+1, d-1] coefficient <= 0
    assert all(lhs[t - 1] == 1 for t in range(1, m + 1)), (u, lhs)
    assert all(lhs[t - 1] == 0 for t in range(m + 1, d - n + 1)), (u, lhs)
    assert all(lhs[t - 1] <= 0 for t in range(d - n + 1, d)), (u, lhs)
    # RHS: coefficient of a_j = t(a_j); coefficient of -b_i = min(u_i, T-1) (b's in layer T are dropped by the Weyl tiles); zeros 0
    t = tmap(layers)
    assert all(rhs[j - 1] == t[('a', j)] for j in range(1, m + 1)), (u, rhs)
    # zero indices may appear in K (they contribute lambda_k = 0 to the value); nothing to check there
    assert all(rhs[d - i] == min(u[i - 1], T - 1) for i in range(1, n + 1)), (u, rhs, T)
    return tiles, layers, T

def all_schedules(m, n):
    for u in itertools.product(range(0, m + 1), repeat=n):
        if min(u) == 0: yield u

if __name__ == "__main__":
    # ---- exact certificate checks for small (m,n,z), all schedules with max u <= T ----
    for (m, n, z) in [(3, 3, 0), (3, 3, 1), (4, 3, 0), (4, 4, 0), (5, 4, 0), (5, 3, 1)]:
        d = m + n + z; T = horn_T(d)
        Tsets = {r: set(tuple(tuple(int(x) for x in row) for row in tri) for tri in T[r]) for r in range(1, d)}
        cnt = 0; ex = None
        for u in all_schedules(m, n):
            layers, TT = build_L(u, m, n)
            if max(u) > TT: continue
            check_certificate(u, m, n, z, Tsets); cnt += 1
            if (m, n, z) == (4, 3, 0) and u == (0, 2, 1): ex = (u, layers, TT)
        print(f"(m,n,z)=({m},{n},{z}): certificate of Theorem 1 verified exactly (own T^d_r membership, own LR=1, LHS/RHS identities) for {cnt} schedules")
        if ex:
            u, layers, TT = ex; tiles, _, _ = certificate(u, m, n, z)
            print(f"   example inverted schedule u={u}: layers {layers}; tiles {tiles}")
    # ---- random points: bound never violated; OL == OL_A ----
    rng = np.random.default_rng(2024)
    def sample(m, n, law):
        if law == 'exp': a = rng.exponential(size=m); b = rng.exponential(size=n)
        elif law == 'unif': a = rng.uniform(size=m); b = rng.uniform(size=n)
        elif law == 'int': a = rng.integers(1, 5, size=m).astype(float); b = rng.integers(1, 5, size=n).astype(float)
        elif law == 'dom': a = rng.exponential(size=m); a[0] += 2 * a.sum(); b = rng.exponential(size=n)
        elif law == 'flatb': a = rng.exponential(size=m); b = np.ones(n) + 0.05 * rng.uniform(size=n)
        a = np.sort(a)[::-1]; b = np.sort(b)[::-1]
        return a / a.sum(), b / b.sum()
    for (m, n, z) in [(3, 3, 0), (4, 3, 0), (4, 4, 0), (5, 4, 0)]:
        d = m + n + z; H = HornLP(d); t0 = time.time()
        scheds = [(u,) + build_L(u, m, n) for u in all_schedules(m, n)]
        worst = -np.inf; eq = 0; eqA = 0; N = 300; under_exceed = 0; worst_under = -np.inf
        for it in range(N):
            law = ['exp', 'unif', 'int', 'dom', 'flatb'][it % 5]
            a, b = sample(m, n, law); lam = spec(a, b, z); kap = H.solve(lam)['val']
            costs = {u: cost_of(L, a, b) for (u, L, TT) in scheds}
            OL = max(costs.values()); OLA = max(v for u, v in costs.items() if all(u[i] <= u[i + 1] for i in range(n - 1)))
            worst = max(worst, OL - kap)
            if abs(OL - kap) < 1e-9: eq += 1
            if abs(OLA - kap) < 1e-9: eqA += 1
            # under-filled: same schedule, positives in order, but layer t>=1 gets q_t in [1, c_t] positives (random choice); take the max over a random sample
            best_under = -np.inf
            for (u, L, TT) in scheds[:40]:
                for _ in range(3):
                    layers = [[] for _ in range(max(u) + 2)]
                    for i, ui in enumerate(u): layers[ui].append(('b', i + 1))
                    j = 1; t = 1
                    while j <= m:
                        if t >= len(layers): layers.append([])
                        c = sum(1 for ui in u if ui < t)
                        if c > 0:
                            q = int(rng.integers(1, c + 1))
                            for _ in range(q):
                                if j > m: break
                                layers[t].append(('a', j)); j += 1
                        t += 1
                    best_under = max(best_under, cost_of(layers, a, b))
            if best_under > kap + 1e-9: under_exceed += 1
            worst_under = max(worst_under, best_under - kap)
        print(f"(m,n,z)=({m},{n},{z}) d={d}: {N} points, {len(scheds)} schedules: max(OL-kappa)={worst:.1e}; kappa==OL at {eq}/{N}; kappa==OL_A at {eqA}/{N}; "
              f"random under-filled layerings exceed kappa at {under_exceed}/{N} points (max excess {worst_under:.3f}); {time.time()-t0:.0f}s", flush=True)
    # ---- Prop 2.4 ----
    H4 = HornLP(4); lam = np.array([1, 1, -1, -1.])
    print(f"kappa_4(1,1,-1,-1): own LP {H4.solve(lam)['val']:.6f}; four-level formula {kappa4(lam)}; cost of {{-b1,-b2}}{{a1}}{{a2}} = 1*a1+2*a2 = 3")
    # generic (2,2): is a_1 + 2 a_2 ever valid? compare at random points
    viol = 0
    for _ in range(50):
        a = np.sort(rng.exponential(size=2))[::-1]; b = np.sort(rng.exponential(size=2))[::-1]; a /= a.sum(); b /= b.sum()
        lam = spec(a, b); kap = H4.solve(lam)['val']
        if a[0] + 2 * a[1] > kap + 1e-9: viol += 1
    print(f"   form a1+2a2 (under-filled layering) exceeds kappa_4 at {viol}/50 random (2,2) points")
    # the failing step: with the "at most" version, tiles overlap.  Show explicitly for u=(0,0), m=2: tile u=1: K={1..4}\{3,4} = {1,2}: s1+s2 >= a1+a2 (=tail_1);
    # Weyl tile for last layer {a2}: s2 >= a2.  Sum: s1 + 2 s2 >= a1 + 2 a2 -- s2 counted twice, so sum s_t >= cost does NOT follow.
    print("   failing step in the 'at most' version: the LW tile of layer u uses the block [t_u, t_u+c_u-1]; when layer u holds q<c_u positives the next block starts at t_u+q < t_u+c_u, so the positive blocks overlap and some s_t gets coefficient 2 (here s_2): the sum of tiles no longer is <= sum_{t<d} s_t.")
