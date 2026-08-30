"""Fixed-seed diagnostics for the extreme-saturation eigenspace theorem."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "figures" / "spectral_lexicography.pdf"
CERTIFICATE = ROOT / "repro" / "spectral_lexicography.json"
SEED = 2026083004


def limiting_vector(samples: np.ndarray) -> tuple[np.ndarray, float]:
    """Normal to the d-1 observations with smallest absolute last score."""
    d = samples.shape[1]
    chosen = np.argsort(np.abs(samples[:, -1]))[: d - 1]
    block = samples[chosen]
    _, _, vh = np.linalg.svd(block, full_matrices=True)
    vector = vh[-1]
    if vector[-1] < 0.0:
        vector = -vector
    sine = float(np.sqrt(max(0.0, 1.0 - vector[-1] ** 2)))
    return vector, sine


def log_logistic_prime(t: np.ndarray) -> np.ndarray:
    absolute = np.abs(t)
    return -absolute - 2.0 * np.log1p(np.exp(-absolute))


def finite_bottom_vector(samples: np.ndarray, r: float, p: float = 1.0) -> np.ndarray:
    log_weights = p * log_logistic_prime(r * samples[:, -1])
    weights = np.exp(log_weights - np.max(log_weights))
    gram = (samples.T * weights) @ samples / samples.shape[0]
    _, vectors = np.linalg.eigh(gram)
    return vectors[:, 0]


def projector_distance(x: np.ndarray, y: np.ndarray) -> float:
    cosine = float(np.clip(abs(x @ y), 0.0, 1.0))
    return float(np.sqrt(max(0.0, 1.0 - cosine**2)))


def main() -> None:
    rng = np.random.default_rng(SEED)
    FIGURE.parent.mkdir(parents=True, exist_ok=True)

    d = 6
    m = d - 1
    sample_sizes = np.array([6, 10, 16, 25, 40, 64, 100, 160])
    repetitions = 1800
    medians = []
    q90 = []
    for n in sample_sizes:
        values = np.empty(repetitions)
        for rep in range(repetitions):
            samples = rng.standard_normal((int(n), d))
            _, values[rep] = limiting_vector(samples)
        medians.append(float(np.median(values)))
        q90.append(float(np.quantile(values, 0.9)))

    d_finite = 5
    n_finite = 30
    r_grid = np.array([1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0])
    finite_repetitions = 500
    distances = np.empty((finite_repetitions, len(r_grid)))
    for rep in range(finite_repetitions):
        samples = rng.standard_normal((n_finite, d_finite))
        limit_vector, _ = limiting_vector(samples)
        for j, r in enumerate(r_grid):
            finite_vector = finite_bottom_vector(samples, float(r))
            distances[rep, j] = projector_distance(finite_vector, limit_vector)

    finite_median = np.median(distances, axis=0)
    finite_q90 = np.quantile(distances, 0.9, axis=0)
    if not medians[-1] < medians[0] / 8.0:
        raise AssertionError((medians[0], medians[-1]))
    if not finite_median[-1] < finite_median[0] / 10.0:
        raise AssertionError((finite_median[0], finite_median[-1]))

    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.8), constrained_layout=True)
    ax = axes[0]
    ax.loglog(sample_sizes, medians, "o-", color="#1f77b4", label="median")
    ax.loglog(sample_sizes, q90, "s-", color="#d95f02", label="90th percentile")
    reference = medians[-1] * sample_sizes[-1] / sample_sizes
    ax.loglog(sample_sizes, reference, "--", color="#333333", label=r"reference $n^{-1}$")
    ax.set_xlabel("sample size $n$")
    ax.set_ylabel(r"limiting $\sin\theta_\infty$")
    ax.set_title(rf"Order-statistic angle law ($d={d}$)")
    ax.grid(True, which="both", alpha=0.18)
    ax.legend(frameon=False, fontsize=8.5)

    ax = axes[1]
    ax.loglog(r_grid, finite_median, "o-", color="#2ca02c", label="median")
    ax.loglog(r_grid, finite_q90, "s-", color="#9467bd", label="90th percentile")
    ax.set_xlabel("teacher norm $r$")
    ax.set_ylabel(r"$\|\widehat P_r^{\rm bot}-P_\infty\|_{\rm op}$")
    ax.set_title(rf"Spectral lexicography ($d={d_finite}$, $n={n_finite}$)")
    ax.grid(True, which="both", alpha=0.18)
    ax.legend(frameon=False, fontsize=8.5)

    fig.savefig(
        FIGURE,
        metadata={
            "Creator": "ARR deterministic spectral-lexicography replay",
            "CreationDate": datetime(2026, 8, 30, tzinfo=timezone.utc),
        },
    )
    plt.close(fig)

    payload = {
        "schema": "arr.spectral-lexicography.v1",
        "seed": SEED,
        "limit_experiment": {
            "dimension": d,
            "repetitions": repetitions,
            "sample_sizes": sample_sizes.tolist(),
            "median_sine": medians,
            "q90_sine": q90,
            "normalization_m32": m ** 1.5,
        },
        "finite_r_convergence": {
            "dimension": d_finite,
            "sample_size": n_finite,
            "repetitions": finite_repetitions,
            "radii": r_grid.tolist(),
            "median_projector_distance": finite_median.tolist(),
            "q90_projector_distance": finite_q90.tolist(),
        },
    }
    CERTIFICATE.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: extreme-saturation angle scaling and finite-r projector convergence")
    print(f"figure_sha256={hashlib.sha256(FIGURE.read_bytes()).hexdigest()}")
    print(f"certificate_sha256={hashlib.sha256(CERTIFICATE.read_bytes()).hexdigest()}")
    print(json.dumps(payload["finite_r_convergence"], indent=2))


if __name__ == "__main__":
    main()
