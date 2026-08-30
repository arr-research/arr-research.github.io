# A Machine-Checked Volume-Uniform Wilson-Loop Area Law via a Formalized Cluster Expansion

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0005](https://www.ai.vixra.org/abs/2607.0005)  
**First submitted:** 2026-07-02T21:47:02+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0005-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We report a complete formalization, in Lean 4 over Mathlib, of volume-uniform Wilson-loop area laws for SU(N c ) lattice gauge theory in an explicit strong-coupling window - including the case of the exact Wilson Boltzmann factor, not a linearized surrogate. The headline theorem bounds the normalized Wilson-loop expectation by N c e P·4dK σ Area(C) e P·4dS(σ) , where Area(C) is an intrinsic combinatorial filling area of the loop, P is its edge-support size, and every constant is volume-free: the bound holds uniformly over all finite lattice sizes. The partition function is cancelled through a fully formalized volume-restricted cluster expansion (loop-tagged factorization, restricted Mayer inversion, Z-ratio bounds, and a pinned-gas resummation built on a Kotecky-Preiss layer with Penrose-style spanning-tree counting). A reusable repackaging converts the bound into manifest exponential area decay with a strictly positive string tension, and the non-vacuity of every hypothesis window is itself machine-checked - both the cluster smallness window and the decay-repackaging window, the latter with an explicit witness of tension log 2 - 1/2. For every exported theorem in this chain the Lean kernel's axiom oracle reports exactly [propext, Classical.choice, Quot.sound]; there is no sorry and no project axiom in the dependency cone. To our knowledge this is the first machine-checked cluster-expansion proof in lattice quantum field theory. All artifacts are public, with per-theorem oracle records in a verification ledger and continuous-integration builds.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0005v1.pdf) — 2026-07-02T21:47:02+00:00
