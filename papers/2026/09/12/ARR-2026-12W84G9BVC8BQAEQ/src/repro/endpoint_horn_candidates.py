#!/usr/bin/env python3
"""Generate the conjectural spectra at Horn-dynamics chamber endpoints.

The construction is exact as an integer partition.  Feasibility is proved by
LR and hive certificates for m=0,1,2,3 (p=4,8,15,28).  At m=4 (p=53) the
specific spectrum is exactly infeasible by an integral Farkas certificate.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def endpoint(m: int) -> int:
    if m < 0:
        raise ValueError("m must be nonnegative")
    return 3 * (2 ** m) + m + 1


def expand(values: list[int], multiplicities: list[int]) -> list[int]:
    if len(values) != len(multiplicities) or any(m <= 0 for m in multiplicities):
        raise AssertionError("invalid run data")
    return [value for value, multiplicity in zip(values, multiplicities) for _ in range(multiplicity)]


def partition_a(m: int) -> list[int]:
    endpoints = [endpoint(j) for j in range(m + 1)]
    values = [endpoints[m], *reversed(endpoints[:m]), 2, 1]
    multiplicities = [1, 1, endpoints[0] - 2]
    multiplicities.extend(endpoints[j] - endpoints[j - 1] for j in range(1, m + 1))
    out = expand(values, multiplicities)
    if len(out) != endpoint(m) or out != sorted(out, reverse=True):
        raise AssertionError("A_m is not a partition of the required length")
    # Directly check self-conjugacy.
    conjugate = [sum(value >= column for value in out) for column in range(1, out[0] + 1)]
    if conjugate != out:
        raise AssertionError("A_m is not self-conjugate")
    return out


def partition_b(m: int) -> list[int]:
    if m == 0:
        return [1]
    values = [2 ** power for power in range(m, -1, -1)]
    multiplicities = [1 if index == 0 else 2 if index == 1 else 3 * 2 ** (index - 2)
                      for index in range(m + 1)]
    return expand(values, multiplicities)


def partition_c(m: int) -> list[int]:
    if m == 0:
        return []
    values = [2 ** power for power in range(m - 1, -1, -1)]
    multiplicities = [1 if index == 0 else 2 ** (index - 1) for index in range(m)]
    return expand(values, multiplicities)


def candidate(m: int) -> dict:
    p = endpoint(m)
    q = 2 * p + 1
    a = partition_a(m)
    b_nonzero = partition_b(m)
    c = partition_c(m)
    if len(b_nonzero) > p or len(c) > p:
        raise AssertionError("endpoint blocks exceed p")
    b = [*b_nonzero, *([0] * (p - len(b_nonzero)))]
    spectrum = [*(2 * p + value for value in a), 2 * p,
                *(p + value for value in b), *c, *([0] * (p - len(c)))]
    if len(spectrum) != 3 * p + 1 or spectrum != sorted(spectrum, reverse=True):
        raise AssertionError("candidate spectrum has the wrong dimension or order")
    kappa = sum(spectrum)
    predicted_kappa = 3 * p * p + 2 * p + sum(a) + sum(b) + sum(c)
    if kappa != predicted_kappa:
        raise AssertionError("block mass identity failed")
    rank = sum(value > 0 for value in spectrum)
    if rank != q + len(c):
        raise AssertionError("rank identity failed")
    return {
        "m": m,
        "p": p,
        "q": q,
        "n": 3 * p + 1,
        "A": a,
        "B": b,
        "C": c,
        "spectrum": spectrum,
        "kappa": kappa,
        "attaining_rank_if_feasible": rank,
        "rank_excess_if_feasible": len(c),
        "feasibility_status": (
            "EXACT_LR_AND_HIVE_KNOWN" if m <= 3 else
            "EXACT_HIVE_INFEASIBLE" if m == 4 else
            "CANDIDATE_UNTESTED"
        ),
    }


def load_exact_states() -> dict[int, dict]:
    out = {}
    for name in ("horn_states_exact_p4_p18.json", "horn_states_exact_p19_p20.json"):
        payload = json.loads((HERE / name).read_text(encoding="utf-8"))
        for state in payload["states"]:
            out[int(state["p"])] = state
    return out


def main() -> None:
    if not __debug__:
        raise SystemExit("refusing optimized Python: audit checks require __debug__")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, default=4)
    parser.add_argument("--output", type=Path, default=HERE / "endpoint_horn_candidates.json")
    args = parser.parse_args()
    if args.max_m < 0:
        parser.error("max-m must be nonnegative")
    exact = load_exact_states()
    records = [candidate(m) for m in range(args.max_m + 1)]
    for record in records:
        p = record["p"]
        if p in exact and exact[p]["spectrum"] != record["spectrum"]:
            raise AssertionError(f"endpoint formula disagrees with exact p={p}")

    # Frozen numerical p=28 spectrum from the pre-formula holdout.
    p28_runs = [(84, 1), (71, 1), (64, 2), (60, 4), (58, 7), (57, 13),
                (56, 1), (36, 1), (32, 2), (30, 3), (29, 6), (28, 16),
                (4, 1), (2, 1), (1, 2), (0, 24)]
    frozen_p28 = expand([value for value, _ in p28_runs], [count for _, count in p28_runs])
    if records[3]["spectrum"] != frozen_p28:
        raise AssertionError("endpoint formula does not reproduce the frozen p=28 spectrum")

    payload = {
        "status": "PASS",
        "claim_status": (
            "EXACT_PARTITION_FORMULA; FEASIBLE_THROUGH_M3; "
            "EXACTLY_INFEASIBLE_AT_M4"
        ),
        "records": records,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    for record in records:
        print(
            f"PASS m={record['m']} p={record['p']} kappa={record['kappa']} "
            f"rank={record['attaining_rank_if_feasible']} {record['feasibility_status']}"
        )
    print(f"WROTE {args.output.resolve()}")


if __name__ == "__main__":
    main()
