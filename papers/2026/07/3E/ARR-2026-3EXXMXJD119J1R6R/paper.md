# The Rate Without the Extent: a Machine-Checked Uniform Spectral Modulus for the Decoupled Z_2 Slice

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0092](https://www.ai.vixra.org/abs/2607.0092)  
**First submitted:** 2026-07-30T14:48:32+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0092-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

Every rate in this lane so far has been a fixed-extent rate. The gap paper provedstrict spectral separation at each extent and said plainly that it was notuniform; the modulus paper gave that separation a number, specRatio(L), andreported measurements saying the number tends to 1 outside the disordered region.A geometric bound whose rate tends to 1 is empty in the volume limit, so nothingin the lane survived L -> infinity, and the word CLUSTERING was never used.PROVED. For the DECOUPLED kernel - the transfer kernel at constant source weight- the modulus is specRatio = tanh(beta) at EVERY extent, with L nowhere in it.Both directions: an operator bound by induction on the extent, and attainment bythe single-site observable the extent paper already built. Composing with themodulus paper's endpoint, the normalised Gibbs two-point function obeys|E[A(X_0)A(X_N)]| <= C_A tanh(beta)^N past one threshold serving everyobservable - a bound whose RATE contains no L, and therefore the first statementin this lane that survives the volume limit.WHY THE PROOF IS NOT THE SPECTRAL DECOMPOSITION. The decoupled kernel is aproduct over sites, so its spectrum is a product; that route needs the spectrumof a Kronecker power, which the library does not carry. It is not needed. Themodulus paper proved that specGap is the GREATEST norm ratio on the fluctuationsector, so bounding it above is an operator inequality and nothing else, and thatfalls to induction: the even part of an observable keeps its mean zero andinherits the rate, the odd part keeps nothing and gets only Schur's test, and thetwo recombine EXACTLY, because tanh(beta) Z = D with Z the row sum and D the oddeigenvalue of a single bond.NOT PROVED, AND A JUDGE THAT FAILED. The COUPLED kernel is untouched. Before anyof this was written we pre-registered two falsifiable predictions. The first -that the decoupled rate is exactly tanh(beta) at every extent - passed to 1e-16,and authorised the work above. The second - that the coupled uniformity boundaryis the Onsager curve - failed on one of eight pre-registered cells, and it staysfailed: that claim is reported as NOT ESTABLISHED, not softened. At constantsource weight the spatial slices are independent, so what is proved here is astatement about a product measure; that is exactly why it is reachable, and it issaid in the paper rather than left to be noticed. Reflection positivity isuntouched, and nothing in this paper is a claim about SU(N), the continuum limit,or the Yang-Mills mass gap.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0092v1.pdf) — 2026-07-30T14:48:32+00:00
