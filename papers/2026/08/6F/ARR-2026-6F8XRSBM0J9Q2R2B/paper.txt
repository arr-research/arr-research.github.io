All-Field Morse–Bott Stability at Critical
Homogeneous Orbits
Half-Grassmann No-Spinodal Rigidity and Exact Jacobi Metastability
Lluis Eriksson
August 15, 2026
Abstract
Let a compact group act orthogonally on a sphere and letµ be the invariant law of a
proper antipodal orbit. We study the orbital potentialUt(a) =
∫
exp(t⟨a,u⟩) dµ(u). At
a point of the source orbit, every spherical-harmonic coefficient of the orbit average is a
squared norm. Combining this positivity with the strictly positive Gegenbauer–Bessel
coefficients of the exponential kernel gives an exact negative spherical-Laplacian identity at
every fieldt> 0. Provided the source orbit is critical—automatically so when the normal
isotropy representation has no fixed vector—irreducibility, or a transitive symmetry of its
irreducible normal blocks, upgrades this trace identity to strict Morse–Bott maximality
for every field. We give an explicit torus-orbit counterexample showing why the criticality
hypothesis cannot be omitted.
Applied to the centered projector embeddings of the real, complex, and quaternionic
half-Grassmannians, the theorem proves all-field local rigidity of the balanced matrix–
Bingham branch and excludes any radial spinodal. In the complex case we go further.
For every two-block external spectrum we derive exact constrained-Hessian eigenvalues
from the reversible Jacobi generator. Their low-field factors show a sharp metastability
threshold: unbalanced strata with positive multiplicityk> 2r/3are genuine local maxima
at weak field, whereas those withk≤ 2r/3have an unstable block split. A Stein inequality
proves the required Hessian sign in all sufficiently high Taylor degrees and leaves an explicit
finite low-degree gate. Thus a global competing phase, if it exists, must arise by nonlocal
coexistence rather than loss of stability of the balanced branch. We do not claim global
spectral optimality or the resulting all-distortion rate–distortion function.
1 Introduction
Matrix–Bingham normalizers on Grassmannians are orbital Laplace transforms and hypergeo-
metric functions of matrix argument. Their evaluation, asymptotics, and information geometry
are well developed [10, 13, 11, 1, 2]. A different problem asks which external spectrum
maximizes such a normalizer under trace and Frobenius constraints. The constraints do not
define a majorization chain, so standard Schur or orbital-integral monotonicity does not decide
the question [9, 15, 12].
The rank-two caseGrC(2,4)admits an exact all-field solution [6]; arbitrary rank has
previously been controlled at high field, yielding an exact high-fidelity rate–distortion segment
[5]. The missing finite-field issue is global: can an intermediate external spectrum overtake the
balanced two-block field? This paper does not resolve that global ordering. It instead closes
its local part at every field and proves that a seemingly natural saddle-based shortcut is false.
The first observation is representation-free. Classical Schoenberg and Gangolli theory
characterizes positive-definite zonal kernels by nonnegative harmonic coefficients [14, 8]. If the
center of the orbital potential lies on the same orbit as the integration measure, the orbital
1

harmonic coefficient is itself a squared mean harmonic. The spherical Laplacian is consequently
strictly negative. Under an explicit criticality condition and a normal-isotropy hypothesis this
trace sign becomes a complete normal-Hessian sign, giving an all-field Morse–Bott theorem.
We also exhibit a proper antipodal orbit for which irreducibility alone does not force criticality.
Group-invariant kernel energies on compact homogeneous manifolds have also been used
for quadrature and discrepancy [3]. Those results optimize an energy over measures or point
sets on the homogeneous space. Our variable is instead an ambient external direction on a
fixed Frobenius sphere, and the conclusion is a transverse Hessian theorem at the embedded
source orbit.
For half-Grassmannians this proves that the balanced field never becomes spinodally
unstable over R, C, or H. In the complex case a second, independent Jacobi calculation
classifies weak-field block splitting at every two-level spectrum. It reveals locally stable
unbalanced branches near the balanced multiplicity. Hence local Hessians cannot eliminate
all competitors: a complete global proof must compare separated values or prove a stronger
Laplace order.
Our contributions are:
(i) a positive-mode spherical-Laplacian identity, a necessary criticality guard, and an all-field
Morse–Bott criterion for homogeneous orbital potentials;
(ii) strict balanced local rigidity for the real, complex, and quaternionic half-Grassmann
matrix–Bingham models;
(iii) exact Jacobi–Stein identities and exact constrained-Hessian operators for every complex
two-block multiplicity stratum;
(iv) the sharp weak-field metastability thresholdk = 2r/3, including its degenerate sixth-
moment boundary; and
(v) a coefficient-tail theorem that reduces one global sign problem to finitely many exact
moments at each fixed(r,k).
The addition theorem, matrix-beta law, and Jacobi ensemble are established ingredients.
Novelty is claimed only for the joined all-field stability and metastability conclusions, not for
those classical tools.
2 Orbital harmonic positivity
Let N≥ 3, letG be a compact group acting orthogonally onRN, letO= Gv⊂S N−1 be an
orbit, and letµbe its invariant probability measure. Writeλ= (N−2)/2and let
Kℓ(x,y) = Cλ
ℓ(⟨x,y⟩)
Cλ
ℓ(1) (2.1)
be the normalized degree-ℓ spherical-harmonic reproducing kernel. The circleN = 2has the
analogous Fourier/Chebyshev formulation, but it is not needed in any application below and is
excluded from the stated Gegenbauer normalization. For an orthonormal real harmonic basis
{Yℓj}j, the addition theorem gives
Kℓ(x,y) =c N,ℓ
∑
j
Yℓj(x)Yℓj(y), c N,ℓ >0.(2.2)
2

Lemma 2.1(Squared orbital coefficient).For everyℓ≥0and everyv∈O,
qℓ :=
∫
O
Kℓ(u,v)dµ(u) =c N,ℓ
∑
j
⏐⏐⏐⏐
∫
O
Yℓj(u)dµ(u)
⏐⏐⏐⏐
2
≥0.(2.3)
IfOis antipodal, thenq ℓ = 0for oddℓ.
Proof. Invariance makes the first integral independent of the selectedv∈O . Averaging it once
more overv and using (2.2) gives the squared-norm formula. Antipodality annihilates every
odd harmonic average.
The evaluation point belonging to the source orbit is essential. Away from the orbit
the corresponding coefficient is an inner product of two harmonic vectors and need not be
nonnegative.
Let an analytic zonal kernel have the expansion
Φ(x) =
∑
ℓ≥0
aℓ
Cλ
ℓ(x)
Cλ
ℓ(1) , a ℓ ≥0,(2.4)
with locally uniform convergence after two derivatives, and define
UΦ(a) =
∫
O
Φ(⟨a,u⟩)dµ(u), a∈S N−1 .(2.5)
Proposition 2.2(Negative orbital Laplacian).At everyv∈O,
∆SN−1 UΦ(v) =−
∑
ℓ≥1
ℓ(ℓ+N−2)a ℓqℓ ≤0.(2.6)
The inequality is strict ifaℓqℓ >0for at least oneℓ≥1.
Proof. Integrate (2.4), apply theorem 2.1, and use∆ Kℓ = −ℓ(ℓ+ N− 2)Kℓ in the first
argument.
ForΦ t(x) = etx all Gegenbauer coefficients are strictly positive fort> 0. If Ois a proper
orbit, its invariant measure is not uniform on the ambient sphere. Since spherical harmonics
determine finite measures on the compact sphere, some nonconstantqℓ is positive. Thus
theorem 2.2 is strict for everyt>0.
3 A critical all-field Morse–Bott theorem
The potential isG-invariant, hence constant alongO, but constancy on the orbit does not by
itself make an orbit point critical: a normal gradient can remain. The following elementary
guard isolates the missing condition.
Lemma 3.1(Criticality guard).For everyv∈O, the spherical gradient satisfies
∇SUΦ(v)∈(N vO)Gv .(3.1)
Consequently( NvO)Gv = {0}implies that the whole orbit is critical. At a critical orbit, the
spherical Hessian annihilatesTvO, including all mixed tangent–normal entries.
Proof. Invariance makes the gradient orthogonal to the orbit and fixed by the stabilizer, proving
(3.1). For an infinitesimal orbit fieldX# one hasdUΦ(X#) = 0. Covariantly differentiating
this identity in an arbitrary spherical directionZgives
HessSUΦ(Z,X#) +dUΦ(∇ZX#) = 0.
The second term vanishes at a critical point. Orbit homogeneity transports criticality and the
Hessian-kernel conclusion fromvto every point ofO.
3

Theorem 3.2(Critical homogeneous orbital Morse–Bott stability).Assume thatO⊂S N−1
is proper and antipodal, thatv is a critical point ofUΦ—for example,( NvO)Gv = {0}—and
that either
(a) the realGv-representation onNvOis irreducible; or
(b) it is a direct sum of pairwise inequivalent irreducibles and a symmetry of the sphere fixing
vand preservingU Φ permutes the summands transitively.
IfΦsatisfies (2.4) with aℓ >0for every ℓ, thenOis a nondegenerate Morse–Bott manifold of
strict local maxima ofUΦ. In particular this holds forΦt(x) =etx at everyt>0.
Proof. By theorem 3.1, the tangent and mixed Hessian entries vanish. Schur’s lemma makes
the self-adjoint Hessian scalar on every indicated irreducible normal summand; the extra
symmetry makes those scalars equal in case (b). Thus the spherical Laplacian is the dimension
of the normal space times their common scalar. It is strictly negative by theorem 2.2; hence
the normal Hessian is negative definite. Its kernel is exactlyTvO, and the Morse–Bott lemma
gives transverse strict local maximality.
Remark 3.3(Why criticality is essential).Let G= SO(2) ×SO(2)act on R2 ⊕R 2 and take
v = (ae1,be1)with a2 + b2 = 1and a̸= b. The proper antipodal orbitaS1 ×bS1 ⊂S 3 has a
one-dimensional, hence irreducible, spherical normal representation, but that representation is
trivial. ForA(θ) = (cosθe 1,sinθe 1),
Ut(A(θ)) =I0(tacosθ)I 0(tbsinθ),
and atcosθ 0 =a,sinθ 0 =b,
d
dθlogUt(A(θ))
⏐⏐⏐⏐
θ0
=tab
[
I1(tb2)
I0(tb2) −I1(ta2)
I0(ta2)
]
.(3.2)
Its small-field expansion is1
2 t2ab(b2 −a2) + O(t4), so the source point is not critical for all
sufficiently small t> 0. This example satisfies the original irreducibility condition but violates
the fixed-vector guard in theorem 3.1.
Corollary 3.4(Uniform tubular exclusion).Assume( NvO)Gv = {0}and either normal-
isotropy condition of theorem 3.2. For every compact[t0,t1] ⊂(0,∞)there is a tubular
neighborhoodTofOsuch that
Ut(a)<U t(v), a∈T \O, v∈O, t∈[t 0,t1].(3.3)
Proof. The smallest magnitude normal-Hessian eigenvalue is continuous on the compact set
O× [t0,t1]and is bounded away from zero. A uniform Taylor remainder and compactness
give the claimed tube.
4 Half-Grassmann no-spinodal rigidity
LetF∈{R,C,H}, letPbe a Haar rank-rorthogonal projector onF 2r, and set
SP =P− 1
2I, ρ 2 =∥SP∥2
F = r
2, u P =SP/ρ.(4.1)
The orbitOF = {uP}is antipodal becauseI−P has the same law. Its real ambient dimensions
are
NR =r(2r+ 1)−1, N C = 4r2 −1, N H = 8r2 −2r−1.(4.2)
4

At
v⋆ = diag(Ir,−Ir)√
2r ,(4.3)
the off-diagonal block is tangent to the conjugacy orbit. The spherical normal space is the
direct sum of the two block-diagonal traceless self-adjoint modules. Each is irreducible under
its stabilizer factor; block exchange together with antipodality makes their Hessian scalars
equal. More explicitly, ifW swaps the twor-blocks, thenA↦→−WAW∗fixes v⋆, exchanges
the normal modules, and preserves the potential becauseµ is both conjugation-invariant and
antipodal. Moreover, a vector fixed by the block stabilizer is scalar on each block; membership
in either traceless normal module forces both scalars to vanish. Hence(Nv⋆OF)Gv⋆ = {0}over
F=R,C,H, and theorem 3.1 proves criticality rather than assuming it.
Theorem 4.1(Balanced no-spinodal theorem).For every r≥ 2, everyF∈{R,C,H} , and
everyt>0, the balanced field orbit (4.3) is a strict constrained local maximizer of
A↦−→Eexp
(
tρ⟨A,uP⟩
)
,trA= 0,∥A∥ F = 1.(4.4)
Its constrained-Hessian kernel consists exactly of conjugacy-orbit directions. Thus the balanced
branch has no finite-field radial spinodal.
Proof. The fixed-vector calculation above supplies the criticality hypothesis. Apply theorem 3.2
to the normal decomposition and the block-exchange symmetry.
For the complex case let
zr(t) =Eetρ⟨v⋆,uP ⟩.
The Gegenbauer–Bessel expansion gives the useful scalar certificate
Gr(t) :=z′′
r(t) + (4r2 −2) z′
r(t)
t −r
2zr(t)>0. (4.5)
Indeed the radial Bessel equation yields
Gr(t) =
∑
ℓ≥1
ℓ(ℓ+ 4r2 −3)
t2 aℓ(t)qℓ >0.(4.6)
Equivalently, the spherical Laplacian atv⋆ equals −t2Gr(t); the common normal-Hessian
eigenvalue is
−t2Gr(t)
2(r2 −1) .(4.7)
5 Complex two-block strata
We now specialize toP∼Gr C(r,2r). Put n= 2r, fix1 ≤k <r, setm= n−k , and letEk
project onto a fixedk-plane. Define
T= tr(E kP), Y=T− k
2, z r,k(u) =EeuY.(5.1)
Thek×kcompressionB=E kPEk has the complex matrix-beta density
cr,kdet(B)r−kdet(I−B) r−k10<B<I dB,(5.2)
and its eigenvalues form a Jacobi unitary ensemble [10, 13, 4]. The Frobenius-unit two-block
field is
Ak =ck
(
Ek −k
nI
)
, c k =
√ n
km,tr(A kP) =c kY.(5.3)
If the physical field strength iss, writeu=sck.
5

Lemma 5.1(Two-block criticality).For every s> 0, the conjugacy orbit ofAk is a critical
manifold of
Fs(A) = logEestr(AP) on{A=A ∗: trA= 0,∥A∥ F = 1}.
Proof.Under the posterior tilted byAk, the meanMs =E AkPcommutes with the stabilizer
U(k) ×U(m). Hence Ms = aEk + b(I−E k)for scalars a,b. Since trMs = r, its traceless part
is proportional to the unique traceless block-scalar directionEk −(k/n)I, and therefore toAk.
The trace-zero ambient gradient ofFs is s(Ms −1
2 I), so it is radial on the Frobenius sphere at
Ak. Every constrained first variation consequently vanishes. Unitary invariance transports
criticality along the full conjugacy orbit.
For the eigenvaluesx1,...,x k ofB, set
S=
k∑
i=1
xi(1−x i).(5.4)
The reversible complex-Jacobi generator is
Lf=
∑
i
xi(1−x i)∂iif+
∑
i
bi(x)∂if,(5.5)
where
bi = (r−k+ 1)(1−2x i) + 2xi(1−x i)
∑
j̸=i
1
xi −xj
.(5.6)
Lemma 5.2(Jacobi–Stein closure).WithΓthe carré du champ of (5.5),
LY=−2rY,Γ(Y,Y) =S,LS= km
2 + 2Y2 −4rS.(5.7)
Under the tilted lawdµu =euYdµ/zr,k(u),
2rδ(u) =uE uS,2rE uY2 =E uS+uE u(YS), δ= (logz r,k)′.(5.8)
Proof. The first two identities follow directly from (5.5). For the third, pair the singular
interaction terms for(i,j)before simplifying. The divided differences ofx(1 −x)(1 −2x) =
x−3x2 + 2x3 reduce toT, ∑ x2
i, andT2; centering cancels every linear term and gives (5.7).
Reversibility givesE[LfeuY] = −uE[Γ(f,Y )euY]. Taking f = Y and thenf = Y2/2gives
(5.8).
6 Exact constrained Hessians
Let q(u) = EuY2 = z′′/z. Fork≥ 2, unitary invariance shows that a Frobenius-unit traceless
split within the positivek-block has posterior variance
α+ = k/4−2rδ/u−q/k
k2 −1 ,(6.1)
while a unit split within the negativem-block has variance
α−= m/4−2rδ/u−q/m
m2 −1 .(6.2)
For example, (6.1) follows from
Eu
[
trB2 −T2
k
]
= k
4 −E uS− q
k,(6.3)
6

and (6.2) follows by applying the same invariant covariance formula to the complementary
block spectrum(1−x 1,...,1−x k,1 r−k,0 r−k).
Along a unit tangent geodesic on the Frobenius sphere, the Hessian of the log partition
divided bys2 is posterior variance minus the spherical Lagrange multiplier. This is a constrained
Hessian because theorem 5.1 supplies the required first-order stationarity:
ℓr,k(u) = Eutr(AkP)
s = nδ(u)
kmu .(6.4)
Define
H+
r,k(u) =z′′+ n(nk−1)
m
z′
u −k2
4 z,
H−
r,k(u) =z′′+ n(nm−1)
k
z′
u −m2
4 z.
(6.5)
Theorem 6.1(Two-block Hessian operators).For every u> 0, the negative-block identity
below holds; whenk≥2the positive-block identity holds as well:
α+ −ℓr,k =−
H+
r,k
k(k2 −1)z , α −−ℓr,k =−
H−
r,k
m(m2 −1)z . (6.6)
For k = 1the positive block has no traceless splitting module, so its first displayed quotient
is omitted. Thus all existing fundamental spectral splitting signs are reduced exactly to scalar
differential inequalities for one Jacobi trace transform.
Proof. Substitute (5.8), (6.1), and (6.2) into (6.4); collect terms usingq = z′′/z and δ =
z′/z.
7 A sharp metastability threshold
The centered law ofYis symmetric. Its second and fourth moments are
µ2 = km
4(n2 −1) , µ 4 = 3km(km−2)
16(n−3)(n−1)(n+ 1)(n+ 3) .(7.1)
These follow either from the matrix-beta Schur expansion or from the standard complex
projector moments. Substitution into (6.5) gives the actual Taylor coefficients
[u2]H+
r,k = k(4r−3k)(k 2 −1)
16(2r−3)(2r−1)(2r+ 1)(2r+ 3) ≥0,(7.2)
with equality only atk= 1, where that splitting module is absent, and
[u2]H−
r,k =− (2r−3k)m(m 2 −1)
16(2r−3)(2r−1)(2r+ 1)(2r+ 3) .(7.3)
When3k= 2r, (7.3) vanishes. The exact sixth moment then gives
[u4]H−
r,2r/3 =− 4r2(4r−3)(4r+ 3)
5832(2r−5)(2r−1) 2(2r+ 1) 2(2r+ 5) <0.(7.4)
Theorem 7.1(Weak-field metastability classification).For sufficiently small nonzero field:
(i) ifk <2r/3, the larger block has an unstable traceless split;
(ii) ifk= 2r/3, the same instability begins at orderu4; and
7

(iii) if2 r/3 <k<r , both block-splitting Hessian eigenvalues are negative, so the unbalanced
two-block orbit is a genuine local maximum modulo its conjugacy orbit.
Proof. Use theorem 6.1 and the signs in (7.2)–(7.4). The remaining off-diagonal directions are
conjugacy-orbit zero modes; the two block modules exhaust the normal spectral directions.
Multiplicity range Weak-field normal type All-/high-field information
1≤k<2r/3saddle larger-block split already unstable
k= 2r/3saddle at orderu 4 quadratic coefficient vanishes
2r/3<k <rmetastable local maximum larger block unstable at high field
k=rstrict local maximum stable for everyu>0by theorem 4.1
Table 1: Exact local classification of the fundamental complex two-block strata. “Metastable”
is a local geometric statement, not a claim of global phase activity.
This theorem rules out the shortcut “every unbalanced two-block stationary orbit is a
saddle.” Near-balanced multiplicities are metastable at weak field. At high field, however,
z′′
z −→k2
4 , z′
uz −→0,
and hence H−
r,k/z→ (k2 −m2)/4 < 0. Each such metastable branch eventually becomes
unstable. This says nothing by itself about which branch has the largest value.
8 A rigorous coefficient-tail reduction
Letµ j =EY j. Coefficientwise negativity ofH−
r,k is equivalent to
µ2j+2
µ2j
< m2
4
2j+ 1
2j+ 1 +n(nm−1)/k .(8.1)
Proposition 8.1(Stein moment-ratio bound).For everyj≥0,
µ2j+2
µ2j
≤k2
4
2j+ 1
2j+ 1 + 2rk.(8.2)
Consequently (8.1) holds whenever
2j(m−k)>m(k 2 −1).(8.3)
Proof.The pointwise inequality
S=
∑
i
xi(1−x i)≤ k
4 −Y2
k (8.4)
follows from Cauchy–Schwarz after writingxi = 1/2 + yi. Reversibility andLY = −2rY give
2rEY2j+2 = (2j+ 1)E(Y 2jS).
Insert (8.4), rearrange, and obtain (8.2). Direct algebra shows that its right-hand side is
strictly smaller than the right-hand side of (8.1) precisely under (8.3).
For every fixed(r,k)this proves the entire sufficiently high-degree tail of the larger-block
Hessian operator. The remaining number of low degrees is finite, but it is not uniform ask↑r .
Finite numerical screens therefore do not constitute an all-rank proof.
8

9 Phase implications and scope
The balanced branch is a strict local maximum at every field by theorem 4.1. Hence any
hypothetical competitor that overtakes it must be separated from the balanced orbit. It
cannot emerge continuously through a vanishing balanced Hessian. On a compact field interval,
theorem 3.4 removes a uniform tube around the balanced orbit from any global search.
The metastability theorem adds a complementary warning. Several unbalanced two-block
strata are also local maxima at weak field, so no argument based only on stationary-point
Hessians can establish the global envelope. A global theorem must instead supply at least one
of:
(a) an all-field Laplace order between external spectra;
(b) a value comparison for every two-block multiplicity plus a theorem reducing global
maximizers to two blocks; or
(c) a nonlocal positivity or total-positivity certificate for the Jacobi Hankel determinants.
The trace transform in (5.1) is connected to differential recurrences for the Jacobi ensemble
[7]; those recurrences do not, by themselves, provide the needed fixed-Frobenius ordering.
The paper proves local orbital geometry and exact metastability. It doesnotprove
global maximization by the balanced field, a complete finite-field phase diagram, or an all-
distortion Shannon rate–distortion function. It also does not interpret local maxima as physical
thermodynamic states unless a separate model supplies such an interpretation.
10 Reproducibility
The accompanying lightweight replay uses exact rational arithmetic and symbolic factorization
to verify (7.1)–(7.4), the algebraic equivalence in (8.3), and the ambient dimensions in (4.2).
It also evaluates the noncritical torus counterexample in theorem 3.3 and checks the positive
Bessel-mode formula on a bounded grid. The replay is evidence against transcription errors,
not a computer-assisted proof of the harmonic or Jacobi theorems; all logical steps used above
are given in the text.
11 Conclusion
Positive-definite orbital potentials have a rigid Laplacian identity at their source orbit: their
nonconstant harmonic content enters with one sign. At a critical source orbit, an isotropy
condition upgrades that trace identity to a complete all-field Morse–Bott maximum theorem;
without criticality this is false, as the explicit torus orbit shows. For half-Grassmann matrix–
Bingham models the normal fixed-vector space vanishes, so the repaired criterion applies
and excludes a balanced spinodal over all three classical division algebras. The exact Jacobi
reduction then exposes a less obvious structure in the complex problem: near-balanced
unbalanced spectra are weak-field metastable, while more asymmetric spectra are saddles.
These results sharply constrain any unresolved intermediate phase while preserving the central
global gate rather than hiding it behind finite moments or numerical evidence.
A Taylor normalization at the degenerate threshold
For completeness, withz(u) = ∑
j≥0 µ2ju2j/(2j)!, an operatorH=z ′′+Az′/u−czhas
[u2]H= 1
2
[
µ4
(
1 + A
3
)
−cµ2
]
,[u 4]H= 1
24
[
µ6
(
1 + A
5
)
−cµ4
]
.(A.1)
9

Atk= 2r/3,m= 4r/3,
µ4 = r2
27(2r−1)(2r+ 1) ,(A.2)
and the Schur expansion of the complex matrix-beta law gives
µ6 = 10r2(4r4 −27r2 + 9)
243(2r−5)(2r−1) 2(2r+ 1) 2(2r+ 5) .(A.3)
Substitution ofA= n(nm−1)/k and c= m2/4in (A.1) yields (7.4). The factorials in (A.1)
are included explicitly because omitting them leaves the signs unchanged but doubles the
quadratic coefficient and multiplies the quartic coefficient by24.
B Algebra behind the Jacobi closure
We record the drift calculation in theorem 5.2. Writep1 = T = ∑
ixi and p2 = ∑
ix2
i, so
S=p 1 −p2. Pairwise symmetrization of the interaction term gives
4
∑
i<j
x2
i(1−x i)−x 2
j(1−x j)
xi −xj
= 4(k−1)T−(4k−6)p 2 −2T 2.(B.1)
Adding the one-particle drift and diffusion terms yields
Lp1 =kr−2rT,Lp 2 = (2r+ 2k)T−4rp 2 −2T 2.(B.2)
Therefore
LS=kr−2kT+ 2T 2 −4rS= k(2r−k)
2 + 2
(
T− k
2
)2
−4rS,(B.3)
which is (5.7). The matrix-beta moment identity used in the replay is
Esλ(B) =s λ(1k) [r]λ
[2r]λ
,(B.4)
with the complex generalized rising factorial[a]λ = ∏
i(a−i + 1)λi. Expanding( trB)j =∑
λ⊢j fλsλ(B)and centering gives (7.1), (A.2), and (A.3) by exact rational simplification.
References
[1] Armine Bagyan and Donald Richards. “Complete Asymptotic Expansions for the Nor-
malizing Constants of High-Dimensional Matrix Bingham and Matrix Langevin Distri-
butions”. In:SIGMA20 (2024), p. 094.doi:10.3842/SIGMA.2024.094.
[2] Antonio Cazzella, Søren Hauberg, Georgios Arvanitidis, and Matteo Matteucci. “On
the Latent Information Geometry of the Grassmann Manifold”. In:Proceedings of
the 29th International Conference on Artificial Intelligence and Statistics. 2026.url:
https://openreview.net/forum?id=BhLHFZwMEr.
[3] Steven B. Damelin, Jeremy Levesley, David L. Ragozin, and Xiaoping Sun. “Energies,
Group-Invariant Kernels and Numerical Integration on Compact Manifolds”. In:Journal
of Complexity25.2 (2009), pp. 152–162.doi:10.1016/j.jco.2008.09.001.
[4] Ioana Dumitriu and Alan Edelman. “Matrix Models for Beta Ensembles”. In:Journal
of Mathematical Physics43.11 (2002), pp. 5830–5847.doi:10.1063/1.1507823. arXiv:
math-ph/0206043.
10

[5] Lluis Eriksson.A Finite-Dimensional Nonanalytic Spectral Transition and Exact High-
Fidelity Rate–Distortion for Rank-rBorn Prediction on Complex Grassmannians. Archive
for Rigorous Research, ARR-2026-6FDEKPVJ0W8BHBMC. 2026.url:https://arr-
research.github.io/papers/ARR-2026-6FDEKPVJ0W8BHBMC/.
[6] Lluis Eriksson.Complete Rank-Two Born-Prediction Rate–Distortion onGrC(2,4): All-
Field Matrix–Bingham Rigidity and a Unique Coexistence Transition.ArchiveforRigorous
Research, ARR-2026-61Y0FFA39M8KMBJ5. 2026.url: https : / / arr - research .
github.io/papers/ARR-2026-61Y0FFA39M8KMBJ5/.
[7] Peter J. Forrester and Santosh Kumar. “Differential Recurrences for the Distribution of
the Trace of theβ-Jacobi Ensemble”. In:Physica D: Nonlinear Phenomena434 (2022),
p. 133220.doi:10.1016/j.physd.2022.133220. arXiv:2011.00787.
[8] Ramesh Gangolli. “Positive Definite Kernels on Homogeneous Spaces and Certain
Stochastic Processes Related to Lévy’s Brownian Motion of Several Parameters”. In:
Annales de l’Institut Henri Poincaré, Section B3.2 (1967), pp. 121–226.url:https:
//www.numdam.org/item/AIHPB_1967__3_2_121_0/.
[9] Claude Itzykson and Jean-Bernard Zuber. “The Planar Approximation. II”. In:Journal
of Mathematical Physics21.3 (1980), pp. 411–421.doi:10.1063/1.524438.
[10] Alan T. James. “Distributions of Matrix Variates and Latent Roots Derived from Normal
Samples”. In:The Annals of Mathematical Statistics35.2 (1964), pp. 475–501.doi:
10.1214/aoms/1177703550.
[11] John T. Kent. “The Complex Bingham Distribution and Shape Analysis”. In:Journal of
the Royal Statistical Society: Series B56.2 (1994), pp. 285–299.doi:10.1111/j.2517-
6161.1994.tb01978.x.
[12] Colin McSwiggen and Siddhartha Sahi.Majorization Inequalities from Logarithmic
Convexity. 2026. arXiv:2605.12680.
[13] Robb J. Muirhead.Aspects of Multivariate Statistical Theory. Wiley, 1982.doi:10.
1002/9780470316559.
[14] I. J. Schoenberg. “Positive Definite Functions on Spheres”. In:Duke Mathematical
Journal9.1 (1942), pp. 96–108.doi:10.1215/S0012-7094-42-00908-6.
[15] Suvrit Sra. “On Inequalities for Normalized Schur Functions”. In:European Journal of
Combinatorics51 (2016), pp. 492–494.doi:10.1016/j.ejc.2015.07.005.
11
