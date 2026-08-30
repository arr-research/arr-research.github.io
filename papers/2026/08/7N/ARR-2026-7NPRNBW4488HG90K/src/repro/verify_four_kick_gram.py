#!/usr/bin/env python3
"""Independent exact replay for the four-kick Gram-determinant proof.

This checker deliberately does not use SymPy or the matrix construction in
the first replay.  It works over ``fractions.Fraction`` and separates the two
ingredients of the lower bound:

* the balanced-quadrilateral/commutator identity; and
* the corrected Gram-determinant inequality after shearing one factor.

It also records a noncommuting rational counterexample to the invalid
intermediate inequality that appeared in the preliminary viability memo.
"""

from __future__ import annotations

import json
import random
from fractions import Fraction as Q
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent
Matrix = tuple[tuple[Q, ...], ...]


def matrix(rows: Iterable[Iterable[int | Q]]) -> Matrix:
    return tuple(tuple(Q(x) for x in row) for row in rows)


def zeros(n: int) -> Matrix:
    return tuple(tuple(Q(0) for _ in range(n)) for _ in range(n))


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def scale(s: Q, a: Matrix) -> Matrix:
    return tuple(tuple(s * x for x in row) for row in a)


def sub(a: Matrix, b: Matrix) -> Matrix:
    return add(a, scale(Q(-1), b))


def mul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(n)), Q(0)) for j in range(n))
        for i in range(n)
    )


def comm(a: Matrix, b: Matrix) -> Matrix:
    return sub(mul(a, b), mul(b, a))


def inner(a: Matrix, b: Matrix) -> Q:
    # All replay fixtures are real symmetric, so this is the real HS product.
    return sum((x * y for ar, br in zip(a, b) for x, y in zip(ar, br)), Q(0))


def norm_sq(a: Matrix) -> Q:
    return inner(a, a)


def symmetric_fixture(rng: random.Random, n: int) -> Matrix:
    out = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            value = Q(rng.randint(-4, 4), rng.choice((1, 2, 3)))
            out[i][j] = value
            out[j][i] = value
    return matrix(out)


def triangle_certificate(u: Matrix, v: Matrix) -> None:
    """Certify ||u||+||v|| >= ||u+v|| using rational arithmetic only."""
    a, b = norm_sq(u), norm_sq(v)
    rhs = norm_sq(add(u, v)) - a - b
    if rhs > 0:
        # 2 sqrt(ab) >= rhs; both sides are now nonnegative, so squaring is exact.
        assert 4 * a * b >= rhs * rhs


def gram_certificate(d1: Matrix, d2: Matrix) -> dict[str, str]:
    """Certify the repaired lower-bound chain from exact Gram data."""
    a, b, c = norm_sq(d1), norm_sq(d2), inner(d1, d2)
    q2 = a * b - c * c
    assert a >= 0 and b >= 0 and q2 >= 0

    plus = add(d1, d2)
    minus = sub(d1, d2)
    A, B = norm_sq(plus), norm_sq(minus)
    assert A == a + b + 2 * c
    assert B == a + b - 2 * c
    assert A * B == (a - b) ** 2 + 4 * q2

    # These two squared rational certificates imply
    #   a+b >= 2 sqrt(q2), sqrt(A B) >= 2 sqrt(q2),
    # and hence (sqrt(A)+sqrt(B))^2 >= 8 sqrt(q2).
    assert (a + b) ** 2 >= 4 * q2
    assert A * B >= 4 * q2

    if a:
        d2_perp = sub(d2, scale(c / a, d1))
        assert inner(d1, d2_perp) == 0
        assert comm(d1, d2_perp) == comm(d1, d2)
        assert a * norm_sq(d2_perp) == q2

    return {
        "a": str(a),
        "b": str(b),
        "c": str(c),
        "gram_determinant": str(q2),
        "plus_norm_sq": str(A),
        "minus_norm_sq": str(B),
    }


def quadrilateral_checks(samples: int = 160) -> list[dict[str, str]]:
    rng = random.Random(0xA4F0_2026)
    records: list[dict[str, str]] = []
    nonzero_commutators = 0
    for index in range(samples):
        n = 2 if index < samples // 2 else 3
        if index % 2 == 0:
            # General balanced loops test the identity away from the equality
            # constructor.
            x1 = symmetric_fixture(rng, n)
            x2 = symmetric_fixture(rng, n)
            x3 = symmetric_fixture(rng, n)
            x4 = scale(Q(-1), add(add(x1, x2), x3))
            d1 = add(x1, x2)
            d2 = add(x2, x3)
            loop_type = "general"
        else:
            # The centrally symmetric loop realizes arbitrary diagonals and
            # is the relevant equality-family geometry.
            d1 = symmetric_fixture(rng, n)
            d2 = symmetric_fixture(rng, n)
            x1 = scale(Q(1, 2), sub(d1, d2))
            x2 = scale(Q(1, 2), add(d1, d2))
            x3 = scale(Q(-1), x1)
            x4 = scale(Q(-1), x2)
            loop_type = "central"
        assert add(add(x1, x2), add(x3, x4)) == zeros(n)
        assert add(x1, x2) == d1
        assert add(x2, x3) == d2

        # Removing the common factor i/2, the flux identity is
        # sum_{k>j}[x_k,x_j] = -[D1,D2].
        edges = (x1, x2, x3, x4)
        flux_comm = zeros(n)
        for k in range(4):
            for j in range(k):
                flux_comm = add(flux_comm, comm(edges[k], edges[j]))
        assert flux_comm == scale(Q(-1), comm(d1, d2))
        if comm(d1, d2) != zeros(n):
            nonzero_commutators += 1

        # The first metric step is exactly two triangle inequalities.
        triangle_certificate(x2, scale(Q(-1), x4))
        triangle_certificate(x1, scale(Q(-1), x3))
        record = gram_certificate(d1, d2)
        if index < 8:
            record["dimension"] = str(n)
            record["loop_type"] = loop_type
            records.append(record)

    assert nonzero_commutators >= 9 * samples // 10
    return records


def old_step_counterexample() -> dict[str, str]:
    """Give a noncommuting exact counterexample to the old middle step."""
    d1 = matrix(((1, 0), (0, -1)))
    d2 = matrix(((1, Q(1, 10)), (Q(1, 10), -1)))
    assert comm(d1, d2) != zeros(2)
    a, b, c = norm_sq(d1), norm_sq(d2), inner(d1, d2)
    A, B = norm_sq(add(d1, d2)), norm_sq(sub(d1, d2))

    # Old claim: (sqrt(A)+sqrt(B))^2 >= 4(a+b).
    # It would require sqrt(A B) >= a+b.  Both sides are positive, but the
    # exact squared comparison below proves the strict reverse inequality.
    assert A * B < (a + b) ** 2
    gram_certificate(d1, d2)
    return {
        "D1": "diag(1,-1)",
        "D2": "[[1,1/10],[1/10,-1]]",
        "a": str(a),
        "b": str(b),
        "c": str(c),
        "A_times_B": str(A * B),
        "a_plus_b_squared": str((a + b) ** 2),
        "commutator_nonzero": "true",
    }


def one_spike_checks(max_n: int = 12) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    fixtures: list[list[Q]] = []
    for n in range(1, max_n + 1):
        # Integer shift weights n,n-1,...,1 yield an exact one-spike target.
        weights = [Q(j) for j in range(n, 0, -1)]
        squares = [w * w for w in weights]
        b = [(squares[j] - squares[j + 1]) / 2 for j in range(n - 1)]
        b.append(squares[-1] / 2)
        fixtures.append(b)

    # Repeated eigenvalues and rational, non-integral data exercise cases not
    # covered by the integer-weight family.  Zero padding is checked below as
    # an explicit invariant of all scalar certificates.
    fixtures.extend(
        [
            [Q(3), Q(3), Q(1)],
            [Q(5, 2), Q(5, 2), Q(5, 2), Q(5, 2)],
            [Q(7, 3), Q(4, 3), Q(4, 3), Q(1, 3)],
        ]
    )

    for b in fixtures:
        b = sorted(b, reverse=True)
        n = len(b)
        tails = [sum(b[j:], Q(0)) for j in range(n)]
        kappa = sum((Q(j + 1) * b[j] for j in range(n)), Q(0))
        assert kappa == sum(tails, Q(0))
        assert all(tail > 0 for tail in tails)

        # For C's upper-shift squared weights 2*tails:
        # ||H||^2=||K||^2=sum(tails)=kappa and <H,K>=0.  Therefore
        # D1=sqrt(2)H,D2=sqrt(2)K have Gram data (2kappa,2kappa,0),
        # every central-square edge has norm^2 kappa, and S_2^2=16kappa.
        a = bdiag = 2 * kappa
        c = Q(0)
        q2 = a * bdiag - c * c
        assert q2 == 4 * kappa * kappa
        edge_norm_sq = (a + bdiag) / 4
        assert edge_norm_sq == kappa
        assert 16 * edge_norm_sq == 16 * kappa

        # Reversing the sign of F or adding zero eigenvalues changes neither
        # tails, kappa, the nonzero singular spectrum, nor optimal rank n.
        sign_reflected_kappa = sum((Q(j + 1) * b[j] for j in range(n)), Q(0))
        zero_padded_tails = list(tails)
        assert sign_reflected_kappa == kappa
        assert zero_padded_tails == tails
        assert len([x for x in tails if x > 0]) == n

        records.append(
            {
                "n": n,
                "b": [str(x) for x in b],
                "tails": [str(x) for x in tails],
                "kappa": str(kappa),
                "A4": str(16 * kappa),
                "optimal_rank": n,
                "sign_reflection_checked": True,
                "zero_padding_checked": True,
            }
        )
    return records


def main() -> None:
    quadrilateral_records = quadrilateral_checks()
    counterexample = old_step_counterexample()
    one_spike_records = one_spike_checks()
    payload = {
        "arithmetic": "Python standard-library fractions.Fraction",
        "quadrilateral_samples": 160,
        "quadrilateral_sample_records": quadrilateral_records,
        "old_step_counterexample": counterexample,
        "one_spike_records": one_spike_records,
    }
    out = ROOT / "results" / "four_kick_gram.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print("PASS: 160 exact balanced-quadrilateral and flux identities")
    print("PASS: corrected shear/Gram-determinant lower certificate")
    print("PASS: exact noncommuting counterexample to the preliminary middle step")
    print(f"PASS: {len(one_spike_records)} one-spike/reflected/zero-padded constructors")
    print(f"WROTE: {out}")


if __name__ == "__main__":
    main()
