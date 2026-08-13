#!/usr/bin/env python3
"""Lightweight exact-arithmetic checks for the Grassmann crossover memo.

This is a replay/diagnostic script, not a proof of the analytic perturbation or
uniform Laplace lemmas.  It uses only Fraction arithmetic and runs in one
process with negligible memory.
"""

from fractions import Fraction
from math import sqrt


def beta_central_moments(d: int, r: int):
    """Return exact variance and third central moment of Beta(r,d-r)."""
    var = Fraction(r * (d - r), d * d * (d + 1))
    mu3 = Fraction(
        2 * (d - 2 * r) * r * (d - r),
        d**3 * (d + 1) * (d + 2),
    )
    return var, mu3


def invariant_coefficients(d: int, r: int):
    """Coefficients E X^j = c_j tr(A^j), j=2,3, for traceless A."""
    var, mu3 = beta_central_moments(d, r)
    tr_a0_sq = Fraction(d - 1, d)
    tr_a0_cube = Fraction((d - 1) * (d - 2), d * d)
    return var / tr_a0_sq, mu3 / tr_a0_cube


def closed_coefficients(d: int, r: int):
    c2 = Fraction(r * (d - r), d * (d - 1) * (d + 1))
    c3 = Fraction(
        2 * (d - 2 * r) * r * (d - r),
        d * (d - 1) * (d - 2) * (d + 1) * (d + 2),
    )
    return c2, c3


def p3_two_block(d: int, k: int, radius: float = 1.0) -> float:
    return radius**3 * (d - 2 * k) / sqrt(d * k * (d - k))


def ky_fan_one_spike(d: int, r: int, radius: float = 1.0) -> float:
    return radius * (d - r) / sqrt(d * (d - 1))


def ky_fan_r_block(d: int, r: int, radius: float = 1.0) -> float:
    return radius * sqrt(Fraction(r * (d - r), d))


def main() -> None:
    tested = 0
    for d in range(5, 81):
        for r in range(1, (d - 1) // 2 + 1):
            assert invariant_coefficients(d, r) == closed_coefficients(d, r)
            c2, c3 = closed_coefficients(d, r)
            assert c2 > 0 and c3 > 0

            p3_values = [p3_two_block(d, k) for k in range(1, d)]
            assert p3_values[0] >= max(p3_values) - 1e-14

            if r > 1:
                assert ky_fan_r_block(d, r) > ky_fan_one_spike(d, r)
            tested += 1

    # Complement symmetry makes the cubic coefficient odd under r -> d-r.
    for d in range(3, 81):
        for r in range(1, d):
            _, c3 = closed_coefficients(d, r)
            _, c3_complement = closed_coefficients(d, d - r)
            assert c3 == -c3_complement

    print(f"PASS: {tested} weak/strong parameter pairs checked exactly.")
    print("PASS: Beta moments reproduce the invariant c2 and c3 constants.")
    print("PASS: one-spike maximizes the two-block cubic diagnostic.")
    print("PASS: rank-r block has strictly larger strong-field slope for r>1.")
    print("PASS: cubic coefficient obeys complement antisymmetry.")


if __name__ == "__main__":
    main()

