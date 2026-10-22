/-! Green 37 / Green 27 witnesses.  Core Lean 4, no Mathlib.  Checked by native_decide (trusts compiler) and `decide +kernel` for small ones. -/

def covers (A : List Nat) (N k : Nat) : Bool :=
  (List.range N).all fun i => A.any fun a => (List.range k).all fun j => A.contains (a + j * (i + 1))

def reps (p : Nat) (A : List Nat) (s : Nat) : Nat :=
  (A.map fun c => (A.filter fun d => c ≤ d && (c + d) % p == s % p).length).foldl (· + ·) 0

def noUnique (p : Nat) (A : List Nat) : Bool :=
  decide (2 ≤ A.length) && A.all fun a => A.all fun b => decide (2 ≤ reps p A (a + b))

theorem g37_k3_N1 : covers [0, 1, 2] 1 3 = true := by native_decide
theorem g37_k3_N1_kernel : covers [0, 1, 2] 1 3 = true := by decide +kernel
theorem g37_k3_N2 : covers [0, 1, 2, 4] 2 3 = true := by native_decide
theorem g37_k3_N2_kernel : covers [0, 1, 2, 4] 2 3 = true := by decide +kernel
theorem g37_k3_N3 : covers [0, 2, 3, 4, 6] 3 3 = true := by native_decide
theorem g37_k3_N3_kernel : covers [0, 2, 3, 4, 6] 3 3 = true := by decide +kernel
theorem g37_k3_N4 : covers [0, 3, 4, 6, 7, 8] 4 3 = true := by native_decide
theorem g37_k3_N4_kernel : covers [0, 3, 4, 6, 7, 8] 4 3 = true := by decide +kernel
theorem g37_k3_N5 : covers [0, 4, 5, 7, 8, 9, 10] 5 3 = true := by native_decide
theorem g37_k3_N5_kernel : covers [0, 4, 5, 7, 8, 9, 10] 5 3 = true := by decide +kernel
theorem g37_k3_N6 : covers [0, 1, 2, 4, 6, 7, 8, 12] 6 3 = true := by native_decide
theorem g37_k3_N6_kernel : covers [0, 1, 2, 4, 6, 7, 8, 12] 6 3 = true := by decide +kernel
theorem g37_k3_N7 : covers [0, 5, 6, 7, 10, 12, 13, 14] 7 3 = true := by native_decide
theorem g37_k3_N7_kernel : covers [0, 5, 6, 7, 10, 12, 13, 14] 7 3 = true := by decide +kernel
theorem g37_k3_N8 : covers [0, 6, 7, 8, 11, 12, 14, 16] 8 3 = true := by native_decide
theorem g37_k3_N8_kernel : covers [0, 6, 7, 8, 11, 12, 14, 16] 8 3 = true := by decide +kernel
theorem g37_k3_N9 : covers [0, 2, 4, 8, 9, 10, 11, 14, 18] 9 3 = true := by native_decide
theorem g37_k3_N9_kernel : covers [0, 2, 4, 8, 9, 10, 11, 14, 18] 9 3 = true := by decide +kernel
theorem g37_k3_N10 : covers [0, 2, 4, 6, 7, 10, 11, 12, 13, 20] 10 3 = true := by native_decide
theorem g37_k3_N10_kernel : covers [0, 2, 4, 6, 7, 10, 11, 12, 13, 20] 10 3 = true := by decide +kernel
theorem g37_k3_N11 : covers [0, 8, 9, 10, 11, 15, 16, 18, 19, 20, 22] 11 3 = true := by native_decide
theorem g37_k3_N11_kernel : covers [0, 8, 9, 10, 11, 15, 16, 18, 19, 20, 22] 11 3 = true := by decide +kernel
theorem g37_k3_N12 : covers [0, 2, 4, 9, 10, 12, 13, 14, 16, 18, 24] 12 3 = true := by native_decide
theorem g37_k3_N12_kernel : covers [0, 2, 4, 9, 10, 12, 13, 14, 16, 18, 24] 12 3 = true := by decide +kernel
theorem g37_k3_N13 : covers [0, 2, 4, 6, 9, 10, 13, 14, 15, 16, 18, 26] 13 3 = true := by native_decide
theorem g37_k3_N14 : covers [0, 2, 4, 8, 11, 13, 14, 15, 16, 18, 22, 28] 14 3 = true := by native_decide
theorem g37_k3_N15 : covers [0, 5, 10, 12, 13, 14, 17, 20, 24, 26, 28, 35] 15 3 = true := by native_decide
theorem g37_k3_N16 : covers [0, 2, 4, 12, 13, 16, 17, 18, 19, 22, 24, 26, 32] 16 3 = true := by native_decide
theorem g37_k3_N17 : covers [0, 2, 6, 9, 15, 16, 17, 18, 21, 26, 28, 30, 34] 17 3 = true := by native_decide
theorem g37_k3_N18 : covers [0, 2, 4, 6, 14, 15, 18, 19, 20, 21, 24, 26, 28, 36] 18 3 = true := by native_decide
theorem g37_k3_N19 : covers [0, 4, 10, 12, 17, 18, 19, 20, 23, 24, 28, 34, 36, 38] 19 3 = true := by native_decide
theorem g37_k3_N20 : covers [0, 2, 4, 6, 8, 11, 16, 17, 20, 21, 22, 23, 30, 32, 40] 20 3 = true := by native_decide
theorem g37_k3_N21 : covers [0, 2, 8, 16, 18, 20, 21, 23, 24, 25, 29, 30, 38, 40, 42] 21 3 = true := by native_decide
theorem g37_k3_N22 : covers [0, 2, 4, 6, 10, 13, 18, 19, 20, 22, 23, 24, 25, 34, 36, 44] 22 3 = true := by native_decide
theorem g37_k3_N23 : covers [0, 2, 8, 17, 18, 20, 22, 23, 26, 27, 32, 33, 34, 42, 44, 46] 23 3 = true := by native_decide
theorem g37_k3_N24 : covers [0, 2, 4, 6, 14, 18, 19, 20, 21, 24, 25, 26, 27, 32, 36, 40, 48] 24 3 = true := by native_decide
theorem g37_k3_N25 : covers [0, 2, 6, 10, 20, 21, 23, 24, 25, 26, 33, 34, 40, 42, 45, 46, 50] 25 3 = true := by native_decide
theorem g37_k3_N26 : covers [0, 2, 4, 10, 14, 18, 20, 21, 25, 26, 27, 28, 31, 36, 40, 48, 52] 26 3 = true := by native_decide
theorem g37_k3_N27 : covers [0, 2, 4, 6, 10, 15, 16, 20, 22, 27, 28, 29, 30, 33, 38, 48, 50, 54] 27 3 = true := by native_decide
theorem g37_k4_N1 : covers [0, 1, 2, 3] 1 4 = true := by native_decide
theorem g37_k4_N1_kernel : covers [0, 1, 2, 3] 1 4 = true := by decide +kernel
theorem g37_k4_N2 : covers [0, 1, 2, 3, 4, 6] 2 4 = true := by native_decide
theorem g37_k4_N2_kernel : covers [0, 1, 2, 3, 4, 6] 2 4 = true := by decide +kernel
theorem g37_k4_N3 : covers [0, 1, 2, 3, 4, 6, 9] 3 4 = true := by native_decide
theorem g37_k4_N3_kernel : covers [0, 1, 2, 3, 4, 6, 9] 3 4 = true := by decide +kernel
theorem g37_k4_N4 : covers [0, 3, 4, 6, 8, 9, 10, 11, 12] 4 4 = true := by native_decide
theorem g37_k4_N4_kernel : covers [0, 3, 4, 6, 8, 9, 10, 11, 12] 4 4 = true := by decide +kernel
theorem g37_k4_N5 : covers [0, 1, 2, 3, 4, 5, 7, 10, 11, 15] 5 4 = true := by native_decide
theorem g37_k4_N5_kernel : covers [0, 1, 2, 3, 4, 5, 7, 10, 11, 15] 5 4 = true := by decide +kernel
theorem g37_k4_N6 : covers [0, 1, 2, 3, 4, 6, 8, 9, 12, 13, 18] 6 4 = true := by native_decide
theorem g37_k4_N6_kernel : covers [0, 1, 2, 3, 4, 6, 8, 9, 12, 13, 18] 6 4 = true := by decide +kernel
theorem g37_k4_N7 : covers [0, 3, 5, 7, 8, 9, 10, 11, 14, 15, 21] 7 4 = true := by native_decide
theorem g37_k4_N7_kernel : covers [0, 3, 5, 7, 8, 9, 10, 11, 14, 15, 21] 7 4 = true := by decide +kernel
theorem g37_k4_N8 : covers [0, 3, 6, 8, 10, 11, 12, 13, 14, 16, 17, 18, 24] 8 4 = true := by native_decide
theorem g37_k4_N8_kernel : covers [0, 3, 6, 8, 10, 11, 12, 13, 14, 16, 17, 18, 24] 8 4 = true := by decide +kernel
theorem g37_k4_N9 : covers [0, 7, 8, 9, 14, 16, 18, 19, 20, 21, 22, 24, 26, 27] 9 4 = true := by native_decide
theorem g37_k4_N9_kernel : covers [0, 7, 8, 9, 14, 16, 18, 19, 20, 21, 22, 24, 26, 27] 9 4 = true := by decide +kernel
theorem g37_k4_N10 : covers [0, 3, 5, 6, 7, 9, 10, 11, 12, 14, 15, 20, 21, 22, 30] 10 4 = true := by native_decide
theorem g37_k4_N10_kernel : covers [0, 3, 5, 6, 7, 9, 10, 11, 12, 14, 15, 20, 21, 22, 30] 10 4 = true := by decide +kernel
theorem g37_k4_N11 : covers [0, 3, 5, 6, 9, 10, 11, 13, 15, 17, 22, 23, 24, 25, 33] 11 4 = true := by native_decide
theorem g37_k4_N11_kernel : covers [0, 3, 5, 6, 9, 10, 11, 13, 15, 17, 22, 23, 24, 25, 33] 11 4 = true := by decide +kernel
theorem g37_k4_N12 : covers [0, 3, 6, 8, 9, 12, 13, 14, 16, 18, 20, 24, 25, 26, 27, 36] 12 4 = true := by native_decide
theorem g37_k4_N12_kernel : covers [0, 3, 6, 8, 9, 12, 13, 14, 16, 18, 20, 24, 25, 26, 27, 36] 12 4 = true := by decide +kernel
theorem g37_k4_N13 : covers [0, 3, 6, 9, 11, 13, 15, 17, 18, 19, 20, 23, 26, 27, 28, 29, 39] 13 4 = true := by native_decide
theorem g37_k4_N14 : covers [0, 6, 7, 12, 13, 14, 15, 17, 18, 21, 22, 26, 28, 30, 32, 39, 42] 14 4 = true := by native_decide
theorem g37_k4_N15 : covers [0, 3, 6, 13, 15, 17, 19, 23, 24, 27, 28, 30, 31, 32, 33, 38, 39, 45] 15 4 = true := by native_decide
theorem g37_k4_N16 : covers [0, 3, 6, 11, 12, 14, 16, 18, 21, 22, 25, 28, 29, 30, 31, 32, 33, 42, 48] 16 4 = true := by native_decide
theorem g37_k4_N17 : covers [0, 3, 6, 9, 14, 15, 17, 19, 21, 24, 25, 28, 31, 32, 33, 34, 35, 36, 45, 51] 17 4 = true := by native_decide
theorem g37_k4_N18 : covers [0, 3, 5, 6, 8, 9, 12, 13, 16, 18, 20, 22, 24, 26, 27, 36, 37, 38, 39, 40, 54] 18 4 = true := by native_decide
theorem g37_k4_N19 : covers [0, 6, 12, 18, 19, 22, 23, 26, 27, 30, 32, 33, 34, 35, 36, 38, 40, 42, 45, 54, 57] 19 4 = true := by native_decide
theorem g37_k4_N20 : covers [0, 3, 16, 18, 20, 22, 24, 29, 32, 33, 36, 37, 40, 41, 42, 43, 46, 48, 51, 52, 54, 60] 20 4 = true := by native_decide
theorem g27_p3 : noUnique 3 [0, 1, 2] = true := by native_decide
theorem g27_p3_kernel : noUnique 3 [0, 1, 2] = true := by decide +kernel
theorem g27_p5 : noUnique 5 [0, 1, 2, 3] = true := by native_decide
theorem g27_p5_kernel : noUnique 5 [0, 1, 2, 3] = true := by decide +kernel
theorem g27_p7 : noUnique 7 [0, 1, 2, 3, 4] = true := by native_decide
theorem g27_p7_kernel : noUnique 7 [0, 1, 2, 3, 4] = true := by decide +kernel
theorem g27_p11 : noUnique 11 [0, 1, 2, 3, 4, 5, 6] = true := by native_decide
theorem g27_p11_kernel : noUnique 11 [0, 1, 2, 3, 4, 5, 6] = true := by decide +kernel
theorem g27_p13 : noUnique 13 [0, 1, 3, 4, 5, 7, 8] = true := by native_decide
theorem g27_p13_kernel : noUnique 13 [0, 1, 3, 4, 5, 7, 8] = true := by decide +kernel
theorem g27_p17 : noUnique 17 [0, 1, 5, 7, 8, 10, 11, 13] = true := by native_decide
theorem g27_p17_kernel : noUnique 17 [0, 1, 5, 7, 8, 10, 11, 13] = true := by decide +kernel
theorem g27_p19 : noUnique 19 [0, 1, 10, 11, 12, 13, 15, 17, 18] = true := by native_decide
theorem g27_p19_kernel : noUnique 19 [0, 1, 10, 11, 12, 13, 15, 17, 18] = true := by decide +kernel
theorem g27_p23 : noUnique 23 [0, 1, 12, 13, 14, 15, 17, 19, 21, 22] = true := by native_decide
theorem g27_p23_kernel : noUnique 23 [0, 1, 12, 13, 14, 15, 17, 19, 21, 22] = true := by decide +kernel
theorem g27_p29 : noUnique 29 [0, 1, 2, 3, 5, 7, 8, 9, 12, 13, 17] = true := by native_decide
theorem g27_p29_kernel : noUnique 29 [0, 1, 2, 3, 5, 7, 8, 9, 12, 13, 17] = true := by decide +kernel
theorem g27_p31 : noUnique 31 [0, 1, 2, 3, 4, 8, 9, 13, 14, 18, 19] = true := by native_decide
theorem g27_p31_kernel : noUnique 31 [0, 1, 2, 3, 4, 8, 9, 13, 14, 18, 19] = true := by decide +kernel
