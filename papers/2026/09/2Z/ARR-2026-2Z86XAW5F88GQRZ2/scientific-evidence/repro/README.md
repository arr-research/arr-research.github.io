# Candidate-2 verification supplement (14 September 2026)

This is author-side repair, not an independent assessment of the revised PDF. Start with `python verify_all_tilings.py` from this directory. It checks all875 frozen exact tiling certificates /4342 tiles using two LR implementations and integer identities. No supplied pickle is included or loaded. For upper-bound replay run `python chain_own.py 8 0,1` from reviewer/, followed by `python chain_m9.py 0`; the equal coefficient sets and unused-zero embeddings give the remaining padded upper bounds. Fresh logs are in fresh-20260914/. The manuscript distinguishes historical claims from the new executions. The original reproduction instructions below are historical: their cache inventory and exactness limit d<=12 are superseded by this supplement. The default proof paths certs.py and horn_own.py rebuild optional small Fulton lists in memory. Legacy exploratory scripts that explicitly require a cache need a fresh locally generated cache, not an unchecked downloaded pickle.

# Reproducibility package for "The inverse self-commutator cost at inertia (m,3)" (13 September 2026)

Layout:

- `author/` — verbatim copy of the author's working directory `cycle2/work/A3_inertia_m3/` (scripts, JSON data, Horn-triple
  pickles `horn_d6..9.pkl`, logs). The scripts import each other by plain `import` and read/write data files in their own
  directory, so run them **from inside `author/`**.
- `reviewer/` — the adversarial reviewer's independent scripts and logs. The only modification: the absolute paths to the
  author's directory and to the reviewer's scratch directory were replaced by `AUTHOR_DIR` / `REVIEWER_DIR`, defined
  relative to this package (one marked line at the top of each affected file). `T_cache.pkl` caches the reviewer's Fulton
  lists T^n_r (n <= 9). Run these **from inside `reviewer/`**. `chain_m9.py z` is a wrapper (added for the manuscript)
  running the reviewer's exact chain check at m = 9 for one z per process.
- `exact_strict.py` — exact rational strict inequality g_0 > max S(m,1) at a chamber-centre point, m = 4,5,7,8 (Section 6).
- `run_fast.sh` — the fast reruns made for the manuscript; `logs/` their outputs and `logs/timings.txt` the wall-clock times.

Dependencies: Python 3.12, `numpy`, `scipy` (HiGHS via `scipy.optimize.linprog`, qhull via `scipy.spatial`), and for the
exact reviewer scripts `pycddlib` (`import cdd.gmp`). Everything labelled exact uses `fractions.Fraction`, integer
arithmetic or cdd/GMP; floating point is used only where the paper says so.

## Quick start (about 90 s)

    bash run_fast.sh          # writes logs/*.log and logs/timings.txt
    python exact_strict.py    # four exact margins 1/40, 1/60, 1/120, 1/150 (logs/exact_strict.log)

## Author's scripts (in `author/`), commands, measured runtimes, expected final lines

| command | s | role | expected last line |
|---|---|---|---|
| `python m3_forms.py 2 7 1500 0,1,2,3,4` then `m3_gather.py`, `m3_analyze.py` | minutes | discovery: hive-LP duals, rationalised forms, validity/exposedness filters (`forms_*`, `cand_*`, `analyze_m*.log`) | counts as in Section 8 |
| `python m3_closure.py m z` | 1–32 | closure loop -> `closed_m{m}_z{z}.json` (`closure_all.log`, `closure_z2.log`) | `RESULT m=.. z=..: N exposed forms, complete (max gap <= 1.8e-14)` |
| `python certs.py m z` (all d <= 12; `run_certs.sh`) | <= 14 | tiling certificates -> `certs_m{m}_z{z}.json`, `certs_all.log` | `RESULT m=9 z=0 d=12: 69/69 forms certified ... tile types {'LW': 307, 'row': 87, 'col': 22}` |
| `python familyA_cert.py 12 4` | 1 | LP-free family-A certificates, exact (Theorem 2) | `TOTAL 945 (form, z) certificates verified` |
| `python coverage_vertices.py m z` (`run_cov.sh`) | <= 27 | chamber vertices + 3x3 chain LP at every vertex -> `coverage_m{m}_z{z}.json`, `coverage_all.log` | `RESULT m=9 z=2 d=14: 969 chamber vertices; every chamber covered ...: True` |
| `python verify_formula2.py 3 9 2000 0,1,3 2026`; `... 9 9 2000 2 2026` | 4–14 each | fresh-sample check with tight re-solves (`verify_formula2.log`, `logs/verify_formula2_9_9_2000_2.log`) | `... 0 points with |gap|>1e-9 after re-solve` |
| `python construct_C.py m z 500` (`run_construct.sh`) | 3–175 | explicit 3x3-block shifts (`construct_all.log`; contains one duplicated m=8 line and one superseded m=5,z=0 line) | residual medians <= 3e-15 |
| `python rank_scan.py m z 150` (`run_rank.sh`) | | optimal-rank scan (`rank_all.log`; "(7,6)" entries are a threshold artefact) | histograms as in Section 6 |
| `python families2.py 3 9 [compare]` | 0 | six-family generator vs `closed_m{m}_z1.json`; with a third argument writes `pred_m{m}.json` | `m=9: generated 69 forms; ... truth 69, extra 0, missing 0` |
| `python test_pred.py 10 1 1200` | 8 | out-of-sample test at m=10 (`test_pred.log`; also m=10,11 at z=0 showing the extra z=0 forms) | `max(kappa-maxpred)=4.88e-15 ... dual forms at gap points: {}` |
| `python m3_horn_duals.py ...`, `horn_cache.py d`, `check_horn_lp.py`, `hive_core.py`, `m3_tools.py`, `lr.py`, `lr2.py`, `catalogue.py`, `restricted.py`, `layering_lp.py`, `tiles.py`, `families.py`, `group_layers.py` | | libraries and exploration scripts (Fulton generator, hive LP, joint/radius LPs, LR coefficients, tile catalogue, chain LP) | |

## Reviewer's scripts (in `reviewer/`)

| command | s | role | expected last line |
|---|---|---|---|
| `python calibrate.py` | | calibration of own T^n_r, LR, Horn and hive LPs | 0 mismatches; known values 6, 10, 74/7, 73/7 |
| `python tiles_check.py` | 1 | 36 certificates / 149 tiles verified with a third LR implementation; dimension-free instantiation | `certificates fully verified: 36/36 (149 tiles)` then the five expected non-realisable cases |
| `python tiles_dimfree2.py` | 45+ | all tiles of the z=1 certificates (m=3,4,5) realisable at z'=2,3,4 (m>=6 not completed) | `certs z=1 m=5: ... 106/106 tiles realisable` |
| `python chain_own.py m_max [z,z,..]` | s to 112 s per (m,z) | EXACT rational chamber vertices (cdd) + exact 3x3 chain LP, m = 3..8 (`chain_own*.log`) | `m=8 z=2 d=13: |S|=59, exact chamber vertices total 746; every chamber covered by one chain: True; chambers needing an inserted zero: 1` |
| `python chain_m9.py z` | 542–546 per z | the same at m = 9 (manuscript rerun; `logs/chain_own_m9_z{z}.log`; the reviewer's own `chain_own_m9.log` is empty because that run was still pending when the review was written) | `m=9 z=2 d=14: |S|=69, exact chamber vertices total 969; every chamber covered by one chain: True; chambers needing an inserted zero: 0` |
| `python formula_check.py [N]`, `python extra_checks.py` | minutes | own hive/Horn LP vs max S at 250 points per (m,z); rank forcing on the new part (m=5,7); m=11 validity/exposedness | `points with |gap|>1e-12: 0` |
| `python padding_check.py` | 8 | EXACT (GMP) Horn LPs at the padding example; rank forcing sample m=4 | `... rank-5 forced at z=1 ... at 48; cap-4 value == kappa_7 at 48` |
| `python exposed_m5.py` | 4 | exposedness of all m=5 forms | `forms never unique argmax: 0 []` |
| `python pred_m11.py`, `python complete_m11.py [m]`, `python z0_extra.py` | 7, 13, 12 | Conjecture 4 at m=10,11,12; chamber-vertex completeness; z=0 extras at m=10..13 | as quoted in Sections 3, 6, 8 |
| `python m2_reduction.py` | 1 | EXACT (m,2) and one-spike reductions, m=4,5 | `... equality: True` |
| `python construct_own.py` | | 28 explicit matrices | `28 points constructed; max commutator residual 4.2e-06` |

## Which script backs which claim

| claim | scripts |
|---|---|
| Theorem 1, sets S(m,z) and their completeness | `m3_closure.py` (+ `m3_tools.py`, `hive_core.py`), reviewer `formula_check.py`, `extra_checks.py` |
| Theorem 1, exact lower bound (d <= 12) | `certs.py` (+ `catalogue.py`, `restricted.py`, `lr.py`, `lr2.py`, `horn_d*.pkl`), reviewer `tiles_check.py` |
| Theorem 1, upper bound | `coverage_vertices.py` (+ `layering_lp.py`), reviewer `chain_own.py` (exact, m <= 8), `chain_m9.py` |
| Theorem 2 | `familyA_cert.py` |
| Theorem 3 | `closed_*.json` (set comparison), `exact_strict.py`, reviewer `padding_check.py`, `extra_checks.py`, `z0_extra.py`, `exposed_m5.py`; `rank_scan.py`, `test_pred.py` (z=0) |
| Conjecture 4 | `families2.py`, `test_pred.py`, reviewer `pred_m11.py`, `complete_m11.py`, `extra_checks.py` |
| Section 5.4 matrices | `construct_C.py`, reviewer `construct_own.py` |
| Section 7 reductions | reviewer `m2_reduction.py`; `construct_C.py` (boundary consistency lines) |
