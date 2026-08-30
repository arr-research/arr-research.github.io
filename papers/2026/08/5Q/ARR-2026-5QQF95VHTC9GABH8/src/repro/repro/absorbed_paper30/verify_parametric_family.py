"""Exact Horn certificate for a one-parameter rank-separation family.

The family is lambda(t)=(4-3t,t,t,t,-1,-1,-1,-1), 0<=t<=1.
Every Horn residual is affine on each of the two proposed primal chambers, so
endpoint verification proves feasibility on the entire closed interval.
Only the Python standard library is used.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path


N = 8
OUT = Path(__file__).resolve().parent / "results" / "parametric_family_certificate.json"


@lru_cache(None)
def horn_t(r: int, n: int):
    subsets = tuple(itertools.combinations(range(1, n + 1), r))
    triples = []
    for I in subsets:
        for J in subsets:
            for K in subsets:
                if sum(I) + sum(J) != sum(K) + r * (r + 1) // 2:
                    continue
                valid = True
                for q in range(1, r):
                    for F, G, H in horn_t(q, r):
                        lhs = sum(I[f - 1] for f in F) + sum(J[g - 1] for g in G)
                        rhs = sum(K[h - 1] for h in H) + q * (q + 1) // 2
                        if lhs > rhs:
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    triples.append((I, J, K))
    return tuple(triples)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def scale(c, x):
    return c * x[0], c * x[1]


def value(x, t):
    return x[0] + x[1] * t


LAMBDA = ((Q(4), Q(-3)),) + ((Q(0), Q(1)),) * 3 + ((Q(-1), Q(0)),) * 4
GAMMA = tuple(scale(Q(2), item) for item in LAMBDA)


def horn_row(I, J, K):
    a = [Q(0)] * 7
    for i in I:
        if i <= 7:
            a[i - 1] += 1
    for j in J:
        if j >= 2:
            a[8 - j] -= 1
    rhs = (Q(0), Q(0))
    for k in K:
        rhs = add(rhs, GAMMA[k - 1])
    return tuple(a), rhs


def constraints():
    rows = []
    for r in range(1, 8):
        for I, J, K in horn_t(r, 8):
            a, rhs = horn_row(I, J, K)
            rows.append((f"H{r}:{I}:{J}:{K}", a, rhs))
    for i in range(6):
        a = [Q(0)] * 7
        a[i], a[i + 1] = Q(1), Q(-1)
        rows.append((f"order:{i+1}", tuple(a), (Q(0), Q(0))))
    a = [Q(0)] * 7
    a[-1] = Q(1)
    rows.append(("nonnegative", tuple(a), (Q(0), Q(0))))
    return tuple(rows)


P_LOW = ((Q(8), Q(-6)), (Q(6), Q(-6)), (Q(4), Q(-4)), (Q(2), Q(0)),
         (Q(0), Q(2)), (Q(0), Q(0)), (Q(0), Q(0)))
P_HIGH = ((Q(8), Q(-6)), (Q(4), Q(-2)), (Q(2), Q(0)), (Q(2), Q(0)),
          (Q(2), Q(-2)), (Q(0), Q(0)), (Q(0), Q(0)))
P_FACE = ((Q(8), Q(-6)), (Q(6), Q(-4)), (Q(4), Q(-2)), (Q(2), Q(0)),
          (Q(0), Q(0)), (Q(0), Q(0)), (Q(0), Q(0)))


LOW_DUAL = (
    ("H1:(1,):(1,):(1,)", Q(1, 2)),
    ("H2:(1, 2):(1, 8):(1, 8)", Q(1, 2)),
    ("H6:(1, 2, 3, 5, 6, 7):(1, 2, 3, 5, 7, 8):(1, 3, 4, 6, 7, 8)", Q(1, 2)),
    ("H7:(1, 2, 3, 4, 5, 6, 7):(1, 2, 3, 4, 6, 7, 8):(1, 2, 3, 4, 6, 7, 8)", Q(1)),
    ("order:6", Q(1, 2)),
    ("nonnegative", Q(1)),
)

HIGH_DUAL = (
    ("H1:(1,):(1,):(1,)", Q(1, 2)),
    ("H4:(1, 2, 5, 6):(1, 2, 5, 8):(1, 4, 7, 8)", Q(1, 2)),
    ("H7:(1, 2, 3, 4, 5, 6, 7):(1, 2, 3, 4, 5, 7, 8):(1, 2, 3, 4, 5, 7, 8)", Q(1, 2)),
    ("H7:(1, 2, 3, 4, 5, 6, 7):(1, 2, 3, 4, 6, 7, 8):(1, 2, 3, 4, 6, 7, 8)", Q(1)),
    ("nonnegative", Q(1)),
)

FACE_DUAL = (
    ("H1:(1,):(1,):(1,)", Q(1, 2)),
    ("H3:(1, 2, 5):(1, 2, 8):(1, 4, 8)", Q(1, 2)),
    ("H5:(1, 2, 3, 5, 6):(1, 2, 3, 7, 8):(1, 3, 4, 7, 8)", Q(1, 2)),
    ("H7:(1, 2, 3, 4, 5, 6, 7):(1, 2, 3, 4, 6, 7, 8):(1, 2, 3, 4, 6, 7, 8)", Q(1, 2)),
)


def qtext(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def affine_text(x):
    return [qtext(x[0]), qtext(x[1])]


def primal_check(label, p, interval, rows):
    residuals = []
    for name, a, rhs in rows:
        lhs = (Q(0), Q(0))
        for coefficient, item in zip(a, p):
            lhs = add(lhs, scale(coefficient, item))
        residual = add(lhs, scale(Q(-1), rhs))
        endpoint_values = [value(residual, t) for t in interval]
        assert min(endpoint_values) >= 0, (label, name, endpoint_values)
        residuals.append((name, residual, endpoint_values))
    for t in interval:
        point = [value(item, t) for item in p]
        assert all(point[i] >= point[i + 1] for i in range(6))
        assert point[-1] >= 0
    stream = json.dumps(
        [[name, affine_text(residual)] for name, residual, _ in residuals],
        separators=(",", ":"),
    ).encode()
    return {
        "label": label,
        "interval": [qtext(t) for t in interval],
        "p_affine": [affine_text(item) for item in p],
        "objective_affine": affine_text(scale(Q(1, 2), tuple(map(sum, zip(*p))))),
        "minimum_endpoint_residual": qtext(min(v for _, _, values in residuals for v in values)),
        "affine_residual_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def dual_check(label, certificate, row_map, variable_count, expected):
    coefficients = [Q(0)] * 7
    rhs = (Q(0), Q(0))
    for name, weight in certificate:
        a, b = row_map[name]
        coefficients = [x + weight * y for x, y in zip(coefficients, a)]
        rhs = add(rhs, scale(weight, b))
    assert coefficients[:variable_count] == [Q(1, 2)] * variable_count, (label, coefficients)
    assert rhs == expected, (label, rhs, expected)
    return {
        "label": label,
        "weights": [[name, qtext(weight)] for name, weight in certificate],
        "combined_coefficients": [qtext(x) for x in coefficients],
        "lower_bound_affine": affine_text(rhs),
    }


def main():
    rows = constraints()
    assert [len(horn_t(r, 8)) for r in range(1, 8)] == [36, 462, 2120, 3516, 2120, 462, 36]
    assert len(rows) == 8759
    row_map = {name: (a, b) for name, a, b in rows}
    low = primal_check("unrestricted_low", P_LOW, (Q(0), Q(1, 2)), rows)
    high = primal_check("unrestricted_high", P_HIGH, (Q(1, 2), Q(1)), rows)
    face = primal_check("rank_at_most_four", P_FACE, (Q(0), Q(1)), rows)
    duals = [
        dual_check("unrestricted_low", LOW_DUAL, row_map, 7, (Q(10), Q(-7))),
        dual_check("unrestricted_high", HIGH_DUAL, row_map, 7, (Q(9), Q(-5))),
        dual_check("rank_at_most_four", FACE_DUAL, row_map, 4, (Q(10), Q(-6))),
    ]
    payload = {
        "status": "PASS",
        "family": "lambda(t)=(4-3t,t,t,t,-1,-1,-1,-1), 0<=t<=1",
        "scope": "exact one-parameter d=8 family; no dimensional-minimality claim",
        "horn_counts": [len(horn_t(r, 8)) for r in range(1, 8)],
        "constraint_count": len(rows),
        "primal_chambers": [low, high, face],
        "duals": duals,
        "unrestricted_value": {"0<=t<=1/2": "10-7t", "1/2<=t<=1": "9-5t"},
        "rank4_value": "10-6t",
        "gap": "min(t,1-t)",
        "minimum_optimal_rank": "5 for 0<t<1; 4 at t=0,1",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("PASS: exact parametric Horn certificate on both chambers")
    print("PASS: kappa=10-7t / 9-5t; rank<=4=10-6t; gap=min(t,1-t)")
    print(f"JSON_SHA256: {hashlib.sha256(text.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
