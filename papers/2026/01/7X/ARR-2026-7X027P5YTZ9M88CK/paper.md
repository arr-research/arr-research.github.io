# Program A: Semi-Infinite Conditional Mutual Information in the 1D TFIM (iMPS)

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2601.0099](https://www.ai.vixra.org/abs/2601.0099)  
**First submitted:** 2026-01-24T17:02:20+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2601.0099-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We study an information-theoretic notion of locality -- approximate quantum Markov behavior -- via the conditional mutual information (CMI) I(A:C|B(w)) in a semi-infinite geometry of the 1D transverse-field Ising model (TFIM). Using infinite matrix product states (iMPS), we compute I(A:C|B(w)) as a function of the collar width w separating two semi-infinite regions. In a representative gapped point (h = 1.5), we observe clean exponential decay and a rapid plateau of the local effective-length estimator, yielding an early-decay length xi_rec^(early) comparable to the iMPS transfer-matrix correlation length xi_corr. Near criticality (h = 1.005), the local estimator increases throughout the accessible range, indicating a pre-asymptotic regime; we therefore report a fixed-window effective length and a window-sensitivity range as a systematic uncertainty. All generated assets used here (two JSONL data streams, the figure, and the LaTeX table snippet) are included in the Overleaf project. v2 (no v1 number is changed): Appendix A is repaired (in v1 the data-source filenames were typeset in math mode and the near-critical entry was missing entirely); Table 1 is re-typeset (collided columns in v1); the Colab scripts of Appendix B are shipped as runnable files in the series repository rather than as listings; series positioning is added -- this paper is a numerical instantiation of the A-CMI hypothesis of the contract note ai.viXra:2601.0066 in a semi-infinite 1D geometry; and an independent verification suite (free fermions via Jordan-Wigner, no tensor networks) reproduces the gapped point of Table 1 exactly (xi_rec^(early) = 1.149 on the main window, window sensitivity [1.149, 1.158], both matching v1 digit for digit), verifies the operational identity I = 2 S_cut - S(B(w)) to 10^{-11}, and reproduces the rising near-critical xi_local(w); a TeNPy cross-check reproduces the free-fermion I(w) pointwise to 5x10^{-5} relative.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2601.0099v1.pdf) — 2026-01-24T17:02:20+00:00
- [v2](https://www.ai.vixra.org/pdf/2601.0099v2.pdf) — 2026-07-05T21:05:26+00:00
