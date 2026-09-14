# Reproducibility package for "All-degree Born rigidity in dimensions four and three"

Environment used: Python 3.12, numpy 2.5.1, scipy 1.18, sympy 1.14, mpmath 1.3 (Windows 11, Git Bash).
Everything labelled exact in the paper uses `fractions.Fraction`, big integers or sympy; no floating point enters Theorem A or the certified lower bound in d = 3.

## Layout

- `author/` — verbatim working directory of the research agent (`cycle3/work/B5_born_rigidity_d4/`), including all outputs of the long runs (`s3_*`, `s3b_*`) that are not rerun here, plus three files produced by `run_fast.sh` (`s6_refined_A_rerun.json`, `s6_refined_B_rerun.json`, `s6_refined_B_rerun_exact_den100000000.json`) and `s8_census_tally_final.txt` (census of the finished multistart logs of seeds 31–34; `s8_census_tally.txt` is the earlier partial census, 100 optima). Its own `README.md` lists every script with command, runtime and output file.
- `reviewer/` — the independent reviewer's scripts (`r1_exact.py`, `r2_lemmaT.py`, `r2b_lemmaT.py`, `r3_exactframe.py`, `r4_opt.py`, `r5_kkt.py`) and the output `r4_seed7.txt` of the 12-start search (about 10 min; not rerun). In `r3` and `r5` one absolute path was replaced by a package-relative one (marked `# REPRO`).
- `run_fast.sh` — reruns every fast script into `logs/` and writes `logs/timings.txt`. Run from anywhere: `bash repro/run_fast.sh`.
- `logs/` — output of the last `run_fast.sh` (14 September 2026).

## What each fast run checks (expected final lines)

| log | claim in the paper | expected |
|---|---|---|
| `s1_exact_simplex_spectra.log` | Table 1; simplex d = 3 (77/45 at k = 4); ONB values; Lemma-T thresholds k >= 11 (d = 4), k >= 14 (d = 3) | `exact: g_k^simp > g_6^simp for all 2<=k<=400, k!=6  [OK]` and the d = 3 analogue with k = 4 |
| `s2_zonal_integral_identity.log` | identity (3.2) exact for n <= 40, d = 3..6 | four `[OK]` lines; 69–154 s |
| `s4int_bipyramid_test.log` | pipeline test | `CERTIFIED: gamma(F) >= 1.545185185185185` |
| `s4int_certificate_B.log` | Theorem B | `CERTIFIED: gamma(F) >= 1.776009937964733  (exact rational 177600993796473305296398794157/10^29)`, min at k = 9, tail >= 1.78533803 |
| `s6_tie_refine_B.log`, `s6_tie_refine_A.log` | 40-digit values of gamma_B, gamma_A, Gram matrices, multipliers | gamma_B = 1.77600994299966361808..., gamma_A = 1.77537254733646573261... |
| `s5_rationalise_and_certify_B.log` | exact frame rebuilt from the rerun 40-digit point, then certified | same certified rational; last line of `timings.txt`: `rerun exact spec identical to original: True` |
| `s7_rank_and_identify_B.log` | rank 4 of the active gradients; no low-degree algebraic relations | singular values 1.476, 0.407, 0.336, 0.123, ~1e-26; `findpoly ... None` |
| `r1_exact.log` | Table 1 recomputed with sympy.jacobi; corrected difference 7334427/36700160 | `diff 22018975/7340032-14/5 = 7334427/36700160` |
| `r2b_lemmaT.log` | Lemma T ratio <= 1 numerically, thresholds | `max |Q|/bound ... : 1.0 at (3, 0.0, 0)`, `bound k=10: 0.017239057 k=11: 0.014586895` |
| `r3_exactframe.log` | independent 60-digit evaluation of the exact frame and of point B | `min ... at k= 9  value 1.776009937964733053`; ties of B to 18 digits |
| `r5_kkt.log` | independent KKT multipliers, rank, directional-derivative check | `lambda: [0.10632927 0.24896864 0.2164758 0.12593285 0.30229343]`, min over directions 0.0108 > 0 |

`r2_lemmaT.py` (direct `mpmath.jacobi` at degree up to 400) exits with a hypergeometric convergence error (`rc=1` in `timings.txt`); it is kept as the reviewer wrote it and is superseded by `r2b_lemmaT.py`, which uses the three-term recurrence and cross-checks it against `mpmath.jacobi` where that converges.

## Known cosmetic defect (not fixed, to keep the author's directory verbatim)

`s6_tie_refine_mp.py` prints the KKT multipliers under a hard-coded header `(k=5,6,8,12,18)` whatever tie set is passed on the command line. In `s6_out_B.txt` and `logs/s6_tie_refine_B.log` the five multipliers belong to the tie set (4, 8, 9, 12, 16) of optimum B, in that order. The reviewer's `r5_kkt.py` reproduces them with the correct labels.

## Long runs (not rerun)

- `s3_d3_N5_global.py SEED` (SEED = 0..3): differential evolution, 20–25 min each; outputs `s3_seedSEED.txt`, `s3_best_seedSEED.json` (seeds 0, 1 reach B; seeds 2, 3 reach A).
- `s3b_d3_multistart.py SEED NSTARTS`: batch 1 (default seed 11) -> `s3b_out.txt`; seeds 21–24 -> `s3b_seed2?.txt` (summary lines only); seeds 31–34 -> `s3b_seed3?.txt` (one line per start; census by `tally.py` -> `s8_census_tally_final.txt`).
- `reviewer/r4_opt.py` -> `r4_seed7.txt`.
