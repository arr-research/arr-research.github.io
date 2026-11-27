"""
MITO-USC-DRESSED-THERMO-CERT-1.0: Zero-floating-point exact algebraic verifier for
Gauge-Invariant Dressed Thermodynamics of Ultrastrong-Coupling Mito-Polaritons.

Direct continuation of ARR-2025-2AQXS44H6Z8GQAG2 (Dec 2025 / Jul 2026) and
ARR-2026-1E91AXEJYT890TQC (Nov 26, 2026), certifying:
  - Universal positive zero-point energy (ZPE) shift across arbitrary detuning & Helfrich horizon
  - Exact resonant ground-state virtual photon/phonon occupation & >5180x virtual/thermal dominance
  - Exact quadrature squeezing, symplectic purity entanglement witness det(2 V_a) > 1, and <H_int + H_{A^2}> = 0
  - Thermodynamic passivity (zero ergotropy), Coulomb-vs-Dipole (PZW) invariance, and dressed KMS balance.

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

SCHEMA_VERSION = "MITO-USC-DRESSED-THERMO-CERT-1.0"
MAX_JSON_BYTES = 1_000_000
MAX_RAT_ABS = 10**24
H_THZ_MEV_EXACT = Fraction(4135667696, 1_000_000_000)  # SI-2019 h * 1 THz / e in meV (exact rational approx to 1e-9)


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


def _req_list(val: Any, name: str, min_len: int = 1, max_len: int = 64) -> list[Any]:
    if not isinstance(val, list) or len(val) < min_len or len(val) > max_len:
        raise VerificationError(f"Expected list of length [{min_len}, {max_len}] for {name}")
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
# Mode 1: zpe_shift_and_helfrich_horizon
# ---------------------------------------------------------------------------

def _verify_mode1(payload: dict[str, Any]) -> dict[str, Any]:
    submode = _req_str(payload.get("submode"), "submode")

    if submode == "resonant_zpe_and_helfrich":
        w0 = _parse_rat(payload.get("omega_0_thz"), "omega_0_thz")
        nu_m = _parse_rat(payload.get("nu_minus_thz"), "nu_minus_thz")
        kappa_bend_mev = _parse_rat(payload.get("helfrich_bending_mev"), "helfrich_bending_mev")
        num_modes = _req_int(payload.get("num_coupled_modes"), "num_coupled_modes", 1, 100000)
        exp_exceeds = _req_bool(payload.get("expected_exceeds_helfrich"), "expected_exceeds_helfrich")
        if w0 <= 0 or nu_m <= 0 or nu_m >= w0 or kappa_bend_mev <= 0:
            raise VerificationError("Invalid resonant ZPE parameters")

        nu_p = (w0 * w0) * _inv(nu_m)
        g = (nu_p - nu_m) * Fraction(1, 2)
        s_sum = nu_p + nu_m
        # Exact universal identity: (nu_p + nu_m)^2 == (2*w0)^2 + 4*g^2
        if s_sum * s_sum != (2 * w0) * (2 * w0) + 4 * g * g:
            raise VerificationError("ZPE sum-square identity failed")

        delta_sum_thz = s_sum - 2 * w0
        if delta_sum_thz != ((w0 - nu_m) * (w0 - nu_m)) * _inv(nu_m):
            raise VerificationError("Exact resonant ZPE identity (w0 - nu_m)^2 / nu_m failed")

        zpe_thz = delta_sum_thz * Fraction(1, 2)
        zpe_mev = zpe_thz * H_THZ_MEV_EXACT
        total_zpe_mev = zpe_mev * num_modes
        exceeds = total_zpe_mev > kappa_bend_mev
        if exceeds != exp_exceeds:
            raise VerificationError(f"Helfrich threshold mismatch: {exceeds} != {exp_exceeds}")

        return {
            "mode": "zpe_shift_and_helfrich_horizon",
            "submode": submode,
            "nu_plus_thz": _rat_pair(nu_p),
            "zpe_shift_thz": _rat_pair(zpe_thz),
            "zpe_shift_mev": _rat_pair(zpe_mev),
            "num_coupled_modes": num_modes,
            "total_zpe_mev": _rat_pair(total_zpe_mev),
            "exceeds_helfrich_bending": exceeds,
        }

    if submode == "detuned_zpe_positivity":
        wc = _parse_rat(payload.get("omega_c_thz"), "omega_c_thz")
        w0 = _parse_rat(payload.get("omega_0_thz"), "omega_0_thz")
        g = _parse_rat(payload.get("coupling_g_thz"), "coupling_g_thz")
        s_lo = _parse_rat(payload.get("sum_bracket_lo_thz"), "sum_bracket_lo_thz")
        s_hi = _parse_rat(payload.get("sum_bracket_hi_thz"), "sum_bracket_hi_thz")
        if wc <= 0 or w0 <= 0 or g <= 0 or s_lo <= 0 or s_lo >= s_hi:
            raise VerificationError("Invalid detuned ZPE parameters")

        # Exact detuned identity: (nu_+ + nu_-)^2 = (wc + w0)^2 + 4*g^2
        s_sq = (wc + w0) * (wc + w0) + 4 * g * g
        if not (s_lo * s_lo < s_sq < s_hi * s_hi):
            raise VerificationError("Detuned (nu_+ + nu_-)^2 outside certified bracket")
        if s_lo <= wc + w0:
            raise VerificationError("Lower bracket does not prove strict positive ZPE shift")

        zpe_lo_thz = (s_lo - (wc + w0)) * Fraction(1, 2)
        zpe_hi_thz = (s_hi - (wc + w0)) * Fraction(1, 2)
        return {
            "mode": "zpe_shift_and_helfrich_horizon",
            "submode": submode,
            "sum_sq_thz2": _rat_pair(s_sq),
            "zpe_shift_lo_thz": _rat_pair(zpe_lo_thz),
            "zpe_shift_hi_thz": _rat_pair(zpe_hi_thz),
            "strictly_positive_zpe": zpe_lo_thz > 0,
        }

    raise VerificationError(f"Unknown Mode 1 submode: {submode}")


# ---------------------------------------------------------------------------
# Mode 2: virtual_occupation_squeezing_and_entanglement
# ---------------------------------------------------------------------------

def _verify_mode2(payload: dict[str, Any]) -> dict[str, Any]:
    w0 = _parse_rat(payload.get("omega_0_thz"), "omega_0_thz")
    nu_m = _parse_rat(payload.get("nu_minus_thz"), "nu_minus_thz")
    n_th_ub = _parse_rat(payload.get("thermal_occ_ub"), "thermal_occ_ub")
    min_ratio = _parse_rat(payload.get("min_virtual_to_thermal_ratio"), "min_virtual_to_thermal_ratio")
    if w0 <= 0 or nu_m <= 0 or nu_m >= w0 or n_th_ub <= 0:
        raise VerificationError("Invalid Mode 2 parameters")

    nu_p = (w0 * w0) * _inv(nu_m)
    g = (nu_p - nu_m) * Fraction(1, 2)
    s_sum = nu_p + nu_m

    # Exact resonant ground-state covariances (identical in Coulomb & Dipole gauges):
    # <q^2>_G = 1 / S, <p^2>_G = (nu_p^2 + nu_m^2) / (2*S)
    q_sq_g = _inv(s_sum)
    p_sq_g = (nu_p * nu_p + nu_m * nu_m) * _inv(2 * s_sum)
    q_sq_0 = _inv(2 * w0)
    p_sq_0 = w0 * Fraction(1, 2)

    q_squeeze = q_sq_g * _inv(q_sq_0)  # 2*w0 / S = 2*w0*nu_m / (w0^2 + nu_m^2) < 1
    p_antisqueeze = p_sq_g * _inv(p_sq_0)  # (nu_p^2 + nu_m^2) / (w0 * S) > 1
    if q_squeeze >= 1 or p_antisqueeze <= 1:
        raise VerificationError("Expected strict position squeezing and momentum anti-squeezing")

    # Exact marginal symplectic purity invariant det(2 V_a) = q_squeeze * p_antisqueeze = 1 + 4*g^2 / S^2 > 1
    det_2va = q_squeeze * p_antisqueeze
    det_formula = 1 + (4 * g * g) * _inv(s_sum * s_sum)
    if det_2va != det_formula or det_2va <= 1:
        raise VerificationError("Symplectic marginal entanglement purity identity failed")

    # Exact bare virtual occupation n_virt = (w0*<q^2> + <p^2>/w0 - 1) / 2 == (w0 - nu_m)^2 / (4*w0*nu_m)
    n_virt_cov = (w0 * q_sq_g + p_sq_g * _inv(w0) - 1) * Fraction(1, 2)
    n_virt_exact = ((w0 - nu_m) * (w0 - nu_m)) * _inv(4 * w0 * nu_m)
    if n_virt_cov != n_virt_exact:
        raise VerificationError("Virtual occupation covariance-vs-closed-form identity failed")

    # Exact interaction + A^2 cancellation: <G|H_C|G> - <G|H_0|G> == 0
    e_ground = s_sum * Fraction(1, 2)
    e_bare_total = w0 + w0 * (n_virt_exact + n_virt_exact)
    if e_ground != e_bare_total:
        raise VerificationError("Exact <H_int + H_{A^2}> = 0 cancellation failed")

    virt_over_th = n_virt_exact * _inv(n_th_ub)
    if virt_over_th <= min_ratio:
        raise VerificationError(f"Virtual/thermal ratio {virt_over_th} <= {min_ratio}")

    if "expected_n_virt" in payload:
        exp_nv = _parse_rat(payload["expected_n_virt"], "expected_n_virt")
        if exp_nv != n_virt_exact:
            raise VerificationError(f"n_virt mismatch: {n_virt_exact} != {exp_nv}")

    return {
        "mode": "virtual_occupation_squeezing_and_entanglement",
        "n_virt_exact": _rat_pair(n_virt_exact),
        "q_squeezing_ratio": _rat_pair(q_squeeze),
        "p_antisqueezing_ratio": _rat_pair(p_antisqueeze),
        "symplectic_purity_det_2Va": _rat_pair(det_2va),
        "virtual_to_thermal_lb": _rat_pair(virt_over_th),
        "interaction_plus_a2_expectation": [0, 1],
        "is_vacuum_entangled": det_2va > 1,
    }


# ---------------------------------------------------------------------------
# Mode 3: passivity_ergotropy_and_gauge_weights
# ---------------------------------------------------------------------------

def _verify_mode3(payload: dict[str, Any]) -> dict[str, Any]:
    submode = _req_str(payload.get("submode"), "submode")

    if submode == "passivity_zero_ergotropy":
        energies = [_parse_rat(x, f"energies[{i}]") for i, x in enumerate(_req_list(payload.get("energies"), "energies", 2, 16))]
        probs = [_parse_rat(x, f"probs[{i}]") for i, x in enumerate(_req_list(payload.get("probs"), "probs", 2, 16))]
        if len(energies) != len(probs):
            raise VerificationError("energies and probs length mismatch")
        for i in range(len(energies) - 1):
            if energies[i] > energies[i + 1]:
                raise VerificationError("energies must be sorted non-decreasing")
        if any(p < 0 for p in probs) or sum(probs, Fraction(0)) != 1:
            raise VerificationError("probs must form a valid probability distribution")

        mean_e = sum((e * p for e, p in zip(energies, probs)), Fraction(0))
        ground_e = energies[0]
        excess = mean_e - ground_e
        if excess < 0:
            raise VerificationError("Passivity violation: mean energy below ground state")

        # Ergotropy for passive state (non-increasing populations) is 0; for non-passive state > 0
        sorted_probs = sorted(probs, reverse=True)
        passive_e = sum((e * p for e, p in zip(energies, sorted_probs)), Fraction(0))
        ergotropy = mean_e - passive_e
        exp_passive = _req_bool(payload.get("expected_is_passive"), "expected_is_passive")
        is_passive = ergotropy == 0
        if is_passive != exp_passive:
            raise VerificationError(f"Passivity mismatch: {is_passive} != {exp_passive}")

        return {
            "mode": "passivity_ergotropy_and_gauge_weights",
            "submode": submode,
            "ground_energy": _rat_pair(ground_e),
            "mean_energy": _rat_pair(mean_e),
            "ergotropy": _rat_pair(ergotropy),
            "is_passive": is_passive,
        }

    if submode == "pzw_gauge_weight_swap":
        w0 = _parse_rat(payload.get("omega_0_thz"), "omega_0_thz")
        nu_m = _parse_rat(payload.get("nu_minus_thz"), "nu_minus_thz")
        n_dipoles = _req_int(payload.get("num_dipoles_N"), "num_dipoles_N", 2, 10**12)
        if w0 <= 0 or nu_m <= 0 or nu_m >= w0:
            raise VerificationError("Require 0 < nu_minus < omega_0")

        denom = w0 * w0 + nu_m * nu_m
        w_coul = (w0 * w0) * _inv(denom)
        w_dip = (nu_m * nu_m) * _inv(denom)
        if w_coul + w_dip != 1:
            raise VerificationError("Coulomb + Dipole complementarity failed")
        if not (w_dip < Fraction(1, 2) < w_coul):
            raise VerificationError("Expected w_dip < 1/2 < w_coul")

        dark_frac = Fraction(n_dipoles - 1, n_dipoles)
        if dark_frac < Fraction(1, 2):
            raise VerificationError("Dark-mode fraction below 1/2 for N >= 2")

        # Gauge-invariant physical dipole coordinate transition weight:
        # Single lower-polariton branch: |<G | sqrt(2*w0)*q_b | MP^->|^2 = w0*nu_m / (w0^2 + nu_m^2) -> 1/2 as g->0
        # Two-branch sum (quadrature squeezing): 2*w0*<G|q_b^2|G> = 2*w0*nu_m / (w0^2 + nu_m^2) -> 1 as g->0
        single_branch_dipole = (w0 * nu_m) * _inv(denom)
        two_branch_dipole_sum = (2 * w0 * nu_m) * _inv(denom)
        if single_branch_dipole <= 0 or single_branch_dipole >= Fraction(1, 2):
            raise VerificationError("Invalid single-branch gauge-invariant dipole transition weight")
        if two_branch_dipole_sum != 2 * single_branch_dipole or two_branch_dipole_sum >= 1:
            raise VerificationError("Invalid two-branch dipole sum weight")

        return {
            "mode": "passivity_ergotropy_and_gauge_weights",
            "submode": submode,
            "w_mat_coulomb": _rat_pair(w_coul),
            "w_mat_dipole": _rat_pair(w_dip),
            "single_branch_dipole_norm": _rat_pair(single_branch_dipole),
            "gauge_invariant_dipole_weight": _rat_pair(two_branch_dipole_sum),
            "dark_manifold_fraction": _rat_pair(dark_frac),
            "dark_scattering_coulomb_ratio": _rat_pair(w_coul * dark_frac),
            "dark_scattering_dipole_ratio": _rat_pair(w_dip * dark_frac),
        }

    raise VerificationError(f"Unknown Mode 3 submode: {submode}")


# ---------------------------------------------------------------------------
# Mode 4: dressed_kms_and_catalytic_zpe_margin
# ---------------------------------------------------------------------------

def _verify_mode4(payload: dict[str, Any]) -> dict[str, Any]:
    w0 = _parse_rat(payload.get("omega_0_thz"), "omega_0_thz")
    nu_m = _parse_rat(payload.get("nu_minus_thz"), "nu_minus_thz")
    kms_suppression = _parse_rat(payload.get("kms_inverse_factor"), "kms_inverse_factor")
    catalytic_barrier_mev = _parse_rat(payload.get("catalytic_barrier_mev"), "catalytic_barrier_mev")
    min_spurious_mult = _parse_rat(payload.get("min_spurious_heating_multiplier"), "min_spurious_heating_multiplier")
    min_zpe_cat_ratio = _parse_rat(payload.get("min_zpe_to_catalytic_ratio"), "min_zpe_to_catalytic_ratio")

    if w0 <= 0 or nu_m <= 0 or nu_m >= w0 or kms_suppression <= 1 or catalytic_barrier_mev <= 0:
        raise VerificationError("Invalid Mode 4 parameters")

    n_virt = ((w0 - nu_m) * (w0 - nu_m)) * _inv(4 * w0 * nu_m)
    spurious_mult = n_virt * kms_suppression
    if spurious_mult <= min_spurious_mult:
        raise VerificationError(f"Spurious heating multiplier {spurious_mult} <= {min_spurious_mult}")

    zpe_thz = ((w0 - nu_m) * (w0 - nu_m)) * _inv(2 * nu_m)
    zpe_mev = zpe_thz * H_THZ_MEV_EXACT
    zpe_cat_ratio = zpe_mev * _inv(catalytic_barrier_mev)
    if zpe_cat_ratio <= min_zpe_cat_ratio:
        raise VerificationError(f"ZPE/catalytic ratio {zpe_cat_ratio} <= {min_zpe_cat_ratio}")

    return {
        "mode": "dressed_kms_and_catalytic_zpe_margin",
        "n_virt_exact": _rat_pair(n_virt),
        "spurious_bare_heating_multiplier": _rat_pair(spurious_mult),
        "zpe_mev": _rat_pair(zpe_mev),
        "catalytic_barrier_mev": _rat_pair(catalytic_barrier_mev),
        "zpe_to_catalytic_ratio": _rat_pair(zpe_cat_ratio),
        "passive_catalysis_energetically_open": zpe_cat_ratio > 1,
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

    if mode == "zpe_shift_and_helfrich_horizon":
        res = _verify_mode1(payload)
    elif mode == "virtual_occupation_squeezing_and_entanglement":
        res = _verify_mode2(payload)
    elif mode == "passivity_ergotropy_and_gauge_weights":
        res = _verify_mode3(payload)
    elif mode == "dressed_kms_and_catalytic_zpe_margin":
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
        print("Usage: python -m src.mito_usc_dressed_thermo_verifier <file_or_dir> ...", file=sys.stderr)
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
