"""Generate the vector figure for the semiclassical coherent-orbit paper."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parent
data_path = ROOT / "semiclassical_coherent_rdf_verification.json"
if not data_path.exists():
    data_path = ROOT / "replay" / "semiclassical_coherent_rdf_verification.json"
if not data_path.exists():
    data_path = ROOT.parent / "replay" / "semiclassical_coherent_rdf_verification.json"
DATA = json.loads(data_path.read_text(encoding="utf-8"))
OUT = ROOT / "paper" / "figures"
if (ROOT / "source").is_dir():
    OUT = ROOT / "source" / "figures"
if (ROOT.parent / "replay").is_dir():
    OUT = ROOT / "figures"
OUT.mkdir(parents=True, exist_ok=True)


def boundary(x: np.ndarray, a: float) -> np.ndarray:
    constant = np.log(2.0 * np.sqrt(np.pi))
    return np.where(
        x <= a,
        a * np.log(a / x) + constant - a,
        constant - x,
    )


plt.rcParams.update({
    "font.size": 9,
    "axes.labelsize": 9,
    "axes.titlesize": 10,
    "legend.fontsize": 8,
    "font.family": "serif",
})

fig, axes = plt.subplots(1, 2, figsize=(7.15, 3.05), constrained_layout=True)

ax = axes[0]
colors = ["#2455a4", "#b4472d", "#247a58"]
for a, color in zip((1.5, 2.5, 4.5), colors):
    x = np.linspace(0.18 * a, 2.15 * a, 500)
    ax.plot(x / a, boundary(x, a), color=color, lw=1.8, label=rf"$a={a:g}$")
    ax.plot([1.0], [np.log(2.0 * np.sqrt(np.pi)) - a], "o", color=color, ms=3.8)
ax.axvline(1.0, color="0.45", lw=0.8, ls="--")
ax.set_xlabel(r"boundary coordinate $x/a=D\log d_N/a$")
ax.set_ylabel(r"centered rate $H_a(x)$ (nats)")
ax.set_title("Universal matched boundary profiles")
ax.legend(frameon=False, loc="best")
ax.grid(alpha=0.18, lw=0.5)

ax = axes[1]
markers = ["o", "s"]
for family, color, marker in zip(DATA["families"], colors[:2], markers):
    rows = family["rows"]
    ell = np.log([row["hilbert_dimension"] for row in rows])
    contact_error = np.abs([row["contact_t_error"] for row in rows])
    slope_error = np.abs([row["slope_error"] for row in rows])
    short = family["family"].split(",")[0]
    ax.loglog(ell, contact_error, marker=marker, color=color, lw=1.4,
              label=short + r" $|t_c-t_{\rm asy}|$")
    ax.loglog(ell, slope_error, marker=marker, color=color, lw=1.1, ls="--",
              label=short + r" $|\rho_c-\rho_{\rm asy}|$")
ax.set_xlabel(r"$ell_N=\log d_N$")
ax.set_ylabel("absolute error (nats)")
ax.set_title("Exact Weyl-series contact diagnostics")
ax.legend(frameon=False, loc="best", handlelength=2.2)
ax.grid(alpha=0.18, which="both", lw=0.5)

for suffix in ("pdf", "png"):
    fig.savefig(OUT / f"semiclassical_universality.{suffix}", dpi=240)
print(f"PASS: wrote vector and raster figures to {OUT}")
