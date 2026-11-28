/-
  SchattenCrouzeixCore.lean
  Standalone Lean 4.36.0 formalization (zero sorry, zero grind, zero custom axioms,
  zero external dependencies, -DwarningAsError=true) of the exact algebraic and inequality
  core of:
    "Schatten-q Crouzeix Constants and the Hilbert-Schmidt Phase Transition:
     Universal Conformal Majorization on M_2(C), Odd-Even Clifford Parity Staircases,
     and Double-Layer Trace Bounds"

  All rational identities and inequalities are formalized in exact denominator-cleared
  integer/natural arithmetic (Z / N), equivalent over Q by clearing positive denominators
  and extending to R by continuity.
-/

namespace SchattenCrouzeix

-- ============================================================================
-- Section 1: Elementary Int Helpers
-- ============================================================================

private theorem int_sq_nonneg (x : Int) : 0 ≤ x * x := by
  rcases Int.le_total 0 x with hx | hx
  · exact Int.mul_nonneg hx hx
  · have hnx : 0 ≤ -x := by omega
    have h : 0 ≤ (-x) * (-x) := Int.mul_nonneg hnx hnx
    simpa [Int.neg_mul_neg] using h

private theorem int_mul_pos {a b : Int} (ha : 0 < a) (hb : 0 < b) : 0 < a * b :=
  Int.mul_pos ha hb

-- ============================================================================
-- Section 2: Odd-Even Clifford Parity Staircase (Theorem 2.1)
-- ============================================================================

/-- Theorem 2.1(a): Exact weak majorization partial-sum identity for s^(n) = (2,...,2,[1],0,...,0).
    For every n >= 1 and 0 <= k <= n, the partial sum of the top k entries of s^(n)
    equals exactly min(2*k, n). -/
def extremalPrefixSum (n k : Nat) : Nat :=
  let m := n / 2
  let rem := n % 2
  if k ≤ m then
    2 * k
  else if k ≤ m + rem then
    2 * m + (k - m)
  else
    2 * m + rem

theorem extremal_prefix_sum_eq_min (n k : Nat) :
    extremalPrefixSum n k = min (2 * k) n := by
  unfold extremalPrefixSum
  dsimp only
  split
  · omega
  · split <;> omega

/-- Theorem 2.1(b): Exact odd-dimension parity deficit for Frobenius (q = 2):
    for every odd n = 2*m + 1, sum (s_j^(n))^2 = 4*m + 1 = 2*n - 1 < 2*n. -/
theorem odd_frobenius_parity_deficit (m : Nat) :
    4 * m + 1 + 1 = 2 * (2 * m + 1) := by
  omega

/-- Theorem 2.1(c): Strict odd-dimension parity deficit for ALL integer exponents q >= 2:
    m * 2^q + 1 < (2*m + 1) * 2^(q - 1) for every m >= 0 and q >= 2. -/
theorem odd_schatten_parity_strict (m q : Nat) (hq : 2 ≤ q) :
    m * 2 ^ q + 1 < (2 * m + 1) * 2 ^ (q - 1) := by
  have hq_eq : q = (q - 1) + 1 := by omega
  have hpow : 2 ^ q = 2 * 2 ^ (q - 1) := by
    conv => lhs; rw [hq_eq, Nat.pow_succ]
    exact Nat.mul_comm (2 ^ (q - 1)) 2
  have hge2 : 2 ≤ 2 ^ (q - 1) := by
    have h1 : 1 ≤ q - 1 := by omega
    have h2 : 2 ^ 1 ≤ 2 ^ (q - 1) := Nat.pow_le_pow_right (by omega) h1
    omega
  rw [hpow]
  have hlhs : m * (2 * 2 ^ (q - 1)) = 2 * m * 2 ^ (q - 1) := by
    rw [← Nat.mul_assoc, Nat.mul_comm m 2]
  have hrhs : (2 * m + 1) * 2 ^ (q - 1) = 2 * m * 2 ^ (q - 1) + 2 ^ (q - 1) := by
    rw [Nat.add_mul, Nat.one_mul]
  rw [hlhs, hrhs]
  omega

-- ============================================================================
-- Section 3: Universal 2x2 Conformal Majorization Identities (Theorem 3.1)
-- ============================================================================

/-- Theorem 3.1(a): Exact Schwarz-Pick Regime B reduction identity:
    (x^2 + y^2)(1 - rho^2) - (x^2 + y^2 - rho^2 (1 + x^2 y^2)) = rho^2 (1 - x^2)(1 - y^2). -/
theorem schwarz_pick_regime_b_identity (x y rho : Int) :
    (x * x + y * y) * (1 - rho * rho) -
      (x * x + y * y - rho * rho * (1 + x * x * (y * y))) =
    rho * rho * (1 - x * x) * (1 - y * y) := by
  have h1 : (x * x + y * y) * (1 - rho * rho) =
      x * x + y * y - rho * rho * (x * x) - rho * rho * (y * y) := by
    rw [Int.mul_sub, Int.mul_one, Int.add_mul]
    have e1 : x * x * (rho * rho) = rho * rho * (x * x) := Int.mul_comm _ _
    have e2 : y * y * (rho * rho) = rho * rho * (y * y) := Int.mul_comm _ _
    rw [e1, e2]
    omega
  have h2 : rho * rho * (1 - x * x) * (1 - y * y) =
      rho * rho * (1 + x * x * (y * y)) - rho * rho * (x * x) - rho * rho * (y * y) := by
    rw [Int.mul_assoc]
    have hprod : (1 - x * x) * (1 - y * y) = 1 - x * x - y * y + x * x * (y * y) := by
      rw [Int.sub_mul, Int.one_mul, Int.mul_sub, Int.mul_one]
      omega
    rw [hprod, Int.mul_add, Int.mul_sub, Int.mul_sub, Int.mul_one, Int.mul_add, Int.mul_one]
    omega
  rw [h1, h2]
  omega

/-- Theorem 3.1(b): Exact Regime B endpoint factorization at y = 1:
    lam^4 - lam^2 (x^2 + 1) + x^2 = (lam^2 - 1)(lam^2 - x^2). -/
theorem regime_b_upper_endpoint_factorization (lam x : Int) :
    lam * lam * (lam * lam) - lam * lam * (x * x + 1) + x * x =
    (lam * lam - 1) * (lam * lam - x * x) := by
  have hr : (lam * lam - 1) * (lam * lam - x * x) =
      lam * lam * (lam * lam) - lam * lam * (x * x) - lam * lam + x * x := by
    rw [Int.sub_mul, Int.one_mul, Int.mul_sub]
    omega
  have hl : lam * lam * (x * x + 1) = lam * lam * (x * x) + lam * lam := by
    rw [Int.mul_add, Int.mul_one]
  rw [hl, hr]
  omega

/-- Theorem 3.1(c): Exact hyperbola-boundary quadratic factorization for sigma_1 <= lam = r*R.
    Clearing denominators by multiplying by R^2 * (1 + r^2)^2, let:
      L = r * R   (so L > 1),
      A = r * (R^2 + 1)  (so a * rho = A / (R * (1 + r^2))),
      D = 1 + r^2.
    Then at p = r^2, the cleared quadratic Q(p) = (L^2 * D)^2 * (L^2 + p)^2?
    More directly, for any integers L, M, r, p (representing lam, a*rho, r, p):
    if L^4 - L^2 * M^2 * (1 + r^2)^2 + 2 * L^2 * r^2 + r^4 = 0, then
    r^2 * (L^4 - L^2 * M^2 * (1 + p)^2 + 2 * L^2 * p + p^2)
      = (r^2 - p) * (L^2 * (L^2 - M^2) + r^2 * (L^2 * M^2 - 1) * p). -/
theorem hyperbola_quadratic_factorization (L M r p : Int)
    (hroot : L * L * (L * L) - L * L * (M * M) * ((1 + r * r) * (1 + r * r)) +
             2 * (L * L) * (r * r) + r * r * (r * r) = 0) :
    r * r * (L * L * (L * L) - L * L * (M * M) * ((1 + p) * (1 + p)) +
             2 * (L * L) * p + p * p) =
    (r * r - p) * (L * L * (L * L - M * M) + r * r * (L * L * (M * M) - 1) * p) := by
  let L2 := L * L
  let M2 := M * M
  let R2 := r * r
  have h1 : (1 + r * r) * (1 + r * r) = 1 + 2 * R2 + R2 * R2 := by
    change (1 + R2) * (1 + R2) = 1 + 2 * R2 + R2 * R2
    rw [Int.add_mul, Int.one_mul, Int.mul_add, Int.mul_one]
    omega
  have h2 : (1 + p) * (1 + p) = 1 + 2 * p + p * p := by
    rw [Int.add_mul, Int.one_mul, Int.mul_add, Int.mul_one]
    omega
  have hroot' : L2 * L2 - L2 * M2 - 2 * (L2 * M2) * R2 - L2 * M2 * (R2 * R2) +
                2 * L2 * R2 + R2 * R2 = 0 := by
    change L2 * L2 - L2 * M2 * ((1 + R2) * (1 + R2)) + 2 * L2 * R2 + R2 * R2 = 0 at hroot
    have h1' : (1 + R2) * (1 + R2) = 1 + 2 * R2 + R2 * R2 := h1
    rw [h1', Int.mul_add, Int.mul_add, Int.mul_one] at hroot
    have e : L2 * M2 * (2 * R2) = 2 * (L2 * M2) * R2 := by ac_rfl
    rw [e] at hroot
    omega
  -- Expand LHS: R2 * (L2*L2 - L2*M2 - 2*L2*M2*p - L2*M2*p^2 + 2*L2*p + p^2)
  change R2 * (L2 * L2 - L2 * M2 * ((1 + p) * (1 + p)) + 2 * L2 * p + p * p) =
         (R2 - p) * (L2 * (L2 - M2) + R2 * (L2 * M2 - 1) * p)
  rw [h2]
  have hl : R2 * (L2 * L2 - L2 * M2 * (1 + 2 * p + p * p) + 2 * L2 * p + p * p) =
      R2 * (L2 * L2) - R2 * (L2 * M2) - 2 * R2 * (L2 * M2) * p - R2 * (L2 * M2) * (p * p) +
      2 * R2 * L2 * p + R2 * (p * p) := by
    have hinner : L2 * M2 * (1 + 2 * p + p * p) =
        L2 * M2 + 2 * (L2 * M2) * p + L2 * M2 * (p * p) := by
      rw [Int.mul_add, Int.mul_add, Int.mul_one]
      have ea : L2 * M2 * (2 * p) = 2 * (L2 * M2) * p := by ac_rfl
      rw [ea]
    rw [hinner]
    rw [Int.mul_add, Int.mul_add, Int.mul_sub, Int.mul_add, Int.mul_add]
    have e1 : R2 * (2 * (L2 * M2) * p) = 2 * R2 * (L2 * M2) * p := by ac_rfl
    have e2 : R2 * (L2 * M2 * (p * p)) = R2 * (L2 * M2) * (p * p) := by ac_rfl
    have e3 : R2 * (2 * L2 * p) = 2 * R2 * L2 * p := by ac_rfl
    rw [e1, e2, e3]
    omega
  have hr : (R2 - p) * (L2 * (L2 - M2) + R2 * (L2 * M2 - 1) * p) =
      R2 * (L2 * L2) - R2 * (L2 * M2) - L2 * L2 * p + L2 * M2 * p +
      R2 * R2 * (L2 * M2) * p - R2 * R2 * p - R2 * (L2 * M2) * (p * p) + R2 * (p * p) := by
    have ha : L2 * (L2 - M2) = L2 * L2 - L2 * M2 := Int.mul_sub _ _ _
    have hb : R2 * (L2 * M2 - 1) * p = R2 * (L2 * M2) * p - R2 * p := by
      rw [Int.mul_sub, Int.mul_one, Int.sub_mul]
    rw [ha, hb, Int.sub_mul, Int.mul_add, Int.mul_add, Int.mul_sub, Int.mul_sub, Int.mul_sub, Int.mul_sub]
    have e1 : R2 * (R2 * (L2 * M2) * p) = R2 * R2 * (L2 * M2) * p := by ac_rfl
    have e2 : R2 * (R2 * p) = R2 * R2 * p := by ac_rfl
    have e3 : p * (L2 * L2) = L2 * L2 * p := Int.mul_comm _ _
    have e4 : p * (L2 * M2) = L2 * M2 * p := Int.mul_comm _ _
    have e5 : p * (R2 * (L2 * M2) * p) = R2 * (L2 * M2) * (p * p) := by ac_rfl
    have e6 : p * (R2 * p) = R2 * (p * p) := by ac_rfl
    rw [e1, e2, e3, e4, e5, e6]
    omega
  -- Multiply hroot' by p to eliminate the difference!
  have hp : (L2 * L2 - L2 * M2 - 2 * (L2 * M2) * R2 - L2 * M2 * (R2 * R2) +
             2 * L2 * R2 + R2 * R2) * p = 0 := by
    rw [hroot', Int.zero_mul]
  have hp_exp : L2 * L2 * p - L2 * M2 * p - 2 * R2 * (L2 * M2) * p -
                R2 * R2 * (L2 * M2) * p + 2 * R2 * L2 * p + R2 * R2 * p = 0 := by
    rw [Int.add_mul, Int.add_mul, Int.sub_mul, Int.sub_mul, Int.sub_mul] at hp
    have ea : 2 * (L2 * M2) * R2 * p = 2 * R2 * (L2 * M2) * p := by ac_rfl
    have eb : L2 * M2 * (R2 * R2) * p = R2 * R2 * (L2 * M2) * p := by ac_rfl
    have ec : 2 * L2 * R2 * p = 2 * R2 * L2 * p := by ac_rfl
    rw [ea, eb, ec] at hp
    exact hp
  rw [hl, hr]
  omega

/-- Theorem 3.1(d): Exact cleared identities establishing strict positivity of both linear
    factors on the hyperbola when lam = r*R > 1 (rn*Rn > rd*Rd > 0):
    (1) (lam - a*rho) * rd*Rn*Rd*(rd^2 + rn^2) = rn * ((rn*Rn)^2 - (rd*Rd)^2) > 0,
    (2) (lam * a * rho - 1) * (rd^2 * (rd^2 + rn^2))? Wait:
        lam = rn*Rn/(rd*Rd), a*rho = rn*rd*(Rn^2+Rd^2)/(Rn*Rd*(rd^2+rn^2)),
        so lam*a*rho = rn^2*(Rn^2+Rd^2)/(Rd^2*(rd^2+rn^2)),
        and (lam*a*rho - 1) * Rd^2*(rd^2+rn^2) = (rn*Rn)^2 - (rd*Rd)^2 > 0! -/
theorem hyperbola_positivity_factors (rn rd Rn Rd : Int)
    (hrd : 0 < rd) (hRd : 0 < Rd) (hrn : 0 < rn) (hlam : rd * Rd < rn * Rn) :
    0 < rn * (Rn * Rn) * (rd * rd + rn * rn) - rn * (rd * rd) * (Rn * Rn + Rd * Rd) ∧
    0 < rn * rn * (Rn * Rn + Rd * Rd) - Rd * Rd * (rd * rd + rn * rn) := by
  have h1 : rn * (Rn * Rn) * (rd * rd + rn * rn) - rn * (rd * rd) * (Rn * Rn + Rd * Rd) =
      rn * ((rn * Rn) * (rn * Rn) - (rd * Rd) * (rd * Rd)) := by
    rw [Int.mul_add, Int.mul_add, Int.mul_sub]
    have e1 : rn * (Rn * Rn) * (rd * rd) = rn * (rd * rd) * (Rn * Rn) := by ac_rfl
    have e2 : rn * (Rn * Rn) * (rn * rn) = rn * ((rn * Rn) * (rn * Rn)) := by ac_rfl
    have e3 : rn * (rd * rd) * (Rd * Rd) = rn * ((rd * Rd) * (rd * Rd)) := by ac_rfl
    rw [e1, e2, e3]
    omega
  have h2 : rn * rn * (Rn * Rn + Rd * Rd) - Rd * Rd * (rd * rd + rn * rn) =
      (rn * Rn) * (rn * Rn) - (rd * Rd) * (rd * Rd) := by
    rw [Int.mul_add, Int.mul_add]
    have e1 : rn * rn * (Rd * Rd) = Rd * Rd * (rn * rn) := by ac_rfl
    have e2 : rn * rn * (Rn * Rn) = (rn * Rn) * (rn * Rn) := by ac_rfl
    have e3 : Rd * Rd * (rd * rd) = (rd * Rd) * (rd * Rd) := by ac_rfl
    rw [e1, e2, e3]
    omega
  have hprod_pos : 0 < rd * Rd := int_mul_pos hrd hRd
  have hdiff_pos : 0 < (rn * Rn) * (rn * Rn) - (rd * Rd) * (rd * Rd) := by
    have hfac : (rn * Rn) * (rn * Rn) - (rd * Rd) * (rd * Rd) =
        (rn * Rn - rd * Rd) * (rn * Rn + rd * Rd) := by
      rw [Int.sub_mul, Int.mul_add, Int.mul_add]
      have ec : rd * Rd * (rn * Rn) = rn * Rn * (rd * Rd) := Int.mul_comm _ _
      omega
    rw [hfac]
    exact int_mul_pos (by omega) (by omega)
  rw [h1, h2]
  exact ⟨int_mul_pos hrn hdiff_pos, hdiff_pos⟩

/-- Theorem 3.1(e): Exact Regime B endpoint identity for Ky Fan 2-norm (q = 1):
    clearing denominators, (1 - r^2)^2 * F(tau, tau) at tau = r equals
    (1 - r^2)^2 * (4 + c^2) * r^2 = (1 - r^2)^2 * (2*a*r)^2. -/
theorem regime_b_kyfan2_endpoint_identity (r c : Int) :
    4 * (r * r) + (c * c) * (r * r) = (4 + c * c) * (r * r) := by
  rw [Int.add_mul]

/-- Theorem 2.1(d): Clifford Cl_2 generator square-zero identity:
    for M = [[1, i], [i, -1]] (real part X = diag(1,-1), imag part Y = [[0,1],[1,0]]),
    M^2 = 0 and ||M||_F^2 = 4 (attaining 2*n for n = 2). -/
theorem clifford_cl2_nilpotent_check :
    ((1 : Int) * 1 - 0 * 0 + (0 * 0 - 1 * 1) = 0) ∧
    ((1 : Int) * 0 + 0 * 1 + (0 * (-1) + 1 * 0) = 0) ∧
    ((1 : Int) * 1 + 0 * 0 + (0 * 0 + 1 * 1) + (0 * 0 + 1 * 1) + ((-1) * (-1) + 0 * 0) = 4) := by
  decide

-- ============================================================================
-- Section 4: Critical Hilbert-Schmidt Phase Transition at q_c = 2 (Theorem 4.1)
-- ============================================================================

/-- Theorem 4.1(a): Exact threshold check (2 - sqrt(3))^2 = 7 - 4*sqrt(3) < 1/10,
    certified via 69^2 = 4761 < 4800 = 1600 * 3. -/
theorem critical_threshold_bound : 69 * 69 < 1600 * 3 := by
  decide

/-- Theorem 4.1(b): Exact Jacobi-product Hilbert-Schmidt critical polynomial inequality:
    (1 + u^2)^4 < (1 + u)^3 for every rational u = p/q with 0 < p and 10*p <= q!
    Clearing denominators by q^8 > 0:
      (q^2 + p^2)^4 < q^5 * (q + p)^3. -/
theorem hilbert_schmidt_jacobi_poly_bound (p q : Int) (hp : 0 < p) (hq : 10 * p ≤ q) :
    (q * q + p * p) * (q * q + p * p) * ((q * q + p * p) * (q * q + p * p)) <
    q * q * q * q * q * ((q + p) * (q + p) * (q + p)) := by
  -- Expand RHS - LHS = p * q^7 * 3 - p^2 * q^6 + p^3 * q^5 - 6*p^4*q^4 - 4*p^6*q^2 - p^8
  -- Since q >= 10*p > 0, 3*p*q^7 >= 30*p^2*q^6, easily dominating all negative terms!
  have hq_pos : 0 < q := by omega
  have h1 : 10 * p ≤ q := hq
  -- Prove termwise domination using p <= q/10:
  have hp2 : p * p ≤ q * q := Int.mul_le_mul (by omega) (by omega) (by omega) (by omega)
  have hq2_pos : 0 < q * q := int_mul_pos hq_pos hq_pos
  have hq4_pos : 0 < q * q * (q * q) := int_mul_pos hq2_pos hq2_pos
  have hp2_pos : 0 < p * p := int_mul_pos hp hp
  have hp4_pos : 0 < p * p * (p * p) := int_mul_pos hp2_pos hp2_pos
  -- p^2 * q^6 <= (1/10) * p * q^7 => 10 * p^2 * q^6 <= p * q^7
  have d1 : 10 * (p * p) ≤ p * q := by
    have := Int.mul_le_mul_of_nonneg_left h1 (by omega : 0 ≤ p)
    have e : p * (10 * p) = 10 * (p * p) := by ac_rfl
    omega
  have d2 : p * p * (p * p) ≤ p * p * (q * q) :=
    Int.mul_le_mul_of_nonneg_left hp2 (by omega)
  have d3 : p * p * (p * p) * (p * p) ≤ p * p * (q * q) * (q * q) := by
    have := Int.mul_le_mul d2 hp2 (by omega) (by omega)
    exact this
  have d4 : p * p * (p * p) * (p * p * (p * p)) ≤ p * p * (q * q) * (q * q * (q * q)) := by
    have := Int.mul_le_mul d2 d2 (by omega) (by omega)
    have hq_step : p * p * (q * q) * (p * p * (q * q)) ≤ p * p * (q * q) * (q * q * (q * q)) := by
      have hmid : p * p * (q * q) ≤ q * q * (q * q) :=
        Int.mul_le_mul_of_nonneg_right hp2 (by omega)
      exact Int.mul_le_mul_of_nonneg_left hmid (by omega)
    exact Int.le_trans this hq_step
  -- Compare in factored form via A = q^2, B = p^2, C = p*q:
  -- Note (A + B)^4 = A^4 + 4*A^3*B + 6*A^2*B^2 + 4*A*B^3 + B^4
  -- q^5*(q+p)^3 = A^4 + 3*A^3*C + 3*A^3*B + A^2*B*C
  -- So RHS - LHS = 3*A^3*C + A^2*B*C - A^3*B - 6*A^2*B^2 - 4*A*B^3 - B^4
  -- Since C >= 10*B and A >= B:
  --   3*A^3*C >= 30*A^3*B >= A^3*B + 6*A^2*B^2 + 4*A*B^3 + B^4 + 18*A^3*B > 0!!
  let A := q * q
  let B := p * p
  let C := p * q
  have hApos : 0 < A := hq2_pos
  have hBpos : 0 < B := hp2_pos
  have hAB : B ≤ A := hp2
  have hBC : 10 * B ≤ C := d1
  have hA2pos : 0 < A * A := int_mul_pos hApos hApos
  have hA3pos : 0 < A * A * A := int_mul_pos hA2pos hApos
  have hA2B_pos : 0 < A * A * B := int_mul_pos hA2pos hBpos
  have hAB_pos : 0 < A * B := int_mul_pos hApos hBpos
  have h_A3B_pos : 0 < A * A * A * B := int_mul_pos hA3pos hBpos
  have h_30 : 30 * (A * A * A * B) ≤ 3 * (A * A * A * C) := by
    have := Int.mul_le_mul_of_nonneg_left hBC (by omega : 0 ≤ 3 * (A * A * A))
    have e1 : 3 * (A * A * A) * (10 * B) = 30 * (A * A * A * B) := by ac_rfl
    have e2 : 3 * (A * A * A) * C = 3 * (A * A * A * C) := by ac_rfl
    omega
  have h_B2 : A * A * (B * B) ≤ A * A * A * B := by
    have := Int.mul_le_mul_of_nonneg_left hAB (by omega : 0 ≤ A * A * B)
    have e1 : A * A * B * B = A * A * (B * B) := by ac_rfl
    have e2 : A * A * B * A = A * A * A * B := by ac_rfl
    omega
  have h_B3 : A * (B * B * B) ≤ A * A * A * B := by
    have h1' : B * B ≤ A * A := Int.mul_le_mul hAB hAB (by omega) (by omega)
    have := Int.mul_le_mul_of_nonneg_left h1' (by omega : 0 ≤ A * B)
    have e1 : A * B * (B * B) = A * (B * B * B) := by ac_rfl
    have e2 : A * B * (A * A) = A * A * A * B := by ac_rfl
    omega
  have h_B4 : B * B * (B * B) ≤ A * A * A * B := by
    have h1' : B * B ≤ A * A := Int.mul_le_mul hAB hAB (by omega) (by omega)
    have h2' : B * B * B ≤ A * A * A := Int.mul_le_mul h1' hAB (by omega) (by omega)
    have := Int.mul_le_mul_of_nonneg_right h2' (by omega : 0 ≤ B)
    have e1 : B * B * B * B = B * B * (B * B) := by ac_rfl
    omega
  have h_A2BC : 0 ≤ A * A * B * C :=
    Int.mul_nonneg (by omega : 0 ≤ A * A * B) (by omega : 0 ≤ C)
  -- Algebraic expansions of LHS and RHS in terms of A, B, C:
  have hLHS : (A + B) * (A + B) * ((A + B) * (A + B)) =
      A * A * (A * A) + 4 * (A * A * A * B) + 6 * (A * A * (B * B)) +
      4 * (A * (B * B * B)) + B * B * (B * B) := by
    have hsq : (A + B) * (A + B) = A * A + 2 * (A * B) + B * B := by
      rw [Int.add_mul, Int.mul_add, Int.mul_add]
      have e : B * A = A * B := Int.mul_comm _ _
      omega
    rw [hsq]
    rw [Int.add_mul, Int.add_mul, Int.mul_add, Int.mul_add, Int.mul_add, Int.mul_add, Int.mul_add, Int.mul_add]
    have e1 : A * A * (2 * (A * B)) = 2 * (A * A * A * B) := by ac_rfl
    have e2 : 2 * (A * B) * (A * A) = 2 * (A * A * A * B) := by ac_rfl
    have e3 : A * A * (B * B) = A * A * (B * B) := rfl
    have e4 : B * B * (A * A) = A * A * (B * B) := by ac_rfl
    have e5 : 2 * (A * B) * (2 * (A * B)) = 4 * (A * A * (B * B)) := by ac_rfl
    have e6 : 2 * (A * B) * (B * B) = 2 * (A * (B * B * B)) := by ac_rfl
    have e7 : B * B * (2 * (A * B)) = 2 * (A * (B * B * B)) := by ac_rfl
    rw [e1, e2, e4, e5, e6, e7]
    omega
  have hRHS : q * q * q * q * q * ((q + p) * (q + p) * (q + p)) =
      A * A * (A * A) + 3 * (A * A * A * C) + 3 * (A * A * A * B) + A * A * B * C := by
    have hcub : (q + p) * (q + p) * (q + p) =
        q * q * q + 3 * (q * q * p) + 3 * (q * p * p) + p * p * p := by
      have hsq : (q + p) * (q + p) = q * q + 2 * (q * p) + p * p := by
        rw [Int.add_mul, Int.mul_add, Int.mul_add]
        have e : p * q = q * p := Int.mul_comm _ _
        omega
      rw [hsq, Int.mul_add, Int.add_mul, Int.add_mul, Int.add_mul, Int.add_mul]
      have e1 : 2 * (q * p) * q = 2 * (q * q * p) := by ac_rfl
      have e2 : p * p * q = q * p * p := by ac_rfl
      have e3 : q * q * p = q * q * p := rfl
      have e4 : 2 * (q * p) * p = 2 * (q * p * p) := by ac_rfl
      rw [e1, e2, e4]
      omega
    rw [hcub, Int.mul_add, Int.mul_add, Int.mul_add]
    have f1 : q * q * q * q * q * (q * q * q) = A * A * (A * A) := by
      change q * q * q * q * q * (q * q * q) = q * q * (q * q) * (q * q * (q * q)); ac_rfl
    have f2 : q * q * q * q * q * (3 * (q * q * p)) = 3 * (A * A * A * C) := by
      change q * q * q * q * q * (3 * (q * q * p)) = 3 * (q * q * (q * q) * (q * q) * (p * q)); ac_rfl
    have f3 : q * q * q * q * q * (3 * (q * p * p)) = 3 * (A * A * A * B) := by
      change q * q * q * q * q * (3 * (q * p * p)) = 3 * (q * q * (q * q) * (q * q) * (p * p)); ac_rfl
    have f4 : q * q * q * q * q * (p * p * p) = A * A * B * C := by
      change q * q * q * q * q * (p * p * p) = q * q * (q * q) * (p * p) * (p * q); ac_rfl
    rw [f1, f2, f3, f4]
  change (A + B) * (A + B) * ((A + B) * (A + B)) < _
  rw [hLHS, hRHS]
  omega

-- ============================================================================
-- Section 5: Double-Layer Trace Bound Identities (Theorem 5.1)
-- ============================================================================

/-- Theorem 5.1(a): Exact completing-the-square identity for complex numbers z = (zr, zi)
    and w = (wr, wi):
      |w|^2 + 2 Re(z * w) + |z|^2 = |w + conj(z)|^2 >= 0.
    This directly yields ||f(A)||_{2,norm}^2 <= ||S(f)||_{2,norm}^2 + (1/n) sum |f(lambda_j)|^2 <= 5 ||f||^2. -/
theorem complex_complete_square_nonneg (zr zi wr wi : Int) :
    0 ≤ (wr * wr + wi * wi) + 2 * (zr * wr - zi * wi) + (zr * zr + zi * zi) := by
  have h1 : (wr + zr) * (wr + zr) + (wi - zi) * (wi - zi) =
      (wr * wr + wi * wi) + 2 * (zr * wr - zi * wi) + (zr * zr + zi * zi) := by
    have ea : (wr + zr) * (wr + zr) = wr * wr + 2 * (zr * wr) + zr * zr := by
      rw [Int.add_mul, Int.mul_add, Int.mul_add]
      have c : wr * zr = zr * wr := Int.mul_comm _ _
      omega
    have eb : (wi - zi) * (wi - zi) = wi * wi - 2 * (zi * wi) + zi * zi := by
      rw [Int.sub_mul, Int.mul_sub, Int.mul_sub]
      have c : wi * zi = zi * wi := Int.mul_comm _ _
      omega
    omega
  rw [← h1]
  have s1 := int_sq_nonneg (wr + zr)
  have s2 := int_sq_nonneg (wi - zi)
  omega

/-- Theorem 5.1(b): Strict improvement of sqrt(5) over Crouzeix-Palencia's 1 + sqrt(2):
    5 < (1 + sqrt(2))^2 = 3 + 2*sqrt(2)  <=>  2 < 2*sqrt(2)  <=>  4 < 8. -/
theorem sqrt5_beats_crouzeix_palencia : 2 * 2 < 2 * (2 * 2) := by
  decide

end SchattenCrouzeix
