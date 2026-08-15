import Lean2dYangMills.SU2ClassHeatKernel

/-!
# The sharp class-sector transfer gap for two-dimensional SU(2)

The class heat semigroup is diagonal in the character basis. This file
isolates the spectral comparison: outside the vacuum mode, every multiplier
is bounded by the fundamental multiplier `exp (-3 t / 4)`, and equality is
attained at the fundamental character.
-/

noncomputable section

namespace Lean2dYangMills

def su2ClassCasimir (n : Nat) : Real :=
  (n : Real) * ((n : Real) + 2) / 4

def su2ClassTransferMultiplier (t : Real) (n : Nat) : Real :=
  Real.exp (-t * su2ClassCasimir n)

@[simp]
theorem su2ClassCasimir_zero : su2ClassCasimir 0 = 0 := by
  norm_num [su2ClassCasimir]

@[simp]
theorem su2ClassCasimir_one : su2ClassCasimir 1 = 3 / 4 := by
  norm_num [su2ClassCasimir]

@[simp]
theorem su2ClassTransferMultiplier_zero (t : Real) :
    su2ClassTransferMultiplier t 0 = 1 := by
  simp [su2ClassTransferMultiplier]

@[simp]
theorem su2ClassTransferMultiplier_one (t : Real) :
    su2ClassTransferMultiplier t 1 = Real.exp (-3 * t / 4) := by
  simp [su2ClassTransferMultiplier]
  ring

theorem three_quarters_le_su2ClassCasimir {n : Nat} (hn : 1 <= n) :
    (3 / 4 : Real) <= su2ClassCasimir n := by
  have hnR : (1 : Real) <= (n : Real) := by exact_mod_cast hn
  unfold su2ClassCasimir
  nlinarith

theorem su2ClassTransferMultiplier_le_fundamental
    {t : Real} (ht : 0 <= t) {n : Nat} (hn : 1 <= n) :
    su2ClassTransferMultiplier t n <= Real.exp (-3 * t / 4) := by
  unfold su2ClassTransferMultiplier
  apply Real.exp_le_exp.mpr
  have hC := three_quarters_le_su2ClassCasimir hn
  nlinarith

theorem su2ClassTransferMultiplier_bound_sharp (t : Real) :
    su2ClassTransferMultiplier t 1 = Real.exp (-3 * t / 4) := by
  exact su2ClassTransferMultiplier_one t

theorem su2ClassTransferGap_pos {t : Real} (ht : 0 < t) :
    0 < 1 - Real.exp (-3 * t / 4) := by
  have hneg : -3 * t / 4 < 0 := by nlinarith
  have hexp : Real.exp (-3 * t / 4) < 1 := by
    simpa using (Real.exp_lt_one_iff.mpr hneg)
  linarith

end Lean2dYangMills
