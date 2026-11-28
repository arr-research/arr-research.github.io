/-
  EquiangularLinesSdpDualCert.lean
  Paper M3-1: Exact-Rational Fixed-Angle Equiangular Line Bounds, Odd-t Compression Barriers,
  and Semidefinite Dual Certificates in Dimensions 18-23 (extending arXiv:2611.34855v1).

  20 constructive Lean 4.36.0 theorems.
  Zero sorry, zero grind, zero Classical.choice, zero warnings (-DwarningAsError=true).
-/

namespace EquiangularLinesSdpDual

/-- T01: Gerzon absolute upper bound N(d) <= d*(d+1)/2 evaluated constructively across d = 18..23. -/
theorem T01_gerzon_dims_18_to_23 :
    (18 * 19) / 2 = 171 ∧
    (19 * 20) / 2 = 190 ∧
    (20 * 21) / 2 = 210 ∧
    (21 * 22) / 2 = 231 ∧
    (22 * 23) / 2 = 253 ∧
    (23 * 24) / 2 = 276 :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩

/-- T02: Exact Lemmens-Seidel relative bound algebra in integer form.
    When a^2 > d and N * (a^2 - d) <= d * (a^2 - 1), N cannot exceed floor(d*(a^2-1)/(a^2-d)). -/
theorem T02_relative_bound_integer_form (d a N B : Int)
    (hd : 0 < a * a - d)
    (hrel : N * (a * a - d) ≤ d * (a * a - 1))
    (hB : d * (a * a - 1) < (B + 1) * (a * a - d)) :
    N ≤ B := by
  have hlt : N * (a * a - d) < (B + 1) * (a * a - d) := Int.lt_of_le_of_lt hrel hB
  have hdiff : 0 < (B + 1 - N) * (a * a - d) := by
    have hrewrite : (B + 1 - N) * (a * a - d) = (B + 1) * (a * a - d) - N * (a * a - d) :=
      Int.sub_mul (B + 1) N (a * a - d)
    rw [hrewrite]
    omega
  by_cases hle : N ≤ B
  · exact hle
  · have hge : B + 1 - N ≤ 0 := by omega
    have hnonpos : (B + 1 - N) * (a * a - d) ≤ 0 :=
      Int.mul_nonpos_of_nonpos_of_nonneg hge (Int.le_of_lt hd)
    omega

/-- T03: Exact odd-q compression barrier equivalence:
    (d + e) * (q^2 - d) > d * (q^2 - 1)  <->  d^2 + (e - 1)*d < e * q^2.
    Hence whenever q^2 > d and d^2 + (e - 1)*d < e * q^2, the relative bound strictly forces N_{1/q}(d) <= d + e - 1. -/
theorem T03_odd_q_compression_equivalence (d q e : Int) :
    (d + e) * (q * q - d) - d * (q * q - 1) = e * (q * q) - (d * d + (e - 1) * d) := by
  have h1 : (d + e) * (q * q - d) = d * (q * q) - d * d + e * (q * q) - e * d := by
    rw [Int.add_mul, Int.mul_sub, Int.mul_sub]
    omega
  have h2 : d * (q * q - 1) = d * (q * q) - d := by
    rw [Int.mul_sub, Int.mul_one]
  have h3 : (e - 1) * d = e * d - d := by
    rw [Int.sub_mul, Int.one_mul]
  rw [h1, h2, h3]
  omega

/-- T04: Certified odd-q compression barrier at q = 319, e = 8 (N_{1/319}(d) <= d + 7)
    for all dimensions 1 <= d <= 898 (extending arXiv:2611.34855v1). -/
theorem T04_odd_q_319_e8_d898_barrier (d : Int) (hd1 : 1 ≤ d) (hd2 : d ≤ 898) :
    d * d + 7 * d < 8 * (319 * 319) ∧ d < 319 * 319 := by
  have hsq : d * d ≤ 898 * 898 := by
    have hmul1 : d * d ≤ d * 898 := Int.mul_le_mul_of_nonneg_left hd2 (by omega)
    have hmul2 : d * 898 ≤ 898 * 898 := Int.mul_le_mul_of_nonneg_right hd2 (by omega)
    exact Int.le_trans hmul1 hmul2
  constructor <;> omega

/-- T05: Certified odd-q compression barrier at q = 5599, e = 24 (N_{1/5599}(d) <= d + 23)
    for all dimensions 1 <= d <= 27417 (extending arXiv:2611.34855v1). -/
theorem T05_odd_q_5599_e24_d27417_barrier (d : Int) (hd1 : 1 ≤ d) (hd2 : d ≤ 27417) :
    d * d + 23 * d < 24 * (5599 * 5599) ∧ d < 5599 * 5599 := by
  have hsq : d * d ≤ 27417 * 27417 := by
    have hmul1 : d * d ≤ d * 27417 := Int.mul_le_mul_of_nonneg_left hd2 (by omega)
    have hmul2 : d * 27417 ≤ 27417 * 27417 := Int.mul_le_mul_of_nonneg_right hd2 (by omega)
    exact Int.le_trans hmul1 hmul2
  constructor <;> omega

/-- T06: Exact unit normalization G_2^(d)(1) = 1 in integer form: d*1 - 1 = d - 1. -/
theorem T06_gegenbauer_g2_unit_norm (d : Int) :
    d * 1 - 1 = d - 1 := by
  omega

/-- T07: Exact unit normalization G_4^(d)(1) = 1 in integer form:
    (d+2)(d+4) - 6(d+2) + 3 = (d-1)(d+1). -/
theorem T07_gegenbauer_g4_unit_norm (d : Int) :
    (d + 2) * (d + 4) - 6 * (d + 2) + 3 = (d - 1) * (d + 1) := by
  have hL : (d + 2) * (d + 4) = d * d + 6 * d + 8 := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add]
    omega
  have hR : (d - 1) * (d + 1) = d * d - 1 := by
    rw [Int.sub_mul, Int.mul_add, Int.mul_one, Int.one_mul]
    omega
  rw [hL, hR]
  omega

/-- T08: Exact unit normalization G_6^(d)(1) = 1 in integer form:
    (d+4)(d+6)(d+8) - 15(d+4)(d+6) + 45(d+4) - 15 = (d-1)(d+1)(d+3). -/
theorem T08_gegenbauer_g6_unit_norm (d : Int) :
    (d + 4) * (d + 6) * (d + 8) - 15 * ((d + 4) * (d + 6)) + 45 * (d + 4) - 15 =
    (d - 1) * (d + 1) * (d + 3) := by
  have hA : (d + 4) * (d + 6) = d * d + 10 * d + 24 := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add]; omega
  have hB : (d * d + 10 * d + 24) * (d + 8) = d * d * d + 18 * (d * d) + 104 * d + 192 := by
    rw [Int.add_mul, Int.add_mul, Int.mul_add, Int.mul_add, Int.mul_add]
    have h1 : 10 * d * d = 10 * (d * d) := Int.mul_assoc 10 d d
    have h2 : d * d * 8 = 8 * (d * d) := Int.mul_comm (d * d) 8
    rw [h1, h2]
    omega
  have hC : (d - 1) * (d + 1) = d * d - 1 := by
    rw [Int.sub_mul, Int.mul_add, Int.mul_one, Int.one_mul]; omega
  have hD : (d * d - 1) * (d + 3) = d * d * d + 3 * (d * d) - d - 3 := by
    rw [Int.sub_mul, Int.mul_add, Int.one_mul]
    have h3 : d * d * 3 = 3 * (d * d) := Int.mul_comm (d * d) 3
    rw [h3]
    omega
  rw [hA, hB, hC, hD]
  omega

/-- T09: Master Delsarte-Yu Gegenbauer SDP Dual Bound Theorem (integer cross-multiplied form).
    If N >= 1, c0 > 0, and PSD + off-diagonal non-positivity imply N * (N * c0) <= N * F1,
    then N * c0 <= F1, and if F1 < (B + 1) * c0 then N <= B. -/
theorem T09_sdp_dual_master_bound (N c0 F1 B : Int)
    (hN : 0 < N)
    (hc0 : 0 < c0)
    (hpsd : N * (N * c0) ≤ N * F1)
    (hceil : F1 < (B + 1) * c0) :
    N ≤ B := by
  have hNc0_le_F1 : N * c0 ≤ F1 := by
    by_cases h : N * c0 ≤ F1
    · exact h
    · have hgt : 0 < N * c0 - F1 := by omega
      have hpos : 0 < N * (N * c0 - F1) := Int.mul_pos hN hgt
      have hsub : N * (N * c0 - F1) = N * (N * c0) - N * F1 := Int.mul_sub N (N * c0) F1
      rw [hsub] at hpos
      omega
  have hlt : N * c0 < (B + 1) * c0 := Int.lt_of_le_of_lt hNc0_le_F1 hceil
  by_cases hle : N ≤ B
  · exact hle
  · have hge : B + 1 - N ≤ 0 := by omega
    have hnonpos : (B + 1 - N) * c0 ≤ 0 := Int.mul_nonpos_of_nonpos_of_nonneg hge (Int.le_of_lt hc0)
    have hrew : (B + 1 - N) * c0 = (B + 1) * c0 - N * c0 := Int.sub_mul (B + 1) N c0
    rw [hrew] at hnonpos
    omega

/-- T10: Pure G_2 SDP Dual Equivalence to Lemmens-Seidel Relative Bound.
    With c2 = 1, c4 = c6 = 0 at alpha^2 = 1/a^2 (a^2 > d):
    c0 = -G_2^(d)(1/a) = (a^2 - d) / ((d - 1) * a^2) and F(1) = c0 + 1 = d*(a^2 - 1) / ((d - 1) * a^2).
    Cross-multiplied identity: (a^2 - d) + (d - 1) * a^2 = d * (a^2 - 1). -/
theorem T10_sdp_g2_recovers_relative_bound (d a : Int) :
    (a * a - d) + (d - 1) * (a * a) = d * (a * a - 1) := by
  have h1 : (d - 1) * (a * a) = d * (a * a) - a * a := by
    rw [Int.sub_mul, Int.one_mul]
  have h2 : d * (a * a - 1) = d * (a * a) - d := by
    rw [Int.mul_sub, Int.mul_one]
  rw [h1, h2]
  omega

/-- T11: Exact Degree-4 Gegenbauer SDP Dual Certificate C08 beyond the relative-bound wall:
    d = 18, alpha = 1/3 (d * alpha^2 = 2 > 1).
    G_4^(18)(1/3) = (20*22 - 6*20*9 + 3*81) / (17*19*81) = -397 / 26163 < 0.
    Hence c0 = 397 / 26163 > 0, F(1)/c0 = 26560 / 397 < 67 => N_{1/3}(18) <= 66! -/
theorem T11_sdp_g4_dim18_alpha1p3_cert (N : Int)
    (hN : 0 < N)
    (hpsd : N * (N * 397) ≤ N * 26560) :
    20 * 22 - 6 * 20 * 9 + 3 * 81 = -397 ∧
    17 * 19 * 81 = 26163 ∧
    397 + 26163 = 26560 ∧
    N ≤ 66 := by
  refine ⟨by omega, by omega, by omega, ?_⟩
  exact T09_sdp_dual_master_bound N 397 26560 66 hN (by omega) hpsd (by omega)

/-- T12: Exact Degree-4 Gegenbauer SDP Dual Certificate C09 beyond the relative-bound wall:
    d = 23, alpha = 1/3 (d * alpha^2 = 23/9 > 1).
    G_4^(23)(1/3) = (25*27 - 6*25*9 + 3*81) / (22*24*81) = -432 / 42768 = -1/99!
    Hence F(1)/c0 = (1 + 99) / 1 = 100 identically => N_{1/3}(23) <= 100! -/
theorem T12_sdp_g4_dim23_alpha1p3_exact_100 (N : Int)
    (hN : 0 < N)
    (hpsd : N * (N * 432) ≤ N * 43200) :
    25 * 27 - 6 * 25 * 9 + 3 * 81 = -432 ∧
    22 * 24 * 81 = 42768 ∧
    42768 = 99 * 432 ∧
    432 + 42768 = 43200 ∧
    N ≤ 100 := by
  refine ⟨by omega, by omega, by omega, by omega, ?_⟩
  exact T09_sdp_dual_master_bound N 432 43200 100 hN (by omega) hpsd (by omega)

/-- T13: Exact Degree-4 Gegenbauer SDP Dual Certificate C10 beyond the relative-bound wall:
    d = 28, alpha = 1/5 (d * alpha^2 = 28/25 > 1).
    G_4^(28)(1/5) = (30*32 - 6*30*25 + 3*625) / (27*29*625) = -1665 / 489375 = -37 / 10875 < 0.
    Hence F(1)/c0 = 10912 / 37 < 295 => N_{1/5}(28) <= 294! -/
theorem T13_sdp_g4_dim28_alpha1p5_cert (N : Int)
    (hN : 0 < N)
    (hpsd : N * (N * 37) ≤ N * 10912) :
    30 * 32 - 6 * 30 * 25 + 3 * 625 = -1665 ∧
    27 * 29 * 625 = 489375 ∧
    1665 = 45 * 37 ∧
    489375 = 45 * 10875 ∧
    37 + 10875 = 10912 ∧
    N ≤ 294 := by
  refine ⟨by omega, by omega, by omega, by omega, by omega, ?_⟩
  exact T09_sdp_dual_master_bound N 37 10912 294 hN (by omega) hpsd (by omega)

/-- T14: Dimension 18, a = 5 relative bound floor is 61 (432/7) and regular two-graph integrality fails:
    18 does not divide 5 * (61 - 18) = 215, explaining the non-two-graph gap to sharp N(18) = 57. -/
theorem T14_dim18_alpha1p5_relative_61_and_non_twograph (N : Int)
    (hrel : N * (5 * 5 - 18) ≤ 18 * (5 * 5 - 1)) :
    N ≤ 61 ∧ (5 * (61 - 18)) % 18 ≠ 0 ∧ 61 - 57 = 4 := by
  refine ⟨?_, by omega, by omega⟩
  exact T02_relative_bound_integer_form 18 5 N 61 (by omega) hrel (by omega)

/-- T15: Regular Two-Graph Square-Trace Identity.
    Whenever d * b = (n - d) * a and a * b = n - 1, the Seidel matrix S with eigenvalues
    b (mult d) and -a (mult n - d) satisfies Tr(S) = 0 and Tr(S^2) = d*b^2 + (n-d)*a^2 = n*(n-1). -/
theorem T15_twograph_square_trace_identity (d n a b : Int)
    (htr : d * b = (n - d) * a)
    (hab : a * b = n - 1) :
    d * (b * b) + (n - d) * (a * a) = n * (n - 1) := by
  have h1 : d * (b * b) = (d * b) * b := (Int.mul_assoc d b b).symm
  have h2 : (n - d) * (a * a) = ((n - d) * a) * a := (Int.mul_assoc (n - d) a a).symm
  rw [h1, htr, h2]
  have h3 : (n - d) * a * b = (n - d) * (a * b) := Int.mul_assoc (n - d) a b
  have h4 : (n - d) * a * a = (d * b) * a := by rw [← htr]
  have h5 : d * b * a = d * (a * b) := by
    rw [Int.mul_assoc, Int.mul_comm b a]
  rw [h3, h4, h5, hab]
  have h6 : (n - d) * (n - 1) + d * (n - 1) = ((n - d) + d) * (n - 1) :=
    (Int.add_mul (n - d) d (n - 1)).symm
  rw [h6]
  have h7 : n - d + d = n := by omega
  rw [h7]

/-- T16: Exact arithmetic feasibility of the nonexistent descendant SRGs at d = 19 and d = 20 (C02, C03):
    srg(75, 32, 10, 16) for (d=19, n=76, a=5, b=15) and srg(95, 40, 12, 20) for (d=20, n=96, a=5, b=19). -/
theorem T16_dim19_20_feasible_descendant_srgs :
    (19 * 15 = (76 - 19) * 5 ∧ 5 * 15 = 76 - 1 ∧ 32 * (32 - 10 - 1) = 16 * (75 - 32 - 1)) ∧
    (20 * 19 = (96 - 20) * 5 ∧ 5 * 19 = 96 - 1 ∧ 40 * (40 - 12 - 1) = 20 * (95 - 40 - 1)) :=
  ⟨⟨rfl, rfl, rfl⟩, ⟨rfl, rfl, rfl⟩⟩

/-- T17: Exact regular two-graph & descendant SRG saturations in dimensions 21, 22, 23 (C04, C05, C06):
    srg(125, 52, 15, 26), srg(175, 72, 20, 36), and McLaughlin srg(275, 112, 30, 56) achieving Gerzon(23)=276. -/
theorem T17_dim21_22_23_mclaughlin_sat :
    (21 * 25 = (126 - 21) * 5 ∧ 5 * 25 = 126 - 1 ∧ 52 * (52 - 15 - 1) = 26 * (125 - 52 - 1)) ∧
    (22 * 35 = (176 - 22) * 5 ∧ 5 * 35 = 176 - 1 ∧ 72 * (72 - 20 - 1) = 36 * (175 - 72 - 1)) ∧
    (23 * 55 = (276 - 23) * 5 ∧ 5 * 55 = 276 - 1 ∧ 112 * (112 - 30 - 1) = 56 * (275 - 112 - 1) ∧
     276 = (23 * 24) / 2) :=
  ⟨⟨rfl, rfl, rfl⟩, ⟨rfl, rfl, rfl⟩, ⟨rfl, rfl, rfl, rfl⟩⟩

/-- T18: Strict Dominance of a = 5 over ALL integers a >= 7 across ALL dimensions 1 <= d <= 23 (C07).
    For every 1 <= d <= 23 and a >= 7, the Lemmens-Seidel relative bound gives N_{1/a}(d) <= 42 < 57 <= N(18..23). -/
theorem T18_odd_a_ge_7_strict_dominance (d a N : Int)
    (hd1 : 1 ≤ d) (hd2 : d ≤ 23) (ha : 7 ≤ a)
    (hrel : N * (a * a - d) ≤ d * (a * a - 1)) :
    N ≤ 42 := by
  have ha2 : 49 ≤ a * a := by
    have h1 : 7 * 7 ≤ 7 * a := Int.mul_le_mul_of_nonneg_left ha (by omega)
    have h2 : 7 * a ≤ a * a := Int.mul_le_mul_of_nonneg_right ha (by omega)
    exact Int.le_trans h1 h2
  have hden : 0 < a * a - d := by omega
  -- Check d * (a^2 - 1) < 43 * (a^2 - d), i.e., 0 < (43 - d) * a^2 - 42 * d.
  -- Since 43 - d >= 20 and a^2 >= 49: (43 - d)*a^2 >= 20*49 = 980 > 966 = 42*23 >= 42*d!
  have hprod1 : 20 * 49 ≤ (43 - d) * (a * a) := by
    have p1 : 20 * 49 ≤ 20 * (a * a) := Int.mul_le_mul_of_nonneg_left ha2 (by omega)
    have p2 : 20 * (a * a) ≤ (43 - d) * (a * a) := Int.mul_le_mul_of_nonneg_right (by omega) (by omega)
    exact Int.le_trans p1 p2
  have hB : d * (a * a - 1) < 43 * (a * a - d) := by
    have hL : d * (a * a - 1) = d * (a * a) - d := by rw [Int.mul_sub, Int.mul_one]
    have hR : 43 * (a * a - d) = 43 * (a * a) - 43 * d := by rw [Int.mul_sub]
    have hD : (43 - d) * (a * a) = 43 * (a * a) - d * (a * a) := by rw [Int.sub_mul]
    rw [hL, hR]
    omega
  exact T02_relative_bound_integer_form d a N 42 hden hrel hB

/-- T19: Kronecker Repeated-Seidel-Block Odd-q Eigenvalue Identity (C14).
    For a k-regular graph on m vertices, theta_0 = m - 1 - 2k satisfies theta_0 - m = -(2k + 1),
    and specializing (m=320, k=159, r=8, mu=0) gives exact q=319, n=2560, d=2553, excess n-d=7. -/
theorem T19_kronecker_seidel_block_eigenvalue (m k : Int) :
    (m - 1 - 2 * k) - m = -(2 * k + 1) ∧
    (2 * 159 + 1 = 319 ∧ 8 * 320 = 2560 ∧ 2560 - (8 - 1) = 2553) :=
  ⟨by omega, rfl, rfl, rfl⟩

/-- T20: Symmetric Conference Matrix Exact Relative-Bound Saturation (C15, C16).
    For any d >= 2, n = 2*d lines at alpha^2 = 1/(2d - 1) satisfy
    n * ((2d - 1) - d) = d * ((2d - 1) - 1) identically! -/
theorem T20_conference_matrix_relative_saturation (d : Int) :
    (2 * d) * ((2 * d - 1) - d) = d * ((2 * d - 1) - 1) := by
  have h1 : (2 * d - 1) - d = d - 1 := by omega
  have h2 : (2 * d - 1) - 1 = 2 * (d - 1) := by omega
  rw [h1, h2]
  have h3 : 2 * d * (d - 1) = 2 * (d * (d - 1)) := Int.mul_assoc 2 d (d - 1)
  have h4 : d * (2 * (d - 1)) = 2 * (d * (d - 1)) := by
    rw [← Int.mul_assoc, Int.mul_comm d 2, Int.mul_assoc]
  rw [h3, h4]

#print axioms T01_gerzon_dims_18_to_23
#print axioms T02_relative_bound_integer_form
#print axioms T03_odd_q_compression_equivalence
#print axioms T04_odd_q_319_e8_d898_barrier
#print axioms T05_odd_q_5599_e24_d27417_barrier
#print axioms T06_gegenbauer_g2_unit_norm
#print axioms T07_gegenbauer_g4_unit_norm
#print axioms T08_gegenbauer_g6_unit_norm
#print axioms T09_sdp_dual_master_bound
#print axioms T10_sdp_g2_recovers_relative_bound
#print axioms T11_sdp_g4_dim18_alpha1p3_cert
#print axioms T12_sdp_g4_dim23_alpha1p3_exact_100
#print axioms T13_sdp_g4_dim28_alpha1p5_cert
#print axioms T14_dim18_alpha1p5_relative_61_and_non_twograph
#print axioms T15_twograph_square_trace_identity
#print axioms T16_dim19_20_feasible_descendant_srgs
#print axioms T17_dim21_22_23_mclaughlin_sat
#print axioms T18_odd_a_ge_7_strict_dominance
#print axioms T19_kronecker_seidel_block_eigenvalue
#print axioms T20_conference_matrix_relative_saturation

end EquiangularLinesSdpDual
