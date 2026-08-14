"""Generate the diagnostic scalar-envelope figure used by the manuscript."""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar


def log_L(n: int, k: int, kap: float) -> float:
    z = kap * kap / 4.0
    term = 1.0
    total = 1.0
    for m in range(1, 10000):
        ratio = z / (m * m)
        for i in range(1, k + 1):
            ratio *= (i + m - 1) / (n - k + i + m - 1)
        term *= ratio
        total += term
        if term < 2e-14 * total and m > kap:
            return math.log(total)
    raise RuntimeError("series failed to converge")


def envelope(n: int, k: int, s: float) -> tuple[float, float]:
    def phi(b: float) -> float:
        return log_L(n, k, 2.0 * s * b) - s * b * b

    grid = np.linspace(0.0, 1.0, 241)
    vals = np.array([phi(float(b)) for b in grid])
    j = int(np.argmax(vals))
    lo = float(grid[max(0, j - 2)])
    hi = float(grid[min(len(grid) - 1, j + 2)])
    if hi == lo:
        return lo, float(vals[j])
    res = minimize_scalar(lambda b: -phi(float(b)), bounds=(lo, hi), method="bounded")
    candidates = [(0.0, 0.0), (float(res.x), -float(res.fun))]
    return max(candidates, key=lambda pair: pair[1])


def main() -> None:
    cases = [
        (4, 2, r"$\Lambda^2\mathbb{C}^4$"),
        (5, 2, r"$\Lambda^2\mathbb{C}^5$"),
        (6, 2, r"$\Lambda^2\mathbb{C}^6$"),
        (6, 3, r"$\Lambda^3\mathbb{C}^6$"),
    ]
    colors = ["#566573", "#8e6c4b", "#236fa1", "#9b2f56"]
    x = np.linspace(0.0, 1.16, 105)
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.75), constrained_layout=True)

    for (n, k, label), color in zip(cases, colors):
        N = math.comb(n, k)
        bs, gains = [], []
        for xx in x:
            b, gain = envelope(n, k, float(xx * N))
            bs.append(b)
            gains.append(gain / N)
        axes[0].plot(x, gains, lw=2.0, color=color, label=label)
        axes[1].plot(x, bs, lw=2.0, color=color, label=label)

    for ax in axes:
        ax.axvline(1.0, color="black", lw=0.9, ls="--", alpha=0.6)
        ax.grid(alpha=0.18, linewidth=0.6)
        ax.set_xlabel(r"normalized field $s/\binom{n}{k}$")
        ax.tick_params(labelsize=8.5)
    axes[0].set_ylabel(r"optimized gain $\max_b\phi_s(b)/\binom{n}{k}$")
    axes[1].set_ylabel(r"active radius $b_*(s)$")
    axes[0].set_title("Dual gain")
    axes[1].set_title("Global report radius")
    axes[0].legend(frameon=False, fontsize=8, loc="upper left")
    axes[1].set_ylim(-0.02, 1.02)

    out = Path(__file__).with_name("paper") / "coherent_orbit_envelopes.pdf"
    fig.savefig(out, bbox_inches="tight")
    fig.savefig(out.with_suffix(".png"), dpi=180, bbox_inches="tight")
    print(out)


if __name__ == "__main__":
    main()
