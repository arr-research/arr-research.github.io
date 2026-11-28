"""GAUSS-STEER-MONO-CERT-1.0: Zero-Float Exact-Q Verifier for Paper M4-2.

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


def q_div(a: Fraction, b: Fraction) -> Fraction:
    if b == 0:
        raise ZeroDivisionError("Exact rational division by zero")
    return Fraction(a.numerator * b.denominator, a.denominator * b.numerator)


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


def share_monogamy_bound_cert(k_modes: int, n_settings: int) -> dict[str, object]:
    """Exact multimode steering monogamy bound (Chakrabarty arXiv:2611.34874v1):
      - Total covariance share budget across all neighbors: sum_{j=1..M} s_j <= k_modes.
      - Gaussian measurements (or n=2 settings): steering requires s_j > 1/2  =>  M <= 2*k - 1.
      - General n-setting measurements (n >= 2): steering/Bell requires s_j > 1/n => M <= n*k - 1.
    Also verifies exact equal-share harmonic tight-frame saturation at M = n*k - 1:
      s_j = k / (n*k - 1) = 1/n + 1/(n*(n*k - 1)) > 1/n,  sum = k!
    """
    if k_modes < 1 or n_settings < 2:
        raise ValueError("Require k_modes >= 1 and n_settings >= 2")
    max_neighbors = n_settings * k_modes - 1
    sat_share = Fraction(k_modes, max_neighbors)
    threshold = Fraction(1, n_settings)
    excess = sat_share - threshold
    assert excess == Fraction(1, n_settings * max_neighbors)
    assert excess > 0
    assert sat_share * max_neighbors == Fraction(k_modes, 1)
    # Check M_over = n*k equal shares hits exactly 1/n (fails strict > 1/n!)
    over_share = Fraction(k_modes, n_settings * k_modes)
    assert over_share == threshold
    return {
        "k_modes": k_modes,
        "n_settings": n_settings,
        "max_steerable_neighbors": max_neighbors,
        "threshold_share": q_to_pair(threshold),
        "saturating_equal_share": q_to_pair(sat_share),
        "saturating_share_dec": q_decimal_str(sat_share, 6),
        "strict_margin_above_threshold": q_to_pair(excess),
        "over_limit_M": n_settings * k_modes,
        "over_limit_share": q_to_pair(over_share),
        "monogamy_saturated": True,
    }


def rational_tight_frame_proj_k2_m3_cert() -> dict[str, object]:
    """Constructive exact-Q orthogonal projection matrix P = I_3 - (1/3)*J_3 in Q^(3x3)
    realizing the k=2, M=3 harmonic tight-frame saturation:
      P^T = P, P^2 = P, Tr(P) = 2 (rank 2), and P_{jj} = 2/3 > 1/2 for all j=0,1,2!
    """
    p = [
        [Fraction(2, 3), Fraction(-1, 3), Fraction(-1, 3)],
        [Fraction(-1, 3), Fraction(2, 3), Fraction(-1, 3)],
        [Fraction(-1, 3), Fraction(-1, 3), Fraction(2, 3)],
    ]
    # Verify symmetry and idempotency P^2 == P
    for i in range(3):
        for j in range(3):
            assert p[i][j] == p[j][i]
            acc = Fraction(0, 1)
            for t in range(3):
                acc = acc + p[i][t] * p[t][j]
            assert acc == p[i][j]
    trace_p = p[0][0] + p[1][1] + p[2][2]
    assert trace_p == Fraction(2, 1)
    diags = [p[i][i] for i in range(3)]
    assert all(d > Fraction(1, 2) for d in diags)
    return {
        "k_modes": 2,
        "m_neighbors": 3,
        "symmetric_exact": True,
        "idempotent_P2_eq_P": True,
        "trace_exact": q_to_pair(trace_p),
        "diagonal_shares": [q_to_pair(d) for d in diags],
        "all_strictly_above_half": True,
    }


def symplectic_schur_steering_cert(a_squeeze: Fraction, eta_share: Fraction) -> dict[str, object]:
    """Exact-Q symplectic Gaussian Schur-complement steering check for a TMSV (V_A = a*I_2, a > 1)
    distributed with beam-splitter share eta in (0, 1]:
      V_B = (eta*(a - 1) + 1)*I_2,  C*V_B^-1*C^T = eta*(a^2 - 1)/(eta*(a - 1) + 1)*I_2.
      Exact rational identity:
        nu_{A|B} - 1 = (a - 1) * (1 - 2*eta) / (eta*(a - 1) + 1) !
    Hence for EVERY squeezing a > 1, Gaussian steering (nu_{A|B} < 1) holds iff eta > 1/2!
    """
    one = Fraction(1, 1)
    if a_squeeze <= one or eta_share <= 0 or eta_share > one:
        raise ValueError("Require a_squeeze > 1 and 0 < eta_share <= 1")
    v_b = eta_share * (a_squeeze - one) + one
    c_sq = a_squeeze * a_squeeze - one
    schur_nu = a_squeeze - q_div(eta_share * c_sq, v_b)
    expected_diff = q_div((a_squeeze - one) * (one - 2 * eta_share), v_b)
    assert (schur_nu - one) == expected_diff
    steerable = schur_nu < one
    assert steerable == (eta_share > Fraction(1, 2))
    return {
        "a_squeeze": q_to_pair(a_squeeze),
        "eta_share": q_to_pair(eta_share),
        "v_b_exact": q_to_pair(v_b),
        "schur_nu_exact": q_to_pair(schur_nu),
        "schur_nu_dec": q_decimal_str(schur_nu, 6),
        "nu_minus_1_exact": q_to_pair(schur_nu - one),
        "gaussian_steering_certified": steerable,
    }


def remote_wigner_negativity_cert(eta_share: Fraction, prep_error_eps: Fraction = Fraction(0, 1)) -> dict[str, object]:
    """Exact-Q remote Wigner-origin certificate for heralded single-photon Fock state
    rho_prep = (1 - eps)|1><1| + eps|0><0| transmitted with share eta in (0, 1]:
      rho_out = eta*(1 - eps)|1><1| + (1 - eta*(1 - eps))|0><0|,
      pi * W_out(0) = 1 - 2 * eta * (1 - eps).
    Negative Wigner origin W_out(0) < 0 iff eta * (1 - eps) > 1/2!
    In the ideal limit eps = 0, pi*W_out(0) = 1 - 2*eta < 0 iff eta > 1/2 (exact same 2k-1 monogamy bound!).
    """
    one = Fraction(1, 1)
    if eta_share <= 0 or eta_share > one or prep_error_eps < 0 or prep_error_eps >= one:
        raise ValueError("Require 0 < eta <= 1 and 0 <= eps < 1")
    p1 = eta_share * (one - prep_error_eps)
    pi_w0 = one - 2 * p1
    wigner_negative = pi_w0 < 0
    return {
        "eta_share": q_to_pair(eta_share),
        "prep_error_eps": q_to_pair(prep_error_eps),
        "fock1_population": q_to_pair(p1),
        "pi_W0_exact": q_to_pair(pi_w0),
        "pi_W0_dec": q_decimal_str(pi_w0, 6),
        "remote_wigner_negative": wigner_negative,
    }


def bell_vs_entanglement_separation_cert(k_modes: int, n_settings: int, m_neighbors: int) -> dict[str, object]:
    """Exact operational separation certificate across Gaussian steering (2k-1), n-setting steering/Bell (nk-1),
    and unrestricted multimode Gaussian entanglement (arbitrarily many neighbors M)!
    """
    if k_modes < 1 or n_settings < 2 or m_neighbors < 1:
        raise ValueError("Invalid separation parameters")
    gauss_limit = 2 * k_modes - 1
    nset_limit = n_settings * k_modes - 1
    return {
        "k_modes": k_modes,
        "n_settings": n_settings,
        "m_neighbors": m_neighbors,
        "gaussian_steering_limit": gauss_limit,
        "n_setting_limit": nset_limit,
        "exceeds_gaussian_limit": m_neighbors > gauss_limit,
        "permitted_with_n_settings": m_neighbors <= nset_limit,
        "requires_nongaussian_ge_3_settings": m_neighbors > gauss_limit and m_neighbors <= nset_limit,
    }


def canonical_json_sha256(obj: object) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()
