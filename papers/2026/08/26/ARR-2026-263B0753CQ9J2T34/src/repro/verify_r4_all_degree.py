"""Exact all-degree two-block certificate for Gr_C(4,8).

Degrees 4 through 268 are checked by exact Hankel-series arithmetic.  The
remaining tail is covered analytically by an explicit support/event bound.
No floating-point sign decision is used.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import factorial


MAX_M = 134


def permutation_sign(p: tuple[int, ...]) -> int:
    inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inversions % 2 else 1


def integral_even(a: int, t: int) -> Fraction:
    value = Fraction(2 ** (2 * a + 1) * factorial(a) ** 2, factorial(2 * a + 1))
    for j in range(t):
        value *= Fraction(2 * j + 1, 2 * j + 2 * a + 3)
    return value


def derivative_series(a: int, offset: int, maximum_power: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(maximum_power + 1)]
    for power in range(maximum_power + 1):
        degree = power + offset
        if degree % 2 == 0:
            out[power] = integral_even(a, degree // 2) / factorial(power)
    return out


def convolve(left: list[Fraction], right: list[Fraction], maximum_power: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(maximum_power + 1)]
    for i, x in enumerate(left):
        if not x:
            continue
        for j, y in enumerate(right[: maximum_power + 1 - i]):
            if y:
                out[i + j] += x * y
    return out


def determinant_series(k: int, a: int, maximum_power: int) -> list[Fraction]:
    # Group equal multisets of derivative offsets before multiplying series.
    groups: Counter[tuple[int, ...]] = Counter()
    for p in permutations(range(k)):
        offsets = tuple(sorted(i + p[i] for i in range(k)))
        groups[offsets] += permutation_sign(p)

    derivative_cache = {
        d: derivative_series(a, d, maximum_power)
        for d in range(2 * k - 1)
    }
    total = [Fraction(0) for _ in range(maximum_power + 1)]
    for offsets, multiplicity in groups.items():
        if multiplicity == 0:
            continue
        product = [Fraction(1)] + [Fraction(0) for _ in range(maximum_power)]
        for offset in offsets:
            product = convolve(product, derivative_cache[offset], maximum_power)
        for i, value in enumerate(product):
            total[i] += multiplicity * value
    return total


def mgf_even_coefficients(k: int) -> list[Fraction]:
    maximum_power = 2 * MAX_M
    series = determinant_series(k, 4 - k, maximum_power)
    normalizer = series[0]
    assert normalizer > 0
    scale_squared = Fraction(2, k * (8 - k))  # (c_k/2)^2
    return [series[2 * m] / normalizer * scale_squared**m for m in range(MAX_M + 1)]


def main() -> None:
    coefficients = {k: mgf_even_coefficients(k) for k in range(1, 5)}
    for k in range(1, 4):
        assert coefficients[k][0] == coefficients[4][0] == 1
        assert coefficients[k][1] == coefficients[4][1]
        for m in range(2, MAX_M + 1):
            assert coefficients[4][m] > coefficients[k][m], (k, m)

    # For m>=134, use |X_k|<=rho_3 for every k<4 and E X_k^2=2/63.
    # The balanced event H>(19/20)I (and its negative copy) has exact
    # probability 2*(1/40)^16 and gives |X_4|>(19/20)*sqrt(2).
    # The lower/upper moment ratio is
    #   (378/5)*40^(-16)*(361/240)^m,
    # which is >1 at m=134 and increases thereafter.
    tail_ratio = Fraction(378, 5) * Fraction(1, 40) ** 16 * Fraction(361, 240) ** 134
    assert tail_ratio > 1

    print(
        {
            "status": "PASS",
            "rank": 4,
            "exact_coefficient_range": [2, MAX_M],
            "tail_starts": 134,
            "tail_ratio_at_start": str(tail_ratio),
        }
    )


if __name__ == "__main__":
    main()
