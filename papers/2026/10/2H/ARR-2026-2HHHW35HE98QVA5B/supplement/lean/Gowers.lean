/-! Gowers-Long F(n): witness 2-increasing sequences of triples. Core Lean 4 only (no Mathlib).
    a <_2 b : a_i < b_i for at least two coordinates i. -/
abbrev T3 := Nat × Nat × Nat
def lt2 (a b : T3) : Bool :=
  ((if a.1 < b.1 then 1 else 0) + (if a.2.1 < b.2.1 then 1 else 0) + (if a.2.2 < b.2.2 then 1 else 0)) ≥ 2
def inRange (n : Nat) (a : T3) : Bool :=
  1 ≤ a.1 && a.1 ≤ n && 1 ≤ a.2.1 && a.2.1 ≤ n && 1 ≤ a.2.2 && a.2.2 ≤ n
/-- every pair i<j satisfies s[i] <_2 s[j], all coordinates in [1,n] -/
def good (n : Nat) (s : List T3) : Bool :=
  s.all (inRange n) &&
  (List.range s.length).all fun i => (List.range s.length).all fun j =>
    !(i < j) || lt2 (s.getD i (0,0,0)) (s.getD j (0,0,0))

def w6 : List T3 := [(1,1,1), (1,2,2), (1,3,3), (2,1,4), (2,2,5), (2,3,6), (3,4,1), (4,5,1), (3,6,2), (5,4,3), (4,6,4), (6,4,5), (5,5,6), (6,6,6)]
def w7 : List T3 := [(1,1,1), (2,2,1), (3,2,2), (1,3,3), (2,4,3), (3,3,4), (4,1,5), (4,2,6), (4,3,7), (5,5,1), (6,6,1), (5,7,2), (6,7,3), (7,4,4), (7,5,5), (7,6,6), (7,7,7)]

theorem w6_len : w6.length = 14 := by native_decide
theorem w7_len : w7.length = 17 := by native_decide
theorem w6_good : good 6 w6 = true := by native_decide
theorem w7_good : good 7 w7 = true := by native_decide
/-- kernel-only check (does not trust the compiler) -/
theorem w6_good_kernel : good 6 w6 = true := by decide +kernel
theorem w7_good_kernel : good 7 w7 = true := by decide +kernel
/-- sanity: false witnesses are rejected -/
theorem bad_rejected : good 3 [(1,1,1),(1,1,2)] = false := by native_decide
theorem bad_range : good 6 [(1,1,7)] = false := by native_decide
