                   Mixed-Jet Rank Floors for Point-Span
                      Higher Osculating Absorption
                                           Lluis Eriksson
                                        Independent researcher

                                August 24, 2026 (version 0.2)


                                              Abstract
         Let X be a smooth projective integral d-fold over an algebraically closed field, let H be
     very ample, and use the complete embedding defined by H m . Fix 1 ≤ s ≤ m. A nonempty
     finite reduced set Z ⊂ X is point-span s-osculating-absorbing if the span SZ of its value
     evaluations contains the affine osculating space of order s at every support. Write

                                m + 1 = q(s + 1) + r,       0 ≤ r ≤ s,

     and put
                                               (
                                          d+s     0,      r = 0,
                                          
                             Bd,s (m) = q      + d+r−1
                                           d         d  , r > 0.
     We prove in arbitrary characteristic that

                                        dim SZ , |Z| ≥ Bd,s (m).

     The proof is scheme-theoretic. Products of point separators isolate arbitrary mixed jets
     of total weight at most m + 1, and discrete convexity selects full order-s blocks plus
     one residual block. The resulting heterogeneous rank certificate also applies to arbitrary
     jet-ample polarizations. For s = 1 the formula recovers the earlier growing first-jet bound.
     Equality holds in every characteristic on rational normal curves, for every s, and on Pd in
     the top-order regime s = m. No implication from tangent absorption to the higher-order
     hypothesis is used or claimed. No classification or exhaustive priority claim is made.


1    Statement and scope
Let k be algebraically closed, let X be smooth, projective, integral, and of dimension d ≥ 1,
and let H be very ample. Write

                                   φm : X −→ P(H 0 (X, H m )∗ )

for the complete embedding. For a nonempty finite reduced set Z ⊂ X, set
                                                                         
                          SZ = Im H 0 (Z, H m |Z )∗ −→ H 0 (X, H m )∗ .

Equivalently, SZ is the span of the evaluation lines at the supports; this formulation makes no
choice of fiber trivializations. For p ∈ X and a ≥ 0, put

                                                                         d+a
                                                                              !

                                              p ),
                       (a + 1)p = Spec(OX,p /ma+1            λd (a) =        ,
                                                                          d

and set λd (−1) = 0.

                                                   1
    The order-a principal-parts evaluation is
                                                                               
                           jpa : H 0 (X, H m ) −→ H 0 (a + 1)p, H m |(a+1)p .

We define the affine order-a osculating space intrinsically by
                                    a
                                d (H m ) = Im((j a )∗ ) ⊂ H 0 (X, H m )∗ .
                                Oscp            p

This convention uses no ordinary derivatives or factorials.

Definition 1.1. Fix 1 ≤ s ≤ m. The set Z is point-span s-osculating-absorbing for H m if
                                             s
                                        d (H m ) ⊆ SZ
                                        Oscp                     (p ∈ Z).

    Write uniquely
                            m + 1 = q(s + 1) + r,            q ≥ 1,     0 ≤ r ≤ s,
and define
                                     Bd,s (m) = qλd (s) + λd (r − 1).                        (1)

Theorem 1.2 (Universal mixed-jet floor). Over an algebraically closed field of arbitrary
characteristic, every nonempty finite reduced point-span s-osculating-absorbing set for the
complete H m -embedding satisfies

                                dim SZ ≥ Bd,s (m),           |Z| ≥ Bd,s (m).

Corollary 1.3 (First-order specialization). For s = 1,

                                       m+1           1,
                                                                  (
                                                                         m even,
                                                    
                            Bd,1 (m) =     (d + 1) +
                                        2            0,                  m odd.

Thus the formula recovers the growing first-jet bound of [5].

    For fixed d, s,
                                            1  d+s
                                                             !
                                Bd,s (m) =         m + Od,s (1).
                                           s+1  d
For d ≥ 2 the leading coefficient strictly increases with s, because
                                     d+s+1
                                            /(s + 2)   d+s+1
                                       d
                                                     =       > 1.
                                      d+s
                                       d /(s + 1)
                                                        s+2

The hierarchy is therefore asymptotically stronger under the correspondingly stronger osculating
hypothesis.


2     The annihilator criterion
Let (s + 1)Z =        p∈Z (s + 1)p. Finite-scheme duality gives
                 `


                                             SZ⊥ = H 0 (X, IZ ⊗ H m )

and                                              ⊥
                                         s
                                    d (H m ) = H 0 (X, I
                                    Osc                  (s+1)Z ⊗ H ).
                                X
                                                                   m
                                       p
                            
                              p∈Z


                                                         2
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


3    Mixed-jet interpolation
Lemma 3.1 (Full jets from powers). If p ∈ X and 0 ≤ a ≤ k, then
                                                                          
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
Lemma 3.2 (Mixed-jet interpolation). Let t ≥ 1, let p1 , . . . , pt be distinct points, let ai ≥ 0,
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
                                           Pi =            ℓij   .
                                                   j̸=i

It is a unit at pi and vanishes to the prescribed order at every other support. Lemma 3.1
realizes arbitrary order-ai data using H ai . Multiplication by the unit Pi is an automorphism
of the truncated local algebra, so degree-K sections realize arbitrary data at pi and zero data
elsewhere. Sum over i.
    For k > K, multiply by a section of H k−K nonzero at every support. It exists because k is
infinite and a finite union of proper linear subspaces cannot exhaust the section space.
    Over the complex numbers this is also the line-bundle specialization of [3, Proposition 2.3].
The direct proof records the exact specialization and is characteristic-free. The interpolation
statement itself is not claimed as new; the point here is its rank consequence under the
absorption constraint and the ensuing optimization.

                                                       3
4      Convex packing and the rank proof
The interpolation lemma first gives a heterogeneous certificate, before optimization.
Proposition 4.1 (Mixed-block rank certificate). Under the hypotheses of Theorem 1.2, choose
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

Proof. Put K = i (ai + 1) − 1 ≤ m. Lemma 3.2, followed by degree raising when K < m,
                  P

says that the selected infinitesimal neighborhoods impose independent conditions on H m .
Dually, their osculating blocks form a direct sum of dimension i λd (ai ). Each block lies in
                                                              P

SZ because ai ≤ s and Z is order-s absorbing.

Lemma 4.2 (Discrete convex packing). If 1 ≤ wi ≤ s + 1 and                     i wi ≤ m + 1, then
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

Proof of Theorem 1.2. Put n = |Z|. If r = 0 and q = 1, nonemptiness gives n ≥ 1 = q.
Now suppose r = 0, q ≥ 2, and n ≤ q − 1. Then n ≥ 1, and the union of the full order-s
neighborhoods at all supports is independent in degree
                             (s + 1)n − 1 ≤ (s + 1)(q − 1) − 1 < m
by Lemma 3.2, and remains so after raising degree to m. Its dual has dimension nλd (s) and
lies in SZ by absorption. This contradicts dim SZ ≤ n, since λd (s) > 1. Hence n ≥ q.
    If r > 0 and n ≤ q, the same contradiction applies because
                           (s + 1)n − 1 ≤ q(s + 1) − 1 = m − r < m.
Thus n ≥ q + 1.
   Choose q supports with full order-s blocks and, if r > 0, one further support with an
order-(r − 1) block. Their mixed interpolation degree is
                                       q(s + 1) + r − 1 = m.
Their independent dual spaces lie in SZ and have total dimension Bd,s (m). Therefore dim SZ ≥
Bd,s (m), and |Z| ≥ dim SZ because SZ is generated by |Z| value lines.

                                                     4
    The certificate and packing argument do not intrinsically require a tensor power. The
following form records the more general input precisely.

Corollary 4.3 (Jet-ample polarization). Let L be an M -jet ample line bundle on X, meaning
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
application of [3, Proposition 2.3] gives this conclusion with M = ℓa for L = Aℓ whenever A is
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

Proof of Corollary 1.3. Divide m + 1 by two. An odd m has no residual block; an even m has
one residual simple value. Substitution in (1) gives the formula.


5    Sharpness on the rational normal curve
Theorem 5.1 (Exact curve minimum). Let X = P1 , H = OP1 (1), and 1 ≤ s ≤ m. The
minimum size and minimum span dimension of a point-span s-osculating-absorbing set for the
complete mth Veronese embedding are both m + 1.

Proof. Since λ1 (a) = a + 1, Theorem 1.2 gives B1,s (m) = q(s + 1) + r = m + 1.
   Conversely, choose any m + 1 distinct points Z ⊂ P1 . A nonzero binary form of degree m
cannot vanish at all of them, so evaluation

                               H 0 (P1 , O(m)) −→ H 0 (Z, OZ (m))

is an isomorphism. Hence SZ = H 0 (P1 , O(m))∗ , which contains every osculating space, and
dim SZ = |Z| = m + 1.

    There is a second exact regime in every dimension.

Theorem 5.2 (Exact top-order minimum). Let X = Pd , H = OPd (1), and s = m ≥ 1. The
minimumsize and minimum span dimension of a point-span m-osculating-absorbing set are
both d+m
      d , over every algebraically closed field.




                                                5
Proof. Theorem 1.2 gives the lower bound because q = 1, r = 0, and Bd,m (m) = λd (m) = d+m  d .
                                                                                                   

Conversely, the evaluation lines of all closed points of P span H (P , O(m)) : their annihilator
                                                          d      0  d       ∗

would otherwise contain a nonzero homogeneous form vanishing identically on        Pd . Select a
                                                                           d+m
basis of evaluation lines and let Z be its supports. Then |Z| = dim SZ = d and SZ is the
whole dual space, so it contains every order-m osculating space.

    The exact replay uses rational Vandermonde matrices for (m, s) = (3, 1), (5, 2), (8, 3), (10, 5).
It also exhaustively checks 250 finite convex-packing cases and two simplex-lattice fixtures in
the top-order regime. These computations certify only the displayed finite fixtures and integer
identities, not the universal theorem or priority.


6     Context and limitations
Jet ampleness encodes simultaneous interpolation on fat points. A tensor-product generation
result over the complex numbers appears in [3]. Higher osculating spaces and fundamental
forms are formulated through principal-parts sheaves over algebraically closed fields in [7]; that
is the intrinsic language used here.
    Osculating spaces, higher Gauss maps, and secant varieties have a substantial literature
[1, 2, 4]. The Veronese literature in particular relates osculating secant defectivity to Hilbert
functions of fat points. These works provide context; this selective comparison does not
establish priority for the value-span absorption floor (1).
    The authorial note B215 contains the order-two mixed interpolation pattern [6]. It is
an antecedent, not independent validation. The present argument removes its unrelated
conditional framework, states the arbitrary-order absorption hypothesis, works in arbitrary
characteristic, optimizes the closed formula, and proves curve sharpness.
    The limitations are material.
    • The higher-order absorption hypothesis is explicit. No implication from first-order
      tangent absorption to second- or higher-order absorption is asserted or used.
    • The restriction s ≤ m ensures the full local rank in Lemma 3.1. No formula for s > m is
      asserted.
    • Completeness of the H m system is used because all separator products must be available.
      Arbitrary subsystems are outside the theorem.
    • Equality is settled for the numerical minimum in dimension one and for s = m on
      projective space. No equality classification in the remaining higher-dimensional regimes
      is claimed; in particular, no nontrivial sharpness example is supplied here for d ≥ 2 and
      s < m.
    • The literature search is selective, the replay is not a proof checker, and no independent
      human peer review has yet been performed.


7     Conclusion
Once the higher-order hypothesis is stated explicitly, point-span osculating absorption has a
uniform characteristic-free rank consequence. Very ampleness isolates mixed fat-point blocks
of total weight at most m + 1, and convex packing gives the explicit floor Bd,s (m). The
same certificate yields a bound for arbitrary jet-ample polarizations. The first-order result is
recovered exactly, while the full hierarchy is sharp on rational normal curves and the top-order
endpoint is sharp on projective space in every dimension. Equality away from these regimes
and the geometry of special higher Gauss fibers remain open.

                                                 6
References
[1] E. Ballico, C. Bocci, E. Carlini, and C. Fontanari, Osculating spaces to secant varieties,
    arXiv:math/0406322 (2004). https://arxiv.org/abs/math/0406322
[2] E. Ballico and C. Fontanari, On the osculatory behaviour of higher dimensional projective varieties,
    arXiv:math/0406319 (2004). https://arxiv.org/abs/math/0406319
[3] M. C. Beltrametti, S. Di Rocco, and A. J. Sommese, On generation of jets for vector bundles, Rev.
    Mat. Complut. 12 (1999), 27–45. https://doi.org/10.5209/rev_REMA.1999.v12.n1.17182
[4] A. Bernardi, M. V. Catalisano, A. Gimigliano, and M. Idà, Secant varieties to osculating varieties
    of Veronese embeddings of Pn , J. Algebra 321 (2009), 982–1004. https://doi.org/10.1016/j.
    jalgebra.2008.10.020
[5] L. Eriksson, Characteristic-Free Bounds and Sharp Gauss-Fiber Examples for Point-Span Tangent
    Absorption, ARR-2026-19BXX42GM38K6VZ3, v1 (2026). https://arr-research.github.io/
    papers/ARR-2026-19BXX42GM38K6VZ3/
[6] L. Eriksson, B215—Simultaneous second-jet interpolation raises the floor, public working note
    (2026), repository record B215.
[7] R. Mallavibarrena and R. Piene, On fundamental forms and osculating bundles, Rend. Istit. Mat.
    Univ. Trieste 56 (2024), Art. 9, 21 pp. https://doi.org/10.13137/2464-8728/36877




                                                  7
