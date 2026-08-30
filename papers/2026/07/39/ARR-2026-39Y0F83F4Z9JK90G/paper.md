# The Diagonal Amos-Type Family at Real Order: a Machine-Checked Quantitative Crossing Classification

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0037](https://www.ai.vixra.org/abs/2607.0037)  
**First submitted:** 2026-07-13T05:29:47+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0037-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

For the one-parameter family B(x) = x/(nu+c+sqrt((nu+c)^2+x^2)) of Amos-type expressions, whose member c = 1/2 is the classical Amos-type upper bound for the modified Bessel ratio I_{nu+1}/I_nu, we formalize in Lean 4, at every real order nu >= 0 over the Gamma-power series, the classification of the parameter: B is a uniform upper bound for the ratio exactly when c <= 1/2, and a uniform lower bound for every c >= 1, with explicit rational counterexample witnesses (the classification itself is known mathematics, due to Ruiz-Antolin and Segura; we claim only the machine-checking). The contribution is the regime between the ends: for every nu >= 0 and c strictly between 1/2 and 1 we prove that the fixed family member crosses the ratio exactly once on (0, infinity) -- a transversal crossing in an explicit finite window, strictly above an explicit threshold, with globally determined sign on both sides and a two-sided scale law; degenerate contact is excluded by an exact second-derivative identity. The chain carries the axiom oracle [propext, Classical.choice, Quot.sound] and no analytic hypothesis beyond nu >= 0, x > 0; a pre-registered certified interval-arithmetic companion verifies the crossing phenomenon independently of the crossing theorems at 30 parameter pairs spanning the hard regimes, all passing at 128 bits.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0037v1.pdf) — 2026-07-13T05:29:47+00:00
