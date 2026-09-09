> Supplement BORN-audit-s1 (9 September 2026): the code below now propagates failures and asserts expected results. Original manuscript/reproduction descriptions follow for provenance. The fresh run is documented in ../VERIFICACION.json; this supplement is not deposited.

# Reproducibility scripts for "One Fold, Unique Contact and the Complete Two-Piece Rate–Distortion Function of Rank-One Complex-Projective Born Prediction" (version 2, 8 September 2026)

All scripts are plain Python 3 (tested with Python 3.12.6, sympy 1.14.0, mpmath 1.3.0 on
Windows 11; nothing else is required). Every script is deterministic and exits with
status 0 only if all its assertions hold. Exact arithmetic (`fractions.Fraction`,
`math.comb`, sympy rationals) is used wherever a proof step is certified; mpmath is used
only for the illustrative Section 7 values and for the cross-checks of the external
workshop's numbers (no proof step depends on floating point).

## Commands

Run everything at once (writes `<name>.out` for every script and `runtimes.txt`):

    cd repro
    python run_all.py

Total wall time about 95 s, of which `verify_signs.py` takes about 80 s. Or run a single
script, e.g. `python workshop_recheck.py`. The scripts locate their data files next to
themselves, so they can be run from any working directory.

## Scripts, what they certify, expected final lines, wall times

| script | certifies (paper section) | arithmetic | wall time |
|---|---|---|---|
| `sym_check.py` | Lemma 3.2 (N_d = ((d-1)/d) Ñ_d/κ; b = 1 − d(M−1)/(κM); Ñ_d = M(M+d)(κ−Ψ_d(M))) and the phase-plane identities (a)–(f) of Theorem 4.1 (Φ on the curve, Ψ_d', Δ, Ψ_d(M_1), ∂Φ/∂κ, denominator on the curve), ĉ_{d,3}; d symbolic (§3, §4) | sympy exact | 2.0 s |
| `check_formula.py` | three-term definition of N_d equals ((d-1)/d) Ñ_d/κ coefficientwise, and [κ^n] Ñ_d = (d−1)!² ĉ_{d,n}/(2d−2+n)! with the closed form (3.3); d = 2..12, n ≤ 60 (§3) | `Fraction` | 0.3 s |
| `verify_signs.py` | closed form (3.3) against the three-term definition and the sign pattern of Theorem 6.1 with the stated n_d; d = 2..40, n ≤ 400 (§3, §6) | `Fraction` | 80.6 s |
| `induction_check.py` | symbolic factorization of the sub-solution defect Π(m,d) of Lemma 6.2(iii); lists the (d,m) with Π < 0 for 3 ≤ d ≤ 60, 3 ≤ m ≤ 2d (exactly m ∈ {2d−1, 2d}) (§6) | sympy | 3.3 s |
| `tail_cases.py` | recursion q_{m+1} = 2(d+m)(q_m+1)/(2d−2+m) (d = 3..29); the boundary comparisons q_m > g_m at m ∈ {2d, 2d+1} for 3 ≤ d ≤ 60 (the computer-assisted part of Theorem 6.1; only 3 ≤ d ≤ 35 is needed); the central-term and (5/3)^{⌊d/2⌋+1} bounds, showing the analytic tail starts exactly at d = 36 (§6) | exact integers | 0.1 s |
| `boundary_exact.py` | the same 66 comparisons written out as explicit rationals q_m, g_m, ĉ_{d,m} with their signs, to `boundary_exact.txt` (§6, §9) | `Fraction` | 0.1 s |
| `h6_remark63_check.py` | expansion (2.5) of G_{d,λ} at b = 0 with d, λ symbolic (Lemma 2.1, fact (H6)); G_{2,3}(b) = −(9/20)b⁴ + (9/35)b⁶ + O(b⁸) (d = 2 case of (H6)); Q' > 0 on a grid for d = 3..6 and Q → −∞ at 0⁺ (Remark 6.3) (§2, §5, §6) | sympy; mpmath 30 digits | 2.9 s |
| `chain_numerics.py` | fold κ_f, contact κ_c, λ_min, λ_c, b_c, D_c, R_c for d ∈ {3,4,5,6,7,8,10,12,15,17,20,30,50,100}; asserts the proved relations κ_1 ≤ κ_f < 2d, M_d(κ_f) ≥ d(d−1)/2, b_d(κ_f) < 1/2, κ_f < κ_c, λ_min < λ_c < λ_0; prints Tables 1–4 of Section 7 and writes `chain_values_50digits.txt` (§7) | mpmath, 60 digits, 220-step bisection | 1.4 s |
| `workshop_recheck.py` | re-verification of the AIRR workshop's checks (TALLER-0002): (A) the 66 boundary signs recomputed from the three-term definition (2.4), not from (3.3); (B) the Section 7 values by the workshop's route (Kummer derivatives M' = ₁F₁(2;d+1;κ)/d, M'' = 2·₁F₁(3;d+2;κ)/(d(d+1)), no Lemma 3.1, no Ψ_d) at 70 digits, compared with the workshop's 20-digit values (embedded in the script) and with `chain_values_50digits.txt`; (C) residuals of H_d, F_d at the roots by direct quadrature of the tilted Beta(1,d−1) moments (§7) | `Fraction`; mpmath 70/45 digits | 2.2 s |

Expected final lines (all reproduced on 2026-09-08; see the `.out` files):

* `sym_check.py`: four `True` lines, then the factored expressions quoted in Section 4, ending with `chat_3 =  -(d - 2)*(2*d + 1)/((d + 1)*(d + 2))`.
* `check_formula.py`: `ALL OK (N == (d-1)/d*Ntilde/kappa and closed form (R3)): True`.
* `verify_signs.py`: `ALL closed-form matches: True time ...`, with `sign changes=1` and
  `last negative n_d` = 5, 7 for d = 3, 4 and = 2d for 5 ≤ d ≤ 40; for d = 2,
  `sign changes=0`, zeros at n = 0, 1, 2.
* `induction_check.py`: `Pi = n*(n - 1)*(2*d**2 - d*n - d - 2)/((d - 1)*(2*d - n + 1)*(2*d - n + 2))`.
* `tail_cases.py`: `recursion exact: True`; column 2 `True` for all d ≥ 3; column 3
  `False` exactly at d = 3, 4; last column `True` from d = 36 on.
* `boundary_exact.py`: `boundary comparisons: 66 ; sign pattern of Theorem 6.1 at the boundary indices: True`.
* `h6_remark63_check.py`: `b^2 coefficient == lambda(2 lambda v_d - R0^2): True   b^3 coefficient == (4/3) lambda^3 mu_{3,d}: True`,
  `G_{2,3}(b) = -9*b**4/20 + 9*b**6/35 + O(b**8)`, and four lines `Q'>0 on grid ...: True`.
* `chain_numerics.py`: the wide diagnostic table, then Tables 1–4 exactly as printed in Section 7, then `wrote chain_values_50digits.txt`.
* `workshop_recheck.py`: `(A) 66 boundary signs ... : True`; for d = 3, 5, 17, 100 a `(B)` line with
  `max rel diff vs workshop (20 digits)` of order 1e-20 and `vs chain_values_50digits.txt` of order 1e-50,
  and a `(C)` line with quadrature residuals ≤ 1e-43 (d ≤ 17) and ≤ 1e-11 (d = 100).

## Data files

* `chain_values_50digits.txt` — every quantity of Section 7 (κ_1, κ_f, 2d−κ_f, M_d(κ_f), d(d−1)/2, b_d(κ_f), λ_min, κ_c, b_c, λ_c, λ_0, D_c, R_c) to 50 significant digits for the fourteen values of d above. Tables 1–4 of the paper are these numbers rounded to 12–14 significant digits.
* `boundary_exact.txt` — the 66 exact rationals q_m, g_m and ĉ_{d,m} for 3 ≤ d ≤ 35, m ∈ {2d, 2d+1}, with the sign of ĉ_{d,m} = sign of c_{d,m−1}. This is the complete finite part of the proof of Theorem 6.1; it can be checked by hand for small d (e.g. d = 3: q_6 = 164/3 > g_6 = 54 gives ĉ_{3,6} = −12 < 0; q_7 = 501/5 < g_7 = 273/2 gives ĉ_{3,7} = 363 > 0, hence n_3 = 5).
* `runtimes.txt`, `*.out` — outputs of the last full run (2026-09-08).

## Provenance and changes since version 1

The scripts were written by the proving agent (Claude Fable 5.1) on 2026-09-07;
`check_formula.py` originally carried a wrong linear term in the closed form (found by the
adversarial reviewer) and was corrected before version 1; `chain_numerics.py` gained the
row d = 17 before version 1. For version 2 (2026-09-08), after the AIRR workshop evaluation
(TALLER-0002):

* `chain_numerics.py`: precision raised to 60 digits and `mpmath.findroot(..., 'bisect')`
  replaced by a fixed 220-step bisection (the former stopped at about 28 correct digits,
  short of the 50 digits announced in version 1; the 10 printed digits of version 1 were
  unaffected); it now also prints the four narrow tables of Section 7 and writes
  `chain_values_50digits.txt`.
* New: `boundary_exact.py`, `h6_remark63_check.py`, `workshop_recheck.py` and the two data
  files; `run_all.py` runs them.
* All outputs in this directory were regenerated on 2026-09-08 by `run_all.py`.
