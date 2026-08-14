"""Exact, lightweight checks for the Slater Cartan dimensions and MGF series.

The representation-theoretic projection identity is proved in the memo; this
script only checks equivalent closed forms and coefficient ratios.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial


def weyl_rectangular_dimension(n: int, k: int, m: int) -> int:
    value = Fraction(1)
    for i in range(1, k + 1):
        for j in range(k + 1, n + 1):
            value *= Fraction(m + j - i, j - i)
    assert value.denominator == 1
    return value.numerator


def hook_content_dimension(n: int, k: int, m: int) -> int:
    # Schur functor for the k-by-m rectangle (m^k).
    value = Fraction(1)
    for row in range(1, k + 1):
        for col in range(1, m + 1):
            hook = (m - col) + (k - row) + 1
            value *= Fraction(n + col - row, hook)
    assert value.denominator == 1
    return value.numerator


def mgf_coefficient(n: int, k: int, m: int) -> Fraction:
    d_m = weyl_rectangular_dimension(n, k, m)
    return Fraction(1, 4**m * factorial(m) ** 2 * d_m)


def rising(x: int, m: int) -> int:
    out = 1
    for ell in range(m):
        out *= x + ell
    return out


def main() -> None:
    checked = 0
    for n in range(2, 9):
        for k in range(1, n):
            d1 = weyl_rectangular_dimension(n, k, 1)
            d2 = weyl_rectangular_dimension(n, k, 2)
            assert d1 == comb(n, k)
            assert d2 == comb(n, k) * comb(n + 1, k) // (k + 1)
            assert (d1*d1 > 2*d2) == ((k+1)*(n-k+1) > 2*(n+1))
            for m in range(0, 7):
                d = weyl_rectangular_dimension(n, k, m)
                assert d == hook_content_dimension(n, k, m)
                assert d == weyl_rectangular_dimension(n, n - k, m)
                pochhammer_d = Fraction(1)
                for i in range(1, k + 1):
                    pochhammer_d *= Fraction(rising(n-k+i, m), rising(i, m))
                assert pochhammer_d == d

                # Hypergeometric parameter form:
                # prod(c)_m/(c+1)_m = prod c/(c+m) = 1/d_m.
                inv_d = Fraction(1)
                for i in range(1, k + 1):
                    for j in range(k + 1, n + 1):
                        c = j - i
                        rising_c = 1
                        rising_cp1 = 1
                        for ell in range(m):
                            rising_c *= c + ell
                            rising_cp1 *= c + 1 + ell
                        inv_d *= Fraction(rising_c, rising_cp1)
                assert inv_d == Fraction(1, d)
                assert mgf_coefficient(n, k, m) > 0
                checked += 1

    print(f"PASS: {checked} exact Weyl/hook/hypergeometric coefficient checks")


if __name__ == "__main__":
    main()
