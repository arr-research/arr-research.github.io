# Independent adversarial referee report

Review date: 2026-08-24.  The referee worked read-only and was instructed not
to assume the author's conclusions.

## Initial verdict on successor draft 0.1

Score: **5.9/10.0**, uncertainty **±0.8**.  Recommendation: **major revision / reject and resubmit**.

The referee found the characteristic-free alternative, the `J(d,m)` bound,
the Frobenius/radicality argument, and the smooth-hypersurface construction
mathematically sound.  One P0 defect made the submitted version unpublishable:
the factorized-polarization corollary applied a proposition about the complete
`H`-embedding to an original embedding that had not been assumed complete.

## Explicit counterexample to the original corollary

The subsystem map

\[
[s:t]\mapsto[s^5+st^4:s^4t+t^5:s^3t^2:s^2t^3]
\]

embeds `P^1` in `P^3` with pullback `H=O(5)=O(2) tensor O(3)`.  Both factors
are very ample.  Nevertheless, the affine tangents at `[1:0]` and `[0:1]`
are both `Span(e_0,e_1)`, so this incomplete embedding has a noninjective
Gauss map.  The factor sections used in the complete system need not lie in
the subsystem defining the original embedding.

The referee's minimal repair was to assume explicitly
`V=H^0(X,H)^*`, or to impose an equivalent product-containment condition on
the original subsystem.

## Findings that passed reconstruction

- The separator `lambda mu^(m-1)` has the required nonzero differential in
  every characteristic without introducing a factor `m`.
- The escape process yields either `d+2` independent first-jet blocks or a
  single original Gauss fiber.
- The arbitrary-support interpolation degrees `2r-1` and `2r`, including the
  parity proof of `J(d,m)`, are correct.
- In characteristic `p`, zero partial derivatives make the minimal form a
  `p`-th power over the algebraically closed field; radicality descends its
  root and contradicts minimal degree.
- Triple-jet interpolation in degree `3N`, the nodal hyperplane section,
  ambient smoothing `F=f+x_0G`, and the final Veronese absorption argument
  are correct as mathematical arguments.

## Requested secondary improvements

- Cite a precise Bertini statement and justify intersection of the Bertini
  open with the affine chart and the conditions `G(p_i) != 0`.
- State the dual identification used in the final span argument.
- Add the base cases in the simplex-lattice induction.
- Say radicality is essential to this proof, unless necessity for the
  statement itself is established.
- Explain why the smooth hypersurface is integral and why quadrics generate
  the local algebra modulo the third power.
- Broaden classical Gauss-map context and keep novelty claims conservative.

The referee estimated **6.7–7.1** after the P0 and these presentation issues
were repaired, subject to a second check.  The post-correction re-audit is
recorded below when completed.

## Post-correction re-audit

The same independent referee rechecked only the repairs and reported that the
P0 is closed.  Updated score: **6.8/10.0**, uncertainty **±0.7**.

Updated component scores were correction 9.0, novelty 4.9 (high uncertainty),
depth 6.5, applications 4.9, verifiability 7.5, and external validation 2.5.
No P0 or logical gap invalidating a theorem remained.  The referee judged the
manuscript internally fit to proceed to genuine external scientific review,
while withholding a definitive publication-ready verdict because priority and
novelty still require specialist external validation.  The final local edit
therefore added a targeted comparison with primary work on `n`-fold tangent
hyperplanes and bitangent loci, but continues to make no exhaustive priority
claim.
