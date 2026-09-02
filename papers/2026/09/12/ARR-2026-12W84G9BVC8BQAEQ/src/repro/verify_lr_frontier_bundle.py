#!/usr/bin/env python3
"""Dependency-minimal replay of the finite LR frontier certificates.

The MILP solver is discovery-only.  This verifier reads its frozen integer row
words and checks the LR tableau axioms using only the Python standard library.
For p=4..20 it also checks identity with the exact KKT spectra.  For p=28 it
checks identity with the chamber-endpoint formula, proving only the displayed
upper bound and attaining rank.
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
TABLEAU_FILES = (
    "lr_tableau_p4.json",
    "lr_tableaux_p5_p8.json",
    "lr_tableaux_p9_p15.json",
    "lr_tableaux_p16_p20.json",
    "lr_tableau_endpoint_p28.json",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode(word: str) -> list[int]:
    return [int(value) for value in word.split()]


def verify_tableau(p: int, x: list[int], words: list[list[int]]) -> dict:
    n = 3 * p + 1
    if len(x) != n or len(words) != n or any(len(word) != p for word in words):
        raise AssertionError(f"p={p}: wrong dimensions")
    if x != sorted(x, reverse=True) or any(value < 0 for value in x):
        raise AssertionError(f"p={p}: spectrum is not a nonnegative partition")
    if any(word != sorted(word) for word in words):
        raise AssertionError(f"p={p}: row order failure")
    cells = {
        (row, x[row] + local + 1): value
        for row, word in enumerate(words)
        for local, value in enumerate(word)
    }
    for (row, column), value in cells.items():
        below = cells.get((row + 1, column))
        if below is not None and value >= below:
            raise AssertionError(f"p={p}: column failure at row={row}, column={column}")
    content = Counter(value for word in words for value in word)
    if content != Counter({symbol: n for symbol in range(1, p + 1)}):
        raise AssertionError(f"p={p}: content failure")
    prefix = Counter()
    prefix_checks = 0
    for word in words:
        for value in reversed(word):
            prefix[value] += 1
            prefix_checks += p - 1
            if any(prefix[symbol] < prefix[symbol + 1] for symbol in range(1, p)):
                raise AssertionError(f"p={p}: lattice-word failure")
    return {
        "p": p,
        "rows": n,
        "cells": n * p,
        "prefix_inequalities_checked": prefix_checks,
        "kappa_upper": sum(x),
        "attaining_rank": sum(value > 0 for value in x),
    }


def exact_spectra() -> dict[int, list[int]]:
    out = {}
    for name in ("horn_states_exact_p4_p18.json", "horn_states_exact_p19_p20.json"):
        payload = json.loads((HERE / name).read_text(encoding="utf-8"))
        if payload.get("status") != "PASS":
            raise AssertionError(f"non-PASS spectrum input {name}")
        for state in payload["states"]:
            out[int(state["p"])] = [int(value) for value in state["spectrum"]]
    return out


def endpoint_p28() -> list[int]:
    # Importing this local generator uses only the standard library.
    from endpoint_horn_candidates import candidate
    return candidate(3)["spectrum"]


def main() -> None:
    if not __debug__:
        raise SystemExit("refusing optimized Python: replay checks require __debug__")
    spectra = exact_spectra()
    expected_p = set(range(4, 21)) | {28}
    records = {}
    input_hashes = {}
    for name in TABLEAU_FILES:
        path = HERE / name
        input_hashes[name] = sha256(path)
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload.get("status") != "PASS":
            raise AssertionError(f"non-PASS tableau input {name}")
        for record in payload["records"]:
            p = int(record["p"])
            if p in records:
                raise AssertionError(f"duplicate p={p}")
            x = [int(value) for value in record["spectrum"]]
            if p <= 20:
                if x != spectra[p]:
                    raise AssertionError(f"p={p}: tableau spectrum differs from exact KKT state")
                claim = "exact optimum and minimum rank inherited from rational KKT certificates"
            elif p == 28:
                if x != endpoint_p28():
                    raise AssertionError("p=28 tableau spectrum differs from endpoint formula")
                claim = "exact LR upper bound only; lower bound and minimum rank remain open"
            else:
                raise AssertionError(f"unexpected p={p}")
            audit = verify_tableau(p, x, [decode(word) for word in record["row_words"]])
            audit["claim"] = claim
            records[p] = audit
    if set(records) != expected_p:
        raise AssertionError(f"wrong p coverage: {sorted(records)}")
    output = {
        "status": "PASS",
        "scope": "standard-library replay of 18 explicit integral LR tableaux",
        "input_sha256": input_hashes,
        "records": [records[p] for p in sorted(records)],
        "total_tableaux": len(records),
        "total_cells": sum(record["cells"] for record in records.values()),
        "p28_conclusion": "kappa(F_(28,57)) <= 2546, attained by rank 61",
        "p28_not_proved": "equality, optimality, and minimum attaining rank",
    }
    destination = HERE / "lr_frontier_bundle_audit.json"
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(
        f"PASS tableaux={output['total_tableaux']} cells={output['total_cells']} "
        "p28=EXACT_UPPER_BOUND_ONLY"
    )
    print(f"WROTE {destination.resolve()}")


if __name__ == "__main__":
    main()
