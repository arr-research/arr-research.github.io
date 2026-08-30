# Finite-Size Scaling of Petz Recovery Length in the TFIM: Threshold-dependent Operational Exponents from Exact Diagonalization

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2601.0040](https://www.ai.vixra.org/abs/2601.0040)  
**First submitted:** 2026-01-12T06:23:09+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2601.0040-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We study finite-size scaling of an operational recovery length extracted from Petz-map recovery in the transverse-field Ising chain. For a tripartition A-B-C with a collar B of width w, we define E_Petz(w) = -log F (squared Uhlmann fidelity), E_best(w) = min over w' <= w of E_Petz(w'), and the effective recovery distance d_eff(epsilon), with log-linear interpolation. Using exact diagonalization at hz = 0, beta = 12, |A| = 2 for N in {9, 10, 11, 12}, we analyze the peak height d_max(epsilon; N) = max over hx of d_eff in a censoring-free threshold regime, finding that the finite-window data are well summarized by descriptive power-law fits d_max(epsilon; N) ~ N^kappa(epsilon) with, e.g., kappa(3e-3) of about 0.44 and kappa(5e-3) of about 0.26, and a pseudocritical drift of the peak location with a threshold-dependent effective exponent nu_eff -- reported as operational quantities, not universal estimates. v2 adds (no v1 number is changed) two mandatory caveats, both quantified by a regenerable suite that reproduces v1's Table 1 exactly: (i) a |C|-shrinkage/growth confound -- the off-critical baseline d_eff(hx = 0.80; N) also grows with N at fixed thresholds, so the raw peak growth conflates critical physics with tripartition geometry; the cleaner object is the critical enhancement Delta(N) = peak - baseline, which still grows with N (e.g. 0.42 to 0.74 over N = 9, 10 at epsilon = 3e-3), so the critical signal survives baseline subtraction while kappa(epsilon) from raw peaks must be read as geometry-contaminated; (ii) functional-form indistinguishability -- over the accessible sub-octave in N, power-law, logarithmic and linear fits of the peak height have R^2 spreads below 0.01, and kappa itself shifts strongly with the fit window; the correct reading of kappa(epsilon) is a descriptive summary, not an established power law. Series positioning and a verification suite are included.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2601.0040v1.pdf) — 2026-01-12T06:23:09+00:00
- [v2](https://www.ai.vixra.org/pdf/2601.0040v2.pdf) — 2026-07-05T15:18:12+00:00
