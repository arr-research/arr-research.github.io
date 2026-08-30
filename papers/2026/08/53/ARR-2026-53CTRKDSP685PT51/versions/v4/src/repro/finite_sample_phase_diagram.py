"""Deterministic finite-sample diagnostic for the weighted logistic Gram law."""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "figures" / "finite_sample_resolution.pdf"
DATA_OUTPUT = ROOT / "repro" / "finite_sample_resolution.json"
SEED = 2026082917
D = 12
RADIUS = 6.0
REPETITIONS = 320
RATIOS = np.asarray([0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0])
POWERS = (1.0, 2.0)
SLAB_HALF_WIDTH = 1.0


def sigmoid_prime(x: np.ndarray | float) -> np.ndarray | float:
    x = np.asarray(x)
    ans = np.exp(-np.abs(x)) / (1.0 + np.exp(-np.abs(x))) ** 2
    return ans if ans.ndim else float(ans)


def population(p: float) -> tuple[float, float]:
    phi = lambda z: np.exp(-0.5 * z * z) / np.sqrt(2.0 * np.pi)
    alpha = quad(lambda z: sigmoid_prime(RADIUS * z) ** p * phi(z), -12.0, 12.0,
                 epsabs=2e-13, epsrel=2e-13, limit=300)[0]
    beta = quad(lambda z: z * z * sigmoid_prime(RADIUS * z) ** p * phi(z), -12.0, 12.0,
                epsabs=2e-13, epsrel=2e-13, limit=300)[0]
    return alpha, beta


def quantiles(values: list[float]) -> tuple[float, float]:
    return tuple(float(v) for v in np.quantile(values, [0.5, 0.9]))


def simulate() -> dict[str, object]:
    rng = np.random.default_rng(SEED)
    sample_sizes = np.maximum(D + 1, np.rint(RATIOS * RADIUS * D).astype(int))
    pop = {p: population(p) for p in POWERS}
    results: dict[float, dict[str, list[tuple[float, float]]]] = {
        p: {"tangential": [], "radial": [], "angle": []} for p in POWERS
    }
    slab_empirical: list[float] = []

    for n in sample_sizes:
        metrics = {
            p: {"tangential": [], "radial": [], "angle": []} for p in POWERS
        }
        empty_count = 0
        for _ in range(REPETITIONS):
            x = rng.standard_normal((n, D))
            z = x[:, -1]
            empty_count += int(np.all(np.abs(RADIUS * z) > SLAB_HALF_WIDTH))
            y = x[:, :-1]
            for p in POWERS:
                alpha, beta = pop[p]
                weights = sigmoid_prime(RADIUS * z) ** p
                gram = (x.T * weights) @ x / n
                tangential = (y.T * weights) @ y / n
                tangential_error = np.linalg.norm(
                    tangential - alpha * np.eye(D - 1), ord=2
                ) / alpha
                eigenvalues, eigenvectors = np.linalg.eigh(gram)
                radial_error = abs(eigenvalues[0] - beta) / beta
                angle = np.sqrt(max(0.0, 1.0 - eigenvectors[-1, 0] ** 2))
                metrics[p]["tangential"].append(float(tangential_error))
                metrics[p]["radial"].append(float(radial_error))
                metrics[p]["angle"].append(float(angle))
        for p in POWERS:
            for key in ("tangential", "radial", "angle"):
                results[p][key].append(quantiles(metrics[p][key]))
        slab_empirical.append(empty_count / REPETITIONS)

    slab_probability = 2.0 * ndtr(SLAB_HALF_WIDTH / RADIUS) - 1.0
    slab_exact = (1.0 - slab_probability) ** sample_sizes
    return {
        "sample_sizes": sample_sizes,
        "ratios": sample_sizes / (RADIUS * D),
        "population": pop,
        "metrics": results,
        "slab_empirical": np.asarray(slab_empirical),
        "slab_exact": slab_exact,
    }


def make_figure(data: dict[str, object]) -> None:
    ratios = np.asarray(data["ratios"])
    metrics = data["metrics"]
    colors = {1.0: "#1565c0", 2.0: "#d95f02"}
    labels = {1.0: r"$p=1$", 2.0: r"$p=2$"}
    fig, axes = plt.subplots(2, 2, figsize=(10.4, 7.2))

    panels = [
        (axes[0, 0], "tangential", "relative tangential operator error"),
        (axes[0, 1], "radial", "relative smallest-eigenvalue error"),
        (axes[1, 0], "angle", r"radial eigenspace error $\sin\theta$"),
    ]
    for ax, key, ylabel in panels:
        for p in POWERS:
            values = np.asarray(metrics[p][key])
            ax.loglog(ratios, values[:, 0], marker="o", color=colors[p], label=labels[p])
            ax.loglog(ratios, values[:, 1], marker=".", ls="--", color=colors[p], alpha=0.72)
        ax.set_xlabel(r"normalized sample size $n/(rd)$")
        ax.set_ylabel(ylabel)
        ax.grid(True, which="both", alpha=0.22)
    axes[0, 0].legend(frameon=False, title="solid: median\ndashed: 90th percentile")

    ax = axes[1, 1]
    exact = np.asarray(data["slab_exact"])
    empirical = np.asarray(data["slab_empirical"])
    floor = 0.5 / REPETITIONS
    ax.semilogy(ratios, np.maximum(exact, 1e-8), color="#4a148c", lw=2,
                label=r"exact probability (display floor $10^{-8}$)")
    positive = empirical > 0.0
    ax.semilogy(ratios[positive], empirical[positive], "o", color="#00897b",
                label="fixed-seed frequency")
    ax.semilogy(ratios[~positive], np.full(np.count_nonzero(~positive), floor), "v",
                color="#00897b", markerfacecolor="none", label="zero events (plotting limit)")
    ax.set_xlabel(r"normalized sample size $n/(rd)$")
    ax.set_ylabel(r"probability no sample has $|rZ|\leq1$")
    ax.grid(True, which="both", alpha=0.22)
    ax.legend(frameon=False)

    fig.suptitle(
        rf"Finite-sample resolution ($d={D}$, $r={RADIUS:g}$, {REPETITIONS} repetitions)",
        fontsize=13,
    )
    fig.tight_layout()
    fixed_time = datetime(2026, 8, 29, tzinfo=timezone.utc)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT,
        bbox_inches="tight",
        metadata={"CreationDate": fixed_time, "ModDate": fixed_time},
    )
    plt.close(fig)


def write_certificate(data: dict[str, object]) -> None:
    metrics = data["metrics"]
    payload = {
        "schema": "arr.finite-sample-resolution.v1",
        "seed": SEED,
        "dimension": D,
        "radius": RADIUS,
        "repetitions": REPETITIONS,
        "powers": list(POWERS),
        "slab_half_width": SLAB_HALF_WIDTH,
        "sample_sizes": np.asarray(data["sample_sizes"]).astype(int).tolist(),
        "normalized_sample_sizes": np.asarray(data["ratios"]).tolist(),
        "population": {
            str(p): {"alpha": data["population"][p][0], "beta": data["population"][p][1]}
            for p in POWERS
        },
        "metrics": {
            str(p): {
                key: [{"median": pair[0], "p90": pair[1]} for pair in metrics[p][key]]
                for key in ("tangential", "radial", "angle")
            }
            for p in POWERS
        },
        "empty_slab": {
            "exact": np.asarray(data["slab_exact"]).tolist(),
            "fixed_seed_frequency": np.asarray(data["slab_empirical"]).tolist(),
        },
    }
    DATA_OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    data = simulate()
    make_figure(data)
    write_certificate(data)
    print(f"wrote {OUTPUT}")
    print(f"wrote {DATA_OUTPUT}")
    print(f"sample_sizes={list(map(int, data['sample_sizes']))}")
    print(f"seed={SEED}, repetitions={REPETITIONS}, d={D}, r={RADIUS}")


if __name__ == "__main__":
    main()
