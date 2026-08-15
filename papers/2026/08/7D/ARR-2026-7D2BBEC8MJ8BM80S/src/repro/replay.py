#!/usr/bin/env python3
"""Deterministic diagnostics for the SU(2) cylinder formulas.

This is a numerical replay, not a proof certificate.  The rigorous algebraic
endpoints are stated and proved in the manuscript and the companion Lean
sources.
"""

from __future__ import annotations

import math

import numpy as np
from numpy.polynomial.legendre import leggauss


def chi(n: int, theta: np.ndarray) -> np.ndarray:
    """SU(2) character chi_n at eigenangle theta, stable at endpoints."""
    out = np.empty_like(theta)
    den = np.sin(theta)
    regular = np.abs(den) > 1e-13
    out[regular] = np.sin((n + 1) * theta[regular]) / den[regular]
    # At theta=0 the removable limit is n+1; at theta=pi it is
    # (-1)^n(n+1).  The quadrature nodes do not hit either endpoint, but the
    # implementation and its stated contract should still be correct there.
    out[~regular] = np.where(
        np.cos(theta[~regular]) >= 0.0,
        n + 1,
        ((-1) ** n) * (n + 1),
    )
    return out


def casimir(n: int) -> float:
    return n * (n + 2) / 4.0


def main() -> None:
    endpoints = np.array([0.0, math.pi])
    endpoint_error = max(
        float(np.max(np.abs(
            chi(n, endpoints) - np.array([n + 1, ((-1) ** n) * (n + 1)])
        )))
        for n in range(13)
    )

    # Weyl probability measure: (2/pi) sin(theta)^2 dtheta on [0,pi].
    x, w = leggauss(400)
    theta = (x + 1.0) * math.pi / 2.0
    weights = w * np.sin(theta) ** 2
    # Jacobian pi/2 cancels the factor 2/pi.
    nmax = 12
    chars = np.stack([chi(n, theta) for n in range(nmax)])
    gram = (chars * weights) @ chars.T
    orth_error = float(np.max(np.abs(gram - np.eye(nmax))))

    s, t = 0.37, 0.61
    a = np.exp(-s * np.array([casimir(n) for n in range(nmax)]))
    b = np.exp(-t * np.array([casimir(n) for n in range(nmax)]))
    semigroup_error = float(np.max(np.abs(a * b - np.exp(
        -(s + t) * np.array([casimir(n) for n in range(nmax)])))))

    nonvac = np.exp(-t * np.array([casimir(n) for n in range(1, nmax)]))
    sharp = math.exp(-3.0 * t / 4.0)
    gap_error = abs(float(np.max(nonvac)) - sharp)
    sharp_mode = int(np.argmax(nonvac)) + 1

    # Random finite character polynomials test reflection positivity at 2s.
    rng = np.random.default_rng(20260814)
    coeff = rng.normal(size=nmax) + 1j * rng.normal(size=nmax)
    reflection_form = float(np.sum(np.abs(coeff) ** 2 * np.exp(
        -2.0 * s * np.array([casimir(n) for n in range(nmax)]))))

    print(f"endpoint_character_max_error={endpoint_error:.3e}")
    print(f"orthogonality_max_error={orth_error:.3e}")
    print(f"semigroup_multiplier_max_error={semigroup_error:.3e}")
    print(f"sharp_gap_error={gap_error:.3e}")
    print(f"sharp_mode={sharp_mode}")
    print(f"reflection_form={reflection_form:.16e}")
    assert endpoint_error == 0.0
    assert orth_error < 2e-12
    assert semigroup_error < 2e-15
    assert gap_error < 2e-15
    assert sharp_mode == 1
    assert reflection_form > 0.0
    print("REPLAY: PASS")


if __name__ == "__main__":
    main()
