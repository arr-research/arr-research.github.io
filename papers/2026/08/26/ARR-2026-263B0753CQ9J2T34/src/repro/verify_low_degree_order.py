"""Exact replay for the all-rank moment-order certificates through degree 10."""

from __future__ import annotations

import sympy as sp

from exact_moment_screen import scaled_even


def all_coefficients_positive(poly: sp.Expr, variable: sp.Symbol) -> bool:
    return all(c > 0 for c in sp.Poly(sp.expand(poly), variable).all_coeffs())


def main() -> None:
    r, q, x, y = sp.symbols("r q x y")

    a6 = 12 * r**4 - 27 * r**2 + 8
    n6 = a6 * q - 32 * r**4 + 8 * r**2
    assert all_coefficients_positive(a6.subs(r, y + 3), y)
    assert all_coefficients_positive(n6.subs({r: y + 3, q: 2 * (y + 3) - 1}), y)

    a8 = 12 * r**6 - 111 * r**4 + 163 * r**2 - 60
    b8 = -76 * r**6 + 163 * r**4 - 60 * r**2
    c8 = 240 * r**6 - 60 * r**4
    p8 = a8 * q**2 + b8 * q + c8
    p8_shift = sp.Poly(sp.expand(p8.subs({r: y + 4, q: 2 * (y + 4) - 1 + x})), x)
    for coefficient in p8_shift.all_coeffs():
        assert all_coefficients_positive(coefficient, y)

    a10 = 80 * r**10 - 2040 * r**8 + 14005 * r**6 - 34367 * r**4 + 35100 * r**2 - 12096
    b10 = -880 * r**10 + 11800 * r**8 - 34367 * r**6 + 35100 * r**4 - 12096 * r**2
    c10 = 6080 * r**10 - 28256 * r**8 + 35100 * r**6 - 12096 * r**4
    d10 = -21504 * r**10 + 53760 * r**8 - 12096 * r**6
    p10 = a10 * q**3 + b10 * q**2 + c10 * q + d10
    p10_shift = sp.Poly(sp.expand(p10.subs({r: y + 5, q: 2 * (y + 5) - 1 + x})), x)
    for coefficient in p10_shift.all_coeffs():
        assert all_coefficients_positive(coefficient, y)

    # Direct Schur--Weyl fixtures cover the exceptional ranks below the
    # positive-denominator thresholds and independently test the formulas'
    # sign consequences at ordinary ranks.
    d4 = (2 * r - 3) * (2 * r - 1) * (2 * r + 1) * (2 * r + 3)
    formula4 = 3 * (r**2 - q) / (2 * q * d4)
    d6 = (2 * r - 5) * (2 * r - 3) * (2 * r - 1) ** 2 * (2 * r + 1) ** 2 * (2 * r + 3) * (2 * r + 5)
    formula6 = 15 * (r**2 - q) * n6 / (4 * q**2 * r * d6)
    d8 = (2 * r - 7) * (2 * r - 5) * (2 * r - 3) * (2 * r - 1) ** 2 * (2 * r + 1) ** 2 * (2 * r + 3) * (2 * r + 5) * (2 * r + 7)
    formula8 = 105 * (r**2 - q) * p8 / (4 * q**3 * r**2 * d8)
    d10_den = (2 * r - 9) * (2 * r - 7) * (2 * r - 5) * (2 * r - 3) ** 2 * (2 * r - 1) ** 2 * (2 * r + 1) ** 2 * (2 * r + 3) ** 2 * (2 * r + 5) * (2 * r + 7) * (2 * r + 9)
    formula10 = 945 * (r**2 - q) * p10 / (8 * q**4 * r**3 * d10_den)

    formulas = {4: formula4, 6: formula6, 8: formula8, 10: formula10}
    thresholds = {4: 2, 6: 3, 8: 4, 10: 5}
    fixtures = 0
    for rv in range(2, 12):
        for kv in range(1, rv):
            for order in (4, 6, 8, 10):
                exact_gap = scaled_even(order, rv, rv) - scaled_even(order, rv, kv)
                assert exact_gap > 0
                if rv >= thresholds[order]:
                    qv = kv * (2 * rv - kv)
                    displayed = formulas[order].subs({r: rv, q: qv})
                    assert displayed == sp.Rational(exact_gap.numerator, exact_gap.denominator)
                fixtures += 1

    print({"status": "PASS", "exact_fixtures": fixtures, "maximum_degree": 10})


if __name__ == "__main__":
    main()
