    The Exact Rank Floor for Point-Span Tangent Absorption
                 in Arbitrary Characteristic
                                            Lluis Eriksson
                                        Independent researcher

                            August 24, 2026 (working version 0.7)


                                               Abstract
         Let X be a smooth projective integral variety of dimension d ≥ 1 over an algebraically
     closed field of arbitrary characteristic, let L be very ample, and let m ≥ 1. For a nonempty
     finite reduced set Z ⊂ X, suppose that in the complete Lm -embedding the vector span of the
     points of Z contains the affine embedded tangent space at every point of Z. Equivalently,

                                H 0 (X, IZ ⊗ Lm ) = H 0 (X, I2Z ⊗ Lm ).

     We prove the exact codimension-free lower bound
                                                      d+m                         d+m
                                                                                   
                rk H 0 (X, Lm ) → H 0 (Z, Lm |Z ) ≥
                                                 
                                                            ,         |Z| ≥             .
                                                       d                           d

     The proof projects the original L-embedding finitely onto Pd , injective on Z and with
     isomorphic tangent maps there. Tangent absorption says that degree-m equations of the
                                                                                       (2)
     projected points survive first fattening. Over a perfect field, the inequality α(IY ) ≥ α(IY )+1
     follows by minimal degree: a nonzero partial derivative lowers the degree, while vanishing of
     all partials in characteristic p makes the form a pth power, and radicality lowers the degree
     again. The binomial floor is sharp for every pair (d, m) over C, including with a proper point
     span: simplex-lattice interpolation points are placed in a hyperplane tangent to a smooth
     hypersurface at every support. We also prove downward propagation to every Lk , k ≤ m,
     and combine the exact floor with independent first-jet blocks and a Gauss-fibre alternative.
     The ingredients are classical. The contribution is their combination into an exact absorption
     theorem in arbitrary characteristic; no novelty is claimed for the derivative/pth-root fattening
     argument itself.


1    Introduction
Let k be an algebraically closed field, let X d be a smooth projective integral k-variety, and let
L be a very ample line bundle. The complete linear system embeds

                                      ϕL : X ,→ P H 0 (X, L)∗ .
                                                                 


For a finite reduced set Z ⊂ X, write

          SZ (m) := Spank {evp : p ∈ Z} ⊂ H 0 (X, Lm )∗ ,            hZ (m) := dimk SZ (m).

In the complete Lm -embedding, the affine tangent space at p is the dual of the first-jet quotient
H 0 (2p, Lm |2p ). We study the rigid incidence

                              TbϕLm (p) ϕLm (X) ⊆ SZ (m)         (p ∈ Z),                               (1)

called point-span tangent absorption. It is stronger than an ordinary Terracini defect: the span
of the reduced evaluations already contains all first-order information at the same supports.

                                                    1
Theorem 1.1 (Exact universal floor). Let k be algebraically closed of arbitrary characteristic.
Let X be a smooth projective integral k-variety of dimension d ≥ 1, let L be very ample, let
m ≥ 1, and let Z ⊂ X be a nonempty finite reduced set. If Z is point-span tangent-absorbing
for the complete system Lm , then
                                                     d+m
                                                               !
                        hZ (m) ≥ Bd (m) :=               ,                |Z| ≥ Bd (m).                 (2)
                                                      d
    There is no dependence on the degree, codimension, equations, projective normality, or
Gauss-map degeneracy of the original embedding. The statement also includes m = 1 and
m = 2, where a previous squared-hyperplane argument did not apply.
    The proof has two structural steps. First choose a finite projection π : X → Pd which is
injective on Z and whose tangent map is an isomorphism at every point of Z. If Y = π(Z)
and a degree-m form F vanishes on Y , its pullback vanishes on Z. Absorption makes the
pullback vanish to second order. The cotangent isomorphisms transfer this back to F , giving
           (2)
(IY )m = (IY )m . Second, a nonzero form of least degree in the radical ideal IY cannot vanish
doubly along Y . In characteristic zero a nonzero partial derivative lowers the degree. In
characteristic p, either the same happens or every partial vanishes, in which case perfection gives
                                                                                   (2)
F = Gp and radicality puts the lower-degree form G in IY . Consequently α(IY ) ≥ α(IY ) + 1
in every characteristic, and the displayed equality forces (IY )m = 0. The d+m      degree-m forms
                                                                                 
                                                                              d
on Pd then evaluate independently on Y .
    The floor is not merely an ambient saturation bound.
Theorem 1.2 (Proper-span equality in every dimension and degree). For every d, m ≥ 1 there
exist over C a smooth integral hypersurface X d ⊂ Pd+1 , a nonempty reduced set Z ⊂ X, and
L = OX (1) such that
                                 d+m                                       d+m+1
                                         !                                              !
              |Z| = hZ (m) =         ,              h (X, L ) =
                                                       0        m
                                                                                            > hZ (m),
                                  d                                         d+1
and Z is point-span tangent-absorbing for Lm . Moreover, every projective tangent space Tp X,
p ∈ Z, may be the same hyperplane.
    Thus neither floor can be raised, even after excluding configurations whose point span is the
entire Lm -ambient space. The equality construction uses the d+m       lattice points
                                                                     
                                                                   d

                          [1 : α1 : · · · : αd : 0],           α ∈ Nd ,     |α| ≤ m,
which are unisolvent for polynomials of total degree at most m. A general high-degree hy-
persurface with prescribed common tangent hyperplane at these points is smooth. On it, the
normal coordinate belongs to the square of every corresponding maximal ideal, converting each
degree-m equation of Z into a double equation.
   For m ≥ 3 the exact theorem combines with a rank-sensitive first-jet argument. Put
                               r1 (Z) := rk H 0 (X, L) → H 0 (Z, L|Z )
                                                                                

and let gL (Z) be the largest number of points of Z in one fibre of the Gauss map of the
L-embedding. We obtain
                                                       d+m
                                                 (               !                  )
                         hZ (m), |Z| ≥ max                 , (d + 1)r1 (Z) .                            (3)
                                                        d
Absorption at degree m descends to degree one. Hence r1 (Z) ≥ d + 1; if equality holds, every
original tangent space along Z is one fixed d-plane. If gL (Z) < d+m
                                                                  d , then

                                                       d+m
                                                (               !                   )
                        hZ (m), |Z| ≥ max                  , (d + 1)(d + 2) .                           (4)
                                                        d

                                                           2
Relation to prior work. The inequality α(I (2) ) ≥ α(I) + 1 for finite reduced points is
standard in the study of fattening and symbolic powers. Bocci–Chiantini [6, Remark 2.2] give
explicitly, for planar point sets over an algebraically closed field of arbitrary characteristic, the
same derivative/pth-root dichotomy used below; that argument is independent of the projective
dimension. See also Bauer–Szemberg [4, Lemma 2.4] for the arbitrary-projective-space differential
inequality in their setting. The Zariski–Nagata description of symbolic powers by differential
operators over perfect fields is surveyed by Dao–De Stefani–Grifo–Huneke–Núñez- Betancourt
[9, Proposition 2.14 and Exercise 2.15]; its mixed-characteristic extension is developed by De
Stefani–Grifo–Jeffries [8]. Our degree-two proof is included to make the positive-characteristic
input explicit and self-contained. Finite general projections and Bertini theorems with prescribed
base schemes are classical; compare Altman–Kleiman [1] and the analogous adapted- projection
construction over finite fields in Wang [11, Lemma A.7]. Terracini loci and strong tangential
base loci concern adjacent, but weaker, incidences [3, 2]. Jet-ampleness provides a broader
language for infinitesimal interpolation [5].
    The novelty claim is deliberately narrow: an adapted finite projection and the standard
fattening inequality are combined to obtain the exact codimension-free rank floor in arbitrary
characteristic, and smooth proper-span extremizers are given over C for every (d, m). No
novelty is claimed for those ingredients separately or for the positive-characteristic fattening
argument. The bibliographic search is not a priority certification, and no peer review is claimed.


2      Ranks, double points, and absorption
At a smooth point p ∈ X, write 2p for the first infinitesimal neighbourhood defined by m2p ; it has
length d + 1. For a finite reduced set Z, put 2Z = p∈Z 2p. Since Lm is very ample, restriction
                                                     `

to 2p is surjective, and its dual is the affine tangent space to the cone over the Lm -embedding.

Definition 2.1. A nonempty finite reduced set Z ⊂ X is point-span tangent-absorbing for Lm
if (1) holds for every p ∈ Z.

Lemma 2.2 (Kernel criterion). The following are equivalent:

    (i) Z is point-span tangent-absorbing for Lm ;

 (ii) H 0 (X, IZ ⊗ Lm ) = H 0 (X, I2Z ⊗ Lm );

(iii) restriction to Z and to 2Z has the same rank.

Proof. The annihilator of SZ (m) is the kernel of restriction to Z. The annihilator of the span
of all affine tangent spaces at the supports is the kernel of restriction to 2Z. The point span is
contained in the tangent span, so equality of spans, annihilators, and ranks are equivalent.

Lemma 2.3 (Downward propagation). If Z is tangent-absorbing for Lm , then it is tangent-
absorbing for Lk for every 1 ≤ k ≤ m.

Proof. Fix s ∈ H 0 (X, IZ ⊗ Lk ) and p ∈ Z. Since Lm−k is globally generated, choose tp ∈
H 0 (X, Lm−k ) with tp (p) ̸= 0; for k = m, take tp = 1. Then stp vanishes on Z, so absorption at
degree m makes it vanish on 2Z. In the local ring at p, tp is a unit; hence s ∈ m2p Lkp . Repeating
for every p gives equality of the kernels at degree k, and Lemma 2.2 applies.


3      The fattening gap over perfect fields
                                                                                               (2)
For a nonempty finite reduced Y ⊂ Pd , let IY be its homogeneous radical ideal and IY                =
  q∈Y mq . For a nonzero homogeneous ideal J, let α(J) be its least nonzero degree.
T      2



                                                 3
Lemma 3.1 (Fattening gap). Let k be a perfect field and let Y ⊂ Pdk be a nonempty finite
reduced set of k-rational points. Then
                                          (2)
                                      α(IY ) ≥ α(IY ) + 1.                                    (5)
                            (2)
Consequently, if (IY )m = (IY )m for some m ≥ 1, then (IY )m = 0.
                                           (2)
Proof. Put a = α(IY ) ≥ 1. If 0 ̸= F ∈ (IY )a , every first partial derivative of F vanishes on
Y and hence belongs to the radical ideal IY . If some partial derivative is nonzero, it lies in
(IY )a−1 , contradicting the definition of a.
    It remains to consider characteristic p > 0 when all first partials vanish. Every exponent
occurring in F is then divisible by p. Since k is perfect, the coefficients have pth roots, so
F = Gp for a nonzero homogeneous form G of degree a/p < a. Radicality of IY and F ∈ IY
give G ∈ IY , again contradicting minimality. This proves (5) in every characteristic.
    For the consequence, suppose (IY )m ̸= 0 and choose 0 ̸= F ∈ (IY )a with a = α(IY ) ≤ m.
For each q ∈ Y , choose a degree-(m − a) form Hq with Hq (q) ̸= 0. Then Hq F ∈ (IY )m =
  (2)                                                             (2)
(IY )m ⊂ m2q . Since Hq is a local unit at q, F ∈ m2q . Thus F ∈ IY , contrary to (5) in degree
a.


4    Finite projections adapted to a finite set
Replacing the ambient space of the L-embedding by the linear span of X does not change L or
any evaluation rank.

Lemma 4.1 (Adapted finite projection). Let X d ⊂ PM be smooth, nondegenerate, projective,
and integral, d ≥ 1, and let Z ⊂ X be finite and reduced. There is a linear projection
                                                             ∼
πΛ : X → Pd which is finite, injective on Z, has dπp : Tp X −→ Tπ(p) Pd for every p ∈ Z, and
           ∗ O (1) = O (1). If M = d, take the identity after identifying X = Pd .
satisfies πΛ  Pd      X

Proof. If M = d, a closed integral d-fold in Pd is all of Pd . Assume M > d. Choose a general
Λ= ∼ PM −d−1 disjoint from X, from the finitely many projective tangent spaces Tp X for p ∈ Z,
and from the finitely many secant lines pq for distinct p, q ∈ Z. Each avoidance condition is a
nonempty open condition on the Grassmannian. Their finite intersection is nonempty because
the Grassmannian is irreducible.
    Projection from Λ is a morphism on X. A fibre is the intersection of X with a linear PM −d
containing Λ as a hyperplane. A positive-dimensional projective closed subset of that PM −d
meets every hyperplane, so such a fibre would meet Λ, contradicting X ∩ Λ = ∅. The morphism
is therefore quasi-finite and projective, hence finite. Avoiding Tp X makes dπp injective, thus an
isomorphism. Equivalently, the induced cotangent map is an isomorphism; this is the only local
property used below. Avoiding secants makes π|Z injective. The pullback identity follows from
the linear system defining the projection.


5    Proof of the exact floor
Proof of Theorem 1.1. Embed X by L, apply Lemma 4.1, and put Y = π(Z). The map Z → Y
is a bijection. If F ∈ (IY )m , then s = π ∗ F ∈ H 0 (X, Lm ) vanishes on Z. Absorption makes s
vanish on 2Z. At p ∈ Z, with q = π(p),

                                      d(s)p = d(F )q ◦ dπp .

The left side is zero and dπp is an isomorphism, so d(F )q = 0. Therefore F ∈ m2q for all q ∈ Y
                (2)
and (IY )m = (IY )m . Lemma 3.1 gives (IY )m = 0.

                                                 4
    Evaluation on Y is consequently injective on H 0 (Pd , O(m)), of dimension d+m d . Pulling
                                                                                                       

this subspace back to H 0 (X, Lm ) and using Z ≃ Y proves hZ (m) ≥ d+m        . Since SZ (m) is
                                                                            
                                                                         d
spanned by |Z| evaluation vectors, |Z| ≥ hZ (m).

Corollary  5.1 (Projective form). Under the hypotheses of Theorem 1.1, dim SpanP ϕLm (Z) ≥
 d+m
  d   − 1.

Corollary 5.2 (No low-cardinality extreme defect). If |Z| < d+m
                                                             d , thickening Z to 2Z strictly
                                                                                  

increases the rank of restriction in Lm .

Remark 5.3. Perfection and radicality are the inputs used by this positive-characteristic proof.
The theorem is stated over an algebraically closed field, hence over a perfect field, and the finite
support is reduced. No analogous conclusion is asserted here for imperfect ground fields or
nonreduced supports.


6    Simplex-lattice unisolvence
Here N = {0, 1, 2, . . .}.
   Fix d, m ≥ 1 and set

                                                                                      d+m
                                                                                            !
         Ad,m := {α = (α1 , . . . , αd ) ∈ N : |α| ≤ m},
                                                d
                                                                      |Ad,m | =                 = Bd (m).
                                                                                       d

For α ∈ Ad,m , let pα = [1 : α1 : · · · : αd ] ∈ Pd .

Lemma 6.1 (Simplex-lattice interpolation). Evaluation at the points pα , α ∈ Ad,m , is an
isomorphism
                                                ∼
                            H 0 (Pd , OPd (m)) −−→ CAd,m .

Proof. On the chart x0 = 1, consider the falling-factorial polynomials
                                                         d
                                                                !
                                                               ti
                              Nβ (t1 , . . . , td ) :=
                                                         Y
                                                                  ,    β ∈ Ad,m .
                                                         i=1
                                                               βi

They form a basis of the polynomials of total degree at most m, since each has leading monomial
Q βi
  i ti /βi !. Order Ad,m by a linear extension of the coordinatewise partial order. Then Nβ (α) = 0
unless βi ≤ αi for every i, while Nα (α) = 1. The evaluation matrix is triangular with diagonal
one. Homogenization proves the assertion.

   This is a concrete multivariate Newton interpolation set. The proof is included so the
equality construction does not depend on numerical conditioning or genericity; related lattice
constructions appear in [7, 10].


7    Smooth common-tangent extremizers
Throughout this section the ground field is C.
   Let W = V (y) ∼  = Pd be a hyperplane in Pd+1 with coordinates [x0 : · · · : xd : y]. Regard
the simplex-lattice set

                             Z = {[1 : α1 : · · · : αd : 0] : α ∈ Ad,m } ⊂ W.

Write 2ZW for the union of first neighbourhoods inside W .



                                                           5
Proposition 7.1 (Smooth prescribed-tangent hypersurface). Put r = |Z| = Bd (m). For every
n ≥ 2r + 1, there is a smooth integral degree-n hypersurface X ⊂ Pd+1 containing Z such that
Tp X = W for every p ∈ Z.

Proof. Consider forms

                          F (x, y) = f (x0 , . . . , xd ) + yG(x0 , . . . , xd , y),          (6)

where f ∈ H 0 (W, I2ZW (n)) and G ∈ H 0 (Pd+1 , O(n − 1)).
    The set-theoretic support of this linear system’s base scheme is exactly Z; no assertion
about its scheme structure is needed. Outside W , the term yG is base-point-free. If q ∈ W \ Z,
for each p ∈ Z choose a hyperplane ℓp ⊂ W through p but not through q. Then p∈Z ℓ2p has
                                                                                     Q

degree 2r, vanishes doubly at Z, and is nonzero at q; multiply it by a degree-(n − 2r) form
nonzero at q.
    Thus the restricted linear system on the smooth open set Pd+1 \ Z is base-point-free. The
characteristic-zero smooth Bertini theorem gives smoothness for a general member on that open
set. At p ∈ Z, all tangential derivatives of f vanish, whereas the normal derivative of F is G(p).
The finitely many conditions G(p) ̸= 0 define a nonempty open set. Hence a general member is
smooth at Z and has tangent hyperplane W there. It is integral: if a projective hypersurface of
positive dimension were reducible, two positive-degree components would meet, and their union
would be singular along the intersection. Bertini with a prescribed base scheme is standard; see
Altman–Kleiman [1].

   The numerical threshold is a transparent sufficient bound; no minimality in n is claimed.

Proof of Theorem 1.2. Take Z ⊂ W as above and choose X = V (F ) from Proposition 7.1, with
n ≥ 2Bd (m) + 1. Since n > m and d + 1 ≥ 2, the hypersurface sequence

                     0 −→ OPd+1 (m − n) −→ OPd+1 (m) −→ OX (m) −→ 0

together with H 0 (O(m − n)) = 0 and H 1 (Pd+1 , O(m − n)) = 0 gives
                                                      ∼
                             H 0 (Pd+1 , O(m)) −−→ H 0 (X, OX (m)).                           (7)

   Let a degree-m form Q(x, y) vanish on Z. Its restriction Q(x, 0) to W vanishes at the
unisolvent set of Lemma 6.1, hence is zero. Thus Q = yR for a degree-(m − 1) form R.
   Fix p ∈ Z. Locally, (6) reads f + yG = 0, where f ∈ m2W,p and G(p) ̸= 0. Thus G is a unit
and, in OX,p ,
                                     y = −f /G ∈ m2X,p .
Therefore Q = yR vanishes on 2p. This holds for every p, proving

                         H 0 (X, IZ ⊗ OX (m)) = H 0 (X, I2Z ⊗ OX (m)).

The set is absorbing by Lemma 2.2.
    Lemma 6.1 shows that      the evaluations have rank |Z| = Bd (m). Equation (7) gives
h0 (X, OX (m)) = d+m+1         d (m), so the point span is proper. The common-tangent assertion
                         
                     d+1    > B
is part of Proposition 7.1.

Remark 7.2. The equality family explains why no improvement follows merely from excluding
ambient point spans. Any stronger theorem needs geometric input that rules out, controls, or
classifies high-contact common-tangent sets.




                                                      6
8    Rank-sensitive jet blocks and Gauss fibres
Return to an arbitrary smooth X and very ample L, and put r1 (Z) = hZ (1). The following
extension is useful for m ≥ 3.
Lemma 8.1 (Squared-hyperplane extension). Let m ≥ 3. Suppose p1 , . . . , ps ∈ X have
independent first neighbourhoods for Lm . If the L-evaluation at x ∈ X is not in the span of
the evaluations at the pi , then 2p1 ∪ · · · ∪ 2ps ∪ 2x also imposes independent conditions on
H 0 (X, Lm ).
Proof. In the L-embedding choose e ∈ H 0 (X, L) vanishing at every pi but not at x. The section
e2 vanishes on the old double points and is a unit on 2x. Since Lm−2 is very ample, restriction
to 2x is surjective. Thus e2 H 0 (X, Lm−2 ) realizes arbitrary first-jet data at x while vanishing on
the old union. Correcting residual data at x proves the claim.

Proposition 8.2 (Rank-sensitive floor). If m ≥ 3 and Z is tangent-absorbing for Lm , then
                                                   d+m
                                               (          !                   )
                          hZ (m), |Z| ≥ max            , (d + 1)r1 (Z) .
                                                    d
Proof. Choose r1 (Z) points whose degree-one evaluations form a basis, ordered so that each
new evaluation escapes the preceding span. A single double point imposes d + 1 independent
conditions. Repeated application of Lemma 8.1 makes the r1 (Z) double points independent in
Lm . By absorption, their (d + 1)r1 (Z)-dimensional dual first-jet span lies in SZ (m). Combine
this with Theorem 1.1 and |Z| ≥ hZ (m).

    Let
                                 γL : X −→ Gr(d + 1, H 0 (X, L)∗ )
be the Gauss map of the L-embedding and define
                           gL (Z) :=           max              |Z ∩ γL−1 (W )|.
                                       W ∈Gr(d+1,H 0 (X,L)∗ )

Proposition 8.3 (Degree-one alternative). Under Theorem 1.1, r1 (Z) ≥ d + 1. If r1 (Z) = d + 1,
the degree-one evaluation span is the affine tangent space at every point of Z; all of Z lies in
one fibre of γL and in its projective tangent d-plane.
Proof. By Lemma 2.3, Z is absorbing for L. Its degree-one evaluation span contains a (d + 1)-
dimensional affine tangent space. If its dimension is exactly d + 1, every such tangent space along
Z is a subspace of the same dimension inside it, hence equals it. Evaluation representatives
also lie in their own affine tangent spaces.

Corollary 8.4 (Gauss-fibre refinement). Let m ≥ 3. If Z is absorbing for Lm and gL (Z) <
d+m
 d , then
                                          d+m
                                       (       !                 )
                    hZ (m), |Z| ≥ max            , (d + 1)(d + 2) .
                                            d
Proof. If r1(Z) = d + 1, Proposition 8.3 puts all Z in one Gauss fibre, while Theorem 1.1 gives
|Z| ≥ d+md , a contradiction. Hence r1 (Z) ≥ d + 2, and Proposition 8.2 applies.

    For a smooth quadric, the Gauss map is injective on geometric points, so the corollary
applies automatically. Indeed, if two points have the same polar hyperplane, after rescaling
their difference lies in the radical of the polar bilinear form. If that difference were nonzero, the
quadratic identity and the fact that both points lie on the quadric would make it a singular point
of the quadric. This also covers characteristic two, where the Gauss map may be inseparable and
“polarity” alone would be imprecise. When the binomial term already dominates (d + 1)(d + 2),
the exact theorem is stronger.

                                                    7
9     Comparison with adjacent interpolation loci
     Object                    Incidence condition
     Terracini locus        The union 2Z fails to impose the expected independent con-
                            ditions; the tangent span is defective.
     Strong tangential base A span generated by selected tangent spaces contains another
     locus                  point or tangent space.
     Point-span tangent ab- The span of reduced evaluations already contains the tangent
     sorption               space at every support; point rank equals double-point rank.
     Equality family here   One hyperplane is tangent at an unisolvent set and its normal
                            coordinate is second order in each local ring, giving exact
                            binomial rank with proper point span.

   Absorption implies an extreme Terracini defect unless the point span is ambient, but
ordinary Terracini defect does not imply absorption. Nor can one generally delete a support
and reinterpret absorption as a strong-base- locus condition: its evaluation direction may be
needed to express its own tangent space. Theorem 1.1 bypasses those classification problems by
transporting the incidence to points in Pd and using initial degree.


10     Exact computational witnesses
The accompanying replay repro/verify_exact_projection_floor.py uses exact rational
arithmetic  to construct simplex-lattice evaluation matrices for a grid of (d, m). It verifies rank
 d+m
   d    and checks a falsification boundary: deleting one node leaves a nonzero degree-m equation,
while adjoining first-jet rows increases the value rank.
     The replay repro/verify_common_tangent_extremizer.py checks explicit local fixtures
of the family F = f + yG. It verifies unisolvence, prescribed normal gradients at the supports,
the local second-order identity for y, and equality of value and double-point ranks. These are
exact finite fixtures. They do not replace Bertini, certify every member, prove the universal
theorem, establish priority, or constitute formal verification.
     The positive-characteristic replay repro/verify_perfect_field_fattening.py works by
exact Gaussian elimination modulo p. It exhausts every nonempty reduced support in P1 (F2 ),
P1 (F3 ), and P2 (F2 ) through explicit stated degree cutoffs. For each support it checks the
initial-degree gap and, degree by degree, that equality of the value and first-neighbourhood
kernels occurs only when the value kernel is zero. Separate fixtures exhibit the all-partials-zero
case F = Gp and the lower-degree radical root G. Its exhaustiveness is confined to these finite
spaces and degree ranges.
     A counterexample to the main theorem would be a smooth d-fold over an algebraically
closed field, a very ample L, and a nonempty reduced absorbing Z with hZ (m) < d+m      d . After
                                                                                           
                                                                                      (2)
an adapted projection it would either violate the transferred equality (IY )m = (IY )m or the
perfect-field fattening gap.


11     Scope, limitations, and provenance
• The exact floor is proved over an algebraically closed field of arbitrary characteristic. The
  proof of the fattening gap uses perfection; no descent to imperfect fields is claimed.

• X is smooth, projective, integral, and pure-dimensional, and Z is nonempty, finite, and
  reduced. Nonreduced supports, singular ambient schemes, and mixed dimensions need
  different local statements.


                                                8
• The proper-span sharpness construction is retained over C and proves existence for a sufficient
  hypersurface degree. It neither supplies a positive-characteristic Bertini realization, classifies
  equality, nor minimizes that degree.

• The Gauss-fibre result is a secondary refinement for m ≥ 3. It does not classify Gauss fibres,
  contact loci, Terracini loci, or strong base loci.

• The work proves no statement about a Millennium Prize Problem. The 0–10 research-impact
  scores used during drafting are editorial heuristics, not mathematical claims.

• Literature searches covered the cited fat-point, projection, Bertini, interpolation, Terracini,
  jet-ampleness, and Gauss-map sources. They are not exhaustive MathSciNet/zbMATH
  review or specialist peer review.

• The replay scripts are finite diagnostic witnesses. No Lean certification, independent repro-
  duction, or external validation is claimed.

   The extension of the exact absorption theorem from characteristic zero to arbitrary char-
acteristic applies the standard Frobenius–radical alternative in the minimal-degree fattening
lemma. The proper-span complex extremizers and secondary block refinements are retained.
OpenAI Codex assisted with proof discovery and auditing, literature triage, replay code, and
drafting. The named author is responsible for the claims and any public submission. No external
human peer review or priority certification is claimed.


References
 [1] A. B. Altman and S. L. Kleiman, Bertini theorems for hypersurface sections containing a subscheme,
     Comm. Algebra 7 (1979), no. 8, 775–790. https://doi.org/10.1080/00927877908822375
 [2] E. Ballico, M. C. Brambilla, and P. Santarsiero, On the strong base locus of a projective variety,
     arXiv:2603.15103 (2026). https://arxiv.org/abs/2603.15103
 [3] E. Ballico and L. Chiantini, On the Terracini locus of projective varieties, Milan J. Math. 89 (2021),
     1–17. https://doi.org/10.1007/s00032-020-00324-5
 [4] T. Bauer and T. Szemberg, The effect of points fattening in dimension three, arXiv:1308.4983 (2014).
     https://arxiv.org/abs/1308.4983
 [5] M. C. Beltrametti, S. Di Rocco, and A. J. Sommese, On generation of jets for vector bundles, Rev.
     Mat. Complut. 12 (1999), no. 1, 27–45. https://doi.org/10.5209/rev_REMA.1999.v12.n1.17182
 [6] C. Bocci and L. Chiantini, The effect of points fattening on postulation, J. Pure Appl. Algebra 215
     (2011), no. 1, 89–98. https://doi.org/10.1016/j.jpaa.2010.04.010
 [7] K. C. Chung and T. H. Yao, On lattices admitting unique Lagrange interpolations, SIAM J. Numer.
     Anal. 14 (1977), no. 4, 735–743. https://doi.org/10.1137/0714050
 [8] A. De Stefani, E. Grifo, and J. Jeffries, A Zariski–Nagata theorem for smooth Z-algebras, J. Reine
     Angew. Math. 761 (2020), 123–140. https://doi.org/10.1515/crelle-2018-0012
 [9] H. Dao, A. De Stefani, E. Grifo, C. Huneke, and L. Núñez-Betancourt, Symbolic powers of ideals, in
     Singularities and Foliations: Geometry, Topology and Applications, Springer Proc. Math. Stat. 222
     (2018), 387–432. https://doi.org/10.1007/978-3-319-73639-6_13
[10] S. L. Lee and G. M. Phillips, Construction of lattices for Lagrange interpolation in projective space,
     Constr. Approx. 7 (1991), no. 3, 283–297. https://doi.org/10.1007/BF01888158
[11] X. Wang, On the Bertini regularity theorem for arithmetic varieties, J. Ec. polytech. Math. 9 (2022),
     601–670; see Lemma A.7. https://doi.org/10.5802/jep.191




                                                    9
