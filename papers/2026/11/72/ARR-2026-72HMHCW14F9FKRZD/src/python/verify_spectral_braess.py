#!/usr/bin/env python3
"""
verify_spectral_braess.py
Exact verification, randomized testing, and 300-DPI figure generation for:
  "Exact Quantitative Laws for the Spectral Braess Paradox: Multiplicative Weyl Bounds,
   Degeneracy Immunity, and the Asymmetric Cheeger-Spectral Rift"
"""

from __future__ import annotations
import json
import math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "figures"
DATA_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)


def norm_lap_eigs(A: np.ndarray) -> np.ndarray:
    d = A.sum(axis=1)
    inv_sd = 1.0 / np.sqrt(d)
    L = np.eye(len(A)) - (inv_sd[:, None] * A * inv_sd[None, :])
    return np.sort(np.linalg.eigvalsh(L))


def psi_2x2(r: float, s: float, lam: float) -> float:
    a11 = (lam * r + 1.0) / (r + 1.0)
    a22 = (lam * s + 1.0) / (s + 1.0)
    a12 = -1.0 / math.sqrt((r + 1.0) * (s + 1.0))
    tr = a11 + a22
    det = a11 * a22 - a12 * a12
    return 0.5 * (tr - math.sqrt(max(0.0, tr * tr - 4.0 * det)))


def phi_reg_lb(r: int, lam: float) -> float:
    """Exact r-regular localization lower bound Phi_reg(r, lam) > r/(r+1) for lam in (0, 1)."""
    A_q = 1.0 - 0.5 * lam * r
    B_q = -2.0
    C_q = 1.0 - lam
    if abs(A_q) < 1e-12:
        t = C_q / 2.0
    else:
        t = (-B_q - math.sqrt(B_q * B_q - 4.0 * A_q * C_q)) / (2.0 * A_q)
    return (2.0 * r + r * r * t * t) / (2.0 * r + 2.0 + r * r * t * t)


def krm_kt_exact(r: int, m: int, t: int) -> float:
    q = r + t - 1
    c2 = m * q
    c1 = -m * (r + 2 * q)
    c0 = 2 * m * r + t * (t - 1)
    disc = c1 * c1 - 4 * c2 * c0
    return (-c1 - math.sqrt(disc)) / (2.0 * c2)


def k_r_m_plus_k_d_k_exact(r: int, m: int, d: int, k: int) -> float:
    """Exact spectral gap of K_{r, m} + K_{d, k} via the exact 4x4 symmetrized quotient matrix."""
    # Blocks: 0 = d centers (deg r+k), 1 = k leaves (deg r+d),
    #         2 = r left vertices (deg m), 3 = m-d-k free right vertices (deg r).
    m_free = m - d - k
    assert m_free > 0
    sizes = np.array([d, k, r, m_free], dtype=np.float64)
    degs = np.array([r + k, r + d, m, r], dtype=np.float64)
    # Edge counts between blocks (symmetric):
    E = np.array([
        [0.0,   d * k, d * r,      0.0],
        [d * k, 0.0,   k * r,      0.0],
        [d * r, k * r, 0.0,        r * m_free],
        [0.0,   0.0,   r * m_free, 0.0],
    ], dtype=np.float64)
    # Normalized adjacency on block-constant subspace: M_{ij} = E_{ij} / sqrt((sizes[i]*degs[i]) * (sizes[j]*degs[j]))
    vols = sizes * degs
    M = E / np.sqrt(np.outer(vols, vols))
    eigs = np.sort(1.0 - np.linalg.eigvalsh(M))
    # Also internal eigenvalues of blocks: within block 0, 1, 2, 3, any zero-sum vector has eigenvalue 1.
    return float(min(eigs[1], 1.0))


def clique_attach_exact(r: int, s: int, M: int) -> tuple[float, float]:
    """Exact lambda_2(G) and lambda_2(G+e) for disjoint clique attachment K_M + {u(deg r), v(deg s)}
    via the exact 5x5 symmetrized quotient matrix (valid for arbitrary large M!)."""
    # Blocks: 0={u} (1), 1={v} (1), 2=N(u) (r), 3=N(v) (s), 4=rest of K_M (M-r-s).
    rem = M - r - s
    assert rem > 0

    def solve(has_edge: bool) -> float:
        e_uv = 1.0 if has_edge else 0.0
        sizes = np.array([1.0, 1.0, float(r), float(s), float(rem)])
        degs = np.array([r + e_uv, s + e_uv, float(M), float(M), float(M - 1)])
        E = np.array([
            [0.0,  e_uv, float(r),        0.0,             0.0],
            [e_uv, 0.0,  0.0,             float(s),        0.0],
            [float(r), 0.0, float(r*(r-1)), float(r*s),    float(r*rem)],
            [0.0,  float(s), float(r*s),  float(s*(s-1)),  float(s*rem)],
            [0.0,  0.0,  float(r*rem),    float(s*rem),    float(rem*(rem-1))],
        ])
        vols = sizes * degs
        M_mat = E / np.sqrt(np.outer(vols, vols))
        eigs = np.sort(1.0 - np.linalg.eigvalsh(M_mat))
        # Internal eigenvalues inside blocks 2, 3, 4 are >= 1 + 1/M > 1
        return float(eigs[1])

    return solve(False), solve(True)


def degeneracy_of_graph(A: np.ndarray) -> int:
    """Exact degeneracy (k-core number) of simple undirected graph A."""
    n = len(A)
    deg = A.sum(axis=1).astype(int).tolist()
    alive = [True] * n
    max_min_deg = 0
    for _ in range(n):
        best_v = min((v for v in range(n) if alive[v]), key=lambda v: deg[v])
        max_min_deg = max(max_min_deg, deg[best_v])
        alive[best_v] = False
        for u in range(n):
            if alive[u] and A[best_v, u] > 0:
                deg[u] -= 1
    return max_min_deg


def main() -> None:
    report: dict = {}

    # 1. Randomized verification of Theorem 1 (Weyl multiplicative), Theorem 2 (Degeneracy Immunity),
    #    and Theorem 3 (Psi(r, s; lambda)) across 2,500 random connected graphs + subgraphs H!
    rng = np.random.default_rng(20261128)
    min_weyl_l2 = 1e9
    min_weyl_lk = 1e9
    min_weyl_abs = 1e9
    min_degen_ratio = 1e9
    min_psi_slack = 1e9

    for _ in range(2500):
        n = int(rng.integers(5, 13))
        A = np.zeros((n, n))
        for i in range(1, n):
            p = int(rng.integers(0, i))
            A[i, p] = A[p, i] = 1.0
        for _ in range(int(rng.integers(0, n))):
            u, v = int(rng.integers(0, n)), int(rng.integers(0, n))
            if u != v:
                A[u, v] = A[v, u] = 1.0
        non_edges = [(u, v) for u in range(n) for v in range(u + 1, n) if A[u, v] == 0]
        if not non_edges:
            continue
        k = int(rng.integers(1, min(len(non_edges), 7) + 1))
        chosen = rng.choice(len(non_edges), size=k, replace=False)
        H = np.zeros((n, n))
        for idx in chosen:
            u, v = non_edges[idx]
            H[u, v] = H[v, u] = 1.0

        d_vec = A.sum(axis=1)
        r_min = int(np.min(d_vec))
        inv_sd = 1.0 / np.sqrt(d_vec)
        rho_tilde = float(np.max(np.abs(np.linalg.eigvalsh(inv_sd[:, None] * H * inv_sd[None, :]))))
        weyl_fac = 1.0 / (1.0 + rho_tilde)

        e0 = norm_lap_eigs(A)
        e1 = norm_lap_eigs(A + H)
        if e0[1] <= 1.0 + 1e-9:
            min_weyl_l2 = min(min_weyl_l2, e1[1] / (weyl_fac * e0[1]))
            d_H = degeneracy_of_graph(H)
            if d_H >= 1:
                deg_lb = 1.0 - math.sqrt(d_H / (d_H + r_min))
                min_degen_ratio = min(min_degen_ratio, (e1[1] / e0[1]) / deg_lb)
        for j in range(1, n):
            if e0[j] <= 1.0 + 1e-9:
                min_weyl_lk = min(min_weyl_lk, e1[j] / (weyl_fac * e0[j]))
        gstar0 = min(e0[1], 2.0 - e0[-1])
        gstar1 = min(e1[1], 2.0 - e1[-1])
        if gstar0 > 1e-9 and gstar0 <= 1.0 + 1e-9:
            min_weyl_abs = min(min_weyl_abs, gstar1 / (weyl_fac * gstar0))
        if k == 1:
            u, v = non_edges[chosen[0]]
            lb = psi_2x2(d_vec[u], d_vec[v], float(e0[1]))
            min_psi_slack = min(min_psi_slack, float(e1[1]) - lb)

    assert min_weyl_l2 >= 1.0 - 1e-9
    assert min_weyl_lk >= 1.0 - 1e-9
    assert min_weyl_abs >= 1.0 - 1e-9
    assert min_degen_ratio >= 1.0 - 1e-9
    assert min_psi_slack >= -1e-9

    report["empirical_verification"] = {
        "trials": 2500,
        "min_weyl_l2_ratio": min_weyl_l2,
        "min_weyl_all_j_ratio": min_weyl_lk,
        "min_weyl_abs_gap_ratio": min_weyl_abs,
        "min_degeneracy_ratio": min_degen_ratio,
        "min_psi_2x2_slack": min_psi_slack,
    }

    # 2. Exact closed-form verification for K_{r, m} + K_t and K_{r, r} + e
    krm_kt_table = []
    for r, t, m in [(1, 2, 10), (1, 3, 20), (1, 4, 30), (2, 2, 20), (2, 4, 30), (3, 3, 30)]:
        n = r + m
        A = np.zeros((n, n))
        for i in range(r):
            for j in range(r, n):
                A[i, j] = A[j, i] = 1.0
        for i in range(r, r + t):
            for j in range(i + 1, r + t):
                A[i, j] = A[j, i] = 1.0
        lam_num = float(norm_lap_eigs(A)[1])
        lam_ex = krm_kt_exact(r, m, t)
        assert abs(lam_num - lam_ex) < 1e-12
        krm_kt_table.append({
            "r": r, "t": t, "m": m,
            "lam_exact": lam_ex,
            "asymptotic_floor": r / (r + t - 1.0),
        })
    report["krm_plus_kt"] = krm_kt_table

    krr_table = []
    for r in range(2, 16):
        lam_ex = krm_kt_exact(r, r, 2)
        krr_table.append({"r": r, "lam_krr_plus_e": lam_ex, "r_over_r1": r / (r + 1.0)})
    assert abs(krm_kt_exact(4, 4, 2) - (14.0 - math.sqrt(26.0)) / 10.0) < 1e-12
    report["krr_plus_e"] = {
        "global_min_r": 4,
        "global_min_val": (14.0 - math.sqrt(26.0)) / 10.0,
        "table": krr_table,
    }

    # 3. Asymmetric Cheeger-Spectral Rift via exact 5x5 quotient matrix (verified vs full matrix at M=40)
    l0_full, l1_full = clique_attach_exact(1, 5, 40)
    # Cross-check quotient matrix against explicit 42x42 adjacency matrix!
    A42 = np.ones((42, 42)) - np.eye(42)
    A42[40, :] = A42[:, 40] = 0; A42[41, :] = A42[:, 41] = 0
    A42[40, 0] = A42[0, 40] = 1.0
    for i in range(1, 6):
        A42[41, i] = A42[i, 41] = 1.0
    assert abs(float(norm_lap_eigs(A42)[1]) - l0_full) < 1e-12
    A42[40, 41] = A42[41, 40] = 1.0
    assert abs(float(norm_lap_eigs(A42)[1]) - l1_full) < 1e-12

    rift_table = []
    for r, s in [(1, 1), (1, 2), (1, 4), (1, 8), (1, 20), (2, 6), (3, 10)]:
        l0, l1 = clique_attach_exact(r, s, 100000)
        psi1 = 1.0 - 1.0 / math.sqrt((r + 1.0) * (s + 1.0))
        cheeg = (r + s) / (r + s + 2.0)
        geom = math.sqrt(r * s) / (math.sqrt(r * s) + 1.0)
        assert abs(l0 - 1.0) < 0.01 and abs(l1 - psi1) < 0.005
        rift_table.append({
            "r": r, "s": s,
            "lam0_M1e5": l0, "lam1_M1e5": l1, "ratio_M1e5": l1 / l0,
            "min_deg_floor": min(r, s) / (min(r, s) + 1.0),
            "geom_weyl_floor": geom,
            "psi_1": psi1,
            "cheeger_floor": cheeg,
        })
    report["asymmetric_rift"] = rift_table

    # 4. Degeneracy Immunity exact tightness via 4x4 quotient matrix (cross-checked vs full matrix!)
    A_chk = np.zeros((1 + 30, 1 + 30))
    for j in range(1, 31):
        A_chk[0, j] = A_chk[j, 0] = 1.0
    for j in range(2, 10):
        A_chk[1, j] = A_chk[j, 1] = 1.0
    assert abs(float(norm_lap_eigs(A_chk)[1]) - k_r_m_plus_k_d_k_exact(1, 30, 1, 8)) < 1e-12

    degen_table = []
    for r, d in [(1, 1), (1, 2), (1, 3), (1, 5), (2, 1), (2, 2), (3, 2)]:
        val = k_r_m_plus_k_d_k_exact(r, 1000000, d, 10000)
        floor = 1.0 - math.sqrt(d / (d + r))
        assert abs(val - floor) < 0.006
        degen_table.append({"r": r, "d": d, "floor": floor, "witness_val": val})
    report["degeneracy_immunity"] = degen_table

    # 5. Regular-graph localization obstruction table + Complete equipartite K_{m,...,m}+e check
    reg_table = []
    for r in [2, 3, 4, 5, 6, 8, 10]:
        lam_ab = 1.0 - 2.0 * math.sqrt(r - 1.0) / r
        reg_table.append({
            "r": r,
            "naive_floor": r / (r + 1.0),
            "lam_alon_boppana": lam_ab,
            "phi_reg_at_ab": phi_reg_lb(r, lam_ab) if lam_ab > 0 else 0.8,
            "phi_reg_at_01": phi_reg_lb(r, 0.1),
            "krr_plus_e": krm_kt_exact(r, r, 2),
        })
    report["regular_localization"] = reg_table

    equipartite_table = []
    for k_parts in [2, 3, 4, 5]:
        for m_sz in [2, 3, 4, 5]:
            r_eq = (k_parts - 1) * m_sz
            n_eq = k_parts * m_sz
            A_eq = np.ones((n_eq, n_eq)) - np.eye(n_eq)
            for blk in range(k_parts):
                A_eq[blk * m_sz:(blk + 1) * m_sz, blk * m_sz:(blk + 1) * m_sz] = 0.0
            e0_eq = norm_lap_eigs(A_eq)
            assert abs(float(e0_eq[1]) - 1.0) < 1e-12
            A_eq2 = A_eq.copy()
            A_eq2[0, 1] = A_eq2[1, 0] = 1.0
            lam2_eq = float(norm_lap_eigs(A_eq2)[1])
            if m_sz == 2:
                lam2_exact = 1.0
            else:
                qa = r_eq * (r_eq + 1)
                qb = -(r_eq * r_eq + 2 * (r_eq + 1) + (r_eq + 1) * (r_eq + m_sz - 2))
                qc = 2 * (r_eq + 1) + r_eq * (r_eq + m_sz - 2)
                lam2_exact = (-qb - math.sqrt(qb * qb - 4 * qa * qc)) / (2 * qa)
            assert abs(lam2_eq - lam2_exact) < 1e-12
            krr_val = krm_kt_exact(r_eq, r_eq, 2)
            if k_parts >= 3:
                assert lam2_eq > krr_val + 1e-12
            equipartite_table.append({
                "k": k_parts, "m": m_sz, "r": r_eq,
                "lam2_equipartite_plus_e": lam2_eq,
                "lam2_krr_plus_e": krr_val,
                "strictly_above_krr": lam2_eq > krr_val + 1e-12,
            })
    report["complete_equipartite_regular"] = equipartite_table

    with open(DATA_DIR / "verification_summary.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    # -----------------------------------------------------------------------
    # Generate 3 bespoke 300-DPI journal-grade figures
    # -----------------------------------------------------------------------
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 10,
        "axes.labelsize": 10.8,
        "axes.titlesize": 11.2,
        "legend.fontsize": 8.6,
        "figure.dpi": 300,
    })

    # Figure 1: Budget-k Optimal Braess Saboteurs vs. Degeneracy Immunity (r = 1)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.6, 4.2))
    ks = np.arange(1, 37)
    y_stanley = 2.0 / (1.0 + np.sqrt(1.0 + 8.0 * ks))
    y_nosal = 1.0 / (1.0 + np.sqrt(ks))
    y_forest = np.full_like(ks, 1.0 - 1.0 / math.sqrt(2.0), dtype=float)
    y_star = 1.0 - np.sqrt(ks / (2.0 * (ks + 1.0)))

    ax1.plot(ks, y_stanley, "-", color="#b2182b", lw=2.0, label=r"General $k$-edge floor $\frac{2}{1+\sqrt{1+8k}}$")
    ax1.plot(ks, y_nosal, "--", color="#2166ac", lw=1.8, label=r"Triangle-free floor $\frac{1}{1+\sqrt{k}}$")
    ax1.plot(ks, y_star, "-.", color="#1b7837", lw=1.8, label=r"Star $K_{1,k}$ exact limit $1 - \sqrt{\frac{k}{2(k+1)}}$")
    ax1.axhline(1.0 - 1.0 / math.sqrt(2.0), color="#1b7837", ls=":", lw=1.3,
                label=r"Forest immunity $1 - \frac{1}{\sqrt{2}} \approx 0.2929$")
    # Plot exact sharp points K_t and K_{a,a}
    t_vals = [2, 3, 4, 5, 6, 7, 8, 9]
    ax1.scatter([t * (t - 1) // 2 for t in t_vals], [1.0 / t for t in t_vals],
                color="#b2182b", s=34, zorder=5, label=r"Sharp cliques $K_t$ ($1/t$)")
    a_vals = [2, 3, 4, 5, 6]
    ax1.scatter([a * a for a in a_vals], [1.0 / (1.0 + a) for a in a_vals],
                color="#2166ac", marker="s", s=32, zorder=5, label=r"Sharp $K_{a,a}$ ($1/(1+a)$)")
    ax1.set_xlabel(r"Number of added edges $k = |E(H)|$")
    ax1.set_ylabel(r"Sharp Braess ratio $\lambda_2(G+H) / \lambda_2(G)$ ($\delta(G)=1$)")
    ax1.set_title(r"(a) Collapse of Cliques vs. Forest Immunity")
    ax1.set_xlim(0.5, 36.5)
    ax1.set_ylim(0.08, 0.56)
    ax1.grid(True, alpha=0.25)
    ax1.legend(loc="upper right", frameon=True, framealpha=0.94, fontsize=7.9)

    ds = np.arange(1, 11)
    for r_val, col, mk in [(1, "#b2182b", "o"), (2, "#2166ac", "s"), (3, "#1b7837", "^"), (5, "#762a83", "D")]:
        vals = 1.0 - np.sqrt(ds / (ds + r_val))
        ax2.plot(ds, vals, f"{mk}-", color=col, lw=1.7, ms=5.2, label=rf"$\delta(G) \geq {r_val}$")
    ax2.annotate(r"Forests ($d=1$): $1-\frac{1}{\sqrt{2}}$", xy=(1, 1 - 1/math.sqrt(2)),
                 xytext=(1.6, 0.03), arrowprops=dict(arrowstyle="->", color="#222222", lw=0.9), fontsize=8.3)
    ax2.annotate(r"Planar ($d \leq 5$): $\geq 1-\sqrt{\frac{5}{6}}$", xy=(5, 1 - math.sqrt(5/6)),
                 xytext=(5.7, 0.015), arrowprops=dict(arrowstyle="->", color="#222222", lw=0.9), fontsize=8.3)
    ax2.set_xlabel(r"Degeneracy $d$ of added subgraph $H$")
    ax2.set_ylabel(r"Exact immunity floor $1 - \sqrt{d/(d+r)}$")
    ax2.set_title(r"(b) Sharp Degeneracy Immunity Across $\delta(G) \geq r$")
    ax2.set_xlim(0.6, 10.4)
    ax2.set_ylim(0.0, 0.68)
    ax2.grid(True, alpha=0.25)
    ax2.legend(loc="upper right", frameon=True, framealpha=0.94)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig1_saboteurs_and_degeneracy.png", dpi=300)
    plt.close(fig)

    # Figure 2: The Asymmetric Cheeger-Spectral Rift (r = 1, s = 1..20)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.6, 4.2))
    s_grid = np.arange(1, 21)
    y_min = np.full_like(s_grid, 0.5, dtype=float)
    y_geom = np.sqrt(s_grid) / (np.sqrt(s_grid) + 1.0)
    y_psi1 = 1.0 - 1.0 / np.sqrt(2.0 * (s_grid + 1.0))
    y_cheeg = (1.0 + s_grid) / (3.0 + s_grid)
    y_wit = [clique_attach_exact(1, int(s), 100000)[1] / clique_attach_exact(1, int(s), 100000)[0] for s in s_grid]

    ax1.plot(s_grid, y_cheeg, "--", color="#1b7837", lw=2.0, label=r"Cheeger floor $\frac{1+s}{3+s}$")
    ax1.plot(s_grid, y_psi1, "-", color="#b2182b", lw=2.0, label=r"Spectral floor $\Psi(1,s;1)=1-\frac{1}{\sqrt{2(s+1)}}$")
    ax1.scatter(s_grid[::2], y_wit[::2], color="#b2182b", s=28, zorder=5, label=r"Witness $G_{1,s,10^5}$")
    ax1.plot(s_grid, y_geom, "-.", color="#2166ac", lw=1.6, label=r"Weyl geometric $\frac{\sqrt{s}}{\sqrt{s}+1}$")
    ax1.plot(s_grid, y_min, ":", color="#555555", lw=1.4, label=r"Min-degree floor $\frac{1}{2}$")
    ax1.fill_between(s_grid, y_psi1, y_cheeg, color="#b2182b", alpha=0.10, label="Cheeger–spectral rift")
    ax1.set_xlabel(r"Degree $s = d_G(v)$ (with $r = d_G(u) = 1$)")
    ax1.set_ylabel(r"Single-edge Braess ratio ($\lambda_2(G) \to 1$)")
    ax1.set_title("(a) Strict Four-Level Hierarchy & Cheeger–Spectral Rift")
    ax1.set_xlim(0.7, 20.3)
    ax1.set_ylim(0.46, 0.96)
    ax1.grid(True, alpha=0.25)
    ax1.legend(loc="lower right", frameon=True, framealpha=0.94, fontsize=8.0)

    lam_grid = np.linspace(0.01, 1.0, 200)
    for s_val, col in [(1, "#555555"), (3, "#2166ac"), (8, "#762a83"), (20, "#b2182b")]:
        ratios = [psi_2x2(1.0, float(s_val), float(l)) / l for l in lam_grid]
        ax2.plot(lam_grid, ratios, "-", color=col, lw=1.9, label=rf"$r=1, s={s_val}$ (Cheeger $\frac{{{1+s_val}}}{{{3+s_val}}}={((1+s_val)/(3+s_val)):.3f}$)")
        ax2.scatter([0.01], [(1 + s_val) / (3 + s_val)], color=col, s=28, zorder=5)
    ax2.set_xlabel(r"Baseline spectral gap $\lambda = \lambda_2(G)$")
    ax2.set_ylabel(r"Normalized floor $\Psi(1, s; \lambda) / \lambda$")
    ax2.set_title(r"(b) Reconciliation with Cheeger as $\lambda \to 0^+$")
    ax2.set_xlim(0.0, 1.02)
    ax2.set_ylim(0.48, 0.95)
    ax2.grid(True, alpha=0.25)
    ax2.legend(loc="lower left", frameon=True, framealpha=0.94, fontsize=8.0)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig2_cheeger_spectral_rift.png", dpi=300)
    plt.close(fig)

    # Figure 3: Regular-Graph Localization Obstruction & K_{r,r} + e Global Minimum at r = 4
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.6, 4.1))
    rs = np.arange(2, 16)
    y_naive = rs / (rs + 1.0)
    y_krr = [krm_kt_exact(int(r), int(r), 2) for r in rs]
    y_ab = [phi_reg_lb(int(r), 1.0 - 2.0 * math.sqrt(r - 1.0) / r) if r >= 3 else 0.8 for r in rs]
    ax1.plot(rs, y_krr, "o-", color="#b2182b", lw=1.9, ms=5.5, label=r"Exact $K_{r,r}+e$ ($\lambda_2(G)=1$)")
    ax1.plot(rs, y_ab, "s-", color="#2166ac", lw=1.8, ms=5.0, label=r"Localization bound $\Phi_{\mathrm{reg}}(r, \lambda_{\mathrm{AB}})$")
    ax1.plot(rs, y_naive, "--", color="#555555", lw=1.5, label=r"Unrestricted floor $r/(r+1)$")
    ax1.annotate(r"Global min $r=4$: $\frac{14-\sqrt{26}}{10} \approx 0.8901$",
                 xy=(4, y_krr[2]), xytext=(6.0, 0.805),
                 arrowprops=dict(arrowstyle="->", color="#222222", lw=0.9), fontsize=8.4)
    ax1.set_xlabel(r"Regularity degree $r$")
    ax1.set_ylabel(r"Single-edge Braess ratio $\lambda_2(G+e) / \lambda_2(G)$")
    ax1.set_title(r"(a) Regular-Graph Obstruction vs. $r/(r+1)$")
    ax1.set_xlim(1.6, 15.4)
    ax1.set_ylim(0.64, 1.015)
    ax1.grid(True, alpha=0.25)
    ax1.legend(loc="lower right", frameon=True, framealpha=0.94, fontsize=8.3)

    lam_g = np.linspace(0.005, 0.999, 200)
    for r_val, col in [(2, "#1b7837"), (3, "#2166ac"), (4, "#762a83"), (6, "#b2182b")]:
        vals = [phi_reg_lb(r_val, float(l)) for l in lam_g]
        ax2.plot(lam_g, vals, "-", color=col, lw=1.8, label=rf"$r={r_val}$ (floor $\frac{{{r_val}}}{{{r_val+1}}}={r_val/(r_val+1):.3f}$)")
        lam_ab = 1.0 - 2.0 * math.sqrt(r_val - 1.0) / r_val
        if lam_ab > 0:
            ax2.scatter([lam_ab], [phi_reg_lb(r_val, lam_ab)], color=col, s=36, zorder=5)
    ax2.set_xlabel(r"Baseline spectral gap $\lambda = \lambda_2(G)$")
    ax2.set_ylabel(r"Localization lower bound $\Phi_{\mathrm{reg}}(r, \lambda)$")
    ax2.set_title(r"(b) $\Phi_{\mathrm{reg}}(r, \lambda)$ (dots mark Alon–Boppana $\lambda_{\mathrm{AB}}$)")
    ax2.set_xlim(0.0, 1.02)
    ax2.set_ylim(0.56, 1.00)
    ax2.grid(True, alpha=0.25)
    ax2.legend(loc="lower left", ncol=2, frameon=True, framealpha=0.95, fontsize=7.9)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig3_regular_localization.png", dpi=300)
    plt.close(fig)

    print("VERIFY_SPECTRAL_BRAESS_OK")
    print(f"  2500-trial mins: weyl_l2={min_weyl_l2:.8f}, weyl_lk={min_weyl_lk:.8f}, weyl_abs={min_weyl_abs:.8f}, degen={min_degen_ratio:.8f}, psi_slack={min_psi_slack:.8f}")
    print(f"  K_{4,4}+e exact min = {(14-math.sqrt(26))/10:.10f}")


if __name__ == "__main__":
    main()
