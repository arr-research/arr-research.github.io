# DLR-Uniform Log-Sobolev Inequality and Mass Gap for Lattice Yang—Mills at Weak Coupling: a Conditional and Windowed Reduction

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2602.0053](https://www.ai.vixra.org/abs/2602.0053)  
**First submitted:** 2026-02-12T19:11:43+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2602.0053-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We study the passage from the uniform log-Sobolev inequality (LSI) on periodic tori, developed in the companion series, to a DLR-uniform LSI for the conditional Gibbs specification of SU(N_c) lattice Yang-Mills in d >= 3 at weak coupling (beta >= beta_0), and from there to a mass gap via Stroock-Zegarlinski and Osterwalder-Seiler reflection positivity. Version 2 corrects the logical status of the main results after a quantitative audit (companion numerical suite included; Appendix A). (i) The fiber assembly (Lemma 3.5) assumes the block Dobrushin condition delta < 1, which v1's own Remark 3.6 left unverified; the printed influence bound c_ij <= tanh(beta n_bd/2) tends to 1 as beta -> infinity and yields delta < 1 only for beta <~ 10^(-2) (d=3) or beta <~ 10^(-3) (d=4) — the opposite of the weak-coupling regime. A rotor exhibit shows the genuine worst-case block influence also tends to 1, so no worst-case criterion can close the gap: the condition is now the explicit hypothesis (H-DOB-blk), and v1's claim of removing the Dobrushin-type Assumption 6.3 of [14] is withdrawn — the present paper reduces that assumption to (H-DOB-blk). (ii) The quantitative absorption in Proposition 4.3 inherits hypothesis (H-P0) of ai.viXra:2602.0052(v2): under the polylog penalty floor p0(g) >= c_0 |log g|^(1+epsilon_0) the required inequality e^(-c p0(g_k)) <= C L_RG^(-(d-1)k) fails already at k = O(1). (iii) The proof assumes g_k <= gamma_0 for all k <= n_max ~ log_LRG diam(Lambda'); with the corrected asymptotic-freedom flow of the series erratum this holds only on the volume window log_LRG diam(Lambda') <= k*(beta), i.e. diam(Lambda') <= e^(C/g^2+O(1)). Theorems 1.1-1.2 are therefore restated as windowed and conditional on (H-DOB-blk) and (H-P0). What survives unconditionally — and is validated numerically — is the boundary-uniformity mechanism itself: the per-plaquette oscillation and gradient bounds (Lemma 3.1; sharp for N_c=2), the "frozen = slow" reduction (Lemma 3.2), the refined dynamical large-field event, the energy-penalty identity ||U-1||_HS^2 = 2N_c(1 - Re tr U / N_c), the TV <= tanh(osc/4) lemma with its two-point equality case, and the Bakry-Emery constant N_c/4 in the = -2 tr(XY) convention. The contribution of the paper is thus retagged: a boundary-uniform reduction of the DLR-LSI and the mass gap to (H-DOB-blk)+(H-P0) within the volume window — not an unconditional mass gap.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2602.0053v1.pdf) — 2026-02-12T19:11:43+00:00
- [v2](https://www.ai.vixra.org/pdf/2602.0053v2.pdf) — 2026-07-06T10:47:13+00:00
