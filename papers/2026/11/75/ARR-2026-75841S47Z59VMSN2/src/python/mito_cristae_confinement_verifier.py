"""
MITO-CRISTAE-CONFINEMENT-CERT-1.0: Zero-floating-point exact algebraic verifier for
Subwavelength Confinement Horizons of 71-THz Mito-Polaritons.

Direct continuation of ARR-2025-2AQXS44H6Z8GQAG2 (Dec 2025 / Jul 2026) and
ARR-2026-1E91AXEJYT890TQC (Nov 26, 2026), auditing the electromagnetic confinement
requirements of Yang, Gu, and Song (bioRxiv:10.64898/2026.09.10.750628v1, Sep 2026).

Strictly zero floating-point literals, zero float() calls, zero true-division (/ or /=),
and zero math/numpy/scipy/decimal imports. All arithmetic uses exact Python int and
fractions.Fraction.
"""

from __future__ import annotations

import json
import pathlib
import sys
from fractions import Fraction
from typing import Any

SCHEMA_VERSION = "MITO-CRISTAE-CONFINEMENT-CERT-1.0"
MAX_JSON_BYTES = 1_000_000
MAX_RAT_ABS = 10**24
SI_C_M_PER_S = 299_792_458  # Exact SI-2019 speed of light (m/s)


class VerificationError(ValueError):
    """Raised whenever a certificate violates schema, bounds, or mathematical invariants."""


def _gcd(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a


def _req_int(val: Any, name: str, lo: int | None = None, hi: int | None = None) -> int:
    if isinstance(val, bool) or not isinstance(val, int):
        raise VerificationError(f"Expected integer for {name}, got {type(val).__name__}")
    if lo is not None and val < lo:
        raise VerificationError(f"{name}={val} below minimum {lo}")
    if hi is not None and val > hi:
        raise VerificationError(f"{name}={val} above maximum {hi}")
    return val


def _req_bool(val: Any, name: str) -> bool:
    if not isinstance(val, bool):
        raise VerificationError(f"Expected boolean for {name}, got {type(val).__name__}")
    return val


def _req_str(val: Any, name: str) -> str:
    if not isinstance(val, str) or not val.strip():
        raise VerificationError(f"Expected non-empty string for {name}")
    return val


def _req_dict(val: Any, name: str) -> dict[str, Any]:
    if not isinstance(val, dict):
        raise VerificationError(f"Expected dict for {name}")
    return val


def _parse_rat(val: Any, name: str) -> Fraction:
    if not isinstance(val, list) or len(val) != 2:
        raise VerificationError(f"Expected [num, den] rational pair for {name}")
    num = _req_int(val[0], f"{name}[0]", -MAX_RAT_ABS, MAX_RAT_ABS)
    den = _req_int(val[1], f"{name}[1]", 1, MAX_RAT_ABS)
    if _gcd(num, den) != 1:
        raise VerificationError(f"Rational {name} not in lowest terms")
    return Fraction(num, den)


def _rat_pair(f: Fraction) -> list[int]:
    return [f.numerator, f.denominator]


def _inv(f: Fraction) -> Fraction:
    if f == 0:
        raise VerificationError("Exact rational division by zero")
    return Fraction(f.denominator, f.numerator)


def _no_dup_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for k, v in pairs:
        if k in out:
            raise VerificationError(f"Duplicate JSON key: {k}")
        out[k] = v
    return out


def _reject_json_constant(token: str) -> Any:
    raise VerificationError(f"Illegal non-finite JSON constant: {token}")


def _reject_json_float(token: str) -> Any:
    raise VerificationError(f"Illegal floating-point JSON literal: {token}")


# ---------------------------------------------------------------------------
# Mode 1: lst_oscillator_strength_and_fp_cutoff
# ---------------------------------------------------------------------------

def _verify_mode1(payload: dict[str, Any]) -> dict[str, Any]:
    submode = _req_str(payload.get("submode"), "submode")

    if submode == "lst_reststrahlen_deficit":
        w0 = _parse_rat(payload.get("omega_0_thz"), "omega_0_thz")
        nu_m = _parse_rat(payload.get("nu_minus_thz"), "nu_minus_thz")
        f_bulk = _parse_rat(payload.get("f_bulk_lipid"), "f_bulk_lipid")
        if w0 <= 0 or nu_m <= 0 or nu_m >= w0:
            raise VerificationError("Require 0 < nu_minus < omega_0")
        if f_bulk <= 0:
            raise VerificationError("Require f_bulk_lipid > 0")

        # Gauge-invariant Hopfield TRK at resonance: nu_p = w0^2 / nu_m, g = (nu_p - nu_m)/2
        nu_p = (w0 * w0) * _inv(nu_m)
        g = (nu_p - nu_m) * Fraction(1, 2)
        eta = g * _inv(w0)
        f_req = 4 * eta * eta
        w_lo_sq = w0 * w0 + 4 * g * g

        # Exact LST identity check: w_LO^2 == w0^2 * (1 + f_req)
        if w_lo_sq != w0 * w0 * (1 + f_req):
            raise VerificationError("LST identity w_LO^2 = w0^2 * (1 + 4*eta^2) failed")

        # Required local-field / mode-volume enhancement factor F_enh = f_req / f_bulk
        f_enh = f_req * _inv(f_bulk)

        # Optional exact bracket checks on w_LO and enhancement floor
        w_lo_lo = _parse_rat(payload.get("w_lo_bracket_lo_thz"), "w_lo_bracket_lo_thz")
        w_lo_hi = _parse_rat(payload.get("w_lo_bracket_hi_thz"), "w_lo_bracket_hi_thz")
        if w_lo_lo <= 0 or w_lo_lo >= w_lo_hi:
            raise VerificationError("Invalid w_LO bracket")
        if not (w_lo_lo * w_lo_lo < w_lo_sq < w_lo_hi * w_lo_hi):
            raise VerificationError("w_LO squared does not lie strictly inside certified bracket")

        min_enh = _parse_rat(payload.get("min_enhancement_factor"), "min_enhancement_factor")
        if f_enh <= min_enh:
            raise VerificationError(f"Enhancement factor {f_enh} does not exceed {min_enh}")

        if "expected_f_osc_req" in payload:
            exp_f = _parse_rat(payload["expected_f_osc_req"], "expected_f_osc_req")
            if exp_f != f_req:
                raise VerificationError(f"f_osc_req mismatch: {f_req} != {exp_f}")

        return {
            "mode": "lst_oscillator_strength_and_fp_cutoff",
            "submode": submode,
            "omega_0_thz": _rat_pair(w0),
            "nu_minus_thz": _rat_pair(nu_m),
            "nu_plus_hopfield_thz": _rat_pair(nu_p),
            "eta_hopfield": _rat_pair(eta),
            "f_osc_required": _rat_pair(f_req),
            "w_lo_sq_thz2": _rat_pair(w_lo_sq),
            "w_lo_bracket_thz": [_rat_pair(w_lo_lo), _rat_pair(w_lo_hi)],
            "f_bulk_lipid": _rat_pair(f_bulk),
            "required_enhancement_factor": _rat_pair(f_enh),
            "exceeds_4_25_threshold": f_req > Fraction(4, 25),
        }

    if submode == "fabry_perot_cutoff_nogo":
        w0 = _parse_rat(payload.get("omega_0_thz"), "omega_0_thz")
        n_eff = _parse_rat(payload.get("n_eff"), "n_eff")
        d_crista_nm = _parse_rat(payload.get("d_crista_nm"), "d_crista_nm")
        min_ratio = _parse_rat(payload.get("min_fp_to_crista_ratio"), "min_fp_to_crista_ratio")
        if w0 <= 0 or n_eff <= 0 or d_crista_nm <= 0:
            raise VerificationError("Require positive frequency, index, and crista width")

        # Exact SI-2019 wavelength in nm: lambda_nm = (c_m_s * 10^9) / (w0_thz * 10^12) = c_m_s / (1000 * w0_thz)
        lambda_nm = Fraction(SI_C_M_PER_S, 1000) * _inv(w0)
        d_fp_nm = lambda_nm * _inv(2 * n_eff)
        ratio = d_fp_nm * _inv(d_crista_nm)
        if ratio <= min_ratio:
            raise VerificationError(f"Fabry-Perot cutoff ratio {ratio} <= {min_ratio}")

        return {
            "mode": "lst_oscillator_strength_and_fp_cutoff",
            "submode": submode,
            "lambda_0_nm": _rat_pair(lambda_nm),
            "d_fp_halfwave_nm": _rat_pair(d_fp_nm),
            "d_crista_nm": _rat_pair(d_crista_nm),
            "fp_to_crista_ratio": _rat_pair(ratio),
            "transverse_fp_forbidden": ratio > 1,
        }

    raise VerificationError(f"Unknown Mode 1 submode: {submode}")


# ---------------------------------------------------------------------------
# Mode 2: lamellar_emt_and_lorentz_hyperbolicity
# ---------------------------------------------------------------------------

def _verify_mode2(payload: dict[str, Any]) -> dict[str, Any]:
    submode = _req_str(payload.get("submode"), "submode")

    if submode == "lamellar_emt_phase":
        d_l = _parse_rat(payload.get("d_lipid_nm"), "d_lipid_nm")
        d_w = _parse_rat(payload.get("d_water_nm"), "d_water_nm")
        eps_l = _parse_rat(payload.get("eps_lipid"), "eps_lipid")
        eps_w = _parse_rat(payload.get("eps_water"), "eps_water")
        expected_phase = _req_str(payload.get("expected_phase"), "expected_phase")
        if d_l <= 0 or d_w <= 0 or eps_w <= 0:
            raise VerificationError("Require positive layer thicknesses and eps_water > 0")

        period = d_l + d_w
        phi = d_l * _inv(period)
        one_minus_phi = 1 - phi

        eps_par = phi * eps_l + one_minus_phi * eps_w
        denom_perp = one_minus_phi * eps_l + phi * eps_w
        if denom_perp == 0:
            raise VerificationError("Exact ENZ pole singularity (denom_perp == 0)")
        eps_perp = (eps_l * eps_w) * _inv(denom_perp)

        # Verify exact Wiener anisotropy identity whenever eps_l > 0
        wiener_gap = eps_par - eps_perp
        expected_wiener = (phi * one_minus_phi * (eps_l - eps_w) * (eps_l - eps_w)) * _inv(denom_perp)
        if wiener_gap != expected_wiener:
            raise VerificationError("Exact Wiener anisotropy identity failed")

        # Classify uniaxial optical phase
        if eps_par > 0 and eps_perp > 0:
            phase = "Elliptic_Positive"
        elif eps_par > 0 and eps_perp < 0:
            phase = "Type_I_Hyperbolic"
        elif eps_par < 0 and eps_perp > 0:
            phase = "Type_II_Hyperbolic"
        else:
            phase = "Opaque_Metallic"

        if phase != expected_phase:
            raise VerificationError(f"Phase mismatch: computed {phase} != expected {expected_phase}")

        return {
            "mode": "lamellar_emt_and_lorentz_hyperbolicity",
            "submode": submode,
            "filling_fraction_phi": _rat_pair(phi),
            "eps_parallel": _rat_pair(eps_par),
            "eps_perp": _rat_pair(eps_perp),
            "wiener_anisotropy_gap": _rat_pair(wiener_gap),
            "optical_phase": phase,
        }

    if submode == "damped_lorentz_threshold":
        eps_inf = _parse_rat(payload.get("eps_inf"), "eps_inf")
        d_eps = _parse_rat(payload.get("delta_eps"), "delta_eps")
        w0 = _parse_rat(payload.get("omega_0_thz"), "omega_0_thz")
        gm = _parse_rat(payload.get("gamma_m_thz"), "gamma_m_thz")
        w_probe = _parse_rat(payload.get("omega_probe_thz"), "omega_probe_thz")
        exp_has_neg = _req_bool(payload.get("expected_has_negative_band"), "expected_has_negative_band")
        if eps_inf <= 0 or d_eps <= 0 or w0 <= 0 or gm <= 0 or w_probe <= 0:
            raise VerificationError("Require strictly positive Lorentz parameters")

        # Exact AM-GM minimum of Re[eps_L(w)] over all w > 0:
        # min_Re = eps_inf - d_eps * w0^2 / (gm * (2*w0 + gm)), attained at w_*^2 = w0^2 + gm*w0
        f_osc = d_eps * _inv(eps_inf)
        q_m = w0 * _inv(gm)
        f_thresh = (gm * (2 * w0 + gm)) * _inv(w0 * w0)
        min_re_eps = eps_inf - (d_eps * w0 * w0) * _inv(gm * (2 * w0 + gm))
        has_neg_band = min_re_eps < 0
        if has_neg_band != exp_has_neg:
            raise VerificationError(f"Negative-band flag mismatch: {has_neg_band} != {exp_has_neg}")

        # Exact Re[eps_L(w_probe)] and Im[eps_L(w_probe)] at probe frequency (e.g. 71 THz or w_*)
        diff = w0 * w0 - w_probe * w_probe
        denom = diff * diff + (gm * w_probe) * (gm * w_probe)
        re_probe = eps_inf + (d_eps * w0 * w0 * diff) * _inv(denom)
        im_probe = (d_eps * w0 * w0 * gm * w_probe) * _inv(denom)

        # Verify universal lower bound Re[eps_L(w_probe)] >= min_re_eps!
        if re_probe < min_re_eps:
            raise VerificationError("AM-GM minimum bound violated")
        # If w_probe < w0, Re[eps_L(w_probe)] MUST strictly exceed eps_inf > 0!
        if w_probe < w0 and re_probe <= eps_inf:
            raise VerificationError("Below-resonance positivity violated")

        return {
            "mode": "lamellar_emt_and_lorentz_hyperbolicity",
            "submode": submode,
            "f_osc": _rat_pair(f_osc),
            "q_matter": _rat_pair(q_m),
            "f_osc_hyperbolic_threshold": _rat_pair(f_thresh),
            "min_re_eps_exact": _rat_pair(min_re_eps),
            "has_negative_permittivity_band": has_neg_band,
            "re_eps_at_probe": _rat_pair(re_probe),
            "im_eps_at_probe": _rat_pair(im_probe),
            "probe_strictly_positive": re_probe > 0,
        }

    raise VerificationError(f"Unknown Mode 2 submode: {submode}")


# ---------------------------------------------------------------------------
# Mode 3: unimodular_transfer_matrix_stack
# ---------------------------------------------------------------------------

def _mat_mul_2x2(A: list[list[Fraction]], B: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]


def _mat_det_2x2(A: list[list[Fraction]]) -> Fraction:
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def _verify_mode3(payload: dict[str, Any]) -> dict[str, Any]:
    """
    Exact unimodular 2x2 transfer matrix for a lossless S-lamella crista unit cell,
    built from exact rational Pythagorean unit-circle phases (c_j^2 + s_j^2 = 1)
    for lipid bilayer (n_L) and aqueous lumen (n_W), verifying:
      - Exact SL(2, Q) unimodularity det(M_cell) = 1 and det(M_cell^S) = 1
      - Exact Chebyshev U_{S-1}(x) recursion vs direct matrix powering M_cell^S
      - Exact passband (|x| <= 1) vs stopband (|x| > 1) classification
      - Exact transmittance T_S and reflectance R_S in ambient index n_W.
    """
    n_l = _parse_rat(payload.get("n_lipid"), "n_lipid")
    n_w = _parse_rat(payload.get("n_water"), "n_water")
    t_l = _parse_rat(payload.get("tan_half_phase_lipid"), "tan_half_phase_lipid")
    t_w = _parse_rat(payload.get("tan_half_phase_water"), "tan_half_phase_water")
    s_layers = _req_int(payload.get("num_lamellae_S"), "num_lamellae_S", 1, 64)
    exp_passband = _req_bool(payload.get("expected_in_passband"), "expected_in_passband")
    max_refl = _parse_rat(payload.get("max_expected_reflectance"), "max_expected_reflectance")

    if n_l <= 0 or n_w <= 0 or t_l <= 0 or t_w <= 0:
        raise VerificationError("Require positive indices and phase tangents")

    # Rational Weierstrass parameterization of unit circle: cos(phi) = (1 - t^2)/(1 + t^2), sin(phi) = 2t/(1 + t^2)
    c_l = (1 - t_l * t_l) * _inv(1 + t_l * t_l)
    s_l = (2 * t_l) * _inv(1 + t_l * t_l)
    c_w = (1 - t_w * t_w) * _inv(1 + t_w * t_w)
    s_w = (2 * t_w) * _inv(1 + t_w * t_w)
    if c_l * c_l + s_l * s_l != 1 or c_w * c_w + s_w * s_w != 1:
        raise VerificationError("Pythagorean unit-circle identity failed")

    # Exact real characteristic matrices (electric/magnetic field normalized so M = [[c, s/n], [-n*s, c]])
    # Note: in optical convention [[c, i*s/n], [i*n*s, c]], mapping H -> i*H yields real SL(2,Q) matrices
    # with identical trace Tr(M_cell)/2 = c_l*c_w - (1/2)*(n_l/n_w + n_w/n_l)*s_l*s_w!
    # We use the exact real 2x2 form in (E, i*H) basis:
    # M_layer = [[c, -s/n], [n*s, c]] -> wait: let's check det: c^2 + s^2 = 1, and
    # Tr(M_L * M_W) = 2*c_l*c_w - (n_l/n_w + n_w/n_l)*s_l*s_w!
    m_l = [[c_l, -(s_l * _inv(n_l))], [n_l * s_l, c_l]]
    m_w = [[c_w, -(s_w * _inv(n_w))], [n_w * s_w, c_w]]
    if _mat_det_2x2(m_l) != 1 or _mat_det_2x2(m_w) != 1:
        raise VerificationError("Single-layer unimodularity failed")

    m_cell = _mat_mul_2x2(m_l, m_w)
    if _mat_det_2x2(m_cell) != 1:
        raise VerificationError("Unit-cell unimodularity failed")

    x = (m_cell[0][0] + m_cell[1][1]) * Fraction(1, 2)
    # Cross-check exact Bloch trace formula:
    x_formula = c_l * c_w - Fraction(1, 2) * (n_l * _inv(n_w) + n_w * _inv(n_l)) * s_l * s_w
    if x != x_formula:
        raise VerificationError("Bloch trace formula mismatch")

    in_passband = -1 <= x <= 1
    if in_passband != exp_passband:
        raise VerificationError(f"Passband classification mismatch: {in_passband} != {exp_passband}")

    # Compute M_cell^S directly AND via exact Chebyshev U_{S-1}(x), U_{S-2}(x)
    m_pow = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    for _ in range(s_layers):
        m_pow = _mat_mul_2x2(m_pow, m_cell)
    if _mat_det_2x2(m_pow) != 1:
        raise VerificationError("Stacked matrix unimodularity failed")

    # Chebyshev U_k(x): U_{-1} = 0, U_0 = 1, U_k = 2*x*U_{k-1} - U_{k-2}
    u_prev = Fraction(0)  # U_{-1}
    u_curr = Fraction(1)  # U_0
    for _ in range(s_layers - 1):
        u_next = 2 * x * u_curr - u_prev
        # Verify Cassini invariant U_k^2 - U_{k-1}*U_{k+1} = 1 at every step
        if u_curr * u_curr - u_prev * u_next != 1:
            raise VerificationError("Chebyshev Cassini invariant failed")
        u_prev, u_curr = u_curr, u_next
    # Now u_curr = U_{S-1}(x), u_prev = U_{S-2}(x)
    # Verify exact Cayley-Hamilton identity M^S = U_{S-1}(x)*M - U_{S-2}(x)*I
    m_cheb = [
        [u_curr * m_cell[0][0] - u_prev, u_curr * m_cell[0][1]],
        [u_curr * m_cell[1][0], u_curr * m_cell[1][1] - u_prev],
    ]
    if m_cheb != m_pow:
        raise VerificationError("Cayley-Hamilton Chebyshev identity M^S = U_{S-1} M - U_{S-2} I failed")

    # Exact normal-incidence reflectance R_S in ambient medium n_w:
    # From M_pow = [[A, B], [C, D]] with A*D - B*C = 1 (in (E, iH) basis, where
    # physical optical transfer matrix is [[A, -iB], [-iC, D]]):
    # |t_S|^{-2} = (1/4) * ( (A + D)^2 + (n_w*B - C/n_w)^2 ) = 1 + (1/4) * ( (A - D)^2 + (n_w*B + C/n_w)^2 )
    A, B = m_pow[0][0], m_pow[0][1]
    C, D = m_pow[1][0], m_pow[1][1]
    d_minus = n_w * B - C * _inv(n_w)
    d_plus = n_w * B + C * _inv(n_w)
    inv_t_sq_1 = Fraction(1, 4) * ((A + D) * (A + D) + d_minus * d_minus)
    inv_t_sq_2 = 1 + Fraction(1, 4) * ((A - D) * (A - D) + d_plus * d_plus)
    if inv_t_sq_1 != inv_t_sq_2:
        raise VerificationError("Unimodular flux-conservation transmittance identity failed")

    transmittance = _inv(inv_t_sq_1)
    reflectance = 1 - transmittance
    if reflectance < 0 or reflectance > max_refl:
        raise VerificationError(f"Reflectance {reflectance} outside [0, {max_refl}]")

    return {
        "mode": "unimodular_transfer_matrix_stack",
        "num_lamellae_S": s_layers,
        "bloch_half_trace_x": _rat_pair(x),
        "in_passband": in_passband,
        "chebyshev_U_S_minus_1": _rat_pair(u_curr),
        "transmittance_T_S": _rat_pair(transmittance),
        "reflectance_R_S": _rat_pair(reflectance),
        "det_M_S": [1, 1],
    }


# ---------------------------------------------------------------------------
# Mode 4: water_loss_q_ceiling_and_visibility
# ---------------------------------------------------------------------------

def _verify_mode4(payload: dict[str, Any]) -> dict[str, Any]:
    w = _parse_rat(payload.get("omega_thz"), "omega_thz")
    eps_eff = _parse_rat(payload.get("eps_eff_real"), "eps_eff_real")
    eps_w_im = _parse_rat(payload.get("eps_water_imag"), "eps_water_imag")
    gamma_w = _parse_rat(payload.get("water_field_fraction"), "water_field_fraction")
    g = _parse_rat(payload.get("coupling_g_thz"), "coupling_g_thz")
    gamma_m = _parse_rat(payload.get("gamma_matter_thz"), "gamma_matter_thz")
    exp_visible = _req_bool(payload.get("expected_strong_coupling_visible"), "expected_strong_coupling_visible")

    if w <= 0 or eps_eff <= 0 or eps_w_im <= 0 or g <= 0 or gamma_m < 0:
        raise VerificationError("Invalid Mode 4 optical/damping parameters")
    if gamma_w <= 0 or gamma_w > 1:
        raise VerificationError("water_field_fraction must lie in (0, 1]")

    q_loss_ceiling = eps_eff * _inv(gamma_w * eps_w_im)
    gamma_c_floor = w * _inv(q_loss_ceiling)

    # Strong-coupling spectral visibility criterion: 2*g > (gamma_c + gamma_m)/2  <=>  4*g > gamma_c + gamma_m
    # Also compute exact complex-pole real splitting margin: 16*g^2 - (gamma_c - gamma_m)^2
    vis_lhs = 4 * g
    vis_rhs = gamma_c_floor + gamma_m
    is_visible = vis_lhs > vis_rhs
    pole_disc = 16 * g * g - (gamma_c_floor - gamma_m) * (gamma_c_floor - gamma_m)

    if is_visible != exp_visible:
        raise VerificationError(f"Visibility mismatch: {is_visible} != {exp_visible}")
    if is_visible and pole_disc <= 0:
        raise VerificationError("Visibility implies positive pole discriminant failed")

    # Optional comparison against reference Q (e.g. D2O recovery factor over H2O)
    out: dict[str, Any] = {
        "mode": "water_loss_q_ceiling_and_visibility",
        "omega_thz": _rat_pair(w),
        "q_loss_ceiling": _rat_pair(q_loss_ceiling),
        "gamma_c_floor_thz": _rat_pair(gamma_c_floor),
        "four_g_thz": _rat_pair(vis_lhs),
        "total_damping_sum_thz": _rat_pair(vis_rhs),
        "pole_discriminant_thz2": _rat_pair(pole_disc),
        "strong_coupling_visible": is_visible,
    }
    if "reference_q_h2o" in payload:
        ref_q = _parse_rat(payload["reference_q_h2o"], "reference_q_h2o")
        if ref_q <= 0:
            raise VerificationError("reference_q_h2o must be > 0")
        rec_factor = q_loss_ceiling * _inv(ref_q)
        out["q_recovery_factor_vs_h2o"] = _rat_pair(rec_factor)
    return out


# ---------------------------------------------------------------------------
# Top-level dispatcher
# ---------------------------------------------------------------------------

def verify_certificate(cert: dict[str, Any]) -> dict[str, Any]:
    cert = _req_dict(cert, "certificate")
    schema = _req_str(cert.get("schema_version"), "schema_version")
    if schema != SCHEMA_VERSION:
        raise VerificationError(f"Unsupported schema_version: {schema}")
    cert_id = _req_str(cert.get("cert_id"), "cert_id")
    mode = _req_str(cert.get("mode"), "mode")
    payload = _req_dict(cert.get("payload"), "payload")

    if mode == "lst_oscillator_strength_and_fp_cutoff":
        res = _verify_mode1(payload)
    elif mode == "lamellar_emt_and_lorentz_hyperbolicity":
        res = _verify_mode2(payload)
    elif mode == "unimodular_transfer_matrix_stack":
        res = _verify_mode3(payload)
    elif mode == "water_loss_q_ceiling_and_visibility":
        res = _verify_mode4(payload)
    else:
        raise VerificationError(f"Unknown verification mode: {mode}")

    return {"schema_version": SCHEMA_VERSION, "cert_id": cert_id, **res}


def verify_file(path: str | pathlib.Path) -> dict[str, Any]:
    p = pathlib.Path(path)
    if not p.is_file():
        raise VerificationError(f"Certificate path is not a regular file: {p}")
    raw = p.read_bytes()
    if len(raw) > MAX_JSON_BYTES:
        raise VerificationError(f"Certificate size {len(raw)} exceeds MAX_JSON_BYTES={MAX_JSON_BYTES}")
    try:
        data = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_no_dup_pairs,
            parse_float=_reject_json_float,
            parse_constant=_reject_json_constant,
        )
    except VerificationError:
        raise
    except Exception as exc:
        raise VerificationError(f"JSON decode failed: {exc}") from exc
    return verify_certificate(data)


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if not args:
        print("Usage: python -m src.mito_cristae_confinement_verifier <file_or_dir> ...", file=sys.stderr)
        return 2
    targets: list[pathlib.Path] = []
    for a in args:
        p = pathlib.Path(a)
        if p.is_dir():
            targets.extend(sorted(p.glob("*.json")))
        else:
            targets.append(p)
    if not targets:
        print("No JSON certificate files found.", file=sys.stderr)
        return 2
    for t in targets:
        res = verify_file(t)
        print(json.dumps(res, sort_keys=True))
    print(f"Verified {len(targets)} certificates under {SCHEMA_VERSION}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
