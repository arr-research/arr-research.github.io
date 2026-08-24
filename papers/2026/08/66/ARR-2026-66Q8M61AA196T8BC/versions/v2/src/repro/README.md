# Exact finite replays

Run from this directory with:

```powershell
python .\run_all_replays.py
python .\verify_higher_osculating_bounds.py --json
```

The verifier uses exact integer arithmetic, rational Hasse-jet matrices, and
modular Gaussian elimination. It checks:

- the exact binomial floor against the legacy mixed floor in 250 cases,
  including 180 strict-dominance cases with `d >= 2` and `s < m`;
- 250 brute-force checks of the legacy convex-packing formula;
- three independent higher-jet block matrices over the rationals;
- four unisolvent evaluation matrices over `F_2`, `F_3`, and `F_5`;
- three local substitutions witnessing `y in m^(s+1)` in small finite
  characteristics; and
- the rational-normal-curve obstruction below `m >= 2s+1`, through `s = 8`.

`results.json` is emitted with canonical LF line endings. The runner regenerates
the output in a temporary directory and requires byte-for-byte equality.

Scope: these are finite diagnostic witnesses. They do not prove the incidence
dimension estimates, existence or smoothness of the general hypersurface, the
universal theorems, novelty, or priority.
