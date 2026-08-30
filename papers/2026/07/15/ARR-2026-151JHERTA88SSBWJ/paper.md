# Machine-Checked CMP116 Fluctuation Reduction: Physical Constraint Coordinates and the Interacting-Hessian Frontier

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0044](https://www.ai.vixra.org/abs/2607.0044)  
**First submitted:** 2026-07-15T20:22:56+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0044-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We give a machine-checked reduction of the finite-dimensional fluctuation integral in Balaban's CMP116 large-field analysis. Starting from the physical block constraint Q, the formal development constructs a sparse right inverse E and the constraint-elimination operator C = I - EQ. It proves QE = I, QC = 0, C² = C, the exact sparse norm ||EB|| = M^(d-1)||B||, and the volume-independent bound ||C|| ≤ 1 + M^(d-1) for d ≥ 3. An exact physical/CMP116 isometry transports C to finite Gaussian coordinates without norm loss. The same development constructs the physical localization projector P_Z0, evaluates the complex quadratic Gaussian, localizes its determinant to rank |I(Z0)|, performs the outer Gaussian integration, and absorbs both costs into an explicit exp(c|Z0|) factor.Two corrections exposed by formalization are central. First, the useful domination occurs after Gaussian integration rather than through an unavailable pointwise supremum in the fluctuation field. Second, the localized quadratic matrix is A = -alpha_5 P_Z0. In the exactly identified trivial-background sector, the terminal Lean theorem inserts the concrete C, the flat Hessian, complement localization, and covariance root directly into the printed source Gamma_k = C^T Delta_k (C P_Z0^c)(C^(k))^(1/2), returning an explicit Cauchy bound without an ambient-volume factor. CMP116, however, requires the base Hessian at a generally nontrivial small background Ubar. We do not construct D²S_Wilson(Ubar) or the random-walk estimate (2.16), and therefore do not prove the physical domination, (2.26), hraw, hRpoly, a continuum limit, or a mass gap. The contribution is an auditable reduction that closes the constraint and Gaussian layers and identifies the first genuinely missing interacting construction.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0044v1.pdf) — 2026-07-15T20:22:56+00:00
- [v2](https://www.ai.vixra.org/pdf/2607.0044v2.pdf) — 2026-07-16T04:47:03+00:00
