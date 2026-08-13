#!/usr/bin/env python3
"""Optional byte-array diagnostic for fixed-environment replays.

This is deliberately not the release gate: a different BLAS may propose a
different congruence basis while Arb still certifies the same public floor.
Use ``verify_release.py`` for the theorem-level check.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def compare_npz(reference: Path, replay: Path) -> None:
    with np.load(reference, allow_pickle=False) as left, np.load(
        replay, allow_pickle=False
    ) as right:
        if left.files != right.files:
            raise SystemExit(f"key mismatch: {reference.name} vs {replay.name}")
        for key in left.files:
            a = left[key]
            b = right[key]
            if a.dtype != b.dtype or a.shape != b.shape or not np.array_equal(a, b):
                raise SystemExit(f"array mismatch in {key}")


def compare_json(reference: Path, replay: Path) -> None:
    if json.loads(reference.read_text(encoding="utf-8")) != json.loads(
        replay.read_text(encoding="utf-8")
    ):
        raise SystemExit(f"JSON mismatch: {reference.name} vs {replay.name}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("reference", type=Path)
    parser.add_argument("replay", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.json:
        compare_json(args.reference, args.replay)
    else:
        compare_npz(args.reference, args.replay)
    print(f"PASS: exact array/value equality for {args.replay.name}")


if __name__ == "__main__":
    main()
