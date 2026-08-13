# Reproducing the support-0.72 certificate

The theorem starts from source commit
`3d997887ccf4e056607c4488a708181db1d507ef` of
`lluiseriksson/riemann-prime-resolvent`.
The release contains a corrected source snapshot, so the adjudication does not
depend on the remote repository remaining available.  The files under
`patched-source/` and `ACCUMULATOR_V2_CHANGES.md` document the delta from the
named upstream commit.  They correct list
accumulation, centre-conversion radii, outward scalar bounds, artifact schemas,
and fail-closed semantic checks.

The full regeneration is intentionally not a laptop smoke test. It was replayed
on a Colab Pro+ CPU runtime with 512-bit Arb arithmetic and
`python-flint 0.9.0`. The final adjudication environment is frozen in
`requirements.txt` and `ENVIRONMENT.txt`.

## 1. Environment

```bash
git clone https://github.com/lluiseriksson/riemann-prime-resolvent.git
cd riemann-prime-resolvent
git checkout 3d997887ccf4e056607c4488a708181db1d507ef
python -m pip install python-flint==0.9.0 numpy scipy mpmath
```

## 2. Canonical aggregate and independent provenance replay

The canonical aggregate is obtained from the allowlisted pre-refactor object
in `provenance-input/` by a deterministic conservative upgrade:

```bash
python upgrade_float_export_v3.py \
  provenance-input/theta-schur-a072-d12-p47-tail8192-v1.npz \
  theta-schur-a072-d12-p47-tail8192-v3.npz
```

That transformation rounds the legacy intrinsic radius upward, adds one ulp
for the stored binary64 centre, rounds the sum upward, and recomputes the exact
rational smooth remainder outward. It cannot narrow any source interval.

An independent corrected-accumulator replay is deposited as
`provenance-input/*overconservative-replay.npz`. Its extra ulp at an internal
roundtrip intentionally prevents it from being the theorem object, but all ten
component midpoint arrays agree exactly with the canonical input and its
aggregate near-band traces are strictly positive. The frozen comparison is
`AGGREGATE_PROVENANCE_AUDIT.json`.

For a direct regenerated object with the v3 source, run:

```python
from experiments.theta_pencil.third_window_schur_certificate import (
    certify_third_window_schur,
)
from pathlib import Path

target = Path("theta-schur-a072-d12-p47-tail8192-v3.npz")
try:
    certify_third_window_schur(
        half_width=0.72,
        low_degree_count=12,
        tail_start=176,
        explicit_end=8192,
        maximum_smooth_power=47,
        tail_balance=0.2,
        residual_balance=0.0001,
        self_remainder_end=32768,
        pointwise_subdivisions=1024,
        precision=512,
        expected_negative_count=0,
        component_cache_path=target,
    )
except ArithmeticError as error:
    # At a=0.72 the intentionally coarse single-floor adjudication is known
    # not to close.  Its source objects are saved before that post-save test;
    # the multiband adjudicator below is the theorem-producing step.
    if not target.is_file():
        raise
    print("expected single-floor nonclosure after cache save:", error)
```

## 3. Independent near-band object

```bash
python -m experiments.theta_pencil.run_arb_third_window_near_tail_checkpointed \
  --half-width 0.72 --degree 12 \
  --boundaries 12 13 14 15 16 17 18 19 20 21 22 23 24 \
  --precision 512 --maximum-smooth-power 47 \
  --cross-map-cache-dir theta-cross-maps \
  --output theta-near-band-a072-d12-to24-by-degree-p512-v3.npz
```

## 4. Final multiband theorem record

```bash
python -m experiments.theta_pencil.third_window_multiband_schur_certificate \
  --component-cache theta-schur-a072-d12-p47-tail8192-v3.npz \
  --band-cache theta-near-band-a072-d12-to24-by-degree-p512-v3.npz \
  --output theta-schur-a072-multiband-to24-by-degree-v3.json
```

## 5. Fast release verification

Place the two NPZ files and the JSON record beside `verify_release.py`, then
run:

```bash
python verify_release.py .
```

The verifier fails on any byte hash, schema, dimension, radius, metadata, or
theorem-record mismatch. It reconstructs the canonical aggregate byte for byte
from the allowlisted predecessor, checks the independent replay midpoints and
nonzero Grams, extracts the frozen v3 source, reruns the multiband adjudicator,
and requires the public conservative positive floors in both parity sectors.

It then runs a separately written shadow implementation:

```bash
python independent_reference_audit.py . \
  --output independent-reference-audit.json
```

This program imports neither the project nor python-flint. It reconstructs the
prime-power graph and parity maps from the printed formulas and independently
reassembles the exported component balls. Its high-precision Weyl margins are
positive in both parity sectors. The shadow audit is a wiring/sign diagnostic;
the Arb adjudicator remains the formal interval proof.

Compressed NPZ archives embed ZIP timestamps, so a fresh replay can be
byte-different while containing exactly the same arrays.  The release includes
`verify_replay_equivalence.py`; use it to compare a fresh replay with the
registered object key by key.  The final JSON is deterministic.
