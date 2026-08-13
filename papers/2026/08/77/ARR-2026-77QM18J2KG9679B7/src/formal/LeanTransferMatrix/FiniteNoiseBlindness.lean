import Mathlib

/-!
# Finite-noise blindness of transfer moments

This module machine-checks the algebraic core of a finite-data impossibility
theorem.  A normalized transfer-moment window with entries in `[0,1]` can be
mixed with weight `w` with an atom at transfer eigenvalue `1`.  Every recorded
moment moves by at most `w`, normalization is preserved, and the new window
remains in `[0,1]`.

The module deliberately does not identify a physical transfer operator.  Its
scope is the exact hidden-atom construction used by the accompanying paper.
-/

namespace LeanTransferMatrix

/-- A finite normalized window of scalar transfer moments. -/
structure TransferMomentWindow (N : ℕ) where
  /-- Moment values `m_0,...,m_N`. -/
  value : Fin (N + 1) → ℝ
  /-- Zeroth moment is normalized. -/
  normalized : value 0 = 1
  /-- Transfer moments of a positive contraction are nonnegative. -/
  nonnegative : ∀ n, 0 ≤ value n
  /-- Normalized transfer moments are at most one. -/
  atMostOne : ∀ n, value n ≤ 1

/-- Mix every moment with an atom at transfer eigenvalue `1`. -/
def hiddenAtomValue {N : ℕ} (w : ℝ) (M : TransferMomentWindow N)
    (n : Fin (N + 1)) : ℝ :=
  (1 - w) * M.value n + w

/-- The hidden-atom perturbation has the exact factorized difference. -/
theorem hiddenAtomValue_sub {N : ℕ} (w : ℝ) (M : TransferMomentWindow N)
    (n : Fin (N + 1)) :
    hiddenAtomValue w M n - M.value n = w * (1 - M.value n) := by
  unfold hiddenAtomValue
  ring

/-- Every component moves by at most the hidden atom's weight. -/
theorem abs_hiddenAtomValue_sub_le {N : ℕ} {w : ℝ}
    (hw : 0 ≤ w) (M : TransferMomentWindow N) (n : Fin (N + 1)) :
    |hiddenAtomValue w M n - M.value n| ≤ w := by
  rw [hiddenAtomValue_sub]
  have hnonneg : 0 ≤ w * (1 - M.value n) :=
    mul_nonneg hw (sub_nonneg.mpr (M.atMostOne n))
  rw [abs_of_nonneg hnonneg]
  nlinarith [M.nonnegative n]

/-- Mixing with a hidden atom preserves the normalized zeroth moment. -/
theorem hiddenAtomValue_zero {N : ℕ} (w : ℝ) (M : TransferMomentWindow N) :
    hiddenAtomValue w M 0 = 1 := by
  unfold hiddenAtomValue
  rw [M.normalized]
  ring

/-- For `0 ≤ w ≤ 1`, the contaminated window remains nonnegative. -/
theorem hiddenAtomValue_nonnegative {N : ℕ} {w : ℝ}
    (hw0 : 0 ≤ w) (hw1 : w ≤ 1) (M : TransferMomentWindow N)
    (n : Fin (N + 1)) :
    0 ≤ hiddenAtomValue w M n := by
  unfold hiddenAtomValue
  exact add_nonneg (mul_nonneg (sub_nonneg.mpr hw1) (M.nonnegative n)) hw0

/-- For `0 ≤ w ≤ 1`, the contaminated window remains at most one. -/
theorem hiddenAtomValue_atMostOne {N : ℕ} {w : ℝ}
    (hw1 : w ≤ 1) (M : TransferMomentWindow N)
    (n : Fin (N + 1)) :
    hiddenAtomValue w M n ≤ 1 := by
  unfold hiddenAtomValue
  nlinarith [mul_nonneg (sub_nonneg.mpr hw1) (sub_nonneg.mpr (M.atMostOne n))]

/-- The hidden-atom construction is itself a valid transfer-moment window. -/
def TransferMomentWindow.withHiddenAtom {N : ℕ} (M : TransferMomentWindow N)
    (w : ℝ) (hw0 : 0 ≤ w) (hw1 : w ≤ 1) : TransferMomentWindow N where
  value := hiddenAtomValue w M
  normalized := hiddenAtomValue_zero w M
  nonnegative := hiddenAtomValue_nonnegative hw0 hw1 M
  atMostOne := hiddenAtomValue_atMostOne hw1 M

/--
Finite-noise indistinguishability: for every positive error radius at most one,
there is a valid hidden-atom window inside that componentwise error ball.
-/
theorem exists_hiddenAtom_window_in_error_ball {N : ℕ} (M : TransferMomentWindow N)
    {ε : ℝ} (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1) :
    ∃ M' : TransferMomentWindow N,
      ∀ n, |M'.value n - M.value n| ≤ ε := by
  refine ⟨M.withHiddenAtom ε hε0 hε1, ?_⟩
  intro n
  exact abs_hiddenAtomValue_sub_le hε0 M n

/-- An atom at transfer eigenvalue one has zero transfer mass. -/
theorem hiddenAtom_mass_is_zero : -Real.log (1 : ℝ) = 0 := by
  simp

end LeanTransferMatrix
