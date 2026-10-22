/-! Green 22: witnesses and exhaustive search, core Lean 4 only (no Mathlib). -/
def w2 : String := "00000011100000000000100110110101101100110101100111110"
def w3 : String := "00000021111112222222222222222222000000000000000000000000000000000000000000000000000000000111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111200222220202202200220202222222220222202220222202220200220222222220222202202202222222200202220222200220222202222202222202200220220222202200220222222202222222220200222222220202222202220220220222202200220202200222222222200220222202220222222202200222220222202222220202202222222222202200222202222220220222200220220202222202222222200222220222220202222202222200220202202220222202202222220202220222220222220200222222222200220222220222222202202220220222202202222222200222222202222200222202220220222202022200220222202202220"
/-- colour of n (1-indexed) from witness string -/
def col (s : String) (n : Nat) : Nat := (s.toList.getD (n-1) '0').toNat - 48

/-- no x,y>=3 with x+y, xy <= N of the same colour -/
def good (N : Nat) (c : Nat → Nat) : Bool :=
  (List.range (N+1)).all fun x => (List.range (N+1)).all fun y =>
    !(3 ≤ x && 3 ≤ y && x*y ≤ N) || c (x+y) != c (x*y)

theorem w2_len : w2.length = 53 := by native_decide
theorem w3_len : w3.length = 773 := by native_decide
theorem w2_good : good 53 (col w2) = true := by native_decide
theorem w3_good : good 773 (col w3) = true := by native_decide
theorem w2_range : w2.toList.all (fun ch => ch == '0' || ch == '1') = true := by native_decide
theorem w3_range : w3.toList.all (fun ch => ch == '0' || ch == '1' || ch == '2') = true := by native_decide

/-- kernel-only (no native_decide) check of the N=53 witness -/
theorem w2_good_kernel : good 53 (col w2) = true := by decide +kernel

/-- Exhaustive backtracking: does an r-colouring of [1,N] without a monochromatic pair exist?
    Assign colours to 1..N in order; when n is assigned check every constraint (x+y,xy) whose
    larger element is n. -/
def conflicts (N : Nat) : Nat → List Nat := fun n =>
  -- earlier elements m<n such that {m,n} is a pair (x+y,xy) with x,y>=3, xy<=N
  ((List.range (N+1)).flatMap fun x => (List.range (N+1)).filterMap fun y =>
    if 3 ≤ x && 3 ≤ y && x*y ≤ N then
      (if x+y == n && x*y < n then some (x*y) else if x*y == n && x+y < n then some (x+y) else none)
    else none)

partial def search (r N : Nat) (cf : Array (List Nat)) (asg : Array Nat) (n : Nat) (used : Nat) : Bool :=
  if n > N then true else
  let forb := (cf[n]!).map (fun m => asg[m-1]!)
  -- symmetry: colours beyond 'used' are interchangeable; try only first unused one
  (List.range (min r (used+1))).any fun k =>
    !(forb.contains k) && search r N cf (asg.push k) (n+1) (max used (k+1))

def exists_col (r N : Nat) : Bool :=
  let cf := (Array.range (N+2)).map (conflicts N)
  search r N cf #[] 1 0

theorem n53_r2 : exists_col 2 53 = true := by native_decide
theorem n54_r2 : exists_col 2 54 = false := by native_decide
theorem n8_r1 : exists_col 1 8 = true := by native_decide
theorem n9_r1 : exists_col 1 9 = false := by native_decide
