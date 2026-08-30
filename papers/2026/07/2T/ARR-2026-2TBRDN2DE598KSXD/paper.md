# The Quotient That Is Not the Identity: A Machine-Checked Degenerate Reflection Pairing and Its Gelfand-Naimark-Segal Quotient

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0076](https://www.ai.vixra.org/abs/2607.0076)  
**First submitted:** 2026-07-28T17:10:48+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0076-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

The Osterwalder-Seiler reconstruction passes from a reflection-positive measureto a Hilbert space by quotienting out the null space of the reflected pairing.In a companion development that step was present but did nothing: the pairingthere was definite, so the quotient was the identity, and that paper says so inits own abstract. This paper supplies the missing case, in Lean 4 with mathlib.For the Z_2 lattice gauge chain we take half-space observables of two timeslices - a four-dimensional space - and form the reflected pairing directly fromthe Boltzmann weights. For beta > 0 the reconstructed physical space istwo-dimensional. Integrating out the future collapses four observables onto twostates, and that collapse is the null space. We prove: the pairing factors through anindependently defined reconstruction map Phi; its self-pairing rearranges into amanifest sum of two non-negative terms, from which positivity and the null spacefollow together; the null space is EXACTLY ker Phi, not merely non-empty; anexplicit non-zero observable lies in it; and the quotient is isomorphic to thephysical space BY THE MAP Phi ITSELF, not by a dimension count.The degeneracy is the mechanism the reconstruction exists to handle, and the oneexpected to reappear in systems with larger half-space algebras. What is notclaimed: this is twotime slices and not m; still Z_2, one variable per slice, fixed finite size, andnot volume-uniform; Z_N for N > 2 is untouched; and the completion step of thereconstruction is trivial here because every space in sight isfinite-dimensional, which we state rather than present as work done. Nothing inthis paper is a claim about SU(N), the continuum limit, or the Yang-Mills massgap.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0076v1.pdf) — 2026-07-28T17:10:48+00:00
