# Exact finite replays

Run from this directory with:

```powershell
python .\run_all_replays.py
python .\verify_higher_osculating_bounds.py
```

The verifier uses integer arithmetic and exact Gaussian elimination through
Python's `fractions.Fraction`. It checks:

- the identity `B(d,1,m)=J(d,m)` for `1 <= d <= 8`, `1 <= m <= 60`;
- the curve identity `B(1,s,m)=m+1` for `1 <= s <= m <= 60`;
- 250 brute-force convex-packing instances;
- a finite range of strict asymptotic-coefficient comparisons;
- four rational-normal-curve value/jet matrices;
- simplex-lattice top-order fixtures for `(d,m,s)=(2,2,2)` and `(3,3,3)`,
  using multivariate Hasse derivatives.

`results.json` is the saved exact output. The package audit requires it to
match a fresh run semantically.

Scope: these are finite arithmetic checks. They do not prove the universal
geometric theorem, literature priority, or novelty.
