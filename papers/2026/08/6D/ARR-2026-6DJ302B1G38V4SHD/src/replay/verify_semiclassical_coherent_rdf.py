"""Bounded diagnostics for the semiclassical coherent-orbit RDF theorem.

The theorem is analytic.  This replay evaluates two exact Weyl dimension
sequences, solves the exact scalar contact equation, and compares it with the
dimension-universal asymptotic.  It deliberately uses no Monte Carlo and
finishes in well under one second on the reference machine.
"""

from __future__ import annotations

import json
from math import log, pi
from pathlib import Path


def partition(t: float, dimension) -> tuple[float, float]:
    """K(t)=log L(t) and K'(t), using a positive recurrence."""
    weights = [1.0]
    raw = 1.0
    running = 1.0
    for m in range(1, 200):
        raw *= (t * t / 4.0) / (m * m)
        weight = raw / dimension(m)
        weights.append(weight)
        running += weight
        if m > t and weight < 1.0e-17 * running:
            break
    derivative = sum((2.0 * m / t) * w for m, w in enumerate(weights)) / running
    return log(running), derivative


def solve_contact(dimension, hilbert_dimension: int, p: int) -> dict:
    a = p + 0.5
    ell = log(hilbert_dimension)
    prediction = 2.0 * ell + 2.0 * a * log(ell) + log(4.0 * pi) - a

    def contact(t: float) -> float:
        k, kp = partition(t, dimension)
        return 2.0 * k - t * kp

    lo, hi = 0.55 * prediction, 1.55 * prediction
    assert contact(lo) < 0.0 < contact(hi)
    for _ in range(80):
        mid = (lo + hi) / 2.0
        if contact(mid) <= 0.0:
            lo = mid
        else:
            hi = mid
    t = (lo + hi) / 2.0
    k, b = partition(t, dimension)
    distortion = 1.0 - b * b
    slope = t / (2.0 * b)
    slope_prediction = ell + a * log(ell) + log(2.0 * pi**0.5)
    return {
        "hilbert_dimension": hilbert_dimension,
        "contact_t": t,
        "contact_t_prediction": prediction,
        "contact_t_error": t - prediction,
        "contact_residual": 2.0 * k - t * b,
        "b": b,
        "D": distortion,
        "scaled_D": distortion * ell,
        "scaled_D_prediction": a,
        "slope": slope,
        "slope_prediction": slope_prediction,
        "slope_error": slope - slope_prediction,
    }


def main() -> None:
    families = []
    specifications = (
        ("SU(2), Sym^N(C^2)", 1, (100, 10_000, 1_000_000)),
        ("SU(3), Sym^N(C^3)", 2, (40, 400, 4_000)),
    )
    for name, p, values in specifications:
        rows = []
        for n in values:
            if p == 1:
                dimension = lambda m, n=n: m * n + 1
                hilbert_dimension = n + 1
            else:
                dimension = lambda m, n=n: (m * n + 1) * (m * n + 2) / 2
                hilbert_dimension = (n + 1) * (n + 2) // 2
            row = {"N": n, **solve_contact(dimension, hilbert_dimension, p)}
            rows.append(row)
        assert abs(rows[-1]["contact_t_error"]) < abs(rows[0]["contact_t_error"])
        assert abs(rows[-1]["slope_error"]) < abs(rows[0]["slope_error"])
        assert abs(rows[-1]["scaled_D"] - (p + 0.5)) < abs(rows[0]["scaled_D"] - (p + 0.5))
        families.append({"family": name, "p": p, "a": p + 0.5, "rows": rows})

    payload = {
        "scope": "Bounded deterministic diagnostics; the asymptotic theorem is analytic.",
        "families": families,
    }
    output = Path(__file__).with_name("semiclassical_coherent_rdf_verification.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    print(f"PASS: wrote {output.name}")


if __name__ == "__main__":
    main()
