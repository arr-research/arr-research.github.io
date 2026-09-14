# Reproducibility package for "The inverse self-commutator cost at inertia (m,n): ordered-layering bounds, interlacing chains, and the Horn tiles that certify them" (14 September 2026)

Layout:

- `author/` — verbatim copy of the author's working directory `cycle3/work/A5_general_mn/` (scripts, the JSON files
  `forms_m{m}_n{n}_z{z}.json` holding the computed sets S(m,n,z), and the original logs), plus the four Fulton-triple
  pickles `horn_d6..9.pkl` copied from `cycle2/work/A3_inertia_m3/`. The only modification is one marked line (`REPRO`)
  in `horn_lp.py`, which now looks for the pickles in its own directory. The scripts import each other by plain `import`
  and read/write data files in their own directory, so run them **from inside `author/`**.
- `reviewer/` — the adversarial reviewer's independent scripts and logs (`myhorn.py`: own Fulton recursion for T^d_r,
  own LR counter, own Horn LP; `test_thm1.py`, `test_thm2AB.py`, `test_oq1.py` with their logs `thm1.log`, `thm2AB.log`,
  `oq1.log`). The only modifications are two absolute paths replaced by package-relative ones (marked `REPRO`, in
  `test_oq1.py` and in the `__main__` block of `myhorn.py`). `myT_9.pkl` (created on first use) caches the reviewer's
  T^9_r. Run these **from inside `reviewer/`**.
- `exact_oq1.py` — written for the manuscript (Section 6): reproduces the reviewer's two chamber points, rationalises
  them, reconstructs exact primal-feasible vertices of the restricted Horn LPs (box <= 3; Pieri-type class) and verifies
  in `fractions.Fraction` arithmetic that their objective is below g(lambda) (weak-duality certificate that no
  certificate from that class exists); then verifies both tiling certificates of Section 6 exactly (membership in T^9_r,
  LR coefficients by the reviewer's and the author's implementations, integer tiling identities). Run from `repro/`.
- `run_fast.sh` — the fast reruns made for the manuscript; `logs/` their outputs and `logs/timings.txt` the wall-clock
  times (one core, Python 3.12.6, numpy 2.5.1, scipy 1.18.0 / HiGHS). `forms_mn.py` is not rerun because it overwrites
  the JSON data files.

Dependencies: Python 3.12, `numpy`, `scipy`. Everything labelled EXACT in the outputs uses `fractions.Fraction` or integer
arithmetic; all LPs are floating point (HiGHS).

## Quick start (about 8 minutes)

    bash run_fast.sh      # writes logs/*.log and logs/timings.txt

## Author's scripts (in `author/`), commands, measured runtimes, expected final lines

| command | s | role (manuscript section) | expected output |
|---|---|---|---|
| `python ol_test.py "3,2,0;4,2,1;3,3,0;3,3,1;4,3,0" 300 1` | 4 | Theorem 1 / Lemma 3.2 numerically (4, 8.1) | every line `max(OL-kappa)<=2e-15`, `kappa=OL` = `kappa=OL_A` (e.g. 181/300, 193/300, 66/300, 59/300, 116/300) |
| `python ol_test.py "4,4,0;5,4,0;5,3,0;6,3,1;5,5,0" 400 2` | 29 | same, larger strata | `kappa=OL` at 51, 98, 174, 215, 31 of 400 |
| `python interlace_test.py "4,2,0;...;5,5,0" 60 3` | 14 | Theorems 2A, 2B numerically (5) | `max|cost(L_k)-kappa| <= 2.2e-15`; `kappa_7 = 23.000000 vs ... 24 -> strict subadditivity: True`; `additive at 182/200` |
| `python region_coverage.py "4,2;6,2;4,3;6,3;5,4;7,4;6,5" 400 3` | 9 | coverage of the union of the R_k (5.2 Remark (c)) | `(6,3): in some R_k: 67 ... some L_k is an argmax: 92`; `(7,4): 13 ... 35` |
| `python pure_chain.py n m N seed` (2 6 400 1; 3 6 400 1; 4 8 300 1) | 1–2 | Section 5.3 | `feasible but violating majorization: 0`; for n=2 also `violating G1: 0` |
| `python inv_rule.py "3,3,0;...;5,5,0"` | 1 | structural rules R1–R5 (8.1, 8.3) | `R1..R5: N/N` except R2 (inversion balance) at z=0: 18/19, 26/27, 60/63, 59/62, 87/92 |
| `python d8_example.py` | 2 | Section 7 | `kappa=13.000000`, two tied forms, `minimal optimal rank = 5`, family c=0.8..3 |
| `python chain_lp.py "3,3,0;...;5,5,0" 300 7` | 19 | Section 8.2 | 13 lines `chain-feasible at 300/300` |
| `python form_boxes.py m n z` (3 3 0; 4 3 0; 5 3 0; 4 4 0; 5 4 0) | 1–24 | per-form B_min (6) | histograms `{0: 6, 1: 4}`, `{0: 10, 1: 5, 2: 4}`, `{0: 13, 1: 9, 2: 3, 3: 2}`, `{0: 14, 1: 8, 2: 10}`, `{0: 21, 1: 13, 2: 19, 3: 8, 4: 2}` |
| `python horn_boxes.py "3,2,0;4,2,1;3,3,0;3,3,1;4,3,0;4,4,0" 60 1` | 10 | random-point box counts and shapes (6) | `max|HornLP-hive| <= 1e-15`, B_min histograms as in `author/misc_runs.log` |
| `python forms_mn.py m n z N` (not in `run_fast.sh`) | 4–60 | discovery of S(m,n,z) (8.1); OVERWRITES `forms_m{m}_n{n}_z{z}.json` | counts 10, 19/18, 27/26, 34, 32, 63/62, 62, 92, 108 (`author/forms_all.log`) |
| `mn_tools.py`, `joint_lp.py`, `horn_lp.py`, `hive_core.py`, `check_horn_lp.py`, `lr.py`, `lr2.py` | | libraries | |

## Reviewer's scripts (in `reviewer/`)

| command | s | role | expected output |
|---|---|---|---|
| `python test_thm1.py` | 64 | exact check of the Theorem 1 certificate for all schedules of six strata (28, 28, 43, 157, 251, 61); random points; Proposition 3.3 | `certificate of Theorem 1 verified exactly ... for N schedules` (6 lines); `max(OL-kappa)<=4.4e-16`; `kappa_4(1,1,-1,-1): own LP 2.000000` |
| `python test_thm2AB.py` | 54 | explicit weighted shifts (2A) and interlacing chains (2B) | residuals `<= 6.2e-16` (2A), `<= 1.6e-15` (2B), `rank C in [m]`; `R_k has EMPTY interior` exactly for k > m-n+1 |
| `python test_oq1.py` | 177 | Theorem 3 (box counts, exact vertex for g=(3,1,1,2,2;-2,-1,0)), (5,3,0) histogram, exposed sets (3,3,0)/(4,4,0), d=8 | `sum s = 10550738857556475461/6825198573622282920 ... < g(lambda) ...: True`; `B_min histogram ... {1: 9, 0: 13, 2: 3, 3: 2}`; `mine - author's: []`; `r_* = 5` |
| `python myhorn.py` | minutes | calibration of the reviewer's T^d_r, LR and Horn LP (counts 41, 142, 522, 2062, 8752, 39716 for d=4..9; agreement with the pickles, the four-level and one-spike formulas and the hive LP) | `own T^d == author's cycle-2 pickle: True` |

## `exact_oq1.py` (in `repro/`, 33 s)

Expected: three lines ending in `sum s < g(lambda_q): True -> no certificate of g from the class '...' exists (weak duality)`
(box<=3 for g=(3,1,1,2,2;-2,-1,0); box<=3 and Pieri-type for g'=(1,1,2,3,4;-2,-1,0)), the rational points and vertices
quoted in Section 6, and for both certificates `in T^9: True`, `LR (reviewer, author) = (1, 1)` for every tile and
`RHS in canonical coordinates ... == g: True`.

## Which script backs which claim

| claim | scripts |
|---|---|
| Theorem 1 (proof in the text); exact certificate check; numerical bound | `reviewer/test_thm1.py`; `author/ol_test.py` |
| Lemma 3.2 (OL = OL_A at every point) | `author/ol_test.py`, `reviewer/test_thm1.py` |
| Proposition 3.3 | `reviewer/test_thm1.py` |
| Theorem 2A (explicit C, additivity, 23 < 24) | `reviewer/test_thm2AB.py`, `author/interlace_test.py` |
| Theorem 2B (explicit C, rank m, empty R_k for k > m-n+1, coverage) | `reviewer/test_thm2AB.py`, `author/interlace_test.py`, `author/region_coverage.py` |
| Proposition 5.6 and the n >= 3 gap statements | `author/pure_chain.py` |
| Theorem 3 (exact) and the exact Pieri obstruction | `exact_oq1.py`, `reviewer/test_oq1.py` |
| box-count tables, shapes, rectangles | `author/form_boxes.py`, `author/horn_boxes.py`, `reviewer/test_oq1.py` |
| Section 7 (d = 8) | `author/d8_example.py`, `reviewer/test_oq1.py` |
| Section 8.1 (exposed sets, rules, padding) | `author/forms_mn.py` (JSON files), `author/inv_rule.py`, `reviewer/test_oq1.py` |
| Section 8.2 (chain feasibility 300/300) | `author/chain_lp.py` (not independently re-implemented) |
