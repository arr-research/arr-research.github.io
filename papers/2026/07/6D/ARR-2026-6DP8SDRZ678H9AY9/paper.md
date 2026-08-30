# One Amos Bound, Three Consumer Sites: Machine-Checked Bessel-Ratio Calculus for Lattice Gauge Expansions

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0033](https://www.ai.vixra.org/abs/2607.0033)  
**First submitted:** 2026-07-12T13:19:13+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0033-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

The Amos-type upper bound on the modified-Bessel ratio, I{nu+1}(x)/I_nu(x) < x/(nu + 1/2 + sqrt((nu+1/2)^2 + x^2)), has a distinguished algebraic property: its right-hand side U satisfies the exact calibration identity 1/U - U = (2nu+1)/x. From that identity alone — by ordered-field algebra, with no further analytic input — follow a unit-step inequality rho_nu - rho{nu+1} < 1/x for consecutive ratios, the strict increase of the log-derivative (log I_nu)' = rho_nu + nu/x across orders, and the strict monotonicity of a phi-sequence arising in a two-dimensional lattice-gauge surface expansion. We formalize this calculus in Lean 4: a single module defines the bound once (AmosBound) and proves the calibration engine and four consequence theorems through that one definition, together with two rational satisfiability witnesses whose Amos hypothesis holds by exact Pythagorean arithmetic; all eighteen Lean statements of the development pass the axiom oracle with exactly [propext, Classical.choice, Quot.sound] against a pinned Mathlib. A certified companion (256-bit interval arithmetic, self-contained series-plus-tail enclosures, committed transcript) certifies the bound provably strictly at all 1206 points of a pre-registered grid covering the arguments the applications consume. A Bessel interface completes the closure: integer-order I_n is defined by its power series in the same pinned development, with positivity, the three-term recurrence, the termwise-differentiated derivative identity I_n' = I_{n+1} + (n/x) I_n, and the logarithmic-derivative identity (log I_n)' = rho_n + n/x all proved as theorems, so the consequence theorems — including the unit step read as strict log-derivative monotonicity, in deriv form — hold for genuine Bessel ratios with the Amos bound as the single remaining hypothesis. The scope is stated exactly: the Amos bound itself remains a classical cited theorem taken as hypothesis — this paper unifies its three previously scattered uses in our formal development into one named proposition with one oracle and one certified numerical witness, and no downstream result changes its verification class.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0033v1.pdf) — 2026-07-12T13:19:13+00:00
