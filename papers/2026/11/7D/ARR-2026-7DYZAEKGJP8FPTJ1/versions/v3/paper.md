# The Eriksson Programme (Yang-Mills): Auditable Claim-to-Theorem Manifest, Certified Obstructions, and Continuation Frontier (Release yang-mills-archive-v1.0)

> Machine-readable rendition extracted from the hash-identified canonical PDF (`paper.pdf`). Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
The Eriksson Programme (Yang–Mills):
      Auditable Claim-to-Theorem Manifest, Certified Obstructions,
    and Continuation Frontier (Release yang-mills-archive-v1.0)

                                               Lluis Eriksson
                                       Independent Researcher, Sweden

                                         23 November 2026 (v3)


                                                  Abstract
          This archival technical note provides a self-contained, auditable claim-to-theorem
      specification and continuation handoff for the Yang–Mills Lean 4 formalization in-
      side THE-ERIKSSON-PROGRAMME at archival release yang-mills-archive-v1.0 (com-
      mit     6b54eca695e96b3038ceda18276c4e28fb45983f;              canonical   Lean      core     check-
      point 02fae0ad in project-state.json,                 Lean v4.29.0-rc6,         pinned mathlib
      07642720480157414db592fa85b626dafb71355b).             Responding to every material objection
      raised by hostile reviews of v1 and v2, this v3 revision supplies exact fully-qualified Lean 4
      theorem statements and complete hypotheses (including the complex modulus and all four
      KP inequalities in the exact-action Wilson-loop area law, the unspannable-chain behavior of
      chainAreaA, the 𝛽 > 0 hypothesis and literal definitions of SingleScaleUVDecay and covUV_-
      concrete in the marginal RG conditional, the unweighted Poincaré predicate vs. penalized
      coercivity and exact scale quantifiers in the Poincaré walls, the explicit transverse periodic
      Fourier witness 𝐴(ℓ) ∈ ker 𝑄ℓ for the flat Hodge factorized-penalty wall, the explicit AmosBound
      inequality, and the CompatibleLocalObservable thermodynamic-limit substrate), a declaration-
      level audit-coverage table distinguishing root oracle_check.lean (2,851 readouts across 46
      imports), per-module oracles, and compiled-only modules, and a reconciled cross-reference of all
      33 companion mathematical-physics repository folders to their 33 live AIRR identifiers.
          The verified core proves fixed-spacing lattice results only: a Kotecký–Preiss / Mayer–Ursell
      polymer engine; volume-uniform strong-coupling SU(𝑁𝑐 ) Wilson-loop area laws and exponential
      clustering of truncated two-plaquette correlations without Peter–Weyl; explicit strictly-interacting
      SU(2) thermodynamic-limit witnesses in 𝑑 = 2 (0 < |𝛽| ≤ 10−5 ) and 𝑑 = 4 (0 < |𝛽| ≤ 10−6 );
      exact Z𝑛 centre-symmetry selection rules; conditional real-sequence 4D marginal-coupling UV-
      summation theorems; real-order Amos/Bessel ratio bounds; and a transfer-matrix identification
      chain for the 1D open Z2 Ising spin chain. No four-dimensional continuum limit (𝑎 → 0), no
      physical SU(𝑁 ) Osterwalder–Schrader or Wightman reconstruction, and no solution to the Clay
      Millennium Yang–Mills Mass Gap problem is claimed.


1     Verification Architecture and Declaration-Level Coverage
Release yang-mills-archive-v1.0 maintains four distinct automated layers, which must not be
conflated:

    1. Root axiom oracle (oracle_check.lean, checked by lean-build.yml): imports Yang-
       MillsCore plus 45 explicit YangMills.{OS,RG,Paper,SUSY}.* modules (46 imports total) and
       executes 2,851 #print axioms readouts. scripts/check_oracle_output.py parses the Lean

                                                       1
```

---

## Page 2

```text
stdout and fails on any sorryAx, non-standard axiom outside [propext, Classical.choice,
      Quot.sound], warning, or missing/reordered readout.

    2. Per-module axiom oracles:              separate oracle files audit specialized                 tracks,
       notably   AmosClosure/Oracle.lean         (real/integer  Amos       suite)     and              Yang-
       Mills/RG/UniformPhysicalCoarseRankWallOracle.lean             (plus        sister               Yang-
       Mills/RG/*Oracle.lean files for the flat Hodge/coarse-rank obstructions).

    3. Core-compiled declarations outside the root oracle: modules compiled by lake build
       YangMillsCore (e.g. ThermodynamicLimit.lean, ThermodynamicNonvacuity.lean, Physi-
       calPoincareWall.lean) are kernel-checked at build time and scanned by scripts/check_-
       consistency.py for sorry and axiom, but are not listed in the root oracle_check.lean.

    4. Standalone / branch-only modules (outside YangMillsCore): the finite SU(2) cylin-
       der modules (R1/R2, Sept 2026) and draft PR #29 (hRpoly) are excluded from Yang-
       MillsCore.lean.

    Table 1 maps each headline claim in Sections 2–3 to its exact Lean declaration and verification
tier.

Headline Claim                  Fully-Qualified Lean Declaration                  Audit Tier
KP / Mayer inversion            YangMills.KP.partition_eq_exp_clusterSum_of_      Root oracle_check.lean
                                kp
Volume-uniform area law         YangMills.normalized_exp_wilson_loop_area_la      Root oracle_check.lean
                                w
Exp. area-law decay             YangMills.area_law_to_exp_area_decay              Root oracle_check.lean
SU(𝑁𝑐 ) 2-plaquette decay       YangMills.sun_two_plaquette_correlator_bound      Root oracle_check.lean
Fixed-lattice clustering        YangMills.sun_lattice_exponential_clustering      Root oracle_check.lean
Z𝑛 centre selection             YangMills.integral_wilsonLoopSU_listProd_gib      Root oracle_check.lean
                                bs_eq_zero
Marginal RG conditional         YangMills.RG.lattice_mass_gap_of_singleScale      Root oracle_check.lean
                                UVDecay_marginal
1D Z2 transfer chain            YangMills.OS.z2_identification,                   Root oracle_check.lean
                                z2_two_point_tanh, z2TransferOp_gap,
                                z2_mass_pos
Thermodynamic limit             YangMills.WindowPolymer.infiniteLocalGibbsSt      Compiled (YangMillsCore)
                                ate
SU(2) 𝑑 = 2, 4 witnesses        YangMills.su2D4InfiniteLocalGibbsStateOnPunc      Compiled (YangMillsCore)
                                turedInterval
Real-order Amos suite           AmosClosure.amosBoundReal_holds,                  AmosClosure/Oracle.lean
                                besselIReal_unit_step
Poincaré walls                  YangMills/RG/PhysicalPoincareWall.lean,           Compiled (YangMillsCore)
                                PhysicalPoincareLowModeFalsifier.lean
Flat coarse-rank wall           YangMills/RG/UniformPhysicalCoarseRankWall.l      UniformPhysicalCoarseRankW
                                ean                                               allOracle.lean
                        Table    1:      Declaration-level   mapping    between     head-
                        line  claims  and    automated     audit coverage   at    commit
                        6b54eca695e96b3038ceda18276c4e28fb45983f.




2     Auditable Claim-to-Theorem Manifest
Every statement below quotes the exact mathematical content and hypotheses of the corresponding
Lean 4 declaration at commit 6b54eca695e96b3038ceda18276c4e28fb45983f. No prior-work pri-


                                                       2
```

---

## Page 3

```text
ority claim is made for the classical lattice theorems; the contribution is Lean 4 mechanization and
the certified obstruction map.

2.1   KP / Mayer polymer engine (YangMills/KP/)
  • YangMills.KP.partition_eq_exp_clusterSum_of_kp (KP/MayerInversion.lean): for
    any finite polymer model 𝑃 ([Fintype P.Polymer]) and weight 𝑎 : 𝑃.Polymer → R satis-
    fying KPCriterion P a, the polymer partition function equals Ξ = exp(clusterSum 𝑃 ) with
    absolutely summable cluster series, backed by Penrose’s tree-graph bound (abs_ursell_le_-
    card_spanningTrees).

2.2   Strong-coupling SU(𝑁𝑐 ) area law, IR clustering, thermodynamic limit, and
      centre selection
  • Volume-uniform exact-action Wilson-loop area law (YangMills.normalized_exp_wil
    son_loop_area_law, L1_GibbsMeasure/RestrictedGate.lean): let 𝑑, 𝑁, 𝑁𝑐 ≥ 1 ([NeZero
    d] [NeZero N] [NeZero N_c]), let 𝑒𝑠 : List (ConcreteEdge 𝑑 𝑁 ) be an arbitrary edge list,
    let 𝛿 ≥ 0, 𝑐, 𝑐′ : ConcretePlaquette 𝑑 𝑁 → C satisfy ‖𝑐𝑝 ‖ ≤ 𝛿, ‖𝑐′𝑝 ‖ ≤ 𝛿, and 𝑐′𝑝 = conj(𝑐𝑝 ),
    and let 𝑡, 𝜀 ≥ 0, 𝜎 ∈ [0, 1]. Define the activity bound 𝑢 := 𝑒2𝛿𝑁𝑐 − 1 and require all four
    volume-independent inequalities:

                                                                       𝑢 𝑒𝑡+𝜀+1
                        (16𝑑 + 1)2 𝑢 𝑒𝑡+𝜀+1 < 1,          16𝑑                           ≤ 𝑡,
                                                                1 − (16𝑑 + 1)2 𝑢 𝑒𝑡+𝜀+1
                                                      (︃                            )︃
                                                                   𝑢 𝑒𝑡
                        (16𝑑 + 1) 𝜎 < 1,
                                  2
                                                𝑢 exp 16𝑑 𝑒                              ≤ 𝜎2.
                                                            1 − (16𝑑 + 1)2 𝑢 𝑒𝑡
                                      𝑡
      Set 𝐾1         :=              𝑢𝑒
                              𝑒 1−(16𝑑+1)2 𝑢𝑒𝑡  and 𝐾2     :=         𝜎
                                                                 1−(16𝑑+1)2 𝜎
                                                                              , and let 𝑍      :=
      weightedPartition(𝜇SU(𝑁𝑐 ) , expReActivity 𝑁𝑐 𝑐) > 0.               Then the complex mod-
      ulus of    the   normalized      expectation  under the exact   plaquette  action 𝑊𝑐 (𝐴) :=
        𝑝 exp 𝑐𝑝 tr(𝑈𝑝 ) + 𝑐𝑝 conj(tr(𝑈𝑝 )) satisfies
                            ′
      ∏︀     (︀                              )︀


        ⃦1
        ⃦ ∫︁                        ⃦
                                            4𝑑 |edgeSupport(𝑒𝑠)|(𝐾1 +𝐾2 ) chainAreaAZ/𝑁𝑐 Z (loopChain(𝑒𝑠))
             tr(𝑈𝑒𝑠 ) 𝑊𝑐 (𝐴) 𝑑𝜇Haar ⃦
                                    ⃦
                                    ⃦ ≤ 𝑁𝑐 𝑒                             𝜎                                 .
        ⃦
        ⃦𝑍

      Here chainAreaA (L0_Lattice/ChainComplex.lean) is defined as Nat.sInf{𝑛 ∈ N | ∃𝑠 : 𝑃 →
      Z/𝑁𝑐 Z, 𝜕2anti 𝑠 = 𝑐 ∧ |supp(𝑠)| = 𝑛}. For unspannable 1-chains (such as open edge words or
      homologically nontrivial torus cycles), the set is empty and Lean’s Nat.sInf returns the junk
      value 0, so 𝜎 0 = 1 and the inequality holds trivially with no area suppression. Likewise, a
      twice-traversed SU(2) loop has loopChainZ/2Z = 0, hence chainAreaA = 0 (𝜎 0 = 1), consistent
      with the free (𝛽 = 0) Haar value E[tr(𝑈𝐶2 )/2] = −1/2 for any simple (non-backtracking) loop
      𝐶 whose holonomy 𝑈𝐶 is Haar-distributed on SU(2).

  • Unconditional SU(𝑁𝑐 ) two-plaquette exponential clustering without Peter–Weyl
    (YangMills.two_plaquette_correlator_bound and its SU(𝑁𝑐 ) specialization YangMills.su
    n_two_plaquette_correlator_bound, L1_GibbsMeasure/TwoPlaquetteCorrelator.lean):
    for any measurable 𝑓 : SU(𝑁𝑐 ) → R with |𝑓 | ≤ 1, any 𝑠 > 0, 𝛽 ∈ R, 𝑡, 𝜀 ≥ 0, setting
                                                        𝑣 𝑒𝑡+𝜀+1
    𝑣 := (𝑒|𝛽|𝑁𝑐 − 1) + 𝑠 + (𝑒|𝛽|𝑁𝑐 − 1)𝑠 and 𝑄 := 1−(16𝑑+1) 2 𝑣 𝑒𝑡+𝜀+1 , assume (16𝑑 + 1) 𝑣 𝑒
                                                                                          2   𝑡+𝜀+1 < 1,

      16𝑑 𝑄 ≤ 𝑡, and the paired distance condition 4𝑒−𝜀𝑘 𝑄 ≤ 1 for distinct plaquettes 𝑝 ̸= 𝑞 with



                                                      3
```

---

## Page 4

```text
2𝑘 ≤ disttouchGraph (𝑝, 𝑞). Then the unnormalized connected correlator satisfies

               ⃒⟨𝑓 (𝑈𝑝 )𝑓 (𝑈𝑞 )⟩unnorm 𝑍 − ⟨𝑓 (𝑈𝑝 )⟩unnorm ⟨𝑓 (𝑈𝑞 )⟩unnorm ⃒ ≤ 8𝑄(1 + 𝑠) 𝑍 𝑒−𝜀𝑘 .
               ⃒                                                           ⃒            2 2

                                                                                         𝑠2
      (The theorem allows 𝜀 ≥ 0; nontrivial exponential decay requires choosing 𝜀 > 0, as supplied
      by the concrete witnesses below.)

  • Fixed-spacing thermodynamic limit and strictly-interacting SU(2) witnesses
    (LocalObservableSubstrate.lean, ThermodynamicLimit.lean, ThermodynamicNonvacu-
    ity.lean): observables belong to CompatibleLocalObservable d G — a finite edge support
    Support embedded injectively into (N𝑑 × Fin 𝑑) inside a box of side minVolume + 1, equipped
    with a measurable bounded kernel 𝐾 : (Support → 𝐺) → R (|𝐾| ≤ 𝐵) realized on periodic
    tori of side 𝑛 + 1 ≥ minVolume + 1 via modulo coordinate reduction edgeAt. Under Uni-
    formLocalKPRegime d B beta (with 𝜀 > 0, 𝜂 > 0), finite-torus expectations form a Cauchy
    sequence in R with exponential tail control as 𝑛 → ∞, converging pointwise on Compatible-
    LocalObservable d G to a linear, positive, normalized, translation-invariant functional Posi-
    tiveNormalizedLocalState d G (YangMills.WindowPolymer.infiniteLocalGibbsState),
    and transferring two-plaquette clustering to the infinite-volume state. ThermodynamicNonva-
    cuity.lean constructs two concrete strictly-interacting SU(2) families (nonconstant plaquette
    energy Re tr 𝑈 , 𝐵 = 2, 𝑡 = 𝜀 = 𝜂 = 10−2 > 0, explicitly requiring 0 < |𝛽|):

        – 𝑑 = 2, 0 < |𝛽| ≤ 10−5 : su2InfiniteLocalGibbsStateOnPuncturedInterval;
        – 𝑑 = 4, 0 < |𝛽| ≤ 10−6 : su2D4InfiniteLocalGibbsStateOnPuncturedInterval.

      Both instantiate PositiveNormalizedLocalState d SU2GaugeGroup with strictly positive de-
      cay parameter 𝜀 = 10−2 and nonzero coupling.

  • Exact Z𝑛 centre-symmetry selection rules (L1_GibbsMeasure/GibbsSelectionRule.lean,
    e.g. integral_wilsonLoopSU_gibbs_eq_zero and integral_wilsonLoopSU_listProd
    _gibbs_eq_zero): multiplying every positively oriented edge by 𝜔 = 𝑒2𝜋𝑖/𝑛 𝐼𝑛 ∈ 𝑍(SU(𝑛))
    leaves every plaquette invariant for all 𝛽 ∈ R (two forward and two backward edges), while
    any positively-oriented edge list 𝑒𝑠 acquires factor 𝜔 |𝑒𝑠| , forcing vanishing interacting Gibbs
    expectation whenever 𝑛 ∤ |𝑒𝑠|.

2.3   Conditional 4D marginal-coupling RG assembly (YangMills/RG/)
  • YangMills.RG.lattice_mass_gap_of_cluster_and_marginal_coupling and lattice_ma
    ss_gap_of_singleScaleUVDecay_marginal (RG/MarginalUVMassGap.lean:111–148): given
    real sequences covIR, 𝑔 : N → R, 𝑅sc : N → N → R, 𝑛sc : N → N, define
                                                               𝑛sc (𝑡)−1
                               covUV_concrete 𝑅sc 𝑛sc 𝑡 :=                 𝑅sc (𝑡, 𝑘),
                                                                 ∑︁

                                                                 𝑘=0

      and the predicate

            SingleScaleUVDecay 𝑅sc 𝑔 𝐶2 𝑐0 𝜅0 :⇐⇒ ∀𝑡, 𝑘 ∈ N, |𝑅sc (𝑡, 𝑘)| ≤ 𝐶2 𝑒−𝑐0 𝑡 𝑔𝑘𝜅0 .
                                                                                          (︀   )︀


      Under the complete hypotheses 0 < 𝜀, 0 < 𝑐0 , 0 ≤ 𝐶2 , 1 < 𝜅0 , 0 < 𝛽, ∀𝑘, 0 < 𝑔𝑘 , ∀𝑘, 𝛽𝑔𝑘 < 1,
      ∀𝑘, 𝑔𝑘+1 = 𝑔𝑘 (1 − 𝛽𝑔𝑘 ), ∀𝑘, |covIR𝑘 | ≤ 𝐶1 𝑒−𝜀𝑘 , and SingleScaleUVDecay Rsc g C2 c0
      kappa0, the theorem derives 1/𝑔𝑘 ≥ 1/𝑔0 + 𝛽𝑘 (hence 𝑔𝑘 = 𝑂(1/𝑘), so ∞         𝜅0
                                                                               𝑘=0 𝑔𝑘 < ∞ whenever
                                                                             ∑︀


                                                    4
```

---

## Page 5

```text
𝜅0 > 1 by 𝑝-series comparison, whereas at 𝜅0 = 1 this 𝑂(1/𝑘) upper bound is not summable)
       and concludes:
                                                                   ⃒ (︁        ∞      )︁
           ∃ gap > 0, ∀𝑡 ∈ N,    ⃒covIR𝑡 + covUV_concrete 𝑅sc 𝑛sc 𝑡⃒ ≤ 𝐶1 + 𝐶2    𝑔 𝜅0 𝑒−gap·𝑡 .
                                 ⃒                                             ∑︁
                                                                                             𝑘
                                                                                       𝑘=0

       This is an abstract real-sequence assembly mentioning no gauge group or Hilbert space; dis-
       charging the physical single-scale input hRpoly remains open.

2.4    Real-order Amos/Bessel suite and 1D Z2 transfer chain
    • Real-order Amos bounds (AmosClosure/Core.lean, AmosBarrierReal.lean): defining
      𝜓𝜈 (𝑥) = 𝑥(𝑟𝜈 (𝑥)−1 − 𝑟𝜈 (𝑥)) for 𝑟𝜈 (𝑥) = 𝐼𝜈+1 (𝑥)/𝐼𝜈 (𝑥) and
                                                                      𝑥
                           AmosBound 𝜈 𝑥 𝑟 :⇐⇒ 𝑟 <                 √︁              ,
                                                          𝜈 + 12 + (𝜈 + 12 )2 + 𝑥2
       the Lean suite proves 2𝜈 + 1 < 𝜓𝜈 (𝑥) (besselPsiReal_gt), AmosBound for 𝑟𝜈 (𝑥) (amosBoundR
       eal_holds), and the unit-step bound 𝑟𝜈 (𝑥) − 𝑟𝜈+1 (𝑥) < 1/𝑥 (besselIReal_unit_step) for all
       real 𝜈 ≥ 0 and all 𝑥 > 0 (audited in AmosClosure/Oracle.lean).
    • 1D open Z2 Ising transfer-matrix chain (ARR-2026-7PRDH0DHH280HRKH v3): machine-
      checks 𝑍𝑛 = 2(𝑒𝛽 + 𝑒−𝛽 )𝑛 , E𝑛 [conj(𝐴(𝜎0 ))𝐵(𝜎𝑛 )] = ⟨𝐴Ω, 𝑇𝛽𝑛 (𝐵Ω)⟩C , E𝑛 [𝑓 (𝜎0 )𝑓 (𝜎𝑛 )] =
      (tanh 𝛽)𝑛 , ‖𝑇𝛽 − 𝑃 ‖ ≤ tanh 𝛽 (𝛽 ≥ 0), and time-zero pairing non-degeneracy. Analytically,
      1 − | tanh 𝛽| is the absolute spectral gap across all 𝛽; for 𝛽 < 0 the non-vacuum eigenvalue
      tanh 𝛽 is negative, so 𝑇𝛽 has no self-adjoint real logarithm 𝐻 with 𝑒−𝐻 = 𝑇𝛽 . Positive kernel
      entries alone do not imply reflection positivity, and finite-extent Perron isolation does not imply
      a uniform gap.


3     Certified Negative Results and Exact Obstruction Classes
    1. Volume-uniform Poincaré walls (ARR-2026-3Q0VH7PMNV8C9VQE): on the unit-spacing pe-
                                                                                2
       riodic torus Λ𝐿𝑁 ′ = (Z/𝐿𝑁 ′ Z)𝑑 (𝑑 ≥ 3, 𝑁𝑐 ≥ 2, internal space R𝑁𝑐 −1 with concrete ma-
       tricial su(𝑁𝑐 ) adjoint model), let 𝐾0 = 𝐷1† 𝐷1 + 𝐷0 𝐷0† be the flat lattice Hodge operator
       (⟨𝐴, 𝐾0 𝐴⟩ = ‖curl 𝐴‖2 + ‖div 𝐴‖2 ) and let 𝑄 be the unscaled line-integral block map satisfying
       𝑄(𝐴𝑣 ) = 𝐿 𝐴coarse
                     𝑣     on direction-wise constants. The formalized Poincaré predicate FlatGauge-
       HodgePoincare d L N’ Nc rho CP is the unweighted inequality
                            0 < 𝐶𝑃               ‖𝐴‖2 ≤ 𝐶𝑃 ⟨𝐴, 𝐾0 𝐴⟩ + ‖𝑄𝐴‖2 ,
                                                             (︀                   )︀
                                      ∧    ∀𝐴,
       which feeds coercivity 𝑐 = min(1, 𝑎)/𝐶𝑃 to the penalized covariance 𝐾 = 𝐾0 + 𝑎𝑄† 𝑄 (𝑎 > 0).
       Two walls refute uniformity as block side grows:
         • Constant-sector wall: on side 𝐿𝑁 ′ for any fixed 𝑁 ′ ≥ 1, testing on 𝐴𝑣 (⟨𝐴𝑣 , 𝐾0 𝐴𝑣 ⟩ = 0,
           ‖𝐴𝑣 ‖2 = (𝐿𝑁 ′ )𝑑 ‖𝑣‖2 , ‖𝑄𝐴𝑣 ‖2 = 𝐿2 (𝑁 ′ )𝑑 ‖𝑣‖2 ) forces 𝐶𝑃 ≥ 𝐿𝑑 /𝐿2 = 𝐿𝑑−2 → ∞ as
           𝐿 → ∞ (this refutes uniformity in 𝐿, not in 𝑁 ′ at fixed 𝐿).
         • Fluctuation-sector wall: restricting to cochains orthogonal to constants on even block
           side 𝐿 = 2𝑀 (fine side (2𝑀 )𝑁 ′ , any fixed 𝑁 ′ ≥ 1), a transported half-period square-wave
           mode satisfies ‖𝑄𝐴‖2 ≤ (2𝑀 )−1 ‖𝐴‖2 and ⟨𝐴, 𝐾0 𝐴⟩ = 8((2𝑀 )𝑁 ′ )−1 ‖𝐴‖2 . Because the
           Poincaré(︀predicate carries  unit weight on ‖𝑄𝐴‖2 and 𝑁 ′ ≥ 1, the Rayleigh numerator is
           at most (2𝑀8)𝑁 ′ + 2𝑀1             9
                                      ‖𝐴‖2 ≤ 2𝑀 ‖𝐴‖2 , forcing 𝐶𝑃 ≥ 2𝑀/9 → ∞ as 𝑀 → ∞ for every
                                   )︀

           𝑁 ≥ 1, 𝑑 ≥ 3, 𝑁𝑐 ≥ 2, and every adjoint model.
             ′



                                                    5
```

---

## Page 6

```text
2. Flat lattice Hodge factorized-penalty and coarse-rank walls (ARR-2026-
       627PF1B4KK9VTRYT, ARR-2026-7EPM3V3DP796BBRR, consolidated dossier papers/flat-
       coarse-rank/): on 𝑋𝑛 = (Z/𝑛Z)𝑑 (𝑛 = ℓ𝑁 ′ , 𝑑 ≥ 2, 𝑁𝑐 ≥ 2, unit-spacing forward-difference
       curl d𝐴 and backward divergence 𝛿𝐴, ⟨𝐴, 𝐾0,𝑛 𝐴⟩ = ‖d𝐴‖2 + ‖𝛿𝐴‖2 ) with the averaged
                                                       𝑘=0 𝐴𝑖 (𝑥 + 𝑘𝑒𝑖 ), pick distinct directions
       line-integral block map (𝑄ℓ 𝐴)𝑖 (𝑦) = ℓ−𝑑 𝑥∈𝐵𝑦 ℓ−1
                                                ∑︀   ∑︀
                                                           2
      𝑝 ̸= 𝑞, orthogonal internal unit vectors 𝑢, 𝑣 ∈ R𝑁𝑐 −1 , 𝜄(𝑧) = (Re 𝑧)𝑢 + (Im 𝑧)𝑣, and define for
      ℓ ≥ 2 the explicit transverse ℓ-periodic Fourier witness:
                                            (ℓ)
                                           𝐴𝑖 (𝑥) := 1𝑖=𝑝 𝜄 𝑒2𝜋𝑖𝑥𝑞 /ℓ .
                                                            (︀       )︀


      Because ℓ−1       2𝜋𝑖𝑟𝑞 /ℓ = 0 and shifts along 𝑝 ̸= 𝑞 leave 𝑥 unchanged, 𝑄 𝐴(ℓ) = 0 identically;
               ∑︀
                 𝑟𝑞 =0 𝑒                                            𝑞                 ℓ
      meanwhile 𝛿𝐴(ℓ) = 0, ‖𝐴(ℓ) ‖2 = (ℓ𝑁 ′ )𝑑 , and ⟨𝐴(ℓ) , 𝐾0,𝑛 𝐴(ℓ) ⟩ = (ℓ𝑁 ′ )𝑑 · 4 sin2 (𝜋/ℓ) (nonzero,
      decaying as 𝑂(ℓ−2 ) — not in ker 𝐾0,𝑛 ). Consequently, for every penalty Ψℓ (𝑄ℓ 𝐴) satisfy-
      ing Ψℓ (0) = 0 (including any factorized quadratic form 𝑄*ℓ 𝑀ℓ 𝑄ℓ and nonlinear penalties),
      𝐶𝑃 (ℓ) ≥ (4 sin2 (𝜋/ℓ))−1 ≥ ℓ2 /(4𝜋 2 ) → ∞ as ℓ → ∞. Beyond fixed 𝑄ℓ , UniformPhysical-
      CoarseRankWall.lean constructs a low-frequency real subspace 𝑆𝑅 of dimension 2(2𝑅 + 1)𝑑
      with ⟨𝐴, 𝐾0,𝑛 𝐴⟩ ≤ (4𝜋 2 𝑑𝑅2 /𝑛2 )‖𝐴‖2 , ruling out uniform coercivity from any fixed-dimensional
      linear coarse measurement plus uniformly bounded-rank fine repair.

    3. Sine-series Wronskian counterexamples (ARR-2026-5FKM2GGK348CPTE9 v3): using the
       doubled Wronskian convention 𝑊 (𝑡) := 2[𝐹𝑎′ (𝑡)𝐹𝑏 (𝑡) − 𝐹𝑎 (𝑡)𝐹𝑏′ (𝑡)] from Theorem
                                                                                         √    1 of that
       paper, 𝑎 = (3, 4, 3), 𝑏 = (3, 2, 1) gives 𝑊 (𝜋/2) = −32 < 0 and 𝑊 (2𝜋/3) = 3 3 > √      0, while
       𝑎 = (6, 10, 24), 𝑏 = (6, 5, 2) gives 𝑊 (𝜋 − 𝜀) = −8𝜀3 + 𝑂(𝜀5 ) < 0 yet 𝑊 (2𝜋/3) = 51 3 > 0,
       refuting unrestricted sine-series Biernacki–Krzyż and generic local-to-global lifting.

    4. Additional programme obstructions (see Table 2 for complete statements):
       spatial coupling breaks the uniform vacuum and finite-extent Perron isolation fails to
       give extent-uniform gaps (ARR-2026-4X084GVAYF87PB3F, ARR-2026-6M8PMVHTMH8YZ9ND, ARR-
       2026-1A608PTGTC9XX9JZ); bounded-order marginal functionals face parity barriers in decou-
       pling inequalities (ARR-2026-5HRC3PS9HZ9WDAA5); and integrating out two free Haar trans-
       porters absent from an observable projects the reduced SU(2) form to the trivial sector
       (docs/SU2-TWO-TRANSPORTER-NOGO-20260731.md).


4     Open Formalization Tasks vs. Open Mathematics
    1. Open formalization task — fixed-spacing physical SU(𝑁 ) Wilson reflection positiv-
       ity: classically proved by Osterwalder and Seiler (1978), but open in this Lean archive beyond
       standalone R1/R2 finite SU(2) cylinder modules outside YangMillsCore.

    2. Open formalization / constructive-QFT task — hRpoly (draft PR #29): concrete
       Balaban/Dimock cluster-expansion-with-holes remainder decay for the physical gauge RG op-
       erator (frozen checkpoint: 20/41 terminal PreEq136 producers, TermSource = 0, uniform
       physical (𝐵0 , 𝛿0 ) and regional transport F5 open).

    3. Open mathematics — 4D continuum limit (𝑎 → 0) and OS/Wightman reconstruc-
       tion with mass gap: removing the UV regulator for SU(𝑁 ) (𝑁 ≥ 2) while establishing a
       non-perturbative mass gap remains the Clay Millennium Problem.




                                                     6
```

---

## Page 7

```text
5    Resolved AIRR Preprint Index (33 Companion Folders)
Table 2 maps all 33 companion mathematical-physics folders in THE-ERIKSSON-PROGRAMME to their
33 live AIRR identifiers on https://airr.science/ (together with this archival technical note ARR-
2026-7DYZAEKGJP8FPTJ1, 34 total). Unrelated empirical audit manuscripts added under papers/ in
November 2026 are excluded.
Repository Folder                   AIRR Identifier                  Topic / Role
paper/area-law                      ARR-2026-2ZQ6F57N2H8MG91V        Volume-uniform Wilson-loop area law
papers/c1-rooted-tree-majorants     ARR-2026-505NQZHR7P9TQ8SA        Rooted-tree majorants for polymers with
                                                                     holes
papers/c2-amos-closure              ARR-2026-6DP8SDRZ678H9AY9        Amos Bessel-ratio calculus across three
                                                                     sites
papers/c3-amos-proof                ARR-2026-17K7KRR6NH9ZVAEJ        Machine-checked Amos bound (integer
                                                                     order)
papers/c4-amos-real                 ARR-2026-3AJ7W5BS3N9VR8KM        Machine-checked Amos-type bound (real
                                                                     order)
papers/c5-crossing                  ARR-2026-39Y0F83F4Z9JK90G        Diagonal Amos-type crossing classification
papers/c6-rg-interface              ARR-2026-0WG9YDY5BA9S3RF4        Non-circular RG interface for Wilson
                                                                     correlators
papers/bessel-amos-fh               ARR-2026-5PXDYNR2ER89HTQG        Order-monotonicity of (log 𝐼𝜈 )′ & 2D LGT
papers/phi-lemma                    ARR-2026-72G1SSCNNG8YDVC2        Weighted Turán-type Bessel monotonicity
papers/surface-theorem              ARR-2026-1FPFA1TSMY9M3T9S        Killed von Mises bridge ratio
                                                                     monotonicity
papers/surface-complete             ARR-2026-3CEWH763KG84B8TM        Global ratio monotonicity (closure)
papers/wronskian-reduction          ARR-2026-5FKM2GGK348CPTE9        Sine-series Wronskian, 𝐹𝐵 > 0 proof &
                                                                     counterexamples
papers/poincare-wall                ARR-2026-3Q0VH7PMNV8C9VQE        Volume-uniform Poincaré walls
papers/flat-coarse-rank             ARR-2026-7EPM3V3DP796BBRR        Flat Hodge factorized-penalty wall (v2
                                                                     dossier)
papers/parity-barriers              ARR-2026-5HRC3PS9HZ9WDAA5        Parity barriers for decoupling inequalities
papers/o-bridge                     ARR-2026-31ED4MTKC18JPSDE        Dense-family clustering-to-gap criterion
papers/reflection-positivity        ARR-2026-10JJK0VCCS87VTQH        Z𝑁 reflection positivity (Z2 instance)
papers/os-chain-z2                  ARR-2026-7PRDH0DHH280HRKH        Open Z2 Ising transfer-matrix chain
papers/os-quotient                  ARR-2026-2TBRDN2DE598KSXD        Degenerate reflection pairing & GNS
                                                                     quotient
papers/perron-kernel                ARR-2026-2YDE42KFDY8Y3AA0        Perron theorem for strictly positive
                                                                     kernels
papers/perron-gap                   ARR-2026-1A608PTGTC9XX9JZ        Finite-extent spectral gap (not uniform)
papers/spatial-extent               ARR-2026-4X084GVAYF87PB3F        Spatial coupling breaks uniform vacuum
papers/spatial-birkhoff             ARR-2026-6M8PMVHTMH8YZ9ND        Second spatial-extent obstruction
papers/spatial-gibbs                ARR-2026-2TTA0WSQBT89X964        Transfer bridge for spatial Z2 slice
papers/spatial-reflection           ARR-2026-02YRWX53DG9M3R0R        Endpoint reflection positivity (Z2 slice)
papers/spatial-os                   ARR-2026-223XBWQ8PQ8Z2RDS        Bond reflection positivity & site form
papers/spatial-spectral             ARR-2026-1A7WS4SDF0894BPS        Fluctuation-sector operator bound
papers/spatial-uniform              ARR-2026-3EXXMXJD119J1R6R        Extent-independent rate (decoupled slice)
papers/congruence-spectrum          ARR-2026-7S1XA3PZEB9QM8FQ        Congruence rigidity and the fusion bound
papers/su2-crossing-compensated     ARR-2026-5V5K6T6DQT9J8SY6        Compensated-flow SU(2) crossing Ward
papers/thermodynamic-limit-kp       ARR-2026-5SGNYDASRB9V9VF9        Thermodynamic limit for local Gibbs
                                                                     states
papers/stationary-doob347           ARR-2026-1AS15VP0199VZ847        Boolean Doob kernels: stationary
                                                                     marginals
papers/stationary-weighting354      ARR-2026-4T35VQ6MZB8F99F4        Boolean Doob kernels: moment transfer
                      Table 2: Complete cross-reference of all 33 companion Yang–Mills
                      and mathematical-physics folders in THE-ERIKSSON-PROGRAMME
                      to live AIRR archive identifiers (plus this technical note
                      ARR-2026-7DYZAEKGJP8FPTJ1, 34 total).



                                                      7
```

---

## Page 8

```text
6    Reproducibility, Citation, and Disclosure
Reproduce   the  full  core   build,    oracle-only imports,  axiom-output  validation,
and   per-module   Amos     oracle   at     release yang-mills-archive-v1.0   (commit
6b54eca695e96b3038ceda18276c4e28fb45983f; on Windows pass -c core.longpaths=true):
git clone -c core.longpaths=true \
  https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME.git
cd THE-ERIKSSON-PROGRAMME && git checkout yang-mills-archive-v1.0
lake exe cache get
lake build YangMillsCore AmosClosure \
  YangMills.RG.UniformPhysicalCoarseRankWallOracle
# Build all 46 imports of oracle_check.lean (matching .github/workflows/lean-build.yml):
grep -E ’^import ’ oracle_check.lean | awk ’{print $2}’ | xargs lake build
lake env lean oracle_check.lean > oracle-output.txt
python scripts/check_oracle_output.py --output oracle-output.txt
lake env lean AmosClosure/Oracle.lean
python scripts/check_consistency.py

Code is licensed AGPL-3.0-or-later; citation metadata live in CITATION.cff and .zenodo.json.
Large language models assisted formalization and editing under author supervision; core claims are
checked by the Lean 4 kernel with standard axioms only. Author Lluis Eriksson administers AIRR
(https://airr.science/); no independent editorial admission or peer review is claimed.




                                                 8
```
