"""MITO-POLARITON-CHANNEL-CAPACITY-CERT-1.0: Zero-Float Exact-Q Verifier for Paper P6.

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


# Exact CODATA 2018 constants in rational form:
# h = 662607015 / 10^42 J*s  =>  h * 1 THz = 662607015 / 10^30 J
# k_B = 1380649 / 10^29 J/K
# At T = 310 K: k_B * T = 428001190 / 10^29 J = 42800119 / 10^28 J
# Exact ln(2) bracket: 693147 / 10^6 < ln(2) < 693148 / 10^6
LN2_LO = Fraction(693147, 1000000)
LN2_HI = Fraction(693148, 1000000)


def ln_bracket(y: Fraction) -> tuple[Fraction, Fraction]:
    """Exact rational lower/upper bracket for ln(y) for any y >= 1 via dyadic reduction.

    Write y = 2^m * (1 + u) with u in [0, 1).
    Then for u in [0, 1):
      2*u / (2 + u) <= ln(1 + u) <= u - u^2/2 + u^3/3  (and <= u).
    For tighter accuracy on u in [0, 1), use exact alternating Mercator up to degree 7 when u <= 1/2,
    or exact rational Padé/elementary 2*u/(2+u) <= ln(1+u) <= u*(6+u)/(6+4*u)?
    Wait: check u*(6+u)/(6+4*u) vs ln(1+u)! At u=1: 7/10 = 0.7 > ln(2) = 0.693147!
    Even simpler and 100% unconditionally elementary:
      2*u / (2 + u) <= ln(1 + u) <= u * (2 + u) / (2 * (1 + u))? Wait: at u=1, 3/4 = 0.75 > ln(2).
    Check 6-step halving of (1+u) or exact (1+u) -> split at 1/2:
      if u < 1/2: alternating series u - u^2/2 + u^3/3 - u^4/4 <= ln(1+u) <= u - u^2/2 + u^3/3!
      if u >= 1/2: write 1+u = (3/2) * (1 + v) with v in [0, 1/3), using 405465/1000000 < ln(3/2) < 405466/1000000!
    """
    if y < Fraction(1, 1):
        raise ValueError("Require y >= 1")
    if y == Fraction(1, 1):
        return (Fraction(0, 1), Fraction(0, 1))
    m = 0
    rem = y
    half = Fraction(1, 2)
    two = Fraction(2, 1)
    while rem >= two:
        rem = rem * half
        m = m + 1
    u = rem - Fraction(1, 1)
    if u < half:
        u2 = u * u
        u3 = u2 * u
        u4 = u3 * u
        u5 = u4 * u
        u6 = u5 * u
        u7 = u6 * u
        u8 = u7 * u
        base = (
            u
            - q_div(u2, Fraction(2, 1))
            + q_div(u3, Fraction(3, 1))
            - q_div(u4, Fraction(4, 1))
            + q_div(u5, Fraction(5, 1))
            - q_div(u6, Fraction(6, 1))
            + q_div(u7, Fraction(7, 1))
        )
        lo_u = base - q_div(u8, Fraction(8, 1))
        hi_u = base
    else:
        # 1 + u = (3/2) * (1 + v) => v = (2*u - 1)/3 in [0, 1/3)
        v = q_div(2 * u - Fraction(1, 1), Fraction(3, 1))
        v2 = v * v
        v3 = v2 * v
        v4 = v3 * v
        v5 = v4 * v
        v6 = v5 * v
        v7 = v6 * v
        v8 = v7 * v
        ln32_lo = Fraction(405465108, 1000000000)
        ln32_hi = Fraction(405465109, 1000000000)
        base = (
            v
            - q_div(v2, Fraction(2, 1))
            + q_div(v3, Fraction(3, 1))
            - q_div(v4, Fraction(4, 1))
            + q_div(v5, Fraction(5, 1))
            - q_div(v6, Fraction(6, 1))
            + q_div(v7, Fraction(7, 1))
        )
        lo_u = ln32_lo + base - q_div(v8, Fraction(8, 1))
        hi_u = ln32_hi + base
    return (m * LN2_LO + lo_u, m * LN2_HI + hi_u)


def bosonic_g_bracket(x: Fraction) -> tuple[Fraction, Fraction]:
    """Exact rational lower/upper bracket on bosonic entropy g(x) = (x+1)ln(x+1) - x ln(x) for x >= 0.

    Rewrite identically for x > 0:
      g(x) = ln(1 + x) + x * ln(1 + 1/x).
    Both arguments (1 + x) >= 1 and (1 + 1/x) > 1 lie in [1, infty)!
    """
    if x < 0:
        raise ValueError("Require x >= 0")
    if x == 0:
        return (Fraction(0, 1), Fraction(0, 1))
    a_lo, a_hi = ln_bracket(Fraction(1, 1) + x)
    b_lo, b_hi = ln_bracket(Fraction(1, 1) + q_inv(x))
    return (a_lo + x * b_lo, a_hi + x * b_hi)


def bosonic_channel_capacity_cert(
    eta: Fraction,
    n_s: Fraction,
    n_b: Fraction,
    freq_thz: Fraction,
    temp_k: Fraction,
) -> dict[str, object]:
    """Exact Giovannetti-Holevo classical capacity, heterodyne ceiling, quantum PLOB wall,
    and Landauer-Holevo energy-per-bit floor for thermal-loss channel E_{eta, N_B}.
    """
    one = Fraction(1, 1)
    if eta <= 0 or eta > one or n_s <= 0 or n_b < 0 or freq_thz <= 0 or temp_k <= 0:
        raise ValueError("Invalid channel parameters")

    x0 = (one - eta) * n_b
    x1 = eta * n_s + x0
    g1_lo, g1_hi = bosonic_g_bracket(x1)
    g0_lo, g0_hi = bosonic_g_bracket(x0)

    # Exact Holevo capacity bracket in nats/use: C_nat = g(x1) - g(x0)
    c_nat_lo = g1_lo - g0_hi
    c_nat_hi = g1_hi - g0_lo
    if c_nat_lo < 0:
        c_nat_lo = Fraction(0, 1)

    # Pure-loss ceiling g(eta * n_s) >= C_nat(eta, n_s, n_b)
    gp_lo, gp_hi = bosonic_g_bracket(eta * n_s)
    assert c_nat_lo <= gp_hi

    # Concavity tangent upper bound (when x0 > 0): C_nat <= eta * n_s * ln(1 + 1/x0)
    if x0 > 0:
        _, ln_tang_hi = ln_bracket(one + q_inv(x0))
        c_tang_ub = eta * n_s * ln_tang_hi
        assert c_nat_lo <= c_tang_ub
    else:
        c_tang_ub = gp_hi

    # Convert to bits/use using LN2_LO < ln(2) < LN2_HI
    c_bit_lo = q_div(c_nat_lo, LN2_HI)
    c_bit_hi = q_div(c_nat_hi, LN2_LO)

    # Heterodyne (incoherent classical receiver) Shannon capacity: ln(1 + eta*n_s / (x0 + 1))
    snr_het = q_div(eta * n_s, x0 + one)
    chet_nat_lo, chet_nat_hi = ln_bracket(one + snr_het)
    chet_bit_lo = q_div(chet_nat_lo, LN2_HI)
    chet_bit_hi = q_div(chet_nat_hi, LN2_LO)
    assert chet_nat_lo <= eta * n_s
    assert chet_nat_lo <= c_nat_hi

    # Unassisted quantum capacity Q (Wolf-Perez-Garcia-Giedke 2007):
    #   Q = 0 identically for eta <= 1/2 (antidegradable);
    #   for eta > 1/2, Q <= log2(eta / (1 - eta)) (continuous at eta = 1/2, vanishes smoothly!)
    #   and for finite N_S, Q <= C_Hol(eta, N_S, N_B).
    # Two-way LOCC-assisted quantum capacity Q_2 (PLOB 2017):
    #   Q_2 <= -log2(1 - eta) for all eta in (0, 1).
    half = Fraction(1, 2)
    q_zero_antidegradable = eta <= half
    if eta == one:
        q_unassisted_ub_bits = Fraction(-1, 1)  # Unbounded (lossless)
        q2_plob_ub_bits = Fraction(-1, 1)
    else:
        _, ln_inv_hi = ln_bracket(q_inv(one - eta))
        q2_plob_ub_bits = q_div(ln_inv_hi, LN2_LO)
        if q_zero_antidegradable:
            q_unassisted_ub_bits = Fraction(0, 1)
        else:
            _, ln_ratio_hi = ln_bracket(q_div(eta, one - eta))
            q_unassisted_ub_bits = q_div(ln_ratio_hi, LN2_LO)

    # Energy per bit in zeptojoules (1 zJ = 10^-21 J):
    # h * 1 THz = 662607015 / 10^9 zJ, k_B * 1 K = 1380649 / 10^8 zJ
    h_thz_zj = Fraction(662607015, 1000000000)
    kb_k_zj = Fraction(1380649, 100000000)
    e_photon_zj = freq_thz * h_thz_zj
    kbt_zj = temp_k * kb_k_zj
    beta_hnu = q_div(e_photon_zj, kbt_zj)

    # Energy per bit = (n_s * e_photon_zj) / C_bits
    e_bit_holevo_lo_zj = q_div(n_s * e_photon_zj, c_bit_hi) if c_bit_hi > 0 else Fraction(0, 1)
    e_bit_het_lo_zj = q_div(n_s * e_photon_zj, chet_bit_hi) if chet_bit_hi > 0 else Fraction(0, 1)
    # Exact tangent-corrected Holevo floor for 0 < eta < 1, N_B > 0:
    #   E_bit^Hol >= h*nu*ln(2) / [eta * ln(1 + 1/((1-eta)*N_B))]
    # At eta = 1 (pure lossless channel with unbounded bandwidth), inf_{N_S>0} E_bit^Hol = 0!
    # Separate thermal receiver Landauer erasure floor = k_B * T * ln(2) (independent of eta).
    if x0 > 0:
        _, ln_tang_hi_val = ln_bracket(one + q_inv(x0))
        exact_holevo_channel_floor_zj = q_div(e_photon_zj * LN2_LO, eta * ln_tang_hi_val)
    else:
        exact_holevo_channel_floor_zj = Fraction(0, 1)
    landauer_erasure_floor_zj = kbt_zj * LN2_LO
    het_floor_zj = q_div(e_photon_zj * LN2_LO, eta)
    hom_floor_zj = het_floor_zj * half

    return {
        "eta": q_to_pair(eta),
        "N_S": q_to_pair(n_s),
        "N_B": q_to_pair(n_b),
        "freq_THz": q_to_pair(freq_thz),
        "T_K": q_to_pair(temp_k),
        "beta_hnu_dec": q_decimal_str(beta_hnu, 4),
        "beta_hnu_exact": q_to_pair(beta_hnu),
        "C_holevo_bits_lo": q_decimal_str(c_bit_lo, 6),
        "C_holevo_bits_hi": q_decimal_str(c_bit_hi, 6),
        "C_holevo_bits_lo_exact": q_to_pair(c_bit_lo),
        "C_holevo_bits_hi_exact": q_to_pair(c_bit_hi),
        "C_het_bits_lo": q_decimal_str(chet_bit_lo, 6),
        "C_het_bits_hi": q_decimal_str(chet_bit_hi, 6),
        "C_het_bits_hi_exact": q_to_pair(chet_bit_hi),
        "C_tangent_ub_nats_exact": q_to_pair(c_tang_ub),
        "Q_zero_antidegradable": q_zero_antidegradable,
        "Q_unassisted_ub_bits_exact": q_to_pair(q_unassisted_ub_bits),
        "Q_unassisted_ub_bits_dec": q_decimal_str(q_unassisted_ub_bits, 4) if q_unassisted_ub_bits >= 0 else "unbounded",
        "Q2_plob_ub_bits_exact": q_to_pair(q2_plob_ub_bits),
        "Q2_plob_ub_bits_dec": q_decimal_str(q2_plob_ub_bits, 4) if q2_plob_ub_bits >= 0 else "unbounded",
        "E_bit_holevo_lo_zJ_dec": q_decimal_str(e_bit_holevo_lo_zj, 4),
        "E_bit_holevo_lo_zJ_exact": q_to_pair(e_bit_holevo_lo_zj),
        "E_bit_het_lo_zJ_dec": q_decimal_str(e_bit_het_lo_zj, 4),
        "E_bit_het_lo_zJ_exact": q_to_pair(e_bit_het_lo_zj),
        "exact_holevo_channel_floor_zJ_dec": q_decimal_str(exact_holevo_channel_floor_zj, 4),
        "exact_holevo_channel_floor_zJ_exact": q_to_pair(exact_holevo_channel_floor_zj),
        "landauer_erasure_floor_zJ_dec": q_decimal_str(landauer_erasure_floor_zj, 4),
        "het_floor_zJ_dec": q_decimal_str(het_floor_zj, 4),
        "hom_floor_zJ_dec": q_decimal_str(hom_floor_zj, 4),
    }


def signaling_horizon_cert(
    p_sig_pw: Fraction,
    rate_bps: Fraction,
    e_bit0_zj: Fraction,
    l_att_um: Fraction,
) -> dict[str, object]:
    """Exact intracellular classical signaling horizon L_max = L_att * ln(P_sig / (R_min * E_bit0)).

    Unit conversion:
      1 pW = 10^-12 J/s = 10^9 zJ/s!
      So P_sig_zJ_per_s = p_sig_pw * 10^9.
      Budget per bit = P_sig_zJ_per_s / rate_bps [zJ/bit].
      Margin M = budget_per_bit / e_bit0_zj.
      If M <= 1: signaling is unconditionally forbidden even at zero loss (eta = 1)!
      If M > 1: L_max = L_att * ln(M), bracketed exactly via ln_bracket(M)!
    """
    if p_sig_pw <= 0 or rate_bps <= 0 or e_bit0_zj <= 0 or l_att_um <= 0:
        raise ValueError("All horizon parameters must be positive")
    p_sig_zj_s = p_sig_pw * Fraction(1000000000, 1)
    budget_zj_bit = q_div(p_sig_zj_s, rate_bps)
    margin = q_div(budget_zj_bit, e_bit0_zj)
    one = Fraction(1, 1)
    if margin <= one:
        return {
            "P_sig_pW": q_to_pair(p_sig_pw),
            "R_min_bps": q_to_pair(rate_bps),
            "E_bit0_zJ": q_to_pair(e_bit0_zj),
            "L_att_um": q_to_pair(l_att_um),
            "budget_zJ_per_bit_dec": q_decimal_str(budget_zj_bit, 4),
            "margin_exact": q_to_pair(margin),
            "margin_dec": q_decimal_str(margin, 6),
            "feasible_zero_loss": False,
            "L_max_over_Latt_lo": "0.0000",
            "L_max_over_Latt_hi": "0.0000",
            "L_max_um_lo": "0.0000",
            "L_max_um_hi": "0.0000",
        }
    ln_lo, ln_hi = ln_bracket(margin)
    l_lo = l_att_um * ln_lo
    l_hi = l_att_um * ln_hi
    return {
        "P_sig_pW": q_to_pair(p_sig_pw),
        "R_min_bps": q_to_pair(rate_bps),
        "E_bit0_zJ": q_to_pair(e_bit0_zj),
        "L_att_um": q_to_pair(l_att_um),
        "budget_zJ_per_bit_dec": q_decimal_str(budget_zj_bit, 4),
        "margin_exact": q_to_pair(margin),
        "margin_dec": q_decimal_str(margin, 3),
        "feasible_zero_loss": True,
        "L_max_over_Latt_lo": q_decimal_str(ln_lo, 4),
        "L_max_over_Latt_hi": q_decimal_str(ln_hi, 4),
        "L_max_over_Latt_lo_exact": q_to_pair(ln_lo),
        "L_max_over_Latt_hi_exact": q_to_pair(ln_hi),
        "L_max_um_lo": q_decimal_str(l_lo, 4),
        "L_max_um_hi": q_decimal_str(l_hi, 4),
        "L_max_um_lo_exact": q_to_pair(l_lo),
        "L_max_um_hi_exact": q_to_pair(l_hi),
    }


def canonical_json_sha256(obj: object) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()
