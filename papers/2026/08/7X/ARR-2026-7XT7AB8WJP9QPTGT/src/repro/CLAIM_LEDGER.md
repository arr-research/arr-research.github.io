# Claim ledger

## Certified claim

- For Suzuki's self-adjoint operator representing the global localized Weil
  form on L2(-0.72,0.72),
  A_0.72 >= 5.890 x 10^-17 I > 0.
- By inclusion of smooth compactly supported cores, the same lower bound holds
  for every 0 < a <= 0.72.

## Exact analytic results proved in the manuscript

- Thirteen-cell prime-power partition and its 7+4+2 translation
  components in the third support window.
- Exact nested Gauss-Stieltjes hierarchy, Markov-square remainder, endpoint
  value R_m(1) = H_m, Jacobi resolvent, and positive increment.
- Fixed-support completeness for strict positivity.
- Degree-resolved and multiband Schur majorants.
- Congruence-Gershgorin transport and full block coercivity.

## Priority language allowed

- "Among the primary sources located, this is the first explicit rigorous
  localized coercivity certificate beyond Yoshida's radius (log 2)/2."
- Gaussian quadrature, Pade/Markov theory, Jacobi resolvents, inverse
  antitonicity, and Schur complements are classical.
- The contribution is the source-faithful arithmetic integration and the
  certified endpoint, not those general tools.

## Claims prohibited

- No proof of RH and no positivity claim for a > 0.72.
- No optimality or maximality of the endpoint.
- No strict monotonicity of a -> lambda_a, no simple crossing, and no
  Loewner ordering between operators acting on different L2(-a,a).
- No identification with the semilocal Connes-Consani scaling Hamiltonian.
- No claim that numerical Ritz positivity proves coercivity.
- No claim that zeta zeros are eigenvalues of A_a.
- No claim that Gauss-Stieltjes or Schur theory is new in general.

## Reproducibility gate

The release uses two distinct, audited provenance routes:

1. the aggregate NPZ is conservatively derived from the allowlisted predecessor
   by the fail-closed centred-binary64 upgrader; an independent corrected-source
   replay has identical component midpoints and nonzero aggregate Grams;
2. the degreewise band NPZ is regenerated directly from the corrected source;
3. the final multiband JSON is regenerated from those two proof objects;
4. all registered SHA-256 values match and `verify_release.py` reports PASS;
5. a separately written, non-Arb shadow implementation reconstructs the
   prime-power graph, parity maps, and Schur assembly with positive Weyl
   margins in both sectors;
6. the final PDF is compiled twice, rendered completely, and visually checked.
