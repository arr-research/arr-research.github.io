"""Lightweight diagnostics for the Grassmann matrix-Bingham spectral switch.

This script is not a proof.  It independently checks the exact second/third
moment coefficients, the weak- and strong-field candidate spectra, and small
Monte Carlo instances using bounded memory and runtime.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


BASE_DIR = Path(__file__).resolve().parent
import sympy as sp


def schur_dimension(partition: tuple[int, ...], n: int) -> sp.Rational:
    """Evaluate s_lambda(1^n) by the hook-content formula."""
    numerator = sp.Integer(1)
    denominator = sp.Integer(1)
    for i, row in enumerate(partition):
        for j in range(row):
            numerator *= n + j - i
            below = sum(1 for lower_row in partition[i + 1 :] if lower_row > j)
            denominator *= row - j + below
    return sp.factor(numerator / denominator)


def schur_moment_coefficients(d: int, r: int) -> dict[str, sp.Rational]:
    """Derive degree 2--4 trace-invariant coefficients from S_m characters."""
    # Entries are (partition, f^lambda, character on the named cycle class).
    degree2 = [((2,), 1, 1), ((1, 1), 1, -1)]
    degree3 = [((3,), 1, 1), ((2, 1), 2, -1), ((1, 1, 1), 1, 1)]
    degree4 = [
        ((4,), 1, 1, 1),
        ((3, 1), 3, -1, -1),
        ((2, 2), 2, 2, 0),
        ((2, 1, 1), 3, -1, 1),
        ((1, 1, 1, 1), 1, 1, -1),
    ]

    def ratio(partition: tuple[int, ...]) -> sp.Rational:
        return schur_dimension(partition, r) / schur_dimension(partition, d)

    c2 = sum(sp.Rational(f * chi, 2) * ratio(part) for part, f, chi in degree2)
    c3 = sum(sp.Rational(f * chi, 3) * ratio(part) for part, f, chi in degree3)
    out = {"c2_schur": sp.factor(c2), "c3_schur": sp.factor(c3)}
    if d >= 4:
        c22 = sum(sp.Rational(f * chi22, 8) * ratio(part) for part, f, chi22, _ in degree4)
        c4 = sum(sp.Rational(f * chi4, 4) * ratio(part) for part, f, _, chi4 in degree4)
        out.update({"c22_schur": sp.factor(c22), "c4_schur": sp.factor(c4)})
    return out


def exact_coefficients(d: int, r: int) -> dict[str, sp.Rational]:
    d0, r0 = map(sp.Integer, (d, r))
    c2 = r0 * (d0 - r0) / (d0 * (d0**2 - 1))
    c3 = (
        2
        * r0
        * (d0 - r0)
        * (d0 - 2 * r0)
        / (d0 * (d0**2 - 1) * (d0**2 - 4))
    )
    out = {"c2": sp.factor(c2), "c3": sp.factor(c3)}
    if d >= 4:
        # E Y^4 = c22 (tr A^2)^2 + c4 tr A^4 for tr A = 0.
        c22 = (
            3
            * r0
            * (r0 - d0)
            * (-d0**3 * r0 + d0**2 * r0**2 + 4 * d0**2 - 6 * d0 * r0 + 6 * r0**2 - 6)
            / (d0**2 * (d0 - 3) * (d0 - 2) * (d0 - 1) * (d0 + 1) * (d0 + 2) * (d0 + 3))
        )
        c4 = (
            -6
            * r0
            * (r0 - d0)
            * (d0**2 - 5 * d0 * r0 + 5 * r0**2 + 1)
            / (d0 * (d0 - 3) * (d0 - 2) * (d0 - 1) * (d0 + 1) * (d0 + 2) * (d0 + 3))
        )
        out.update({"c22": sp.factor(c22), "c4": sp.factor(c4)})
    return out


def one_spike(d: int) -> np.ndarray:
    a = np.empty(d)
    a[0] = np.sqrt((d - 1) / d)
    a[1:] = -1 / np.sqrt(d * (d - 1))
    return a


def r_block(d: int, r: int) -> np.ndarray:
    a = np.empty(d)
    a[:r] = np.sqrt((d - r) / (r * d))
    a[r:] = -np.sqrt(r / (d * (d - r)))
    return a


def haar_projector_diagonals(
    rng: np.random.Generator, d: int, r: int, samples: int
) -> np.ndarray:
    out = np.empty((samples, d), dtype=np.float64)
    for k in range(samples):
        g = rng.normal(size=(d, r)) + 1j * rng.normal(size=(d, r))
        q, _ = np.linalg.qr(g, mode="reduced")
        out[k] = np.sum(np.abs(q) ** 2, axis=1)
    return out


def logmeanexp(values: np.ndarray) -> float:
    m = float(np.max(values))
    return m + float(np.log(np.mean(np.exp(values - m))))


def controlled_log_mgf(y: np.ndarray, t: float, exact_variance: float) -> float:
    """Apply exact mean/variance control variates to a common-sample log MGF.

    This is only a diagnostic.  It removes the Monte Carlo O(t) and O(t^2)
    anisotropy that otherwise masks the genuine O(t^3) weak-field split.
    """
    raw = logmeanexp(t * y)
    return raw - t * float(np.mean(y)) + 0.5 * t * t * (
        exact_variance - float(np.var(y))
    )


def random_spectra(rng: np.random.Generator, d: int, count: int) -> np.ndarray:
    x = rng.normal(size=(count, d))
    x -= x.mean(axis=1, keepdims=True)
    x /= np.linalg.norm(x, axis=1, keepdims=True)
    return x


def run(d: int, r: int, samples: int, spectra: int, seed: int) -> dict:
    if not (1 <= r <= d - 1):
        raise ValueError("require 1 <= r <= d-1")
    rng = np.random.default_rng(seed)
    diag_p = haar_projector_diagonals(rng, d, r, samples)
    candidates = random_spectra(rng, d, spectra)
    a1 = one_spike(d)
    ar = r_block(d, r)
    candidates = np.vstack([a1, ar, candidates])
    coeffs = exact_coefficients(d, r)
    schur_coeffs = schur_moment_coefficients(d, r)
    assert schur_coeffs["c2_schur"] == coeffs["c2"]
    assert schur_coeffs["c3_schur"] == coeffs["c3"]
    if d >= 4:
        assert schur_coeffs["c22_schur"] == coeffs["c22"]
        assert schur_coeffs["c4_schur"] == coeffs["c4"]
    fields = [0.2, 0.5, 1.0, 5.0, 20.0]
    exact_variance = float(coeffs["c2"])
    table = []
    for t in fields:
        scores = np.array(
            [controlled_log_mgf(diag_p @ candidates[j], t, exact_variance) for j in range(len(candidates))]
        )
        best = int(np.argmax(scores))
        table.append(
            {
                "t": t,
                "one_spike": float(scores[0]),
                "r_block": float(scores[1]),
                "best_index": best,
                "best_score": float(scores[best]),
            }
        )
    weak_p3_one = float(np.sum(a1**3))
    weak_p3_rblock = float(np.sum(ar**3))
    strong_one = float(np.sum(np.sort(a1)[-r:]))
    strong_rblock = float(np.sum(np.sort(ar)[-r:]))
    return {
        "parameters": {"d": d, "r": r, "samples": samples, "spectra": spectra, "seed": seed},
        "exact": {k: str(v) for k, v in coeffs.items()},
        "schur_character_check": {k: str(v) for k, v in schur_coeffs.items()},
        "candidate_checks": {
            "one_spike_trace": float(a1.sum()),
            "one_spike_norm2": float(a1 @ a1),
            "r_block_trace": float(ar.sum()),
            "r_block_norm2": float(ar @ ar),
            "p3_one_spike": weak_p3_one,
            "p3_r_block": weak_p3_rblock,
            "kyfan_r_one_spike": strong_one,
            "kyfan_r_r_block": strong_rblock,
        },
        "monte_carlo": table,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", type=int, default=6)
    parser.add_argument("--r", type=int, default=2)
    parser.add_argument("--samples", type=int, default=12000)
    parser.add_argument("--spectra", type=int, default=300)
    parser.add_argument("--seed", type=int, default=20260811)
    parser.add_argument(
        "--output", type=Path, default=BASE_DIR / "grassmann_switch_diagnostics.json"
    )
    args = parser.parse_args()
    result = run(args.d, args.r, args.samples, args.spectra, args.seed)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
