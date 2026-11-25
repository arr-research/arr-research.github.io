# Tropical Spanning Criteria, Exact F2-Polynomial No-Strings Certificates, and Machine-Checked Energy-Barrier Bounds for 3D Translation-Invariant Stabilizer Codes

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-05022X80229X1V76` (v1)  
**Intake Receipt:** `SUB-D5B66C38DC781D96`  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/fracton-barrier-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `c5177c87c8d209b258787492e6a448c888cb967e5055e739e404f80445d822c3`

## Abstract

Certifying that a three-dimensional translation-invariant CSS or trivariate bicycle (TB) stabilizer code is a genuine Type-II fracton phase—free of mobile string-like logical operators along every lattice direction v in Z^3 \ {0} and of every period p >= 1—is the algebraic gatekeeper for logarithmic energy barriers and partial self-correction. Recent universal certification frameworks (e.g., Xu & Xu, arXiv:2611.06469) and formal QEC verification libraries (QECert, arXiv:2611.05047) highlight a persistent gap: directional tests restricted to coordinate axes or short lattice vectors can be fooled by higher-slope stealth strings, while floating-point or heuristic solvers leave formal soundness gaps. We close this gap with three tightly integrated contributions. First, we prove the Tropical Spanning Criterion (Theorem 2.3): because every element of F_2bar^* is a root of unity, a nontrivial coprime 2-generator 3D translation-invariant CSS code (f, g) in F_2[x^{+-1}, y^{+-1}, z^{+-1}]^2 (gcd(f, g) = 1, <f, g> != R) satisfies the Universal All-Direction No-Strings Condition if and only if every geometrically irreducible curve component C_i of V(f, g) in (F_2bar^*)^3 has a full-rank tropical valuation fan, rank_Q(Trop(C_i)) = 3. Second, we introduce a zero-floating-point-trust certificate format (FRACTON-CERT-1.0) combining exact F_2[x,y,z] resultant Bezout cofactors, six F_2[t] axis-content Bezout witnesses, exact F_4(t) birational parameterizations with explicit rational inverses t = N(x,y)/D(x,y) (Proposition 3.1, blocking reducible-factor forgeries by reduced-degree matching), exact component completeness prod_i H_i(x,y) = R_z(x,y), and exact place-valuation ray matrices with det(W) != 0, alongside dual coprime F_2[x,y,z]/F_4-point obstruction certificates for string-harboring codes. Third, we mechanize 16 core algebraic, tropical, and conditional scale-ladder energy-barrier theorems culminating in B(d) >= c_1 floor(log_{2*beta+3}(d/R_0)) (Theorem 4.1) in zero-dependency Lean 4 (v4.35.0, 0 sorry, 0 Classical.choice). Across a systematic scan of 155 weight-4 and weight-5 3D TB codes (strictly separating 1 non-coprime code and 10 trivial product-state codes with <f,g> = R, leaving 144 nontrivial codes), 24/103 (23.3%) of nontrivial codes passing all coordinate-axis checks—and 23/102 (22.5%) passing all 13 unit-box directions (||v||_inf = 1)—harbor ||v||_inf = 2 stealth rigid strings such as v = (0,-1,2) and v = (-2,-1,2), collapsing their energy barriers to E_string <= 6 despite fracton-like finite-torus homology k(L); extending the screen to ||v||_inf = 3 exposes 12 additional traps, raising nontrivial false-positive rates to 35.0% (axis-only) and 34.3% (unit-box). All 8 published atlas certificates verify with zero floating-point operations and reject 26/26 live adversarial forgery and type-injection attacks.

## Full Extracted Text

--- Page 1 ---
Tropical Spanning Criteria, ExactF2-Polynomial
No-Strings Certificates, and Machine-Checked
Energy-Barrier Bounds for 3D Translation-Invariant
Stabilizer Codes
Lluis Eriksson∗
November 24, 2026
Abstract
Certifying that a three-dimensional translation-invariant CSS or trivariate bicycle (TB)
stabilizer code is a genuine Type-II fracton phase—free of mobile string-like logical operators
alongeverylattice direction v∈Z 3 \{0}and ofeveryperiod p≥ 1—is the algebraic gatekeeper
for logarithmic energy barriers and partial self-correction. Recent universal certification
frameworks (e.g., Xu & Xu, 2026) and formal QEC verification efforts highlight a persistent
gap: directional tests restricted to coordinate axes or short lattice vectors can be fooled by
higher-slope “stealth strings,” while floating-point or heuristic solvers leave formal soundness
gaps. We close this gap with three tightly integrated contributions. First, we prove the
Tropical Spanning Criterion(Theorem 2.3): because every element ofF
×
2 is a root of unity,
a nontrivial coprime 2-generator 3D translation-invariant CSS code(f,g) ∈F 2[x±1,y±1,z±1]2
(gcd(f,g) = 1, ⟨f,g⟩̸ = R) satisfies the Universal All-Direction No-Strings Conditionif and
only ifevery geometrically irreducible curve componentCi ⊂V (f,g) ⊂(F
×
2 )3 has a full-rank
tropical valuation fan,rankQ(Trop(Ci)) = 3. Second, we introduce a zero-floating-point-trust
certificate format (FRACTON-CERT-1.0) combining exactF2[x,y,z ]resultant Bézout cofactors,
six F2[t]axis-content Bézout witnesses, exactF4(t)birational parameterizations with explicit
rational inverses t = N(x,y)/D(x,y)(Proposition 3.1, blocking reducible-factor forgeries
by reduced-degree matching), exact component completeness∏
iHi(x,y) = Rz(x,y), and
exact place-valuation ray matrices withdet(W) ̸= 0, alongside dual coprimeF2[x,y,z ]/F4-
point obstruction certificates for string-harboring codes. Third, we mechanize the algebraic,
tropical, and scale-ladder energy-barrier core—16 theorems culminating in the conditional
logarithmic bound B(d) ≥c 1⌊log2β+3(d/R0)⌋(Theorem 4.1)—in zero-dependency Lean 4
(v4.35.0) with0 sorry and0 Classical.choice. Across a systematic scan of 155 weight-4
and weight-5 3D TB codes (strictly separating 1 non-coprime code and 10 trivial product-state
codes with ⟨f,g⟩ = R, leaving 144 nontrivial codes),24/103 (23.3%)of nontrivial codes
passing all coordinate-axis checks—and23/102 (22.5%)passing all 13 unit-box directions
(∥v∥∞= 1)—harbor ∥v∥∞= 2stealth rigid strings such asv= (0,−1,2)and v= (−2,−1,2),
collapsing their energy barriers toEstring ≤6despite fracton-like finite-torus homologyk(L);
extending the screen to∥v∥∞= 3exposes 12 additional traps, raising nontrivial false-positive
rates to35.0%(axis-only) and34.3%(unit-box). All 8 published atlas certificates verify
with zero floating-point operations and reject 26/26 live adversarial forgery and type-injection
attacks.
1 Introduction
Self-correcting quantum memories aim to protect encoded quantum information passively against
thermal noise via macroscopic energy barriers between orthogonal ground states [5, 14, 3, 4]. In
∗Independent researcher (Sweden). Prepared with AI assistance (Google Antigravity). Code, Lean 4 proofs, and
exact F2/F4/Z certificates: https://github.com/lluiseriksson/fracton-barrier-certificates (MIT license).
1

--- Page 2 ---
three spatial dimensions, Haah’s Cubic Code A [7] established the paradigm ofType-II fracton
stabilizer codes: 3D translation-invariant CSS Hamiltonians withno string-like logical operators,
forcing any sequence of single-qubit Pauli operations mapping between logical states on a distance-
d lattice to overcome a logarithmically growing energy barrierEmin(d) = Ω(logd)[ 3, 11, 12]. In
Haah’s Laurent-polynomial module formalism [8], a 2-generator CSS / trivariate bicycle (TB) code
over R= F2[x±1,y±1,z±1]is specified by two coprime polynomials(f,g) ∈R2 with ⟨f,g⟩̸ = R,
and the absence of mobile excitations is equivalent to the algebraicno-strings condition: for every
nonzero lattice vectorv = (vx,vy,vz) ∈Z 3 \{0}and every periodp≥ 1, the shifted binomial
1 +up
v (whereu v =xvx yvy zvz ) is a non-zero-divisor in the excitation moduleR/⟨f,g⟩.
Recent breakthroughs in November 2026 have sharpened both the physics and formal-
verification frontiers of this problem. Xu & Xu [13] proposed universal certification criteria
for partially self-correcting 3D translation-invariant stabilizer codes, while high-rate bivariate and
trivariate bicycle LDPC architectures [2] and formal QEC libraries in Lean 4 [9] have underscored
the demand for machine-checkable guarantees rather than heuristic numerical screening. Yet
certifying theuniversalquantifier overalldirections v∈Z 3 \{0}andallperiods p≥ 1faces three
sharp mathematical and engineering obstacles:
1. Stealth Strings Beyond Coordinate Axes and Unit-Box Diagonals.Testing only the
three coordinate axes(1,0,0),(0,1,0),(0,0,1)—or even all 13 primitive directions in the unit
box ∥v∥∞= 1—cannot rule out higher-slope rigid strings such asy+z2 ∈⟨f,g⟩ (v= (0,−1,2))
or x2y+z2 ∈⟨f,g⟩ (v= (−2,−1,2)). Worse, stealth-string codes can exhibit wildly oscillating
finite-torus logical qubit countsk(L)indistinguishable by eye from Type-II fractons, while
naive scans that omit torus-unit filtering can also misclassify trivial product-state codes
(⟨f,g⟩=R) as fractons.
2. Component Completeness and Reducible-Factor Forgery.Checking a single algebraic
branch of the characteristic varietyV(f,g) ⊂(F×
2 )3 is unsound if an omitted or reducible
factor hides a mobile excitation sector. Any independently checkable certificate must certify
both thateveryirreducible component has been accounted for and that no claimed component
is secretly reducible.
3. Floating-Point and Informal Proof Gaps.Numerical Gröbner or tropical approximations
over C cannot be trusted in characteristic2, and hand-waved energy-barrier derivations leave
subtle gaps between algebraic no-strings criteria and hierarchical cluster-merging inductions.
Contributions.We resolve all three obstacles within a single exact, machine-checked framework:
• Exact Tropical Spanning Criterion (Theorem 2.3).Leveraging the defining arithmetic
property ofF2—every nonzero scalarc∈ F×
2 is a root of unity—we prove that the Universal
All-Direction No-Strings Condition holds for nontrivial coprime(f,g) ∈R 2 if and only if
every geometrically irreducible componentCi ⊂V (f,g) ⊂(F×
2 )3 has rankQ(Trop(Ci)) = 3.
Conversely, any rank-≤2component produces an exact primitive kernel vectorv∈Trop (Ci)⊥∩
(Z3 \{0})exposing a rigid string operator.
• Zero-Float FRACTON-CERT-1.0 Certificates & Birational Irreducibility (Section 3).
We design a self-contained exactF2/F4/Z certificate format and pure-Python verifier with
zero floating-point operationsand recursive rejection of anyfloat or bool anywhere in the
JSON tree. Using exact birational inversest= N(x,y)/D(x,y)and reduced F4[t]GCD degree
matching (Proposition 3.1), the verifier proves geometric irreducibility of each plane-curve
factor Hi(x,y)and exact completeness ∏
iHi(x,y) = Rz(x,y), closing reducible-component
forgery attacks completely. Dual coprime obstruction certificates prove string existence via
exact F2[x,y,z ]identities pcf + qcg= (m1 + m2)S paired with anF4-torus pointP∈V (f,g)
withS(P)̸= 0.
2

--- Page 3 ---
• Zero-Dependency Lean 4 Kernel (Section 4).We formalize 16 core theo-
rems in lean/FractonBarrier.lean on leanprover/lean4:v4.35.0 [6] with0 sorry,
0 Classical.choice, and zero external library dependencies, covering CSS commuta-
tion, Bézout-scaled Koszul elimination, homomorphism soundness on ⟨f,g⟩, F4-point
nontriviality, axis-content refutation, exact3×3integer Cramer tropical spanning, tropical
kernel orthogonality, conditional hierarchical logarithmic barrier induction, and finite-torus
homology.
• 8-Code Certified Atlas & 155-Code 3D TB Stealth-String Scan (Section 5).
We certify four Type-II fracton codes (Haah Cubic Code A,TB-Fracton-5, TB-Fracton-7,
TB-Fracton-11) and four string-harboring codes (including two stealth traps passing all 13
unit-box checks), compute exactF2 torus homologyk(L)for L= 2 ... 9, and quantify a23.3%
(through ∥v∥∞≤2) to35.0%(through ∥v∥∞≤3) axis-only false-positive rate and22.5%to
34.3%unit-box stealth-string false-positive rate among the 144 nontrivial 3D TB codes.
2 Algebraic Framework and the Tropical Spanning Criterion
2.1 Laurent-Polynomial Module Formalism for 2-Generator 3D CSS Codes
Let R= F2[x±1,y±1,z±1]be the Laurent polynomial ring overF2 representing translations on
the 3D cubic latticeZ3, with involutionh(x,y,z ) = h(x−1,y−1,z−1). A 2-generator translation-
invariant CSS (equivalently, 3D trivariate bicycle) code places two physical qubits per unit cell and
assigns oneX-type and oneZ-type stabilizer check per site via parity-check mapsσX : R2 →R
andσ Z :R2 →Rdefined by
σX(a,b) = fa+ gb, σ Z(c,d) =gc+fd,(1)
for polynomialsf,g∈F 2[x,y,z ] ⊂R (shifted to nonnegative exponents without loss of generality).
Exact CSS commutation holds unconditionally in characteristic2because the symplectic inner
product between theX-check row(f,g)and theZ-check row( g,f)is
fg+g f=fg+gf= 0inR(2)
(mechanized in Lean ascss_exact_commutation). A Z-type Pauli error supported on sublattices
(p,q) ∈R2 produces theX-check syndromeϵ(p,q) = pf + qg∈R (in lean/FractonBarrier.lean
we equivalently writesyndrome f g a b = g * a + f * b with stabilizer( fq,gq ), obtained by
swapping the two sublattice entries(p,q) ↔(b,a)). LocalZ-stabilizers( gh,fh)satisfy ϵ(gh,fh) =
(gf + fg)h = 0( stabilizer_in_kernel). Given any Bézout identityuf + vg = r, every kernel
element satisfies the Bézout-scaled Koszul elimination identityra= f(ua+vb)and rb= g(ua+vb)
(mechanized askoszul_local_exactness); when gcd(f,g) = 1in the UFD R, cancellation ofr
yields exactness of the Koszul complex atR2, so every finite-support zero-syndrome operator is a
local stabilizer and the topological charge module isM=R/⟨f,g⟩.
Definition 2.1(Universal All-Direction No-Strings Condition).For v= (vx,vy,vz) ∈Z 3 \{0},
write uv = xvx yvy zvz ∈R ×. A nontrivial coprime 2-generator CSS code(f,g)( gcd(f,g) = 1,
⟨f,g⟩̸ = R) admits arigid string operatorof directionvand periodp≥ 1if there exists a nontrivial
excitationS∈R\⟨f,g⟩such that
(1 +up
v)S∈⟨f,g⟩,(3)
i.e., there exist cofactorspc,qc ∈R with pcf + qcg= (1 + up
v)S and S /∈⟨f,g⟩. The code satisfies
theUniversal All-Direction No-Strings Conditionif no such( v,p,S )exists for any v∈Z 3 \{0}
and anyp≥1.
Lemma 2.2(Bézout Membership andF 4-Point Nontriviality).Letf,g,S∈F 2[x,y,z].
3

--- Page 4 ---
(a) If pcf+qcg= (m1 +m2)S for distinct monomialsm1,m2 ∈F 2[x,y,z ]with exponent difference
v= exp(m2)−exp(m 1)̸= 0, then(1 +u v)S∈⟨f,g⟩inR.
(b) If there exists a pointP = (px,py,pz) ∈(F×
2 )3 (in particular,P∈ (F×
4 )3) such thatf(P) = 0,
g(P) = 0, andS(P)̸= 0, thenS /∈⟨f,g⟩inR.
Proof. Part (a) follows by multiplying bym−1
1 ∈R ×. For (b), anyh = af + bg∈⟨f,g⟩⊂R
evaluates to h(P) = a(P)f(P) + b(P)g(P) = 0at P∈ (F×
2 )3 (mechanized as bezout_ideal_
membership), contradictingS(P) ̸= 0(mechanized in Lean aspoint_eval_certifies_nontrivial_
syndrome).
2.2 Why Coordinate-Axis Checks Are Necessary but Not Sufficient
Before stating the universal theorem, we note the exact algebraic certificate for coordinate-axis
strings. Eliminating each variable in turn via exact Bézout cofactorsuzf + vzg= Rz(x,y) ̸= 0,
uyf + vyg = Ry(x,z) ̸= 0, anduxf + vxg = Rx(y,z) ̸= 0unconditionally certifies gcd(f,g) = 1
in F2[x,y,z ](any non-constant common factorh|f,g depends on at least one variablexk and
must divideRxk , contradictingRxk ̸= 0). Expanding Rz(x,y) = ∑M
m=0 cm(x) ym, if there exist
a0(x),...,a M(x)∈F 2[x]such that
M∑
m=0
am(x)cm(x) =xe for somee≥0,(4)
then no nonzerox0 ∈F×
2 can annihilate allcm(x)simultaneously (Lean theorem axis_content_
bezout_refutes_constant_x). Hence V(f,g)contains no curve component on whichx is constant,
ruling out allx-axis strings(1 + xp)S∈⟨f,g⟩ for everyp≥ 1simultaneously. Applying (4) to
all six bivariate resultants rules out all coordinate-axis strings—yet leaves oblique directionsv
completely unguarded.
2.3 The Tropical Spanning Criterion
Let V(f,g) = {P∈ (F×
2 )3 : f(P) = g(P) = 0}be the characteristic variety in the 3D algebraic
torus overF2. When gcd(f,g) = 1and ⟨f,g⟩̸ = R (so V(f,g) ̸= ∅by Hilbert’s Nullstellensatz),
Krull’s Principal Ideal Theorem implies that every irreducible componentCi (i= 1,...,r , r≥ 1)
of V(f,g)is an algebraic curve (dimCi = 1). Let ˜Ci be the smooth projective normalization of
Ci, and for each discrete valuation (place)ν of the function fieldF2(Ci)centered at a puncture of
Ci ⊂(F×
2 )3 (where at least one coordinate has a zero or pole), define the integertropical valuation
ray
wν =
(
ν(x), ν(y), ν(z)
)
∈Z 3 \{0}.(5)
By the Bieri–Groves theorem [1, 10], the tropicalizationTrop(Ci) ⊂R 3 is the union of the rays
R≥0 wν over all puncturesνof ˜Ci. We now establish our central characterization theorem.
Theorem 2.3(Tropical Spanning Criterion for 3D Stabilizer Codes overF2).Let f,g∈R =
F2[x±1,y±1,z±1]be coprime (gcd(f,g) = 1) with⟨f,g⟩̸ = R, so thatV(f,g) ⊂(F×
2 )3 is a nonempty
union of r≥ 1geometrically irreducible curves C1,...,C r. Then( f,g)satisfies the Universal
All-Direction No-Strings Condition (Definition 2.1)if and only iffor everyi∈{1,...,r},
rankQ
(
spanQ{wν :ν∈punctures( ˜Ci)}
)
= 3,(6)
equivalently, each component Ci possesses three valuation rays w1,w2,w3 ∈Z 3 satisfying
det[w1,w2,w3]̸= 0.
4

--- Page 5 ---
Proof. In the Noetherian UFDR, gcd(f,g) = 1and ⟨f,g⟩̸ = R imply that⟨f,g⟩ is unmixed of
height2(every associated prime p∈Ass R(R/⟨f,g⟩)is a minimal prime over⟨f,g⟩ of height2; see
[8]). An element1+ up
v is a zero-divisor inR/⟨f,g⟩ if and only if1+up
v ∈p for some minimal prime
p over ⟨f,g⟩, which holds overF2 if and only if1 +up
v vanishes identically on some geometrically
irreducible curve componentCi ⊂V (f,g)—that is, the monomial functionuv = xvx yvy zvz is a
constantc∈ F×
2 withc p = 1onC i.
(⇐) Sufficiency.Suppose every Ci admits three raysw1,w2,w3 ∈Z 3 with det[w1,w2,w3] ̸= 0,
and suppose for contradiction thatuv = c∈ F×
2 is constant onCi for somev∈Z 3 \{0}. Since
every discrete valuationνvanishes on nonzero constants (ν(c) = 0), we obtain
v·w j =vxνj(x) +vyνj(y) +vzνj(z) =νj(uv) =νj(c) = 0 (j= 1,2,3).(7)
By the exact3 ×3integer Cramer identity (mechanized in Lean astropical_spanning_refutes_
all_directions), det[w1,w2,w3] ̸= 0forces v= (0,0,0), a contradiction. Hence no(1 +up
v)can
vanish on anyCi, certifying the Universal All-Direction No-Strings Condition for everyv∈Z 3 \{0}
and everyp≥1.
(⇒) Necessity (Finite-Field Key).Suppose some componentCi satisfies rankQ(Trop(Ci)) ≤2.
Because all valuation rayswν lie inZ3, the orthogonal complementTrop(Ci)⊥⊂Q 3 has dimension
≥1and therefore contains a nonzero primitive integer vectorv= (vx,vy,vz) ∈Z 3 \{0}satisfying
v·w ν = 0foreverypuncture ν of ˜Ci (in particular, for any two spanning raysw1,w2, the cross
product v= w1 ×w2 satisfies v·w 1 = v·w 2 = 0, mechanized astropical_kernel_witness_orth).
Consequently, the rational functionuv = xvx yvy zvz ∈F2(Ci)× has zero order of vanishing and
zero pole order at every puncture of˜Ci, and has neither zeros nor poles onCi ⊂(F×
2 )3 since x,y,z
are invertible on the torus. Thusuv is a regular function on the projective curve˜Ci, hence a
nonzero constantc∈ F×
2 . Crucially, becauseF2 is the algebraic closure of thefinite fieldF2, every
c∈ F×
2 lies in some finite subfieldF×
2m and therefore satisfiesc2m−1 = 1. Setting p= 2m −1 ≥1,
the binomial1 + up
v vanishes identically onCi, hence1 + up
v belongs to the corresponding minimal
prime pi over ⟨f,g⟩, making1 + up
v a zero-divisor inR/⟨f,g⟩ and yielding a rigid string operator
of directionvand period dividing2 m −1.
Remark2.4 (Contrast with Characteristic Zero).Over C, a constant monomialuv = c∈C ×need
not be a root of unity, sorank(Trop(Ci)) ≤2would not automatically force a periodic binomial
1 −up
v to vanish. OverF2 (and any finite fieldFq),everynonzero constant is automatically a root
of unity, turning the Tropical Spanning Criterion into an exactif and only iftheorem.
3 Zero-Floating-Point-Trust Certificates and Birational Irre-
ducibility
To make Theorem 2.3 auditable by an independent verifier withzerofloating-point operations and
zeroreliance on computer-algebra black boxes, we design theFRACTON-CERT-1.0 JSON schema
with two dual certificate types:
1.fracton_no_strings : certifies a Type-II fracton code (all directionsv̸= 0, all periodsp≥ 1).
2.stealth_string_obstruction : certifies a rigid/stealth string operator along an explicitv̸= 0
for a coprime code.
3.1 Closing the Reducible-Factor Forgery Attack
For any code withf = f0(x,y) + z (monic linear inz, satisfied by Haah Cubic Code A and our
entire 3D TB atlas), substitutingz= f0(x,y)maps V(f,g) ⊂(F×
2 )3 isomorphically onto the plane
curve V(Rz) \{f0 = 0}⊂ (F×
2 )2, whereuzf+ vzg= Rz(x,y) ̸= 0. Suppose a prover suppliesF4(t)
5

--- Page 6 ---
rational parameterizationsϕi(t) = (Px(t)/Q(t), Py(t)/Q(t), Pz(t)/Q(t))and claimed plane-curve
factorsH i(x,y)∈F 4[x,y]satisfying ∏
iHi(x,y) =R z(x,y)inF 4[x,y].
A subtle adversarial attack exists if one checks onlyHi(Px/Q,Py/Q) = 0and ∏
iHi = Rz:
a dishonest prover could setH1 = Rz = A(x,y)B(x,y)for a reducible curve where A has a
rank-3 tropical fan andB harbors a stealth string, parameterize onlyA, and pass both checks.
We eliminate this forgery vector completely using the following exact algebraic criterion (which
remains valid even for inseparable projections in characteristic2).
Proposition 3.1(Birational Irreducibility and Defining-Equation Certificate).Let ϕ(t) =
(Px(t)/Q(t), Py(t)/Q(t)) ∈F 4(t)2 be a rational map, let H(x,y) ∈F 4[x,y] \{0} satisfy
H(Px/Q,Py/Q) = 0identically in F4(t), and letAx/Bx = Px/Qand Ay/By = Py/Qbe the reduced
fractions inF4(t)( gcdF4[t](Ax,Bx) = gcdF4[t](Ay,By) = 1) with d∗
y = max(degAx,degB x) ≥1
and d∗
x = max(degAy,degB y) ≥1. Suppose there exist polynomialsN(x,y),D(x,y) ∈F 4[x,y]
such that
N
(
x(t), y(t)
)
=t·D
(
x(t), y(t)
)
andD
(
x(t), y(t)
)
̸= 0(8)
identically in F4(t), where( x(t),y(t)) = ( Px(t)/Q(t), Py(t)/Q(t)). If degx(H) = d∗
x and
degy(H) = d∗
y, thenH(x,y)isgeometrically irreducibleover F2 and equals the exact defining
polynomialIC(x,y)ofC= ϕ(P1)up to a nonzero scalar inF×
2 .
Proof. Equation (8) implies t = N(x(t),y(t))/D(x(t),y(t))lies in F2(x(t),y(t)), whence
F2(x(t),y(t)) = F2(t). Because F2 is algebraically closed in the pure transcendental extension
F2(t), the image curveC = ϕ(P1) is geometrically irreducible overF2 with minimal defining poly-
nomial IC(x,y) ∈F2[x,y], andIC |H in F2[x,y]. Sincex(t) = Ax(t)/Bx(t)is non-constant (hence
transcendental overF2) withgcd(Ax,Bx) = 1, the bivariate polynomialAx(T)−xBx(T) ∈F2[T][x]
is linear and primitive inx over F2[T], hence irreducible inF2[x,T]and therefore irreducible
in F2(x)[T]by Gauss’s lemma, with exact T-degree d∗
y = max(degAx,degB x)(leading terms
cannot cancel sincex is transcendental). Thus[ F2(t) : F2(x)] = d∗
y. As F2(t) = F2(x,y)and
IC is irreducible overF2(x), we obtaindegy(IC) = [ F2(x,y) : F2(x)] = d∗
y, and symmetrically
degx(IC) = d∗
x. Writing H = u·I C in F2[x,y]yields degx(u) = degx(H) −d ∗
x = 0and
degy(u) = degy(H)−d ∗
y = 0, sou∈ F×
2 .
Our verifier verify_code_certificate_exact (src/fracton_certifier.py) begins with a re-
cursive type sanitizer rejecting anyfloat or bool anywhere in the JSON tree and enforcing
schema_version == "FRACTON-CERT-1.0". It then checks strictly with exact Python integers and
F4 lookup tables: (i) all threeF2[x,y,z ]resultant Bézout identities (Rz,Ry,Rx) for both certificate
types (provinggcd(f,g) = 1), (ii) all sixF2[t]axis-content Bézout identities(4) including exact
gcd_bitmask replay, (iii) for each componentCi, vanishing off,g,H i on( Px/Q,Py/Q,Pz/Q), the
birational inverse identity(8), exactF4[t]GCD degree matching (degx(Hi) = d∗
x, degy(Hi) = d∗
y),
duplicate-free place-valuation verificationν(x),ν(y),ν(z)at every finite a∈F 4 and t= ∞, and
exact integerdet[w1,w2,w3] ̸= 0, (iv) exact component completeness∏
iHi(x,y) = Rz(x,y)in
F4[x,y], and (v) optional exactF2 bitmask replay of finite-torus logical qubit countsk(L).
4 Hierarchical Energy-Barrier Scaling and Lean 4 Mechanization
4.1 Scale-Ladder Energy-Barrier Theorem
Following Bravyi–Haah [3], once the Universal All-Direction No-Strings Condition holds for(f,g),
every neutral excitation cluster of diameterr must be created by an operator of diameter at most
βr (for a code-dependent geometric constantβ≥ 1), while every charged excitation cluster carries
syndrome weight at leastwch ≥1. Note thatwch = 1is the true universal lower bound: even
in Haah Cubic Code A, where globalZ2 parity (f(1,1,1) = g(1,1,1) = 0) constrains thetotal
syndrome weight to be even, applyingp= f2k−1 produces f2k
= 1 + x2k
+ y2k
+ z2k
, isolating
6

--- Page 7 ---
Table 1: Complete audit of all 16 theorems inlean/FractonBarrier.lean verified on Lean 4
v4.35.0viaAuditAxioms.lean(0 warnings, 0sorry, 0Classical.choice).
# Lean 4 Theorem Identifier Mathematical Role (Exact Mechanized Statement) Kernel Axioms
1char2_add_selfCharacteristic-2 cancellationa+a= 0∅
2css_exact_commutationCSS stabilizer commutationg(fq) +f(gq) = 0∅
3syndrome_linearityF 2-linearity of syndrome mapσ(a,b) =ga+fb∅
4stabilizer_in_kernelLocal stabilizers(fq,gq)lie inker(σ)∅
5koszul_local_exactnessBézout-scaled Koszul elimination corera=f(ua+vb), rb=g(ua+vb)∅
6bezout_ideal_membershipHomomorphism soundness:ev(f) = ev(g) = 0⇒ev(uf+vg) = 0∅
7point_eval_certifies_nontrivial_syndromeev(f) = ev(g) = 0∧ev(S)̸= 0⇒∀a,b, σ(a,b)̸=S∅
8axis_content_bezout_refutes_constant_xAxis-content Bézout∑amcm=u,ev(u)̸= 0refutes all-zerocm [propext]
9tropical_det_cramer_xExact3×3integer Cramer identity forvx [propext, Quot.sound]
10tropical_det_cramer_yExact3×3integer Cramer identity forvy [propext, Quot.sound]
11tropical_det_cramer_zExact3×3integer Cramer identity forvz [propext, Quot.sound]
12tropical_spanning_refutes_all_directionsdet(W)̸= 0∧Wv= 0⇒v= 0(Thm 2.3)[propext, Quot.sound]
13tropical_kernel_witness_orthCross-product kernelv=w1×w2⊥w1,w2 [propext, Quot.sound]
14hierarchical_barrier_inductionExactm-step scale-ladder inductionB(m)≥b0+mwch [propext, Quot.sound]
15scale_ladder_barrier_lower_boundConditional distance lower bound (Thm 4.1)[propext, Quot.sound]
16torus_css_logical_qubitsExact torus dimension2N−(rX+rZ) = 2(N−rX)forrZ=rX [propext, Quot.sound]
four single-site (weight-1) charged fracton clusters at mutual distance2k; moreover, codes such
as TB-Fracton-5, TB-Fracton-7, and TB-Fracton-11 have odd wt(g) ∈{5,5,7}. Iterating the
scale-separated cluster-merging decomposition with step incrementc1 ≥1(universally c1 = 1)
yields an exact, machine-checkable inductive lower bound.
Theorem 4.1(Conditional Scale-Ladder Logarithmic Energy-Barrier Bound).LetR0 ≥1, β≥ 1,
and c1 ≥1be positive integers, and letB : N→N denote the minimum energy barrier required to
separate a nontrivial logical operator of support diameter at leastr. Suppose that for every scale
r≥R 0, the hierarchical cluster-merging step satisfies
B
(
(2β+ 3)r
)
≥B(r) +c 1.(9)
Then for every integer levelm≥0and every distanced≥R 0(2β+ 3) m (with monotoneB),
B(d)≥B(R 0) +c1m≥c 1
⌊
log2β+3
( d
R0
)⌋
.(10)
Conversely, any code admitting a certified rigid string identitypcf + qcg = (m1 + m2)S with
S /∈⟨f,g⟩admits a single-qubit Pauli trajectory implementing a macroscopic logical operator of
arbitrarily large distancedwith constant energy barrierEstring =O(1)independent ofd.
4.2 Zero-Dependency Lean 4 Formalization (v4.35.0)
We mechanized the entire algebraic, tropical, and scale-ladder core inlean/FractonBarrier.lean
(438 lines, zero external dependencies) on Lean 4 [6] (leanprover/lean4:v4.35.0) and audited
every theorem vialean/AuditAxioms.lean. All 16 theorems compile cleanly with0 warnings,
0 sorry, and0 Classical.choice. Table 1 summarizes the complete theorem inventory and exact
kernel axiom footprint.
5 Computational Experiments and Certified Atlas
All four experiments are 100% deterministic, execute in under1 .0 svia scripts/run_all_
experiments.py, and produce JSON datasets and exact.cert.json witnesses audited byscripts/
verify_all.py.
5.1 Experiment 1: 8-Code Zero-Float Certified Atlas
We construct and independently verify eight coprime 3D translation-invariant CSS codes: four
genuine Rank-3 Type-II fracton codes—all sharingf = 1 + x+ y+ z—and four string-harboring
7

--- Page 8 ---
Table 2: Exp 1: 8-code zero-floating-point-trust certified atlas
(results/exp1_certified_atlas.json). Every Type-II fracton certificate verifies 3 resul-
tant Bézout identities, 6 axis-content Bézout identities, birational irreducibility (Proposition 3.1),
exact completeness ∏
iHi = Rz, and det(W) ̸= 0. Every string certificate verifies 3 resultant
coprimality witnesses,pcf+ qcg= (m1 + m2)S, and anF4-torus pointP∈V (f,g)with S(P) ̸= 0.
Codeg(x,y,z)(withf= 1 +x+y+zunless noted) Axis Unit-Box Rank|det|/ DirvBirational Inv /P∈(F×4)3 Status
Haah Code A1 +xy+yz+zxPASS PASS 31,1(2 lines)t=y(both) Fracton
TB-Fracton-51 +x2+xy+yz+zxPASS PASS 31t= (1 +x+y)/(x+y)Fracton
TB-Fracton-71 +x3+xy+yz+zxPASS PASS 33t=y/(x+ 1)Fracton
TB-Fracton-111 +x2+y+xy+xy2+xz+yzPASS PASS 32t=yFracton
TB-AxisString† 1 +y+xz(f= 1 +x+yz; 2 comps.) Fail Fail 2(0,0,1)P= (ω,ω 2,1)String
TB-DiagString† 1 +y+z(f= 1 +x+y)FOOLEDFail 2(−1,0,1)P= (ω,ω 2,ω)String
TB-Stealth-F11 +x2+xy+yzFOOLED FOOLED2(0,−1,2)P= (1,1,1)String
TB-Stealth-2121 +x2+y2+xy+yzFOOLED FOOLED2(−2,−1,2)P= (ω,ω,1)String
†Non-standardflisted in parentheses; all other atlas codes usef= 1 +x+y+z.
Figure 1: (a) Normalized 3D tropical valuation rays of Haah Cubic Code A (solid blue, rank 3,
|det| = 1,1) andTB-Fracton-7 (dashed green, rank 3,|det| = 3) contrasted with the coplanar
rank-2 tropical planey= 2zof TB-Stealth-F1 and its orthogonal stealth-string vectorv= (0,−1,2)
(red). (b) Certification matrix across the 8-code atlas showing where coordinate-axis and 13-
direction unit-box checks are fooled by stealth traps.
obstruction codes spanning coordinate-axis, face-diagonal, and higher-slope stealth strings. Table 2
lists the exact defining polynomials, tropical determinants, birational inverses, and verification
outcomes, visualized in Figure 1.
The two stealth traps deserve explicit algebraic inspection:
•TB-Stealth-F1 (g = 1 + x2 + xy + yz, weight 4): passes all six coordinate-axis Bézout
checks and all 10 unit-box face/body diagonals, yet satisfies the exactF2[x,y,z ]identity
(1 + x+ z)f + g= y+ z2 with S = 1and P = (1,1,1) ∈V (f,g)( S(P) = 1 ̸= 0), exposing a
rigid string alongv= (0,−1,2).
•TB-Stealth-212 (g= 1 +x2 + y2 + xy+ yz, weight 5): likewise passes all six axis checks and all
10 unit-box diagonals, yetRz = 1 + x2 + y forces z2 = x2y (modf,g )via the exact identity
(1+ x+y2 +z)f+(1+ y)g= x2y+z2 with S = 1and P = (ω,ω, 1) ∈(F×
4 )3 (f(P) = g(P) = 0,
S(P) = 1), exposing a rigid string alongv= (−2,−1,2).
Notably, during atlas construction our zero-float verifier also caught an additional weight-6 stealth
trap, g= 1 +x+ y+ xy+ yz+ zx (Rz = x2 + xy+ y2 + 1), whose smooth-conic parameterization
satisfies xy = z2 (a hidden(1 ,1,−2)string, det(W) = 0), illustrating in practice how exact
tropical certification prevents subtle manual errors.
8

--- Page 9 ---
Figure 2: (a) ExactF2[x,y,z ]classification of 155 weight-4 and weight-5 3D TB codes separating
1 non-coprime and 10 trivial product-state codes (⟨f,g⟩ = R) from 144 nontrivial codes, revealing
23.3%–35.0% axis-only and 22.5%–34.3% unit-box stealth-string false-positive rates. (b) ExactF2
finite-torus logical qubit countsk(L)for L= 2 ... 9, showing Haah Code A’s fractal peaks, the
L= 7( F×
8 ) resonancek(7) = 12of TB-Fracton-5/7/11, and the deceptively fracton-like oscillation
of the stealth trapTB-Stealth-F1.
5.2 Experiment 2: Systematic 155-Code 3D Trivariate Bicycle Stealth-String
Scan
To quantify how prevalent stealth strings are in 3D TB code families, we systematically scanned
all
(10
3
)
= 120weight-4 codes plus35structured weight-5 codes (155distinct codes total) of the
form f = 1 + x+ y+ z, g = 1 + ∑
m∈Sm drawn from the 10-monomial quadratic/cubic pool
{x2,y2,z2,xy,yz,zx,x 3,y3,x2y,xy2}. Every code was tested strictly overF2[x,y,z ]via exact
elimination, exact torus-unit stripping (testing whetherRz = xayb(1 + x+ y)c ∈R ×, which
implies ⟨f,g⟩ = Rand V(f,g) = ∅), and exact pseudo-Euclidean resultants across: (1) coprimality
(Rz ̸= 0), (2) nontriviality (⟨f,g⟩̸ = R), (3) all six coordinate-axis content Bézout checks, (4) all
10 non-axis primitive unit-box directions (∥v∥∞= 1), (5) all 36 primitive∥v∥∞= 2directions,
and (6) all 96 primitive∥v∥∞= 3directions (testing both p= 1and p= 3factors1 + uv and
1 +uv +u2
v on the torus-unit-stripped curve).
As shown in Figure 2(a), of the 155 codes,1is non-coprime (Rz = 0) and10(all weight-5)
aretrivial product-state codes( ⟨f,g⟩ = R, V(f,g) = ∅, e.g., g = 1 + x2 + y2 + z2 + xy giving
f2 + g= xy∈R ×), leaving144 nontrivial coprime codes. Of these 144 nontrivial codes,41
fail coordinate-axis checks, leaving103nontrivial codes passing all six axis checks (102also pass
all 10 unit-box diagonals). Strikingly:
• Through ∥v∥∞≤2:24/103 (23.3%)of axis-passing nontrivial codes—and23/102 (22.5%)
of unit-box-passing nontrivial codes—harbor rigid strings (1unit-box diagonal +23∥v∥∞= 2
stealth traps: 15 weight-4 and 8 weight-5).
• Through ∥v∥∞≤3:12 additional higher-slope stealth trapsemerge (e.g.,g= 1 + x2 +
y2 + x3 giving x3 + z2 ∈⟨f,g⟩ along v= (3,0,−2)), raising the nontrivial false-positive rates
to36/103 (35.0%)(axis-only) and35/102 (34.3%)(unit-box)!
• The remaining67 nontrivial codespass the full 145-direction ∥v∥∞ ≤ 3screen
(passes_norm3_screen), forming a clean necessary-screen candidate pool for full Theo-
rem 2.3 tropical certification.
9

--- Page 10 ---
5.3 Experiment 3: ExactF 2 Finite-Torus Homologyk(L)
Using exact arbitrary-precision bitmask Gaussian elimination overF2 (torus_css_logical_qubits_
exact, matched with Lean’storus_css_logical_qubits), we computedk(L) = 2(L3 −rankF2 (HX))
forL= 2,3,...,9(n= 2L 3 ∈[16,1458]physical qubits) across all 8 atlas codes (Figure 2(b)):
•Haah Cubic Code A:k(2...9) = [6,2,14,2,6,2,30,2], reproducing Haah’s exactk(2 m) =
2m+2 −2sequence [7].
•TB-Fracton-5 , TB-Fracton-7, TB-Fracton-11:all three yield k(2 ... 9) = [0,0,0,0,0,12,0,0],
exhibiting a sharpF×
8 Frobenius resonance atL= 7 = 23 −1( n= 686, k= 12encoded qubits)
wherex 7 =y7 =z7 = 1admitsF 8-rational points on the irreducible curveV(f,g).
•TB-Stealth-F1 :yields k(2 ... 9) = [4 ,2,8,2,4,14,16,2], oscillating steeply withL (peaking
at k(8) = 16and k(7) = 14) despite harboring av = (0,−1,2)rigid string—proving that
non-monotonick(L)alone cannot distinguish Type-II fractons from stealth-string traps.
• Periodic string codes: TB-AxisString yields[0 ,8,0,0,16,24,0,8], while TB-DiagString
and TB-Stealth-212 both yield[0 ,4,0,0,8,12,0,4], displaying periodic3 |L and7 |L
enhancements.
5.4 Experiment 4: Parametric Theorem 4.1 Scaling vs. ExactO(1)String
Barriers
Finally, we benchmarked Theorem 4.1’s scale-ladder scaling (strictly with the unconditionally
sound universal stepc1 = 1) against exact finite-torus syndrome floors and exact optimalO(1)
string-growth trajectories (Figure 3).
1. Exact L= 5Low-Weight Syndrome Audit.Exhaustively checking every translation-
inequivalent weight-1 and weight-2Z-error on the5 ×5 ×5torus (n= 250qubits) confirms
zero trivial weight-2 pairs and exact minimum nonzero syndrome weights(w1,w2) = (4,4)for
Haah Code A,(4,3)for TB-Fracton-5,(4 ,5)for TB-Fracton-7, and(4 ,5)for TB-Fracton-11,
verifyingwch ≥1on all low-weight errors.
2. Exact Permutation-MinimizedO(1)String Barriers.For each of the four certified string
codes, optimizing overallpermutations of the single-qubit Pauli operators in the step witness
(pc,qc)yields exact distance-independent two-endpoint barriersEstring ≤3( TB-DiagString),
≤5(TB-AxisString),≤6(TB-Stealth-F1), and≤6(TB-Stealth-212).
3. Parametric Theorem 4.1 Crossover (c1 = 1).Evaluating Theorem 4.1’s conditional scale-
ladder boundB(d) ≥⌊log 2β+3(d/R0)⌋(with R0 = 1, universalc1 = 1) across representative
geometric cluster-radius constantsβ∈{ 1,2,3}(bases5 ,7,9) overd∈ [4,222]illustrates the
asymptotic separation: atd= 222 = 4,194,304, thec1 = 1bound reaches9( β = 1),7( β = 2),
and6( β = 3), overtaking the exactO(1)string barriers (≤3,5,6,6). We emphasize that
concrete values of(R0,β)for individual codes are input hypotheses to Theorem 4.1 (Section 6).
5.5 Adversarial Forgery Testing and Gate-2 Reproducibility
Our pytest suite (tests/test_suite.py) subjectsverify_code_certificate_exactto26 live ad-
versarial forgery and type-injection attacks: (1) tampered resultant cofactoru, (2) unelimi-
nated variable inRz, (3) tampered axis-content Bézout cofactor, (4) omitted Galois-conjugate
component C2, (5) reducible-factor forgery placingRz = H1H2 inside component 1’sfactor_H_xy
(blocked by Proposition 3.1), (6) forged birational inverseN/D̸= t, (7) forged tropical ray at a
valid place, (8) repeated/collinear tropical rays (det = 0), (9) tampered recorded determinant,
(10) forged finite-torusk(L), (11) duplicate unused place entry, (12) mismatchedgcd_bitmask,
10

--- Page 11 ---
Figure 3: (a) Conditional parametric instantiations of Theorem 4.1 (universalc1 = 1, R0 = 1,
β∈{ 1,2,3}) versus exact permutation-minimizedO(1)two-endpoint barriers of the four certified
string codes. (b) Exact L = 5torus weight-1 and weight-2 syndrome-floor audit (w1,w2 ≥3
against the universalwch ≥1floor) together with the end-to-end verification stack summary.
(13) forgedschema_version, (14–19) recursivebool/float injection across exponents,F4 coeffi-
cients, det (True/1.0), k_logical (6.0/False), andgcd_bitmask (3.14159), (20) tampered string
cofactor pc, (21) trivial displacementm1 = m2, (22) trivial syndromeS = f∈⟨f,g⟩ (S(P) = 0),
(23) off-variety F4 point (f(P) ̸= 0), (24) zero torus coordinate0 /∈F×
4 , (25) mismatched
string_direction, and (26) non-coprime string certificate (f = g= 1 + x). All26/26 attacks
are rejected, and scripts/verify_all.py replays Lean 4 compilation, axiom auditing, all 8
certificates, all 15 pytest checks, and all 30 SHA-256 hashes in under 3 seconds.
6 Limitations and Scope
We delineate three explicit scope boundaries:
1. Genus-0Rational Components in the Current Verifier.Theorem 2.3 holds forall
nontrivial coprime 2-generator codes regardless of the geometric genus ofCi. Our current
zero-float verifierFRACTON-CERT-1.0 certifies genus-0rational curve components via explicit
F4(t)birational parameterizations (and requiresf monic linear in one variable for the direct
projection completeness check∏
iHi = Rz). Extending the verifier to higher-genus curves
(using Puiseux / discrete-valuation-ring uniformizers overF2m and general Sylvester resultants)
and multi-generator (k>2) CSS codes is a natural next step.
2. Directional Screen vs. Full Tropical Certification in Exp 2.Experiment 2’s 155-code
scan exhaustively classifies all 145 primitive directions with∥v∥∞≤3(proving exact lower
bounds of 35.0% axis-only and 34.3% unit-box false-positive rates among the 144 nontrivial
codes). Confirming any individual survivor among the 67passes_norm3_screen candidates as
a certified Type-II fracton requires constructing its full Theorem 2.3 tropical witness, as done
for our four atlas fracton codes in Experiment 1.
3. Scale-Ladder Bridge Constants.Lean’s scale_ladder_barrier_lower_bound mechanizes
the exact conditional inductive recursion(9)–(10) for arbitrary( R0,β,c 1); mechanizing the
full 3D geometric cluster-decomposition lemma of Bravyi–Haah [3] that derives concrete
code-specific(R 0,β)constants from(f,g)inside Lean 4 remains open future work.
11

--- Page 12 ---
7 Conclusion
We have established the Tropical Spanning Criterion (Theorem 2.3) as an exact, finite-field-native
necessary and sufficient characterization of the Universal All-Direction No-Strings Condition for
nontrivial 3D translation-invariant 2-generator stabilizer codes, closed the reducible-factor forgery
loophole via birational irreducibility certificates (Proposition 3.1), mechanized 16 foundational
algebraic and barrier-scaling theorems in zero-dependency Lean 4, and exposed a 23.3%–35.0% axis-
only and 22.5%–34.3% unit-box stealth-string false-positive rate across 144 nontrivial 3D TB codes.
Together, these tools turn Type-II fracton certification into a fast, zero-float, machine-verifiable
engineering primitive for partially self-correcting 3D quantum memories.
References
[1] Robert Bieri and J. R. J. Groves. The geometry of the set of characters induced by valuations.
Journal für die reine und angewandte Mathematik, 347:168–195, 1984.
[2] Sergey Bravyi, Andrew W. Cross, Jay M. Gambetta, Dmitri Maslov, Patrick Rall, and
Theodore J. Yoder. High-threshold and low-overhead fault-tolerant quantum memory.Nature,
627:778–782, 2024.
[3] Sergey Bravyi and Jeongwan Haah. Energy landscape of 3d spin hamiltonians with topological
order.Physical Review Letters, 107(15):150504, 2011.
[4] Sergey Bravyi and Jeongwan Haah. Quantum self-correction in the 3d cubic code model.
Physical Review Letters, 111(20):200501, 2013.
[5] Sergey Bravyi and Barbara Terhal. A no-go theorem for a two-dimensional self-correcting
quantum memory based on stabilizer codes.New Journal of Physics, 11(4):043029, 2009.
[6] Leonardo de Moura and Sebastian Ullrich. The Lean 4 theorem prover and programming
language. InAutomated Deduction – CADE 28, pages 625–635. Springer, 2021.
[7] Jeongwan Haah. Local stabilizer codes in three dimensions without string logical operators.
Physical Review A, 83(4):042330, 2011.
[8] Jeongwan Haah. Commuting Pauli Hamiltonians as maps between free modules.Communi-
cations in Mathematical Physics, 324(2):351–399, 2013.
[9] Keming He, Jiahan Chen, Enji Xiong, Zhongyi Ni, Lei Zhang, and Xin Wang. QECert: Formal
foundations for quantum error-correction theory in Lean.arXiv preprint arXiv:2611.05047,
November 2026.
[10] Diane Maclagan and Bernd Sturmfels.Introduction to Tropical Geometry, volume 161 of
Graduate Studies in Mathematics. American Mathematical Society, 2015.
[11] Rahul M. Nandkishore and Michael Hermele. Fractons.Annual Review of Condensed Matter
Physics, 10:295–313, 2019.
[12] Michael Pretko, Xie Chen, and Yizhi You. Fracton phases of matter.International Journal
of Modern Physics A, 35(06):2030003, 2020.
[13] Chong-Yuan Xu and Yong Xu. Universally certifying partially self-correcting quantum
memories in 3d translation-invariant stabilizer codes.arXiv preprint arXiv:2611.06469,
November 2026.
[14] Beni Yoshida. Feasibility of self-correcting quantum memory and thermal stability of
topological order.Annals of Physics, 326(10):2566–2633, 2011.
12
