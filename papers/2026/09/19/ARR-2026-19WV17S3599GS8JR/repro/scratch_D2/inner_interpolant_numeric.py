"""Numerical construction of a rational inner interpolant of McMillan degree exactly delta_Gr.

Pipeline (report, Theorem 1 upper bound):
  exact minimal-basis witness M (N x k polynomial, column degrees e_j, Q_i M(zeta_i)=0, rank k at nodes)
  -> R = M^# M (Laurent, >0 on T) -> outer factor H (matrix Fejer-Riesz, Wilson-Newton iteration)
  -> F0 = M H^{-1} (inner column) -> Taylor coefficients -> block Hankel rank = McMillan degree
  -> ERA minimal realization -> observability-Gramian scaling makes [A B; C D] an isometry
  -> unitary completion [A B B'; C D D'] -> square inner S of the same degree
  -> checks: S unitary on T, wind(det S) = degree, S(zeta_i) e_[1..k] spans Y_i.
Also: numeric 52B6 detector-rank bound Delta for k=2, N=4 via the Klein-quadric conic.
"""
import sys, time, itertools
import numpy as np, scipy.linalg as sla
sys.path.insert(0, '.')
import grassmann_degree_exact as G
from sympy import Matrix, Poly, symbols, I, zeros, Rational
z = G.z
np.set_printoptions(precision=3, suppress=True, linewidth=150)


def sym_poly_matrix_to_coeffs(F, N, k):
    degs = []
    for a in range(N):
        for j in range(k):
            e = F[a, j].expand()
            degs.append(Poly(e, z).degree() if e != 0 else 0)
    emax = max(degs)
    Ms = [np.zeros((N, k), complex) for _ in range(emax + 1)]
    for a in range(N):
        for j in range(k):
            e = F[a, j].expand()
            if e == 0:
                continue
            for (s,), c in Poly(e, z).terms():
                Ms[s][a, j] = complex(c)
    return Ms


def laurent_R(Ms):
    m = len(Ms) - 1
    R = {}
    for t in range(-m, m + 1):
        R[t] = sum(Ms[s].conj().T @ Ms[s + t] for s in range(m + 1) if 0 <= s + t <= m)
    return R, m


def eval_laurent(R, theta):
    return sum(R[t][None] * np.exp(1j * t * theta)[:, None, None] for t in R)


def wilson_factor(R, m, k, Nf=4096, iters=60, tol=1e-14):
    """outer H (polynomial, degree <= m) with H^# H = R on T; H(0) invertible.
    Wilson (1972) Newton iteration: H <- [ (I + Psi_0)/2 + sum_{t>=1} Psi_t z^t ] H,  Psi = H^{-*} R H^{-1}."""
    theta = 2 * np.pi * np.arange(Nf) / Nf
    Rg = eval_laurent(R, theta)
    H = np.tile(np.linalg.cholesky(R[0]).conj().T, (Nf, 1, 1))   # R0 = H0^* H0
    err = None
    for it in range(iters):
        Hinv = np.linalg.inv(H)
        Psi = np.einsum('nij,njk,nkl->nil', Hinv.conj().transpose(0, 2, 1), Rg, Hinv)
        C = np.fft.fft(Psi, axis=0) / Nf         # Psi(theta) = sum_t Psi_t e^{i t theta}; C[t] = Psi_t
        T = np.zeros_like(Psi)
        T += (np.eye(k) + C[0])[None] / 2
        ph = np.exp(1j * theta)
        acc = np.zeros_like(Psi)
        # Horner-like accumulation of sum_{t=1}^{Nf/2-1} C[t] e^{i t theta}
        for t in range(Nf // 2 - 1, 0, -1):
            acc = (acc + C[t][None]) * ph[:, None, None]
        T += acc
        H = np.einsum('nij,njk->nik', T, H)
        err = np.max(np.abs(T - np.eye(k)[None]))
        if err < tol:
            break
    Hc = np.fft.fft(H, axis=0) / Nf
    tail = np.max(np.abs(Hc[m + 1:Nf - m]))
    Hs = [Hc[t] for t in range(m + 1)]
    return Hs, it + 1, err, tail


def poly_eval(Ms, zs):
    return sum(M[None] * (zs ** s)[:, None, None] for s, M in enumerate(Ms))


def taylor_F0(Ms, Hs, T):
    """F0 = M H^{-1}: F_t = (M_t - sum_{s<t} F_s H_{t-s}) H_0^{-1}"""
    N, k = Ms[0].shape
    H0inv = np.linalg.inv(Hs[0])
    F = []
    for t in range(T):
        acc = Ms[t].copy() if t < len(Ms) else np.zeros((N, k), complex)
        for s in range(max(0, t - len(Hs) + 1), t):
            acc -= F[s] @ Hs[t - s]
        F.append(acc @ H0inv)
    return F


def hankel_rank(Fc, q, tol=1e-9):
    Hk = np.block([[Fc[s + t + 1] for t in range(q)] for s in range(q)])
    sv = np.linalg.svd(Hk, compute_uv=False)
    n = int(np.sum(sv > tol * sv[0]))
    return n, sv, Hk


def era_realization(Fc, q, n):
    N, k = Fc[0].shape
    Hk = np.block([[Fc[s + t + 1] for t in range(q)] for s in range(q)])
    U, s, Vh = np.linalg.svd(Hk)
    O = U[:, :n] * np.sqrt(s[:n])
    Ct = (np.sqrt(s[:n])[:, None]) * Vh[:n]
    A = np.linalg.pinv(O[:-N]) @ O[N:]
    B = Ct[:, :k]
    C = O[:N]
    D = Fc[0]
    return A, B, C, D


def tf(A, B, C, D, zs):
    n = A.shape[0]
    return np.array([D + zz * C @ np.linalg.solve(np.eye(n) - zz * A, B) for zz in zs])


def subspace_dist(W1, W2):
    P1 = W1 @ np.linalg.pinv(W1)
    P2 = W2 @ np.linalg.pinv(W2)
    return np.linalg.norm(P1 - P2, 2)


def winding(vals):
    ang = np.unwrap(np.angle(np.concatenate([vals, vals[:1]])))
    return (ang[-1] - ang[0]) / (2 * np.pi)


def detector_bound_plucker(Ws_np):
    """52B6 Theorem 5.2 statistic Delta for k=2, N=4, one node per target:
    Delta = max over admissible D (2x4, rank(D W_i)=2 for some i) of sum_i (2 - rank(D W_i)).
    Cauchy-Binet: det(D W_i) = sum_I det(D_{:,I}) det(W_i[I,:]) is LINEAR in the Plucker vector of D.
    Rank pattern (1,...,1,2): p in |J| hyperplanes cap Klein quadric; a rank-0 node forces D ~ Q_j."""
    L = len(Ws_np)
    pairs = list(itertools.combinations(range(4), 2))

    def plucker(W):   # W 4x2 -> minors det W[I,:]
        return np.array([np.linalg.det(W[list(p), :]) for p in pairs])

    def decompose(p):  # Plucker vector p_I = det(D_{:,I}) -> a 2x4 D (rows span the 2-plane)
        # For a decomposable p = a^b (a,b in C^4 as row vectors), the antisymmetric matrix
        # Pm[a,b] = p_{ab} equals a^T b - b^T a, whose column space is span(a,b).
        Pm = np.zeros((4, 4), complex)
        for (a, b), v in zip(pairs, p):
            Pm[a, b] = v
            Pm[b, a] = -v
        U, s, Vh = np.linalg.svd(Pm)
        return U[:, :2].T   # rows spanning column space (transpose, not conjugate)

    def ranks(D):
        return [np.linalg.matrix_rank(D @ W, tol=1e-8) for W in Ws_np]

    def q(p):
        return p[0] * p[5] - p[1] * p[4] + p[2] * p[3]

    best, wit = 0, None
    for j in range(L):
        Q = sla.null_space(Ws_np[j].conj().T).conj().T   # annihilator rows
        r = ranks(Q)
        if max(r) == 2:
            s = sum(2 - x for x in r)
            if s > best:
                best, wit = s, ('annihilator', j, r)
    Ps = [plucker(W) for W in Ws_np]
    rng = np.random.default_rng(0)
    for size in range(L - 1, 0, -1):
        for J in itertools.combinations(range(L), size):
            A = np.array([Ps[i] for i in J])
            ns = sla.null_space(A)
            if ns.shape[1] == 0:
                continue
            found = None
            for trial in range(20):
                u = ns @ rng.standard_normal(ns.shape[1])
                v = ns @ rng.standard_normal(ns.shape[1])
                ts = np.array([0, 1, -1])
                vals = np.array([q(u + t * v) for t in ts])
                c2 = (vals[1] + vals[2] - 2 * vals[0]) / 2
                c1 = (vals[1] - vals[2]) / 2
                c0 = vals[0]
                roots = np.roots([c2, c1, c0]) if abs(c2) > 1e-14 else np.array([-c0 / c1])
                for t in roots:
                    p = u + t * v
                    if abs(q(p)) < 1e-9 * np.linalg.norm(p) ** 2:
                        D = decompose(p)
                        # sanity: Plucker of D proportional to p
                        pD = plucker(D.T)
                        if np.linalg.norm(np.cross(np.r_[pD, 0][:3], np.r_[p, 0][:3])) > 1e-6 * np.linalg.norm(p) * np.linalg.norm(pD):
                            pass
                        r = ranks(D)
                        if max(r) == 2:
                            found = (p, D, r)
                            break
                if found is not None:
                    break
            if found is not None:
                p, D, r = found
                s = sum(2 - x for x in r)
                if s > best:
                    best, wit = s, ('pattern', J, r)
        if best >= size + 1:
            break
    return best, wit


def run_instance(name, N, k, zetas, Ws, Qs, F_witness=None, q_hankel=60, T=400):
    t0 = time.time()
    L = len(zetas)
    zs_nodes = np.array([complex(zt) for zt in zetas])
    Ws_np = [np.array(W.tolist(), dtype=complex) for W in Ws]
    print(f"=== {name}: N={N} k={k} L={L}")
    if F_witness is None:
        total, (e1, e2), V1, V2, table = G.delta_gr_k2(N, Qs, zetas, Ws, verbose=False)
        F_witness = G.random_pair(V1, V2, N, e1, e2, seed=7)
        G.check_data(F_witness, Qs, zetas, Ws, k)
        fd, g = G.forney_degree(F_witness, N, k)
        print(f"  exact: delta_Gr = {total}, column degrees {(e1, e2)}, Forney degree of witness {fd}, gcd {g.as_expr()}")
        delta = total
    else:
        G.check_data(F_witness, Qs, zetas, Ws, k)
        fd, g = G.forney_degree(F_witness, N, k)
        delta = fd
        print(f"  witness Forney degree {fd} (= delta_Gr for this data), gcd of minors {g.as_expr()}")
    Ms = sym_poly_matrix_to_coeffs(F_witness, N, k)
    sc = max(np.abs(M).max() for M in Ms)
    Ms = [M / sc for M in Ms]
    coldeg = [max(s for s, M in enumerate(Ms) if np.abs(M[:, j]).max() > 0) for j in range(k)]
    print(f"  witness column degrees {coldeg}, sum {sum(coldeg)}")
    R, m = laurent_R(Ms)
    theta = np.linspace(0, 2 * np.pi, 2001)[:-1]
    zs = np.exp(1j * theta)
    Rg = eval_laurent(R, theta)
    print(f"  min eig of R on T: {min(np.linalg.eigvalsh(Rg[i]).min() for i in range(len(theta))):.3e}  (must be > 0)")
    Hs, its, err, tail = wilson_factor(R, m, k)
    Hg = poly_eval(Hs, zs)
    fr_err = np.max(np.abs(np.einsum('nji,njk->nik', Hg.conj(), Hg) - Rg))
    detH = np.array([np.linalg.det(Hg[i]) for i in range(len(zs))])
    dc = np.fft.fft(detH) / len(detH)
    coeffs = dc[:k * m + 1]
    lead = k * m
    while lead > 0 and abs(coeffs[lead]) < 1e-9 * np.abs(coeffs).max():
        lead -= 1
    roots = np.roots(coeffs[:lead + 1][::-1]) if lead > 0 else np.array([])
    print(f"  Wilson iterations {its}, last step {err:.1e}, polynomial tail {tail:.1e}, |H^#H - R|_max {fr_err:.1e}")
    minroot = np.abs(roots).min() if lead > 0 else float('inf')
    print(f"  deg det H = {lead} (finite poles of F0), min |zero of det H| = {minroot:.4f} (must be > 1)")
    Fc = taylor_F0(Ms, Hs, T)
    print(f"  Taylor decay: |F_{T-1}| = {np.abs(Fc[-1]).max():.1e}")
    n, sv, Hk = hankel_rank(Fc, q_hankel)
    print(f"  block-Hankel singular values (first {delta+3}): {sv[:delta+3]}")
    print(f"  McMillan degree of F0 (Hankel rank) = {n}   [delta_Gr = {delta}, sum of column degrees = {sum(coldeg)}, k*max e = {k*m}]")
    print(f"  pole order at infinity = {n - lead}")
    F0g = poly_eval(Ms, zs) @ np.linalg.inv(Hg)
    inner_err = np.max(np.abs(np.einsum('nji,njk->nik', F0g.conj(), F0g) - np.eye(k)))
    print(f"  |F0^* F0 - I| on T: {inner_err:.1e}")
    A, B, C, D = era_realization(Fc, q_hankel, n)
    real_err = np.max(np.abs(tf(A, B, C, D, zs) - F0g))
    print(f"  ERA realization (n={n}) reproduces F0 on T to {real_err:.1e}; spectral radius of A = {np.abs(np.linalg.eigvals(A)).max():.4f}")
    Qo = sla.solve_discrete_lyapunov(A.conj().T, C.conj().T @ C)
    Tm = sla.sqrtm(Qo)
    Ti = np.linalg.inv(Tm)
    A2, B2, C2 = Tm @ A @ Ti, Tm @ B, C @ Ti
    U0 = np.block([[A2, B2], [C2, D]])
    iso_err = np.max(np.abs(U0.conj().T @ U0 - np.eye(n + k)))
    print(f"  after observability-Gramian scaling, |[A B;C D]^*[A B;C D] - I| = {iso_err:.1e}  (isometric realization)")
    comp = sla.null_space(U0.conj().T)          # (n+N) x (N-k)
    Ufull = np.hstack([U0, comp])
    print(f"  unitary completion: |U^*U - I| = {np.max(np.abs(Ufull.conj().T @ Ufull - np.eye(n + N))):.1e}")
    Bf = np.hstack([B2, comp[:n]])
    Df = np.hstack([D, comp[n:]])
    Sg = tf(A2, Bf, C2, Df, zs)
    unit_err = np.max(np.abs(np.einsum('nji,njk->nik', Sg.conj(), Sg) - np.eye(N)))
    detS = np.array([np.linalg.det(Sg[i]) for i in range(len(zs))])
    wnd = winding(detS)
    Sc = [Df] + [C2 @ np.linalg.matrix_power(A2, t - 1) @ Bf for t in range(1, T)]
    nS, svS, _ = hankel_rank(Sc, q_hankel)
    print(f"  square inner S (N x N): |S^*S - I| on T = {unit_err:.1e}, wind(det S) = {wnd:.6f}, Hankel rank = {nS}")
    Snodes = tf(A2, Bf, C2, Df, zs_nodes)
    dists = [subspace_dist(Snodes[i][:, :k], Ws_np[i]) for i in range(L)]
    print(f"  subspace distances dist(S(zeta_i) ran X, Y_i): {np.array(dists)}")
    ok = (n == delta) and (nS == delta) and abs(wnd - delta) < 1e-6 and max(dists) < 1e-9 and unit_err < 1e-9
    print(f"  VERDICT: deg S = delta_Gr = {delta} and all interpolation/unitarity checks < 1e-9: {ok}")
    if N == 4 and k == 2:
        db, wit = detector_bound_plucker(Ws_np)
        print(f"  52B6 detector-rank bound Delta = {db} (witness {wit}); span bound r-k = {G.span_dim(Ws)-k}; universal k(L-1) = {k*(L-1)}; delta_Gr = {delta}")
    print(f"  time {time.time()-t0:.1f}s")
    sys.stdout.flush()
    return ok


if __name__ == '__main__':
    results = {}
    for seed in [1, 2]:
        zetas, Ws, Qs = G.instance_random(4, 2, 4, seed)
        results[f'random{seed}'] = run_instance(f"random seed {seed}", 4, 2, zetas, Ws, Qs)
    zetas, Ws, Qs = G.instance_random(4, 2, 4, 1)
    Ws5 = [Matrix.vstack(W, zeros(1, 2)) for W in Ws]
    Qs5 = [G.left_annihilator(W) for W in Ws5]
    results['embedded5'] = run_instance("random seed 1 embedded in C^5", 5, 2, zetas, Ws5, Qs5)
    zetas, Ws, Qs, P0 = G.instance_from_curve(4, 2, 4, (1, 2), seed=5)
    results['curve12'] = run_instance("structured (1,2)-curve data, L=4", 4, 2, zetas, Ws, Qs)
    Fb = Matrix.hstack(P0[:, 0], (z - Rational(1, 2)) * P0[:, 1])
    results['curve12_basepoint'] = run_instance("same data, non-minimal witness with base point z=1/2 (col degrees (1,3))", 4, 2, zetas, Ws, Qs, F_witness=Fb)
    for L in [5, 6]:
        zetas, Ws, Qs = G.instance_random(4, 2, L, 11 + L)
        results[f'genericL{L}'] = run_instance(f"generic k=2 N=4 L={L}", 4, 2, zetas, Ws, Qs)
    print("SUMMARY:", results)
