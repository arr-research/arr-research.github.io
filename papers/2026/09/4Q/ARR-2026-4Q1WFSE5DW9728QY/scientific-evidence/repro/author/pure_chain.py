"""Experiment 5: the pure-a chain.  State sigma = spec(S) (n values, trace = total of the remaining layers), then layers
of n sorted a's (last possibly partial).  Which sigma are chain-feasible?  (For n = 2 the (m,2) paper's recursion gives
tau_2 <= sigma_2 <= tau_1 - max_t(delta^t_1 - delta^t_2) for the F_0 layering; we test candidate descriptions for n = 3, 4.)
tau_i = sum_t delta^t_i (column sums), G_{ij} = max_t (delta^t_i - delta^t_j) (max intralayer gap between columns i<j).
Candidates: (M) sigma majorized by tau (bottom-k sums of sigma >= bottom-k sums of tau);
            (G1) sigma_i <= tau_{i-1} - G_{i-1,i} for i = 2..n;
            (G2) sigma_i + ... + sigma_j <= tau_{i-1} + ... + tau_{j-1} - G_{i-1,j} for i <= j  (generalised);
            (G3) for every k: sum of the k smallest sigma's <= sum of the k smallest tau's shifted... (see code).
Usage: python pure_chain.py n m N [seed]"""
import sys, time, itertools, numpy as np
from chain_lp import feasible

def col_sums(layers, n):
    tau = np.zeros(n)
    for L in layers:
        for i, x in enumerate(sorted(L, reverse=True)): tau[i] += x
    return tau

def gaps(layers, n):
    G = np.zeros((n, n))
    for L in layers:
        s = sorted(L, reverse=True) + [0.0] * (n - len(L))
        for i in range(n):
            for j in range(i + 1, n): G[i, j] = max(G[i, j], s[i] - s[j])
    return G

def majorized(sig, tau):
    s = np.sort(sig); t = np.sort(tau)
    return all(s[:k].sum() >= t[:k].sum() - 1e-9 for k in range(1, len(s)))

if __name__ == "__main__":
    n, m, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); seed = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    rng = np.random.default_rng(seed); t0 = time.time()
    stats = {'feas': 0, 'tot': 0, 'M_nec_viol': 0, 'G1_nec_viol': 0, 'G2_nec_viol': 0, 'all_suff_fail': 0, 'all_hold': 0}
    examples = []
    for i in range(N):
        a = np.sort(rng.exponential(size=m))[::-1]; a /= a.sum()
        layers = [list(a[j:j + n]) for j in range(0, m, n)]
        tau = col_sums(layers, n); G = gaps(layers, n)
        # random state sigma with trace 1 (Dirichlet), sorted
        sig = np.sort(rng.dirichlet(np.ones(n) * rng.choice([0.5, 1, 3])))[::-1]
        chain = [[-x for x in sig]] + layers      # layer 0 = -sigma (a fictitious negative layer), so S_1 = diag(sigma)
        f = feasible(chain, n)
        M = majorized(sig, tau)
        G1 = all(sig[i] <= tau[i - 1] - G[i - 1, i] + 1e-9 for i in range(1, n))
        G2 = all(sig[i:j + 1].sum() <= tau[i - 1:j].sum() - G[i - 1, j] + 1e-9 for i in range(1, n) for j in range(i, n))
        stats['tot'] += 1; stats['feas'] += f
        if f and not M: stats['M_nec_viol'] += 1
        if f and not G1: stats['G1_nec_viol'] += 1
        if f and not G2: stats['G2_nec_viol'] += 1
        if M and G2:
            stats['all_hold'] += 1
            if not f:
                stats['all_suff_fail'] += 1
                if len(examples) < 3: examples.append((a.round(4), sig.round(4), tau.round(4)))
    print(f"n={n} m={m}: {N} random (layers, sigma): feasible {stats['feas']}; feasible but violating majorization: {stats['M_nec_viol']}; "
          f"feasible but violating G1: {stats['G1_nec_viol']}; violating G2: {stats['G2_nec_viol']}; "
          f"(M and G2) hold at {stats['all_hold']} points, of which infeasible: {stats['all_suff_fail']}; {time.time()-t0:.0f}s")
    for e in examples: print("   (M,G2) hold but infeasible: a", e[0], "sigma", e[1], "tau", e[2])
