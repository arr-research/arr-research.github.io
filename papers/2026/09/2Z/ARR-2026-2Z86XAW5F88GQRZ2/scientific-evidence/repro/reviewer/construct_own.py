"""Task (c, part 2): explicit optimizers from the block-shift chain at 20+ random points (own code end to end):
argmax form -> level layering (zero inserted if needed) -> chain LP (float, max min-slack) -> per-step inverse eigenvalue solve
(Q in SO(n) by least squares + Newton polish on the eigenvalues) -> C = sum M_t -> residuals of CC^T - C^TC - 2F and of the cost."""
import os; AUTHOR_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "author")); REVIEWER_DIR = os.path.dirname(os.path.abspath(__file__))  # repro: these replace absolute paths in the original review scripts
import sys, json, itertools, numpy as np
from scipy.optimize import linprog, least_squares
from scipy.linalg import expm, eigh
sys.path.insert(0, AUTHOR_DIR)
from horn_own import T, Hive, spec, rand_point, form_val
from chain_own import layering, with_zeros
W = AUTHOR_DIR
HORN = {n: [(I, J, K) for r in range(1, n) for (I, J, K) in T(r, n)] for n in (1, 2, 3)}

def chain_lp(layers):
    Tn = len(layers) - 1; n = [len(L) for L in layers]; nv = 3 * Tn + 1
    def var(t, k): return (t - 1) * 3 + (k - 1)
    A, ub, E, eb = [], [], [], []; bounds = [(0, None)] * (3 * Tn) + [(0, 1)]
    for t in range(1, Tn + 1):
        for k in (1, 2):
            r = np.zeros(nv); r[var(t, k)] = -1; r[var(t, k + 1)] = 1; A.append(r); ub.append(0)
        for k in range(min(n[t - 1], n[t]) + 1, 4): bounds[var(t, k)] = (0, 0)
    s1 = sorted([-x for x in layers[0]], reverse=True) + [0.0] * (3 - n[0])
    for k in range(1, 4):
        r = np.zeros(nv); r[var(1, k)] = 1; E.append(r); eb.append(s1[k - 1])
    for t in range(1, Tn):
        nt = n[t]; beta = sorted([-x for x in layers[t]], reverse=True)
        r = np.zeros(nv)
        for k in range(1, nt + 1): r[var(t + 1, k)] += 1; r[var(t, k)] -= 1
        E.append(r); eb.append(sum(beta))
        for I, J, K in HORN[nt]:
            r = np.zeros(nv)
            for k in K: r[var(t + 1, k)] += 1
            for i in I: r[var(t, i)] -= 1
            r[-1] = 1; A.append(r); ub.append(sum(beta[j - 1] for j in J))
    sT = sorted(layers[Tn], reverse=True) + [0.0] * (3 - n[Tn])
    for k in range(1, 4):
        r = np.zeros(nv); r[var(Tn, k)] = 1; E.append(r); eb.append(sT[k - 1])
    c = np.zeros(nv); c[-1] = -1
    res = linprog(c, A_ub=np.array(A), b_ub=np.array(ub), A_eq=np.array(E), b_eq=np.array(eb), bounds=bounds, method='highs',
                  options=dict(primal_feasibility_tolerance=1e-10, dual_feasibility_tolerance=1e-10))
    if res.status != 0 or res.x[-1] < -1e-9: return None
    return res.x[:-1].reshape(Tn, 3)

def skew(th, n):
    S = np.zeros((n, n)); k = 0
    for i in range(n):
        for j in range(i + 1, n): S[i, j] = th[k]; S[j, i] = -th[k]; k += 1
    return S

def solve_step(sig, D, tau, rng):
    """R = Q diag(sig) Q^T with eig(R - diag(D)) = tau (sorted desc)."""
    n = len(D); sig = np.sort(sig)[::-1]; tau = np.sort(tau)[::-1]
    if n == 1: return np.diag(sig), abs(sig[0] - D[0] - tau[0])
    p = n * (n - 1) // 2
    def res(th):
        Q = expm(skew(th, n)); return np.sort(np.linalg.eigvalsh(Q @ np.diag(sig) @ Q.T - np.diag(D)))[::-1] - tau
    best = None
    for k in range(40):
        th0 = np.zeros(p) if k == 0 else rng.uniform(-np.pi, np.pi, size=p)
        r = least_squares(res, th0, method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=2000)
        e = np.max(np.abs(res(r.x)))
        if best is None or e < best[1]: best = (r.x, e)
        if e < 1e-13: break
    Q = expm(skew(best[0], n)); return Q @ np.diag(sig) @ Q.T, best[1]

def build_C(layers, sigma, rng):
    Tn = len(layers) - 1; n = [len(L) for L in layers]; N = sum(n); off = np.cumsum([0] + n)
    C = np.zeros((N, N)); worst = 0.0; S = np.diag([-x for x in layers[0]])
    for t in range(1, Tn + 1):
        sig = np.array(sorted(list(sigma[t - 1][:min(3, n[t])]) + [0.0] * max(0, n[t] - 3), reverse=True))[:n[t]]
        D = np.array(layers[t], float)
        if t < Tn: R, e = solve_step(sig, D, np.array(sigma[t][:n[t]]), rng)
        else: R = np.diag(D); e = np.max(np.abs(np.sort(sig)[::-1] - np.sort(D)[::-1]))
        worst = max(worst, e)
        ws, Wm = eigh(S); vr, V = eigh(R)
        k = min(n[t - 1], n[t]); iw = np.argsort(ws)[::-1][:k]; iv = np.argsort(vr)[::-1][:k]
        sv = np.sqrt(2 * np.clip((ws[iw] + vr[iv]) / 2, 0, None))
        C[off[t]:off[t + 1], off[t - 1]:off[t]] = V[:, iv] @ np.diag(sv) @ Wm[:, iw].T
        S = R - np.diag(D)
    return C, worst

rng = np.random.default_rng(77); results = []
for (m, z) in ((4, 0), (4, 1), (5, 0), (5, 1), (6, 1), (7, 0), (3, 1)):
    S = [tuple(f) for f in json.load(open(f"{W}/closed_m{m}_z{0 if z == 0 else 1}.json"))]; d = m + z + 3; Hv = Hive(d)
    for i in range(4):
        a, b = rand_point(m, rng, law=i % 6); lam = spec(a, b, z)
        kap = Hv.solve(lam)['val']; vals = sorted(((form_val(f, a, b), f) for f in S), reverse=True); mx, gf = vals[0]
        base = layering(gf, m); cands = [base] + ([c for nz in range(1, min(z, 2) + 1) for c in with_zeros(base, nz)] if z else [])
        done = False
        for ch in cands:
            lay = [[(-b[i] if k == 'b' else (a[i] if k == 'a' else 0.0)) for (k, i) in L] for L in ch]
            sg = chain_lp(lay)
            if sg is None: continue
            C, e = build_C(lay, sg, rng)
            F = np.diag([x for L in lay for x in L]) / 1.0
            comm = C @ C.T - C.T @ C - 2 * F
            res_c = np.max(np.abs(comm)); cost = 0.5 * np.sum(C * C)
            results.append((m, z, res_c, abs(cost - mx), abs(kap - mx), np.linalg.matrix_rank(C, tol=1e-9), ch is base))
            print(f"m={m} z={z} pt{i}: form {gf}, chain {'base' if ch is base else 'with zero'}; step eig residual {e:.1e}; "
                  f"max|CC^T-C^TC-2F| = {res_c:.1e}; |cost - maxS| = {abs(cost-mx):.1e}; |kappa - maxS| = {abs(kap-mx):.1e}; rank C = {np.linalg.matrix_rank(C, tol=1e-9)}", flush=True)
            done = True; break
        if not done: print(f"m={m} z={z} pt{i}: NO feasible chain among candidates for form {gf}  <-- PROBLEM")
print(f"{len(results)} points constructed; max commutator residual {max(r[2] for r in results):.1e}; max cost residual {max(r[3] for r in results):.1e}")
