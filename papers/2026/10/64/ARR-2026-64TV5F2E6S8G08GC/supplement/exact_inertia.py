# SPDX-License-Identifier: Apache-2.0
"""Exact symmetric congruence with recorded one- and two-dimensional pivots."""
import sympy as sp

def inertia(M):
    A = M.copy()
    counts = [0, 0, 0]
    blocks = []
    while A.rows:
        diag = next((i for i in range(A.rows) if A[i, i] != 0), None)
        if diag is not None:
            ix = [diag] + [i for i in range(A.rows) if i != diag]
            A = A.extract(ix, ix)
            p = A[0, 0]
            counts[0 if p > 0 else 1] += 1
            blocks.append(dict(size=1, index=diag, pivot=str(p)))
            A = A[1:, 1:] - A[1:, 0:1] * A[0:1, 1:] / p
        else:
            pair = next(((i, j) for i in range(A.rows) for j in range(i + 1, A.rows) if A[i, j]), None)
            if pair is None:
                counts[2] += A.rows
                blocks.append(dict(size=A.rows, zero_block=True))
                break
            ix = list(pair) + [i for i in range(A.rows) if i not in pair]
            A = A.extract(ix, ix)
            P = A[:2, :2]
            counts[0] += 1
            counts[1] += 1
            blocks.append(dict(size=2, indices=list(pair), matrix=[[str(v) for v in row] for row in P.tolist()]))
            A = A[2:, 2:] - A[2:, :2] * P.inv() * A[:2, 2:]
    return (counts, blocks)
