# Algebraic Entropy and Conditional Mutual Information in a Tiny Gauge-Invariant Truncated Hilbert Space: A Reproducible Toy-Model Study with Effective Mixing Hamiltonians

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2601.0115](https://www.ai.vixra.org/abs/2601.0115)  
**First submitted:** 2026-01-28T08:43:53+00:00 (source displays no timezone)  
**Latest declared source version:** v3  
**ARR mirror:** [v3 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2601.0115-v3.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We present a reproducible pipeline to compute region algebraic entropies and conditional mutual informations (CMI) in a tiny truncated Hilbert space (here dim = 8) indexed by discrete fusion-like descriptors desc = (x, mu) on L = 4 cells. To generate nontrivial ground states within the descriptor-labeled subspace, we introduce an effective Hermitian mixing Hamiltonian based on a weighted k-nearest-neighbor (kNN) graph Laplacian over configuration labels. Across a parameter sweep, we identify a strong-mixing regime where the participation ratio approaches dim (consistent with Laplacian-dominated ground states on connected graphs) and algebraic CMI diagnostics become extremely small (down to 10^{-6} and below) for the chosen algebraic factorization, while region algebraic entropies remain O(1) and exhibit near-quantized values ~ n log 2. We stress that the mixing term is an ansatz used to probe information-theoretic diagnostics and is not claimed to coincide with a Kogut-Susskind plaquette operator. v2 (no v1 number is changed): the reproducibility gap of v1 is repaired -- v1's pipeline loaded an unshipped basis file (descs.pkl) that was never specified, so the v1 dataset was not regenerable from the paper; v2 prints a canonical self-contained basis whose pipeline reproduces every structural finding, keeping v1's Table 1 as an archival dataset; two empirical observations are upgraded to proved statements -- the descriptor-to-key map is injective, making S_alg a genuine von Neumann entropy of a sector (center-type) decomposition, and in the strong-mixing limit the ground state converges to the uniform superposition where the quantization S_alg = n log 2 and the vanishing of both CMIs are exact; the additional experiments recommended in v1 (Haar baseline, kNN ablations, finer t_mix grid) are executed -- the Haar median of I_sum is 0.39, five to six orders of magnitude above the strong-mixing point, so the small-CMI regime is nontrivial; and the verification suite is fully self-contained (no Drive dependencies).

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2601.0115v1.pdf) — 2026-01-28T08:43:53+00:00
- [v2](https://www.ai.vixra.org/pdf/2601.0115v2.pdf) — 2026-07-05T22:07:41+00:00
- [v3](https://www.ai.vixra.org/pdf/2601.0115v3.pdf) — 2026-07-31T23:16:43+00:00
