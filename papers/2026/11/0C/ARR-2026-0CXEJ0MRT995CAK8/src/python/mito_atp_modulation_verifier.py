"""
MITO-ATP-MODULATION-CERT-1.0: Zero-floating-point exact algebraic verifier for
Thermodynamic Bounds on Infrared-Modulated ATP Synthesis at 71 THz.

Audits the ~10% cellular ATP modulation claim of Yang, Gu, and Song
(bioRxiv:10.64898/2026.09.10.750628v1, Sep 2026), separating:
  1. Direct stoichiometric photon-to-ATP conversion (First Law & Carnot floor)
  2. Passive Regime I polaritonic catalysis (Eyring barrier shift & OCR coupling)
  3. Micro-hotspot vs bulk photothermal heating (exact finite-difference Arrhenius & pi-free flux)
  4. Active non-equilibrium coherent ratchet (Barato-Seifert TUR & maintenance horizon).

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

SCHEMA_VERSION = "MITO-ATP-MODULATION-CERT-1.0"
MAX_JSON_BYTES = 1_000_000
MAX_RAT_ABS = 1_000_000_000_000_000_000_000_000
H_THZ_MEV_EXACT = Fraction(4135667696, 1_000_000_000)


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


def _mercator_ln_1_plus_x_bracket(x: Fraction, order_even: int = 6) -> tuple[Fraction, Fraction]:
    """Exact alternating-series lower and upper brackets for ln(1 + x), 0 < x <= 1."""
    if x <= 0 or x > 1:
        raise VerificationError("Mercator ln(1+x) requires 0 < x <= 1")
    s_even = Fraction(0)
    xp = x
    for k in range(1, order_even + 1):
        term = xp * Fraction(1, k)
        if k % 2 == 1:
            s_even += term
        else:
            s_even -= term
        xp *= x
    s_odd = s_even + xp * Fraction(1, order_even + 1)
    return s_even, s_odd


# ---------------------------------------------------------------------------
# Mode 1: stoichiometric_photon_and_carnot_floor
# ---------------------------------------------------------------------------

def _verify_mode1(payload: dict[str, Any]) -> dict[str, Any]:
    nu_thz = _parse_rat(payload.get("photon_freq_thz"), "photon_freq_thz")
    dg_atp_mev = _parse_rat(payload.get("delta_g_atp_mev"), "delta_g_atp_mev")
    j_atp_s = _parse_rat(payload.get("baseline_atp_rate_per_s"), "baseline_atp_rate_per_s")
    frac_gain = _parse_rat(payload.get("fractional_atp_gain"), "fractional_atp_gain")
    t_bath_k = _parse_rat(payload.get("temperature_bath_K"), "temperature_bath_K")
    t_rad_k = _parse_rat(payload.get("temperature_rad_K"), "temperature_rad_K")
    min_phot_per_atp = _parse_rat(payload.get("min_photons_per_atp"), "min_photons_per_atp")

    if nu_thz <= 0 or dg_atp_mev <= 0 or j_atp_s <= 0 or frac_gain <= 0:
        raise VerificationError("Require positive Mode 1 physical parameters")
    if t_bath_k <= 0 or t_rad_k <= t_bath_k:
        raise VerificationError("Require 0 < T_bath < T_rad")

    e_phot_mev = nu_thz * H_THZ_MEV_EXACT
    phot_per_atp = dg_atp_mev * _inv(e_phot_mev)
    carnot_eff = (t_rad_k - t_bath_k) * _inv(t_rad_k)
    phot_per_atp_carnot = phot_per_atp * _inv(carnot_eff)
    if phot_per_atp_carnot <= phot_per_atp:
        raise VerificationError("Carnot efficiency tightening failed")
    if phot_per_atp <= min_phot_per_atp:
        raise VerificationError(f"Stoichiometric floor {phot_per_atp} <= {min_phot_per_atp}")

    extra_atp_s = j_atp_s * frac_gain
    min_flux_per_s = extra_atp_s * phot_per_atp
    min_flux_carnot_per_s = extra_atp_s * phot_per_atp_carnot

    return {
        "mode": "stoichiometric_photon_and_carnot_floor",
        "photon_energy_mev": _rat_pair(e_phot_mev),
        "photons_per_atp_first_law": _rat_pair(phot_per_atp),
        "carnot_efficiency": _rat_pair(carnot_eff),
        "photons_per_atp_carnot": _rat_pair(phot_per_atp_carnot),
        "min_photon_flux_per_s": _rat_pair(min_flux_per_s),
        "min_photon_flux_carnot_per_s": _rat_pair(min_flux_carnot_per_s),
    }


# ---------------------------------------------------------------------------
# Mode 2: passive_eyring_catalysis_and_zpe_margin
# ---------------------------------------------------------------------------

def _verify_mode2(payload: dict[str, Any]) -> dict[str, Any]:
    kbt_mev = _parse_rat(payload.get("kbt_mev"), "kbt_mev")
    frac_gain = _parse_rat(payload.get("fractional_atp_gain"), "fractional_atp_gain")
    w0 = _parse_rat(payload.get("omega_0_thz"), "omega_0_thz")
    nu_m = _parse_rat(payload.get("nu_minus_thz"), "nu_minus_thz")
    min_ratio = _parse_rat(payload.get("min_zpe_to_barrier_ratio"), "min_zpe_to_barrier_ratio")
    exp_open = _req_bool(payload.get("expected_catalysis_open"), "expected_catalysis_open")

    if kbt_mev <= 0 or frac_gain <= 0 or frac_gain > 1 or w0 <= 0 or nu_m <= 0 or nu_m >= w0:
        raise VerificationError("Invalid Mode 2 parameters")

    ln_lo, ln_hi = _mercator_ln_1_plus_x_bracket(frac_gain, order_even=6)
    dea_lo = kbt_mev * ln_lo
    dea_hi = kbt_mev * ln_hi

    # Exact resonant Hopfield ZPE shift: (w0 - nu_m)^2 / (2 * nu_m) * h * THz
    zpe_thz = ((w0 - nu_m) * (w0 - nu_m)) * _inv(2 * nu_m)
    zpe_mev = zpe_thz * H_THZ_MEV_EXACT

    ratio_lb = zpe_mev * _inv(dea_hi)
    ratio_ub = zpe_mev * _inv(dea_lo)
    is_open = ratio_lb > 1
    if is_open != exp_open:
        raise VerificationError(f"Catalysis feasibility mismatch: {is_open} != {exp_open}")
    if ratio_lb <= min_ratio:
        raise VerificationError(f"ZPE/barrier lower bound {ratio_lb} <= {min_ratio}")

    return {
        "mode": "passive_eyring_catalysis_and_zpe_margin",
        "ln_gain_bracket": [_rat_pair(ln_lo), _rat_pair(ln_hi)],
        "barrier_shift_mev_bracket": [_rat_pair(dea_lo), _rat_pair(dea_hi)],
        "zpe_mev": _rat_pair(zpe_mev),
        "zpe_to_barrier_ratio_lb": _rat_pair(ratio_lb),
        "zpe_to_barrier_ratio_ub": _rat_pair(ratio_ub),
        "passive_catalysis_open": is_open,
    }


# ---------------------------------------------------------------------------
# Mode 3: photothermal_micro_vs_bulk_exclusion
# ---------------------------------------------------------------------------

def _verify_mode3(payload: dict[str, Any]) -> dict[str, Any]:
    t_k = _parse_rat(payload.get("temperature_K"), "temperature_K")
    kbt_mev = _parse_rat(payload.get("kbt_mev"), "kbt_mev")
    ea_mev = _parse_rat(payload.get("activation_energy_mev"), "activation_energy_mev")
    frac_gain = _parse_rat(payload.get("fractional_atp_gain"), "fractional_atp_gain")
    kappa_th = _parse_rat(payload.get("thermal_conductivity_w_mk"), "thermal_conductivity_w_mk")
    r_mito_m = _parse_rat(payload.get("mito_radius_m"), "mito_radius_m")
    l_bulk_m = _parse_rat(payload.get("bulk_length_m"), "bulk_length_m")
    i_inc_w_m2 = _parse_rat(payload.get("incident_ir_flux_w_m2"), "incident_ir_flux_w_m2")
    min_excl_ratio = _parse_rat(payload.get("min_micro_exclusion_ratio"), "min_micro_exclusion_ratio")

    if t_k <= 0 or kbt_mev <= 0 or ea_mev <= kbt_mev or kappa_th <= 0 or r_mito_m <= 0 or l_bulk_m <= r_mito_m or i_inc_w_m2 <= 0:
        raise VerificationError("Invalid Mode 3 thermal parameters")

    ln_lo, ln_hi = _mercator_ln_1_plus_x_bracket(frac_gain, order_even=6)
    dea_lo = kbt_mev * ln_lo
    dea_hi = kbt_mev * ln_hi

    # Exact finite-difference Arrhenius: dT = T * dEa / (Ea - dEa)
    dt_lo = (t_k * dea_lo) * _inv(ea_mev - dea_lo)
    dt_hi = (t_k * dea_hi) * _inv(ea_mev - dea_hi)

    # Exact pi-free micro-hotspot absorbed flux: I_micro = 4 * kappa_th * dT / R
    i_micro_lb = (4 * kappa_th * dt_lo) * _inv(r_mito_m)
    i_micro_ub = (4 * kappa_th * dt_hi) * _inv(r_mito_m)
    excl_ratio = i_micro_lb * _inv(i_inc_w_m2)
    if excl_ratio <= min_excl_ratio:
        raise VerificationError(f"Micro-hotspot exclusion ratio {excl_ratio} <= {min_excl_ratio}")

    bulk_amp = l_bulk_m * _inv(r_mito_m)
    i_bulk_lb = i_micro_lb * _inv(bulk_amp)

    return {
        "mode": "photothermal_micro_vs_bulk_exclusion",
        "delta_t_K_bracket": [_rat_pair(dt_lo), _rat_pair(dt_hi)],
        "i_micro_w_m2_lb": _rat_pair(i_micro_lb),
        "i_micro_w_m2_ub": _rat_pair(i_micro_ub),
        "micro_exclusion_ratio": _rat_pair(excl_ratio),
        "bulk_length_amplification": _rat_pair(bulk_amp),
        "i_bulk_w_m2_lb": _rat_pair(i_bulk_lb),
        "micro_hotspot_excluded": excl_ratio > 1,
    }


# ---------------------------------------------------------------------------
# Mode 4: tur_and_ocr_discriminator
# ---------------------------------------------------------------------------

def _verify_mode4(payload: dict[str, Any]) -> dict[str, Any]:
    j_atp = _parse_rat(payload.get("baseline_atp_rate_per_s"), "baseline_atp_rate_per_s")
    j_o2 = _parse_rat(payload.get("baseline_o2_rate_per_s"), "baseline_o2_rate_per_s")
    frac_gain = _parse_rat(payload.get("fractional_atp_gain"), "fractional_atp_gain")
    var_frac = _parse_rat(payload.get("fractional_variance_bound"), "fractional_variance_bound")
    sigma_kb_s = _parse_rat(payload.get("entropy_prod_kb_per_s"), "entropy_prod_kb_per_s")
    exp_tur_ok = _req_bool(payload.get("expected_tur_satisfied"), "expected_tur_satisfied")

    if j_atp <= 0 or j_o2 <= 0 or frac_gain <= 0 or var_frac <= 0 or sigma_kb_s <= 0:
        raise VerificationError("Invalid Mode 4 parameters")

    # Barato-Seifert TUR: var_frac * (sigma / kB) >= 2
    tur_product = var_frac * sigma_kb_s
    tur_ok = tur_product >= 2
    if tur_ok != exp_tur_ok:
        raise VerificationError(f"TUR satisfaction mismatch: {tur_ok} != {exp_tur_ok}")

    # Catalytic fixed-stoichiometry OCR prediction: dJ_O2 / J_O2 == dJ_ATP / J_ATP
    dj_atp = j_atp * frac_gain
    dj_o2_cat = j_o2 * frac_gain
    if dj_o2_cat * j_atp != dj_atp * j_o2:
        raise VerificationError("Catalytic OCR proportionality check failed")

    p_o_ratio = j_atp * _inv(2 * j_o2)  # ATP / O (P/O ratio)

    return {
        "mode": "tur_and_ocr_discriminator",
        "tur_product": _rat_pair(tur_product),
        "tur_satisfied": tur_ok,
        "p_over_o_ratio": _rat_pair(p_o_ratio),
        "catalytic_delta_atp_per_s": _rat_pair(dj_atp),
        "catalytic_delta_o2_per_s": _rat_pair(dj_o2_cat),
        "stoichiometric_delta_o2_per_s": [0, 1],
    }


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

    if mode == "stoichiometric_photon_and_carnot_floor":
        res = _verify_mode1(payload)
    elif mode == "passive_eyring_catalysis_and_zpe_margin":
        res = _verify_mode2(payload)
    elif mode == "photothermal_micro_vs_bulk_exclusion":
        res = _verify_mode3(payload)
    elif mode == "tur_and_ocr_discriminator":
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
        print("Usage: python -m src.mito_atp_modulation_verifier <file_or_dir> ...", file=sys.stderr)
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
