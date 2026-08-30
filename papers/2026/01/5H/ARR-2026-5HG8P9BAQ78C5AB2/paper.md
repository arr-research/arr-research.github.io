# Petz Recoverability in AQFT via Conditional Expectations: A Framework and a Conditional Exponential Recovery Bound

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2601.0046](https://www.ai.vixra.org/abs/2601.0046)  
**First submitted:** 2026-01-13T05:25:36+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2601.0046-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We formulate an operational notion of recoverability in algebraic quantum field theory for type III local von Neumann algebras. Fixing a faithful normal KMS reference state and assuming a state-preserving conditional expectation, we define the recovery channel and, working in a fixed split implementation for each separation r, we assume (i) exponential decay of split-implemented conditional mutual information and (ii) a CMI-to-recovery inequality. Under these explicit bridge assumptions we obtain a conditional exponential recoverability bound E_rec(r) <= g(C1 e^(-m r)). v2 corrects the duality underlying the construction: v1 defined the Petz-type channel as the "Accardi-Cecchini adjoint" via the pairing omega(Z R(X)) = omega(eps(Z) X) and "proved" finite-dimensional consistency with the standard Petz map; that identity is false in general (the printed proof contains an invalid cyclicity step; numerically the identity fails at order 1e-1 on random faithful states, holding only in commuting/product situations). The correct statement, proved and machine-verified here, is that the standard Petz map is the trace-predual of the generalized (Accardi-Cecchini) conditional expectation; accordingly, v2 defines the recovery channel in Schrodinger picture as precomposition with the conditional expectation. This also repairs a type/direction error in v1's recovered-state definition, whose corrected form (omega restricted to AB, composed with the normal extension of id_A tensor eps) reproduces the standard Petz reconstruction exactly in finite dimensions. We further relabel v1's finite-dimensional map as the generalized conditional expectation (its Takesaki module property fails generically -- verified), record that for a true state-preserving conditional expectation the recovery is the CE-pullback, and add series positioning: this note is the AQFT capstone announced by the companions, its split-implemented CMI is one of three compatible regularizations in the series, and the numerical program deferred by v1 has since been executed. The main theorem is unchanged: a conditional framework statement isolating the missing bridge assumptions.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2601.0046v1.pdf) — 2026-01-13T05:25:36+00:00
- [v2](https://www.ai.vixra.org/pdf/2601.0046v2.pdf) — 2026-07-05T17:09:22+00:00
