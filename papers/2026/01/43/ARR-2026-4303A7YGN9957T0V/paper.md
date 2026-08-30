# Emergent Information Distance from Petz Recovery: Temperature and Perturbation Dependence in TFIM Exact Diagonalization

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2601.0042](https://www.ai.vixra.org/abs/2601.0042)  
**First submitted:** 2026-01-11T14:41:55+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2601.0042-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We define an operational notion of effective distance from approximate quantum state recovery. Given a tripartition A-B-C with B a collar of width w separating A from C, we compute a Petz recovery reconstruction error E_Petz(w) = -log F(rho_ABC, rho_Petz(w)) (squared Uhlmann fidelity) and define an emergent distance d_eff(epsilon) as the minimal collar width such that the best-achieved error up to w falls below a threshold epsilon. Using exact diagonalization for the transverse-field Ising chain at N = 11, hx = 1.05, |A| = 2, we find that d_eff(1e-3) grows strongly with inverse temperature beta in the unperturbed case (hz = 0), from 1.00 at beta = 0.5 to 3.57 at beta = 5.0, while remaining near-minimal in the longitudinally perturbed case (hz = 0.5), close to 1.0 across the same range. We also introduce a discrete curvature diagnostic based on second differences of log E_Petz(w) on a pre-floor window, reported only when identifiable. v2 (no v1 number is changed): the garbled reproducibility paragraph of v1 is replaced by a real, regenerable verification suite, which reproduces the beta-sweep to two decimals already at N = 9 (d_eff = 1.00, 1.00, 1.51, 2.11, 2.82, 3.55 vs 3.57 at N = 11; mu_prefloor endpoints 8.44 to 1.35 vs 1.33; PSD-projection sensitivity 3.3e-8 vs about 3e-8) -- independently confirming the finite-size robustness of the appendix; the mild |C|-shrinkage caveat is stated with cross-references to its quantified analysis in the companions; and series positioning is added.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2601.0042v1.pdf) — 2026-01-11T14:41:55+00:00
- [v2](https://www.ai.vixra.org/pdf/2601.0042v2.pdf) — 2026-07-05T15:57:50+00:00
