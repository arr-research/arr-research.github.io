"""Independent numerical check that no inner interpolant of degree < delta_Gr exists (evidence, not proof),
by direct nonconvex search over ALL rational inner N x N functions of degree d written as a
Blaschke-Potapov product  S(z) = U prod_q (I + (b_{a_q}(z) - 1) u_q u_q^*),  |a_q| < 1, |u_q| = 1.
Objective: sum_i || (I - P_{Y_i}) S(zeta_i) X ||_F^2  (zero iff S(zeta_i) ran X = Y_i for all i).
Many random restarts of Levenberg-Marquardt; the best value found at d = delta_Gr - 1 is compared
with the value at d = delta_Gr (which must reach ~0).
The data are the same exact instances as in review_exact_delta.py (seeds 101 for L=3, 404 for L=4).
"""
import sys, time
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0, '.')
import review_exact_delta as R

rng_global = np.random.default_rng(2026)


def unpack(theta, N, d):
    idx = 0
    # unitary U via Cayley transform of a Hermitian matrix: U = (I + iH)(I - iH)^{-1}
    Hr = theta[idx:idx + N * N].reshape(N, N); idx += N * N
    Hh = (Hr + Hr.T) / 2 + 1j * (np.triu(Hr, 1) - np.triu(Hr, 1).T)
    U = np.linalg.solve(np.eye(N) - 1j * Hh, np.eye(N) + 1j * Hh)
    facs = []
    for q in range(d):
        ar, ai = theta[idx], theta[idx + 1]; idx += 2
        rho = np.tanh(np.hypot(ar, ai)) * 0.999999
        ang = np.arctan2(ai, ar)
        a = rho * np.exp(1j * ang)
        u = theta[idx:idx + N] + 1j * theta[idx + N:idx + 2 * N]; idx += 2 * N
        u = u / (np.linalg.norm(u) + 1e-300)
        facs.append((a, u))
    return U, facs


def S_eval(U, facs, zeta):
    N = U.shape[0]
    S = U.copy()
    for a, u in facs:
        b = (zeta - a) / (1 - np.conj(a) * zeta)
        S = S @ (np.eye(N) + (b - 1) * np.outer(u, u.conj()))
    return S


def residuals(theta, N, d, zetas, X, Pperp):
    U, facs = unpack(theta, N, d)
    out = []
    for zt, Pp in zip(zetas, Pperp):
        Rm = Pp @ S_eval(U, facs, zt) @ X
        out.append(Rm.real.ravel()); out.append(Rm.imag.ravel())
    return np.concatenate(out)


def search(N, k, d, zetas, Ws, restarts=150, seed=0):
    rng = np.random.default_rng(seed)
    X = np.eye(N)[:, :k].astype(complex)
    Pperp = []
    for W in Ws:
        Qm, _ = np.linalg.qr(W)
        Pperp.append(np.eye(N) - Qm @ Qm.conj().T)
    nparam = N * N + d * (2 + 2 * N)
    best = np.inf
    t0 = time.time()
    for r in range(restarts):
        th0 = rng.standard_normal(nparam)
        res = least_squares(residuals, th0, args=(N, d, zetas, X, Pperp), method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
        val = np.sum(res.fun ** 2)
        if val < best:
            best = val
    return best, time.time() - t0


if __name__ == '__main__':
    for (L, seed, delta) in [(3, 101, 2), (4, 404, 4)]:
        Ws_sym = R.random_frames(4, 2, L, seed)
        Ws = [np.array(W.tolist(), dtype=complex) for W in Ws_sym]
        zetas = [complex(zt) for zt in R.NODES[:L]]
        print(f"=== instance L={L} seed {seed} (exact delta_Gr = {delta})")
        for d in range(max(0, delta - 2), delta + 1):
            best, dt = search(4, 2, d, zetas, Ws, restarts=(120 if d < delta else 40), seed=d)
            print(f"  degree d={d}: best objective over restarts = {best:.3e}   ({dt:.0f}s)")
            sys.stdout.flush()
