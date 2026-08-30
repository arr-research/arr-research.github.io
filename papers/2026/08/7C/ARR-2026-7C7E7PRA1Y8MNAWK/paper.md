# Machine-Checked Finite-SU(2) Trace-Skein Closure for Makeenko-Migdal Crossing Terms

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2608.0001](https://www.ai.vixra.org/abs/2608.0001)  
**First submitted:** 2026-08-01T18:50:53+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2608.0001-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

Finite-rank Makeenko-Migdal equations generate products of Wilson traces at self-intersections. For SU(2), this apparent multitrace obstruction closes exactly on single traces, but the statement is normalization-sensitive: the traceless Lie algebra contributes a finite-rank correction that disappears for U(2) and must not be dropped. We give a Lean 4/Mathlib formalization of the complete group-algebraic closure mechanism on Mathlib's concrete special unitary matrix group. With normalized trace tau(A)=Tr(A)/2 and normalized anti-Hermitian Pauli directions X_j=i sigma_j/2, the kernel checks the Casimir identity, the rank-two Fierz identity, the induced crossing contraction, and the SU(2) trace-skein identity tau(g)tau(h)=(tau(gh)+tau(gh^{-1}))/2. Consequently, the finite-SU(2) crossing term tau(g)tau(h)-tau(gh)/4 equals tau(gh)/4+tau(gh^{-1})/2. We then formalize a universal local interface with four cyclically ordered branch holonomies, an independent orientation on each branch, the two opposite-strand words, and precisely the two direct/reversed reconnections. Its corrected crossing term closes on those reconnections for every branch assignment and orientation choice. A recursive theorem also extends the reduction to products of arbitrarily many fundamental traces. The identities are classical; the contribution is a concrete, kernel-checked normalization bridge from Pauli contraction to the single-trace closure used in finite-rank loop equations. We do not claim a formal derivation of the Yang-Mills area derivative, planar loop geometry, or the full Makeenko-Migdal equation.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2608.0001v1.pdf) — 2026-08-01T18:50:53+00:00
