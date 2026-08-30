#!/usr/bin/env python3
"""Dependency-free exact replay for the rank-adaptive trace-tax theorem."""

from __future__ import annotations

import argparse
import itertools
import json
import os
from fractions import Fraction as Q
from pathlib import Path
from tempfile import NamedTemporaryFile

ROOT = Path(__file__).resolve().parent


def check(condition, message):
    """Raise on a failed verification without relying on assert."""
    if not condition:
        raise RuntimeError(message)


def shift_commutator(mu):
    d = len(mu)
    partial = [sum(mu[:k]) for k in range(1, d)]
    diag = [partial[0]]
    diag.extend(partial[k] - partial[k - 1] for k in range(1, d - 1))
    diag.append(-partial[-1])
    return partial, diag


def symbolic_shift_check(size=8):
    """Check the generic identity in a free rational coefficient module."""
    basis = []
    for index in range(size - 1):
        vector = [Q(0)] * (size - 1)
        vector[index] = Q(1)
        basis.append(tuple(vector))
    last = tuple(Q(-1) for _ in range(size - 1))
    mu = basis + [last]

    partial = []
    running = [Q(0)] * (size - 1)
    for vector in mu[:-1]:
        running = [a + b for a, b in zip(running, vector)]
        partial.append(tuple(running))
    diag = [partial[0]]
    diag.extend(
        tuple(a - b for a, b in zip(partial[k], partial[k - 1]))
        for k in range(1, size - 1)
    )
    diag.append(tuple(-a for a in partial[-1]))
    check(diag == mu, "free-module weighted-shift identity failed")


def write_json_atomic(path, payload):
    path = path.resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(
        mode="w", encoding="utf-8", newline="\n", delete=False, dir=path.parent
    ) as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
        temporary = Path(handle.name)
    os.replace(temporary, path)


def exact_checks(max_d=12, output=None):
    check(max_d >= 2, "--max-d must be at least 2")
    records = []
    for d in range(2, max_d + 1):
        # Zero-padded one-spike upper and Horn lower certificates at every rank.
        P = Q(1)
        rank_records = []
        for rank in range(2, d + 1):
            mu = [P] + [Q(0)] * (d - rank) + [-P / Q(rank - 1)] * (rank - 1)
            nonzero_order = [P] + [-P / Q(rank - 1)] * (rank - 1) + [Q(0)] * (d - rank)
            partial, diag = shift_commutator(nonzero_order)
            check(diag == nonzero_order, f"shift diagonal failed at d={d}, rank={rank}")
            shift_cost = sum(partial)
            horn_bounds = [2 * P * Q(rank - ell, rank - 1) for ell in range(1, rank)]
            check(
                sum(horn_bounds) / 2 == Q(rank, 2) * P == shift_cost,
                f"Horn/shift endpoint mismatch at d={d}, rank={rank}",
            )
            rank_records.append(
                {
                    "rank": rank,
                    "spectrum": [str(x) for x in mu],
                    "spike_cost": str(shift_cost),
                    "horn_sum_cost": str(sum(horn_bounds) / 2),
                }
            )

        # Every flat two-sign block with both multiplicities >=2 admits the
        # strict adjacent-swap improvement used in the equality proof.
        swaps = []
        for m in range(2, d - 1):
            n = d - m
            if n < 2:
                continue
            middle = P * (1 - Q(1, m) - Q(1, n))
            deficit = P * (Q(1, m) + Q(1, n))
            check(middle >= 0 and deficit > 0, f"flat-swap check failed at d={d}, m={m}")
            swaps.append({"m": m, "n": n, "middle": str(middle), "deficit": str(deficit)})
        records.append({"d": d, "rank_adaptive_spikes": rank_records, "flat_swap_checks": swaps})

    symbolic_shift_check(size=8)

    # Exact average block-order identity on deterministic rational examples.
    examples = []
    for m, n in ((1, 4), (2, 3), (3, 2), (4, 1), (2, 5), (3, 4)):
        positives = [Q(2 * i, m * (m + 1)) for i in range(1, m + 1)]
        negatives = [Q(2 * j, n * (n + 1)) for j in range(1, n + 1)]
        check(sum(positives) == sum(negatives) == 1, f"normalization failed for {(m, n)}")
        costs = []
        for ap in itertools.permutations(positives):
            for bp in itertools.permutations(negatives):
                seq = list(ap) + [-b for b in bp]
                partial, _ = shift_commutator(seq)
                check(min(partial) >= 0, f"negative block partial sum for {(m, n)}")
                costs.append(sum(partial))
        check(sum(costs) / len(costs) == Q(m + n, 2), f"average failed for {(m, n)}")
        examples.append({"m": m, "n": n, "orders": len(costs), "average": str(sum(costs) / len(costs))})

    payload = {
        "schema": "dimension-sharp-selfcommutator-tax-v2",
        "max_dimension_checked": max_d,
        "free_module_shift_size": 8,
        "dimensions": records,
        "average_examples": examples,
    }
    out = Path(output) if output else ROOT / "verification.json"
    write_json_atomic(out, payload)
    print(f"PASS: exact zero-padded one-spike upper/lower match for every rank in d=2..{max_d}")
    print("PASS: all flat two-sign adjacent-swap checks")
    print("PASS: free-module weighted-shift identity and exact block-order averages")
    print(f"WROTE: {out.resolve()}")


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("optimized Python (-O) is unsupported: verification must retain checks")
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=12)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    exact_checks(args.max_d, args.output)
