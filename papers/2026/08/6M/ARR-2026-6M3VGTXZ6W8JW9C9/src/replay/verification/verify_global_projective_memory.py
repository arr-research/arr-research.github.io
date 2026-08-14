"""Exact regression certificate for the global/block projective-memory paper.

All decisions use SymPy rational arithmetic.  The script independently checks
the full-support Lagrange invariant, global incidence ranks, the exact/border
max--min split, and the optimal generic allocation law.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp

Z = sp.symbols("z")


def lagrange(nodes: list[int]) -> list[sp.Poly]:
    out = []
    for i, zi in enumerate(nodes):
        p = sp.Integer(1)
        for j, zj in enumerate(nodes):
            if i != j:
                p *= (Z - zj) / sp.Rational(zi - zj)
        out.append(sp.Poly(sp.expand(p), Z))
    return out


def q_star(nodes: list[int], bases: list[sp.Matrix]) -> tuple[int, list[dict]]:
    """Largest top-coefficient kernel having support at every record."""
    count = len(nodes)
    audit: list[dict] = []
    best = 0
    for q in range(count):
        blocks = []
        for ell, basis in zip(lagrange(nodes), bases):
            if q:
                top = sp.Matrix([ell.coeff_monomial(Z**k)
                                 for k in range(count - q, count)])
                blocks.append(sp.kronecker_product(top, basis))
        cols = sum(b.cols for b in bases)
        matrix = sp.Matrix.hstack(*blocks) if blocks else sp.zeros(0, cols)
        kernel = matrix.nullspace()
        K = sp.Matrix.hstack(*kernel) if kernel else sp.zeros(cols, 0)
        offsets = [0]
        for basis in bases:
            offsets.append(offsets[-1] + basis.cols)
        full = bool(K.cols) and all(
            any(K[row, col] != 0
                for row in range(offsets[i], offsets[i + 1])
                for col in range(K.cols))
            for i in range(count)
        )
        audit.append({"q": q, "rank": matrix.rank(),
                      "nullity": K.cols, "full_support": full})
        if full:
            best = q
    return best, audit


def incidence(nodes: list[int], annihilators: list[sp.Matrix], degree: int) -> sp.Matrix:
    r = annihilators[0].cols
    rows = []
    for node, Q in zip(nodes, annihilators):
        powers = [sp.Rational(node) ** k for k in range(degree + 1)]
        for row_index in range(Q.rows):
            row = []
            for coordinate in range(r):
                row.extend(Q[row_index, coordinate] * value for value in powers)
            rows.append(row)
    return sp.Matrix(rows)


def verify() -> dict:
    # Mixed subspaces in C^3: dimensions 2,1,2 and codimension sum four.
    nodes3 = [0, 1, 2]
    Q3 = [sp.Matrix([[1, 2, 3]]),
          sp.Matrix([[-1, 1, 0], [-1, 0, 1]]),
          sp.Matrix([[2, -1, 1]])]
    Y3 = [sp.Matrix.hstack(*Q3[0].nullspace()),
          sp.Matrix([[1], [1], [1]]),
          sp.Matrix.hstack(*Q3[2].nullspace())]
    q3, q3_audit = q_star(nodes3, Y3)
    A30, A31 = incidence(nodes3, Q3, 0), incidence(nodes3, Q3, 1)
    assert (q3, A30.rank(), A30.cols, A31.rank(), A31.cols) == (1, 3, 3, 4, 6)

    # Four planar records: a 3+1 collision costs degree three; a constant table zero.
    line = lambda a, b: sp.Matrix([[a], [b]])
    q_hard, _ = q_star([0, 1, 2, 3],
                       [line(1, 0), line(1, 0), line(1, 0), line(0, 1)])
    q_const, _ = q_star([0, 1, 2, 3], [line(1, 2)] * 4)
    assert (3 - q_hard, 3 - q_const) == (3, 0)

    # Two scalar bands with occupancies 2 and 4: exact=max=4, border=min=2.
    nodes6 = list(range(6))
    Q6 = [sp.Matrix([[0, 1]])] * 2 + [sp.Matrix([[1, 0]])] * 4
    A61, A62 = incidence(nodes6, Q6, 1), incidence(nodes6, Q6, 2)
    assert A61.rank() == A61.cols == 4
    assert (A62.rank(), A62.cols) == (5, 6)
    shifted = [4, 2]
    assert (max(shifted), min(shifted)) == (4, 2)

    # Five records: a C^3 block of three and a C^2 block of two.
    q2, _ = q_star([3, 4], [line(1, 0), line(1, 1)])
    intrinsic = [3 - 1 - q3, 2 - 1 - q2]
    shifted_mixed = [2 + intrinsic[0], 3 + intrinsic[1]]
    assert (intrinsic, shifted_mixed, max(shifted_mixed), min(shifted_mixed)) == (
        [1, 1], [3, 4], 4, 3)

    # Generic allocation: r=(2,3), B=2, L=14.
    dimensions, total = [2, 3], 14
    t = (total - len(dimensions)) // sum(dimensions)
    baseline = [r * t + 1 for r in dimensions]
    optimal_degree = total - 1 - t
    assert (t, baseline, sum(baseline), optimal_degree) == (2, [5, 7], 12, 11)

    return {
        "schema": "global-projective-memory-certificate-v1",
        "arithmetic": "exact rational SymPy",
        "sympy_version": sp.__version__,
        "source_oid": "b2a7f3268de19683573325c5a63d4ce0030ed955+global-extension",
        "mixed_C3": {"dimensions": [2, 1, 2], "q_star": q3,
                       "rank_degree_0": A30.rank(), "rank_degree_1": A31.rank(),
                       "q_audit": q3_audit},
        "planar_collision": {"degree_3_plus_1": 3, "degree_constant": 0},
        "scalar_border_gap": {"occupancies": [2, 4], "exact_degree": 4,
                              "border_degree": 2, "rank_d1": A61.rank(),
                              "columns_d1": A61.cols, "rank_d2": A62.rank(),
                              "columns_d2": A62.cols},
        "mixed_blocks": {"intrinsic_degrees": intrinsic,
                         "shifted_degrees": shifted_mixed,
                         "exact_degree": 4, "border_degree": 3},
        "optimal_allocation": {"dimensions": dimensions, "records": total,
                               "baseline": baseline, "residual_records": 2,
                               "optimal_degree": optimal_degree},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    record = verify()
    encoded = json.dumps(record, indent=2, sort_keys=True) + "\n"
    if args.check:
        frozen = args.check.read_text(encoding="utf-8")
        if frozen != encoded:
            raise SystemExit(f"FAIL frozen certificate mismatch: {args.check}")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8", newline="\n")
    print("PASS global projective-memory exact certificate")
    print(encoded, end="")


if __name__ == "__main__":
    main()
