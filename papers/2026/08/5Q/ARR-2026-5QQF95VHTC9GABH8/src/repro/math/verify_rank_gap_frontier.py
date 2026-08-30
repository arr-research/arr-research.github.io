"""Canonical exact replay for the Paper 30 rank-gap frontier package.

This standard-library-only verifier regenerates the recursive Horn T-sets and
certifies, over ``fractions.Fraction``:

* the complete one-parameter dimension-eight phase; and
* a genuinely two-valued dimension-nine witness.

It proves finite Horn feasibility and the displayed sparse dual identities.
It deliberately makes no claim about dimensions at most seven, dimensional
minimality, a universal rank-excess bound, priority, or peer review.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction as Q
from functools import lru_cache


@lru_cache(None)
def horn_t(r: int, n: int):
    """Return the recursive Horn set T_r^n using one-based subsets."""

    subsets = tuple(itertools.combinations(range(1, n + 1), r))
    out = []
    for I in subsets:
        for J in subsets:
            for K in subsets:
                if sum(I) + sum(J) != sum(K) + r * (r + 1) // 2:
                    continue
                valid = True
                for q in range(1, r):
                    for F, G, H in horn_t(q, r):
                        lhs = sum(I[f - 1] for f in F)
                        lhs += sum(J[g - 1] for g in G)
                        rhs = sum(K[h - 1] for h in H)
                        rhs += q * (q + 1) // 2
                        if lhs > rhs:
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    out.append((I, J, K))
    return tuple(out)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), Q(0))


def scale(c, x):
    return tuple(c * a for a in x)


def qtext(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def horn_row(n, I, J):
    """Coefficient row after suppressing the conventional final zero p_n."""

    row = [Q(0)] * (n - 1)
    for i in I:
        if i < n:
            row[i - 1] += 1
    for j in J:
        if j > 1:
            row[n - j] -= 1
    return tuple(row)


def constraints(n, gamma0, gamma1=None):
    """Return rows ``a.p >= b0+b1*t``, including order/nonnegativity."""

    if gamma1 is None:
        gamma1 = (Q(0),) * n
    rows = []
    for r in range(1, n):
        for I, J, K in horn_t(r, n):
            rows.append(
                (
                    (r, I, J, K),
                    horn_row(n, I, J),
                    sum((gamma0[k - 1] for k in K), Q(0)),
                    sum((gamma1[k - 1] for k in K), Q(0)),
                )
            )
    for i in range(n - 2):
        row = [Q(0)] * (n - 1)
        row[i], row[i + 1] = Q(1), Q(-1)
        rows.append((("order", i + 1), tuple(row), Q(0), Q(0)))
    row = [Q(0)] * (n - 1)
    row[-1] = Q(1)
    rows.append((("nonnegative",), tuple(row), Q(0), Q(0)))
    return tuple(rows)


def affine(x0, x1, t):
    return tuple(a + t * b for a, b in zip(x0, x1))


def verify_primal(label, rows, p0, p1, endpoints, expected_cost, expected_rank):
    """Check every affine residual at endpoints, hence on the whole interval."""

    minimum = None
    active = 0
    stream = []
    for t in endpoints:
        p = affine(p0, p1, t)
        assert all(p[i] >= p[i + 1] for i in range(len(p) - 1))
        assert p[-1] >= 0
        assert sum(p, Q(0)) / 2 == expected_cost(t)
        assert sum(x > 0 for x in p) == expected_rank(t)
        for name, row, b0, b1 in rows:
            slack = dot(row, p) - b0 - t * b1
            assert slack >= 0, (label, t, name, slack)
            minimum = slack if minimum is None else min(minimum, slack)
            active += int(slack == 0)
            stream.append([qtext(t), str(name), qtext(slack)])
    return {
        "label": label,
        "endpoints": [qtext(t) for t in endpoints],
        "minimum_endpoint_slack": qtext(minimum),
        "active_endpoint_rows": active,
        "endpoint_slack_sha256": hashlib.sha256(
            json.dumps(stream, separators=(",", ":")).encode()
        ).hexdigest(),
    }


def verify_dual(label, certificate, row_map, face_rank, rhs_expected):
    """Check a nonnegative combination giving the objective on a rank face."""

    coefficient = (Q(0),) * len(next(iter(row_map.values()))[0])
    rhs0 = Q(0)
    rhs1 = Q(0)
    emitted = []
    for name, weight in certificate:
        assert weight >= 0
        assert name in row_map, name
        row, b0, b1 = row_map[name]
        coefficient = add(coefficient, scale(weight, row))
        rhs0 += weight * b0
        rhs1 += weight * b1
        emitted.append([str(name), qtext(weight)])
    assert coefficient[:face_rank] == (Q(1, 2),) * face_rank
    assert (rhs0, rhs1) == rhs_expected
    return {
        "label": label,
        "rows": emitted,
        "combined_coefficients": [qtext(x) for x in coefficient],
        "value_affine": [qtext(rhs0), qtext(rhs1)],
    }


def d8_package():
    # lambda_t=(4-3t,t,t,t,-1,-1,-1,-1), 0<=t<=1; gamma=2 lambda.
    gamma0 = (Q(8), Q(0), Q(0), Q(0), Q(-2), Q(-2), Q(-2), Q(-2))
    gamma1 = (Q(-6), Q(2), Q(2), Q(2), Q(0), Q(0), Q(0), Q(0))
    rows = constraints(8, gamma0, gamma1)
    row_map = {name: (row, b0, b1) for name, row, b0, b1 in rows}

    low0 = (Q(8), Q(6), Q(4), Q(2), Q(0), Q(0), Q(0))
    low1 = (Q(-6), Q(-6), Q(-4), Q(0), Q(2), Q(0), Q(0))
    high0 = (Q(8), Q(4), Q(2), Q(2), Q(2), Q(0), Q(0))
    high1 = (Q(-6), Q(-2), Q(0), Q(0), Q(-2), Q(0), Q(0))
    face0 = (Q(8), Q(6), Q(4), Q(2), Q(0), Q(0), Q(0))
    face1 = (Q(-6), Q(-4), Q(-2), Q(0), Q(0), Q(0), Q(0))

    H1 = (1, (1,), (1,), (1,))
    H4A = (4, (1, 2, 5, 6), (1, 2, 5, 8), (1, 4, 7, 8))
    H7P3 = (
        7,
        (1, 2, 3, 4, 5, 6, 7),
        (1, 2, 3, 4, 5, 7, 8),
        (1, 2, 3, 4, 5, 7, 8),
    )
    H7P4 = (
        7,
        (1, 2, 3, 4, 5, 6, 7),
        (1, 2, 3, 4, 6, 7, 8),
        (1, 2, 3, 4, 6, 7, 8),
    )
    low_dual = (
        (H1, Q(1, 2)),
        ((2, (1, 2), (1, 8), (1, 8)), Q(1, 4)),
        ((4, (1, 2, 3, 6), (1, 2, 7, 8), (1, 4, 7, 8)), Q(1, 4)),
        (H4A, Q(1, 4)),
        ((5, (1, 2, 3, 5, 6), (1, 2, 3, 7, 8), (1, 3, 4, 7, 8)), Q(1, 4)),
        (H7P4, Q(3, 4)),
        (("nonnegative",), Q(5, 4)),
    )
    high_dual = (
        (H1, Q(1, 2)),
        (H4A, Q(1, 2)),
        (H7P3, Q(1, 2)),
        (H7P4, Q(1)),
        (("nonnegative",), Q(1)),
    )
    face_dual = (
        (H1, Q(1, 2)),
        ((3, (1, 2, 5), (1, 2, 8), (1, 4, 8)), Q(1, 2)),
        ((5, (1, 2, 3, 5, 6), (1, 2, 3, 7, 8), (1, 3, 4, 7, 8)), Q(1, 2)),
        (H7P4, Q(1, 2)),
    )

    primal = [
        verify_primal("d8_full_low", rows, low0, low1, (Q(0), Q(1, 2)), lambda t: Q(10)-7*t, lambda t: 4 if t == 0 else 5),
        verify_primal("d8_full_high", rows, high0, high1, (Q(1, 2), Q(1)), lambda t: Q(9)-5*t, lambda t: 4 if t == 1 else 5),
        verify_primal("d8_rank4", rows, face0, face1, (Q(0), Q(1)), lambda t: Q(10)-6*t, lambda _t: 4),
    ]
    dual = [
        verify_dual("d8_full_low", low_dual, row_map, 7, (Q(10), Q(-7))),
        verify_dual("d8_full_high", high_dual, row_map, 7, (Q(9), Q(-5))),
        verify_dual("d8_rank4", face_dual, row_map, 4, (Q(10), Q(-6))),
    ]
    counts = [len(horn_t(r, 8)) for r in range(1, 8)]
    assert counts == [36, 462, 2120, 3516, 2120, 462, 36]
    assert len(rows) == 8759
    return {
        "spectrum": "(4-3t,t,t,t,-1,-1,-1,-1), 0<=t<=1",
        "horn_counts_by_size": counts,
        "horn_total": sum(counts),
        "constraint_count": len(rows),
        "primal_checks": primal,
        "dual_checks": dual,
        "full_value": ["10-7t on [0,1/2]", "9-5t on [1/2,1]"],
        "rank4_value": "10-6t",
        "gap": "min(t,1-t)",
        "minimum_optimal_rank": "5 for 0<t<1; 4 at t=0,1",
    }


def d9_package():
    # lambda=(5,5,5,5,-4,-4,-4,-4,-4); gamma=2 lambda.
    gamma = (Q(10), Q(10), Q(10), Q(10), Q(-8), Q(-8), Q(-8), Q(-8), Q(-8))
    rows = constraints(9, gamma)
    row_map = {name: (row, b0, b1) for name, row, b0, b1 in rows}
    full = (Q(16), Q(12), Q(10), Q(10), Q(8), Q(2), Q(0), Q(0))
    face = (Q(16), Q(14), Q(12), Q(10), Q(8), Q(0), Q(0), Q(0))
    zero = (Q(0),) * 8

    full_dual = (
        ((1, (3,), (1,), (3,)), Q(1, 2)),
        ((1, (4,), (1,), (4,)), Q(1)),
        ((4, (2, 3, 6, 7), (1, 2, 6, 7), (3, 4, 8, 9)), Q(1, 2)),
        ((7, (1, 2, 3, 4, 6, 7, 8), (1, 2, 3, 4, 6, 7, 8), (1, 2, 3, 4, 7, 8, 9)), Q(1, 2)),
        ((8, (1, 2, 3, 4, 5, 6, 7, 8), (1, 2, 3, 4, 6, 7, 8, 9), (1, 2, 3, 4, 6, 7, 8, 9)), Q(1, 2)),
        (("nonnegative",), Q(1)),
    )
    face_dual = (
        ((1, (4,), (1,), (4,)), Q(1, 2)),
        ((4, (3, 4, 6, 7), (1, 2, 5, 6), (3, 4, 8, 9)), Q(1, 2)),
        ((6, (2, 3, 4, 6, 7, 8), (1, 2, 3, 5, 6, 7), (2, 3, 4, 7, 8, 9)), Q(1, 2)),
        ((7, (1, 2, 3, 4, 6, 7, 8), (1, 2, 3, 4, 6, 7, 8), (1, 2, 3, 4, 7, 8, 9)), Q(1, 2)),
        ((8, (1, 2, 3, 4, 5, 6, 7, 8), (1, 2, 3, 4, 6, 7, 8, 9), (1, 2, 3, 4, 6, 7, 8, 9)), Q(3, 2)),
    )

    primal = [
        verify_primal("d9_full", rows, full, zero, (Q(0),), lambda _t: Q(29), lambda _t: 6),
        verify_primal("d9_rank5", rows, face, zero, (Q(0),), lambda _t: Q(30), lambda _t: 5),
    ]
    dual = [
        verify_dual("d9_full", full_dual, row_map, 8, (Q(29), Q(0))),
        verify_dual("d9_rank5", face_dual, row_map, 5, (Q(30), Q(0))),
    ]
    counts = [len(horn_t(r, 9)) for r in range(1, 9)]
    assert counts == [45, 792, 5317, 13704, 13704, 5317, 792, 45]
    assert len(rows) == 39724
    return {
        "spectrum": [5, 5, 5, 5, -4, -4, -4, -4, -4],
        "inertia": [4, 5, 0],
        "horn_counts_by_size": counts,
        "horn_total": sum(counts),
        "constraint_count": len(rows),
        "primal_checks": primal,
        "dual_checks": dual,
        "full_value": 29,
        "rank5_value": 30,
        "gap": 1,
        "minimum_optimal_rank": 6,
    }


def main():
    payload = {
        "status": "PASS",
        "scope": (
            "exact finite Horn certificates only; d<=7, dimensional minimality, "
            "and a universal rank-excess bound remain open"
        ),
        "d8_parametric_family": d8_package(),
        "d9_two_valued_witness": d9_package(),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
