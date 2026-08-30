# Where the Elementary Reconstruction Stops: Spatial Coupling Breaks the Uniform Vacuum, Machine-Checked

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0075](https://www.ai.vixra.org/abs/2607.0075)  
**First submitted:** 2026-07-28T19:17:42+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0075-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

Two companion developments verified an Osterwalder-Seiler reconstruction end toend for a lattice gauge chain whose spatial slice is a single point. Every stepof that chain begins by knowing the vacuum, and in the one-dimensional case thevacuum is free: the normalised transfer kernel has constant row sums, so theuniform vector is fixed, and T*Omega = Omega follows from normalisation alone.This paper asks what survives when the slice acquires spatial extent, andanswers in Lean 4 with mathlib.The algebraic half survives untouched. With time bonds only, the row sums of thetransfer kernel are constant for every spatial extent L, so the uniform vacuumpersists on a space of dimension 2^L; and the single-site sign observable is aneigenvector whose normalised eigenvalue is exactly tanh beta, with L free in thestatement.The uniform vacuum does not survive. Switching on a coupling between sites inside aslice makes the spatial weight depend only on the source configuration, so itfactors out of the sum over the target and the row sums becomeconfiguration-dependent. We exhibit two explicit configurations of a two-siteslice with different row sums, and conclude that no constant row sum exists: theuniform vector is not fixed, so T*Omega = Omega is FALSE for it. The vacuumbecomes a Perron vector that row-sum normalisation no longer supplies in closedform, and every later step of the reconstruction loses its starting point.We state plainly what the positive half is and is not. The decoupled system is Lnon-interacting copies of a two-state system, and the rate it yields - theeigenvalue tanh beta of the single-site sign mode - is independent of L fortrivial reasons, so it is physically empty and is recorded only because itisolates which half of the construction survives. NO GAP FOR THE COUPLED SYSTEM IS PROVED HERE, AND NONE IS CLAIMED.Nothing in this paper is a claim about SU(N), the continuum limit, or theYang-Mills mass gap.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0075v1.pdf) — 2026-07-28T19:17:42+00:00
