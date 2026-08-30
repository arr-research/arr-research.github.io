# Recurrence-Amos Proof of the Unit-Step Order-Monotonicity of (log I_nu)', with a Feynman-Hellmann Application to Two-Dimensional Lattice Gauge Theory

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0020](https://www.ai.vixra.org/abs/2607.0020)  
**First submitted:** 2026-07-09T13:40:14+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0020-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

Let I_nu denote the modified Bessel function of the first kind and, forx>0, let rho_nu(x) = I_{nu+1}(x)/I_nu(x). We give a four-step, fullyelementary proof of the sharp difference inequality0 < rho_nu(x) - rho_{nu+1}(x) < 1/x (x>0, nu>=0), whose right-handinequality is exactly the strict increase of the logarithmic derivative(log I_nu)'(x) under the unit shift nu -> nu+1; consequentlynu -> (log I_nu)'(x) is strictly increasing along every unit-spaced gridnu_0 + N, in particular on the integer and half-integer orders arising inthe application. The stronger continuous-order statement is known(Freitas-Laugesen, arXiv:1810.07461, Lemma 10, via Bessel zeros); we makeno elementary claim about fractional steps. The proof given here uses noinformation about Bessel zeros: it combines the three-term recurrence withthe classical Amos-type upper bound rho_nu < x/(a+sqrt(a^2+x^2)),a = nu+1/2, and rests on the observation that this bound is exactlycalibrated for the problem: 1/U - U = 2a/x is an algebraic identity, and(2nu+1)/x is precisely the threshold the unit step requires; in fact theunit-step monotonicity and the Amos bound are equivalent. As anapplication we record the following consequence in two-dimensional latticegauge theory: for the Wilson action, every mass gap between charactersectors of the 2D transfer operator - for U(1) and SU(2) alike - is astrictly decreasing function of the bare coupling beta, by theFeynman-Hellmann identity. The algebraic core of the proof ismachine-checked in Lean 4/Mathlib (no sorry; axiom oracle: Lean's threestandard axioms), and an independent high-precision numerical audit ofevery inequality used is reported.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0020v1.pdf) — 2026-07-09T13:40:14+00:00
