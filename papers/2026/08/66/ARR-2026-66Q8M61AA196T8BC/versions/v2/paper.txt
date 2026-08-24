               Exact Floors and Proper-Span Extremizers
                   for Higher Osculating Absorption
                                           Lluis Eriksson
                                        Independent researcher

                                  August 24, 2026 (version 2)


                                               Abstract
         Let X be a smooth projective integral d-fold over an algebraically closed field, let H be
     very ample, and use the complete embedding defined by H m . Fix 1 ≤ s ≤ m. A nonempty
     finite reduced set Z ⊂ X is point-span s-osculating-absorbing if the span SZ of its value
     evaluations contains the affine osculating space of order s at every support. We prove the
     exact characteristic-free floor
                                                       d+m
                                                            
                                      dim SZ , |Z| ≥           .
                                                          d
     The estimate follows from the exact tangent-absorption theorem, but its sharpness under the
     stronger higher-order hypothesis is not formal. For every (d, m, s) and every algebraically
     closed field we construct a smooth integral hypersurface and a proper-span equality set
     with dim SZ = |Z| = d+m   d  . All supports lie in one hyperplane whose normal coordinate
     vanishes to order s + 1 on the hypersurface. The proof uses two explicit incidence estimates
     and is valid in positive characteristic.
         We also prove a rank-sensitive refinement. If r1 (Z) is the evaluation rank in H and
     m ≥ 2s + 1, then
                                                   d+m       d+s
                                                                     
                           dim SZ , |Z| ≥ max              ,        r1 (Z) .
                                                      d        d
     The degree threshold is necessary for a uniform statement, as rational normal curves show.
     The earlier mixed-jet certificate is retained for jet-ample polarizations, but its numerical
     floor is explicitly identified as nonoptimal for tensor powers after the exact tangent theorem.
     No equality classification, minimal hypersurface degree, or exhaustive priority claim is
     made.


1    Statement and scope
Let k be algebraically closed, let X be smooth, projective, integral, and of dimension d ≥ 1,
and let H be very ample. Write

                                   φm : X −→ P(H 0 (X, H m )∗ )

for the complete embedding. For a nonempty finite reduced set Z ⊂ X, set
                                                                          
                          SZ = Im H 0 (Z, H m |Z )∗ −→ H 0 (X, H m )∗ .

Equivalently, SZ is the span of the evaluation lines at the supports; this formulation makes no
choice of fiber trivializations. For p ∈ X and a ≥ 0, put
                                                                         d+a
                                                                               !

                                             p ),
                      (a + 1)p = Spec(OX,p /ma+1             λd (a) =        ,
                                                                          d

                                                   1
and set λd (−1) = 0.
   The order-a principal-parts evaluation is
                                                                            
                        jpa : H 0 (X, H m ) −→ H 0 (a + 1)p, H m |(a+1)p .

We define the affine order-a osculating space intrinsically by
                               a
                            d (H m ) = Im((j a )∗ ) ⊂ H 0 (X, H m )∗ .
                            Oscp            p

This convention uses no ordinary derivatives or factorials.

Definition 1.1. Fix 1 ≤ s ≤ m. The set Z is point-span s-osculating-absorbing for H m if
                                      s
                                   d (H m ) ⊆ SZ
                                   Oscp                    (p ∈ Z).

   Put
                                                        d+m
                                                            !
                                          Nd,m :=           .
                                                         d

Theorem 1.2 (Exact higher-osculating floor). Over an algebraically closed field of arbitrary
characteristic, every nonempty finite reduced point-span s-osculating-absorbing set for the
complete H m -embedding satisfies

                               dim SZ ≥ Nd,m ,            |Z| ≥ Nd,m .

Theorem 1.3 (Rank-sensitive higher blocks). Let

                           r1 (Z) = rk H 0 (X, H) −→ H 0 (Z, H|Z ) .
                                                                         


If m ≥ 2s + 1, then
                           dim SZ , |Z| ≥ max {Nd,m , λd (s)r1 (Z)} .
The threshold m ≥ 2s + 1 cannot be weakened in a uniform theorem with the same second term.

Theorem 1.4 (Characteristic-free proper-span equality). For every algebraically closed field,
every d, m ≥ 1, and every 1 ≤ s ≤ m, there exist a smooth integral hypersurface X d ⊂ Pd+1 , a
nonempty reduced set Z ⊂ X, and H = OX (1) such that

                                                                   d+m+1
                                                                                 !
                      |Z| = dim SZ = Nd,m < h0 (X, H m ) =               ,
                                                                    d+1

and Z is point-span s-osculating-absorbing for H m . All supports may lie in one hyperplane
whose defining coordinate belongs to ms+1
                                      X,p for every p ∈ Z.

    Theorem 1.2 supersedes the smaller mixed floor published in the first version of this record.
That earlier inequality remains correct, as does its heterogeneous interpolation certificate, but
higher-order absorption contains tangent absorption and the latter now has the exact binomial
floor [6]. The contributions of this revision are the higher-block refinement and proper-span
sharpness in every order and characteristic.




                                                    2
2     The annihilator criterion
Let (s + 1)Z =    p∈Z (s + 1)p. Finite-scheme duality gives
                 `


                                      SZ⊥ = H 0 (X, IZ ⊗ H m )
and                                      ⊥
                                     s
                                  d (H m ) = H 0 (X, I
                                  Osc                  (s+1)Z ⊗ H ).
                             X
                                                                 m
                                     p
                         
                          p∈Z

Lemma 2.1 (Higher-order kernel criterion). The set Z is point-span s-osculating-absorbing if
and only if
                     H 0 (X, IZ ⊗ H m ) = H 0 (X, I(s+1)Z ⊗ H m ).
Proof. The inclusion from right to left always holds because I(s+1)Z ⊆ IZ . Absorption is
equivalent to
                                        d s (H m ) ⊆ SZ .
                                       Osc
                                   X
                                           p
                                        p∈Z
Taking annihilators reverses this inclusion and supplies the converse inclusion between the
displayed spaces of sections.
                                                   a                 s
                                         d (H m ) ⊆ Osc
   The principal-parts filtration gives Osc  p
                                                       d (H m ) for a ≤ s. Thus order-s
                                                          p
absorption contains every lower-order jet block. The converse is not asserted.
                                                                                1
                                                                d (H m ) is contained in
Proof of Theorem 1.2. Because s ≥ 1, every affine tangent space Oscp
   s
Oscp (H ) and hence in SZ . Thus Z is point-span tangent-absorbing. The exact tangent-
d       m

absorption theorem [6, Theorem 1.1] gives
                                                       d+m
                                                             !
                                  dim SZ , |Z| ≥                 = Nd,m .
                                                        d
No characteristic-zero derivative or factorial is introduced by this reduction.

Lemma 2.2 (Downward propagation). If Z is point-span s-osculating-absorbing for H m , then
it is point-span s-osculating-absorbing for H k for every s ≤ k ≤ m.
Proof. Fix a ∈ H 0 (X, IZ ⊗ H k ) and p ∈ Z. Choose bp ∈ H 0 (X, H m−k ) with bp (p) ̸= 0; take
bp = 1 if k = m. Then abp vanishes on Z, so Lemma 2.1 in degree m makes it vanish on
                                                                    p . This holds at every
(s + 1)p. The germ of bp is a unit, hence the germ of a belongs to ms+1
support, so the two kernels in degree k agree and Lemma 2.1 applies.


3     Mixed-jet interpolation
Lemma 3.1 (Full jets from powers). If p ∈ X and 0 ≤ a ≤ k, then
                                                                           
                             H 0 (X, H k ) −→ H 0 (a + 1)p, H k |(a+1)p
                              a
                         d (H k ) = λ (a).
is surjective. Hence dim Oscp        d

Proof. Choose u0 ∈ H 0 (X, H) nonzero at p. Very ampleness and smoothness give u1 , . . . , ud ,
vanishing at p, such that xi = ui /u0 form a regular system of parameters. For every multi-index
α with |α| ≤ a,
                                          k−|α| α1
                                         u0    u1 · · · uαd d
has local representative xα after trivializing by uk0 . These monomials form a basis modulo
 p . No differentiation is used.
ma+1

                                                       3
Lemma 3.2 (Higher-block extension). Assume m ≥ 2s + 1. Suppose the schemes (s +
1)p1 , . . . , (s + 1)pt impose independent conditions on H m . If the H-evaluation at x ∈ X is not
in the span of the evaluations at p1 , . . . , pt , then adjoining (s + 1)x preserves independence.

Proof. Choose e ∈ H 0 (X, H) vanishing at every pi and nonzero at x. Then es+1 vanishes
on all old (s + 1)-neighbourhoods and is a unit on (s + 1)x. Put k = m − s − 1. The
numerical hypothesis gives k ≥ s, so Lemma 3.1 says that H k realizes arbitrary order-s data
at x. Multiplication by the local unit es+1 preserves that jet target and kills all old targets.
Correcting residual data at x proves surjectivity on the enlarged disjoint union.

Proof of Theorem 1.3. Choose r1 (Z) supports whose degree-one evaluation lines form a basis,
ordered so that each new line escapes the preceding span. A single (s + 1)-neighbourhood
imposes λd (s) independent conditions on H m by Lemma 3.1. Repeated use of Lemma 3.2
makes the r1 (Z) selected neighbourhoods independent. Their dual order-s osculating blocks
form a direct sum of dimension λd (s)r1 (Z) inside SZ . Combine this with Theorem 1.2 and
|Z| ≥ dim SZ .
    To see that the degree threshold is necessary for this uniform second term, take X = P1 ,
H = OP1 (1), and m + 1 distinct points. Their H m -evaluation span is the whole (m + 1)-
dimensional ambient vector space, so they absorb every order s ≤ m, while r1 (Z) = 2. If
m ≤ 2s, then m + 1 < 2(s + 1) = λ1 (s)r1 (Z).

Lemma 3.3 (Mixed-jet interpolation). Let t ≥ 1, let p1 , . . . , pt be distinct points, let ai ≥ 0,
and put
                                             t
                                       K=          (ai + 1) − 1.
                                             X

                                             i=1

Then restriction is surjective:
                                           t                                  
                        H 0 (X, H K ) −→         H 0 (ai + 1)pi , H K |(ai +1)pi .
                                           M

                                           i=1

The same holds for H k in every degree k ≥ K.

Proof. For each i ̸= j, choose ℓij ∈ H 0 (X, H) with ℓij (pj ) = 0 and ℓij (pi ) ̸= 0, and set
                                                   Y aj +1
                                           Pi =           ℓij   .
                                                   j̸=i

It is a unit at pi and vanishes to the prescribed order at every other support. Lemma 3.1
realizes arbitrary order-ai data using H ai . Multiplication by the unit Pi is an automorphism
of the truncated local algebra, so degree-K sections realize arbitrary data at pi and zero data
elsewhere. Sum over i.
    For k > K, multiply by a section of H k−K nonzero at every support. It exists because k is
infinite and a finite union of proper linear subspaces cannot exhaust the section space.

    Over the complex numbers this is also the line-bundle specialization of [4, Proposition 2.3].
The direct proof records the exact specialization and is characteristic-free. The interpolation
statement itself is not claimed as new; the point here is its rank consequence under the
absorption constraint and the ensuing optimization.




                                                     4
4      The retained mixed-jet certificate
Write uniquely
                         m + 1 = q(s + 1) + r,                q ≥ 1,      0 ≤ r ≤ s,
and put
                                 Bd,s (m) = qλd (s) + λd (r − 1).                                    (1)

Theorem 4.1 (Mixed-jet floor from version one). Under the hypotheses of Theorem 1.2,

                                       dim SZ , |Z| ≥ Bd,s (m).

For d ≥ 2 and s < m, this valid inequality is strictly weaker than the exact floor Nd,m of
Theorem 1.2; it is retained because the heterogeneous certificate below also applies to abstract
jet-ample polarizations.

    The interpolation lemma first gives a heterogeneous certificate, before optimization.

Proposition 4.2 (Mixed-block rank certificate). Under the hypotheses of Theorem 1.2, choose
t ≥ 1 distinct supports p1 , . . . , pt ∈ Z and orders 0 ≤ ai ≤ s. If
                                        t
                                              (ai + 1) ≤ m + 1,
                                        X

                                        i=1

then
                                                      t
                                        dim SZ ≥              λd (ai ).
                                                      X

                                                      i=1

Proof. Put K = i (ai + 1) − 1 ≤ m. Lemma 3.3, followed by degree raising when K < m,
                  P

says that the selected infinitesimal neighborhoods impose independent conditions on H m .
Dually, their osculating blocks form a direct sum of dimension i λd (ai ). Each block lies in
                                                              P

SZ because ai ≤ s and Z is order-s absorbing.

Lemma 4.3 (Discrete convex packing). If 1 ≤ wi ≤ s + 1 and                      i wi ≤ m + 1, then
                                                                                P


                                 X d + wi − 1
                                                          !
                                                              ≤ Bd,s (m).
                                   i
                                                  d

Equality is attained by q weights s + 1 and, if r > 0, one weight r.

Proof. Put f (0) = 0 and f (w) = d+w−1 for w ≥ 1. Its forward differences
                                              
                                   d

                                                                d+w−1
                                                                            !
                               f (w + 1) − f (w) =
                                                                 d−1

are nondecreasing for w ≥ 1, while f (1) − f (0) = 1. Moving one unit from a smaller block to
a larger block below the cap s + 1 does not decrease the total; a weight-one block disappears
when it loses its unit. Repetition packs the budget into full blocks and at most one residual
block. If the original total weight is smaller than m + 1, first enlarge a nonfull block or append
a weight-one block; either operation strictly increases the objective. Thus an optimum uses
the whole budget, and the packed pattern gives (1).




                                                      5
Proof of Theorem 4.1. Put n = |Z|. If r = 0 and q = 1, nonemptiness gives n ≥ 1 = q.
Now suppose r = 0, q ≥ 2, and n ≤ q − 1. Then n ≥ 1, and the union of the full order-s
neighborhoods at all supports is independent in degree

                             (s + 1)n − 1 ≤ (s + 1)(q − 1) − 1 < m

by Lemma 3.3, and remains so after raising degree to m. Its dual has dimension nλd (s) and
lies in SZ by absorption. This contradicts dim SZ ≤ n, since λd (s) > 1. Hence n ≥ q.
    If r > 0 and n ≤ q, the same contradiction applies because

                           (s + 1)n − 1 ≤ q(s + 1) − 1 = m − r < m.

Thus n ≥ q + 1.
   Choose q supports with full order-s blocks and, if r > 0, one further support with an
order-(r − 1) block. Their mixed interpolation degree is

                                      q(s + 1) + r − 1 = m.

Their independent dual spaces lie in SZ and have total dimension Bd,s (m). Therefore dim SZ ≥
Bd,s (m), and |Z| ≥ dim SZ because SZ is generated by |Z| value lines.

    The certificate and packing argument do not intrinsically require a tensor power. The
following form records the more general input precisely.
Corollary 4.4 (Jet-ample polarization). Let L be an M -jet ample line bundle on X, meaning
that for every set of distinct points pi and positive integers bi with i bi = M +1, the restriction
                                                                            P

map
                                  H 0 (X, L) −→      H 0 (bi pi , L|bi pi )
                                                 M

                                                i
is surjective. Fix 1 ≤ s ≤ M , write M + 1 = Q(s + 1) + R with 0 ≤ R ≤ s, and define SZ and
the osculating spaces using L in place of H m . If a nonempty finite reduced set Z is point-span
s-osculating-absorbing, then

                                            d+s   d+R−1
                                                    !                 !
                           dim SZ , |Z| ≥ Q     +       ,
                                             d      d

where the last summand is interpreted as zero when R = 0. Over the complex numbers, repeated
application of [4, Proposition 2.3] gives this conclusion with M = ℓa for L = Aℓ whenever A is
a-jet ample and 1 ≤ s ≤ ℓa. Here a ≥ 1 and ℓ ≥ 1 are integers.
Proof. The stated jet-ampleness also gives surjectivity when i bi < M + 1: add one point
                                                                  P

outside the selected finite set with the missing positive weight, and then project away its jet
target. Such a point exists because d ≥ 1 and the algebraically closed field is infinite. Thus
every selected collection with bi = ai + 1 ≤ s + 1 and total weight at most M + 1 is independent.
The support-threshold proof above applies verbatim with M in place of m, including the
separate case Q = 1, R = 0. Selecting Q full blocks and, when R > 0, one residual block gives
the displayed rank. The last assertion is the tensor-product theorem cited above, iterated ℓ − 1
times.


5    Characteristic-free unisolvent supports
Lemma 5.1 (Existence of an evaluation basis). For every algebraically closed field and every
d, m ≥ 1, there is a set of Nd,m distinct points Z ⊂ Pd such that evaluation is an isomorphism
                                                ∼
                              H 0 (Pd , O(m)) −−→ H 0 (Z, OZ (m)).

                                                6
Proof. The evaluation lines of all k-points span H 0 (Pd , O(m))∗ . Otherwise their annihilator
would contain a nonzero homogeneous degree-m form vanishing at every k-point of Pd ,
which is impossible over the infinite field k. Select a basis from these evaluation lines. Very
ampleness separates points, so their Nd,m supports are distinct; dualizing gives the displayed
isomorphism.

   This existence proof replaces the integer simplex lattice used in version one. That lattice
remains a useful characteristic-zero fixture, but its points can collide and its falling-factorial
basis can degenerate when the characteristic is at most m.


6    Smooth higher-contact extremizers
Let W = V (y) ∼
              = Pd be a hyperplane in Pd+1 and let Z ⊂ W be an unisolvent set from
                                                                                W,p ;
Lemma 5.1. Write (s + 1)ZW for the disjoint union of the subschemes defined by ms+1
equivalently,
                               I(s+1)ZW =     ms+1
                                           \
                                                W,p .
                                                    p∈Z

This is a fat-point or symbolic-power ideal sheaf, not an assertion about the ordinary power of
the homogeneous ideal of Z.

Proposition 6.1 (Smooth prescribed higher contact). Put N = Nd,m and E = (s + 1)N . For
every n ≥ E + 1, there is a smooth integral degree-n hypersurface X ⊂ Pd+1 containing Z such
that
                                    y ∈ ms+1
                                          X,p      (p ∈ Z).
In particular W is the tangent hyperplane at every support and has contact through order s
there.

Proof. Set
                                   V = H 0 W, I(s+1)ZW (n) .
                                                               

We first choose f ∈ V whose zero divisor is smooth on W \ Z. Fix q ∈ W \ Z. For every p ∈ Z,
choose a hyperplane ℓp,q through p and not through q, and put

                                         Aq =
                                                Y
                                                      ℓs+1
                                                       p,q .
                                                p∈Z

Then Aq has degree E, belongs to H 0 (W, I(s+1)ZW (E)), and is a unit on the first neighbourhood
2q. Since n − E ≥ 1, OW (n − E) generates all first jets at q. Multiplication by Aq |2q therefore
proves that
                                   V −→ H 0 (2q, O2q (n))
is surjective.
    Consider the incidence

                         Σ1 = {(q, [f ]) ∈ (W \ Z) × P(V ) : jq1 f = 0}.

For fixed q, vanishing of the first jet has codimension d + 1; hence

                      dim Σ1 ≤ d + dim P(V ) − (d + 1) = dim P(V ) − 1.

The closure of its image cannot fill P(V ). Choose f outside that closure. Then V (f ) is smooth
at every one of its points outside Z. This is an incidence calculation with local jets, so no
Euler identity, ordinary derivative convention, or characteristic restriction is involved.


                                                7
   Fix such an f and let

                    U = H 0 (Pd+1 , O(n − 1)),       FG = f + yG       (G ∈ U ).

On the open set y ̸= 0, multiplication by y is an isomorphism on first neighbourhoods. Since
n − 1 ≥ 1, the affine map

                         U −→ H 0 (2q, O2q (n)),      G 7−→ jq1 (f + yG)

is surjective for every such q. The condition that FG be singular at a fixed point of the
(d + 1)-dimensional ambient open set has codimension d + 2. Thus

                               Σ2 = {(q, G) : y(q) ̸= 0, jq1 FG = 0}

has dimension at most (d + 1) + dim U − (d + 2) = dim U − 1. The closure of its image is
therefore a proper closed subset of U . The additional conditions G(p) ̸= 0, p ∈ Z, are the
complements of finitely many hyperplanes in the irreducible affine space U . Choose G outside
the closure of the incidence image and outside all those hyperplanes.
     Let X = V (FG ). It is smooth on y ̸= 0 by the second incidence. If q ∈ W \ Z lies on X,
then f (q) = 0 and the tangential first jet of f is nonzero, so X is smooth at q. At p ∈ Z, all
first jets of f vanish and the normal first jet of FG is G(p) ̸= 0, so X is smooth there as well.
    The hypersurface is connected. Indeed, from

                          0 −→ OPd+1 (−n) −→ OPd+1 −→ OX −→ 0

and H 1 (Pd+1 , O(−n)) = 0 for d + 1 ≥ 2, one gets H 0 (X, OX ) = k. A smooth scheme has
disjoint irreducible components; connectedness therefore makes X integral.
    Finally, regard f as its lift independent of y. Since that lift belongs to ms+1
                                                                                Pd+1 ,p
                                                                                        , its image
            X,p . In OX,p the germ of G is a unit and
belongs to ms+1

                                       y = −f /G ∈ ms+1
                                                    X,p ,

which proves the required contact.

Proof of Theorem 1.4. Choose Z ⊂ W by Lemma 5.1, take n ≥ (s + 1)Nd,m + 1, and choose
X by Proposition 6.1. In particular n > m. The hypersurface sequence twisted by m, together
with
                 H 0 (Pd+1 , O(m − n)) = 0,     H 1 (Pd+1 , O(m − n)) = 0,
gives an isomorphism
                                                 ∼
                             H 0 (Pd+1 , O(m)) −−→ H 0 (X, OX (m)).                             (2)
    Let a section on the right vanish on Z and denote its unique ambient lift by Q. Its
restriction Q|W is a degree-m form vanishing at the unisolvent set Z, hence Q|W = 0. Thus
Q = yR for a degree-(m − 1) form R. Proposition 6.1 gives

                                   Q = yR ∈ ms+1
                                             X,p       (p ∈ Z).

Therefore
                       H 0 (X, IZ ⊗ OX (m)) = H 0 (X, I(s+1)Z ⊗ OX (m)),
and Lemma 2.1 proves order-s absorption.
   Unisolvence gives dim SZ = |Z| = Nd,m . Equation (2) gives

                                                 d+m+1
                                                            !
                            h (X, OX (m)) =
                               0
                                                                > Nd,m ,
                                                  d+1
so the point span is proper.

                                                 8
Corollary 6.2 (Exact universal minimum). For every algebraically closed field and every
d, m ≥ 1, 1 ≤ s ≤ m, the minimum possible cardinality and span dimension of a point-span
s-osculating-absorbing set, as (X, H, Z) vary under the standing hypotheses, are both Nd,m .
The minimum remains the same after requiring the point span to be proper.

Proof. The lower bound is Theorem 1.2; the proper-span equality examples are Theorem 1.4.


    The degree n ≥ (s + 1)Nd,m + 1 is a transparent sufficient threshold, not a minimality
claim. The proof certifies an open set of choices rather than one distinguished equation.


7     Exact computational witnesses
The accompanying replay uses exact rational and finite-field linear algebra. It checks the
original mixed-block identities, the new rank-sensitive formula and its P1 falsification boundary,
unisolvent evaluation sets in several small characteristics, and local fixtures in which the normal
coordinate lies in ms+1 . Fresh JSON output is compared byte for byte with the committed
result. These are finite diagnostic witnesses: they do not prove the incidence dimension counts,
smoothness of a general member, the universal rank theorem, or priority.


8     Context and limitations
Jet ampleness encodes simultaneous interpolation on fat points. A tensor-product generation
result over the complex numbers appears in [4]. Higher osculating spaces and fundamental
forms are formulated through principal-parts sheaves over algebraically closed fields in [8]; that
is the intrinsic language used here.
    Ballico’s X-rank of a linear subspace is the direct established language for the minimum
number of points of X whose span contains a prescribed linear space [3]. That work computes
ranks of tangent-containing subspaces for rational normal curves and several Veronese con-
figurations. The present condition is simultaneous and self-referential: one reduced set must
absorb the order-s osculating space at every one of its own supports. We do not claim to
introduce subspace rank or point-span absorption as a general concept.
    Osculating spaces, higher Gauss maps, and secant varieties have a substantial literature
[1, 2, 5]. The Veronese literature relates osculating secant defectivity to Hilbert functions of
fat points. Those questions differ from proper-span equality for simultaneous absorption, but
they delimit the novelty claim. This selective comparison is not a priority certification.
    The authorial note B215 contains the order-two mixed interpolation pattern [7]; it is
an antecedent, not independent validation. Version one of this ARR record extracted that
certificate and optimized its packing formula. The later exact tangent theorem [6] made
that numerical floor nonoptimal for tensor powers. This major revision records the corrected
hierarchy rather than concealing the chronology.
    The limitations are material.

    • The higher-order absorption hypothesis is explicit. Tangent absorption alone is not
      claimed to imply second- or higher-order absorption.

    • The restriction s ≤ m ensures the full local rank in Lemma 3.1. No formula for s > m is
      asserted.

    • Completeness of the H m system is used because all separator products must be available.
      Arbitrary subsystems are outside the theorem.



                                                9
    • The higher-block term requires m ≥ 2s + 1. The curve counterexample shows this
      threshold is necessary for that uniform formula, but no optimal replacement is claimed
      below the threshold.

    • The extremizers prove existence at the sufficient hypersurface degree n ≥ (s + 1)Nd,m + 1.
      They neither minimize n, classify equality sets, nor provide one canonical equation.

    • The exact floor is invoked from a separate, earlier ARR record. The proper-span
      construction and higher-block proof are given here in full.

    • The literature search is selective. The replay is not a proof checker, and no independent
      human peer review or exhaustive priority review is claimed.


9     Conclusion
Higher-osculating absorption has the same exact universal binomial floor as tangent absorption,
but the stronger condition is not geometrically empty. Arbitrary-characteristic hypersurfaces
with prescribed order-(s + 1) normal contact realize the floor with a proper point span in
every dimension, degree, and allowed osculating order. Away from that high-contact branch,
the rank-sensitive block argument forces λd (s)r1 (Z) independent conditions once m ≥ 2s + 1.
The mixed-jet certificate remains useful for abstract jet-ample polarizations, while its older
tensor-power floor is now explicitly subordinate to the exact theorem. Minimal construction
degree, equality classification, and stronger bounds below the block threshold remain open.


References
 [1] E. Ballico, C. Bocci, E. Carlini, and C. Fontanari, Osculating spaces to secant varieties,
     arXiv:math/0406322 (2004). https://arxiv.org/abs/math/0406322
 [2] E. Ballico and C. Fontanari, On the osculatory behaviour of higher dimensional projective varieties,
     arXiv:math/0406319 (2004). https://arxiv.org/abs/math/0406319
 [3] E. Ballico, On the X-rank of linear subspaces, Rev. Roumaine Math. Pures Appl. 58 (2013),
     437–451. https://imar.ro/journals/Revue_Mathematique/pdfs/2013/4/4.pdf
 [4] M. C. Beltrametti, S. Di Rocco, and A. J. Sommese, On generation of jets for vector bundles, Rev.
     Mat. Complut. 12 (1999), 27–45. https://doi.org/10.5209/rev_REMA.1999.v12.n1.17182
 [5] A. Bernardi, M. V. Catalisano, A. Gimigliano, and M. Idà, Secant varieties to osculating varieties
     of Veronese embeddings of Pn , J. Algebra 321 (2009), 982–1004. https://doi.org/10.1016/j.
     jalgebra.2008.10.020
 [6] L. Eriksson, The exact rank floor for point-span tangent absorption in arbitrary characteris-
     tic, ARR-2026-2MHNZRRJP49Y9SWP, v3 (2026). https://arr-research.github.io/papers/
     ARR-2026-2MHNZRRJP49Y9SWP/versions/v3/
 [7] L. Eriksson, B215—Simultaneous second-jet interpolation raises the floor, public working note
     (2026), repository record B215.
 [8] R. Mallavibarrena and R. Piene, On fundamental forms and osculating bundles, Rend. Istit. Mat.
     Univ. Trieste 56 (2024), Art. 9, 21 pp. https://doi.org/10.13137/2464-8728/36877




                                                  10
