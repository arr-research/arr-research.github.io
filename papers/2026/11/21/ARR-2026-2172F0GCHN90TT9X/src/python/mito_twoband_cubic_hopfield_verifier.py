"""MITO-TWOBAND-CUBIC-HOPFIELD-CERT-1.0: Zero-Float Exact-Q Verifier for Paper P4.

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


def q_mul(a: Fraction, b: Fraction) -> Fraction:
    return a * b


def q_sq(a: Fraction) -> Fraction:
    return a * a


def q_cube(a: Fraction) -> Fraction:
    return a * a * a


def q_div(a: Fraction, b: Fraction) -> Fraction:
    if b == 0:
        raise ZeroDivisionError("Exact rational division by zero")
    return Fraction(a.numerator * b.denominator, a.denominator * b.numerator)


def q_inv(a: Fraction) -> Fraction:
    return q_div(Fraction(1, 1), a)


def q_abs(a: Fraction) -> Fraction:
    return -a if a < 0 else a


def q_min(a: Fraction, b: Fraction) -> Fraction:
    return a if a <= b else b


def q_max(a: Fraction, b: Fraction) -> Fraction:
    return a if a >= b else b


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


def isqrt_bracket(x: Fraction, tol_den: int = 1000000) -> tuple[Fraction, Fraction]:
    """Exact rational lower/upper bracket [lo, hi] for sqrt(x) with hi - lo <= 1/tol_den."""
    if x < 0:
        raise ValueError("Negative radicand")
    if x == 0:
        return (Fraction(0, 1), Fraction(0, 1))
    # Find integer upper bound
    lo = Fraction(0, 1)
    hi = Fraction(1, 1)
    while q_sq(hi) < x:
        hi = hi + hi
    tol = Fraction(1, tol_den)
    half = Fraction(1, 2)
    while hi - lo > tol:
        mid = q_mul(lo + hi, half)
        if q_sq(mid) <= x:
            lo = mid
        else:
            hi = mid
    return (lo, hi)


def trk_diamagnetic_shift(g1: Fraction, w1: Fraction, g2: Fraction, w2: Fraction) -> Fraction:
    """Exact TRK diamagnetic shift D = g1^2 / w1 + g2^2 / w2."""
    return q_div(q_sq(g1), w1) + q_div(q_sq(g2), w2)


def cubic_hopfield_poly(
    x: Fraction,
    wc: Fraction,
    w1: Fraction,
    w2: Fraction,
    g1: Fraction,
    g2: Fraction,
) -> Fraction:
    """Exact gauge-invariant two-band cubic Hopfield secular polynomial P3(X).

    P3(X) = (X - wc^2 - 4*wc*D)*(X - w1^2)*(X - w2^2)
            - 4*wc*(g1^2*w1*(X - w2^2) + g2^2*w2*(X - w1^2))
    where D = g1^2/w1 + g2^2/w2.
    """
    d_trk = trk_diamagnetic_shift(g1, w1, g2, w2)
    wc2 = q_sq(wc)
    w12 = q_sq(w1)
    w22 = q_sq(w2)
    term1 = (x - wc2 - 4 * wc * d_trk) * (x - w12) * (x - w22)
    term2 = 4 * wc * (q_sq(g1) * w1 * (x - w22) + q_sq(g2) * w2 * (x - w12))
    return term1 - term2


def cubic_hopfield_poly_factored(
    x: Fraction,
    wc: Fraction,
    w1: Fraction,
    w2: Fraction,
    g1: Fraction,
    g2: Fraction,
) -> Fraction:
    """Exact TRK-cancelled factored form:
    P3(X) = (X - wc^2)(X - w1^2)(X - w2^2) - 4*wc*X*( (g1^2/w1)*(X - w2^2) + (g2^2/w2)*(X - w1^2) ).
    """
    wc2 = q_sq(wc)
    w12 = q_sq(w1)
    w22 = q_sq(w2)
    t1 = (x - wc2) * (x - w12) * (x - w22)
    t2 = 4 * wc * x * (q_div(q_sq(g1), w1) * (x - w22) + q_div(q_sq(g2), w2) * (x - w12))
    return t1 - t2


def vieta_invariants(
    wc: Fraction,
    w1: Fraction,
    w2: Fraction,
    g1: Fraction,
    g2: Fraction,
) -> dict[str, Fraction]:
    """Exact Vieta symmetric invariants (e1, e2, e3) of P3(X) = X^3 - e1*X^2 + e2*X - e3."""
    d_trk = trk_diamagnetic_shift(g1, w1, g2, w2)
    wc2 = q_sq(wc)
    w12 = q_sq(w1)
    w22 = q_sq(w2)
    e1 = wc2 + w12 + w22 + 4 * wc * d_trk
    e2 = (
        wc2 * (w12 + w22)
        + w12 * w22
        + 4 * wc * (q_div(q_sq(g1) * w22, w1) + q_div(q_sq(g2) * w12, w2))
    )
    e3 = wc2 * w12 * w22
    return {"e1": e1, "e2": e2, "e3": e3, "D_trk": d_trk}


def bracket_cubic_root(
    lo: Fraction,
    hi: Fraction,
    wc: Fraction,
    w1: Fraction,
    w2: Fraction,
    g1: Fraction,
    g2: Fraction,
    tol_den: int = 1000000,
) -> tuple[Fraction, Fraction]:
    """Exact rational bisection of P3(X) on a strict sign-change interval [lo, hi]."""
    flo = cubic_hopfield_poly(lo, wc, w1, w2, g1, g2)
    fhi = cubic_hopfield_poly(hi, wc, w1, w2, g1, g2)
    if flo == 0:
        return (lo, lo)
    if fhi == 0:
        return (hi, hi)
    if (flo > 0 and fhi > 0) or (flo < 0 and fhi < 0):
        raise ValueError("No strict sign change on interval")
    tol = Fraction(1, tol_den)
    half = Fraction(1, 2)
    a, b, fa = lo, hi, flo
    while b - a > tol:
        mid = q_mul(a + b, half)
        fm = cubic_hopfield_poly(mid, wc, w1, w2, g1, g2)
        if fm == 0:
            return (mid, mid)
        if (fa < 0 and fm < 0) or (fa > 0 and fm > 0):
            a, fa = mid, fm
        else:
            b = mid
    return (a, b)


def solve_two_band_hopfield(
    wc: Fraction,
    w1: Fraction,
    w2: Fraction,
    g1: Fraction,
    g2: Fraction,
    tol_den: int = 1000000,
) -> dict[str, object]:
    """Certify strict Cauchy-Hopfield interlacing 0 < X_LP < w1^2 < X_MP < w2^2 < X_UP < X_max
    and bracket all three squared and linear polariton frequencies plus exact Hopfield weights.
    """
    if not (wc > 0 and w1 > 0 and w2 > w1 and g1 > 0 and g2 > 0):
        raise ValueError("Require wc > 0, 0 < w1 < w2, g1 > 0, g2 > 0")

    inv = vieta_invariants(wc, w1, w2, g1, g2)
    w12 = q_sq(w1)
    w22 = q_sq(w2)
    x_max = inv["e1"]

    p0 = cubic_hopfield_poly(Fraction(0, 1), wc, w1, w2, g1, g2)
    p1 = cubic_hopfield_poly(w12, wc, w1, w2, g1, g2)
    p2 = cubic_hopfield_poly(w22, wc, w1, w2, g1, g2)
    pmax = cubic_hopfield_poly(x_max, wc, w1, w2, g1, g2)

    # Verify strict sign alternation and exact TRK identity P3(0) = -wc^2*w1^2*w2^2
    assert p0 == -inv["e3"]
    assert p0 < 0 and p1 > 0 and p2 < 0 and pmax > 0
    assert cubic_hopfield_poly_factored(x_max, wc, w1, w2, g1, g2) == pmax

    xlp_lo, xlp_hi = bracket_cubic_root(Fraction(0, 1), w12, wc, w1, w2, g1, g2, tol_den)
    xmp_lo, xmp_hi = bracket_cubic_root(w12, w22, wc, w1, w2, g1, g2, tol_den)
    xup_lo, xup_hi = bracket_cubic_root(w22, x_max, wc, w1, w2, g1, g2, tol_den)

    nu_lp_lo, _ = isqrt_bracket(xlp_lo, tol_den)
    _, nu_lp_hi = isqrt_bracket(xlp_hi, tol_den)
    nu_mp_lo, _ = isqrt_bracket(xmp_lo, tol_den)
    _, nu_mp_hi = isqrt_bracket(xmp_hi, tol_den)
    nu_up_lo, _ = isqrt_bracket(xup_lo, tol_den)
    _, nu_up_hi = isqrt_bracket(xup_hi, tol_den)

    # Certified ZPE shift: Delta_nu = (nu_lp + nu_mp + nu_up) - (wc + w1 + w2)
    bare_sum = wc + w1 + w2
    dnu_lo = (nu_lp_lo + nu_mp_lo + nu_up_lo) - bare_sum
    dnu_hi = (nu_lp_hi + nu_mp_hi + nu_up_hi) - bare_sum
    assert dnu_lo > 0

    # Exact Hopfield weights evaluated at midpoint of each certified X bracket
    # Plus rigorous interval bounds on MP0 photonic weight using [xmp_lo, xmp_hi]
    half = Fraction(1, 2)
    a1 = 4 * wc * w1 * q_sq(g1)
    a2 = 4 * wc * w2 * q_sq(g2)

    def weights_at(x: Fraction) -> dict[str, Fraction]:
        t1 = q_div(a1, q_sq(x - w12))
        t2 = q_div(a2, q_sq(x - w22))
        denom = Fraction(1, 1) + t1 + t2
        wc_w = q_inv(denom)
        w1_w = q_div(t1, denom)
        w2_w = q_div(t2, denom)
        assert wc_w + w1_w + w2_w == Fraction(1, 1)
        return {"wc": wc_w, "w1": w1_w, "w2": w2_w}

    w_lp = weights_at(q_mul(xlp_lo + xlp_hi, half))
    w_mp = weights_at(q_mul(xmp_lo + xmp_hi, half))
    w_up = weights_at(q_mul(xup_lo + xup_hi, half))

    # Universal analytic upper bound on MP0 photonic weight (no root-finding needed!):
    # 1 / w_{c,MP} > 1 + (3 * min(A1, A2) + A1 + A2) / (w2^2 - w1^2)^2
    delta2 = w22 - w12
    universal_denom_lb = Fraction(1, 1) + q_div(3 * q_min(a1, a2) + a1 + a2, q_sq(delta2))
    wc_mp_universal_ub = q_inv(universal_denom_lb)
    assert w_mp["wc"] < wc_mp_universal_ub

    # Exact interval upper/lower bound on w_{c,MP} from [xmp_lo, xmp_hi]
    # On (w1^2, w2^2), x - w1^2 <= xmp_hi - w1^2 and w2^2 - x <= w2^2 - xmp_lo
    mp_denom_lo = (
        Fraction(1, 1)
        + q_div(a1, q_sq(xmp_hi - w12))
        + q_div(a2, q_sq(w22 - xmp_lo))
    )
    mp_denom_hi = (
        Fraction(1, 1)
        + q_div(a1, q_sq(xmp_lo - w12))
        + q_div(a2, q_sq(w22 - xmp_hi))
    )
    wc_mp_lo = q_inv(mp_denom_hi)
    wc_mp_hi = q_inv(mp_denom_lo)
    assert wc_mp_lo <= w_mp["wc"] <= wc_mp_hi < wc_mp_universal_ub

    return {
        "inputs": {
            "wc": q_to_pair(wc),
            "w1": q_to_pair(w1),
            "w2": q_to_pair(w2),
            "g1": q_to_pair(g1),
            "g2": q_to_pair(g2),
        },
        "vieta": {k: q_to_pair(v) for k, v in inv.items()},
        "sign_check": {
            "P3_0_neg": p0 < 0,
            "P3_w1sq_pos": p1 > 0,
            "P3_w2sq_neg": p2 < 0,
            "P3_xmax_pos": pmax > 0,
        },
        "X_brackets": {
            "LP": [q_to_pair(xlp_lo), q_to_pair(xlp_hi)],
            "MP": [q_to_pair(xmp_lo), q_to_pair(xmp_hi)],
            "UP": [q_to_pair(xup_lo), q_to_pair(xup_hi)],
        },
        "nu_brackets_THz": {
            "LP": [q_decimal_str(nu_lp_lo, 4), q_decimal_str(nu_lp_hi, 4)],
            "MP": [q_decimal_str(nu_mp_lo, 4), q_decimal_str(nu_mp_hi, 4)],
            "UP": [q_decimal_str(nu_up_lo, 4), q_decimal_str(nu_up_hi, 4)],
        },
        "nu_brackets_exact": {
            "LP": [q_to_pair(nu_lp_lo), q_to_pair(nu_lp_hi)],
            "MP": [q_to_pair(nu_mp_lo), q_to_pair(nu_mp_hi)],
            "UP": [q_to_pair(nu_up_lo), q_to_pair(nu_up_hi)],
        },
        "zpe_freq_shift_THz": {
            "lo": q_decimal_str(dnu_lo, 4),
            "hi": q_decimal_str(dnu_hi, 4),
            "exact_lo": q_to_pair(dnu_lo),
            "exact_hi": q_to_pair(dnu_hi),
            "positive": dnu_lo > 0,
        },
        "weights_mid": {
            "LP": {k: q_decimal_str(v, 6) for k, v in w_lp.items()},
            "MP": {k: q_decimal_str(v, 6) for k, v in w_mp.items()},
            "UP": {k: q_decimal_str(v, 6) for k, v in w_up.items()},
        },
        "weights_mid_exact": {
            "LP": {k: q_to_pair(v) for k, v in w_lp.items()},
            "MP": {k: q_to_pair(v) for k, v in w_mp.items()},
            "UP": {k: q_to_pair(v) for k, v in w_up.items()},
        },
        "mp_photonic_bounds": {
            "lo": q_decimal_str(wc_mp_lo, 6),
            "hi": q_decimal_str(wc_mp_hi, 6),
            "universal_ub": q_decimal_str(wc_mp_universal_ub, 6),
            "exact_lo": q_to_pair(wc_mp_lo),
            "exact_hi": q_to_pair(wc_mp_hi),
            "exact_universal_ub": q_to_pair(wc_mp_universal_ub),
        },
    }


def anharmonicity_2dir_certificate(
    w1_alpha: Fraction,
    w2_alpha: Fraction,
    w1_beta: Fraction,
    w2_beta: Fraction,
    delta1: Fraction,
    delta2: Fraction,
    n1: int,
    n2: int,
) -> dict[str, object]:
    """Exact 1/N collective Kerr anharmonicity suppression and 2D-IR cross-peak certificate."""
    if n1 <= 0 or n2 <= 0:
        raise ValueError("Require N1, N2 > 0")
    fn1 = Fraction(n1, 1)
    fn2 = Fraction(n2, 1)
    diag_alpha = q_div(q_sq(w1_alpha) * delta1, fn1) + q_div(q_sq(w2_alpha) * delta2, fn2)
    cross_ab = 2 * (
        q_div(w1_alpha * w1_beta * delta1, fn1) + q_div(w2_alpha * w2_beta * delta2, fn2)
    )
    n_min = Fraction(n1 if n1 <= n2 else n2, 1)
    d_max = q_max(delta1, delta2)
    universal_ub = q_div(d_max, n_min)
    assert diag_alpha <= universal_ub
    suppression_ratio = q_div(d_max, diag_alpha) if diag_alpha > 0 else Fraction(0, 1)
    return {
        "N1": n1,
        "N2": n2,
        "dark_mode_count": n1 + n2 - 2,
        "delta1_THz": q_to_pair(delta1),
        "delta2_THz": q_to_pair(delta2),
        "diag_alpha_THz_exact": q_to_pair(diag_alpha),
        "diag_alpha_THz_dec": q_decimal_str(diag_alpha, 9),
        "cross_ab_THz_exact": q_to_pair(cross_ab),
        "cross_ab_THz_dec": q_decimal_str(cross_ab, 9),
        "universal_ub_THz_exact": q_to_pair(universal_ub),
        "suppression_vs_bare_exact": q_to_pair(suppression_ratio),
        "suppression_vs_bare_dec": q_decimal_str(suppression_ratio, 2),
    }


def dark_leakage_certificate(
    sigma_inh: Fraction,
    delta_gap: Fraction,
    linewidth_gamma: Fraction,
) -> dict[str, object]:
    """Exact non-Markovian inhomogeneous support-leakage bound eta_leak <= sigma^2 / delta_gap^2."""
    if delta_gap <= 0 or sigma_inh < 0 or linewidth_gamma <= 0:
        raise ValueError("Require delta_gap > 0, sigma_inh >= 0, linewidth_gamma > 0")
    eta_ub = q_div(q_sq(sigma_inh), q_sq(delta_gap))
    resolved_vs_disorder = sigma_inh < delta_gap
    resolved_vs_linewidth = linewidth_gamma < delta_gap
    return {
        "sigma_inh_THz": q_to_pair(sigma_inh),
        "delta_gap_THz": q_to_pair(delta_gap),
        "linewidth_gamma_THz": q_to_pair(linewidth_gamma),
        "eta_leak_ub_exact": q_to_pair(eta_ub),
        "eta_leak_ub_dec": q_decimal_str(eta_ub, 6),
        "polaron_protected_lt_1pct": eta_ub < Fraction(1, 100),
        "resolved_vs_disorder": resolved_vs_disorder,
        "resolved_vs_linewidth": resolved_vs_linewidth,
    }


def canonical_json_sha256(obj: object) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()
