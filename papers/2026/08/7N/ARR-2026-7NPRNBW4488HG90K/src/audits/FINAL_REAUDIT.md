# Final independent mathematical re-audit

Original audit date: 2026-08-24  
Final source recheck: 2026-08-30

## Verdict

**PASS — unconditional.**

Final audited canonical source:

```text
paper.tex
SHA-256: 9D7E1A2E32B395343D66A7FEB80A9B06B694D03607D3755587422B4A5451C2BA
```

The `F=0` guard now appears at the start of Lemma 2.1, before reciprocal
scaling or division by `||H||^2`, and disposes of both minima and the
orthogonal-pair assertion.  The guards at the starts of Theorems 5.1 and 5.2
likewise precede their projection and Gram shear.  The nonzero arguments then
have nonvanishing directions and denominators.

All earlier findings are resolved.  The all-target cumulative-sum shift,
attainment, polar singular-floor removal, Horn-tail inequalities, optimizer
rigidity, sign reflection, zero padding, repeated eigenvalues, `n=1` boundary,
Gini identity, sharp stability constants, triangular sign and factor,
four-kick diagonal identity, corrected Gram chain, square attainment,
switching ratio, examples, theorem scopes, and provenance qualifications are
internally consistent.  No residual P0/P1 issue or actionable mathematical
correction remains.

The 30 August source recheck additionally covers Corollary 4.2.  Its strict
Schur-concavity statement follows directly from
`kappa(F_b)=nP-sum_{k=1}^{n-1} B_k`: majorization increases every proper
prefix sum, and equality of the costs forces equality of their total deficit;
because every prefix deficit is nonnegative, all prefixes, and hence all
coordinates, coincide.  The added `23.02%` switching reduction is the decimal
evaluation of the exact ratio already proved in Corollary 5.4.  These additions
introduce no new imported theorem or numerical approximation into a proof.

This is a mathematical source audit, not external peer review, formal proof
certification, a priority guarantee, or publication authorization.
