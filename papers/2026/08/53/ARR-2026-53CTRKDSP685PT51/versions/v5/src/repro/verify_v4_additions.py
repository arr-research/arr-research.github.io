"""Deterministic checks for the v4 phase, lower-tail, and eigenspace additions."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.special import gamma

from explicit_sample_constants import moments


ROOT = Path(__file__).resolve().parents[1]
PHI0 = 1.0 / math.sqrt(2.0 * math.pi)


def close(a: float, b: float, tolerance: float = 2e-10) -> None:
    if not math.isclose(a, b, rel_tol=tolerance, abs_tol=tolerance):
        raise AssertionError((a, b, tolerance))


def check_confidence_constants() -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    tail_cutoffs = {1.0: 6.255617232612532, 2.0: 3.517897910753385}
    expected_delta = {1.0: 1.4660271729156032e-34, 2.0: 6.001630555411756e-29}
    for p in (1.0, 2.0):
        m0, _, _ = moments(p)
        m0_2p, m2_2p, _ = moments(2.0 * p)
        m0_4p, _, _ = moments(4.0 * p)
        l_p = m0_2p / (2.0 * PHI0 * m0**2)
        k_p = 4.0 * m0_4p / (PHI0 * m0_2p**2)
        radius = math.sqrt(m2_2p / m0_2p)
        delta_hc = 0.5 * math.exp(-12.0 * PHI0 * tail_cutoffs[p] * k_p)
        if not math.isclose(delta_hc, expected_delta[p], rel_tol=2e-12, abs_tol=0.0):
            raise AssertionError((p, delta_hc, expected_delta[p]))
        if not l_p > 0.0 or not k_p > 0.0 or not radius > 0.0:
            raise AssertionError((p, l_p, k_p, radius))
        output[str(int(p))] = {
            "L_p": l_p,
            "K_p": k_p,
            "radius": radius,
            "a_p": tail_cutoffs[p],
            "delta_hc": delta_hc,
        }
    return output


def check_phase_certificate() -> list[dict[str, float | str]]:
    payload = json.loads((ROOT / "repro" / "radial_phase_transition.json").read_text(encoding="utf-8"))
    if payload["schema"] != "arr.radial-phase-transition.v1" or payload["dimension"] != 3:
        raise AssertionError(payload)
    expected = {0.5: 0.8115609745760033, 1.0: 1.3430830414331165, 2.0: 2.326288066546293}
    summary = []
    for record in payload["records"]:
        a = float(record["a"])
        close(float(record["leading_constant"]), expected[a])
        ratios = np.asarray(record["normalized_ratio"], dtype=float)
        if np.any(ratios <= 0.0) or ratios[-1] <= ratios[0]:
            raise AssertionError((a, ratios))
        summary.append({"a": a, "phase": record["phase"], "last_ratio": float(ratios[-1])})
    return summary


def check_spectral_certificate() -> dict[str, float]:
    payload = json.loads((ROOT / "repro" / "spectral_lexicography.json").read_text(encoding="utf-8"))
    if payload["schema"] != "arr.spectral-lexicography.v1" or payload["seed"] != 2026083004:
        raise AssertionError(payload)
    limit = payload["limit_experiment"]
    sizes = np.asarray(limit["sample_sizes"], dtype=float)
    medians = np.asarray(limit["median_sine"], dtype=float)
    scaled = sizes * medians
    if medians[-1] >= medians[0] / 8.0 or not 0.45 < scaled[-1] / scaled[-2] < 1.8:
        raise AssertionError((sizes, medians, scaled))
    finite = payload["finite_r_convergence"]
    distances = np.asarray(finite["median_projector_distance"], dtype=float)
    if distances[-1] >= distances[0] / 10.0:
        raise AssertionError(distances)
    lower_constant = math.exp(-0.5) / (24.0 * math.sqrt(2.0))
    close(lower_constant, 0.01787008093668139)
    return {
        "lower_constant": lower_constant,
        "last_n_times_median": float(scaled[-1]),
        "last_projector_distance": float(distances[-1]),
    }


def check_inverse_gaussian_identity() -> None:
    # Algebraic, sample-wise check of tan(theta)=||Y^{-1}zeta||.
    rng = np.random.default_rng(2026083005)
    for m in (2, 4, 7):
        y = rng.standard_normal((m, m))
        zeta = rng.standard_normal(m)
        tangent = np.linalg.solve(y, zeta)
        normal = np.concatenate((-tangent, [1.0]))
        normal /= np.linalg.norm(normal)
        tan_from_normal = np.linalg.norm(normal[:-1]) / abs(normal[-1])
        close(tan_from_normal, float(np.linalg.norm(tangent)), tolerance=2e-12)


def main() -> None:
    confidence = check_confidence_constants()
    phases = check_phase_certificate()
    spectral = check_spectral_certificate()
    check_inverse_gaussian_identity()
    print("PASS: v4 exact phases, explicit confidence constants, and spectral lexicography diagnostics")
    print(json.dumps({"confidence": confidence, "phases": phases, "spectral": spectral}, indent=2))


if __name__ == "__main__":
    main()
