"""Bounded replay for the oriented two-plane / Plucker RDF derivation.

This script checks exact coefficient identities symbolically and performs a
small deterministic Monte Carlo normalization smoke test.  It is diagnostic,
not a substitute for the analytic proof.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp


def exact_checks(max_n: int = 20) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for n in range(3, max_n + 1):
        a = sp.Rational(n - 1, 2)
        b = sp.Rational(n, 2)
        ex2 = sp.simplify(sp.Rational(1, 2) / (a * b))
        ex4 = sp.simplify(sp.Rational(3, 2) / (a * (a + 1) * b * (b + 1)))
        expected2 = sp.Rational(2, n * (n - 1))
        expected4 = sp.Rational(24, n * (n - 1) * (n + 1) * (n + 2))
        cumulant4 = sp.factor(ex4 - 3 * ex2**2)
        expected_c4 = sp.Rational(12 * (n * n - 5 * n - 2), n**2 * (n - 1) ** 2 * (n + 1) * (n + 2))
        assert sp.simplify(ex2 - expected2) == 0
        assert sp.simplify(ex4 - expected4) == 0
        assert sp.simplify(cumulant4 - expected_c4) == 0
        duplication = sp.simplify(
            sp.Rational(2) ** (n - 3)
            / sp.sqrt(sp.pi)
            * sp.gamma(sp.Rational(n, 2))
            * sp.gamma(sp.Rational(n - 1, 2))
        )
        assert sp.simplify(duplication - sp.gamma(n - 1) / 2) == 0
        rows.append(
            {
                "n": n,
                "E_X2": str(expected2),
                "E_X4": str(expected4),
                "cumulant4": str(expected_c4),
                "cumulant4_sign": int(sp.sign(expected_c4)),
                "laplace_constant": str(sp.gamma(n - 1) / 2),
            }
        )
    return rows


def haar_oriented_plane(rng: np.random.Generator, n: int) -> np.ndarray:
    frame = rng.normal(size=(n, 2))
    q, r = np.linalg.qr(frame, mode="reduced")
    # Fix the QR column signs deterministically without changing Haar law.
    signs = np.sign(np.diag(r))
    signs[signs == 0] = 1
    return q * signs


def simple_overlap(frame: np.ndarray) -> float:
    return float(np.linalg.det(frame[:2, :]))


def series_L(n: int, t: float, terms: int = 120) -> float:
    a = (n - 1) / 2
    b = n / 2
    total = 1.0
    term = 1.0
    z = t * t / 4
    for k in range(1, terms):
        term *= z / ((a + k - 1) * (b + k - 1))
        total += term
        if abs(term) < 1e-16 * abs(total):
            break
    return total


def monte_carlo_checks(samples: int = 120_000) -> list[dict[str, float]]:
    rng = np.random.default_rng(20260813)
    rows: list[dict[str, float]] = []
    for n, t in [(3, 1.1), (4, 1.3), (6, 0.9), (8, 0.7)]:
        xs = np.empty(samples)
        for j in range(samples):
            xs[j] = simple_overlap(haar_oriented_plane(rng, n))
        empirical = float(np.mean(np.exp(t * xs)))
        exact = series_L(n, t)
        stderr = float(np.std(np.exp(t * xs), ddof=1) / math.sqrt(samples))
        zscore = abs(empirical - exact) / stderr
        assert zscore < 6.0
        rows.append(
            {
                "n": float(n),
                "t": t,
                "empirical_L": empirical,
                "series_L": exact,
                "standard_error": stderr,
                "absolute_zscore": zscore,
                "empirical_E_X2": float(np.mean(xs * xs)),
                "exact_E_X2": 2 / (n * (n - 1)),
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("oriented_plucker_rdf_verification.json"))
    parser.add_argument("--samples", type=int, default=120_000)
    args = parser.parse_args()
    if args.samples > 200_000:
        raise SystemExit("bounded replay cap: --samples must be <= 200000")
    result = {
        "scope": "symbolic coefficient checks and bounded Monte Carlo smoke test; not a proof",
        "exact_checks": exact_checks(),
        "monte_carlo": monte_carlo_checks(args.samples),
    }
    args.output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"PASS: wrote {args.output}")


if __name__ == "__main__":
    main()
