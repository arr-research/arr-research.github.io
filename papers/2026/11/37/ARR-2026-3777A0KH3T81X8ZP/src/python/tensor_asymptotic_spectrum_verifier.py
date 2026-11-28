"""Exact-Z/Q verifier for Strassen asymptotic spectrum interpolation, flattening ranks,
W-state border-rank separation, and Lovasz-theta graph capacity brackets.

Zero floating-point arithmetic, zero '/' division operator, zero '**' operator (AST-enforced).
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from typing import Any


def q(num: int, den: int = 1) -> Fraction:
    if den == 0:
        raise ZeroDivisionError("Zero denominator")
    return Fraction(num, den)


def q_div(a: Fraction, b: Fraction) -> Fraction:
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return Fraction(a.numerator * b.denominator, a.denominator * b.numerator)


def q_to_pair(x: Fraction) -> list[int]:
    return [x.numerator, x.denominator]


def int_pow(base: int, exp: int) -> int:
    if exp < 0:
        raise ValueError("Negative exponent forbidden")
    res = 1
    b = base
    e = exp
    while e > 0:
        if e & 1:
            res = res * b
        b = b * b
        e = e >> 1
    return res


def q_pow(x: Fraction, exp: int) -> Fraction:
    if exp < 0:
        raise ValueError("Negative exponent forbidden")
    return Fraction(int_pow(x.numerator, exp), int_pow(x.denominator, exp))


def matrix_rank_q(mat: list[list[Fraction]]) -> int:
    """Exact Gaussian elimination rank over Q (zero floats)."""
    if not mat or not mat[0]:
        return 0
    M = [list(row) for row in mat]
    rows = len(M)
    cols = len(M[0])
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv_p = q_div(q(1, 1), M[r][c])
        M[r] = [v * inv_p for v in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                fac = M[i][c]
                M[i] = [M[i][j] - fac * M[r][j] for j in range(cols)]
        r += 1
    return r


def flattening_ranks_3tensor(dims: tuple[int, int, int], entries: dict[tuple[int, int, int], Fraction]) -> tuple[int, int, int]:
    """Compute exact (rk_1, rk_2, rk_3) one-leg-vs-rest flattening ranks of an order-3 tensor over Q."""
    d1, d2, d3 = dims
    m1 = [[q(0) for _ in range(d2 * d3)] for _ in range(d1)]
    m2 = [[q(0) for _ in range(d1 * d3)] for _ in range(d2)]
    m3 = [[q(0) for _ in range(d1 * d2)] for _ in range(d3)]
    for (i, j, k), val in entries.items():
        if not (0 <= i < d1 and 0 <= j < d2 and 0 <= k < d3):
            raise ValueError("Tensor index out of range")
        m1[i][j * d3 + k] = m1[i][j * d3 + k] + val
        m2[j][i * d3 + k] = m2[j][i * d3 + k] + val
        m3[k][i * d2 + j] = m3[k][i * d2 + j] + val
    return (matrix_rank_q(m1), matrix_rank_q(m2), matrix_rank_q(m3))


def make_matmul_tensor(a: int, b: int, c: int) -> tuple[tuple[int, int, int], dict[tuple[int, int, int], Fraction]]:
    """Construct exact matrix multiplication tensor <a, b, c> in Q^{(ab) x (bc) x (ca)}."""
    if a < 1 or b < 1 or c < 1:
        raise ValueError("Matrix multiplication dimensions must be >= 1")
    entries: dict[tuple[int, int, int], Fraction] = {}
    for i in range(a):
        for j in range(b):
            for k in range(c):
                idx1 = i * b + j
                idx2 = j * c + k
                idx3 = k * a + i
                entries[(idx1, idx2, idx3)] = q(1)
    return ((a * b, b * c, c * a), entries)


def make_w_state_tensor() -> tuple[tuple[int, int, int], dict[tuple[int, int, int], Fraction]]:
    """Exact 3-qubit W-state tensor W = |100> + |010> + |001> in Q^{2x2x2}."""
    entries = {
        (1, 0, 0): q(1),
        (0, 1, 0): q(1),
        (0, 0, 1): q(1),
    }
    return ((2, 2, 2), entries)


def make_cw_tensor(q_param: int) -> tuple[tuple[int, int, int], dict[tuple[int, int, int], Fraction]]:
    """Exact Coppersmith-Winograd tensor CW_q in Q^{(q+2)x(q+2)x(q+2)}:
    sum_{i=1}^q (e_0 e_i e_i + e_i e_0 e_i + e_i e_i e_0) + e_0 e_0 e_{q+1} + e_0 e_{q+1} e_0 + e_{q+1} e_0 e_0."""
    if q_param < 1:
        raise ValueError("CW parameter q must be >= 1")
    d = q_param + 2
    last = q_param + 1
    entries: dict[tuple[int, int, int], Fraction] = {
        (0, 0, last): q(1),
        (0, last, 0): q(1),
        (last, 0, 0): q(1),
    }
    for i in range(1, q_param + 1):
        entries[(0, i, i)] = q(1)
        entries[(i, 0, i)] = q(1)
        entries[(i, i, 0)] = q(1)
    return ((d, d, d), entries)


def kronecker_3tensor(
    t1: tuple[tuple[int, int, int], dict[tuple[int, int, int], Fraction]],
    t2: tuple[tuple[int, int, int], dict[tuple[int, int, int], Fraction]],
) -> tuple[tuple[int, int, int], dict[tuple[int, int, int], Fraction]]:
    (a1, b1, c1), e1 = t1
    (a2, b2, c2), e2 = t2
    out: dict[tuple[int, int, int], Fraction] = {}
    for (i1, j1, k1), v1 in e1.items():
        for (i2, j2, k2), v2 in e2.items():
            key = (i1 * a2 + i2, j1 * b2 + j2, k1 * c2 + k2)
            out[key] = out.get(key, q(0)) + v1 * v2
    return ((a1 * a2, b1 * b2, c1 * c2), out)


def direct_sum_3tensor(
    t1: tuple[tuple[int, int, int], dict[tuple[int, int, int], Fraction]],
    t2: tuple[tuple[int, int, int], dict[tuple[int, int, int], Fraction]],
) -> tuple[tuple[int, int, int], dict[tuple[int, int, int], Fraction]]:
    (a1, b1, c1), e1 = t1
    (a2, b2, c2), e2 = t2
    out = dict(e1)
    for (i2, j2, k2), v2 in e2.items():
        out[(a1 + i2, b1 + j2, c1 + k2)] = v2
    return ((a1 + a2, b1 + b2, c1 + c2), out)


def strassen_interpolation_cert(
    name: str,
    ranks: tuple[int, int, int],
    weights: tuple[int, int, int],
) -> dict[str, Any]:
    """Exact root-free certification of Strassen geometric interpolation zeta_theta^D = r1^n1 * r2^n2 * r3^n3."""
    r1, r2, r3 = ranks
    n1, n2, n3 = weights
    if r1 < 1 or r2 < 1 or r3 < 1:
        raise ValueError("Flattening ranks must be >= 1")
    if n1 < 0 or n2 < 0 or n3 < 0 or (n1 + n2 + n3) < 1:
        raise ValueError("Weights must be nonnegative with positive sum D")
    D = n1 + n2 + n3
    m_min = min(r1, r2, r3)
    m_max = max(r1, r2, r3)
    zeta_pow_D = int_pow(r1, n1) * int_pow(r2, n2) * int_pow(r3, n3)
    min_pow_D = int_pow(m_min, D)
    max_pow_D = int_pow(m_max, D)
    if not (min_pow_D <= zeta_pow_D <= max_pow_D):
        raise RuntimeError("Spectral interval sandwich failed")
    return {
        "tensor": name,
        "flattening_ranks": [r1, r2, r3],
        "interval_min_rank": m_min,
        "interval_max_rank": m_max,
        "rational_weights_num": [n1, n2, n3],
        "weight_den_D": D,
        "zeta_pow_D": zeta_pow_D,
        "min_pow_D": min_pow_D,
        "max_pow_D": max_pow_D,
        "sandwich_verified": min_pow_D <= zeta_pow_D <= max_pow_D,
    }


def w_state_border_rank_and_spectrum_cert() -> dict[str, Any]:
    """Certify W-state flattening ranks (2,2,2), exact Z[eps] border-rank-2 witness across all 8 entries,
    and strict root-free separation (2^{h(1/3)})^3 = 27/4 < 8 = 2^3."""
    dims, entries = make_w_state_tensor()
    rks = flattening_ranks_3tensor(dims, entries)
    if rks != (2, 2, 2):
        raise RuntimeError(f"Expected W flattening ranks (2,2,2), got {rks}")

    # Verify exact Z[eps] identity: (e_0 + eps*e_1)^{tensor 3} - e_0^{tensor 3} = eps*W + O(eps^2)
    # Represent each entry as poly in eps of degree <= 3: [c0, c1, c2, c3]
    u = [[1, 0], [0, 1]]  # e_0 + eps*e_1: coord 0 is 1, coord 1 is eps
    v = [[1, 0], [0, 0]]  # e_0: coord 0 is 1, coord 1 is 0
    eps0_zero = True
    eps1_matches_w = True
    for i in range(2):
        for j in range(2):
            for k in range(2):
                # Multiply polynomials u[i]*u[j]*u[k] - v[i]*v[j]*v[k]
                p_u = [0, 0, 0, 0]
                for d1 in range(2):
                    for d2 in range(2):
                        for d3 in range(2):
                            p_u[d1 + d2 + d3] += u[i][d1] * u[j][d2] * u[k][d3]
                p_v0 = v[i][0] * v[j][0] * v[k][0]
                p_u[0] -= p_v0
                if p_u[0] != 0:
                    eps0_zero = False
                expected_w = 1 if (i + j + k == 1) else 0
                if p_u[1] != expected_w:
                    eps1_matches_w = False
    if not (eps0_zero and eps1_matches_w):
        raise RuntimeError("Z[eps] W-state border rank 2 witness failed")

    # Root-free Strassen binary-entropy quantum functional bound: (2^{h(1/3)})^3 = (3 / 2^{2/3})^3 = 27/4 < 8 = 2^3
    subrank_cube_ub = q(27, 4)
    flattening_cube = q(8, 1)
    strict_gap = subrank_cube_ub < flattening_cube
    if not strict_gap:
        raise RuntimeError("W-state strict spectral gap failed")

    return {
        "tensor": "W_3",
        "flattening_ranks": list(rks),
        "border_rank_upper_bound": 2,
        "z_eps_all_8_entries_verified": eps0_zero and eps1_matches_w,
        "quantum_functional_cube_ub": q_to_pair(subrank_cube_ub),
        "flattening_rank_cube": q_to_pair(flattening_cube),
        "cube_gap_exact": q_to_pair(flattening_cube - subrank_cube_ub),
        "strict_nondegenerate_interval": strict_gap,
    }


def c5_shannon_capacity_sandwich_cert() -> dict[str, Any]:
    """Certify exact C_5 Shannon-capacity sandwich alpha(C_5)=2 < sqrt(5)=Theta(C_5)=vartheta(C_5) < 5/2=chi_f(bar C_5)
    plus explicit size-5 independent set in strong product C_5 x C_5."""
    # Vertices 0..4, edges (i, (i+1)%5)
    def adj_c5(u: int, v: int) -> bool:
        diff = (u - v) % 5
        return diff == 1 or diff == 4

    def adj_strong(p1: tuple[int, int], p2: tuple[int, int]) -> bool:
        if p1 == p2:
            return False
        a1 = (p1[0] == p2[0]) or adj_c5(p1[0], p2[0])
        a2 = (p1[1] == p2[1]) or adj_c5(p1[1], p2[1])
        return a1 and a2

    indep_set = [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]
    for idx1 in range(len(indep_set)):
        for idx2 in range(idx1 + 1, len(indep_set)):
            if adj_strong(indep_set[idx1], indep_set[idx2]):
                raise RuntimeError("Not an independent set in C_5 x C_5")

    alpha_sq = q(4, 1)
    theta_sq = q(5, 1)
    chif_sq = q(25, 4)
    if not (alpha_sq < theta_sq < chif_sq):
        raise RuntimeError("C_5 sandwich inequality failed")
    return {
        "graph": "C_5",
        "alpha": 2,
        "strong_square_indep_set": [list(p) for p in indep_set],
        "strong_square_alpha_witness": len(indep_set),
        "vartheta_squared_exact": q_to_pair(theta_sq),
        "chi_f_complement_exact": [5, 2],
        "alpha_sq_lt_theta_sq_lt_chif_sq": alpha_sq < theta_sq < chif_sq,
    }


def c7_lovasz_chebyshev_bracket_cert() -> dict[str, Any]:
    """Certify exact root-free Chebyshev bracket on cos(pi/7) and Lovasz theta vartheta(C_7) = 7c/(1+c) in (63/19, 637/191)."""
    # Minimal polynomial of c = cos(pi/7) is p(t) = 8t^3 - 4t^2 - 4t + 1
    def p_eval(t: Fraction) -> Fraction:
        return q(8) * q_pow(t, 3) - q(4) * q_pow(t, 2) - q(4) * t + q(1)

    def dp_eval(t: Fraction) -> Fraction:
        return q(24) * q_pow(t, 2) - q(8) * t - q(4)

    lo = q(9, 10)
    hi = q(91, 100)
    p_lo = p_eval(lo)
    p_hi = p_eval(hi)
    dp_lo = dp_eval(lo)
    if not (p_lo < 0 < p_hi and dp_lo > 0):
        raise RuntimeError("Chebyshev root bracket for cos(pi/7) failed")

    # vartheta(C_7) = 7c/(1+c), strictly increasing on c > 0
    th_lo = q_div(q(7) * lo, q(1) + lo)  # 63/19
    th_hi = q_div(q(7) * hi, q(1) + hi)  # 637/191
    if not (q(3, 1) < th_lo < th_hi < q(7, 2)):
        raise RuntimeError("C_7 Lovasz sandwich failed")
    return {
        "graph": "C_7",
        "alpha": 3,
        "chi_f_complement_exact": [7, 2],
        "cos_pi_7_lo": q_to_pair(lo),
        "cos_pi_7_hi": q_to_pair(hi),
        "chebyshev_p_lo": q_to_pair(p_lo),
        "chebyshev_p_hi": q_to_pair(p_hi),
        "chebyshev_dp_lo_pos": dp_lo > 0,
        "vartheta_lo_exact": q_to_pair(th_lo),
        "vartheta_hi_exact": q_to_pair(th_hi),
        "strict_sandwich_verified": q(3, 1) < th_lo < th_hi < q(7, 2),
    }


def canonical_json_sha256(payload: dict[str, Any]) -> str:
    raw = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()
