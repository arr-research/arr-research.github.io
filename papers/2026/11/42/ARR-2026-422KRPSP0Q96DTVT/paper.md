# Machine-Checked Sign-Vector Kernel and Exact-Rational Certificates for Flag Targets, Quasipolyhedral Non-Attainment, Frame Slices, and Acyclic Chamber DAGs

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-422KRPSP0Q96DTVT` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/hyperplane-arrangement-traversal-certificates (`v2.0.0`)  
**Canonical PDF SHA-256:** `5e27f657c240df5f369e79a6a768c7d12a4ebc7389323589ee958075a4a9bbb4`

## Abstract

Brennan Dury (arXiv:2611.32976, November 24, 2026) constructed objective-driven acyclic digraphs on chambers of locally finite affine hyperplane arrangements: from each objective-bounded chamber c, a codimension-r flag at its optimal face F yields 2^r - 1 outgoing targets via a sign-flip rule, and both Euclidean and Frame strategies force escape to strictly higher optimal values in bounded steps. We deliver an explicitly scoped, zero-floating-point verification stack pairing two complementary layers. First, an 18-theorem zero-dependency Lean 4.35.0 kernel (HyperplaneTraversal.lean; 0 sorry, 0 warnings, 0 Classical.choice; 5 zero-axiom, 1 [propext], 12 [propext, Quot.sound]) proves single-coordinate sign-closure poset axioms, combinatorial sign-flip counting/distinctness/containment identities, cleared integer/inductive laws of Section 2 Figure 2's quasipolyhedral non-attainment counterexample (l_n(x) = 2^{-(n+1)}(x-n-2)), and scalar algebraic projections of Lemma 4, Lemma 15, Lemma 17, Proposition 3 (lexLt3), and Theorem 3. Second, ARRANGEMENT-TRAVERSAL-CERT-1.0 performs full multi-dimensional exact-Q verification of codimension ranks, Figure 2 truncations, full-rank Frame slices, and strict-complementarity KKT chamber DAGs across 16 canonical certificates (0.110-1.003 ms)—including a fully specified 8-chamber 4-line central fan DAG (L=3)—while rejecting 66/66 live adversarial forgeries.

## Full Extracted Text

--- Page 1 ---
Machine-Checked Sign-Vector Kernel and Exact-Rational
Certificates for Flag Targets, Quasipolyhedral
Non-Attainment, Frame Slices, and Acyclic Chamber DAGs
Lluis Eriksson∗
November 25, 2026
Abstract
Brennan Dury (arXiv:2611.32976, November 24, 2026)
constructed objective-driven acyclic digraphs on cham-
bers of locally finite affine hyperplane arrangements:
from each objective-bounded chamberc, a codimension-
r flag at its optimal face F yields2 r −1outgoing tar-
gets via a sign-flip rule, and both Euclidean and Frame
strategies force escape to strictly higher optimal val-
ues in bounded steps. We deliver an explicitly scoped,
zero-floating-point verification stack pairing two comple-
mentary layers. First, an 18-theorem zero-dependency
Lean 4.35.0 kernel (HyperplaneTraversal.lean; 0sorry,
0 warnings, 0 Classical.choice; 5 zero-axiom, 1
[propext], 12 [propext, Quot.sound]) proves single-
coordinate sign-closure poset axioms, combinatorial sign-
flip counting/distinctness/containment identities, cleared
integer/inductive laws of Section 2 Figure 2’s quasipolyhe-
dral non-attainment counterexample (ℓn(x) = 2−(n+1)(x−
n− 2)), and scalar algebraic projections of Lemma 4,
Lemma 15, Lemma 17, Proposition 3 (lexLt3), and The-
orem 3. Second,ARRANGEMENT-TRAVERSAL-CERT-1.0 per-
forms full multi-dimensional exact-Q verification of codi-
mension ranks, Figure 2 truncations, full-rank Frame slices,
and strict-complementarity KKT chamber DAGs across 16
canonical certificates (0.110–1.003 ms)—including a fully
specified 8-chamber 4-line central fan DAG (L= 3)—while
rejecting 66/66 live adversarial forgeries.
1 Introduction and Scope Calibra-
tion
Classical chamber-traversal constructions on real hyper-
plane arrangements—such as Edelman’s walk [ 4] and
Salvetti–Settepanella polar paths [5]—navigate toward a
fixed base chamber. Brennan Dury [3] introduced objective-
driven acyclic chamber digraphs on locally finite affine
hyperplane arrangementsPwith a nonconstant affine ob-
jectiveω, built on four algebraic and geometric mechanisms:
1. Sign-vector face calculus & Theorem 2 targets:Faces
are nonempty relatively open fibres ofx↦→signP(x) ∈
∗Independent researcher; manuscript prepared with transparent AI
assistance via Google Antigravity. Source code (MIT), Lean 4 proofs
(MIT), and manuscript/figures (CC-BY-4.0):https://github.com/l
luiseriksson/hyperplane-arrangement-traversal-certificates.
{−1,0,+1}P, ordered by closure containment E⊆
F⇐⇒ ∀q,sign E(q) ∈{0,sign F(q)}(Proposition 1).
A codimension-r flag of facesF = Fr,Fr−1,...,F 0 = c
with Fi ⊆Fi−1 and codim(Fi) =ipartitions the vanish-
ing formsQ(F,P) =Q1 ⊔···⊔Q r into nonempty layers
Qi := Q(Fi,P) \Q(Fi−1,P); writing ℓ(q) ∈{1,...,r}
for the unique layer index withq∈Q ℓ(q), every α∈
{±1}r \{1r}defines one of2 r −1distinct outgoing
target chambersbFL(α)[1] via
signbFL(α)(q) =
{
αℓ(q) signc(q), q∈Q(F,P),
signc(q), q /∈Q(F,P). (1)
2. Figure 2 quasipolyhedral non-attainment (Section 2):
While every bounded-above affine objective on a closed
face of a locally finite arrangement attains its supremum
(Theorem 1), C = {(x,y) : y≤ℓ n(x) ∀n≥ 0}with
ℓn(x) = 2−(n+1)(x−n− 2)has y <0everywhere yet
ω(pn) =−2−n →0; every lineHn hits {0}×[−1,0]at
yn =−(n+ 2)2 −(n+1), violating local finiteness.
3. Frame slice recursion & strict potential (Section 6,
Lemma 17, Proposition 3):Normalizing tangent-cone
generators onto Pη(c,G) = RG(c) ∩{η = −1} via
vH = −ξH/η(ξH)and uniquely maximizing an admissi-
ble frame covectorφ yields strictly negative next cov-
ector valuesη+(q−p ) = φ(q) −φ(p) < 0, strictly in-
creasing the( r+ 1)-component lexicographic potential
P∗
F(c) = (λ(c,ω),dimF(c,ω),S F
r (c),...,S F
2 (c)).
4. Acyclicity & uniform escape lengthL (Theorem 3 &
Theorem 5):Because GF is acyclic on finite level sets,
every directed walk of lengthL = Lmax + 1escapes
strictly above its starting optimal valueλ(c0,ω).
Honest Two-Layer Scope Calibration.We distin-
guish strictly between what is proved universally in Lean 4
vs. verified in full dimension on finite rational witnesses vs.
left in [3]:
1. Lean 4 kernel (§2, Table 1):18 zero-dependency
constructive theorems inHyperplaneTraversal.lean
(Lean 4.35.0 [ 2]; 0 sorry, 0 warnings,
0 Classical.choice). Table 1 prints every ex-
act theorem type, hypothesis, and axiom footprint
verbatim.
1

--- Page 2 ---
2. Exact-Q multi-dimensional verifier (§3, Ta-
ble 2): ARRANGEMENT-TRAVERSAL-CERT-1.0 performs
full vector-space Gaussian rank checks, exact Fig-
ure 2 feasibility, full-rank Frame slices, and strict-
complementarity KKT chamber DAG certification with
zero floats.
3. Explicit non-claims:Our Lean 4 kernel doesnotfor-
malize general vector-space hyperplane arrangements,
polyhedral faces, LP duality, multi-dimensional chamber
DAGs, Theorem 1 compactness, or Lemma 18 Zariski-
open admissibility; Theorems 1–8 and 13–18 formal-
ize their exact single-coordinate sign calculus, counting
identities, and cleared scalar/3-tuple algebraic projec-
tions, while multi-dimensional geometry is audited by
ARRANGEMENT-TRAVERSAL-CERT-1.0.
2 Zero-Dependency Lean 4 Kernel
lean/HyperplaneTraversal.lean compiles standalone
under Lean 4.35.0 with zero external dependencies and
is audited byAuditAxioms.lean with 0 warnings, 0sorry,
0 Classical.choice, and 0Lean.ofReduceBool: 5 zero-
axiom (none: #1–3, #5, #7), 1[propext] (#6), and 12
[propext, Quot.sound].
Proposition 1(Constructive Scope of
HyperplaneTraversal.lean).All 18 statements in
Table 1 hold constructively without external libraries or
Classical.choice. In particular, Theorem 11 inductively
proves0 <n + 2≤2n+1 for alln∈N (showing every line
Hn of Figure 2 meets{0}× [−1,0]), Theorem 14 proves
strict partial-order acyclicity oflexLt3, Theorem 15 proves
Lemma 17’s negative next covectorφq−φp <0 <φp−φq,
and Theorem 16 provesηξ = (−1)D< 0under the explicit
hypothesis0<D.
3 Exact-QVerifier Architecture
The pure-stdlib zero-float veri-
fier src/arrangement_certifier.py
(ARRANGEMENT-TRAVERSAL-CERT-1.0) enforces strict
JSON typing, canonical reduced rationals, and uniform
2048-bit / 1024-char / 128-char ID bounds across four
modes:
1. Mode 1 (Theorem 2 Flag Sign Targets):Evaluates
interior witness points along F0 = c,F1,...,F r = F
with Fi ⊆Fi−1, verifies exact Gaussian codimension
rank rank(Q(Fi,P)) =i at every level and exact layer
partition Q1 ⊔···⊔Q r, and certifies that all2r−1target
witnesses realize(1), are pairwise distinct, and contain
Fin their closures.
2. Mode 2 (Section 2 Figure 2 Counterexam-
ple):Independently verifies exact interpolation pk =
(k,−2−k) ∈Hk ∩Hk−1, all( N + 1)2 halfplane inequal-
ities y(pk) ≤ℓ n(x(pk)), compact-segment intercepts
y0(Hn) = −(n+ 2)2−(n+1) ∈[−1,0), and exact gap
0−ω(p N) = 2−N.
Figure 1: (a) Exact Theorem 2 outgoing target fanout2r−1
vs. total flag chambers2r across codimensionsr= 1... 8.
(b) Section 2 Figure 2 exact supremum gap−ω(pn) = 2−n
and origin intercept|y0(Hn)|= (n+ 2)2−(n+1) ≤1across
n= 0...12.
3. Mode 3 (Section 6 Frame Slice & Potential):
Enforces full-rank tangent cones (rank = d), pairwise
distinct slice vertices vk = −ξk/η(ξk) ∈ {η= −1}
with distinct source/target slices, valid face dimensions
0 ≤dimF < d, unique admissibility ofarg maxφ(vk),
Lemma 17 next-covector negativityη+(q−p ) =φ(q) −
φ(p)<0onkerη, and strict increaseP ∗(c)<lex P∗(b).
4. Mode 4 (Acyclic Chamber DAG & EscapeL):
On every objective-bounded chamberc, enforces non-
negativity yk ≥0, strict complementarity (yk >0 ⇐⇒
qk(x∗) = 0,yk = 0 ⇐⇒q k(x∗) ̸= 0), and LP dual sta-
tionaritycω+∑
kykσkak = 0certifyingx∗∈relint (F(c))
anddimF(c) =d−rank(Q(F(c),P)); on every objective-
unbounded chamber, verifies a positive recession ray and
canonical zero/empty fields. It then checks that every
objective-bounded chamber’s outgoing edges match all
2r−1Theorem 2 targets of its flag layers withF(c) ⊆b,
checks strict increase of the certified 3-tuple potential
proxy( λ,dimF,S )(exact for r≤ 2, and sufficient on our
r= 3octant where all targets jump toλ= ∞; Dury’s
general P∗
F has r+ 1components for r≥ 3), certifies
Kahn DAG acyclicity, and computesL=Lmax + 1.
4 Empirical Atlas, Explicit 4-Line
Fan, and Red-Team Audit
Running scripts/run_all_experiments.py produces all
16 canonical certificates (Table 2) and four exact-Q datasets,
audited end-to-end byscripts/verify_all.py with SHA-
256 verification across all 41 tracked files.
Explicit Verification of the 8-Chamber 4-Line Cen-
tral Fan DAG (Fig. 2(a)).Certificate #15 uses the
four central linesH0 : x2 = 0,H1 : x1 = 0,H2 : x1 −x2 = 0,
H3 : x1 + x2 = 0and objective ω(x) = x2. In the lower
half-plane (x2 <0), the four objective-bounded sectors are,
from left to right:
•c LL at( −2,−1), signs( −,−,−,−): adjacent to H0,
so F = {x2 = 0,x1 ≤0}(dim 1), x∗ = (−1,0), y =
(1,0,0,0), layer[[0]], unique target cUL = (+,−,−,−)
at(−2,1).
2

--- Page 3 ---
Table 1: Complete inventory of all 18 Lean 4.35.0 theorems inlean/HyperplaneTraversal.lean with exact quantified
statements, hypotheses, and audited axiom footprints (0sorry, 0 warnings, 0Classical.choice; P,Q abbreviates
[propext, Quot.sound]).
# Lean 4 Theorem Identifier Exact Machine-Checked Statement & Hypotheses Axioms
1sign_closure_reflexive∀s∈Sign,signLes s(wheresignLea b:⇐⇒a= 0∨a=b).none
2sign_closure_transitive∀a,b,c∈Sign,signLea b→signLeb c→signLea c.none
3sign_closure_antisymmetric∀a,b∈Sign,signLea b→signLeb a→a=b.none
4theorem2_target_count_formula∀r∈N,1≤r→1 + (2 r −1) = 2r ∧1≤2 r −1.P,Q
5theorem2_sign_identity_at_ones∀s∈Sign,flipSign trues=s.none
6theorem2_distinct_targets_opposite_sign∀a,b∈Bool, s∈Sign, s̸= 0→a̸=b→flipSigna s̸=flipSignb s.propext
7theorem2_base_containment_preserved∀α∈Bool, s∈Sign,signLe0 (flipSignα s).none
8lemma4_weak_objective_increase∀λ c,λb,x∗∈Z, λc =x∗→x∗≤λb →λc ≤λb (scalar projection).P,Q
9fig2_line_passes_through_pn_and_pn1∀n∈Z,(n−n−2 =−2)∧((n+ 1)−n−2 =−1)(clearedℓ n(pn),ℓn(pn+1)).P,Q
10fig2_line_envelope_domination∀n,x∈Z,(x−(n+ 1)−2)−2(x−n−2) = (n+ 1)−x(cleared envelope step).P,Q
11fig2_origin_intercept_in_compact_unit_segment∀n∈N,0<n+ 2∧n+ 2≤2 n+1 (inductive proofy0(Hn)∈[−1,0)).P,Q
12fig2_strict_negativity_on_C∀x,n∈Z, x+ 1≤n→x−n−2≤−3∧x−n−2<0.P,Q
13opposite_ray_negativity_impossible∀u∈Z, u<0→−u<0→⊥(scalar opposite-ray contradiction).P,Q
14lex_potential_strict_increase_trans∀a,b,c∈Z 3,lexLt3a b→lexLt3b c→lexLt3a c∧¬lexLt3a a.P,Q
15lemma17_slice_denominator_positive∀φ p,φq ∈Z, φq <φp →φq −φp <0∧0<φ p−φq.P,Q
16slice_vertex_normalization_identity∀η ξ,D∈Z,0<D→η ξ =−D→η ξ = (−1)·D∧η ξ <0.P,Q
17dag_escape_length_bound∀r 0,t,K∈N, r 0 +t<K→t<K(scalar rank-escape bound).P,Q
18euclidean_inner_product_opposite_unit_neg∀u c,ub ∈Z, uc <0→−u c ≤ub →ub <0→⊥(scalar Lem. 15 projection).P,Q
Table 2: Complete 16-certificateARRANGEMENT-TRAVERSAL-CERT-1.0 atlas with explicit dimensions, parameters, exact
certified witness invariants, and median zero-float replay latencies (all 16 verified; 66/66 live adversarial attacks rejected).
# Certificate ID Mode Explicit Certified Parameters ms
1m1_flag_2d_axes_fig4_panel1M1d=2,r=2(Dury Fig. 4a:x 1,x2,x1+x2=0): layers[[1],[0,2]],3distinct targets. 0.147
2m1_flag_2d_axes_fig4_panel2M1d=2,r=2(Dury Fig. 4b:x 1,x2,x1+x2=0): layers[[0],[1,2]],3distinct targets. 0.148
3m1_flag_3d_coupled_codim3M1d=3,r=3(5coupled planes): layers[[2],[1,4],[0,3]], exact ranks0,1,2,3,7targets. 0.344
4m1_flag_4d_affine_codim4_15targetsM1d=4,r=4(7planes, 1 non-central): layers[[3],[2,5],[1],[0,4]],15distinct targets. 1.003
5m2_fig2_counterexample_N4M2 Sec. 2 Fig. 2 truncationN=4:25halfplane checks,y 0 ∈[−1,0), gap= 1/16. 0.137
6m2_fig2_counterexample_N8M2 Sec. 2 Fig. 2 truncationN=8:81halfplane checks,y 0 ∈[−1,0), gap= 1/256. 0.256
7m2_fig2_counterexample_N12M2 Sec. 2 Fig. 2 truncationN=12:169halfplane checks,y 0 ∈[−1,0), gap= 1/4096. 0.506
8m2_fig2_counterexample_N16M2 Sec. 2 Fig. 2 truncationN=16:289halfplane checks,y 0 ∈[−1,0), gap= 1/65536. 0.860
9m3_frame_2d_same_face_lex_stepM3d=2, full-rank cones:λ=0,dimF=0,S F:−1/2→1,η + =−5/2<0. 0.110
10m3_frame_3d_simplex_slice_stepM3d=3, simplicial cones:λ=5,dimF=0,S F: 0→1,η + ∈{−2,−1}. 0.168
11m3_frame_3d_dim_jump_stepM3d=3, full-rank cones:λ=3,dimF: 0→1,η + ∈{−5/2,−2}. 0.186
12m3_frame_4d_objective_jump_stepM3d=4, full-rank cones:λ: 2→7/2,dimF=0,η + ∈{−3,−2,−1}. 0.265
13m4_dag_2d_cross_4chambersM4d=2cross (x 1,x2=0),ω=x 1+2x2:1obj-bounded,3unbounded,L max=0,L=1. 0.201
14m4_dag_2d_grid_9chambersM4d=2 2×2grid,ω=x 1+2x2:4obj-bounded,5unbounded,L max=0,L=1. 0.580
15m4_dag_2d_degenerate_escape_L3M4d=24-line fan (H 0..H3),ω=x 2:4obj-bounded,4unbounded,L max=2,L=3. 0.683
16m4_dag_3d_octants_8chambersM4d=3octants,ω=x 1+2x2+3x3:1obj-bounded (7edges),7unbounded,L=1. 0.341
•c LM at( −1,−2), signs( −,−, +,−): bounded above by
x1 ≤0andx 2 ≤x1, soF={(0,0)}(dim 0) with strict-
complementarity KKTy= (1/4,1/4,1/2,1/4) ≥0satis-
fying(0 ,1) +∑ ykσkak = (0,0). Layers[[1] ,[0,2,3]]flip
{1}↦→(−,+,+,−) = cRM, {0,2,3}↦→(+,−,−, +) =
cUML at( −1,2), and{0,1,2,3}↦→(+,+,−, +) =cUMR
at(1,2).
•c RM at(1 ,−2), signs( −,+,+,−): bounded above by
x1 ≥0and x2 ≤−x 1, so F = {(0,0)}(dim 0) with
y = (1/4,1/4,1/4,1/2) ≥0. Layers[[3] ,[0,1,2]]flip
{3}↦→(−,+,+,+) = cRR, {0,1,2}↦→(+,−,−,−) =
cUL, and{0,1,2,3}↦→(+,−,−,+) =c UML.
•c RR at(2 ,−1), signs( −,+,+,+): adjacent to H0, so
F = {x2 = 0,x1 ≥0}(dim 1), x∗= (1,0), y= (1,0,0,0),
layer[[0]], unique targetcUR = (+,+,+,+)at(2,1).
Thus cLM(dim 0) →cRM(dim 0) →cRR(dim 1) →cUR(∞)
is an exact certified walk withLmax = 2and L= 3, match-
ing Eq. (1) on every single edge.
Replay Atlas and 66/66 Red-Team Audit (Fig. 3).
All 16 canonical certificates replay in0.110–1.003 ms with
Figure 2: (a) Certified 8-chamber 4-line central fan DAG
(H0 : x2=0, H1 : x1=0, H2 : x1−x2=0, H3 : x1+x2=0)
under ω(x) =x2: orange same-level pathcLM →c RM →
cRR (λ= 0) and blue escape edges (λ→∞ ), givingL= 3.
(b) Theorem 3 uniform escape lengthL= Lmax + 1scaling
across level-set widthsk= 1...8.
zero floats. Our red-team suite (tests/test_suite.py)
tests 66 live forgery attacks (12 global schema/type/rational
+ 13 Mode 1 + 12 Mode 2 + 14 Mode 3 + 15 Mode 4—in-
cluding float/None/bool injection, unreduced fractions,
codimension rank-jump bypasses, broken flag closures, miss-
3

--- Page 4 ---
Figure 3: (a) Exact zero-float replay latency across all 16
canonical certificates (0.110–1.003 ms). (b) Live adversarial
red-team audit rejecting 66/66 forgeries across five attack
classes.
ing Theorem 2 targets, forged Figure 2 vertices/intercepts,
rank-deficient cones, negative yk, boundary- x∗ strict-
complementarity bypasses, forgeddimF, dropped DAG
edges, and cycles), achieving66/66 rejectionswith zero
bypasses.
5 Conclusion
We delivered an explicitly scoped 18-theorem zero-
dependency Lean 4.35.0 kernel (0 sorry, 0 warn-
ings, 0 Classical.choice, 5 zero-axiom theorems)
paired with the exact- Q multi-dimensional verifier
ARRANGEMENT-TRAVERSAL-CERT-1.0, 16 explicit canonical
certificates (0.110–1.003 ms), full explicit verification of the
8-chamber 4-line central fan DAG (L= 3), and 66/66 live
adversarial forgery rejections.
References
[1] Marcelo Aguiar and Swapneel Mahajan.Topics in Hy-
perplane Arrangements, volume 226 ofMathematical
Surveys and Monographs. American Mathematical So-
ciety, 2017.
[2] Leonardo de Moura and Sebastian Ullrich. The Lean 4
theorem prover and programming language. InAuto-
mated Deduction – CADE 28, pages 625–635. Springer,
2021.
[3] Brennan Dury. Traversing hyperplane arrangements
with an affine objective. arXiv:2611.32976 [math.CO],
2026.
[4] Paul H. Edelman. A partial order on the regions ofRn
dissected by hyperplanes.Transactions of the American
Mathematical Society, 283(2):617–631, 1984.
[5] Mario Salvetti and Simona Settepanella. Combinatorial
Morse theory and minimality of hyperplane arrange-
ments.Geometry & Topology, 11(3):1733–1766, 2007.
4
