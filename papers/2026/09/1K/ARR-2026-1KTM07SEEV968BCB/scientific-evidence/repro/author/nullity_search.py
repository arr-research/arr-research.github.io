"""nullity_search.py -- numerical search for large kernels of Weyl combinations with prescribed support.

Alternating projections between  V_S = span{W_g : g in S}  and the variety of matrices of rank <= d - k:
   C -> best rank-(d-k) approximation (SVD truncation) -> orthogonal projection onto V_S (Weyl coefficients
   c_g = Tr(W_g^* C)/d) -> renormalise.  Residual reported: sigma_{d-k+1}(C)/sigma_1(C) at the final iterate,
   with the minimal |c_g|/max|c_g| (a residual < 1e-9 with all coefficients bounded away from 0 is a
   numerical witness of nullity >= k on the full support; a residual < 1e-9 with a vanishing coefficient is
   a witness on a sub-support only).

Support generators (d = p^k):
   random    : uniformly random l-subsets of (Z/d)^2
   coset     : l-subsets of a coset of the p-torsion subgroup T = p^{k-1}(Z/d)^2 (all W_g commute when k>=2)
   blocked   : g0 plus points of g0+T covering all p+1 directions mod p, plus random other points
               (these are the supports where the first-order pigeonhole cannot be guaranteed)
   collinear : l points on a line through the origin (sanity: should reach Omega_k(l) only for lines of
               'p-adic' type; reported for comparison)
usage: python nullity_search.py d l k_target mode nsupports restarts iters [seed]
"""
import sys, random, time
import numpy as np

def factor_pk(d):
    p = 2
    while d % p: p += 1
    k = 0; dd = d
    while dd % p == 0: dd //= p; k += 1
    return p, k, dd  # dd == 1 iff prime power

def weyl_basis(d, S):
    omega = np.exp(2j * np.pi / d)
    Ws = []
    for (a, b) in S:
        W = np.zeros((d, d), dtype=complex)
        for j in range(d):
            W[(j + a) % d, j] = omega ** (b * j % d)
        Ws.append(W)
    return np.array(Ws)

def search(d, S, k, restarts, iters, rng):
    Ws = weyl_basis(d, S)
    Wconj = Ws.conj()
    ell = len(S)
    best = (np.inf, None, None)
    for r in range(restarts):
        c = rng.normal(size=ell) + 1j * rng.normal(size=ell)
        c /= np.linalg.norm(c)
        for it in range(iters):
            C = np.tensordot(c, Ws, axes=(0, 0))
            U, s, Vh = np.linalg.svd(C)
            s2 = s.copy(); s2[d - k:] = 0
            Cr = (U * s2) @ Vh
            # projection onto V_S: c_g = Tr(W_g^* Cr)/d = sum_{ij} conj(W_g)_{ij} (Cr)_{ij} / d
            c = np.einsum('gij,ij->g', Wconj, Cr) / d
            nc = np.linalg.norm(c)
            if nc < 1e-14: break
            c /= nc
        C = np.tensordot(c, Ws, axes=(0, 0))
        s = np.linalg.svd(C, compute_uv=False)
        res = s[d - k] / s[0]
        if res < best[0]:
            best = (res, c.copy(), np.min(np.abs(c)) / np.max(np.abs(c)))
        if res < 1e-11 and best[2] > 1e-3:
            break
    return best

def gen_support(d, ell, mode, rng, p, k):
    labels = [(a, b) for a in range(d) for b in range(d)]
    if mode == "random":
        return rng.sample(labels, ell)
    if mode == "coset":
        g0 = rng.choice(labels)
        T = [((g0[0] + a * p**(k - 1)) % d, (g0[1] + b * p**(k - 1)) % d) for a in range(p) for b in range(p)]
        return rng.sample(T, min(ell, len(T)))
    if mode == "blocked":
        g0 = (0, 0)
        # one point of T per direction mod p: (1,0),(s,1) for s in F_p  scaled by p^{k-1}
        dirs = [(1, 0)] + [(s, 1) for s in range(p)]
        pts = [((u * p**(k - 1)) % d, (v * p**(k - 1)) % d) for (u, v) in dirs]
        pts = [pt for pt in pts if pt != g0]
        S = [g0] + pts
        rest = [g for g in labels if g not in S]
        if ell < len(S):
            return S[:ell]
        S += rng.sample(rest, ell - len(S))
        return S
    if mode == "collinear":
        u = rng.choice([g for g in labels if g != (0, 0)])
        pts = list({((t * u[0]) % d, (t * u[1]) % d) for t in range(d)})
        return rng.sample(pts, min(ell, len(pts)))
    raise ValueError(mode)

if __name__ == "__main__":
    d, ell, ktar, mode, nsup, restarts, iters = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])
    seed = int(sys.argv[8]) if len(sys.argv) > 8 else 0
    p, k, rest = factor_pk(d)
    rng = random.Random(seed); nrng = np.random.default_rng(seed)
    t0 = time.time()
    found = 0; best_overall = (np.inf, None, None, None)
    for i in range(nsup):
        S = gen_support(d, ell, mode, rng, p, k)
        res, c, minc = search(d, S, ktar, restarts, iters, nrng)
        if res < best_overall[0]:
            best_overall = (res, minc, S, c)
        if res < 1e-9 and minc > 1e-3:
            found += 1
            print(f"  WITNESS nullity>={ktar}: S={S}, residual={res:.2e}, min|c|/max|c|={minc:.3f}")
            print("     c =", np.array2string(c, precision=6))
    res, minc, S, c = best_overall
    print(f"d={d} l={ell} target nullity={ktar} mode={mode}: supports={nsup}, restarts={restarts}, iters={iters}; "
          f"full-support witnesses={found}; best residual={res:.3e} (min|c|/max|c|={minc:.3f}) at S={S}   [{time.time()-t0:.0f}s]")
