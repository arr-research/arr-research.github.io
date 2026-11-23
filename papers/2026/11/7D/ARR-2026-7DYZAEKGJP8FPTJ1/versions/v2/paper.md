# The Eriksson Programme (Yang-Mills): Auditable Claim-to-Theorem Manifest, Certified Obstructions, and Continuation Frontier (Release yang-mills-archive-v1.0)

> Machine-readable rendition extracted from the hash-identified canonical PDF (`paper.pdf`). Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
The Eriksson Programme (Yang–Mills):
  Auditable Claim-to-Theorem Manifest, Certified Obstructions,
and Continuation Frontier (Release yang-mills-archive-v1.0)

                                             Lluis Eriksson
                                     Independent Researcher, Sweden

                                       23 November 2026 (v2)


                                                Abstract
          This archival technical note provides a self-contained, auditable claim-to-theorem
      specification and continuation handoff for the Yang–Mills Lean 4 formalization in-
      side THE-ERIKSSON-PROGRAMME at archival release yang-mills-archive-v1.0 (com-
      mit 6b54eca695e96b3038ceda18276c4e28fb45983f;                canonical Lean core check-
      point 02fae0ad in project-state.json,               Lean v4.29.0-rc6,         pinned mathlib
      07642720480157414db592fa85b626dafb71355b). Responding to every material objection
      raised against v1 (ARR-2026-7DYZAEKGJP8FPTJ1 v1), this v2 revision replaces directory-level
      summaries with exact fully-qualified Lean 4 theorem statements, explicit coupling and
      geometric hypotheses, concrete strictly-interacting non-vacuity witnesses, exact operator
      classes and volume quantifiers for the certified obstructions, a strict distinction between
      YangMillsCore-compiled, oracle_check-audited, and standalone declarations, and resolved
      AIRR identifiers for all 32 indexed mathematical-physics records.
          We state the mathematical boundary without pseudo-metrics. The verified core proves fixed-
      spacing lattice results: a Kotecký–Preiss / Mayer–Ursell polymer engine; volume-uniform strong-
      coupling SU(Nc ) Wilson-loop area laws (indexed by Z/Nc Z-chain homology area chainAreaA)
      and exponential clustering of truncated two-plaquette correlations without Peter–Weyl; an ex-
      plicit strictly-interacting SU(2) non-vacuity window 0 < |β| ≤ 10−5 ; exact Zn centre-symmetry
      selection rules for positively-oriented Wilson loops with n ∤ |es|; conditional 4D marginal-
      coupling UV-summation theorems requiring κ0 > 1; real-order Amos/Bessel ratio bounds on
      ν ≥ 0; and a transfer-matrix identification chain for the 1D open Z2 Ising spin chain. No
      four-dimensional continuum limit (a → 0), no physical SU(N ) Osterwalder–Schrader or Wight-
      man reconstruction, and no solution to the Clay Millennium Yang–Mills Mass Gap problem is
      claimed. We separate open formalization tasks (fixed-spacing SU(N ) Wilson reflection positiv-
      ity and the Balaban/Dimock hRpoly estimate in draft PR #29) from open mathematics (4D
      continuum Yang–Mills existence and mass gap).


1     Verification Architecture and Coverage Boundary
To eliminate ambiguity between built modules, audited declarations, and standalone work, the
archival release yang-mills-archive-v1.0 maintains three distinct automated boundaries:

    1. Core compilation and axiom oracle (lean-build.yml). On every push and PR
       to main (with a cache-free cold_build: true manual dispatch option), GitHub
       Actions installs Lean v4.29.0-rc6, fetches prebuilt mathlib .olean caches for com-
       mit 07642720480157414db592fa85b626dafb71355b, runs lake build YangMillsCore

                                                    1
```

---

## Page 2

```text
(recorded core count: 8466 jobs in project-state.json), builds the modules imported
      by oracle_check.lean, executes lake env lean oracle_check.lean, and verifies via
      scripts/check_oracle_output.py that every #print axioms readout depends only on
      [propext, Classical.choice, Quot.sound].

    2. Lexical honesty guard (ci.yml). scripts/check_consistency.py scans YangMills/
       and Lean/ (excluding YangMills/Experimental/) for sorry, and scans the verified-core
       directories (L0_Lattice, L1_GibbsMeasure, KP, ClayCore, Paper, RG, YangMillsCore.lean,
       and core P8_PhysicalGap Haar/compactness files) for axiom. A lexical scan alone never
       certifies compilation or non-vacuity; it is strictly supplementary to lean-build.yml and the
       non-vacuity witnesses below.

    3. Standalone and branch-only modules (explicitly outside YangMillsCore). The finite
       SU(2) Wilson cylinder geometry/measure modules (R1/R2, Sept 2026) and draft PR #29
       (hRpoly) are not imported by YangMillsCore.lean and are not covered by the core build
       guarantee.


2     Auditable Claim-to-Theorem Manifest
Every headline claim in this archive maps to a concrete fully-qualified Lean 4 declaration in Yang-
MillsCore (at commit 6b54eca695e96b3038ceda18276c4e28fb45983f). Below we state the deci-
sive domains, quantifiers, coupling windows, and non-vacuity witnesses so each statement can be
checked directly from this note.

2.1    KP / Mayer polymer engine (YangMills/KP/)
    • YangMills.KP.partition_eq_exp_clusterSum_of_kp (KP/MayerInversion.lean:2038):
      for any finite polymer model P ([Fintype P.Polymer]) and weight function
      a : P.Polymer → R satisfying the Kotecký–Preiss criterion KPCriterion P a, the
      polymer partition function satisfies Ξ = exp(clusterSum P ) with absolutely summable
      cluster series.

    • YangMills.KP.abs_ursell_le_card_spanningTrees and kp_convergence: proves Pen-
      rose’s tree-graph bound |ϕ(X)| ≤ #SpanningTrees(GX ) via greedy BFS partition schemes
      and yields exponential convergence under the KP smallness condition.

2.2    Strong-coupling SU(Nc ) area                law,     IR    clustering,      and    non-vacuity
       (YangMills/L1_GibbsMeasure/)
    • Volume-uniform exact-action Wilson-loop area law: YangMills.normalized_exp_-
      wilson_loop_area_law (L1_GibbsMeasure/RestrictedGate.lean:2045). For any dimen-
      sion d, lattice side N , gauge rank Nc ≥ 1 ([NeZero N_c]), arbitrary edge list es :
      List (ConcreteEdge d N ), complex plaquette couplings ∥cp ∥ ≤ δ with c′p = cp , and parameters
      t, ε ≥ 0, σ ∈ [0, 1] satisfying the explicit volume-independent KP smallness inequalities

                                                                   (e2δNc − 1)et+ε+1
               (16d + 1)2 (e2δNc − 1)et+ε+1 < 1,    (16d)                                    ≤ t,
                                                            1 − (16d + 1)2 (e2δNc − 1)et+ε+1

      together with (16d + 1)2 σ < 1 and the effective-activity bound (e2δNc − 1) exp(· · · ) ≤
      σ 2 , the normalized expectation of tr(Ues ) under the exact exponential plaquette action

                                                    2
```

---

## Page 3

```text
p exp(cp tr Up + cp tr Up ) obeys
      Q


             ⟨tr Ues ⟩ ≤ Nc exp 4d |edgeSupport(es)| Cperim σ chainAreaAZ/Nc Z (loopChain(es)) ,
                                                               


      with constants independent of lattice side N . Because the exponent is the minimal spanning-
      surface area in Z/Nc Z-chain homology (chainAreaA), twice-traversed SU(2) loops have
      loopChainZ/2Z = 0 and hence chainAreaA = 0 (σ 0 = 1), cleanly accommodating the ex-
      act Haar identity E[tr(UC2 )/2] = −1/2 at β = 0.

  • Unconditional       SU(Nc )     two-plaquette       exponential        clustering          without
    Peter–Weyl:          YangMills.sun_two_plaquette_correlator_bound                  (L1_GibbsMea-
    sure/TwoPlaquetteCorrelator.lean:710).             For any Nc ≥ 1, any measurable
    f : SU(Nc ) → R with |f | ≤ 1, any s > 0, β ∈ R, t, ε ≥ 0 satisfying
    (16d + 1)2 (e|β|Nc − 1) + s + (e|β|Nc − 1)s et+ε+1 < 1 and its paired KP smallness bound,
    and any two distinct plaquettes p ̸= q at touching-graph distance 2k ≤ disttouchGraph (p, q),
    the connected two-plaquette correlator under the Wilson Gibbs measure with action
    −β wilsonAction(Re tr) decays as |Covβ (f (Up ), f (Uq ))| ≤ C(d, Nc , β, s, t, ε) e−εk , uniformly
    in lattice side N .

  • Explicit strictly-interacting non-vacuity witness: YangMills/L1_GibbsMeasure/Ther
    modynamicNonvacuity.lean proves that the uniform local KP regime is non-empty for the
    strictly interacting SU(2) Wilson theory with nonconstant plaquette energy Re tr U on the
    explicit interval 0 < |β| ≤ 10−5 with t = ε = η = 10−2 (and explicitly rules out degeneration
    to the free β = 0 point).

  • Fixed-spacing thermodynamic limit: YangMills/L1_GibbsMeasure/IntegerThermod
    ynamicLimit.lean constructs a translation-invariant infinite-volume state on finite-support
    integer-lattice edge observables (IntegerLocalObservable) along periodic torus exhaustions
    of side n + 1 → ∞ at fixed spacing inside UniformLocalKPRegime, passing two-plaquette
    clustering to the limit (ThermodynamicCorrelation.lean). This is an infinite-volume lattice
    limit, not an ultraviolet continuum limit.

  • Exact Zn centre-symmetry selection rule: YangMills.integral_wilsonLoopSU_gibb
    s_eq_zero (L1_GibbsMeasure/GibbsSelectionRule.lean:120). Under the global centre
    action multiplying every positively-oriented edge by ω = e2πi/n In ∈ Z(SU(n)), every plaquette
    traverses two forward and two backward edges so the Wilson action is exactly invariant for
    all β ∈ R. Any positively-oriented edge list es (hpos) transforms with eigenvalue ω |es| , so
    its interacting Gibbs expectation vanishes whenever n ∤ |es|. (Contractible plaquettes have
    signed net charge 0 (mod n) and are not forced to vanish.)

2.3   Conditional 4D marginal-coupling RG assembly (YangMills/RG/)
  • YangMills.RG.lattice_mass_gap_of_singleScaleUVDecay_marginal (RG/MarginalUVM
    assGap.lean:132): an abstract real-sequence theorem taking sequences covIR, g : N → R and
    per-scale remainders Rsc : N → N → R with gk > 0, βgk < 1, exact one-loop logistic recursion
    gk+1 = gk (1 − βgk ), exponent κ0 > 1 (guaranteeing absolute summability k gkκ0 < ∞, unlike
                                                                             P

    κ0 = 1 where O(1/k) diverges), exponential IR decay |covIRk | ≤ C1 e−εk , and carried UV
    hypothesis SingleScaleUVDecay Rsc g C2 c0 kappa0. It concludes exponential decay of
    covIRt + covUVt . It mentions no gauge group, Hilbert space, or transfer matrix; the missing
    physical input is hRpoly.

                                                  3
```

---

## Page 4

```text
2.4    Modified Bessel / Amos suite and 1D Z2 transfer chain
    • Real-order Amos bounds (AmosClosure/AmosBoundProofReal.lean): for all real orders
      ν ≥ 0 and x > 0 (starting from geometric series domination on 0 < x ≤ 1/4 and extending via
      Riccati barrier lemmas), proves the strict Amos-type inequality for Iν+1 (x)/Iν (x), companion
      crossing classifications (ARR-2026-39Y0F83F4Z9JK90G), and global ratio monotonicity of the
      killed von Mises bridge (ARR-2026-3CEWH763KG84B8TM).

    • 1D open Z2 Ising transfer-matrix chain (YangMills/OS/Z2Identification.lean):
      proves En [A(σ0 )B(σn )] = ⟨AΩ, Tβn (BΩ)⟩C , exact correlation (tanh β)n , spectral gap 1 −
      | tanh β| (1 − tanh β for β ≥ 0), and time-zero pairing non-degeneracy (ARR-2026-
      7PRDH0DHH280HRKH v2). It is a 1D finite-slice spin chain, not a 4D SU(N ) OS reconstruction;
      strictly positive kernel entries alone do not imply reflection positivity, and finite-extent Perron
      isolation does not imply a uniform gap.


3     Certified Negative Results and Exact Obstruction Classes
    1. Volume-uniform Poincaré walls (ARR-2026-3Q0VH7PMNV8C9VQE): for the flat gauge-fixed
       Hodge plus block-averaging quadratic form ⟨A, K0 A⟩ + a∥QA∥2 on the fine d-dimensional
       torus of side LN ′ (d ≥ 3, Nc ≥ 2, concrete su(Nc ) adjoint model), every flat block-Poincaré
       constant satisfies CP ≥ Ld−2 , refuting any volume-uniform coercivity constant via this route.
       In the fluctuation sector on fine side (2M )N ′ , transported half-period square-wave modes
       satisfy ∥QA∥2 ≤ (2M )−1 ∥A∥2 and ⟨A, K0 A⟩ = 8((2M )N ′ )−1 ∥A∥2 , forcing CP ≥ 2M/9 for
       every N ′ ≥ 1, d ≥ 3, Nc ≥ 2, and every adjoint model.

    2. Flat lattice Hodge factorized-penalty and coarse-rank walls (ARR-2026-
       627PF1B4KK9VTRYT, ARR-2026-7EPM3V3DP796BBRR, and expanded v2 dossier papers/flat-
       coarse-rank/): on flat periodic tori, divergence-zero exact-kernel Fourier families annihilated
       by the specified block-averaging map Q obstruct every penalty of the form Q∗ M Q factored
       through Q.

    3. Spatial coupling and Birkhoff obstructions in Z2 slices (ARR-2026-4X084GVAYF87PB3F,
       ARR-2026-6M8PMVHTMH8YZ9ND, ARR-2026-1A608PTGTC9XX9JZ): isolates where uniform-
       vacuum and extent-independent bounds fail under spatial coupling.

    4. Parity barriers for decoupling inequalities (ARR-2026-5HRC3PS9HZ9WDAA5): no com-
       parison functional of bounded marginal order can certify uniform decoupling.

    5. Sine-series Wronskian counterexamples (ARR-2026-5FKM2GGK348CPTE9
                                                               √                          v2): explicit
       finite arrays a = (3, 4, 3), b = (3, 2, 1) (W (2π/3) = 3 √3 > 0) and a = (6, 10, 24), b = (6, 5, 2)
       (W (π − ε) = −8ε3 + O(ε5 ) < 0 yet W (2π/3) = 51 3 > 0) refute unrestricted sine-series
       Biernacki–Krzyż and generic local-to-global lifting.

    6. Two-transporter Haar projection no-go (docs/SU2-TWO-TRANSPORTER-NOGO-
       20260731.md): two free Haar-integrated transporters absent from the observable project the
       reduced SU(2) quadratic form to the trivial sector.




                                                    4
```

---

## Page 5

```text
4     Open Formalization Tasks vs. Open Mathematics
We separate bounded formalization tasks (classically known mathematics not yet formalized in this
Lean archive) from genuinely open mathematics:

    1. Open formalization task — physical SU(N ) Wilson reflection positivity at fixed
       spacing: classically proved by Osterwalder and Seiler (1978), but still open in this
       Lean archive beyond the standalone R1/R2 finite SU(2) cylinder geometry and normalized
       product-Haar measure (docs/evidence/physical-cylinder-r2-20260906/, outside Yang-
       MillsCore).

    2. Open formalization / constructive-QFT task — hRpoly (frozen in draft PR #29):
       concrete Balaban/Dimock cluster-expansion-with-holes remainder activity decay for the phys-
       ical gauge RG operator. Frozen checkpoint (docs/HRPOLY-STATUS.md): 20/41 terminal
       PreEq136 producers, TermSource = 0, uniform physical (B0 , δ0 ) and regional transport (F5)
       open.

    3. Open mathematics — 4D continuum limit (a → 0) and OS/Wightman recon-
       struction with positive mass gap for SU(N ) (N ≥ 2): no complete proof exists in the
       literature or in this repository; removing the UV regulator while retaining a non-perturbative
       mass gap remains the Clay Millennium Problem.


5     Resolved AIRR Preprint Index (All 32 Records)
Table 1 maps all 32 mathematical-physics folders in THE-ERIKSSON-PROGRAMME to their live AIRR
identifiers on https://airr.science/ (resolving the two entries that were pending in v1). Unre-
lated empirical audit manuscripts added under papers/ in November 2026 are excluded.

Repository Folder                 AIRR Identifier                Topic / Role
paper/area-law                    ARR-2026-2ZQ6F57N2H8MG91V      Volume-uniform Wilson-loop area law
papers/c1-rooted-tree-majorants   ARR-2026-505NQZHR7P9TQ8SA      Rooted-tree majorants for polymers with
                                                                 holes
papers/c2-amos-closure            ARR-2026-6DP8SDRZ678H9AY9      Amos Bessel-ratio calculus across three
                                                                 sites
papers/c3-amos-proof              ARR-2026-17K7KRR6NH9ZVAEJ      Machine-checked Amos bound (integer
                                                                 order)
papers/c4-amos-real               ARR-2026-3AJ7W5BS3N9VR8KM      Machine-checked Amos-type bound (real
                                                                 order)
papers/c5-crossing                ARR-2026-39Y0F83F4Z9JK90G      Diagonal Amos-type crossing
                                                                 classification
papers/c6-rg-interface            ARR-2026-0WG9YDY5BA9S3RF4      Non-circular RG interface for Wilson
                                                                 correlators
papers/bessel-amos-fh             ARR-2026-5PXDYNR2ER89HTQG      Order-monotonicity of (log Iν )′ & 2D
                                                                 LGT
papers/phi-lemma                  ARR-2026-72G1SSCNNG8YDVC2      Weighted Turán-type Bessel monotonicity
papers/surface-theorem            ARR-2026-1FPFA1TSMY9M3T9S      Killed von Mises bridge ratio
                                                                 monotonicity
papers/surface-complete           ARR-2026-3CEWH763KG84B8TM      Global ratio monotonicity (closure)
papers/wronskian-reduction        ARR-2026-5FKM2GGK348CPTE9      Sine-series Wronskian, FB > 0 proof &
                                                                 counterexamples
papers/poincare-wall              ARR-2026-3Q0VH7PMNV8C9VQE      Volume-uniform Poincaré walls
papers/flat-coarse-rank           ARR-2026-7EPM3V3DP796BBRR      Flat Hodge factorized-penalty wall (v2
                                                                 dossier)


                                                    5
```

---

## Page 6

```text
Repository Folder                  AIRR Identifier                  Topic / Role
papers/parity-barriers             ARR-2026-5HRC3PS9HZ9WDAA5        Parity barriers for decoupling inequalities
papers/o-bridge                    ARR-2026-31ED4MTKC18JPSDE        Dense-family clustering-to-gap criterion
papers/reflection-positivity       ARR-2026-10JJK0VCCS87VTQH        ZN reflection positivity (Z2 instance)
papers/os-chain-z2                 ARR-2026-7PRDH0DHH280HRKH        Open Z2 Ising transfer-matrix chain
papers/os-quotient                 ARR-2026-2TBRDN2DE598KSXD        Degenerate reflection pairing & GNS
                                                                    quotient
papers/perron-kernel               ARR-2026-2YDE42KFDY8Y3AA0        Perron theorem for strictly positive
                                                                    kernels
papers/perron-gap                  ARR-2026-1A608PTGTC9XX9JZ        Finite-extent spectral gap (not uniform)
papers/spatial-extent              ARR-2026-4X084GVAYF87PB3F        Spatial coupling breaks uniform vacuum
papers/spatial-birkhoff            ARR-2026-6M8PMVHTMH8YZ9ND        Second spatial-extent obstruction
papers/spatial-gibbs               ARR-2026-2TTA0WSQBT89X964        Transfer bridge for spatial Z2 slice
papers/spatial-reflection          ARR-2026-02YRWX53DG9M3R0R        Endpoint reflection positivity (Z2 slice)
papers/spatial-os                  ARR-2026-223XBWQ8PQ8Z2RDS        Bond reflection positivity & site form
papers/spatial-spectral            ARR-2026-1A7WS4SDF0894BPS        Fluctuation-sector operator bound
papers/spatial-uniform             ARR-2026-3EXXMXJD119J1R6R        Extent-independent rate (decoupled slice)
papers/congruence-spectrum         ARR-2026-7S1XA3PZEB9QM8FQ        Congruence rigidity and the fusion bound
papers/su2-crossing-compensated    ARR-2026-5V5K6T6DQT9J8SY6        Compensated-flow SU(2) crossing Ward
papers/thermodynamic-limit-kp      ARR-2026-5SGNYDASRB9V9VF9        Thermodynamic limit for local Gibbs
                                                                    states
papers/stationary-doob347          ARR-2026-1AS15VP0199VZ847        Boolean Doob kernels: stationary
                                                                    marginals
papers/stationary-weighting354     ARR-2026-4T35VQ6MZB8F99F4        Boolean Doob kernels: moment transfer
                    Table 1: Complete cross-reference of Yang–Mills and mathematical-
                    physics manuscripts in THE-ERIKSSON-PROGRAMME to live AIRR archive
                    identifiers.




6    Reproducibility, Citation, and Disclosure
Reproduce the verified Lean 4 core at release yang-mills-archive-v1.0 (commit
6b54eca695e96b3038ceda18276c4e28fb45983f; on Windows pass -c core.longpaths=true):

git clone -c core.longpaths=true \
  https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME.git
cd THE-ERIKSSON-PROGRAMME && git checkout yang-mills-archive-v1.0
lake exe cache get && lake build YangMillsCore
lake env lean oracle_check.lean && python scripts/check_consistency.py

Code is licensed AGPL-3.0-or-later; citation metadata live in CITATION.cff and .zenodo.json.
Large language models assisted formalization and editing under author supervision; core claims are
checked by the Lean 4 kernel with standard axioms only. Author Lluis Eriksson administers AIRR
(https://airr.science/); no independent editorial admission or peer review is claimed.




                                                     6
```
