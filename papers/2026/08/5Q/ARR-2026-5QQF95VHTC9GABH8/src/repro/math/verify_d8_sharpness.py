"""Dependency-free exact certificate for the dimension-eight sharpness witness."""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction as Q
from functools import lru_cache


@lru_cache(None)
def horn_t(r: int, n: int):
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
                        lhs = sum(I[f - 1] for f in F) + sum(J[g - 1] for g in G)
                        rhs = sum(K[h - 1] for h in H) + q * (q + 1) // 2
                        if lhs > rhs:
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    out.append((I, J, K))
    return tuple(out)


def horn_row(n, I, J):
    row = [Q(0)] * (n - 1)
    for i in I:
        if i < n:
            row[i - 1] += 1
    for j in J:
        if j > 1:
            row[n - j] -= 1
    return tuple(row)


def rows(n, gamma):
    out = []
    for r in range(1, n):
        for I, J, K in horn_t(r, n):
            out.append(((r, I, J, K), horn_row(n, I, J), sum(gamma[k - 1] for k in K)))
    for i in range(n - 2):
        row = [Q(0)] * (n - 1)
        row[i], row[i + 1] = 1, -1
        out.append((("order", i + 1), tuple(row), Q(0)))
    row = [Q(0)] * (n - 1)
    row[-1] = 1
    out.append((("nonnegative",), tuple(row), Q(0)))
    return tuple(out)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Q(0))


def verify_primal(label, all_rows, p, cost, rank):
    assert all(p[i] >= p[i + 1] for i in range(len(p) - 1)) and p[-1] >= 0
    assert sum(p, Q(0)) / 2 == cost
    assert sum(x > 0 for x in p) == rank
    slacks = []
    for name, row, rhs in all_rows:
        slack = dot(row, p) - rhs
        assert slack >= 0, (label, name, slack)
        slacks.append((str(name), str(slack)))
    return {
        "label": label,
        "cost": str(cost),
        "rank": rank,
        "minimum_slack": str(min(Q(x) for _, x in slacks)),
        "slack_sha256": hashlib.sha256(json.dumps(slacks, separators=(",", ":")).encode()).hexdigest(),
    }


def verify_dual(label, all_rows, certificate, face_rank, value):
    row_map = {name: (row, rhs) for name, row, rhs in all_rows}
    coefficient = [Q(0)] * 7
    rhs = Q(0)
    for name, weight in certificate:
        assert weight >= 0 and name in row_map
        row, bound = row_map[name]
        for i, entry in enumerate(row):
            coefficient[i] += weight * entry
        rhs += weight * bound
    assert tuple(coefficient[:face_rank]) == (Q(1, 2),) * face_rank
    assert rhs == value
    return {
        "label": label,
        "combined_coefficients": [str(x) for x in coefficient],
        "right_side": str(rhs),
        "rows": [[str(name), str(weight)] for name, weight in certificate],
    }


def main():
    # F has spectrum (5,1,1,1,-2,-2,-2,-2); gamma=2 lambda.
    gamma = (Q(10), Q(2), Q(2), Q(2), Q(-4), Q(-4), Q(-4), Q(-4))
    all_rows = rows(8, gamma)
    H1 = (1, (1,), (1,), (1,))
    H4 = (4, (1, 2, 5, 6), (1, 2, 5, 8), (1, 4, 7, 8))
    H7A = (
        7,
        (1, 2, 3, 4, 5, 6, 7),
        (1, 2, 3, 4, 5, 7, 8),
        (1, 2, 3, 4, 5, 7, 8),
    )
    H7B = (
        7,
        (1, 2, 3, 4, 5, 6, 7),
        (1, 2, 3, 4, 6, 7, 8),
        (1, 2, 3, 4, 6, 7, 8),
    )
    full_dual = (
        (H1, Q(1, 2)),
        (H4, Q(1, 2)),
        (H7A, Q(1, 2)),
        (H7B, Q(1)),
        (("nonnegative",), Q(1)),
    )
    face_dual = (
        (H1, Q(1, 2)),
        ((3, (1, 2, 5), (1, 2, 8), (1, 4, 8)), Q(1, 2)),
        ((5, (1, 2, 3, 5, 6), (1, 2, 3, 7, 8), (1, 3, 4, 7, 8)), Q(1, 2)),
        (H7B, Q(1, 2)),
    )
    counts = [len(horn_t(r, 8)) for r in range(1, 8)]
    assert counts == [36, 462, 2120, 3516, 2120, 462, 36]
    payload = {
        "status": "PASS",
        "spectrum": [5, 1, 1, 1, -2, -2, -2, -2],
        "inertia_rank": 4,
        "horn_counts_by_size": counts,
        "horn_rows": sum(counts),
        "all_constraints": len(all_rows),
        "primals": [
            verify_primal("unrestricted", all_rows, (Q(10), Q(6), Q(4), Q(4), Q(2), Q(0), Q(0)), Q(13), 5),
            verify_primal("rank_at_most_four", all_rows, (Q(10), Q(8), Q(6), Q(4), Q(0), Q(0), Q(0)), Q(14), 4),
        ],
        "duals": [
            verify_dual("unrestricted", all_rows, full_dual, 7, Q(13)),
            verify_dual("rank_at_most_four", all_rows, face_dual, 4, Q(14)),
        ],
        "conclusion": "minimum optimal rank 5; rank-four penalty 1",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
