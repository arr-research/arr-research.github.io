# Recoverability Geometry: Distances and Embeddings from Quantum Markov Data — Definitions, Diagnostics, and a Reconstruction Protocol

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2601.0043](https://www.ai.vixra.org/abs/2601.0043)  
**First submitted:** 2026-01-13T12:50:18+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2601.0043-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We propose an operational route from recoverability data to effective geometry. Given a tripartition A-B(w)-C and a collar width w, we consider a Petz-type recoverability error E_rec(w) defined via fidelity and extracted from a fixed collaring rule (A, C, w) -> B(w). We define distance-like functionals from the minimal buffer needed to suppress E_rec(w) below a threshold, and from exponential fit scales when such a regime exists; these are organized into a (generally non-metric) dissimilarity matrix on coarse regions, symmetrized when needed, and embedded via multidimensional scaling or diffusion maps. The paper emphasizes precise definitions (collaring rule, symmetrization, censoring below numerical floors) and falsifiable diagnostics (approximate triangle inequalities, robustness to thresholds and regularization). A minimal control experiment in the 1D transverse-field Ising model illustrates the pipeline and the growth of a recoverability length near criticality. v2 (definitions unchanged) adds: a regenerable suite replacing the "representative run" of v1 -- the control table is regenerated from scratch, its g = 0.5 row is flagged as unstable by the paper's own fit-window policy, and a three-point-fit caveat is stated; the first in-model test of the tracking conjecture -- from the same ground states, xi_rec/xi_corr in {0.98, 0.53, 0.52} across regimes, same order of magnitude throughout; a first numerical illustration of the embedding machinery (four coarse regions, MDS recovering the chain order exactly, triangle violations bounded by discretization), which also surfaces an operational lesson: tracing out the region between B(w) and C fakes separation and inverts monotonicity, so the separation condition of the collaring rule is essential, and profiles below the separating width are not admissible; the observation that the fixed-|A|,|C|/traced-environment design of the control is precisely the fixed-target protocol that resolves the |C|-shrinkage confound identified in the companion d_eff notes; and series positioning.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2601.0043v1.pdf) — 2026-01-13T12:50:18+00:00
- [v2](https://www.ai.vixra.org/pdf/2601.0043v2.pdf) — 2026-07-05T16:21:06+00:00
