# Exact finite replays

Run from this directory with:

```powershell
python .\run_all_replays.py
python .\verify_successor_fixtures.py --json > results.json
```

The script uses exact rational Gaussian elimination through Python's
`fractions.Fraction`.  It checks the displayed plane and threefold
simplex-lattice configurations, a small triple-jet interpolation matrix, a
four-point quadratic-Veronese tangent-space fixture, the coincident endpoint
tangents in the incomplete `O(5)` subsystem counterexample, and the elementary
Frobenius zero-derivative pattern in characteristics 2, 3, and 5.

Scope: finite matrix fixtures only.  These computations do not prove Bertini
smoothness, the universal theorems, novelty, or priority.
