# Paper 32 — sharp onset and unbounded self-commutator rank excess

Standalone source and exact replay package for:

> *Sharp Onset and Unbounded Growth of Norm-Optimal Self-Commutator Rank*

Permanent record: `ARR-2026-5QQF95VHTC9GABH8`.

The manuscript absorbs the complete Paper 31 threshold result and strengthens
it in a new direction.  It proves inertia-rank attainment for every traceless
Hermitian target through dimension seven, a sharp dimension-eight failure,
and an exact family in dimension `27t` satisfying

```text
kappa(F_(3t)) = 87t,
17t < r_*(F_(3t)) <= 18t,
r_0(F_(3t)) = 15t.
```

Thus the additive rank excess above inertia is unbounded.

## Reproduce

Use Python 3.12 and install the frozen dependencies:

```text
python -m pip install -r requirements.txt
python run_scientific_replay.py
```

The default runner executes:

1. the canonical exact projected-epigraph certificate for all 33 sign/zero
   strata through `d=7`;
2. a supplemental independent audit that preserves every `cdd` equality flag
   and checks both Farkas orientations;
3. the dependency-free dimension-eight integer witness;
4. the absorbed Paper 30 recursive-Horn replay of the full dimension-eight
   phase and dimension-nine witness;
5. the independent direct-LR replay of the full dimension-eight family;
6. hashes and semantic equality of all frozen JSON artifacts.
7. exact order-18 and order-27 hive primal/dual certificates;
8. two independent exact coarse-grid telescoping replays;
9. the all-`k` endpoint identities and the all-`t` unboundedness theorem.

The Windows/WSL exact `lcdd_gmp` full-rank route is preserved with its vendored
`cddlib` binaries and may additionally be run with:

```text
python run_scientific_replay.py --with-wsl-route
```

It is independent corroboration for nonsingular strata; the canonical
`pycddlib` verifier is the route covering singular strata.

## Consolidation and absorption

The Paper 31 proof objects for the universal threshold, the dimension-eight
onset, and the dimension-nine seed are vendored directly under `math/`.
Paper 30's underlying family sources and frozen JSON streams are preserved
under `repro/absorbed_paper30/`.  No sibling development directory is needed
after extraction.

Build and verify the deterministic archive with:

```text
python package_release.py
python package_release.py --check
```

The ZIP contains `manifest.json`, file sizes and SHA-256 hashes.  Discovery
scripts, caches, LaTeX intermediates and the exploratory Paper 32 amplification
work are deliberately excluded.

The ZIP is byte-deterministic for a frozen input tree.  MiKTeX does not make
the PDF byte-deterministic across fresh rebuilds because its trailer metadata
changes; the release therefore freezes and verifies the exact deposited PDF
hash while source, extracted text, and rendered content remain separately
auditable.

## Proof boundary

The replay certifies finite Horn/polyhedral implications and exact symbolic
coarse-graining conditional on the classical Horn/hive theorem.  It is not
proof-assistant certification, peer review, priority adjudication, a
classification of optimizer matrices, an exact formula for `r_*(F_(3t))`, or
the conjectural complete intermediate rank-cost curve.
