# Refix-Path Bell Transport on Ibm Quantum Hardware: High-Resolution Replication, Comparative Geometry Dependence, and Stress Tests of a Static—Dynamic Link

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2512.0105](https://www.ai.vixra.org/abs/2512.0105)  
**First submitted:** 2025-12-31T20:11:52+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2512.0105-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

This note reports a replicated, high-resolution Bell-transport experiment on IBM Quantum superconducting hardware using a prefix-path protocol that controls spatial heterogeneity across transport lengths. A single physical qubit chain is fixed and increasing transport length L is realized via prefixes of that chain, so that L changes depth while keeping qubits nested rather than switching to different qubit subsets. We reconstruct the Bell-state fidelity F(L) from Pauli correlators E_XX, E_YY, E_ZZ and apply a minimal drift correction using interleaved full-Phi+ control blocks. Beyond a single-chain sweep, we perform a comparative geometry test across three disjoint physical chains on the same backend: the effective decay scale differs significantly across chains (with >10 sigma separations under fit uncertainties), providing operational evidence that the transport decay scale is geometry-dependent under fixed compilation constraints. Motivated by the Rate Inheritance Principle (RIP) framing, we also investigate whether a phase-sensitive static correlation metric measured on idle chains can predict dynamical transport decay. A curated three-chain set exhibits an ordering agreement between a static Ramsey-X nearest-neighbor covariance metric and the transport decay scales mu measured on the same chains; however, scale-up studies over n=18 randomly sampled chains and a preregistered out-of-sample prediction test do not show statistically significant monotone association under permutation testing. We interpret the static—dynamic ordering agreement as conditional and geometry-specific, while the geometry dependence of dynamical decay is robust. v2 adds: a fitting-choice caveat with a synthetically validated re-analysis pipeline for future variant tables, a power bound showing the negative preregistered test excludes a strong device-wide static—dynamic law (from published quantities alone), an all-lengths rate proxy specification, small-sample and estimator caveats, context references, and an offline re-analysis script with documented schema for a future data revision.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2512.0105v1.pdf) — 2025-12-31T20:11:52+00:00
- [v2](https://www.ai.vixra.org/pdf/2512.0105v2.pdf) — 2026-07-05T07:16:09+00:00
