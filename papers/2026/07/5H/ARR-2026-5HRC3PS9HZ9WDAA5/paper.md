# Parity Barriers for Decoupling Inequalities: Why No Comparison Functional of Bounded Marginal Order Can Certify Uniform Decoupling

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0018](https://www.ai.vixra.org/abs/2607.0018)  
**First submitted:** 2026-07-09T14:57:20+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0018-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

For every r>=1, the uniform measure on the even-parity subset of {+-1}^{r+1}is r-wise independent, yet the last coordinate has unit variance while beingan a.s. function of the others. This example is classical - parity-checkcodes are the standard construction of k-wise independent distributions inthe pseudorandomness literature (Joffe; Alon-Babai-Itai; Alon-Goldreich-Mansour) - and no novelty is claimed for it. What is recorded here is aconsequence we have not seen isolated as a statement: any "comparisonfunctional" whose value depends only on marginal data of order <= r, withconstants uniform over finite measures, takes identical values on the paritymeasure and on the uniform product measure, and is therefore consistent withperfect decoupling on a measure where decoupling fails maximally. Hence noinequality built from bounded-order functionals can imply uniform decouplingprinciples - Dobrushin-type mixing, approximate tensorisation withmeasure-free constants, covariance decay - on any class of measurescontaining the parity family. The case r=1 recovers, and explainsstructurally, the failure of raw-oscillation/Doob and Efron-Stein-type stepsfound repeatedly in an adversarial audit of a constructive Yang-Millsprogramme; no repair within bounded-order data can succeed, because thebarrier recurs at every order. Statements (a) and (b) are machine-checkedin Lean 4/Mathlib parametrically in r (all n; no sorry; standard axiomsonly), the abstract certifying-barrier schema is formalized as well, andfinite decide instances (r<=4) plus exact rational arithmetic (r<=6) serveas independent audits.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0018v1.pdf) — 2026-07-09T14:57:20+00:00
