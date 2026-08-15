# Exact Branch Rigidity and Unique Crossing in Grassmann Matrix--Bingham Free Energies: Finite Certification, All-Field Gr_C(3,6) and Gr_C(4,8) Two-Block Order, and a Gr_C(2,5) Exchange Theorem

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
Exact Branch Rigidity and Unique Crossing in
      Grassmann Matrix–Bingham Free Energies
Finite Certification, All-Field GrC (3, 6) and GrC (4, 8) Two-Block Order, and a
                          GrC (2, 5) Exchange Theorem

                                            Lluis Eriksson

                                           August 15, 2026


                                                Abstract
         Let P be a Haar-distributed complex Grassmann projector and consider the matrix–
     Bingham normalizer ZA (s) = E exp{s tr(AP )} on the trace-zero, Frobenius-unit external
     sphere. We determine several exact, complementary pieces of its finite-dimensional branch
     geometry. On every half Grassmannian GrC (r, 2r), the balanced rank-r two-block field
     strictly maximizes the normalized two-block moments of degrees 4, 6, 8, and 10. The
     differences factor through the squared multiplicity defect (r − k)2 and admit explicit positive-
     coefficient certificates. Together with a matrix-beta endpoint calculation, this proves
     balanced dominance at both small and large field for every rank and confines any violation
     of the all-field conjecture to an intermediate-field reentrant island.
         At GrC (3, 6), the first half rank beyond the exceptional GrC (2, 4) model [5], we close
     that two-block gate for every field. Andreief’s identity reduces the three normalizers to
     elementary Hankel determinants, and an all-degree coefficient argument proves strict Laplace
     order of the balanced 3 + 3 spectrum over the 1 + 5 and 2 + 4 spectra. Combined with an
     exact Jacobi–Stein Hessian identity, the two losing branches have an unstable larger-block
     split at every nonzero field, whereas the balanced branch is Morse–Bott stable. We then
     prove a fixed-rank finite certification theorem: an explicit event inside the uniform Hermitian
     matrix cube controls every sufficiently high moment, giving a finite sufficient certificate for
     coefficientwise two-block order, and hence for all-field order, at each fixed rank. At GrC (4, 8),
     exact Hankel arithmetic through degree 268 plus this analytic tail closes all remaining degrees
     and closes another half-rank case here. Away from half rank the geometry changes: on
     GrC (2, 5) the one-spike and rank-two canonical branches exchange dominance exactly once.
     We derive their compactly supported piecewise-polynomial
                                                  √                    densities, certify four density
     sign changes by Sturm arithmetic over Q( 6), and use strict total positivity of the Laplace
     kernel to prove that the crossing is unique and simple. A second exact sign-change argument
     proves that both positive orientations dominate their negative counterparts, closing the
     complete oriented two-level family.
         These results concern the complete canonical two-block family. We do not prove that an
     arbitrary multi-level external spectrum is globally dominated, and therefore do not claim an
     unrestricted all-distortion rate–distortion function. That boundary is stated as part of the
     theorem ledger.


1    Introduction
For a Haar rank-r projector P on Cd , the orbital Laplace transform

                ZA (s) = E exp{s tr(AP )},          A = A∗ ,     tr A = 0,    ∥A∥F = 1,                   (1.1)

is simultaneously a unitary orbital integral, a hypergeometric function of matrix argument,
and the normalizer of a matrix–Bingham exponential family [9, 15, 12, 8]. Its evaluation


                                                     1
```

---

## Page 2

```text
and asymptotic analysis are classical problems, including recent complete high-dimensional
normalizer expansions [2]. The extremal problem in the external spectrum is more delicate:
trace and Frobenius constraints do not place the candidate spectra on a majorization chain, so
standard Schur convexity does not choose a maximizer [17, 13, 14].
    This distinction matters in information theory. An external-spectrum theorem can collapse
a Gibbs dual for calibrated Born-probability prediction to a scalar optimization, but only after
global optimality over all spectra and posterior-mean feasibility have been established. Complete
results are known for the exceptional half rank GrC (2, 4) and on a high-fidelity segment at
arbitrary rank [5, 3]. The preceding paper in this sequence proved all-field local Morse–Bott
stability of the balanced half-Grassmann branch, as well as exact metastability thresholds for
unbalanced two-block branches [4]. Local stability, however, cannot compare separated values
and cannot exclude a first-order exchange.
    Here we attack the separated-value problem within the complete canonical two-block family.
The unifying tools are finite-dimensional determinantal representations and oscillation control.
Schur–Weyl moment identities yield positive polynomial certificates through degree ten at
every half rank. At r = 3, the first half rank beyond the exceptional GrC (2, 4) theorem of [5],
matrix-beta compression and Andreief’s identity turn the entire Taylor series into three explicit
Hankel determinants; a discrete variation argument proves coefficientwise order in every even
degree. Off half rank, density sign changes become the useful invariant: a Sturm certificate and
the variation-diminishing property of esy prove a unique canonical exchange on GrC (2, 5).
    The main results are:
    (i) strict balanced two-block moment order in degrees 4, 6, 8, 10 for every GrC (r, 2r), with
        exact positive-coefficient certificates;

 (ii) exact small- and large-field balanced barriers at every half rank;

(iii) strict all-field, all-degree two-block Laplace order on GrC (3, 6);

 (iv) an all-field local-maximizer classification of its three two-block critical orbits;

 (v) a finite exact certificate theorem at every fixed half rank, closed in full on GrC (4, 8) by
     rational Hankel arithmetic and an analytic tail; and

 (vi) a unique and simple canonical branch crossing on GrC (2, 5), proved by exact densities,
      Sturm theory, and strict total positivity.
No numerical optimizer is used in a theorem. The accompanying scripts replay the displayed
symbolic identities and exact root counts; the induction and oscillation arguments are contained
in the paper.
     A targeted primary-literature search found no prior theorem giving the coefficientwise all-
field comparisons across every two-level multiplicity on GrC (3, 6) or GrC (4, 8), nor the complete
oriented two-level exchange on GrC (2, 5). This is not a claim of exhaustive priority. Jacobi
trace laws, Hankel representations, matrix–Bingham normalizers, and total-positivity theory are
established ingredients; novelty is claimed only for the normalized cross-multiplicity comparisons,
the finite sufficient tail architecture, and the exact crossing count.


2     Canonical two-block fields and matrix-beta compression
Let P be Haar on GrC (r, d), represented by its rank-r orthogonal projector. For 1 ≤ k ≤ d−1, fix
a rank-k projector Ek . The trace-zero, Frobenius-unit two-block field with positive multiplicity
k is                               s              s
                                      d−k               k
                           Ad,k =          Ek −              (I − Ek ).                     (2.1)
                                       dk           d(d − k)

                                                 2
```

---

## Page 3

```text
Its statistic is an affine rescaling of the principal overlap Tk = tr(Ek P ):
                                                    s
                                                           d          kr
                                                                                 
                                  tr(Ad,k P ) =                  Tk −    .                            (2.2)
                                                        k(d − k)      d

When d = 2r, complementation makes this law symmetric. It is convenient to write
                                                    s
                           k                               2r
                  Yk = Tk − ,           Xk =                      Yk ,           Zr,k (s) = EesXk .   (2.3)
                           2                            k(2r − k)

The common quadratic moment follows from unitary isotropy:
                                                                r
                                              EXk2 =                    ,                             (2.4)
                                                          2(4r2 − 1)

independent of k.
   For k ≤ r, the nonzero eigenvalues of Ek P Ek have the complex matrix-beta law Bk (r, r).
Finite Jacobi-trace densities and their Fourier–Laplace recurrences are classical [7]. With
Hk = 2Ek P Ek − Ik , the eigenvalue density is proportional to

                          Y                   k
                                              Y
                                (xi − xj )2       (1 − x2i )r−k ,           −1 < xi < 1.              (2.5)
                          i<j                 i=1

Thus the two-block problem is a dimension-shift comparison between Jacobi trace laws. Equiv-
alently, at k = r, Hr is uniform on the Hermitian matrix interval −I < H < I, and every
smaller-k branch is a normalized coordinate compression of this matrix-cube law.


3     All-rank rigidity through degree ten
Put
                                     q = k(2r − k),             q0 = 2r − 1.                          (3.1)
Then q0 ≤ q ≤ r2 , and

                       r2 − q = (r − k)2 ,              q − q0 = (k − 1)(2r − k − 1).                 (3.2)

For m ≥ 0, the raw moments of Tk admit the Schur–Weyl expression
                                                    X                          (r)λ
                                   ETkm =                      f λ sλ (1k )         .                 (3.3)
                                                  λ⊢m
                                                                              (2r)λ
                                              ℓ(λ)≤min(k,r)


Here f λ = m!/ u∈λ h(u), sλ (1k ) = u∈λ (k + c(u))/h(u), and (a)λ = i (a − i + 1)λi . Formula
                Q                        Q                                                Q

(3.3) follows by expanding (tr Ek P )m , applying Schur–Weyl duality, and integrating the unitary
representation matrix coefficients; it is also the standard matrix-beta moment formula [9, 15].
    Define the balanced gap
                                  ∆2m (r, k) = EXr2m − EXk2m .                              (3.4)

Theorem 3.1 (Universal moment order through degree ten). For every r ≥ 2, every 1 ≤ k < r,
and m = 2, 3, 4, 5,
                                   ∆2m (r, k) > 0.                                   (3.5)
In particular, the balanced multiplicity uniquely maximizes the fourth, sixth, eighth, and tenth
normalized moments throughout the canonical two-block family.


                                                           3
```

---

## Page 4

```text
Proof. Center (3.3), rescale by (2.3), and collect in the single invariant q = k(2r − k). For
degree four one obtains

                                               3(r2 − q)
                            ∆4 =                                      .                         (3.6)
                                   2q(2r − 3)(2r − 1)(2r + 1)(2r + 3)

For degree six, set
                          N6 (r, q) = (12r4 − 27r2 + 8)q − 32r4 + 8r2 ,
                               D6 = (2r − 5)(2r − 3)(2r − 1)2 (2r + 1)2                         (3.7)
                                        × (2r + 3)(2r + 5).
For r ≥ 3,
                                            15(r2 − q)N6 (r, q)
                                     ∆6 =                       .                               (3.8)
                                                 4q 2 rD6
The coefficient of q is positive, and at q = q0 the resulting polynomial, after r = y + 3, is

                      24y 5 + 316y 4 + 1578y 3 + 3653y 2 + 3736y + 1165 > 0.                    (3.9)

The remaining case is ∆6 (2, 1) = 17/5670.
   For degrees eight and ten one finds

                                         105(r2 − q)P8 (r, q)
                                    ∆8 =                      ,                              (3.10)
                                              4q 3 r2 D8
                                         945(r2 − q)P10 (r, q)
                                   ∆10 =                        ,                            (3.11)
                                              8q 4 r3 D10
where the factors are displayed in section A. For r ≥ 4, substituting r = y + 4 and q = 2r − 1 + x
makes P8 a quadratic in x whose three coefficient polynomials have strictly positive coefficients.
For r ≥ 5, the substitution r = y + 5, q = 2r − 1 + x does the same for the four coefficients of the
cubic P10 . The complete integer arrays are given in section B. Since x, y ≥ 0, both polynomials
are positive.
    The exceptional exact gaps are
                      2                   967                   8111
        ∆8 (2, 1) =      , ∆8 (3, 1) =          , ∆8 (3, 2) =          ,
                    1215                3378375               69189120
                       74                    202877                    17789
        ∆10 (2, 1) =       , ∆10 (3, 1) =             , ∆10 (3, 2) =           ,
                     81081                 1520268750                249080832
                        20129                     2615                      65701
        ∆10 (4, 1) =           , ∆10 (4, 2) =            , ∆10 (4, 3) =              .
                     770461692                 181945764                 14578987500
All denominators in their stated rank ranges are positive, while r2 − q = (r − k)2 > 0. This
proves every asserted sign.

   The fourth-moment gap has an immediate analytic consequence. Since the laws are symmetric
and their variances agree, the first nonzero coefficient of Zr,r − Zr,k is ∆4 s4 /4!.

Corollary 3.2 (Weak-field barrier). For every fixed r ≥ 2 and k < r, there is εr,k > 0 such that

                              Zr,r (s) > Zr,k (s)       (0 < |s| < εr,k ).                   (3.12)




                                                    4
```

---

## Page 5

```text
4    The exact high-field barrier
The upper endpoint of Xk follows directly from the admissible principal angles:
                                                              s
                                                                     rk
                                       ρk := max Xk =                       .                                (4.1)
                                                                  2(2r − k)
                                                  p
It is strictly increasing in k, so ρk < ρr =           r/2 for k < r. The endpoint exponent can also be
computed exactly.
Proposition 4.1 (Watson endpoint asymptotic). For fixed r ≥ 2 and 1 ≤ k ≤ r, there is a
constant Cr,k > 0 such that

                            Zr,k (s) = Cr,k esρk s−kr 1 + O(s−1 ) ,
                                                                      
                                                                                s → +∞.                      (4.2)

Consequently, for every k < r, Zr,r (s) > Zr,k (s) for all sufficiently large |s|.
Proof. In (2.5), write xi = 1 − yi . At fixed small total deficit δ = i yi , the Jacobi weight
                                                                                        P

contributes degree k(r−k) and the squared Vandermonde contributes degree k(k−1). Integration
over the (k − 1)-simplex therefore gives a scalar trace density proportional to δ kr−1 with a
strictly positive Selberg-type coefficient. The linear rescaling (2.3) preserves the exponent.
Watson’s lemma gives (4.2). The strict endpoint inequality makes the exponential factor decisive.
Symmetry yields the negative-field statement.

Corollary 4.2 (Reentrant-island obstruction). Any failure of balanced two-block Laplace order
on a half Grassmannian must be confined to a bounded interval separated from zero and infinity.
In particular, a competing branch must create at least two additional positive zeros of Zr,r − Zr,k .
    The same endpoint idea can be sharpened from an asymptotic statement to an explicit
infinite-tail certificate. Set
                     1                 (2r − 1)2 (r + 1)                            2   (r − 1)(4r2 − 1)
          ar = 1 −      ,       Br =                     ,          Cr = 2(4r)−r                         .   (4.3)
                     2r                   4r2 (r − 1)                                         r+1
Let Mr be the least nonnegative integer for which

                                                 Cr BrMr > 1.                                                (4.4)

This is an exact rational definition and requires no logarithm.
Theorem 4.3 (Finite certification at every fixed half rank). Fix r ≥ 2. If

                               EXr2m > EXk2m       (1 ≤ k < r, 2 ≤ m < Mr ),                                 (4.5)

then the same inequalities hold for every m ≥ 2, and consequently

                                 Zr,r (s) > Zr,k (s)         (s ̸= 0, 1 ≤ k < r).                            (4.6)

Moreover, every sign in the finite hypothesis is exactly decidable by rational Hankel-determinant
arithmetic.
Proof. The common variance is σr2 = r/[2(4r2 − 1)]. The largest unbalanced support is attained
at k = r − 1 and has square
                                             r(r − 1)
                                       ρ2∗ =          .
                                             2(r + 1)
Therefore
                                             EXk2m ≤ σr2 ρ2m−2
                                                          ∗    .                                             (4.7)

                                                         5
```

---

## Page 6

```text
√
For balanced multiplicity, Xr = tr(H)/ 2r with H uniform on −I < H < I in the r2 -real-
dimensional Hermitian space. Each event H > ar I and H < −ar I has probability exactly
      2
(4r)−r : after Bp= (H + I)/2, it is a translate of the 1/(4r)-scaled matrix interval. On their
union |Xr | > ar r/2, whence
                                                                           m
                                                                       r
                                                                  
                                                     2
                                     EXr2m ≥ 2(4r)−r               a2r          .                  (4.8)
                                                                       2
Dividing (4.8) by (4.7) gives
                                             EXr2m
                                                   ≥ Cr Brm .                                      (4.9)
                                             EXk2m
The identity
                          (2r − 1)2 (r + 1) − 4r2 (r − 1) = 4r2 − 3r + 1 > 0
proves Br > 1, so (4.4) closes every m ≥ Mr . Hypothesis (4.5) closes the finite prefix, and
the two ranges cover every m ≥ 2. Symmetry and the common variance then prove (4.6)
coefficientwise.
    Finally, (5.2) in the next section holds at every rank with a = r −k. Its even entry coefficients
are rational beta integrals satisfying a first-order rational recurrence. A finite Leibniz expansion
therefore decides every sign in (4.5) using integers and reduced rational fractions.

     The universal cutoffs are conservative: for r = 2, . . . , 10 they are

                             12, 58, 165, 360, 672, 1131, 1766, 2610, 3695.                       (4.10)

The theorem proves termination at each fixed rank, not positivity of the finite block uniformly
in r.
    The moment theorem does not by itself exclude such zeros. The next section does exclude
them at r = 3.


5     All-field two-block rigidity on GrC (3, 6)
For k = 1, 2, 3, put                   s
                                               6                           ck
                                ck =                ,            Xk =         tr Hk .              (5.1)
                                           k(6 − k)                        2
Define the Hankel determinants
                                             Z 1                                    k−1
                            (a)                          i+j          2 a ux
                           Dk (u) = det              x         (1 − x ) e       dx            .    (5.2)
                                                −1                                    i,j=0

Andreief’s identity [1, 6] applied to (2.5) gives
                                                          (3−k)
                                                     Dk        (sck /2)
                                       Z3,k (s) =           (3−k)
                                                                        .                          (5.3)
                                                           Dk     (0)
Differentiating I0 (u) = 2 sinh(u)/u yields

     (2)        u2 sinh u − 3u cosh u + 3 sinh u                          (2)     16
    D1 (u) = 16                 5
                                                 ,                       D1 (0) = ,
                               u                                                  15
               2u4 + 2u2 cosh(2u) + 4u2 − 6u sinh(2u) + 3 cosh(2u) − 3            16
     (1)                                                                  (1)
    D2 (u) = 8                               8
                                                                       , D2 (0) = ,
                                           u                                      45
                   4             3             2          3
     (0)          u sinh u − 2u cosh u + 3u sinh u − sinh u               (0)      32
    D3 (u) = −32                                             ,           D3 (0) =     . (5.4)
                                       u9                                         135
All values at zero are removable limits.

                                                          6
```

---

## Page 7

```text
Theorem 5.1 (All-field GrC (3, 6) two-block rigidity). For every real s,

                              Z3,3 (s) ≥ Z3,2 (s),       Z3,3 (s) ≥ Z3,1 (s).               (5.5)

                                   ̸ 0. Equivalently, the balanced 3 + 3 spectrum uniquely
Both inequalities are strict for s =
maximizes the matrix–Bingham normalizer among all trace-zero, Frobenius-unit spectra having
exactly two levels.

Proof. Write Z3,k (s) =
                          P           2m . Expansion of (5.4) gives
                            m≥0 bk,m s

                                  15(3/10)m
                   b1,m =                           ,                                       (5.6)
                          (2m + 3)(2m + 5)(2m + 1)!
                                             360(3/4)m
                   b2,m =                                                ,                  (5.7)
                          (m + 2)(m + 3)(m + 4)(2m + 3)(2m + 5)(2m + 1)!
                          135{19683 9m − p(m)}
                   b3,m =                      ,                                            (5.8)
                              4 6m (2m + 9)!

where
                      p(m) = 64m4 + 896m3 + 4640m2 + 10552m + 8931.                         (5.9)
The constant coefficients equal one and the quadratic coefficients all equal 3/140.
   Put

        p1 (m) = 9p(m),       q1 (m) = 18 (m + 1)(m + 2)(m + 3)(2m + 7)(2m + 8)(2m + 9),
        p2 (m) = 3p(m),       q2 (m) = 41 (m + 1)(2m + 7)(2m + 9).

Common denominators give the exact identities

              4 6m (2m + 9)!
                             (b3,m − b1,m ) = 177147 9m − p1 (m) − 256(9/5)m q1 (m),       (5.10)
                    15
              4 6m (2m + 9)!
                             (b3,m − b2,m ) = 59049 9m − p2 (m) − 2048(9/2)m q2 (m).       (5.11)
                    45
For m = n + 2, direct factorization gives

             5q1 (m) − q1 (m + 1) = (n + 4)(n + 5)(n + 6)(2n + 13)(2n2 + 14n + 15),
             9p1 (m) − p1 (m + 1) = 2304(n + 4)(n + 5)(n + 6)(2n + 13),
             2q2 (m) − q2 (m + 1) = 41 (2n + 13)(2n2 + 11n + 6),
             9p2 (m) − p2 (m + 1) = 768(n + 4)(n + 5)(n + 6)(2n + 13).                     (5.12)

Thus q1 (m)/5m , p1 (m)/9m , q2 (m)/2m , and p2 (m)/9m decrease for m ≥ 2. Evaluating at m = 2
gives
                                               2574 18929   585728
                  9−m RHS(5.10) ≥ 177147 − 256      −     =        > 0,
                                                5      3      15
                                               429 170361   18304
                  9−m RHS(5.11) ≥ 59049 − 2048     −      =       > 0.                     (5.13)
                                               16     81      9
Therefore b3,m > b1,m , b2,m for every m ≥ 2. Summing the coefficient gaps proves (5.5), with
strictness away from zero.

    The theorem compares every two-level multiplicity, not arbitrary spectra with three or more
eigenvalues. A full-spectrum maximizer would require a separate stationary-spectrum reduction.



                                                     7
```

---

## Page 8

```text
6    All-field instability classification of the GrC (3, 6) branches
The value theorem can be supplemented by exact local geometry. Let
                                      k
                     Yek = tr(Ek P ) − ,          zk (u) = EeuYk ,        m = 6 − k.           (6.1)
                                                               e
                                      2
The Jacobi–Stein calculation of [4] shows that the constrained Hessian eigenvalue on a traceless
split of the larger block has sign opposite to
                                                 6(6m − 1) zk′ (u) m2
                          Hk− (u) = zk′′ (u) +                    −   zk (u).                  (6.2)
                                                     k         u    4
Its moment-ratio theorem makes the coefficient of u2j strictly negative whenever

                                      2j(m − k) > m(k 2 − 1).                                  (6.3)

Corollary 6.1 (All-field two-block instability classification). On GrC (3, 6), the 1 + 5 and 2 + 4
two-block critical orbits have an unstable larger-block split for every nonzero field and therefore
are not local maxima. The balanced 3 + 3 orbit is a strict local maximum modulo conjugation
for every nonzero field. Hence it is the unique local maximum within the complete two-level
stationary class.
Proof. For k = 1, condition (6.3) covers every j ≥ 1 and
                                         u2   u4
                           H1− (u) = −      −    − ··· < 0              (u ̸= 0).              (6.4)
                                         42 3696
For k = 2, (6.3) covers every j ≥ 4. The constant and quadratic terms vanish, and exact
expansion of (5.4) gives
                                            1                             1
                           [u4 ]H2− = −         ,        [u6 ]H2− = −          .               (6.5)
                                          16170                         840840
Thus every nonzero coefficient is negative. The Hessian sign convention in (6.2) supplies a
positive constrained-Hessian direction, and hence an instability, for both losing strata. The
balanced all-field Morse–Bott sign is the half-Grassmann no-spinodal theorem of [4].

    This closes two possible loopholes simultaneously: neither losing branch can overtake
balanced in value, and neither can restabilize at an intermediate field. It still leaves multi-level
stationary spectra outside its scope.


7    A unique canonical exchange on GrC (2, 5)
The half-rank symmetry is essential. Consider
                  1                                             1
            A1 = √ diag(4, −1, −1, −1, −1),               A2 = √ diag(3, 3, −2, −2, −2),       (7.1)
                  20                                            30
and Zk (s) = Ees tr(Ak P ) for P ∼ GrC (2, 5).
Theorem 7.1 (Unique canonical crossing). The difference Z2 (s)−Z1 (s) has exactly one positive
zero. The zero is simple. Hence there is a unique s× > 0 such that

                  Z1 (s) > Z2 (s)   (0 < s < s× ),         Z2 (s) > Z1 (s)     (s > s× ).      (7.2)

Moreover, for every s > 0 each displayed positive orientation strictly dominates its negative
orientation. Since multiplicities 4 and 3 are, up to conjugacy, −A1 and −A2 , respectively, (7.2)
is the unique exchange of the complete oriented two-level family.

                                                     8
```

---

## Page 9

```text
7.1     Exact overlap densities
           √
Set Yk =     30 tr(Ak P ). For A1 , q = P11 has the Beta(2, 3) law and
                           √                           √ √           √
                             6                        4 6( 6y − 9)2 ( 6y + 6)
                     Y1 =      (5q − 2),     f1 (y) =                         ,             (7.3)
                            2                                  16875
      √            √
on − 6 < y < 3 6/2.
    For A2 , let T = tr(E2 P ). The two principal overlaps have joint density 36(x1 − x2 )2 (1 −
x1 )(1 − x2 ) on (0, 1)2 and Y2 = 5T − 4. Integration along x1 + x2 = t yields

                                     6(y + 4)3 (y 2 − 42y + 66)
                                   
                                                                ,   −4 < y < 1,
                                   
                                   
                                   
                        f2 (y) =               78125                                               (7.4)
                                             5
                                    6(6 − y) ,
                                   
                                                                    1 < y < 6.
                                   
                                       78125
Direct integration gives
                                                                                   √
                                                  3                         2−3        6
               EY1 = EY2 = 0,        EY12 = EY22 = ,          EY23 − EY13 =                < 0.    (7.5)
                                                       2                          14

7.2     Four sign changes, certified exactly
                                                                                 √
Let h = f2 − f1 . Outside the support of f1 , h = f2 > 0. On the lower overlap (− 6, 1),
                                                     6
                                          h(y) =         p− (y),                                   (7.6)
                                                   78125
where
                                                                     √ !
                                             4510               2000  6
                      p− (y) = y 5 − 30y 4 −      y 3 + −1160 +          y2
                                               9                   9
                                                       √
                               + 980y + 4224 − 1500 6.                                             (7.7)
        √
On (1, 3 6/2),
                                                      6
                                         h(y) = −         p+ (y),                                  (7.8)
                                                    78125
where
                                                                 √ !
                                         4240               2000  6
                  p+ (y) = y 5 − 30y 4 +      y 3 + −2160 −          y2
                                           9                   9
                                                    √
                           + 5980y − 7776 + 1500 6.                                                (7.9)
                       √
Sturm sequences over Q( 6) prove that p− has one root in each of

                            (−9/4, −11/5),       (−1/2, −9/20),                                   (7.10)
                       √
and no other root in (− 6, 1); p+ has one root in each of

                                      (5/4, 13/10),        (3, 31/10),                            (7.11)
                          √
and no other root in (1, 3 6/2). Their terminal Sturm remainders are nonzero constants, so all
four roots are simple. Exact signs at rational probes give

                                         sgn h = +, −, +, −, +.                                   (7.12)

Thus h has exactly four sign changes.

                                                      9
```

---

## Page 10

```text
7.3   Variation diminution
We use the classical strict total positivity of the kernel K(s, y) = esy [10, 11, 16].

Lemma 7.2 (Continuous generalized Descartes rule). If a nonzero compactly supported signed
density h has m sign changes, then its bilateral Laplace transform
                                                    Z
                                           L(s) =        esy h(y) dy                       (7.13)
                                                     R

has at most m real zeros, counted with multiplicity.

Proof. Suppose L had zeros si of total multiplicity greater than m. Differentiating (7.13)
supplies orthogonality to the corresponding functions y j esi y . These functions form an extended
complete Chebyshev system because the exponential kernel is strictly totally positive. The
standard interpolation theorem then constructs a nonzero linear combination with simple zeros
at the sign-change points of h and the same sign as h on every intervening interval. Its integral
against h is strictly positive, while the orthogonality makes it zero, a contradiction.

Lemma 7.3 (Strict orientation dominance). Let Mj (t) = EetYj for the two rescaled statistics
in (7.3)–(7.4). Then
                         Mj (t) > Mj (−t)    (t > 0, j = 1, 2).
Consequently the positive multiplicity-1 and multiplicity-2 orientations strictly dominate multi-
plicities 4 and 3, respectively, at positive field.
                                                                          R ty
Proof. Put gj (y)√= fj (y) − fj (−y) and Oj (t) = Mj (t) − Mj (−t) =       e gj (y) dy.
   For 0 < y < 6, direct subtraction in (7.3) gives

                                                    16y(2y 2 − 9)
                                       g1 (y) =                   .
                                                        1875
    √             √
For 6 < y < 3 6/2, the reflected density vanishes and g1 (y) > 0. Since 0 < 9/2 < 6, the
positive half-line has exactly one sign change and the odd density g1 has√ the global pattern
−, +, −, +, hence three sign changes. Moreover, EY1 = 0 and EY13 = 3 6/14 > 0. Thus O1
has a zero of exactly multiplicity three at the origin and is positive immediately to its right.
Lemma 7.2 leaves no budget for another real zero, so O1 (t) > 0 for every t > 0.
   For 0 < y < 1, (7.4) gives

                                           12y(y 4 − 390y 2 + 480)
                                g2 (y) =                           > 0;
                                                    78125
the polynomial in y 2 decreases on [0, 1] and has endpoint value 91. For 1 < y < 4,

                         12p(y)
              g2 (y) =          ,    p(y) = 30y 4 − 375y 3 + 1660y 2 − 3000y + 1776.
                         78125
An exact rational Sturm sequence gives exactly two simple roots, one in (23/20, 7/6) and one in
(11/4, 14/5), with signs +, −, +. For 4 < y < 6, the reflected density vanishes and g2 (y) > 0.
Hence the odd density g2 has exactly five sign changes. Since EY2 = 0 and EY23 = 1/7 > 0, O2
has a zero of multiplicity three at the origin and is positive just to its right. Lemma 7.2 leaves
at most two additional real zeros. Nonzero zeros occur in opposite pairs with equal multiplicity.
A simple positive zero would change sign and require a second positive zero to return to the
positive large-field sign; an even positive zero and its negative partner would already consume
four multiplicities. Both possibilities exceed the remaining budget. Therefore O2 (t) > 0 for
every t > 0.


                                                        10
```

---

## Page 11

```text
√
Proof of theorem 7.1. After the harmless rescaling s 7→ s/ 30, the difference Z2 − Z1 is the
Laplace transform of h. Equations (7.5) show that it has a zero of exactly multiplicity three
at the origin and is negative immediately to the right. By (7.12) and theorem 7.2, at most
one additional real zero√remains, counting multiplicity. The upper support endpoint of Y2 is
6, strictly larger than 3 6/2, the endpoint of Y1 ; hence Z2 − Z1 > 0 for all sufficiently large
positive s. A positive zero therefore exists. It consumes the remaining zero budget and must be
unique and simple. Lemma 7.3 removes the two negative orientations, proving the complete
oriented-family statement.

    The diagnostic value s× ≈ 4.858579 is not used in the proof.


8      A finite exact all-field certificate on GrC (4, 8)
The fixed-rank theorem becomes a complete all-field result at the next half rank. For P ∼
GrC (4, 8), let
                s              s
                    8−k                k
         Ak =           Ek −                (I − Ek ),          Zk (s) = Ees tr(Ak P ) ,   1 ≤ k ≤ 4.      (8.1)
                     8k            8(8 − k)

Theorem 8.1 (Computer-assisted all-field GrC (4, 8) two-block rigidity). For every real s and
k = 1, 2, 3,
                                     Z4 (s) ≥ Zk (s),                                    (8.2)
                             ̸ 0. More strongly, after the common constant and quadratic
with strict inequality for s =
coefficients, every even Taylor coefficient of Z4 is strictly larger than its counterpart in Zk .

   The proof is computer-assisted only on a finite exact-rational block. Its infinite tail is
analytic and independent of the replay.

Proof. Put c2k = 8/[k(8 − k)]. Matrix-beta compression and Andreief’s identity give
                                                       (4−k)
                                                      Dk   (sck /2)
                                        Zk (s) =        (4−k)
                                                                    ,                                      (8.3)
                                                       Dk     (0)

with D as in (5.2). If
                                                Z 1
                                       Ja,t =         x2t (1 − x2 )a dx,
                                                 −1
then
                                    22a+1 (a!)2            Ja,t+1      2t + 1
                          Ja,0 =                ,                 =             .                          (8.4)
                                     (2a + 1)!              Ja,t    2t + 2a + 3
The coefficient of uℓ in the (i, j) entry of the determinant is zero when ℓ + i + j is odd and
otherwise equals
                                             Ja,(ℓ+i+j)/2
                                                          .                               (8.5)
                                                  ℓ!
Leibniz expansion and finite convolution of these rational series prove, with no rounding or
tolerance,
                       [s2m ]Z4 > [s2m ]Zk ,      k = 1, 2, 3, 2 ≤ m ≤ 134.               (8.6)
                                                                                                   p
   It remains to close the infinite tail. Every unbalanced branch has |Xk | ≤ ρ3 =                      6/5 and
common variance 2/63, hence
                                               2 6 m−1
                                                  
                                         2m
                                     EXk ≤               .                                                 (8.7)
                                              63 5


                                                       11
```

---

## Page 12

```text
√
For k = 4, X4 = tr(H)/ 8 with H uniform on the 16-dimensional Hermitian matrix interval.
Each event H √> (19/20)I and H < −(19/20)I has probability 40−16 , and on their union
|X4 | > (19/20) 2. Therefore
                                                361 m
                                                   
                              EX42m ≥ 2 40−16         .                            (8.8)
                                                200
The ratio of (8.8) to (8.7) is at least
                                                         m
                                          378 −16 361
                                                  
                                             40               .                                (8.9)
                                           5      240
Exact integer comparison shows that (8.9) exceeds one at m = 134; its base 361/240 is greater
than one, so every m ≥ 134 is covered. This overlaps the exact finite block. The laws are
symmetric, and summing the strict even coefficient gaps proves (8.2).

Remark 8.2 (Audit surface). The finite checker expands each determinant through degree 268
using Python Fraction; it uses neither quadrature nor floating-point sign tests. A hostile audit
independently checked normalization, truncation, the 40−16 event volume, the cutoff overlap,
symmetry, and exhaustion of the two-level class. On the constrained reference machine the
replay took about 3.1 seconds and peaked at 13.3 MiB resident memory. These resource figures
document the replay; they are not mathematical assumptions.

    Theorem 8.1 is the second half-rank case closed here, not a uniform-in-rank theorem. The
general result gives coefficientwise dominance at every fixed rank a terminating exact sufficient
certificate; when that certificate passes, it proves all-field order. A failed coefficient sign does
not by itself decide the sign of the full Laplace-transform difference, and the required finite
block grows with r.


9      What the exact branch theorems do and do not prove
The results separate three distinct levels of control:

 (a) Local orbit stability: the constrained Hessian near a specified branch, supplied for half
     rank by [4].

 (b) Canonical branch order: comparison of all two-level multiplicities. This is closed here for
     GrC (3, 6) and GrC (4, 8), and for the complete oriented two-level family on GrC (2, 5).

    (c) Full-spectrum global order: comparison with every trace-zero, Frobenius-unit spectrum,
        including three or more distinct eigenvalues. This remains open in every example treated
        here.

    For GrC (3, 6) or GrC (4, 8), a hypothetical counterexample to the balanced global conjecture
must have at least three eigenvalues. It cannot lie on a two-block crossing and cannot arise from
a spinodal instability of the balanced branch. For GrC (2, 5), the unique canonical exchange
rules out reentrance between the one-spike and rank-two sources, but a noncanonical multi-level
branch could still exceed both.
    Accordingly, none of the following is claimed:

    (i) that every global stationary spectrum has at most two levels;

 (ii) that the balanced 3 + 3 field is globally optimal over the full spectral sphere, or that the
      balanced 4 + 4 field is globally optimal over its full spectral sphere;

 (iii) that the full-spectrum GrC (2, 5) envelope is exhausted by the two displayed positive-
       orientation branches, or equivalently that no multi-level branch exceeds them; or

                                                12
```

---

## Page 13

```text
(iv) an unrestricted all-distortion rate–distortion function derived from either unproved enve-
      lope.
    This boundary is not cosmetic. The fixed-norm candidate spectra are typically majorization-
incomparable, and the local theory already permits metastable unbalanced half-rank branches.
A global theorem needs a new stationary-spectrum reduction, a pair-smoothing inequality, or
an exact certificate covering every multiplicity stratum.


10     Reproducibility
Five lightweight exact replay scripts accompany the manuscript, organized into four groups.
  (i) matrix_cube/verify_low_degree_order.py reconstructs (3.6)–(3.11), verifies every
      positive-coefficient array in section B, and checks 220 independent Schur–Weyl fixtures.
 (ii) verify_gr36_two_block_laplace.py reconstructs the Hankel determinants, the coeffi-
      cient formulas, the discrete factorizations, and the remaining exact Hessian coefficients.
(iii) finite_global/verify_d5r2_canonical_crossing.py derives the two       √ densities sym-
      bolically and performs every Sturm count and sign decision in exact Q( 6) arithmetic.
 (iv) matrix_cube/verify_finite_tail_cutoffs.py checks the exact universal cutoffs in
      (4.10), while matrix_cube/verify_r4_all_degree.py checks the complete rational block
      (8.6) and the exact tail threshold.
The scripts replay finite algebra. They do not substitute a numerical search for an un-
proved full-spectrum theorem. The release package includes every script and its dependency,
the one-command wrapper replay/run_all_replays.py, a persisted exact result ledger, an
environment-and-command manifest, and SHA256SUMS. Verification is explicitly partial: bibliog-
raphy screening, independent peer review, full-spectrum optimization, and scientific priority are
not assessed by the replay.


A     Moment-gap polynomials
The degree-eight quantities in (3.10) are
                          A8 = 12r6 − 111r4 + 163r2 − 60,
                          B8 = −76r6 + 163r4 − 60r2 ,
                          C8 = 240r6 − 60r4 ,
                     P8 (r, q) = A8 q 2 + B8 q + C8 ,
                          D8 = (2r − 7)(2r − 5)(2r − 3)(2r − 1)2 (2r + 1)2
                                   × (2r + 3)(2r + 5)(2r + 7).
For degree ten,
                  A10 = 80r10 − 2040r8 + 14005r6 − 34367r4 + 35100r2 − 12096,
                  B10 = −880r10 + 11800r8 − 34367r6 + 35100r4 − 12096r2 ,
                  C10 = 6080r10 − 28256r8 + 35100r6 − 12096r4 ,
                   (0)
                  D10 = −21504r10 + 53760r8 − 12096r6 ,
                                                        (0)
             P10 (r, q) = A10 q 3 + B10 q 2 + C10 q + D10 ,
                  D10 = (2r − 9)(2r − 7)(2r − 5)(2r − 3)2 (2r − 1)2
                         × (2r + 1)2 (2r + 3)2 (2r + 5)(2r + 7)(2r + 9).

                                                 13
```

---

## Page 14

```text
B     Positive-coefficient certificates
                                     P2            j
For P8 (y + 4, 2(y + 4) − 1 + x) =    j=0 c8,j (y)x , the coefficient polynomials are

                    c8,0 = 48y 8 + 1336y 7 + 15788y 6 + 102818y 5 + 400038y 4
                            + 939548y 3 + 1272831y 2 + 874408y + 214900,
                    c8,1 = 48y 7 + 1244y 6 + 13284y 5 + 75025y 4 + 237852y 3
                            + 408430y 2 + 320064y + 55448,
                    c8,2 = 12y 6 + 288y 5 + 2769y 4 + 13584y 3 + 35587y 2
                            + 46616y + 23284.
                                      P3               j
For P10 (y + 5, 2(y + 5) − 1 + x) =      j=0 c10,j (y)x ,

          c10,0 = 640y 13 + 37120y 12 + 979040y 11 + 15522336y 10 + 164732888y 9
                  + 1232842288y 8 + 6674149082y 7 + 26363797506y 6 + 75611253136y 5
                  + 154443659379y 4 + 216240062046y 3 + 193546929296y 2
                  + 96708725184y + 19346224491,
          c10,1 = 960y 12 + 53120y 11 + 1321200y 10 + 19491680y 9 + 189485684y 8
                  + 1274609832y 7 + 6058238765y 6 + 20392541954y 5 + 47930087778y 4
                  + 76137334976y 3 + 77150587905y 2 + 45135152502y + 12252504972,
          c10,2 = 480y 11 + 25280y 10 + 591760y 9 + 8107120y 8 + 71984830y 7
                  + 432888668y 6 + 1786158088y 5 + 4998471151y 4 + 9107125370y 3
                  + 9854406754y 2 + 5054136464y + 430182883,
          c10,3 = 80y 10 + 4000y 9 + 87960y 8 + 1118400y 7 + 9086005y 6
                  + 49140150y 5 + 178467508y 4 + 427325160y 3 + 639926925y 2
                  + 533261250y + 182589154.
Every displayed coefficient is strictly positive.


C     Exact Sturm ledger for the canonical crossing
For reproducibility without decimal roots, the theorem-bearing Sturm counts are
                       Polynomial          Interval         Number of roots
                                              √
                       p−                  (− 6, 1)         2
                       p−                  (−9/4, −11/5)    1
                       p−                       √ −9/20)
                                           (−1/2,           1
                       p+                  (1, 3 6/2)       2
                       p+                  (5/4, 13/10)     1
                       p+                  (3, 31/10)       1
                       p (orientation)     (1, 4)           2
                       p (orientation)     (23/20, 7/6)     1
                       p (orientation)     (11/4, 14/5)     1
The exact probe points −12/5, −2, 0, 6/5, 2, 7/2 produce the density signs +, −, +, +, −, +;
accounting for the support-only positive intervals reduces this to the global five-block pattern
+, −, +, −, +. For the rank-two orientation polynomial p, rational probes in its three root-
separated intervals give +, −, +. Together with positivity on (0, 1) and (4, 6) and odd reflection,
this gives the five sign changes used in Lemma 7.3.

                                                    14
```

---

## Page 15

```text
References
 [1]   C. Andréief. “Note sur une relation entre les intégrales définies des produits des fonctions”.
       In: Mémoires de la Société des Sciences Physiques et Naturelles de Bordeaux 2.3 (1883),
       pp. 1–14.
 [2]   Armine Bagyan and Donald Richards. “Complete Asymptotic Expansions for the Normal-
       izing Constants of High-Dimensional Matrix Bingham and Matrix Langevin Distributions”.
       In: SIGMA 20 (2024), p. 094. doi: 10.3842/SIGMA.2024.094.
 [3]   Lluis Eriksson. A Finite-Dimensional Nonanalytic Spectral Transition and Exact High-
       Fidelity Rate–Distortion for Rank-r Born Prediction on Complex Grassmannians. Archive
       for Rigorous Research, ARR-2026-6FDEKPVJ0W8BHBMC. 2026. url: https://arr-
       research.github.io/papers/ARR-2026-6FDEKPVJ0W8BHBMC/.
 [4]   Lluis Eriksson. All-Field Morse–Bott Stability at Critical Homogeneous Orbits: Half-
       Grassmann No-Spinodal Rigidity and Exact Jacobi Metastability. Archive for Rigorous
       Research, ARR-2026-6F8XRSBM0J9Q2R2B. 2026. url: https://arr-research.github.
       io/papers/ARR-2026-6F8XRSBM0J9Q2R2B/.
 [5]   Lluis Eriksson. Complete Rank-Two Born-Prediction Rate–Distortion on GrC (2, 4): All-
       Field Matrix–Bingham Rigidity and a Unique Coexistence Transition. Archive for Rigorous
       Research, ARR-2026-61Y0FFA39M8KMBJ5. 2026. url: https://arr-research.github.
       io/papers/ARR-2026-61Y0FFA39M8KMBJ5/.
 [6]   Peter J. Forrester. Log-Gases and Random Matrices. Princeton University Press, 2010.
       doi: 10.1515/9781400835416.
 [7]   Peter J. Forrester and Santosh Kumar. “Differential Recurrences for the Distribution of
       the Trace of the β-Jacobi Ensemble”. In: Physica D: Nonlinear Phenomena 434 (2022),
       p. 133220. doi: 10.1016/j.physd.2022.133220. arXiv: 2011.00787.
 [8]   Claude Itzykson and Jean-Bernard Zuber. “The Planar Approximation. II”. In: Journal
       of Mathematical Physics 21.3 (1980), pp. 411–421. doi: 10.1063/1.524438.
 [9]   Alan T. James. “Distributions of Matrix Variates and Latent Roots Derived from Normal
       Samples”. In: The Annals of Mathematical Statistics 35.2 (1964), pp. 475–501. doi:
       10.1214/aoms/1177703550.
[10]   Samuel Karlin. Total Positivity. Vol. 1. Stanford University Press, 1968.
[11] Samuel Karlin and William J. Studden. Tchebycheff Systems: With Applications in Analysis
     and Statistics. Wiley–Interscience, 1966.
[12] John T. Kent. “The Complex Bingham Distribution and Shape Analysis”. In: Journal of
     the Royal Statistical Society: Series B 56.2 (1994), pp. 285–299. doi: 10.1111/j.2517-
     6161.1994.tb01978.x.
[13] Colin McSwiggen and Jonathan Novak. “Majorization and Spherical Functions”. In:
     International Mathematics Research Notices 2022.5 (2022), pp. 3977–4000. doi: 10.1093/
     imrn/rnaa390.
[14] Colin McSwiggen and Siddhartha Sahi. Majorization Inequalities from Logarithmic Con-
     vexity. 2026. arXiv: 2605.12680.
[15] Robb J. Muirhead. Aspects of Multivariate Statistical Theory. Wiley, 1982. doi: 10.1002/
     9780470316559.
[16] Allan Pinkus. Totally Positive Matrices. Cambridge University Press, 2010. doi: 10.1017/
     CBO9780511691713.
[17] Suvrit Sra. “On Inequalities for Normalized Schur Functions”. In: European Journal of
     Combinatorics 51 (2016), pp. 492–494. doi: 10.1016/j.ejc.2015.07.005.

                                                 15
```
