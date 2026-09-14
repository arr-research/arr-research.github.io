# Reproducibility package for the revised sparse cyclic Weyl operator manuscript

Python 3.12.6 on Windows 11; numpy 2.5.1, sympy 1.14.0; python-flint 0.9.0 is needed only by the reviewer's
exact scripts (`exact_zeros.py`, `zeros_spot.py`, `flats_check.py`). No proof in the manuscript depends on
floating point: the exact certificates (Theorem Z, tables, Clifford identities, obstruction codes) use
integer/cyclotomic arithmetic; the numerical scripts (`operator_first_order_checks.py`, `composite_trinomials.py`,
`nullity_search.py`, the T3 part of `gap_table.py`) are sanity checks and searches, labelled as such in the paper.

## Provenance

Historical author/reviewer identities and session independence below are author-supplied, not authenticated. This revision preserves every original Python script and data file. The scalar envelope is attributed to Delvaux–Van Barel; not all results had separate implementation coverage or a fresh rerun. The known d=14 numerical threshold mismatch below remains disclosed.


* `author/` — the thirteen scripts of the working report `cycle2/report_C2_weyl_prime_power.md`, copied
  unchanged from `cycle2/work/C2_weyl_prime_power/` (author agents, 2026-09-12/13). `author/logs/` holds their
  logs, copied unchanged at the time this manuscript was closed. Two of the author's exact-table runs were still
  in progress at that moment (`log_zerosQ_composite.txt`: d = 12, m = 8; the d = 15 exact run had not started
  writing); the paper only uses the entries present in the copied logs.
* `reviewer/` — the independent adversarial reviewer's scripts and logs (`cycle2/work/review_C2_checks/`,
  2026-09-13), unchanged.
* `run_fast.py` — written for the manuscript; reruns the fast subset below.
* `out/` — outputs of the rerun of 2026-09-13 (`<name>.out`, `runtimes.txt`, `run_fast_console.txt`), plus the two
  longer runs started separately: `rev_flats_27_4.out` (reviewer's exact flats method, d = 27, m = 4: Z = 12,
  7 min) and `zerosQ_cyclic_15_m5.out` (author's exact flats method, d = 15, m = 5: Z = 12, exhaustive over
  34 support orbits, 4455 s); both values are used in the paper (Sections 4.8 and 5.3).

## Commands (run from this directory)

    python run_fast.py                 # all 38 fast jobs (about 6 min); see out/runtimes.txt
    python run_fast.py <name> ...      # a subset, by job name (names in run_fast.py)

Individual scripts (run inside `author/` or `reviewer/`):

    python cyclotomic_certify.py d                  # Theorem Z certificate in Z[omega_d]; d in 4 8 9 16 25 27 32 49 81
    python charp_order_exhaustive.py p k mmax       # Theorem A data (exact-order maxima, monotone maxima = Omega_k)
    python omega_table.py                           # Omega_k recursion = digit definition, p^k <= 128
    python coset_meshulam_vs_omega.py               # gap table (Section 6.1) and torsion-coset comparison (6.2)
    python first_order_obstruction_code.py d        # dim of the obstruction code N(p,k), two-line word, weight distribution (d=4)
    python obstruction_min_distance_check.py 8 16 9 # Lemma N cross-check: min weight >= 2p
    python operator_first_order_checks.py 16 100    # Clifford identities (numerical, discrete target) + Theorem B' on instances
    python exact_check_firstorder_violations.py     # the three flagged d=16 instances: exact rank 128/128
    python composite_trinomials.py 6 8 9 10 12 14 15  # Theorem T3 values by the sector formula + SVD
    python zeros_exact_Q.py cyclic|plane n mmin mmax  # exact tables over Q(omega_n) (Section 5.3, 6.2)
    python cyclic_zeros_exact.py d mmin mmax        # the F_q model (two primes); NOT a certificate
    python nullity_search.py d l k mode nsup restarts iters [seed]   # numerical searches (Section 6.3)
    python thmA_check.py p k mmax                   # reviewer: Theorem A, both forms, over F_p-bar
    python thmZ_construction.py 4 8 9 16 25 27 32   # reviewer: f_r has w_p(r) terms and exactly r zeros
    python clifford_exact.py 4 8 9                  # reviewer: U_s, V_s identities exactly in Z[omega_{2d}] / Z[omega_d]
    python codes_minweight.py                       # reviewer: Radon code (p=2,3,5) and N(p,k) (d=4,8,9,16) min weight = 2p
    python gap_table.py                             # reviewer: gap table, Omega closed forms, T2 exhaustive d<=15, T3 examples
    python zeros_spot.py cyclic|plane               # reviewer: exact spot checks of the tables
    python flats_check.py d m                       # reviewer: exact Z(d,m) by the flats method (16 3, 16 4: seconds; 27 4: 7 min)

## Rerun of 2026-09-13 (writing agent)

All 38 jobs of `run_fast.py` exited with status 0 and reproduced the logged values: Theorem Z certificates for
all nine d (81: 87 s), Theorem A exhaustive data (d = 4, 8, 9, 16 all m), the gap table (identical from both
scripts), obstruction-code dimensions 7/34/45 and minimum weights, the exact tables for d = 6 (all m), d = 10
(m <= 4), d = 14 (m <= 3), the plane (Z/4)^2 (m <= 4), the reviewer's spot checks (d = 6, 10, 12, 14 and the plane),
Z(16,3) = 8, Z(16,4) = 12, the three exact 128/128 ranks, the T3 values, and the Clifford identities (4352
numerical at d = 16; 96/768/972 exact at d = 4/8/9). Note: `gap_table.py` reports one "mismatch" among its 60
random trinomials (d = 14, coefficient b = 0.3i): as the reviewer recorded, b^14 is about 5e-8, the sector
determinant is tiny but nonzero, and the numerical nullity threshold is at fault, not the formula.

Not repeated (slow; logs in `author/logs/`): the exact tables for d = 10 (m >= 5, 486 s total), d = 12 (m >= 5,
up to 2462 s), d = 14 (m = 4, 5), d = 18 (m = 4), the plane (Z/4)^2 for m = 5..7 (up to 1771 s); the obstruction
codes for d = 25, 27 (427 s, 462 s); the F_q tables; the numerical searches (`log_gap_search.txt`,
`log_theoremB_sanity.txt`); the 25/27 instance checks and the charp data for d = 25, 27 (m <= 7).
