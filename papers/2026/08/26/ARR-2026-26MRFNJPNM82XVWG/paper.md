# Irreducible Channel Mixing and Exponential Calibration Laws for Matrix-Polynomial and Linear-Phase MIMO FIR Filters

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2608.0029](https://www.ai.vixra.org/abs/2608.0029)  
**First submitted:** 2026-08-10T02:01:56+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2608.0029-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

Scalar Chebyshev filtering treats every vector in a block Krylov iterate with the same polynomial, while simultaneously diagonalizable matrix coefficients amount to independent scalar filters after a fixed channel rotation. We study the larger class of Hermitian matrix-polynomial filters under tangential pass constraints. Already at fixed channel dimension d=3, we construct rationally generated signatures with quantitative full-spark margin for which an irreducible symmetric filter has stopband leakage O(exp(-cN)). In contrast, every exactly calibrated symmetric coefficient family with any common nontrivial invariant channel subspace has leakage at least one; this comparator strictly contains the pairwise-commuting class and permits a fully noncommutative 2 by 2 block. A quantitative theorem covers approximately reducible filters by charging their sampled off-block coupling together with calibration error. The signature margin and the admissible combined error are both exp(-O(N)), not exp(-N^3). This exponential scale is unavoidable: for arbitrary pass nodes and signatures in the same separated bands, an explicit scalar binomial-tail polynomial has both pass error and stopband leakage at most exp(-2N/81). Thus constant-error separation is impossible, while the irreducible construction achieves the correct exponential scale class. An affine cosine substitution gives the same robust law for fixed-latency reciprocal linear-phase MIMO FIR filters. We also give an exact rational five-tap certificate with stopband norm at most 25/32 and prove that its advantage survives reducible calibration errors delta < 7/1920. A second exact-arithmetic certificate is calibrated from a public triaxial pump-vibration data set: it gives leakage below 0.96 versus one for every exactly calibrated reducible symmetric class, while its maximum directional error on six held-out records is 0.00385. In a frequency-domain-decomposition test on the frozen held-out cospectra, filtering rotates the leading modal direction by at most 0.222 degrees and changes its leading spectral ordinate by at most 2.4 × 10^-5 relatively. Numerical programs test the mechanism and expose an ordinary graph-denoising setting in which scalar Chebyshev filtering is instead preferable. Tangential matrix interpolation, MIMO filtering, scalar two-band approximation and convex FIR design are not claimed as new; the contribution is the fixed-order reducible/irreducible separation together with its two-sided calibration scale.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2608.0029v1.pdf) — 2026-08-10T02:01:56+00:00
