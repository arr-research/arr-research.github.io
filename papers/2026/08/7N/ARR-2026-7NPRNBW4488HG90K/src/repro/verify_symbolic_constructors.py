#!/usr/bin/env python3
"""Independent SymPy replay of the Paper 28 matrix constructors.

This route uses exact symbolic square roots and complex Hermitian arithmetic.
It is intentionally separate from the standard-library rational Gram checker.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
I = sp.I


def comm(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return a * b - b * a


def hs_inner(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(a.conjugate().T * b))


def hs_sq(a: sp.Matrix) -> sp.Expr:
    return hs_inner(a, a)


def flux(edges: list[sp.Matrix]) -> sp.Matrix:
    out = sp.zeros(edges[0].rows)
    for k in range(len(edges)):
        for j in range(k):
            out += I * comm(edges[k], edges[j]) / 2
    return sp.simplify(out)


def matrix_is_zero(a: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in a)


def one_spike_records(max_n: int = 2) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    fixtures: list[list[sp.Rational]] = []
    for n in range(1, max_n + 1):
        fixtures.append([sp.Rational(n - j + 1, n + 2) for j in range(1, n + 1)])
    fixtures.append([sp.Rational(3), sp.Rational(3)])

    for b in fixtures:
        b = sorted(b, reverse=True)
        n = len(b)
        tails = [sum(b[j:], sp.S.Zero) for j in range(n)]
        kappa = sum(((j + 1) * b[j] for j in range(n)), sp.S.Zero)
        assert sp.simplify(kappa - sum(tails, sp.S.Zero)) == 0

        cmat = sp.zeros(n + 1)
        for j, tail in enumerate(tails):
            cmat[j, j + 1] = sp.sqrt(2 * tail)
        h = sp.simplify((cmat + cmat.conjugate().T) / 2)
        k = sp.simplify((cmat - cmat.conjugate().T) / (2 * I))
        target = sp.simplify((cmat * cmat.conjugate().T - cmat.conjugate().T * cmat) / 2)
        expected = sp.diag(sum(b, sp.S.Zero), *[-x for x in b])
        assert matrix_is_zero(target - expected)
        assert matrix_is_zero(target + I * comm(h, k))
        assert sp.simplify(hs_sq(h) - kappa) == 0
        assert sp.simplify(hs_sq(k) - kappa) == 0
        assert sp.simplify(hs_inner(h, k)) == 0

        alpha = 2 / sp.root(3, 4)
        triangle = [
            alpha * h,
            alpha * (-h / 2 + sp.sqrt(3) * k / 2),
        ]
        triangle.append(-triangle[0] - triangle[1])
        assert matrix_is_zero(sum(triangle, sp.zeros(n + 1)))
        assert matrix_is_zero(flux(triangle) - target)
        triangle_norms = [sp.simplify(hs_sq(edge)) for edge in triangle]
        assert all(sp.simplify(value - 4 * kappa / sp.sqrt(3)) == 0 for value in triangle_norms)
        triangle_perimeter_sq = sp.simplify(sum(sp.sqrt(value) for value in triangle_norms) ** 2)
        assert sp.simplify(triangle_perimeter_sq - 12 * sp.sqrt(3) * kappa) == 0

        d1, d2 = sp.sqrt(2) * h, sp.sqrt(2) * k
        square = [
            (d1 - d2) / 2,
            (d1 + d2) / 2,
            -(d1 - d2) / 2,
            -(d1 + d2) / 2,
        ]
        assert matrix_is_zero(sum(square, sp.zeros(n + 1)))
        assert matrix_is_zero(flux(square) - target)
        square_norms = [sp.simplify(hs_sq(edge)) for edge in square]
        assert all(sp.simplify(value - kappa) == 0 for value in square_norms)
        square_perimeter_sq = sp.simplify(sum(sp.sqrt(value) for value in square_norms) ** 2)
        assert sp.simplify(square_perimeter_sq - 16 * kappa) == 0

        uniform = sum(b, sp.S.Zero) / n
        defect = sp.Rational(n + 1, 2) * sum(b, sp.S.Zero) - kappa
        gini = sp.Rational(1, 2) * sum(
            (b[i] - b[j] for i in range(n) for j in range(i + 1, n)),
            sp.S.Zero,
        )
        distance = sum((abs(x - uniform) for x in b), sp.S.Zero)
        assert sp.simplify(defect - gini) == 0
        assert sp.simplify(defect - sp.Rational(n, 4) * distance) >= 0
        assert sp.simplify(sp.Rational(n - 1, 2) * distance - defect) >= 0

        records.append(
            {
                "n": n,
                "b": [str(x) for x in b],
                "kappa": str(kappa),
                "singular_squares": [str(2 * x) for x in tails],
                "A3": str(triangle_perimeter_sq),
                "A4": str(square_perimeter_sq),
            }
        )
    return records


def gram_regressions() -> dict[str, object]:
    fixtures = [
        (
            sp.Matrix([[1, 0], [0, -1]]),
            sp.Matrix([[1, sp.Rational(1, 10)], [sp.Rational(1, 10), -1]]),
        ),
        (
            sp.Matrix([[1, 2], [2, -1]]),
            sp.Matrix([[0, 1], [1, 0]]),
        ),
        (
            sp.Matrix([[1, 1, 0], [1, -1, 2], [0, 2, 0]]),
            sp.Matrix([[0, 2, 1], [2, 1, 0], [1, 0, -1]]),
        ),
    ]
    rows: list[dict[str, str]] = []
    for d1, d2 in fixtures:
        a, b, c = hs_sq(d1), hs_sq(d2), hs_inner(d1, d2)
        q2 = sp.simplify(a * b - c**2)
        plus, minus = hs_sq(d1 + d2), hs_sq(d1 - d2)
        assert sp.simplify(plus * minus - ((a - b) ** 2 + 4 * q2)) == 0
        assert sp.simplify((a + b) ** 2 - 4 * q2) >= 0
        assert sp.simplify(plus * minus - 4 * q2) >= 0
        if a != 0:
            shear = sp.simplify(d2 - (c / a) * d1)
            assert sp.simplify(hs_inner(d1, shear)) == 0
            assert matrix_is_zero(comm(d1, shear) - comm(d1, d2))
            assert sp.simplify(a * hs_sq(shear) - q2) == 0
        rows.append({"a": str(a), "b": str(b), "c": str(c), "gram_determinant": str(q2)})

    d1, d2 = fixtures[0]
    a, b = hs_sq(d1), hs_sq(d2)
    plus, minus = hs_sq(d1 + d2), hs_sq(d1 - d2)
    assert sp.simplify(plus * minus - (a + b) ** 2) < 0
    return {"fixtures": rows, "old_middle_step_disproved": True}


def main() -> None:
    payload = {
        "engine": f"SymPy {sp.__version__}",
        "one_spike_and_loop_records": one_spike_records(),
        "gram_regressions": gram_regressions(),
    }
    out = ROOT / "results" / "symbolic_constructors.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    out.write_text(data, encoding="utf-8", newline="\n")
    digest = hashlib.sha256(data.encode("utf-8")).hexdigest()
    print("PASS: exact one-spike matrices, singular spectra, stability, triangles, and squares")
    print("PASS: corrected Gram certificate and exact counterexample to the discarded step")
    print(f"SHA256: {digest}")
    print(f"WROTE: {out}")


if __name__ == "__main__":
    main()
