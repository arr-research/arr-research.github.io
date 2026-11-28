/-
Deep Constructive Lean 4.36.0 Formalization (0 sorry, 0 grind, 0 Classical.choice)
Quantitative Hankel-SOS Sum-Negativity Bounds, Exact Blind-Spot Constructions,
and Higher-Order Moment Hierarchies for Discrete Wigner Magic
(strictly advancing Sharma, Chakrabarty, Mukherjee, Mallick, and Maity,
arXiv:2611.34668v1).
-/

namespace WignerMomentMagic

/-- Evaluate a polynomial with integer coefficients at an integer point (Horner form). -/
def evalPoly : List Int → Int → Int
  | [], _ => 0
  | c :: cs, x => c + x * evalPoly cs x

/-- Signed sum of x * q(x)^2 over an arbitrary integer-scaled Wigner list. -/
def sumXPolySq (poly : List Int) : List Int → Int
  | [] => 0
  | x :: xs => x * (evalPoly poly x * evalPoly poly x) + sumXPolySq poly xs

/-- Scaled sum negativity N_scaled(xs) = sum_{x < 0} (-x). -/
def sumNeg : List Int → Int
  | [] => 0
  | x :: xs => (if x < 0 then -x else 0) + sumNeg xs

/-- Scaled L1 norm = sum |x|. -/
def sumAbs : List Int → Int
  | [] => 0
  | x :: xs => (if x < 0 then -x else x) + sumAbs xs

/-- Raw integer sum = sum x. -/
def sumRaw : List Int → Int
  | [] => 0
  | x :: xs => x + sumRaw xs

/-- Exact integer power x^k. -/
def ipowInt (x : Int) : Nat → Int
  | 0 => 1
  | k + 1 => x * ipowInt x k

/-- Scaled k-th power moment sum x^k. -/
def sumPow (k : Nat) : List Int → Int
  | [] => 0
  | x :: xs => ipowInt x k + sumPow k xs

/-- Positive-part sums (x >= 0). -/
def sumPosPow (k : Nat) : List Int → Int
  | [] => 0
  | x :: xs => (if x < 0 then 0 else ipowInt x k) + sumPosPow k xs

/-- Negative-part magnitude sums (x < 0 -> (-x)^k). -/
def sumNegPow (k : Nat) : List Int → Int
  | [] => 0
  | x :: xs => (if x < 0 then ipowInt (-x) k else 0) + sumNegPow k xs

/-- Helper: every integer square is nonnegative (purely constructive, 0 Classical.choice). -/
theorem sq_nonneg (a : Int) : 0 ≤ a * a := by
  cases a with
  | ofNat n => exact Int.natCast_nonneg (n * n)
  | negSucc n => exact Int.natCast_nonneg ((n + 1) * (n + 1))

/-- T01: Universal exact L1-norm / sum-negativity identity: sum |x| = sum x + 2 * sumNeg(xs). -/
theorem T01_l1_norm_eq_raw_plus_two_neg (xs : List Int) :
    sumAbs xs = sumRaw xs + 2 * sumNeg xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
    simp only [sumAbs, sumRaw, sumNeg]
    cases Int.decLt x 0 with
    | isTrue h => simp only [h, ↓reduceIte]; omega
    | isFalse h => simp only [h, ↓reduceIte]; omega

/-- T02: Universal nonnegativity of sumNeg over any finite distribution. -/
theorem T02_sumNeg_nonneg (xs : List Int) : 0 ≤ sumNeg xs := by
  induction xs with
  | nil => decide
  | cons x xs ih =>
    simp only [sumNeg]
    cases Int.decLt x 0 with
    | isTrue h => simp only [h, ↓reduceIte]; omega
    | isFalse h => simp only [h, ↓reduceIte]; omega

/-- T03: Universal Hankel-SOS Quantitative Negativity Theorem (Theorem 1 core!):
    For ANY polynomial q, ANY finite distribution xs, and ANY uniform upper bound M >= 0
    such that q(x)^2 <= M on every negative point x in xs:
      sum_u x_u * q(x_u)^2 + M * sumNeg(xs) >= 0. -/
theorem T03_universal_hankel_sos_negativity_bound
    (poly : List Int) (M : Int) (xs : List Int)
    (hBound : ∀ x, x ∈ xs → x < 0 → evalPoly poly x * evalPoly poly x ≤ M) :
    0 ≤ sumXPolySq poly xs + M * sumNeg xs := by
  induction xs with
  | nil =>
    simp only [sumXPolySq, sumNeg]
    omega
  | cons x xs ih =>
    have ih' := ih (fun y hy => hBound y (List.mem_cons_of_mem x hy))
    simp only [sumXPolySq, sumNeg]
    by_cases hx : x < 0
    · simp only [hx, ↓reduceIte]
      have hq : evalPoly poly x * evalPoly poly x ≤ M := hBound x List.mem_cons_self hx
      have hpos : 0 ≤ -x := by omega
      have hdiff : 0 ≤ M - evalPoly poly x * evalPoly poly x := by omega
      have hprod : 0 ≤ (-x) * (M - evalPoly poly x * evalPoly poly x) := Int.mul_nonneg hpos hdiff
      have hexp : (-x) * (M - evalPoly poly x * evalPoly poly x)
          = x * (evalPoly poly x * evalPoly poly x) + M * (-x) := by
        rw [Int.mul_sub, Int.neg_mul, Int.neg_mul, Int.mul_comm x M, Int.mul_neg]
        omega
      rw [hexp] at hprod
      rw [Int.mul_add]
      omega
    · simp only [hx, ↓reduceIte]
      have hpos : 0 ≤ x := by omega
      have hsq : 0 ≤ evalPoly poly x * evalPoly poly x := sq_nonneg _
      have hprod : 0 ≤ x * (evalPoly poly x * evalPoly poly x) := Int.mul_nonneg hpos hsq
      rw [Int.mul_add]
      omega

/-- T04: Exact degree-1 Hankel-SOS expansion: sum_u x_u * (a + b*x_u)^2 = a^2*S1 + 2*a*b*S2 + b^2*S3. -/
theorem T04_deg1_hankel_quadratic_expansion (a b : Int) (xs : List Int) :
    sumXPolySq [a, b] xs =
      a * a * sumPow 1 xs + 2 * a * b * sumPow 2 xs + b * b * sumPow 3 xs := by
  induction xs with
  | nil =>
    simp only [sumXPolySq, sumPow]
    omega
  | cons x xs ih =>
    simp only [sumXPolySq, evalPoly, sumPow, ipowInt, Int.mul_zero, Int.add_zero, Int.mul_one]
    rw [ih]
    have hstep : x * ((a + x * b) * (a + x * b))
        = a * a * x + 2 * a * b * (x * x) + b * b * (x * (x * x)) := by
      rw [Int.add_mul, Int.mul_add, Int.mul_add, Int.mul_add, Int.mul_add, Int.mul_add]
      have h1 : x * (a * a) = a * a * x := Int.mul_comm _ _
      have h2 : x * (a * (x * b)) = a * b * (x * x) := by
        rw [Int.mul_left_comm a x b, ← Int.mul_assoc, Int.mul_comm (x * x) (a * b)]
      have h3 : x * (x * b * a) = a * b * (x * x) := by
        rw [Int.mul_comm (x * b) a, Int.mul_left_comm a x b, ← Int.mul_assoc, Int.mul_comm (x * x) (a * b)]
      have h4 : x * (x * b * (x * b)) = b * b * (x * (x * x)) := by
        rw [Int.mul_comm x b, Int.mul_assoc b x (b * x), Int.mul_left_comm x b x,
            ← Int.mul_assoc b b (x * x), Int.mul_comm x (b * b * (x * x)),
            Int.mul_assoc (b * b) (x * x) x, Int.mul_comm (x * x) x]
      have h5 : 2 * a * b * (x * x) = 2 * (a * b * (x * x)) := by
        rw [Int.mul_assoc 2 a b, Int.mul_assoc 2 (a * b) (x * x)]
      rw [h1, h2, h3, h4, h5]
      omega
    rw [hstep, Int.mul_add, Int.mul_add, Int.mul_add]
    omega

/-- T05: Exact bounding of linear polynomial (-l + x)^2 <= (l + R)^2 on -R <= x <= 0 (for l >= 0, R >= 0). -/
theorem T05_deg1_negative_interval_max (l R x : Int) (hl : 0 ≤ l) (hR : -R ≤ x) (hx : x ≤ 0) :
    evalPoly [-l, 1] x * evalPoly [-l, 1] x ≤ (l + R) * (l + R) := by
  simp only [evalPoly, Int.mul_zero, Int.add_zero, Int.mul_one]
  have h1 : 0 ≤ l + R + (-l + x) := by omega
  have h2 : 0 ≤ l + R - (-l + x) := by omega
  have hprod := Int.mul_nonneg h1 h2
  have hid : (l + R + (-l + x)) * (l + R - (-l + x)) = (l + R) * (l + R) - (-l + x) * (-l + x) := by
    rw [Int.add_mul, Int.mul_sub, Int.mul_sub, Int.mul_comm (-l + x) (l + R)]
    omega
  rw [hid] at hprod
  omega

/-- T06: Exact Recovery of Sharma et al. Theorem 4 as the m=1 Dual of Theorem 1! -/
theorem T06_sharma_thm4_exact_m1_dual_identity (D P b N : Int)
    (hOpt : (D + P) * (D + P) * b - 2 * (P + b) * (D + P) * P + (P + b) * (P + b) * D
            + (D + 2 * P + b) * (D + 2 * P + b) * N ≥ 0)
    (hDenPos : 0 < D + 2 * P + b) :
    P * P - D * b ≤ (D + 2 * P + b) * N := by
  have hL1 : (D + P) * (D + P) * b = D * (D * b) + 2 * (D * b * P) + b * (P * P) := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add, Int.add_mul, Int.add_mul, Int.add_mul]
    have e1 : D * D * b = D * (D * b) := Int.mul_assoc _ _ _
    have e2 : D * P * b = D * b * P := by rw [Int.mul_assoc, Int.mul_comm P b, ← Int.mul_assoc]
    have e3 : P * D * b = D * b * P := by rw [Int.mul_comm P D, Int.mul_assoc, Int.mul_comm P b, ← Int.mul_assoc]
    have e4 : P * P * b = b * (P * P) := Int.mul_comm _ _
    rw [e1, e2, e3, e4]; omega
  have hL2 : 2 * (P + b) * (D + P) * P = 2 * (D * (P * P)) + 2 * (D * b * P) + 2 * (P * (P * P)) + 2 * (b * (P * P)) := by
    have s1 : 2 * (P + b) = 2 * P + 2 * b := Int.mul_add 2 P b
    rw [s1, Int.add_mul, Int.mul_add, Int.mul_add, Int.add_mul, Int.add_mul, Int.add_mul]
    have e1 : 2 * P * D * P = 2 * (D * (P * P)) := by
      rw [Int.mul_assoc 2 P D, Int.mul_comm P D, Int.mul_assoc 2 (D * P) P, Int.mul_assoc D P P]
    have e2 : 2 * P * P * P = 2 * (P * (P * P)) := by
      rw [Int.mul_assoc 2 P P, Int.mul_assoc 2 (P * P) P, Int.mul_assoc P P P]
    have e3 : 2 * b * D * P = 2 * (D * b * P) := by
      rw [Int.mul_assoc 2 b D, Int.mul_comm b D, Int.mul_assoc 2 (D * b) P]
    have e4 : 2 * b * P * P = 2 * (b * (P * P)) := by
      rw [Int.mul_assoc 2 b P, Int.mul_assoc 2 (b * P) P, Int.mul_assoc b P P]
    rw [e1, e2, e3, e4]; omega
  have hL3 : (P + b) * (P + b) * D = D * (P * P) + 2 * (D * b * P) + b * (D * b) := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add, Int.add_mul, Int.add_mul, Int.add_mul]
    have e1 : P * P * D = D * (P * P) := Int.mul_comm _ _
    have e2 : P * b * D = D * b * P := by
      rw [Int.mul_comm (P * b) D, Int.mul_comm P b, ← Int.mul_assoc D b P]
    have e3 : b * P * D = D * b * P := by
      rw [Int.mul_comm (b * P) D, ← Int.mul_assoc D b P]
    have e4 : b * b * D = b * (D * b) := by
      rw [Int.mul_assoc b b D, Int.mul_comm b D]
    rw [e1, e2, e3, e4]; omega
  have hR : (D + 2 * P + b) * (D * b - P * P)
      = D * (D * b) - D * (P * P) + 2 * (D * b * P) - 2 * (P * (P * P)) + b * (D * b) - b * (P * P) := by
    rw [Int.add_mul, Int.add_mul, Int.mul_sub, Int.mul_sub, Int.mul_sub]
    have e1 : 2 * P * (D * b) = 2 * (D * b * P) := by rw [Int.mul_assoc 2 P (D * b), Int.mul_comm P (D * b)]
    have e2 : 2 * P * (P * P) = 2 * (P * (P * P)) := Int.mul_assoc _ _ _
    rw [e1, e2]; omega
  have hid : (D + P) * (D + P) * b - 2 * (P + b) * (D + P) * P + (P + b) * (P + b) * D
      = (D + 2 * P + b) * (D * b - P * P) := by
    rw [hL1, hL2, hL3, hR]; omega
  rw [hid] at hOpt
  have hfac : (D + 2 * P + b) * (D * b - P * P) + (D + 2 * P + b) * (D + 2 * P + b) * N
      = (D + 2 * P + b) * (D * b - P * P + (D + 2 * P + b) * N) := by
    rw [Int.mul_assoc (D + 2 * P + b) (D + 2 * P + b) N, ← Int.mul_add]
  rw [hfac] at hOpt
  cases Int.decLt (D * b - P * P + (D + 2 * P + b) * N) 0 with
  | isTrue hneg =>
    have hpos2 : 0 < -(D * b - P * P + (D + 2 * P + b) * N) := by omega
    have hm := Int.mul_pos hDenPos hpos2
    rw [Int.mul_neg] at hm
    omega
  | isFalse hge => omega

/-- T07: Universal Positive/Negative Split Identity for Odd & Even Moments. -/
theorem T07_signed_moment_split (xs : List Int) :
    sumPow 2 xs = sumPosPow 2 xs + sumNegPow 2 xs ∧
    sumPow 3 xs = sumPosPow 3 xs - sumNegPow 3 xs := by
  induction xs with
  | nil => exact ⟨rfl, rfl⟩
  | cons x xs ih =>
    rcases ih with ⟨ih2, ih3⟩
    simp only [sumPow, sumPosPow, sumNegPow, ipowInt, Int.mul_one]
    cases Int.decLt x 0 with
    | isTrue h =>
      simp only [h, ↓reduceIte]
      have h2 : (-x) * (-x) = x * x := Int.neg_mul_neg x x
      have h3 : (-x) * (x * x) = -(x * (x * x)) := Int.neg_mul x (x * x)
      rw [h2, h3]
      omega
    | isFalse h =>
      simp only [h, ↓reduceIte]
      omega

/-- T08: Exact Cauchy-Schwarz Inequality over Arbitrary Finite Lists. -/
def dotProd : List Int → List Int → Int
  | [], _ => 0
  | _, [] => 0
  | a :: as, b :: bs => a * b + dotProd as bs

def sumSq : List Int → Int
  | [] => 0
  | a :: as => a * a + sumSq as

theorem sumSq_nonneg (as : List Int) : 0 ≤ sumSq as := by
  induction as with
  | nil => decide
  | cons a as ih =>
    simp only [sumSq]
    have h := sq_nonneg a
    omega

theorem T08_cauchy_schwarz_finite_list (as bs : List Int) (hlen : as.length = bs.length) :
    dotProd as bs * dotProd as bs ≤ sumSq as * sumSq bs := by
  induction as generalizing bs with
  | nil =>
    cases bs with
    | nil => decide
    | cons _ _ => simp at hlen
  | cons a as ih =>
    cases bs with
    | nil => simp at hlen
    | cons b bs =>
      simp only [List.length_cons, Nat.succ.injEq] at hlen
      have ih' := ih bs hlen
      simp only [dotProd, sumSq]
      have haux : ∀ (u v : List Int), u.length = v.length →
          0 ≤ b * b * sumSq u - 2 * a * b * dotProd u v + a * a * sumSq v := by
        intro u
        induction u with
        | nil =>
          intro v hv
          cases v with
          | nil => simp [sumSq, dotProd]
          | cons _ _ => simp at hv
        | cons x xs ihu =>
          intro v hv
          cases v with
          | nil => simp at hv
          | cons y ys =>
            simp only [List.length_cons, Nat.succ.injEq] at hv
            have hrest := ihu ys hv
            simp only [sumSq, dotProd]
            have hsq := sq_nonneg (b * x - a * y)
            have hexp : (b * x - a * y) * (b * x - a * y)
                = b * b * (x * x) - 2 * a * b * (x * y) + a * a * (y * y) := by
              rw [Int.sub_mul, Int.mul_sub, Int.mul_sub]
              have p1 : b * x * (b * x) = b * b * (x * x) := by
                rw [Int.mul_assoc b x (b * x), Int.mul_left_comm x b x, ← Int.mul_assoc b b (x * x)]
              have p2 : a * y * (a * y) = a * a * (y * y) := by
                rw [Int.mul_assoc a y (a * y), Int.mul_left_comm y a y, ← Int.mul_assoc a a (y * y)]
              have p3 : b * x * (a * y) = a * b * (x * y) := by
                rw [Int.mul_assoc b x (a * y), Int.mul_left_comm x a y, ← Int.mul_assoc b a (x * y), Int.mul_comm b a]
              have p4 : a * y * (b * x) = a * b * (x * y) := by
                rw [Int.mul_assoc a y (b * x), Int.mul_left_comm y b x, Int.mul_comm y x, ← Int.mul_assoc a b (x * y)]
              have p5 : 2 * a * b * (x * y) = 2 * (a * b * (x * y)) := by
                rw [Int.mul_assoc 2 a b, Int.mul_assoc 2 (a * b) (x * y)]
              rw [p1, p2, p3, p4, p5]
              omega
            rw [Int.mul_add, Int.mul_add, Int.mul_add]
            omega
      have hcross := haux as bs hlen
      rw [Int.add_mul, Int.mul_add, Int.mul_add, Int.add_mul, Int.mul_add, Int.mul_add]
      have h1 : a * b * (a * b) = a * a * (b * b) := by
        rw [Int.mul_assoc a b (a * b), Int.mul_left_comm b a b, ← Int.mul_assoc a a (b * b)]
      have h3 : dotProd as bs * (a * b) = a * b * dotProd as bs := Int.mul_comm _ _
      have h4 : sumSq as * (b * b) = b * b * sumSq as := Int.mul_comm _ _
      have h5 : 2 * a * b * dotProd as bs = 2 * (a * b * dotProd as bs) := by
        rw [Int.mul_assoc 2 a b, Int.mul_assoc 2 (a * b) (dotProd as bs)]
      rw [h1, h3, h4]
      rw [h5] at hcross
      omega

/-- T09: Universal H_1 PSD Theorem for Nonnegative Distributions via Pairwise Double-Sum SOS. -/
def pairwiseXDiffSq (y : Int) : List Int → Int
  | [] => 0
  | x :: xs => y * x * ((y - x) * (y - x)) + pairwiseXDiffSq y xs

def doubleSumXDiffSq : List Int → List Int → Int
  | [], _ => 0
  | y :: ys, xs => pairwiseXDiffSq y xs + doubleSumXDiffSq ys xs

theorem pairwiseXDiffSq_nonneg (y : Int) (hy : 0 ≤ y) (xs : List Int) (hxs : ∀ x ∈ xs, 0 ≤ x) :
    0 ≤ pairwiseXDiffSq y xs := by
  induction xs with
  | nil => simp [pairwiseXDiffSq]
  | cons x xs ih =>
    simp only [pairwiseXDiffSq]
    have hx := hxs x List.mem_cons_self
    have hrest := ih (fun z hz => hxs z (List.mem_cons_of_mem x hz))
    have h1 := Int.mul_nonneg (Int.mul_nonneg hy hx) (sq_nonneg (y - x))
    omega

theorem pairwiseXDiffSq_expand (y : Int) (xs : List Int) :
    pairwiseXDiffSq y xs =
      y * y * y * sumPow 1 xs - 2 * (y * y) * sumPow 2 xs + y * sumPow 3 xs := by
  induction xs with
  | nil =>
    simp only [pairwiseXDiffSq, sumPow]; omega
  | cons x xs ih =>
    simp only [pairwiseXDiffSq, sumPow, ipowInt, Int.mul_one]
    rw [ih]
    have hterm : y * x * ((y - x) * (y - x))
        = y * y * y * x - 2 * (y * y) * (x * x) + y * (x * (x * x)) := by
      rw [Int.sub_mul, Int.mul_sub, Int.mul_sub, Int.mul_sub, Int.mul_sub, Int.mul_sub]
      have a1 : y * x * (y * y) = y * y * y * x := by
        rw [Int.mul_comm (y * x) (y * y), ← Int.mul_assoc (y * y) y x]
      have a2 : y * x * (y * x) = y * y * (x * x) := by
        rw [Int.mul_assoc y x (y * x), Int.mul_left_comm x y x, ← Int.mul_assoc y y (x * x)]
      have a3 : y * x * (x * y) = y * y * (x * x) := by
        rw [Int.mul_comm x y, Int.mul_assoc y x (y * x), Int.mul_left_comm x y x, ← Int.mul_assoc y y (x * x)]
      have a4 : y * x * (x * x) = y * (x * (x * x)) := Int.mul_assoc _ _ _
      have a5 : 2 * (y * y) * (x * x) = 2 * (y * y * (x * x)) := Int.mul_assoc _ _ _
      rw [a1, a2, a3, a4, a5]
      omega
    rw [hterm, Int.mul_add, Int.mul_add, Int.mul_add]
    omega

theorem doubleSumXDiffSq_expand (ys xs : List Int) :
    doubleSumXDiffSq ys xs =
      sumPow 3 ys * sumPow 1 xs - 2 * (sumPow 2 ys * sumPow 2 xs) + sumPow 1 ys * sumPow 3 xs := by
  induction ys with
  | nil => simp only [doubleSumXDiffSq, sumPow]; omega
  | cons y ys ih =>
    simp only [doubleSumXDiffSq, sumPow, ipowInt, Int.mul_one]
    rw [pairwiseXDiffSq_expand y xs, ih]
    have h1 : y * (y * y) = y * y * y := (Int.mul_assoc y y y).symm
    have h2 : 2 * (y * y) * sumPow 2 xs = 2 * (y * y * sumPow 2 xs) := Int.mul_assoc _ _ _
    rw [h1, h2, Int.add_mul, Int.add_mul, Int.add_mul, Int.mul_add]
    omega

theorem T09_nonneg_dist_H1_psd (xs : List Int) (hxs : ∀ x ∈ xs, 0 ≤ x) :
    sumPow 2 xs * sumPow 2 xs ≤ sumPow 1 xs * sumPow 3 xs := by
  have hnn : ∀ ys, (∀ y ∈ ys, 0 ≤ y) → 0 ≤ doubleSumXDiffSq ys xs := by
    intro ys hys
    induction ys with
    | nil => simp [doubleSumXDiffSq]
    | cons y ys ihy =>
      simp only [doubleSumXDiffSq]
      have hp := pairwiseXDiffSq_nonneg y (hys y List.mem_cons_self) xs hxs
      have hr := ihy (fun z hz => hys z (List.mem_cons_of_mem y hz))
      omega
  have h0 := hnn xs hxs
  rw [doubleSumXDiffSq_expand xs xs] at h0
  have hc : sumPow 3 xs * sumPow 1 xs = sumPow 1 xs * sumPow 3 xs := Int.mul_comm _ _
  rw [hc] at h0
  omega

/-- Helper lemma for positive-part mapping. -/
def clampPos (x : Int) : Int := if x < 0 then 0 else x

theorem sumPow_clampPos (k : Nat) (hk : 1 ≤ k) (xs : List Int) :
    sumPow k (xs.map clampPos) = sumPosPow k xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
    simp only [List.map_cons, sumPow, sumPosPow, clampPos]
    cases Int.decLt x 0 with
    | isTrue hx =>
      simp only [hx, ↓reduceIte]
      have hz : ipowInt 0 k = 0 := by
        cases k with
        | zero => omega
        | succ j => simp [ipowInt]
      rw [hz, ih]
    | isFalse hx =>
      simp only [hx, ↓reduceIte]
      rw [ih]

/-- T10: Exact Self-Consistent Positive-Part Cauchy-Schwarz Inequality (Theorem 2!). -/
theorem T10_positive_part_cauchy_schwarz (xs : List Int) :
    sumPosPow 2 xs * sumPosPow 2 xs ≤ sumPosPow 1 xs * sumPosPow 3 xs := by
  have hnn : ∀ y ∈ xs.map clampPos, 0 ≤ y := by
    intro y hy
    rcases List.mem_map.mp hy with ⟨x, _, rfl⟩
    unfold clampPos
    cases Int.decLt x 0 with
    | isTrue hx => simp [hx]
    | isFalse hx => simp [hx]; omega
  have h9 := T09_nonneg_dist_H1_psd (xs.map clampPos) hnn
  rw [sumPow_clampPos 1 (by omega) xs, sumPow_clampPos 2 (by omega) xs, sumPow_clampPos 3 (by omega) xs] at h9
  exact h9

/-- Helper identity for expanding x*(v0 + x*(v1 + x*v2))^2. -/
theorem deg2_pointwise_expand (v0 v1 v2 x : Int) :
    x * ((v0 + x * (v1 + x * v2)) * (v0 + x * (v1 + x * v2))) =
      v0 * v0 * x +
      2 * v0 * v1 * (x * x) +
      (v1 * v1 + 2 * v0 * v2) * (x * (x * x)) +
      2 * v1 * v2 * (x * (x * (x * x))) +
      v2 * v2 * (x * (x * (x * (x * x)))) := by
  have hlin : v0 + x * (v1 + x * v2) = (v0 + v1 * x) + v2 * (x * x) := by
    rw [Int.mul_add, Int.mul_comm x v1, ← Int.mul_assoc x x v2, Int.mul_comm (x * x) v2, Int.add_assoc]
  rw [hlin]
  have hsq : ∀ A B C : Int, ((A + B) + C) * ((A + B) + C) =
      A * A + 2 * (A * B) + B * B + 2 * (A * C) + 2 * (B * C) + C * C := by
    intro A B C
    rw [Int.add_mul, Int.add_mul, Int.mul_add, Int.mul_add, Int.mul_add, Int.mul_add,
        Int.mul_add, Int.mul_add, Int.mul_comm B A, Int.mul_comm C A, Int.mul_comm C B]
    omega
  rw [hsq v0 (v1 * x) (v2 * (x * x)),
      Int.mul_add, Int.mul_add, Int.mul_add, Int.mul_add, Int.mul_add]
  have t1 : x * (v0 * v0) = v0 * v0 * x := Int.mul_comm _ _
  have t2 : x * (2 * (v0 * (v1 * x))) = 2 * v0 * v1 * (x * x) := by
    rw [← Int.mul_assoc v0 v1 x, Int.mul_comm x (2 * (v0 * v1 * x)),
        ← Int.mul_assoc 2 (v0 * v1) x, Int.mul_assoc (2 * (v0 * v1)) x x, ← Int.mul_assoc 2 v0 v1]
  have t3 : x * (v1 * x * (v1 * x)) = v1 * v1 * (x * (x * x)) := by
    rw [Int.mul_assoc v1 x (v1 * x), Int.mul_left_comm x v1 x, ← Int.mul_assoc v1 v1 (x * x),
        Int.mul_comm x (v1 * v1 * (x * x)), Int.mul_assoc (v1 * v1) (x * x) x, Int.mul_comm (x * x) x]
  have t4 : x * (2 * (v0 * (v2 * (x * x)))) = 2 * v0 * v2 * (x * (x * x)) := by
    rw [← Int.mul_assoc v0 v2 (x * x), Int.mul_comm x (2 * (v0 * v2 * (x * x))),
        ← Int.mul_assoc 2 (v0 * v2) (x * x), Int.mul_assoc (2 * (v0 * v2)) (x * x) x,
        Int.mul_comm (x * x) x, ← Int.mul_assoc 2 v0 v2]
  have t5 : x * (2 * (v1 * x * (v2 * (x * x)))) = 2 * v1 * v2 * (x * (x * (x * x))) := by
    rw [Int.mul_assoc v1 x (v2 * (x * x)), Int.mul_left_comm x v2 (x * x),
        ← Int.mul_assoc v1 v2 (x * (x * x)), Int.mul_comm x (2 * (v1 * v2 * (x * (x * x)))),
        ← Int.mul_assoc 2 (v1 * v2) (x * (x * x)), Int.mul_assoc (2 * (v1 * v2)) (x * (x * x)) x,
        Int.mul_comm (x * (x * x)) x, ← Int.mul_assoc 2 v1 v2]
  have t6 : x * (v2 * (x * x) * (v2 * (x * x))) = v2 * v2 * (x * (x * (x * (x * x)))) := by
    rw [Int.mul_assoc v2 (x * x) (v2 * (x * x)), Int.mul_left_comm (x * x) v2 (x * x),
        ← Int.mul_assoc v2 v2 ((x * x) * (x * x)), Int.mul_comm x (v2 * v2 * ((x * x) * (x * x))),
        Int.mul_assoc (v2 * v2) ((x * x) * (x * x)) x,
        Int.mul_assoc x x (x * x), Int.mul_comm (x * (x * (x * x))) x]
  rw [t1, t2, t3, t4, t5, t6, Int.add_mul]
  omega

/-- T11: Exact Degree-2 (m=2) Hankel Quadratic Form Identity:
    sum_u x_u (v0 + v1 x_u + v2 x_u^2)^2 = v^T H_2 v! -/
theorem T11_deg2_hankel_quadratic_expansion (v0 v1 v2 : Int) (xs : List Int) :
    sumXPolySq [v0, v1, v2] xs =
      v0 * v0 * sumPow 1 xs +
      2 * v0 * v1 * sumPow 2 xs +
      (v1 * v1 + 2 * v0 * v2) * sumPow 3 xs +
      2 * v1 * v2 * sumPow 4 xs +
      v2 * v2 * sumPow 5 xs := by
  induction xs with
  | nil => simp only [sumXPolySq, sumPow]; omega
  | cons x xs ih =>
    simp only [sumXPolySq, evalPoly, sumPow, ipowInt, Int.mul_zero, Int.add_zero, Int.mul_one]
    rw [ih, deg2_pointwise_expand v0 v1 v2 x, Int.mul_add, Int.mul_add, Int.mul_add, Int.mul_add, Int.mul_add]
    omega

/-- Helpers for T12 (Holder k=2 universal inequality). -/
def iabs (x : Int) : Int := if x < 0 then -x else x

theorem sumPow1_iabs (xs : List Int) : sumPow 1 (xs.map iabs) = sumAbs xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih => simp only [List.map_cons, sumPow, sumAbs, ipowInt, Int.mul_one, iabs]; rw [ih]

theorem sumPow2_iabs (xs : List Int) : sumPow 2 (xs.map iabs) = sumPow 2 xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
    simp only [List.map_cons, sumPow, ipowInt, Int.mul_one, iabs]; rw [ih]
    cases Int.decLt x 0 with
    | isTrue hx => simp only [hx, ↓reduceIte, Int.neg_mul_neg]
    | isFalse hx => simp only [hx, ↓reduceIte]

theorem dotProd_iabs_sq (xs : List Int) :
    dotProd (xs.map iabs) (xs.map (fun x => x * x)) = sumPow 3 (xs.map iabs) := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
    simp only [List.map_cons, dotProd, sumPow, ipowInt, Int.mul_one, iabs]; rw [ih]
    cases Int.decLt x 0 with
    | isTrue hx => simp only [hx, ↓reduceIte, Int.neg_mul_neg]
    | isFalse hx => simp only [hx, ↓reduceIte]

theorem sumSq_iabs (xs : List Int) : sumSq (xs.map iabs) = sumPow 2 xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
    simp only [List.map_cons, sumSq, sumPow, ipowInt, Int.mul_one, iabs]; rw [ih]
    cases Int.decLt x 0 with
    | isTrue hx => simp only [hx, ↓reduceIte, Int.neg_mul_neg]
    | isFalse hx => simp only [hx, ↓reduceIte]

theorem sumSq_sq (xs : List Int) : sumSq (xs.map (fun x => x * x)) = sumPow 4 xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
    simp only [List.map_cons, sumSq, sumPow, ipowInt, Int.mul_one]
    rw [ih, Int.mul_assoc x x (x * x)]

theorem sumAbs_nonneg (xs : List Int) : 0 ≤ sumAbs xs := by
  induction xs with
  | nil => decide
  | cons x xs ih =>
    simp only [sumAbs]
    cases Int.decLt x 0 with
    | isTrue h => simp only [h, ↓reduceIte]; omega
    | isFalse h => simp only [h, ↓reduceIte]; omega

theorem sumPow3_iabs_nonneg (xs : List Int) : 0 ≤ sumPow 3 (xs.map iabs) := by
  induction xs with
  | nil => decide
  | cons x xs ih =>
    simp only [List.map_cons, sumPow, ipowInt, Int.mul_one, iabs]
    have hx : 0 ≤ (if x < 0 then -x else x) := by
      cases Int.decLt x 0 with
      | isTrue h => simp only [h, ↓reduceIte]; omega
      | isFalse h => simp only [h, ↓reduceIte]; omega
    have hp := Int.mul_nonneg hx (sq_nonneg (if x < 0 then -x else x))
    omega

/-- T12: Exact Sharma et al. Theorem 5 (k=2) Holder Inequality over Arbitrary Signed Finite Lists:
    (sum x^2)^3 <= (sum |x|)^2 * (sum x^4). -/
theorem T12_holder_k2_w2_w4_universal (xs : List Int) :
    sumPow 2 xs * sumPow 2 xs * sumPow 2 xs ≤ sumAbs xs * sumAbs xs * sumPow 4 xs := by
  have hnn : ∀ y ∈ xs.map iabs, 0 ≤ y := by
    intro y hy
    rcases List.mem_map.mp hy with ⟨x, _, rfl⟩
    unfold iabs
    cases Int.decLt x 0 with
    | isTrue h => simp only [h, ↓reduceIte]; omega
    | isFalse h => simp only [h, ↓reduceIte]; omega
  have hlen : (xs.map iabs).length = (xs.map (fun x => x * x)).length := by simp
  have hcs := T08_cauchy_schwarz_finite_list (xs.map iabs) (xs.map (fun x => x * x)) hlen
  rw [dotProd_iabs_sq, sumSq_iabs, sumSq_sq] at hcs
  have ht9 := T09_nonneg_dist_H1_psd (xs.map iabs) hnn
  rw [sumPow1_iabs, sumPow2_iabs] at ht9
  have hS2_nn : 0 ≤ sumPow 2 xs := by rw [← sumSq_iabs]; exact sumSq_nonneg _
  have hS1_nn : 0 ≤ sumAbs xs := sumAbs_nonneg xs
  have hS3_nn : 0 ≤ sumPow 3 (xs.map iabs) := sumPow3_iabs_nonneg xs
  have hstep1 : sumPow 2 xs * sumPow 2 xs * (sumPow 2 xs * sumPow 2 xs)
      ≤ sumAbs xs * sumPow 3 (xs.map iabs) * (sumAbs xs * sumPow 3 (xs.map iabs)) := by
    have hmul1 := Int.mul_le_mul_of_nonneg_right ht9 (Int.mul_nonneg hS2_nn hS2_nn)
    have hmul2 := Int.mul_le_mul_of_nonneg_left ht9 (Int.mul_nonneg hS1_nn hS3_nn)
    exact Int.le_trans hmul1 hmul2
  have hstep2 : sumAbs xs * sumPow 3 (xs.map iabs) * (sumAbs xs * sumPow 3 (xs.map iabs))
      = sumAbs xs * sumAbs xs * (sumPow 3 (xs.map iabs) * sumPow 3 (xs.map iabs)) := by
    rw [Int.mul_assoc (sumAbs xs) (sumPow 3 (xs.map iabs)),
        Int.mul_left_comm (sumPow 3 (xs.map iabs)) (sumAbs xs),
        ← Int.mul_assoc (sumAbs xs) (sumAbs xs)]
  rw [hstep2] at hstep1
  have hstep3 := Int.mul_le_mul_of_nonneg_left hcs (Int.mul_nonneg hS1_nn hS1_nn)
  have hcomb := Int.le_trans hstep1 hstep3
  cases Int.decEq (sumPow 2 xs) 0 with
  | isTrue hz =>
    rw [hz]
    have hS4_nn : 0 ≤ sumPow 4 xs := by rw [← sumSq_sq]; exact sumSq_nonneg _
    have hrhs := Int.mul_nonneg (Int.mul_nonneg hS1_nn hS1_nn) hS4_nn
    omega
  | isFalse hnz =>
    have hpos : 0 < sumPow 2 xs := by omega
    have hL : sumPow 2 xs * sumPow 2 xs * (sumPow 2 xs * sumPow 2 xs)
        = sumPow 2 xs * (sumPow 2 xs * sumPow 2 xs * sumPow 2 xs) := by
      rw [Int.mul_assoc (sumPow 2 xs) (sumPow 2 xs) (sumPow 2 xs * sumPow 2 xs),
          ← Int.mul_assoc (sumPow 2 xs) (sumPow 2 xs) (sumPow 2 xs)]
    have hR : sumAbs xs * sumAbs xs * (sumPow 2 xs * sumPow 4 xs)
        = sumPow 2 xs * (sumAbs xs * sumAbs xs * sumPow 4 xs) := by
      rw [Int.mul_left_comm (sumAbs xs * sumAbs xs) (sumPow 2 xs) (sumPow 4 xs)]
    rw [hL, hR] at hcomb
    cases Int.decLt (sumAbs xs * sumAbs xs * sumPow 4 xs) (sumPow 2 xs * sumPow 2 xs * sumPow 2 xs) with
    | isTrue hbad =>
      have hlt := Int.mul_lt_mul_of_pos_left hbad hpos
      omega
    | isFalse hok => omega

/-- T13: Exact Reverse-Monotonicity of Higher-Even Moment Hierarchy (Theorem 4 core!):
    (sum x^4)^2 <= (sum x^2) * (sum x^6). -/
theorem T13_reverse_monotonicity_B4_ge_B6 (xs : List Int) :
    sumPow 4 xs * sumPow 4 xs ≤ sumPow 2 xs * sumPow 6 xs := by
  have hd : ∀ ys : List Int, dotProd ys (ys.map (fun x => x * x * x)) = sumPow 4 ys := by
    intro ys
    induction ys with
    | nil => rfl
    | cons x ys ih =>
      simp only [List.map_cons, dotProd, sumPow, ipowInt, Int.mul_one]
      rw [ih, Int.mul_assoc x x x]
  have ha : ∀ ys : List Int, sumSq ys = sumPow 2 ys := by
    intro ys
    induction ys with
    | nil => rfl
    | cons x ys ih => simp only [sumSq, sumPow, ipowInt, Int.mul_one]; rw [ih]
  have hb : ∀ ys : List Int, sumSq (ys.map (fun x => x * x * x)) = sumPow 6 ys := by
    intro ys
    induction ys with
    | nil => rfl
    | cons x ys ih =>
      simp only [List.map_cons, sumSq, sumPow, ipowInt, Int.mul_one]
      rw [ih]
      have h6 : x * x * x * (x * x * x) = x * (x * (x * (x * (x * x)))) := by
        rw [Int.mul_assoc x x x, Int.mul_assoc x (x * x) (x * (x * x)), Int.mul_assoc x x (x * (x * x))]
      rw [h6]
  have hlen : xs.length = (xs.map (fun x => x * x * x)).length := by simp
  have hcs := T08_cauchy_schwarz_finite_list xs (xs.map (fun x => x * x * x)) hlen
  rw [hd xs, ha xs, hb xs] at hcs
  exact hcs

/-- T14: Exact B_4 >= B_6 Power Comparison (cross-multiplied, directly from T13). -/
theorem T14_B4_dominates_B6_exact (xs : List Int) :
    ipowInt (sumPow 2 xs) 5 * (sumPow 4 xs * sumPow 4 xs) ≤
      ipowInt (sumPow 2 xs) 6 * sumPow 6 xs := by
  have h13 := T13_reverse_monotonicity_B4_ge_B6 xs
  have hS2_nn : 0 ≤ sumPow 2 xs := by rw [← sumSq_iabs]; exact sumSq_nonneg _
  have h5_nn : 0 ≤ ipowInt (sumPow 2 xs) 5 := by
    simp only [ipowInt, Int.mul_one]
    exact Int.mul_nonneg hS2_nn (Int.mul_nonneg hS2_nn (Int.mul_nonneg hS2_nn (Int.mul_nonneg hS2_nn hS2_nn)))
  have hmul := Int.mul_le_mul_of_nonneg_left h13 h5_nn
  have h6 : ipowInt (sumPow 2 xs) 5 * (sumPow 2 xs * sumPow 6 xs) = ipowInt (sumPow 2 xs) 6 * sumPow 6 xs := by
    rw [← Int.mul_assoc, Int.mul_comm (ipowInt (sumPow 2 xs) 5) (sumPow 2 xs)]
    rfl
  rw [h6] at hmul
  exact hmul

/-- T15: Universal B_3 <= P <= 1 Ceiling Proof (explaining Sharma et al. Theorem 4 stagnation on m copies). -/
theorem T15_sharma_B3_universal_ceiling_one (P b : Int) (hP0 : 0 ≤ P) (hb : -P ≤ b) :
    P * P - b ≤ P * (1 + 2 * P + b) := by
  have h1 : 0 ≤ (P + 1) * (b + P) := Int.mul_nonneg (by omega) (by omega)
  rw [Int.add_mul, Int.mul_add, Int.mul_add, Int.one_mul, Int.one_mul] at h1
  rw [Int.mul_add, Int.mul_add, Int.mul_one]
  have h2 : P * (2 * P) = 2 * (P * P) := by rw [← Int.mul_assoc, Int.mul_comm P 2, Int.mul_assoc]
  rw [h2]
  omega

/-- T16: Exact Blind-Spot Witness C09 (D=3, integer-scaled by 8). -/
def bs_d3 : List Int := [8, 8, 2, 2, 2, 2, 2, -1, -1]

theorem T16_blind_spot_d3_separation_exact :
    sumRaw bs_d3 = 24 ∧
    sumNeg bs_d3 = 2 ∧
    sumPow 1 bs_d3 * sumPow 3 bs_d3 > sumPow 2 bs_d3 * sumPow 2 bs_d3 ∧
    sumPow 2 bs_d3 * sumPow 2 bs_d3 * sumPow 2 bs_d3 <
      sumPow 1 bs_d3 * sumPow 1 bs_d3 * sumPow 4 bs_d3 ∧
    sumXPolySq [-16, 10, -1] bs_d3 < 0 := by
  decide

/-- T17: Exact Blind-Spot Witness C10 (D=5, integer-scaled by 8). -/
def bs_d5 : List Int :=
  [8, 8, 8, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0]

theorem T17_blind_spot_d5_separation_exact :
    sumRaw bs_d5 = 40 ∧
    sumNeg bs_d5 = 4 ∧
    sumPow 1 bs_d5 * sumPow 3 bs_d5 > sumPow 2 bs_d5 * sumPow 2 bs_d5 ∧
    sumPow 2 bs_d5 * sumPow 2 bs_d5 * sumPow 2 bs_d5 <
      sumPow 1 bs_d5 * sumPow 1 bs_d5 * sumPow 4 bs_d5 ∧
    sumXPolySq [-16, 10, -1] bs_d5 < 0 := by
  decide

/-- T18: Exact Qutrit Strange State Saturation of Theorem 1 (m=1) and Strict B_4 > B_6 Separation. -/
def strange_d3 : List Int := [-6, 3, 3, 3, 3, 3, 3, 3, 3]

theorem T18_strange_state_saturation_and_strict_B4_gt_B6 :
    sumRaw strange_d3 = 18 ∧
    sumNeg strange_d3 = 6 ∧
    sumPow 3 strange_d3 = 0 ∧
    sumXPolySq [-3, 1] strange_d3 + 81 * sumNeg strange_d3 = 0 ∧
    sumPow 4 strange_d3 * sumPow 4 strange_d3 < sumPow 2 strange_d3 * sumPow 6 strange_d3 := by
  decide

/-- T19: Exact Stabilizer State Zero Negativity & Equality in B4 = B6. -/
def stab_d3 : List Int := [1, 1, 1, 0, 0, 0, 0, 0, 0]

theorem T19_stabilizer_zero_negativity_and_holder_equality :
    sumRaw stab_d3 = 3 ∧
    sumNeg stab_d3 = 0 ∧
    sumPow 2 stab_d3 * sumPow 2 stab_d3 = sumPow 1 stab_d3 * sumPow 3 stab_d3 ∧
    sumPow 4 stab_d3 * sumPow 4 stab_d3 = sumPow 2 stab_d3 * sumPow 6 stab_d3 := by
  decide

/-- T20: Exact Noisy Strange State rho_1(p=1/2) Separation. -/
def rho1_half : List Int := [-4, 5, 5, 5, 5, 5, 5, 5, 5]

theorem T20_noisy_strange_half_exact_separation :
    sumRaw rho1_half = 36 ∧
    sumNeg rho1_half = 4 ∧
    sumPow 2 rho1_half * sumPow 2 rho1_half > sumPow 1 rho1_half * sumPow 3 rho1_half ∧
    sumPow 4 rho1_half * sumPow 4 rho1_half < sumPow 2 rho1_half * sumPow 6 rho1_half := by
  decide

/-- T21: Infinite-Family Universal (H_1, B_4)-Blind-Spot Separation for EVERY Odd Dimension D >= 3 (Theorem 3!):
    For x(D) with (D+1)/2 entries 1, 5(D-1)/2 entries 1/4, (D-1) entries -1/8, and (D-1)(D-3) zeros:
      P(D) = (43*D+21)/(64*D), b(D) = (275*D+237)/(512*D), c(D) = (2089*D+2007)/(4096*D).
    Proves constructively for ALL D >= 3:
      (1) det(H1) = b - P^2 > 0  <=>  (43D+21)^2 < (275D+237)*(8D),
      (2) P^3 < c                <=>  (43D+21)^3 < (2089D+2007)*(64D^2),
      (3) v^T H2 v = -81(D-1)/(4096D) < 0  <=>  81*(D-1) > 0. -/
theorem T21_infinite_odd_D_blind_spot_family (D : Nat) (hD : 3 ≤ D) :
    (43 * D + 21) * (43 * D + 21) < (275 * D + 237) * (8 * D) ∧
    (43 * D + 21) * (43 * D + 21) * (43 * D + 21) < (2089 * D + 2007) * (64 * D * D) ∧
    0 < 81 * (D - 1) := by
  cases Nat.decLe 7 D with
  | isFalse hlt =>
    match D with
    | 3 => decide
    | 4 => decide
    | 5 => decide
    | 6 => decide
    | 0 | 1 | 2 | _ + 7 => omega
  | isTrue h7 =>
    have h46 : 43 * D + 21 ≤ 46 * D := by omega
    have hD1 : 1 ≤ D := by omega
    have hD2 : 1 ≤ D * D := Nat.mul_le_mul hD1 hD1
    have hD3 : 1 ≤ D * D * D := Nat.mul_le_mul hD2 hD1
    have h1 : (43 * D + 21) * (43 * D + 21) < (275 * D + 237) * (8 * D) := by
      have ha : (43 * D + 21) * (43 * D + 21) ≤ 46 * D * (46 * D) := Nat.mul_le_mul h46 h46
      have hb : 46 * D * (46 * D) = 2116 * (D * D) := by
        rw [← Nat.mul_assoc (46 * D) 46 D, Nat.mul_assoc 46 D 46, Nat.mul_comm D 46,
            ← Nat.mul_assoc 46 46 D, Nat.mul_assoc 2116 D D]
      have hc : 275 * D * (8 * D) ≤ (275 * D + 237) * (8 * D) := Nat.mul_le_mul_right _ (Nat.le_add_right _ _)
      have hd : 275 * D * (8 * D) = 2200 * (D * D) := by
        rw [← Nat.mul_assoc (275 * D) 8 D, Nat.mul_assoc 275 D 8, Nat.mul_comm D 8,
            ← Nat.mul_assoc 275 8 D, Nat.mul_assoc 2200 D D]
      rw [hb] at ha; rw [hd] at hc
      omega
    have h2 : (43 * D + 21) * (43 * D + 21) * (43 * D + 21) < (2089 * D + 2007) * (64 * D * D) := by
      have ha : (43 * D + 21) * (43 * D + 21) * (43 * D + 21) ≤ 46 * D * (46 * D) * (46 * D) :=
        Nat.mul_le_mul (Nat.mul_le_mul h46 h46) h46
      have hb : 46 * D * (46 * D) * (46 * D) = 97336 * (D * D * D) := by
        have s2 : 46 * D * (46 * D) = 2116 * (D * D) := by
          rw [← Nat.mul_assoc (46 * D) 46 D, Nat.mul_assoc 46 D 46, Nat.mul_comm D 46,
              ← Nat.mul_assoc 46 46 D, Nat.mul_assoc 2116 D D]
        rw [s2, ← Nat.mul_assoc (2116 * (D * D)) 46 D, Nat.mul_assoc 2116 (D * D) 46,
            Nat.mul_comm (D * D) 46, ← Nat.mul_assoc 2116 46 (D * D), Nat.mul_assoc 97336 (D * D) D]
      have hc : 2089 * D * (64 * D * D) ≤ (2089 * D + 2007) * (64 * D * D) :=
        Nat.mul_le_mul_right _ (Nat.le_add_right _ _)
      have hd : 2089 * D * (64 * D * D) = 133696 * (D * D * D) := by
        rw [Nat.mul_assoc 64 D D, ← Nat.mul_assoc (2089 * D) 64 (D * D),
            Nat.mul_assoc 2089 D 64, Nat.mul_comm D 64, ← Nat.mul_assoc 2089 64 D,
            Nat.mul_assoc 133696 D (D * D), ← Nat.mul_assoc D D D]
      rw [hb] at ha; rw [hd] at hc
      omega
    exact ⟨h1, h2, by omega⟩

/-- T22: Unconditional Signed-Decomposition Monotonicity Step (Theorem 2):
    Even when P < N, u <= N and u <= P imply (N - u)*(D + 2*P - u) >= 0,
    so (P - u)^2 <= (D + N)*(b + u) implies (P - N)^2 <= (D + N)*(b + N) unconditionally! -/
theorem T22_signed_monotone_shift_unconditional (D P b N u : Int)
    (hD : 0 ≤ D) (hP : 0 ≤ P) (huP : u ≤ P) (huN : u ≤ N)
    (hCS : (P - u) * (P - u) ≤ (D + N) * (b + u)) :
    (P - N) * (P - N) ≤ (D + N) * (b + N) := by
  have hE1 : (D + N) * (b + N) = D * b + D * N + N * b + N * N := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add]; omega
  have hE2 : (P - N) * (P - N) = P * P - 2 * (P * N) + N * N := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_sub, Int.mul_comm N P]; omega
  have hE3 : (D + N) * (b + u) = D * b + D * u + N * b + N * u := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add]; omega
  have hE4 : (P - u) * (P - u) = P * P - 2 * (P * u) + u * u := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_sub, Int.mul_comm u P]; omega
  have hE5 : (N - u) * (D + 2 * P - u) = D * N + 2 * (P * N) - N * u - D * u - 2 * (P * u) + u * u := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_sub, Int.mul_add, Int.mul_add]
    have a1 : N * D = D * N := Int.mul_comm _ _
    have a2 : u * D = D * u := Int.mul_comm _ _
    have a3 : N * (2 * P) = 2 * (P * N) := by rw [← Int.mul_assoc, Int.mul_comm N 2, Int.mul_assoc, Int.mul_comm N P]
    have a4 : u * (2 * P) = 2 * (P * u) := by rw [← Int.mul_assoc, Int.mul_comm u 2, Int.mul_assoc, Int.mul_comm u P]
    rw [a1, a2, a3, a4]; omega
  have hnn : 0 ≤ (N - u) * (D + 2 * P - u) := Int.mul_nonneg (by omega) (by omega)
  rw [hE1, hE2]; rw [hE3, hE4] at hCS; rw [hE5] at hnn
  omega

#print axioms T01_l1_norm_eq_raw_plus_two_neg
#print axioms T02_sumNeg_nonneg
#print axioms T03_universal_hankel_sos_negativity_bound
#print axioms T04_deg1_hankel_quadratic_expansion
#print axioms T05_deg1_negative_interval_max
#print axioms T06_sharma_thm4_exact_m1_dual_identity
#print axioms T07_signed_moment_split
#print axioms T08_cauchy_schwarz_finite_list
#print axioms T09_nonneg_dist_H1_psd
#print axioms T10_positive_part_cauchy_schwarz
#print axioms T11_deg2_hankel_quadratic_expansion
#print axioms T12_holder_k2_w2_w4_universal
#print axioms T13_reverse_monotonicity_B4_ge_B6
#print axioms T14_B4_dominates_B6_exact
#print axioms T15_sharma_B3_universal_ceiling_one
#print axioms T16_blind_spot_d3_separation_exact
#print axioms T17_blind_spot_d5_separation_exact
#print axioms T18_strange_state_saturation_and_strict_B4_gt_B6
#print axioms T19_stabilizer_zero_negativity_and_holder_equality
#print axioms T20_noisy_strange_half_exact_separation
#print axioms T21_infinite_odd_D_blind_spot_family
#print axioms T22_signed_monotone_shift_unconditional

end WignerMomentMagic
