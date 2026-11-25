# Certified Verification of NEXPTIME-Hardness for Degree-Bounded Local-Sum MPNN Satisfiability

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-6F537FT31Z903828` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/mpnn-degbsat-nexptime-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `803394e2d9a09ae42ab8cf9e6be7f798ca6a256d8aa5c04e174964ba88139010`

## Abstract

Marco Salzer (arXiv:2611.32595, Nov 2026) proved that degree-bounded satisfiability (DEGBSAT) for local-sum Message Passing Neural Networks with ReLU activations and rational node labels is NEXPTIME-hard even at fixed degree bound d = 3, closing the PSPACE-vs-NEXP gap via a proof architecture proposed by GPT-6 Astra. We present a standalone zero-dependency Lean 4.35.0 formalization of 18 core rational-encoding, polyhedral-count, ReLU-FNN, and MPNN acceptance theorems (zero sorry, zero warnings, zero Classical.choice) paired with an exact-Q four-mode certificate verifier (MPNN-DEGBSAT-CERT-1.0) that executes Salzer's full (h+2)-layer MPNN M_w without floating-point arithmetic. Across 16 canonical certificates (0.080-114.497 ms, total 286.40 ms), all invariants replay identically over Q while rejecting 62/62 live adversarial forgery attacks.

## Full Extracted Text

--- Page 1 ---
Certified Verification of NEXPTIME-Hardness for
Degree-Bounded Local-Sum MPNN Satisfiability
Lluis Eriksson∗
November 25, 2026
Abstract
Marco Sälzer (arXiv:2611.32595, Nov. 2026) resolved
the exact complexity of degree-bounded satisfiability
(DegBSat) for local-sum Message Passing Neural Net-
works (MPNNs) with ReLU activations and rational node
labels, closing the gap betweenPSPACE-hardness and the
NEXP upper bound by provingNEXP-hardness already at
fixed degree boundd = 3—via a proof architecture pro-
posed by an AI model (GPT-6 Astra). The reduction packs
arbitrary-length nondeterministic Turing machine (NTM)
tapesintobase-( |Γ|+2)rationalencodings, expressessingle-
step transitions as a finite union∆of rational polyhedra,
recognizes∆and accepting configurations F via exact
ReLU-FNNs, and verifies2 p(|w|)-step runs inp(|w|) + 2
local-sum message-passing layers on degree-≤3trees. We
construct a standalone, zero-dependencyLean 4.35.0for-
malization of 18 core encoding, polyhedral, ReLU-FNN,
and MPNN acceptance theorems (zerosorry, zero warn-
ings, zero Classical.choice) paired with an exact-Q
four-mode certificate verifier (MPNN-DEGBSAT-CERT-1.0)
that executes Sälzer’s full(h+2)-layer MPNNMw without
floating-point arithmetic. Across 16 canonical certificates
(0.080–114.497 ms, total286 .40 ms), all invariants replay
identically overQ while rejecting 62/62 live adversarial
forgery attacks.
1 Introduction
FormalverificationofGraph NeuralNetworksasks whether
a classifying MPNN accepts any graph violating a safety
specification [1, 6]. For local-sum ReLU MPNNs over
arbitrary rational node labels, unbounded-degree satisfia-
bility is undecidable [2], whereas restricting input graphs
to degree at mostd (DegBSat) restores decidability [6]
with anNEXP upper bound whend is given in unary [4].
Sälzer [5] closed the longstandingPSPACE-vs.-NEXP gap
by proving NEXP-hardness even for fixed degreed = 3
(Theorem 6.1 and Corollary 6.2).
The reduction combines four exact rational gadgets:
1. Base-b Tape Encoding (Lemma 3.1):With work-
ing alphabetΓ = {1,...,k} and base b = k + 2,
∗Independent Researcher. Code, Lean 4 proofs, and certificates:
MIT License; manuscript and figures: CC-BY-4.0. Prepared with AI
coding, formalization, and drafting assistance from Google Antigrav-
ity; all proofs, exact-Q verifiers, and adversarial tests were indepen-
dently compiled and verified locally. Repository:https://github.
com/lluiseriksson/mpnn-degbsat-nexptime-certificates
enc(a1 ···a m) = ∑ m
i=1 aib−i + s/((b− 1)bm)lies in
I = [1/(b−1),k/(b−1)](width( k−1)/(k+ 1) <1),
pusha(x) = (x+ a)/band popa(x) = bx−a implement
tape shifts, andpopa(enc(w))∈I⇐⇒a= head(w).
2. Polyhedral NTM Step Relation (Lemma 4.1):
Single steps and accepting-state padding form a union
∆of |Γ|(|δ|+ 1)rational polyhedra in Q6, and accept-
ing configurations formF(|Γ|polyhedra inQ3), soT
accepts w in ≤n steps iff( enc(cw),x) ∈∆n for some
x∈F.
3. ReLU-FNN Polyhedral Union Recognizer
(Lemma 5.1):For S = ⋃n
i=1{x : Aix≤b i},
NS(x) = mini
∑
j relu((Aix−b i)j)is realized exactly
using min(x,y) = relu(x−relu (x−y ))and satisfies
NS(x)≥0withN S(x) = 0⇐⇒x∈S.
4. Binary Run-Tree Local-Sum MPNN (Theo-
rem 6.1):For height h = p(|w|), each node stores
2(h+1)typed blocks( zt,At,Bt)of total dimensiond=
14(h+ 1). LayerN1 evaluates local endpoint-matching,
leaf-∆, and root-Ferrors( x(1)
u )1,(x(1)
u )2 ≥0; h sum-
aggregation layers propagate non-negative errors to the
root v; andNh+2 outputsrelu(1−(x(h+1)
v )1−(x(h+1)
v )2),
accepting iff both errors vanish on a degree-≤3witness
of length2 h.
Contributions and Scope.We do not re-formalize
complexity-class many-one reductions or Turing-machine
time hierarchies inside Lean 4; instead, we pro-
vide an independent machine-checked verification suite
for every algebraic, polyhedral, neural, and graph-
level invariant of [ 5]: (i) 18 zero- sorry, zero-
Classical.choice Lean 4.35.0[ 3] theorems in
MPNNDegBSat.lean; (ii) the zero-floating-point exact-Q
verifier MPNN-DEGBSAT-CERT-1.0; (iii) 16 canonical certifi-
cates (including full exact(h+ 2)-layerMw execution on
degree-≤3accepting and corrupted graphs); and (iv) a
62-attack live adversarial red-team suite with 41-artifact
SHA-256 manifest enforcement.
2 Constructive Lean 4.35.0 Kernel
The standalone modulelean/MPNNDegBSat.lean builds
cleanly under Lean 4.35.0 with zero external libraries,
zero warnings, and zero sorry. Auditing all 18 theo-
rems via #print axioms (AuditAxioms.lean) confirms
2 zero-axiom theorems (none), 16 using only[propext,
1

--- Page 2 ---
Table 1: All 18 machine-checked Lean 4.35.0 the-
orems in MPNNDegBSat.lean (zero sorry, zero
Classical.choice).
# Lean Theorem Identifier Paper Ref. Axioms
1interval_I_well_formedSec. 3p, Q
2blank_encoding_in_ISec. 3none
3blank_encoding_fixed_pointLem. 3.1p, Q
4push_preserves_I_clearedLem. 3.1(1–2)p, Q
5pop_push_left_inverse_clearedLem. 3.1(2)p, Q
6push_pop_right_inverse_clearedLem. 3.1(2)p, Q
7lemma31_pop_separates_wrong_symbol_gtLem. 3.1(3)p, Q
8lemma31_pop_separates_wrong_symbol_ltLem. 3.1(3)p, Q
9lemma31_pop_in_I_iff_eqLem. 3.1(3)p, Q
10delta_polyhedron_count_exactSec. 4 Eq. 1p, Q
11relu_nonneg_and_zero_iffLem. 5.1p, Q
12lemma51_relu_min_exactLem. 5.1p, Q
13lemma51_poly_violation_zero_iffLem. 5.1p, Q
14lemma51_union_min_zero_iffLem. 5.1p, Q
15theorem61_label_dim_exactThm. 6.1p, Q
16theorem61_binary_tree_node_countThm. 6.1p, Q
17theorem61_degree_at_most_3Cor. 6.2none
18theorem61_final_layer_accept_iff_zeroThm. 6.1p, Q
Axiom key:none= zero axioms (2);p, Q=[propext, Quot.sound](16).
Quot.sound], and0using Classical.choice or
Lean.ofReduceBool(Table 1).
Proposition 1(Machine-Checked Core Identities).The
Lean 4.35.0 kernel establishes the following identities uni-
versally overN,Z, andList Int:
1. Exact Tape Encoding & Pop Disambiguation (Thms. 1–
9):For k≥ 1,b = k+ 2,bs= s(b−1) +s; ifD≤x (k+
1) ≤kD and1 ≤a≤k , then( k+ 2)D≤ (aD+ x)(k+
1) ≤k (k+ 2)D; and forD >0, D≤z (k+ 1) ≤kD ,
D≤((h−a)D+z)(k+ 1)≤kD⇐⇒a=h.
2. Polyhedron Count & ReLU-FNN Exactness (Thms. 10–
14): g + gdr + gdl = g(dr + dl + 1); for x,y≥ 0,
relu(x−relu (x−y)) = min(x,y); inductively overList
Int, sumRelu(xs) ≥0with= 0 ⇐⇒ ∀v∈xs,v≤ 0,
and minReluList(acc,vs) ≥0with= 0 ⇐⇒acc =
0∨∃v∈vs,v= 0.
3. MPNN Dimension, Degree 3, & Acceptance Layer
(Thms. 15–18):2( h+ 1)·7 = 14(h+ 1),2 h + (2h −1) =
2h+1 −1, tree degrees2,1 + 2,1 ≤3, and fore1,e2 ≥0,
relu(1−e 1 −e2) = 1⇐⇒e 1 = 0∧e 2 = 0.
3 Exact-QVerifier
The verifier MPNN-DEGBSAT-CERT-1.0
(src/mpnn_certifier.py, src/mpnn_exact.py) uses
Python fractions.Fraction exclusively (source-audited
for zero float(, math., or numpy). Every payload
undergoes strict JSON typing with nesting-depth cap32,
anchored canonical rational parsing (\A...\Z, reduced
denominators ≥2, no trailing newlines), exact key-set
checks, and 2048-bit integer caps across four modes:
1. Mode 1 (Lemma 3.1 Tape Encoding):Com-
putes enc(w) ∈I , verifies pusha(enc(w)) = enc(aw)
and pophead(w)(enc(w)) = enc(tail(w)), and checks
popa(enc(w)) ∈I⇐⇒a = head(w)for all a∈
{1,...,k}.
Figure 1: (a) Lemma 3.1 interval width(k−1)/(k+ 1) <1
and exact minimum wrong-pop distance toI for k= 2 ... 8.
(b) Exponential verified NTM run length2h vs. polynomial
MPNN label dimension14(h+ 1)and depth h+ 2( h=
1...12).
2. Mode 2 (Lemma 4.1 Polyhedral NTM Runs):
Builds all |Γ|(|δ|+ 1)polyhedra of∆ ⊂Q 6 and |Γ|
polyhedra ofF⊂Q 3, checks initial configurationcw,
and verifies exact membership(xj−1,xj) ∈∆for j =
1,...,2 h andx 2h ∈F.
3. Mode 3 (Lemma 5.1 ReLU-FNN Unions):Evalu-
ates the exact ReLU minimum-tree networkNS(x)over
Q against directAix≤b i checks on non-trivial inside
and outside query sets, verifyingNS(x) = 0 ⇐⇒x∈
S.
4. Mode 4 (Theorem 6.1 Full MPNNMw Execu-
tion):Checks simple undirected graph degree≤3and
label dimension14( h+ 1), builds∆and Ffrom the
NTM specification, runs all h+ 2exact- Q message-
passing layers ofMw = ( N1,...,N h+2), and verifies
exact root error flags and final acceptance output
Mw(G,v)∈[0,1].
4 Empirical Atlas and Red-Team
Audit
Runningrun_all_experiments.py produces 16 canonical
certificates(4permode)andfourexact- Q datasets, verified
end-to-end byverify_all.py with SHA-256 enforcement
across all 41 tracked artifacts.
Encoding Separation and Polyhedral NTM Runs
(Fig. 1).Mode 1 (0 .080–0.093 ms) verifies empty-tape
fixed point enc(ϵ) = 3 /4( k = 3 ,b = 5) and multi-
symbol words acrossk∈{ 3,4,6}(147/500,1777 /3240,
153299/229376), confirming exact single-symbolpop dis-
ambiguation. Mode 2 (5.394–20.855 ms) audits 2-, 4-, and
8-step NTM runs (with both right/left head motion and
accepting padding) across|∆|∈{ 18,24}six-dimensional
rational polyhedra.
ReLU-FNN Zero Sets and Full Degree-3 MPNN
Execution (Fig. 2).Mode 3 (0 .361–5.677 ms) audits
exact ReLU-FNN recognizers on 2D disjoint boxes, 3D non-
convex unions, and actual NTM polyhedraF⊂Q 3 and
∆ ⊂Q 6. Mode 4 (18.112–114.497 ms) executes Sälzer’s
2

--- Page 3 ---
Figure 2: (a) Exact Lemma 5.1 ReLU-FNN zero-set profile
NS(x,x)along the diagonal across disjoint boxes P1 =
[0,1]2 and P2 = [3,4]2 (zero iff( x,x) ∈S , peaking at2at
x= 2). (b) Mode 4 exact(h+ 2)-layerMw(G,v)outputs
on degree-≤3witnesses:1on h= 1,2,3accepting trees
vs.2/5(reject) on a corrupted leaf.
Figure 3: (a) Exact zero-float replay la-
tency (0 .080–114.497 ms) across all 16 canonical
MPNN-DEGBSAT-CERT-1.0 certificates. (b) Live adversarial
red-team audit rejecting 62/62 forged payloads across all
five categories.
exact( h+ 2)-layer MPNNMw on degree-≤3binary de-
composition trees of heightsh= 1(3nodes,28-dim), h= 2
(7nodes,42-dim), and h= 3(15nodes,56-dim, verifying
an 8-step padded NTM run withMw(G,v) = 1), plus a
soundness witness where perturbing one leaf coordinate
by+1 /5propagates error3 /5to the root and yields exact
rejectionM w(G,v) = 2/5̸= 1.
Replay Latency and 62/62 Red-Team Audit
(Fig. 3).All 16 canonical certificates replay in0 .080–
114.497 ms (total286 .40 ms). The live adversarial suite
(tests/test_suite.py) executes 62 targeted forgery
attacks—12 global schema/type/rational/newline attacks
plus 12–13 domain attacks per mode (invalid symbols,
wrong pop flags, integer-as-boolean list confusion, dupli-
cate/illegal NTM steps, non-accepting final states, trivial
inside-only/outside-only Mode 3 queries, degree-4graph
violations, self-loops, wrong label dimensions, and forged
acceptanceoncorruptedlabels)—achieving62/62 (100%)
rejection.
5 Conclusion
We delivered a self-contained, zero-floating-point verifica-
tion stack for Sälzer’sNEXP-hardness proof of fixed-degree
(d = 3) local-sum MPNN satisfiability [ 5], combining
18 zero-sorry, zero-Classical.choice Lean 4.35.0 theo-
rems with the exact-Q verifier MPNN-DEGBSAT-CERT-1.0,
16 canonical certificates (including full(h+ 2)-layer exact
Mw execution), and 62/62 adversarial forgery rejections.
References
[1] Pablo Barceló, Egor V. Kostylev, Mikaël Monet, Jorge
Pérez, Juan L. Reutter, and Juan Pablo Silva. The
logical expressiveness of graph neural networks. In
Proceedings of the 8th International Conference on
Learning Representations (ICLR), 2020.
[2] Michael Benedikt, Chia-Hsuan Lu, and Tony Tan. De-
cidability of graph neural networks via logical char-
acterizations.ACM Transactions on Computational
Logic, 27(2):13:1–13:65, 2026.
[3] Leonardo de Moura and Sebastian Ullrich. The Lean 4
theorem prover and programming language. InAuto-
mated Deduction – CADE 28, pages 625–635. Springer,
2021.
[4] MarcoSälzer.The Complexity of Formal Verification of
Neural Network Based Models. PhD thesis, University
of Kassel, 2025.
[5] Marco Sälzer. Degree-bounded satisfiability of local
MPNNs with sum aggregation is NEXPTIME-hard.
arXiv:2611.32595 [cs.CC], 2026.
[6] Marco Sälzer and Martin Lange. Fundamental limits in
formal verification of message-passing neural networks.
InProceedings of the Eleventh International Conference
on Learning Representations (ICLR), 2023.
3
