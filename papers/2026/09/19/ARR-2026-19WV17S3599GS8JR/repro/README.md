# Reproducibility package for "The Grassmannian Degree Law for Passive k-Plane Spectral Routing" (version 2, 8 September 2026)

Environment used for every run below: Windows 11, Python 3.12.6, SymPy 1.14.0, NumPy 2.5.1, SciPy 1.18.0
(no other dependencies; no network access). All scripts are run from *their own directory* (they use
`sys.path.insert(0, '.')`, the reviewer's scripts also `sys.path.insert(0, '../scratch_D2')`, the witness verifier
`sys.path.insert(0, '../scratch_D2')`, and the two `scratch_v2` wrappers `chdir` into `scratch_D2_review`), so keep the
subdirectories side by side and unchanged. Runtimes are wall-clock on a laptop.

Everything numerical in the paper can be reproduced from this folder alone. What each part of the paper rests on:

* **Proofs.** Theorems 1, 5.7, 6.1, 7.4 and Propositions 4.2, 5.4, 7.3 are proved in the text without computation.
  In version 2 the proof of Theorem 7.4 uses the explicit graph witness `Y_i = graph(zeta_i^e I_k)`; the exact random
  witnesses of Table 1 are no longer part of any proof (they confirm the theorem on random data).
* **Exact certificates (Tables 1, 2; Conjecture 7.5 evidence).** `witnesses/*.json` + `witnesses/verify_witness.py`,
  `scratch_D2/grassmann_degree_exact.py`, `scratch_D2/extra_checks.py`, `scratch_D2_review/review_exact_delta.py`,
  `scratch_v2/k3r6_generic.py`. A witness tuple with nonzero wedges at all nodes is an exact upper bound on `delta_Gr`;
  the recorded failure of every tuple of smaller degree sum (a zero `V_e`, or a wedge form that is the zero matrix) is
  an exact lower bound (Lemma A, last form). `review_exact_delta.py` uses a Schwartz-Zippel random test for `k >= 3`
  only; for every `k = 3` instance reported (Table 2) each tuple with a smaller sum contains a zero `V_e`, so those
  verdicts are exact too (see the `dimV` columns in the logs).
* **Symbolic checks of version 2.** `scratch_v2/taller_and_graph_witness.py` (Example 6.2 and the graph witness),
  `taller_check/check_core.py` (the workshop's own script, rerun unchanged).
* **Floating point (Table 3, detector search, Potapov search).** `scratch_D2/inner_interpolant_numeric.py`,
  `scratch_D2/extra_checks*.py`, `scratch_D2_review/review_basepoint_additivity.py`, `scratch_D2_review/review_potapov_search.py`.
  These check the two classical inputs (Fejér-Riesz factor, isometric realization and completion) on concrete
  instances and are not part of any proof; the Potapov search is evidence only (nonconvex).

## Contents

| file | purpose | paper |
|---|---|---|
| `witnesses/<instance>.json` (10 files) | exact data (nodes, frames), `delta_Gr`, column degrees, the two witness columns, and the lower-bound certificate (dimensions of every `V_e` in every failing pair, wedge-form verdicts), all as SymPy strings over `Q(i)` | Table 1, Section 8 |
| `witnesses/verify_witness.py` | independent re-verification of every JSON file (interpolation, rank at nodes, Forney degree, coprime minors, recomputed dimensions, recomputed zero wedge forms) | Section 8 |
| `witnesses/export_witnesses.py` | how the JSON files were produced from `scratch_D2/witnesses.pkl` and `scratch_D2/exact_rerun.log` | - |
| `scratch_D2/grassmann_degree_exact.py` | exact `delta_Gr` for `k = 2` over `Q(i)` (enumeration of column-degree pairs, wedge test), Forney degree of a random witness, base-point example; writes `witnesses.pkl` | Lemma A (last form), Table 1 |
| `scratch_D2/inner_interpolant_numeric.py` | witness -> `M^# M` -> Wilson outer factor -> `F_0 = M H_o^{-1}` -> block-Hankel degree -> ERA -> isometric realization -> unitary completion -> square inner `S`; checks; Klein-quadric detector bound `Delta` | Table 3, Sec. 7.6 |
| `scratch_D2/extra_checks.py` | base point outside the closed disc; `Gr(2,3) = P^2` duality with the `k = 1` law | Tables 1, 3 |
| `scratch_D2/extra_checks2.py` | base point at infinity (leading-coefficient rank drop) | Table 3 |
| `scratch_D2_review/review_exact_delta.py` | reviewer's independent exact `delta_Gr` (own code, own nodes and seeds), all published special cases | Table 2 |
| `scratch_D2_review/review_basepoint_additivity.py` | six extra base-point witnesses through the author's pipeline | Thm 6.1, Table 3 |
| `scratch_D2_review/review_potapov_search.py` | nonconvex least-squares search over all degree-`d` Blaschke-Potapov products (evidence, not proof) | Sec. 8, last paragraph |
| `scratch_v2/taller_and_graph_witness.py` | symbolic verification of the workshop's Example 6.2 (unitarity of `S_1`, `S_2` on the circle, determinants `z`, `z^2`, gcd 1, interpolation values, Hankel-rank degrees 1, 2, 2) and of the graph witness of Theorem 7.4 (`dim V_e' = 0` for `e' < e`, `dim V_e = m_0`, for `k = 2, 3` and `L = 1..12`; Forney degree of `[I; z^e I]`) | Example 6.2, Thm 7.4 |
| `scratch_v2/k3r6_generic.py` | exact `delta_Gr` for random `k = 3`, `N = 6`, `L = 4, 5, 6` with the reviewer's code | Table 2 (last row), Thm 7.4 |
| `scratch_v2/potapov_L3.py` | the `L = 3` stage of the Potapov search, rerun in isolation | Sec. 8 |
| `taller_check/check_core.py` | the AIRR workshop's script (papers 1-3; the paper-3 block is the Theorem 6.1 counterexample), copied unchanged and rerun; writes `checks-core.json` | Example 6.2 |
| `logs_original/` | logs of the original author and reviewer sessions (2026-09-07) | - |

`scratch_D2/witnesses.pkl` is the pickle written by `grassmann_degree_exact.py` (witness pencils as strings); the JSON
files are its readable form.

## Commands, runtimes, expected final lines

```
cd witnesses
python verify_witness.py                 # 16 s.  Last line: ALL WITNESS FILES VERIFIED
                                         #   (per file: "...fdeg=<delta> gcd=1 lower-bound tuples checked=<n>")
python export_witnesses.py               # 2 s.   Rewrites the 10 JSON files from ../scratch_D2/witnesses.pkl (optional)

cd ../scratch_D2
python -u grassmann_degree_exact.py      # 7 min 57 s (2026-09-07 rerun; original 6 min 54 s); per instance 1.4 s (L=3) ... 226 s (L=7)
                                         #   delta_Gr lines: 4, 4, 4, 4 (embedded in C^5), 3, 3, 2, 4, 6, 6; base-point example: gcd z - 1/2, Forney degree 3; last line: done
python -u inner_interpolant_numeric.py   # 50 s.  Last line: SUMMARY: {'random1': True, 'random2': True, 'embedded5': True, 'curve12': True, 'curve12_basepoint': False, 'genericL5': True, 'genericL6': True}
                                         #   (False = the witness with a base point at z = 1/2 compiles to degree 4, not 3, as Theorem 6.1 predicts)
python -u extra_checks.py                # 8 s.   Ends with "Gr(2,3), L=6: delta_Gr = 4 ... dual k=1 projective degree = 4"; base point at z=2: VERDICT True, degree 3
python -u extra_checks2.py               # 3 s.   Base point at infinity: VERDICT True, degree 3

cd ../scratch_D2_review
python -u review_exact_delta.py          # 15 s.  28 instances; last lines: k=3 N=6 L=3 generic ... delta_Gr = 3; done
                                         #   NOTE: the line "word ABABA ... delta_Gr = 6 ... [MISMATCH: expected 4]" is a typo in the
                                         #   reviewer's expectation table (52B6 gives k(L - n_*) = 2(5-2) = 6); the computed 6 is correct.
python -u review_basepoint_additivity.py # 31 s.  Compiler degrees 5, 5, 4, 4, 3, 5 = fdeg(P) + #{zeros of gcd in D}; last line: ##### predicted compiler degree 5
python -u review_potapov_search.py       # 60 min. L=3: best objectives 1.992e+00 (d=0), 9.673e-01 (d=1), 5.96e-30 (d=2);
                                         #   L=4: 0.5721 (d=2), 0.1497 (d=3), 2.96e-30 (d=4)   (see potapov_rerun.log)

cd ../scratch_v2
python -u taller_and_graph_witness.py    # 4 s.   Prints S1^*S1 = S2^*S2 = I on T, det z / z^2, gcd 1, deg 1/2/2, then the dimension table for L=1..12,
                                         #   "k=3, r=6 graph witness: ... OK", and fdeg 2, 4, 6 for e = 1, 2, 3
python -u k3r6_generic.py                # 23 s.  delta_Gr = 6, 6, 9 for L = 4, 5, 6 (column degrees (2,2,2), (2,2,2), (3,3,3)), each "[matches expectation]"
python -u potapov_L3.py                  # 6 min 23 s. Same three objectives as the L=3 stage above

cd ../taller_check
python check_core.py                     # 3 s.   Last line: Paper 3: exact inner-matrix counterexample to the final iff in Theorem 6.1 verified
```

## Reruns and their logs

* 2026-09-07 (while preparing version 1): `*_rerun.log` / `*_rerun.time` next to each script in `scratch_D2/` and
  `scratch_D2_review/` (including the full 60-minute Potapov run, `potapov_rerun.log`).
* 2026-09-08 (version 2): `*_rerun_20260908.log` / `.time` next to each script (`inner_interpolant_numeric`,
  `extra_checks`, `extra_checks2`, `review_exact_delta`, `review_basepoint_additivity`), `witnesses/verify_witness_run.log`,
  `scratch_v2/*_run.log`, `scratch_v2/potapov_L3_rerun.log`, `taller_check/check_core_rerun.log` and `checks-core.json`.
  Every verdict line is identical to the 2026-09-07 run and to the original logs (Potapov `L = 3` objectives identical to
  four digits; runtimes 36/108/232 s versus 25/82/172 s in the reviewer's session).
* `grassmann_degree_exact.py` was not rerun on 2026-09-08 (8 minutes); its 2026-09-07 output is `scratch_D2/exact_rerun.log`,
  and `witnesses/verify_witness.py` re-derives every certificate it produced in 16 s.

## Notes

* The numerical pipeline uses rank tolerance `1e-9` (relative) for the Hankel rank and `1e-8` for the detector
  ranks; the Hankel singular values show a clean gap in every instance (see the logs).
* Nodes are Gaussian-rational points of the unit circle (`(3+4i)/5`, `(5+12i)/13`, ...); target frames are random
  Gaussian-integer matrices with entries in `[-3, 3] + [-3, 3] i` generated by `random.Random(seed)` with the seeds in the
  scripts; all of this is also written explicitly in the JSON files, so the seeds are not needed to reproduce Table 1.
