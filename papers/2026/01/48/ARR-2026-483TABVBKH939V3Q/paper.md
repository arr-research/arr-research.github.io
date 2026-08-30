# Operational Influence Proxies in a TFIM Surrogate: Non-Monotonicity and a Controlled ω = 0 Witness Floor Mechanism

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2601.0022](https://www.ai.vixra.org/abs/2601.0022)  
**First submitted:** 2026-01-08T22:09:15+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2601.0022-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We study spatial influence detection in a transverse-field Ising chain (TFIM) subjected to localized Markovian noise. Using an operational one-site trace-distance influence proxy computed from TEBD combined with Monte Carlo wavefunction (MCWF) sampling, we test whether remote dissipation produces an identifiable nonzero asymptotic influence offset (a "floor") as a function of separation epsilon. Uncertainties are estimated by trajectory bootstrap and model selection is performed between exponential decay and exponential-plus-offset forms using both BIC and the finite-sample corrected criterion AICc. In the TFIM surrogate regimes explored, we find no robustly identifiable floor for both dephasing and amplitude-damping channels; instead, the influence proxy is non-monotone in separation, consistent with coherent finite-size structure superimposed on average attenuation. To demonstrate that floors can exist as a controlled mechanism independent of fragile spatial fits, we present a Davies/witness stress test: for nonzero zero-frequency bath weight gamma(0) > 0, a commutator witness yields a strictly positive lower bound on an effective decay envelope. Exact-diagonalization calculations show this lower bound is robust to enlarging the observable support and to variations in inverse temperature. v2 adds: a synthetic-injection power analysis showing that over the sampled one-octave window epsilon in [16,32] with n = 5 points, a constant floor is nearly degenerate with a slow exponential -- AICc essentially never detects a floor and even BIC requires D0 ~ 30 sigma -- so "no identifiable floor" is in part a design limitation, now stated as such; a fully declared exact-diagonalization benchmark for the witness (v1 did not record its ED parameters), regenerable from scratch by the shipped suite; a null case showing the witness switches off (kappa_min ~ 1e-29) for couplings with vanishing omega = 0 component; an invariant-subspace caveat for the envelope interpretation; and series cross-references.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2601.0022v1.pdf) — 2026-01-08T22:09:15+00:00
- [v2](https://www.ai.vixra.org/pdf/2601.0022v2.pdf) — 2026-07-05T10:46:14+00:00
