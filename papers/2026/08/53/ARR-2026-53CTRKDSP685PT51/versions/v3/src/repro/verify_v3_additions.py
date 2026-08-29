"""Deterministic checks for the sharp-complexity and spherical v3 additions."""

from __future__ import annotations

import json
import math
from pathlib import Path

from scipy.special import gamma, polygamma

from explicit_sample_constants import constants, moments
from verify_saturation_law import fixed_sphere_eigenvalues


ROOT = Path(__file__).resolve().parents[1]
PHI0 = 1.0 / math.sqrt(2.0 * math.pi)


def close(a: float, b: float, tol: float = 1e-12) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError((a, b, tol))


def main() -> None:
    expected = {
        1.0: (3.71718255692737, 22929, 22.479248806962307),
        2.0: (2.1530165380915105, 294162, 52.36896222874753),
    }
    lower_coefficients = {}
    for p, (radius, sample_constant, angle_constant) in expected.items():
        result = constants(p)
        close(result.radius_threshold, radius)
        if result.c_p != sample_constant:
            raise AssertionError((p, result.c_p, sample_constant))
        close(result.c_p_angle, angle_constant)
        m0, _, _ = moments(p)
        m0_2p, _, _ = moments(2.0 * p)
        lower_coefficients[str(int(p))] = m0_2p / (16.0 * PHI0 * m0 * m0)

    close(lower_coefficients["1"], 1.0 / (96.0 * PHI0))
    close(lower_coefficients["2"], 9.0 / (560.0 * PHI0))

    # Adjacent chi moments give Q_R=1 for a Gaussian radius.
    for d in (2, 5, 12):
        er = math.sqrt(2.0) * gamma((d + 1.0) / 2.0) / gamma(d / 2.0)
        er_inv = gamma((d - 1.0) / 2.0) / (math.sqrt(2.0) * gamma(d / 2.0))
        close(er / ((d - 1.0) * er_inv), 1.0)

    # Direct fixed-sphere quadrature approaches Q_R/[2 psi_1(p)].
    spherical_checks = []
    for d in (3, 7):
        q_radius = d / (d - 1.0)
        for p in (1.0, 2.0):
            r = 45.0
            alpha, beta = fixed_sphere_eigenvalues(r, p, d)
            scaled = (alpha / beta) / (r * r)
            target = q_radius / (2.0 * float(polygamma(1, p)))
            if abs(scaled / target - 1.0) > 0.012:
                raise AssertionError((d, p, scaled, target))
            spherical_checks.append(
                {"dimension": d, "p": p, "r": r, "scaled_ratio": scaled, "target": target}
            )

    for nu in (3.0, 5.0, 12.0):
        q_student = (nu - 2.0) / (nu - 1.0)
        if not 0.0 < q_student < 1.0:
            raise AssertionError((nu, q_student))

    certificate = json.loads((ROOT / "repro" / "finite_sample_resolution.json").read_text())
    if certificate["schema"] != "arr.finite-sample-resolution.v1":
        raise AssertionError(certificate["schema"])
    if certificate["seed"] != 2026082917 or certificate["repetitions"] != 320:
        raise AssertionError("finite-sample certificate settings changed")
    if len(certificate["sample_sizes"]) != 7:
        raise AssertionError("unexpected finite-sample grid")

    print("PASS: explicit C_p constants, matching-lower coefficients, spherical Q_R constants, and figure certificate")
    print(json.dumps({"lower_coefficients": lower_coefficients, "spherical_checks": spherical_checks}, indent=2))


if __name__ == "__main__":
    main()
