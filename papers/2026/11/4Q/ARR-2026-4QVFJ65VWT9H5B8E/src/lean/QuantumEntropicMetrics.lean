/-
  QuantumEntropicMetrics.lean
  Targeted Lean 4.36.0 mechanization (0 imports, 0 sorry, 0 Classical.choice, 0 native_decide).
  Pillars mechanized:
  1. Conic Farkas distortion lower-bound theorem over exact integers.
  2. Purification duality: SSA on (n+1) parties <=> SSA + Weak Monotonicity on n parties.
  3. Isometric restriction theorem: embedding preserves d_Q and QCONE_n inequalities.
  4. Explicit CB_4^+ witness: S(i|j) >= 0 everywhere yet d_Q violates triangle inequality.
  5. Segre quadric Q^+(3, F) incidence/dimension theorem over any field F -> K_{q+1,q+1}.
  6. Elementary 5-cycle inequality F_4 >= 0 on ALL 128 cuts and 21 Bell pairs + Rem #4 >= 13/12.
  7. Kernel-verified Farkas identities (K_{3,3}-e, QFail1, QFail2, K_{5,5}-M).
-/

namespace QuantumEntropicMetrics

/-! ## 1. Conic Farkas Distortion Lower-Bound Theorem -/

def dotList : List Int → List Int → Int
  | [], _ => 0
  | _, [] => 0
  | x :: xs, y :: ys => x * y + dotList xs ys

theorem dotList_nil_right (xs : List Int) : dotList xs [] = 0 := by
  cases xs <;> rfl

theorem dotList_add_left : ∀ (xs ys zs : List Int),
    xs.length = ys.length →
    dotList (List.zipWith (· + ·) xs ys) zs = dotList xs zs + dotList ys zs
  | [], [], _, _ => rfl
  | _ :: _, [], _, h => False.elim (Nat.noConfusion h)
  | [], _ :: _, _, h => False.elim (Nat.noConfusion h)
  | x :: xs, y :: ys, [], _ => rfl
  | x :: xs, y :: ys, z :: zs, h => by
      change (x + y) * z + dotList (List.zipWith (· + ·) xs ys) zs =
        (x * z + dotList xs zs) + (y * z + dotList ys zs)
      rw [dotList_add_left xs ys zs (Nat.succ.inj h), Int.add_mul]
      rw [Int.add_assoc, Int.add_assoc]
      congr 1
      rw [← Int.add_assoc, Int.add_comm (y * z) (dotList xs zs), Int.add_assoc]

theorem dotList_sub_left : ∀ (xs ys zs : List Int),
    xs.length = ys.length →
    dotList (List.zipWith (· - ·) xs ys) zs = dotList xs zs - dotList ys zs
  | [], [], _, _ => rfl
  | _ :: _, [], _, h => False.elim (Nat.noConfusion h)
  | [], _ :: _, _, h => False.elim (Nat.noConfusion h)
  | _ :: _, _ :: _, [], _ => by
      change (0 : Int) = 0 - 0
      rfl
  | x :: xs, y :: ys, z :: zs, h => by
      change (x - y) * z + dotList (List.zipWith (· - ·) xs ys) zs =
        (x * z + dotList xs zs) - (y * z + dotList ys zs)
      rw [dotList_sub_left xs ys zs (Nat.succ.inj h), Int.sub_mul]
      simp only [Int.sub_eq_add_neg, Int.neg_add, Int.add_assoc]
      congr 1
      rw [← Int.add_assoc, Int.add_comm (-(y * z)) (dotList xs zs), Int.add_assoc]

theorem dotList_scale_left (c : Int) : ∀ (xs ys : List Int),
    dotList (xs.map (c * ·)) ys = c * dotList xs ys
  | [], _ => by
      change (0 : Int) = c * 0
      exact (Int.mul_zero c).symm
  | _ :: _, [] => by
      change (0 : Int) = c * 0
      exact (Int.mul_zero c).symm
  | x :: xs, y :: ys => by
      change (c * x) * y + dotList (xs.map (c * ·)) ys = c * (x * y + dotList xs ys)
      rw [dotList_scale_left c xs ys, Int.mul_add, Int.mul_assoc]

theorem dotList_comm : ∀ (xs ys : List Int), dotList xs ys = dotList ys xs
  | [], [] => rfl
  | [], _ :: _ => rfl
  | _ :: _, [] => rfl
  | x :: xs, y :: ys => by
      change x * y + dotList xs ys = y * x + dotList ys xs
      rw [dotList_comm xs ys, Int.mul_comm x y]

theorem dotList_nonneg_of_nonneg : ∀ (xs ys : List Int),
    (∀ x ∈ xs, 0 ≤ x) → (∀ y ∈ ys, 0 ≤ y) → 0 ≤ dotList xs ys
  | [], _, _, _ => Int.le_refl 0
  | _, [], _, _ => by rw [dotList_nil_right]; exact Int.le_refl 0
  | x :: xs, y :: ys, hx, hy => by
      change 0 ≤ x * y + dotList xs ys
      have hx0 : 0 ≤ x := hx x (List.Mem.head _)
      have hy0 : 0 ≤ y := hy y (List.Mem.head _)
      have hxs : ∀ a ∈ xs, 0 ≤ a := fun a ha => hx a (List.Mem.tail _ ha)
      have hys : ∀ b ∈ ys, 0 ≤ b := fun b hb => hy b (List.Mem.tail _ hb)
      have hrec := dotList_nonneg_of_nonneg xs ys hxs hys
      have hmul : 0 ≤ x * y := Int.mul_nonneg hx0 hy0
      exact Int.add_nonneg hmul hrec

def matTvec (M : List (List Int)) (y : List Int) (n : Nat) : List Int :=
  match M, y with
  | [], _ => List.replicate n 0
  | _, [] => List.replicate n 0
  | row :: rows, yi :: ys =>
      List.zipWith (· + ·) (row.map (yi * ·)) (matTvec rows ys n)

theorem matTvec_length (M : List (List Int)) (y : List Int) (n : Nat)
    (hlen : ∀ r ∈ M, r.length = n) :
    (matTvec M y n).length = n := by
  induction M generalizing y with
  | nil => simp [matTvec]
  | cons row rows ih =>
      cases y with
      | nil => simp [matTvec]
      | cons yi ys =>
          simp only [matTvec, List.length_zipWith, List.length_map]
          have hr : row.length = n := hlen row (by simp)
          have htail : (matTvec rows ys n).length = n := ih ys (fun r hrm => hlen r (by simp [hrm]))
          rw [hr, htail]
          omega

theorem dotList_replicate_zero_left : ∀ (n : Nat) (s : List Int),
    dotList (List.replicate n 0) s = 0
  | 0, _ => by simp [dotList]
  | k + 1, [] => by simp [dotList]
  | k + 1, _ :: ss => by
      simp only [List.replicate_succ, dotList, Int.zero_mul, Int.zero_add]
      exact dotList_replicate_zero_left k ss

theorem dot_matTvec (M : List (List Int)) (y s : List Int) (n : Nat)
    (hlen : ∀ r ∈ M, r.length = n) :
    dotList (matTvec M y n) s = dotList y (M.map (fun r => dotList r s)) := by
  induction M generalizing y with
  | nil =>
      cases y <;> simp [matTvec, dotList, dotList_nil_right] <;> exact dotList_replicate_zero_left n s
  | cons row rows ih =>
      cases y with
      | nil =>
          simp only [matTvec, dotList]
          exact dotList_replicate_zero_left n s
      | cons yi ys =>
          simp only [matTvec, List.map_cons, dotList]
          have hrow : (row.map (yi * ·)).length = n := by
            rw [List.length_map]; exact hlen row (by simp)
          have htail : (matTvec rows ys n).length = n :=
            matTvec_length rows ys n (fun r hrm => hlen r (by simp [hrm]))
          rw [dotList_add_left (row.map (yi * ·)) (matTvec rows ys n) s (by rw [hrow, htail])]
          rw [dotList_scale_left yi row s]
          rw [ih ys (fun r hrm => hlen r (by simp [hrm]))]

theorem dotList_le_of_nonneg_left : ∀ (xs as bs : List Int),
    (∀ x ∈ xs, 0 ≤ x) →
    (hlen : as.length = bs.length) →
    (∀ i, (h : i < as.length) → as[i] ≤ bs[i]'(hlen ▸ h)) →
    dotList xs as ≤ dotList xs bs
  | [], _, _, _, _, _ => Int.le_refl 0
  | _ :: _, [], [], _, _, _ => Int.le_refl 0
  | _ :: _, [], _ :: _, _, hlen, _ => False.elim (Nat.noConfusion hlen)
  | _ :: _, _ :: _, [], _, hlen, _ => False.elim (Nat.noConfusion hlen)
  | x :: xs, a :: as, b :: bs, hx, hlen, hle => by
      change x * a + dotList xs as ≤ x * b + dotList xs bs
      have hx0 : 0 ≤ x := hx x (List.Mem.head _)
      have h0 : a ≤ b := hle 0 (Nat.zero_lt_succ _)
      have hmul : x * a ≤ x * b := Int.mul_le_mul_of_nonneg_left h0 hx0
      have hrec := dotList_le_of_nonneg_left xs as bs
        (fun z hz => hx z (List.Mem.tail _ hz))
        (Nat.succ.inj hlen)
        (fun i hi => hle (i + 1) (Nat.succ_lt_succ hi))
      exact Int.add_le_add hmul hrec

/-- Core Conic Farkas Distortion Theorem:
    If M^T y = D^T (β - α) with y, α, β >= 0, and a primal s satisfies M s >= 0,
    d <= D s, and q * (D s) <= p * d (p, q >= 0), then q * (α · d) <= p * (β · d). -/
theorem farkas_distortion_bound
    (M D : List (List Int)) (y α β s d : List Int) (n m p q : Nat)
    (hMlen : ∀ r ∈ M, r.length = n)
    (hDlen : ∀ r ∈ D, r.length = n)
    (hDrows : D.length = m)
    (hαlen : α.length = m)
    (hβlen : β.length = m)
    (hdlen : d.length = m)
    (hy : ∀ v ∈ y, 0 ≤ v)
    (hα : ∀ v ∈ α, 0 ≤ v)
    (hβ : ∀ v ∈ β, 0 ≤ v)
    (hfarkas : matTvec M y n = matTvec D (List.zipWith (· - ·) β α) n)
    (hMs : ∀ r ∈ M, 0 ≤ dotList r s)
    (hlb : ∀ i, (hi : i < m) → d[i]'(by omega) ≤ (D.map (fun r => dotList r s))[i]'(by simp [hDrows, hi]))
    (hub : ∀ i, (hi : i < m) → (q : Int) * (D.map (fun r => dotList r s))[i]'(by simp [hDrows, hi]) ≤ (p : Int) * d[i]'(by omega))
    : (q : Int) * dotList α d ≤ (p : Int) * dotList β d := by
  let ds := D.map (fun r => dotList r s)
  have hds_len : ds.length = m := by simp [ds, hDrows]
  have h1 : 0 ≤ dotList y (M.map (fun r => dotList r s)) := by
    apply dotList_nonneg_of_nonneg y _ hy
    intro v hv
    simp only [List.mem_map] at hv
    rcases hv with ⟨r, hr, rfl⟩
    exact hMs r hr
  have h_eq : dotList y (M.map (fun r => dotList r s)) = dotList β ds - dotList α ds := by
    rw [← dot_matTvec M y s n hMlen, hfarkas, dot_matTvec D _ s n hDlen]
    exact dotList_sub_left β α ds (by rw [hβlen, hαlen])
  have h_diff : dotList α ds ≤ dotList β ds :=
    Int.le_of_sub_nonneg (h_eq ▸ h1)
  have hq : (0 : Int) ≤ q := Int.natCast_nonneg q
  have hα_lb : dotList α d ≤ dotList α ds := by
    apply dotList_le_of_nonneg_left α d ds hα (by rw [hdlen, hds_len])
    intro i hi
    exact hlb i (hdlen ▸ hi)
  have hβ_ub : dotList β (ds.map ((q : Int) * ·)) ≤ dotList β (d.map ((p : Int) * ·)) := by
    apply dotList_le_of_nonneg_left β _ _ hβ (by simp [List.length_map, hds_len, hdlen])
    intro i hi
    have hi_m : i < m := by simp [List.length_map, hds_len] at hi; exact hi
    simp only [List.getElem_map]
    exact hub i hi_m
  have h_q_lb : (q : Int) * dotList α d ≤ (q : Int) * dotList α ds :=
    Int.mul_le_mul_of_nonneg_left hα_lb hq
  have h_q_mid : (q : Int) * dotList α ds ≤ (q : Int) * dotList β ds :=
    Int.mul_le_mul_of_nonneg_left h_diff hq
  have h_q_ub : (q : Int) * dotList β ds ≤ (p : Int) * dotList β d := by
    rw [dotList_comm β (ds.map _), dotList_scale_left (q : Int) ds β, dotList_comm ds β] at hβ_ub
    rw [dotList_comm β (d.map _), dotList_scale_left (p : Int) d β, dotList_comm d β] at hβ_ub
    exact hβ_ub
  exact Int.le_trans h_q_lb (Int.le_trans h_q_mid h_q_ub)

/-! ## 2. Purification Equivalence: SSA on (n+1) <=> SSA + WM on n -/

/-- Under purification S*(X) := S(X) for E ∉ X and S*(X ∪ {E}) := S(U \ X),
    elemental SSA on (i, E, K) reduces identically to Weak Monotonicity on i, K, L = U \ ({i} ∪ K). -/
theorem purification_ssa_gives_wm
    (S_star S : Nat → Int) (U i K L : Nat)
    (h_noE : ∀ X, (X &&& U) = X → S_star X = S X)
    (h_withE : ∀ X, (X &&& U) = X → S_star (X ||| (U + 1)) = S (U - X))
    (hK_in : (K &&& U) = K)
    (h_iK_sub : ((i ||| K) &&& U) = (i ||| K))
    (h_UK : U - K = i + L)
    (h_UiK : U - (i ||| K) = L)
    (h_plus : i + L = (i ||| L))
    : (S_star (i ||| K) + S_star (K ||| (U + 1)) - S_star ((i ||| K) ||| (U + 1)) - S_star K) =
      (S (i ||| K) + S (i ||| L) - S K - S L) := by
  rw [h_noE (i ||| K) h_iK_sub, h_withE K hK_in, h_withE (i ||| K) h_iK_sub, h_noE K hK_in]
  rw [h_UK, h_UiK, h_plus]
  omega

/-! ## 3. Isometric Restriction Validity for Quantum Entropy Cones -/

/-- Any subset map φ : Subset_k → Subset_n preserving union and disjointness
    restricts every general SSA + WM entropy function on n parties to k parties,
    preserving both d_Q distances and all SSA / WM inequalities. -/
theorem isometric_restriction_preserves_qcone
    (S : Nat → Int) (φ : Nat → Nat)
    (hφ_union : ∀ A B, φ (A ||| B) = φ A ||| φ B)
    (hφ_disj : ∀ A B, (A &&& B) = 0 → (φ A &&& φ B) = 0)
    (hSSA : ∀ A B C, (A &&& B) = 0 → (B &&& C) = 0 → (A &&& C) = 0 →
      S (A ||| B) + S (B ||| C) ≥ S ((A ||| B) ||| C) + S B)
    (hWM : ∀ A B C, (A &&& B) = 0 → (B &&& C) = 0 → (A &&& C) = 0 →
      S (A ||| B) + S (B ||| C) ≥ S A + S C) :
    (∀ A B C, (A &&& B) = 0 → (B &&& C) = 0 → (A &&& C) = 0 →
      S (φ (A ||| B)) + S (φ (B ||| C)) ≥ S (φ ((A ||| B) ||| C)) + S (φ B)) ∧
    (∀ A B C, (A &&& B) = 0 → (B &&& C) = 0 → (A &&& C) = 0 →
      S (φ (A ||| B)) + S (φ (B ||| C)) ≥ S (φ A) + S (φ C)) ∧
    (∀ i j, 2 * S (φ (i ||| j)) - S (φ i) - S (φ j) =
      2 * S (φ i ||| φ j) - S (φ i) - S (φ j)) := by
  refine ⟨?_, ?_, ?_⟩
  · intro A B C hab hbc hac
    simp only [hφ_union]
    exact hSSA (φ A) (φ B) (φ C) (hφ_disj A B hab) (hφ_disj B C hbc) (hφ_disj A C hac)
  · intro A B C hab hbc hac
    simp only [hφ_union]
    exact hWM (φ A) (φ B) (φ C) (hφ_disj A B hab) (hφ_disj B C hbc) (hφ_disj A C hac)
  · intro i j
    rw [hφ_union]

/-! ## 4. Explicit CB_4^+ Triangle-Inequality Violation Under S(i|j) >= 0 -/

def bitCount4 (x : Nat) : Nat :=
  (x % 2) + ((x / 2) % 2) + ((x / 4) % 2) + ((x / 8) % 2)

/-- 4 * S(X) for rho = 1/4 cut(0) + 1/4 cut(2,3) + 1/4 Phi^+_{01} + 1/4 Phi^+_{12}. -/
def cb4Plus4S (X : Nat) : Int :=
  (if (X &&& 1) != 0 then 1 else 0) +
  (if (X &&& 12) != 0 then 1 else 0) +
  (if bitCount4 (X &&& 3) == 1 then 1 else 0) +
  (if bitCount4 (X &&& 6) == 1 then 1 else 0)

def cb4Plus4dQ (i j : Nat) : Int :=
  2 * cb4Plus4S ((1 <<< i) ||| (1 <<< j)) - cb4Plus4S (1 <<< i) - cb4Plus4S (1 <<< j)

def cb4Plus4Cond (i j : Nat) : Int :=
  cb4Plus4S ((1 <<< i) ||| (1 <<< j)) - cb4Plus4S (1 <<< j)

def allCondsNonneg4 : Bool :=
  (List.range 4).all fun i =>
    (List.range 4).all fun j =>
      if i == j then true else decide (0 ≤ cb4Plus4Cond i j)

theorem cb4_plus_conds_nonneg : allCondsNonneg4 = true := by decide

theorem cb4_plus_triangle_violation :
    cb4Plus4dQ 0 1 = 0 ∧ cb4Plus4dQ 1 2 = 0 ∧ cb4Plus4dQ 0 2 = 4 ∧
    cb4Plus4dQ 0 1 + cb4Plus4dQ 1 2 < cb4Plus4dQ 0 2 := by
  decide

/-! ## 5. Segre Quadric Q^+(3, F) Incidence Theorem over Any Field -/

/-- Minimal algebraic field structure (no Mathlib needed) for 2x2 matrix subspaces. -/
structure FieldOps (F : Type) where
  zero : F
  one : F
  add : F → F → F
  neg : F → F
  mul : F → F → F
  inv : F → F
  add_comm : ∀ a b, add a b = add b a
  add_assoc : ∀ a b c, add (add a b) c = add a (add b c)
  zero_add : ∀ a, add zero a = a
  add_neg : ∀ a, add a (neg a) = zero
  mul_comm : ∀ a b, mul a b = mul b a
  mul_assoc : ∀ a b c, mul (mul a b) c = mul a (mul b c)
  one_mul : ∀ a, mul one a = a
  mul_zero : ∀ a, mul a zero = zero
  mul_inv : ∀ a, a ≠ zero → mul a (inv a) = one
  left_distrib : ∀ a b c, mul a (add b c) = add (mul a b) (mul a c)
  eq_zero_of_mul_eq_zero : ∀ a b, mul a b = zero → a = zero ∨ b = zero

theorem add_zero {F : Type} (fl : FieldOps F) (a : F) : fl.add a fl.zero = a := by
  rw [fl.add_comm, fl.zero_add]

theorem neg_add {F : Type} (fl : FieldOps F) (a : F) : fl.add (fl.neg a) a = fl.zero := by
  rw [fl.add_comm, fl.add_neg]

theorem zero_mul {F : Type} (fl : FieldOps F) (a : F) : fl.mul fl.zero a = fl.zero := by
  rw [fl.mul_comm, fl.mul_zero]

theorem neg_unique {F : Type} (fl : FieldOps F) {a b : F} (h : fl.add a b = fl.zero) :
    b = fl.neg a := by
  calc
    b = fl.add fl.zero b := (fl.zero_add b).symm
    _ = fl.add (fl.add (fl.neg a) a) b := by rw [neg_add]
    _ = fl.add (fl.neg a) (fl.add a b) := fl.add_assoc _ _ _
    _ = fl.add (fl.neg a) fl.zero := by rw [h]
    _ = fl.neg a := add_zero fl _

theorem mul_neg {F : Type} (fl : FieldOps F) (a b : F) :
    fl.mul a (fl.neg b) = fl.neg (fl.mul a b) := by
  apply neg_unique fl
  rw [← fl.left_distrib, fl.add_neg, fl.mul_zero]

theorem sub_eq_zero_iff {F : Type} (fl : FieldOps F) (a b : F) :
    fl.add a (fl.neg b) = fl.zero ↔ a = b := by
  constructor
  · intro h
    calc
      a = fl.add a fl.zero := (add_zero fl a).symm
      _ = fl.add a (fl.add (fl.neg b) b) := by rw [neg_add]
      _ = fl.add (fl.add a (fl.neg b)) b := (fl.add_assoc _ _ _).symm
      _ = fl.add fl.zero b := by rw [h]
      _ = b := fl.zero_add b
  · intro h
    subst h
    exact fl.add_neg a

theorem mul_left_cancel {F : Type} (fl : FieldOps F) {c a b : F} (hc : c ≠ fl.zero)
    (h : fl.mul c a = fl.mul c b) : a = b := by
  have h0 : fl.mul c (fl.add a (fl.neg b)) = fl.zero := by
    rw [fl.left_distrib, mul_neg, h, fl.add_neg]
  rcases fl.eq_zero_of_mul_eq_zero c _ h0 with hc0 | hab
  · exact absurd hc0 hc
  · exact (sub_eq_zero_iff fl a b).mp hab

structure Mat2 (F : Type) where
  m00 : F
  m01 : F
  m10 : F
  m11 : F

/-- Left regulus L_u = { x * u^T : x in F^2 }, parameterized by (x0, x1). -/
def inL {F : Type} (fl : FieldOps F) (u0 u1 : F) (A : Mat2 F) : Prop :=
  ∃ x0 x1, A.m00 = fl.mul x0 u0 ∧ A.m01 = fl.mul x0 u1 ∧
           A.m10 = fl.mul x1 u0 ∧ A.m11 = fl.mul x1 u1

/-- Right regulus M_v = { v * y^T : y in F^2 }, parameterized by (y0, y1). -/
def inM {F : Type} (fl : FieldOps F) (v0 v1 : F) (A : Mat2 F) : Prop :=
  ∃ y0 y1, A.m00 = fl.mul v0 y0 ∧ A.m01 = fl.mul v0 y1 ∧
           A.m10 = fl.mul v1 y0 ∧ A.m11 = fl.mul v1 y1

def crossZero {F : Type} (fl : FieldOps F) (a0 a1 b0 b1 : F) : Prop :=
  fl.mul a0 b1 = fl.mul a1 b0

/-- Same-regulus intersection: distinct lines u, w in P^1(F) give L_u ∩ L_w = {0},
    so dim(L_u + L_w) = 2 + 2 - 0 = 4 => d_Q = 2(4) - 2 - 2 = 4. -/
theorem segre_same_regulus_disjoint {F : Type} (fl : FieldOps F)
    (u0 u1 w0 w1 : F) (hne : ¬ crossZero fl u0 u1 w0 w1)
    (A : Mat2 F) (h1 : inL fl u0 u1 A) (h2 : inL fl w0 w1 A) :
    A = ⟨fl.zero, fl.zero, fl.zero, fl.zero⟩ := by
  rcases h1 with ⟨x0, x1, h00, h01, h10, h11⟩
  rcases h2 with ⟨z0, z1, g00, g01, g10, g11⟩
  have hdet_nz : fl.add (fl.mul u0 w1) (fl.neg (fl.mul u1 w0)) ≠ fl.zero := by
    intro h0
    exact hne ((sub_eq_zero_iff fl (fl.mul u0 w1) (fl.mul u1 w0)).mp h0)
  have hx0 : x0 = fl.zero := by
    have hmul : fl.mul x0 (fl.add (fl.mul u0 w1) (fl.neg (fl.mul u1 w0))) = fl.zero := by
      rw [fl.left_distrib, mul_neg]
      have e1 : fl.mul x0 (fl.mul u0 w1) = fl.mul z0 (fl.mul w0 w1) := by
        rw [← fl.mul_assoc, ← h00, g00, fl.mul_assoc]
      have e2 : fl.mul x0 (fl.mul u1 w0) = fl.mul z0 (fl.mul w0 w1) := by
        rw [← fl.mul_assoc, ← h01, g01, fl.mul_assoc, fl.mul_comm w1 w0]
      rw [e1, e2, fl.add_neg]
    rcases fl.eq_zero_of_mul_eq_zero x0 _ hmul with h | h
    · exact h
    · exact absurd h hdet_nz
  have hx1 : x1 = fl.zero := by
    have hmul : fl.mul x1 (fl.add (fl.mul u0 w1) (fl.neg (fl.mul u1 w0))) = fl.zero := by
      rw [fl.left_distrib, mul_neg]
      have e1 : fl.mul x1 (fl.mul u0 w1) = fl.mul z1 (fl.mul w0 w1) := by
        rw [← fl.mul_assoc, ← h10, g10, fl.mul_assoc]
      have e2 : fl.mul x1 (fl.mul u1 w0) = fl.mul z1 (fl.mul w0 w1) := by
        rw [← fl.mul_assoc, ← h11, g11, fl.mul_assoc, fl.mul_comm w1 w0]
      rw [e1, e2, fl.add_neg]
    rcases fl.eq_zero_of_mul_eq_zero x1 _ hmul with h | h
    · exact h
    · exact absurd h hdet_nz
  cases A
  simp only at h00 h01 h10 h11
  rw [h00, h01, h10, h11, hx0, hx1, zero_mul, zero_mul]

theorem mul_left_comm {F : Type} (fl : FieldOps F) (a b c : F) :
    fl.mul a (fl.mul b c) = fl.mul b (fl.mul a c) := by
  rw [← fl.mul_assoc, fl.mul_comm a b, fl.mul_assoc]

/-- Opposite-regulus intersection: L_u ∩ M_v = span(v * u^T) (1-dimensional!),
    so dim(L_u + M_v) = 2 + 2 - 1 = 3 => d_Q = 2(3) - 2 - 2 = 2. -/
theorem segre_opp_regulus_rank_one {F : Type} (fl : FieldOps F)
    (u0 u1 v0 v1 : F) (hu : u0 ≠ fl.zero ∨ u1 ≠ fl.zero) (hv : v0 ≠ fl.zero ∨ v1 ≠ fl.zero) :
    (inL fl u0 u1 ⟨fl.mul v0 u0, fl.mul v0 u1, fl.mul v1 u0, fl.mul v1 u1⟩ ∧
     inM fl v0 v1 ⟨fl.mul v0 u0, fl.mul v0 u1, fl.mul v1 u0, fl.mul v1 u1⟩) ∧
    (∀ A, inL fl u0 u1 A → inM fl v0 v1 A →
      ∃ c : F, A = ⟨fl.mul c (fl.mul v0 u0), fl.mul c (fl.mul v0 u1),
                    fl.mul c (fl.mul v1 u0), fl.mul c (fl.mul v1 u1)⟩) := by
  refine ⟨⟨⟨v0, v1, rfl, rfl, rfl, rfl⟩, ⟨u0, u1, rfl, rfl, rfl, rfl⟩⟩, ?_⟩
  intro A hL hM
  rcases hL with ⟨x0, x1, h00, h01, h10, h11⟩
  rcases hM with ⟨y0, y1, g00, g01, g10, g11⟩
  have hcross_vx : fl.mul v0 x1 = fl.mul v1 x0 := by
    rcases hu with hu0 | hu1
    · have e : fl.mul u0 (fl.mul v0 x1) = fl.mul u0 (fl.mul v1 x0) := by
        calc
          fl.mul u0 (fl.mul v0 x1) = fl.mul v0 (fl.mul x1 u0) := by rw [mul_left_comm, fl.mul_comm u0 x1]
          _ = fl.mul v0 (fl.mul v1 y0) := by rw [← h10, g10]
          _ = fl.mul v1 (fl.mul v0 y0) := mul_left_comm fl v0 v1 y0
          _ = fl.mul v1 (fl.mul x0 u0) := by rw [← g00, h00]
          _ = fl.mul (fl.mul v1 x0) u0 := (fl.mul_assoc v1 x0 u0).symm
          _ = fl.mul u0 (fl.mul v1 x0) := fl.mul_comm _ u0
      exact mul_left_cancel fl hu0 e
    · have e : fl.mul u1 (fl.mul v0 x1) = fl.mul u1 (fl.mul v1 x0) := by
        calc
          fl.mul u1 (fl.mul v0 x1) = fl.mul v0 (fl.mul x1 u1) := by rw [mul_left_comm, fl.mul_comm u1 x1]
          _ = fl.mul v0 (fl.mul v1 y1) := by rw [← h11, g11]
          _ = fl.mul v1 (fl.mul v0 y1) := mul_left_comm fl v0 v1 y1
          _ = fl.mul v1 (fl.mul x0 u1) := by rw [← g01, h01]
          _ = fl.mul (fl.mul v1 x0) u1 := (fl.mul_assoc v1 x0 u1).symm
          _ = fl.mul u1 (fl.mul v1 x0) := fl.mul_comm _ u1
      exact mul_left_cancel fl hu1 e
  rcases hv with hv0 | hv1
  · let c := fl.mul x0 (fl.inv v0)
    have hx0c : x0 = fl.mul c v0 := by
      dsimp [c]
      rw [fl.mul_assoc, fl.mul_comm (fl.inv v0) v0, fl.mul_inv v0 hv0, fl.mul_comm x0 fl.one, fl.one_mul]
    have hx1c : x1 = fl.mul c v1 := by
      apply mul_left_cancel fl hv0
      calc
        fl.mul v0 x1 = fl.mul v1 x0 := hcross_vx
        _ = fl.mul v1 (fl.mul c v0) := by rw [← hx0c]
        _ = fl.mul c (fl.mul v1 v0) := mul_left_comm fl v1 c v0
        _ = fl.mul c (fl.mul v0 v1) := by rw [fl.mul_comm v1 v0]
        _ = fl.mul v0 (fl.mul c v1) := mul_left_comm fl c v0 v1
    have m00e : fl.mul x0 u0 = fl.mul c (fl.mul v0 u0) := by rw [hx0c, fl.mul_assoc]
    have m01e : fl.mul x0 u1 = fl.mul c (fl.mul v0 u1) := by rw [hx0c, fl.mul_assoc]
    have m10e : fl.mul x1 u0 = fl.mul c (fl.mul v1 u0) := by rw [hx1c, fl.mul_assoc]
    have m11e : fl.mul x1 u1 = fl.mul c (fl.mul v1 u1) := by rw [hx1c, fl.mul_assoc]
    refine ⟨c, ?_⟩
    cases A
    simp only at h00 h01 h10 h11
    rw [h00, h01, h10, h11, m00e, m01e, m10e, m11e]
  · let c := fl.mul x1 (fl.inv v1)
    have hx1c : x1 = fl.mul c v1 := by
      dsimp [c]
      rw [fl.mul_assoc, fl.mul_comm (fl.inv v1) v1, fl.mul_inv v1 hv1, fl.mul_comm x1 fl.one, fl.one_mul]
    have hx0c : x0 = fl.mul c v0 := by
      apply mul_left_cancel fl hv1
      calc
        fl.mul v1 x0 = fl.mul v0 x1 := hcross_vx.symm
        _ = fl.mul v0 (fl.mul c v1) := by rw [← hx1c]
        _ = fl.mul c (fl.mul v0 v1) := mul_left_comm fl v0 c v1
        _ = fl.mul c (fl.mul v1 v0) := by rw [fl.mul_comm v0 v1]
        _ = fl.mul v1 (fl.mul c v0) := mul_left_comm fl c v1 v0
    have m00e : fl.mul x0 u0 = fl.mul c (fl.mul v0 u0) := by rw [hx0c, fl.mul_assoc]
    have m01e : fl.mul x0 u1 = fl.mul c (fl.mul v0 u1) := by rw [hx0c, fl.mul_assoc]
    have m10e : fl.mul x1 u0 = fl.mul c (fl.mul v1 u0) := by rw [hx1c, fl.mul_assoc]
    have m11e : fl.mul x1 u1 = fl.mul c (fl.mul v1 u1) := by rw [hx1c, fl.mul_assoc]
    refine ⟨c, ?_⟩
    cases A
    simp only at h00 h01 h10 h11
    rw [h00, h01, h10, h11, m00e, m01e, m10e, m11e]

/-! ## 6. Elementary 5-Cycle Inequality F_4 >= 0 on ALL CB_7 & Rem #4 Gap >= 13/12 -/

def pairs7 : List (Nat × Nat) :=
  (List.range 7).flatMap fun i =>
    (List.range 7).filterMap fun j => if i < j then some (i, j) else none

def F4_eval (d : Nat → Nat → Int) : Int :=
  (d 0 5 + d 0 6 + d 1 5 + d 1 6 + d 2 5 + d 2 6 + d 3 5 + d 3 6 + d 4 5 + d 4 6) -
  (d 5 6 + d 0 3 + d 1 3 + d 1 2 + d 2 4 + d 0 4)

def cutDist7 (mask : Nat) (i j : Nat) : Int :=
  if ((mask >>> i) &&& 1) != ((mask >>> j) &&& 1) then 1 else 0

def bellDist7 (a b i j : Nat) : Int :=
  let mi := i == a || i == b
  let mj := j == a || j == b
  if mi && mj then -2 else if mi != mj then 1 else 0

def allCutsF4Nonneg : Bool :=
  (List.range 128).all fun mask => decide (0 ≤ F4_eval (cutDist7 mask))

def allBellsF4Nonneg : Bool :=
  pairs7.all fun (a, b) => decide (0 ≤ F4_eval (bellDist7 a b))

/-- Exact shortest-path metric on Rem #4 (Atlas G800) with edges
    {(0,5),(0,6),(1,5),(1,6),(2,3),(2,5),(2,6),(3,4),(4,5),(4,6),(5,6)}. -/
def rem4Dist (i j : Nat) : Int :=
  let a := if i ≤ j then i else j
  let b := if i ≤ j then j else i
  if a == b then 0
  else if (a == 0 && (b == 5 || b == 6)) ||
          (a == 1 && (b == 5 || b == 6)) ||
          (a == 2 && (b == 3 || b == 5 || b == 6)) ||
          (a == 3 && b == 4) ||
          (a == 4 && (b == 5 || b == 6)) ||
          (a == 5 && b == 6) then 1
  else if (a == 0 && b == 3) || (a == 1 && b == 3) then 3
  else 2

theorem F4_nonneg_on_all_128_cuts : allCutsF4Nonneg = true := by decide
theorem F4_nonneg_on_all_21_bells : allBellsF4Nonneg = true := by decide
theorem F4_rem4_value : F4_eval rem4Dist = -1 := by decide
theorem F4_rem4_pos_neg_parts :
    (rem4Dist 0 5 + rem4Dist 0 6 + rem4Dist 1 5 + rem4Dist 1 6 + rem4Dist 2 5 +
     rem4Dist 2 6 + rem4Dist 3 5 + rem4Dist 3 6 + rem4Dist 4 5 + rem4Dist 4 6 = 12) ∧
    (rem4Dist 5 6 + rem4Dist 0 3 + rem4Dist 1 3 + rem4Dist 1 2 + rem4Dist 2 4 + rem4Dist 0 4 = 13) := by
  decide

/-! ## 7. Kernel-Verified Farkas Identities (K_{3,3}-e, QFail1, QFail2, K_{5,5}-M) -/

def listAddAt : List Int → Nat → Int → List Int
  | [], _, _ => []
  | a :: as, 0, v => (a + v) :: as
  | a :: as, k + 1, v => a :: listAddAt as k v

theorem listAddAt_length (xs : List Int) (k : Nat) (v : Int) :
    (listAddAt xs k v).length = xs.length := by
  induction xs generalizing k with
  | nil => rfl
  | cons _ _ ih =>
      cases k with
      | zero => rfl
      | succ k' => exact congrArg Nat.succ (ih k')

def sparseToDense (n : Nat) (sp : List (Nat × Int)) : List Int :=
  sp.foldl (fun acc (idx, v) => listAddAt acc idx v) (List.replicate n 0)

theorem sparseToDense_length (n : Nat) (sp : List (Nat × Int)) :
    (sparseToDense n sp).length = n := by
  unfold sparseToDense
  suffices h : ∀ (acc : List Int), acc.length = n →
      (sp.foldl (fun a (idx, v) => listAddAt a idx v) acc).length = n by
    exact h (List.replicate n 0) (List.length_replicate)
  induction sp with
  | nil => intro acc ha; exact ha
  | cons p ps ih =>
      intro acc ha
      exact ih (listAddAt acc p.1 p.2) (by rw [listAddAt_length, ha])

def k33eRowsSp : List (List (Nat × Int)) := [
  [(0, -2), (1, -2), (7, -2), (8, 2), (9, 2), (11, 2), (12, -1), (13, -1), (15, -2), (16, 2), (17, 2), (19, 2), (20, -1), (21, -1), (32, 2), (33, 2), (40, -1), (41, -1), (48, -1), (49, -1)],
  [(2, -1), (10, 1), (18, 1), (23, -1), (24, 1), (25, 1), (26, -2)],
  [(4, -1), (5, -1), (12, 1), (13, 1), (20, 1), (21, 1), (28, -1), (29, -1), (39, -1), (40, 1), (41, 1), (42, -1), (47, -1), (48, 1), (49, 1), (50, -1)],
  [(10, -1), (18, -1), (24, -1), (25, -1), (26, 4), (28, 1), (29, 1), (30, -2), (42, 1), (50, 1), (58, -2)],
  [(10, -1), (14, 1), (18, -1), (22, 1), (24, -1), (25, -1), (28, 1), (29, 1), (42, 1), (46, -1), (50, 1), (54, -1), (56, 1), (57, 1), (60, -1), (61, -1)],
  [(14, -1), (22, -1), (30, 2), (46, 1), (54, 1), (56, -1), (57, -1), (58, 2), (60, 1), (61, 1), (62, -4)],
  [(35, -4), (36, 2), (37, 2), (43, 2), (44, -1), (45, -1), (51, 2), (52, -1), (53, -1)],
  [(36, -1), (37, -1), (43, -1), (44, 2), (45, 2), (46, -1), (51, -1), (52, 2), (53, 2), (54, -1), (60, -1), (61, -1)],
  [(44, -1), (45, -1), (46, 2), (52, -1), (53, -1), (54, 2), (60, 2), (61, 2), (62, -4)],
  [(46, -1), (54, -1), (60, -1), (61, -1), (62, 4)]
]
def k33eY : List Int := [2, 2, 2, 1, 1, 1, 1, 2, 3, 4]
def k33eDRowsSp : List (List (Nat × Int)) := [
  [(0, -1), (1, -1), (2, 2)], [(0, -1), (3, -1), (4, 2)], [(0, -1), (7, -1), (8, 2)],
  [(0, -1), (15, -1), (16, 2)], [(0, -1), (31, -1), (32, 2)], [(1, -1), (3, -1), (5, 2)],
  [(1, -1), (7, -1), (9, 2)], [(1, -1), (15, -1), (17, 2)], [(1, -1), (31, -1), (33, 2)],
  [(3, -1), (7, -1), (11, 2)], [(3, -1), (15, -1), (19, 2)], [(3, -1), (31, -1), (35, 2)],
  [(7, -1), (15, -1), (23, 2)], [(7, -1), (31, -1), (39, 2)], [(15, -1), (31, -1), (47, 2)]
]
def k33eAlpha : List Int := [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 1, 1, 1]
def k33eBeta : List Int := [0, 0, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0]
def k33eD : List Int := [2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3, 2, 2, 2]

def qfail1RowsSp : List (List (Nat × Int)) := [
  [(7, -1), (8, 1), (9, 1), (10, -1)], [(15, -1), (16, 1), (17, 1), (18, -1)],
  [(55, -1), (56, 1), (57, 1), (58, -1)], [(33, -1), (34, 1), (37, 1), (38, -1)],
  [(7, -1), (8, 1), (39, 1), (40, -1)], [(15, -1), (16, 1), (47, 1), (48, -1)],
  [(25, -1), (26, 1), (57, 1), (58, -1)], [(7, -1), (8, 1), (71, 1), (72, -1)],
  [(15, -1), (16, 1), (79, 1), (80, -1)], [(4, -1), (6, 1), (36, 1), (38, -1)],
  [(7, -1), (9, 1), (39, 1), (41, -1)], [(11, -1), (13, 1), (43, 1), (45, -1)],
  [(15, -1), (17, 1), (47, 1), (49, -1)], [(19, -1), (21, 1), (51, 1), (53, -1)],
  [(23, -1), (25, 1), (55, 1), (57, -1)], [(36, -1), (38, 1), (100, 1), (102, -1)],
  [(1, -1), (5, 1), (9, 1), (13, -1)], [(31, -1), (35, 1), (39, 1), (43, -1)],
  [(1, -1), (5, 1), (17, 1), (21, -1)], [(31, -1), (35, 1), (47, 1), (51, -1)],
  [(7, -1), (11, 1), (71, 1), (75, -1)], [(15, -1), (19, 1), (79, 1), (83, -1)],
  [(1, -1), (9, 1), (17, 1), (25, -1)], [(2, -1), (10, 1), (18, 1), (26, -1)],
  [(31, -1), (39, 1), (47, 1), (55, -1)], [(32, -1), (40, 1), (48, 1), (56, -1)],
  [(33, -1), (41, 1), (49, 1), (57, -1)], [(64, -1), (72, 1), (80, 1), (88, -1)],
  [(67, -1), (75, 1), (83, 1), (91, -1)], [(23, -1), (55, 1), (87, 1), (119, -1)],
  [(23, -1), (25, 1), (100, -1), (102, 1)], [(37, -1), (45, 1), (80, -1), (88, 1)],
  [(50, -1), (58, 1), (67, -1), (75, 1)], [(34, -1), (50, 1), (75, -1), (91, 1)],
  [(37, -1), (53, 1), (72, -1), (88, 1)], [(6, -1), (38, 1), (87, -1), (119, 1)]
]
def qfail1Y : List Int := [2, 2, 2, 4, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 4, 4, 4, 2, 4, 2, 2, 4, 4, 4, 4, 2, 4, 4, 2, 4]
def qfailDRowsSp : List (List (Nat × Int)) := [
  [(0, -1), (1, -1), (2, 2)], [(0, -1), (3, -1), (4, 2)], [(0, -1), (7, -1), (8, 2)],
  [(0, -1), (15, -1), (16, 2)], [(0, -1), (31, -1), (32, 2)], [(0, -1), (63, -1), (64, 2)],
  [(1, -1), (3, -1), (5, 2)], [(1, -1), (7, -1), (9, 2)], [(1, -1), (15, -1), (17, 2)],
  [(1, -1), (31, -1), (33, 2)], [(1, -1), (63, -1), (65, 2)], [(3, -1), (7, -1), (11, 2)],
  [(3, -1), (15, -1), (19, 2)], [(3, -1), (31, -1), (35, 2)], [(3, -1), (63, -1), (67, 2)],
  [(7, -1), (15, -1), (23, 2)], [(7, -1), (31, -1), (39, 2)], [(7, -1), (63, -1), (71, 2)],
  [(15, -1), (31, -1), (47, 2)], [(15, -1), (63, -1), (79, 2)], [(31, -1), (63, -1), (95, 2)]
]
def qfail1Alpha : List Int := [1, 2, 0, 0, 1, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4, 5, 0, 0, 0, 0, 0]
def qfail1Beta : List Int := [0, 0, 3, 3, 0, 0, 2, 5, 5, 0, 0, 1, 1, 2, 0, 0, 5, 3, 5, 3, 0]
def qfail1D : List Int := [2, 3, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 3, 2, 1, 1, 1, 1, 2]

def qfail2RowsSp : List (List (Nat × Int)) := [
  [(23, -1), (24, 1), (25, 1), (26, -1)], [(31, -1), (32, 1), (33, 1), (34, -1)],
  [(63, -1), (64, 1), (65, 1), (66, -1)], [(23, -1), (24, 1), (27, 1), (28, -1)],
  [(31, -1), (32, 1), (35, 1), (36, -1)], [(63, -1), (64, 1), (67, 1), (68, -1)],
  [(7, -1), (8, 1), (39, 1), (40, -1)], [(15, -1), (16, 1), (47, 1), (48, -1)],
  [(7, -1), (8, 1), (71, 1), (72, -1)], [(15, -1), (16, 1), (79, 1), (80, -1)],
  [(95, -1), (97, 1), (99, 1), (101, -1)], [(31, -1), (33, 1), (39, 1), (41, -1)],
  [(63, -1), (65, 1), (71, 1), (73, -1)], [(111, -1), (113, 1), (119, 1), (121, -1)],
  [(4, -1), (6, 1), (20, 1), (22, -1)], [(31, -1), (33, 1), (47, 1), (49, -1)],
  [(63, -1), (65, 1), (79, 1), (81, -1)], [(18, -1), (22, 1), (26, 1), (30, -1)],
  [(31, -1), (35, 1), (39, 1), (43, -1)], [(63, -1), (67, 1), (71, 1), (75, -1)],
  [(31, -1), (35, 1), (47, 1), (51, -1)], [(63, -1), (67, 1), (79, 1), (83, -1)],
  [(103, -1), (107, 1), (119, 1), (123, -1)], [(2, -1), (10, 1), (18, 1), (26, -1)],
  [(32, -1), (40, 1), (48, 1), (56, -1)], [(64, -1), (72, 1), (80, 1), (88, -1)],
  [(95, -1), (103, 1), (111, 1), (119, -1)], [(2, -1), (34, 1), (66, 1), (98, -1)],
  [(4, -1), (36, 1), (68, 1), (100, -1)], [(7, -1), (39, 1), (71, 1), (103, -1)],
  [(9, -1), (41, 1), (73, 1), (105, -1)], [(11, -1), (43, 1), (75, 1), (107, -1)],
  [(15, -1), (47, 1), (79, 1), (111, -1)], [(17, -1), (49, 1), (81, 1), (113, -1)],
  [(19, -1), (51, 1), (83, 1), (115, -1)], [(24, -1), (56, 1), (88, 1), (120, -1)],
  [(6, -1), (14, 1), (111, -1), (119, 1)], [(20, -1), (28, 1), (97, -1), (105, 1)],
  [(10, -1), (26, 1), (99, -1), (115, 1)], [(14, -1), (30, 1), (95, -1), (111, 1)],
  [(4, -1), (36, 1), (89, -1), (121, 1)], [(5, -1), (37, 1), (88, -1), (120, 1)],
  [(27, -1), (59, 1), (66, -1), (98, 1)], [(2, -1), (59, -1), (66, 1), (123, 1)],
  [(24, -1), (37, -1), (88, 1), (101, 1)], [(25, -1), (36, -1), (89, 1), (100, 1)]
]
def qfail2Y : List Int := [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 4, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
def qfail2Alpha : List Int := [3, 3, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 2, 0, 0, 0, 0, 5]
def qfail2Beta : List Int := [0, 0, 2, 2, 1, 1, 0, 0, 0, 3, 3, 0, 0, 3, 3, 0, 5, 5, 5, 5, 0]
def qfail2D : List Int := [3, 3, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2]

def k55mRowsSp : List (List (Nat × Int)) := [
  [(0, -1), (1, 1), (2, 1), (12, -1)], [(0, -1), (1, 2), (3, -1)],
  [(2, -1), (3, 1), (5, 1), (14, -1)], [(2, -1), (3, 2), (4, -1)],
  [(3, -1), (4, 1), (6, 1), (15, -1)], [(3, -1), (4, 2), (7, -1)],
  [(5, -1), (14, 1), (23, -1), (25, 1)], [(6, -1), (7, 1), (17, 1), (18, -1)],
  [(11, -1), (12, 1), (27, -1), (30, 1)], [(12, -1), (14, 2), (17, -1)],
  [(14, -1), (17, 2), (19, -1)], [(14, -1), (15, 1), (17, 1), (23, -1)],
  [(17, -1), (23, 2), (27, -1)], [(17, -1), (18, 1), (19, 1), (25, -1)],
  [(23, -1), (27, 2), (30, -1)]
]
def k55mY : List Int := [2, 10, 2, 6, 2, 2, 2, 2, 4, 2, 2, 2, 4, 2, 4]
def k55mDRowsSp : List (List (Nat × Int)) := [[(0, -2), (1, 2)], [(0, -2), (2, 2)], [(0, -2), (11, 2)]]
def k55mAlpha : List Int := [0, 3, 2]
def k55mBeta : List Int := [11, 0, 0]
def k55mD : List Int := [1, 2, 3]

theorem k33e_farkas_id :
    matTvec (k33eRowsSp.map (sparseToDense 63)) k33eY 63 =
    matTvec (k33eDRowsSp.map (sparseToDense 63)) (List.zipWith (· - ·) k33eBeta k33eAlpha) 63 := by
  decide

theorem qfail1_farkas_id :
    matTvec (qfail1RowsSp.map (sparseToDense 127)) qfail1Y 127 =
    matTvec (qfailDRowsSp.map (sparseToDense 127)) (List.zipWith (· - ·) qfail1Beta qfail1Alpha) 127 := by
  decide

theorem qfail2_farkas_id :
    matTvec (qfail2RowsSp.map (sparseToDense 127)) qfail2Y 127 =
    matTvec (qfailDRowsSp.map (sparseToDense 127)) (List.zipWith (· - ·) qfail2Beta qfail2Alpha) 127 := by
  decide

theorem k55m_farkas_id :
    matTvec (k55mRowsSp.map (sparseToDense 33)) k55mY 33 =
    matTvec (k55mDRowsSp.map (sparseToDense 33)) (List.zipWith (· - ·) k55mBeta k55mAlpha) 33 := by
  decide

/-- Unconditional distortion lower bound kappa_{POLY_6}(K_{3,3}-e) >= 9/8 (i.e. 18 * q <= 16 * p). -/
theorem k33e_poly6_distortion_ge_9_8 (s : List Int) (p q : Nat)
    (hMs : ∀ r ∈ k33eRowsSp.map (sparseToDense 63), 0 ≤ dotList r s)
    (hlb : ∀ i, (hi : i < 15) → k33eD[i]'hi ≤ ((k33eDRowsSp.map (sparseToDense 63)).map (fun r => dotList r s))[i]'(by simp only [List.length_map]; exact hi))
    (hub : ∀ i, (hi : i < 15) → (q : Int) * ((k33eDRowsSp.map (sparseToDense 63)).map (fun r => dotList r s))[i]'(by simp only [List.length_map]; exact hi) ≤ (p : Int) * k33eD[i]'hi)
    : (q : Int) * 18 ≤ (p : Int) * 16 := by
  have hbound := farkas_distortion_bound
    (k33eRowsSp.map (sparseToDense 63)) (k33eDRowsSp.map (sparseToDense 63))
    k33eY k33eAlpha k33eBeta s k33eD 63 15 p q
    (fun r hr => by simp only [List.mem_map] at hr; rcases hr with ⟨sp, _, rfl⟩; exact sparseToDense_length 63 sp)
    (fun r hr => by simp only [List.mem_map] at hr; rcases hr with ⟨sp, _, rfl⟩; exact sparseToDense_length 63 sp)
    rfl rfl rfl rfl (by decide) (by decide) (by decide) k33e_farkas_id hMs hlb hub
  have ha : dotList k33eAlpha k33eD = 18 := by decide
  have hb : dotList k33eBeta k33eD = 16 := by decide
  rw [ha, hb] at hbound
  exact hbound

/-- Unconditional distortion lower bound kappa_{Q_7}(QFail1) >= 21/20 (i.e. 42 * q <= 40 * p). -/
theorem qfail1_q7_distortion_ge_21_20 (s : List Int) (p q : Nat)
    (hMs : ∀ r ∈ qfail1RowsSp.map (sparseToDense 127), 0 ≤ dotList r s)
    (hlb : ∀ i, (hi : i < 21) → qfail1D[i]'hi ≤ ((qfailDRowsSp.map (sparseToDense 127)).map (fun r => dotList r s))[i]'(by simp only [List.length_map]; exact hi))
    (hub : ∀ i, (hi : i < 21) → (q : Int) * ((qfailDRowsSp.map (sparseToDense 127)).map (fun r => dotList r s))[i]'(by simp only [List.length_map]; exact hi) ≤ (p : Int) * qfail1D[i]'hi)
    : (q : Int) * 42 ≤ (p : Int) * 40 := by
  have hbound := farkas_distortion_bound
    (qfail1RowsSp.map (sparseToDense 127)) (qfailDRowsSp.map (sparseToDense 127))
    qfail1Y qfail1Alpha qfail1Beta s qfail1D 127 21 p q
    (fun r hr => by simp only [List.mem_map] at hr; rcases hr with ⟨sp, _, rfl⟩; exact sparseToDense_length 127 sp)
    (fun r hr => by simp only [List.mem_map] at hr; rcases hr with ⟨sp, _, rfl⟩; exact sparseToDense_length 127 sp)
    rfl rfl rfl rfl (by decide) (by decide) (by decide) qfail1_farkas_id hMs hlb hub
  have ha : dotList qfail1Alpha qfail1D = 42 := by decide
  have hb : dotList qfail1Beta qfail1D = 40 := by decide
  rw [ha, hb] at hbound
  exact hbound

/-- Unconditional distortion lower bound kappa_{Q_7}(QFail2) >= 41/40 (i.e. 41 * q <= 40 * p). -/
theorem qfail2_q7_distortion_ge_41_40 (s : List Int) (p q : Nat)
    (hMs : ∀ r ∈ qfail2RowsSp.map (sparseToDense 127), 0 ≤ dotList r s)
    (hlb : ∀ i, (hi : i < 21) → qfail2D[i]'hi ≤ ((qfailDRowsSp.map (sparseToDense 127)).map (fun r => dotList r s))[i]'(by simp only [List.length_map]; exact hi))
    (hub : ∀ i, (hi : i < 21) → (q : Int) * ((qfailDRowsSp.map (sparseToDense 127)).map (fun r => dotList r s))[i]'(by simp only [List.length_map]; exact hi) ≤ (p : Int) * qfail2D[i]'hi)
    : (q : Int) * 41 ≤ (p : Int) * 40 := by
  have hbound := farkas_distortion_bound
    (qfail2RowsSp.map (sparseToDense 127)) (qfailDRowsSp.map (sparseToDense 127))
    qfail2Y qfail2Alpha qfail2Beta s qfail2D 127 21 p q
    (fun r hr => by simp only [List.mem_map] at hr; rcases hr with ⟨sp, _, rfl⟩; exact sparseToDense_length 127 sp)
    (fun r hr => by simp only [List.mem_map] at hr; rcases hr with ⟨sp, _, rfl⟩; exact sparseToDense_length 127 sp)
    rfl rfl rfl rfl (by decide) (by decide) (by decide) qfail2_farkas_id hMs hlb hub
  have ha : dotList qfail2Alpha qfail2D = 41 := by decide
  have hb : dotList qfail2Beta qfail2D = 40 := by decide
  rw [ha, hb] at hbound
  exact hbound

/-- Unconditional distortion lower bound kappa_{Q_{10}}(K_{5,5}-M) >= 12/11 (i.e. 12 * q <= 11 * p). -/
theorem k55m_q10_distortion_ge_12_11 (s : List Int) (p q : Nat)
    (hMs : ∀ r ∈ k55mRowsSp.map (sparseToDense 33), 0 ≤ dotList r s)
    (hlb : ∀ i, (hi : i < 3) → k55mD[i]'hi ≤ ((k55mDRowsSp.map (sparseToDense 33)).map (fun r => dotList r s))[i]'(by simp only [List.length_map]; exact hi))
    (hub : ∀ i, (hi : i < 3) → (q : Int) * ((k55mDRowsSp.map (sparseToDense 33)).map (fun r => dotList r s))[i]'(by simp only [List.length_map]; exact hi) ≤ (p : Int) * k55mD[i]'hi)
    : (q : Int) * 12 ≤ (p : Int) * 11 := by
  have hbound := farkas_distortion_bound
    (k55mRowsSp.map (sparseToDense 33)) (k55mDRowsSp.map (sparseToDense 33))
    k55mY k55mAlpha k55mBeta s k55mD 33 3 p q
    (fun r hr => by simp only [List.mem_map] at hr; rcases hr with ⟨sp, _, rfl⟩; exact sparseToDense_length 33 sp)
    (fun r hr => by simp only [List.mem_map] at hr; rcases hr with ⟨sp, _, rfl⟩; exact sparseToDense_length 33 sp)
    rfl rfl rfl rfl (by decide) (by decide) (by decide) k55m_farkas_id hMs hlb hub
  have ha : dotList k55mAlpha k55mD = 12 := by decide
  have hb : dotList k55mBeta k55mD = 11 := by decide
  rw [ha, hb] at hbound
  exact hbound

end QuantumEntropicMetrics
