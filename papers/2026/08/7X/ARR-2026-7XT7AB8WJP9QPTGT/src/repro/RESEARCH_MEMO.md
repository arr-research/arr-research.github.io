# Paper 17 research memo

## Provisional title

**Certified Localized Weil Positivity Through Support 0.72: Multiband Schur Complements and a Complete Stieltjes Hierarchy**

## Central result

For Suzuki's localized Weil operator `A_a`, defined only as the self-adjoint
operator associated with the closed global localized form `Q_W^a` on
`L^2(-a,a)`, in the normalization fixed at
`riemann-prime-resolvent` commit
`3d997887ccf4e056607c4488a708181db1d507ef`, the source-level Arb chain is
intended to prove

```
A_0.72 >= 5.890e-17 I > 0.
```

Extension by zero of the test space then yields strict positivity for every
`0 < a <= 0.72`.  This is a bounded-support theorem.  It is not RH, since
the localized Weil criterion requires nonnegativity at every support.
This statement is not an identification with the semilocal Connes--Consani
operator, whose sign, constraints, and principal-value normalization differ.

## Analytic contributions packaged with the certificate

1. The logarithmic boundary potential has the exact Stieltjes representation

   `V(x) = -1/2 log(1-x^2) = 1/2 integral_0^1 x^2/(1-t x^2) dt`.

2. Its `m`-node Gauss--Legendre approximant `R_m` is an increasing lower
   hierarchy.  The Markov remainder is an exact continuous square, and the
   increment `R_{m+1}-R_m` is one explicit Schur square.

3. At fixed support, monotone form convergence and compact resolvent give
   `lambda_k(L_{a,m}) -> lambda_k(L_a)` increasingly.  Hence strict
   positivity at fixed support has a terminating Stieltjes certificate.

4. If a complement obeys

   `D >= sum_{n>=N} d_n P_n`, `d_n=H_n+c>0`,

   then inverse antitonicity yields the degree-resolved Schur correction.  A
   geometric partition in the denominators gives a `(1+epsilon)` Loewner
   majorant using only `O_epsilon(log log M)` bands through degree `M`.

5. The support-0.72 closure uses low degree 12, tail start 176, explicit end
   8192, smooth order 47, 512-bit Arb balls, and the split
   degreewise `[12,13),..., [23,24)`, then `[24,176), [176,infinity)`.

## Completed release gates

- The aggregate NPZ was conservatively upgraded from the allowlisted
  predecessor.  A corrected-source replay independently reproduces all ten
  component midpoints and nonzero aggregate Grams; it is a provenance audit,
  not an interval-inclusion replacement for the canonical object.
- The degreewise band NPZ was regenerated directly from corrected source.
- Registered SHA-256 values, schemas, interval semantics, provenance, the
  multiband JSON, and a fresh Arb readjudication are checked fail-closed by
  `verify_release.py`.
- A no-project-import, non-Arb shadow auditor independently reconstructs the
  eleven translation edges, both parity isometries, the residual-band sign,
  balance factors, and the complete Schur assembly. Its positive Weyl margins
  are diagnostic corroboration; the Arb route remains the theorem proof.
- The operator normalization and nested-core support monotonicity were
  independently audited.
- State monotonicity as `lambda_{a'} >= lambda_a` for `a'<=a`; do not compare
  `A_{a'}` and `A_a` directly because they act on different Hilbert spaces.
- Audit priority against Suzuki (arXiv:2606.09096), Kim et al.
  (arXiv:2607.24830), and related localized Weil computations.
- State all limitations prominently and avoid any RH claim.

## Registered release objects

The final hashes are frozen in the release verifier and manifest.  The legacy
v1 aggregate is included only as an allowlisted provenance input; invalidated
v1/v2 certificates and stale source documentation are excluded from the
release.
