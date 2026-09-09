# Reproducibility package for "Rank plus Weyl sparsity is at least p+1" (version 2, 2026-09-08)

Everything numerical or exact that the paper claims can be reproduced from this directory alone. No network access is needed.

## Environment

Windows 11, Python 3.12 (3.12.6 used on 2026-09-07/08), numpy 2.5.1, scipy 1.18.0, sympy 1.14.0, mpmath 1.3.0 (bundled with sympy). Install with `pip install numpy scipy sympy`. All commands below are run **from this directory** (`cd repro`), because three scripts import sibling modules. Runtimes are wall-clock on a laptop (single process); expect a factor of 2 either way on other machines.

## Provenance of the files

* `e1_…`–`e5_…`: written by the proving agent during the research phase.
* `review_…`: written from scratch by the independent reviewing agent, without importing the author's scripts.
* `w1_workshop_and_data.py`: added in version 2; re-derives the two checks of the external workshop (AIRR taller 2026-09-08, item TALLER-0001) independently of the author's ring code, writes the full-precision data files, and verifies the self-contained decoder of Lemma 7 numerically.
* `logs_original/`: outputs as produced during the research phase (plus the reviewer's own rerun of `e2`, `review_C1_e2_rerun.txt`).
* `*_rerun.txt`, `runtimes_rerun_2026-09-07.txt`: rerun for version 1 (2026-09-07).
* `*_rerun_2026-09-08.txt`, `runtimes_rerun_2026-09-08.txt`, `w1_workshop_and_data_out.txt`: rerun for version 2 (2026-09-08). The three fast scripts produced output identical to the 2026-09-07 logs modulo timings (checked with `diff` after stripping the `[..s]` stamps).
* `data/`: full-precision data files (see below).

All random instances use fixed seeds (`e1`: `default_rng(12345)`; `e2`: `random.seed(7)`; `e4`: `default_rng(3)`; `e5`: `random.seed(11)` and `default_rng(1)`; `review_check_proof`: `default_rng(0)` and `Random(2026)`; `review_line_conjecture*`: `default_rng(5)`; `w1`: `default_rng(5)`), so the 92 instances of Section 7(a), the 14 instances of 7(b), the 68 instances of 7(f) and the numerical witnesses are regenerated exactly.

## Fast scripts (rerun 2026-09-08)

| script | command | what it certifies (paper section) | runtime | expected final line |
|---|---|---|---|---|
| `e2_exact_padic_checks.py` | `python e2_exact_padic_checks.py > e2_out.txt` | Section 7(a). Exact Z[ω] arithmetic. Clifford identity (4.1) for all s and all labels, p ∈ {3,5,7,11} (1826 cases). 92 seeded instances (p = 5, 7, 11; 2 ≤ ℓ ≤ 5; four regimes): integrality of U C U⁻¹ in every direction, reduction = fibre-sum circulant (4.2), rank over Q(ω) ≥ F_p-rank of the reduction, reduced rank = p − ord₁ ḡ with ord₁ ḡ ≤ m − 1, max over directions ≥ p − ℓ + 1. | 52 s (09-07), 59 s (09-08) | `ALL EXACT CHECKS PASSED` |
| `review_check_proof.py` | `python review_check_proof.py > review_out.txt` | Section 7(b). Part A: (4.1) with the explicit phase e(s,a,b), p ∈ {3,5,7}. Part B: p = 7, ℓ = 5 over Z[ω₇, √2] (split prime, two residue maps), 14 instances × 2 primes × 8 directions. Part C: exhaustive ord₁ ≤ m − 1 over F_p (p = 7 all m, 823 542 polynomials; p = 5 all m; p = 11, m ≤ 4). Part D: sharpness family ∏(Z − ωⁱI), p = 7. | 42 s (09-07), 47 s (09-08) | `ALL REVIEWER CHECKS PASSED [..s]` |
| `review_line_conjecture_exact.py` | `python review_line_conjecture_exact.py > line_out.txt` | Section 7(c), Proposition 5. Exact rank 3 over Q(ω₅) (regular representation over Q) of the five parabola operators C_k; no three support points collinear (exact). Imports `review_check_proof` (ring arithmetic) and `review_line_conjecture` (which runs the reviewer's numerics at import time). | 9 s (09-07), 12 s (09-08) | lines 2–6: `k=0..4: … exact rank over Q(omega_5) = 3, nullity = 2`; line 8: `Line conjecture (nullity <= maxcollinear - 1 = 1) is FALSE; Theorem 1 (nullity <= l - 1 = 4) is respected.`; then the numerical block of `review_line_conjecture.py` |
| `w1_workshop_and_data.py` | `python w1_workshop_and_data.py` | Section 7(g). (1) Workshop checks re-derived: 1826 identities (4.1) by integer exponent arithmetic; rank 12 of the 20×20 regular-representation matrix of each parabola operator C_k (Fraction elimination and sympy agree) → rank 3, nullity 2. (2) Writes `data/parabola_certificate.json`, `data/gp5_numerical_witness.json`, `data/w1_report.json`. (3) Lemma 7 decoder for p ∈ {3,5,7}, all 1 ≤ r ≤ p: TT* = (p/r)I, Cauchy–Binet identity Σ_E w_E w_E* = (p/r)^{r−1} I, orthogonality ⟨w_E, φ_b⟩ = 0 iff b ∈ E, POVM completeness, zero probability outside the reported list (size p − r + 1), and ρ = Σ_E C_E C_E* with s_W(C_E) = p − r + 1. | 6 s | `W1: ALL CHECKS PASSED` |

## Slower scripts (original logs in `logs_original/`; `e4`, `e5`, `review_line_conjecture` were also rerun on 2026-09-08 while writing this README)

| script | command | what it does (paper section) | runtime | expected final line |
|---|---|---|---|---|
| `e1_orbits_numeric.py` | `python e1_orbits_numeric.py p l restarts`; runs used: `3 2 20`, `5 2 20`, `5 3 20`, `5 4 20`, `5 5 60`, `7 2 20`, `7 3 40`, `7 4 60`, `7 5 60`, `11 4 30` | Section 7(d). AGL(2,p)-orbit representatives of ℓ-subsets of F_p² (canonical forms; Σ|orbit| = C(p², ℓ) asserted), alternating-minimisation search for nullity k = 1..ℓ on each orbit; reports min σ_{p−k+1}. Logs: `logs_original/e1_p{p}_l{l}.txt`. | < 1 s … 186 s (p = 7, ℓ = 5); 38 s (p = 11, ℓ = 4) | `RESULT p=7 l=4: max attained nullity over all orbits = 3 (law requires <= 3); min over orbits of min_c sigma_(p-l+1) = 1.800e-01; orbits attaining l-1: [...]` (and analogously for the other runs; the table of Section 7(d) is read off these lines) |
| `e3_groebner_p7_l4.py` | `python e3_groebner_p7_l4.py > e3_out.txt` | Section 7(e). sympy Gröbner certification (unit ideal of Φ₇(w) and the 4×4 minors) that no coefficient vector gives rank ≤ 3 for p = 7, ℓ = 4, per orbit. 6 of 8 orbits certified; the two "three collinear + one" orbits are certified instead by Proposition 4 (a rerun with all 1225 minors was stopped after 25 min). | 0.2–40 s per orbit | per orbit `… CERTIFIED rank>=4 (Groebner basis = {1}) …` for six orbits; see `logs_original/e3_out.txt` |
| `e4_corank_attainment.py` | `python e4_corank_attainment.py` | Section 7(f)(i). Every corank k ≤ ℓ − 1 at exact sparsity ℓ (collinear construction of Section 5.1), p ∈ {5, 7, 11, 13}; numerical check. | 1 s | `p=13: all pairs (l,k), 1<=l<=p, 0<=k<=l-1: exact sparsity l and corank k attained: True` |
| `e5_line_plus_point_and_gp5.py` | `python e5_line_plus_point_and_gp5.py` | Section 7(f)(ii). (i) Proposition 4 ("line + one point": rank ≥ p − 1) on 68 seeded exact Z[ω] instances, p ∈ {5, 7, 11}; (ii) numerical minimiser on the general-position 5-set of p = 5 with all coefficients bounded away from zero. Imports `e2_exact_padic_checks` and `e1_orbits_numeric`. | 20 s | `(i) p=11: line+point supports, exact rank >= p-1 in all instances (min rank seen 11)` then `(ii) p=5 general-position 5-set [(0, 0), (1, 0), (0, 1), (1, 1), (2, 3)]: min sigma_4 = 5.40e-15, |c| = [0.4262 0.5414 0.4969 0.2931 0.4386]` |
| `review_line_conjecture.py` | `python review_line_conjecture.py` | Reviewer's numerics for the line conjecture (both general-position orbits of p = 5, ℓ = 5) and discovery of the cyclic symmetry Φ of the parabola. | 2 s | five `eigenvalue …` lines, each ending with `singular values [1.414214 1.414214 1. 0. 0.]` |

## Full-precision data (`data/`)

* `parabola_certificate.json` — Proposition 5. Support {(t, t²)}, conventions, and for k = 0..4: the exponent vector f_k (C_k = Σ_t ω^{f_k(t)} W_(t,t²)), the 20×20 integer matrix of C_k in the regular representation of Q(ω₅) over Q (basis 1, ω, ω², ω³), its rank over Q (12), rank over Q(ω₅) (3) and nullity (2). Also the singular values of C_0 in double precision (squares 10, 10, 5, 0, 0) and the exact no-three-collinear flag. Anyone can recompute the ranks from the stored integer matrices with any exact linear-algebra tool.
* `gp5_numerical_witness.json` — Section 7(c), the *numerical* nullity-2 witness on the other general-position orbit of p = 5, ℓ = 5, support {(0,0),(1,0),(0,1),(1,1),(2,3)}: coefficients (real and imaginary parts as full-precision Python floats), |c_g| (all ≥ 0.29), singular values, σ₄ ≈ 2.6·10⁻¹⁶, and σ₄ recomputed from the stored strings. This witness is numerical only; no exact certificate is claimed for this orbit.
* `w1_report.json` — summary numbers of `w1_workshop_and_data.py` (identity count 1826; regular-representation rank 12; rank 3; nullity 2; decoder checks for p ∈ {3,5,7}).

## Notes

* The exact scripts use only integer arithmetic (Z[ω] as integer vectors, Fraction-based Gaussian elimination); no floating point enters the certificates in `e2`, `review_check_proof` (Parts A–D, except an optional floating-point cross-check of the exact rank), `review_line_conjecture_exact` (the exact part) or `w1` parts (1a)–(1b).
* The full text of Krahmer–Pfander–Rashkov (arXiv:math/0611493), used during the research phase for the rank-one comparison, is not redistributed here.
* The external workshop's own script (`check_core.py`, kept in `taller_feedback/` of the research cycle, not in this folder) reports `clifford_identities_exact: 1826`, `parabola_regular_representation_rank: 12`, `rank_over_Q_omega: 3`, `nullity: 2` for this paper; `w1_workshop_and_data.py` reproduces these numbers.
