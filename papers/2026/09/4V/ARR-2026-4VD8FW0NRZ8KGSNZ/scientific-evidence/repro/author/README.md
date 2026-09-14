# B5_born_rigidity_d4 - scripts (Python 3.12, numpy 2.5.1, scipy 1.18, sympy 1.14, mpmath 1.3)
All commands run from this directory. Exact arithmetic where claimed (Fractions / big integers / sympy).

| script | what | command | runtime | output |
|---|---|---|---|---|
| s1_exact_simplex_spectra.py | exact rational g_k of ONB and simplex, d = 3,4, k <= 400 (Fraction three-term recurrence); min over k; Lemma-T threshold | python s1_exact_simplex_spectra.py 400 | < 1 s | s1_out.txt |
| s2_zonal_integral_identity.py | exact symbolic check of E[z^n] = P_n^{(d-2,0)}(2t-1)/C(n+d-2,n) as polynomials in t, n <= 40, d = 3..6; recurrence vs sympy.jacobi | python s2_zonal_integral_identity.py 40 | 69 s | s2_out.txt |
| s3_d3_N5_global.py | d = 3, N = 5: differential evolution + NM/Powell polish on the exact Bloch parametrisation | python s3_d3_N5_global.py SEED (0-3) | 24-25 min each (4 in parallel) | s3_seedSEED.txt, s3_best_seedSEED.json |
| s3b_d3_multistart.py | random multistart local search (NM+Powell) | python s3b_d3_multistart.py SEED NSTARTS | ~37 s per start | s3b_out.txt, s3b_seedSEED.txt |
| s4_d3_exact_certificate.py | exact Q(sqrt q) certificate with Fractions (too slow beyond small denominators; bipyramid test) | python s4_d3_exact_certificate.py | < 1 s | - |
| s4int_d3_exact_certificate.py | exact gcd-free integer-scaled certificate in Z[rho]; tail by Lemma T | python s4int_d3_exact_certificate.py SPEC.json 600 | 7 s | s4int_*.txt, s5_B_den1e8.txt |
| s4iv_d3_interval_certificate.py | interval-arithmetic attempt (FAILS: exponential width growth of the forward recurrence; kept for the record) | - | - | s4iv_refined_den1e8.txt |
| s5_rationalise_and_certify.py | numerical optimum -> exact rational/Q(sqrt q) frame (stereographic rational points, den 1e8) -> s4int | python s5_rationalise_and_certify.py s6_refined_B.json 600 100000000 | 7 s | s5_B_den1e8.txt, *_exact_den*.json |
| s6_tie_refine_mp.py | 40-digit Gauss-Newton refinement of the tie system + KKT multipliers | python s6_tie_refine_mp.py s3_best_seed0.json 4,8,9,12,16 s6_refined_B.json | ~1 min | s6_out_B.txt, s6_refined_B.json (optimum A: s6_out.txt, s6_refined.json) |
| s7_identify_and_rank.py | rank of active gradients; findpoly/identify attempts | python s7_identify_and_rank.py s6_refined_B.json 4,8,9,12,16 | ~1 min | s7_out_B.txt, s7_out.txt |
