"""
Exact zero-float rational verifier for Quantitative Hankel-SOS Sum-Negativity
Bounds, Exact Blind-Spot Constructions, and Higher-Order Moment Hierarchies
for Discrete Wigner Magic (strictly advancing Sharma, Chakrabarty, Mukherjee,
Mallick, and Maity, arXiv:2611.34668v1).

Strict AST purity: zero float literals, zero '/', zero '**', zero floating-point
libraries. All calculations use exact reduced rational pairs (num, den) in Q
and exact quadratic extension Q(sqrt(5)) = {(a, b) : a + b*sqrt(5), a,b in Q}
for the ququint state |psi_4>.
"""

from __future__ import annotations

import hashlib
import json
import math
from typing import Any

Rat = tuple[int, int]  # (num, den) with den > 0, gcd(|num|, den) == 1


def canonical_json_sha256(obj: Any) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def q(num: int, den: int = 1) -> Rat:
    if den == 0:
        raise ZeroDivisionError("Zero denominator")
    if den < 0:
        num = -num
        den = -den
    g = math.gcd(abs(num), den)
    return (num // g, den // g)


def q_add(a: Rat, b: Rat) -> Rat:
    return q(a[0] * b[1] + b[0] * a[1], a[1] * b[1])


def q_sub(a: Rat, b: Rat) -> Rat:
    return q(a[0] * b[1] - b[0] * a[1], a[1] * b[1])


def q_mul(a: Rat, b: Rat) -> Rat:
    return q(a[0] * b[0], a[1] * b[1])


def q_div(a: Rat, b: Rat) -> Rat:
    if b[0] == 0:
        raise ZeroDivisionError("Rational division by zero")
    return q(a[0] * b[1], a[1] * b[0])


def q_neg(a: Rat) -> Rat:
    return (-a[0], a[1])


def q_abs(a: Rat) -> Rat:
    return (abs(a[0]), a[1])


def q_pow(a: Rat, k: int) -> Rat:
    if k < 0:
        raise ValueError("Negative exponent")
    res: Rat = (1, 1)
    base: Rat = a
    e = k
    while e > 0:
        if e & 1:
            res = q_mul(res, base)
        base = q_mul(base, base)
        e >>= 1
    return res


def q_cmp(a: Rat, b: Rat) -> int:
    lhs = a[0] * b[1]
    rhs = b[0] * a[1]
    if lhs < rhs:
        return -1
    if lhs > rhs:
        return 1
    return 0


def q_max(vals: list[Rat]) -> Rat:
    best = vals[0]
    for v in vals[1:]:
        if q_cmp(v, best) > 0:
            best = v
    return best


def q_min(vals: list[Rat]) -> Rat:
    best = vals[0]
    for v in vals[1:]:
        if q_cmp(v, best) < 0:
            best = v
    return best


def q_list(a: Rat) -> list[int]:
    return [a[0], a[1]]


# ---------------------------------------------------------------------------
# Exact Q(sqrt(5)) arithmetic for exact ququint |psi_4> mixed-state moments
# Element (a, b) represents a + b * sqrt(5) with a, b in Q.
# ---------------------------------------------------------------------------

Q5 = tuple[Rat, Rat]


def q5(a: Rat, b: Rat = (0, 1)) -> Q5:
    return (a, b)


def q5_add(x: Q5, y: Q5) -> Q5:
    return (q_add(x[0], y[0]), q_add(x[1], y[1]))


def q5_mul(x: Q5, y: Q5) -> Q5:
    # (a + b s5)(c + d s5) = (ac + 5bd) + (ad + bc) s5
    real_part = q_add(q_mul(x[0], y[0]), q_mul(q(5), q_mul(x[1], y[1])))
    s5_part = q_add(q_mul(x[0], y[1]), q_mul(x[1], y[0]))
    return (real_part, s5_part)


def q5_pow(x: Q5, k: int) -> Q5:
    res: Q5 = ((1, 1), (0, 1))
    base: Q5 = x
    e = k
    while e > 0:
        if e & 1:
            res = q5_mul(res, base)
        base = q5_mul(base, base)
        e >>= 1
    return res


def q5_is_neg(x: Q5) -> bool:
    """Exact sign test: a + b*sqrt(5) < 0."""
    a, b = x
    sa = q_cmp(a, (0, 1))
    sb = q_cmp(b, (0, 1))
    if sa <= 0 and sb <= 0:
        return sa < 0 or sb < 0
    if sa >= 0 and sb >= 0:
        return False
    # Opposite signs: compare a^2 vs 5 b^2
    a2 = q_mul(a, a)
    five_b2 = q_mul(q(5), q_mul(b, b))
    if sa < 0 and sb > 0:
        return q_cmp(a2, five_b2) > 0
    # sa > 0 and sb < 0
    return q_cmp(five_b2, a2) > 0


# ---------------------------------------------------------------------------
# Exact Wigner moments, Hankel matrices, and Theorem 1-4 certificates
# ---------------------------------------------------------------------------


def rescaled_moments_rational(D: int, xs: list[Rat], k_max: int) -> list[Rat]:
    """
    Given rescaled Wigner coordinates x_u = D * W_u in [-1, 1] with sum(x_u) = D,
    compute exact rescaled moments m_k = D^{k-1} w_k = (1/D) sum_u x_u^k for k=0..k_max.
    """
    inv_D = q(1, D)
    s1 = (0, 1)
    for x in xs:
        if q_cmp(q_abs(x), (1, 1)) > 0:
            raise ValueError(f"|x_u| > 1 violates Wigner bound: {x}")
        s1 = q_add(s1, x)
    if q_cmp(s1, q(D)) != 0:
        raise ValueError(f"Normalization failed: sum(x_u)={s1} != D={D}")
    ms: list[Rat] = []
    for k in range(k_max + 1):
        acc = (0, 1)
        for x in xs:
            acc = q_add(acc, q_pow(x, k))
        ms.append(q_mul(inv_D, acc))
    return ms


def sum_negativity_rational(D: int, xs: list[Rat]) -> Rat:
    acc = (0, 1)
    for x in xs:
        if q_cmp(x, (0, 1)) < 0:
            acc = q_add(acc, q_neg(x))
    return q_mul(q(1, D), acc)


def hankel_matrix(ms: list[Rat], m: int) -> list[list[Rat]]:
    """(m+1)x(m+1) Hankel matrix [H_m]_{ij} = m_{i+j+1} (with m_1 = 1)."""
    return [[ms[i + j + 1] for j in range(m + 1)] for i in range(m + 1)]


def mat_det_rational(mat: list[list[Rat]]) -> Rat:
    """Exact Gaussian elimination determinant over Q."""
    n = len(mat)
    a = [list(row) for row in mat]
    det = (1, 1)
    for k in range(n):
        piv_row = -1
        for r in range(k, n):
            if a[r][k][0] != 0:
                piv_row = r
                break
        if piv_row == -1:
            return (0, 1)
        if piv_row != k:
            a[k], a[piv_row] = a[piv_row], a[k]
            det = q_neg(det)
        piv = a[k][k]
        det = q_mul(det, piv)
        for i in range(k + 1, n):
            fac = q_div(a[i][k], piv)
            for j in range(k + 1, n):
                a[i][j] = q_sub(a[i][j], q_mul(fac, a[k][j]))
            a[i][k] = (0, 1)
    return det


def hankel_quadratic_form(ms: list[Rat], v: list[Rat]) -> Rat:
    """Exact v^T H_m v = sum_{i,j} v_i v_j m_{i+j+1}."""
    m = len(v) - 1
    acc = (0, 1)
    for i in range(m + 1):
        for j in range(m + 1):
            term = q_mul(q_mul(v[i], v[j]), ms[i + j + 1])
            acc = q_add(acc, term)
    return acc


def exact_max_poly_sq_on_unit_interval_deg2(v: list[Rat]) -> Rat:
    """
    Exact rational maximum of q(-y)^2 on y in [0, 1] for deg <= 2 polynomial
    q(x) = v_0 + v_1 x + v_2 x^2 (so q(-y) = v_0 - v_1 y + v_2 y^2).
    """
    if len(v) == 2:
        # Linear: extreme at y=0 or y=1
        y0 = q_mul(v[0], v[0])
        y1 = q_pow(q_sub(v[0], v[1]), 2)
        return q_max([y0, y1])
    if len(v) == 3:
        v0, v1, v2 = v
        cands = [
            q_pow(v0, 2),
            q_pow(q_add(q_sub(v0, v1), v2), 2),
        ]
        if v2[0] != 0:
            ystar = q_div(v1, q_mul(q(2), v2))
            if q_cmp(ystar, (0, 1)) > 0 and q_cmp(ystar, (1, 1)) < 0:
                val = q_add(q_sub(v0, q_mul(v1, ystar)), q_mul(v2, q_pow(ystar, 2)))
                cands.append(q_pow(val, 2))
        return q_max(cands)
    # Safe universal L1-norm upper bound for arbitrary degree m >= 3:
    # For y in [0,1], |q(-y)| <= sum_j |v_j|, so max_{y in [0,1]} q(-y)^2 <= (sum |v_j|)^2!
    s = (0, 1)
    for c in v:
        s = q_add(s, q_abs(c))
    return q_pow(s, 2)


def schur_witness_H2(ms: list[Rat]) -> list[Rat]:
    """
    Exact rational Schur-complement witness vector v in Q^3 for H_2 when det(H_1) > 0:
      v = (-H_1^{-1} [b, c]^T, 1) = [(P*c - b^2)/(b - P^2), (P*b - c)/(b - P^2), 1].
    Satisfies v^T H_2 v = det(H_2) / det(H_1) < 0 whenever det(H_2) < 0!
    """
    P, b, c = ms[2], ms[3], ms[4]
    det1 = q_sub(b, q_mul(P, P))
    if det1[0] == 0:
        raise ZeroDivisionError("det(H_1) == 0; Schur witness undefined")
    v0 = q_div(q_sub(q_mul(P, c), q_mul(b, b)), det1)
    v1 = q_div(q_sub(q_mul(P, b), c), det1)
    return [v0, v1, (1, 1)]


def exact_hankel_sos_negativity_bound(ms: list[Rat], v: list[Rat], exact_max_bound: Rat | None = None) -> dict[str, Any]:
    """
    Theorem 1 certificate:
    For any witness vector v = (v_0, ..., v_m) in Q^{m+1} with v^T H_m v < 0,
    and any certified upper bound M_v >= max_{y in [0,1]} q_v(-y)^2,
    we have N(rho) >= (-v^T H_m v) / M_v > 0!
    """
    qf = hankel_quadratic_form(ms, v)
    if exact_max_bound is None:
        m_bound = exact_max_poly_sq_on_unit_interval_deg2(v)
    else:
        m_bound = exact_max_bound
    if q_cmp(qf, (0, 1)) < 0:
        lb = q_div(q_neg(qf), m_bound)
    else:
        lb = (0, 1)
    return {
        "witness_v": [q_list(c) for c in v],
        "quadratic_form_vTHv": q_list(qf),
        "M_v_upper_bound": q_list(m_bound),
        "certified_N_lower_bound": q_list(lb),
        "detects_negativity": q_cmp(lb, (0, 1)) > 0,
    }


def sharma_b3_rational(P: Rat, b: Rat) -> Rat:
    """Sharma et al. Theorem 4: B_3 = max(0, (P^2 - b) / (1 + 2P + b))."""
    num = q_sub(q_mul(P, P), b)
    if q_cmp(num, (0, 1)) <= 0:
        return (0, 1)
    den = q_add(q_add((1, 1), q_mul(q(2), P)), b)
    return q_div(num, den)


def sharma_b4_ratio_rational(P: Rat, c: Rat) -> Rat:
    """Exact squared ratio P^3 / c for Sharma et al. Theorem 5 (detects iff P^3 / c > 1)."""
    return q_div(q_pow(P, 3), c)


def noisy_strange_state_xs(p: Rat) -> list[Rat]:
    """Exact d=3 noisy strange state rho_1(p) = p|S><S| + (1-p)I/3: D=3, 9 points."""
    x0 = q_div(q_sub((1, 1), q_mul(q(4), p)), q(3))
    x1 = q_div(q_add((2, 1), p), q(6))
    return [x0] + [x1] * 8


def noisy_ququint_rho2_moments(p: Rat, k_max: int = 9) -> dict[str, Any]:
    """
    Exact Q(sqrt(5)) computation of ALL rescaled Wigner moments m_k (k=1..k_max)
    for the d=5 noisy ququint state rho_2(p) = p|psi_4><psi_4| + (1-p)I/5!
    Notice that because the (1+sqrt(5)) and (1-sqrt(5)) terms appear in EXACT
    Galois-conjugate pairs (8 of each!), EVERY moment m_k is 100% RATIONAL in Q!!
    """
    one_fifth = q(1, 5)
    c_base = q_mul(q_sub((1, 1), p), one_fifth)  # (1-p)/5
    # 25 phase-space points x_u = 5 * W_u(p) in Q(sqrt(5)):
    # 1 point: p*1 + (1-p)/5 = (4p + 1)/5
    # 4 points: p*(1/5) + (1-p)/5 = 1/5
    # 4 points: p*0 + (1-p)/5 = (1-p)/5
    # 8 points: p*(1+sqrt(5))/5 + (1-p)/5 = 1/5 + (p/5)*sqrt(5)
    # 8 points: p*(1-sqrt(5))/5 + (1-p)/5 = 1/5 - (p/5)*sqrt(5)
    groups: list[tuple[int, Q5]] = [
        (1, q5(q_add(p, c_base))),
        (4, q5(one_fifth)),
        (4, q5(c_base)),
        (8, q5(one_fifth, q_mul(p, one_fifth))),
        (8, q5(one_fifth, q_neg(q_mul(p, one_fifth)))),
    ]
    ms: list[Rat] = []
    for k in range(k_max + 1):
        acc: Q5 = ((0, 1), (0, 1))
        for mult, val in groups:
            pw = q5_pow(val, k)
            term = (q_mul(q(mult), pw[0]), q_mul(q(mult), pw[1]))
            acc = q5_add(acc, term)
        if acc[1][0] != 0:
            raise AssertionError("Galois conjugate sqrt(5) cancellation failed!")
        ms.append(q_mul(one_fifth, acc[0]))

    # Exact negativity in Q(sqrt(5)): only the 8 points (1/5 - (p/5)*sqrt(5)) can be negative (when 5 p^2 > 1)
    neg_pt = groups[4][1]
    is_neg = q5_is_neg(neg_pt)
    # N(p) = (8/5) * ((p/5)*sqrt(5) - 1/5) = (8/25)*(p*sqrt(5) - 1) if 5p^2 > 1 else 0
    return {
        "p": q_list(p),
        "is_wigner_negative": is_neg,
        "exact_N_q5": [q_list(q(-8, 25)), q_list(q_mul(q(8, 25), p))] if is_neg else [[0, 1], [0, 1]],
        "moments_exact_Q": ms,
    }


def verify_higher_even_holder_monotonicity(D: int, xs: list[Rat], k_vals: list[int]) -> dict[str, Any]:
    """
    Theorem 4 exact certificate:
    For each integer k >= 2, B_{2k}^{2k-2} = (P^{2k-1}) / m_{2k} <= (1 + 2N)^{2k-2}.
    Checks exact rational inequality (P^{2k-1}/m_{2k})^{2k} >= (P^{2k+1}/m_{2k+2})^{2k-2}
    showing B_4 >= B_6 >= B_8 >= ... (strictly decreasing whenever |x_u| is non-constant on support!).
    """
    k_max = 2 * max(k_vals)
    ms = rescaled_moments_rational(D, xs, k_max)
    N = sum_negativity_rational(D, xs)
    l1_norm = q_add((1, 1), q_mul(q(2), N))
    P = ms[2]
    rows = []
    for k in k_vals:
        m2k = ms[2 * k]
        lhs_pow = q_div(q_pow(P, 2 * k - 1), m2k)  # = B_{2k}^{2k-2}
        rhs_pow = q_pow(l1_norm, 2 * k - 2)        # = ||W||_1^{2k-2}
        if q_cmp(lhs_pow, rhs_pow) > 0:
            raise AssertionError("Higher-even Holder bound violated!")
        rows.append(
            {
                "k": k,
                "order_2k": 2 * k,
                "B_2k_pow_2k_minus_2": q_list(lhs_pow),
                "l1_norm_pow_2k_minus_2": q_list(rhs_pow),
                "holder_valid": True,
            }
        )
    # Check pairwise reverse monotonicity: B_{2k} >= B_{2k+2} iff (B_{2k}^{2k-2})^{2k} >= (B_{2k+2}^{2k})^{2k-2}
    monotone_checks = []
    for idx in range(len(k_vals) - 1):
        k1 = k_vals[idx]
        k2 = k_vals[idx + 1]
        a1 = q_div(q_pow(P, 2 * k1 - 1), ms[2 * k1])
        a2 = q_div(q_pow(P, 2 * k2 - 1), ms[2 * k2])
        lhs = q_pow(a1, 2 * k2 - 2)
        rhs = q_pow(a2, 2 * k1 - 2)
        cmp_res = q_cmp(lhs, rhs)
        if cmp_res < 0:
            raise AssertionError("Reverse monotonicity B_{2k} >= B_{2k+2} violated!")
        monotone_checks.append(
            {
                "pair": [2 * k1, 2 * k2],
                "strict_drop": cmp_res > 0,
                "non_increasing": cmp_res >= 0,
            }
        )
    return {
        "N_exact": q_list(N),
        "l1_norm_exact": q_list(l1_norm),
        "orders": rows,
        "reverse_monotonicity": monotone_checks,
    }
