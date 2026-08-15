"""Exact-rational diagnostic for two-block moment differences.

The identities are Schur--Weyl formulas.  A finite screen cannot establish
the all-degree theorem; it can, however, turn any negative sign into a
rigorous counterexample.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import factorial


def partitions(total: int, cap: int | None = None):
    if total == 0:
        yield ()
        return
    cap = total if cap is None else min(total, cap)
    for first in range(cap, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


@lru_cache(None)
def hooks(lam: tuple[int, ...]) -> tuple[int, ...]:
    out = []
    for i, row in enumerate(lam):
        for j in range(row):
            out.append(row - j + sum(lower > j for lower in lam[i + 1 :]))
    return tuple(out)


def schur_ones(lam: tuple[int, ...], dimension: int) -> int:
    if len(lam) > dimension:
        return 0
    value = Fraction(1)
    q = 0
    for i, row in enumerate(lam):
        for j in range(row):
            value *= Fraction(dimension + j - i, hooks(lam)[q])
            q += 1
    assert value.denominator == 1
    return value.numerator


def rising(a: int, count: int) -> int:
    value = 1
    for j in range(count):
        value *= a + j
    return value


@lru_cache(None)
def raw_moment(order: int, r: int, k: int) -> Fraction:
    if order == 0:
        return Fraction(1)
    value = Fraction(0)
    for lam in partitions(order):
        if len(lam) > min(k, r):
            continue
        hook_product = 1
        for h in hooks(lam):
            hook_product *= h
        f_lam = factorial(order) // hook_product
        poch_r = poch_n = 1
        for i, row in enumerate(lam):
            poch_r *= rising(r - i, row)
            poch_n *= rising(2 * r - i, row)
        value += Fraction(f_lam * schur_ones(lam, k) * poch_r, poch_n)
    return value


def centered_even(order: int, r: int, k: int) -> Fraction:
    assert order % 2 == 0
    value = Fraction(0)
    for j in range(order + 1):
        value += Fraction(factorial(order), factorial(j) * factorial(order - j)) * Fraction(
            -k, 2
        ) ** (order - j) * raw_moment(j, r, k)
    return value


def scaled_even(order: int, r: int, k: int) -> Fraction:
    # X_k = sqrt(2r/[k(2r-k)]) Y_k; compare even powers without radicals.
    return centered_even(order, r, k) * Fraction(2 * r, k * (2 * r - k)) ** (order // 2)


def main() -> None:
    cases = 0
    for r in range(2, 16):
        # Near-balanced multiplicities are the narrowest-support-gap cases.
        for k in sorted({1, max(1, r // 2), r - 1}):
            if k >= r:
                continue
            for order in range(4, 22, 2):
                gap = scaled_even(order, r, r) - scaled_even(order, r, k)
                assert gap > 0, (r, k, order, gap)
                cases += 1
    print({"status": "NO_COUNTEREXAMPLE_EXACT_FINITE_SCREEN", "cases": cases})


if __name__ == "__main__":
    main()
