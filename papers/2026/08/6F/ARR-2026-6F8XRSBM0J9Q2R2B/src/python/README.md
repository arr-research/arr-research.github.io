# Python replay

Run from this directory with Python 3:

```text
python verify_orbital_metastability.py
```

The bounded replay checks exact moment, Taylor, threshold, and tail identities; evaluates the explicit torus criticality counterexample; and performs a finite Bessel-positivity diagnostic. Its frozen output is `orbital_metastability_verification.json`.

The replay is supporting evidence, not a formal proof or an independent scientific validation. It runs without pools, network access, or heavy branch-and-bound computation.
