# Global Ratio Monotonicity for a Killed von Mises Bridge

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0089](https://www.ai.vixra.org/abs/2607.0089)  
**First submitted:** 2026-07-28T22:32:03+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0089-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

For beta > 0 let I_m = I_m(beta) denote modified Bessel functions ofthe first kind, and set  a_m = I_m^2 [(m-1) I_(m-1)^2 + (m+1) I_(m+1)^2],  b_m = m I_m^4,  F_A(t) = sum_(m>=1) a_m sin(mt),  F_B(t) = sum_(m>=1) b_m sin(mt),  E(t) = F_A(t)/(2 F_B(t)).The global ratio-monotonicity problem for the surface expansion of atwo-dimensional SU(2) lattice gauge observable is: (i) F_B > 0 on(0,pi), and (ii) E' < 0 on (0,pi), for every beta > 0. Bothstatements are proved. Positivity of F_B has two exact proofs. Ratiomonotonicity is reduced to exact algebraic identities andoutward-rounded interval certificates: small and compact beta arehandled by pair identities and interval Taylor models;20 <= beta <= 1000/9 by a direct Wronskian cover; andbeta >= 1000/9 has three certified moving-edge lambda lanes. Theremaining lambda >= 3 lane is closed by the exact identityE'/(-sin(t/2)/2) = Q + X_full, where Q > 19/20, an exactmain--mirror--rest decomposition, and a division-free covariancecertificate proving X_main > -1/20 on two adjacent rectangles thatcover the full angular interval. The exact near and far relay marginsare positive. All load-bearing production and independent replaytranscripts are checked for exact rational coverage, dependencyhashes, strict outward-rounded decision endpoints, and byte equality.The structural core is exact: E is, as an algebraic identity, the meanof cos(psi) under the midpoint law of a four-step killed von Misesbridge; the generating kernels reduce, via the Neumann additiontheorem, to two-dimensional integrals of a single Bessel functionwhose saddle deficit is an exact sum of two squares; and exact saddlecancellations yield the coefficients of the verified closedsecond-order law  E = cos(t/2)(1 - c(t)/beta) + O(beta^-2),  c(t) = (4 cos^2(t/4) - 1)/(2 cos(t/4) cos(t/2)).Three certified negative results (interval arithmetic, twoimplementations, nested enclosures) kill every monotone full-pathcoupling, with an exact mechanism at threshold beta |cos t| = 3/2. Atthe pi endpoint we also give exact identities for the cubiccoefficient c_3 (telescoped alternating form, integral form, parity)together with its verified prefactor law. Every claim is labelledexact / certified / verified; the machine-checked lemmas are Lean4/Mathlib, machine-checked modulo classical Bessel inputs carried asnamed hypotheses.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0089v1.pdf) — 2026-07-28T22:32:03+00:00
