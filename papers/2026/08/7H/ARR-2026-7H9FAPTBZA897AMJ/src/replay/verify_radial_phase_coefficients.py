"""Bounded exact replay for the Paper-12 radial coefficient theorem.

This is diagnostic replay, not a substitute for the all-q proof.
It uses Python integers and Fraction only; no floating-point sign decision is
used in the coefficient or tail checks.
"""

from fractions import Fraction
from math import comb, factorial


def coefficient(q: int, r: int) -> Fraction:
    a = [Fraction(factorial(q), factorial(q + 2 * i)) for i in range(r + 1)]
    return 2 * sum(
        Fraction(r - (2 * i - r) ** 2) * a[i] * a[r - i]
        for i in range(r + 1)
    )


def central_variance(q: int, r: int) -> Fraction:
    m = q + r
    weights = [comb(2 * m, m + d) for d in range(-r, r + 1, 2)]
    return Fraction(
        sum(d * d * w for d, w in zip(range(-r, r + 1, 2), weights)),
        sum(weights),
    )


def rho(r: int) -> Fraction:
    return Fraction((r - 1) * (r - 2), (3 * r + 4) * (3 * r + 5))


def geometric_majorant(r: int) -> Fraction:
    rr = rho(r)
    a = r + 2
    return (
        Fraction(a * a - r, 1 - rr)
        + Fraction(4 * a, 1) * rr / (1 - rr) ** 2
        + Fraction(4, 1) * rr * (1 + rr) / (1 - rr) ** 3
    )


def tail_bound(r: int) -> Fraction:
    return (
        Fraction(4 * comb(4 * r + 2, 3 * r + 3), 2 ** (4 * r + 2))
        * geometric_majorant(r)
    )


def main() -> None:
    checked = 0
    for q in range(4, 61):
        for r in range(2, 121):
            c = coefficient(q, r)
            expected = 0 if (q, r) == (4, 3) else (-1 if r < q else 1)
            observed = (c > 0) - (c < 0)
            assert observed == expected, (q, r, c)
            variance_sign = (Fraction(r) - central_variance(q, r) > 0) - (
                Fraction(r) - central_variance(q, r) < 0
            )
            assert variance_sign == observed, (q, r)
            checked += 1

    previous = None
    for r in range(4, 301):
        bound = tail_bound(r)
        assert bound < Fraction(1, 2), (r, bound)
        if previous is not None:
            assert bound < previous, (r, bound, previous)
        previous = bound

    assert tail_bound(4) == Fraction(125128041, 301137536)
    print(f"PASS: {checked} exact coefficient signs; 297 exact tail bounds")


if __name__ == "__main__":
    main()
