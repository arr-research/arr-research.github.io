# Hostile proof audit — v4

Date: 2026-08-30

Verdict: **PASS within the stated scopes**. This is an AI-assisted adversarial audit, not formal verification or independent peer review.

## Exact inverse-radius phases

- The kernel identity is correct in every `d >= 3` by dominated convergence. In `d=2`, splitting at `|s|=q/2` and using exponential localization controls the angular boundary singularity and gives both `q^3 J(q) -> m_2` and `sup_q q^3 J(q) < infinity`.
- Tonelli plus `s=q|t|` gives the exact factor
  `B((1-a)/2,(d-1)/2) M_{a+1}(h)/2`; no factor of two is missing.
- For `0<a<1`, the local-density majorant is integrable and the contribution of `R >= eta` is `O(r^-3)`, negligible after `r^(a+2)` scaling.
- At `a=1`, the logarithmic Cesaro limit is `m_2 log r`, giving the exact coefficient `c_d c m_2`.
- At `a>1`, the local density makes `E R^-1` finite and the preceding spherical theorem applies.

## Explicit high-confidence lower tail

- The second moment of `T=n^-1 sum A_i^2Y_i^2` is exactly bounded by `rho^2(1+3 chi/n)`.
- Paley--Zygmund contributes `1/[4(1+3 chi/n)]`; the elementary Gaussian lower tail contributes `3/10`, giving `3/[40(1+3 chi/n)]` and `3/80` when `n>=3 chi`.
- The substitutions
  `L_p=m_0(2p)/[2 phi(0)m_0(p)^2]` and
  `K_p=4m_0(4p)/[phi(0)m_0(2p)^2]` are correct.
- The small-`n` slab dichotomy gives the declared explicit `delta_p^hc`; its numerical values are extremely conservative and are labeled as proof ranges.

## Spectral lexicography

- Cauchy--Binet on exterior powers shows that after normalization only the first `k` sample columns in increasing `|Z_i|` order survive. This creates the eventual spectral gaps and the full upper flag.
- The selected tangential matrix is iid Gaussian and independent of the ordered scores. Its normal is proportional to `(-Y_*^-1 zeta,1)`.
- Rotational invariance and conditioning on rows `2,...,m` give the exact law `||Y_*^-1 zeta|| =_d ||zeta||/|G|`.
- The half-normal Markov and Chernoff arguments yield the displayed constants, including `exp(-1/2)/(24 sqrt(2))` and `8 exp(1/2)`.
- The matching `1/delta` statement is restricted to the theorem's confidence range. The manuscript states the required order of limits and does not claim a joint finite-`r`, growing-`n,d` rate.

## Remaining genuine open points

- A uniform joint rate for `r,n,d` in bottom-projector recovery remains open.
- The shell theorem still uses a conservative Euclidean net; no model-specific marked-kernel lower bound is claimed.
- No labeled estimator or minimax parameter theorem is inferred from the oracle Gram results.

