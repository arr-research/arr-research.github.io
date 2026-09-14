"""exact_check_firstorder_violations.py -- the three instances flagged 'nullity>ord' in log_firstorder_16.txt.
The numerical nullity (threshold 1e-8 * sigma_max, complex doubles) reported 1 while the first-order theorem predicts 0
(only one coefficient survives modulo 2: a single monomial, order 0).  Here the determinant is decided EXACTLY:
the 16x16 matrix over Q(omega_16) is mapped through the regular representation of Q(omega_16) = Q[x]/(x^8+1) to a
128x128 integer matrix whose rank (exact Fraction elimination) is 128 iff det C != 0 (the determinant of the big matrix
is the field norm of det C).  We also print sigma_min/sigma_max to exhibit the conditioning artefact.
"""
from fractions import Fraction
import numpy as np

d = 16; n = 8  # phi(16) = 8, Phi_16 = x^8 + 1

def mul_matrix_of_omega_power(e):
    """8x8 integer matrix of multiplication by omega^e on the basis 1, x, ..., x^7 of Z[x]/(x^8+1)."""
    e %= d
    M = [[0]*n for _ in range(n)]
    for j in range(n):  # image of basis vector x^j is x^{j+e} reduced: x^8 = -1
        t = j + e; sign = 1
        while t >= n: t -= n; sign = -sign
        M[t][j] = sign
    return M

def rank_Q(A):
    A = [[Fraction(v) for v in row] for row in A]
    m = len(A); ncol = len(A[0]); r = 0
    for c in range(ncol):
        piv = None
        for i in range(r, m):
            if A[i][c] != 0: piv = i; break
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]; A[r] = [v / pv for v in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]; A[i] = [a - f*b for a, b in zip(A[i], A[r])]
        r += 1
        if r == m: break
    return r

def weyl_num(a, b, omega):
    W = np.zeros((d, d), dtype=complex)
    for j in range(d): W[(j + a) % d, j] = omega ** (b*j % d)
    return W

instances = [
    ([(13, 8), (15, 9), (8, 7)], {(13, 8): 1, (15, 9): 8, (8, 7): 8}),
    ([(7, 15), (10, 15), (3, 4)], {(7, 15): -4, (10, 15): 4, (3, 4): -1}),
    ([(2, 9), (1, 14), (14, 4)], {(2, 9): 1, (1, 14): 5, (14, 4): -5}),
]
omega = np.exp(2j*np.pi/d)
for S, coeffs in instances:
    big = [[0]*(d*n) for _ in range(d*n)]
    Cn = np.zeros((d, d), dtype=complex)
    for (a, b) in S:
        c = coeffs[(a, b)]
        Cn += c*weyl_num(a, b, omega)
        for j in range(d):
            i = (j + a) % d
            blk = mul_matrix_of_omega_power(b*j)
            for u in range(n):
                for v in range(n):
                    big[i*n + u][j*n + v] += c*blk[u][v]
    rk = rank_Q(big)
    sv = np.linalg.svd(Cn, compute_uv=False)
    print(f"S={S} coeffs={coeffs}: rank over Q of the 128x128 regular-representation matrix = {rk} "
          f"=> det C {'!= 0 (C invertible, exact nullity 0)' if rk == d*n else '= 0'};"
          f" numerics: sigma_max={sv[0]:.3e}, sigma_min={sv[-1]:.3e}, ratio={sv[-1]/sv[0]:.3e}")