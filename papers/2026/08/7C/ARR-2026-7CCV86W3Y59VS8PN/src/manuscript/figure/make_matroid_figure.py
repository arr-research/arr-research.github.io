"""Generate the single schematic figure for Paper 20.

The drawing is deterministic and deliberately schematic: panel A represents
linear dependence and matroid blocks, not metric Choi-state distances.
"""

from __future__ import annotations

import hashlib
import os
from datetime import datetime, timezone
from pathlib import Path

# Fix timestamps used by backends before importing Matplotlib.
os.environ.setdefault("SOURCE_DATE_EPOCH", "1786665600")

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


OUT_DIR = Path(__file__).resolve().parent
PNG_PATH = OUT_DIR / "paper20_matroidal_bayes_figure.png"
PDF_PATH = OUT_DIR / "paper20_matroidal_bayes_figure.pdf"
HASH_PATH = OUT_DIR / "SHA256SUMS.txt"

FIXED_TIME = datetime(2026, 8, 14, 0, 0, 0, tzinfo=timezone.utc)

COLORS = {
    "ink": "#17202A",
    "muted": "#5D6D7E",
    "phase": "#2E86AB",
    "phase_light": "#D9EEF7",
    "coloop": "#D1495B",
    "coloop_light": "#F8DDE1",
    "topd": "#7F8C8D",
    "matroid": "#1B998B",
    "grid": "#D5D8DC",
}


def configure() -> None:
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "axes.titlesize": 12,
            "axes.labelsize": 10,
            "axes.linewidth": 0.8,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
            "figure.dpi": 120,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.06,
            "pdf.compression": 9,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.hashsalt": "paper20-matroid-v1",
        }
    )


def panel_a(ax: plt.Axes) -> None:
    ax.set_xlim(-1.15, 3.15)
    ax.set_ylim(-1.15, 1.35)
    ax.axis("off")

    flat = FancyBboxPatch(
        (-1.0, -0.78),
        2.35,
        1.75,
        boxstyle="round,pad=0.08,rounding_size=0.16",
        facecolor=COLORS["phase_light"],
        edgecolor=COLORS["phase"],
        linewidth=1.5,
    )
    ax.add_patch(flat)
    ax.text(
        0.17,
        1.10,
        r"phase flat  $\mathrm{span}\{I,Z\}$  (rank 2)",
        ha="center",
        va="center",
        color=COLORS["phase"],
        weight="bold",
    )

    points = {
        r"$\phi_0$": (-0.62, -0.18),
        r"$\phi_1$": (0.78, -0.18),
        r"$\phi_2$": (0.08, 0.52),
    }
    for label, (x, y) in points.items():
        ax.scatter([x], [y], s=160, color=COLORS["phase"], zorder=3,
                   edgecolor="white", linewidth=1.1)
        ax.text(x, y - 0.25, label, ha="center", va="center",
                color=COLORS["ink"], weight="bold", fontsize=11)

    ax.plot(
        [points[r"$\phi_0$"][0], points[r"$\phi_2$"][0], points[r"$\phi_1$"][0]],
        [points[r"$\phi_0$"][1], points[r"$\phi_2$"][1], points[r"$\phi_1$"][1]],
        color=COLORS["phase"],
        alpha=0.45,
        linewidth=1.2,
        linestyle="--",
    )
    ax.text(
        0.17,
        -0.63,
        r"$\sum_j |\phi_j\rangle\!\langle\phi_j|=\frac{3}{2}P_{\rm diag}$",
        ha="center",
        color=COLORS["muted"],
        fontsize=9.4,
    )

    for label, y in ((r"$X$", 0.10),):
        ax.scatter([2.35], [y], s=175, marker="D", color=COLORS["coloop"],
                   edgecolor="white", linewidth=1.1, zorder=3)
        ax.text(2.62, y, label + "  coloop", ha="left", va="center",
                color=COLORS["ink"], weight="bold")

    ax.annotate(
        "independent of the phase flat",
        xy=(2.35, 0.08),
        xytext=(1.43, -0.93),
        arrowprops={"arrowstyle": "->", "color": COLORS["muted"], "lw": 1.0},
        color=COLORS["muted"],
        fontsize=8.7,
        ha="left",
    )
    ax.text(
        -1.05,
        -1.05,
        r"Matroid: $U_{2,3}\oplus U_{1,1}$",
        ha="left",
        va="center",
        color=COLORS["ink"],
        fontsize=9.5,
        weight="bold",
    )
    ax.set_title("A   Trine phase flat and a Pauli coloop", loc="left",
                 color=COLORS["ink"], weight="bold")


def panel_b(ax: plt.Axes) -> None:
    labels = [r"$\phi_0$", r"$\phi_1$", r"$\phi_2$", r"$X$"]
    priors = [0.30, 0.30, 0.30, 0.10]
    colors = [COLORS["phase"]] * 3 + [COLORS["coloop"]]
    x = list(range(len(labels)))

    bars = ax.bar(x, priors, width=0.68, color=colors, edgecolor="white", linewidth=0.8)
    ax.set_xticks(x, labels)
    # Reserve a clean header band for the two exact ceilings.
    ax.set_ylim(0, 0.48)
    ax.set_ylabel("prior probability")
    ax.set_title("B   Prior-weighted ceiling", loc="left", color=COLORS["ink"],
                 weight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color=COLORS["grid"], linewidth=0.7, alpha=0.75)
    ax.set_axisbelow(True)

    for bar, value in zip(bars, priors):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.009,
            f"{value:.2f}",
            ha="center",
            va="bottom",
            color=COLORS["ink"],
            fontsize=9,
        )

    ax.text(
        0.02,
        0.95,
        r"top-$D_E$ ($D_E=3$):  $\phi_0+\phi_1+\phi_2=\mathbf{0.90}$",
        transform=ax.transAxes,
        ha="left",
        va="top",
        color=COLORS["topd"],
        fontsize=10,
        bbox={"boxstyle": "round,pad=0.28", "fc": "white", "ec": COLORS["topd"],
              "lw": 1.1},
    )
    ax.text(
        0.02,
        0.82,
        r"matroid / GEN:  $\phi_0+\phi_1+X=\mathbf{0.70}$",
        transform=ax.transAxes,
        ha="left",
        va="top",
        color=COLORS["matroid"],
        fontsize=10,
        bbox={"boxstyle": "round,pad=0.28", "fc": "white", "ec": COLORS["matroid"],
              "lw": 1.3},
    )
def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    configure()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.55), gridspec_kw={"wspace": 0.28})
    panel_a(axes[0])
    panel_b(axes[1])
    fig.suptitle(
        "Support congestion sharpens dimension-only quantum discrimination bounds",
        x=0.5,
        y=1.01,
        color=COLORS["ink"],
        fontsize=13,
        weight="bold",
    )
    fig.text(
        0.5,
        -0.015,
        "Schematic: positions encode dependence blocks, not Choi-state distances.",
        ha="center",
        va="top",
        fontsize=8.5,
        color=COLORS["muted"],
    )

    png_metadata = {
        "Title": "Paper 20 matroidal Bayes ceiling",
        "Author": "Lluis Eriksson",
        "Description": "Schematic dependence flat and exact prior-bound comparison",
        "Software": "paper20-matroid-figure-v1",
        "Creation Time": "2026-08-14T00:00:00Z",
    }
    pdf_metadata = {
        "Title": "Paper 20 matroidal Bayes ceiling",
        "Author": "Lluis Eriksson",
        "Subject": "Schematic dependence flat and exact prior-bound comparison",
        "Keywords": "quantum process discrimination, Rado matroid, Bayes ceiling",
        "Creator": "paper20-matroid-figure-v1",
        "Producer": "paper20-matroid-figure-v1",
        "CreationDate": FIXED_TIME,
        "ModDate": FIXED_TIME,
    }
    fig.savefig(PNG_PATH, metadata=png_metadata)
    fig.savefig(PDF_PATH, metadata=pdf_metadata)
    plt.close(fig)

    lines = [f"{sha256(PNG_PATH)}  {PNG_PATH.name}", f"{sha256(PDF_PATH)}  {PDF_PATH.name}"]
    HASH_PATH.write_text("\n".join(lines) + "\n", encoding="ascii", newline="\n")
    print(f"wrote {PNG_PATH.name}, {PDF_PATH.name}, and {HASH_PATH.name}")


if __name__ == "__main__":
    main()
