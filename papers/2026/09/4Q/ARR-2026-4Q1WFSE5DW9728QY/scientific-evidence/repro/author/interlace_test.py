"""Experiment 4: numerical checks of Theorem 2A (diagonal/aligned-spike chains) and Theorem 2B (interlacing region).
2B: layering L_k = {-b_1}{a_1}...{a_{k-1}}{a_k,-b_2,...,-b_n}{a_{k+1..k+n}}{a_{k+n+1..k+2n}}...; tau_i(k) = sum_r a_{k+i+rn};
    region R_k = {tau_i(k) <= b_i <= tau_{i-1}(k), i=2..n} (inside the stratum).  Claim: kappa = cost(L_k) on R_k.
2A: aligned spikes: an ordered full-capacity layering with a bijection per layer defining n balanced paths; claim kappa = cost.
    Non-aligned direct sums: kappa < sum of one-spike costs (examples).
Usage: python interlace_test.py "m,n,z;..." N [seed]"""
import sys, time, numpy as np
from mn_tools import *

def tau(a, k, n):
    m = len(a); out = []
    for i in range(1, n + 1):
        s = 0.0; j = k + i
        while j <= m: s += a[j - 1]; j += n
        out.append(s)
    return out

def layering_Lk(m, n, k):
    L = [[('b', 1)]]
    for j in range(1, k): L.append([('a', j)])
    L.append([('a', k)] + [('b', i) for i in range(2, n + 1)])
    j = k + 1
    while j <= m:
        L.append([('a', jj) for jj in range(j, min(j + n, m + 1))]); j += n
    return L

def sample_region(m, n, k, rng, tries=200):
    """Random point of R_k with P=1 (rejection on b_1 >= b_2)."""
    for _ in range(tries):
        a = np.sort(rng.exponential(size=m))[::-1]; a /= a.sum()
        t = tau(a, k, n); b = [None] * n
        for i in range(2, n + 1):
            lo, hi = t[i - 1], t[i - 2]
            b[i - 1] = lo + (hi - lo) * rng.uniform()
        b[0] = 1.0 - sum(b[1:])
        if b[0] >= b[1] - 1e-12 and all(b[i] >= b[i + 1] - 1e-12 for i in range(n - 1)) and b[-1] > 0:
            return a, np.array(b)
    return None, None

def sample_aligned(m, n, rng):
    """Random ordered full-capacity layering (nondecreasing schedule) with random per-layer bijections -> balanced spikes."""
    for _ in range(200):
        u = tuple(sorted(rng.integers(0, m, size=n)));
        if u[0] != 0: u = tuple(x - u[0] for x in u)
        L = ordered_layering(u, m, n)
        if L is None: continue
        a = np.sort(rng.exponential(size=m))[::-1]
        # paths: path i starts at b_i in layer u_i; in each layer the a's are assigned to alive paths by a random bijection
        bsum = np.zeros(n)
        for t, layer in enumerate(L):
            if t == 0: continue
            alive = [i for i in range(n) if u[i] < t]
            aa = [i for k, i in layer if k == 'a']
            if len(aa) > len(alive): break
            perm = rng.permutation(len(alive))[:len(aa)]
            for q, j in enumerate(aa): bsum[alive[perm[q]]] += a[j - 1]
        else:
            if bsum.min() <= 0: continue
            b_sorted = np.sort(bsum)[::-1]
            # the layering as a partition of VALUES: relabel b's by sorted order
            order = np.argsort(-bsum)          # order[r] = original path index of the r-th largest
            inv = {int(order[r]): r + 1 for r in range(n)}
            L2 = [[(k, inv[i - 1]) if k == 'b' else (k, i) for k, i in layer] for layer in L]
            return a / a.sum(), b_sorted / a.sum(), L2, u
    return None, None, None, None

if __name__ == "__main__":
    cases = [tuple(int(x) for x in c.split(',')) for c in sys.argv[1].split(';')]
    N = int(sys.argv[2]); seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    for (m, n, z) in cases:
        d = m + n + z; M = HiveLP(d); rng = np.random.default_rng(seed + 100 * m + 10 * n + z); t0 = time.time()
        # Theorem 2B
        worst = 0.0; cnt = 0; per_k = {}
        for k in range(1, m + 1):
            for i in range(N):
                a, b = sample_region(m, n, k, rng)
                if a is None: continue
                L = layering_Lk(m, n, k); c = cost(L, a, b); kap = M.solve(spec(a, b, z))['val']
                worst = max(worst, abs(c - kap)); cnt += 1
                per_k[k] = per_k.get(k, 0) + 1
        print(f"(m,n,z)=({m},{n},{z}): Theorem 2B: {cnt} points in the regions R_k (k=1..{m}, counts {per_k}): max|cost(L_k)-kappa| = {worst:.1e}", flush=True)
        # boundary sharpness of R_k for n>=3: points just outside (b_i slightly above tau_{i-1} or below tau_i): does kappa < cost?
        out_viol = 0; out_tot = 0
        for k in range(1, m + 1):
            for i in range(N // 4):
                a, b = sample_region(m, n, k, rng)
                if a is None: continue
                t = tau(a, k, n); L = layering_Lk(m, n, k)
                # push b_n below tau_n by 5% of its value (and compensate on b_1)
                bb = b.copy(); eps = 0.05 * bb[-1] + 1e-3; bb[-1] -= eps; bb[0] += eps
                if bb[-1] <= 0: continue
                c = cost(L, a, bb); kap = M.solve(spec(a, bb, z))['val']; out_tot += 1
                if kap > c + 1e-9: out_viol += 1
        print(f"   just outside R_k (b_n pushed 5% below tau_n): kappa > cost(L_k) strictly (L_k no longer optimal) at {out_viol}/{out_tot}", flush=True)
        # Theorem 2A
        worst = 0.0; cnt = 0
        for i in range(N):
            a, b, L, u = sample_aligned(m, n, rng)
            if a is None: continue
            c = cost(L, a, b); kap = M.solve(spec(a, b, z))['val']; worst = max(worst, abs(c - kap)); cnt += 1
        print(f"   Theorem 2A: {cnt} aligned-spike points: max|cost-kappa| = {worst:.1e}; {time.time()-t0:.0f}s", flush=True)
    # non-aligned direct sum example: (10,1,1,1; 13) + (5; 5)
    a = np.array([10, 5, 1, 1, 1.]); b = np.array([13, 5.]); M = HiveLP(7)
    kap = M.solve(spec(a, b, 0))['val']; ones = (10 + 2 + 3 + 4) + 5
    print(f"Non-aligned direct sum (10,1,1,1;13)+(5;5): kappa_7 = {kap:.6f} vs sum of one-spike costs {ones} -> strict subadditivity: {kap < ones - 1e-9}")
    # random direct sums of two one-spikes: additivity iff alignable (test)
    rng = np.random.default_rng(5); add = 0; tot = 0
    for i in range(200):
        m1, m2 = rng.integers(1, 4), rng.integers(1, 4)
        a1 = np.sort(rng.exponential(size=m1))[::-1]; a2 = np.sort(rng.exponential(size=m2))[::-1]
        a = np.sort(np.concatenate([a1, a2]))[::-1]; b = np.sort([a1.sum(), a2.sum()])[::-1]
        P = a.sum(); M = HiveLP(len(a) + 2); kap = M.solve(spec(a / P, b / P, 0))['val'] * P
        s = sum((j + 1) * x for j, x in enumerate(a1)) + sum((j + 1) * x for j, x in enumerate(a2)); tot += 1
        if abs(kap - s) < 1e-9: add += 1
    print(f"random two-spike direct sums: additive at {add}/{tot}")
