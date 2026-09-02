# Exact Rank Transitions through p=32 — reproducibility bundle

This archive accompanies *Exact Rank Transitions through p=32 and a
Half-Integral Optimum at p=53* (Lluis Eriksson, 2 September 2026).

## Scope

- `verify_exact_frontier_p21_p32.py` checks, with exact `Fraction`
  arithmetic, one feasible primal hive, one matching unrestricted dual, and
  one strict predecessor-rank dual for every `21 <= p <= 32`.
- `verify_p53_independent.py` independently rebuilds the triangular hive
  indexing and verifies the `p=53` primal and both duals without importing the
  discovery or primary replay code.
- `verify_p53_exact_endpoint.py` is the primary exact replay of the same
  theorem.
- `verify_p53_endpoint_nogo.py` checks the integral Farkas refutation of the
  former trace-8843 integer candidate.
- `verify_lr_frontier_bundle.py` checks the frozen integral LR tableaux for
  `4 <= p <= 20` and `p=28`. The exact lower certificates for `4 <= p <= 20`
  belong to the related archived ARR record cited in the manuscript; this
  bundle preserves their extracted states and independently checks the LR
  upper constructions.

The package proves finite statements only. It does not claim an all-parameter
recurrence or classify all minimizers.

## Replay

Use CPython 3.11 or newer from the extracted archive root:

```text
python -I replay/verify_exact_frontier_p21_p32.py
python -I replay/verify_p53_independent.py
python -I replay/verify_p53_exact_endpoint.py
python -I replay/verify_p53_endpoint_nogo.py
python -I replay/verify_lr_frontier_bundle.py
```

Each verifier refuses optimized execution (`python -O`) so that assertions
cannot be silently removed. No network access or non-standard Python package
is required for proof replay.

`MANIFEST.sha256` records the SHA-256 of every preserved file other than the
manifest itself. `tools/package_release.py` deterministically rebuilds the ZIP
from the workspace source paths used for this release.

