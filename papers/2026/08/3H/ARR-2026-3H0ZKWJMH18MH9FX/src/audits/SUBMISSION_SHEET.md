# Submission sheet

## Work

- **Title:** Strictly Scalable Exterior Decoders for Quantum Lists: Exact
  Full-Spark Widths and Fixed-Probe Weyl Bayes Curves
- **Author:** Lluis Eriksson
- **Type:** independent research paper
- **Status:** release candidate complete; PDF, replay, manifest, and ZIP verified
- **Intended archive:** ARR; deposit explicitly authorized by the author
- **PDF:** 12 A4 pages, 2 tables, 0 figures, 447420 bytes
- **PDF SHA-256:** `bf67bc3c4ae3f0b191c375691c375b93f9fdb3b70ce7f16f031bcb905324e16f`
- **Related ARR record:** ARR-2026-15SJ1ANHDN8D88Z1 (support-matroid bounds and
  the previously published `(4,2,2)` subthreshold fixture; cited as a
  companion; the new formulas strictly generalize that previously reported
  fixture rather than reclaiming it)

## Scope

Building on the known learning-width/factor-width characterization, the paper
proves an exact one-shot retained-list threshold for full-spark
pure-state ray ensembles admitting strictly positive tight representatives,
constructs the threshold POVM from weighted Hodge duals,
gives its physical-space annihilator form and a constructive nullspace
algorithm for `r^2`-outcome compression, and
derives an exact consecutive-support fixed-probe Weyl frontier.  In the branch
`r|d`, a dimension converse and arithmetic-support probe close the global
optimization over all pure Schmidt-rank-`r` probes at `d/r`.  A spectral
theorem gives robust positive error floors below threshold, and the complete
Bayes list curve is solved for the consecutive rank-two Weyl probe.

## Limitations

- The arbitrary-probe optimum is not claimed when `r` does not divide `d`.
- No adaptive, multiuse, LOCC, or indefinite-order claim.
- No complete subthreshold Bayes curve beyond the specified rank-two Weyl
  family; the general robust result is a lower bound, not an exact optimum.
- No extension to arbitrary mixed states or full-spark ray ensembles that are
  not strictly scalable.
- The Python replay is diagnostic, not a formal proof or peer review.
- Priority was audited against the listed primary sources, but novelty is not
  asserted as an absolute `first`.
- General perfect-list feasibility and learning width equals factor width are
  explicitly credited to Johnston--Lovitz--Russo--Sikora (2025).

## Disclosure and assessment

The PDF contains an AI-assistance disclosure.  Scientific correctness was
stress-tested internally and by exact finite replays; independent peer review,
formal-proof certification, and external scientific validation are
`not_assessed`.
