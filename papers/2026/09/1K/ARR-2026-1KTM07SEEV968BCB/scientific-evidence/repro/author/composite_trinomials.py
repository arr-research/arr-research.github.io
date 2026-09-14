"""composite_trinomials.py -- exact maximal nullity of Weyl combinations with s_W <= 2 and s_W = 3
in cyclic dimension d, by the sector formula of ARR-2026-0WESHW4YMM9FG8EK (Theorem 2):
  D = cI + aU + bV (after right-multiplying by a Weyl adjoint), U = W_u, V = W_v, UV = zeta VU, q = ord(zeta),
  joint eigenvalue pairs (s,t) of (U^q, V^q) have common multiplicity m, and
  dim ker D = m * #{(s,t): a^q s + b^q t = (-1)^q c^q}.
  For abc != 0: two pairs can be killed iff there are two joint pairs (s1,t1),(s2,t2) with s1!=s2, t1!=t2,
  s1 t2 != s2 t1  (then nullity 2m; otherwise nullity m is the maximum, always attainable).
  For c = 0 (binomial) the maximum is d / ord(v - u) -> max over labels = d / (smallest prime factor of d).
The joint spectrum is computed numerically (commuting unitaries U^q, V^q; joint eigenvectors from a generic
combination), multiplicities read off exactly (integers), and the claimed maximum is re-verified by
building the matrix with explicit coefficients and computing its SVD nullity.
usage: python composite_trinomials.py d1 d2 ...
"""
import sys, itertools
import numpy as np
from math import gcd

def weyl(d, a, b, omega):
    W = np.zeros((d, d), dtype=complex)
    for j in range(d):
        W[(j + a) % d, j] = omega ** (b * j % d)
    return W

def order(x, d):
    g = gcd(gcd(x[0], x[1]), d)
    return d // g

def joint_pairs(A, B):
    """A, B commuting unitaries. return list of (s, t, mult)"""
    d = A.shape[0]
    rng = np.random.default_rng(0)
    al, be = rng.normal(size=2) + 1j * rng.normal(size=2)
    M = al * A + be * B
    w, V = np.linalg.eig(M)
    pairs = []
    for i in range(d):
        v = V[:, i]
        s = (v.conj() @ A @ v) / (v.conj() @ v); t = (v.conj() @ B @ v) / (v.conj() @ v)
        pairs.append((s, t))
    # group
    groups = []
    for s, t in pairs:
        for g in groups:
            if abs(g[0] - s) < 1e-6 and abs(g[1] - t) < 1e-6:
                g[2] += 1; break
        else:
            groups.append([s, t, 1])
    return groups

def nullity(M):
    sv = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(sv < 1e-8 * max(sv[0], 1.0)))

def analyse(d):
    omega = np.exp(2j * np.pi / d)
    labels = [(a, b) for a in range(d) for b in range(d) if (a, b) != (0, 0)]
    # binomials
    best2 = max(d // order(u, d) for u in labels)
    res = {"binomial_max": best2}
    best3 = 0; best3_info = None; best3_comm = 0; best3_noncomm = 0
    seen = set()
    for u, v in itertools.combinations(labels, 2):
        delta = (u[0] * v[1] - u[1] * v[0]) % d
        q = d // gcd(d, delta)
        key = (q, tuple(sorted([u, v])))
        U = weyl(d, u[0], u[1], omega); V = weyl(d, v[0], v[1], omega)
        Uq = np.linalg.matrix_power(U, q); Vq = np.linalg.matrix_power(V, q)
        groups = joint_pairs(Uq, Vq)
        mults = sorted(set(g[2] for g in groups))
        assert len(mults) == 1, (d, u, v, mults)
        assert mults[0] % q == 0
        m = mults[0] // q   # Theorem 2: each sector E_{s,t} has dimension q*m, nullity contribution m
        two = False; pair_choice = None
        for g1, g2 in itertools.combinations(groups, 2):
            s1, t1, s2, t2 = g1[0], g1[1], g2[0], g2[1]
            if abs(s1 - s2) > 1e-6 and abs(t1 - t2) > 1e-6 and abs(s1 * t2 - s2 * t1) > 1e-6:
                two = True; pair_choice = (s1, t1, s2, t2); break
        nul = 2 * m if two else m
        if nul > best3:
            # verify by explicit construction
            if two:
                s1, t1, s2, t2 = pair_choice
                A = (t2 - t1); B = (s1 - s2); Cq = (-1) ** q * (A * s1 + B * t1)
            else:
                s1, t1 = groups[0][0], groups[0][1]
                A = 1.0; B = 1.0; Cq = (-1) ** q * (A * s1 + B * t1)
            a = A ** (1 / q); b = B ** (1 / q); c = Cq ** (1 / q)
            D = c * np.eye(d) + a * U + b * V
            nv = nullity(D)
            best3 = nul; best3_info = (u, v, q, m, two, nv)
        if q == 1: best3_comm = max(best3_comm, nul)
        else: best3_noncomm = max(best3_noncomm, nul)
    res.update({"trinomial_max": best3, "trinomial_info": best3_info,
                "trinomial_max_commuting": best3_comm, "trinomial_max_noncommuting": best3_noncomm})
    return res

if __name__ == "__main__":
    for d in map(int, sys.argv[1:]):
        r = analyse(d)
        print(f"d={d}: max nullity s_W<=2 (binomial) = {r['binomial_max']};  s_W=3 genuine trinomial: max = {r['trinomial_max']} "
              f"(commuting {r['trinomial_max_commuting']}, noncommuting {r['trinomial_max_noncommuting']}); witness (u,v,q,m,two-sector,verified nullity) = {r['trinomial_info']}")
