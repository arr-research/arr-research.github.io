"""Generate the exact-memory/border-memory phase figure."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.75), constrained_layout=True)

# Scalar two-band architecture: occupancies m and L-m.
L = 12
m = np.arange(1, L)
exact = np.maximum(m, L - m)
border = np.minimum(m, L - m)
ax = axes[0]
ax.fill_between(m, border, exact, color="#d97706", alpha=0.18,
                label="high-delay border interval")
ax.plot(m, exact, "o-", color="#9a3412", lw=1.8, ms=3.5,
        label=r"exact $d_{\min}$ (maximum)")
ax.plot(m, border, "s-", color="#0369a1", lw=1.8, ms=3.2,
        label=r"border $d_{\partial}$ (minimum)")
ax.set(xlabel=r"records in band 1, $L_1$", ylabel="McMillan degree",
       title="(a) Exact memory versus closure")
ax.set_xticks([1, 3, 6, 9, 11])
ax.set_yticks(range(0, 13, 2))
ax.legend(frameon=False, fontsize=7.5, loc="upper center")
ax.grid(alpha=0.2)

# Generic one-block projective law.
ax = axes[1]
Ls = np.arange(2, 17)
for r, color, marker in [(2, "#0f766e", "o"), (3, "#4338ca", "s"),
                         (4, "#7e22ce", "^"), (8, "#be123c", "D")]:
    degree = np.floor(Ls * (r - 1) / r).astype(int)
    ax.step(Ls, degree, where="mid", color=color, lw=1.5,
            marker=marker, ms=3, label=fr"$r={r}$")
ax.plot(Ls, Ls - 1, "--", color="0.45", lw=1,
        label=r"independent limit $L-1$")
ax.set(xlabel=r"number of records, $L$", ylabel="generic exact degree",
       title="(b) Projective-span law")
ax.set_xticks([2, 4, 8, 12, 16])
ax.set_yticks([0, 4, 8, 12, 15])
ax.legend(frameon=False, fontsize=7.5, ncol=2, loc="upper left")
ax.grid(alpha=0.2)

out = HERE / "figures" / "global_projective_phases.pdf"
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, bbox_inches="tight")
print(out)
