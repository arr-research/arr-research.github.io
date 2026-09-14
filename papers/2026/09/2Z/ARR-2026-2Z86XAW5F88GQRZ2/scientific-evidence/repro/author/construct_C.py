"""Explicit 3x3-block weighted shifts: for random points (incl. exact ties) build C with CC^T - C^TC = 2F and cost = max S.
Chain spectra from an LP over the 3x3 Horn inequalities with maximal slack (interior point of the chain polytope), then each
step R_t = Q diag(sigma) Q^T with Q in SO(n) solved by least squares on the sorted eigenvalues of R_t - D_t.
Usage: python construct_C.py m z N"""
import sys, json, time, itertools, numpy as np
from scipy.optimize import linprog, least_squares
from scipy.linalg import expm, eigh
from layering_lp import horn_ineqs
from m3_forms import spec_m3
from m3_gather import rand_m3x, LAWS
from hive_core import HiveLP


def chain_lp(layers, tol=1e-12):
    """max slack delta s.t. chain constraints with slack; returns (delta, sigma (T x 3)) or (None, None)."""
    T = len(layers) - 1; n = [len(L) for L in layers]; nv = 3 * T + 1

    def var(t, k): return (t - 1) * 3 + (k - 1)
    A_ub, b_ub, A_eq, b_eq = [], [], [], []; bounds = [(0, None)] * (3 * T) + [(0, 1)]
    for t in range(1, T + 1):
        for k in (1, 2):
            row = np.zeros(nv); row[var(t, k)] = -1; row[var(t, k + 1)] = 1; A_ub.append(row); b_ub.append(0.0)
        cap = min(n[t - 1], n[t])
        for k in range(cap + 1, 4): bounds[var(t, k)] = (0, 0)
    s1 = sorted([-x for x in layers[0]], reverse=True) + [0.0] * (3 - n[0])
    for k in range(1, 4):
        row = np.zeros(nv); row[var(1, k)] = 1; A_eq.append(row); b_eq.append(max(s1[k - 1], 0.0))
    for t in range(1, T):
        nt = n[t]; beta = sorted([-x for x in layers[t]], reverse=True)
        row = np.zeros(nv)
        for k in range(1, nt + 1): row[var(t + 1, k)] += 1; row[var(t, k)] -= 1
        A_eq.append(row); b_eq.append(sum(beta))
        for I, J, K in horn_ineqs(nt):
            row = np.zeros(nv)
            for k in K: row[var(t + 1, k)] += 1
            for i in I: row[var(t, i)] -= 1
            row[-1] = 1.0
            A_ub.append(row); b_ub.append(sum(beta[j - 1] for j in J))
    sT = sorted(layers[T], reverse=True) + [0.0] * (3 - n[T])
    for k in range(1, 4):
        row = np.zeros(nv); row[var(T, k)] = 1; A_eq.append(row); b_eq.append(max(sT[k - 1], 0.0))
    c = np.zeros(nv); c[-1] = -1
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub) + tol, A_eq=np.array(A_eq), b_eq=np.array(b_eq), bounds=bounds,
                  method='highs', options=dict(primal_feasibility_tolerance=1e-10, dual_feasibility_tolerance=1e-10))
    if res.status != 0: return None, None
    return res.x[-1], res.x[:-1].reshape(T, 3)


def skew(th, n):
    S = np.zeros((n, n)); k = 0
    for i in range(n):
        for j in range(i + 1, n): S[i, j] = th[k]; S[j, i] = -th[k]; k += 1
    return S


def _eig_res(R, D, tau):
    return np.max(np.abs(np.sort(np.linalg.eigvalsh(R - np.diag(D)))[::-1] - tau))


def solve_step(sig, D, tau, rng, tries=12):
    """Find Q in SO(n) with eig(Q diag(sig) Q^T - D) = tau (both sorted desc). n=2: closed form (affine determinant).
    n=3: (i) rank-one target (tau = (x,0,0)): closed form by the secular equation of D + x v v^T; (ii) otherwise least squares on
    the characteristic-polynomial coefficients of R - D, polished on the sorted eigenvalues; also from the S-side parametrisation
    (S' = W diag(tau) W^T, R = D + S' with spectrum sig).  The eigenvalue residual is returned."""
    n = len(D); Sg = np.diag(sig); tau = np.sort(tau)[::-1]; D = np.asarray(D, float); sig = np.sort(sig)[::-1]
    if n == 1: return Sg, abs(sig[0] - D[0] - tau[0])
    if n == 2:
        s1, s2 = sig; d1, d2 = D; target = tau[0] * tau[1]
        base = (s2 - d1) * (s1 - d2); slope = (s1 - s2) * (d1 - d2)
        x = 0.5 if abs(slope) < 1e-15 else (target - base) / slope
        x = min(1.0, max(0.0, x)); th = np.arccos(np.sqrt(x))
        Q = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]]); R = Q @ Sg @ Q.T
        return R, _eig_res(R, D, tau)
    cands = []
    # (i) rank-one target: R = D + x v v^T with spectrum sig; v_i^2 = prod_j (sig_j - d_i) / (x prod_{j != i} (d_j - d_i))
    if tau[1] <= 1e-13 and tau[0] > 1e-13 and min(abs(D[i] - D[j]) for i in range(3) for j in range(i + 1, 3)) > 1e-9:
        x = tau[0]; v2 = np.array([np.prod([sig[j] - D[i] for j in range(3)]) / (x * np.prod([D[j] - D[i] for j in range(3) if j != i])) for i in range(3)])
        if np.all(v2 > -1e-12):
            v = np.sqrt(np.clip(v2, 0, None)); R = np.diag(D) + x * np.outer(v, v); cands.append((R, _eig_res(R, D, tau)))
            if cands[-1][1] < 1e-13: return cands[-1]
    e2t = tau[0] * tau[1] + tau[0] * tau[2] + tau[1] * tau[2]; e3t = tau[0] * tau[1] * tau[2]
    def cp(A):
        e2 = A[0, 0] * A[1, 1] + A[0, 0] * A[2, 2] + A[1, 1] * A[2, 2] - A[0, 1] ** 2 - A[0, 2] ** 2 - A[1, 2] ** 2
        return np.array([e2, np.linalg.det(A)])
    def resid_R(th):
        Q = expm(skew(th, 3)); return cp(Q @ Sg @ Q.T - np.diag(D)) - np.array([e2t, e3t])
    def eres_R(th):
        Q = expm(skew(th, 3)); return np.sort(np.linalg.eigvalsh(Q @ Sg @ Q.T - np.diag(D)))[::-1] - tau
    Tg = np.diag(tau); s2t = sig[0] * sig[1] + sig[0] * sig[2] + sig[1] * sig[2]; s3t = sig[0] * sig[1] * sig[2]
    def resid_S(th):
        W = expm(skew(th, 3)); return cp(W @ Tg @ W.T + np.diag(D)) - np.array([s2t, s3t])
    def eres_S(th):
        W = expm(skew(th, 3)); return np.sort(np.linalg.eigvalsh(W @ Tg @ W.T + np.diag(D)))[::-1] - sig
    for resid, eres, side in ((resid_R, eres_R, 'R'), (resid_S, eres_S, 'S')):
        best = None
        for k in range(tries):
            th0 = rng.uniform(-np.pi, np.pi, size=3) if k else np.zeros(3)
            r = least_squares(resid, th0, method='trf', xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=300)
            r2 = least_squares(eres, r.x, method='trf', xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=200)
            th = r2.x if np.max(np.abs(r2.fun)) < np.max(np.abs(eres(r.x))) else r.x
            e = np.max(np.abs(eres(th)))
            if best is None or e < best[1]: best = (th, e)
            if e < 1e-13: break
        th = best[0]
        if side == 'R': R = expm(skew(th, 3)) @ Sg @ expm(skew(th, 3)).T
        else: W = expm(skew(th, 3)); R = W @ Tg @ W.T + np.diag(D)
        cands.append((R, _eig_res(R, D, tau)))
        if cands[-1][1] < 1e-13: break
    return min(cands, key=lambda c: c[1])


def build_C(layers, sigma, rng):
    """layers: list of lists of eigenvalues; sigma: T x 3 chain spectra. Returns C (block bidiagonal, layered basis), worst step residual."""
    T = len(layers) - 1; n = [len(L) for L in layers]; N = sum(n); off = np.cumsum([0] + n)
    C = np.zeros((N, N)); worst = 0.0
    S = np.diag([-x for x in layers[0]])
    for t in range(1, T + 1):
        sig = np.array(sorted(list(sigma[t - 1][:min(3, n[t])]) + [0.0] * max(0, n[t] - 3), reverse=True))[:n[t]]
        D = np.array(layers[t], float)
        if t < T: R, e = solve_step(sig, D, np.array(sigma[t][:n[t]]), rng)
        else: R = np.diag(D); e = np.max(np.abs(np.sort(sig)[::-1] - np.sort(D)[::-1]))
        worst = max(worst, e)
        ws, W = eigh(S); vr, V = eigh(R)
        k = min(n[t - 1], n[t]); idx_w = np.argsort(ws)[::-1][:k]; idx_v = np.argsort(vr)[::-1][:k]
        sv = np.sqrt(2 * np.clip((ws[idx_w] + vr[idx_v]) / 2, 0, None))
        Mt = V[:, idx_v] @ np.diag(sv) @ W[:, idx_w].T
        C[off[t]:off[t + 1], off[t - 1]:off[t]] = Mt
        S = R - np.diag(D)
    return C, worst


def chains_for(g, m, z):
    al = list(g[:m]); be = list(g[m:m + 2]) + [0]; w3 = max(al); la = [w3 - x for x in al]; lb = [x + w3 for x in be]
    T = max(lb); base = []
    for t in range(T, -1, -1): base.append([('b', i) for i in range(3) if lb[i] == t] + [('a', j) for j in range(m) if la[j] == t])
    cands = [base]
    if z >= 1:
        slots = [t for t in range(len(base)) if len(base[t]) < 3]
        for nz in range(1, min(z, 2) + 1):
            for combo in itertools.combinations_with_replacement(slots, nz):
                new = [list(L) for L in base]; ok = True
                for t in combo:
                    if len(new[t]) >= 3: ok = False; break
                    new[t].append(('z', 0))
                if ok: cands.append(new)
    return cands


if __name__ == "__main__":
    m, z, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); d = m + z + 3
    S_forms = [tuple(f) for f in json.load(open(f"closed_m{m}_z{0 if z == 0 else 1}.json"))]
    Sarr = np.array(S_forms, float); M = HiveLP(d); rng = np.random.default_rng(11 + m + 100 * z); t0 = time.time()
    res_hist = []; fails = []; ranks = {}; nz_used = {}; kgap = 0.0
    for i in range(N):
        law = LAWS[i % len(LAWS)] if i % 4 else 'tie'; a, b = rand_m3x(m, rng, law)
        if i % 8 == 7:   # exact ties
            k = rng.integers(1, m); a[k] = a[k - 1]; a = a / a.sum()
            if rng.random() < 0.5: b[2] = b[1]; b = b / b.sum()
        lam = spec_m3(a, b, z); kap = M.solve(lam)['val']
        vals = Sarr[:, :m] @ a + Sarr[:, m] * b[0] + Sarr[:, m + 1] * b[1]; order = np.argsort(-vals); vmax = vals[order[0]]
        kgap = max(kgap, abs(kap - vmax))
        done = False
        for gi in order:
            if vals[gi] < vmax - 1e-9: break
            for ch in chains_for(S_forms[gi], m, z):
                layers = [[(-b[k] if kind == 'b' else (a[k] if kind == 'a' else 0.0)) for kind, k in L] for L in ch]
                delta, sigma = chain_lp(layers)
                if delta is None: continue
                C, e = build_C(layers, sigma, rng)
                Fm = np.diag(np.concatenate([np.array(L) for L in layers]))
                r1 = np.max(np.abs(C @ C.T - C.T @ C - 2 * Fm)); r2 = abs(0.5 * np.sum(C * C) - vmax)
                res_hist.append((r1, r2, e)); nz = sum(1 for L in ch for x in L if x[0] == 'z'); nz_used[nz] = nz_used.get(nz, 0) + 1
                rk = int(np.linalg.matrix_rank(C, tol=1e-8)); ranks[rk] = ranks.get(rk, 0) + 1
                done = True; break
            if done: break
        if not done: fails.append((a, b))
    r1 = np.array([x[0] for x in res_hist]); r2 = np.array([x[1] for x in res_hist])
    print(f"m={m} z={z} d={d}: {N} points ({len(res_hist)} constructed, {len(fails)} failures); residual max|CC^T-C^TC-2F|: median {np.median(r1):.1e}, max {r1.max():.1e}, #>1e-9: {int((r1>1e-9).sum())}; |cost-maxS|: max {r2.max():.1e}; |kappa_LP-maxS| max {kgap:.1e}; zeros used {nz_used}; rank C {ranks}  ({time.time()-t0:.0f}s)", flush=True)
    for a, b in fails[:3]: print("   FAIL at a=", np.round(a, 5), "b=", np.round(b, 5))
