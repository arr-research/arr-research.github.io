"""Lightweight numerical replay and figure for the oriented-Plucker paper.

The analytic theorem is primary.  This script evaluates its one-dimensional
beta integral, locates diagnostic coexistence contacts, and draws the exact
covariant branches.  It uses one process and bounded fixed grids only.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq


def moments(n: int, kappa: float) -> tuple[float, float, float]:
    q = n - 2
    # Scale by exp(-|kappa|) to remain stable; the scale cancels in ratios.
    scale = abs(kappa)

    def base(x: float) -> float:
        return 0.5 * q * (1.0 - abs(x)) ** (q - 1) * math.exp(kappa * x - scale)

    vals = [quad(lambda x, j=j: x**j * base(x), -1.0, 1.0,
                 epsabs=2e-12, epsrel=2e-12, limit=100)[0] for j in range(3)]
    z, z1, z2 = vals
    log_l = math.log(z) + scale
    mean = z1 / z
    var = z2 / z - mean * mean
    return log_l, mean, var


def contact_function(n: int, kappa: float) -> float:
    k, b, _ = moments(n, kappa)
    return 2.0 * k - kappa * b


def first_contact(n: int) -> dict[str, float] | None:
    # The contact diagnostic is finite and O(1).  Starting at 0.1 avoids
    # subtractive cancellation in F=2K-kappa K' at the removable zero root.
    grid = np.geomspace(1e-1, 250.0, 1200)
    vals = np.array([contact_function(n, float(x)) for x in grid])
    roots: list[float] = []
    for a, b, fa, fb in zip(grid[:-1], grid[1:], vals[:-1], vals[1:]):
        if fa * fb < 0 and max(abs(fa), abs(fb)) > 1e-10:
            roots.append(brentq(lambda x: contact_function(n, x), float(a), float(b), xtol=2e-13))
    # For positive fourth cumulant F is negative near zero; the physical
    # contact is the first negative-to-positive root.
    for root in roots:
        left = contact_function(n, root * (1 - 1e-5))
        right = contact_function(n, root * (1 + 1e-5))
        if left < 0 < right:
            k, radius, _ = moments(n, root)
            lam = root / (2 * radius)
            return {
                "kappa_c": root,
                "b_c": radius,
                "lambda_c": lam,
                "D_c": 1 - radius * radius,
                "R_c": root * radius - k,
                "contact_residual": 2 * k - root * radius,
            }
    return None


def make_figure(output: Path) -> list[dict[str, float | int | None]]:
    output.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.05))
    x = np.linspace(-1, 1, 801)
    for n in (3, 4, 5, 6, 8):
        q = n - 2
        density = 0.5 * q * (1 - np.abs(x)) ** (q - 1)
        axes[0].plot(x, density, label=fr"$n={n}$")
    axes[0].set_xlabel(r"overlap $x=\langle W,Q\rangle$")
    axes[0].set_ylabel(r"$f_n(x)$")
    axes[0].set_title("Exact Plucker-overlap laws")
    axes[0].legend(frameon=False, ncol=2)
    axes[0].grid(alpha=0.2)

    diagnostics: list[dict[str, float | int | None]] = []
    for n in (3, 4, 5, 6, 7, 8):
        kappas = np.geomspace(1e-3, 70, 520)
        branch_d: list[float] = []
        branch_r: list[float] = []
        for kap in kappas:
            k, b, _ = moments(n, float(kap))
            branch_d.append(1 - b * b)
            branch_r.append(kap * b - k)
        order = np.argsort(branch_d)
        (line,) = axes[1].plot(np.asarray(branch_d)[order], np.asarray(branch_r)[order], label=fr"$n={n}$")
        contact = first_contact(n)
        diagnostics.append({"n": n, **(contact or {"kappa_c": None})})
        if contact:
            color = line.get_color()
            axes[1].scatter([contact["D_c"]], [contact["R_c"]], s=22, color=color, zorder=4)
            axes[1].plot([contact["D_c"], 1.0], [contact["R_c"], 0.0],
                         linestyle="--", linewidth=1.1, color=color, alpha=0.8)
    axes[1].set_xlim(0, 1)
    axes[1].set_ylim(bottom=0)
    axes[1].set_xlabel(r"distortion $D$")
    axes[1].set_ylabel(r"rate $R$ (nats)")
    axes[1].set_title("Covariant branches; dots mark coexistence")
    axes[1].legend(frameon=False, ncol=2)
    axes[1].grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(output, bbox_inches="tight")
    fig.savefig(output.with_suffix(".png"), dpi=180, bbox_inches="tight")
    plt.close(fig)
    return diagnostics


def main() -> None:
    parser = argparse.ArgumentParser()
    here = Path(__file__).resolve().parent
    parser.add_argument("--figure", type=Path, default=here / "paper" / "figures" / "plucker_frontier.pdf")
    parser.add_argument("--json", type=Path, default=here / "plucker_frontier_diagnostics.json")
    args = parser.parse_args()
    diagnostics = make_figure(args.figure)
    payload = {
        "scope": "one-dimensional diagnostic replay; analytic proofs are primary",
        "contacts": diagnostics,
    }
    args.json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"PASS: wrote {args.figure} and {args.json}")


if __name__ == "__main__":
    main()
