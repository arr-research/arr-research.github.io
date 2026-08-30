"""Fixed-seed replay for the quantitative finite-saturation projector bound."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "figures" / "joint_spectral_resolution.pdf"
CERTIFICATE = ROOT / "repro" / "joint_spectral_resolution.json"
SEED = 2026083011


def log_logistic_prime(t: np.ndarray) -> np.ndarray:
    absolute = np.abs(t)
    return -absolute - 2.0 * np.log1p(np.exp(-absolute))


def projector_distance(x: np.ndarray, y: np.ndarray) -> float:
    cosine = float(np.clip(abs(x @ y), 0.0, 1.0))
    return float(np.sqrt(max(0.0, 1.0 - cosine * cosine)))


def finite_bottom_vector(samples: np.ndarray, r: float, p: float) -> np.ndarray:
    log_weights = p * log_logistic_prime(r * samples[:, -1])
    weights = np.exp(log_weights - np.max(log_weights))
    gram = (samples.T * weights) @ samples / samples.shape[0]
    _, vectors = np.linalg.eigh(gram)
    return vectors[:, 0]


def selected_normal(samples: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    dimension = samples.shape[1]
    order = np.argsort(np.abs(samples[:, -1]))
    selected = samples[order[: dimension - 1]]
    _, _, vh = np.linalg.svd(selected, full_matrices=True)
    return vh[-1], order


def main() -> None:
    rng = np.random.default_rng(SEED)
    FIGURE.parent.mkdir(parents=True, exist_ok=True)

    dimension = 5
    sample_size = 30
    power = 1.0
    samples = rng.standard_normal((sample_size, dimension))
    limit_vector, order = selected_normal(samples)
    m = dimension - 1
    selected = samples[order[:m]]
    singular_min = float(np.linalg.svd(selected, compute_uv=False)[-1])
    tail_operator_squared = float(np.linalg.norm(samples[order[m:]].T, 2) ** 2)
    absolute_scores = np.abs(samples[order, -1])
    spacing = float(absolute_scores[m] - absolute_scores[m - 1])

    radii = np.linspace(5.0, 80.0, 76)
    errors = []
    exact_bounds = []
    logistic_bounds = []
    exact_qs = []
    coarse_qs = []
    checked = 0
    for radius in radii:
        bottom = finite_bottom_vector(samples, float(radius), power)
        error = projector_distance(bottom, limit_vector)
        log_weights = power * log_logistic_prime(radius * absolute_scores)
        weight_ratio = float(np.exp(log_weights[m] - log_weights[m - 1]))
        exact_q = weight_ratio * tail_operator_squared / (singular_min * singular_min)
        coarse_q = (
            4.0**power
            * np.exp(-power * radius * spacing)
            * tail_operator_squared
            / (singular_min * singular_min)
        )
        exact_bound = exact_q if exact_q < 1.0 else np.nan
        coarse_bound = coarse_q if coarse_q < 1.0 else np.nan
        if exact_q < 1.0 and exact_q > 2e-7:
            checked += 1
            if error > exact_bound * (1.0 + 2e-7) + 2e-9:
                raise AssertionError((radius, error, exact_q))
        errors.append(error)
        exact_bounds.append(exact_bound)
        logistic_bounds.append(coarse_bound)
        exact_qs.append(exact_q)
        coarse_qs.append(coarse_q)

    if checked < 8:
        raise AssertionError(("too few numerically stable bound checks", checked))
    if not errors[-1] < errors[0] / 100.0:
        raise AssertionError((errors[0], errors[-1]))
    if np.any(np.asarray(exact_qs) > np.asarray(coarse_qs) * (1.0 + 2e-12)):
        raise AssertionError("logistic ratio bound failed")

    fig, ax = plt.subplots(figsize=(6.6, 4.2), constrained_layout=True)
    ax.semilogy(radii, errors, color="#1f77b4", linewidth=2.0, label="projector error")
    ax.semilogy(radii, exact_bounds, "--", color="#d95f02", label=r"exact $q_r$")
    ax.semilogy(radii, logistic_bounds, ":", color="#2ca02c", label="explicit logistic envelope")
    ax.set_xlabel("teacher norm $r$")
    ax.set_ylabel(r"$\|\widehat P_r^{\rm bot}-P_\infty\|_{\rm op}$")
    ax.set_title(rf"Finite-saturation certificate ($d={dimension}$, $n={sample_size}$)")
    ax.grid(True, which="both", alpha=0.18)
    ax.legend(frameon=False)
    fig.savefig(
        FIGURE,
        metadata={
            "Creator": "ARR deterministic joint-spectral replay",
            "CreationDate": datetime(2026, 8, 30, tzinfo=timezone.utc),
        },
    )
    plt.close(fig)

    payload = {
        "schema": "arr.joint-spectral-resolution.v1",
        "seed": SEED,
        "dimension": dimension,
        "sample_size": sample_size,
        "power": power,
        "selected_spacing": spacing,
        "selected_singular_min": singular_min,
        "tail_operator_squared": tail_operator_squared,
        "radii": radii.tolist(),
        "projector_error": errors,
        "exact_q": exact_qs,
        "coarse_q": coarse_qs,
        "checked_bound_points": checked,
    }
    CERTIFICATE.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: deterministic finite-saturation projector bound")
    print(f"figure_sha256={hashlib.sha256(FIGURE.read_bytes()).hexdigest()}")
    print(f"certificate_sha256={hashlib.sha256(CERTIFICATE.read_bytes()).hexdigest()}")
    print(
        json.dumps(
            {
                "spacing": spacing,
                "singular_min": singular_min,
                "tail_operator_squared": tail_operator_squared,
                "checked_bound_points": checked,
                "last_error": errors[-1],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
