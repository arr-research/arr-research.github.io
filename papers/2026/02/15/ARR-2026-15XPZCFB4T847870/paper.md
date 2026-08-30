# Doob Influence Bounds for Polymer Remainders in 4D Lattice Yang-Mills Renormalization — a Corrected and Conditional Influence Bound

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2602.0070](https://www.ai.vixra.org/abs/2602.0070)  
**First submitted:** 2026-02-14T18:53:53+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2602.0070-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We study a uniform Doob martingale influence bound for the irrelevant polymer remainder arising in multiscale renormalization group analyses of four-dimensional SU(N_c) lattice Yang-Mills theory at fixed physical volume, via the Doob influence seminorm sigma_nu(f)^2 = sum_i E_nu[(Delta_i f)^2] and its exact covariance identity. Version 2 corrects a genuine error of v1: the increment-oscillation inequality E[(Delta_i f)^2 | F_{i-1}] <= (1/4) osc_{e_i}(f)^2 was asserted for ARBITRARY probability measures; it is false in general (Example 3.4: two perfectly correlated spins, f = X_2, give E[(Delta_1 f)^2] = 1 while osc_{e_1}(f) = 0), because the Doob increment collects influence transmitted through correlations. The correct, measure-independent statement uses the CONDITIONAL oscillation (Lemma 3.5); passing back to the raw single-link oscillation requires a decoupling hypothesis (H-DEC) bounding the influence-leakage matrix, of Dobrushin type — plausible for the interpolating Gibbs measures nu_{k,t} in the small-field weak-coupling regime, but unproven, and structurally akin to the (H-DOB-blk) family of the audited chain. On exact Gibbs chains the v1 bound is violated already at weak coupling for delocalized observables, while the (H-DEC)-corrected bound holds with the Dobrushin coefficient. Under (H-DEC), the imported oscillation input (A2) (now cited from 2602.0069 v2: traceable, conditional — beta_LF dichotomy included), and the lattice-animal lemma (proved here, verified exactly), the main theorem holds: sup_t sigma_{nu_{k,t}}(V_k^irr) <= C uniformly in the RG scale k, by the exact scale cancellation M 2^{-4k} = 4(L/a_0)^4. The Duhamel interface then delivers a one-step rate delta_k = O(4^{-k}) — precisely the geometrically summable rate that Assumption 3.5 of 2602.0063 v3 requires (its Remark 3.7 with eta = 2) — CONDITIONALLY on (H-DEC) + (A2) + the assumed blocking contraction (H-LIP). v1's closing claim "this establishes the RG-Cauchy property" is softened accordingly: this paper supplies the leading candidate for closing (H-CAUCHY), not its proof. All quantitative claims, including the counterexample and the Dobrushin-corrected bound on exact Gibbs chains, are adjudicated in a companion suite.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2602.0070v1.pdf) — 2026-02-14T18:53:53+00:00
- [v2](https://www.ai.vixra.org/pdf/2602.0070v2.pdf) — 2026-07-06T22:13:35+00:00
