# A Machine-Checked Proof of the Amos Bound for Modified Bessel Function Ratios

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0032](https://www.ai.vixra.org/abs/2607.0032)  
**First submitted:** 2026-07-12T13:23:29+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0032-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

Amos's upper bound for the modified Bessel function ratio, rho_n(x) = I_{n+1}(x)/I_n(x) < x/(n + 1/2 + sqrt((n+1/2)^2 + x^2)) = B_n(x), is a classical theorem, and its derivation through the qualitative theory of the associated Riccati equation is an established technique. This paper contributes, to our knowledge, the first formalization: a complete, machine-checked Lean 4 proof of the bound for every integer order n >= 0 and every x > 0, over the power-series definition of I_n carried in the same pinned development, with axiom oracle [propext, Classical.choice, Quot.sound] and no analytic hypothesis of any kind. The formalized route runs through the Riccati equation rho_n' = 1 - ((2n+1)/x) rho_n - rho_n^2 (itself derived from the formalized series calculus), the observation that B_n is exactly the positive root of the Riccati quadratic, a small-argument zone bound uniform in n obtained from pure geometric tail estimates, and a first-crossing barrier argument in a transformed variable psi_n = x(1/rho_n - rho_n) whose structural feature — every touch of the critical level forces rho_n' = 0, so the barrier never needs to be differentiated — is the simplification this formalization contributes. As corollaries, the unit-step inequality, the strict monotonicity of the logarithmic derivative across orders (in deriv form), and a phi-monotonicity step used by a lattice-gauge surface expansion all become unconditional theorems. The theorem is proved for the in-core power-series definition of the integer-order modified Bessel function; no formal identification with an external special-functions library object, and no extension to noninteger order, is claimed.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0032v1.pdf) — 2026-07-12T13:23:29+00:00
