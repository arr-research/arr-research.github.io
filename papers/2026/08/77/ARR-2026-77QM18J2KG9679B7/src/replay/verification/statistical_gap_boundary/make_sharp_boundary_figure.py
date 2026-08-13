from __future__ import annotations

import json
import math
from pathlib import Path
from statistics import NormalDist

import matplotlib.pyplot as plt


def recurrence(n: int, x: float, kind: str) -> float:
    if n == 0:
        return 1.0
    p0, p1 = (1.0, x) if kind == "T" else (1.0, 2.0 * x + 1.0)
    if n == 1:
        return p1
    for _ in range(2, n + 1):
        p0, p1 = p1, 2.0 * x * p1 - p0
    return p1


def main() -> None:
    theta = 0.5
    delta = 0.25
    gamma = 0.2
    y_delta = 1.0 + 2.0 * delta / theta
    degrees = list(range(9))
    first = [theta / recurrence(n, y_delta, "T") ** 2 for n in degrees]
    fourth = [theta / recurrence(n, y_delta, "W") ** 2 for n in degrees]
    threshold = delta * gamma / (1.0 - gamma)

    fisher = 473198881 / 12500000
    alpha = 0.05
    z = NormalDist().inv_cdf(1.0 - alpha)
    h_values = [j / 500 for j in range(301)]
    powers = [1.0 - NormalDist().cdf(z - h * math.sqrt(fisher)) for h in h_values]

    plt.rcParams.update({"font.size": 9, "axes.titlesize": 10, "axes.labelsize": 9})
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.75), constrained_layout=True)

    ax = axes[0]
    ax.semilogy(degrees, first, "o--", color="#2f65ad", label=r"first kind: $\theta/T_N(y_\delta)^2$")
    ax.semilogy(degrees, fourth, "s-", color="#b4472d", label=r"fourth kind: $\theta/W_N(y_\delta)^2$")
    ax.axhline(threshold, color="#333333", linestyle=":", label="uniform-sign threshold")
    ax.set_xlabel("polynomial degree $N$")
    ax.set_ylabel("worst low-band localizer loss")
    ax.set_title("Exact weighted-filter improvement")
    ax.set_xticks(degrees)
    ax.grid(True, which="both", alpha=0.25)
    ax.legend(frameon=False, fontsize=7.5)

    ax = axes[1]
    ax.plot(h_values, powers, color="#704c9f", linewidth=2)
    ax.axhline(alpha, color="#333333", linestyle=":", label=r"size $\alpha=0.05$")
    ax.set_xlabel(r"local hidden weight $h=\sqrt{n}\,w_n$")
    ax.set_ylabel("optimal asymptotic power")
    ax.set_ylim(0.0, 1.02)
    ax.set_title("Hidden-atom LAN power envelope")
    ax.grid(True, alpha=0.25)
    ax.legend(frameon=False, fontsize=8)

    output_dir = Path(__file__).with_name("figures")
    output_dir.mkdir(exist_ok=True)
    pdf_path = output_dir / "sharp_visibility_lan_phase.pdf"
    png_path = output_dir / "sharp_visibility_lan_phase.png"
    fig.savefig(pdf_path, bbox_inches="tight")
    fig.savefig(png_path, dpi=220, bbox_inches="tight")
    plt.close(fig)

    payload = {
        "status": "PASS",
        "theta": theta,
        "delta": delta,
        "gamma": gamma,
        "uniform_sign_threshold": threshold,
        "first_kind_minimum_degree": next(n for n, value in zip(degrees, first) if value < threshold),
        "fourth_kind_minimum_degree": next(n for n, value in zip(degrees, fourth) if value < threshold),
        "fisher_information": fisher,
        "alpha": alpha,
    }
    (output_dir / "sharp_visibility_lan_phase.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print("sharp boundary figure: PASS")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
