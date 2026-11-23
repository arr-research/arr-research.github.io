# From the Gibbs Weight to the Spectral Gap: A Machine-Checked Transfer-Matrix Identification and Spectral-Gap Chain for the Open Z_2 Ising Spin Chain

> Machine-readable rendition extracted from the hash-identified canonical PDF (`paper.pdf`). Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
From the Gibbs Weight to the Spectral Gap:
        A Machine-Checked Transfer-Matrix Identification and
                        Spectral-Gap Chain
                 for the Open Z2 Ising Spin Chain
       Verbatim Lean 4 definitions, exact machine-checked vs. analytic boundaries,
                         and reproducible axiom-oracle audit

                                              Lluis Eriksson

                                         23 November 2026 (v3)


                                                  Abstract
         We report a Lean 4 / mathlib formalization of the transfer-matrix identification and
     spectral-gap chain for the one-dimensional open-boundary Z2 Ising spin chain (one Z2 spin per
                                                                                         ∏︀𝑛−1
     time slice, 2×2 transfer operator): from the Boltzmann path weight 𝑊𝛽 (𝜎) = 𝑡=0 𝑒𝛽𝑠(𝜎𝑡 ,𝜎𝑡+1 )
     and an independently defined normalized transfer operator 𝑇𝛽 on C2 , through the com-
     puted partition function 𝑍𝑛 = 2(𝑒𝛽 + 𝑒−𝛽 )𝑛 and the Hermitian identification theorem
     E𝑛 [conj(𝐴(𝜎0 )) 𝐵(𝜎𝑛 )] = ⟨𝐴Ω, 𝑇𝛽𝑛 (𝐵Ω)⟩C (using Mathlib’s inner product, conjugate-linear in
     the first slot), to the exact two-point correlation E𝑛 [𝑓 (𝜎0 )𝑓 (𝜎𝑛 )] = (tanh 𝛽)𝑛 of the real-valued
     sign observable 𝑓 .
         We separate explicitly between machine-checked Lean 4 declarations (quoted verbatim
     from Z2Transfer.lean, SharpBridge.lean, and Z2Identification.lean, together with
     their presence in oracle_check.lean) and elementary analytic consequences proved in prose:
     specifically, Lean proves the operator norm bound ‖𝑇𝛽 − |Ω⟩⟨Ω|‖ ≤ tanh 𝛽 for 𝛽 ≥ 0 and
     the scalar positivity inequalities 0 < 1 − tanh 𝛽 (∀𝛽) and 0 < − log(tanh 𝛽) (𝛽 > 0), while
     the exact all-𝛽 eigenvalue spectrum {1, tanh 𝛽}, the distinction at 𝛽 < 0 between the abso-
     lute spectral gap 1 − | tanh 𝛽| and the algebraic eigenvalue gap 1 − tanh 𝛽, and the rank-one
     nonexistence of a finite Hermitian 𝐻 with 𝑇0 = 𝑒−𝐻 at 𝛽 = 0 are elementary analytic con-
     sequences established in Section 3. We further clarify that z2_pairing_nondegenerate cov-
     ers only time-zero single-slice observables, whereas the full positive-time Osterwalder–Seiler
     GNS quotient is nontrivial (witnessed by 𝐹 (𝜎0 , 𝜎1 ) = 𝑓 (𝜎1 ) − (tanh 𝛽)𝑓 (𝜎0 )) and is for-
     malized separately (ARR-2026-2TBRDN2DE598KSXD), and that companion reflection positivity
     (ARR-2026-10JJK0VCCS87VTQH) is not a logical dependency of this module. Nothing here is
     a claim about SU(𝑁 ), spatial-volume uniformity, continuum limits, or the Clay Yang–Mills
     problem.


1    Introduction and exact scope
Constructive lattice field theory specifies a Euclidean probability measure, whereas a mass gap is a
spectral property of a self-adjoint transfer operator. Connecting the two requires an identification
theorem expressing Euclidean expectations in the measure as matrix elements of powers of the
transfer operator, proved without circularity (without defining the measure from the operator).



                                                       1
```

---

## Page 2

```text
For the open-boundary 1D Z2 Ising spin chain on 𝑛 + 1 time slices 𝜎 : {0, . . . , 𝑛} → {0, 1}, we
define solely from exp and the bond sign 𝑠(𝑖, 𝑗) = +1 (𝑖 = 𝑗), −1 (𝑖 ̸= 𝑗):
                                            𝑛−1
                                            ∏︁                                      ∑︁
                                 𝑊𝛽 (𝜎) =         𝑒𝛽𝑠(𝜎𝑡 ,𝜎𝑡+1 ) ,       𝑍𝑛 (𝛽) =        𝑊𝛽 (𝜎),
                                            𝑡=0                                     𝜎
                   [︀                  ]︀     1 ∑︁
                 E𝑛 conj(𝐴(𝜎0 )) 𝐵(𝜎𝑛 ) =            conj(𝐴(𝜎0 )) 𝐵(𝜎𝑛 ) 𝑊𝛽 (𝜎).
                                            𝑍𝑛 (𝛽) 𝜎

(We write conj(·) explicitly rather than an overline so plain-text PDF extraction never drops
complex conjugation.) Independently, on C2 with Mathlib’s Euclidean inner product ⟨𝑥, 𝑦⟩C =
∑︀
  𝑖∈{0,1} conj(𝑥𝑖 ) 𝑦𝑖 (conjugate-linear in the first slot, linear in the second), we define

                                                              𝑒𝛽                        𝑒−𝛽
                  𝑇𝛽 = 𝑎(𝛽) 1 + 𝑏(𝛽) 𝑆,      𝑎(𝛽) =                  ,    𝑏(𝛽) =               ,
                                                         𝑒𝛽 + 𝑒−𝛽                   𝑒𝛽 + 𝑒−𝛽
where 𝑆 swaps the two coordinates.

Scope boundaries.
    1. Open 1D Z2 Ising spin chain, not 1D pure-link gauge theory. An open one-
       dimensional pure-link gauge theory has no plaquettes and every link configuration is gauge-
       equivalent; the model formalized here is the open 1D Z2 Ising spin chain.

    2. Transfer-matrix identification, not full positive-time OS reconstruction. The
       companion reflection-positivity module (ARR-2026-10JJK0VCCS87VTQH) is not imported or
       consumed by Z2Identification.lean.

    3. Temporal vs. spatial uniformity. The exact identity (tanh 𝛽)𝑛 holds for every temporal
       separation 𝑛 ∈ N; spatial-volume uniformity does not arise because each spatial slice is a
       single site (dim C2 = 2).

    4. Classical mathematics. The 1D Ising transfer matrix is textbook [2]; the candidate con-
       tribution is a replayable, non-circular Lean 4 formalization connecting the Gibbs path sum
       to operator clustering. No exhaustive priority search over all external Lean/Isabelle/Coq
       Ising formalizations is claimed, and nothing here bears on SU(𝑁 ), continuum limits, or the
       Clay problem [3].


2     Verbatim Lean 4 definitions and checked theorem signatures
To make every definition and every machine-checked statement auditable directly
from this PDF, we quote verbatim the complete definitions and theorem signatures
from YangMills/OS/SharpBridge.lean, YangMills/OS/Z2Transfer.lean, and Yang-
Mills/OS/Z2Identification.lean at archival release yang-mills-archive-v1.0 (commit
6b54eca695e96b3038ceda18276c4e28fb45983f, where these files are byte-identical to their
original freeze checkpoint bd2c18394ce8a55ec73413c11a9f311bbf002248):

-- YangMills/OS/SharpBridge.lean (lines 67-82)
noncomputable def vacuumProjectionC (Omega : H) : H ->L[Complex] H :=
  (innerSL Complex Omega).smulRight Omega
noncomputable def projectedTransferC (T : H ->L[Complex] H) (Omega : H) : H ->L[Complex] H :=


                                                     2
```

---

## Page 3

```text
T - vacuumProjectionC Omega
noncomputable def connCorrC (T : H ->L[Complex] H) (Omega : H) (v : H) (n : Nat) : Complex :=
  inner Complex v ((T ^ n) v) - inner Complex v Omega * inner Complex Omega v

-- YangMills/OS/Z2Transfer.lean (lines 74-165, 261-355)
noncomputable def invSqrtTwo : Real := (Real.sqrt 2)^(-1)
noncomputable def swapLin : EuclideanSpace Complex (Fin 2) ->l[Complex]
    EuclideanSpace Complex (Fin 2) where
  toFun := fun v => WithLp.toLp 2 (fun i => v.ofLp (1 - i)) ...
noncomputable def swapOp : EuclideanSpace Complex (Fin 2) ->L[Complex]
    EuclideanSpace Complex (Fin 2) := LinearMap.toContinuousLinearMap swapLin
noncomputable def z2Norm (beta : Real) : Real := Real.exp beta + Real.exp (-beta)
noncomputable def z2A (beta : Real) : Real := Real.exp beta / z2Norm beta
noncomputable def z2B (beta : Real) : Real := Real.exp (-beta) / z2Norm beta
noncomputable def z2TransferOp (beta : Real) :
    EuclideanSpace Complex (Fin 2) ->L[Complex] EuclideanSpace Complex (Fin 2) :=
  (z2A beta : Complex) • 1 + (z2B beta : Complex) • swapOp
noncomputable def z2Vac : EuclideanSpace Complex (Fin 2) :=
  WithLp.toLp 2 (fun _ => ((invSqrtTwo : Real) : Complex))

theorem z2TransferOp_fix (beta : Real) : z2TransferOp beta z2Vac = z2Vac
theorem z2TransferOp_selfAdjoint (beta : Real) : IsSelfAdjoint (z2TransferOp beta)
theorem z2Projected_eq (beta : Real) (v : EuclideanSpace Complex (Fin 2)) (i : Fin 2) :
    (projectedTransferC (z2TransferOp beta) z2Vac v).ofLp i
      = ((z2A beta - z2B beta : Real) : Complex) * (v.ofLp i - (v.ofLp 0 + v.ofLp 1) / 2)
theorem z2TransferOp_gap {beta : Real} (hbeta : 0 <= beta) :
    ||projectedTransferC (z2TransferOp beta) z2Vac|| <= z2A beta - z2B beta
theorem z2_clustering_of_transfer {beta : Real} (hbeta : 0 <= beta)
    (v : EuclideanSpace Complex (Fin 2)) :
    Exists fun C : Real => forall n : Nat,
      ||connCorrC (z2TransferOp beta) z2Vac v n|| <= C * (z2A beta - z2B beta) ^ n
theorem z2_spectral_gap_pos (beta : Real) : 0 < 1 - Real.tanh beta
theorem z2_mass_pos {beta : Real} (hbeta : 0 < beta) : 0 < -Real.log (Real.tanh beta)

-- YangMills/OS/Z2Identification.lean (lines 67-112, 221-422)
def z2Sign (i j : Fin 2) : Real := if i = j then 1 else -1
noncomputable def z2Bond (beta : Real) (i j : Fin 2) : Real :=
  Real.exp (beta * z2Sign i j)
noncomputable def z2PathWeight (beta : Real) {n : Nat}
    (sigma : Fin (n + 1) -> Fin 2) : Real :=
  Finset.prod Finset.univ fun t : Fin n =>
    z2Bond beta (sigma t.castSucc) (sigma t.succ)
noncomputable def z2Partition (beta : Real) (n : Nat) : Real :=
  Finset.sum Finset.univ fun sigma : Fin (n + 1) -> Fin 2 => z2PathWeight beta sigma
noncomputable def z2PathSum (beta : Real) (n : Nat) (A B : Fin 2 -> Complex) : Complex :=
  Finset.sum Finset.univ fun sigma : Fin (n + 1) -> Fin 2 =>
    (starRingEnd Complex) (A (sigma 0)) * B (sigma (Fin.last n))
      * ((z2PathWeight beta sigma : Real) : Complex)
noncomputable def z2Expect (beta : Real) (n : Nat) (A B : Fin 2 -> Complex) : Complex :=
  z2PathSum beta n A B / ((z2Partition beta n : Real) : Complex)
noncomputable def z2Vec (A : Fin 2 -> Complex) : EuclideanSpace Complex (Fin 2) :=
  WithLp.toLp 2 A
noncomputable def z2Obs (A : Fin 2 -> Complex) : EuclideanSpace Complex (Fin 2) :=
  ((invSqrtTwo : Real) : Complex) • z2Vec A
def z2SignObs : Fin 2 -> Complex := fun i => if i = 0 then 1 else -1

theorem z2Partition_eq (beta : Real) (n : Nat) :
    z2Partition beta n = 2 * (z2Norm beta) ^ n


                                                   3
```

---

## Page 4

```text
theorem z2_identification (beta : Real) (n : Nat) (A B : Fin 2 -> Complex) :
    z2Expect beta n A B = inner Complex (z2Obs A) (((z2TransferOp beta) ^ n) (z2Obs B))
theorem z2Vec_signObs_eigen (beta : Real) :
    z2TransferOp beta (z2Vec z2SignObs) = ((z2A beta - z2B beta : Real) : Complex) • z2Vec z2SignObs
theorem z2_two_point_tanh (beta : Real) (n : Nat) :
    z2Expect beta n z2SignObs z2SignObs = ((Real.tanh beta : Real) : Complex) ^ n
theorem z2_one_point_sign_eq_zero (beta : Real) (n : Nat) :
    z2Expect beta n z2SignObs (fun _ => (1 : Complex)) = 0
theorem z2_pairing_nondegenerate (beta : Real) {A : Fin 2 -> Complex}
    (h : z2Expect beta 0 A A = 0) : A = fun _ => 0

Remark 2.1 (Non-circularity check). The measure-side dependency closure is z2Expect →
{z2PathSum, z2Partition} → z2PathWeight → z2Bond → {exp, z2Sign}, containing no ref-
erence to z2TransferOp, z2A, or z2B. The two sides meet at a single bridge lemma z2Bond_eq
expressing 𝑘𝛽 (𝑖, 𝑗) = (𝑒𝛽 + 𝑒−𝛽 )(𝑎𝛿𝑖𝑗 + 𝑏(1 − 𝛿𝑖𝑗 )).


3     Machine-checked spectral theorems vs. analytic consequences
To avoid any ambiguity between kernel-checked declarations and standard mathematical deduc-
tions in prose, we separate the two explicitly.

Theorem     3.1  (Machine-checked spectral statements in Z2Transfer.lean and
Z2Identification.lean). The Lean 4 kernel verifies (with zero sorry and standard ax-
ioms only):

    1. 𝑇𝛽 Ω = Ω, 𝑇𝛽* = 𝑇𝛽 , and 𝑇𝛽 𝑓 = (tanh 𝛽)𝑓 for all 𝛽 ∈ R (z2TransferOp_fix,
       z2TransferOp_selfAdjoint, z2Vec_signObs_eigen, z2A_sub_z2B_eq_tanh);

    2. the exact componentwise identity (𝑇𝛽 − |Ω⟩⟨Ω|)𝑣 = (tanh 𝛽)(𝑣 − ⟨Ω, 𝑣⟩C Ω) for all 𝛽 ∈ R
       (z2Projected_eq);

    3. the one-sided operator-norm bound ‖𝑇𝛽 − |Ω⟩⟨Ω|‖ ≤ tanh 𝛽 < 1 for 𝛽 ≥ 0 (z2TransferOp_-
       gap, z2A_sub_z2B_lt_one);

    4. the scalar inequalities 0 < 1 − tanh 𝛽 for all 𝛽 ∈ R (z2_spectral_gap_pos) and 0 <
       − log(tanh 𝛽) for 𝛽 > 0 (z2_mass_pos);

    5. the clustering corollary z2_clustering_of_transfer for 𝛽 ≥ 0.

Proposition 3.2 (Elementary analytic consequences across 𝛽 ∈ R, proved in prose). The
following standard spectral statements follow immediately from the 2 × 2 eigendecomposition
𝑇𝛽 = 𝑃 + (tanh 𝛽)(1 − 𝑃 ) (where 𝑃 = |Ω⟩⟨Ω|, 1 − 𝑃 = |𝑒− ⟩⟨𝑒− | with 𝑒− = 2−1/2 (1, −1)),
and are not separately formalized as operator-logarithm theorems in Lean:

    1. Exact spectrum: spec(𝑇𝛽 ) = {1, tanh 𝛽} for every 𝛽 ∈ R, and ‖𝑇𝛽 − 𝑃 ‖ = | tanh 𝛽| for
       every 𝛽 ∈ R.

    2. Positive coupling (𝛽 > 0): 0 < tanh 𝛽 < 1, so 𝑇𝛽 is strictly positive definite and admits
       the unique Hermitian logarithm 𝐻 = − log(𝑇𝛽 ) = (− log tanh 𝛽)(1−𝑃 ) satisfying 𝑇𝛽 = 𝑒−𝐻 ,
       with Hamiltonian mass gap 𝑚(𝛽) = − log(tanh 𝛽) > 0.




                                                4
```

---

## Page 5

```text
3. Negative coupling (𝛽 < 0): the non-vacuum eigenvalue tanh 𝛽 is negative, so 𝑇𝛽 has
       no real self-adjoint logarithm 𝐻 with 𝑇𝛽 = 𝑒−𝐻 . Here one must distinguish the absolute
       spectral gap 1 − | tanh 𝛽| = 1 + tanh 𝛽 ∈ (0, 1) (which governs the contraction rate ‖𝑇𝛽 −
       𝑃 ‖ = | tanh 𝛽|) from the algebraic eigenvalue gap 1 − tanh 𝛽 ∈ (1, 2) (for instance, at
       tanh 𝛽 = −1/2, the absolute spectral gap is 1/2 while the algebraic eigenvalue gap is 3/2).
       The Lean lemma z2_spectral_gap_pos states only the scalar inequality 0 < 1 − tanh 𝛽.

    4. Zero coupling (𝛽 = 0): tanh 0 = 0, so 𝑇0 = 𝑃 is rank-one and singular; no finite Hermi-
       tian operator 𝐻 on C2 satisfies 𝑒−𝐻 = 𝑇0 (as 𝑒−𝐻 is always invertible). For every 𝑛 ≥ 1,
       the sign two-point correlation E𝑛 [𝑓 (𝜎0 )𝑓 (𝜎𝑛 )] = 0 and all connected two-point correlations
       across distinct sites vanish identically (whereas uncentered expectations of constant observ-
       ables remain E𝑛 [1 · 1] = 1). Restricting z2_mass_pos to 𝛽 > 0 avoids Lean’s junk value
       Real.log 0 = 0.


4     The identification theorem and exact correlation
Theorem 4.1 (Hermitian transfer-matrix identification; z2_identification). For every 𝛽 ∈ R,
every 𝑛 ∈ N, and all 𝐴, 𝐵 : {0, 1} → C,

                              E𝑛 conj(𝐴(𝜎0 )) 𝐵(𝜎𝑛 ) = ⟨𝐴Ω, 𝑇𝛽𝑛 (𝐵Ω)⟩C ,
                                    [︀               ]︀


where ⟨𝑥, 𝑦⟩C = 𝑖∈{0,1} conj(𝑥𝑖 ) 𝑦𝑖 is Mathlib’s Euclidean inner product, conjugate-linear in the
                  ∑︀

first argument (z2 _i de nt if ic at io n ).

Proof, as formalized. Split the sum over 𝜎 : Fin(𝑛 + 1) → Fin 2 at the first spin 𝜎 = (𝑠, 𝜏 ).
Factoring out the first bond 𝑘𝛽 (𝑠, 𝜏0 ) = (𝑒𝛽 + 𝑒−𝛽 )(𝑇𝛽 )𝑠,𝜏0 and using self-adjointness of 𝑇𝛽 yields
by induction on 𝑛 (z2PathSum_succ):

                            conj(𝐴(𝜎0 )) 𝐵(𝜎𝑛 ) 𝑊𝛽 (𝜎) = (𝑒𝛽 + 𝑒−𝛽 )𝑛 ⟨𝐴, 𝑇𝛽𝑛 𝐵⟩C .
                       ∑︁

                       𝜎

Setting 𝐴 = 𝐵 ≡ 1 and using 𝑇𝛽 1 = 1 gives 𝑍𝑛 (𝛽) = 2(𝑒𝛽 + 𝑒−𝛽 )𝑛 (z2Partition_eq). Divid-
ing cancels (𝑒𝛽 + 𝑒−𝛽 )𝑛 and leaves 21 ⟨𝐴, 𝑇𝛽𝑛 𝐵⟩C = ⟨2−1/2 𝐴, 𝑇𝛽𝑛 (2−1/2 𝐵)⟩C = ⟨𝐴Ω, 𝑇𝛽𝑛 (𝐵Ω)⟩C .
(Without conj(·) on 𝐴(𝜎0 ), the identity fails already at 𝑛 = 0 for 𝐴 ≡ 𝑖, 𝐵 ≡ 1, where
E0 [𝑖 · 1] = 𝑖 ̸= −𝑖 = ⟨𝑖Ω, Ω⟩C .)

Corollary 4.2 (Exact sign two-point function; z2_two_point_tanh). For the real-valued sign
observable 𝑓 (0) = +1, 𝑓 (1) = −1 (so conj(𝑓 (𝜎)) = 𝑓 (𝜎)), every 𝛽 ∈ R, and every 𝑛 ∈ N,

                            E𝑛 𝑓 (𝜎0 )𝑓 (𝜎𝑛 ) = (tanh 𝛽)𝑛 ,
                               [︀          ]︀                     [︀     ]︀
                                                                E𝑛 𝑓 (𝜎0 ) = 0

(z2 _t wo _p oi nt _t an h , z2 _o ne _p oi nt _s ig n_ eq _z er o ).

Remark 4.3 (Portability to general finite kernels). For a general finite symmetric kernel 𝐾, path
induction yields 𝑍𝑛 = 1⊤ 𝐾 𝑛 1. The power formula 𝑍𝑛 = |𝑆| 𝜆𝑛 and the uniform vacuum Ω =
|𝑆|−1/2 1 require constant row sums (𝐾1 = 𝜆1), not symmetry alone.




                                                     5
```

---

## Page 6

```text
5    Time-zero definiteness, the positive-time OS quotient, and
     clustering
Remark 5.1 (Time-zero definiteness vs. the full positive-time OS quotient). The 𝑛 = 0 instance
of Theorem 4.1 gives E0 [conj(𝐴(𝜎0 ))𝐴(𝜎0 )] = ‖𝐴Ω‖2 , so z2_pairing_nondegenerate proves
that the pairing is strictly positive definite on time-zero single-slice observables 𝐴(𝜎0 ). This
does not mean that the Osterwalder–Seiler reflection pairing on the full positive-time algebra
{𝜎0 , 𝜎1 , . . . } is definite: under site reflection across 𝑡 = 0, the nonzero observable 𝐹 (𝜎0 , 𝜎1 ) :=
𝑓 (𝜎1 ) − (tanh 𝛽)𝑓 (𝜎0 ) satisfies E[𝐹 | 𝜎0 ] = 0 for every finite 𝛽, hence has zero reflected norm
E[conj(𝜃𝐹 ) 𝐹 ] = 0 by Markov conditional independence across 𝜎0 . Thus the full positive-time
GNS quotient is nontrivial even for the 1D Ising chain and is formalized separately (ARR-2026-
2TBRDN2DE598KSXD).
Remark 5.2 (Algebraic structure of 𝑇𝛽 and role of the abstract clustering criterion). With 𝑃 =
|Ω⟩⟨Ω| and 𝑟 = tanh 𝛽 = 𝑎−𝑏, algebraically 𝑇𝛽 = 𝑃 +𝑟(1−𝑃 ) = 𝑟1+(1−𝑟)𝑃 . The distinction from
earlier toy witnesses is constructive, not algebraic: 𝑇𝛽 is built from the Boltzmann bond weights
𝑒±𝛽 rather than taking a target rate 𝑟 as input. Finally, z2_two_point_tanh is proved directly
from the eigenfunction 𝑇𝛽 𝑓 = (tanh 𝛽)𝑓 ; the separate corollary z2_clustering_of_transfer
feeds 𝑇𝛽 into the abstract dense-family clustering criterion connCorrC_le_of_gap (ARR-2026-
31ED4MTKC18JPSDE) for arbitrary 𝑣 ∈ C2 and 𝛽 ≥ 0, rather than serving as a dependency of
Corollary 4.2.


6    Source-pinned declaration manifest and reproducibility
All Lean files live in https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME. Both
YangMills/OS/Z2Transfer.lean and YangMills/OS/Z2Identification.lean were frozen at
commit bd2c18394ce8a55ec73413c11a9f311bbf002248 and remain byte-identical at archival re-
lease yang-mills-archive-v1.0 (commit 6b54eca695e96b3038ceda18276c4e28fb45983f, Lean
v4.29.0-rc6, pinned Mathlib 07642720480157414db592fa85b626dafb71355b). Every theorem
in Theorem 3.1 and Section 4 compiles inside YangMillsCore, and the five headline theorems
(z2Partition_eq, z2_identification, z2_two_point_tanh, z2TransferOp_gap, z2_mass_-
pos) are audited directly by #print axioms inside the root oracle_check.lean validated by
scripts/check_oracle_output.py.
    Reproduce the build and verify the axiom output locally (on Windows include -c
core.longpaths=true):
git clone -c core.longpaths=true \
  https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME.git
cd THE-ERIKSSON-PROGRAMME && git checkout yang-mills-archive-v1.0
lake exe cache get && lake build YangMillsCore
lake env lean oracle_check.lean > oracle-output.txt
python scripts/check_oracle_output.py --output oracle-output.txt

GitHub Actions (lean-build.yml) runs this exact build-and-oracle check on main, rejecting any
sorryAx or non-standard axiom outside [propext, Classical.choice, Quot.sound].

Disclosure
Large language models assisted Lean 4 formalization and manuscript editing under author su-
pervision; every theorem in Section 2 is checked by the Lean 4 kernel. Author Lluis Eriksson


                                                    6
```

---

## Page 7

```text
administers AIRR (https://airr.science/); no independent editorial admission or human peer
review is claimed.


References
[1] K. Osterwalder and E. Seiler, Gauge field theories on a lattice, Annals of Physics 110 (1978), 440–471.

[2] B. Simon, The Statistical Mechanics of Lattice Gases, Volume I, Princeton University Press, 1993.

[3] A. Jaffe and E. Witten, Quantum Yang–Mills theory, Clay Mathematics Institute Millennium Prize
    Problem description, 2000.

[4] L. de Moura and S. Ullrich, The Lean 4 theorem prover and programming language, CADE-28, LNCS
    12699 (2021), 625–635.




                                                    7
```
