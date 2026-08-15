Cellulation-Independent Boundary Gauge Averaging
and Sharp Class-Sector Gaps in Two-Dimensional
Yang–Mills
Compact-group theorem, exact SU(2) constant, and auditable reduction
Lluis Eriksson
with AI-assisted derivation, formalization, and manuscript preparation

August 2026

Version 0.6

Abstract
Let G be a compact connected Lie group equipped with a bi-invariant metric. For
two-dimensional G Yang–Mills with heat-kernel action, we prove a cellulation-independent
finite theorem that turns a framed annular amplitude into the physical transfer kernel
on gauge-invariant boundary states. An explicit conditional-Haar parametrization makes
boundary constraints and boundary-edge subdivision unambiguous. Elementary edge and
face subdivisions leave the normalized edge integral unchanged; after a finite subdivision
made only from these two moves, a radial cut exposes one relative boundary frame, whose
normalized Haar average gives
Z
X
Zt (g, h) =
pt (gxh−1 x−1 ) dx =
e−tcλ χλ (g)χλ (h).
G
λ∈b
G
Here cλ is the Casimir eigenvalue. Thus boundary gauge averaging is exactly the orthogonal
projection of the group heat semigroup onto class functions. Writing c∗ (G) = minλ̸=1 cλ ,
we obtain reflection positivity, the semigroup law, and the sharp mean-zero norm and gap
∥Tt ∥1⊥ = e−tc∗ (G) ,

gap(Tt ) = 1 − e−tc∗ (G) .

Every irrep of minimum positive Casimir saturates the bound. For the stated SU(2) normalization, c∗ = 3/4, uniquely at the fundamental representation, so boundary correlations
across k equal-area strips decay sharply as e−3kt/4 . We also give a gap calculus for products
and finite central quotients; in particular the induced metric on SO(3) = SU(2)/{±I} removes the fundamental channel and raises the minimum from 3/4 to 2. The ingredients are
classical; the contribution is their quantitative end-to-end assembly, including a tree–cotree
disk-elimination schedule, subdivision independence, and an explicit machine-checked SU(2)
frontier. No claim concerns four-dimensional Yang–Mills or arbitrary local observables.

Keywords. two-dimensional Yang–Mills; compact Lie group; heat kernel; subdivision invariance; transfer operator; spectral gap; Lean 4.
MSC 2020. 81T13, 81T25, 22E30, 68V20.

1

Result and epistemic scope

The character solution and the construction of two-dimensional Yang–Mills on compact surfaces
are classical [2, 3, 4]. The point of this paper is not to rediscover them. It is to state and
prove as one finite quantitative theorem a chain usually split among subdivision moves, lattice
gauge fixing, harmonic analysis, and transfer-operator language:
1

arbitrary regular
annular cellulation

subdivide, cut,
collapse to disk

relative-frame
Haar average

compact-group
class kernel

sharp gap and
clustering

Each arrow has a different logical status. All finite-dimensional and spectral steps are proved
below. The disk edge-integral endpoint and the concrete SU(2) character identities have
companion Lean proofs. The topology is that of a regular finite cellulation of an annulus; no
continuum measure, singular decomposition, or local-field reconstruction is claimed.
Our main result is the following.
Theorem 1.1 (Cellulation-independent compact-group transfer). Let G be a compact connected
Lie group with a bi-invariant metric and Haar measure normalized to one. Let t > 0. On
every regular finite annular cellulation of total area t, the heat-kernel lattice amplitude with
gauge-invariant boundary holonomies represented by g, h ∈ G is independent of the cellulation
and equals
X
Zt (g, h) =
e−tcλ χλ (g)χλ (h).
(1)
b
λ∈G

The associated integral operator Tt on L2cl (G) is a positive self-adjoint contraction satisfying
Tt χλ = e−tcλ χλ ,

Ts Tt = Ts+t .

If c∗ (G) = minλ̸=1 cλ , then on L2cl (G) ⊖ C1,
∥Tt ∥ = e−tc∗ (G) .

(2)

Equivalently the bottom of the spectrum of I − Tt on that subspace is 1 − e−tc∗ (G) . Equality is
attained by every character whose irrep has Casimir c∗ (G).
Compactness and connectedness imply that the Laplacian has discrete spectrum, the
constants are its only zero modes, and c∗ (G) > 0. The area t already includes the coupling
and metric convention. Replacing the heat generator by α∆ replaces t everywhere by αt.
Stating the convention is essential: numerical gap constants from different normalizations
cannot otherwise be compared.

2

Compact-group harmonic analysis

b be the unitary dual. For λ ∈ G,
b write d , χ , and c ≥ 0 for its dimension, character,
Let G
λ
λ
λ
and Casimir eigenvalue. Peter–Weyl and elliptic heat-kernel theory give

pt (u) =

X

dλ e−tcλ χλ (u).

(3)

b
λ∈G

For each fixed t > 0 the series and all character series used below converge absolutely and
uniformly; this also follows directly from the smoothness of the heat kernel and standard
spectral estimates on a compact manifold. The characters form an orthonormal basis of L2cl (G)
and satisfy
Z
G

χλ (u)χµ (u) du = δλµ ,

The key operation is orbital averaging.
2

χλ (u−1 ) = χλ (u).

(4)

b
Lemma 2.1 (Orbital character product). For a, b ∈ G and every λ ∈ G,
Z

χλ (xax−1 b) dx =

G

χλ (a)χλ (b)
.
dλ

(5)

Proof. Let
ρλ be the irreducible unitary representation of dimension dλ . Schur’s lemma applied
R
to A = G ρλ (x)ρλ (a)ρλ (x)−1 dx gives A = (χλ (a)/dλ )I. Taking the trace after multiplication
by ρλ (b) proves (5).
Remark 2.2. The factor d−1
λ in (5) cancels the dimension in (3). Missing this cancellation is
precisely what confuses the framed heat kernel with the gauge-invariant cylinder kernel. The
conjugating variable must occur as xax−1 in (5); the superficially similar word axa−1 does not
satisfy this identity.
For G = SU(2) with the normalization used in the machine-checked specialization, irreps
are indexed by n ∈ N0 and
dn = n + 1,

cn =

n(n + 2)
,
4

The characters are real and Weyl integration reads

3

χn (θ) =

sin((n + 1)θ)
.
sin θ

(6)

Rπ
2
SU(2) F = (2/π) 0 F (θ) sin θ dθ.

R

From a physical edge integral to the annulus

We state the finite model explicitly. Let Γ be an oriented regular finite cellulation with edge
set E and faces F . An edge configuration is U ∈ GE . If Uf is the ordered face holonomy and
af > 0 its area, the heat-kernel density is
ρΓ (U ) =

Y

paf (Uf ),

f ∈F

t=

X

(7)

af .

f ∈F

All edge integrations use product probability Haar measure. There is no formal path integral
in this definition.
Definition 3.1 (Boundary-conditioned amplitude). Choose one marked vertex on each boundary and fix representatives g, h ∈ G of the two oriented boundary holonomies. Reorient the
edges of an oriented boundary cycle in its direction and write them as b = (e1 , . . . , er ) from the
marked vertex. Its conditional Haar integral at holonomy g is
Z
Holb =g

Φ dνg :=

Z
Gr−1



Φ u1 , . . . , ur−1 , (u1 · · · ur−1 )−1 g

 r−1
Y

duj .

(8)

j=1

If the ambient orientation gives an inverse edge, the corresponding coordinate is inverted;
inversion preserves Haar probability. The amplitude ZΓ (g, h) is the integral of (7) against
product Haar on internal edges and the two measures (8). Thus no delta distribution or omitted
gauge-volume normalization is hidden in the notation. Independent changes of frame at the
two marked vertices conjugate g and h, so the physical amplitude is a class function in each
variable.
Lemma 3.2 (Canonical boundary fibre). The value in (8) is independent of which boundary
edge is solved for. If a boundary edge is replaced by two consecutive edges, the multiplication
map from their conditional Haar coordinates to the old edge coordinate pushes the new fibre
measure to the old one.

3

Proof. It suffices to compare adjacent eliminated coordinates. Freeze every other edge, absorb
their ordered product and g into a fixed C ∈ G, and call the two adjacent coordinates v, y. The
constraint has the form vy = C. Solving for v parametrizes the fibre by y 7→ (Cy −1 , y); solving
for y parametrizes it by v 7→ (v, v −1 C). The transition y 7→ Cy −1 is an inversion followed by a
translation and hence preserves normalized Haar measure. Adjacent exchanges connect all
choices.
For a subdivision write the old coordinate as u = ab. Haar invariance gives
Z
G2

F (ab) da db =

Z
G

F (u) du.

On a fixed-holonomy fibre, one of a, b is solved from the same ordered-product constraint; the
remaining coordinate integrates to one. This proves the stated pushforward, including the
case in which the old edge was the eliminated coordinate.
The next lemma is the finite mechanism behind cellulation independence.
Lemma 3.3 (Exact elementary subdivision moves). The boundary-conditioned amplitude is
unchanged by either of the following moves, with the boundary data held fixed:
(i) subdivision of an edge into two consecutive edges;
(ii) subdivision of a face of area a + b by a new edge into faces of positive areas a and b.
Consequently it is unchanged under any finite sequence of such subdivisions or their inverses
whenever the inverse cellulation remains regular.
Proof. For (i), every occurrence of the old variable u is replaced by u1 u2 . For any integrable
F , Haar invariance and normalization give
Z
G2

F (u1 u2 ) du1 du2 =

Z
G

F (u) du.

The extra vertex therefore contributes exactly one, not a gauge-volume factor. If the edge is
on a conditioned boundary, the same conclusion is precisely the fibre-pushforward statement of
theorem 3.2; hence this proof does not silently exclude subdivision of the edge used to impose
holonomy. For (ii), orient the new edge so that the two new face words are Au and u−1 B. The
heat-semigroup convolution identity gives
Z
G

pa (Au)pb (u−1 B) du = pa+b (AB),

which is precisely the old face factor. Fubini proves both statements inside the full edge
integral.
Lemma 3.4 (A radial cut after finite subdivision). Every regular finite cellulation of an
annulus has a finite regular subdivision whose one-skeleton contains a simple path joining the
two boundary components. Cutting along this path produces a disk cellulation; its exterior word
consists of the first physical boundary, one copy of the path, the oppositely oriented second
boundary, and the reverse copy of the path.
Proof. Choose a properly embedded PL arc α between the boundary components and put it in
general position with respect to the original one-skeleton: its endpoints lie in boundary edges,
it avoids old vertices, and its finitely many interior intersections with edges are transverse.
First subdivide every edge at an intersection point (and at the two endpoints). These are
moves (i) of theorem 3.3. In each old face the components of α are now pairwise disjoint
polygonal arcs with endpoints at vertices of the subdivided boundary. Insert these arcs one
at a time. Each insertion divides one disk face into two disk faces, so it is move (ii); choose
4

positive daughter areas whose sum is the old face area. After finitely many insertions α is a
simple edge path in the new regular cellulation. This gives directly the required subdivision
using only the two analytically invariant moves, rather than appealing to an unmatched stellar
operation. Cutting an annulus along a proper boundary-to-boundary arc produces a disk, and
its oriented boundary is the first physical boundary, one copy of α, the oppositely oriented
second boundary, and the reverse copy of α.
Let D be the disk obtained from the chosen cut. We write AD (q) for its conditioned edge
integral with exterior holonomy fixed to q ∈ G; all other edge variables are integrated against
product Haar probability.
Lemma 3.5 (Exact disk collapse). For every regular disk cellulation with positive face areas
af and exterior holonomy q,
AD (q) = pP af (q).
(9)
f

Proof. Choose the boundary edge eliminated by (8) and call it e0 . The remaining boundary
edges form a path, so they extend to a primal spanning tree T containing every boundary edge
except e0 . Root T at the marked boundary vertex. Successively changing from a tree-edge
variable to the group element at its child vertex is triangular: every step is a left or right Haar
translation. Gauge covariance of face holonomy and centrality of paf then set every tree edge
to the identity, with each tree-coordinate integral contributing exactly one.
Euler’s identity |E| − |V | + 1 = |F | leaves one chord per bounded face. Elementary planar
tree–cotree duality says that the duals of E \ T form a tree on the bounded faces and the
exterior face. Because T contains all boundary edges except e0 , the dual of e0 is its unique
edge incident to the exterior. Remove that dual edge and root the resulting tree of bounded
faces at the face adjacent to e0 .
Now eliminate bounded faces from the leaves toward the root. For a non-root leaf, its
parent chord occurs once in its face word and once with opposite orientation in the parent
word. After absorbing the other fixed factors into A, B ∈ G, the relevant integral is exactly
Z
G

pa (Au)pb (u−1 B) du = pa+b (AB).

Thus integrating the parent chord deletes that leaf and merges its positive area into the
parent. This is a finite, explicitly ordered elimination; it continues until one face remains.
P
Its boundary word is the fixed exterior holonomy q and its area is f af , proving (9). The
argument uses only normalized Haar invariance, centrality, planar tree–cotree duality, and
heat-kernel convolution, and is valid for every compact group in the hypotheses.
Lemma 3.6 (Radial-cut disintegration). For a subdivided annular cellulation as in theorem 3.4 and fixed oriented boundary holonomies g, h, cutting and regluing give the exact
finite-dimensional identity
ZΓ (g, h) =

Z
G

AD (gxh−1 x−1 ) dx.

(10)

No heat-kernel expansion is used in this step.
Proof. The boundary representatives g and h are held fixed throughout; only internal coordinates are changed. Orient the two copies of the cut oppositely and choose a rooted spanning
tree of the cut-open disk containing all but one of the cut-path links. Introduce a vertex
potential kv ∈ G recursively along the tree and replace every edge variable by
−1
Ue 7−→ ks(e)
Ue kt(e) .

5

annulus

g
x

cut

x

pt (gxh−1 x−1 )

x−1

h−1
Figure 1: A radial cut exposes a relative boundary frame x. The disk edge integral collapses
to one heat kernel; gluing Haar-averages x.
For fixed values of the other coordinates this is a composition of left and right translations
on G; normalized Haar measure is therefore unchanged. Every tree edge becomes the identity. Centrality of each paf makes every face factor invariant under the simultaneous vertex
conjugations, so no Jacobian or residual vertex-volume factor appears.
No boundary representative is integrated and no boundary gauge is divided out in this
coordinate change. The only coordinate not removed by the internal tree gauge is the transport
x from the frame of the first boundary to that of the second. Reading the exterior word of the
disk from the first boundary, the four surviving blocks are g, x, h−1 , and x−1 , in that order.
Thus the conditional integral at fixed x is AD (gxh−1 x−1 ). Regluing identifies the two copies
of the cut but does not fix their relative frame; Fubini disintegrates the product Haar integral
over this last coordinate. Integrating x proves (10).
Proposition 3.7 (Cellulation-independent annular reduction). For every regular finite annular
cellulation of total area t,
Z
Zt (g, h) =

G

pt (gxh−1 x−1 ) dx.

(11)

Proof. Use theorem 3.4 to choose a finite subdivision containing a radial edge path. By
theorem 3.3, the original and subdivided boundary amplitudes are identical. The fixedboundary disk theorem gives AD (q) = pt (q) by the explicit tree–cotree schedule in theorem 3.5;
no gauge-fixing or face-elimination choice is left implicit. Substitute this disk identity into (10).
The resulting right side depends only on t, g, h, proving cellulation independence as well.
Theorem 3.8 (Boundary gauge projection). For t > 0 and g, h ∈ G,
Z
G

pt (gxh−1 x−1 ) dx =

X

e−tcλ χλ (g)χλ (h).

(12)

b
λ∈G

The series converges absolutely and uniformly on G × G for fixed t > 0.
Proof. Absolute uniform convergence of the heat-kernel character expansion justifies termwise
integration. Insert (3), cyclically permute inside the character, and apply theorem 2.1 with
a = h−1 and b = g. Then χλ (h−1 ) = χλ (h), and the orbital factor d−1
the dimension
λ cancels
P 2 −tc
in (3). Uniform convergence of the resulting series follows from |χλ | ≤ dλ and λ dλ e λ < ∞,
the heat trace of the scalar Laplacian on the compact manifold G.
Remark 3.9 (Framed versus gauge-invariant boundaries). The framed transition density is
pt (gh−1 ) on L2 (G) and contains all matrix coefficients. The kernel Zt in (12) acts on L2cl (G)
and contains one character per irreducible representation. They are related by orthogonal
projection, but are not pointwise equal.
6

4

Transfer operator and reflection positivity

Define conjugation averaging on L2 (G) by
Z

(Pcl f )(g) =

G

f (xgx−1 ) dx.

(13)

Proposition 4.1 (Boundary averaging is an orthogonal projection). The operator Pcl is a
self-adjoint idempotent contraction whose range is exactly L2cl (G). It preserves constants and
positivity. If St is the full group heat semigroup with kernel pt (gh−1 ), then
Pcl St = St Pcl ,

Tt = St |L2 (G) = Pcl St Pcl |L2 (G) .
cl

cl

(14)

Thus the physical cylinder operator is a genuine invariant-sector restriction, not an unrelated
kernel obtained by deleting dimension factors by hand.
Proof. Haar invariance gives P2cl = Pcl : after two averages, replace the second conjugating
variable y by yx−1 . The same changes of variables show ⟨Pcl f, g⟩ = ⟨f, Pcl g⟩, so an idempotent
Pcl is the orthogonal projection onto its range. Its fixed points are precisely the conjugationinvariant functions. Averaging preserves 1, nonnegativity, and the L2 norm bound by Jensen’s
inequality. Finally, pt is central, so conjugation commutes with convolution by pt . Restricting
the resulting commuting square to the fixed-point space gives (14); its two-point kernel is
(12).
Define, initially on continuous class functions,
(Tt f )(g) =

Z
G

Zt (g, h)f (h) dh.

(15)

Uniform convergence and (4) give the diagonal action
Tt χλ = e−tcλ χλ .

(16)

It follows immediately that Tt extends to a positive self-adjoint contraction on L2cl (G), Tt 1 = 1,
and Ts Tt = Ts+t .
Proposition 4.2 (Reflection form). For s > 0 and F ∈ L2cl (G),
ZZ
G×G

F (g)Z2s (g, h)F (h) dg dh = ∥Ts F ∥22 ≥ 0.

(17)

For a finite family Fj ∈ L2cl (G) and coefficients zj ∈ C, the corresponding matrix of reflected
pairings is positive semidefinite.
Proof. The semigroup identity gives
Z2s (g, h) = G Zs (g, k)Zs (k, h) dk. Fubini and selfR
P
adjointness turn the left side into G |(Ts F )(k)|2 dk. Replace F by j zj Fj for the matrix
statement.
R

This is the transfer-kernel form of Osterwalder–Schrader positivity for the one-dimensional
time slicing supplied by the cylinder. We do not claim here a reconstruction of a local twodimensional Wightman field theory; the bounded transfer operator is the precise object proved
positive.

7

5

Exact compact-group gap and sharp boundary clustering

Let L2cl (G)0 = {f ∈ L2cl (G) : G f = 0}. The trivial character is 1, so L2cl (G)0 is the closed span
of the nontrivial irreducible characters. Since G is connected and the metric is positive definite,
the scalar Laplacian has constants as its entire kernel. Discreteness of its spectrum therefore
gives
c∗ (G) := min cλ > 0.
R

λ̸=1

Theorem 5.1 (Sharp compact-group mean-zero norm). For t > 0,
∥Tt |L2 (G)0 ∥ = e−tc∗ (G) ,
cl

inf σ (I − Tt )|L2 (G)0 = 1 − e−tc∗ (G) .


cl

The equality space is exactly the span of characters with cλ = c∗ (G).
Proof. Write f =

λ̸=1 aλ χλ . Parseval and (16) give

P

∥Tt f ∥22 =

X

e−2tcλ |aλ |2 ≤ e−2tc∗ (G)

λ̸=1

X

|aλ |2 .

λ̸=1

Any character with minimum positive Casimir attains equality. The equality condition in the
weighted sum also identifies the entire equality space. The spectral statement for I − Tt follows
from the same diagonalization.
Corollary 5.2 (Sharp boundary strip clustering). Let f, g ∈ L2cl (G)0 and let k ≥ 0 be an
integer. Across k strips of area t > 0,
|⟨f, Ttk g⟩| ≤ e−ktc∗ (G) ∥f ∥2 ∥g∥2 .

(18)

The exponential rate and prefactor-one operator bound are sharp. Equality is obtained by taking
f = g to be any unit character of minimum positive Casimir.
Proof. Ttk = Tkt and theorem 5.1 give the bound by Cauchy–Schwarz; a minimum- Casimir
character gives equality.
Corollary 5.3 (Exact SU(2) constant). For G = SU(2) with (6),
3
c∗ (SU(2)) = ,
4

∥Tt |1⊥ ∥ = e−3t/4 ,

gap(Tt ) = 1 − e−3t/4 .

The minimum is unique and the equality space is Cχ1 . Hence (18) becomes the sharp bound
e−3kt/4 .
Proof. For n ≥ 1, (6) and n(n + 2) − 3 = (n − 1)(n + 3) ≥ 0 show that cn ≥ 3/4, with equality
only at n = 1. Apply theorems 5.1 and 5.2.
The compact-group formulation reveals how the boundary gap changes under two basic
operations. This is sometimes hidden when one works only with a fixed matrix group.
Proposition 5.4 (Product and central-quotient gap calculus). Let G1 , G2 carry productnormalized bi-invariant metrics.
(i) For the product metric,
c∗ (G1 × G2 ) = min{c∗ (G1 ), c∗ (G2 )}.
If the first minimum is smaller, the minimum sector is the first minimum sector tensored
with the trivial representation of the second; the symmetric statement holds if the second
is smaller. If they coincide, the two families form the minimum sector.
8

(ii) If Γ is a finite central subgroup of G and G/Γ has the induced quotient metric, then
c∗ (G/Γ) = min cλ ≥ c∗ (G).
λ̸=1
Γ⊆ker ρλ

The inequality is strict exactly when no minimum-Casimir irrep of G is trivial on Γ.
Consequently, in the normalization (6),
c∗ (SO(3)) = 2,

SO(3)

gap(Tt

) = 1 − e−2t .

(19)

Proof. Every irrep of a product is λ1 ⊠ λ2 , and the product Laplacian gives cλ1 ⊠λ2 = cλ1 + cλ2 .
The smallest nonzero sum is therefore the smaller factor minimum, with the stated equality
sector. Irreps of G/Γ are exactly the irreps of G whose kernels contain Γ. The quotient map
is a local isometry, so their Casimir eigenvalues are unchanged. Taking the minimum over
this restricted dual proves (ii) and its strictness criterion. For SU(2)/{±I}, precisely the even
labels n descend. The first nontrivial one is n = 2, and (6) gives c2 = 2.
Remark 5.5 (Generator gap). The generator H defined spectrally by Hχλ = cλ χλ is unbounded,
but Tt = e−tH is bounded. Its lowest nonzero energy is c∗ (G), equal to 3/4 in the stated
SU(2) normalization. The bounded statement (2), specialized to SU(2), is what the current
formal interface certifies. Calling this the solution of the four-dimensional Yang–Mills mass-gap
problem would be false: the dimension, dynamics, and target theorem are different.

6

What is machine checked

The companion Lean development uses Mathlib’s concrete SU(2), constructs normalized Haar
probability, proves the Weyl character formulas and their orthogonality, and proves the actual
infinite heat-kernel convolution semigroup. The following endpoints are directly relevant:
Lean endpoint

Mathematical content

integral_su2Haar_orbit_character_
general
integral_su2ClassHeatKernel_mul

orbital product formula (5)

su2Migdal_twoFace_class_merge
conditionedEdgeModelAmplitude_eq_
heatKernel
su2ClassTransferMultiplier_le_
fundamental
su2ClassTransferMultiplier_bound_
sharp

infinite class-kernel semigroup with a
genuine Haar integral
two-face class Migdal merge
fixed-boundary physical disk edge integral
equals the heat kernel
every non-vacuum multiplier is bounded by
e−3t/4
the fundamental mode attains that bound

The fixed-boundary disk theorem lives on the public boundary-conditioned branch at commit 6dbb8cebc18ab2d65b6ae24af5216347c476df3f; its provenance file identifies the audited
mathematical snapshot a1fbea97cbe673d383dbb4bc5e2a2fb70dbf190a. The sharp multiplier
lemmas are included with this manuscript as SU2ClassTransferGap.lean. The exact target
Lean2dYangMills.SU2ClassTransferGap was rebuilt in this environment from the pinned
manifest: Lake completed all 2,817 jobs with exit code zero. A separate #print axioms audit
reports only propext, Classical.choice, and Quot.sound for the four new endpoints. The
exact boundary-conditioned commit was also rebuilt as the complete Lean2dYangMills library:
Lake completed all 3,097 jobs with exit code zero, including the physical disk endpoint cited
above.
9

Limitation 6.1 (Formalization boundary). The current Lean corpus does not yet package
elementary subdivision invariance, the PL radial-cut reduction, and the disk collapse as one
theorem about regular annular combinatorial maps, nor does it construct the L2 completion
and its unbounded generator. Accordingly, the machine-checked claim is the conjunction of
the disk integral, orbital character identity, class semigroup, and scalar sharp multiplier bound.
The compact-group extension, topological reduction, and Hilbert-space assembly are proved in
this paper, but are not advertised as one monolithic Lean theorem.

7

Reproducibility and falsification checks

The deterministic script repro/replay.py performs five diagnostics:
1. the removable endpoint values χn (0) = n + 1 and χn (π) = (−1)n (n + 1) are tested
exactly;
2. Gauss–Legendre integration of the Weyl formula checks the character Gram matrix;
3. multiplier arithmetic checks e−scn e−tcn = e−(s+t)cn ;
4. a finite spectral search checks that n = 1 is the unique sharp mode;
5. a random complex character polynomial checks positivity of the reflected quadratic form.
These floating-point checks are useful falsifiers for normalization and sign errors, but they are
not substitutes for proof. A successful run prints REPLAY: PASS.

8

Novelty, priority, and limitations

Migdal’s lattice solution, the heat-kernel formulation, and Witten’s character expansion make
the basic cylinder formula classical [1, 2, 4]. The Markov/gluing structure of the rigorous
two-dimensional Yang–Mills measure is also established in the literature [4, 5]. We therefore
make no priority claim for (1) or for diagonalizing a compact-group heat semigroup.
The present theorem is therefore an assembly result, not a priority claim for the character
solution or for subdivision invariance separately. Its increment through Version 0.5 is mathematically explicit: the restriction to an “admissible” SU(2) cellulation has been removed, and
the sharp spectral statement is parametrized by the minimum positive Casimir of an arbitrary
compact connected structure group. The contribution claimed here is:
• an explicit finite-edge-to-transfer chain with all normalization factors;
• exact invariance under the two elementary subdivision moves and a finite PL reduction
from every regular annular cellulation to a radial-cut model;
• a theorem-level distinction between framed and gauge-invariant boundary kernels;
• the exact compact-group transfer gap 1 − e−tc∗ (G) and sharp boundary strip-clustering
constant in the same convention as the physical edge integral;
• a precise map of which links are already machine checked and which are paper proofs.
Version 0.6 does not enlarge that novelty claim. It closes three proof interfaces that were
previously compressed: the conditional Haar measure is given by coordinates and shown
independent of the eliminated boundary edge; the PL arc is inserted using exactly the edge
and face moves covered by the analytic invariance lemma; and the disk identity is proved
10

by a finite tree–cotree elimination schedule. These changes strengthen self-containment and
falsifiability, not historical priority.
The result is special to the exactly soluble two-dimensional heat-kernel model. It does
not address four-dimensional continuum Yang–Mills, interacting local observables in four
dimensions, or the Clay Millennium problem. Nor does it turn the boundary estimate into
clustering for arbitrary local bulk observables or an Osterwalder–Schrader reconstruction.
Regular finite cellulations are covered; singular CW decompositions and continuum limits are
not.

9

Conclusion

Two elementary Haar identities make the finite annular theory independent of its regular
cellulation; a radial cut then exposes boundary gauge averaging as the hinge between the
physical edge model and the class-function transfer operator. The dimension factor cancels for
every compact connected G, reflection positivity is a semigroup square, and the sharp gap is
fixed by c∗ (G). For SU(2) the unique fundamental channel saturates the exact e−3t/4 decay.
The theorem remains deliberately modest about priority and dimension, but the normalization,
cellulation reduction, physical integral, spectral optimum, and formal frontier now belong to
one checkable chain.

A

Coefficient-level proof of positivity

For a finite character polynomial F =
ZZ

λ∈Λ aλ χλ , direct insertion into (17) gives

P

F (g)Z2s (g, h)F (h) dg dh =

X

e−2scλ |aλ |2 .

λ∈Λ

This formula simultaneously proves positivity and locates its null space. At positive time
every coefficient is strictly positive, so the reflected form is strictly positive on nonzero finite
character polynomials. Density extends it to all of L2cl (G); strict positivity remains, although
there is no uniform lower bound because the Casimir spectrum is unbounded.

B

SU(2) normalization cross-check

At n = 0, c0 = 0 and Tt 1 = 1. At n = 1, c1 = 3/4. At n = 2, c2 = 2. Hence the first
multipliers are
1, e−3t/4 , e−2t , e−15t/4 , . . . .
The full heat kernel at the identity begins instead as
pt (1) = 1 + 4e−3t/4 + 9e−2t + 16e−15t/4 + · · · ,
because pt (1) contains dn χn (1) = d2n . The two-point class kernel at (1, 1) has the same diagonal
value, while its expansion at general (g, h) has no dimension coefficient. This is a compact
check that all three formulas are consistent rather than interchangeable.

C

Exact reproduction protocol

The single release archive contains the manuscript and its complete audit payload. At its
root are paper.pdf, manuscript.tex, RELEASE_NOTES.md, and MANIFEST.sha256. Its repro/
directory contains:
11

• replay.py;
• SU2ClassTransferGap.lean;
• AuditClassTransferGap.lean;
• requirements.txt and a command-level README.md;
• reproduce.ps1;
• lean-2d-yang-mills.bundle, a complete Git history containing both exact cited commits;
• pinned-main/, containing the main commit’s exact Lake manifest, package file, and Lean
toolchain declaration.
Thus neither the PDF nor the Lean dependency snapshot has to be obtained as a second
attachment. Every preserved file is covered by the root manifest. From repro/, the numerical
replay alone is
python -m pip install -r requirements.txt
python replay.py
and the complete two-checkout Lean replay is
powershell -ExecutionPolicy Bypass -File .\reproduce.ps1
The driver creates fresh directories from the included Git bundle; it never edits an existing
clone. It checks out main at
05c4ec316cb9aa295416670a2578b1c2e77e1c36
for the scalar gap module and the boundary-conditioned branch at
6dbb8cebc18ab2d65b6ae24af5216347c476df3f
for conditionedEdgeModelAmplitude_eq_heatKernel. The audited builds completed 2,817
jobs for the scalar-gap checkout and 3,097 jobs for the complete boundary-conditioned checkout;
the release driver is designed to repeat both endpoints and terminate with FULL REPRODUCTION:
PASS. This still does not turn the compact-group/topological paper proof into a monolithic
Lean theorem; it makes the formal claims that are made independently reproducible and
version-unambiguous.

References
[1] A. A. Migdal, Recursion equations in gauge field theories, Soviet Physics JETP 42
(1975), 413–418.
[2] E. Witten, On quantum gauge theories in two dimensions, Communications in
Mathematical Physics 141 (1991), 153–209. https://projecteuclid.org/euclid.cmp/
1104248198.
[3] A. N. Sengupta, Gauge theory on compact surfaces, Memoirs of the American Mathematical Society 126 (1997), no. 600. https://doi.org/10.1090/memo/0600.
[4] T. Lévy, Yang–Mills measure on compact surfaces, Memoirs of the American Mathematical
Society 166 (2003), no. 790. https://arxiv.org/abs/math/0101239.
[5] B. K. Driver, F. Gabriel, B. C. Hall, and T. Kemp, The Makeenko–Migdal equation for
Yang–Mills theory on compact surfaces, Communications in Mathematical Physics 352
(2017), 967–978. https://arxiv.org/abs/1602.03905.
12

[6] C. P. Rourke and B. J. Sanderson, Introduction to Piecewise-Linear Topology, Springer,
1972.
[7] The mathlib Community, The Lean mathematical library, in CPP 2020, 367–381.
https://doi.org/10.1145/3372885.3373824.

13

