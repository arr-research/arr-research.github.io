"""Lightweight replay for the exact Gr_C(2,4) all-distortion theorem.

Exact arithmetic checks the pair-sum transform, complete-homogeneous bound,
moments, and radial cumulants.  Deterministic quadrature checks the elementary
normalizer and reports a diagnostic first coexistence contact.  Numerics are
not used to prove spectral optimality or uniqueness of a radial branch.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq


def h_complete(values: tuple[Fraction, ...], degree: int) -> Fraction:
    h = [Fraction(0) for _ in range(degree + 1)]
    h[0] = Fraction(1)
    for value in values:
        old = h.copy()
        for k in range(1, degree + 1):
            h[k] = old[k] + value * h[k - 1]
    return h[degree]


def exact_simplex_sweep(denominator: int = 40, max_degree: int = 14) -> dict:
    checked = 0
    equality_counts: dict[str, int] = {}
    for degree in range(max_degree + 1):
        equal = 0
        for i in range(denominator + 1):
            for j in range(denominator - i + 1):
                k = denominator - i - j
                xyz = (
                    Fraction(i, denominator),
                    Fraction(j, denominator),
                    Fraction(k, denominator),
                )
                value = h_complete(xyz, degree)
                assert value <= 1
                if value == 1:
                    equal += 1
                checked += 1
        equality_counts[str(degree)] = equal
    # h_0 and h_1 are constant; h_m, m>=2, is equal only at 3 vertices.
    assert equality_counts["0"] == (denominator + 1) * (denominator + 2) // 2
    assert equality_counts["1"] == (denominator + 1) * (denominator + 2) // 2
    for degree in range(2, max_degree + 1):
        assert equality_counts[str(degree)] == 3
    return {
        "denominator": denominator,
        "max_degree": max_degree,
        "checked_inequalities": checked,
        "equality_counts": equality_counts,
    }


def exact_moment_checks() -> dict:
    # For ||A||_F=1, exact invariant moments from Schur--Weyl integration.
    p2 = Fraction(1)
    p4_balanced = Fraction(1, 4)
    moment2 = p2 / 15
    moment4 = (5 * p2 * p2 - 4 * p4_balanced) / 280
    assert moment2 == Fraction(1, 15)
    assert moment4 == Fraction(1, 70)

    # Expansion of 24/(sR)^4 [cosh(sR)-1-(sR)^2/2].
    partition_moment2 = Fraction(2 * 24, math.factorial(6))
    partition_moment4 = Fraction(24 * math.factorial(4), math.factorial(8))
    assert partition_moment2 == moment2
    assert partition_moment4 == moment4

    # For T-1=2 tr(S_Q P), ||S_Q||_F^2=1/4.
    variance_t = Fraction(1, 15)
    fourth_centered_t = Fraction(1, 70)
    fourth_cumulant_t = fourth_centered_t - 3 * variance_t**2
    assert fourth_cumulant_t == Fraction(1, 1050)
    lambda_spinodal = Fraction(30)

    return {
        "balanced_partition_moment2": str(moment2),
        "balanced_partition_moment4": str(moment4),
        "Var_T": str(variance_t),
        "centered_fourth_T": str(fourth_centered_t),
        "fourth_cumulant_T": str(fourth_cumulant_t),
        "zero_branch_spinodal_lambda": str(lambda_spinodal),
    }


def pair_sum_checks(samples: int = 200, seed: int = 20260813) -> dict:
    rng = np.random.default_rng(seed)
    maximum_residual = 0.0
    for _ in range(samples):
        a = rng.normal(size=4)
        a -= np.mean(a)
        x = a[0] + a[1]
        y = a[0] + a[2]
        z = a[0] + a[3]
        residual = abs(x * x + y * y + z * z - float(a @ a))
        maximum_residual = max(maximum_residual, residual)
    assert maximum_residual < 1.0e-12
    return {
        "samples": samples,
        "seed": seed,
        "maximum_pair_sum_norm_residual": maximum_residual,
    }


def _h_at_ones(n: int, degree: int) -> int:
    if degree < 0:
        return 0
    return math.comb(n + degree - 1, degree)


def schur_log_partition(a: np.ndarray, field: float, maximum: int = 80) -> float:
    """Independent Schur--Weyl series for d=4, r=2."""
    h = np.zeros(maximum + 3)
    h[0] = 1.0
    for value in a:
        old = h.copy()
        for degree in range(1, maximum + 3):
            h[degree] = old[degree] + value * h[degree - 1]
    partition = 0.0
    for degree in range(maximum + 1):
        moment = 0.0
        for q in range(degree // 2 + 1):
            p = degree - q
            f_lambda = (
                math.factorial(degree)
                * (p - q + 1)
                / (math.factorial(p + 1) * math.factorial(q))
            )
            s_rank = (
                _h_at_ones(2, p) * _h_at_ones(2, q)
                - _h_at_ones(2, p + 1) * _h_at_ones(2, q - 1)
            )
            s_dim = (
                _h_at_ones(4, p) * _h_at_ones(4, q)
                - _h_at_ones(4, p + 1) * _h_at_ones(4, q - 1)
            )
            s_a = h[p] * h[q]
            if q:
                s_a -= h[p + 1] * h[q - 1]
            moment += f_lambda * s_rank * s_a / s_dim
        partition += field**degree * moment / math.factorial(degree)
    return math.log(partition)


def divided_difference_log_partition(a: np.ndarray, field: float) -> float:
    x = a[0] + a[1]
    y = a[0] + a[2]
    z = a[0] + a[3]
    squared = np.array([x * x, y * y, z * z])
    total = 0.0
    for index in range(3):
        denominator = 1.0
        for other in range(3):
            if index != other:
                denominator *= squared[index] - squared[other]
        total += math.cosh(field * math.sqrt(squared[index])) / denominator
    return math.log(24.0 * total / field**4)


def hciz_cross_check(samples: int = 24, seed: int = 20260814) -> dict:
    rng = np.random.default_rng(seed)
    maximum_residual = 0.0
    accepted = 0
    while accepted < samples:
        a = rng.normal(size=4)
        a -= np.mean(a)
        a /= np.linalg.norm(a)
        x = a[0] + a[1]
        y = a[0] + a[2]
        z = a[0] + a[3]
        squared = np.array([x * x, y * y, z * z])
        if np.min(np.abs(squared[:, None] - squared[None, :] + np.eye(3))) < 1e-4:
            continue
        for field in (0.7, 2.0, 4.0):
            schur = schur_log_partition(a, field)
            divided = divided_difference_log_partition(a, field)
            maximum_residual = max(maximum_residual, abs(schur - divided))
        accepted += 1
    assert maximum_residual < 5.0e-10
    return {
        "samples": samples,
        "fields": [0.7, 2.0, 4.0],
        "seed": seed,
        "maximum_log_partition_residual": maximum_residual,
        "scope": "Independent deterministic formula cross-check; not the proof.",
    }


class JacobiNormalizer:
    def __init__(self, order: int) -> None:
        nodes, weights = leggauss(order)
        x = (nodes + 1.0) / 2.0
        w = weights / 2.0
        self.trace = x[:, None] + x[None, :]
        self.weight = 6.0 * w[:, None] * w[None, :] * (
            x[:, None] - x[None, :]
        ) ** 2
        assert abs(float(np.sum(self.weight)) - 1.0) < 1.0e-13

    def values(self, kappa: float) -> tuple[float, float, float]:
        exponent = kappa * self.trace
        shift = float(np.max(exponent))
        tilted = self.weight * np.exp(exponent - shift)
        mass = float(np.sum(tilted))
        log_m = shift + math.log(mass)
        mean = float(np.sum(tilted * self.trace) / mass)
        variance = float(np.sum(tilted * (self.trace - mean) ** 2) / mass)
        return log_m, mean, variance


def elementary_log_m(kappa: float) -> float:
    if abs(kappa) < 0.25:
        # Quadrature is more stable than subtracting four nearly equal terms.
        return JacobiNormalizer(96).values(kappa)[0]
    numerator = (
        math.exp(2.0 * kappa)
        - (kappa * kappa + 2.0) * math.exp(kappa)
        + 1.0
    )
    return math.log(12.0 * numerator / kappa**4)


def numerical_replay(order: int = 128) -> dict:
    quadrature = JacobiNormalizer(order)
    table = []
    for kappa in (0.5, 2.0, 5.0, 10.0, 20.0):
        log_q, mean, variance = quadrature.values(kappa)
        log_e = elementary_log_m(kappa)
        table.append(
            {
                "kappa": kappa,
                "log_M_quadrature": log_q,
                "log_M_elementary": log_e,
                "difference": log_q - log_e,
                "mean_overlap": mean,
                "variance_overlap": variance,
                "b": mean - 1.0,
                "D": 0.25 * (1.0 - (mean - 1.0) ** 2),
                "R": kappa * mean - log_q,
            }
        )
        assert abs(log_q - log_e) < 2.0e-12

    def contact(kappa: float) -> float:
        log_m, mean, _ = quadrature.values(kappa)
        return log_m - kappa - 0.5 * kappa * (mean - 1.0)

    kappa_c = brentq(contact, 2.0, 10.0, xtol=1.0e-13, rtol=1.0e-13)
    log_m, mean, _ = quadrature.values(kappa_c)
    b = mean - 1.0
    lam = 2.0 * kappa_c / b
    distortion = 0.25 * (1.0 - b * b)
    information = kappa_c * mean - log_m
    assert lam < 30.0
    return {
        "order": order,
        "normalizer_table": table,
        "diagnostic_first_positive_contact": {
            "kappa": kappa_c,
            "b": b,
            "lambda": lam,
            "D": distortion,
            "R": information,
            "contact_residual": contact(kappa_c),
            "scope": (
                "Diagnostic scalar root only. The theorem proves existence "
                "of a discontinuous onset but does not use this decimal or "
                "claim uniqueness of all positive contacts."
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--denominator", type=int, default=40)
    parser.add_argument("--max-degree", type=int, default=14)
    parser.add_argument("--order", type=int, default=128)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("work/tenth_paper/balanced_grassmann_verification.json"),
    )
    args = parser.parse_args()
    result = {
        "exact_simplex": exact_simplex_sweep(
            args.denominator, args.max_degree
        ),
        "exact_moments": exact_moment_checks(),
        "pair_sum_transform": pair_sum_checks(),
        "hciz_cross_check": hciz_cross_check(),
        "numerical": numerical_replay(args.order),
        "scope": (
            "Exact coefficientwise inequalities prove spectral optimality. "
            "Quadrature and the contact decimal are bounded diagnostics."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
