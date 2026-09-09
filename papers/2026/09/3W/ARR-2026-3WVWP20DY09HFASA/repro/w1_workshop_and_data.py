"""Version-2 additions (2026-09-08).

(1) Reproduces, independently of the author's ring code, the two checks made by the external workshop
    (taller_feedback/check_core.py, item TALLER-0001): the 1826 exact Clifford identities (4.1) for
    p in {3,5,7,11} and the rank 12 of the 20x20 regular-representation matrix of the parabola operator
    (rank 3 over Q(omega_5), nullity 2).
(2) Writes full-precision data files into data/:
      parabola_certificate.json   exact exponent vectors f_k of the five parabola operators C_k, the
                                  20x20 integer regular-representation matrix of each, its rank over Q
                                  (Fraction elimination and sympy), singular values of C_0 (double precision).
      gp5_numerical_witness.json  the numerical nullity-2 witness on the other general-position 5-set of
                                  p = 5 (reviewer's alternating minimisation, seed 5), coefficients at full
                                  double precision, and a recomputation of sigma_4 from the stored numbers.
(3) Numerically verifies the self-contained achievability construction of Section 6 (v2): the Cauchy-Binet
    (Hodge) POVM for the consecutive probe of Schmidt rank r in prime dimension p, for p in {3,5,7} and
    all 1 <= r <= p: completeness, perfectness with lists of size p-r+1, and the equivalent factorisation
    rho = sum_E C_E C_E^* with s_W(C_E) = p-r+1.

Run:  python w1_workshop_and_data.py          (about 20 s; last line must be 'W1: ALL CHECKS PASSED')
"""
import json, itertools, os, time
from fractions import Fraction
import numpy as np

t0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data'); os.makedirs(DATA, exist_ok=True)
report = {}

# ---------------------------------------------------------------- (1a) identities (4.1), workshop style
count = 0
for p in [3, 5, 7, 11]:
    inv2 = pow(2, -1, p)
    for s in range(p):
        for a in range(p):
            for b in range(p):
                aa = -(s * a + b) % p                      # new shift label
                e = (-s * inv2 * a * a - a * b) % p        # phase exponent e(s,a,b)
                for j in range(p):
                    for k in range(p):
                        lhs = j * (k + a) + s * inv2 * (k + a) ** 2 + b * k     # entry (j,k) of U_s W_(a,b)
                        rhs = e + a * (j - aa) + (j - aa) * k + s * inv2 * k * k  # entry (j,k) of w^e X^aa Z^a U_s
                        assert (lhs - rhs) % p == 0
                count += 1
assert count == 1826 == 27 + 125 + 343 + 1331
report['clifford_identities_exact'] = count
print(f'(1a) identity (4.1) exact for all s and labels, p in 3,5,7,11: {count} cases  [{time.time()-t0:.1f}s]')

# ---------------------------------------------------------------- (1b) parabola operators over Q(omega_5)
p = 5
def rank_fraction(M):
    """Rank of an integer matrix by exact Gaussian elimination over Q."""
    A = [[Fraction(x) for x in row] for row in M]; n, m = len(A), len(A[0]); r = 0
    for c in range(m):
        piv = next((i for i in range(r, n) if A[i][c] != 0), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(n):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        r += 1
    return r

# multiplication by omega on Q(omega_5) = Q[x]/(x^4+x^3+x^2+x+1) in the basis 1,x,x^2,x^3
Wm = np.array([[0, 0, 0, -1], [1, 0, 0, -1], [0, 1, 0, -1], [0, 0, 1, -1]], dtype=object)
def matpow(M, e):
    R = np.identity(4, dtype=object)
    for _ in range(e % 5): R = R.dot(M)
    return R
S = [(t, t * t % p) for t in range(p)]
def fk(k):  # f_k(t) = sum_{i<t} (i^2 + i - k) mod 5
    return [sum(i * i + i - k for i in range(t)) % p for t in range(p)]
def regular_rep(f):
    """20x20 integer matrix of C = sum_t omega^{f(t)} W_(t,t^2) over Q (regular representation of Q(omega_5))."""
    C = np.zeros((20, 20), dtype=object)
    for (a, b), ph in zip(S, f):
        for k in range(p):
            j = (k + a) % p                                   # X^a Z^b |k> = omega^{bk} |k+a>
            C[j * 4:(j + 1) * 4, k * 4:(k + 1) * 4] += matpow(Wm, b * k + ph)
    return C
cert = {'p': 5, 'support': S, 'basis_of_Q(omega_5)': '1, w, w^2, w^3 with w^4 = -1-w-w^2-w^3',
        'convention': 'X|k> = |k+1>, Z|k> = w^k |k>, W_(a,b) = X^a Z^b; C_k = sum_t w^{f_k(t)} W_(t,t^2)',
        'operators': []}
import sympy
for k in range(p):
    f = fk(k); C = regular_rep(f)
    rk = rank_fraction(C.tolist()); rk2 = sympy.Matrix(C.tolist()).rank()
    assert rk == rk2 == 12
    cert['operators'].append({'k': k, 'f_k': f, 'regular_representation_20x20': [[int(x) for x in row] for row in C],
                              'rank_over_Q': rk, 'rank_over_Q(omega_5)': rk // 4, 'nullity': p - rk // 4})
assert fk(0) == [0, 0, 2, 3, 0]
# numeric singular values of C_0
w = np.exp(2j * np.pi / p); X = np.roll(np.eye(p), 1, axis=0); Z = np.diag(w ** np.arange(p))
Wab = lambda a, b: np.linalg.matrix_power(X, a % p) @ np.linalg.matrix_power(Z, b % p)
C0 = sum(w ** ph * Wab(a, b) for (a, b), ph in zip(S, fk(0)))
sv = np.linalg.svd(C0, compute_uv=False)
cert['C_0_singular_values_double'] = [repr(float(x)) for x in sv]
cert['C_0_CCstar_eigenvalues_expected'] = [10, 10, 5, 0, 0]
assert np.allclose(sv ** 2, [10, 10, 5, 0, 0], atol=1e-12)
# no three points collinear
for A, B, Cc in itertools.combinations(S, 3):
    assert ((B[0] - A[0]) * (Cc[1] - A[1]) - (B[1] - A[1]) * (Cc[0] - A[0])) % p != 0
cert['no_three_collinear'] = True
json.dump(cert, open(os.path.join(DATA, 'parabola_certificate.json'), 'w'), indent=1)
report['parabola_regular_representation_rank'] = 12; report['rank_over_Q_omega'] = 3; report['nullity'] = 2
print(f'(1b) parabola: all five C_k have regular-representation rank 12 -> rank 3 over Q(omega_5), nullity 2 '
      f'(Fraction elimination and sympy agree); sigma(C_0)^2 = {np.round(sv**2,12).tolist()}  [{time.time()-t0:.1f}s]')

# ---------------------------------------------------------------- (2) numerical witness on the other GP orbit
def search(Ws, k, restarts, rng, iters=400):
    best = (np.inf, None)
    for _ in range(restarts):
        c = rng.normal(size=len(Ws)) + 1j * rng.normal(size=len(Ws)); c /= np.linalg.norm(c)
        for _ in range(iters):
            C = sum(ci * Wi for ci, Wi in zip(c, Ws))
            _, _, Vh = np.linalg.svd(C); V = Vh[-k:].conj().T
            M = np.stack([(Wi @ V).ravel() for Wi in Ws], axis=1)
            _, s_, Vh2 = np.linalg.svd(M); c = Vh2[-1].conj(); c /= np.linalg.norm(c)
        C = sum(ci * Wi for ci, Wi in zip(c, Ws)); s_ = np.linalg.svd(C, compute_uv=False)
        if s_[p - k] < best[0]: best = (s_[p - k], c.copy())
    return best
S2 = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 3)]
val, c = search([Wab(*g) for g in S2], 2, 40, np.random.default_rng(5))
C2 = sum(ci * Wab(*g) for ci, g in zip(c, S2)); sv2 = np.linalg.svd(C2, compute_uv=False)
wit = {'p': 5, 'support': S2, 'method': 'alternating minimisation of sigma_4^2+sigma_5^2 on |c|=1, 40 restarts, 400 iterations, numpy default_rng(5)',
       'coefficients_re': [repr(float(x.real)) for x in c], 'coefficients_im': [repr(float(x.imag)) for x in c],
       'abs_coefficients': [repr(float(abs(x))) for x in c], 'singular_values': [repr(float(x)) for x in sv2],
       'sigma_4': repr(float(sv2[3])), 'note': 'numerical only; the coefficient ratios were not recognised as low-degree algebraic numbers'}
# recompute from the stored strings
c_back = np.array([complex(float(a), float(b)) for a, b in zip(wit['coefficients_re'], wit['coefficients_im'])])
sv_back = np.linalg.svd(sum(ci * Wab(*g) for ci, g in zip(c_back, S2)), compute_uv=False)
assert sv_back[3] < 1e-12 and min(abs(c_back)) > 0.25
wit['sigma_4_recomputed_from_file'] = repr(float(sv_back[3]))
json.dump(wit, open(os.path.join(DATA, 'gp5_numerical_witness.json'), 'w'), indent=1)
print(f'(2)  general-position orbit {S2}: sigma_4 = {sv2[3]:.2e}, min|c| = {min(abs(c)):.4f}; written to data/gp5_numerical_witness.json  [{time.time()-t0:.1f}s]')

# ---------------------------------------------------------------- (3) self-contained achievability (Section 6, v2)
def check_consecutive(p, r):
    w = np.exp(2j * np.pi / p)
    phi = [np.array([w ** (b * x) for x in range(r)]) / np.sqrt(r) for b in range(p)]     # phase frame in C^r
    T = np.stack(phi, axis=1)                                                             # r x p synthesis
    assert np.allclose(T @ T.conj().T, (p / r) * np.eye(r))                               # tight, bound p/r
    ws = {}
    for E in itertools.combinations(range(p), r - 1):
        TE = T[:, list(E)]
        wE = np.array([(-1) ** x * np.conj(np.linalg.det(np.delete(TE, x, axis=0))) for x in range(r)]) if r > 1 else np.array([1.0 + 0j])
        ws[E] = wE
        for b in range(p):
            ip = np.vdot(wE, phi[b])
            if b in E: assert abs(ip) < 1e-9
            else: assert abs(ip) > 1e-9                                                   # full spark
    G = sum(np.outer(wE, wE.conj()) for wE in ws.values())
    assert np.allclose(G, (p / r) ** (r - 1) * np.eye(r))                                 # Cauchy-Binet identity
    # full POVM on C^p (x) C^r and perfectness
    X = np.roll(np.eye(p), 1, axis=0); Z = np.diag(w ** np.arange(p))
    A = np.zeros((p, r), dtype=complex); A[:r, :r] = np.eye(r) / np.sqrt(r)               # consecutive probe
    vec = lambda M: M.reshape(-1)                                                          # |M>> = sum M_ij |i>|j>
    out = {(a, b): vec(np.linalg.matrix_power(X, a) @ np.linalg.matrix_power(Z, b) @ A) for a in range(p) for b in range(p)}
    J = {a: np.zeros((p * r, r), dtype=complex) for a in range(p)}
    for a in range(p):
        for x in range(r): J[a][((x + a) % p) * r + x, x] = 1                              # |x> -> |x+a>|x>
    total = np.zeros((p * r, p * r), dtype=complex); lists = {}
    for a in range(p):
        for E, wE in ws.items():
            M = (r / p) ** (r - 1) * J[a] @ np.outer(wE, wE.conj()) @ J[a].conj().T
            total += M; lists[(a, E)] = [(a, b) for b in range(p) if b not in E]
            for g, v in out.items():
                pr = np.vdot(v, M @ v).real
                if g not in lists[(a, E)]: assert abs(pr) < 1e-9
    Mrest = np.eye(p * r) - total
    ev = np.linalg.eigvalsh((Mrest + Mrest.conj().T) / 2); assert ev.min() > -1e-9         # remainder is PSD
    for v in out.values(): assert abs(np.vdot(v, Mrest @ v)) < 1e-9                        # and never fires
    assert all(len(L) == p - r + 1 for L in lists.values())
    # equivalent (6.1) factorisation: C_E = h_E(Z) with h_E(w^j) = (w_E)_j for j<r, 0 otherwise
    F = np.array([[w ** (j * t) for t in range(p)] for j in range(p)])                     # values <- coefficients
    rho = A @ A.conj().T; acc = np.zeros((p, p), dtype=complex)
    for E, wE in ws.items():
        vals = np.zeros(p, dtype=complex); vals[:r] = wE
        coef = np.linalg.solve(F, vals)                                                    # h_E coefficients
        supp = [t for t in range(p) if abs(coef[t]) > 1e-9]
        assert sorted(supp) == [t for t in range(p) if t not in E]                         # support F_p \ E
        CE = sum(coef[t] * np.linalg.matrix_power(Z, t) for t in range(p)) / np.sqrt(r * (p / r) ** (r - 1))
        acc += CE @ CE.conj().T
    assert np.allclose(acc, rho)
    return len(ws)
tot = 0
for pp in [3, 5, 7]:
    for rr in range(1, pp + 1): tot += check_consecutive(pp, rr)
report['consecutive_probe_hodge_povm_checked'] = {'primes': [3, 5, 7], 'all r': True, 'effects_per_sector_total': tot}
print(f'(3)  consecutive-probe decoder (Cauchy-Binet POVM) verified for p in 3,5,7 and all r: completeness, '
      f'perfectness with lists of size p-r+1, and rho = sum_E C_E C_E^* with s_W(C_E) = p-r+1  [{time.time()-t0:.1f}s]')

json.dump(report, open(os.path.join(DATA, 'w1_report.json'), 'w'), indent=1)
print('W1: ALL CHECKS PASSED')
