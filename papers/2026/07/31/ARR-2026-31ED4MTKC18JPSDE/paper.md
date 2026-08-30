# Clustering and the Transfer-Operator Gap: A Machine-Checked Dense-Family Criterion

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0070](https://www.ai.vixra.org/abs/2607.0070)  
**First submitted:** 2026-07-27T16:38:14+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0070-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

Inside a Lean 4 formalization programme for four-dimensional SU(N_c) latticeYang-Mills, we machine-check the operator-theoretic criterion that standsbetween exponential decay of a Euclidean correlator and a spectral gap of atransfer operator. Let T be a bounded self-adjoint operator on a Hilbert spaceand W a unit vector fixed by T, so that TW = W, and put S = T - |W><W|.Exponential decay at rate r of the connected two-point function<v, T^n v> - |<W,v>|^2 at every v is equivalent to the operator-norm bound||S|| <= r.The substantive part is the dense-family criterion. WritingD_r = {v : there is C with ||S^n v|| <= C r^n for all n}, we prove that D_r isa linear subspace and that its density alone forces ||S|| <= r, the constantsbeing entirely unconstrained: a family of observables whose span is dense, eachcarrying its own finite constant, suffices. Consequently prefactors that growwith the support of the observable - the shape cluster expansions produce - donot obstruct the gap, provided the exponential rate is common to the family andthe family spans densely. Those two provisos are essential; without them thestatement is false.No mathematical novelty is claimed for the criterion itself, which we expect tobe known in the language of local spectral theory; what is offered is itsmechanization, its packaging for families of observables, and the consequencefor prefactors. We also record what the formalization does not contain: noOsterwalder-Seiler Hilbert space for any gauge theory, no reflection positivityof the Wilson measure, no identification of a Euclidean correlator with a matrixelement. Nothing here is a claim about the continuum limit or about the Clayproblem. All results are machine-checked with no sorry and no project axioms.  (W stands for the vacuum vector Omega. If the form's preview renders Unicode  cleanly you may substitute the real symbols; the ASCII form above is the safe  default and matches the PDF's content either way.)

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0070v1.pdf) — 2026-07-27T16:38:14+00:00
