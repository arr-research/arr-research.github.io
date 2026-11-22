# The Eriksson Programme (Yang-Mills): Machine-Checked Lattice Gauge Foundations, Certified Obstructions, and the Open Frontier

> Machine-readable rendition extracted from the hash-identified canonical PDF (`paper.pdf`). Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
The Eriksson Programme (Yang–Mills):
               Machine-Checked Lattice Gauge Foundations,
               Certified Obstructions, and the Open Frontier
                                            Lluis Eriksson
                                   Independent Researcher, Sweden

                                         22 November 2026


                                               Abstract
          We present an archival technical synthesis and handoff specification for the Yang–
     Mills formalization programme inside THE-ERIKSSON-PROGRAMME (archival release
     yang-mills-archive-v1.0). The repository pins Lean 4 (v4.29.0-rc6) and mathlib
     (07642720480157414db592fa85b626dafb71355b) and maintains a continuously verified core
     module, YangMillsCore, whose build and axiom oracle pass in GitHub Actions with zero
     sorry declarations, zero project-specific axioms, and every headline declaration restricted to
     Lean’s three foundational axioms [propext, Classical.choice, Quot.sound].
          Within this verified core, the programme establishes: (i) a reusable Kotecký–Preiss and
     Mayer–Ursell polymer cluster-expansion engine (including Penrose’s tree-graph inequality and
     zero-free polydiscs); (ii) finite-volume and volume-uniform strong-coupling Wilson-loop area
     laws and unconditional exponential decay of truncated plaquette correlations for SU(N ) lattice
     gauge theory without invoking Peter–Weyl, together with fixed-spacing thermodynamic limits;
     (iii) exact ZN centre-symmetry selection rules and fundamental Haar/Schur identities; (iv)
     machine-checked modified-Bessel/Amos ratio bounds and global ratio monotonicity for killed
     von Mises bridges; (v) complete Osterwalder–Seiler reflection-positivity and transfer-operator
     chains for Z2 lattice gauge systems; and (vi) certified negative obstructions isolating exact
     walls in block-Poincaré coercivity, flat lattice Hodge rank, spatial coupling, and sine-series
     monotonicity.
          We state the limits with equal precision. No four-dimensional continuum limit (a → 0),
     no physical SU(N ) Osterwalder–Schrader or Wightman reconstruction, and no solution to the
     Clay Millennium Yang–Mills Mass Gap problem is claimed; the repository’s historical Clay-
     distance shorthand remains ∼0% (< 0.1%). Three open fronts are isolated and documented
     for future researchers and automated provers: the concrete Balaban/Dimock physical activity
     estimate hRpoly (frozen in draft PR #29 at 20/41 terminal producers and TermSource = 0),
     physical SU(N ) reflection positivity and transfer-operator gaps beyond finite-cylinder geom-
     etry (R1/R2), and continuum/OS–Wightman reconstruction. All accompanying preprints in
     the AIRR archive (https://airr.science/) and reproduction steps are indexed in one citable
     record.


1    Scope, Verification Standard, and Epistemic Boundary
Formalizing constructive quantum field theory in an interactive theorem prover exposes two dis-
tinct failure modes: silent logical gaps (sorry or unproved axiom declarations) and vacuous for-
malizations whose top-level statements hold for degenerate models (such as trivial gauge groups


                                                   1
```

---

## Page 2

```text
or coordinated dummy scalings). Early phases of THE-ERIKSSON-PROGRAMME encountered both;
the mature repository enforces a strict archival discipline verified automatically on every push
and pull request to main:

    1. Pinned toolchain and dependencies. lean-toolchain pins leanprover/lean4:v4.29.0-rc6;
       lakefile.lean     and   lake-manifest.json     pin     mathlib    to    commit
       07642720480157414db592fa85b626dafb71355b and fix all transitive dependency re-
       visions.

    2. Automated compilation and axiom oracle. GitHub Actions workflow lean-build.yml
       builds YangMillsCore (recorded core count: 8466 Lake jobs in project-state.json) and
       runs oracle_check.lean, requiring every #print axioms readout to depend on nothing
       beyond [propext, Classical.choice, Quot.sound].

    3. Zero-sorry and zero-core-axiom textual guard.                     Workflow ci.yml runs
       scripts/check_consistency.py, a comment-aware scanner forbidding sorry across
       the proof tree and forbidding axiom declarations across the verified-core source directories
       (L0_Lattice, L1_GibbsMeasure, KP, ClayCore, Paper, RG, and the core P8_PhysicalGap
       Haar/compactness modules). Missing analytic theorems are carried strictly as explicit
       theorem hypotheses (HYPOTHESIS_FRONTIER.md), never as axioms.

    4. Explicit Clay-distance boundary. The programme does not prove existence of a
       four-dimensional continuum Yang–Mills theory on R4 , Osterwalder–Schrader or Wight-
       man axioms for SU(N ) (N ≥ 2), or a continuum mass gap. The assembly lemmas
       in YangMills/Paper/ClusteringToGap.lean are explicitly documented as real-sequence
       exponential-decay lemmas; their physical role is conditional on genuine gauge-theoretic IR
       and UV inputs.


2     Summary of Machine-Checked Results in YangMillsCore
Table 1 summarizes the verified mathematical engines available for direct reuse by downstream
formalization efforts and automated provers.




                                                 2
```

---

## Page 3

```text
Layer                   Verified Content (0 sorry, 0 project axioms)                Lean Location
KP / Mayer polymer      Mayer–Ursell inversion (Ξ = exp(clusterSum)), Penrose       YangMills/KP/
engine                  tree-graph inequality via greedy BFS partition schemes,
                        polymer reconstruction Z = Ξ, Kotecký–Preiss
                        convergence, and activity-domain zero-free polydiscs.
Wilson area laws & IR   Finite-volume and volume-uniform strong-coupling            YangMills/L1_GibbsMeasure/
clustering              Wilson-loop area laws (linearized and exact activity);      paper/area-law/
                        unconditional exponential decay of truncated plaquette
                        correlations for SU(N ) in an explicit non-empty coupling
                        window without Peter–Weyl; fixed-spacing
                        thermodynamic limit on integer coordinates.
Haar & ZN centre        Left-invariant vanishing engine, interacting Wilson-loop    YangMills/ClayCore/
symmetry                N -ality selection rules at any coupling β, fundamental
                        Schur orthogonality on SU(N ), U(1) character
                        orthogonality on AddCircle, and certification of SU(1)
                        degeneracy.
Conditional RG          Block-spin averaging with gauge covariance and ℓ2           YangMills/RG/
substrates              contraction, finite-dimensional Gaussian pushforwards,      YangMills/Paper/
                        exponential-decay kernel calculus, marginal-coupling 4D
                        summability (MarginalUVMassGap.lean), and
                        source-plus-defect error-budget landing pads
                        (YMActivityBudget).
Bessel / Amos & 2D      Machine-checked Amos-type bounds for modified Bessel        AmosClosure/
surface suite           ratios at integer and real order, quantitative crossing     MarkedRootedClosure/
                        classification, Turán-type monotonicity, sine-series
                        Wronskian identity, and global ratio monotonicity for
                        killed von Mises bridges.
Z2 / ZN OS & transfer   Complete machine-checked Osterwalder–Seiler chain for       YangMills/OS/
chains                  the Z2 gauge chain, degenerate reflection pairing and
                        GNS quotient, Perron theorem for strictly positive
                        kernels, spatial coupling obstructions, and
                        congruence-spectrum rigidity.
Finite SU(2) cylinder   Four-vertex, six-link, two-plaquette SU(2) cylinder         docs/evidence/
(R1/R2)                 geometry, normalized product-Haar Gibbs measure, and        physical-cylinder-r2-20260906/
                        exact reflection/Fubini identities (standalone, outside
                        YangMillsCore; positivity and transfer remain open).

   Table 1: Verified mathematical engines in the archival release yang-mills-archive-v1.0.




                                                     3
```

---

## Page 4

```text
3     Certified Obstructions and Negative Results
A central contribution of the programme for future researchers is a body of machine-checked
negative theorems ruling out tempting but mathematically false shortcuts:

    • Volume-uniform Poincaré walls (ARR-2026-3Q0VH7PMNV8C9VQE): obstructs flat and
      fluctuation-sector block-Poincaré routes to Combes–Thomas coercivity in lattice Yang–
      Mills.

    • Flat      lattice    Hodge      factorized-penalty         and  coarse-rank      walls
      (ARR-2026-627PF1B4KK9VTRYT, ARR-2026-7EPM3V3DP796BBRR, and expanded revision
      dossier papers/flat-coarse-rank/): exact-kernel Fourier families obstruct every penalty
      factored through a block map in a flat lattice gauge form.

    • Spatial coupling and Birkhoff obstructions in Z2 slices (ARR-2026-4X084GVAYF87PB3F,
      ARR-2026-6M8PMVHTMH8YZ9ND, ARR-2026-1A608PTGTC9XX9JZ): isolates where elementary
      uniform-vacuum and extent-independent spectral arguments break under spatial coupling.

    • Parity barriers for decoupling inequalities (ARR-2026-5HRC3PS9HZ9WDAA5): no com-
      parison functional of bounded marginal order can certify uniform decoupling.

    • Failure of Biernacki–Krzyż for sine series (papers/wronskian-reduction/): explicit
      counterexample a = (3, 4, 3), b = (3, 2, 1) showing coefficient-ratio monotonicity cannot
      certify the sign of the antisymmetrized sine-sum Wronskian.

    • Two-transporter Haar projection design no-go (docs/SU2-TWO-TRANSPORTER-NOGO-20260731.md):
      two free Haar-integrated transporters absent from the observable project the reduced SU(2)
      quadratic form to the trivial sector.


4     Open Frontiers for Continuation
Future human teams or autonomous theorem provers picking up this archive should start from
HORIZON.md, HYPOTHESIS_FRONTIER.md, and YangMills/CLOSURE.md. Three concrete frontiers
remain open:

    1. Physical UV activity estimate (hRpoly), frozen in draft PR #29. Construct the con-
       crete Balaban/Dimock cluster-expansion-with-holes remainder decay bound for the actual
       gauge RG operator. At the frozen September 2026 checkpoint (docs/HRPOLY-STATUS.md),
       the checklist records 20/41 terminal PreEq136 producers, TermSource = 0, physical win-
       dow 15 compatible but not attained, and uniform physical (B0 , δ0 ) plus regional transport
       (F5) open.

    2. Physical SU(N ) reflection positivity and transfer-operator spectral gap at
       fixed spacing. Extend the verified R1/R2 finite SU(2) cylinder geometry and product-
       Haar measure to genuine complex Gram-matrix positivity retaining all crossing pla-
       quette weights, a strictly positive centered norm, and a physical transfer operator
       (docs/POST-HRPOLY-CONTINUUM-AUDIT-20260906.md).

    3. Four-dimensional continuum limit (a → 0) and Osterwalder–Schrader / Wight-
       man reconstruction (M4–M5). This remains open mathematics well beyond current

                                                 4
```

---

## Page 5

```text
formalization infrastructure: removing the ultraviolet regulator while retaining a non-
     perturbative positive mass gap for SU(N ) (N ≥ 2) and constructing the continuum Hilbert
     space and fields.

    Late-2026 open research branches on GitHub (not merged into YangMillsCore) preserve ad-
ditional work on concentric integer-shell energy control and flat cochains (PRs #180–#190) and
Boolean Doob chain retention criteria (PRs #292, #299).


5    Cross-Referenced AIRR Preprint Index
Table 2 links the core mathematical-physics manuscripts in THE-ERIKSSON-PROGRAMME to their
stable records in the AIRR archive (https://airr.science/). Unrelated empirical audit
manuscripts added under papers/ in November 2026 are excluded from this index.

Repository Folder               AIRR Identifier             Topic / Role
paper/area-law                  ARR-2026-2ZQ6F57N2H8MG91V   Volume-uniform Wilson-loop area law
papers/c1-rooted-tree-majorants ARR-2026-505NQZHR7P9TQ8SA   Rooted-tree majorants for polymers with
                                                            holes
papers/c2-amos-closure          ARR-2026-6DP8SDRZ678H9AY9   Amos Bessel-ratio calculus across three
                                                            sites
papers/c3-amos-proof            ARR-2026-17K7KRR6NH9ZVAEJ   Machine-checked Amos bound (integer
                                                            order)
papers/c4-amos-real             ARR-2026-3AJ7W5BS3N9VR8KM   Machine-checked Amos-type bound (real
                                                            order)
papers/c5-crossing              ARR-2026-39Y0F83F4Z9JK90G   Diagonal Amos-type crossing
                                                            classification
papers/c6-rg-interface          ARR-2026-0WG9YDY5BA9S3RF4   Non-circular RG interface for Wilson
                                                            correlators
papers/bessel-amos-fh           ARR-2026-5PXDYNR2ER89HTQG   Order-monotonicity of (log Iν )′ & 2D
                                                            LGT
papers/phi-lemma                ARR-2026-72G1SSCNNG8YDVC2   Weighted Turán-type Bessel
                                                            monotonicity
papers/surface-theorem          ARR-2026-1FPFA1TSMY9M3T9S   Killed von Mises bridge ratio
                                                            monotonicity
papers/surface-complete         ARR-2026-3CEWH763KG84B8TM   Global ratio monotonicity (closure)
papers/poincare-wall            ARR-2026-3Q0VH7PMNV8C9VQE   Volume-uniform Poincaré walls
papers/flat-coarse-rank         ARR-2026-7EPM3V3DP796BBRR   Flat Hodge factorized-penalty wall (v2
                                                            dossier)
papers/parity-barriers          ARR-2026-5HRC3PS9HZ9WDAA5   Parity barriers for decoupling
                                                            inequalities
papers/o-bridge                 ARR-2026-31ED4MTKC18JPSDE   Dense-family clustering-to-gap criterion
papers/reflection-positivity    ARR-2026-10JJK0VCCS87VTQH   ZN reflection positivity (Z2 instance)
papers/os-quotient              ARR-2026-2TBRDN2DE598KSXD   Degenerate reflection pairing & GNS
                                                            quotient
papers/perron-kernel            ARR-2026-2YDE42KFDY8Y3AA0   Perron theorem for strictly positive
                                                            kernels
papers/perron-gap               ARR-2026-1A608PTGTC9XX9JZ   Finite-extent spectral gap (not uniform)
papers/spatial-extent           ARR-2026-4X084GVAYF87PB3F   Spatial coupling breaks uniform vacuum
papers/spatial-birkhoff         ARR-2026-6M8PMVHTMH8YZ9ND   Second spatial-extent obstruction
papers/spatial-gibbs            ARR-2026-2TTA0WSQBT89X964   Transfer bridge for spatial Z2 slice
papers/spatial-reflection       ARR-2026-02YRWX53DG9M3R0R   Endpoint reflection positivity (Z2 slice)
papers/spatial-os               ARR-2026-223XBWQ8PQ8Z2RDS   Bond reflection positivity & site form
papers/spatial-spectral         ARR-2026-1A7WS4SDF0894BPS   Fluctuation-sector operator bound




                                               5
```

---

## Page 6

```text
Repository Folder                  AIRR Identifier                  Topic / Role
papers/spatial-uniform             ARR-2026-3EXXMXJD119J1R6R        Extent-independent rate (decoupled
                                                                    slice)
papers/congruence-spectrum         ARR-2026-7S1XA3PZEB9QM8FQ        Congruence rigidity and the fusion
                                                                    bound
papers/su2-crossing-compensated ARR-2026-5V5K6T6DQT9J8SY6           Compensated-flow SU(2) crossing Ward
papers/thermodynamic-limit-kp   ARR-2026-5SGNYDASRB9V9VF9           Thermodynamic limit for local Gibbs
                                                                    states
papers/stationary-doob347          ARR-2026-1AS15VP0199VZ847        Boolean Doob kernels: stationary
                                                                    marginals
papers/stationary-weighting354     ARR-2026-4T35VQ6MZB8F99F4        Boolean Doob kernels: moment transfer
papers/os-chain-z2                 Pending AIRR deposit             Complete Z2 Osterwalder–Seiler chain
papers/wronskian-reduction         Pending AIRR deposit             Wronskian identity for antisymmetrized
                                                                    sine sums
                    Table 2: Cross-reference of Yang–Mills and mathematical-physics
                    manuscripts in THE-ERIKSSON-PROGRAMME to AIRR archive identifiers.




6    Reproducibility and Citation
To reproduce the verified Lean 4 core from scratch (on Windows, pass -c core.longpaths=true
due to nested historical audit paths under papers/marginal-transfer/):

git clone -c core.longpaths=true \
  https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME.git
cd THE-ERIKSSON-PROGRAMME
git checkout yang-mills-archive-v1.0
lake exe cache get
lake build YangMillsCore
lake env lean oracle_check.lean
python scripts/check_consistency.py

   The code is released under AGPL-3.0-or-later with machine-readable citation metadata in
CITATION.cff and .zenodo.json.


Disclosure of AI Assistance and Editorial Independence
Parts of the Lean 4 formalization, audit tooling, and manuscript preparation in
THE-ERIKSSON-PROGRAMME were assisted by large language models under the supervision of
the author; every core mathematical claim is independently checked by the Lean 4 kernel
(YangMillsCore) with standard axioms only. The author (Lluis Eriksson) administers the
AIRR archive (https://airr.science/); accordingly, this technical note claims no independent
editorial admission or peer-review endorsement beyond its transparent machine-checked evidence
and explicit scope boundaries.




                                                    6
```
