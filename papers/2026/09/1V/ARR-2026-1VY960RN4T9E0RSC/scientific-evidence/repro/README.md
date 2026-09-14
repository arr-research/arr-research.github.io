# Reproducibility scripts for "One Fold if and only if the Overlap Law is Right-Skewed: A Riccati Criterion for Tilted Beta Normalizers" (13 September 2026)

Plain Python 3 (tested with Python 3.12.6, sympy 1.14.0, mpmath 1.3.0 on Windows 11; nothing
else is required). Every script is deterministic and exits with status 0 only if all of its
assertions hold. Symbolic identities are certified with sympy exact arithmetic; mpmath is used
for the numerical scans and tables only (no proof step depends on floating point).

## Provenance

* `sym_riccati.py`, `sym_evenpart.py`, `sym_evenpart_ode.py`, `scan_ac.py`, `scan_evenpart.py`,
  `checks_bounds.py` — copied unchanged from the working directory
  `cycle2/work/B3_onefold_criterion/` of the author agent's report (2026-09-12).
* `reviewer/rev_sym.py`, `rev_num.py`, `rev_even.py`, `rev_last.py` — the independent adversarial
  reviewer's scripts (2026-09-13), copied unchanged from its scratchpad.
* `manuscript_checks.py`, `tables_ac.py`, `run_all.py` — written for the manuscript.

## Commands

    cd repro
    python run_all.py          # everything; writes <name>.out and runtimes.txt; ~13 min
    python run_all.py --fast   # skips scan_ac.py, checks_bounds.py, tables_ac.py, reviewer/rev_num.py

Scripts may also be run individually from this directory (`checks_bounds.py` imports
`scan_evenpart.py`, so run it here).

## Scripts, what they certify, expected final lines, wall times (rerun 2026-09-13)

| script | certifies (manuscript section) | arithmetic | wall time |
|---|---|---|---|
| `sym_riccati.py` | Riccati equation (3.1), H (3.2), Psi', Delta, dG/dk, Psi(1/2); small-kappa coefficients (3.3); the 0F1 reduction (7.1)–(7.2); the (L,S) system of the even part (§3, §4, §7, §8) | sympy exact | 33 s |
| `sym_evenpart.py` | Proposition 8.1(i),(iii): (L,S) system, u^2 k J quadratic in kappa, (s,u) dynamics; small-kappa order of k J | sympy exact | 2 s |
| `sym_evenpart_ode.py` | Proposition 8.1(ii),(iv): second- and third-order ODEs for L_q, the identity H' + (3m+(2q+2)/k)H = Delta_q, symbolic q | sympy exact | 2 s |
| `manuscript_checks.py` | 48 checks: every displayed identity of Sections 2–8, including the chain identities (6.1) with generic K, the integration-by-parts integrand of (5.2), Kummer's second theorem to O(k^10), the c<1/2 repair (k m' = 1-2c at m = 1), the reviewer's coefficients (8.3), L_1, L_2, L_4 identifications | sympy exact | 153 s |
| `scan_evenpart.py` | zero counts of H_q and F_q for q = 1..20, 25, 30, 40, 50, 60; residual of (8.2) at the folds; writes `scan_evenpart.json` | mpmath 30 digits | 4 s |
| `checks_bounds.py` | kappa(1-m) < c-a for a >= 1 and its failure for a < 1; identity (5.2) numerically; sign changes of Delta_q along the trajectory (`delta_signchanges.json`); unimodality of the tilted variance of L_q | mpmath 30 digits | 24 s |
| `scan_ac.py` | the 744-pair scan of Section 9 (zero counts of H and F, fold bounds, Riccati-vs-Kummer agreement); writes `scan_ac.json` | mpmath 30 digits | 146 s |
| `tables_ac.py` | Tables 1–4 of Section 9 with the proved relations asserted in every row (Kummer-derivative route only) | mpmath 40 digits | 160 s |
| `reviewer/rev_sym.py` | reviewer's symbolic re-derivation of T1–T7 of the report | sympy exact | 34 s |
| `reviewer/rev_num.py` | reviewer's independent (a,c) grid, boundary c = 2a, near-boundary, a < 1 counterexamples, sup of kappa(1-m)-(c-a) | mpmath 30 digits | 90 s |
| `reviewer/rev_even.py` | reviewer's numerical checks of the L_q ODEs and identity, sign changes of Delta_q, 0F1 with small c | mpmath 30 digits | 30 s |
| `reviewer/rev_last.py` | reviewer's small-kappa coefficients (8.3), kappa_c for q = 4, small-kappa H checks | sympy; mpmath | 99 s |

Expected final lines:

* `manuscript_checks.py`: 48 lines starting with `OK`, then `ALL OK`.
* `sym_riccati.py`, `sym_evenpart.py`, `sym_evenpart_ode.py`: the printed identities, no assertion error.
* `scan_ac.py`: `ANOMALIES: 0`.
* `scan_evenpart.py`: one line per q with `nH`, `nF` equal to 0 for q <= 3 and 1 for q >= 4.
* `checks_bounds.py`: `holds` for a >= 1.5 and `FAILS` for a < 1 (a = 1 prints a 1e-28 excess: the bound is sharp but never attained); one sign change of Delta_q for q >= 4, none for q <= 3.
* `tables_ac.py`: the four tables of Section 9 (values to 10 digits), `runtime s: ...`.
* `reviewer/rev_sym.py`: residual-zero lines; `reviewer/rev_num.py`: every grid line ends with `OK`; `reviewer/rev_last.py`: the coefficients `[k^2]= -4*(2*q + 5)*(q**2 - q - 8)/(...)` and `[k^3]= -4*(q**2 - q - 8)/(...)`.

The `.out` files from the rerun of 2026-09-13 are included, together with `scan_ac.json`,
`scan_evenpart.json`, `delta_signchanges.json` and `runtimes.txt`.
