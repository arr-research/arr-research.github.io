    Characteristic-Free Bounds and Sharp Gauss-Fiber Examples
                 for Point-Span Tangent Absorption
                                            Lluis Eriksson
                                        Independent researcher

                                            August 24, 2026


                                               Abstract
         Let X ⊂ P(V ) be a smooth projective variety over an algebraically closed field, let
                d

      H = OX (1), and use the complete embedding defined by H m , m ≥ 3. A finite reduced set
      Z ⊂ X is point-span tangent-absorbing if the span SZ of its evaluation functionals contains
      the affine embedded tangent space at every support. We prove, in arbitrary characteristic,
                                                                        d+m
                                                                           
                   dim SZ , |Z| ≥ max J(d, m), min (d + 1)(d + 2),                  ,
                                                                          d
      where                                            (
                                       m+1               1,       m even,
                                          
                             J(d, m) =       (d + 1) +
                                        2                0,       m odd.
      The proof retains the escape-or-Gauss-fiber alternative. The characteristic-free step is a
      minimal-degree argument: in characteristic p, a polynomial with all first partials zero is a
      pth power, and radicality replaces the characteristic-zero derivative contradiction.
          We give two complementary geometric results. If the original embedding is the complete
      H-embedding and H = A ⊗ B with both factors separating distinct points, its Gauss map
      is injective and only the strong branch can occur. Conversely, over C, for every d ≥ 2 and
      m ≥ 3 we construct a smooth hypersurface whose exceptional Gauss branch contains an
      absorbing set with
                                                        d+m
                                                              
                                       dim SZ = |Z| =           .
                                                           d
      Thus the binomial estimate is exact within the exceptional branch in all these dimensions
      and degrees. The construction is existential and uses finite jet interpolation and Bertini;
      no classification or broad priority claim is made. A companion paper proves the sharper
      exact global binomial floor in characteristic zero; the present paper’s distinct contribution
      is the characteristic-free alternative and its accompanying Gauss-map geometry.


1     Introduction and statements
Let k be an algebraically closed field, let X d ⊂ P(V ) be smooth and integral, and put
H = OX (1). Write
                          φm = φ|H m | : X −→ P H 0 (X, H m )∗
                                                               

for the complete embedding. For a nonempty finite reduced set Z ⊂ X, set
                            SZ := Spank {evp : p ∈ Z} ⊂ H 0 (X, H m )∗ .
Definition 1.1. The set Z is point-span tangent-absorbing with respect to H m if
                                  Tbφm (p) φm (X) ⊆ SZ       (p ∈ Z),
where the left side is the affine tangent space to the cone over the complete H m -embedding.

                                                   1
   Let
                           γH : X −→ Gr(d + 1, V ),         p 7−→ Tbp X
be the Gauss map of the original H-embedding. The main result is the following.

Theorem 1.2 (Characteristic-free rank alternative). Let k be algebraically closed of arbitrary
characteristic, let X d ⊂ P(V ) be smooth and integral with d ≥ 1, and let m ≥ 3. If Z ⊂ X is
a nonempty finite reduced point-span tangent-absorbing set for the complete H m -embedding,
then at least one of the following nonexclusive alternatives holds:

 (a) Z contains d + 2 supports whose first infinitesimal neighborhoods impose independent
     conditions on H m , and hence

                                   dim SZ , |Z| ≥ (d + 1)(d + 2);

 (b) there is a vector subspace W ⊂ V , dim W = d + 1, such that

                             Z ⊂ X ∩ P(W ),           Tbp X = W       (p ∈ Z),

       and
                                                         d+m
                                                                  !
                                        dim SZ , |Z| ≥       .
                                                          d

Consequently,
                                                          d+m
                                            (                            !)
                       dim SZ , |Z| ≥ min (d + 1)(d + 2),                     .             (1)
                                                           d

   The next bound is independent of the Gauss alternative and grows with m.

Theorem 1.3 (Growing jet-block bound). Under the hypotheses of Theorem 1.2, put

                                    m+1           1,
                                                          (
                                                                  m even,
                                             
                         J(d, m) :=     (d + 1) +
                                     2            0,              m odd.

Then
                                    dim SZ , |Z| ≥ J(d, m).
In particular, combining this with (1) gives the bound in the abstract, and J(d, m) > (d+1)(d+2)
for every m ≥ 2d + 4.

   Our first geometric corollary rules out the exceptional branch for a broad class of original
embeddings.

Corollary 1.4 (Factorized polarizations). Assume in addition that the original embedding is
the complete H-embedding, so V = H 0 (X, H)∗ , and that H = A ⊗ B, where A and B each
separate every ordered pair of distinct closed points. Then the Gauss map γH is injective on
closed points, alternative (a) of Theorem 1.2 holds, and

                                dim SZ , |Z| ≥ (d + 1)(d + 2).

In particular this applies when H = Lr for a very ample line bundle L and r ≥ 2.




                                                  2
Remark 1.5 (Why completeness is necessary). The factorization alone does not control the
Gauss map of an arbitrary incomplete subsystem. Indeed

                           [s : t] 7−→ [s5 + st4 : s4 t + t5 : s3 t2 : s2 t3 ]

embeds P1 in P3 by a subsystem of H 0 (P1 , O(5)). The four coordinates have no common zero:
at either endpoint one of the first two is nonzero, and on st = ̸ 0 the last two are nonzero. On
   ̸ 0 the ratio of the last two coordinates recovers t/s; near [1 : 0] and [0 : 1], respectively,
st =
the ratios of the second to the first and the first to the second recover local parameters. Thus
the map is injective and immersive. Nevertheless the affine tangents at the two endpoints are
both Span(e0 , e1 ). Here O(5) = O(2) ⊗ O(3) with both factors very ample. Hence the complete
embedding hypothesis in Corollary 1.4 cannot simply be dropped.

    The opposite behavior also occurs. The following statement makes exact only the estimate
inside branch (b); it does not say that the binomial is the global minimum when the other
branch has the smaller bound.

Theorem 1.6 (Sharp exceptional Gauss branch). For every d ≥ 2 and m ≥ 3, set

                                           d+m
                                                  !
                                  N=           ,            e = 3N.
                                            d

There exist a smooth integral complex hypersurface X d ⊂ Pd+1 of degree e, a hyperplane
Λ∼= Pd , and a reduced set Z ⊂ X ∩ Λ of N points such that

                                        Tbp X = Λ
                                                b      (p ∈ Z)

and Z is point-span tangent-absorbing for the complete OX (m)-embedding, with

                                       dimC SZ = |Z| = N.

Thus the binomial lower bound in alternative (b) of Theorem 1.2 is attained for every such
(d, m).

    The proofs are self-contained apart from standard Bertini and cohomology of projective
space. The finite-jet constructions are related to jet ampleness [3]; the rank defect sits at
the extreme end of Terracini-type interpolation phenomena [2, 8]. Earlier public working-
note forms of the hypersurface and factorization arguments appear in [5, 6]. Those notes
are antecedents, not external validation. The companion ARR paper [7] proves the sharper
exact universal binomial floor in characteristic zero by an adapted finite projection and a
symbolic-power argument. The present paper neither supersedes nor reproves that sharper
characteristic-zero statement: it extends the rank framework to arbitrary characteristic, adds
the growing bound J(d, m), and isolates complementary Gauss-map criteria and examples. No
exhaustive novelty or priority assertion is made.


2    First jets and the annihilator criterion
For p ∈ X, let 2p be the first infinitesimal neighborhood defined by m2p . It has length d + 1.
Restriction to 2p is surjective for a very ample line bundle, and the dual of its target is the
affine tangent space to the cone over the associated embedding.
    Let 2Z = p∈Z 2p. The point span and the tangent span have annihilators
              `


                                     SZ⊥ = H 0 (X, IZ ⊗ H m ),

                                                   3
and                                            ⊥

                                   Tbφm (p) φm (X) = H 0 (X, I2Z ⊗ H m ).
                               X
                           
                            p∈Z

Since each evaluation line lies in its affine tangent space, double annihilators give the following
exact criterion.

Lemma 2.1 (Kernel criterion). The set Z is point-span tangent-absorbing if and only if

                               H 0 (X, IZ ⊗ H m ) = H 0 (X, I2Z ⊗ H m ).

Equivalently, restriction to Z and restriction to 2Z have the same rank.

     This formulation is scheme-theoretic and characteristic-free.


3      Independent first-jet blocks
We use two kinds of finite interpolation. The first exploits projective independence and is
efficient already in degree three.

Lemma 3.1 (Projectively independent supports). Let S ⊂ X be a finite set whose represen-
tatives in V are linearly independent. If m ≥ 3, then 2S imposes independent conditions on
H m.

Proof. Order S = {p1 , . . . , pr }. A single first neighborhood is separated by H m . Suppose the
first neighborhoods at p1 , . . . , pj−1 have been separated. Projective independence supplies a
linear form a vanishing on their representative span and nonzero at pj . Then a2 vanishes on all
the previous first neighborhoods and is a unit on 2pj . Since H m−2 is very ample, its sections
restrict surjectively to 2pj ; multiplication by the unit a2 preserves that local surjectivity
without changing the old data. Induction proves the claim.

   This direct proof is the characteristic-free specialization needed here. Over C, the same
conclusion also follows from Ballico–Chiantini’s product criterion with L1 = H 2 , L2 = H m−2
and their condition † [2, Definition 3.1 and Theorem 3.5].
   The second interpolation statement works for arbitrary distinct supports and is the direct
input for Theorem 1.3.

Lemma 3.2 (Arbitrary-support jet blocks). Let p1 , . . . , pr be distinct points of X.

    (i) The union 2p1 ∪ · · · ∪ 2pr imposes independent conditions on H 2r−1 .

 (ii) If q is a further point, then 2p1 ∪ · · · ∪ 2pr ∪ q imposes independent conditions on H 2r .

Both conclusions remain true after increasing the exponent of H.

Proof. For every ordered pair of distinct supports choose a section of H that vanishes at the
second support and is nonzero at the first.
    For part (i), fix i and multiply the squares of separators vanishing at all pj with j ̸= i. The
product Pi ∈ H 0 (X, H 2r−2 ) is a unit at pi and vanishes on 2pj for j ̸= i. Multiplying Pi by
sections of H, whose first jets span at pi , realizes arbitrary data on 2pi and zero data on every
other block. Summing over i proves surjectivity.
    For part (ii), multiply the preceding Pi by one separator vanishing at q and nonzero at pi ,
then multiply by a section of H to prescribe the first jet at pi . This has total degree 2r and
kills the simple value at q. Conversely, the product of squared separators vanishing at each


                                                   4
pi and nonzero at q is a section of H 2r that vanishes on all double blocks and is a unit at q.
These sections separate the whole mixed scheme.
    To raise the degree, multiply the constructed sections by a section of a positive power of H
that is nonzero at every selected support. Such a section exists because k is infinite and a
finite union of proper linear subspaces cannot exhaust the space of sections. Multiplication by
this local unit preserves the prescribed truncated jets.

    Lemma 3.2 is also a concrete instance of the tensor product behavior of jet-ampleness
established in [3, Proposition 2.3].


4      Escape or concentration in a Gauss fiber
Lemma 4.1 (Tangent escape separator). Let 0 ̸= v ∈ W ⊊ V represent p = [v] ∈ X, and let
u ∈ Tbp X \ W . For every m ≥ 1 there is a section of H m that vanishes on X ∩ P(W ) but has
nonzero first jet at p in the direction u.

Proof. Choose λ ∈ V ∗ with λ|W = 0 and λ(u) ̸= 0, and choose µ ∈ V ∗ with µ(v) ̸= 0. The
restriction to X of f = λµm−1 vanishes on X ∩ P(W ), while

                                   dfv (u) = λ(u)µ(v)m−1 ̸= 0.

No numerical factor depending on m is used.

Lemma 4.2 (Support alternative). Assume Z is point-span tangent-absorbing. Let p1 , . . . , pr ∈
Z have linearly independent representatives and put W = Span(v1 , . . . , vr ).

    (i) If r ≤ d, some point of Z lies outside P(W ).

 (ii) If r = d + 1, either some point of Z lies outside P(W ), or

                                 Z ⊂ P(W ),          Tbp X = W    (p ∈ Z).

Proof. Suppose Z ⊂ P(W ). If r ≤ d, then dim W = r < d + 1 = dim Tbp1 X, so Lemma 4.1
produces a section annihilating SZ but not the tangent space at p1 , contrary to absorption.
    If r = d + 1, the spaces W and Tbp X have the same dimension. If they differ for some p ∈ Z,
choose a tangent direction outside W and apply the same separator. Hence the no-escape case
forces equality at every support.


5      Unisolvence in the Gauss branch in all characteristics
Lemma 5.1 (Gauss-branch unisolvence). Let W have dimension d + 1, let Z ⊂ P(W ) be a
nonempty finite reduced set, and assume

                                     Tbp X = W         (p ∈ Z).

If Z is point-span tangent-absorbing for H m , then, for R = Sym(W ∗ ) and I = I(Z) ⊂ R,

                                              Im = 0.

Consequently,
                                                        d+m
                                                             !
                                    dim SZ , |Z| ≥          .
                                                         d



                                                 5
Proof. Let F ∈ Im . The inclusion W ⊆ V induces a surjection Symm (V ∗ ) ↠ Symm (W ∗ ), so
F extends to a degree-m form on V . Its restriction to X vanishes on Z, hence pairs to zero
with SZ . Absorption forces its first jet along X to vanish at every p ∈ Z. Since Tbp X = W ,
this is the full projective first jet of F on P(W ).
    Choose coordinates x0 , . . . , xd on W with p = [1 : 0 : · · · : 0]. On x0 = 1, a zero value and
zero directional derivatives mean that F (1, x1 , . . . , xd ) has no terms of degree zero or one. By
homogeneity this is equivalent to F ∈ I(p)2 . Therefore

                                                                                                 (2)
                                                 \
                                          Im ⊆         I(p)2 .
                                                 p∈Z

   Suppose Im ̸= 0 and choose a nonzero homogeneous F ∈ I of minimal positive degree
α ≤ m. For each p ∈ Z, choose Gp ∈ Rm−α with Gp (p) ̸= 0. Then Gp F ∈ Im , so (2) and local
invertibility of Gp give F ∈ I(p)2 locally at every support. All first partial derivatives of F
consequently vanish on Z and belong to the radical ideal I.
   If at least one partial derivative is nonzero, it has degree α − 1 and contradicts the
minimality of α. Otherwise the characteristic is p > 0 and every monomial of F has each
exponent divisible by p. Because k is algebraically closed, hence perfect, its coefficients have
pth roots and
                                            F = Gp
for a homogeneous polynomial G of degree α/p < α. Radicality of I and F ∈ I imply G ∈ I,
again a contradiction. Hence Im = 0.
    The evaluation map Rm → kZ is injective and has rank d+m    d . Every form on W extends
                                                                  

to V , so this value matrix is a submatrix of restriction for H m and its rank is at most both
dim SZ and |Z|.

Remark 5.2. The reducedness of Z, equivalently radicality of I(Z) in this setting, is essential
to this proof in the Frobenius case. The argument is elementary but is consistent with the
differential characterization of symbolic powers over perfect fields; see [4] for a broader modern
framework.


6    Proofs of the rank bounds
Proof of Theorem 1.2. Starting from any support, repeated application of Lemma 4.2(i) se-
lects d + 1 points with linearly independent representatives. Lemma 3.1 makes their first
neighborhoods independent. Their dual tangent blocks, each of dimension d + 1, lie in SZ , so

                              dim SZ ≥ (d + 1)2 ,         |Z| ≥ dim SZ .

   Apply Lemma 4.2(ii). If a further point escapes, the resulting d+2 supports are projectively
independent and Lemma 3.1 gives alternative (a). If no point escapes, the same lemma gives
a common W and common Gauss fiber; then Lemma 5.1 gives alternative (b). Taking the
smaller branch bound proves (1).

Proof of Theorem 1.3. Write first m = 2q + 1. If |Z| ≤ q, part (i) of Lemma 3.2, followed
by degree raising, makes 2Z independent in degree m. Its dual tangent span would have
dimension |Z|(d + 1) but would lie by absorption in SZ , whose dimension is at most |Z|, a
contradiction. Hence Z contains q + 1 supports. Their first neighborhoods are independent in
H 2(q+1)−1 = H m , so
                         dim SZ , |Z| ≥ (q + 1)(d + 1) = J(d, m).




                                                  6
   If m = 2q, the same argument excludes |Z| ≤ q. Choose q supports and one further support.
Lemma 3.2(ii) makes the first q double blocks and the last simple value independent in degree
2q = m. All their dual spaces lie in SZ , giving
                               dim SZ , |Z| ≥ q(d + 1) + 1 = J(d, m).
The threshold comparison is immediate in the two parity cases.


7    Injective Gauss maps from factorization
Proposition 7.1 (Point-separating factors). Let H = A ⊗ B be very ample, and suppose A
and B each separate every ordered pair of distinct closed points. Then the Gauss map of the
complete H-embedding is injective on closed points.
Proof. Fix p ̸= q. Choose
        a ∈ H 0 (X, A),     a(p) = 0, a(q) ̸= 0,         b ∈ H 0 (X, B),     b(p) = 0, b(q) ̸= 0.
The product s = ab ∈ H 0 (X, H) belongs to H 0 (X, H ⊗ m2p ) but satisfies s(q) ̸= 0. Thus the
hyperplane defined by s contains the affine tangent space at p but not the evaluation line at q,
which lies in the tangent space at q. Consequently Tbp X ̸= Tbq X.

Proof of Corollary 1.4. Proposition 7.1 makes   every Gauss fiber a singleton. Alternative (b)
of Theorem 1.2 would require |Z| ≥ d+m        1 inside one fiber, so it is impossible. If H = Lr
                                         
                                       d   >
with r ≥ 2, use the point-separating factors L and Lr−1 .


8    Smooth hypersurfaces realizing the exceptional bound
We now work over C. We first record two elementary interpolation facts.
Lemma 8.1 (Simplex-lattice unisolvence). For n, r ≥ 0, the lattice
                          ∆n,r = {(a1 , . . . , an ) ∈ Zn≥0 : a1 + · · · + an ≤ r}
is unisolvent for polynomials of total degree at most r.
Proof. If n = 0 or r = 0, the assertion is the constant-polynomial case. Now induct on n + r.
If f vanishes on ∆n,r , its restriction to xn = 0 vanishes on ∆n−1,r , so f = xn g by induction.
Then g(x1 , . . . , xn−1 , t + 1) vanishes   on ∆n,r−1 and is zero by induction. Thus f = 0. The
number of lattice points is n+r        , the dimension of the polynomial space.
                                     
                                   n

Lemma 8.2 (Prescribed triple jets). Let p1 , . . . , pN be distinct points of Pd and set e = 3N .
Then
                                                         N
                                  H 0 (Pd , O(e)) −→
                                                         M
                                                             OPd ,pi /m3pi
                                                  i=1
is surjective. Moreover, H (P , I3Z (e)) is basepoint-free on Pd \ Z.
                          0  d

Proof. For fixed i, choose for each j ̸= i a linear form vanishing at pj and nonzero at pi . The
product of their cubes has degree 3(N − 1), is a unit at pi , and vanishes to order at least three
at every other support. In affine coordinates centered at pi , the classes of monomials of total
degree at most two form a basis of the local algebra modulo m3pi ; they are restrictions of global
quadrics. After multiplying by one further linear form nonzero at every support and adjusting
the local datum by the resulting unit, degree-e forms realize arbitrary triple jets at pi and zero
jets elsewhere. Summing over i proves surjectivity.
           / Z, choose a linear form ℓi vanishing at pi and nonzero at q for every i. The product
     For q ∈
  i ℓi has degree e, belongs to I3Z , and is nonzero at q.
Q 3


                                                     7
Proposition 8.3 (A large special Gauss fiber). For every d ≥ 2 and N ≥ 1 there is a smooth
integral hypersurface X d ⊂ Pd+1
                             C   of degree 3N and a hyperplane Λ ∼
                                                                 = Pd such that one fiber of
the Gauss map contains any prescribed set of N distinct points of Λ.
Proof. Use coordinates with Λ = (x0 = 0) and let Z = {p1 , . . . , pN } ⊂ Λ. By Lemma 8.2,
choose a degree-e form f0 on Λ whose constant and linear terms vanish at each pi and whose
quadratic term there is nondegenerate. Every member of
                                      f0 + H 0 (Λ, I3Z (e))
has the same ordinary-double-point jets. The translation space is basepoint-free away from
Z. The corresponding projective system has base locus exactly Z; its nonempty Bertini open
meets the affine chart where the coefficient of f0 is one. Hence Bertini gives a member f whose
hypersurface Y = (f = 0) ⊂ Λ has ordinary double points at the pi and is smooth away from
them [9, III, Corollary 10.9].
   Consider ambient degree-e forms
                         F = f + x0 G,       G ∈ H 0 (Pd+1 , O(e − 1)).
The projective linear system spanned by f and x0 H 0 (Pd+1 , O(e − 1)) has base locus exactly
Y . Its Bertini-smooth locus outside Y is a nonempty open subset of the irreducible parameter
space, and it meets the affine chart in which the coefficient of f is one. At a smooth point
of Y , the differential of f in a direction tangent to Λ is nonzero. At a marked node, choose
G(pi ) ̸= 0; then
                                         dFpi = G(pi ) dx0 ,
so the ambient hypersurface is smooth there and has tangent hyperplane Λ. Away from
Y , Bertini makes a general member smooth [9, III, Corollary 10.9]. The finitely many
conditions G(pi ) ̸= 0 are nonempty open conditions in the same irreducible affine chart, so
their intersection with the Bertini open is nonempty. The resulting hypersurface is reduced
by smoothness. If it had two positive-degree components, they would meet in Pd+1 because
d ≥ 2 [9, I, Theorem 7.2], making their union singular; hence it is irreducible and therefore
integral. All marked points lie in the Gauss fiber over Λ.

Proof of Theorem 1.6. Take N = d+m        and identify the affine chart of Λ ∼
                                                                             = Pd with Cd . Let Z
                                        
                                      d
be the homogenization of ∆d,m . Lemma 8.1 says that no nonzero degree-m form on Λ vanishes
on all of Z. Equivalently, their degree-m evaluation vectors span the full vector space Symm (Λ)b
of dimension N . Here we use the canonical dual identification H 0 (Λ, OΛ (m))∗ ∼  = Symm (Λ).
                                                                                             b
    Apply Proposition 8.3 to these supports, obtaining a smooth degree-e = 3N hypersurface
X. Since e > m and d + 1 ≥ 3, the restriction sequence
                    0 −→ OPd+1 (m − e) −→ OPd+1 (m) −→ OX (m) −→ 0
and the vanishing of intermediate cohomology of projective space [9, III, Theorem 5.1] show
that
                                             ∼
                                             → H 0 (X, OX (m)).
                           H 0 (Pd+1 , O(m)) −
Thus the complete OX (m)-embedding is the restriction of the ambient mth Veronese embedding.
   If p = [v] ∈ Z, Proposition 8.3 gives Tbp X = Λ.
                                                 b The affine tangent space after the Veronese
embedding is
                                            b ⊆ Symm (Λ).
                                      v m−1 Λ         b

The differential carries the scalar factor m, which is nonzero and irrelevant to this subspace
because the construction is over C. The right side is exactly the span of the evaluation vectors
of Z. Therefore every tangent block lies in SZ and Z is absorbing. The same unisolvence gives
dim SZ = N = |Z|.

                                               8
Remark 8.4. For (d, m) = (2, 3) the construction gives ten absorbing points on a smooth
degree-30 surface in P3 , so the exact value ten is not confined to a linearly embedded plane.
In higher parameters the example is sharp for the exceptional branch but need not attain the
smaller global branch bound.


9     Relation to adjacent notions and limitations
The equality of value and first-jet kernels in Lemma 2.1 is stronger than an ordinary Terracini
defect. It says that the full double-point rank has collapsed to the value rank. Conversely, a
Terracini defect alone does not imply absorption [2, 8].
    Under absorption one also has

                               SZ = Span{Tbφm (p) φm (X) : p ∈ Z}.

If A ⊆ Z is minimal with the same tangent span, then Z \ A lies in the strong base locus of
A. This places the problem inside the framework of [1], while the additional equality with
a span of evaluations is the special constraint used here. Strong base loci and Terracini loci
are not comparable in general [1]. For classical background on Gauss maps, tangent loci, and
dual varieties, see [12]. Multitangent hyperplanes also have a substantial enumerative and
dual-variety literature. Vainsencher counts n-fold tangent hyperplanes to surfaces in specific
generic settings for 1 ≤ n ≤ 6 [11], while Holweck studies bitangent components in singular
loci of dual varieties [10]. Those works concern enumerative or dual-singularity questions; they
do not by themselves establish the value-span absorption constraint used here or priority for
the present construction.
    The following limitations are material.

    • Theorem 1.2 is stated over algebraically closed fields. A version over a nonclosed perfect
      field would require a careful formulation for closed points and residue fields; it is not
      asserted here.

    • The hypersurface construction is over C. It uses ordinary double points with nondegen-
      erate quadratic parts and a standard Bertini argument; no positive-characteristic version
      is claimed.

    • The construction proves existence, not an explicit globally smooth equation. Finite rank
      replays can certify interpolation and absorption matrices, but cannot replace Bertini or
      prove the universal theorem.

    • Neither equality configurations nor varieties with large special Gauss fibers are classified.
      The simplex lattice is one unisolvent fixture among many.

    • The cited literature comparison is selective. The paper claims the displayed deductions
      and constructions, not exhaustive priority for tangent containment, jet separation, or
      special Gauss fibers.


10      Conclusion
Point-span tangent absorption admits a uniform characteristic-free structure: support escape
gives independent tangent blocks, while failure of escape puts all supports into a single original
Gauss fiber and forces degree-m unisolvence there. Arbitrary-support interpolation adds
the growing bound J(d, m). Factorization eliminates the Gauss branch when the original
H-embedding is complete, whereas smooth complex hypersurfaces with prescribed nodal


                                                 9
hyperplane sections realize its binomial estimate exactly. These results sharpen the rank
picture in arbitrary characteristic without asserting a classification or relying on computational
fixtures as proof. In characteristic zero the stronger exact global floor is supplied by the
companion work [7].


References
 [1] E. Ballico, M. C. Brambilla, and P. Santarsiero, On the strong base locus of a projective
     variety, arXiv:2603.15103 (2026). https://arxiv.org/abs/2603.15103

 [2] E. Ballico and L. Chiantini, On the Terracini locus of projective varieties, Milan J. Math.
     89 (2021), 1–17. https://doi.org/10.1007/s00032-020-00324-5

 [3] M. C. Beltrametti, S. Di Rocco, and A. J. Sommese, On generation of jets for vector
     bundles, Rev. Mat. Complut. 12 (1999), 27–45. https://doi.org/10.5209/rev_REMA.
     1999.v12.n1.17182

 [4] A. De Stefani, E. Grifo, and J. Jeffries, A Zariski–Nagata theorem for smooth Z-
     algebras, J. Reine Angew. Math. 761 (2020), 123–140. https://doi.org/10.1515/
     crelle-2018-0012

 [5] L. Eriksson, B219—Special Gauss fibers can be arbitrarily large, public working note
     (2026), repository record B219.

 [6] L. Eriksson, B220—A factorized polarization has injective Gauss map, public working
     note (2026), repository record B220.

 [7] L. Eriksson, The Exact Universal Rank Floor for Point-Span Tangent Absorption: Projec-
     tion, Fattening, and Common-Tangent Extremizers, ARR-2026-2MHNZRRJP49Y9SWP,
     v1 (2026). https://arr-research.github.io/papers/ARR-2026-2MHNZRRJP49Y9SWP/

 [8] F. Galuppi, P. Santarsiero, D. A. Torrance, and E. T. Turatti, Geometry of first nonempty
     Terracini loci, arXiv:2311.09067 (2023). https://arxiv.org/abs/2311.09067

 [9] R. Hartshorne, Algebraic Geometry, Graduate Texts in Mathematics, vol. 52, Springer,
     New York, 1977.

[10] F. Holweck, Singularities of duals of Grassmannians, J. Algebra 337 (2011), 369–384.
     https://doi.org/10.1016/j.jalgebra.2011.04.023

[11] I. Vainsencher, Enumeration of n-fold tangent hyperplanes to a surface, J. Algebraic Geom.
     4 (1995), 503–526. https://arxiv.org/abs/alg-geom/9312012

[12] F. L. Zak, Tangents and Secants of Algebraic Varieties, Translations of Mathematical
     Monographs, vol. 127, American Mathematical Society, Providence, 1993.




                                               10
