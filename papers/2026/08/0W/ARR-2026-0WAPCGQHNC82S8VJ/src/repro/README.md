# Exact replay

Run:

```powershell
python .\verify_dual_multiplicity.py --output .\results.json
python .\run_all_replays.py
```

The verifier uses only Python's standard library and exact integer/Fraction
arithmetic. It checks finite simplex-lattice evaluation ranks, monomial
Jacobian quotients for the ordinary local model
`sum_i x_i^(s+1)`, numerical branch/multiplicity/tangent-cone totals, and a
100-case grid showing that the predecessor's rank term collapses on a Gauss
fibre at its threshold.

These are diagnostic fixtures. They do not prove the incidence constructions,
Gauss normalization, the universal theorem, the classical
multiplicity--Milnor formula, novelty, or priority.
