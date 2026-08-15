"""Exact replay for the all-field Gr_C(3,6) two-block theorem.

The proof is the symbolic all-m induction recorded in
THEOREM_FRONTIER_GR36_TWO_BLOCK.md.  This script checks the closed coefficient
formulas, the factorizations driving the induction, and exact coefficients
through a declared finite diagnostic range.  It makes no full-spectrum claim.
"""

from __future__ import annotations

import sympy as sp


m, n, u = sp.symbols("m n u", integer=True, nonnegative=True)


def coefficient_formulas():
    b1 = 15 * sp.Rational(3, 10) ** m / (
        (2 * m + 3) * (2 * m + 5) * sp.factorial(2 * m + 1)
    )
    b2 = 360 * sp.Rational(3, 4) ** m / (
        (m + 2)
        * (m + 3)
        * (m + 4)
        * (2 * m + 3)
        * (2 * m + 5)
        * sp.factorial(2 * m + 1)
    )
    p = 64 * m**4 + 896 * m**3 + 4640 * m**2 + 10552 * m + 8931
    b3 = 135 * (19683 * 9**m - p) / (
        4 * 6**m * sp.factorial(2 * m + 9)
    )
    return tuple(map(sp.factor, (b1, b2, b3)))


def hankel_forms():
    i0 = 2 * sp.sinh(u) / u
    i1 = sp.simplify(i0 - sp.diff(i0, u, 2))
    i2 = sp.simplify(i0 - 2 * sp.diff(i0, u, 2) + sp.diff(i0, u, 4))
    forms = []
    for k, base in ((1, i2), (2, i1), (3, i0)):
        matrix = sp.Matrix(
            [[sp.diff(base, u, i + j) for j in range(k)] for i in range(k)]
        )
        forms.append(sp.factor(sp.simplify(matrix.det())))
    return tuple(forms)


def main() -> None:
    d1, d2, d3 = hankel_forms()
    expected1 = 16 * (
        u**2 * sp.sinh(u) - 3 * u * sp.cosh(u) + 3 * sp.sinh(u)
    ) / u**5
    expected2 = 8 * (
        2 * u**4
        + 2 * u**2 * sp.cosh(2 * u)
        + 4 * u**2
        - 6 * u * sp.sinh(2 * u)
        + 3 * sp.cosh(2 * u)
        - 3
    ) / u**8
    expected3 = -32 * (
        u**4 * sp.sinh(u)
        - 2 * u**3 * sp.cosh(u)
        + 3 * u**2 * sp.sinh(u)
        - sp.sinh(u) ** 3
    ) / u**9
    assert all(
        sp.simplify(left - right) == 0
        for left, right in zip((d1, d2, d3), (expected1, expected2, expected3))
    )
    assert [sp.limit(value, u, 0) for value in (d1, d2, d3)] == [
        sp.Rational(16, 15),
        sp.Rational(16, 45),
        sp.Rational(32, 135),
    ]

    b1, b2, b3 = coefficient_formulas()
    assert [sp.simplify(value.subs(m, 0)) for value in (b1, b2, b3)] == [1, 1, 1]
    assert [sp.simplify(value.subs(m, 1)) for value in (b1, b2, b3)] == [
        sp.Rational(3, 140)
    ] * 3

    p = 64 * m**4 + 896 * m**3 + 4640 * m**2 + 10552 * m + 8931
    p1 = 9 * p
    q1 = sp.Rational(1, 8) * (
        (m + 1) * (m + 2) * (m + 3) * (2 * m + 7) * (2 * m + 8) * (2 * m + 9)
    )
    p2 = 3 * p
    q2 = sp.Rational(1, 4) * (m + 1) * (2 * m + 7) * (2 * m + 9)

    rhs1 = 177147 * 9**m - p1 - 256 * sp.Rational(9, 5) ** m * q1
    rhs2 = 59049 * 9**m - p2 - 2048 * sp.Rational(9, 2) ** m * q2
    assert sp.simplify(
        4 * 6**m * sp.factorial(2 * m + 9) * (b3 - b1) / 15 - rhs1
    ) == 0
    assert sp.simplify(
        4 * 6**m * sp.factorial(2 * m + 9) * (b3 - b2) / 45 - rhs2
    ) == 0

    shifts = (
        (5 * q1 - q1.subs(m, m + 1), (n + 4) * (n + 5) * (n + 6) * (2 * n + 13) * (2 * n**2 + 14 * n + 15)),
        (9 * p1 - p1.subs(m, m + 1), 2304 * (n + 4) * (n + 5) * (n + 6) * (2 * n + 13)),
        (2 * q2 - q2.subs(m, m + 1), sp.Rational(1, 4) * (2 * n + 13) * (2 * n**2 + 11 * n + 6)),
        (9 * p2 - p2.subs(m, m + 1), 768 * (n + 4) * (n + 5) * (n + 6) * (2 * n + 13)),
    )
    for actual, expected in shifts:
        assert sp.expand(actual.subs(m, n + 2) - expected) == 0

    for degree_index in range(2, 65):
        assert sp.simplify((b3 - b1).subs(m, degree_index)) > 0
        assert sp.simplify((b3 - b2).subs(m, degree_index)) > 0

    # Exact low-degree completion of the Paper-15 Stein tail criterion for
    # the two losing Gr_C(3,6) strata.  D_k(v)/D_k(0) is the MGF of tr(H_k),
    # so z_k(u)=D_k(u/2)/D_k(0) is the MGF of Y_k=tr(B_k)-k/2.
    z1 = sp.simplify(d1.subs(u, u / 2) / sp.Rational(16, 15))
    z2 = sp.simplify(d2.subs(u, u / 2) / sp.Rational(16, 45))
    h1 = sp.simplify(
        sp.diff(z1, u, 2) + 174 * sp.diff(z1, u) / u - sp.Rational(25, 4) * z1
    )
    h2 = sp.simplify(
        sp.diff(z2, u, 2) + 69 * sp.diff(z2, u) / u - 4 * z2
    )
    h1_series = sp.series(h1, u, 0, 8).removeO().expand()
    h2_series = sp.series(h2, u, 0, 10).removeO().expand()
    assert h1_series.coeff(u, 0) == 0
    assert h1_series.coeff(u, 2) == -sp.Rational(1, 42)
    assert h2_series.coeff(u, 0) == 0
    assert h2_series.coeff(u, 2) == 0
    assert h2_series.coeff(u, 4) == -sp.Rational(1, 16170)
    assert h2_series.coeff(u, 6) == -sp.Rational(1, 840840)

    print("PASS: exact Gr_C(3,6) two-block Hankel forms and all-m induction identities")
    print("diagnostic: strict exact coefficient gaps checked for m=2,...,64")
    print("PASS: exact low-degree completion of the all-field Stein saddle signs")
    print("scope: all-field within two-level spectra; no full-spectrum or RDF claim")


if __name__ == "__main__":
    main()
