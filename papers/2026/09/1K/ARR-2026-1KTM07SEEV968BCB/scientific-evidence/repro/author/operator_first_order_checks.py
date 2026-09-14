"""operator_first_order_checks.py -- checks of the prime-power operator argument (d = p^k):

(A) Clifford conjugation identities, exactly in integer exponent arithmetic:
      p odd :  U_s = F' Q_s,  Q_s = diag(omega^{s 2^{-1} j^2}),         U_s W_(a,b) U_s^{-1} = omega^{e} X^{-(sa+b)} Z^{a}
      p = 2 :  Q_s = diag(omega_{2d}^{s j^2}),                         Q_s W_(a,b) Q_s^{-1} = omega_{2d}^{s a} omega^{s a(a-1)/2} X^a Z^{sa+b}
      V_s = F'^{-1} Q_s F' (directions (1,-s), s in pZ) checked numerically as "phase times Weyl".
    The checks are numerical (complex doubles) but the target is a discrete set (a root of unity times a
    0/1-pattern matrix), so agreement to 1e-9 identifies the identity uniquely.
(B) Random / adversarial instances with integer coefficients (some coefficient not divisible by p):
      for every primitive direction lambda (p^{k-1}(p+1) of them) compute the fibre sums mod p,
      the reduced polynomial gbar_lambda in F_p[x]/(x^d-1), its order at 1 (via Lucas matrix / direct
      expansion in y = x-1 over F_p), and check   nullity(C) <= ord_1 gbar_lambda   whenever gbar != 0,
      and   ord_1 gbar_lambda <= Omega_k(m_lambda).  Also checks the pigeonhole: some direction is
      nonzero whenever  sum_{g != g0} p^{v(g-g0)} < p^{k-1}(p+1)  for a g0 with p ∤ c_{g0}.
    Nullity of C is computed numerically (SVD, threshold 1e-8) -- exactness is not needed for an
    upper-bound check because the theorem predicts nullity <= ord; a violation would show up as a
    numerically clear small singular value pattern.  Instances with nullity > 0 are also re-verified with
    a second threshold.
usage: python operator_first_order_checks.py d ninstances
"""
import sys, itertools, random
import numpy as np
from math import comb, gcd

def factor_pk(d):
    p = 2
    while d % p: p += 1
    k = 0; dd = d
    while dd % p == 0: dd //= p; k += 1
    assert dd == 1
    return p, k

def weyl(d, a, b, omega):
    W = np.zeros((d, d), dtype=complex)
    for j in range(d):
        W[(j + a) % d, j] = omega ** (b * j % d)
    return W

def omega_k(p, k, m):
    best = 0
    for r in range(p**k):
        w = 1; rr = r
        while rr: w *= (rr % p) + 1; rr //= p
        if w <= m: best = r
    return best

def ord1_modp(coeffs, p, d):
    """coeffs: dict t -> residue mod p, t in [0,d). order at x=1 of sum c_t x^t in F_p[x] (deg<d).
    Uses Hasse derivatives: coefficient of y^i in g(1+y) is sum_t c_t binom(t,i)."""
    if all(v % p == 0 for v in coeffs.values()):
        return None
    for i in range(d):
        s = sum(v * comb(t, i) for t, v in coeffs.items()) % p
        if s: return i
    return d  # cannot happen for nonzero g of degree < d

def primitive_directions(p, k):
    d = p**k
    dirs = [(1, s % d) for s in range(d)]            # lambda(a,b) = a + s b   -> (alpha,beta)=(1,s)
    dirs += [(s % d, 1) for s in range(0, d, p)]     # beta unit normalised to 1, alpha in pZ
    assert len(dirs) == p**(k - 1) * (p + 1)
    return dirs

def check_identities(d, p, k):
    omega = np.exp(2j * np.pi / d)
    Fp = np.array([[omega ** ((j * l) % d) for l in range(d)] for j in range(d)])
    Fpinv = np.linalg.inv(Fp)
    W = {(a, b): weyl(d, a, b, omega) for a in range(d) for b in range(d)}
    nbad = 0; ncheck = 0
    if p % 2:
        inv2 = pow(2, -1, d)
        Qs = {s: np.diag([omega ** ((s * inv2 * j * j) % d) for j in range(d)]) for s in range(d)}
        for s in range(d):
            U = Fp @ Qs[s]; Ui = np.linalg.inv(U)
            for (a, b), Wab in W.items():
                lhs = U @ Wab @ Ui
                e = (-s * inv2 * a * a - a * b) % d
                rhs = (omega ** e) * W[((-(s * a + b)) % d, a)]
                ncheck += 1
                if np.abs(lhs - rhs).max() > 1e-8: nbad += 1
    else:
        om2 = np.exp(2j * np.pi / (2 * d))
        Qs = {s: np.diag([om2 ** ((s * j * j) % (2 * d)) for j in range(d)]) for s in range(d)}
        for s in range(d):
            Q = Qs[s]; Qi = np.linalg.inv(Q)
            for (a, b), Wab in W.items():
                lhs = Q @ Wab @ Qi
                rhs = (om2 ** ((s * a) % (2 * d))) * (omega ** ((s * a * (a - 1) // 2) % d)) * W[(a, (s * a + b) % d)]
                ncheck += 1
                if np.abs(lhs - rhs).max() > 1e-8: nbad += 1
        # F' conjugation
        for (a, b), Wab in W.items():
            lhs = Fp @ Wab @ Fpinv
            rhs = (omega ** ((-a * b) % d)) * W[((-b) % d, a)]
            ncheck += 1
            if np.abs(lhs - rhs).max() > 1e-8: nbad += 1
    # V_s = F'^{-1} Q_s F' for s in pZ : must be phase * W_{(a - s b, b)} (p odd: Q_s with 2^{-1}; p=2: om2 version)
    nphase_bad = 0
    for s in range(0, d, p):
        V = Fpinv @ Qs[s] @ Fp; Vi = np.linalg.inv(V)
        for (a, b), Wab in W.items():
            lhs = V @ Wab @ Vi
            tgt = W[((a - s * b) % d, b)]
            # phase = ratio on a nonzero entry
            idx = np.unravel_index(np.argmax(np.abs(tgt)), tgt.shape)
            ph = lhs[idx] / tgt[idx]
            if abs(abs(ph) - 1) > 1e-8 or np.abs(lhs - ph * tgt).max() > 1e-8: nphase_bad += 1
            # phase must be a 2d-th root of unity (d-th for odd p)
            n_root = d if p % 2 else 2 * d
            if abs(ph ** n_root - 1) > 1e-7: nphase_bad += 1
    print(f"(A) d={d}: identities checked={ncheck}, failures={nbad}; V_s (s in pZ) phase*Weyl failures={nphase_bad}")
    return nbad == 0 and nphase_bad == 0

def instance_check(d, p, k, S, coeffs, omega, verbose=False):
    """S list of labels, coeffs dict label->int (some not divisible by p). returns (nullity, mins over nonzero dirs of ord, any violation)"""
    C = sum(coeffs[g] * weyl(d, g[0], g[1], omega) for g in S)
    sv = np.linalg.svd(C, compute_uv=False)
    scale = sv[0] if sv[0] > 0 else 1.0
    nullity = int(np.sum(sv < 1e-8 * scale))
    nullity2 = int(np.sum(sv < 1e-6 * scale))
    dirs = primitive_directions(p, k)
    best = None; viol = []
    nonzero_dirs = 0
    for (al, be) in dirs:
        fib = {}
        for g in S:
            t = (al * g[0] + be * g[1]) % d
            fib[t] = (fib.get(t, 0) + coeffs[g]) % p
        fib = {t: v for t, v in fib.items() if v}
        if not fib: continue
        nonzero_dirs += 1
        o = ord1_modp(fib, p, d)
        m_lam = len(fib)
        if o > omega_k(p, k, m_lam):
            viol.append(("ord>Omega", (al, be), o, m_lam))
        if nullity > o:
            viol.append(("nullity>ord", (al, be), nullity, o))
        if best is None or o < best: best = o
    # pigeonhole predicate
    g0s = [g for g in S if coeffs[g] % p]
    pig = False
    for g0 in g0s:
        tot = 0
        for g in S:
            if g == g0: continue
            h = ((g[0] - g0[0]) % d, (g[1] - g0[1]) % d)
            v = 0
            while h[0] % p**(v + 1) == 0 and h[1] % p**(v + 1) == 0 and v + 1 <= k: v += 1
            tot += p**v
        if tot < p**(k - 1) * (p + 1): pig = True
    if pig and nonzero_dirs == 0:
        viol.append(("pigeonhole-failed",))
    return nullity, nullity2, best, nonzero_dirs, viol

if __name__ == "__main__":
    d = int(sys.argv[1]); ninst = int(sys.argv[2])
    p, k = factor_pk(d)
    omega = np.exp(2j * np.pi / d)
    okA = check_identities(d, p, k)
    rng = random.Random(1234)
    labels = [(a, b) for a in range(d) for b in range(d)]
    nviol = 0; n_nonzero = 0; n_alldirs_zero = 0; ties = 0
    for it in range(ninst):
        ell = rng.randint(2, min(d, p + 3))
        regime = it % 4
        if regime == 0:      # random support, random small integer coefficients
            S = rng.sample(labels, ell); coeffs = {g: rng.randint(-5, 5) or 1 for g in S}
        elif regime == 1:    # collinear support in Z-direction, equality family lifted
            S = [(0, (b * p**(k - 1)) % d) for b in range(min(ell, p))]
            coeffs = {g: rng.randint(1, p - 1) if p > 2 else 1 for g in S}
        elif regime == 2:    # support inside a coset of the p-torsion subgroup (all fibre sums may vanish)
            g0 = rng.choice(labels)
            T = [((g0[0] + a * p**(k - 1)) % d, (g0[1] + b * p**(k - 1)) % d) for a in range(p) for b in range(p)]
            S = rng.sample(T, min(ell, p * p)); coeffs = {g: 1 + p * rng.randint(0, 3) for g in S}
        else:                # coefficients forcing vertical fibre cancellations mod p
            S = rng.sample(labels, ell); coeffs = {g: rng.randint(1, 9) for g in S}
            a0 = S[0][0]
            same = [g for g in S if g[0] == a0]
            if len(same) >= 2:
                coeffs[same[1]] = (-sum(coeffs[g] for g in same if g != same[1])) % p or p
        if all(c % p == 0 for c in coeffs.values()):
            coeffs[S[0]] = 1
        nullity, nullity2, best, nonzero_dirs, viol = instance_check(d, p, k, S, coeffs, omega)
        if nullity != nullity2: ties += 1
        if nonzero_dirs == 0: n_alldirs_zero += 1
        if nullity > 0: n_nonzero += 1
        if viol:
            nviol += 1
            print("VIOLATION", S, coeffs, nullity, best, viol[:3])
    print(f"(B) d={d}: instances={ninst}, violations={nviol}, instances with nullity>0: {n_nonzero}, "
          f"instances with all directions zero: {n_alldirs_zero}, threshold-ambiguous: {ties}")
    # explicit sharpness family: prod_{i<l-1}(Z^{p^{k-1}} - omega_p^i), l <= p, nullity (l-1)p^{k-1}
    Zm = weyl(d, 0, 1, omega)
    for ell in range(1, p + 1):
        M = np.eye(d, dtype=complex)
        for i in range(ell - 1):
            M = M @ (np.linalg.matrix_power(Zm, p**(k - 1)) - np.exp(2j * np.pi * i / p) * np.eye(d))
        # Weyl coefficients: c_(a,b) = Tr(W_(a,b)^* M)/d
        cnt = sum(1 for a in range(d) for b in range(d) if abs(np.trace(weyl(d, a, b, omega).conj().T @ M)) / d > 1e-9)
        sv = np.linalg.svd(M, compute_uv=False)
        nul = int(np.sum(sv < 1e-8 * max(sv[0], 1)))
        print(f"   sharpness family l={ell}: s_W={cnt}, nullity={nul}, (l-1)p^(k-1)={(ell-1)*p**(k-1)}")
