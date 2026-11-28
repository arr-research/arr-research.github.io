/-
HeisenbergDavenport.lean
Formalization of the algebraic, geometric, and extremal foundations for the
Large Davenport Constant of the finite Heisenberg group H_{p^3} = UT_3(F_p)
for every odd prime (indeed every odd modulus p = 2*k + 1 >= 3).

Author: Lluis Eriksson (ORCID: 0009-0006-7494-9040)
License: MIT
Constraints: 0 imports, 0 sorry, 0 grind, 0 native_decide, 0 Classical.choice.
-/

namespace HeisenbergDavenport

/-- Odd modulus `p = 2*k + 1` as an integer. For `k ≥ 1`, `p ≥ 3`. -/
def pInt (k : Nat) : Int := 2 * (k : Int) + 1

/-- Multiplicative inverse of `2` modulo `2*k + 1`: namely `k + 1`. -/
def inv2 (k : Nat) : Int := (k : Int) + 1

theorem pInt_pos (k : Nat) : 0 < pInt k := by
  unfold pInt
  omega

theorem two_mul_inv2_mod (k : Nat) : (2 * inv2 k) % pInt k = 1 % pInt k := by
  unfold inv2 pInt
  have h : (2 * ((k : Int) + 1)) = (2 * (k : Int) + 1) + 1 := by omega
  rw [h, Int.add_emod, Int.emod_self, Int.zero_add, Int.emod_emod]

/-- Elements of the Heisenberg group in exponential coordinates `(x, y, a)`.
    Arithmetic in `hmul` is kept exact over `Int`, with equivalence modulo `pInt k`
    expressed via `hmod` and `HEqMod`. -/
structure HElem where
  x : Int
  y : Int
  a : Int
  deriving DecidableEq, Repr

/-- Symplectic determinant on `Z^2`. -/
def det2 (u v : HElem) : Int := u.x * v.y - u.y * v.x

theorem det2_self (u : HElem) : det2 u u = 0 := by
  unfold det2
  rw [Int.mul_comm u.x u.y]
  omega

theorem det2_antisymm (u v : HElem) : det2 u v = -det2 v u := by
  unfold det2
  rw [Int.mul_comm u.x v.y, Int.mul_comm u.y v.x]
  omega

theorem det2_add_left (u v w : HElem) :
    det2 ⟨u.x + v.x, u.y + v.y, 0⟩ w = det2 u w + det2 v w := by
  unfold det2
  simp only [Int.add_mul]
  omega

theorem det2_add_right (u v w : HElem) :
    det2 u ⟨v.x + w.x, v.y + w.y, 0⟩ = det2 u v + det2 u w := by
  unfold det2
  simp only [Int.mul_add]
  omega

/-- Exponential group law: `(u, a) * (v, b) = (u + v, a + b + inv2 * det(u, v))`. -/
def hmul (k : Nat) (u v : HElem) : HElem :=
  ⟨u.x + v.x, u.y + v.y, u.a + v.a + inv2 k * det2 u v⟩

def hone : HElem := ⟨0, 0, 0⟩

def hinv (u : HElem) : HElem := ⟨-u.x, -u.y, -u.a⟩

def hmod (k : Nat) (u : HElem) : HElem :=
  ⟨u.x % pInt k, u.y % pInt k, u.a % pInt k⟩

def HEqMod (k : Nat) (u v : HElem) : Prop := hmod k u = hmod k v

def hprod (k : Nat) : List HElem → HElem
  | [] => hone
  | g :: gs => hmul k g (hprod k gs)

def hpow (k : Nat) (g : HElem) : Nat → HElem
  | 0 => hone
  | n + 1 => hmul k g (hpow k g n)

/-! ## 1. Exact Exponential Group Law & Heisenberg Axioms -/

theorem hmul_one_left (k : Nat) (u : HElem) : hmul k hone u = u := by
  unfold hmul hone det2
  cases u
  simp

theorem hmul_one_right (k : Nat) (u : HElem) : hmul k u hone = u := by
  unfold hmul hone det2
  cases u
  simp

theorem hmul_assoc (k : Nat) (u v w : HElem) :
    hmul k (hmul k u v) w = hmul k u (hmul k v w) := by
  unfold hmul det2
  simp only [HElem.mk.injEq, Int.add_mul, Int.mul_add, Int.mul_sub]
  refine ⟨by omega, by omega, by omega⟩

theorem hmul_inv_left (k : Nat) (u : HElem) : hmul k (hinv u) u = hone := by
  unfold hmul hinv hone det2
  simp only [Int.neg_mul, HElem.mk.injEq]
  refine ⟨by omega, by omega, ?_⟩
  rw [Int.mul_comm u.y u.x]
  omega

theorem hmul_inv_right (k : Nat) (u : HElem) : hmul k u (hinv u) = hone := by
  unfold hmul hinv hone det2
  simp only [Int.mul_neg, HElem.mk.injEq]
  refine ⟨by omega, by omega, ?_⟩
  rw [Int.mul_comm u.y u.x]
  omega

theorem hpow_formula (k : Nat) (g : HElem) (n : Nat) :
    hpow k g n = ⟨(n : Int) * g.x, (n : Int) * g.y, (n : Int) * g.a⟩ := by
  induction n with
  | zero =>
    unfold hpow hone
    simp
  | succ n ih =>
    unfold hpow
    rw [ih]
    unfold hmul det2
    have hdet : g.x * ((n : Int) * g.y) - g.y * ((n : Int) * g.x) = 0 := by
      have h1 : g.x * ((n : Int) * g.y) = (n : Int) * (g.x * g.y) := by
        rw [← Int.mul_assoc, Int.mul_comm g.x (n : Int), Int.mul_assoc]
      have h2 : g.y * ((n : Int) * g.x) = (n : Int) * (g.x * g.y) := by
        rw [← Int.mul_assoc, Int.mul_comm g.y (n : Int), Int.mul_assoc, Int.mul_comm g.y g.x]
      rw [h1, h2]
      omega
    rw [hdet]
    have hn : ((n + 1 : Nat) : Int) = (n : Int) + 1 := by omega
    simp only [hn, Int.add_mul, Int.one_mul, HElem.mk.injEq]
    refine ⟨by omega, by omega, by omega⟩

theorem hpow_p_eq_one (k : Nat) (g : HElem) :
    HEqMod k (hpow k g (2 * k + 1)) hone := by
  rw [hpow_formula]
  unfold HEqMod hmod hone pInt
  have hnat : ((2 * k + 1 : Nat) : Int) = 2 * (k : Int) + 1 := by omega
  simp only [hnat, Int.mul_emod_right, Int.zero_emod]

theorem commutator_eq_det (k : Nat) (u v : HElem) :
    HEqMod k (hmul k (hmul k (hinv u) (hinv v)) (hmul k u v)) ⟨0, 0, det2 u v⟩ := by
  have hexact :
      hmul k (hmul k (hinv u) (hinv v)) (hmul k u v) = ⟨0, 0, 2 * inv2 k * det2 u v⟩ := by
    unfold hmul hinv det2
    have hdet1 : (-u.x) * (-v.y) - (-u.y) * (-v.x) = u.x * v.y - u.y * v.x := by
      simp [Int.neg_mul, Int.mul_neg]
    have hdet2 : (-u.x + -v.x) * (u.y + v.y) - (-u.y + -v.y) * (u.x + v.x) = 0 := by
      have hx : -u.x + -v.x = -(u.x + v.x) := by omega
      have hy : -u.y + -v.y = -(u.y + v.y) := by omega
      rw [hx, hy]
      simp only [Int.neg_mul]
      rw [Int.mul_comm (u.x + v.x) (u.y + v.y)]
      omega
    rw [hdet1, hdet2]
    simp only [HElem.mk.injEq]
    refine ⟨by omega, by omega, ?_⟩
    have hadd :
        -u.a + -v.a + inv2 k * (u.x * v.y - u.y * v.x) +
          (u.a + v.a + inv2 k * (u.x * v.y - u.y * v.x)) + inv2 k * 0 =
        inv2 k * (u.x * v.y - u.y * v.x) + inv2 k * (u.x * v.y - u.y * v.x) := by omega
    rw [hadd]
    have h2 : ∀ z : Int, 2 * inv2 k * z = inv2 k * z + inv2 k * z := by
      intro z
      rw [Int.mul_assoc, Int.two_mul]
    rw [h2]
  rw [hexact]
  unfold HEqMod hmod
  simp only [HElem.mk.injEq, true_and]
  rw [Int.mul_emod, two_mul_inv2_mod, ← Int.mul_emod, Int.one_mul]

/-! ## 2. Commutator-Area Product Identity & Lemma 1 Contraction Law -/

def vecXSum : List HElem → Int
  | [] => 0
  | g :: gs => g.x + vecXSum gs

def vecYSum : List HElem → Int
  | [] => 0
  | g :: gs => g.y + vecYSum gs

def centralSum : List HElem → Int
  | [] => 0
  | g :: gs => g.a + centralSum gs

/-- Alternating determinant (signed area) functional `∑_{i < j} det(g_i, g_j)`. -/
def areaSum : List HElem → Int
  | [] => 0
  | g :: gs => areaSum gs + (g.x * vecYSum gs - g.y * vecXSum gs)

theorem vecXSum_append (l1 l2 : List HElem) :
    vecXSum (l1 ++ l2) = vecXSum l1 + vecXSum l2 := by
  induction l1 with
  | nil => simp [vecXSum]
  | cons g gs ih => simp [vecXSum, ih, Int.add_assoc]

theorem vecYSum_append (l1 l2 : List HElem) :
    vecYSum (l1 ++ l2) = vecYSum l1 + vecYSum l2 := by
  induction l1 with
  | nil => simp [vecYSum]
  | cons g gs ih => simp [vecYSum, ih, Int.add_assoc]

theorem centralSum_append (l1 l2 : List HElem) :
    centralSum (l1 ++ l2) = centralSum l1 + centralSum l2 := by
  induction l1 with
  | nil => simp [centralSum]
  | cons g gs ih => simp [centralSum, ih, Int.add_assoc]

theorem areaSum_append (l1 l2 : List HElem) :
    areaSum (l1 ++ l2) =
      areaSum l1 + areaSum l2 + (vecXSum l1 * vecYSum l2 - vecYSum l1 * vecXSum l2) := by
  induction l1 with
  | nil => simp [areaSum, vecXSum, vecYSum]
  | cons g gs ih =>
    simp only [List.cons_append, areaSum, vecXSum, vecYSum, vecXSum_append, vecYSum_append, ih]
    simp only [Int.add_mul, Int.mul_add]
    omega

/-- Exact commutator-area product formula for arbitrary finite words in `H_{p^3}`. -/
theorem hprod_eq_area (k : Nat) (l : List HElem) :
    hprod k l = ⟨vecXSum l, vecYSum l, centralSum l + inv2 k * areaSum l⟩ := by
  induction l with
  | nil =>
    simp [hprod, hone, vecXSum, vecYSum, centralSum, areaSum]
  | cons g gs ih =>
    simp only [hprod, ih]
    unfold hmul det2
    simp only [vecXSum, vecYSum, centralSum, areaSum, Int.mul_add, HElem.mk.injEq, true_and]
    omega

theorem hprod_append (k : Nat) (l1 l2 : List HElem) :
    hprod k (l1 ++ l2) = hmul k (hprod k l1) (hprod k l2) := by
  rw [hprod_eq_area, hprod_eq_area, hprod_eq_area]
  unfold hmul det2
  rw [vecXSum_append, vecYSum_append, centralSum_append, areaSum_append]
  simp only [Int.mul_add, HElem.mk.injEq, true_and]
  omega

/-- Algebraic core of Lemma 1 (Order-Value Growth):
    Replacing `(u + w)` at any position in an ordering by `(u, w)` vs `(w, u)` shifts
    the signed area `areaSum` by `+det(u, w)` vs `-det(u, w)` (leaving all cross-terms
    with `pre` and `post` invariant). -/
theorem areaSum_contract_pair (pre post : List HElem) (u w : HElem) :
    areaSum (pre ++ [u, w] ++ post) =
        areaSum (pre ++ [⟨u.x + w.x, u.y + w.y, 0⟩] ++ post) + det2 u w ∧
    areaSum (pre ++ [w, u] ++ post) =
        areaSum (pre ++ [⟨u.x + w.x, u.y + w.y, 0⟩] ++ post) - det2 u w := by
  let uw : HElem := ⟨u.x + w.x, u.y + w.y, 0⟩
  have hL : areaSum ([u, w] ++ post) = areaSum ([uw] ++ post) + det2 u w := by
    simp only [uw, List.cons_append, List.nil_append, areaSum, vecXSum, vecYSum, det2]
    simp only [Int.add_mul, Int.mul_add]
    omega
  have hR : areaSum ([w, u] ++ post) = areaSum ([uw] ++ post) - det2 u w := by
    simp only [uw, List.cons_append, List.nil_append, areaSum, vecXSum, vecYSum, det2]
    simp only [Int.add_mul, Int.mul_add]
    rw [Int.mul_comm w.x u.y, Int.mul_comm w.y u.x]
    omega
  have hx1 : vecXSum ([u, w] ++ post) = vecXSum ([uw] ++ post) := by
    simp [uw, vecXSum, Int.add_assoc]
  have hy1 : vecYSum ([u, w] ++ post) = vecYSum ([uw] ++ post) := by
    simp [uw, vecYSum, Int.add_assoc]
  have hx2 : vecXSum ([w, u] ++ post) = vecXSum ([uw] ++ post) := by
    simp [uw, vecXSum]; omega
  have hy2 : vecYSum ([w, u] ++ post) = vecYSum ([uw] ++ post) := by
    simp [uw, vecYSum]; omega
  constructor
  · change areaSum (pre ++ [u, w] ++ post) = areaSum (pre ++ [uw] ++ post) + det2 u w
    rw [List.append_assoc pre [u, w] post, areaSum_append pre ([u, w] ++ post)]
    rw [List.append_assoc pre [uw] post, areaSum_append pre ([uw] ++ post)]
    rw [hL, hx1, hy1]
    omega
  · change areaSum (pre ++ [w, u] ++ post) = areaSum (pre ++ [uw] ++ post) - det2 u w
    rw [List.append_assoc pre [w, u] post, areaSum_append pre ([w, u] ++ post)]
    rw [List.append_assoc pre [uw] post, areaSum_append pre ([uw] ++ post)]
    rw [hR, hx2, hy2]
    omega

/-! ## 3. Arithmetic Pairing & Constructive Three-Set Pigeonhole -/

/-- Exact pairing sum for complementary non-zero-sum pieces summing to `0 (mod p)`:
    `((-s1) % p) + ((-s2) % p) = p`. -/
theorem arithmetic_pairing_complement (k : Nat) (s1 s2 : Int)
    (hsum : (s1 + s2) % pInt k = 0) (hne : (-s1) % pInt k ≠ 0) :
    ((-s1) % pInt k) + ((-s2) % pInt k) = pInt k := by
  have hp : 0 < pInt k := pInt_pos k
  have h1 : 0 ≤ (-s1) % pInt k ∧ (-s1) % pInt k < pInt k :=
    ⟨Int.emod_nonneg (-s1) (Int.ne_of_gt hp), Int.emod_lt_of_pos (-s1) hp⟩
  have h2 : 0 ≤ (-s2) % pInt k ∧ (-s2) % pInt k < pInt k :=
    ⟨Int.emod_nonneg (-s2) (Int.ne_of_gt hp), Int.emod_lt_of_pos (-s2) hp⟩
  have hmod : ((-s1) % pInt k + (-s2) % pInt k) % pInt k = 0 := by
    rw [← Int.add_emod]
    have hneg : -s1 + -s2 = -(s1 + s2) := by omega
    rw [hneg, Int.emod_eq_zero_of_dvd]
    exact Int.dvd_neg.mpr (Int.dvd_of_emod_eq_zero hsum)
  have hdvd : pInt k ∣ ((-s1) % pInt k + (-s2) % pInt k) := Int.dvd_of_emod_eq_zero hmod
  rcases hdvd with ⟨q, hq⟩
  have hq_pos : 0 < q := by
    by_cases hle : q ≤ 0
    · have hm : pInt k * q ≤ pInt k * 0 := Int.mul_le_mul_of_nonneg_left hle (Int.le_of_lt hp)
      omega
    · omega
  have hq_lt2 : q < 2 := by
    by_cases hge : 2 ≤ q
    · have hm : pInt k * 2 ≤ pInt k * q := Int.mul_le_mul_of_nonneg_left hge (Int.le_of_lt hp)
      omega
    · omega
  have hq1 : q = 1 := by omega
  rw [hq1, Int.mul_one] at hq
  exact hq

/-- Constructive boolean counting over `0 .. n-1`: if three subsets of `{0, ..., n-1}`
    have total indicator sum `> 2 * n`, then some index lies in all three subsets. -/
def countPred (P : Nat → Bool) : Nat → Nat
  | 0 => 0
  | n + 1 => countPred P n + if P n then 1 else 0

theorem three_set_pigeonhole (P Q R : Nat → Bool) :
    ∀ n : Nat, 2 * n < countPred P n + countPred Q n + countPred R n →
      ∃ x : Nat, x < n ∧ P x = true ∧ Q x = true ∧ R x = true
  | 0, h => by simp [countPred] at h
  | n + 1, h => by
    have h_step : countPred P (n + 1) + countPred Q (n + 1) + countPred R (n + 1) =
        (countPred P n + countPred Q n + countPred R n) +
        ((if P n then 1 else 0) + (if Q n then 1 else 0) + (if R n then 1 else 0)) := by
      simp [countPred]; omega
    by_cases htop : P n = true ∧ Q n = true ∧ R n = true
    · exact ⟨n, by omega, htop⟩
    · have hind : (if P n then 1 else 0) + (if Q n then 1 else 0) + (if R n then 1 else 0) ≤ 2 := by
        cases hP : P n <;> cases hQ : Q n <;> cases hR : R n <;> simp_all
      have hrec : 2 * n < countPred P n + countPred Q n + countPred R n := by omega
      rcases three_set_pigeonhole P Q R n hrec with ⟨x, hxlt, hx⟩
      exact ⟨x, by omega, hx⟩

/-! ## 4. Uniform All-Prime Product-One Proofs for S^(1), S^(2) and Short-Subsequence Exclusion for T_eta, T_s -/

def hxElem : HElem := ⟨1, 0, 0⟩
def hyElem : HElem := ⟨0, 1, 0⟩
def hzElem : HElem := ⟨0, 0, 1⟩
def hxzElem : HElem := ⟨1, 0, 1⟩
def hyzElem : HElem := ⟨0, 1, 1⟩
def hx2zElem : HElem := ⟨2, 0, 1⟩

theorem hprod_replicate (k : Nat) (g : HElem) (n : Nat) :
    hprod k (List.replicate n g) = hpow k g n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [List.replicate_succ, hprod, hpow, ih]

/-- Explicit product-one ordering of `S^(1)` of length `3p - 1 = 6k + 2` for every odd modulus `p = 2k + 1` (`k ≥ 1`). -/
def s1Word (k : Nat) : List HElem :=
  List.replicate (2 * k) hxElem ++ [hyElem] ++ [hxzElem] ++
  List.replicate (2 * k - 1) hyElem ++ [hyzElem] ++ List.replicate (2 * k) hzElem

theorem s1Word_length (k : Nat) (hk : 1 ≤ k) :
    (s1Word k).length = 3 * (2 * k + 1) - 1 := by
  unfold s1Word
  simp only [List.length_append, List.length_replicate, List.length_cons, List.length_nil]
  omega

theorem s1Word_prod_one (k : Nat) (hk : 1 ≤ k) :
    HEqMod k (hprod k (s1Word k)) hone := by
  unfold s1Word
  simp only [hprod_append, hprod_replicate, hpow_formula, hprod, hmul_one_right]
  have h2k : ((2 * k : Nat) : Int) = 2 * (k : Int) := by omega
  have h2km1 : ((2 * k - 1 : Nat) : Int) = 2 * (k : Int) - 1 := by omega
  unfold hmul det2 hxElem hyElem hxzElem hyzElem hzElem
  simp only [h2k, h2km1, Int.mul_zero, Int.mul_one, Int.add_zero, Int.zero_add]
  unfold HEqMod hmod hone
  simp only [HElem.mk.injEq]
  have hx_eq : 2 * (k : Int) + 1 = pInt k := by unfold pInt; omega
  have hy_eq : 1 + (2 * (k : Int) - 1) + 1 = pInt k := by unfold pInt; omega
  have ha_eq :
      inv2 k * (2 * (k : Int)) + 1 + inv2 k * (0 - 1) +
        inv2 k * ((2 * (k : Int) + 1) * (2 * (k : Int) - 1)) + 1 +
        inv2 k * (2 * (k : Int) + 1) + 2 * (k : Int) =
      pInt k * (pInt k * inv2 k) := by
    let kk : Int := (k : Int) * (k : Int)
    have hpoly :
        (2 * (k : Int) + 1) * (2 * (k : Int) - 1) = 4 * kk - 1 := by
      dsimp [kk]
      simp only [Int.add_mul, Int.mul_sub, Int.one_mul, Int.mul_one]
      have hcomm : 2 * (k : Int) * (2 * (k : Int)) = 4 * ((k : Int) * (k : Int)) := by
        rw [Int.mul_assoc 2 (k : Int), Int.mul_comm (k : Int) (2 * (k : Int))]
        rw [Int.mul_assoc 2 (k : Int), ← Int.mul_assoc 2 2]
        omega
      rw [hcomm]; omega
    have hcoeff :
        2 * (k : Int) + (0 - 1) + (2 * (k : Int) + 1) * (2 * (k : Int) - 1) + (2 * (k : Int) + 1) =
        (4 * kk + 4 * (k : Int) + 1) - 2 := by
      rw [hpoly]; omega
    have hsq : pInt k * pInt k = 4 * kk + 4 * (k : Int) + 1 := by
      unfold pInt; dsimp [kk]
      simp only [Int.add_mul, Int.mul_add, Int.one_mul, Int.mul_one]
      have hcomm : 2 * (k : Int) * (2 * (k : Int)) = 4 * ((k : Int) * (k : Int)) := by
        rw [Int.mul_assoc 2 (k : Int), Int.mul_comm (k : Int) (2 * (k : Int))]
        rw [Int.mul_assoc 2 (k : Int), ← Int.mul_assoc 2 2]
        omega
      rw [hcomm]; omega
    have hsum_inv :
        inv2 k * (2 * (k : Int)) + 1 + inv2 k * (0 - 1) +
          inv2 k * ((2 * (k : Int) + 1) * (2 * (k : Int) - 1)) + 1 +
          inv2 k * (2 * (k : Int) + 1) + 2 * (k : Int) =
        inv2 k * (2 * (k : Int) + (0 - 1) + (2 * (k : Int) + 1) * (2 * (k : Int) - 1) + (2 * (k : Int) + 1)) +
          (2 * (k : Int) + 2) := by
      simp only [Int.mul_add]; omega
    rw [hsum_inv, hcoeff, Int.mul_sub]
    have h2i : inv2 k * 2 = 2 * (k : Int) + 2 := by unfold inv2; omega
    rw [h2i, ← hsq, Int.mul_comm (inv2 k) (pInt k * pInt k), Int.mul_assoc]
    omega
  refine ⟨?_, ?_, ?_⟩
  · simpa [Int.add_assoc] using (by rw [hx_eq, Int.emod_self, Int.zero_emod] : (2 * (k : Int) + 1) % pInt k = 0 % pInt k)
  · simpa [Int.add_assoc] using (by rw [hy_eq, Int.emod_self, Int.zero_emod] : (1 + (2 * (k : Int) - 1) + 1) % pInt k = 0 % pInt k)
  · simpa [Int.add_assoc] using (by rw [ha_eq, Int.mul_emod_right, Int.zero_emod] : (inv2 k * (2 * (k : Int)) + 1 + inv2 k * (0 - 1) + inv2 k * ((2 * (k : Int) + 1) * (2 * (k : Int) - 1)) + 1 + inv2 k * (2 * (k : Int) + 1) + 2 * (k : Int)) % pInt k = 0 % pInt k)

/-- Explicit product-one ordering of `S^(2)` of length `3p - 1 = 6k + 2` for every odd modulus `p = 2k + 1` (`k ≥ 1`). -/
def s2Word (k : Nat) : List HElem :=
  [hyElem] ++ List.replicate (2 * k) hxzElem ++ [hx2zElem] ++
  List.replicate (2 * k - 1) hyElem ++ [hyzElem] ++ List.replicate (2 * k) hxElem

theorem s2Word_length (k : Nat) (hk : 1 ≤ k) :
    (s2Word k).length = 3 * (2 * k + 1) - 1 := by
  unfold s2Word
  simp only [List.length_append, List.length_replicate, List.length_cons, List.length_nil]
  omega

theorem s2Word_prod_one (k : Nat) (hk : 1 ≤ k) :
    HEqMod k (hprod k (s2Word k)) hone := by
  unfold s2Word
  simp only [hprod_append, hprod_replicate, hpow_formula, hprod, hmul_one_right]
  have h2k : ((2 * k : Nat) : Int) = 2 * (k : Int) := by omega
  have h2km1 : ((2 * k - 1 : Nat) : Int) = 2 * (k : Int) - 1 := by omega
  unfold hmul det2 hxElem hyElem hxzElem hyzElem hx2zElem
  simp only [h2k, h2km1, Int.mul_zero, Int.mul_one, Int.add_zero, Int.zero_add]
  unfold HEqMod hmod hone
  simp only [HElem.mk.injEq]
  have hx_eq : 2 * (k : Int) + 2 + 2 * (k : Int) = pInt k * 2 := by unfold pInt; omega
  have hy_eq : 1 + (2 * (k : Int) - 1) + 1 = pInt k := by unfold pInt; omega
  have ha_eq :
      2 * (k : Int) + inv2 k * (0 - 1 * (2 * (k : Int))) + 1 + inv2 k * (0 - 1 * 2) +
        inv2 k * ((2 * (k : Int) + 2) * (2 * (k : Int) - 1)) + 1 +
        inv2 k * (2 * (k : Int) + 2) +
        inv2 k * (0 - (1 + (2 * (k : Int) - 1) + 1) * (2 * (k : Int))) = 0 := by
    let kk : Int := (k : Int) * (k : Int)
    have h4k : 2 * (k : Int) * (2 * (k : Int)) = 4 * kk := by
      dsimp [kk]
      rw [Int.mul_assoc 2 (k : Int), Int.mul_comm (k : Int) (2 * (k : Int))]
      rw [Int.mul_assoc 2 (k : Int), ← Int.mul_assoc 2 2]
      omega
    have hp1 : (2 * (k : Int) + 2) * (2 * (k : Int) - 1) = 4 * kk + 2 * (k : Int) - 2 := by
      simp only [Int.add_mul, Int.mul_sub]
      rw [h4k]; omega
    have hp2 : (1 + (2 * (k : Int) - 1) + 1) * (2 * (k : Int)) = 4 * kk + 2 * (k : Int) := by
      have hy1 : 1 + (2 * (k : Int) - 1) + 1 = 2 * (k : Int) + 1 := by omega
      rw [hy1, Int.add_mul, Int.one_mul, h4k]
    have hcoeff :
        (0 - 1 * (2 * (k : Int))) + (0 - 1 * 2) + (2 * (k : Int) + 2) * (2 * (k : Int) - 1) +
          (2 * (k : Int) + 2) + (0 - (1 + (2 * (k : Int) - 1) + 1) * (2 * (k : Int))) = -2 := by
      rw [hp1, hp2]; omega
    have hfactor :
        2 * (k : Int) + inv2 k * (0 - 1 * (2 * (k : Int))) + 1 + inv2 k * (0 - 1 * 2) +
          inv2 k * ((2 * (k : Int) + 2) * (2 * (k : Int) - 1)) + 1 +
          inv2 k * (2 * (k : Int) + 2) +
          inv2 k * (0 - (1 + (2 * (k : Int) - 1) + 1) * (2 * (k : Int))) =
        inv2 k * ((0 - 1 * (2 * (k : Int))) + (0 - 1 * 2) +
          (2 * (k : Int) + 2) * (2 * (k : Int) - 1) + (2 * (k : Int) + 2) +
          (0 - (1 + (2 * (k : Int) - 1) + 1) * (2 * (k : Int)))) + (2 * (k : Int) + 2) := by
      simp only [Int.mul_add]; omega
    rw [hfactor, hcoeff]
    unfold inv2; omega
  refine ⟨?_, ?_, ?_⟩
  · simpa [Int.add_assoc] using (by rw [hx_eq, Int.mul_emod_right, Int.zero_emod] : (2 * (k : Int) + 2 + 2 * (k : Int)) % pInt k = 0 % pInt k)
  · simpa [Int.add_assoc] using (by rw [hy_eq, Int.emod_self, Int.zero_emod] : (1 + (2 * (k : Int) - 1) + 1) % pInt k = 0 % pInt k)
  · simpa [Int.add_assoc] using (by rw [ha_eq, Int.zero_emod] : (2 * (k : Int) + inv2 k * (0 - 1 * (2 * (k : Int))) + 1 + inv2 k * (0 - 1 * 2) + inv2 k * ((2 * (k : Int) + 2) * (2 * (k : Int) - 1)) + 1 + inv2 k * (2 * (k : Int) + 2) + inv2 k * (0 - (1 + (2 * (k : Int) - 1) + 1) * (2 * (k : Int)))) % pInt k = 0 % pInt k)

/-- Helper for `Nat`: if `a ≤ p` and `a % p = 0` with `p ≥ 1`, then `a = 0 ∨ a = p`. -/
theorem nat_mod_zero_le (a p : Nat) (hp : 1 ≤ p) (hle : a ≤ p) (hmod : a % p = 0) :
    a = 0 ∨ a = p := by
  rcases Nat.dvd_of_mod_eq_zero hmod with ⟨q, hq⟩
  by_cases hq2 : 2 ≤ q
  · have hm : p * 2 ≤ p * q := Nat.mul_le_mul_left p hq2
    omega
  · have : q = 0 ∨ q = 1 := by omega
    rcases this with rfl | rfl
    · left; omega
    · right; omega

/-- Helper for `Nat`: if `1 ≤ a` and `a % p = 0`, then `p ≤ a`. -/
theorem nat_mod_zero_ge (a p : Nat) (hpos : 1 ≤ a) (hmod : a % p = 0) : p ≤ a := by
  rcases Nat.dvd_of_mod_eq_zero hmod with ⟨q, hq⟩
  rcases Nat.eq_zero_or_pos q with rfl | hq_pos
  · omega
  · have hm : p * 1 ≤ p * q := Nat.mul_le_mul_left p hq_pos
    omega

/-- Arithmetic exclusion core for `T_eta` and `T_s` (Theorem 3) valid for ALL odd moduli `p ≥ 3`.
    Any nonempty subsequence `U` of `T_eta` of length `≤ p` with zero abelian sum lies
    on a single direction line (`areaSum = 0` in every ordering) and has nonzero central
    coordinate `a2 + b2 + c2 + d (mod p)`. -/
theorem t_eta_central_nonzero (p a1 a2 b1 b2 c1 c2 d : Nat)
    (hp : 3 ≤ p)
    (ha1 : a1 ≤ p - 1) (ha2 : a2 ≤ p - 1)
    (hb1 : b1 ≤ p - 1) (hb2 : b2 ≤ p - 1)
    (hc1 : c1 ≤ p - 1) (hc2 : c2 ≤ p - 1)
    (hd : d ≤ p - 1)
    (hlen_pos : 1 ≤ a1 + a2 + b1 + b2 + c1 + c2 + d)
    (hlen_le : a1 + a2 + b1 + b2 + c1 + c2 + d ≤ p)
    (hx0 : (a1 + a2 + c1 + c2) % p = 0)
    (hy0 : (b1 + b2 + c1 + c2) % p = 0) :
    (a2 + b2 + c2 + d) % p ≠ 0 := by
  by_cases hc0 : c1 + c2 = 0
  · have hx' : (a1 + a2) % p = 0 := by
      have hsum : a1 + a2 + c1 + c2 = a1 + a2 := by omega
      rwa [← hsum]
    have hy' : (b1 + b2) % p = 0 := by
      have hsum : b1 + b2 + c1 + c2 = b1 + b2 := by omega
      rwa [← hsum]
    have ha0 := nat_mod_zero_le (a1 + a2) p (by omega) (by omega) hx'
    have hb0 := nat_mod_zero_le (b1 + b2) p (by omega) (by omega) hy'
    rcases ha0 with ha0 | hap <;> rcases hb0 with hb0 | hbp
    · have hval : a2 + b2 + c2 + d = d := by omega
      rw [hval, Nat.mod_eq_of_lt (by omega)]
      omega
    · have hval : a2 + b2 + c2 + d = b2 := by omega
      rw [hval, Nat.mod_eq_of_lt (by omega)]
      omega
    · have hval : a2 + b2 + c2 + d = a2 := by omega
      rw [hval, Nat.mod_eq_of_lt (by omega)]
      omega
    · omega
  · by_cases hcp : c1 + c2 = p
    · have hval : a2 + b2 + c2 + d = c2 := by omega
      rw [hval, Nat.mod_eq_of_lt (by omega)]
      omega
    · have hge1 := nat_mod_zero_ge (a1 + a2 + c1 + c2) p (by omega) hx0
      have hge2 := nat_mod_zero_ge (b1 + b2 + c1 + c2) p (by omega) hy0
      omega

end HeisenbergDavenport
