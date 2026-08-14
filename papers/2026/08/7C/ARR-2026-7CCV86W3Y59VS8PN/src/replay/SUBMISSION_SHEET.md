# Submission sheet

## Identity

- **Title:** Matroidal Bayes Bounds for General Quantum Process Discrimination: Canonical Compression, Support Congestion, and Exact Qubit Phase Families
- **Author:** Lluis Eriksson
- **Date:** August 2026
- **Suggested field:** Quantum information / mathematical physics
- **Record type:** Research paper
- **Status:** Prepared, audited, and not yet submitted
- **Pages:** 14
- **Figures:** 1
- **Related ARR record:** ARR-2026-6WX2JF38WE87GB2M, *Algebraic Query Support for Unitary Oracles*

## Abstract

Minimum-error discrimination of quantum processes is normally optimized over
testers whose normalization may encode parallel, sequential, or
indefinite-order access.  For a fixed physical deterministic tester
normalization, Moore--Penrose compression maps the tester exactly to a POVM on
normalized effective states and preserves every conditional probability.  We
associate to the support subspaces of arbitrary positive process operators a
Rado matroid on the hypothesis labels and prove that every correct-label
probability vector lies in its independence polytope.  Consequently the Bayes
success probability is at most the prior weight of a maximum-weight
independent transversal, computable greedily.  A robust extension replaces
exact supports by arbitrary positive low-rank cores and charges only the
prior-weighted worst-case discarded tester mass; valid full-rank admixture of
weight eta degrades the certificate by at most eta.  An explicit reduction to
linear matroid intersection supplies pseudocode and an arithmetic complexity
bound.  For rank-one processes this
strictly refines the sum-of-largest-priors dimension bound.  Distinct qubit
phase gates form a rank-two flat, while off-diagonal Pauli gates are coloops,
giving an infinite exactly solved family.  A trine-plus-coloop instance has
exact general-tester optimum 0.70 against a 0.90 total-span relaxation, with a
nonzero decision effect for every hypothesis.  The support theorem is not
claimed universally tight; an identical full-rank mixed-state example shows
the precise limitation.

## Contribution boundary

The paper does **not** claim novelty for canonical tester normalization,
Rado's theorem, Edmonds' polytope theorem, the pure-state top-d-priors bound,
or the symmetric trine PGM.  Its contribution is the support-matroid
organization of correct-label probabilities, its lift to physical general
testers, the strict-prior-prefix equality audit, the spectral-tail robust
extension, the explicit mixed-support implementation, and the exact process
families.

## Reproducibility and disclosure

- Exact replay: `verify_canonical_tester_compression.py`
- Self-contained extracted-package check: `python package_release.py --check`
- AI assistance was used for exploratory algebra, drafting, and consistency
  checks.  The author remains responsible for the claims, proofs, references,
  and final manuscript.
- No peer review, independent replication, Lean certification, or novelty
  guarantee is asserted.
