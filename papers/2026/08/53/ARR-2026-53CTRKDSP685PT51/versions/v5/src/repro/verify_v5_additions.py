"""Deterministic checks for the v5 joint and uniform-obstruction additions."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad

from explicit_sample_constants import moments


ROOT = Path(__file__).resolve().parents[1]
C_PLUS = math.sqrt(2.0 / math.pi)
PHI0 = 1.0 / math.sqrt(2.0 * math.pi)


def log_logistic_prime(t: float) -> float:
    absolute = abs(t)
    return -absolute - 2.0 * math.log1p(math.exp(-absolute))


def projector_distance(x: np.ndarray, y: np.ndarray) -> float:
    cosine = float(np.clip(abs(x @ y), 0.0, 1.0))
    return math.sqrt(max(0.0, 1.0 - cosine * cosine))


def check_logistic_ratio() -> None:
    for p in (0.4, 1.0, 2.3):
        for radius in (0.5, 3.0, 20.0):
            for lower, upper in ((0.01, 0.02), (0.2, 0.7), (1.0, 1.8)):
                ratio = math.exp(
                    p
                    * (
                        log_logistic_prime(radius * upper)
                        - log_logistic_prime(radius * lower)
                    )
                )
                envelope = 4.0**p * math.exp(-p * radius * (upper - lower))
                if ratio > envelope * (1.0 + 2e-14):
                    raise AssertionError((p, radius, lower, upper, ratio, envelope))


def check_threshold_constants() -> dict[str, float]:
    p = 1.3
    d = 7
    m = d - 1
    n = 240
    delta = 0.18
    epsilon = 0.12
    matrix_scale = math.sqrt(n) + math.sqrt(d) + math.sqrt(2.0 * math.log(3.0 / delta))
    prefactor = 9.0 * 4.0**p * C_PLUS**2 * m**3 * matrix_scale**2 / delta**2
    threshold = 3.0 * C_PLUS * n / (p * delta) * math.log(prefactor / epsilon)
    eta = prefactor * math.exp(-p * threshold * delta / (3.0 * C_PLUS * n))
    if not math.isclose(eta, epsilon, rel_tol=2e-13, abs_tol=0.0):
        raise AssertionError((eta, epsilon))

    matrix_scale_joint = math.sqrt(n) + math.sqrt(d) + math.sqrt(2.0 * math.log(6.0 / delta))
    joint_prefactor = 36.0 * 4.0**p * C_PLUS**2 * m**3 * matrix_scale_joint**2 / delta**2
    joint_threshold = 6.0 * C_PLUS * n / (p * delta) * math.log(
        72.0 * 4.0**p * C_PLUS**2 * m**3 * matrix_scale_joint**2 / (epsilon * delta**2)
    )
    joint_eta = joint_prefactor * math.exp(-p * joint_threshold * delta / (6.0 * C_PLUS * n))
    if not math.isclose(joint_eta, epsilon / 2.0, rel_tol=2e-13, abs_tol=0.0):
        raise AssertionError((joint_eta, epsilon / 2.0))
    return {"projector_threshold": threshold, "teacher_threshold": joint_threshold}


def check_samplewise_hierarchy() -> dict[str, float]:
    rng = np.random.default_rng(2026083012)
    checked = 0
    worst_ratio = 0.0
    for _ in range(120):
        d = 4
        n = 12
        m = d - 1
        samples = rng.standard_normal((n, d))
        weights = np.exp(-np.linspace(0.0, 70.0, n))
        selected = samples[:m].T
        tail = samples[m:].T
        singular_min = float(np.linalg.svd(selected, compute_uv=False)[-1])
        eta = float(weights[m] / weights[m - 1] * np.linalg.norm(tail, 2) ** 2 / singular_min**2)
        if eta >= 0.9:
            continue
        gram = (samples.T * weights) @ samples
        _, vectors = np.linalg.eigh(gram)
        _, _, vh = np.linalg.svd(samples[:m], full_matrices=True)
        error = projector_distance(vectors[:, 0], vh[-1])
        if error > eta * (1.0 + 2e-9) + 2e-10:
            raise AssertionError((error, eta))
        checked += 1
        worst_ratio = max(worst_ratio, error / eta)
    if checked < 40:
        raise AssertionError(checked)
    return {"checked": float(checked), "worst_error_over_eta": worst_ratio}


def logistic_prime_power(value: float, p: float) -> float:
    return math.exp(p * log_logistic_prime(value))


def check_angular_variance() -> dict[str, float]:
    radius = 50.0
    output: dict[str, float] = {}
    for p in (1.0, 2.0):
        alpha = quad(
            lambda z: logistic_prime_power(radius * z, p) * math.exp(-z * z / 2.0) / math.sqrt(2.0 * math.pi),
            -math.inf,
            math.inf,
            epsabs=2e-13,
        )[0]
        second = 3.0 * quad(
            lambda z: logistic_prime_power(radius * z, 2.0 * p)
            * math.exp(-z * z / 2.0)
            / math.sqrt(2.0 * math.pi),
            -math.inf,
            math.inf,
            epsabs=2e-13,
        )[0]
        observed = second / (alpha * alpha * radius)
        m0, _, _ = moments(p)
        m0_2p, _, _ = moments(2.0 * p)
        target = 3.0 * m0_2p / (PHI0 * m0 * m0)
        if not math.isclose(observed, target, rel_tol=2e-3, abs_tol=0.0):
            raise AssertionError((p, observed, target))
        output[str(int(p))] = observed
    return output


def check_certificate() -> None:
    payload = json.loads((ROOT / "repro" / "joint_spectral_resolution.json").read_text(encoding="utf-8"))
    if payload["schema"] != "arr.joint-spectral-resolution.v1" or payload["seed"] != 2026083011:
        raise AssertionError(payload)
    if payload["checked_bound_points"] < 40 or payload["projector_error"][-1] >= 1e-6:
        raise AssertionError(payload)


def main() -> None:
    check_logistic_ratio()
    thresholds = check_threshold_constants()
    hierarchy = check_samplewise_hierarchy()
    angular = check_angular_variance()
    check_certificate()
    print("PASS: v5 joint spectral constants, hierarchy bound, and angular-process variance")
    print(json.dumps({"thresholds": thresholds, "hierarchy": hierarchy, "angular": angular}, indent=2))


if __name__ == "__main__":
    main()
