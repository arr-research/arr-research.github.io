# Petz Recoverability Versus Wilson-Loop Diagnostics in 2+1D Z2 Lattice Gauge Theory: Benchmarks by Exact Diagonalization and Tensor-Network Ladders

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2601.0051](https://www.ai.vixra.org/abs/2601.0051)  
**First submitted:** 2026-01-14T20:03:27+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2601.0051-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We provide reproducible finite-size benchmarks testing whether a Petz-type recoverability proxy correlates with Wilson-loop confinement diagnostics in Z2 lattice gauge theory in 2+1 dimensions: an exact-diagonalization benchmark on 2x2 and 2x3 plaquette lattices (Gauss penalty, ~ 1 verified), and TeNPy DMRG ladders 2xL, L in {4, 6, 8}, chi_max = 96, with a warm-start bond-dimension stability check (chi = 96 to 192 stable to all shown digits). In the tensor-network part, E_rec is reported as a function of contiguous buffer size |B| in MPS site ordering (a declared proxy), not the BFS collar of the ED part. v2 (no v1 number is changed): the broken Appendix A.1 of v1 -- whose published PDF literally prints "Missing file" where the ED reproduction script should appear -- is repaired by pointing to the series repository, where that script and a full verification suite for the ED benchmark already live with the companion paper; internal working titles leaked throughout v1's scripts and captions are removed; the MPS-ordering proxy is sharpened with new evidence -- on an exact Z2 ladder the geometric admissible buffer decays cleanly (5e-4 to 3e-8) while the contiguous-ordering proxy starts orders of magnitude higher and saturates, and a from-scratch DMRG replication (reduced chi, Lx = 4) reproduces both the trend direction of the money plots and v1's own buffer inversion E_rec(|B|=2) > E_rec(|B|=1), confirming it as a property of the contiguous proxy rather than a numerical accident; the confinement-vs-gap degeneracy established for the ED twin applies verbatim to the ladder money plots and is now stated; and series positioning is added. All conclusions remain finite-size benchmark statements.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2601.0051v1.pdf) — 2026-01-14T20:03:27+00:00
- [v2](https://www.ai.vixra.org/pdf/2601.0051v2.pdf) — 2026-07-05T18:33:10+00:00
