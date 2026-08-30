# A Machine-Checked Proof of an Amos-Type Bound for Modified Bessel Ratios at Real Order

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0030](https://www.ai.vixra.org/abs/2607.0030)  
**First submitted:** 2026-07-12T20:21:46+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0030-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

The Amos-type upper bound for the modified Bessel function ratio, rho_nu(x) = I_{nu+1}(x)/I_nu(x) < x/(nu + 1/2 + sqrt((nu+1/2)^2 + x^2)), is classical, and its derivation through the qualitative theory of the associated Riccati equation is an established technique. A companion paper formalized the bound at integer order over a factorial power series. This paper extends the formalization to every real order nu >= 0: the function I_nu is defined by its Gamma-power series (real exponents via rpow), and the complete chain — convergence, positivity, the three-term recurrence, termwise differentiation with a dominated-derivative argument that must treat the leading term separately (its exponent nu-1 is negative for nu < 1), the Riccati equation, a small-argument zone bound uniform in nu, and a first-crossing barrier — is machine-checked in Lean 4 with axiom oracle [propext, Classical.choice, Quot.sound] and no analytic hypothesis beyond nu >= 0, x > 0. Two structural locks tie the result to the integer development: an identification theorem proves that at nu = n the Gamma-series object coincides with the factorial-series object, so the integer-order theorem of the companion development is recovered as a corollary in three rewrites; and a genuinely non-integer instance at nu = 1/2 witnesses that the endpoint lives outside the natural-number embedding. The theorem is proved for the in-core Gamma-series definition; no identification with an external special-functions library object is claimed.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0030v1.pdf) — 2026-07-12T20:21:46+00:00
