# Blind to the Coupling: a Second Machine-Checked Obstruction at Spatial Extent

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0088](https://www.ai.vixra.org/abs/2607.0088)  
**First submitted:** 2026-07-28T23:30:40+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0088-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

A companion paper proved that when a spatial coupling is switched on in a Z_2lattice gauge slice, the transfer kernel loses constant row sums, so the uniformvector is no longer fixed and the elementary route to the vacuum stops. Thestandard replacement, when row sums fail, is the Hilbert projective metric: astrictly positive kernel contracts it, and the contraction factor bounds thesubdominant spectral ratio. This paper asks what that replacement gives here, andanswers in Lean 4 with mathlib.It gives no coupling-sensitive and no volume-uniform information, for twoindependent reasons, and both are proved. First, BLINDNESS: the projectivecross-ratio is invariant under multiplication by any nowhere-zero function of thesource configuration alone. The coupled kernel is exactly such a product, so themetric assigns the interacting and the non-interacting kernels the same diameterat every spatial extent - the route cannot see the coupling at all. Second,VOLUME DEGENERATION: two constant configurations realise the cross-ratioe^(4 beta L), so every admissible projective diameter is at least 4 beta L andevery contraction factor obtainable this way is at least tanh(beta L), which lieswithin 2 e^(-2 beta L) of the trivial bound 1. At the one place where the truthis known - the decoupled kernel, whose subdominant ratio the companion papercomputes to be exactly tanh beta at every L - this route already returnstanh(beta L) instead. The degeneration is the method's, not the model's.We then hand over the object the elementary route stopped producing, at thesmallest interacting size. In the character basis the coupled two-site kernelsplits into two 2x2 blocks, and we exhibit a strictly positive eigenvector inclosed form, together with a second exact eigenpair. The identity A - B = 4between the two decoupled even-sector eigenvalues drives every estimate. Theblindness is proved two-sided, so it covers the symmetrised conventionw^(1/2) K w^(1/2) as well, and the positive eigenvector is proved to dominateevery eigenvalue, real or complex - so its eigenvalue is the spectral radius,which is the Perron statement this development needs and proves without aPerron-Frobenius theorem in the library.NO VOLUME-UNIFORM STATEMENT ABOUT AN INTERACTING SYSTEM IS PROVED HERE, AND NONEIS CLAIMED; the general-L behaviour is recorded separately as measured andunproved. Nothing in this paper is a claim about SU(N), the continuum limit, orthe Yang-Mills mass gap.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0088v1.pdf) — 2026-07-28T23:30:40+00:00
