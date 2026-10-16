# Uniform tropical bounds for amplified determinants: finite phase witnesses and multiscale quantum noise

Text extraction of canonical paper.pdf; consult the PDF for equations.

Uniform tropical bounds for amplified determinants:
finite phase witnesses and multiscale quantum noise
Lluis Eriksson
Independent researcher, Sweden
16 October 2026 — research draft
Abstract
W e study determinants of matrix pencils evaluated on auxiliary matrices under a normal-
ized Hilbert–Schmidt energy constraint. F or a fixed full noncommutative-rank pencil of size
d, we show that its objective, regularized over all auxiliary sizes, is uniformly comparable
on the entire positive coeﬀicient orthant to the monomial envelope of its noncommutative
Newton polytope. The lower bound uses auxiliary size max{1, d−1} and a single tuple whose
entries vary only by scalar phases. A finite phase menu suﬀices. Thus every simultaneous
coeﬀicient reweighting has the same noise exponent at that fixed size as under unrestricted
amplification. F or mixtures of quantum channels this gives an exact piecewise-linear law for
arbitrary simultaneous power-law noise rates, including the normalization of mixture weights.
An explicit six-parameter qutrit pencil has five branches, one absent at scalar size; a single
fixed size-two tuple approximates its regularized objective within a factor four for every pos-
itive parameter choice. The algebraic polytope and its stabilization are established results.
Our contribution is a uniform analytic comparison and its finite-witness and noise-law conse-
quences; we do not claim exact finite-size optimization or a coeﬀicient-uniform approximation
factor for general pencils.
1 Question and prior work
F or fixed matrices A1, . . . , As ∈ Md(C), let
Fm(z) = max∑
i Tr(Y ∗
i Yi)/m=1
det
 X
i
ziAi ⊗ Yi
!
2/(dm)
, (1)
F∞(z) = sup
m≥1
Fm(z), z ∈ (0, ∞)s. (2)
The maximum at each fixed size exists by compactness. When the Ai are Kraus operators,
this is the amplified determinant objective studied in [ 3, 4]. The parameter m is part of that
mathematical amplification; it is not a free ancillary resource in a different channel-testing model.
An asymptotic formula on one noise ray need not control other rays, and pointwise finite-
size witnesses need not give a uniform bound as coeﬀicients approach zero. W e address both
issues by comparing the entire positive-parameter family with a finite polyhedral envelope. The
resulting constants depend on the fixed matrix tuple, but neither on the coeﬀicients nor on the
amplification size.
The main algebraic input is the theory of weighted noncommutative determinants developed
by Hirai and by Hirai–Ikeda [1], and extended by Hirai–Iwamasa–Oki–Soma [ 2]. Its noncommu-
tative Newton polytope, integrality , weighted-degree algorithms, and stabilization in auxiliary
size are prior results. The proof below combines that input with maximum modulus, generic
nonvanishing, and Parseval’s identity . The earlier depolarizing-noise rank law [ 3] treats a par-
ticular perturbation; here the comparison is simultaneous over arbitrary positive reweightings
and gives a bounded-size family of witnesses.
1

2 The algebraic polytope
Let Xi be generic m × m matrices with independent commuting entries. In each monomial of
Dm(X) = det
 X
i
Ai ⊗ Xi
!
,
group the entry degrees by the index i. If this grouped vector is α ∈ Ns, include α/m in
Pm. More precisely , Pm is the convex hull of all such normalized grouped degrees with nonzero
coeﬀicient. Put
P = conv
[
m≥1
Pm.
W e assume the span of theAi has full noncommutative rank. If it does not, all the determinants
in (1) vanish and there is no finite logarithmic noise exponent.
Lemma 1 (Established stabilization). The set P is an integral polytope in{u ∈ Rs
≥0 : P
i ui = d}.
F or every m ≥ d − 1 with m ≥ 1, one has Pm = P.
Proof. The full-determinant polytope and its stabilization are stated explicitly in [1, Section 4.2,
after Theorem 4.3; Theorem 4.4]; see also [2, Theorem 3.12]. F or an integer weight vectorw, the
maximum degree of the generic blow-up of P
i Aitwi xi, divided by m, is the support function of
Pm at w. Proposition 2.6 of [ 2] identifies it with the degree of the Dieudonné determinant for
every m ≥ d − 1. That degree is the support function of P. Equality at every integer direction
implies equality of the compact convex polytopes. The case d = 1 is immediate. Homogeneity
gives the sum of coordinates.
The conventions in [ 2] use maximum degrees at infinity . W e will obtain minimum weighted
degrees for parameters tending to zero by changing the sign of the weight vector; no interchange
of an infinite supremum with a small-noise limit is needed.
3 A uniform analytic comparison
W rite
TP (z) = max
u∈P
Y
i
z2ui/d
i , M = max{1, d − 1},
and let G = (TrA∗
i Aj)i,j be the Gram matrix of the coeﬀicients.
Theorem 2 (Uniform tropical comparison) . There is a constant cA > 0 such that, for every
positive z,
cATP (z) ≤ FM (z) ≤ F∞(z) ≤ CATP (z), C A = λmax(G)
d . (3)
The lower bound is attained within a family (eiϕ1 Y1, . . . , eiϕs Ys) for one fixed energy-normalized
tuple Y of size M. A finite set of phase choices, independent of z, suﬀices for the same lower
constant.
Lemma 3 (T oric maximum modulus). F or a nonzero polynomial p in s variables and positive
z,
|p(z)| ≤ max
|ωi|=1
|p(ω)| max
α∈Newt(p)
zα.
Proof. First take zi = rki , where r > 1 and the ki are integers of either sign. The Laurent
polynomial f(w) = p(wk1 , . . . , wks ) has largest exponent at most H = maxα∈Newt(p) k · α. The
function w−Hf(w) is analytic on the exterior unit disk including infinity . Applying maximum
modulus there gives the assertion. Approximate arbitrary log z by rational vectors, using r =
e1/N, and use continuity . Cancellation among terms of f can only decrease its largest exponent.
2

Proof of Theorem 2. Fix m and an admissible tuple Y , and let pY (z) = det(P
i ziAi ⊗ Yi). Its
Newton polytope is contained in mP because specialization can remove monomials but cannot
add grouped degrees. F or |ωi| = 1, the Gram inequality and arithmetic–geometric mean imply
|pY (ω)|2/(dm) ≤ 1
dm

X
i
ωiAi ⊗ Yi

2
F
(4)
≤ λmax(G)
dm
X
i
∥Yi∥2
F = CA. (5)
Lemma 3 now gives the upper bound uniformly in m and Y . T aking their suprema preserves it.
F or the lower bound, let V be the finite vertex set of P. By Lemma 1, for every v ∈ V
the coeﬀicient of zMv in det(P
i ziAi ⊗ Xi) is a nonzero polynomial in the entries of X. Their
finite product is nonzero. Choose a tuple where all these coeﬀicients are nonzero, and scale it
to energy one. W rite pY (z) =P
α bαzα and bv = bMv ̸= 0. Parseval on the phase torus gives
Z
Ts
|pY (z1ω1, . . . , zsωs)|2 dω =
X
α
|bα|2z2α. (6)
The maximum over phases is at least each term on the right. T aking the power 1/(dM) of the
squared modulus yields ( 3) with
cA = min
v∈V
|bv|2/(dM) > 0.
Each coordinate degree is at most dM. Replacing the integral by the product grid of (dM + 1)st
roots of unity gives the same coeﬀicient orthogonality . Since pY is homogeneous, one common
phase is immaterial and can be fixed. Thus at most (dM +1)s−1 choices suﬀice (one if s = 1).
Corollary 4 (Uniform limitation on further amplification) . F or the fixed pencil,
1 ≤ F∞(z)
FM (z) ≤ CA
cA
for al l z > 0.
This bound also holds when the coeﬀicients fol low an arbitrary path, including paths with no
limiting power-law direction.
This is a fixed-pencil statement. The proof supplies neither a universal small value of CA/cA
nor a polynomial-size phase menu. It does not state that FM = F∞, or that the supremum is
attained at size M.
4 Multiscale noise and channel normalization
Corollary 5 (All directional exponents) . F orw ∈ Rs and 0 < t < 1,
F∞(tw1 , . . . , tws ) ≍A tθ(w), θ (w) = 2
d min
u∈P
w · u.
The constants can be chosen independently of both w and t. The function θ is continuous,
concave, piecewise linear, and rational linear on every cone of its fan. The same exponent holds
for FM .
Proof. Substitute zi = twi into (3). Because log t < 0, the maximum monomial corresponds to
a minimum scalar product. The remaining properties follow from the finite integral vertex set
of P.
3

F or rational matrix entries and rational weights, the existing algorithms for weighted non-
commutative determinants [2] compute the exponent under their stated complexity guarantees.
This does not compute the regularized prefactor or optimize ( 1).
Let Eg be finitely many CPTP maps on Md, with Kraus lists Agj whose union has full
noncommutative rank. Project P to the group coordinates qg = P
j ugj and call the resulting
polytope Q. It lies in P
g qg = d. F or positive probabilities pg, the Kraus list of Ep = P
g pgEg
is √pgAgj . Theorem 2 gives
a∞(Ep) ≍A max
q∈Q
Y
g
pqg/d
g , (7)
where a∞ denotes the regularized objective for a Kraus list at unit coeﬀicients. The comparison
is independent of p and the same comparison holds at size M. F or normalized power-law weights
pg(t) = tβg
P
h tβh
,
we obtain
lim
t↓0
log a∞(Ep(t))
log t = 1
d min
q∈Q
β · q − min
g
βg. (8)
The subtraction on the right is required by trace preservation.
More generally , if R(z) =P
i z2
i A∗
i Ai is positive definite, then Ki(z) =ziAiR(z)−1/2 defines
a CPTP map. F actoring the common right matrix from the block determinant proves, at every
size and after taking the supremum,
a∞(Ez) = F∞(z)
det(R(z))1/d . (9)
The normalizing determinant is a positive sum of monomials by Cauchy–Binet. Its small-noise
order must therefore be subtracted from the unnormalized order. These identities concern matrix
amplification as in [ 4]; they do not change its hypothesis-testing access assumptions.
5 A qutrit phase diagram with an explicit factor four
Let
A12 = E12 − E21, A 23 = E23 − E32, A 31 = E31 − E13, D j = Ejj .
Assign amplitudes (x, y, z, a, b, c ) to these six matrices, in that order. Define
T = max{(abc)2/3, (cx2)2/3, (ay2)2/3, (bz2)2/3, (xyz)2/3}. (10)
Proposition 6. F or every positive choice of the six amplitudes,
1
6T ≤ F2 ≤ F∞ ≤ 2
3T.
The lower bound uses a single fixed tuple of size two, independent of al l six amplitudes. Its value
is at least one quarter of the regularized optimum throughout the positive parameter orthant.
Proof. F or a grouped normalized monomial degree u = (ux, uy, uz, ua, ub, uc), row and column
counts in the block determinant imply
2ua + ux + uz = 2, 2ub + ux + uy = 2, 2uc + uy + uz = 2, u ≥ 0.
This polytope has the five vertices
(0, 0, 0, 1, 1, 1), (2, 0, 0, 0, 0, 1), (0, 2, 0, 1, 0, 0),
(0, 0, 2, 0, 1, 0), (1, 1, 1, 0, 0, 0).
4

T o verify exhaustiveness directly , eliminateua, ub, uc; the remaining constraints are ux, uy, uz ≥ 0
and the three pairwise sums at most 2. Their vertices are the origin, the three axis points of
coordinate 2, and (1, 1, 1). The first four degrees occur in the scalar identity
det
0
@
a x −z
−x b y
z −y c
1
A= abc + cx2 + ay2 + bz2.
Let σx, σy, σz be the standard Pauli matrices and set
Y = 1√
6(σx, σy, σz, I2, I2, I2).
Its energy is one. Put S = abc + ay2 + bz2 + cx2. Direct block-determinant expansion gives the
exact identity
det
 X
i
ziAi ⊗ Yi
!
= (S + 2ixyz)2
216 . (11)
F or an explicit verification before normalization, the real terms of the determinant are S2 −
4x2y2z2, while its imaginary terms are 4ixyzS. The coeﬀicients of the five doubled vertex
degrees are 1, 1, 1, 1, −4. Thus all five vertices occur and the polytope is exact. The value
supplied by this one tuple is
W(x, y, z, a, b, c ) = (S2 + 4x2y2z2)1/3
6 . (12)
F or positive amplitudes,S dominates each of its four summands, andS2+4x2y2z2 also dominates
(xyz)2. Therefore W ≥ T/6, with no phase search. Orthogonality of the coeﬀicient matrices
gives G = diag(2, 2, 2, 1, 1, 1) and hence upper constant 2/3 from Theorem 2. The same fixed
tuple is admissible for every parameter choice.
F or the scalar objective the last branch in ( 10) is absent. T aking x = y = z = 1 and
(a, b, c) = (tr1 , tr2 , tr3 ) with all rj > 0 makes the regularized exponent zero, whereas the scalar
exponent is 2
3 minj rj. The CPTP normalization is
R = diag(a2 + x2 + z2, b 2 + x2 + y2, c 2 + y2 + z2),
which has a strictly positive limit on this ray , so the separation persists for the normalized
channels. General rays are governed by the five linear forms in ( 10) with the exponent of det R
subtracted as in ( 9). This example exhibits a whole parameter region of exponent separation,
rather than just an isolated singular pencil.
6 Checks, scope, and remaining questions
The accompanying exact computation verifies the factorization ( 11), enumerates the polytope
vertices, and checks the five vertex coeﬀicients. Numerical stress tests use 240 random complex
tuples at auxiliary sizes 1, 2, 3, 4, 5, 7 over a wide range of positive weights; no violation of the
proved upper bound was found. Another 120 positive parameter choices check the fixed-witness
formula across widely separated scales. T en additional choices verify the discrete phase Parseval
identity underlying the earlier general construction. These checks supplement the proofs and
are not formal verification or evidence of an unproved global numerical optimum.
The main result controls logarithmic asymptotics uniformly and limits the benefit of larger
amplification for a fixed pencil. It leaves open sharp general prefactors, eﬀicient selection of
good phases, and practical bounds for the constant as the coeﬀicient matrices themselves vary .
5

In particular, it does not establish a universal constant-factor approximation through operator
capacity , nor any random-matrix log-determinant convergence conjecture. The five-branch ex-
ample is an explicit application, not a claim that the underlying fractional matching polytope
is new.
This draft was developed with AI assistance and is intended for mathematical review. Any
associated model assessment must identify the precise reviewed version and disclose shared
context. Neither a model score nor the numerical checks certify novelty or replace expert peer
review.
References
[1] H. Hirai and M. Ikeda, A cost-scaling algorithm for computing the degree of determinants ,
arXiv:2008.11388v2 (2020), Section 4.2.
[2] H. Hirai, Y. Iwamasa, T. Oki and T. Soma, Algebraic combinatorial optimization on the
degree of determinants of noncommutative symbolic matrices , Mathematical Programming,
DOI: 10.1007/s10107-024-02158-0. Preprint arXiv:2310.15502 (2023). Numbered statements
cited here follow the arXiv version.
[3] L. Eriksson, Sharp determinant bounds for amplified antisymmetric channels and a noise
law for noncommutative rank , AIRR working paper ARR-2026-6FWR12DH3F8QBA5C, v1
(2026).
[4] L. Eriksson, Universal optimal tests of unknown unitary dynamics: determinant exponents
and tensor stability , AIRR working paper ARR-2026-2GTKNVK5QM9H8BFR, v1 (2026).
6