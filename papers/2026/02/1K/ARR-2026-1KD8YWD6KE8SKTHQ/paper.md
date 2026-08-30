# Large-Field Suppression for Lattice Gauge Theories: From Balaban's Renormalization Group to Conditional Concentration — a Conditional and Windowed Verification

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2602.0056](https://www.ai.vixra.org/abs/2602.0056)  
**First submitted:** 2026-02-12T19:07:45+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2602.0056-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We verify, at the level of form, the large-field hypothesis (Hypothesis 4.2) of the companion paper on integrated cross-scale derivative bounds for Wilson lattice gauge theory (Paper III). The proof rests on three ingredients: (i) a dictionary lemma translating the Hilbert-Schmidt large-field condition on plaquette holonomies into Balaban's Lie-algebra formulation; (ii) an interface lemma connecting conditional measures with Balaban's T-operation and its uniform small-factor bound on admissible background fields (Eq. (1.89) of Balaban, Large field renormalization II); (iii) the uniformity estimate (Eq. (1.75) ibid.) ensuring that slow-field dependence contributes only an O(1) multiplicative constant. For d = 2, we give an independent proof via character-positive convolutions that avoids the Balaban machinery entirely. Version 2 corrects the status of these results after the quantitative audit of the series (ai.viXra:2602.0051-0055, all v2). (a) v1's claim that the bound is "more than sufficient" for the absorption condition of Paper III is withdrawn: the printed small factor is exp(-c p0(g_k)) with c = 2/(1+beta_0), and with the polylog floor on p0 the suppression trivializes (e^(-c p0(gamma_0)) ~ 0.95) and the absorption inequality fails at every scale (excess >= 10^4.6); effectiveness requires the power-law hypothesis (H-P0) of 2602.0052 v2. (b) v1's premise "p0(g_k) -> infinity as g_k -> 0 along the flow" and Sec. 7's appeal to a stability theorem rely on the inverted-sign running-coupling flow of the series erratum; with the correct asymptotic-freedom flow the small-field condition g_k <= gamma_0 holds only for k <= k*(beta), and all statements are windowed: L_vol <= e^(C/g^2+O(1)). (c) v1's Remarks 4.1-4.2 (slow-field identification and Balaban conditional representation) are unproved interface statements; they are made explicit here as hypothesis (H-SFI), cf. the interface lemmas of 2602.0052 v2. (d) In d = 2 the prefactor K_beta(1)/Z(U_B) of Proposition 6.4 is not uniform in beta, so the d = 2 route verifies a fixed-beta variant only; this is now stated in the theorem. What survives unconditionally and is validated in the companion numerical suite: the HS/Lie-algebra dictionary (Lemma 2.1), the gauge-invariance identity (Remark 2.2), the block event inclusion (Lemma 3.2), and the character-positivity mechanism of Section 6 (Peter-Weyl positivity of the Wilson weight, convolution stability, maximum at the identity, and conditional tail domination in an exact d = 2 toy).

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2602.0056v1.pdf) — 2026-02-12T19:07:45+00:00
- [v2](https://www.ai.vixra.org/pdf/2602.0056v2.pdf) — 2026-07-06T21:03:37+00:00
