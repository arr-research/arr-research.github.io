# Reproducibility package for "The inverse self-commutator cost at inertia (m,2)" (version 2, 8 September 2026)

Everything needed to reproduce every numerical or exact claim of the manuscript is in this directory. All scripts
live at the top level (the reviewer's scripts import the author's modules `layer_chain`, `conj_formula`, `lr`,
`check_horn_lp`, `hive_core` by plain `import`, so keep them together; the subfolders `author/` and `reviewer/` are
archival copies of the original exploration and review scripts; the leftover `sys.path.insert(0, "../research/scratch_A2")`
lines in `rank_more.py`, `lp_checks.py`, `adversarial.py` are harmless no-ops here).

Dependencies: Python 3 (tested with CPython 3.12 on Windows 11, one core), `numpy`, `scipy` (HiGHS via
`scipy.optimize.linprog`), `sympy`. Everything exact uses `fractions.Fraction` or sympy; floating point is used only
where the text says so (LP cross-checks, explicit matrices built from eigen-decompositions).

Quick start (about 70 s):

    python run_all.py        # writes logs/<name>.log for every script below and logs/timings.txt
    python run_extra.py      # optional, about 60 s: adversarial.py and lp_checks.py

## Data files (`data/`, `logs/`)
| file | content |
|---|---|
| `data/rank4_optimizer_exact.json` | the rank-4 optimizer C of Section 7 for lambda = (2, 2, 3/2, 0, -5/2, -3): every nonzero entry as an exact sympy expression (Q-combinations of square roots of integers) and to 30 significant digits; cost 15/2; common spectrum (13/4, 5/2, 3/2, 1/4, 0, 0); float64 residual 1.42e-15; residual of the 4-decimal print 2.149e-4 |
| `data/rank4_optimizer_30digits.txt` | the same 6 x 6 matrix, 30 significant digits, row-major, basis order (-b2, -b1, a1, a2, 0, a3) |
| `logs/taller_check_horn.json` | output of the workshop's `check_horn.py` rerun on this machine (identical numbers to the workshop's `evidencias/TALLER-0004.json`) |

## Scripts, commands, measured runtimes (2026-09-08) and expected final lines
| command | s | role | expected last line(s) of `logs/<name>.log` |
|---|---|---|---|
| `python lr.py` | 1.9 | LR coefficients by tableau counting; LR>0 == Fulton recursion for d<=7 (counts 3; 6,6; 10,21,10; 15,56,56,15; 21,126,228,126,21; 28,252,751,751,252,28); Pieri triples c=1 for d<=12 | `d=12: shifted-pair triples i=2..8: ... all c=1` |
| `python verify_mn2.py 8` | 4.7 | PART1 certificates (m<=8, z in {0,1,2}, 675 triples, membership in T^d_r for d<=8), PART2 regions/chambers (400 exact points per m), PART2b explicit C (60 points per m, residual <= 2e-8), PART3 d=4/d=5/one-spike | `ALL CHECKS PASSED` |
| `python layer_chain.py 13 300` | 2.8 | exact interval recursion; 300 random exact stratum points per m<=13 | `m=13: 300 samples, failures=0, ...` |
| `python my_construct.py` | 0.2 | reviewer's 2x2-block constructor; the rank-4 counterexample (float) | `resid=4.80e-15 cost=7.500000 rank=4  common spectrum s=[3.25 2.5 1.5 0.25 0. 0.]` then the 4-decimal matrix |
| `python rank_test.py` | 1.1 | exact Horn feasibility of s(t)=(7/2-t,5/2,3/2,t,0,0), t=0,1/2, all 522 inequalities of d=6; LP max of s_4 at cost 15/2 | `LP max s_4 at cost<=Phi: 0.5 ...` |
| `python rank_more.py` | 24.9 | rank-(m+1) optimizers for m=3,5,7 (z=1); 332 matrices at boundary points m=6,9,12 (worst 8.4e-9); exposed-form counts 2,5,6,8,9,11,12,14 | `m=9: unique-argmax forms = 14 (predicted 14); missing: []` |
| `python my_cert.py` | 1.3 | reviewer's re-derivation of all 168 certificates (m<=7, z in {0,1,2,5}); write-outs for m=4; the nine certificates with a +s_{m+1} term (G3, G5, G7 at z=1,2,5); every Weyl row is `I=(j,) J=(1,) K=(j,)` | `certificates checked: 168` then the nine loophole certificates |
| `python symbolic.py` | 1.4 | sympy: tail-sum == closed forms, chamber differences, layering costs, one-spike limit (m<=9); d=4 and d=5 identifications | `m=9: ... all identities hold symbolically` then the d=4/d=5 term lists |
| `python nonunique_check.py` | 0.1 | exact Horn feasibility (own generator) of the two optimal families of Theorem C'(4) | five lines ending in `violated=None` |
| `python d5_dominated_terms.py` | 1.1 | the seven dominated d=5 terms and their nonpositive corrections | `rho q6 = a1 + 2*a2 - b2   -> ('F1', -2*a3)` |
| `python exact_rank4_matrix.py` | 1.7 | **(v2)** closed-form rank-4 optimizer; asserts `C C^T - C^T C - 2F == 0` exactly in sympy; writes `data/` | `exact residual ... : True; cost 1/2||C||^2 = 15/2 ...`, `float64 residual of the exact entries: 1.42e-15 ; residual after rounding to 4 decimals: 2.149e-04 ; rank 4` |
| `python coverage_exact.py 10 40` | 8.1 | **(v2)** exact coverage grid, 2<=m<=10, 9567 points (every breakpoint E_k, E_1-g_j, b1=b2, midpoints, uniform grid, b2->0; flat/strict/tied/geometric/dominant-gap/tiny-a_m spectra): checks (i)-(vii) listed in the docstring (Prop. 5.4 regions, Prop. 5.5 coverage, Theorem B chambers, Theorem C'(3),(4), G-activity criterion of Section 6) | `ALL COVERAGE CHECKS PASSED: 9567 exact points, m <= 10` |
| `python pieri_triples_search.py 9` | 15.7 | **(v2)** exhaustive Fulton enumeration of T^d_r (d<=9): all Horn triples sharing the s-form of (Pi)_i (6; 12,40; 32,24; 94,48,160), the Pieri triple is the only one with right side A_i; full vs Lidskii-Wielandt-only Horn LP at G-chamber points, d=6,7 | `d=9 i=6: 160 Horn triples share the s-form s_5+s_8-s_8 ... it is not of Lidskii-Wielandt type`; earlier lines `... Lidskii-Wielandt-only LP falls short by up to 11.1% of Phi` (d=6,7, m=3), `10.1%` (m=4), `3.9%` (d=7, m=5) |
| `python taller_check_horn.py` | 3.5 | **(v2)** the workshop's own script, verbatim (writes `checks-horn.json` next to itself; `run_all.py` moves it to `logs/taller_check_horn.json`) | JSON with `"lp_total_cases": 200`, all `max_abs_error` <= 7.2e-15, `"printed_rounded_matrix_residual": 0.000214919...` |
| `python adversarial.py` (run_extra) | 2.5 | 2708 exact boundary-heavy points, own vs author feasibility (0 mismatches), 400 matrices (worst 2.3e-14) | `no-feasible=0 ... mismatches=0` |
| `python lp_checks.py` (run_extra) | 54 | own float Horn LP at 9 x 600 points == Phi; dual gradients; uniqueness scans (0/60, 0/60, 0/80, 3/80, 2/40, 37/60) | as quoted in Section 7 of the paper |

Timings are wall-clock on one core (`logs/timings.txt`, `logs/timings_extra.txt`). Float residuals are reported at the
1e-14 level except at exact tie points (up to 2e-8, 8.4e-9), where the eigensolves are ill-conditioned; the exact
matrix of Section 7 has residual exactly zero.

## Which script backs which claim of the paper
| claim | script(s) |
|---|---|
| Lemma 4.1-4.3 triples are in T^d_r, LR coefficient 1 | `lr.py`, `verify_mn2.py` (PART1), `my_horn.py` via `my_cert.py` |
| Section 4.1: triples sharing the Pieri s-form; Lidskii-Wielandt-only LP is insufficient | `pieri_triples_search.py` |
| Propositions 4.4-4.5 certificates (all m<=8) and the m=4 write-outs | `verify_mn2.py` (PART1), `my_cert.py` (+ `my_cert.log`) |
| Lemmas 5.1-5.3, Proposition 5.4 regions, Proposition 5.5 coverage | `layer_chain.py`, `my_construct.py`, `verify_mn2.py` (PART2), `adversarial.py`, `coverage_exact.py` |
| Theorem B chambers, exposed-form counts 2,5,6,8,9,11,12,14, G-activity criterion | `symbolic.py`, `rank_more.py`, `coverage_exact.py` |
| Theorem C'(3): rank-(m+1) optimizers; the exact matrix of Section 7 | `rank_test.py`, `rank_more.py`, `my_construct.py`, `exact_rank4_matrix.py`, `coverage_exact.py` (check v) |
| Theorem C'(4): non-unique optimal spectra | `nonunique_check.py`, `lp_checks.py`, `coverage_exact.py` (check vi) |
| Section 8: d=4 and d=5 formulas, one-spike limit | `symbolic.py`, `d5_dominated_terms.py`, `verify_mn2.py` (PART3) |
| LP == Phi (float cross-checks) | `lp_checks.py`, `conj_formula.py`/`hive_core.py`, `taller_check_horn.py` |

## Author's exploration scripts (original names kept)
`conj_formula.py` (the forms), `lr.py`, `layer_chain.py`, `verify_mn2.py`, `hive_core.py` + `mn2_forms.py` (hive LP and
extraction of exposed forms from duals, the origin of the conjecture; `python mn2_forms.py 2 5 200 0,1,2`),
`check_horn_lp.py` + `horn_duals_pad.py` (Fulton generator `horn_t`, full Horn LP and dual certificates;
`python horn_duals_pad.py m pad [seed]`).

## Reviewer's scripts (independent implementations)
`my_horn.py`, `my_cert.py` (+ `my_cert.log`), `my_construct.py`, `rank_test.py`, `rank_more.py`, `symbolic.py`,
`adversarial.py`, `lp_checks.py`, and the reviewer's reruns `rerun_lr_verify.log`, `rerun_layer_chain.log`.
