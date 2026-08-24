Strictly Scalable Exterior Decoders for Quantum Lists:
Exact Full-Spark Widths and Fixed-Probe Weyl Bayes
Curves
Lluis Eriksson
August 24, 2026
Abstract
A quantum list measurement succeeds when its classical output contains the prepared label.
General zero-error feasibility is already characterized by the learning width, equivalently the
factor width of the Gram matrix. We use a physical-space form of that known criterion to
close an exact realization-sensitive branch and then go beyond feasibility. For every full-spark
ensemble ofN pure-state rays spanningCr that isstrictly scalable—its rays admit nonzero tight
representatives—the minimum list size for zero error is
ℓmin =N−r+ 1.
The converse is forced by full spark: a smaller-list effect must annihilater spanning states and
hence vanish. Attainment is constructive. Hodge duals of all(r−1)-fold frame wedges form a tight
frame, and their rank-one projectors give a POVM whose output is the complementary list. The
factor-width criterion becomes an annihilator cone in the physical Hilbert space; standard conic
Carathéodory then gives a realization with at mostr2 outcomes. Below threshold, a smallest-
eigenvalue functional gives a strict Bayes-error floor for every full-spark ensemble and remains
positive under explicit operator-norm perturbations. Applied to a flat Schmidt-rank-r probe of
the completed-dimensional Weyl-channel ensemble, the theorem yields the exact fixed-probe
frontier ℓmin = d−r + 1. This strictly exceeds both the support-matroid threshold⌈d/r⌉and
the global summed-projector obstruction on infinite families. An arithmetic-support probe with
the same Schmidt rank has a different exact threshold. More strongly, whenr|d , a dimension
converse and that arithmetic construction close the optimization overallpure Schmidt-rank-r
probes: minψℓmin(ψ) = d/r. For the consecutive rank-two probe we also determine the complete
one-shot Bayes curve,
P⋆
succ(d,ℓ) = ℓ+ sin(πℓ/d)/sin(π/d)
d ,1≤ℓ≤d.
The nondivisible probe optimum, adaptive channel testers, and asymptotic capacity remain
outside scope.
1 Introduction
Quantum state exclusion asks a measurement to certify hypotheses that did not produce the
observed system. Its list formulation returns a set of candidate labels and succeeds when the true
label lies in that set. General semidefinite formulations and optimality conditions are known [1];
antidistinguishability has exact algebraic and Gram-matrix criteria in several settings [2, 3, 4],
and finite group orbits admit exact one-state-exclusion solutions [5]. Recent work also studies
asymptotic zero-error list capacity for pure-state classical–quantum channels [6]. Two-out-of-four
state elimination has both an exact finite analysis and an optical realization [7, 8]; the multiple-
exclusion task itself is therefore not new here.
Most directly, Johnston, Lovitz, Russo, and Sikora define the same finite candidate-list task as
k-learnability and prove that its minimum perfect list size, thelearning width, equals the factor
1

width of the state Gram matrix [9]. Their result subsumes the general feasibility question. We do
not claim a new criterion for arbitrary ensembles. Our contribution is an exact evaluation of that
width on the strictly scalable full-spark branch, a weighted exterior-power factorization that gives
the POVM explicitly, and exact fixed- and optimized-probe Weyl consequences including a complete
rank-two Bayes curve. We also record a simple perturbatively stable spectral subthreshold bound.
The present question is deliberately different and finite: given one copy of one ofN prescribed
pure states, what is the smallest output list that can contain the label with certainty? This question
separates two layers. Linear dependence controls how many states a nonzero effect can annihilate,
while positivity decides whether sufficiently many such effects can resolve the identity. A support
matroid captures the first layer but not the second [10]. We identify a broad branch where both
layers close exactly.
Let g1,...,g N ∈C r be unit state vectors. We call their ray ensemble strictly scalable when
positive numberssi exist such thatfi = sigi form a tight frame [11]. This is broader than requiring
the physical state vectors themselves to form a unit-norm tight frame, while remaining invariant
under the choice of nonzero ray representatives. Tightness of the scaled representatives supplies
a positive identity resolution. Full spark—everyr rays are independent—maximizes resistance to
erasure and is a standard frame-theory notion [12, 13]. Neither property alone determines our
threshold. Together they do:
ℓmin =N−r+ 1.
The construction uses exterior algebra. For every(r−1)-subset E of labels, the Hodge dualwE
of ⋀
i∈Efi is orthogonal exactly to thoser−1frame vectors. Exterior powers of the tight frame
operator show that the projectors|wE⟩⟨wE|resolve the identity after one common normalization.
The measurement reports[N]\E.
The cross-product tightness identity itself is classical in real frame geometry [14]; full-spark
harmonic frames are likewise classical [12]. We do not claim either ingredient as new. The
contribution is their exact synthesis into a quantum list decoder, the matching full-spark converse,
a physical-space realization of the known factor-width criterion, and the resulting Weyl frontiers.
Our main results are:
1. The known learning-width/factor-width criterion has an equivalent physical-space form: the
identity lies in a cone generated by projectors onto vectors with sufficiently many frame zeros
(Theorem 2.1). This form also yields the standardr2 conic-Carathéodory realization.
2. Every strictly scalable full-spark ensemble ofN pure-state rays inCr has exact perfect list
thresholdN−r+ 1, attained by an explicit weighted Hodge POVM (Theorem 3.2).
3. For arbitrary nonnegative priors and density operators, the simple spectral quantityγℓ gives
the universal error floorPerr ≥rγℓ. It is strictly positive below the full-spark threshold when
every prior is positive, and is stable under operator-norm perturbations (Theorem 4.1).
4. For the fixed flat consecutive-support Schmidt-rank-r probe of alld2 Weyl channels, perfect
decoding is possible exactly whenℓ≥d−r+ 1(Theorem 6.1).
5. For r = 2, every subthreshold optimum is explicit:P⋆
succ(d,ℓ) = [ ℓ+ sin(πℓ/d)/sin (π/d)]/d
(Theorem 6.3).
6. If r|d , optimizing over every pure Schmidt-rank-r probe gives the exact global value
minψℓmin(ψ) =d/r(Corollary 6.5).
The hypotheses and resource claims are intentionally narrow. Full spark and strict scalability
are separately necessary for the stated universal theorem, as counterexamples show. The global
Weyl optimum is closed only in the divisor branchr|d ; the nondivisible branch, adaptive uses, and
indefinite causal order are not optimized here.
2

2 Learning width, factor width, and annihilator cones
Let[ N] = {1,...,N} and letgi ∈C r be unit vectors spanningCr. Writeρi = |gi⟩⟨gi|. A list POVM
of size at mostℓis a family
{ML ⪰0 :L⊆[N],|L|≤ℓ},
∑
L
ML =I r.
Zero effects and unused lists are allowed. This is the weak exclusion convention; a strong convention
requiring every listed subset to occur with a nonzero effect is a different problem [15]. It is perfect if
Tr(ρiML) = 0wheneveri /∈L.(1)
For any prior with full support, this is equivalent to unit average success. Lists of smaller cardinality
may be padded, so “at mostℓ” and “exactlyℓ” have the same feasibility threshold.
Thelearning widthis the least such feasibleℓ. If G= [⟨gi,gj⟩]N
i,j=1 is the Gram matrix, its factor
width is the leastℓfor which
G=
∑
a
|ua⟩⟨ua|,|suppu a|≤ℓ.(2)
Johnston et al. prove that learning width equals factor width [9]. The next theorem records the
equivalent physical-space form needed for the exterior construction; the equivalence itself is not
claimed new.
Forv̸= 0, define its zero set with respect to the frame
Z(v) ={i∈[N] :⟨g i,v⟩= 0}
and the admissible annihilator set
Vℓ ={v∈C r \{0}:|Z(v)|≥N−ℓ}.
Theorem 2.1(Factor width in physical-space form).A perfect list decoder of size at mostℓ exists
if and only if
Ir ∈cone{|v⟩⟨v|:v∈V ℓ}.(3)
Equivalently, the Gram matrix has factor width at mostℓ. If it exists, one can choose a perfect
decoder with at mostr2 nonzero outcomes.
Proof. Suppose first thatIr = ∑m
a=1 ca|va⟩⟨va|with ca > 0and va ∈Vℓ. Set Ma = ca|va⟩⟨va|and
report La = [ N] \Z (va). Then |La|≤ℓ , the effects sum to the identity, andi /∈La implies
⟨gi,va⟩= 0. Hence Eq. (1) holds.
Conversely, let{ML}be perfect. Positivity gives
⟨gi,MLgi⟩= 0 =⇒M 1/2
L gi = 0.
Thus every eigenvector with positive eigenvalue in a spectral decomposition ofML is orthogonal to
allg i withi /∈L, hence belongs toVℓ. Summing all spectral decompositions proves Eq. (3).
Finally, Hermitianr×r matrices form a real vector space of dimensionr2. Conic Caratheodory
reduces any representation ofIr in Eq.(3) to at mostr2 generators. The first part of the proof
turns those generators into a perfect decoder.
For completeness, letV : CN →C r have columns gi, so G = V∗V. A cone decomposition
Ir = ∑
aca|va⟩⟨va|maps to ua = √caV∗va, giving Eq. (2); the support of ua is the reported
list. Conversely, every factor ua in Eq. (2) lies in ranG = ranV ∗, so write ua = V∗va. Then
V∗(∑
a|va⟩⟨va|−I r)V = 0. Since V is surjective, the middle operator vanishes. This is the
coordinate translation of the known factor-width criterion.
Theorem 2.1 is the realization-sensitive, physical-space form of the learning-width criterion. The
zero sets are flats of the represented support matroid, but the inclusion ofIr in their projector
cone depends on angles and positivity. Forℓ = N− 1it is closely related to known rank-one
descriptions of antidistinguishing POVMs [2]; its role here is to connect sparse Gram factors to
physical annihilators and to compress the exterior decoder below.
3

3 The exact scalable full-spark threshold
A nonzero frameF= (f i)N
i=1 ⊂C r is tight if
N∑
i=1
|fi⟩⟨fi|=αI r, α= 1
r
N∑
i=1
∥fi∥2 >0.(4)
It is full spark if everyr frame vectors are linearly independent. For the associated physical states
we normalize only at the end,
gi = fi
∥fi∥, ρ i =|gi⟩⟨gi|.(5)
Thus the hypothesis concerns the rays: equivalently, the unit vectorsgi form a strictly scalable
full-spark ensemble, with positive scaling weightssi = ∥fi∥. Individual normalization need not
preserve tightness; the representatives in Eq. (4) are the data used by the exterior construction.
ForE={i 1,...,i r−1}⊂[N], let
fE =fi1 ∧···∧f ir−1 ∈
r−1⋀
Cr.
Fix an antiunitary Hodge identification⋆: ⋀r−1 Cr →C r and putwE = ⋆fE. Equivalently,wE is
the cofactor vector characterized up to the fixed Hodge convention by
⟨fi,wE⟩= 0 (i∈E),∥w E∥2 = det[⟨fi,fj⟩]i,j∈E.(6)
Lemma 3.1(Exterior tightness).IfFobeys Eq.(4), then
∑
E∈([N]
r−1)
|wE⟩⟨wE|=α r−1Ir.(7)
Proof. Let T : CN →C r be the synthesis operatorTei = fi. Then TT∗= αIr. Apply the(r−1)st
exterior-power functor:
(
r−1⋀
T)(
r−1⋀
T)∗=
r−1⋀
(TT∗) =αr−1I∧r−1Cr .
The columns of⋀r−1 T are thefE. Conjugation by the antiunitary Hodge map preserves rank-one
sums and sendsfE tow E, which gives Eq. (7).
The identity is a complex version of the classical cross-product tight-frame construction [14].
We use it as a POVM normalization, not as a new frame-theory claim.
Theorem 3.2(Strictly scalable full-spark list threshold).Let F = ( fi)N
i=1 be a nonzero tight
full-spark frame spanningCr, withN >r, and letρi be the normalized ray states in Eq.(5). The
minimum perfect list size is
ℓmin =N−r+ 1.(8)
Equivalently, the Gram matrix of the normalized rays has factor widthN−r + 1. At the threshold,
an explicit perfect POVM is
ME =α−(r−1)|wE⟩⟨wE|, L E = [N]\E,|E|=r−1.(9)
Moreover, a perfect threshold decoder exists using at mostr2 of these complementary lists.
Proof. For the converse, supposeℓ≤N−r . Every allowed listLomits at leastr labels. Perfectness
implies MLgi = 0, equivalentlyMLfi = 0, for all omittedi. Anyr omitted frame vectors spanCr
by full spark, soML = 0. This would hold for every outcome, contradicting∑
LML = Ir. Therefore
ℓ≥N−r+ 1.
4

For attainment, Lemma 3.1 shows that the effects in Eq.(9) sum toIr. Equation (6) and gi ∥fi
show thatME annihilates every physical state with label inE, exactly the labels omitted from the
reported list. Hence the decoder is perfect with list sizeN−r+ 1.
Full spark makes each(r−1)-fold wedge nonzero and prohibits a vector from havingr frame
zeros. Consequently every generator of the threshold cone in Theorem 2.1 is proportional to some
wE. Conic Caratheodory therefore selects at mostr2 of the displayed effects, with possibly different
positive weights, while retaining the identity resolution.
Proposition 3.3(Constructive r2 compression).The symmetric Hodge POVM in Eq. (9) can
be compressed to at mostr2 nonzero outcomes by finitely many real-nullspace computations and
nonnegative weight updates. The retained outcomes report the same lists and remain a perfect
decoder.
Proof. Write the current identity resolution asIr = ∑m
j=1 cjPj, wherecj >0and every Pj is one of
the Hodge projectors. Regard Hermitian matrices as vectors in the real spaceHerm(r)of dimension
r2. If m>r 2, compute a nonzero real vectorβ satisfying ∑
j βjPj = 0. Its coefficients have both
signs: a nonzero positive combination of nonzero positive semidefinite matrices cannot vanish. After
changing the sign ofβif necessary, set
t= min
βj>0
cj
βj
, c ′
j =cj −tβj.
Then everyc′
j ≥0, at least one becomes zero, and∑
j c′
jPj = Ir. Delete zero coefficients and repeat.
The procedure terminates with at mostr2 effects. Only weights change, so every retained effect
keeps its original annihilated set and reported list.
Remark 3.4(What each hypothesis does).Full spark is used only in the converse and to identify
the maximal zero sets. Tightness is used only to place the identity in the annihilator cone through
Eq.(7). Section 7 shows that neither hypothesis can be deleted from the universal statement.
Remark 3.5(Weighted physical form).If unit state representativesgi obey ∑
iλi|gi⟩⟨gi|= Ir with
every λi >0, takefi = √λigi and α= 1. Then the threshold effects are the Hodge projectors of
the weighted wedges⋀
i∈E
√λigi. Hence the theorem is genuinely projective: unequal representative
norms are not physical probabilities, but a strictly positive scalability certificate used to synthesize
the POVM. The unit-norm tight theorem is the special caseλi =r/N.
The number
(N
r−1
)
of effects in Eq.(9) is a symmetric description, not a hardware lower bound.
Proposition 3.3 turns the standard conic-Caratheodory bound into an explicit finite compression
algorithm. It requires nullspaces of real matrices withr2 rows; it is not asserted to minimize the
number of outcomes or to be numerically well conditioned without certified linear algebra.
4 A spectral subthreshold certificate
The zero-error threshold is discontinuous as a yes/no statement, but its failure admits a quantitative
and perturbatively stable certificate. Letpi ≥0, ∑
ipi = 1, and letρi be arbitrary density operators
onC r. For every allowed listLdefine the omitted-prior operator
QL =
∑
i/∈L
piρi, γ ℓ = min
|L|≤ℓ
λmin(QL).
Theorem 4.1(Spectral list-error bound).For every list POVM of size at mostℓ,
Perr ≥rγℓ.(10)
If the states are pure, have full-support priors, and their rays are full spark, thenγℓ >0whenever
ℓ≤N−r. Moreover, if∥ ˜ρi −ρi∥op ≤εi, then
˜Perr ≥rmax


0,min
|L|≤ℓ

λmin(QL)−
∑
i/∈L
piεi




≥rmax
{
0,γℓ −
∑
i
piεi
}
.(11)
5

Table 1: Support threshold versus the exact perfect-list threshold for a representative unit-norm
tight subfamily.
N rsupport/global threshold⌈N/r⌉exactN−r+ 1
4 2 2 3
6 2 3 5
6 3 2 4
8 4 2 5
10 5 2 6
Proof.For a POVM{ML}, the probability of omitting the true label is
Perr =
∑
L
Tr(MLQL).
SinceQ L ⪰γℓIr for every allowed list,
Perr ≥γℓ
∑
L
TrML =rγℓ.
If ℓ≤N−r , everyL omits at leastr labels. For a full-spark pure ensemble those omitted rays
span Cr; because their priors are positive,QL is positive definite. There are finitely many lists, so
their smallest eigenvalues have a strictly positive minimum.
Finally, ∥˜QL −QL∥op ≤∑
i/∈Lpiεi. Weyl’s eigenvalue perturbation inequality gives the first
lower bound in Eq. (11); replacing every omitted-list sum by∑
ipiεi gives the second.
This is the scalar smallest-eigenvalue witness obtained from the standard quantum decision SDP
[16, 17]; no novelty is claimed for that dual mechanism. Its usefulness here is that it depends on
the actual angles and priors, not only on the support matroid. It therefore supplies quantitative
information that the zero-error width discards. It is a certified lower bound, not generally the exact
Bayes error; Section 6.1 gives a nontrivial family whose complete optimum can nevertheless be
solved.
5 What support-only obstructions miss
For a full-sparkN-frame inCr, the rank of a subfamily ismin{|A|,r}. The ℓ-fold support-matroid
obstruction therefore vanishes once
ℓ≥
⌈N
r
⌉
.(12)
This is a necessary support threshold, not a measurement construction [10]. Theorem 3.2 gives the
exact physical thresholdN−r+ 1, which may be much larger.
For the unit-norm tight subfamily the common global projector test also becomes
∑
i
ρi = N
r Ir ⪯ℓI r
at Eq.(12). Thus both coarse tests can be silent while perfect decoding remains impossible. We stress
“global”: stronger subset-wise projector criteria exist in exclusion theory [15], and no equivalence
with them is claimed.
For example, keepingr = 2and increasing N produces an infinite strict family: the support
obstruction disappears at⌈N/2⌉, while the physical threshold isN−1.
6

6 A fixed-probe Weyl-channel frontier
We now turn the frame theorem into an exact communication statement. LetX|x⟩= |x+ 1 modd⟩
andZ|x⟩=ω x|x⟩, whereω=e 2πi/d. One of thed2 equiprobable channels
Uab(·) =X aZb(·)Z−bX−a,(a,b)∈Z 2
d,
is used once. Dense coding is the rank-d endpoint [18]. Partially entangled deterministic dense
coding and its probe dependence are classical [19, 20]. We fix the specific flat consecutive-support
Schmidt-rank-rprobe
|Φr⟩= 1√r
r−1∑
x=0
|x⟩A|x⟩R,1≤r≤d.(13)
No optimization over probes is implicit. The companion record [10] gives a general unitary-error-
basis list cap and reports the point(d,r,ℓ) = (4,2,2)for a consecutive-support probe. The theorem
below strictly generalizes that fixed-probe comparison across alld and r; it does not re-claim the
companion fixture.
Theorem 6.1(Fixed-probe Weyl frontier).For the completed-dimensional Weyl ensemble and the
probe Eq.(13), perfect one-use list decoding is possible if and only if
ℓ≥d−r+ 1.(14)
At equality, a decoder first reads the shift sector and then applies the Hodge POVM of Theorem 3.2
to the phase frame in that sector.
Proof.The output vector is
|ψab⟩= 1√r
r−1∑
x=0
ωbx|x+a⟩A|x⟩R.(15)
Different agive mutually orthogonal subspaces. For fixeda, thedvectors are unitarily equivalent to
|φb⟩= 1√r(1,ωb,...,ω (r−1)b)T ∈C r.
They form a unit-norm tight frame with boundd/r. Every r×r minor of the synthesis matrix is a
Vandermonde determinant on distinctdth roots of unity, so the frame is full spark [12]. Theorem 3.2
supplies a perfect within-sector list of sized−r + 1, and the shift measurement identifiesa without
error. This proves sufficiency.
For necessity, letML be any effect of a perfect global list measurement. Replacing every effect by
its pinching into the orthogonal shift sectors preserves positivity, completeness, and all probabilities
of the states in Eq.(15); hence we may take every effect block diagonal. In each sector,L contains
at mostℓ phase labels. Ifℓ≤d−r , the effect’s block must annihilate at leastr phase states; full
spark forces that block to vanish. Every block vanishes, henceML = 0. Since all effects would
vanish, no POVM exists. Thus Eq. (14) is necessary.
6.1 The complete rank-two Bayes curve
Forr= 2, the phase ensemble in each shift sector is the regular equatoriald-gon
|φb⟩= |0⟩+ω b|1⟩√
2 .
Lemma 6.2(Largest sum of polygon vertices).For0≤k≤d,
max
S⊆Zd,|S|=k
⏐⏐⏐⏐⏐⏐
∑
b∈S
ωb
⏐⏐⏐⏐⏐⏐
= sin(πk/d)
sin(π/d) ,
with the right-hand side interpreted as zero fork= 0,d. A consecutive arc attains the maximum.
Endpoint projection ties may give more than one maximizing arc but do not change the value.
7

Proof. Let S maximize the modulus and, when its sum is nonzero, letube its unit complex direction.
Then ⏐⏐⏐⏐⏐⏐
∑
b∈S
ωb
⏐⏐⏐⏐⏐⏐
=
∑
b∈S
ℜ(uωb).
Replacing S by thek vertices with largest projection onucannot decrease this expression, while the
modulus of their sum is at least that projection. Thek largest projections on any direction form a
consecutive arc of the regular polygon, with only the stated endpoint ambiguity. A geometric-series
evaluation of such an arc gives the displayed sine ratio for1≤k < d. When k > d/2, the same
value also follows by complementing: the sum over the complement is the negative of the original
sum because alldroots sum to zero. The casesk= 0,dare immediate.
Minimum-error discrimination of geometrically uniform states and the associated square-root
measurement are classical [21]. The following result solves the different list-valued objective for
every list size.
Theorem 6.3(Exact rank-two Weyl list curve).For the complete uniformd2 Weyl ensemble and
the consecutive-support probe|Φ2⟩, the optimal one-use success probability with lists of size at most
ℓis
P⋆
succ(d,ℓ) = 1
d
(
ℓ+ sin(πℓ/d)
sin(π/d)
)
,1≤ℓ≤d.(16)
In particularP⋆
succ < 1for ℓ≤d− 2and equals one for ℓ = d−1,d, recovering Theorem 6.1 at
r= 2.
Proof. Pinch any global measurement into the orthogonal shift sectors as in the proof of Theorem 6.1.
For a setL⊆Z d of phase labels,|L|≤ℓ, put
AL =
∑
b∈L
|φb⟩⟨φb|= 1
2
(
|L| ∑
b∈Lω−b
∑
b∈Lωb |L|
)
.
Hence
λmax(AL) = 1
2

|L|+
⏐⏐⏐⏐⏐⏐
∑
b∈L
ωb
⏐⏐⏐⏐⏐⏐

.
Lemma 6.2 shows that the largest possible root sum has magnitude
Rd,ℓ = sin(πℓ/d)
sin(π/d) .(17)
For the upper bound, writeLa = {b: (a,b) ∈L}. If |La|<ℓ , padding it toℓ phase labels can
only increase the positive operatorALa. Hence each pinched effect blockM(a)
L obeys
Tr
(
M(a)
L ALa
)
≤ℓ+R d,ℓ
2 TrM(a)
L .
Summing over lists and thedtwo-dimensional shift sectors gives
Psucc ≤ 1
d2
ℓ+R d,ℓ
2
∑
a,L
TrM(a)
L = 1
d2
ℓ+R d,ℓ
2 (2d),
which is Eq. (16).
If ℓ = d, the single effectI2 labelled by the full list attains one, so supposeℓ < d. Choose
a consecutive base listL0 and a unit eigenvectorv0 of AL0 at its largest eigenvalue. Translate
both by the cyclic phase action:Lt = L0 + t and vt = diag(1,ωt)v0. Every vt is equatorial and∑d−1
t=0 |vt⟩⟨vt|= (d/2)I2, soMt = (2/d)|vt⟩⟨vt|is a POVM. It attains the largest eigenvalue for every
translated list. Applying this covariant list POVM after the projective shift measurement proves
equality in every sector and hence globally.
8

The endpoints have a direct meaning:
r= 1 :ℓ min =d, r=d:ℓ min = 1.
Each additional flat Schmidt coefficient removes exactly one label from the zero-error list. Rear-
ranging Eq. (14) gives the exact fixed-family memory witness
r≥d−ℓ+ 1.
Here r is the Schmidt rank of the specified probe, not a claim about a general quantum-memory
cost.
Remark 6.4(The support pattern matters).The frontier is not determined by Schmidt rank alone.
Ifr|dandq=d/r, the equally entangled arithmetic-support probe
|˜Φr⟩= 1√r
r−1∑
t=0
|qt⟩A|t⟩R
produces mutually orthogonal sectors labelled bya and bmodr ; each output vector is shared by
exactly theq labels with the same residue class. Measuring those sectors therefore gives the exact
threshold ℓmin = q = d/r. Necessity follows because theq corresponding labels produce identical
output states. Thus, for example,(d,r) = (4,2)gives ℓmin = 2for this probe but3for Eq. (13).
Theorem 6.1 is consequently a support-pattern theorem. The next corollary shows that the arithmetic
pattern is globally optimal in the divisor branch.
Corollary 6.5(Optimized Weyl divisor branch).Suppose r|d . Among all pure probes of Schmidt
rank exactlyrfor the complete uniformd 2 Weyl ensemble,
min
ψ: SR(ψ)=r
ℓmin(ψ) = d
r.(18)
The arithmetic-support probe in Remark 6.4 is optimal. The lower bound specializes the support-
dimension mechanism already used for complete unitary error bases in [10]; the new point here is its
matching arithmetic-support construction for every divisor pair.
Proof. Fix any such probe and letKbe the span of itsd2 pure output vectors. Since the channel
output has dimension d and the probe’s reference support has dimensionr, D = dimK≤dr .
Compress any perfect list POVM toK, so that∑
LML = IK. Writingρab for the output states and
using ∑
(a,b)∈Lρab ⪯|L|I Kgives
1 = 1
d2
∑
L
Tr

ML
∑
(a,b)∈L
ρab


≤ ℓ
d2
∑
L
TrML = ℓD
d2 ≤ℓr
d.
Thus every rank-rprobe needsℓ≥d/r . The arithmetic-support probe attains equality by Remark 6.4.
7 Necessity of strict scalability and full spark
7.1 Tight but not full spark
InC 2, take
f1 =f2 =e1, f 3 =f4 =e2.
This is a unit-norm tight frame but not full spark. The basis measurement reports{1,2}or {3,4},
soℓ= 2is perfect, belowN−r+ 1 = 3. Full spark cannot be removed from the converse.
9

7.2 Full spark but not strictly scalable
Take the three qubit vectors
f1 =|0⟩, f 2 = 3|0⟩+|1⟩√
10 , f 3 = 3|0⟩−|1⟩√
10 .
Every pair is independent, so the frame is full spark. All three Bloch vectors have strictly positivez
component. A list-two effect must omit at least one label and is therefore supported on the line
orthogonal to the omitted state. Its Bloch vector has strictly negativez component. No positive
combination of such nonzero effects can sum to the identity, whose Bloch vector is zero. Hence list
two is impossible althoughN−r + 1 = 2. The same hemisphere argument shows that no strictly
positive rescaling of these rays is tight: every weighted Bloch sum still has positivez component.
Strict scalability cannot be removed from attainment. This is the qubit cone criterion of [2] in the
present list language.
7.3 Other boundaries
Zero-prior labels must be removed before definingN. A nonzero effect cannot annihilate a full-rank
state, so replacing frame vectors by arbitrary mixed states is invalid. Near-tight frames do not
inherit exact zero error by continuity: feasibility is a closed conic condition with exact orthogonality
constraints. Theorem 4.1 instead supplies a quantitative floor under bounded state perturbations,
while Theorem 6.3 gives an exact subthreshold curve only for the specified rank-two Weyl family.
8 Relation to prior work and scope
Table 2 states the contribution boundary. General exclusion SDPs, antidistinguishability, group-
covariant one-state exclusion, exterior tightness, full-spark harmonic frames, and the equality
between learning width and Gram-matrix factor width, as well as the notion of factor-width rank, all
predate this work. In particular, factor-width rank records the minimum number of sparse rank-one
terms [22]; ther2 bound below is the standard conic-Carathéodory consequence in the real vector
space of Hermitian operators on ther-dimensional support. In particular, the group-generated
solution of [5] concerns an outcome that excludes its matching single label. Our threshold decoder
instead associates an outcome withr−1simultaneously excluded labels and solves the smallest
retained list over an arbitrary strictly scalable full-spark ray ensemble. The channel-capacity
results of [6] are asymptotic in block length; our result is a one-shot, fixed-codebook feasibility
law. The companion record [10] already proves a general unitary-error-basis list cap and the single
(d,r,ℓ) = (4,2,2)subthreshold fixture. Our formulas strictly generalize that reported point; we do
not claim it again as an independent contribution. The new Weyl content here is the exact all-(d,r)
zero-error threshold for the specified consecutive-support probe, its Hodge decoder, and the exact
optimization over all rank-r pure probes whenr|d , together with the complete rank-two list-valued
Bayes curve.
We make no “first ever” priority claim. The general feasibility criterion is explicitly credited
to [9]. Targeted comparison with the primary sources above did not locate the scalable all-frame
evaluation N−r + 1, the complementary weighted Hodge decoder, the consecutive-support Weyl
frontier d−r + 1, the global divisor-branch optimumd/r, or the exact rank-two list curve. The
novelty claim is restricted to those evaluations and constructions, not to factor width, exclusion,
exterior algebra, covariant discrimination, or dense coding individually.
9 Reproducibility
The accompanying lightweight NumPy replay checks seven finite layers:
1. harmonic frames are tight and full spark for a grid of small(N,r);
10

Table 2: Contribution boundary. “Used” means explicitly credited rather than claimed as new.
Topic Status here New synthesis claimed here
Learning width=Gram factor
width
Used Exact evaluationN−r + 1on the
scalable full-spark branch
Exclusion SDP and optimality Used Exact scalable full-spark list
threshold
Pure-state annihilator/factor
cones and factor-width rank
Used; ther2 compression is a
standard Carathéodory corollary
Weighted Hodge factorization and
exact full-spark width
Cross-products/exterior powers
of tight frames
Used Hodge projectors as a threshold
POVM
Full-spark
Fourier/Vandermonde frames
Used Exact consecutive-support Weyl
frontier
Dense coding and Weyl
channels
Used Fixed-probe frontier, global divisor
optimum, and rank-two Bayes
curve
Geometrically uniform state
discrimination
Used Exact list-valued regular-polygon
curve
2. exterior Hodge effects reproduceαr−1I, including a non-unit-norm tight full-spark fixture;
3. nullspace elimination compresses a finite Hodge POVM to at mostr2 effects while retaining
the identity resolution;
4. consecutive- and arithmetic-support Weyl fixtures agree with the closed formulas, including
the divisor-branch optimum;
5. the rank-two Weyl Bayes formula agrees with explicit covariant POVMs for a grid of dimensions
and list sizes;
6. the spectral subthreshold floor and its perturbation inequality hold on finite harmonic-frame
fixtures;
7. both hypothesis counterexamples behave as stated.
The replay is diagnostic evidence, not a proof of the all-dimensional theorems. Those follow from
the exterior-power, full-spark, and Weyl arguments in Sections 3 and 6. No formal-proof-assistant
certification, peer review, or independent scientific validation is claimed.
10 Conclusion
For quantum list decoding, linear independence alone is an obstruction and positivity is the
construction problem. Strictly scalable full-spark ray ensembles make the two meet exactly: full
spark forcesℓ≥N−r + 1, while the(r− 1)st exterior power of tightness builds the matching
POVM. The known factor-width criterion, in physical-space annihilator form, explains why this
construction is physical; standard conic Carathéodory explains ther2-outcome compression.
The Weyl application turns the abstract threshold into a sharp resource frontier for a fixed family
of partially entangled probes. In the divisor branch, a dimension converse closes the global rank-r
probe optimization atd/r. For rank two, the regular-polygon geometry closes the entire one-shot
list-success curve, while a simple spectral witness quantifies failure below threshold for arbitrary
full-spark ensembles and survives bounded state perturbations. The construction also supplies
an infinite separation between support-only feasibility tests and actual zero-error measurements.
Natural open problems are to close the nondivisible probe optimum, obtain exact subthreshold
curves beyond rank two, and find other represented matroids whose physical-space factor cone
admits a closed positive identity resolution.
11

AI assistance disclosure.OpenAI Codex assisted with theorem exploration, literature triage,
proof stress testing, verifier development, and manuscript editing. The author selected and reviewed
the claims, proofs, citations, and computational evidence and remains responsible for the work. AI
output is not treated as independent scientific evidence.
References
[1] Somshubhro Bandyopadhyay, Rahul Jain, Jonathan Oppenheim, and Christopher Perry. Conclusive exclusion of
quantum states.Physical Review A, 89:022336, 2014.
[2] Teiko Heinosaari and Oskari Kerppo. Antidistinguishability of pure quantum states.Journal of Physics A: Mathematical
and Theoretical, 51:365303, 2018.
[3] Vincent Russo and Jamie Sikora. Inner products of pure states and their antidistinguishability.Physical Review A,
107:L030202, 2023.
[4] Nathaniel Johnston, Vincent Russo, and Jamie Sikora. Tight bounds for antidistinguishability and circulant sets of pure
quantum states.Quantum, 9:1622, 2025.
[5] Arnau Diebra, Santiago Llorens, Emili Bagan, Gael Sentis, and Ramon Munoz-Tapia. Quantum state exclusion for
group-generated ensembles of pure states.Physical Review Research, 8:L012001, 2026.
[6] Marco Dalai, Filippo Girardi, and Ludovico Lami. Zero-error list decoding for classical–quantum channels, 2026. version
2.
[7] Jonathan Crickmore, Ittoop V. Puthoor, Berke Ricketti, Sarah Croke, Mark Hillery, and Erika Andersson. Unambiguous
quantum state elimination for qubit sequences.Physical Review Research, 2:013256, 2020.
[8] Jonathan W. Webb, Ittoop V. Puthoor, Joseph Ho, Jonathan Crickmore, Emma Blakely, Alessandro Fedrizzi, and Erika
Andersson. Experimental demonstration of optimal unambiguous two-out-of-four quantum state elimination.Physical
Review Research, 5:023094, 2023.
[9] Nathaniel Johnston, Benjamin Lovitz, Vincent Russo, and Jamie Sikora. The complexity of perfect quantum state
classification, 2025.
[10] Lluis Eriksson. Bayesian matroid-union bounds for quantum list discrimination: Support congestion, process compression,
and exact adaptive-parallel phases, 2026. ARR-2026-15SJ1ANHDN8D88Z1, Archive for Rigorous Research.
[11] Gitta Kutyniok, Kasso A. Okoudjou, Friedrich Philipp, and Elizabeth K. Tuley. Scalable frames.Linear Algebra and its
Applications, 438(5):2225–2238, 2013.
[12] Boris Alexeev, Jameson Cahill, and Dustin G. Mixon. Full spark frames.Journal of Fourier Analysis and Applications,
18(6):1167–1194, 2012.
[13] Peter G. Casazza and Gitta Kutyniok, editors.Finite Frames: Theory and Applications. Birkhauser, 2013.
[14] Grigory Ivanov. Tight frames and related geometric problems.Canadian Mathematical Bulletin, 64(4):942–963, 2021.
[15] Benjamin Stratton, Chung-Yun Hsieh, and Paul Skrzypczyk. Operational interpretation of the choi rank through
exclusion tasks.Physical Review A, 110:L050601, 2024.
[16] Alexander S. Holevo. Statistical decision theory for quantum systems.Journal of Multivariate Analysis, 3:337–394, 1973.
[17] Horace P. Yuen, Robert S. Kennedy, and Melvin Lax. Optimum testing of multiple hypotheses in quantum detection
theory.IEEE Transactions on Information Theory, 21(2):125–134, 1975.
[18] Charles H. Bennett and Stephen J. Wiesner. Communication via one- and two-particle operators on einstein–podolsky–
rosen states.Physical Review Letters, 69:2881–2884, 1992.
[19] Shay Mozes, Jonathan Oppenheim, and Benni Reznik. Deterministic dense coding with partially entangled states.
Physical Review A, 71:012311, 2005.
[20] Shengjun Wu, Scott M. Cohen, Yuqing Sun, and Robert B. Griffiths. Deterministic and unambiguous dense coding.
Physical Review A, 73:042311, 2006.
[21] Yonina C. Eldar and G. David Forney, Jr. On quantum detection and the square-root measurement.IEEE Transactions
on Information Theory, 47(3):858–872, 2001.
[22] Nathaniel Johnston, Shirin Moein, and Sarah Plosker. The factor width rank of a matrix, 2025.
12
