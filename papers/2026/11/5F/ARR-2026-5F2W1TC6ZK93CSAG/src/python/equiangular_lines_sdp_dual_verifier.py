"""EQUILINE-SDP-DUAL-CERT-1.0: Zero-Float Exact-Q Verifier for Paper M3-1.

Strict AST hygiene:
  - Zero float literals or float() calls
  - Zero numeric '/' (BinOp Div) or '**' (BinOp Pow) operators
  - Zero Fraction.limit_denominator calls
  - Standard library only (fractions.Fraction, hashlib, json)
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json


def q(n: int, d: int = 1) -> Fraction:
    return Fraction(n, d)


def q_sq(a: Fraction) -> Fraction:
    return a * a


def q_div(a: Fraction, b: Fraction) -> Fraction:
    if b == 0:
        raise ZeroDivisionError("Exact rational division by zero")
    return Fraction(a.numerator * b.denominator, a.denominator * b.numerator)


def q_inv(a: Fraction) -> Fraction:
    return q_div(Fraction(1, 1), a)


def q_abs(a: Fraction) -> Fraction:
    return -a if a < 0 else a


def q_to_pair(x: Fraction) -> list[int]:
    return [x.numerator, x.denominator]


def q_decimal_str(x: Fraction, digits: int = 6) -> str:
    sign = "-" if x < 0 else ""
    ax = q_abs(x)
    scale = 1
    for _ in range(digits):
        scale = scale * 10
    scaled = (ax.numerator * scale) // ax.denominator
    int_part = scaled // scale
    frac_part = scaled % scale
    return f"{sign}{int_part}.{str(frac_part).zfill(digits)}"


def floor_q(x: Fraction) -> int:
    return x.numerator // x.denominator


def gerzon_bound(d: int) -> int:
    if d <= 0:
        raise ValueError("Dimension d must be positive")
    return (d * (d + 1)) // 2


def relative_bound_exact(d: int, alpha_sq: Fraction) -> dict[str, object]:
    """Exact Lemmens-Seidel relative bound N_alpha(d) <= d*(1 - alpha^2) / (1 - d*alpha^2)
    valid strictly when d*alpha^2 < 1.
    """
    one = Fraction(1, 1)
    if d <= 1 or alpha_sq <= 0 or alpha_sq >= one:
        raise ValueError("Require d >= 2 and 0 < alpha^2 < 1")
    denom = one - d * alpha_sq
    if denom <= 0:
        return {
            "d": d,
            "alpha_sq": q_to_pair(alpha_sq),
            "valid": False,
            "bound_exact": None,
            "bound_floor": None,
        }
    val = q_div(d * (one - alpha_sq), denom)
    return {
        "d": d,
        "alpha_sq": q_to_pair(alpha_sq),
        "valid": True,
        "bound_exact": q_to_pair(val),
        "bound_dec": q_decimal_str(val, 4),
        "bound_floor": floor_q(val),
        "gerzon_bound": gerzon_bound(d),
    }


def gegenbauer_g2(d: int, t_sq: Fraction) -> Fraction:
    """Normalized ultraspherical polynomial G_2^(d)(t) = (d*t^2 - 1) / (d - 1)."""
    return q_div(d * t_sq - Fraction(1, 1), Fraction(d - 1, 1))


def gegenbauer_g4(d: int, t_sq: Fraction) -> Fraction:
    """Normalized ultraspherical polynomial G_4^(d)(t) = ((d+2)(d+4)t^4 - 6(d+2)t^2 + 3) / ((d-1)(d+1))."""
    num = (d + 2) * (d + 4) * q_sq(t_sq) - 6 * (d + 2) * t_sq + Fraction(3, 1)
    den = Fraction((d - 1) * (d + 1), 1)
    return q_div(num, den)


def gegenbauer_g6(d: int, t_sq: Fraction) -> Fraction:
    """Normalized ultraspherical polynomial G_6^(d)(t) satisfying E[G_6] = E[t^2 G_6] = E[t^4 G_6] = 0, G_6(1) = 1.

    Explicit formula on S^(d-1):
      num = (d+4)(d+6)(d+8) t^6 - 15 (d+4)(d+6) t^4 + 45 (d+4) t^2 - 15
      den = (d-1)(d+1)(d+3)
    Check at t=1:
      (d+4)((d+6)(d+8) - 15(d+6) + 45) - 15
      = (d+4)(d^2 + 14d + 48 - 15d - 90 + 45) - 15
      = (d+4)(d^2 - d + 3) - 15 = d^3 + 3d^2 - d - 3 = (d-1)(d+1)(d+3)!
    """
    t4 = q_sq(t_sq)
    t6 = t4 * t_sq
    num = (
        (d + 4) * (d + 6) * (d + 8) * t6
        - 15 * (d + 4) * (d + 6) * t4
        + 45 * (d + 4) * t_sq
        - Fraction(15, 1)
    )
    den = Fraction((d - 1) * (d + 1) * (d + 3), 1)
    return q_div(num, den)


def sdp_dual_gegenbauer_cert(
    d: int,
    alpha_sq: Fraction,
    c2: Fraction,
    c4: Fraction,
    c6: Fraction,
) -> dict[str, object]:
    """Exact Delsarte-Yu even-degree Gegenbauer SDP dual certificate for equiangular lines.

    Given c2, c4, c6 >= 0, define F(t) = c0 + c2*G2(t) + c4*G4(t) + c6*G6(t)
    with c0 := -(c2*G2(alpha) + c4*G4(alpha) + c6*G6(alpha)).
    If c0 > 0, then F(+-alpha) = 0 <= 0, all Gegenbauer weights >= 0, and
      N_alpha(d) <= F(1) / c0 = 1 + (c2 + c4 + c6) / c0!
    """
    if d <= 2 or alpha_sq <= 0 or alpha_sq >= Fraction(1, 1):
        raise ValueError("Require d >= 3 and 0 < alpha^2 < 1")
    if c2 < 0 or c4 < 0 or c6 < 0:
        raise ValueError("Gegenbauer dual weights must be non-negative")
    g2 = gegenbauer_g2(d, alpha_sq)
    g4 = gegenbauer_g4(d, alpha_sq)
    g6 = gegenbauer_g6(d, alpha_sq)
    c0 = -(c2 * g2 + c4 * g4 + c6 * g6)
    valid = c0 > 0
    if not valid:
        return {
            "d": d,
            "alpha_sq": q_to_pair(alpha_sq),
            "c2": q_to_pair(c2),
            "c4": q_to_pair(c4),
            "c6": q_to_pair(c6),
            "G2": q_to_pair(g2),
            "G4": q_to_pair(g4),
            "G6": q_to_pair(g6),
            "c0": q_to_pair(c0),
            "valid": False,
            "sdp_bound_exact": None,
            "sdp_bound_floor": None,
        }
    f_at_alpha = c0 + c2 * g2 + c4 * g4 + c6 * g6
    assert f_at_alpha == Fraction(0, 1)
    f_at_1 = c0 + c2 + c4 + c6
    bound = q_div(f_at_1, c0)
    return {
        "d": d,
        "alpha_sq": q_to_pair(alpha_sq),
        "c2": q_to_pair(c2),
        "c4": q_to_pair(c4),
        "c6": q_to_pair(c6),
        "G2": q_to_pair(g2),
        "G4": q_to_pair(g4),
        "G6": q_to_pair(g6),
        "c0": q_to_pair(c0),
        "F_at_alpha": q_to_pair(f_at_alpha),
        "F_at_1": q_to_pair(f_at_1),
        "valid": True,
        "sdp_bound_exact": q_to_pair(bound),
        "sdp_bound_dec": q_decimal_str(bound, 4),
        "sdp_bound_floor": floor_q(bound),
    }


def odd_q_compression_barrier_cert(d: int, q_odd: int, excess_e: int) -> dict[str, object]:
    """Exact odd-q compression barrier:
    For odd q >= 3, q^2 > d, and target forbidden excess e >= 1:
      N_{1/q}(d) <= d + e - 1  iff  d^2 + (e - 1)*d < e * q^2!
    Also computes the exact maximum dimension d_max(q, e) certified to satisfy N_{1/q}(d) <= d + e - 1.
    """
    if d <= 0 or q_odd < 3 or q_odd % 2 == 0 or excess_e < 1:
        raise ValueError("Require d > 0, odd q >= 3, excess_e >= 1")
    lhs = d * d + (excess_e - 1) * d
    rhs = excess_e * q_odd * q_odd
    certified = (q_odd * q_odd > d) and (lhs < rhs)
    rel = relative_bound_exact(d, Fraction(1, q_odd * q_odd))
    if certified:
        assert rel["valid"] is True and rel["bound_floor"] <= d + excess_e - 1
    return {
        "d": d,
        "q_odd": q_odd,
        "excess_e": excess_e,
        "target_upper_bound": d + excess_e - 1,
        "lhs_d2_plus_em1_d": lhs,
        "rhs_e_q2": rhs,
        "strict_gap": rhs - lhs,
        "certified_le_d_plus_e_minus_1": certified,
        "relative_bound_floor": rel["bound_floor"],
    }


def regular_twograph_srg_cert(d: int, n: int, a_int: int) -> dict[str, object]:
    """Exact regular two-graph & descendant SRG(n-1, k, lam, mu) feasibility certificate
    at cosine 1/a_int in dimension d with n lines (relative bound saturation check).

    For Gram matrix G = I_n + (1/a)*S of rank d with two eigenvalues 0 (mult n-d) and L (mult d):
      S has eigenvalues -a (mult n-d) and b = a*(n-d)/d (mult d).
      Descendant SRG has v = n-1, restricted eigenvalues r = (a - 1)/2, s = (-1 - b)/2,
      degree k = (v - (b - a))/2, mu = k + r*s, lam = mu + r + s.
    """
    if d <= 0 or n <= d or a_int <= 1:
        raise ValueError("Require 0 < d < n and a_int >= 2")
    num_b = a_int * (n - d)
    b_is_int = (num_b % d == 0)
    b_val = num_b // d if b_is_int else -1
    trace_zero = b_is_int and (d * b_val == (n - d) * a_int)
    tr_s2_exact = b_is_int and (d * b_val * b_val + (n - d) * a_int * a_int == n * (n - 1))
    v = n - 1
    descendant_valid = False
    srg_params: dict[str, int] | None = None
    if trace_zero and tr_s2_exact and ((a_int - 1) % 2 == 0) and ((b_val + 1) % 2 == 0) and ((v - 1 - (b_val - a_int)) % 2 == 0):
        r = (a_int - 1) // 2
        s = -(b_val + 1) // 2
        k = (v - 1 - (b_val - a_int)) // 2
        mu = k + r * s
        lam = mu + r + s
        param_eq = (k * (k - lam - 1) == mu * (v - k - 1))
        descendant_valid = param_eq and (0 <= lam < k < v) and (0 <= mu <= k)
        srg_params = {"v": v, "k": k, "lambda": lam, "mu": mu, "r": r, "s": s}
    return {
        "d": d,
        "n": n,
        "a": a_int,
        "b_is_integer": b_is_int,
        "b_eigenvalue": b_val if b_is_int else None,
        "trace_zero": trace_zero,
        "tr_S2_matches_n_nm1": tr_s2_exact,
        "descendant_srg_arithmetically_feasible": descendant_valid,
        "descendant_srg": srg_params,
    }


def kronecker_seidel_block_cert(m: int, k_reg: int, r_blocks: int, mu_q_block: int) -> dict[str, object]:
    """Exact Kronecker repeated-Seidel-block construction S = I_r (x) S_0 + (J_r - I_r) (x) J_m.

    For a k-regular graph G_0 on m vertices:
      theta_0 = m - 1 - 2*k, so block-constant off-mode eigenvalue is theta_0 - m = -(2*k + 1) = -q_odd!
      With r blocks (n = r*m) and assuming lambda_min(S_0) >= -q_odd with multiplicity mu_q_block:
        multiplicity of -q_odd in S is (r - 1) + r * mu_q_block,
        realizing n = r*m equiangular lines at cosine 1/(2*k + 1) in dimension d = n - nullity!
    """
    if m <= 1 or k_reg < 0 or k_reg >= m or r_blocks < 1 or mu_q_block < 0:
        raise ValueError("Invalid block parameters")
    q_odd = 2 * k_reg + 1
    theta0 = m - 1 - 2 * k_reg
    assert theta0 - m == -q_odd
    n = r_blocks * m
    nullity = (r_blocks - 1) + r_blocks * mu_q_block
    d = n - nullity
    if d <= 0:
        raise ValueError("Nullity must be strictly less than n")
    return {
        "m": m,
        "k_reg": k_reg,
        "r_blocks": r_blocks,
        "q_odd": q_odd,
        "theta0": theta0,
        "top_eigenvalue": theta0 + (r_blocks - 1) * m,
        "n_lines": n,
        "nullity_excess": nullity,
        "dimension_d": d,
    }


def conference_matrix_family_cert(d: int) -> dict[str, object]:
    """Symmetric conference matrix family of order n = 2*d (n = 2 mod 4, so d odd >= 3):
    C^T = C, C^2 = (n - 1)*I_n => G = I_n + (1/sqrt(n-1))*C has eigenvalues 0 (mult d) and 2 (mult d),
    achieving n = 2*d equiangular lines at quadratic irrational cosine alpha = 1/sqrt(2*d - 1),
    saturating the relative bound d*(1 - 1/(2d-1)) / (1 - d/(2d-1)) = d*(2d-2)/(d-1) = 2*d identically!
    """
    if d < 3 or d % 2 == 0:
        raise ValueError("Symmetric conference matrix requires odd d >= 3 (n = 2d = 2 mod 4)")
    n = 2 * d
    alpha_sq = Fraction(1, n - 1)
    rel = relative_bound_exact(d, alpha_sq)
    assert rel["valid"] is True and rel["bound_exact"] == [n, 1]
    return {
        "d": d,
        "n_lines": n,
        "alpha_sq": q_to_pair(alpha_sq),
        "exact_relative_bound": rel["bound_exact"],
        "saturates_relative_bound": True,
    }


def canonical_json_sha256(obj: object) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()
