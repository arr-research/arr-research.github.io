# A Machine-Checked Exact Evaluation of the Two-Dimensional SU(2) Heat-Kernel Lattice Model on Certified Finite Combinatorial Disk Cellulations: From Haar Measure to Conditioned Original-Edge Amplitudes

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0039](https://www.ai.vixra.org/abs/2607.0039)  
**First submitted:** 2026-07-14T18:49:45+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0039-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We present an end-to-end Lean 4/Mathlib formalization of the exact evaluation of the two-dimensional SU(2) heat-kernel lattice model on certified finite combinatorial disk cellulations. The development starts from normalized Haar probability on the concrete matrix group SU(2). It identifies its transport to S^3 with the canonical spherical measure, proves an all-order orbital integration formula, derives translated character convolution, and passes from finite character sums to the infinite heat-kernel semigroup by dominated convergence. A genuine shared-edge integral then yields the two-face Migdal move.The geometric layer is independent of any reduction tree. A cellulation stores vertices, paired half-edges, cyclic face words, incidence, Euler characteristic, and positive face areas. Connected dual graphs admit certified elimination schedules, every valid schedule reduces to the heat kernel at total area, and all schedules give the same amplitude. For the original edge model, a rooted spanning tree produces a measurable, product-Haar-preserving gauge equivalence SU(2)^E ≃ SU(2)^(V{r}) × SU(2)^(ET). A compatible tree-cotree construction then retains the exterior holonomy rather than integrating it out. For every certified physical disk cellulation, the boundary-conditioned original-edge amplitude is exactly the SU(2) heat kernel at the total face area. Coefficient extraction gives, for every irreducible label n, the normalized exterior-boundary identity E_P[W_n(H_boundary)] = exp[-n(n+2)(sum_f t_f)/4], where H_boundary is the retained holonomy of the complete exterior boundary word. The universal record is demonstrably inhabited: a concrete three-spoke disk has (V,E,F)=(4,6,3) and derived dual graph K_3. A reproduced audit covers 177 audited declarations, explicitly including both headline theorems, and finds only propext, Classical.choice, and Quot.sound in their dependency cones. The analytic solution is classical. The contribution is a concrete kernel-checked composition from Haar measure and characters to physical edge variables, gauge fixing, tree-cotree elimination, and the exact boundary-observable endpoint.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0039v1.pdf) — 2026-07-14T18:49:45+00:00
- [v2](https://www.ai.vixra.org/pdf/2607.0039v2.pdf) — 2026-08-01T15:44:49+00:00
