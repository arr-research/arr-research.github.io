"""Bounded exact replay for the Paper 12 global-phase coefficient theorem.

The proof is analytic.  This script checks its finite arithmetic, screens a
larger coefficient rectangle using integers only, and verifies the rational
tail-bound monotonicity certificate.  It uses no random sampling.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial
import json


def binomial_sum(q: int, r: int) -> int:
    """Positive factors removed from [x^(2r-1)] J_q(x)."""
    M = q + r
    return sum(
        (r - d * d) * comb(2 * M, M + d)
        for d in range(-r, r + 1, 2)
    )


def expected_sign(q: int, r: int) -> int:
    if r == 1 or (q, r) == (4, 3):
        return 0
    return -1 if r < q else 1


def convolution_coefficient(q: int, r: int) -> Fraction:
    """Coefficient from the direct Cauchy-product formula."""
    ans = Fraction(0)
    for i in range(r + 1):
        j = r - i
        ai = Fraction(factorial(q), factorial(q + 2 * i))
        aj = Fraction(factorial(q), factorial(q + 2 * j))
        ans += 2 * (r - (i - j) ** 2) * ai * aj
    return ans


def binomial_coefficient(q: int, r: int) -> Fraction:
    """Same coefficient after the centered-binomial reduction."""
    M = q + r
    return Fraction(2 * factorial(q) ** 2 * binomial_sum(q, r), factorial(2 * M))


def rho(r: int) -> Fraction:
    return Fraction((r - 1) * (r - 2), (3 * r + 4) * (3 * r + 5))


def tail_B(r: int) -> Fraction:
    return Fraction(
        (2 * r + 1) ** 2 * comb(4 * r + 2, r - 1),
        2 ** (4 * r - 1),
    ) / (1 - rho(r))


def ratio_polynomial_shift_coefficients() -> list[int]:
    # Coefficients in ascending powers of t after r=t+8.  Positivity proves
    # B_(r+1)/B_r < 1 for every integer r>=8.
    return [
        12273932391840,
        13783566886439,
        6925079425457,
        2050989435663,
        396725533319,
        52389135596,
        4784578836,
        298477658,
        12174752,
        293256,
        3168,
    ]


def tail_ratio_certificate(r: int) -> tuple[int, int]:
    """Denominator-minus-numerator for the exact ratio B_(r+1)/B_r."""
    numerator = (
        (r + 1) * (r + 3) * (2 * r + 3) ** 3 * (3 * r + 7)
        * (3 * r + 8) * (4 * r + 3) ** 2 * (4 * r + 5)
    )
    denominator = (
        6 * r * (r + 2) * (r + 4) * (2 * r + 1) ** 2
        * (3 * r + 4) ** 2 * (3 * r + 5) ** 2 * (4 * r + 7)
    )
    return denominator - numerator, denominator


def main() -> None:
    mismatches = []
    reduction_mismatches = []
    for q in range(4, 41):
        for r in range(1, 101):
            value = binomial_sum(q, r)
            sign = (value > 0) - (value < 0)
            if sign != expected_sign(q, r):
                mismatches.append({"q": q, "r": r, "sum": value})
            if q <= 10 and r <= 15 and convolution_coefficient(q, r) != binomial_coefficient(q, r):
                reduction_mismatches.append({"q": q, "r": r})

    boundary = {str(r): binomial_sum(r + 1, r) for r in range(4, 8)}
    B8 = tail_B(8)
    exact_ratio_decrease = all(tail_B(r + 1) < tail_B(r) for r in range(8, 41))
    shifted = ratio_polynomial_shift_coefficients()
    ratio_identity_ok = True
    for r in range(8, 41):
        difference, _ = tail_ratio_certificate(r)
        t = r - 8
        polynomial_value = sum(coef * t**power for power, coef in enumerate(shifted))
        ratio_identity_ok &= difference == polynomial_value

    report = {
        "coefficient_rectangle": {"q": [4, 40], "r": [1, 100]},
        "mismatches": mismatches,
        "binomial_reduction_mismatches_q_4_10_r_1_15": reduction_mismatches,
        "boundary_sums_r_4_to_7": boundary,
        "B8": {"numerator": B8.numerator, "denominator": B8.denominator},
        "B8_less_than_one": B8 < 1,
        "B_ratio_decreases_screen_r_8_to_40": exact_ratio_decrease,
        "shifted_difference_coefficients_all_positive": all(x > 0 for x in shifted),
        "tail_ratio_polynomial_identity_screen_r_8_to_40": ratio_identity_ok,
        "status": "PASS" if not mismatches and not reduction_mismatches and B8 < 1 and exact_ratio_decrease and all(x > 0 for x in shifted) and ratio_identity_ok else "FAIL",
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
