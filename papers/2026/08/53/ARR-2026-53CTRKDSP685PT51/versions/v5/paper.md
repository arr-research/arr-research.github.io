# The Schwarzian Bridge in a Single Sigmoid Neuron: Oracle Gram Resolution, Joint Spectral Lexicography, and Spherical Saturation Phases

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
The Schwarzian Bridge in a Single Sigmoid Neuron
 Oracle Gram Resolution, Joint Spectral Lexicography, and Spherical
                        Saturation Phases

                                      Lluis Eriksson
                                  Independent Researcher
                                lluiseriksson@gmail.com

                                            August 2026


                                                Abstract
      A sigmoid is increasing on scalars, yet its bend controls two different geometries.
  The classical Schwarzian criterion implies that a negative-Schwarzian activation is not
  matrix-monotone of order two. We give a closed logistic formula showing every distinct two-
  point Löwner determinant to be negative, a dimension-minimal 2 × 2 positive-semidefinite
  perturbation witness certified with interval arithmetic, and the corresponding classical
  serial-chain consequence.
      Our central link is that the same local invariant determines the leading quadratic onset
  coefficient of saturation anisotropy. At a centered inflection of an increasing activation g,
  for a sensitivity hp = (g 0 )p and isotropic spherically symmetric input X,

                                                                           EkXk4
                    κp,X (r) = 1 − qX p Sg(0)r2 + O(r4 ),           qX =            .
                                                                           d(d + 2)

  The Gaussian coefficient is the special case qX = 1. The adjacent-point Löwner determinant
  is g 0 (0)2 Sg(0)δ 2 /6 + O(δ 3 ). Negative Schwarzian therefore simultaneously gives local
  noncommutative order failure and positive initial radial–tangential anisotropy. We turn
  the equality of limits into a finite-scale inequality with explicit constants determined by
  derivative suprema and input moments.
      For isotropic Gaussian inputs in dimension d ≥ 2, population curvature at a teacher
  of norm r has one radial eigenvalue and d − 1 equal tangential eigenvalues. For any
  nonnegative sensitivity profile h with finite defining expectations, these eigenvalues are
  exactly
                    αh (r) = Eh(rZ),       βh (r) = E[Z 2 h(rZ)],  Z ∼ N (0, 1),
  and, if its zeroth and second Lebesgue moments are finite and positive,

                                        ϕ(0)m0                     ϕ(0)m2
                            αh (r) ∼           ,        βh (r) ∼          .
                                           r                         r3
  Thus saturation suppresses magnitude information by two additional powers: the radial–
  tangential ratio obeys αh (r)/βh (r) ∼ (m0 /m2 )r2 . For every real p > 0 and hp = σ 0p , we
  prove strict monotonicity and the unified identities

              Γ(p)2                   r2                       p    p     p(p + 1) 6
   m0 (p) =         ,    κp (r) ∼           ,      κp (r) = 1 + r2 − r4 +         r + O(r8 ).
              Γ(2p)                 2ψ1 (p)                    2    8        16

  For n samples we prove an explicit two-sided relative Löwner bound for the fixed-teacher
  oracle weighted Gram matrix. A conditional-Gaussian lower bound shows that the sample
  complexity of this specific loss is sharply
                                                          
                                           r[d + log(1/δ)]
                                      Θp                     .
                                                  ε2

                                                    1
```

---

## Page 2

```text
The factor rd is intrinsic: a tangential off-diagonal column has d − 2 coordinates and
        normalized variance of order r/n. We also give a uniform full-dyadic-shell extension and
        concrete sufficient constants√C1 = 22929 and C2 = 294162. A marked angular-process
        lower bound proves that a log R penalty is intrinsic for shell uniformity in its stated
        iterated limit, although a matching finite-sample chaining theorem remains open. The
        weaker bottom-eigenspace target has a different extreme-saturation law: its empirical
        projector converges to the normal of the d − 1 samples nearest the transition hyperplane,
        with exact angle distribution tan θ∞ = kζk/|G|, matching Θ(d3/2 /ε) complexity at fixed
                                                 d

        nondegenerate confidence, and matching 1/δ dependence in the theorem’s stated confidence
        range. We then leave the iterated limit: a deterministic hierarchy lemma and half-normal
        spacing, Gaussian invertibility and operator-norm bounds yield, with probability at least
        1 − δ, an explicit finite-saturation certificate
                                                                               
                            bot                p 2       3 2    −2          prδ
                        kPr − P∞ kop ≤ 9 4 c+ (d − 1) Mn,d,δ δ exp −
                          b                                                       ,
                                                                          3c+ n

        whenever the right side is below one. Combined with the exact angle law, this gives a
        simultaneous finite (r, n, d, ε, δ) recovery theorem. The rate is deliberately conservative
        and does not claim the optimal crossover.
           The quadratic saturation law extends beyond Gaussian inputs. If X = RU is isotropic
        spherical, ER−1 < ∞, then
                                             m0 2                      ER
                               κh (r) ∼ QR      r ,       QR =                .
                                             m2                   (d − 1)ER−1

        Gaussian, fixed-sphere and isotropic Student inputs give respectively QR = 1, d/(d − 1)
        and (ν − 2)/(ν − 1). For radii with density fR (ρ) ∼ cρa−1 at zero, we prove exact leading
        constants in all three phases: r−(a+2) for 0 < a < 1, r−3 log r at a = 1, and r−3 for a > 1.
        An autonomous Abelian kernel lemma handles the critical boundary, and deterministic
        quadrature exhibits all three phases. We also give an isotropic Rademacher counterexample.
        These claims refine, but do not replace, prior one-sided and bilateral Hessian results and
        recent labeled-estimation theory. Deterministic replays, a fixed-seed finite-sample phase
        diagram and an immutable public source record accompany the proofs.

Keywords. single neuron; sigmoid; matrix monotonicity; Löwner order; Schwarzian deriva-
tive; Fisher information; spherical design; weighted sample covariance; finite-sample concentra-
tion.


1     Question, result, and claim boundary
The scalar logistic curve is
                                          1                       1
                              σ(s) =           ,      σ 0 (s) =     sech2 (s/2).
                                       1 + e−s                    4
It is strictly increasing, so larger scalar scores produce larger outputs. We first ask whether
this order survives spectral functional calculus on noncommuting matrices. It does not, at the
smallest possible matrix size and on every interval. We then return to the ordinary teacher
neuron σ(w?> X) with X ∼ N (0, Id ). There, a perturbation perpendicular to w? rotates the
separating hyperplane, while a parallel perturbation changes its confidence scale and must
be detected through samples near the transition layer. Our goal is to compute both failures
exactly.
    The main contributions are:

    1. a closed logistic specialization of the classical negative-Schwarzian obstruction, proving
       directly that every nontrivial two-point Löwner matrix is indefinite;

                                                      2
```

---

## Page 3

```text
2. a dimension-minimal 2 × 2 witness A  B but σ(A)  σ(B), with outward-rounded
       eigenvalue certification, and a Löwner-order reformulation of the known serial-composition
       consequence;

    3. a spherical-input Schwarzian bridge equating the local order defect with the leading
       radial–tangential anisotropy, including its exact fourth-moment multiplier qX ;

    4. an explicit finite-scale bridge bounding the discrepancy between the normalized Löwner
       determinant and anisotropy at nonzero (δ, r);

    5. a profile-generic two-eigenvalue refinement under Gaussian design, with finite-r brackets
       and, for every p > 0, closed moments, strict ratio monotonicity and exact endpoint laws
       for hp = σ 0p ;

    6. a two-sided relative concentration theorem for the fixed-teacher oracle sensitivity matrix,
       with a matching r[d + log(1/δ)]/ε2 lower bound for bilateral relative Loewner loss, explicit
       constants for p = 1, 2, an autonomous high-confidence lower-tail lemma, a uniform full-
               √ extension, and an iterated marked-process lower bound proving that its
       dyadic-shell
       angular log R penalty is intrinsic;

    7. spectral-lexicography theorems for the weaker bottom-eigenspace target: a fully sep-
       arated deterministic exterior-power flag lemma, an exact Gaussian-inverse angle law,
       matching Θ(d3/2 /ε) complexity at fixed nondegenerate confidence, and an explicit joint
       finite-(r, n, d, δ) certificate for convergence to the selected-sample normal and then to the
       teacher direction;

    8. a spherical saturation theorem with exact asymptotic radius factor QR , an elliptical
       whitening corollary, and exact constants and a critical logarithmic law for radii regularly
       varying at zero; and

    9. exact local consequences for stationary fixed-step optimization and estimation, plus a
       documented replay sequence of the identities, interval witness, inequalities, and figure.

    The matrix-order theorem concerns spectral functional calculus σ(A), not entrywise activa-
tion of a vector. The radial theorem is not a claim about deep networks, global optimization,
implicit bias, or arbitrary inputs. Its local coefficient and its large-saturation law extend
from Gaussian to spherical inputs under different, stated moment hypotheses. The two ques-
tions meet at a precise boundary: scalar monotonicity controls neither noncommuting PSD
perturbations nor the conditioning of parameter directions.


2      A sigmoid is not an order-preserving operator
For Hermitian matrices, A  B means that B − A is positive semidefinite. A scalar function
f is matrix-monotone of order two on an interval J if f (A)  f (B) for every pair of 2 × 2
Hermitian matrices with spectra in J and A  B, where f (A) is defined by spectral functional
calculus. If A and B commute, scalar monotonicity is sufficient because they are simultaneously
diagonalizable. The question is what happens without commutativity.
    For distinct x, y ∈ J, define the two-point Löwner matrix

                                                          f (x) − f (y)
                                                                       
                                              f 0 (x)
                            Lf (x, y) =  f (x) − f (y)       x−y                               (1)
                                                                        .
                                                                       
                                                               0
                                                              f (y)
                                             x−y


                                                   3
```

---

## Page 4

```text
The fixed-order Löwner criterion says that matrix monotonicity of order two requires Lf (x, y) 
0 for every pair [1, 2]. The equivalent local criterion Sf ≥ 0 for increasing smooth functions
is classical [3, Lemma 10]; the result below is an explicit logistic specialization, not a new
qualitative matrix-monotonicity criterion.
    Cook, Hammerlindl and Tucker define
                                                                               2
                                             0    0               x−y
                              χf (x, y) = f (x)f (y)
                                                              f (x) − f (y)

and study the class χf ≤ 1, including sigmoid activations and serial compositions [4]. If
Df (x, y) = (f (x) − f (y))/(x − y), then

                              det Lf (x, y) = Df (x, y)2 [χf (x, y) − 1].                              (2)

Thus their two-point inequality is algebraically the nonpositive Löwner-determinant inequality.
Our contribution in this subsection is the strict closed logistic identity and the certified matrix
witness, not the underlying Schwarzian/composition mechanism.

Theorem 2.1 (closed logistic two-point determinant). Let
                                                  1
                                sα,b (x) =                    ,            α > 0.
                                             1 + e−α(x−b)
For every x 6= y, the Löwner matrix Lsα,b (x, y) has negative determinant. Consequently the
logistic activation is not matrix-monotone of order two on any nondegenerate interval.

Proof. Put u = eα(x−b) , v = eα(y−b) , and r = v/u = eα(y−x) . Direct cancellation gives the
exact identity
                                              α2 u2             (r − 1)2
                                                                        
                    det Lsα,b (x, y) =                      r −            .              (3)
                                        (1 + u)2 (1 + v)2       (log r)2
For r 6= 1, write t = log r. Strict convexity of sinh on (0, ∞) gives
                                                                  √
                         |r − 1| = 2et/2 | sinh(t/2)| > et/2 |t| = r | log r|.

The bracket in (3) is therefore strictly negative. Every nondegenerate interval contains a
distinct pair, so the Löwner criterion completes the proof.

    This is stronger than finding one bad scale: changing the slope α, shifting the bias b,
or restricting the score range never removes the obstruction. It also identifies the precise
failure. The diagonal entries in (1) are positive, but the divided difference is too large for their
geometric mean.

Proposition 2.2 (dimension-minimal explicit PSD witness). For the standard logistic sigmoid,
let                                                           
                           −1/2 0                      1    1 1
                    A=                 ,     B =A+                 .                     (4)
                            0    1/2                  100 1 1
Then A  B but σ(A)  σ(B). At 256-bit outward-rounded Arb precision,

                       spec(B) ⊂ [−0.4901000, −0.4900999] ∪ [0.5100999, 0.5101000],                    (5)
           spec(σ(B) − σ(A)) ⊂ [−9.9150, −9.9147] 10              −5
                                                                           ∪ [0.0047990, 0.0047992],   (6)
            det(σ(B) − σ(A)) ∈ [−4.7583, −4.7581] 10              −7
                                                                       .                               (7)




                                                      4
```

---

## Page 5

```text
Proof. B − A has eigenvalues 0 and 1/50. If a = 1/2, ε = 1/100, and d = (a2 + ε2 )1/2 , then B
has eigenvalues λ± = ε ± d and

                                               σ(λ+ ) + σ(λ− )                σ(λ+ ) − σ(λ− )
           σ(B) = mI + n(B − εI),        m=                    ,         n=                   .
                                                      2                             2d
Substitution reduces the three enclosures to scalar exponential and square-root balls. The
replay evaluates them with directed Arb rounding; the negative eigenvalue in (6) proves the
claim.

   The witness is illustrative, while Theorem 2.1 is the proof for every interval. The derivative
form also explains why an indefinite Löwner matrix produces witnesses: for diagonal A =
diag(x, y), the Fréchet derivative in the all-ones PSD direction is precisely the Schur product
with Lf (x, y).

2.1   Serial depth does not repair the order
For a C 3 function with nonzero derivative, its Schwarzian is
                                                                2
                                          f 000 3        f 00
                                                     
                                      Sf = 0 −                       .                             (8)
                                           f    2        f0

The logistic sigmoid and a scaled hyperbolic tangent satisfy

                                      α2
                          Ssα,b = −      ,     S tanh(αx + β) = −2α2 .                             (9)
                                      2
Corollary 2.3 (serial spectral reformulation). Let F be a finite scalar composition of positive-
slope affine maps and at least one increasing logistic or hyperbolic-tangent activation. Then
SF < 0 everywhere, and F is not matrix-monotone of order two on any nondegenerate interval.

Proof. The composition identity

                                 S(f ◦ g) = (Sf ◦ g)(g 0 )2 + Sg                                  (10)

and (9) give SF < 0, since positive affine maps have zero Schwarzian and all derivatives in the
chain are positive. For h → 0, Taylor expansion of the two-point determinant gives

                                               F 0 (x)2
                         det LF (x, x + h) =            SF (x) h2 + O(h3 ).                       (11)
                                                   6
It is negative for all sufficiently small nonzero h. Every interval contains such a pair.

    The corollary restates, in spectral Löwner order, the serial closure proved in the nowhere-
coexpanding framework [4]. It is deliberately about serial scalar chains. It does not cover
sums of neurons, skip connections, multivariate architectures, or entrywise coordinate order.
Its content is that composing more of the same S-shaped bend cannot turn the resulting scalar
function into a PSD-order-preserving spectral activation.


3     Two models, one sensitivity matrix
Write r = kw? k and u = w? /r when r > 0. We use two standard observation models.




                                                 5
```

---

## Page 6

```text
Squared-output regression.           For the realizable population loss
                                        1 
                                                                                              (12)
                                                             2
                               Lsq (w) = E σ(w> X) − σ(w?> X) ,
                                        2
the residual vanishes at w? , so its Hessian is the Gauss–Newton matrix

                                 Hsq (w? ) = E σ 0 (w?> X)2 XX > .                            (13)
                                                               


The same matrix, divided by a known output-noise variance τ 2 , is the Fisher information of
Y = σ(w?> X) + ε, ε ∼ N (0, τ 2 ).

Bernoulli logistic neuron. If Y | X ∼ Bernoulli(σ(w?> X)), the expected negative-log-
likelihood Hessian and the Fisher information coincide:

                               HB (w? ) = E σ 0 (w?> X)XX > .                   (14)
                                                          


    Both are instances of the sensitivity matrix

                          Hh (r, u) := E h(ru> X)XX > ,                                       (15)
                                                    
                                                                   h ≥ 0.

The power of the reduction below is that no high-dimensional integration remains.
    Amari, Karakida and Oizumi already derived the exact one-unit Gaussian Fisher decompo-
sition for h = φ02 , including the radial–tangential split and the bias block [25]. We do not claim
that decomposition or the squared-output branch as new. For the Bernoulli profile h = σ 0 ,
Chen and Mazumdar recently identified the same radial and orthogonal Hessian functions and
proved their r−3 and r−1 orders in a finite-sample analysis  p of logistic regression [16]. Their
follow-up proves the minimax norm-estimation rate Θ( r3 /n) [17]. We do not claim those
exponents or the Bernoulli optimization penalty as new. The purpose of the next sections is to
isolate the profile-generic mechanism, give finite-radius brackets and exact logistic constants,
prove strict monotonicity of both eigenvalue ratios, and connect their small-r coefficients to
the Schwarzian order defect.


4    Universal Gaussian saturation theorem
Let ϕ(z) = (2π)−1/2 e−z /2 and define the even sensitivity moments
                          2


                                       Z
                             mj (h) :=    tj h(t) dt (j = 0, 2, 4),
                                            R

whenever finite. Evenness of h is not needed for the spectral reduction or leading asymptotics,
but it holds in our sigmoid applications and makes the interpretation symmetric.

Theorem 4.1 (exact spectrum and finite-r brackets). Let d ≥ 2, X ∼ N (0, Id ), r > 0,
u ∈ S d−1 , and let h : R → [0, ∞) be measurable with E[(1 + Z 2 )h(rZ)] < ∞. Then

                              Hh (r, u) = αh (r)(I − uu> ) + βh (r)uu> ,                      (16)

where
                 αh (r) = Eh(rZ),         βh (r) = E[Z 2 h(rZ)],     Z ∼ N (0, 1).            (17)
If m0 , m2 < ∞ and are positive, then

                        ϕ(0)m0                   ϕ(0)m2                  αh (r)   m0 2
             αh (r) ∼          ,      βh (r) ∼          ,    κh (r) :=          ∼    r .      (18)
                           r                       r3                    βh (r)   m2

                                                   6
```

---

## Page 7

```text
If m0 , m2 , m4 < ∞, the following nonasymptotic brackets hold for every r > 0:
                             ϕ(0)       m2             ϕ(0)m0
                                    m0 − 2 ≤ αh (r) ≤            ,                             (19)
                               r         2r                 r
                             ϕ(0)       m4             ϕ(0)m2
                                3
                                    m2 −    2
                                              ≤ βh (r) ≤         .                             (20)
                              r          2r                r3
Negative lower endpoints are interpreted as valid but uninformative bounds.
Proof. Decompose X = Zu + Y , where Z ∼ N (0, 1), Y ∼ N (0, I − uu> ), and Z, Y are
independent. The mixed terms vanish and EY Y > = I − uu> , giving (16)–(17). Changing
variables t = rz gives the exact one-dimensional formulae
                           Z                                  Z
                      ϕ(0)                               ϕ(0)
                                                                                       (21)
                                     2    2                                2    2
             αh (r) =         h(t)e−t /(2r ) dt, βh (r) = 3      t2 h(t)e−t /(2r ) dt.
                       r    R                             r    R

Dominated convergence proves (18). Finally, 1 − x ≤ e−x ≤ 1 for x ≥ 0 inserted into (21)
proves (19)–(20).


5    Spherical saturation beyond Gaussian design
The Gaussian density at the transition hyperplane is not the essential constant. Let X = RU
be spherically symmetric, where U is uniform on S d−1 and independent of the radius R.
Isotropy is exactly ER2 = d. Write
                                    Γ(d/2)                             ER
                        cd = √                  ,       QR =                  .
                                 π Γ((d − 1)/2)                   (d − 1)ER−1
Theorem 5.1 (spherical saturation with exact asymptotic constants). Let d ≥ 2, R > 0
almost surely, ER2 = d and ER−1 < ∞. Let h ≥ 0 have 0 < m0 , m2 < ∞. For d = 2,
additionally assume h(t) ≤ Ce−a|t| ; no additional condition is needed when d ≥ 3. Then
                             cd ER m0                                             m2
                 αh,X (r) ∼            ,                    βh,X (r) ∼ cd ER−1       ,         (22)
                             d−1 r                                                r3
                                 m0 2
                  κh,X (r) ∼ QR     r .                                                        (23)
                                 m2
For hp = σ 0p and every p > 0,
                                                     QR 2
                                       κp,X (r) ∼           r .                                (24)
                                                    2ψ1 (p)
Proof. Put T = u> U . Its density is cd (1 − t2 )(d−3)/2 1(−1,1) (t), and conditional on T = t every
unit transverse coordinate has second moment (1 − t2 )/(d − 1). Changing variables s = rRT
gives the exact identities
                                       " Z                            (d−1)/2 #
                                                                s2
                                                        
                                  cd
                   rαh,X (r) =        E R          h(s) 1 − 2 2               ds ,              (25)
                                d−1         |s|<rR            r R
                                    "                                 (d−3)/2 #
                                                                   2
                                         Z              
                                                                  s
                  r3 βh,X (r) = cd E R−1         s2 h(s) 1 − 2 2               ds .             (26)
                                          |s|<rR               r R

The first integrand is dominated by Rm0 . For d ≥ 3 the second is dominated by R−1 m2 .
For d = 2, splitting its inner integral at |s| = rR/2 gives a uniform bound from exponential
localization; the boundary contribution is bounded by a constant times (rR)3 e−arR/2 . Domi-
nated convergence proves (22). The ratio and the identity m0 (p)/m2 (p) = 1/[2ψ1 (p)] prove
the rest.

                                                    7
```

---

## Page 8

```text
The factor QR is the conditional transverse variance on the transition hyperplane. It is
distribution sensitive and satisfies 0 < QR ≤ d/(d − 1). Three closed examples are

                 isotropic spherical law                 radius            QR
                 N (0, Id )  √                            χd
                                                          √                  1
                 uniform on dS d−1                   √      d            d/(d − 1)
                 isotropic Student tν , ν > 2          ν − 2 χd /χν   (ν − 2)/(ν − 1)

The last line follows from the adjacent chi-moment identities. If X = AS with A invertible
and S isotropic spherical, then exactly

                         Hh,X (w) = AHh,S (kA> wk, A> w/kA> wk)A> .

Thus the theorem transfers to elliptical inputs after whitening; in Euclidean coordinates it is
a generalized eigenvalue statement relative to AA> , not generally a literal radial–tangential
eigendecomposition.
    We now make the inverse-radius boundary exact. The following elementary Abelian lemma
is the only transition calculus needed. It is stated separately so that the critical logarithm and
its coefficient can be checked without appealing to an unnamed regular-variation theorem.
Lemma 5.2 (spherical
                R 2 transition kernel). Let d ≥ 2, let h : R → [0, ∞) be bounded, and
suppose 0 < m2 = R s h(s) ds < ∞. For q > 0 define
                                    Z 1
                         Jd,h (q) =     t2 h(qt)(1 − t2 )(d−3)/2 dt.
                                           −1

When d = 2, additionally assume h(s) ≤ Ce−λ|s| ; no extra condition is needed for d ≥ 3. Then
                                          Z x
                      3
                     q Jd,h (q) −→ m2 ,         q 2 Jd,h (q) dq ∼ m2 log x.               (27)
                                                     0

For every 0 < a < 1, writing Ma+1 (h) = R |s|a+1 h(s) ds, one moreover has
                                             R

                  Z ∞                                    
                                       1    1−a d−1
                        a+1
                      q Jd,h (q) dq = B           ,         Ma+1 (h) < ∞.                      (28)
                   0                   2      2       2
Proof. For d ≥ 3, the change s = qt gives
                                       Z q              (d−3)/2
                                                     s2
                                                 
                            3                    2
                           q Jd,h (q) =    s h(s) 1 − 2          ds.
                                        −q           q

The integrand is bounded by s2 h(s) and converges pointwise to it, proving the first limit by
dominated convergence. For d = 2, split the last integral at |s| = q/2. Dominated convergence
applies on the inner part, while the outer part is O(q 3 e−λq/2 ) after returning to the t variable.
The same split gives J2,h (q) = O(q −3 ). Hence in every dimension q 2 Jd,h (q) = m2 /q + o(q −1 ),
whose logarithmic integral proves the second limit. For (28), Tonelli’s theorem and s = q|t|
give
                    Z ∞                              Z 1
                          a+1
                         q Jd,h (q) dq = Ma+1 (h)        t−a (1 − t2 )(d−3)/2 dt
                     0                                0
                                                              
                                           1    1−a d−1
                                         = B           ,         Ma+1 (h).
                                           2       2      2
Boundedness of h controls the origin, while Ma+1 (h) < ∞ follows from a + 1 < 2 and the
assumed second moment. This also proves finiteness directly.

                                                     8
```

---

## Page 9

```text
Theorem 5.3 (exact three-phase inverse-radius boundary). Let d ≥ 2, X = RU be isotropic
spherical, and let the positive radius have a density satisfying

                     fR (ρ) = cρa−1 (1 + o(1))    (ρ ↓ 0),       c > 0, a > 0,             (29)

and ER2 = d. Let h : R → [0, ∞) be bounded with 0 < m0 , m2 < ∞; when d = 2, additionally
assume exponential localization as in Lemma 5.2. Put
                                                         
                cd ER                    cd c     1−a d−1
       Ad,h,R =       m0 ,      Da,d,h =      B      ,      Ma+1 (h) (0 < a < 1).
                d−1                       2        2   2

No assumption on the density away from zero is imposed beyond the displayed isotropic second
moment. Then
                                   αh,X (r) ∼ Ad,h,R r−1 ,                               (30)
and the radial eigenvalue has the exact three-phase law
                                     
                                     
                                      Da,d,h r−(a+2) , 0 < a < 1,
                                     
                                     
                          βh,X (r) ∼ cd c m2 r−3 log r, a = 1,                             (31)
                                     
                                     
                                       cd ER−1 m2 r−3 , a > 1.
                                     
                                     

Consequently                      
                                  
                                  (Ad,h,R /Da,d,h )ra+1 , 0 < a < 1,
                                  
                                                 r2
                                  
                                   ER m0
                                  
                        κh,X (r) ∼ (d − 1)cm2 log r ,      a = 1,                          (32)
                                  
                                                 m0 2
                                  
                                  
                                        ER
                                                     r , a > 1.
                                    (d − 1)ER−1 m2
                                  

Thus ER−1 < ∞ is exactly the quadratic-phase boundary inside the class (29).

Proof. The identity (25) is dominated by Rm0 . Since ER < ∞ follows from isotropy, dominated
convergence proves (30) for every a > 0.
   For the radial direction, direct conditioning on R = ρ and then putting q = rρ gives

                                       cd ∞
                                          Z
                             βh,X (r) = 3      fR (q/r)q 2 Jd,h (q) dq.                 (33)
                                       r 0

Fix η > 0 small enough that (29) supplies fR (ρ) ≤ Cρa−1 on (0, η). The contribution of R ≥ η
obeys, directly from (26),
                                                                                          (34)
                                       (R≥η)
                                   r3 βh,X (r) ≤ Cd,h /η.
For d ≥ 3 one may take Cd,h = cd m2 . For d = 2, the split in Lemma 5.2 proves that q 3 J2,h (q)
is uniformly bounded; hence one may take

                                    C2,h = cd sup q 3 J2,h (q)
                                                 q>0

directly.
    Suppose first that 0 < a < 1. On q < ηr, the integrand of ra+2 β/cd converges pointwise
to cq a+1 Jd,h (q) and is bounded by Cq a+1 Jd,h (q). Lemma 5.2 makes this majorant integrable.
Dominated convergence and (34), whose scaled contribution is O(ra−1 ), yield
                                             Z ∞
                           a+2
                          r βh,X (r) −→ cd c       q a+1 Jd,h (q) dq = Da,d,h .
                                             0


                                                 9
```

---

## Page 10

```text
At a = 1, for every  > 0 one may decrease η so that c −  ≤ fR (ρ)     R ηr ≤2 c +  on (0, η).
Therefore the small-radius part in (33) is squeezed between c ±  times 0 q Jd,h (q) dq. The
second limit in (27) and the O(1) tail bound (34), followed by  ↓ 0, prove r3 β/(log r) → cd cm2 .
    Finally, a > 1 makes ER−1 < ∞: local integrability follows from ρ−1 fR (ρ)  ρa−2 , and
the part above any fixed radius is automatic. Theorem 5.1 proves the last line. Dividing (30)
by (31) proves (32).

    For a concrete isotropic family in every phase, let
                                                      p
                         Q ∼ Gamma(a, 1),       R = d/[a(a + 1)] Q.

Then ER2 = d and c = {Γ(a)[d/(a(a + 1))]a/2 }−1 . Figure 1 evaluates the defining integrals for
a ∈ {1/2, 1, 2} and normalizes by the constants in (31); it is a diagnostic of all three limits,
not evidence used by the proof.

                                                         Three inverse-radius phases (d = 3, h = σ )           0




                                             1.0
     β(r) divided by its exact leading law




                                             0.9

                                             0.8

                                             0.7

                                             0.6

                                             0.5                                         a   = 0.5 (subcritical)   a= 2 (integrable)
                                                                                         a   = 1 (critical)        asymptotic limit
                                                   101    102                103                           104                105
                                                                        teacher norm r

Figure 1: Exact spherical phase normalizations for d = 3, h = σ 0 , and isotropic Gamma radii.
Every curve tends to one under its theorem-specific normalization; the slow approach, especially
in the critical a = 1 regime, is part of the predicted asymptotics. Values are deterministic
adaptive quadrature.

    Covariance isotropy alone still does not force any phase law. For independent Rademacher
coordinates, u = e1 and even h, one has Hh (r, u) = h(r)Id and hence κ = 1: here X12 = 1, all
mixed expectations vanish by sign symmetry, and h(rX1 ) = h(r).
    The radius–direction representation is classical [7]; non-Gaussian reference exponents also
appear in regular-design logistic theory [18]. The contribution here is the exact QR constant, its
all-p logistic specialization, and the sharp inverse-radius boundary within the stated regularly
varying class, not the spherical representation or the first occurrence of non-Gaussian r−1 /r−3
scales.


6    Spherical and finite-scale Schwarzian bridges
The matrix-order and saturation calculations meet exactly at an inflection point. Gaussian
independence makes the full saturation curve one-dimensional, but it is not responsible for the


                                                                          10
```

---

## Page 11

```text
local bridge: rotational symmetry and suitable moments suffice. The fourth moment identifies
the coefficient below; the stated sixth moment controls its O(r4 ) remainder.

Theorem 6.1 (spherical local order–anisotropy bridge). Let d ≥ 2 and let X ∈ Rd be isotropic
and spherically symmetric with EkXk6 < ∞. Let g ∈ C 5 (R) satisfy g 0 > 0 and g 00 (0) = 0. For
p > 0, suppose hp = (g 0 )p has bounded fourth derivative. For u ∈ S d−1 put Z = u> X and
                                                                                               αp,X
     Hp,X (r, u) = E[hp (rZ)XX > ] = αp,X (r)(I − uu> ) + βp,X (r)uu> ,               κp,X =        .
                                                                                               βp,X

Then, with
                                                     EkXk4
                                           qX :=             ,
                                                    d(d + 2)
one has
                       κp,X (r) − 1                  6qX p     det Lg (0, δ)
                  lim         2
                                    = −qX p Sg(0) = − 0 2 lim                .                           (35)
                   r↓0      r                        g (0) δ→0      δ2
In particular, Sg(0) < 0 makes Lg (0, δ) indefinite and κp,X (r) > 1 at all sufficiently small
nonzero scales. Standard Gaussian input has qX = 1.

Proof. Rotations fixing u force the displayed two-eigenspace form, with
                                                             1
             βp,X (r) = E[Z 2 hp (rZ)],       αp,X (r) =        E[(kXk2 − Z 2 )hp (rZ)].
                                                            d−1
Choose a unit v ⊥ u. Spherical symmetry and isotropy give

                               EZ 4 = 3qX ,         E[Z 2 (v > X)2 ] = qX .

Taylor’s formula, cancellation of odd terms under X = −X, and the sixth-moment assumption
                                                             d

therefore give

                           qX h00p (0) 2                                       3qX h00p (0) 2
     αp,X (r) = hp (0) +              r + O(r4 ),        βp,X (r) = hp (0) +               r + O(r4 ).
                               2                                                   2
Taking the ratio yields κp,X (r) = 1 − qX h00p (0)r2 /hp (0) + O(r4 ). Since log hp = p log g 0 and
g 00 (0) = 0,
                                  h00p (0)   g 000 (0)
                                           =p 0        = pSg(0).
                                  hp (0)      g (0)
The adjacent-point expansion (11) gives the remaining equality.

    The equality of limits has a computable finite-scale version. The constants below are
deliberately explicit rather than optimized.

Theorem 6.2 (explicit finite-scale bridge). Under Gaussian input, retain the hypotheses of
Theorem 6.1 and write

                             a = hp (0),    b = h00p (0),   M4 = kh(4)
                                                                   p k∞ .

Choose r0 > 0 so that
                                          3|b| 2 5M4 4 a
                                              r +   r ≤ ,                                                (36)
                                           2 0    8 0  2
and set                                              2
                                      3M4            b     5|b|M4 2
                                 Ch =     +3             +       r .
                                       2a            a       4a2 0


                                                    11
```

---

## Page 12

```text
For a chosen δ0 > 0, put

                   A = g 0 (0), c = g 000 (0), d4 = g (4) (0), M5 = sup |g (5) (x)|,
                                                                    |x|≤δ0

                    |c| |d4 |δ0 M5 δ02                    |Ad4 | 7AM5 δ0
                K=     +        +      ,           Dg =         +        + δ0 K 2 .
                     6     24      120                     12      120
Then for 0 < r ≤ r0 and 0 < |δ| ≤ δ0 ,

                                κp (r) − 1 + pSg(0)r2 ≤ Ch r4 ,                                   (37)
                                             A2 Sg(0)
                           det Lg (0, δ) −        δ 2 ≤ Dg |δ|3 ,                                 (38)
                                           6
                        κp (r) − 1  6p det Lg (0, δ)              6pDg
                                   + 2                ≤ Ch r 2 +       |δ|.                       (39)
                            r2      A       δ2                     A2
Thus the order defect predicts anisotropy at finite, independently chosen scales with a certified
error bar.
Proof. Gaussian Taylor remainders give
               b                         M4 4                     3b 2                   5M4 4
       αp = a + r2 + Rα ,      |Rα | ≤     r ,         βp = a +     r + Rβ ,   |Rβ | ≤      r .
               2                         8                        2                       8
Condition (36) makes βp ≥ a/2. Subtracting 1 − (b/a)r2 before dividing by βp yields
                                    "           2              #
                             b 2      3M4        b      5|b|M4 2 4
                    κp − 1 + r ≤           +3        +         r r ,
                             a         2a        a        4a2 0

which is (37) because b/a = pSg(0).
   Taylor expansion at zero gives
                         c     d4                g(δ) − g(0)      c     d4
            g 0 (δ) = A + δ 2 + δ 3 + R1 ,                   = A + δ 2 + δ 3 + R2 ,
                         2     6                      δ           6     24
where |R1 | ≤ M5 |δ|4 /24 and |R2 | ≤ M5 |δ|4 /120. Writing the determinant as A(g 0 (δ) − A) −
2A(V − A) − (V − A)2 , with V = (g(δ) − g(0))/δ, gives (38) with the displayed Dg . Finally,
divide (37) by r2 , divide (38) by δ 2 , multiply the latter by 6p/A2 , and use the triangle
inequality.

    For the standard logistic sigmoid, Sσ = −1/2. Theorem 6.1 therefore predicts the exact
initial coefficient p/2 for every hp = σ 0p , recovered globally below. Equation (39) strengthens
the conceptual coefficient match into a falsifiable finite-scale comparison.
    For a general h, κh = αh /βh in (18) is an anisotropy ratio; it is the spectral condition
number only after the eigenvalue ordering is known. The two powers are geometric. At large
r, only a score slab of width O(r−1 ) remains unsaturated, producing α  r−1 . A radial
perturbation carries an additional factor Z 2 = O(r−2 ) inside that slab, producing β  r−3 .
Both modes are supported by the near-boundary slab; the radial mode is weaker because it
carries the additional Z 2 factor.


7    All-power logistic saturation laws
For every real p > 0 set hp (t) = σ 0 (t)p . The cases p = 1 and p = 2 are Bernoulli Fisher
and squared-output curvature, respectively, but the analytic law is not restricted to those
observation models. The Gamma transform below is classical generalized-logistic distribution
theory [27, eqs. (2.3)–(2.5)]; our use of it is geometric.

                                                  12
```

---

## Page 13

```text
Lemma 7.1 (closed sensitivity moments for every p > 0). Let ψj denote the polygamma
function of order j. Then
                                                     Γ(p + ik)Γ(p − ik)
                                 Z
                       hp (k) :=
                       b            eikt hp (t) dt =                    ,        (40)
                                  R                        Γ(2p)
and
              Γ(p)2
                                                            m4 (p) = 12ψ1 (p)2 + 2ψ3 (p) m0 (p).   (41)
                                                                                        
   m0 (p) =         ,       m2 (p) = 2ψ1 (p)m0 (p),
              Γ(2p)
In particular,

                            profile      m0          m2                m4
                           h1 = σ 0       1        π 2 /3             7π 4 /15
                           h2 = σ 02     1/6   (π 2 − 6)/18     7π 4 /90 − 2π 2 /3

Proof. With x = et ,
                                                    Z ∞
                            xp                             xp+ik−1
              hp (t) =             ,     hp (k) =
                                         b                          dx = B(p + ik, p − ik),
                         (1 + x)2p                  0     (1 + x)2p

which proves (40). Since hp (t) = O(e−p|t| ), all polynomial moments are finite and differentiation
under the Fourier integral is justified. Differentiating its logarithm at zero gives (log b
                                                                                          hp )00 (0) =
                  hp )(4) (0) = 2ψ3 (p). Since m2 = −b
−2ψ1 (p) and (log b                                                       hp (0), (41) follows. The
                                                        h00p (0) and m4 = b
                                                                            (4)

table uses the standard integer polygamma values.

Theorem 7.2 (strict all-power logistic anisotropy). For every p > 0, κp (0) = 1, κp (r) > 1 for
r > 0, and κp is strictly increasing on (0, ∞). At the two endpoints,
                                     p    p     p(p + 1) 6
                         κp (r) = 1 + r2 − r4 +         r + O(r8 )          (r ↓ 0),               (42)
                                     2    8        16
and
                                      r2         ψ3 (p)
                         κp (r) =           +1+          + O(r−2 )       (r → ∞).                  (43)
                                    2ψ1 (p)     4ψ1 (p)2
Thus κ1 (r) ∼ 3r2 /π 2 and κ2 (r) ∼ 3r2 /(π 2 − 6).
Proof. Normalize the density qp,r (z) ∝ hp (rz)ϕ(z). Then βp (r)/αp (r) = Eqp,r Z 2 . If r2 > r1 ,
the derivative on z > 0 of the log likelihood ratio is
                   d      hp (r2 z)                                      
                      log           = −p r2 tanh(r2 z/2) − r1 tanh(r1 z/2) < 0.
                   dz     hp (r1 z)
Thus the distribution of |Z| under qp,r decreases strictly in monotone-likelihood-ratio order as
r increases, and its strictly increasing statistic Z 2 has decreasing expectation. Hence αp /βp
increases strictly. At r = 0 isotropy gives one. Lemma 7.1 inserted into Theorem 4.1, with
one further term in e−t /(2r ) , gives the large-r statement. More explicitly, m6 (p) < ∞ by the
                        2    2


exponential tail, and Taylor remainder bounds for e−x give
             ϕ(0)         m2      m4                          ϕ(0)        m4           
    αp (r) =        m0 − 2 + 4 + O(r−6 ) ,              βp (r) = 3 m2 − 2 + O(r−4 ) .
               r           2r     8r                             r           2r
Their ratio yields (43). Finally,

                               p 2 p(1 + 3p) 4 p(15p2 + 15p + 4) 6
                                                                        
                        −p                                             8
             hp (t) = 4     1− t +          t −                 t + O(t ) .
                               4       96            5760

                                                     13
```

---

## Page 14

```text
For each fixed p > 0, every derivative of hp is bounded. Taylor’s theorem therefore bounds the
displayed remainder globally by khp k∞ |t|8 /8!; after setting t = rZ, this is integrable in both
                                    (8)

αp and βp because the Gaussian has a finite tenth moment. Inserting the Gaussian moments
through EZ 8 = 105 in the coefficients and taking the ratio gives (42).

    Figure 2 shows the two statistically canonical members of the all-power family. The solid
and dashed curves are direct Gaussian integrals; the dotted curves are the asymptotic constants
in (43).

                                             One tangential law, one radial bottleneck                                             Profile-generic large-r anisotropy: κ ≍ r2
                                                                                                                            103
                                                                                                                                  square loss: h = σ 2
                                                                                                                                                    0




                                     10−1                                                                                         Bernoulli Fisher: h = σ
curvature / information eigenvalue




                                                                                                                                                            0




                                     10−2                                                                                   102




                                                                                                       anisotropy κ = α/β
                                     10−3
                                                                                                                            101
                                     10−4
                                            square loss: h = σ 2, tangential
                                                              0




                                     10−5   square loss: h = σ 2, radial
                                                              0
                                                                                                                            100
                                            Bernoulli Fisher: h = σ , tangential
                                                                   0




                                            Bernoulli Fisher: h = σ , radial
                                                                   0




                                                   10−1                  100               101                                         10−1                 100               101
                                                            teacher weight norm r = ‖w ⋆ ‖                                                     teacher weight norm r = ‖w ⋆ ‖


Figure 2: Exact curvature/information eigenvalues and their ratio. Saturation leaves d − 1
tangential directions at order r−1 but pushes the radial direction to order r−3 . The quadratic
condition-number law is not a fitted exponent; it follows from Theorem 4.1.

    The cancellation of every p2 contribution in the fourth-order ratio coefficient is worth
noting: the full all-power family has the correction −pr4 /8, followed by the first nonlinear-in-p
term p(p + 1)r6 /16.


8                                      Finite-sample resolution of the weighted Gram matrix
The population eigenvalues alone do not say when a sample resolves the radial mode. We now
answer that question for the fixed-oracle matrix
                                                                                       n
                                                                  b h,n (r, u) = 1                                                            iid
                                                                                       X
                                                                  H                           h(ru> Xi )Xi Xi> ,                       Xi ∼ N (0, Id ).
                                                                                 n
                                                                                        i=1

Prior self-concordant analyses already give bilateral constant-factor empirical-Hessian sand-
wiches, including a uniform result for Gaussian logistic regression [19, Eq. (92)]; fixed-point
standardized-Hessian concentration is also available under generic matrix-Bernstein conditions
[22]. Chardon, Lerasle and Mourtada prove a uniform one-sided lower bound for the empirical
Bernoulli Hessian (p = 1) under the sufficient condition n & r(d + t) [18, Theorem 6]. We do
not claim the first bilateral concentration or the first finite-sample lower bound. The result
below instead gives tunable two-sided relative error for a fixed teacher, applies to a general
bounded profile and hence every p > 0, separates radial, tangential and cross errors, and
returns an eigenspace angle.
    Put m = d − 1, Z = u> X, Y = X − Zu, and W = h(rZ). Define

                                                                  α = EW,          β = E[W Z 2 ],     γj = E[W 2 Z 2j ]                        (j = 0, 1, 2),


                                                                                                      14
```

---

## Page 15

```text
and the envelopes

                    H = khk∞ ,           K1 = sup z 2 h(rz)2 ,               K2 = sup z 2 h(rz).
                                                 z                                    z

Theorem 8.1 (explicit relative empirical spectrum). Assume 0 ≤ h ≤ H, K1 , K2 < ∞, and
α, β > 0. Let 0 < δ < 1 and set

                                     t = log(12/δ),               u0 = m log 9 + t,
                              p             H 2t                                 p            K1 t
               S0+ = nγ0 +     2nH 2 γ0 t +      ,                 S1+ = nγ1 +    2nK1 γ1 t +      ,
                                             3                                                 3
                                 r
                                     2γ0 t Ht 4
                                                             q
                                                               S0+ u0 + Hu0 ,                             (44)
                                                                            
                          eT =            +    +
                                      n     3n   n
                                                                    q
                                                                      S1+ √   √ 
                                 r
                                     2γ2 t K2 t
                          eR =            +     ,            qn =          m + 2t .                       (45)
                                      n     3n                        n
Then, with probability at least 1 − δ, in the radial–tangential basis
                                                       
                                                  C bn
                                        Hh,n = >
                                        b
                                                  bn cn

satisfies simultaneously

                     kC − αIm kop ≤ eT ,               |cn − β| ≤ eR ,           kbn k2 ≤ qn .            (46)

Consequently, for                                                   
                                                         eT eR             qn
                                       εn := max           ,             +√ ,                             (47)
                                                         α β                αβ
one has the two-sided relative Löwner bound

                          (1 − εn )Hh (r, u)  H
                                               b h,n (r, u)  (1 + εn )Hh (r, u).                         (48)

If G := α − β − eT − eR > 0, the empirical matrix has a unique eigenvalue βb below the tangential
block spectrum, and its unit eigenvector ub obeys
                                                qn                                  qn2
                                    u, u) ≤
                              tan ∠(b              ,              |βb − β| ≤ eR +       .                 (49)
                                                G                                   G
Every other ordered eigenvalue differs from α by at most max{eT , eR } + qn .
Proof. Write
                     1X                                1X                                   1X
               C=       Wi Yi Yi> ,           bn =        W i Z i Yi ,           cn =          Wi Zi2 .
                     n                                 n                                    n
                          i                                   i                                i

Scalar Bernstein controls W − α and, one-sidedly, i Wi2 ≤ S0+ . Conditional on the weights,
                                                                     P
for a fixed unit v,
                                                                 iid
                    X                      X
                 v>   Wi (Yi Yi> − Im )v =   Wi (G2i − 1),   Gi ∼ N (0, 1).
                      i                                  i

The exact Gaussian moment-generating function gives
                       X                   s X
                                2
                           Wi (Gi − 1) ≤ 2 u0       Wi2 + 2Hu0
                                 i                                       i


                                                             15
```

---

## Page 16

```text
outside conditional probability 2e−u0 . A 1/4-net of S m−1 has at most 9m points and kAkop ≤
2 maxv in net |v > Av|, proving the first bound in (46). Bernstein applied to Wi Zi2 ∈ [0, K2 ]
proves the radial bound.
    Conditionally on the Zi ,
                                                  W 2Z 2
                                            P             
                                   bn ∼ N 0, i 2i i Im .
                                                  n
A second one-sided Bernstein bound gives i Wi2 Zi2 ≤ S1+ , and the Gaussian norm tail proves
                                            P
the cross bound. The listed failures total less than 9e−t < δ.
    Conjugating H   b h,n − Hh by H −1/2 = diag(α−1/2 Im , β −1/2 ) shows that its norm is at
                                     h
most (47); this is equivalent to (48). If G > 0, then cn < λmin (C). Interlacing leaves one
eigenvalue below C. The eigenvector equation and the Schur complement give respectively
      u, u) ≤ qn /G and 0 ≤ cn −βb ≤ qn2 /G. Weyl’s inequality gives the remaining assertion.
tan ∠(b

   For hp = σ 0p , all quantities in Theorem 8.1 are one-dimensional and computable. The
elementary bound σ 0 (s) ≤ e−|s| gives, for every p > 0,

                                                   e−2              4e−2
                              H = 4−p ,   K1 ≤           ,   K2 ≤          ,                  (50)
                                                   p2 r2            p2 r 2

and, with ϕ(0) = (2π)−1/2 ,
                                ϕ(0)           ϕ(0)               3ϕ(0)
                         γ0 ≤        ,    γ1 ≤    3 3
                                                      ,    γ2 ≤ 5 5 .                          (51)
                                 pr            2p r               2p r

Indeed, after s = rZ, use hp (s)2 ≤ e−2p|s| and R |s|j e−2p|s| ds = 2j!/(2p)j+1 for j = 0, 2, 4.
                                                R

Corollary 8.2 (effective sample size for every logistic power). Let
                                                          
                                2           3m2 (p) m4 (p)
                              Rp = max             ,         .
                                             m0 (p) m2 (p)
For r ≥ Rp , 0 < ε ≤ 1/2 and 0 < δ < 1, the explicit condition εn ≤ ε in (47), with (50)–(51)
substituted, guarantees (48). In particular, for each fixed p > 0 there are finite computable
constants Cp , Cp0 such that
                                             r [d + log(12/δ)]
                                     n ≥ Cp                                               (52)
                                                     ε2
is sufficient and, after increasing Cp if necessary, eT + eR ≤ (α − β)/2. Hence G ≥ (α − β)/2
and, on the same event,
                                    r                  p                         !
                                      d + log(1/δ)       [d + log(1/δ)] log(1/δ)
                sin ∠(bu, u) ≤ Cp0                  +                              .
                                           nr                      n

Thus the effective number of transition-layer observations is n/r: relative resolution of a
population eigenvalue of order r−3 does not itself require r3 samples.
Proof. The brackets in Theorem 4.1 and the definition of Rp give
                     ϕ(0)m0 (p)               ϕ(0)m2 (p)                       ϕ(0)m0 (p)
                α≥              ,        β≥              ,     α−β ≥                      .
                         2r                      2r3                               2r
Insert these andp(50)–(51) in (44)–(47). Each relative block term is bounded by a p-dependent
constant times r[d + log(12/δ)]/n+r[d+log(12/δ)]/n. The cross term has the same first order.
Increasing a finite constant Cp makes their sum at most ε and also makes eT + eR ≤ (α − β)/2.
Thus G ≥ (α − β)/2 ≥ ϕ(0)m0 (p)/(4r), and substitution of qn into (49) gives the displayed
bound with a finite computable Cp0 .

                                                  16
```

---

## Page 17

```text
For the two statistical powers, the conservative majorant used in this proof gives fully
numerical choices:

                      p      Rp       Cp in (52)      Cp0 in the angle bound
                      1   3.717183       22929              22.479249
                      2   2.153017      294162              52.368963

These are sufficient, not optimized, constants. The explicit-constants replay prints every
intermediate coefficient and checks that the resulting quadratic majorant is at most ε for
0 < ε ≤ 1/2.
    We next prove that the product scale in (52) is intrinsic for the stated bilateral loss. Choose
any finite ap > 0 satisfying      Z
                                                         m2 (p)
                                          s2 hp (s) ds ≤        .
                                   |s|>ap                 16

For r ≥ max{ m4 (p)/m2 (p), 4ϕ(0)ap }, the empty-transition-slab event and Markov’s inequal-
              p

ity give                                                               
                                          βp (r)       1        4ϕ(0)ap n
                       Pr λmin (Hp,n ) <
                                b                   ≥ exp −                 .                  (53)
                                            2          2            r
Hence failure probability at most δ < 1/2 requires
                                              r       1
                                      n≥           log .                                      (54)
                                           4ϕ(0)ap    2δ

To verify (53), condition on no |Zi | ≤ ap /r. This event has probability at least the exponential
shown; the conditional mean radial entry is at most βp /4, so with conditional probability at
least 1/2 that entry, and therefore the smallest eigenvalue, is below βp /2.
    The high-confidence half of the matching lower bound is an exact consequence of the next
lemma. Stating it autonomously exposes every constant and removes any dependence on an
implicit moderate-deviation argument.

Lemma 8.3 (explicit Gaussian-product lower tail). Let Ai ≥ 0 be iid with 0 < ρ = EA2i < ∞
                  ∞. Let Yi , Yi0 be independent standard Gaussians, independent of the Ai ,
and χ = EA4i /ρ2 <P
and put Dn = n−1 ni=1 Ai Yi Yi0 . For every ε > 0,

                                                            2nε2
                                                                
                                               3
                     Pr{|Dn | > ε} ≥                  exp −        .                   (55)
                                         40(1 + 3χ/n)        ρ

In particular, if n ≥ 3χ, the leading constant is at least 3/80.

Proof. Set T = n−1 i A2i Yi2 . Direct expansion gives
                     P

                                                         
                                     2    2       1 3χ
                    ET = ρ,       ET = ρ 1 − +               ≤ ρ2 (1 + 3χ/n).
                                                  n     n

Paley–Zygmund therefore gives Pr{T ≥ ρ/2} ≥ [4(1 + 3χ/n)]−1 . Conditional on (Ai , Yi )i≤n ,
Dn ∼ N (0, T /n). The elementary bound
                                             3 −x2
                                  2Φ(−x) ≥      e ,         x ≥ 0,                            (56)
                                             10
then proves (55). For completeness, on 0 ≤ x ≤ 1 use 2Φ(−x) ≥ 2Φ(−1) > 3/10; on x ≥ 1 use
the Mills bound Φ(−x) ≥ ϕ(x)x/(1 + x2 ), whose ratio to e−x is increasing from a value larger
                                                           2


than 3/10.

                                                 17
```

---

## Page 18

```text
Theorem 8.4 (matching lower complexity for bilateral relative Loewner loss). Fix p > 0.
There are finite constants R                                     ep , d ≥ 3, 0 < ε ≤ 1/2 and
                             ep , cp , δp > 0 such that, for r ≥ R
0 < δ ≤ δp , the implication
                                                                             r[d + log(1/δ)]
          Pr{(1 − ε)Hp  H
                         b p,n  (1 + ε)Hp } ≥ 1 − δ         =⇒     n ≥ cp                     (57)
                                                                                    ε2
holds. At constant confidence the dimension term has the explicit sufficient obstruction
                 m0 (2p)    r(d − 2)                                                    1
         n<                               =⇒        Pr{relative Loewner failure} ≥         ,   (58)
              16ϕ(0)m0 (p)2    ε2                                                     1152
provided nγ0 ≥ H 2 and the finite-radius moment brackets hold. The displayed coefficient equals
1/[96ϕ(0)] for p = 1 and 9/[560ϕ(0)] for p = 2.
    The confidence constants can be made fully explicit. Define
                     m0 (2p)                      4m0 (4p)              1
            Lp =                ,      Kp =                  ,    δphc = e−12ϕ(0)ap Kp .       (59)
                   2ϕ(0)m0 (p)2                 ϕ(0)m0 (2p)2            2
                ep to ensure r2 ≥ m2 (2p)/m0 (2p), success necessarily implies the following
After enlarging R
bound whenever 0 < δ < min{3/80, δphc }:
                                              Lp r       3
                                        n≥        2
                                                    log     .                                  (60)
                                              2 ε       80δ

     P Restrict> the relative inequality
Proof.                                      P m 2= d − 1 dimensional tangential block C =
                                         to the
       i Wi Yi Yi . Put γ0 = EW and S0 =       i Wi . Since W ≤ H, Paley–Zygmund gives
n −1                             2


                           Pr{S0 ≥ nγ0 /2} ≥ 1/8        (nγ0 ≥ H 2 ).

Conditional on the weights, T0 = i Wi2 Yi12 has second moment at most 3S02 , so Pr{T0 ≥
                                    P
S0 /2 | W } ≥ 1/12. Conditional on (W, Y1 ), the remaining d − 2 entries of the first off-diagonal
column of C are Gaussian with common variance T0 /n2 . A final Paley–Zygmund bound gives
Pr{χ2d−2 ≥ (d − 2)/2} ≥ 1/12. Hence, with probability at least 1/1152,
                                                   r
                                                     (d − 2)γ0
                                kC/α − Im kop ≥                .
                                                       8nα2
The scaled integrals give
                                       γ0      m0 (2p)
                                         2
                                           ≥              r,
                                       α     2ϕ(0)m0 (p)2
which proves (58). If nγ0 < H 2 , then n = Op (r) and the slab bound (53) supplies a fixed
failure probability after decreasing δp .
    For the confidence term, take A = W/α in Lemma 8.3. The finite-radius brackets give
                                 EW 2                      EW 4
                            ρ=        ≥ Lp r,        χ=            ≤ Kp r.                     (61)
                                  α2                      (EW 2 )2
Indeed, use α ≤ ϕ(0)m0 (p)/r, EW 2 ≥ ϕ(0)m0 (2p)/(2r), and EW 4 ≤ ϕ(0)m0 (4p)/r. If
n < 3Kp r, the slab bound (53) gives failure at least δphc . Thus success for δ < δphc forces
n ≥ 3Kp r, and the last sentence of Lemma 8.3 gives failure at least

                                               2nε2
                                                   
                                       3
                                         exp −        .
                                      80       Lp r
This proves (60). Combining it with the dimension bound by max{a, b} ≥ (a + b)/2 proves
(57) with explicit admissible ranges.

                                                   18
```

---

## Page 19

```text
For reproducibility, choosing ap by equality in the defining tail condition gives the following
numerical constants. The tiny δphc values reflect deliberately crude slab and fourth-moment
bounds; they are proof ranges, not estimates of practical behavior.

                       p      ap              Lp               Kp               δphc
                       1   6.255617      0.208886        2.578246          1.4661 × 10−34
                       2   3.517898      0.322281        3.817398          6.0017 × 10−29

    The theorem is about the fixed-oracle weighted Gram matrix, not a minimax estimator.
Nor should it be exported unchanged to weaker targets. Direct scalar Bernstein gives an
Op (r/ε2 ) radial-entry upper bound at constant confidence; the empty-slab argument gives
only the fixed-accuracy Ωp (r) obstruction recorded above. The ordinary bottom eigenspace
behaves differently: in the iterated extreme-saturation limit it is governed by sample order
statistics rather than relative Gram resolution.
    The algebraic flag mechanism below is an instance of classical scaled-SVD asymptotics
[8]. The contribution here is its logistic ordering by distance to the transition hyperplane,
the resulting bottom projector, its quantitative finite-saturation resolution, and the exact
stochastic angle law and complexity. We first isolate the two steps that are easy to compress
incorrectly.
Lemma 8.5 (deterministic spectral lexicography). Let x1 , . . . , xn ∈ Rd , n ≥ d, and suppose
ξk = x1 ∧ · · · ∧ xk 6= 0 for k = 1, . . . , d. Let bj (r) > 0 satisfy
                                         b` (r)
                                                −→ 0              (j < `),                          (62)
                                         bj (r)

and set Hr =      j=1 bj (r)xj xj . If λ1 (r) ≥ · · · ≥ λd (r) > 0 are its eigenvalues, then for every
               Pn               >

k < d,
                               Vk
                                    Hr                              λk+1 (r)
                             Qk             −→ ξk ξk> ,                      −→ 0.                  (63)
                               j=1 bj (r)
                                                                     λk (r)
Consequently the top-k gap is eventually open and, for its projector Er,k ,

                                   kEr,k − Pspan{x1 ,...,xk } kop −→ 0.                             (64)

For k = d − 1, the bottom eigenvalue is eventually simple and its projector converges to the
normal of the first d − 1 vectors.
Proof. For a k-subset I = {i1 < · · · < ik } write ξI = xi1 ∧ · · · ∧ xik . Cauchy–Binet gives
                               k
                                                           !
                               ^           X Y
                                   Hr =              bi (r) ξI ξI> .
                                                |I|=k    i∈I


                                                          Q is one. For I 6= I0 , if ` is the first index
After normalization, the coefficient of I0 = {1, . . . , k}
with i` 6= `, then i` > ` and ij ≥ j thereafter, so j bij (r)/bj (r) → 0 by (62). The sum is
finite, proving the operator-norm V limit.
    The two largest eigenvalues of k Hr are λ1 · · · λk and λ1 · · · λk−1 λk+1 . Weyl’s inequalities
applied to the rank-one limit show that their ratio tends to zero, which gives the second assertion
in (63) and the eventual gap. Let qr,k span the top exterior eigenspace and qk = ξk /kξk k.
Rank-one spectral perturbation gives Pqr,k → Pqk . If ϑr,1 , . . . , ϑr,k are the principal angles
between the underlying k-planes, the Plücker identity is
                                                            k
                                                            Y
                                         |hqr,k , qk i| =         cos ϑr,j .
                                                            j=1


                                                        19
```

---

## Page 20

```text
The product tends to one, hence maxj sin ϑr,j → 0. This maximum equals the operator-norm
distance between the two projectors, proving (64). Orthogonal complements finish the k = d−1
case.

Lemma 8.6 (inverse of a square Gaussian matrix). Let Y ∈ Rm×m have iid N (0, 1) entries,
and let z ∈ Rm be deterministic or independent of Y . Then Y is invertible almost surely and
there exists G ∼ N (0, 1), independent of z, such that

                                                              kzk
                                                                                                      (65)
                                                          d
                                           kY −1 zk =             .
                                                              |G|

Proof. Choose a measurable orthogonal Q(z) with Q(z)z = kzke1 , setting Q(0) = Im , and
put A = Q(z)Y . The case z = 0 is immediate. Conditional on z, orthogonal invariance
makes A an iid standard Gaussian matrix with a law independent of z; hence A and z are
independent. Write its rows as a>   1 , . . . , am , and measurably choose a unit normal v to rows
                                                 >

2, . . . , m. Conditional on those rows and on z, G = a>      1 v ∼ N (0, 1), with a conditional law
independent of z. The system A(Y z) = kzke1 forces Y −1 z = cv and then cG = kzk. Taking
                                     −1

norms proves (65), including the asserted independence.

Lemma 8.7 (finite hierarchy perturbation). Let d ≥ 2, m = d − 1, n ≥ d, let x1 , . . . , xn ∈ Rd ,
and let a1 ≥ · · · ≥ an > 0. Put
                                                                                   n
                                                                                   X
                 X0 = [x1 · · · xm ],     X> = [xm+1 · · · xn ],              H=         ai xi x>
                                                                                                i ,
                                                                                   i=1

suppose s = σmin (X0 ) > 0, and let P0 project onto range(X0 )⊥ . If

                                               am+1 kX> k2op
                                        η :=                 < 1,                                     (66)
                                                am    s2
then the bottom eigenvalue of H is simple and

                                        kPbot (H) − P0 kop ≤ η.                                       (67)

Proof. Write H = A + R for the sums over i ≤ m and i > m. The kernel of A is the range of
P0 , while its least positive eigenvalue is at least γ = am s2 . Since R  0, the second eigenvalue
of H in increasing order is at least γ, whereas Rayleigh’s principle on a unit normal v gives
λ1 (H) ≤ v > Rv < γ under (66). Thus the bottom eigenvalue is simple. Expanding v in an
eigenbasis qj of H and using Hv = Rv gives
                                               X                              kRvk2
                         kPq⊥ vk2 ≤ γ −2             λj (H)2 |hv, qj i|2 ≤          .
                             1                                                 γ2
                                               j≥2

                                                                                            >,
The left side is the squared distance between the rank-one projectors. Finally R  am+1 X> X>
giving (67).

Theorem 8.8 (spectral lexicography and exact limiting angle law). Fix p > 0, d ≥ 2, n ≥ d,
and u ∈ S d−1 . Let Xi ∼ N (0, Id ), Zi = u> Xi , and
                       iid


                                                n
                                   br = 1
                                                X
                                   H                   σ 0 (rZi )p Xi Xi> .
                                        n
                                                i=1




                                                       20
```

---

## Page 21

```text
Let π be the almost surely unique permutation for which |Zπ(1) | < · · · < |Zπ(n) |, and put
Vk = span{Xπ(1) , . . . , Xπ(k) }. Almost surely, for every k < d and all sufficiently large r, a gap
separates the top k eigenvalues. If Er,k denotes that cluster’s projector, then

                           kEr,k − PVk kop −→ 0,              k = 1, . . . , d − 1.             (68)

For all sufficiently large r, the bottom eigenvalue is simple almost surely. Denoting its rank-one
projector by Pbrbot , one has convergence in operator norm,

                            kPbrbot − P∞ kop −→ 0,              P∞ := PV ⊥ .                    (69)
                                                                            d−1


   Write m = d − 1, let A(j) = |Zπ(j) |, and let ζ = (Zπ(1) , . . . , Zπ(m) )> . If θ∞ is the acute
angle between the range of P∞ and u, then the following identity is exact:
                                 kζk
                                                                   G independent of ζ.          (70)
                             d
                    tan θ∞ =         ,      G ∼ N (0, 1),
                                 |G|

Let c+ =    2/π and c− = 2ϕ(1) = c+ e−1/2 . For m ≥ 2,
           p

                                  (                 )
                                             m3/2      1
                               Pr kζk ≥ √             ≥ .                                       (71)
                                            6 2c+ n    2

If n ≥ 4m/c− , then                (                    )
                                          4m3/2
                                 Pr kζk ≤                   ≥ 1 − e−9m/8 .                      (72)
                                           c− n

Let θr be the acute angle between the range of Pbrbot and u. For d ≥ 3 it follows that, for
0 < ε ≤ 1/2 and 0 < δ < c− /2,

                                                                       e−1/2 (d − 1)3/2
                   lim Pr{sin θr ≤ ε} ≥ 1 − δ           =⇒       n≥      √              .       (73)
                   r→∞                                                 24 2      εδ

Conversely, if δ ≥ 2e−9m/8 , n ≥ 4m/c− , and

                                                          m3/2
                                           n ≥ 8e1/2           ,                                (74)
                                                           εδ
then the limiting success probability is at least 1 − δ. Thus the limiting sample complexity
has matching order Θ(m3/2 /(εδ)) in the displayed confidence range, and Θ(d3/2 /ε) at fixed
confidence.

Proof. Order the samples as xj = Xπ(j) and the weights as wj (r) = σ 0 (rZπ(j) )p . Since

                                                        e−|s|
                                         σ 0 (s) =                 ,
                                                     (1 + e−|s| )2

one has w` (r)/wj (r) → 0 exponentially whenever j < `. Almost surely the first d reordered
samples are independent. Lemma 8.5, with bj = wj /n, therefore proves the eventual gaps and
(68)–(69), including the inverse Plücker step.
    Rotate so u = ed and write X = (Y, Z). Conditional on the entire score vector, the
permutation is fixed while the selected tangential rows remain iid Gaussian. Thus the m × m
                        > , j ≤ m, is independent of ζ. A normal to the selected span is
matrix Y∗ with rows Yπ(j)
proportional to (−Y∗−1 ζ, 1), so tan θ∞ = kY∗−1 ζk. Lemma 8.6 proves (70) with the stated
independence.

                                                     21
```

---

## Page 22

```text
It remains to bound the first m half-normal order statistics. Their distribution function
F (t) = 2Φ(t) − 1 satisfies

                         F (t) ≤ c+ t (t ≥ 0),        F (t) ≥ c− t (0 ≤ t ≤ 1).               (75)

For k = bm/2c and t = k/(2c+ n), the count Nt = #{i : |Zi | ≤ t} has mean at most k/2.
Markov’s inequality gives Pr{A(k) > t} ≥ 1/2. Since k ≥ m/3 and at least m/2 of the first m
order statistics exceed A(k) , this proves (71). For the other direction take t = 4m/(c− n) ≤ 1.
Now ENt ≥ 4m, and a Chernoff bound gives Pr{Nt < m} ≤ e−9m/8 . On the complement,
       √
kζk ≤ mA(m) ≤ 4m3/2 /(c− n), proving (72).
    Finally, Pr{|G| ≤ x} ≥ c− min{x, 1} and Pr{|G| ≤ x} ≤ c+ x. Combining the first
inequality with (71) yields, for every τ > 0,
                                                      (             )
                                               c−         m3/2
                          Pr{tan θ∞ > τ } ≥       min √           ,1 .
                                                2       6 2c+ nτ
                                    √
Since sin θ ≤ ε implies tan θ ≤ ε/ 1 − ε2 ≤ 2ε, this proves (73). For the upper bound, with
probability at least 1 − q − e−9m/8 ,
                                                      4c+ m3/2
                                           tan θ∞ ≤            .
                                                      c− q n

Set q = δ/2 and use c+ /c− = e1/2 to obtain (74). Almost-sure projector convergence and
continuity of the limiting angle law justify the displayed probability limit.

    The hierarchy can also be resolved before taking a limit. The next result is simultaneous
in all displayed parameters; its constants are explicit but intentionally conservative.
Theorem 8.9 (joint finite-saturation   spectral resolution). Use the notation of Theorem 8.8,
put m = d − 1 and c+ = 2/π, and define
                       p

                                       √     √      p
                              Mn,d,δ = n + d + 2 log(3/δ),
                                                                   
                                                               prδ
                                      p 2  3   2    −2
                      ηn,d,δ (r) = 9 4 c+ m Mn,d,δ δ exp −            .                  (76)
                                                              3c+ n
For every 0 < δ < 1, with probability at least 1 − δ, whenever ηn,d,δ (r) < 1 the bottom eigenvalue
is simple and
                                  kPbrbot − P∞ kop ≤ ηn,d,δ (r).                               (77)
For every 0 < ε < 1, (77) is at most ε if
                                                                      !
                                       3c+ n
                                                              2
                                                 9 4p c2+ m3 Mn,d,δ
                                    r≥       log                          .                   (78)
                                        pδ               εδ 2

   Let c− = c+ e−1/2 . If d ≥ 3, 0 < ε ≤ 1/2,

                                                      4m                      m3/2
                     4e−9m/8 ≤ δ < 1,            n≥      ,      n ≥ 32e1/2         ,
                                                      c−                       εδ
                √        √
and, with M =
                                  p
                    n+       d+    2 log(6/δ),

                                                   72 4p c2+ m3 M 2
                                                                   
                                       6c+ n
                                    r≥       log                      ,                       (79)
                                        pδ               εδ 2
then
                                    Pr{kPbrbot − uu> kop ≤ ε} ≥ 1 − δ.                        (80)

                                                    22
```

---

## Page 23

```text
Proof. Write A(j) = |Zπ(j) | and ∆m = A(m+1) − A(m) . The exact logistic formula gives
                                                               2p
                                                1 + e−rA(m)
                                           
                      wm+1 (r)
                               = e−pr∆m                              ≤ 4p e−pr∆m .             (81)
                       wm (r)                  1 + e−rA(m+1)

Let F (t) = 2Φ(t) − 1. The variables F (|Zi |) are iid uniform, and the adjacent spacing
D = F (A(m+1) ) − F (A(m) ) has law Beta(1, n). Hence Pr{D ≤ x} = 1 − (1 − x)n ≤ nx. Since
F is c+ -Lipschitz,                              
                                              δ          δ
                                 Pr ∆m ≥            ≥1− .                             (82)
                                            3c+ n        3
    Rotate as before. The tangential block Y∗ of the selected m samples is an independent
standard Gaussian matrix, and σmin ([Xπ(1) · · · Xπ(m) ]) ≥ σmin (Y∗ ). For each column yj , let Dj
be its distance to the span of the other columns. Deterministically, σmin (Y∗ ) ≥ m−1/2 minj Dj :
choose the largest coordinate of a least singular vector. Conditionally on the other columns,
Dj = |G|. A union bound and Pr{|G| ≤ x} ≤ c+ x give
    d

                                                        
                                                   δ              δ
                              Pr σmin (Y∗ ) ≥        3/2
                                                           ≥1− .                                (83)
                                               3c+ m              3

The standard Gaussian operator-norm tail also gives
                                                                  δ
                            Pr{k[X1 · · · Xn ]kop ≤ Mn,d,δ } ≥ 1 − .                           (84)
                                                                  3
On the intersection of (82)–(84), insert (81) into Lemma 8.7 with ai = wi (r)/n; the common
factor 1/n cancels. This proves (76)–(78).
    For the final claim, apply the first part with failure budget δ/2 and target ε/2, giving (79).
The event (72) fails with probability at most e−9m/8 ≤ δ/4. With another failure probability
at most δ/4, |G| ≥ δ/(4c+ ), and the exact angle law yields

                                                       m3/2  ε
                                   tan θ∞ ≤ 16e1/2          ≤ .
                                                        nδ   2
The triangle inequality for rank-one projectors proves (80).

    The factor m3 δ −2 in (76) comes from the elementary column-distance proof of (83); sharp
Gaussian invertibility estimates can improve this polynomial factor [9]. The exponential spacing
mechanism and the scale rδ/n are unchanged. Thus Theorem 8.9 closes the existence of a joint
finite-parameter regime but does not identify the optimal crossover around r comparable to n.




                                                  23
```

---

## Page 24

```text
Order-statistic angle law (d = 6)                                                      Spectral lexicography (d = 5, n = 30)
                                                                       median                              100
                                                                       90th percentile
                                                                       reference n−1
                    100
 limiting sin θ∞




                                                                                          ‖Pbot
                                                                                          ̂
                                                                                            r   − P∞‖op
                                                                                                          10−1


                   10−1                                                                                                median
                                                                                                                       90th percentile
                                101                                       102                                    100                             101
                                                 sample size n                                                                           teacher norm r

Figure 3: Fixed-seed diagnostics for Theorem 8.8. Left: the limiting angular loss follows the
predicted n−1 scale at fixed dimension (the theorem gives matching m3/2 /(εδ) complexity
in its stated confidence range). Right: finite-r bottom projectors approach the sample-wise
lexicographic limit; the proof, not this simulation, establishes convergence.


                                                                 Finite-saturation certificate (d = 5, n = 30)
                                           100                                                                              projector error
                                                                                                                            exact qr
                                          10−1                                                                              explicit logistic envelope
                                          10−2
                                          10−3
                                − P∞‖op




                                          10−4
                          ‖Pbot
                          ̂
                            r




                                          10−5
                                          10−6
                                          10−7

                                                      10          20            30           40       50                     60            70        80
                                                                                         teacher norm r

Figure 4: A fixed-sample certificate for Lemma 8.7. The actual bottom-projector error is
bounded by the data-dependent hierarchy ratio qr once qr < 1; the closed logistic envelope
replaces the exact adjacent weight ratio by 4p e−pr∆m . The figure is diagnostic, while the
inequality is deterministic.

    The order of limits in Theorem 8.8 remains essential for its exact law and matching
complexity: d, n, p, ε, δ are fixed while r → ∞, and only then are limit experiments compared.
Theorem 8.9 supplies a genuine joint finite-parameter regime by controlling the adjacent
half-normal spacing and selected Gaussian conditioning simultaneously. Its sufficient threshold
is not claimed sharp near the crossover r  n. In particular, an Ω(rd) angular necessity cannot
hold uniformly through extreme saturation; it remains the scale of the sufficient relative-Gram
event, not of the weaker bottom-projector target.




                                                                                         24
```

---

## Page 25

```text
8.1    Uniform all-power sensitivity on a full dyadic shell
The pointwise theorem admits a proof-complete full-dyadic-shell extension at the price of an
elementary covering logarithm. For Gp (w) = E[hp (w> X)XX > ] and its empirical analogue
b p,n (w), set
G
                     √
               Bn,δ = d + 2 log(2n/δ), µ3,d = [d(d + 2)]3/4 , Lp = p4−p ,
                           p


                                                                                                      4R d
                                                                                                      
       ϕ(0)m2 (p)                   3                              εbp
bp =              ,   Ap,n,δ = Lp (Bn,δ +µ3,d ),   η = min R,                        ,   N=        1+      .
           16                                                   32Ap,n,δ R3                            η
Theorem 8.10 (uniform relative sensitivity on a full dyadic shell). Fix p > 0, R ≥ Rp ,
0 < ε ≤ 1/2, and 0 < δ < 1/2. If
                                                     
                                      R            24N
                             n ≥ 128Cp 2 d + log          ,                       (85)
                                      ε             δ

then, with probability at least 1 − δ, simultaneously for every w with R ≤ kwk ≤ 2R,

                              (1 − ε)Gp (w)  G
                                              b p,n (w)  (1 + ε)Gp (w).                                 (86)

The computable condition is implicit in n only through Bn,δ ; no optimality is claimed for its
covering logarithm.

Proof. Since kh0p k∞ ≤ Lp ,

                        khp (w> x)xx> − hp (v > x)xx> kop ≤ Lp kw − vkkxk3 .

With probability at least 1 − δ/2, all sampled Gaussian norms are at most Bn,δ . On this event
Dn = G b p,n − Gp is Ap,n,δ -Lipschitz in operator norm. Cover the shell by an η-net of size at
most N and apply Corollary 8.2 at every net point with error ε/8 and failure δ/(2N ); (85) is
exactly a conservative sufficient condition. On the shell, λmin Gp (w) ≥ bp R−3 . Moving from a
net point to w therefore changes both Dn and Gp by at most (ε/32)λmin Gp (w). For every x,
                                  hε               εi >
                 |x> Dn (w)x| ≤ (1 + ε/32) +          x Gp (w)x ≤ εx> Gp (w)x,
                                   8              32
which is (86). The two failure probabilities total at most δ.

    The logarithm in the preceding elementary net is not quantitatively sharp, but its angular
log R component cannot disappear altogether. The following obstruction is stated in the
iterated regime in which it is proved.

Theorem 8.11 (intrinsic angular logarithm). Fix p > 0 and d ≥ 2, and define

                                                 b p,n (w) − Gp (w) Gp (w)−1/2
                                      Gp (w)−1/2 G
                                                                   
                 Ln,R =      sup                                                              .
                          R≤kwk≤2R                                                       op


There is cp > 0, depending only on p, such that
                                        (               r             )
                                                            R log R
                             lim lim inf Pr Ln,R ≥ cp                     = 1.                           (87)
                            R→∞ n→∞                            n

Thus no uniform high-probability inequality of order Op ( R/n) can hold for every large R and
                                                           p

all sufficiently large n. This does not assert that every logarithm in Theorem 8.10 is necessary.


                                                   25
```

---

## Page 26

```text
Proof. It suffices to work in a fixed two-dimensional coordinate plane. Put uθ = (cos θ, sin θ),
vθ = (− sin θ, cos θ) and

                                                                    FR,θ
                        FR,θ (x) = hp (Ru>     > 2
                                         θ x)(vθ x) ,     TR,θ =          .
                                                                   αp (R)

Because uθ ⊥ vθ , P TR,θ = 1, and the tangential Rayleigh quotient gives

                                  Ln,R ≥ sup |(Pn − P )TR,θ |.                               (88)
                                            θ

For independent standard normals Z, Y ,
                               2
                            P FR,θ = E[hp (RZ)2 Y 4 ] = 3Eh2p (RZ).

The saturation moments already proved imply

                             1                     3m0 (2p)
                               kTR,θ k22 −→ ap :=             > 0.                           (89)
                             R                    ϕ(0)m0 (p)2

   Transition layers separated by more than their R−1 bandwidth have negligible normalized
overlap:
                        lim lim sup     sup      R P (FR,θ FR,φ ) = 0.                (90)
                        A→∞ R→∞ A/R≤|θ−φ|≤π/2

By rotation take θ = 0, φ = ∆, write x = (z, y) in the chosen plane, and set s = Rz. The
integral on the left before the supremum becomes
          ZZ                                                     s     2
              ϕ(s/R)ϕ(y)hp (s)hp (s cos ∆ + Ry sin ∆)y 2 y cos ∆ − sin ∆ ds dy.
                                                                  R

If ∆ ≥ A/R, then R sin ∆ ≥ 2A/π. Along every sequence with A → ∞, the second profile
tends to zero for almost every y 6= 0. A constant times ϕ(y)hp (s)y 2 (y 2 + s2 ) is an integrable
envelope, so dominated convergence and the sequential criterion for the supremum prove (90).
    Choose a fixed sufficiently large Ap . For large R, the grid

                             ΘR = {jAp /R : 0 ≤ j ≤ bπR/(2Ap )c}

has cardinality comparable to R. Equations (89)–(90) show that distinct centered functions
                                             (0) √
on this grid have L2 (P ) distance at least cp R. Sudakov’s minoration for the associated
finite Gaussian bridge therefore gives
                                                        p
                             E max GP (TR,θ − 1) ≥ c(1)
                                                    p    R log R.
                               θ∈ΘR

Indeed, uniformly over distinct grid points,
         1                               1
           k(TR,θ − 1) − (TR,φ − 1)k22 =   kTR,θ k22 + kTR,φ k22 − 2P (TR,θ TR,φ ) ≥ ap
                                                                                  
         R                               R
for all sufficiently large R. The maximal variance is at most Cp R by (89); Borell’s Gaussian
                                                           (2) √
concentration then shows that this maximum exceeds cp R log R with probability tending
to one. For each fixed R, the grid is finite, so the multivariate central limit theorem transfers
                     √
the statement to { n(Pn − P )TR,θ : θ ∈ ΘR } as n → ∞. Taking R → ∞ afterward and using
(88) proves (87).




                                                26
```

---

## Page 27

```text
Theorem 8.11 forces one angular log R in the high-precision iterated limit, but the current
Euclidean net also pays dimension, log(1/ε) and random-envelope terms not covered by the
lower bound. A matching nonasymptotic marked-process lower bound and a chaining upper
bound remain open; the classical kernel laws [20, 21] identify the same scale but do not directly
handle the present nonseparable Gaussian marks.
    For p = 1, G b 1,n (w) is exactly the logistic-likelihood Hessian and is label-free. For p 6= 1 it
is a sensitivity Gram, not that likelihood Hessian. Earlier work proves uniform local constant-
factor sandwiches and an optimal-scale one-sided p = 1 lower bound [19, 18]; the narrower
addition here is a full dyadic shell, all p > 0, and tunable bilateral precision. It is not by itself
an estimator theorem.

                                                                                Finite-sample resolution (d = 12, r = 6, 320 repetitions)
                                             6 × 100                                      solid: median                                                     100




                                                                                                                      relative smallest-eigenvalue error
                                                                                          dashed: 90th percentile
relative tangential operator error




                                             4 × 100                                                  p=1
                                             3 × 100                                                  p=2

                                             2 × 100

                                                              100                                                                                          10−1
                                     6 × 10−1
                                     4 × 10−1
                                     3 × 10−1
                                                                          100                           101                                                                  100                            101
                                                                       normalized sample size n/(rd)                                                                      normalized sample size n/(rd)
                                                              100                                                                                          10−1
                                                                                                                    probability no sample has |rZ| ≤ 1




                                                                                                                                                           10−2
                             radial eigenspace error sin θ




                                                                                                                                                           10−3
                                                                                                                                                           10−4                 exact probability (display floor 10−8)
                                                                                                                                                                                fixed-seed frequency
                                                                                                                                                           10−5                 zero events (plotting limit)
                                                             10−1
                                                                                                                                                           10−6
                                                                                                                                                           10−7
                                                                                                                                                           10−8
                                                                          100                           101                                                       0   2   4     6      8     10 12          14     16
                                                                       normalized sample size n/(rd)                                                                      normalized sample size n/(rd)


Figure 5: Fixed-seed diagnostic at d = 12, r = 6, with 320 repetitions per sample size. Solid
curves are medians and dashed curves are 90th percentiles. The first three panels display
tangential relative error, ordinary smallest-eigenvalue relative error, and radial eigenspace
angle. The fourth compares the exact empty-slab probability with its simulated frequency;
exact values below 10−8 are clipped only in the plot and remain untruncated in the JSON
certificate. The normalization n/(rd) is the sharp scale for full bilateral relative Loewner loss;
the ordinary eigenvalue and angle panels are diagnostics and make no claim that this is their
optimal threshold.


9                                                            What the law costs
9.1                                                           Stationary fixed-step gradient descent
For either logistic profile, assume d ≥ 2 and that one constant scalar step size η is reused at
every iteration. At the teacher, the Jacobian of one gradient-descent step is I − ηHh . Its radial
eigenvalue is 1 − ηβ and its tangential eigenvalue is 1 − ηα. The best scalar step for this local


                                                                                                                27
```

---

## Page 28

```text
quadratic model is
                                    2                    α−β   κ−1
                            η? =       ,          ρ? =       =     .                       (91)
                                   α+β                   α+β   κ+1
Consequently − log ρ? ∼ 2/κ. For worst-case local error with components allowed in both
eigenspaces, the e-folding iteration count Te := (− log ρ? )−1 therefore has the exact leading
scaling
                                         3                    3
                            Te,sq ∼            r2 ,  Te,B ∼ 2 r2                          (92)
                                    2(π 2 − 6)               2π
for the optimally tuned stationary scalar-step linearization. This is not a global iteration
bound or an algorithm-independent obstruction: away from the teacher the Hessian contains
residual terms, and nonstationary polynomial methods can exploit the two-point spectrum.
Indeed, the scalar schedule η1 = 1/α, η2 = 1/β makes (I − η2 H)(I − η1 H) = 0 in this exact
local quadratic. Natural-gradient or matrix-preconditioned updates can also remove the local
condition number by acting differently on the two eigenspaces.

9.2   Estimation
For n independent Gaussian-output observations with known variance τ 2 , the Fisher informa-
tion is nHh2 /τ 2 . The Cramér–Rao inequality gives, along any unit tangential vector v ⊥ u
and the radial vector u,

                                        τ2                            τ2
                        Var(v > w)
                                b ≥           ,        Var(u> w)
                                                              b ≥           .              (93)
                                      nα2 (r)                       nβ2 (r)

The ratio of the displayed radial lower bound to the tangential lower bound is κ2 (r). Hence
tangential variance is bounded below at order r/n, while radial variance is bounded below
at order r3 /n. The analogous Bernoulli bounds replace h2 by h1 . The same quadratic ratio
therefore appears in these coordinatewise information lower bounds and in stationary fixed-step
descent, although the latter can be removed by a nonstationary schedule.


10    Bias and universality
A conventional neuron includes a bias b. At b = 0 the augmented parameter (w, b) has
Fisher/Hessian block
                                          XX > X
                                                
                               E h(rZ)               .
                                           X>   1
For even h, the radial–bias cross term E[Zh(rZ)] vanishes. The bias eigenvalue equals αh (r),
so the spectrum contains one radial eigenvalue βh and d tangential/bias eigenvalues αh . A
nonzero bias preserves the (d − 1) tangential eigenspace but replaces the radial and bias
coordinates by the explicit 2 × 2 block

                               E[Z 2 h(rZ + b)] E[Zh(rZ + b)]
                                                             
                                                                .                       (94)
                               E[Zh(rZ + b)]     E[h(rZ + b)]

The centered theorem is therefore not an artifact of omitting the bias; it is the diagonal point
of a fully explicit two-coordinate extension.
    The exponent two is broader than the logistic curve. Theorem 4.1 shows that any localized
sensitivity profile with finite positive m0 and m2 has the same r2 anisotropy, with only the
constant m0 /m2 depending on the activation and observation model. Profiles with heavy
sensitivity tails or vanishing second moment fall outside this universality class and can have
different laws.


                                                  28
```

---

## Page 29

```text
11    Relation to prior work
Table 1 states the claim boundary before the detailed discussion.

  Prior result                   Result here                     Exact difference
  Fixed-order                    closed logistic determinant     explicit specialization and
  Löwner/Schwarzian              and certified 2 × 2 witness     certificate; not a new criterion or
  criterion and serial closure                                   closure law
  [3, 4]
  One-unit Gaussian Fisher       spherical local bridge and      coefficient cross-identification and
  split for φ02 [25]             Gaussian all-p laws             extensions; not a new one-unit
                                                                 decomposition
  Bernoulli exponents and        pointwise and shell-uniform     tunable precision and all powers;
  finite-sample logistic         relative Gram bounds,           log obstruction is iterated, not a
  Hessian bounds                 matching pointwise              matching finite-sample shell
  [16, 19, 18, 22]               complexity, and an intrinsic    theorem
                                 angular log
  Scaled-SVD flags [8] and       spectral lexicography, exact    flag mechanism is classical; logistic
  Gaussian logistic              angle law, and joint            ordering and joint certificate are
  direction/Hessian theory       finite-saturation resolution    the refinement; not labeled
  [15, 18, 16, 17]                                               estimation or a crossover-sharp
                                                                 rate
  Classical spherical            exact QR constants and three    leading constants and critical
  representation [7] and         inverse-radius phases           logarithm; not a new spherical
  regular-design reference                                       representation or first
  exponents [18]                                                 non-Gaussian exponent
  Generalized-logistic           Gamma/polygamma                 transform is classical; the unified
  transforms and cumulants       moments inside neuronal         anisotropy, endpoint laws and
  [27, 26]                       anisotropy                      monotonicity are the contribution
  Lam’s historical v2            Löwner–anisotropy coefficient   different objects and coefficient; no
  Fisher–Schwarzian              identity                        claim to the first general
  construction [28]                                              Fisher–Schwarzian connection

                           Table 1: Result-by-result priority boundary.

    Löwner matrices characterize fixed-order matrix monotonicity; modern treatments include
Hiai–Sano and Heinävaara [1, 2]. Kozlovski and Sands prove the relevant classical equivalence
between Sf ≥ 0 and order-two matrix monotonicity and record the Schwarzian composition
law [3]. Hence the qualitative logistic obstruction and its serial-chain extension are classical
consequences; negative Schwarzian also implies the all-pair determinant sign through strict
convexity of (f 0 )−1/2 . Cook, Hammerlindl and Tucker develop the algebraically equivalent
nowhere-coexpanding inequality, prove serial closure, and explicitly discuss sigmoid activations
and one-dimensional neural compositions [4]. Neural papers have proposed analytic quantum
activations and trainable matrix activations [5, 6], but their objectives are circuit implementa-
tion or matrix-valued parameterization, not preservation of PSD order by the spectral logistic
function. In the primary sources we located, we did not find the closed logistic identity (3), the
explicit certified witness, or the coefficient identity (35) linking the Löwner defect to Gaussian
radial–tangential anisotropy. This is a bounded novelty statement, not a claim that no earlier
source can exist.
    Learning one neuron is already a nontrivial optimization problem. Yehudai and Shamir
study when gradient methods learn a single neuron under broad activations and input dis-
tributions, including positive and negative results [10]. Diakonikolas et al. treat monotone
neurons with adversarial label noise and obtain polynomial learners for logistic activations
under log-concave inputs [11]. Wu extends learnability results to nonmonotone activations

                                                  29
```

---

## Page 30

```text
[12], and Vardi et al. show that adding a bias qualitatively changes the ReLU landscape
[13]. Recent single-index work analyzes SGD under anisotropic Gaussian inputs [14]. Under
Gaussian logistic regression, Hsu and Mazumdar study the signal-dependent difficulty of
direction and temperature estimation [15]. Chen and Mazumdar identify the Bernoulli radial
and tangential Hessian functions, prove their r−3 and r−1 orders and show tangential curvature
                                 p nonzero signal [16]; they subsequently prove a minimax
exceeds radial curvature for every
norm-estimation rate of order r3 /n [17]. Ostrovskii and Bach prove a uniform bilateral
constant-factor empirical-Hessian sandwich for Gaussian logistic regression [19, Eq. (92)],
while Fisher et al. give a generic fixed-point standardized-Hessian concentration framework
[22]. Chardon, Lerasle and Mourtada prove, for p = 1, a uniform one-sided empirical Hessian
lower bound under the sufficient condition n & r(d + t) [18, Theorem 6]. We therefore do
not claim the Bernoulli exponents, the p = 1 ordering, the effective transition-slab scale, the
first bilateral Hessian concentration, or the first finite-sample lower bound. Our empirical
contribution is the explicit pointwise (1 ± ε) approximation (48) for all p > 0, its matching
bilateral lower complexity, the full-dyadic-shell extension (86), the angular-log obstruction
(87), the distinct extreme-saturation projector law (70), and its joint certificate (77). The
shell upper theorem still pays additional conservative covering terms and is not asserted to
improve the optimal local one-sided rate; the joint projector threshold is sufficient rather than
crossover-sharp. Stewart’s scaled-SVD analysis already supplies the underlying deterministic
flag mechanism [8]. In the primary sources searched through August 30, 2026, we did not
locate the logistic nearest-hyperplane projector, its exact angle law, finite hierarchy certificate,
or the marked angular-log obstruction for this neuronal Gram process. This is a bounded
search statement, not a guarantee of priority. Recent work already constructs minimax labeled
estimators, including a split-sample direction/norm scheme with bias correction [17]; our oracle
Gram theorem is not an estimator.
    Fisher geometry and natural gradient are classical [23]. Karakida et al. study broad Fisher
spectral statistics for random deep networks [24]; Amari, Karakida and Oizumi also give
the direct one-unit Gaussian φ02 decomposition and bias coupling used here [25]. Our radial
contribution is therefore not the two-eigenspace reduction. It is the profile-generic moment
theorem, nonasymptotic brackets, closed all-power logistic constants, strict global monotonicity,
and their connection through (35) to the Löwner order defect. The generalized-logistic Gamma
transform and its polygamma cumulants in Lemma 7.1 are classical [27, 26]; the claim is
their neural-geometric use, ratio monotonicity and endpoint package, not discovery of the
distributional identity. Lam’s v2 preprint connected Schwarzian curvature with Fisher–Rao
geometry on manifolds of densities [28]. The current v3 explicitly corrects and supersedes v1–v2
and removes that architecture [29]. Neither version contains the one-neuron radial–tangential
coefficient or its equality with the two-point Löwner defect. We cite v2 only as a dated
historical adjacency; its Lp parameter is unrelated to the sensitivity exponent in hp = σ 0p .


12    Reproducibility and hostile checks
The documented sequence in repro/README.md runs the original and v3 checks together with
four newer scripts:

radial_phase_transition.py, spectral_lexicography.py, verify_v4_additions.py,
            joint_spectral_resolution.py, verify_v5_additions.py.

Together they perform the following independent checks:

  1. it spot-checks (3) at separated scales and constructs Proposition 2.2 with 256-bit directed
     Arb balls;


                                                30
```

---

## Page 31

```text
2. it checks the spherical fourth-moment coefficient for Gaussian and fixed-radius spherical
    inputs;

 3. it compares numerical quadrature of m0 , m2 , m4 with the Gamma/polygamma formula
    for several noninteger and integer p;

 4. it checks the small-r jet through r6 and the refined large-r expansion;

 5. it evaluates α, β directly over a logarithmic radius grid and checks positivity and grid
    monotonicity for p = 1, 2;

 6. it checks (37)–(39) at declared finite scales;

 7. for three declared fixed random seeds it evaluates the empirical radial, tangential and
    cross blocks and verifies that those realized errors lie inside (46);

 8. it checks both sides of (19)–(20) at declared finite radii;

 9. a second replay evaluates the explicit C1 , C2 majorants and lower-bound constants; and

10. a fixed-seed replay regenerates Figure 5 and its JSON certificate, while the main replay
    regenerates Figure 2 and its certificate;

11. deterministic adaptive quadrature regenerates Figure 1 and checks all three exact phase
    constants for isotropic Gamma radii; and

12. a fixed-seed eigenspace replay regenerates Figure 3, while a separate check validates the
    explicit Lp , Kp confidence constants and the sample-wise normal-vector identity.

13. a fixed-sample hierarchy replay regenerates Figure 4 and checks the exact data-dependent
    projector certificate and its closed logistic envelope at every numerically stable radius.

14. a v5 verifier checks the joint-threshold constants, random sample-wise hierarchy certificates
    and the angular-process variance constant for p = 1, 2.

The numerical monotonicity and finite-radius checks are performed on declared grids; the uni-
versal statements are proved analytically above. The replay uses Python, python-flint, NumPy,
SciPy, and Matplotlib. It is diagnostic rather than a substitute for the analytic proofs, which
reduce to the Löwner determinant identity, the Schwarzian chain rule, Gaussian orthogonal de-
composition, Bernstein/net bounds, an Abelian kernel lemma, exterior powers, elementary order
statistics and spacings, Gaussian-process separation, an explicit Gaussian lower tail, and closed
Fourier moments. The stable record, versioned source archives, audit reports and manifests
are public at https://arr-research.github.io/papers/ARR-2026-53CTRKDSP685PT51/.


13    Limitations and next theorem
The Löwner theorem concerns spectral matrix functions, not entrywise vector activations; it
does not say that a standard feedforward neuron reverses coordinatewise order. The empirical
results assume Gaussian input. The local Schwarzian coefficient needs fourth moments, whereas
the spherical asymptotic law needs transition-layer regularity; ER−1 < ∞ is needed precisely
for its quadratic phase, with the other phases covered by Theorem 5.3. Covariance isotropy
alone is insufficient by the Rademacher example following it. Elliptical laws can be whitened,
but radial/tangential directions then use the covariance metric.
    The sharp Gram complexity statement is pointwise for a fixed teacher and bilateral relative
Loewner loss. The exact bottom-eigenspace law remains an iterated limit, while Theorem 8.9

                                               31
```

---

## Page 32

```text
supplies only a conservative joint sufficient regime of order r & (n/δ) log(poly(n, d)/(εδ));
it does not characterize the crossover r  n or give a matching joint lower bound. The
                                      √ its full Euclidean-net logarithm is not quantitatively
dyadic-shell upper theorem is uniform but
sharp. Theorem 8.11 proves that one log R angular penalty is intrinsic in an iterated limit,
not that all current covering terms are necessary. A matching nonasymptotic shell lower
bound and a chaining upper bound remain open. None of these oracle results is an estimator
guarantee using labels or a minimax parameter lower bound. The optimization result remains
local, and the Cramér–Rao statement concerns regular unbiased estimation.


AI assistance disclosure
AI tools assisted with public-literature and repository triage, proof stress testing, numerical
replay, drafting, and PDF production. The author remains responsible for the mathematical
claims and any remaining errors.


References
 [1] F. Hiai and T. Sano, Löwner matrices of matrix convex and monotone functions, Journal of the
     Mathematical Society of Japan 64(2) (2012), 343–364. https://arxiv.org/abs/1007.2478
 [2] O. Heinävaara, Characterizing matrix monotonicity of fixed order on general sets, preprint (2019).
     https://arxiv.org/abs/1906.06155
 [3] O. Kozlovski and D. Sands, Higher order Schwarzian derivatives in interval dynamics, Fundamenta
     Mathematicae 206 (2009), 217–239. https://arxiv.org/abs/0812.2646
 [4] A. Cook, A. Hammerlindl and W. Tucker, Nowhere coexpanding functions, Chaos 33 (2023),
     123105. https://arxiv.org/abs/2303.12814
 [5] M. Maronese, C. Destri and E. Prati, Quantum activation functions for quantum neural networks,
     Quantum Information Processing 21 (2022), 128. https://arxiv.org/abs/2201.03700
 [6] Z. Liu, S. Cao, Y. Li and L. Zikatanov, Neural networks with trainable matrix activation functions,
     Journal of Machine Learning for Modeling and Computing 6(2) (2025), 1–11. https://arxiv.
     org/abs/2109.09948
 [7] S. Cambanis, S. Huang and G. Simons, On the theory of elliptically contoured distributions, Jour-
     nal of Multivariate Analysis 11(3) (1981), 368–385. https://doi.org/10.1016/0047-259X(81)
     90082-8
 [8] G. W. Stewart, On the asymptotic behavior of scaled singular value and QR decompo-
     sitions, Mathematics of Computation 43(168) (1984), 483–489. https://doi.org/10.1090/
     S0025-5718-1984-0758196-7
 [9] A. Sankar, D. A. Spielman and S.-H. Teng, Smoothed analysis of the condition numbers and growth
     factors of matrices, SIAM Journal on Matrix Analysis and Applications 28(2) (2006), 446–476.
     https://doi.org/10.1137/S0895479803436202
[10] G. Yehudai and O. Shamir, Learning a Single Neuron with Gradient Methods, Proceedings of
     Machine Learning Research 125 (2020), 3756–3786. https://proceedings.mlr.press/v125/
     yehudai20a.html
[11] I. Diakonikolas, V. Kontonis, C. Tzamos and N. Zarifis, Learning a Single Neuron with Adversarial
     Label Noise via Gradient Descent, Proceedings of Machine Learning Research 178 (2022), 4313–4361.
     https://proceedings.mlr.press/v178/diakonikolas22c.html
[12] L. Wu, Learning a Single Neuron for Non-monotonic Activation Functions, Proceedings of Machine
     Learning Research 151 (2022), 4178–4197. https://proceedings.mlr.press/v151/wu22c.html
[13] G. Vardi, G. Yehudai and O. Shamir, Learning a Single Neuron with Bias Using Gradient
     Descent, Advances in Neural Information Processing Systems 34 (2021), 28690–28700. https:
     //arxiv.org/abs/2106.01101

                                                  32
```

---

## Page 33

```text
[14] G. Braun, M. H. Quang and M. Imaizumi, Learning a Single Index Model from Anisotropic Data
     with Vanilla Stochastic Gradient Descent, Proceedings of Machine Learning Research 258 (2025),
     1216–1224. https://proceedings.mlr.press/v258/braun25a.html
[15] D. Hsu and A. Mazumdar, On the Sample Complexity of Parameter Estimation in Logistic
     Regression with Normal Design, Proceedings of Machine Learning Research 247 (2024), 2418–2437.
     https://proceedings.mlr.press/v247/hsu24a.html
[16] J. Chen and A. Mazumdar, Finite-Sample Performance of Gradient Descent in Logistic Regression
     with Gaussian Design, arXiv:2606.21683 (2026). https://arxiv.org/abs/2606.21683
[17] J. Chen and A. Mazumdar, Minimax Optimal Estimator and Improved Error Rate for the MLE
     in Logistic Regression with Gaussian Design, arXiv:2608.17260 (2026). https://arxiv.org/abs/
     2608.17260
[18] H. Chardon, M. Lerasle and J. Mourtada, Finite-sample performance of the maximum likelihood
     estimator in logistic regression, arXiv:2411.02137v3 (first posted 2024; v3 2026). https://arxiv.
     org/abs/2411.02137v3
[19] D. M. Ostrovskii and F. Bach, Finite-sample analysis of M-estimators using self-concordance,
     Electronic Journal of Statistics 15(1) (2021), 326–391. https://doi.org/10.1214/20-EJS1780
[20] P. J. Bickel and M. Rosenblatt, On some global measures of the deviations of density function esti-
     mates, Annals of Statistics 1(6) (1973), 1071–1095. https://doi.org/10.1214/aos/1176342558
[21] E. Giné, V. Koltchinskii and L. Sakhanenko, Kernel density estimators: convergence in distribution
     for weighted sup-norms, Probability Theory and Related Fields 130 (2004), 167–198. https:
     //doi.org/10.1007/s00440-003-0314-z
[22] J. Fisher, L. Liu, K. Pillutla, Y. Choi and Z. Harchaoui, Influence Diagnostics under Self-
     concordance, Proceedings of Machine Learning Research 206 (2023), 10028–10076. https://
     proceedings.mlr.press/v206/fisher23a.html
[23] S.-i. Amari, Natural Gradient Works Efficiently in Learning, Neural Computation 10 (1998),
     251–276. https://doi.org/10.1162/089976698300017746
[24] R. Karakida, S. Akaho and S.-i. Amari, Universal Statistics of Fisher Information in Deep Neural
     Networks: Mean Field Approach, Proceedings of Machine Learning Research 89 (2019), 1032–1041.
     https://proceedings.mlr.press/v89/karakida19a.html
[25] S.-i. Amari, R. Karakida and M. Oizumi, Fisher Information and Natural Gradient Learning
     in Random Deep Networks, Proceedings of Machine Learning Research 89 (2019), 694–702.
     https://proceedings.mlr.press/v89/amari19a.html
[26] C. J. Lee, A. Zito, H. Sang and D. B. Dunson, Logistic-beta processes for dependent random
     probabilities with beta marginals, Bayesian Analysis 20(4) (2025), 1345–1369. https://doi.org/
     10.1214/25-BA1541
[27] M. O. Ojo and A. K. Olapade, On a Six-Parameter Generalized Logistic Distribution,
     Kragujevac Journal of Mathematics 26 (2004), 31–38. https://imi.pmf.kg.ac.rs/kjm/pub/
     12616736649184_5.pdf
[28] H. P. G. Lam, Real Bers embedding on the line: Fisher–Rao linearization, Schwarzian curvature,
     and scattering coordinates, arXiv:2602.07373v2 (2026). https://arxiv.org/abs/2602.07373v2
[29] H. P. G. Lam, Zero-energy scattering and the real Bers image on the line, arXiv:2602.07373v3
     (2026), correcting and superseding v1–v2. https://arxiv.org/abs/2602.07373v3




                                                  33
```
