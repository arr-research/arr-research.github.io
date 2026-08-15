"""Exact-rational replay for the fixed-r finite certification theorem."""

from fractions import Fraction


def cutoff(r: int) -> int:
    base = Fraction((2 * r - 1) ** 2 * (r + 1), 4 * r * r * (r - 1))
    constant = (
        Fraction(2 * (r - 1) * (4 * r * r - 1), r + 1)
        * Fraction(1, 4 * r) ** (r * r)
    )
    assert base > 1
    m = 0
    value = constant
    while value <= 1:
        value *= base
        m += 1
    assert constant * base**m > 1
    if m:
        assert constant * base ** (m - 1) <= 1
    return m


def main() -> None:
    values = {r: cutoff(r) for r in range(2, 11)}
    assert values == {2: 12, 3: 58, 4: 165, 5: 360, 6: 672, 7: 1131, 8: 1766, 9: 2610, 10: 3695}

    # Optimized rational r=4 fixture used by the all-degree certificate.
    r = 4
    a = Fraction(19, 20)
    support_ratio_squared = Fraction(r - 1, r + 1)
    base = a * a / support_ratio_squared
    probability = Fraction(1, 40) ** 16
    constant = Fraction(2) * probability * Fraction(r - 1, 1) * Fraction(4 * r * r - 1, r + 1)
    m = 0
    value = constant
    while value <= 1:
        value *= base
        m += 1
    assert m == 134

    print({"status": "PASS", "universal_cutoffs_r2_to_r10": values, "optimized_r4": m})


if __name__ == "__main__":
    main()
