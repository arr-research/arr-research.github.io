# Claim ledger — final two-query paper

## Green: proved in the manuscript

- The 24 reverse echoes share the half trace
  `q(z)=1-32z^2+128z^3-256z^4` and split into two free 12-label `A4` orbits.
- One-query channel discrimination is globally solved for 12 or 24 equal-prior
  labels by `(|q|+sqrt(3(1-q^2)))^2/N`.
- The Bell-square two-copy frame has generic rank nine and the exact spectrum
  stated in Proposition 4.1. Its optimum is the scalar-clamp formula in
  Theorem 4.2; the pretty-good measurement is not generally optimal.
- Every two-query parallel input, including arbitrary references, is optimized
  by Theorem 5.1. At `q=1/2`,
  `P_parallel=(5+sqrt(15))/24` and the optimal singlet weight is
  `(5-sqrt(15))/10`; two Bell pairs are strictly suboptimal.
- Any causally ordered two-query protocol has output span at most nine, hence
  success at most `9/24=3/8`.
- At `q=1/2`, the displayed rational comb normalization, algebraic orbit
  weights, and exact identity `K C K=K` attain `3/8`.
- The same comb has the explicit six-Kraus realization in Appendix C.
- Therefore the adaptive advantage over every parallel strategy is exactly
  `(4-sqrt(15))/24>0`.
- Keeping that causal tester fixed proves a strict advantage throughout
  `|y-y_*|<(4-sqrt(15))/(1536 sqrt(3))`; the phenomenon is not isolated.
- The collision table is exhaustive on `0<=z<=1/3`; the adaptive point is
  generic and has 24 distinct physical channels.
- The central causal certificate is replayed exactly in
  `Q[t]/(t^8+12t^6-10t^4-20t^2-239)` without an SDP or random search.

## Yellow: scope qualifiers

- “Causal” means ordinary causally ordered two-query circuits, allowing
  adaptive coherent memory and delayed final measurement.
- The task is minimum-error identification of a uniformly random order label.
  At collision points, repeated labels remain repeated hypotheses.
- The dimension-nine obstruction is specific to the common-trace,
  common-norm tetrahedral echo family.
- The exact causal optimum is proved at the algebraic pulse `q=1/2`; the open
  interval proves advantage but not the exact causal optimum away from it.
- The architecture is noiseless and finite dimensional.
- The word/collision and representation scripts mix symbolic calculations with
  floating-point diagnostics and explicit tolerances. They corroborate, but do
  not replace, the analytic universal proofs in the manuscript.

## Red: prohibited claims

- No indefinite causal order, quantum switch, or causal nonseparability.
- No noisy-hardware, metrological, communication, or computational advantage.
- No universal theorem that adaptive strategies beat parallel ones.
- No claim that the 24 words form a unitary group or a single `A4` orbit.
- No novelty claim for Yuen–Kennedy–Lax, group-covariant discrimination,
  quantum combs, or generic unitary-design bounds.
- No absolute priority claim. The new contribution is the exact synthesis for
  this non-group echo family, especially the rational adaptive certificate and
  closed parallel-versus-causal separation.
