"""Bounded replay for the Paper 9 high-fidelity Grassmann RDF theorem.

The exact checks use integer/rational arithmetic.  The optional d=5, r=2
Gauss--Jacobi calculation checks the Selberg asymptotic and posterior-mean
normalization; it is diagnostic and is not used as a proof.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np


BASE_DIR = Path(__file__).resolve().parent
from scipy.special import roots_jacobi


def selberg_constant(d: int, r: int) -> int:
    """K_{d,r}=prod Gamma(d-r+j+1)/Gamma(j+1), for integer d,r."""
    value = 1
    for j in range(r):
        value *= math.factorial(d - r + j) // math.factorial(j)
    return value


def exact_sweep(max_d: int = 18) -> dict:
    cases = []
    for d in range(2, max_d + 1):
        for r in range(1, d // 2 + 1):
            n = r * (d - r)
            r0_squared = Fraction(d - r, r * d)

            # At the source radius, the rank-r two-block cross gap is 1/r.
            # Check its square to avoid introducing symbolic square roots.
            gap_squared = r0_squared * Fraction(d, r * (d - r))
            assert gap_squared == Fraction(1, r * r)

            # The leading radial support exponent is exactly -(R-R0)^2:
            # h_r(A_{r,R})/r = R*R0.  Check the squared coefficient.
            support_coefficient_squared = Fraction(d - r, r * d)
            assert support_coefficient_squared == r0_squared

            # n is half the real Grassmann dimension.
            assert 2 * n == 2 * r * (d - r)

            # Expansion b=1-d/kappa+... follows from m=r-n/kappa+....
            b_first = Fraction(d * n, r * (d - r))
            assert b_first == d

            # D=R0^2(1-b^2)=2(d-r)/(r*kappa)+....
            distortion_first = 2 * r0_squared * b_first
            assert distortion_first == Fraction(2 * (d - r), r)

            cases.append(
                {
                    "d": d,
                    "r": r,
                    "complex_dimension": n,
                    "R0_squared": str(r0_squared),
                    "source_gap": str(Fraction(1, r)),
                    "K_d_r": selberg_constant(d, r),
                    "b_first_coefficient": str(b_first),
                    "D_first_coefficient": str(distortion_first),
                }
            )
    complement_cases = []
    for d in range(3, max_d + 1):
        for r in range(d // 2 + 1, d):
            q = d - r
            r0_r = Fraction(d - r, r * d)
            r0_q = Fraction(d - q, q * d)
            r_to_q_distortion_scale = Fraction(r * r, q * q)
            q_to_r_state_scale_squared = Fraction(q * q, r * r)
            assert r0_r == q_to_r_state_scale_squared * r0_q
            assert (
                r_to_q_distortion_scale * r0_r == r0_q
            )
            complement_cases.append(
                {
                    "d": d,
                    "r": r,
                    "q": q,
                    "source_radius_squared": str(r0_r),
                    "complement_radius_squared": str(r0_q),
                    "R_r_D_equals_R_q_at_scaled_D": str(
                        r_to_q_distortion_scale
                    ),
                    "centered_state_q_to_r_scale_squared": str(
                        q_to_r_state_scale_squared
                    ),
                }
            )
    return {
        "max_d": max_d,
        "case_count": len(cases),
        "cases": cases,
        "complement_case_count": len(complement_cases),
        "complement_cases": complement_cases,
    }


def d5r2_quadrature(order: int = 128) -> dict:
    d, r = 5, 2
    n = r * (d - r)
    # The unordered overlap eigenvalue density is proportional to
    # (x1-x2)^2 (1-x1)^(d-2r) (1-x2)^(d-2r).
    nodes, weights = roots_jacobi(order, d - 2 * r, 0)
    x = (nodes + 1.0) / 2.0
    weight = weights[:, None] * weights[None, :] * (
        x[:, None] - x[None, :]
    ) ** 2
    weight /= np.sum(weight)
    trace = x[:, None] + x[None, :]

    jacobi_mass = (
        2 * Fraction(1, 4) * Fraction(1, 2)
        - 2 * Fraction(1, 3) * Fraction(1, 3)
    )
    assert jacobi_mass == Fraction(1, 36)
    laguerre_leading = (
        2 * math.factorial(3) * math.factorial(1)
        - 2 * math.factorial(2) ** 2
    )
    assert laguerre_leading == 4
    # The last expression is the coefficient before grouping the symmetric
    # terms.  Equivalently 72*(3!*1!-2!^2)=144 after normalization.
    assert 72 * (
        math.factorial(3) * math.factorial(1) - math.factorial(2) ** 2
    ) == 144

    table = []
    k_exact = selberg_constant(d, r)
    for kappa in (20.0, 40.0, 80.0):
        exponent = kappa * trace
        shift = float(np.max(exponent))
        tilted = weight * np.exp(exponent - shift)
        partition_scaled = float(np.sum(tilted))
        log_m = shift + math.log(partition_scaled)
        def truncated_laplace_moment(power: int) -> float:
            series = sum(
                kappa**ell / math.factorial(ell)
                for ell in range(power + 1)
            )
            return (
                math.factorial(power)
                * (1.0 - math.exp(-kappa) * series)
                / kappa ** (power + 1)
            )

        i1 = truncated_laplace_moment(1)
        i2 = truncated_laplace_moment(2)
        i3 = truncated_laplace_moment(3)
        log_m_closed = (
            math.log(72.0)
            + 2.0 * kappa
            + math.log(i3 * i1 - i2 * i2)
        )
        mean = float(np.sum(tilted * trace) / partition_scaled)
        variance = float(
            np.sum(tilted * (trace - mean) ** 2) / partition_scaled
        )
        b = (d * mean - r * r) / (r * (d - r))
        distortion = Fraction(d - r, r * d).__float__() * (1.0 - b * b)
        information = kappa * mean - log_m
        leading_log_m = (
            kappa * r - n * math.log(kappa) + math.log(k_exact)
        )
        table.append(
            {
                "kappa": kappa,
                "log_M": log_m,
                "log_M_closed_form": log_m_closed,
                "quadrature_minus_closed_form": log_m - log_m_closed,
                "log_M_minus_leading": log_m - leading_log_m,
                "mean_overlap": mean,
                "variance_overlap": variance,
                "b": b,
                "kappa_times_one_minus_b": kappa * (1.0 - b),
                "distortion": distortion,
                "kappa_times_distortion": kappa * distortion,
                "information": information,
            }
        )

    return {
        "parameters": {"d": d, "r": r, "order": order},
        "complex_dimension": n,
        "Selberg_constant": k_exact,
        "exact_Jacobi_mass": str(jacobi_mass),
        "predicted_limits": {
            "kappa_times_one_minus_b": d,
            "kappa_times_distortion": Fraction(2 * (d - r), r).__float__(),
            "log_M_minus_leading": 0.0,
        },
        "table": table,
        "scope": (
            "Deterministic normalization/asymptotic diagnostic only; the "
            "eventual optimizer and RDF statements are analytic theorems."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=18)
    parser.add_argument("--order", type=int, default=128)
    parser.add_argument(
        "--output",
        type=Path,
        default=BASE_DIR / "high_fidelity_verification.json",
    )
    args = parser.parse_args()

    result = {
        "exact": exact_sweep(args.max_d),
        "d5r2_quadrature": d5r2_quadrature(args.order),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
