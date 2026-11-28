/-
  FiniteFreeRootGapsCore.lean
  Constructive Lean 4.36.0 formalization (zero sorry, zero grind, zero custom axioms,
  zero external dependencies) of the exact algebraic and inequality core of:
  "Finite Free Root-Gap Dynamics: Universal Marcel Riesz Monotonicity, Sharp Degree-3-to-4
   Euclidean and Hyperbolic Pythagorean Transitions, and Exact Heat-Flow Compression"

  All rational identities and inequalities are formulated in exact denominator-cleared
  integer arithmetic (Z / N), which is equivalent over Q by clearing positive denominators
  and extends to R by continuity.
-/

namespace FiniteFreeRootGaps

-- ============================================================================
-- Section 1: Elementary Int Helpers
-- ============================================================================

private theorem int_sq_nonneg (x : Int) : 0 ≤ x * x := by
  rcases Int.le_total 0 x with hx | hx
  · exact Int.mul_nonneg hx hx
  · have hnx : 0 ≤ -x := by omega
    have h : 0 ≤ (-x) * (-x) := Int.mul_nonneg hnx hnx
    simpa [Int.neg_mul_neg] using h

private theorem int_mul_le_mul_of_nonneg {a b c d : Int}
    (ha : 0 ≤ a) (hc : 0 ≤ c) (hab : a ≤ b) (hcd : c ≤ d) : a * c ≤ b * d := by
  have h1 : a * c ≤ b * c := Int.mul_le_mul_of_nonneg_right hab hc
  have hb : 0 ≤ b := Int.le_trans ha hab
  have h2 : b * c ≤ b * d := Int.mul_le_mul_of_nonneg_left hcd hb
  exact Int.le_trans h1 h2

private theorem int_le_of_sq_le_sq {x y : Int} (hx : 0 ≤ x) (hy : 0 ≤ y)
    (hsq : x * x ≤ y * y) : x ≤ y := by
  by_cases h : x ≤ y
  · exact h
  · have hpos1 : 0 < x - y := by omega
    have hpos2 : 0 < x + y := by omega
    have hprod : 0 < (x - y) * (x + y) := Int.mul_pos hpos1 hpos2
    have hid : (x - y) * (x + y) = x * x - y * y := by
      rw [Int.sub_mul, Int.mul_add, Int.mul_add, Int.mul_comm y x]
      omega
    rw [hid] at hprod
    omega

-- ============================================================================
-- Section 2: Degree-2 and Degree-3 Additive Pythagorean Laws (Theorem 2)
-- ============================================================================

/-- Theorem 2(a): Exact degree-2 finite free additive Pythagorean identity.
    Clearing the factor 1/2 in e2(p ⊞_2 q) = e2 + f2 + (1/2)*e1*f1:
    2 * disc(p ⊞_2 q) = 2 * disc(p) + 2 * disc(q). -/
theorem degree2_additive_pythagorean (e1 e2 f1 f2 : Int) :
    2 * ((e1 + f1) * (e1 + f1)) - 4 * (2 * e2 + 2 * f2 + e1 * f1) =
    2 * (e1 * e1 - 4 * e2) + 2 * (f1 * f1 - 4 * f2) := by
  have hsq : (e1 + f1) * (e1 + f1) = e1 * e1 + 2 * (e1 * f1) + f1 * f1 := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add, Int.mul_comm f1 e1]; omega
  rw [hsq]
  omega

/-- Theorem 2(b) Lemma 1: Homogeneous Viète trigonometric-algebraic identity for cubics.
    Setting s = p / q and clearing q^6 gives:
    q^6 - p^2 * (3*q^2 - 4*p^2)^2 = (q^2 - p^2) * (q^2 - 4*p^2)^2. -/
theorem cubic_viete_factorization (p q : Int) :
    let P := p * p
    let Q := q * q
    Q * Q * Q - P * ((3 * Q - 4 * P) * (3 * Q - 4 * P)) =
    (Q - P) * ((Q - 4 * P) * (Q - 4 * P)) := by
  simp only
  let P := p * p
  let Q := q * q
  change Q * Q * Q - P * ((3 * Q - 4 * P) * (3 * Q - 4 * P)) =
         (Q - P) * ((Q - 4 * P) * (Q - 4 * P))
  have hl : (3 * Q - 4 * P) * (3 * Q - 4 * P) =
            9 * (Q * Q) - 24 * (P * Q) + 16 * (P * P) := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_sub]
    have e1 : 3 * Q * (3 * Q) = 9 * (Q * Q) := by
      have : 3 * Q * (3 * Q) = (3 * 3) * (Q * Q) := by ac_rfl
      rw [this]; omega
    have e2 : 3 * Q * (4 * P) = 12 * (P * Q) := by
      have : 3 * Q * (4 * P) = (3 * 4) * (P * Q) := by ac_rfl
      rw [this]; omega
    have e3 : 4 * P * (3 * Q) = 12 * (P * Q) := by
      have : 4 * P * (3 * Q) = (4 * 3) * (P * Q) := by ac_rfl
      rw [this]; omega
    have e4 : 4 * P * (4 * P) = 16 * (P * P) := by
      have : 4 * P * (4 * P) = (4 * 4) * (P * P) := by ac_rfl
      rw [this]; omega
    rw [e1, e2, e3, e4]; omega
  have hr : (Q - 4 * P) * (Q - 4 * P) =
            Q * Q - 8 * (P * Q) + 16 * (P * P) := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_sub]
    have e2 : Q * (4 * P) = 4 * (P * Q) := by ac_rfl
    have e3 : 4 * P * Q = 4 * (P * Q) := by ac_rfl
    have e4 : 4 * P * (4 * P) = 16 * (P * P) := by
      have : 4 * P * (4 * P) = (4 * 4) * (P * P) := by ac_rfl
      rw [this]; omega
    rw [e2, e3, e4]; omega
  rw [hl, hr]
  rw [Int.mul_add, Int.mul_sub, Int.sub_mul, Int.mul_add, Int.mul_sub, Int.mul_add, Int.mul_sub]
  have k1 : P * (9 * (Q * Q)) = 9 * (P * Q * Q) := by ac_rfl
  have k2 : P * (24 * (P * Q)) = 24 * (P * P * Q) := by ac_rfl
  have k3 : P * (16 * (P * P)) = 16 * (P * P * P) := by ac_rfl
  have k4 : Q * (Q * Q) = Q * Q * Q := by ac_rfl
  have k5 : Q * (8 * (P * Q)) = 8 * (P * Q * Q) := by ac_rfl
  have k6 : Q * (16 * (P * P)) = 16 * (P * P * Q) := by ac_rfl
  have k7 : P * (Q * Q) = P * Q * Q := by ac_rfl
  have k8 : P * (8 * (P * Q)) = 8 * (P * P * Q) := by ac_rfl
  rw [k1, k2, k3, k4, k5, k6, k7, k8]
  omega

/-- Theorem 2(b) Lemma 2: Core degree-3 additive Pythagorean superadditivity inequality.
    If B1^2 <= u1^2 * v1 and B2^2 <= u2^2 * v2 with u1, u2, v1, v2 >= 0, then
    (B1 + B2)^2 <= (u1 + u2)^2 * (v1 + v2). -/
theorem cubic_pythagorean_core (u1 u2 v1 v2 B1 B2 : Int)
    (hu1 : 0 ≤ u1) (hu2 : 0 ≤ u2) (hv1 : 0 ≤ v1) (hv2 : 0 ≤ v2)
    (hB1 : B1 * B1 ≤ u1 * u1 * v1) (hB2 : B2 * B2 ≤ u2 * u2 * v2) :
    (B1 + B2) * (B1 + B2) ≤ (u1 + u2) * (u1 + u2) * (v1 + v2) := by
  have huv_nn : 0 ≤ u1 * u2 * (v1 + v2) :=
    Int.mul_nonneg (Int.mul_nonneg hu1 hu2) (by omega)
  have hcross : 2 * (B1 * B2) ≤ u1 * u2 * (v1 + v2) := by
    by_cases hneg : 2 * (B1 * B2) ≤ 0
    · exact Int.le_trans hneg huv_nn
    · have hpos : 0 ≤ 2 * (B1 * B2) := by omega
      apply int_le_of_sq_le_sq hpos huv_nn
      have hsq1 : (2 * (B1 * B2)) * (2 * (B1 * B2)) = 4 * ((B1 * B1) * (B2 * B2)) := by
        have e : (2 * (B1 * B2)) * (2 * (B1 * B2)) = (2 * 2) * ((B1 * B1) * (B2 * B2)) := by ac_rfl
        rw [e]; omega
      have hprod : (B1 * B1) * (B2 * B2) ≤ (u1 * u1 * v1) * (u2 * u2 * v2) :=
        int_mul_le_mul_of_nonneg (int_sq_nonneg B1) (int_sq_nonneg B2) hB1 hB2
      have h4prod : 4 * ((B1 * B1) * (B2 * B2)) ≤ 4 * ((u1 * u1 * v1) * (u2 * u2 * v2)) :=
        Int.mul_le_mul_of_nonneg_left hprod (by omega)
      have hamgm : 4 * (v1 * v2) ≤ (v1 + v2) * (v1 + v2) := by
        have hid : (v1 + v2) * (v1 + v2) - 4 * (v1 * v2) = (v1 - v2) * (v1 - v2) := by
          rw [Int.add_mul, Int.mul_add, Int.mul_add, Int.sub_mul, Int.mul_sub, Int.mul_sub,
              Int.mul_comm v2 v1]
          omega
        have hnn := int_sq_nonneg (v1 - v2)
        omega
      have h4u : 4 * ((u1 * u1 * v1) * (u2 * u2 * v2)) ≤
                 (u1 * u2 * (v1 + v2)) * (u1 * u2 * (v1 + v2)) := by
        have eq1 : 4 * ((u1 * u1 * v1) * (u2 * u2 * v2)) =
                   ((u1 * u2) * (u1 * u2)) * (4 * (v1 * v2)) := by ac_rfl
        have eq2 : (u1 * u2 * (v1 + v2)) * (u1 * u2 * (v1 + v2)) =
                   ((u1 * u2) * (u1 * u2)) * ((v1 + v2) * (v1 + v2)) := by ac_rfl
        rw [eq1, eq2]
        exact Int.mul_le_mul_of_nonneg_left hamgm (int_sq_nonneg (u1 * u2))
      rw [hsq1]
      exact Int.le_trans h4prod h4u
  have hrem : 0 ≤ u1 * u1 * v2 + u2 * u2 * v1 + u1 * u2 * (v1 + v2) := by
    have t1 : 0 ≤ u1 * u1 * v2 := Int.mul_nonneg (int_sq_nonneg u1) hv2
    have t2 : 0 ≤ u2 * u2 * v1 := Int.mul_nonneg (int_sq_nonneg u2) hv1
    omega
  have hlhs : (B1 + B2) * (B1 + B2) = B1 * B1 + B2 * B2 + 2 * (B1 * B2) := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add, Int.mul_comm B2 B1]; omega
  have hrhs : (u1 + u2) * (u1 + u2) * (v1 + v2) =
      (u1 * u1 * v1 + u2 * u2 * v2 + u1 * u2 * (v1 + v2)) +
      (u1 * u1 * v2 + u2 * u2 * v1 + u1 * u2 * (v1 + v2)) := by
    have husq : (u1 + u2) * (u1 + u2) = u1 * u1 + 2 * (u1 * u2) + u2 * u2 := by
      rw [Int.add_mul, Int.mul_add, Int.mul_add, Int.mul_comm u2 u1]; omega
    rw [husq]
    simp only [Int.add_mul, Int.mul_add]
    have e1 : 2 * (u1 * u2) * v1 = 2 * (u1 * u2 * v1) := by ac_rfl
    have e2 : 2 * (u1 * u2) * v2 = 2 * (u1 * u2 * v2) := by ac_rfl
    rw [e1, e2]; omega
  rw [hlhs, hrhs]
  omega

-- ============================================================================
-- Section 3: Degree-2 & Degree-3 Multiplicative Laws (Theorem 3)
-- ============================================================================

/-- Theorem 3(a): Exact degree-2 multiplicative hyperbolic Pythagorean identity.
    For normalized p(x) = (x - 1)(x - a) and q(x) = (x - 1)(x - b),
    4 * disc(p ⊠_2 q) = (1+a)^2*(1+b)^2 - 16*a*b
    = (a-1)^2*(b+1)^2 + 4*a*(b-1)^2. -/
theorem degree2_hyperbolic_discriminant_identity (a b : Int) :
    ((1 + a) * (1 + b)) * ((1 + a) * (1 + b)) - 16 * (a * b) =
    (a - 1) * (a - 1) * ((b + 1) * (b + 1)) + 4 * a * ((b - 1) * (b - 1)) := by
  have ha1 : (1 + a) * (1 + a) = (a - 1) * (a - 1) + 4 * a := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add, Int.sub_mul, Int.mul_sub, Int.mul_sub]; omega
  have hb1 : (1 + b) * (1 + b) = (b - 1) * (b - 1) + 4 * b := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add, Int.sub_mul, Int.mul_sub, Int.mul_sub]; omega
  have hl : ((1 + a) * (1 + b)) * ((1 + a) * (1 + b)) =
            ((1 + a) * (1 + a)) * ((1 + b) * (1 + b)) := by ac_rfl
  have hb2 : (1 + b) * (1 + b) = (b + 1) * (b + 1) := by rw [Int.add_comm 1 b]
  have e : 4 * a * (4 * b) = 16 * (a * b) := by
    have : 4 * a * (4 * b) = (4 * 4) * (a * b) := by ac_rfl
    rw [this]; omega
  calc
    ((1 + a) * (1 + b)) * ((1 + a) * (1 + b)) - 16 * (a * b)
      = ((a - 1) * (a - 1) + 4 * a) * ((1 + b) * (1 + b)) - 16 * (a * b) := by rw [hl, ha1]
    _ = (a - 1) * (a - 1) * ((1 + b) * (1 + b)) + 4 * a * ((1 + b) * (1 + b)) - 16 * (a * b) := by
        rw [Int.add_mul]
    _ = (a - 1) * (a - 1) * ((b + 1) * (b + 1)) + 4 * a * ((b - 1) * (b - 1) + 4 * b) - 16 * (a * b) := by
        rw [hb2]; conv => lhs; arg 1; arg 2; rw [← hb2, hb1]
    _ = (a - 1) * (a - 1) * ((b + 1) * (b + 1)) + 4 * a * ((b - 1) * (b - 1)) := by
        rw [Int.mul_add (4 * a), e]; omega

/-- Theorem 3(b) Part 1: Deformed cubic discriminant factorization!
    Setting U = 3*u = mu*ut and V = 3*v = mu*vt,
    D_mu(U/3, V/3) = U^2*V^2 + mu*(mu+3)*U*V - (mu+1)*(U^3 + V^3) - mu^3
    equals mu^3 * (mu*(ut^2 - vt)*(vt^2 - ut) - (ut^3 + vt^3 + 1 - 3*ut*vt)). -/
theorem deformed_cubic_discriminant_factorization (mu ut vt : Int) :
    let U := mu * ut
    let V := mu * vt
    (U * U) * (V * V) + mu * (mu + 3) * (U * V) - (mu + 1) * (U * U * U + V * V * V) - mu * mu * mu =
    (mu * mu * mu) * (mu * ((ut * ut - vt) * (vt * vt - ut)) - (ut * ut * ut + vt * vt * vt + 1 - 3 * (ut * vt))) := by
  simp only
  have hfac : (ut * ut - vt) * (vt * vt - ut) =
              ut * ut * (vt * vt) - ut * ut * ut - vt * vt * vt + ut * vt := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_sub]
    have e2 : vt * (vt * vt) = vt * vt * vt := by ac_rfl
    have e3 : vt * ut = ut * vt := Int.mul_comm vt ut
    rw [e2, e3]; omega
  rw [hfac]
  have t1 : (mu * ut * (mu * ut)) * (mu * vt * (mu * vt)) =
            (mu * mu * mu) * (mu * (ut * ut * (vt * vt))) := by ac_rfl
  have t2 : mu * (mu + 3) * (mu * ut * (mu * vt)) =
            (mu * mu * mu) * (mu * (ut * vt)) + (mu * mu * mu) * (3 * (ut * vt)) := by
    rw [Int.mul_add, Int.add_mul]
    have e1 : mu * mu * (mu * ut * (mu * vt)) = (mu * mu * mu) * (mu * (ut * vt)) := by ac_rfl
    have e2 : mu * 3 * (mu * ut * (mu * vt)) = (mu * mu * mu) * (3 * (ut * vt)) := by ac_rfl
    rw [e1, e2]
  have t3 : (mu + 1) * (mu * ut * (mu * ut) * (mu * ut) + mu * vt * (mu * vt) * (mu * vt)) =
            (mu * mu * mu) * (mu * (ut * ut * ut)) + (mu * mu * mu) * (mu * (vt * vt * vt)) +
            (mu * mu * mu) * (ut * ut * ut) + (mu * mu * mu) * (vt * vt * vt) := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add, Int.one_mul]
    have e1 : mu * (mu * ut * (mu * ut) * (mu * ut)) = (mu * mu * mu) * (mu * (ut * ut * ut)) := by ac_rfl
    have e2 : mu * (mu * vt * (mu * vt) * (mu * vt)) = (mu * mu * mu) * (mu * (vt * vt * vt)) := by ac_rfl
    have e3 : mu * ut * (mu * ut) * (mu * ut) = (mu * mu * mu) * (ut * ut * ut) := by ac_rfl
    have e4 : mu * vt * (mu * vt) * (mu * vt) = (mu * mu * mu) * (vt * vt * vt) := by ac_rfl
    rw [e1, e2, e3, e4]; omega
  rw [t1, t2, t3]
  have hr : (mu * mu * mu) * (mu * (ut * ut * (vt * vt) - ut * ut * ut - vt * vt * vt + ut * vt) -
                              (ut * ut * ut + vt * vt * vt + 1 - 3 * (ut * vt))) =
            (mu * mu * mu) * (mu * (ut * ut * (vt * vt))) -
            (mu * mu * mu) * (mu * (ut * ut * ut)) -
            (mu * mu * mu) * (mu * (vt * vt * vt)) +
            (mu * mu * mu) * (mu * (ut * vt)) -
            (mu * mu * mu) * (ut * ut * ut) -
            (mu * mu * mu) * (vt * vt * vt) -
            (mu * mu * mu) +
            (mu * mu * mu) * (3 * (ut * vt)) := by
    simp only [Int.mul_add, Int.mul_sub, Int.mul_one]
    omega
  rw [hr]; omega

/-- Theorem 3(b) Part 2: Exact rational identity behind Phi(a, b) = Q(a, b) + (a + b + a*b)
    where Q(a, b) = (a - b)^2 / ((1 - a)*(1 - b)) = R + R^{-1} - 2 with R = (1 - a)/(1 - b).
    For a = p/q and b = r/s:
    (p*s - r*q)^2 = ((q - p)*s)^2 + ((s - r)*q)^2 - 2*((q - p)*s)*((s - r)*q). -/
theorem phi_square_identity_int (p q r s : Int) :
    (p * s - r * q) * (p * s - r * q) =
    ((q - p) * s) * ((q - p) * s) + ((s - r) * q) * ((s - r) * q) -
    2 * (((q - p) * s) * ((s - r) * q)) := by
  have hd : (q - p) * s - (s - r) * q = r * q - p * s := by
    rw [Int.sub_mul, Int.sub_mul, Int.mul_comm q s]; omega
  have hsq : ((q - p) * s - (s - r) * q) * ((q - p) * s - (s - r) * q) =
             ((q - p) * s) * ((q - p) * s) + ((s - r) * q) * ((s - r) * q) -
             2 * (((q - p) * s) * ((s - r) * q)) := by
    let X := (q - p) * s; let Y := (s - r) * q
    change (X - Y) * (X - Y) = X * X + Y * Y - 2 * (X * Y)
    rw [Int.sub_mul, Int.mul_sub, Int.mul_sub, Int.mul_comm Y X]; omega
  rw [← hsq, hd]
  have hneg : r * q - p * s = -(p * s - r * q) := by omega
  rw [hneg, Int.neg_mul_neg]

/-- Theorem 3(b) Part 3: Core multiplicative ratio contraction in cleared-denominator integer form!
    Let a1 = p1/q1, b1 = r1/s1, a2 = p2/q2, b2 = r2/s2 in (0, 1), and let M = Mn/Md >= 1
    satisfy R1 = (1-a1)/(1-b1) <= M and R2 = (1-a2)/(1-b2) <= M.
    Then R12 = (1 - a1*a2)/(1 - b1*b2) <= M! -/
theorem ratio_contraction_upper_int
    (p1 q1 r1 s1 p2 q2 r2 s2 Mn Md : Int)
    (hp1 : 0 < p1) (hpq1 : p1 < q1) (hr1 : 0 < r1) (hrs1 : r1 < s1)
    (hp2 : 0 < p2) (hpq2 : p2 < q2) (hr2 : 0 < r2) (hrs2 : r2 < s2)
    (hMd : 0 < Md) (hM1 : Md ≤ Mn)
    (hR1 : Md * (q1 - p1) * s1 ≤ Mn * (s1 - r1) * q1)
    (hR2 : Md * (q2 - p2) * s2 ≤ Mn * (s2 - r2) * q2) :
    Md * (q1 * q2 - p1 * p2) * (s1 * s2) ≤ Mn * (s1 * s2 - r1 * r2) * (q1 * q2) := by
  have hq1 : 0 < q1 := by omega
  have hs1 : 0 < s1 := by omega
  have hq2 : 0 < q2 := by omega
  have hs2 : 0 < s2 := by omega
  have hid_pq : q1 * q2 - p1 * p2 = (q1 - p1) * q2 + p1 * (q2 - p2) := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_comm p1 q2]; omega
  have hid_rs : s1 * s2 - r1 * r2 = (s1 - r1) * s2 + r1 * (s2 - r2) := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_comm r1 s2]; omega
  have hid_pq2 : q1 * q2 - p1 * p2 = (q2 - p2) * q1 + p2 * (q1 - p1) := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_comm q2 q1, Int.mul_comm p2 p1]; omega
  have hid_rs2 : s1 * s2 - r1 * r2 = (s2 - r2) * s1 + r2 * (s1 - r1) := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_comm s2 s1, Int.mul_comm r2 r1]; omega
  by_cases h1 : p1 * s1 ≤ r1 * q1
  · rw [hid_pq, hid_rs, Int.mul_add, Int.add_mul, Int.mul_add, Int.add_mul]
    have t1 : Md * ((q1 - p1) * q2) * (s1 * s2) ≤ Mn * ((s1 - r1) * s2) * (q1 * q2) := by
      have e1 : Md * ((q1 - p1) * q2) * (s1 * s2) = (Md * (q1 - p1) * s1) * (q2 * s2) := by ac_rfl
      have e2 : Mn * ((s1 - r1) * s2) * (q1 * q2) = (Mn * (s1 - r1) * q1) * (q2 * s2) := by ac_rfl
      rw [e1, e2]
      exact Int.mul_le_mul_of_nonneg_right hR1 (Int.le_of_lt (Int.mul_pos hq2 hs2))
    have t2 : Md * (p1 * (q2 - p2)) * (s1 * s2) ≤ Mn * (r1 * (s2 - r2)) * (q1 * q2) := by
      have e1 : Md * (p1 * (q2 - p2)) * (s1 * s2) = (p1 * s1) * (Md * (q2 - p2) * s2) := by ac_rfl
      have e2 : Mn * (r1 * (s2 - r2)) * (q1 * q2) = (r1 * q1) * (Mn * (s2 - r2) * q2) := by ac_rfl
      rw [e1, e2]
      exact int_mul_le_mul_of_nonneg
        (Int.le_of_lt (Int.mul_pos hp1 hs1))
        (Int.le_of_lt (Int.mul_pos (Int.mul_pos hMd (by omega : 0 < q2 - p2)) hs2))
        h1 hR2
    omega
  · by_cases h2 : p2 * s2 ≤ r2 * q2
    · rw [hid_pq2, hid_rs2, Int.mul_add, Int.add_mul, Int.mul_add, Int.add_mul]
      have t1 : Md * ((q2 - p2) * q1) * (s1 * s2) ≤ Mn * ((s2 - r2) * s1) * (q1 * q2) := by
        have e1 : Md * ((q2 - p2) * q1) * (s1 * s2) = (Md * (q2 - p2) * s2) * (q1 * s1) := by ac_rfl
        have e2 : Mn * ((s2 - r2) * s1) * (q1 * q2) = (Mn * (s2 - r2) * q2) * (q1 * s1) := by ac_rfl
        rw [e1, e2]
        exact Int.mul_le_mul_of_nonneg_right hR2 (Int.le_of_lt (Int.mul_pos hq1 hs1))
      have t2 : Md * (p2 * (q1 - p1)) * (s1 * s2) ≤ Mn * (r2 * (s1 - r1)) * (q1 * q2) := by
        have e1 : Md * (p2 * (q1 - p1)) * (s1 * s2) = (p2 * s2) * (Md * (q1 - p1) * s1) := by ac_rfl
        have e2 : Mn * (r2 * (s1 - r1)) * (q1 * q2) = (r2 * q2) * (Mn * (s1 - r1) * q1) := by ac_rfl
        rw [e1, e2]
        exact int_mul_le_mul_of_nonneg
          (Int.le_of_lt (Int.mul_pos hp2 hs2))
          (Int.le_of_lt (Int.mul_pos (Int.mul_pos hMd (by omega : 0 < q1 - p1)) hs1))
          h2 hR1
      omega
    · have hprod : (r1 * q1) * (r2 * q2) ≤ (p1 * s1) * (p2 * s2) :=
        int_mul_le_mul_of_nonneg
          (Int.le_of_lt (Int.mul_pos hr1 hq1))
          (Int.le_of_lt (Int.mul_pos hr2 hq2))
          (by omega) (by omega)
      have hcmp : (q1 * q2 - p1 * p2) * (s1 * s2) ≤ (s1 * s2 - r1 * r2) * (q1 * q2) := by
        rw [Int.sub_mul, Int.sub_mul]
        have e1 : q1 * q2 * (s1 * s2) = s1 * s2 * (q1 * q2) := by ac_rfl
        have e2 : r1 * r2 * (q1 * q2) = (r1 * q1) * (r2 * q2) := by ac_rfl
        have e3 : p1 * p2 * (s1 * s2) = (p1 * s1) * (p2 * s2) := by ac_rfl
        rw [e1, e2, e3]; omega
      have hpos : 0 ≤ (q1 * q2 - p1 * p2) * (s1 * s2) := by
        have hpq12 : p1 * p2 < q1 * q2 := by
          have m1 : p1 * p2 < q1 * p2 := Int.mul_lt_mul_of_pos_right hpq1 hp2
          have m2 : q1 * p2 < q1 * q2 := Int.mul_lt_mul_of_pos_left hpq2 hq1
          exact Int.lt_trans m1 m2
        exact Int.mul_nonneg (by omega) (Int.le_of_lt (Int.mul_pos hs1 hs2))
      have eL : Md * (q1 * q2 - p1 * p2) * (s1 * s2) = Md * ((q1 * q2 - p1 * p2) * (s1 * s2)) := by ac_rfl
      have eR : Mn * (s1 * s2 - r1 * r2) * (q1 * q2) = Mn * ((s1 * s2 - r1 * r2) * (q1 * q2)) := by ac_rfl
      rw [eL, eR]
      exact int_mul_le_mul_of_nonneg (Int.le_of_lt hMd) hpos hM1 hcmp

/-- Theorem 3(b) Part 4: Real-rootedness domination (U = 3u >= mu, V = 3v >= mu, mu >= 3).
    Delta(U/3, V/3) - D_mu(U/3, V/3) >= (mu - 3)^3 * (mu + 1) >= 0.
    Hence D_mu >= 0 and mu > 3 strictly implies Delta > 0 (3 distinct positive real roots). -/
theorem discriminant_dominates_deformed (mu U V : Int)
    (hmu : 3 ≤ mu) (hU : mu ≤ U) (hV : mu ≤ V) :
    let Delta := (U * U) * (V * V) + 18 * (U * V) - 4 * (U * U * U + V * V * V) - 27
    let Dmu   := (U * U) * (V * V) + mu * (mu + 3) * (U * V) - (mu + 1) * (U * U * U + V * V * V) - mu * mu * mu
    (mu - 3) * (mu - 3) * (mu - 3) * (mu + 1) ≤ Delta - Dmu := by
  simp only
  have hdiff : ((U * U) * (V * V) + 18 * (U * V) - 4 * (U * U * U + V * V * V) - 27) -
               ((U * U) * (V * V) + mu * (mu + 3) * (U * V) - (mu + 1) * (U * U * U + V * V * V) - mu * mu * mu) =
               (mu - 3) * (U * U * U + V * V * V - (mu + 6) * (U * V) + (mu * mu + 3 * mu + 9)) := by
    simp only [Int.sub_mul, Int.mul_add, Int.mul_sub, Int.add_mul, Int.one_mul]
    have e1 : mu * (mu * (U * V)) = mu * mu * (U * V) := by ac_rfl
    have e2 : mu * (6 * (U * V)) = 6 * (mu * (U * V)) := by ac_rfl
    have e4 : mu * 3 * (U * V) = 3 * (mu * (U * V)) := by ac_rfl
    have e5 : 3 * (6 * (U * V)) = 18 * (U * V) := by
      have : 3 * (6 * (U * V)) = (3 * 6) * (U * V) := by ac_rfl
      rw [this]; omega
    have e6 : mu * (mu * mu) = mu * mu * mu := by ac_rfl
    have e7 : mu * (3 * mu) = 3 * (mu * mu) := by ac_rfl
    have e8 : 3 * (3 * mu) = 9 * mu := by
      have : 3 * (3 * mu) = (3 * 3) * mu := by ac_rfl
      rw [this]; omega
    have e9 : mu * 9 = 9 * mu := Int.mul_comm mu 9
    rw [e1, e2, e4, e5, e6, e7, e8, e9]
    omega
  rw [hdiff]
  let a := U - mu
  let b := V - mu
  have ha : 0 ≤ a := by omega
  have hb : 0 ≤ b := by omega
  have hUa : U = mu + a := by omega
  have hVb : V = mu + b := by omega
  have h2id :
      2 * (U * U * U + V * V * V - (mu + 6) * (U * V) + (mu * mu + 3 * mu + 9) -
           (mu - 3) * (mu - 3) * (mu + 1)) =
      2 * (a * a * a + b * b * b) +
      (mu + 6) * ((a - b) * (a - b)) +
      (5 * mu - 6) * (a * a + b * b) +
      4 * mu * (mu - 3) * (a + b) := by
    rw [hUa, hVb]
    have hcube : ∀ x : Int, (mu + x) * (mu + x) * (mu + x) =
        mu * mu * mu + 3 * (mu * mu * x) + 3 * (mu * (x * x)) + x * x * x := by
      intro x
      simp only [Int.add_mul, Int.mul_add]
      have c0 : mu * x * mu = mu * mu * x := by ac_rfl
      have c1 : x * mu * mu = mu * mu * x := by ac_rfl
      have c2 : x * x * mu = mu * (x * x) := by ac_rfl
      have c3 : x * mu * x = mu * (x * x) := by ac_rfl
      have c4 : mu * x * x = mu * (x * x) := by ac_rfl
      rw [c0, c1, c2, c3, c4]; omega
    rw [hcube a, hcube b]
    have hmid : (mu + 6) * ((mu + a) * (mu + b)) =
        mu * mu * mu + 6 * (mu * mu) + mu * mu * a + mu * mu * b +
        6 * (mu * a) + 6 * (mu * b) + mu * (a * b) + 6 * (a * b) := by
      simp only [Int.add_mul, Int.mul_add]
      have f0 : mu * (mu * mu) = mu * mu * mu := by ac_rfl
      have f1 : mu * (mu * b) = mu * mu * b := by ac_rfl
      have f2 : mu * (a * mu) = mu * mu * a := by ac_rfl
      have f5 : 6 * (a * mu) = 6 * (mu * a) := by ac_rfl
      rw [f0, f1, f2, f5]; omega
    have hm3 : (mu - 3) * (mu - 3) * (mu + 1) = mu * mu * mu - 5 * (mu * mu) + 3 * mu + 9 := by
      simp only [Int.sub_mul, Int.mul_sub, Int.mul_add, Int.mul_one]
      have f1 : mu * 3 * mu = 3 * (mu * mu) := by ac_rfl
      have f2 : 3 * mu * mu = 3 * (mu * mu) := by ac_rfl
      have f3 : mu * 3 = 3 * mu := Int.mul_comm mu 3
      rw [f1, f2, f3]; omega
    have hsq_gen : ∀ x y : Int, (x - y) * (x - y) = x * x + y * y - 2 * (x * y) := by
      intro x y
      rw [Int.sub_mul, Int.mul_sub, Int.mul_sub, Int.mul_comm y x]; omega
    have hsq := hsq_gen a b
    rw [hmid, hm3, hsq]
    simp only [Int.mul_add, Int.add_mul, Int.mul_sub, Int.sub_mul]
    have g3 : mu * (2 * (a * b)) = 2 * (mu * (a * b)) := by ac_rfl
    have g4 : 6 * (2 * (a * b)) = 12 * (a * b) := by
      have : 6 * (2 * (a * b)) = (6 * 2) * (a * b) := by ac_rfl
      rw [this]; omega
    have g5 : 4 * mu * mu * a = 4 * (mu * mu * a) := by ac_rfl
    have g6 : 4 * mu * mu * b = 4 * (mu * mu * b) := by ac_rfl
    have g7 : 4 * mu * 3 * a = 12 * (mu * a) := by
      have : 4 * mu * 3 * a = (4 * 3) * (mu * a) := by ac_rfl
      rw [this]; omega
    have g8 : 4 * mu * 3 * b = 12 * (mu * b) := by
      have : 4 * mu * 3 * b = (4 * 3) * (mu * b) := by ac_rfl
      rw [this]; omega
    have g9 : 5 * mu * (a * a) = 5 * (mu * (a * a)) := by ac_rfl
    have g10 : 5 * mu * (b * b) = 5 * (mu * (b * b)) := by ac_rfl
    rw [g3, g4, g5, g6, g7, g8, g9, g10]
    omega
  have h2nn : 0 ≤ 2 * (U * U * U + V * V * V - (mu + 6) * (U * V) + (mu * mu + 3 * mu + 9) -
                       (mu - 3) * (mu - 3) * (mu + 1)) := by
    rw [h2id]
    have t1 : 0 ≤ 2 * (a * a * a + b * b * b) := by
      have ta : 0 ≤ a * a * a := Int.mul_nonneg (int_sq_nonneg a) ha
      have tb : 0 ≤ b * b * b := Int.mul_nonneg (int_sq_nonneg b) hb
      omega
    have t2 : 0 ≤ (mu + 6) * ((a - b) * (a - b)) :=
      Int.mul_nonneg (by omega) (int_sq_nonneg (a - b))
    have t3 : 0 ≤ (5 * mu - 6) * (a * a + b * b) :=
      Int.mul_nonneg (by omega) (by have := int_sq_nonneg a; have := int_sq_nonneg b; omega)
    have t4 : 0 ≤ 4 * mu * (mu - 3) * (a + b) :=
      Int.mul_nonneg (Int.mul_nonneg (by omega) (by omega)) (by omega)
    omega
  have hinner : (mu - 3) * (mu - 3) * (mu + 1) ≤
      U * U * U + V * V * V - (mu + 6) * (U * V) + (mu * mu + 3 * mu + 9) := by omega
  have hres := Int.mul_le_mul_of_nonneg_left hinner (by omega : 0 ≤ mu - 3)
  have hre : (mu - 3) * ((mu - 3) * (mu - 3) * (mu + 1)) =
             (mu - 3) * (mu - 3) * (mu - 3) * (mu + 1) := by ac_rfl
  rwa [hre] at hres

-- ============================================================================
-- Section 4: Finite Free Heat-Flow Telescoping & Dyson Rate Bounds (Theorem 4)
-- ============================================================================

/-- Transparent exact fraction for certifying the telescoping Coulomb sum
    sum_{k=1}^n 1/(k*(k+1)) = n/(n+1) = 1 - 1/(n+1). -/
structure QPos where
  num : Nat
  den : Nat
  deriving DecidableEq

def qAdd (x y : QPos) : QPos :=
  ⟨x.num * y.den + y.num * x.den, x.den * y.den⟩

def qEq (x y : QPos) : Prop :=
  x.num * y.den = y.num * x.den

def coulombSumQ : Nat → QPos
  | 0 => ⟨0, 1⟩
  | n + 1 => qAdd (coulombSumQ n) ⟨1, (n + 1) * (n + 2)⟩

/-- Theorem 4(a): Exact telescoping identity sum_{k=1}^n 1/(k*(k+1)) = n/(n+1). -/
theorem coulombSum_closed_form (n : Nat) :
    qEq (coulombSumQ n) ⟨n, n + 1⟩ := by
  induction n with
  | zero => rfl
  | succ k ih =>
    unfold qEq at ih
    dsimp only [coulombSumQ, qAdd, qEq]
    let sn := (coulombSumQ k).num
    let sd := (coulombSumQ k).den
    change (sn * ((k + 1) * (k + 2)) + 1 * sd) * (k + 2) = (k + 1) * (sd * ((k + 1) * (k + 2)))
    have hih : sn * (k + 1) = k * sd := ih
    have h1 : sn * ((k + 1) * (k + 2)) = k * sd * (k + 2) := by
      have : sn * ((k + 1) * (k + 2)) = (sn * (k + 1)) * (k + 2) := by ac_rfl
      rw [this, hih]
    rw [h1, Nat.one_mul]
    have hfac : k * sd * (k + 2) + sd = sd * ((k + 1) * (k + 1)) := by
      have e1 : k * sd * (k + 2) = sd * (k * (k + 2)) := by ac_rfl
      have e2 : sd * (k * (k + 2)) + sd = sd * (k * (k + 2) + 1) := by
        rw [Nat.mul_add (sd) (k * (k + 2)) 1, Nat.mul_one]
      have e3 : k * (k + 2) + 1 = (k + 1) * (k + 1) := by
        rw [Nat.mul_add, Nat.add_mul, Nat.mul_add, Nat.mul_one, Nat.one_mul]; omega
      rw [e1, e2, e3]
    rw [hfac]
    ac_rfl

/-- Theorem 4(b): Even-parity optimal Dyson expansion bound:
    1/(L+1) + 1/(R+1) >= 4 / (L + R + 2), cleared of denominators:
    4 * (L + 1) * (R + 1) <= (L + R + 2)^2. -/
theorem dyson_rate_lower_bound_even (L R : Nat) :
    4 * ((L + 1) * (R + 1)) ≤ (L + R + 2) * (L + R + 2) := by
  have h1 : ((L : Int) + R + 2) * ((L : Int) + R + 2) - 4 * (((L : Int) + 1) * ((R : Int) + 1)) =
            ((L : Int) - R) * ((L : Int) - R) := by
    simp only [Int.add_mul, Int.mul_add, Int.sub_mul, Int.mul_sub]
    rw [Int.mul_comm (R : Int) (L : Int)]
    omega
  have hnn := int_sq_nonneg ((L : Int) - R)
  have hint : 4 * (((L : Int) + 1) * ((R : Int) + 1)) ≤ ((L : Int) + R + 2) * ((L : Int) + R + 2) := by
    omega
  have hcast : ((4 * ((L + 1) * (R + 1)) : Nat) : Int) ≤ (((L + R + 2) * (L + R + 2) : Nat) : Int) := by
    simpa [Int.natCast_mul, Int.natCast_add] using hint
  exact Int.ofNat_le.mp hcast

/-- Theorem 4(c): Odd-parity sharper Dyson expansion bound:
    When L + R + 2 = 2*m + 1 is odd, |L - R| >= 1, so
    4 * (L + 1) * (R + 1) <= (2*m + 1)^2 - 1, giving 1/(L+1) + 1/(R+1) >= 4*d / (d^2 - 1). -/
theorem dyson_rate_lower_bound_odd (L R m : Nat) (hodd : L + R + 2 = 2 * m + 1) :
    4 * ((L + 1) * (R + 1)) + 1 ≤ (2 * m + 1) * (2 * m + 1) := by
  have hdiff_sq : 1 ≤ ((L : Int) - R) * ((L : Int) - R) := by
    by_cases hpos : 0 < (L : Int) - R
    · have h1 : (1 : Int) ≤ (L : Int) - R := by omega
      exact int_mul_le_mul_of_nonneg (by omega) (by omega) h1 h1
    · have h1 : (1 : Int) ≤ (R : Int) - L := by omega
      have hsq : 1 ≤ ((R : Int) - L) * ((R : Int) - L) :=
        int_mul_le_mul_of_nonneg (by omega) (by omega) h1 h1
      have heq : ((R : Int) - L) * ((R : Int) - L) = ((L : Int) - R) * ((L : Int) - R) := by
        have : (R : Int) - L = -((L : Int) - R) := by omega
        rw [this, Int.neg_mul_neg]
      rwa [heq] at hsq
  have hid : ((L : Int) + R + 2) * ((L : Int) + R + 2) - 4 * (((L : Int) + 1) * ((R : Int) + 1)) =
             ((L : Int) - R) * ((L : Int) - R) := by
    simp only [Int.add_mul, Int.mul_add, Int.sub_mul, Int.mul_sub]
    rw [Int.mul_comm (R : Int) (L : Int)]
    omega
  have hcast_d : ((L : Int) + R + 2) = 2 * (m : Int) + 1 := by omega
  rw [hcast_d] at hid
  have hint : 4 * (((L : Int) + 1) * ((R : Int) + 1)) + 1 ≤ (2 * (m : Int) + 1) * (2 * (m : Int) + 1) := by
    omega
  have hcast : ((4 * ((L + 1) * (R + 1)) + 1 : Nat) : Int) ≤
               (((2 * m + 1) * (2 * m + 1) : Nat) : Int) := by
    simpa [Int.natCast_mul, Int.natCast_add] using hint
  exact Int.ofNat_le.mp hcast

-- ============================================================================
-- Section 5: Exact Counterexamples (d = 4, d = 5) & Universal Sturm Failure
-- ============================================================================

/-- Theorem 5(a): Exact degree-4 arithmetic progression self-convolution counterexample.
    p_AP^(4)(x) = x^4 - (5/2)x^2 + 9/16 => (p_AP^(4) ⊞_4 p_AP^(4))(x) = x^4 - 5x^2 + 13/6,
    discriminant 25 - 4*(13/6) = 49/3, and gap^2 = 10 - 14/sqrt(3) < 2 since 192 < 196. -/
theorem degree4_counterexample_exact :
    (2 * 27 + 2 * 25 = 8 * 13) ∧
    (25 * 6 - 4 * 13 = 49 * 2) ∧
    (8 * 8 * 3 < 14 * 14) := by
  decide

/-- Theorem 5(b): Exact degree-5 arithmetic progression self-convolution counterexample.
    p_AP^(5)(x) = x^5 - 5x^3 + 4x => (p_AP^(5) ⊞_5 p_AP^(5))(x) = x^5 - 10x^3 + (31/2)x,
    inner squared root = 5 - sqrt(19/2) < 2 since 18 < 19. -/
theorem degree5_counterexample_exact :
    (2 * 4 * 120 + 36 * 25 = 60 * 31) ∧
    (25 * 2 - 31 = 19) ∧
    (3 * 3 * 2 < 19) := by
  decide

/-- Theorem 5(c): Exact Hermite heat-flow violation constants kappa_4 < 1 and kappa_5 < 1.
    d=4: gap(He_4)^2 = 12 - 4*sqrt(6) > 2  <=>  96 < 100.
    d=5: gap(He_5)^2 = 5 - sqrt(10) > 5/3  <=>  90 < 100. -/
theorem hermite_kappa_4_5_strictly_below_one :
    (4 * 4 * 6 < 10 * 10) ∧ (9 * 10 < 10 * 10) := by
  decide

/-- Theorem 5(d): Universal Sturm-Liouville violation certifying kappa_d < 1 for ALL d >= 4!
    Using pi > 314/100 (so pi^2 > 98596/10000), clearing denominators:
    - Even d >= 4: 8 / d < (98596/10000) / (d + 1/2)  <=>  80000 * (2*d + 1) < 98596 * 2 * d.
    - Odd  d >= 5: 8*d / (d^2 - 1) < (98596/10000) / (d + 1/2)
                   <=>  80000 * d * (2*d + 1) < 98596 * 2 * (d*d - 1). -/
theorem sturm_universal_failure_even (d : Nat) (hd : 4 ≤ d) :
    80000 * (2 * d + 1) < 98596 * (2 * d) := by
  omega

theorem sturm_universal_failure_odd (d : Nat) (hd : 5 ≤ d) :
    80000 * d * (2 * d + 1) < 98596 * 2 * (d * d - 1) := by
  have hd2 : 1 ≤ d * d := by
    have : 5 * 5 ≤ d * d := Nat.mul_le_mul hd hd
    omega
  have h1 : 105960 ≤ 37192 * d - 80000 := by omega
  have h2 : 5 * 105960 ≤ d * (37192 * d - 80000) := Nat.mul_le_mul hd h1
  have h3 : 80000 * d ≤ 37192 * (d * d) := by
    have : 80000 * d ≤ 37192 * d * d := by
      have ha : 80000 ≤ 37192 * d := by omega
      exact Nat.mul_le_mul_right d ha
    have hassoc : 37192 * d * d = 37192 * (d * d) := Nat.mul_assoc 37192 d d
    omega
  have h4 : d * (37192 * d - 80000) = 37192 * (d * d) - 80000 * d := by
    rw [Nat.mul_sub_left_distrib]
    have e1 : d * (37192 * d) = 37192 * (d * d) := by ac_rfl
    have e2 : d * 80000 = 80000 * d := Nat.mul_comm d 80000
    rw [e1, e2]
  have h5 : 197192 < 37192 * (d * d) - 80000 * d := by omega
  have hl : 80000 * d * (2 * d + 1) = 160000 * (d * d) + 80000 * d := by
    rw [Nat.mul_add, Nat.mul_one]
    have : 80000 * d * (2 * d) = (80000 * 2) * (d * d) := by ac_rfl
    rw [this]
  have hr : 98596 * 2 * (d * d - 1) = 197192 * (d * d) - 197192 := by
    rw [Nat.mul_sub_left_distrib, Nat.mul_one]
  rw [hl, hr]
  omega

end FiniteFreeRootGaps
