# Residual Derivative Bounds and Windowed Uniform Log-Sobolev Inequality for SU(Nc) Lattice Yang-Mills at Weak Coupling

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2602.0055](https://www.ai.vixra.org/abs/2602.0055)  
**First submitted:** 2026-02-12T19:09:28+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2602.0055-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We prove residual derivative bounds for the polymer expansion of Balaban's multiscale decomposition of the Wilson lattice gauge measure for SU(N_c) in dimension d >= 3, and we assemble them, together with the companion series, into a uniform log-Sobolev inequality. Version 2 corrects the status of this assembly after a quantitative audit. (i) The core mechanism of the paper — locality of polymer functionals, Cauchy estimates on Balaban's analytic domains, and a volume-independent counting bound for connected polymers containing a fixed link — survives intact and is validated numerically; it yields a pointwise derivative bound on the polymer residual with constants independent of the lattice volume, CONDITIONALLY on Balaban's small-field inputs (B1)-(B4). (ii) However, the final step of v1's Theorem 3.5, the inequality k <= C_RG(1+beta_k), relied on the inverted-sign running-coupling flow of the series erratum; with the correct asymptotic-freedom flow the reduced coupling beta_k DECREASES along the cascade, the small-field condition g_k <= gamma_0 is available only for k <= k*(beta), and the derivative bound holds in the windowed form C_res(1+beta) for L_vol <= e^(C/g^2+O(1)). (iii) The assembly of the main theorem inherits two hypotheses identified in the audits of 2602.0052 v2 and 2602.0053 v2: the large-field absorption step requires a power-law penalty exponent — hypothesis (H-P0) — since with the stated polylog floor the suppression factor trivializes (e^(-c_sf p0(gamma_0)) ~ 0.95 at gamma_0 = 0.1) and the absorption inequality fails at every scale (excess >= 10^4.6); and any quantitative use of the conditional fiber LSI via Holley-Stroock carries the penalty e^(-2 beta n_plaq) — hypothesis (H-YGZ) (log10 alpha_blk ~ -5559 at gamma_0 = 0.1, n_plaq = 64). (iv) Version 1's Corollary 1.2 and Remark 5.1 claimed that the Dobrushin-type Assumption 6.3 of Paper I is "no longer needed" via the DLR route of the companion 2602.0053; the v2 audit of that companion shows the route REDUCES Assumption 6.3 to an unverified block condition (H-DOB-blk) whose printed bound c_ij <= tanh(beta n_bd/2) trivializes at weak coupling. Accordingly, v1's closing claim is replaced: the uniform LSI of Theorem 1.1 is WINDOWED and CONDITIONAL on (H-P0) and (H-YGZ), and the mass gap of Corollary 1.2 is additionally conditional on (H-DOB-blk). This replacement also records the completed retagging of the chain: the companion 2602.0054 has been audited and replaced (v2, conditional/windowed assembly), so 2602.0051-0055 now all carry their v2 statuses; reference [6] is corrected (v1 listed 2602.0053 under the title of 2602.0054). All quantitative claims are adjudicated in a companion numerical suite (9 deterministic checks).

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2602.0055v1.pdf) — 2026-02-12T19:09:28+00:00
- [v2](https://www.ai.vixra.org/pdf/2602.0055v2.pdf) — 2026-07-06T20:00:57+00:00
