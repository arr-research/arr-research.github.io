# s3: d = 3, N = 5 equal-trace frames: global optimisation of gamma = inf_k g_k over the exact feasible family.
# Naimark complement (exp4): 5 unit Bloch vectors n_i with sum n_i = 0 exactly; |<x_i,x_j>|^2 = (2/9)(1 + n_i.n_j).
# Exact parametrisation (no penalty): n1,n2,n3 free on S^2 (6 angles), s = n1+n2+n3 (need |s|<=2),
# n4 = -s/2 + v, n5 = -s/2 - v with v in s^perp, |v|^2 = 1 - |s|^2/4, direction angle psi.  7 parameters, SO(3) redundancy.
# g_k = (9/25) [5 + 2 sum_{i<j} Q_{k,3}(t_ij)],  Q_{k,3}(t) = P_k^{(1,0)}(2t-1)/(k+1) by forward three-term recurrence (float64).
import numpy as np, sys, time, json
from scipy.optimize import differential_evolution, minimize
K = 300
IDX = np.triu_indices(5, 1)

def Q3_all(tvals, K):
    """Q_{k,3}(t) for k=0..K, tvals array. Recurrence for P_n^{(1,0)}(x)."""
    x = 2.0 * tvals - 1.0
    a, b = 1, 0
    P = np.empty((K + 1, len(tvals)))
    P[0] = 1.0; P[1] = (a + 1) + (a + b + 2) / 2.0 * (x - 1)
    for n in range(1, K):
        c1 = 2 * (n + 1) * (n + a + b + 1) * (2 * n + a + b)
        c2 = (2 * n + a + b + 1) * (a * a - b * b)
        c3 = (2 * n + a + b) * (2 * n + a + b + 1) * (2 * n + a + b + 2)
        c4 = 2 * (n + a) * (n + b) * (2 * n + a + b + 2)
        P[n + 1] = ((c2 + c3 * x) * P[n] - c4 * P[n - 1]) / c1
    return P / (np.arange(K + 1)[:, None] + 1.0)

def bloch(p):
    th = p[0:6:2]; ph = p[1:6:2]; psi = p[6]
    n = np.stack([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)], 1)
    s = n.sum(0); s2 = s @ s
    if s2 > 4.0:
        return None
    ax = np.eye(3)[np.argmin(np.abs(s))]
    e = np.cross(s, ax); ne = np.linalg.norm(e)
    if ne < 1e-14:
        e = np.array([1.0, 0, 0]); ne = 1.0
    e /= ne; f = np.cross(s, e); nf = np.linalg.norm(f)
    f = f / nf if nf > 1e-14 else np.cross(e, np.array([0, 0, 1.0]))
    rho = np.sqrt(max(1.0 - s2 / 4.0, 0.0))
    v = rho * (np.cos(psi) * e + np.sin(psi) * f)
    return np.vstack([n, -s / 2 + v, -s / 2 - v])

def spectrum(n, K=K):
    G = n @ n.T
    tv = (2.0 / 9.0) * (1.0 + G[IDX])
    Q = Q3_all(tv, K)
    return (9.0 / 25.0) * (5.0 + 2.0 * Q.sum(1))     # g_k, k = 0..K

def gamma(p):
    n = bloch(p)
    if n is None:
        return 1e3
    g = spectrum(n)
    return -g[2:].min()

if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    bounds = [(0, np.pi), (0, 2 * np.pi)] * 3 + [(0, 2 * np.pi)]
    t0 = time.time()
    res = differential_evolution(gamma, bounds, seed=seed, popsize=40, maxiter=3000, tol=1e-12, mutation=(0.5, 1.0),
                                 recombination=0.9, polish=False, init='sobol', updating='deferred', workers=1)
    p = res.x; best = -res.fun
    print(f"seed={seed}: DE best gamma = {best:.10f} after {res.nit} gens, {time.time()-t0:.0f}s", flush=True)
    # local polish: Nelder-Mead then Powell, a few rounds
    for it in range(4):
        r = minimize(gamma, p, method='Nelder-Mead', options={'maxiter': 40000, 'xatol': 1e-13, 'fatol': 1e-15, 'adaptive': True})
        p = r.x
        r = minimize(gamma, p, method='Powell', options={'maxiter': 40000, 'xtol': 1e-13, 'ftol': 1e-15})
        p = r.x
    best = -gamma(p)
    n = bloch(p); g = spectrum(n, 2000)
    order = np.argsort(g[2:])[:8] + 2
    print(f"seed={seed}: polished gamma = {best:.12f}; |sum n| = {np.linalg.norm(n.sum(0)):.1e}; runtime {time.time()-t0:.0f}s")
    print("  smallest g_k (k, g_k):", [(int(k), round(float(g[k]), 10)) for k in order])
    print("  limit 9/5 = 1.8; ONB 1.5; N=4 simplex 77/45 =", 77 / 45)
    G = n @ n.T
    np.set_printoptions(precision=8, suppress=True, linewidth=150)
    print("  Bloch Gram n_i.n_j =\n", G)
    print("  overlaps t_ij = (2/9)(1+n_i.n_j) =\n", (2 / 9) * (1 + G))
    json.dump({'seed': seed, 'gamma': best, 'p': p.tolist(), 'n': n.tolist(), 'G': G.tolist(),
               'active': [(int(k), float(g[k])) for k in order]}, open(f's3_best_seed{seed}.json', 'w'), indent=1)
