#!/usr/bin/env python3
"""Fail-closed runner for both independent Paper 28 replays."""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPLAYS = (
    (
        ROOT / "verify_four_kick_gram.py",
        ROOT / "results" / "four_kick_gram.json",
        "7095534026866159b37de40e2055b30ca9e765401a38f3fca4809bac2bf3d9cd",
    ),
    (
        ROOT / "verify_symbolic_constructors.py",
        ROOT / "results" / "symbolic_constructors.json",
        "b455b13c193dfbe101bf53632da046ff08575d507b7c104286470f9af0c35b5a",
    ),
)


def main() -> None:
    for checker, output, expected in REPLAYS:
        subprocess.run([sys.executable, str(checker)], check=True)
        actual = hashlib.sha256(output.read_bytes()).hexdigest()
        if actual != expected:
            raise SystemExit(
                f"FAIL: frozen replay hash drift for {output.name}\n"
                f"expected: {expected}\n"
                f"actual:   {actual}"
            )
        print(f"PASS: {output.name} frozen SHA-256 {actual}")
    print("PASS: both independent exact replay routes completed.")


if __name__ == "__main__":
    main()
