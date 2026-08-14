# All-Field Simple-Bivector Rigidity and Exact Shannon Rate–Distortion for Haar Oriented Two-Planes

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
All-Field Simple-Bivector Rigidity and Exact Shannon
    Rate–Distortion for Haar Oriented Two-Planes
         A dimension-uniform Plücker theorem with discontinuous onset for n ≥ 6

                                              Lluis Eriksson
                                    Independent Researcher, Sweden
                                        lluiseriksson@gmail.com

                                             August 14, 2026


                                                  Abstract
          Let W = x ∧ y be the unit simple bivector of a Haar oriented two-plane in Rn . We solve
      the fixed-norm
              P      external-field problem for its linear exponential partition in every dimension.
      If B = j pj e2j−1 ∧ e2j , then
                                               X (s2 /4)k hk (p2 , . . . , p2 )
                                 Ees⟨B,W ⟩ =                      1        m
                                                                                  .
                                                     ((n − 1)/2)k (n/2)k
                                               k≥0

      Coefficientwise positivity and hk (z) ≤ ( zj )k imply that, at every nonzero field and fixed
                                               P
      exterior norm, the unique maximizing orthogonal orbit consists of simple bivectors. The
      optimal overlap has the elementary density
                                          n−2
                               fn (t) =       (1 − |t|)n−3 ,          −1 ≤ t ≤ 1.
                                           2
      We then determine the unrestricted classical Shannon rate–distortion function of the Haar
      Plücker source under squared ambient loss. The decoder may use an arbitrary standard-Borel
      memory and is not restricted to the Grassmann orbit: conditional least squares places its
      reports in the full Grassmann orbitope, the unit mass-norm ball. The all-field theorem
      reduces the exact converse and covariant attainment to one scalar radius. For n = 3, 4, 5
      we prove continuous activation, a unique positive branch, and no radial reentrance. For
      every n ≥ 6, a positive fourth cumulant instead forces a discontinuous directional-information
      onset and an adjacent time-sharing face. We also obtain the exact high-fidelity constant.
      The result concerns signed Plücker-coordinate compression, not quantum rate–distortion or
      Born-probability prediction.


1    Introduction
The oriented Grassmannian Gr+       n                                      2 n
                                2 (R ) embeds into the unit sphere of Λ R by the classical Plücker
map: an oriented orthonormal frame (x, y) is sent to the unit simple bivector W = x ∧ y. This
representation retains orientation and makes linear queries of the plane ordinary Euclidean
coordinates. It also exposes a nontrivial distinction between the source orbit and its convex hull.
Posterior means are generally mixed bivectors rather than planes.
    Grassmann quantization and chordal distortion have a substantial literature, including finite-
codebook, high-rate, and recent covering bounds [1–3]. Matrix Langevin and Bingham families
on Stiefel and projector Grassmann manifolds are likewise classical [4–6]. Those problems do not
settle the one considered here. Our sufficient statistic is linear in the signed Plücker bivector, and
the Shannon decoder is allowed to range over the full convex hull rather than the source orbit.
An exact RDF consequently requires a global external-bivector optimization, not just evaluation
of a normalizer along a chosen parameter.

                                                       1
```

---

## Page 2

```text
Present paper                         Rank-two complex companion
    Source               signed W ∈ Gr+   n
                                      2 (R )                   state P/2, P ∈ GrC (2, 4)
    Reports              mass-norm unit ball                   0 ⪯ σ ⪯ I/2, tr σ = 1
    Loss                 ambient bivector square loss          integrated Born/Frobenius loss
    Closure              all n; full radial phase for n ≤ 5    exceptional n = 6 orbit; full radial
                                                               and block phase

      Table 1: The shared n = 6 homogeneous orbit and the distinct operational questions.


    The relevant convex body is the Grassmann orbitope, studied in the general theory of
orbitopes and calibrated geometry [7, 8]. General compact-symmetry and Gibbs-duality methods
are established [9–11], and the uniform sphere has an exact modern RDF treatment [12]. The new
step here is the dimension-uniform fixed-Euclidean-norm envelope of a singular orthogonal orbital
integral, including its equality case, and the unrestricted all-distortion RDF that this envelope
enables. Classical Harish–Chandra machinery provides a wider integral framework [13, 14]; our
proof instead uses a direct conditional-sphere calculation that makes every coefficient positive.
    Our main outputs are:

    1. an exact all-degree series for the linear Plücker partition of a Haar oriented two-plane;

    2. a global all-field theorem: simple external bivectors uniquely maximize that partition at
       fixed exterior norm in every n ≥ 3;

    3. an elementary beta-type overlap density and scalar hypergeometric normalizer;

    4. an exact unrestricted Shannon RDF with reports in the full mass-norm ball, including a
       standard-Borel converse, covariant attainment, and nonexposed time sharing;

    5. a complete continuous radial phase for n = 3, 4, 5, a rigorous discontinuous first activation
       for every n ≥ 6, and the exact high-fidelity constant.

    The novelty claim is deliberately scoped. Plücker coordinates, orthogonal canonical form,
orbital integrals, the Grassmann orbitope, mass/comass duality, and generic Gibbs duality are
prior structure. To our knowledge, the fixed-norm all-field simple-bivector extremum with equality
and the resulting exact unrestricted all-distortion RDF for n ≥ 5 have not previously been stated.
The cases n = 3 and n = 4 are consistency checks: the former is spherical and the latter admits a
product-sphere description.
    The relation to the rank-two complex companion is exact at the level of the source orbit but
not at the level of the operational problem. When n = 6, Spin(6) ≃ SU (4) identifies Gr+        6
                                                                                            2 (R )
with GrC (2, 4). The companion studies the normalized projector P/2, Born-probability loss, and
posterior density matrices; the present paper studies the signed Plücker coordinate W , ambient
bivector loss, and the mass-norm ball. The companion completely classifies its exceptional scalar
phase and proves source-universal block consequences. Here the new content is the dimension-
uniform all-field theorem and RDF, together with the sharp continuous/discontinuous boundary
at n = 6. Thus neither manuscript subsumes the other, and no theorem from the companion is
used below.


2     Geometry, norm, and source model
Let
              Gn = Gr+   n                     n                                2 n
                     2 (R ) = {x ∧ y : x, y ∈ R , ⟨x, y⟩ = 0, ∥x∥ = ∥y∥ = 1} ⊂ Λ R

with normalized Haar probability µ. We use the exterior inner product for which ei ∧ ej , i < j, is
an orthonormal basis. Hence every W ∈ Gn has ∥W ∥ = 1.

                                                    2
```

---

## Page 3

```text
Every B ∈ Λ2 Rn has an orthogonal canonical form
                            m
                            X                                                                  X
                      B=          pj e2j−1 ∧ e2j ,           m = ⌊n/2⌋,            ∥B∥2 =          p2j .   (1)
                            j=1                                                                j

Let CB be the associated skew matrix, defined by ⟨B, u ∧ v⟩ = ⟨CB u, v⟩. Our convention gives

                                                   ∥CB ∥2F = 2∥B∥2 .                                       (2)

All fixed-radius statements use the exterior norm in equation (1); equation (2) records the
otherwise easy-to-miss factor of two.
    For real s, define
                                   Zn (s, B) = EW ∼µ es⟨B,W ⟩ .                          (3)
The law is symmetric because both orientations occur, so Zn is even in s and B.


3    Positive series and all-field rigidity
Generate W = x ∧ y by drawing x uniformly from S n−1 and then y uniformly from the unit
sphere in x⊥ . Since CB x ⊥ x,
                                                                       d
                                        ⟨B, x ∧ y⟩ = ⟨CB x, y⟩ = ∥CB x∥Y,

where Y is a coordinate of the uniform law on S n−2 . Its moment-generating series is
                                                       X         (t2 /4)k
                                              EetY =                        .                              (4)
                                                             k!((n − 1)/2)k
                                                       k≥0

   Put qj = x22j−1 + x22j . The paired blocks, and for odd n the final unpaired coordinate square,
form a Dirichlet vector with paired parameters one and total parameter n/2. The unpaired block
has coefficient zero in ∥CB x∥2 . Hence
                                                  k
                                         X                     k!
                                  E          p2j qj  =            hk (p21 , . . . , p2m ),               (5)
                                                             (n/2)k
                                          j

where hk is the complete homogeneous symmetric polynomial.

Theorem 3.1 (positive all-degree orbital series). For every n ≥ 3, B ∈ Λ2 Rn , and real s,

                                                    ∞
                                                    X (s2 /4)k hk (p2 , . . . , p2 )
                                                                           1         m
                                   Zn (s, B) =                                           .                 (6)
                                                             ((n − 1)/2)k (n/2)k
                                                    k=0


The series is absolutely convergent and every coefficient is nonnegative.

Proof. Substitute equation (5) into the conditional expansion equation (4). Absolute convergence
follows directly from | ⟨B, W ⟩ | ≤ ∥B∥ or from the ratio test.

    For nonnegative z1 , . . . , zm ,

                                        hk (z1 , . . . , zm ) ≤ (z1 + · · · + zm )k .                      (7)

Indeed, each monomial coefficient on the left is one and the corresponding multinomial coefficient
on the right is at least one. At k = 2, equality forces zi zj = 0 for i ̸= j.

                                                              3
```

---

## Page 4

```text
Theorem 3.2 (all-field simple-bivector rigidity). Fix R > 0 and s ̸= 0. Among all B ∈ Λ2 Rn
with ∥B∥ = R, the partition Zn (s, B) is uniquely maximized, up to the orthogonal action and sign,
by a simple bivector B = RQ. Its value is

                                                  n − 1 n (sR)2
                                                                
                             Ln (sR) := 1 F2 1;        , ;         .                           (8)
                                                    2   2    4

For n = 3 every nonzero bivector is simple, so the assertion is uniqueness of the fixed-radius orbit.

Proof. Apply equation (7) coefficientwise to equation (6), using j p2j = R2 . Equality of the
                                                                      P
summed series at nonzero s forces equality in its strictly positive k = 2 term, hence exactly one
p2j is nonzero. This is precisely the canonical form of a simple bivector. At a simplex vertex
hk (R2 , 0, . . .) = R2k , and summing gives equation (8) because (1)k /k! = 1.


4    The exact overlap law
Let Q be a fixed unit simple bivector and X = ⟨W, Q⟩. The vertex specialization of equation (6)
gives
                                  (2k)!             (2k)!
                 EX 2k = k                      =           ,  EX 2k+1 = 0.                 (9)
                          4 ((n − 1)/2)k (n/2)k   (n − 1)2k
Proposition 4.1 (elementary overlap density). The simple Plücker overlap has density

                                               n−2
                                   fn (x) =        (1 − |x|)n−3 1[−1,1] (x).                            (10)
                                                2

Consequently                                       Z 1
                                Ln (t) = (n − 2)         cosh(tx)(1 − x)n−3 dx.                         (11)
                                                    0

Proof. The density in equation (10) is normalized and symmetric. Its even moments are
                         Z 1
                                                                                    (2k)!
               (n − 2)         x2k (1 − x)n−3 dx = (n − 2)B(2k + 1, n − 2) =                ,
                          0                                                       (n − 1)2k

which agree with equation (9). Compact support makes the moment problem determinate.
Integrating etx against the density gives equation (11).

    Thus the optimal normalizer is elementary in every integer dimension: it is an exponential
divided by tn−2 plus a finite Taylor correction. In particular, L3 (t) = sinh(t)/t. For n ≥ 4 the
orbit is a proper submanifold of its ambient sphere even though its optimal one-dimensional
overlap remains elementary.
    The second and fourth moments are
                                     2                                 24
                      EX 2 =               ,       EX 4 =                           .                   (12)
                                  n(n − 1)                   n(n − 1)(n + 1)(n + 2)

5    The full reproduction body
                                               P
Write a bivector in canonical form A =           j pj Vj , where the Vj are orthogonal unit simple bivectors.
Its mass norm is                                             X
                                               ∥A∥mass =         |pj |.
                                                             j

This is the atomic norm generated by unit simple bivectors; its polar is the comass norm. In
degree two the canonical skew decomposition makes the description explicit.

                                                         4
```

---

## Page 5

```text
Proposition 5.1 (oriented Grassmann orbitope).

                          Kn := conv(Gn ) = {A ∈ Λ2 Rn : ∥A∥mass ≤ 1}.                          (13)

In particular, every simple ray bQ, 0 ≤ b ≤ 1, is feasible.
Proof. The mass norm is convex, orthogonally invariant, and equals one on every orbit point, so
the convex hull is contained in the displayed ball. Conversely,
                                                                  
                                X                           X
                           A=       |pj | sgn(pj )Vj + 1 −   |pj | 0,
                                  j                             j

and 0 = (V + (−V ))/2. This is a convex combination of oriented unit simple bivectors.

    Let U be an arbitrary standard-Borel classical memory and let YU be any square-integrable
Λ2 Rn -valued report. Conditional least squares gives

           E∥W − YU ∥2 = E∥W − AU ∥2 + E∥AU − YU ∥2 ,                   AU = E(W | U ) ∈ Kn .   (14)

The deterministic replacement U 7→ AU cannot increase mutual information. Thus arbitrary
reports reduce exactly to the full body equation (13), not to orbit-valued quantization.


6    Exact unrestricted rate–distortion
Define the Shannon RDF under squared Plücker loss by

                          Rn (D) = inf I(W ; U ),         E∥W − YU ∥2 ≤ D,                      (15)

where the infimum is over arbitrary standard-Borel memories and square-integrable reports. The
natural interval is 0 ≤ D ≤ 1: the constant zero report gives distortion one.
   Put Kn = log Ln and

                       Cn (λ) = e−λ max exp{Kn (2λb) − λb2 },               λ ≥ 0.              (16)
                                      0≤b≤1

Theorem 6.1 (exact unrestricted Plücker RDF). For every n ≥ 3 and 0 ≤ D ≤ 1,
                                                                  
                                                                              2
                       Rn (D) = sup λ(1 − D) − max [Kn (2λb) − λb ] .                           (17)
                                 λ≥0                    0≤b≤1


Every exposed positive-radius point is attained by a covariant exponential channel. Source-
independent revealed flags attain all nonexposed points. The endpoints are Rn (1) = 0 and
Rn (0) = +∞.
Proof. For λ ≥ 0, conditional Gibbs duality and equation (14) give
                                                                        2
                        I(W ; U ) ≥ −λD − log sup Ee−λ∥W −A∥
                                                A∈Kn
                                                                    2
                                 = −λD − log sup e−λ(1+∥A∥ ) Zn (2λ, A).                        (18)
                                                A∈Kn

At fixed Euclidean radius, theorem 3.2 replaces A by a simple bQ without leaving Kn . Maximizing
over 0 ≤ b ≤ 1 yields equation (16) and the converse in equation (17).
    Let b > 0 be active at a finite field and put κ = 2λb. The endpoint b = 1 is not active: under
the finite tilted law X < 1 almost surely, so Kn′ (κ) < 1 and

                           ∂b [Kn (2λb) − λb2 ]b=1 = 2λ[Kn′ (2λ) − 1] < 0.

                                                    5
```

---

## Page 6

```text
Every positive active radius is therefore interior and satisfies

                                      b = Kn′ (κ),        κ = 2λb.                                (19)

      Draw Q Haar on Gn and specify the reverse channel

                                      dPκ (W | Q)   eκ⟨W,Q⟩
                                                  =         .                                     (20)
                                        dµ(W )       Ln (κ)
Covariance makes the source marginal Haar. The tilted mean is the gradient of the analytic
partition. At a simple external bivector, constrained stationarity in theorem 3.2 annihilates
every fixed-sphere tangential derivative, so the gradient is radial; this also excludes the apparent
additional ∗Q stabilizer direction in n = 4. Hence

                                    E(W | Q) = Kn′ (κ)Q = bQ.

The report is its posterior mean, so equality holds in equation (14) and equation (18). The
attained pair is
                         D(κ) = 1 − b(κ)2 ,   R(κ) = κb(κ) − Kn (κ).                    (21)
    If several radii are active at one field, an independently revealed flag mixes their covariant
channels. Every component retains the Haar source marginal; rate and distortion therefore mix
affinely. Danskin’s theorem identifies the subdifferential of the dual envelope with the convex hull
of these active distortions. The zero report attains (1, 0). To see the high-field endpoint explicitly,
Kn (t) ≤ t for t ≥ 0. Thus every b ≤ 1 − ε has radial objective at most λ(2b − b2 ) ≤ λ(1 − ε2 ),
whereas the feasible point b = 1 has value Kn (2λ) − λ = λ − (n − 2) log(2λ) + O(1) by theorem 9.1.
Every active radius therefore tends to one and its distortion tends to zero. Monotonicity of
convex subgradients covers (0, 1), and closure supplies both endpoints. Exact reconstruction of a
nonatomic positive-dimensional source requires infinite mutual information, giving Rn (0) = +∞.
Fenchel–Moreau duality proves equality everywhere.


7      Complete radial phase below dimension six
Let
                                                                      κ
                              mn (κ) = Kn′ (κ),          λn (κ) =           .
                                                                    2mn (κ)
A positive stationary radius satisfies b = mn (κ) and λ = λn (κ). Moreover
                                                 mn (κ) − κm′n (κ)
                                     λ′n (κ) =                     .                              (22)
                                                     2mn (κ)2
Lemma 7.1 (low-dimensional radial monotonicity). For n = 3, 4, 5 and every κ > 0,

                                         mn (κ) − κm′n (κ) > 0.                                   (23)

Proof. For n = 3, L3 (x) = sinh x/x. Multiplying equation (23) by the positive factor L3 (x)2 x3
reduces it to
                          J3 (x) = x2 + x sinh x cosh x − 2 sinh2 x > 0.
The coefficients below degree six vanish, and for r ≥ 3 the coefficient of x2r is

                                          22r−2 (2r − 4)
                                                         > 0.
                                              (2r)!
For n = 4, the identity
                                                           sinh(x/2) 2
                                                                   
                                         2(cosh x − 1)
                              L4 (x) =                 =
                                              x2              x/2

                                                     6
```

---

## Page 7

```text
reduces the assertion to the n = 3 inequality at x/2.
   For n = 5, L5 (x) = 6(sinh x − x)/x3 . After multiplication by the positive factor L5 (x)2 x7 /36,
equation (23) becomes
                          J5 (x) = x3 sinh x + x sinh x cosh x + 11x sinh x
                                     − 3x2 cosh x − 3x2 − 6 sinh2 x > 0.
The coefficients through degree eight vanish. For r ≥ 5, the coefficient of x2r multiplied by (2r)! is
                                    22r−1 (r − 6) + 8r(r2 − 3r + 4).
Indeed, substitute the Taylor series for sinh x, cosh x, and sinh x cosh x = 12 sinh(2x) into J5 . After
collecting the x2r terms over the common denominator (2r)!, the constant, quadratic, quartic,
sextic, and octic coefficients cancel identically, while the remaining numerator is exactly the
displayed expression. This makes the sign argument coefficientwise rather than numerical. It
equals 48 at r = 5; for r ≥ 6 both displayed contributions are nonnegative and the polynomial
one is positive.

Theorem 7.2 (complete continuous phase for n = 3, 4, 5). For n = 3, 4, 5, directional information
activates continuously at
                                               n(n − 1)
                                          λ0 =          .
                                                   4
For 0 ≤ λ ≤ λ0 , the zero radius is the unique global maximizer. For λ > λ0 , there is exactly one
positive global maximizer; it tends continuously to zero at the threshold. There is no coexistence,
later radial exchange, or reentrance.
Proof. By equation (22) and Lemma 7.1, λn (κ) is strictly increasing. The moment expansion
and the high-field limit give
                                          1      n(n − 1)
                        lim λn (κ) =           =          ,      λn (κ) −→ ∞.
                        κ↓0            2 Var X      4
There is no positive stationary radius below the threshold and exactly one above it. At λ > λ0
the zero radius is locally unstable, so the unique positive stationary point is the unique global
maximum; the endpoint b = 1 was excluded in the proof of theorem 6.1. Strict monotonicity
gives continuous emergence and rules out every later exchange.


8    A dimension-six discontinuity threshold
           n
            
Let N =    2 . From equation (12),

                                                  12(n2 − 5n − 2)
                               cum4 (X) =                               .                          (24)
                                             n2 (n − 1)2 (n + 1)(n + 2)
It is positive exactly for n ≥ 6.
    Define the radial free energy
                               ϕλ (b) = Kn (2λb) − λb2 ,      0 ≤ b ≤ 1.                           (25)
Since Kn′′ (0) = 1/N , the quadratic coefficient at b = 0 is λ(2λ/N − 1). The zero-radius spinodal
is λ0 = N/2.
Theorem 8.1 (discontinuous first directional activation). For every n ≥ 6, there is a field
0 < λc < λ0 at which b = 0 coexists with at least one positive global maximizer bc > 0 of
equation (25). Hence the onset of directional information is discontinuous and the RDF has an
exact linear time-sharing face adjacent to (D, R) = (1, 0).
    The theorem does not assert uniqueness of the positive contact or exclude later radial transi-
tions.

                                                   7
```

---

## Page 8

```text
Proof. At λ0 the quadratic term vanishes. The quartic term is cum4 (X)(2λ0 )4 b4 /24, which is
positive by equation (24); therefore maxb ϕλ0 (b) > 0. At small positive field, Hoeffding’s lemma
for the centered variable X ∈ [−1, 1] gives Kn (t) ≤ t2 /2, and thus

                                      ϕλ (b) ≤ (2λ2 − λ)b2 < 0

for 0 < λ < 1/2 and b > 0. The zero radius is then the unique maximizer.
    Let g(λ) = max0≤b≤1 ϕλ (b) and let λc be the infimum of fields where g is positive. Continuity
and compactness give 0 < λc < λ0 and a zero-value contact. Positive maximizing radii approaching
the contact cannot converge to zero: because λc < λ0 , the quadratic coefficient remains uniformly
negative near λc , and analyticity makes ϕλ (b) < 0 uniformly for all sufficiently small b > 0. A
subsequential contact radius therefore satisfies bc > 0. The two active channels have distortions
one and 1 − b2c ; source-independent flagged mixing produces the stated linear RDF face.

    Together, theorems 7.2 and 8.1 establish a sharp dimension-six change in the nature of first
activation. For n ≥ 6 we make no claim about uniqueness of the positive contact or later radial
transitions.


9    High-fidelity constant
Proposition 9.1 (exact leading asymptotics). Put q = n − 2. As κ → ∞,

                                          q! κ −q
                                                  1 + O(e−κ κq−1 ) .
                                                                  
                               Ln (κ) =     e κ                                                  (26)
                                          2
Consequently, as D ↓ 0,
                                                2q          q!
                               Rn (D) = q log      − q − log + o(1).                             (27)
                                                D           2
Proof. Use equation (11) and retain the endpoint x = 1:
                                                                 
                                                            q−1 j
                     q 1 κx
                       Z
                                             q!             X  κ
                          e (1 − x)q−1 dx = eκ κ−q 1 − e−κ       .
                     2 0                     2                 j!
                                                                    j=0


The e−κx half is exponentially smaller after the same scaling, which proves equation (26). Therefore

        Kn (κ) = κ − q log κ + log(q!/2) + o(1),       b = Kn′ (κ) = 1 − q/κ + O(e−κ κq−1 ).

Equation 21 gives D = 2q/κ + O(κ−2 ) and R = q log κ − q − log(q!/2) + o(1). Substitution yields
equation (27).

   The pre-log q = n−2 is half the manifold dimension 2(n−2), in agreement with high-resolution
geometry. The exact constant comes from the oriented positive-overlap cell; losing the factor 1/2
would fail the check L3 (κ) ∼ eκ /(2κ).


10     Diagnostics, special cases, and scope
For n = 3, Hodge duality identifies unit bivectors with S 2 , and L3 = sinh κ/κ reproduces the sphere.
For n = 4, Gr+      4     2    2
               2 (R ) ≃ S × S ; the constrained-gradient argument in theorem 6.1 is included
precisely so that this reducible stabilizer geometry cannot introduce a hidden posterior-mean
component. In n = 6, the exceptional isomorphism Spin(6) ≃ SU (4) relates the oriented-plane
orbit to GrC (2, 4). The present theorem explains why the simple skew block appears there and
extends that mechanism to every real dimension without relying on the exceptional isomorphism.


                                                   8
```

---

## Page 9

```text
Exact Plucker-overlap laws                                      Covariant branches; dots mark coexistence
       3.0                                                                       14
                                              n=3       n   =6                                                            n=3         n=6
                                              n=4       n   =8                   12                                       n=4         n=7
       2.5                                    n=5                                                                         n=5         n=8

                                                                                 10
       2.0




                                                                 rate R (nats)
                                                                                  8
       1.5
()
fn x




                                                                                  6
       1.0
                                                                                  4
       0.5
                                                                                  2
       0.0
                                                                                  0
             −1.00 −0.75 −0.50 −0.25 0.00 0.25 0.50 0.75 1.00                      0.0       0.2       0.4          0.6         0.8         1.0
                                overlap x = ⟨W, Q⟩                                                       distortion D


Figure 1: Left: the exact overlap densities from theorem 4.1. Right: covariant parametric branches
from equation (21). For n ≥ 6, dots mark numerically replayed coexistence contacts and dashed
segments show their rigorously guaranteed time-sharing faces. The plot is diagnostic; the all-field,
RDF, and onset statements are analytic.


    The operational object here is a signed Plücker label. It can represent an oriented plane or an
antisymmetric area coordinate, and squared loss is integrated squared error over an orthonormal
basis of linear Plücker queries. This is not automatically a quantum-state RDF: a physical ray
identifies global sign, and Born probabilities square amplitudes, changing both the sufficient
statistic and the loss. We therefore make no claim about intrinsic randomness, measurement
update, click simulation, or a derivation of Born’s rule.

Reproducibility. The release includes two bounded scripts. The first independently checks
the exact moments, norm constants, and Monte Carlo normalization. The second evaluates only
the one-dimensional beta integral, records diagnostic contacts, and generates figure 1. From the
workspace root:

python work/eleventh_paper/verify_oriented_plucker_rdf.py --samples 60000
python work/eleventh_paper/reproduce_plucker_frontier.py

Both are diagnostic replays; no numerical result is used in the analytic proofs. The release
freezes the two scripts and their two JSON outputs in work/eleventh_paper/release/REPLAY_
MANIFEST.sha256. The manifest itself has SHA–256
                     16be07c5377ecd94b78a9d230341664c832be893394a71c55e2bc0719b89d6f7.

This content address, rather than a mutable working-tree path, identifies the replay used for the
release.


11            Conclusion
The linear Plücker orbit of an oriented two-plane admits a dimension-uniform rigidity theorem:
at fixed exterior norm, every linear exponential moment is globally and uniquely maximized by a
simple external bivector. A positive complete-homogeneous series makes the result elementary
and exposes an exact beta overlap law. Combining that spectral envelope with the full Grassmann
orbitope yields the unrestricted all-distortion Shannon RDF, including covariant attainment and
nonexposed time sharing. In dimensions six and above, the fourth cumulant forces a discontinuous
first directional activation; at high fidelity the complete constant is explicit.


                                                                 9
```

---

## Page 10

```text
The remaining radial question is deliberately separated from what is proved. Dimensions 3, 4, 5
are completely classified, but for n ≥ 6 we have not classified every later stationary branch or
established no reentrance. A full high-dimensional radial uniqueness theorem would sharpen the
scalar representation, but it is not needed for the exact variational RDF or the discontinuous-onset
result proved here.


References
 [1]   Wei Dai, Youjian Liu, and Brian Rider. “Quantization Bounds on Grassmann Manifolds of
       Arbitrary Dimensions and MIMO Communications with Feedback”. In: IEEE Transactions
       on Information Theory 54.3 (2008), pp. 1108–1123. doi: 10.1109/TIT.2007.915691. arXiv:
       0705.2272 [cs.IT].
 [2]   Erwin Riegler, Günther Koliander, and Helmut Bölcskei. “Lossy Compression of General
       Random Variables”. In: Information and Inference: A Journal of the IMA 12.3 (2023),
       pp. 1759–1829. doi: 10.1093/imaiai/iaac035. arXiv: 2111.12312 [cs.IT].
 [3]   Saqib Riasat and Hessam Mahdavifar. “Covering in Hamming and Grassmann Spaces: New
       Bounds and Reed–Solomon-Based Constructions”. In: (2026). Preprint, revised 2026. arXiv:
       2512.22911 [cs.IT].
 [4]   T. D. Downs. “Orientation Statistics”. In: Biometrika 59.3 (1972), pp. 665–676. doi:
       10.1093/biomet/59.3.665.
 [5]   C. G. Khatri and K. V. Mardia. “The von Mises–Fisher Matrix Distribution in Orientation
       Statistics”. In: Journal of the Royal Statistical Society: Series B 39.1 (1977), pp. 95–106.
       doi: 10.1111/j.2517-6161.1977.tb01610.x.
 [6]   Yasuko Chikuse. “Concentrated Matrix Langevin Distributions”. In: Journal of Multivariate
       Analysis 85.2 (2003), pp. 375–394. doi: 10.1016/S0047-259X(02)00065-9.
 [7]   Raman Sanyal, Frank Sottile, and Bernd Sturmfels. “Orbitopes”. In: Mathematika 57.2
       (2011), pp. 275–314. doi: 10.1112/S002557931100132X. arXiv: 0911.5436 [math.MG].
 [8]   Alexander Barvinok and Grigoriy Blekherman. “Convex Geometry of Orbits”. In: Combina-
       torial and Computational Geometry. Ed. by Jacob E. Goodman, János Pach, and Emo Welzl.
       Vol. 52. Mathematical Sciences Research Institute Publications. Cambridge: Cambridge
       University Press, 2005, pp. 51–77. arXiv: math/0312268.
 [9]   Peter Harremoës. “Maximum Entropy on Compact Groups”. In: Entropy 11.2 (2009),
       pp. 222–237. doi: 10.3390/e11020222. arXiv: 0901.0015 [cs.IT].
[10] Toby Berger. Rate Distortion Theory: A Mathematical Basis for Data Compression. Engle-
     wood Cliffs, NJ: Prentice-Hall, 1971.
[11] Imre Csiszár. “On an Extremum Problem of Information Theory”. In: Studia Scientiarum
     Mathematicarum Hungarica 9 (1974), pp. 57–71.
[12] Alex Dytso and Martina Cardone. “The Rate-Distortion Function of the Uniform Distribu-
     tion on the Sphere”. In: 2024 IEEE International Symposium on Information Theory. 2024,
     pp. 873–878. doi: 10.1109/ISIT57864.2024.10619427. arXiv: 2401.04248 [cs.IT].
[13] Harish-Chandra. “Differential Operators on a Semisimple Lie Algebra”. In: American
     Journal of Mathematics 79.1 (1957), pp. 87–120. doi: 10.2307/2372387.
[14] Colin McSwiggen. “The Harish-Chandra Integral: An Introduction with Examples”. In:
     L’Enseignement Mathématique 67.3–4 (2021), pp. 229–299. doi: 10.4171/LEM/1017. arXiv:
     1806.11155 [math.RT].




                                                10
```
