# Strict but Not Uniform: a Machine-Checked Spectral Gap at Every Finite Extent of the Coupled Slice

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0084](https://www.ai.vixra.org/abs/2607.0084)  
**First submitted:** 2026-07-29T10:08:56+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0084-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

A companion paper supplied the vacuum of the coupled Z_2 slice at every spatialextent: a strictly positive eigenvector, unique up to scale, carrying thespectral radius. It listed PERIPHERAL SEPARATION as out of scope, and thatomission is not cosmetic - without it |mu| <= lambda leaves mu = -lambda open,and no gap follows at all.This paper closes it, and then draws the consequence that matters, which isnegative.PROVED. For a strictly positive kernel on a finite nonempty type, -lambda is notan eigenvalue, hence every real eigenvalue other than the Perron eigenvalue isSTRICTLY smaller in absolute value. Specialised to the coupled slice: at everyextent L, every beta, and every strictly positive source weight, the transferoperator has a strict spectral gap. The proof of peripheral separation avoidsthe equality case of the triangle inequality, which is where the classicalargument spends its effort: writing u = |w|, p = u - w and q = u + w, one getsA p = lambda q and A q = lambda p, so a nonzero p would make A p strictlypositive, hence q strictly positive, hence w nonnegative, hence p = 0.The separation is then extended from the real eigenvalues to ALL of them. Thecoupled kernel is conjugate by a positive diagonal to its symmetrised form,which is symmetric; and a real symmetric kernel has real eigenvalues, by acomputation that pairs the eigenvector against its image twice and is tworearrangements of a double sum. So there are no complex peripheral eigenvaluesleft to exclude, and the strict gap is a statement about the whole spectrum.That composition is itself a single machine-checked theorem(coupled_gap_all_eigenvalues), not a step left to the reader. We also deliverthe vacuum in Euclidean normalisation, norm(Omega) = 1 with T Omega = Omega.NOT PROVED, AND THIS IS THE TITLE. The gap is STRICT, not QUANTITATIVE: thetheorem provides no modulus of separation, and in particular nothing uniform inL. Direct numerical diagonalisation shows the subdominant ratio running0.9205, 0.9829, 0.9964, 0.9992 at L = 2,3,4,5 for beta = 0.8, gamma = 1.2 -collapsing towards 1. That computation is reported as measured and unproved, andno theorem here depends on it; its role is to say that a paper reporting onlythe positive half would be reporting the half that does not matter.Nothing in this paper is a claim about SU(N), the continuum limit, or theYang-Mills mass gap.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0084v1.pdf) — 2026-07-29T10:08:56+00:00
