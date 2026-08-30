# Influence Bounds for Polymer Remainders in Balaban's Renormalization Group: an Unconditional Efron-Stein Bound and a Conditional (B6) Closure for the RG-Cauchy Programme in 4D Lattice Yang-Mills

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2602.0072](https://www.ai.vixra.org/abs/2602.0072)  
**First submitted:** 2026-02-14T11:43:03+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2602.0072-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We study the influence estimate — Assumption (B6) — required by the RG-Cauchy summability framework for blocked observables in four-dimensional SU(N_c) lattice Yang-Mills theory, measured by the Efron-Stein seminorm sigma_nu(f)^2 = sum_e E_nu[Var_{nu_e}(f)]. In the small-field regime of Balaban's multiscale effective action, under (A1) a polymer representation, (A2) a per-link oscillation bound with irrelevance factor 2^(-2k), and (A3) lattice-animal counting — all imported from the traceability companion 2602.0069 v2 (conditional) — we prove the UNCONDITIONAL seminorm bound sup_t sigma_{nu_{k,t}}(V_k^irr) <= C independent of the RG scale k: the single-link conditional variance obeys Var_{nu_e}(f) <= (1/4) osc_e(f)^2 for EVERY measure (Lemma 3.2 — conditioning on all other links freezes them, so no influence leaks; this is the sound half, in exact duality with the sibling paper 2602.0070, whose per-link lemma failed but whose covariance identity was exact). Version 2 corrects the unsound half: v1's covariance bound |Cov_nu(f,h)| <= sigma_nu(f) sigma_nu(h) (its Eq. (18)) is FALSE for non-product nu — Example 3.5: perfectly correlated spins give sigma_nu(X_2) = 0 < 1 = Var_nu(X_2) — because Efron-Stein tensorisation is an independence theorem, and the interpolating Gibbs measures nu_{k,t} couple links. On exact Ising chains the tensorisation ratio Var/sum E[Var_e] equals 1.00/1.35/3.40/52.4 at J = 0/0.15/0.5/1.5. Restoring the Duhamel application requires APPROXIMATE TENSORISATION of variance (H-AT): Var_nu(f) <= C_AT sum_e E_nu[Var_{nu_e}(f)] uniformly along the interpolation — a Dobrushin-uniqueness-type condition, the same family as the sibling's (H-DEC) and the chain's (H-DOB-blk), verified here on exact Gibbs chains at weak coupling (C_AT ~ 1.35) and violated without it. There is also a seminorm-interface gap: the companion Duhamel lemma is proved for the Doob seminorm, and sigma_Doob is NOT dominated by the Efron-Stein seminorm for non-product nu (same counterexample; the two seminorms are incomparable in general). Conclusion: (B6) AS CONSUMED by the RG-Cauchy argument is closed conditionally on (H-AT) (or (H-DEC)); the unconditional content of this paper is the Efron-Stein seminorm bound and its scale-uniform M 2^(-4k) = 4(L/a_0)^4 cancellation (with the convergence threshold kappa > log C_anim of v1's Remark B.1 confirmed). Joint statement with 2602.0070 v2: the UV block's only open probabilistic input is Dobrushin-type decoupling of the interpolating measures. All claims, including both counterexample adjudications and the weak-coupling validation of (H-AT), are machine-verified in a companion suite.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2602.0072v1.pdf) — 2026-02-14T11:43:03+00:00
- [v2](https://www.ai.vixra.org/pdf/2602.0072v2.pdf) — 2026-07-06T22:27:51+00:00
