# The Schwarzian Bridge in a Single Sigmoid Neuron: Spherical Inputs, All-Power Laws, and Empirical Resolution

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
The Schwarzian Bridge in a Single Sigmoid Neuron
      Spherical Inputs, All-Power Laws, and Empirical Resolution

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

  For n samples we prove an explicit two-sided relative Löwner bound for the weighted
  empirical Gram matrix, radial-eigenvalue and eigenspace-angle bounds, and the sufficient
  logistic scaling n ≥ Cp r[d + log(1/δ)]/ε2 , with a computable constant depending only on p.
  An empty-transition-slab argument proves a necessary cp r log(1/δ) term, while a matching
  product lower bound remains open. Prior work contains a one-sided p = 1 empirical
  bound, bilateral constant-factor Hessian sandwiches, the Bernoulli population exponents,
  and the one-unit squared-output reduction. Our additions include an explicit pointwise,

                                                    1
```

---

## Page 2

```text
block-resolved (1 ± ε) theorem for every logistic power p > 0, with saturation scaling, angle
        control and a slab obstruction, together with the spherical and quantitative bridges and
        unified all-p endpoint laws. A deterministic replay and immutable public source record
        accompany the proofs.

Keywords. single neuron; sigmoid; matrix monotonicity; Löwner order; Schwarzian deriva-
tive; Fisher information; Gaussian design; weighted sample covariance; finite-sample concen-
tration.


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

    6. a two-sided relative concentration theorem for the empirical sensitivity matrix, with
       an explicit radial-eigenvector angle, all-p logistic threshold and necessary slab/rank
       obstructions; and

    7. exact local consequences for stationary fixed-step optimization and estimation, plus a
       one-command replay of the identities, interval witness, inequalities, and figure.
    The matrix-order theorem concerns spectral functional calculus σ(A), not entrywise activa-
tion of a vector. The radial theorem is not a claim about deep networks, global optimization,
implicit bias, or arbitrary inputs. Its local coefficient extends from Gaussian to isotropic
spherical inputs, while its large-saturation constants remain Gaussian. The two questions meet
at a precise boundary: scalar monotonicity controls neither noncommuting PSD perturbations
nor the conditioning of parameter directions.

                                                     2
```

---

## Page 3

```text
2    A sigmoid is not an order-preserving operator
For Hermitian matrices, A  B means that B − A is positive semidefinite. A scalar function
f is matrix-monotone of order two on an interval J if f (A)  f (B) for every pair of 2 × 2
Hermitian matrices with spectra in J and A  B, where f (A) is defined by spectral functional
calculus. If A and B commute, scalar monotonicity is sufficient because they are simultaneously
diagonalizable. The question is what happens without commutativity.
    For distinct x, y ∈ J, define the two-point Löwner matrix
                                                       f (x) − f (y)
                                                                    
                                              0
                                             f (x)
                           Lf (x, y) =  f (x) − f (y)     x−y                              (1)
                                                                     .
                                                                    
                                                           f 0 (y)
                                             x−y
The fixed-order Löwner criterion says that matrix monotonicity of order two requires Lf (x, y) 
0 for every pair [1, 2]. The equivalent local criterion Sf ≥ 0 for increasing smooth functions
is classical [3, Lemma 10]; the result below is an explicit logistic specialization, not a new
qualitative matrix-monotonicity criterion.
    Cook, Hammerlindl and Tucker define
                                                                   2
                                          0    0          x−y
                             χf (x, y) = f (x)f (y)
                                                      f (x) − f (y)

and study the class χf ≤ 1, including sigmoid activations and serial compositions [4]. If
Df (x, y) = (f (x) − f (y))/(x − y), then

                              det Lf (x, y) = Df (x, y)2 [χf (x, y) − 1].                       (2)

Thus their two-point inequality is algebraically the nonpositive Löwner-determinant inequality.
Our contribution in this subsection is the strict closed logistic identity and the certified matrix
witness, not the underlying Schwarzian/composition mechanism.

Theorem 2.1 (closed logistic two-point determinant). Let
                                                  1
                                sα,b (x) =                  ,   α > 0.
                                             1 + e−α(x−b)
For every x 6= y, the Löwner matrix Lsα,b (x, y) has negative determinant. Consequently the
logistic activation is not matrix-monotone of order two on any nondegenerate interval.

Proof. Put u = eα(x−b) , v = eα(y−b) , and r = v/u = eα(y−x) . Direct cancellation gives the
exact identity
                                              α2 u2            (r − 1)2
                                                                       
                    det Lsα,b (x, y) =                      r−            .               (3)
                                        (1 + u)2 (1 + v)2      (log r)2
For r 6= 1, write t = log r. Strict convexity of sinh on (0, ∞) gives
                                                                  √
                         |r − 1| = 2et/2 | sinh(t/2)| > et/2 |t| = r | log r|.

The bracket in (3) is therefore strictly negative. Every nondegenerate interval contains a
distinct pair, so the Löwner criterion completes the proof.

    This is stronger than finding one bad scale: changing the slope α, shifting the bias b,
or restricting the score range never removes the obstruction. It also identifies the precise
failure. The diagonal entries in (1) are positive, but the divided difference is too large for their
geometric mean.

                                                   3
```

---

## Page 4

```text
Proposition 2.2 (dimension-minimal explicit PSD witness). For the standard logistic sigmoid,
let                                                           
                           −1/2 0                      1    1 1
                    A=                 ,     B =A+                 .                     (4)
                            0    1/2                  100 1 1
Then A  B but σ(A)  σ(B). At 256-bit outward-rounded Arb precision,
                      spec(B) ⊂ [−0.4901000, −0.4900999] ∪ [0.5100999, 0.5101000],            (5)
          spec(σ(B) − σ(A)) ⊂ [−9.9150, −9.9147] 10      −5
                                                              ∪ [0.0047990, 0.0047992],       (6)
           det(σ(B) − σ(A)) ∈ [−4.7583, −4.7581] 10−7 .                                       (7)

Proof. B − A has eigenvalues 0 and 1/50. If a = 1/2, ε = 1/100, and d = (a2 + ε2 )1/2 , then B
has eigenvalues λ± = ε ± d and
                                               σ(λ+ ) + σ(λ− )          σ(λ+ ) − σ(λ− )
           σ(B) = mI + n(B − εI),        m=                    ,   n=                   .
                                                      2                       2d
Substitution reduces the three enclosures to scalar exponential and square-root balls. The
replay evaluates them with directed Arb rounding; the negative eigenvalue in (6) proves the
claim.

   The witness is illustrative, while Theorem 2.1 is the proof for every interval. The derivative
form also explains why an indefinite Löwner matrix produces witnesses: for diagonal A =
diag(x, y), the Fréchet derivative in the all-ones PSD direction is precisely the Schur product
with Lf (x, y).

2.1   Serial depth does not repair the order
For a C 3 function with nonzero derivative, its Schwarzian is
                                         f 000 3 f 00 2
                                                   
                                   Sf = 0 −              .                                    (8)
                                          f      2 f0
The logistic sigmoid and a scaled hyperbolic tangent satisfy
                                      α2
                          Ssα,b = −      ,     S tanh(αx + β) = −2α2 .                        (9)
                                      2
Corollary 2.3 (serial spectral reformulation). Let F be a finite scalar composition of positive-
slope affine maps and at least one increasing logistic or hyperbolic-tangent activation. Then
SF < 0 everywhere, and F is not matrix-monotone of order two on any nondegenerate interval.
Proof. The composition identity
                                 S(f ◦ g) = (Sf ◦ g)(g 0 )2 + Sg                            (10)
and (9) give SF < 0, since positive affine maps have zero Schwarzian and all derivatives in the
chain are positive. For h → 0, Taylor expansion of the two-point determinant gives
                                               F 0 (x)2
                         det LF (x, x + h) =            SF (x) h2 + O(h3 ).                 (11)
                                                   6
It is negative for all sufficiently small nonzero h. Every interval contains such a pair.

    The corollary restates, in spectral Löwner order, the serial closure proved in the nowhere-
coexpanding framework [4]. It is deliberately about serial scalar chains. It does not cover
sums of neurons, skip connections, multivariate architectures, or entrywise coordinate order.
Its content is that composing more of the same S-shaped bend cannot turn the resulting scalar
function into a PSD-order-preserving spectral activation.

                                                 4
```

---

## Page 5

```text
3    Two models, one sensitivity matrix
Write r = kw? k and u = w? /r when r > 0. We use two standard observation models.

Squared-output regression.          For the realizable population loss
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
sition for h = φ02 , including the radial–tangential split and the bias block [20]. We do not claim
that decomposition or the squared-output branch as new. For the Bernoulli profile h = σ 0 ,
Chen and Mazumdar recently identified the same radial and orthogonal Hessian functions and
proved their r−3 and r−1 orders in a finite-sample analysis  p of logistic regression [13]. Their
follow-up proves the minimax norm-estimation rate Θ( r3 /n) [14]. We do not claim those
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

                            Hh (r, u) = αh (r)(I − uu> ) + βh (r)uu> ,                        (16)

where
                 αh (r) = Eh(rZ),       βh (r) = E[Z 2 h(rZ)],     Z ∼ N (0, 1).              (17)

                                                5
```

---

## Page 6

```text
If m0 , m2 < ∞ and are positive, then

                        ϕ(0)m0                  ϕ(0)m2                      αh (r)   m0 2
             αh (r) ∼          ,     βh (r) ∼          ,       κh (r) :=           ∼    r .            (18)
                           r                      r3                        βh (r)   m2

If m0 , m2 , m4 < ∞, the following nonasymptotic brackets hold for every r > 0:

                              ϕ(0)      m2           ϕ(0)m0
                                     m0 − 2 ≤ αh (r) ≤        ,                                        (19)
                               r         2r               r
                              ϕ(0)      m4           ϕ(0)m2
                                     m2 − 2 ≤ βh (r) ≤        .                                        (20)
                               r3        2r              r3
Negative lower endpoints are interpreted as valid but uninformative bounds.

Proof. Decompose X = Zu + Y , where Z ∼ N (0, 1), Y ∼ N (0, I − uu> ), and Z, Y are
independent. The mixed terms vanish and EY Y > = I − uu> , giving (16)–(17). Changing
variables t = rz gives the exact one-dimensional formulae
                           Z                                    Z
                      ϕ(0)                                 ϕ(0)
                                   −t2 /(2r2 )
                                                                                         (21)
                                                                             2    2
             αh (r) =         h(t)e            dt, βh (r) = 3      t2 h(t)e−t /(2r ) dt.
                       r    R                               r    R

Dominated convergence proves (18). Finally, 1 − x ≤ e−x ≤ 1 for x ≥ 0 inserted into (21)
proves (19)–(20).


5   Spherical and finite-scale Schwarzian bridges
The matrix-order and saturation calculations meet exactly at an inflection point. Gaussian
independence makes the full saturation curve one-dimensional, but it is not responsible for the
local bridge: rotational symmetry and suitable moments suffice. The fourth moment identifies
the coefficient below; the stated sixth moment controls its O(r4 ) remainder.

Theorem 5.1 (spherical local order–anisotropy bridge). Let d ≥ 2 and let X ∈ Rd be isotropic
and spherically symmetric with EkXk6 < ∞. Let g ∈ C 5 (R) satisfy g 0 > 0 and g 00 (0) = 0. For
p > 0, suppose hp = (g 0 )p has bounded fourth derivative. For u ∈ S d−1 put Z = u> X and
                                                                                              αp,X
     Hp,X (r, u) = E[hp (rZ)XX > ] = αp,X (r)(I − uu> ) + βp,X (r)uu> ,             κp,X =         .
                                                                                              βp,X

Then, with
                                                   EkXk4
                                          qX :=            ,
                                                  d(d + 2)
one has
                      κp,X (r) − 1                  6qX p     det Lg (0, δ)
                  lim        2
                                   = −qX p Sg(0) = − 0 2 lim                .                          (22)
                  r↓0      r                        g (0) δ→0      δ2
In particular, Sg(0) < 0 makes Lg (0, δ) indefinite and κp,X (r) > 1 at all sufficiently small
nonzero scales. Standard Gaussian input has qX = 1.

Proof. Rotations fixing u force the displayed two-eigenspace form, with
                                                            1
             βp,X (r) = E[Z 2 hp (rZ)],      αp,X (r) =        E[(kXk2 − Z 2 )hp (rZ)].
                                                           d−1
Choose a unit v ⊥ u. Spherical symmetry and isotropy give

                              EZ 4 = 3qX ,        E[Z 2 (v > X)2 ] = qX .

                                                  6
```

---

## Page 7

```text
Taylor’s formula, cancellation of odd terms under X = −X, and the sixth-moment assumption
                                                               d

therefore give

                           qX h00p (0) 2                                         3qX h00p (0) 2
     αp,X (r) = hp (0) +              r + O(r4 ),          βp,X (r) = hp (0) +               r + O(r4 ).
                               2                                                     2
Taking the ratio yields κp,X (r) = 1 − qX h00p (0)r2 /hp (0) + O(r4 ). Since log hp = p log g 0 and
g 00 (0) = 0,
                                  h00p (0)   g 000 (0)
                                           =p 0        = pSg(0).
                                  hp (0)      g (0)
The adjacent-point expansion (11) gives the remaining equality.

    The equality of limits has a computable finite-scale version. The constants below are
deliberately explicit rather than optimized.

Theorem 5.2 (explicit finite-scale bridge). Under Gaussian input, retain the hypotheses of
Theorem 5.1 and write

                              a = hp (0),      b = h00p (0),   M4 = kh(4)
                                                                      p k∞ .

Choose r0 > 0 so that
                                           3|b| 2 5M4 4 a
                                               r +   r ≤ ,                                                 (23)
                                            2 0    8 0  2
and set                                                2
                                        3M4            b     5|b|M4 2
                                 Ch =       +3             +       r .
                                         2a            a       4a2 0
For a chosen δ0 > 0, put

                   A = g 0 (0), c = g 000 (0), d4 = g (4) (0), M5 = sup |g (5) (x)|,
                                                                        |x|≤δ0


                    |c| |d4 |δ0 M5 δ02                         |Ad4 | 7AM5 δ0
                K=     +        +      ,                Dg =         +        + δ0 K 2 .
                     6     24      120                          12      120
Then for 0 < r ≤ r0 and 0 < |δ| ≤ δ0 ,

                                 κp (r) − 1 + pSg(0)r2 ≤ Ch r4 ,                                           (24)
                                               A2 Sg(0)
                             det Lg (0, δ) −         δ 2 ≤ Dg |δ|3 ,                                       (25)
                                              6
                           κp (r) − 1  6p det Lg (0, δ)              6pDg
                                 2
                                      + 2        2
                                                         ≤ Ch r 2 +       |δ|.                             (26)
                               r       A       δ                      A2

Thus the order defect predicts anisotropy at finite, independently chosen scales with a certified
error bar.

Proof. Gaussian Taylor remainders give
               b                            M4 4                      3b 2                     5M4 4
       αp = a + r2 + Rα ,        |Rα | ≤      r ,          βp = a +     r + Rβ ,     |Rβ | ≤      r .
               2                            8                         2                         8
Condition (23) makes βp ≥ a/2. Subtracting 1 − (b/a)r2 before dividing by βp yields
                                    "           2              #
                             b 2      3M4        b      5|b|M4 2 4
                    κp − 1 + r ≤           +3        +         r r ,
                             a         2a        a        4a2 0

                                                       7
```

---

## Page 8

```text
which is (24) because b/a = pSg(0).
   Taylor expansion at zero gives
                            c     d4             g(δ) − g(0)      c     d4
               g 0 (δ) = A + δ 2 + δ 3 + R1 ,                = A + δ 2 + δ 3 + R2 ,
                            2     6                   δ           6     24
where |R1 | ≤ M5 |δ|4 /24 and |R2 | ≤ M5 |δ|4 /120. Writing the determinant as A(g 0 (δ) − A) −
2A(V − A) − (V − A)2 , with V = (g(δ) − g(0))/δ, gives (25) with the displayed Dg . Finally,
divide (24) by r2 , divide (25) by δ 2 , multiply the latter by 6p/A2 , and use the triangle
inequality.

    For the standard logistic sigmoid, Sσ = −1/2. Theorem 5.1 therefore predicts the exact
initial coefficient p/2 for every hp = σ 0p , recovered globally below. Equation (26) strengthens
the conceptual coefficient match into a falsifiable finite-scale comparison.
    For a general h, κh = αh /βh in (18) is an anisotropy ratio; it is the spectral condition
number only after the eigenvalue ordering is known. The two powers are geometric. At large
r, only a score slab of width O(r−1 ) remains unsaturated, producing α  r−1 . A radial
perturbation carries an additional factor Z 2 = O(r−2 ) inside that slab, producing β  r−3 .
Both modes are supported by the near-boundary slab; the radial mode is weaker because it
carries the additional Z 2 factor.


6     All-power logistic saturation laws
For every real p > 0 set hp (t) = σ 0 (t)p . The cases p = 1 and p = 2 are Bernoulli Fisher
and squared-output curvature, respectively, but the analytic law is not restricted to those
observation models. The Gamma transform below is classical generalized-logistic distribution
theory [22, eqs. (2.3)–(2.5)]; our use of it is geometric.
Lemma 6.1 (closed sensitivity moments for every p > 0). Let ψj denote the polygamma
function of order j. Then
                                                     Γ(p + ik)Γ(p − ik)
                                 Z
                       hp (k) :=
                       b            eikt hp (t) dt =                    ,        (27)
                                  R                        Γ(2p)
and
               Γ(p)2
                                                           m4 (p) = 12ψ1 (p)2 + 2ψ3 (p) m0 (p).   (28)
                                                                                       
    m0 (p) =         ,     m2 (p) = 2ψ1 (p)m0 (p),
               Γ(2p)
In particular,

                           profile     m0         m2                  m4
                          h1 = σ0      1         π 2 /3              7π 4 /15
                          h2 = σ 02   1/6    (π 2 − 6)/18      7π 4 /90 − 2π 2 /3

Proof. With x = et ,
                                                 Z ∞
                           xp                             xp+ik−1
               hp (t) =           ,   hp (k) =
                                      b                            dx = B(p + ik, p − ik),
                        (1 + x)2p                0       (1 + x)2p

which proves (27). Since hp (t) = O(e−p|t| ), all polynomial moments are finite and differentiation
under the Fourier integral is justified. Differentiating its logarithm at zero gives (log b
                                                                                          hp )00 (0) =
                  hp )(4) (0) = 2ψ3 (p). Since m2 = −b
−2ψ1 (p) and (log b                                                       hp (0), (28) follows. The
                                                        h00p (0) and m4 = b
                                                                            (4)

table uses the standard integer polygamma values.

                                                     8
```

---

## Page 9

```text
Theorem 6.2 (strict all-power logistic anisotropy). For every p > 0, κp (0) = 1, κp (r) > 1 for
r > 0, and κp is strictly increasing on (0, ∞). At the two endpoints,
                                                                              p    p     p(p + 1) 6
                                                                  κp (r) = 1 + r2 − r4 +         r + O(r8 )                                         (r ↓ 0),                    (29)
                                                                              2    8        16
and
                                                                                     r2         ψ3 (p)
                                                                       κp (r) =            +1+          + O(r−2 )                          (r → ∞).                             (30)
                                                                                   2ψ1 (p)     4ψ1 (p)2
Thus κ1 (r) ∼ 3r2 /π 2 and κ2 (r) ∼ 3r2 /(π 2 − 6).
Proof. Normalize the density qp,r (z) ∝ hp (rz)ϕ(z). Then βp (r)/αp (r) = Eqp,r Z 2 . If r2 > r1 ,
the derivative on z > 0 of the log likelihood ratio is
                                                             d      hp (r2 z)                                      
                                                                log           = −p r2 tanh(r2 z/2) − r1 tanh(r1 z/2) < 0.
                                                             dz     hp (r1 z)
Thus the distribution of |Z| under qp,r decreases strictly in monotone-likelihood-ratio order as
r increases, and its strictly increasing statistic Z 2 has decreasing expectation. Hence αp /βp
increases strictly. At r = 0 isotropy gives one. Lemma 6.1 inserted into Theorem 4.1, with
one further term in e−t /(2r ) , gives the large-r statement. More explicitly, m6 (p) < ∞ by the
                         2    2


exponential tail, and Taylor remainder bounds for e−x give
             ϕ(0)          m2     m4                          ϕ(0)        m4           
    αp (r) =         m0 − 2 + 4 + O(r−6 ) ,             βp (r) = 3 m2 − 2 + O(r−4 ) .
               r            2r    8r                              r          2r
Their ratio yields (30). Finally,
                                p 2 p(1 + 3p) 4 p(15p2 + 15p + 4) 6
                                                                                  
                        −p                                                      8
             hp (t) = 4     1− t +               t −                   t + O(t ) .
                                4          96                5760
For each fixed p > 0, every derivative of hp is bounded. Taylor’s theorem therefore bounds the
displayed remainder globally by khp k∞ |t|8 /8!; after setting t = rZ, this is integrable in both
                                    (8)

αp and βp because the Gaussian has a finite tenth moment. Inserting the Gaussian moments
through EZ 8 = 105 in the coefficients and taking the ratio gives (29).

    Figure 1 shows the two statistically canonical members of the all-power family. The solid
and dashed curves are direct Gaussian integrals; the dotted curves are the asymptotic constants
in (30).

                                             One tangential law, one radial bottleneck                                         Profile-generic large-r anisotropy: κ ≍ r2
                                                                                                                        103
                                                                                                                              square loss: h = σ 2
                                                                                                                                                0




                                     10−1                                                                                     Bernoulli Fisher: h = σ
curvature / information eigenvalue




                                                                                                                                                        0




                                     10−2                                                                               102
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




                                                   10−1                  100               101                                     10−1                 100               101
                                                            teacher weight norm r = ‖w ⋆ ‖                                                 teacher weight norm r = ‖w ⋆ ‖


Figure 1: Exact curvature/information eigenvalues and their ratio. Saturation leaves d − 1
tangential directions at order r−1 but pushes the radial direction to order r−3 . The quadratic
condition-number law is not a fitted exponent; it follows from Theorem 4.1.

                                                                                                  9
```

---

## Page 10

```text
The cancellation of every p2 contribution in the fourth-order ratio coefficient is worth
noting: the full all-power family has the correction −pr4 /8, followed by the first nonlinear-in-p
term p(p + 1)r6 /16.


7    Finite-sample resolution of the weighted Gram matrix
The population eigenvalues alone do not say when a sample resolves the radial mode. We now
answer that question for the fixed-oracle matrix
                                        n
                     b h,n (r, u) = 1                                         iid
                                        X
                     H                        h(ru> Xi )Xi Xi> ,         Xi ∼ N (0, Id ).
                                    n
                                        i=1

Prior self-concordant analyses already give bilateral constant-factor empirical-Hessian sand-
wiches, including a uniform result for Gaussian logistic regression [16, Eq. (92)]; fixed-point
standardized-Hessian concentration is also available under generic matrix-Bernstein conditions
[17]. Chardon, Lerasle and Mourtada prove a uniform one-sided lower bound for the empirical
Bernoulli Hessian (p = 1) under the sufficient condition n & r(d + t) [15, Theorem 6]. We do
not claim the first bilateral concentration or the first finite-sample lower bound. The result
below instead gives tunable two-sided relative error for a fixed teacher, applies to a general
bounded profile and hence every p > 0, separates radial, tangential and cross errors, and
returns an eigenspace angle.
    Put m = d − 1, Z = u> X, Y = X − Zu, and W = h(rZ). Define

                    α = EW,       β = E[W Z 2 ],          γj = E[W 2 Z 2j ]    (j = 0, 1, 2),

and the envelopes

                    H = khk∞ ,          K1 = sup z 2 h(rz)2 ,          K2 = sup z 2 h(rz).
                                                 z                                  z

Theorem 7.1 (explicit relative empirical spectrum). Assume 0 ≤ h ≤ H, K1 , K2 < ∞, and
α, β > 0. Let 0 < δ < 1 and set

                                 t = log(12/δ),             u0 = m log 9 + t,
                           p             H 2t                                 p            K1 t
             S0+ = nγ0 +    2nH 2 γ0 t +      ,               S1+ = nγ1 +      2nK1 γ1 t +      ,
                                          3                                                 3
                              r
                                  2γ0 t Ht 4
                                                          q
                                                            S0+ u0 + Hu0 ,                          (31)
                                                                         
                       eT =            +    +
                                   n     3n   n
                                                                 q
                                                                   S1+ √   √ 
                              r
                                  2γ2 t K2 t
                       eR =            +     ,            qn =          m + 2t .                    (32)
                                   n     3n                        n
Then, with probability at least 1 − δ, in the radial–tangential basis
                                                         
                                                  C   b n
                                        b h,n =
                                        H
                                                  b>
                                                   n cn

satisfies simultaneously

                     kC − αIm kop ≤ eT ,             |cn − β| ≤ eR ,          kbn k2 ≤ qn .         (33)

Consequently, for                                               
                                                         eT eR         qn
                                    εn := max              ,         +√ ,                           (34)
                                                         α β            αβ

                                                         10
```

---

## Page 11

```text
one has the two-sided relative Löwner bound

                          (1 − εn )Hh (r, u)  H
                                               b h,n (r, u)  (1 + εn )Hh (r, u).                           (35)

If G := α − β − eT − eR > 0, the empirical matrix has a unique eigenvalue βb below the tangential
block spectrum, and its unit eigenvector ub obeys

                                                 qn                                   qn2
                                       u, u) ≤
                                 tan ∠(b            ,            |βb − β| ≤ eR +          .                 (36)
                                                 G                                    G
Every other ordered eigenvalue differs from α by at most max{eT , eR } + qn .

Proof. Write
                    1X                                  1X                                    1X
               C=      Wi Yi Yi> ,              bn =       W i Z i Yi ,             cn =         Wi Zi2 .
                    n                                   n                                     n
                          i                                  i                                    i

Scalar Bernstein controls W − α and, one-sidedly,                     i Wi ≤ S0 . Conditional on the weights,
                                                                          2   +
                                                                   P
for a fixed unit v,
                                                                                            iid
                      X                               X
                 v>           Wi (Yi Yi> − Im )v =          Wi (G2i − 1),            Gi ∼ N (0, 1).
                      i                                 i

The exact Gaussian moment-generating function gives

                                 X                        s X
                                       Wi (G2i − 1)    ≤ 2 u0 Wi2 + 2Hu0
                                   i                                  i


outside conditional probability 2e−u0 . A 1/4-net of S m−1 has at most 9m points and kAkop ≤
2 maxv in net |v > Av|, proving the first bound in (33). Bernstein applied to Wi Zi2 ∈ [0, K2 ]
proves the radial bound.
    Conditionally on the Zi ,               P        2 2   
                                                 i Wi Zi
                                   bn ∼ N 0,              Im .
                                                   n2
A second one-sided Bernstein bound gives i Wi2 Zi2 ≤ S1+ , and the Gaussian norm tail proves
                                            P
the cross bound. The listed failures total less than 9e−t < δ.
    Conjugating H   b h,n − Hh by H −1/2 = diag(α−1/2 Im , β −1/2 ) shows that its norm is at
                                     h
most (34); this is equivalent to (35). If G > 0, then cn < λmin (C). Interlacing leaves one
eigenvalue below C. The eigenvector equation and the Schur complement give respectively
      u, u) ≤ qn /G and 0 ≤ cn −βb ≤ qn2 /G. Weyl’s inequality gives the remaining assertion.
tan ∠(b

   For hp = σ 0p , all quantities in Theorem 7.1 are one-dimensional and computable. The
elementary bound σ 0 (s) ≤ e−|s| gives, for every p > 0,

                                                            e−2                  4e−2
                                  H = 4−p ,      K1 ≤             ,       K2 ≤          ,                   (37)
                                                            p2 r2                p2 r 2

and, with ϕ(0) = (2π)−1/2 ,

                                       ϕ(0)    ϕ(0)               3ϕ(0)
                               γ0 ≤         ,    γ1 ≤
                                                  3 3
                                                      ,    γ2 ≤ 5 5 .                          (38)
                                        pr     2p r               2p r

Indeed, after s = rZ, use hp (s)2 ≤ e−2p|s| and R |s|j e−2p|s| ds = 2j!/(2p)j+1 for j = 0, 2, 4.
                                                R



                                                            11
```

---

## Page 12

```text
Corollary 7.2 (effective sample size for every logistic power). Let
                                                          
                                2           3m2 (p) m4 (p)
                              Rp = max             ,         .
                                             m0 (p) m2 (p)

For r ≥ Rp , 0 < ε ≤ 1/2 and 0 < δ < 1, the explicit condition εn ≤ ε in (34), with (37)–(38)
substituted, guarantees (35). In particular, for each fixed p > 0 there are finite computable
constants Cp , Cp0 such that
                                             r [d + log(12/δ)]
                                     n ≥ Cp                                               (39)
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

                     ϕ(0)m0 (p)            ϕ(0)m2 (p)                 ϕ(0)m0 (p)
                α≥              ,     β≥              ,      α−β ≥               .
                         2r                   2r3                         2r
Insert these andp(37)–(38) in (31)–(34). Each relative block term is bounded by a p-dependent
constant times r[d + log(12/δ)]/n+r[d+log(12/δ)]/n. The cross term has the same first order.
Increasing a finite constant Cp makes their sum at most ε and also makes eT + eR ≤ (α − β)/2.
Thus G ≥ (α − β)/2 ≥ ϕ(0)m0 (p)/(4r), and substitution of qn into (36) gives the displayed
bound with a finite computable Cp0 .

   The sufficient product scaling in (39) is not claimed minimax-sharp. Two necessary
obstructions can nevertheless be proved. First, positive weights imply rank(H       b p,n ) ≤ n, so
n ≥ d is necessary for a positive smallest eigenvalue. Second, choose any finite ap > 0 satisfying
                                   Z
                                                          m2 (p)
                                           s2 hp (s) ds ≤        .
                                    |s|>ap                 16

For r ≥ max{    m4 (p)/m2 (p), 4ϕ(0)ap }, the empty-transition-slab event and Markov’s inequal-
               p

ity give                                                         
                                b p,n ) < βp (r) ≥ 1 exp − 4ϕ(0)ap n .
                       Pr λmin (H                                                             (40)
                                            2      2          r
Hence failure probability at most δ < 1/2 requires
                                              r       1
                                      n≥           log .                                      (41)
                                           4ϕ(0)ap    2δ

To verify (40), condition on no |Zi | ≤ ap /r. This event has probability at least the exponential
shown; the conditional mean radial entry is at most βp /4, so with conditional probability at
least 1/2 that entry, and therefore the smallest eigenvalue, is below βp /2.
    The lower bounds (41) and n ≥ d do not combine into a matching Ω(rd) theorem. Establish-
ing that product lower bound requires a smallest-singular-value result for the heteroskedastic
weighted Gaussian design and remains open. Nor is (41) a minimax parameter-estimation
theorem: the teacher, profile and input law are fixed in this oracle Gram problem.

                                                12
```

---

## Page 13

```text
8     What the law costs
8.1   Stationary fixed-step gradient descent
For either logistic profile, assume d ≥ 2 and that one constant scalar step size η is reused at
every iteration. At the teacher, the Jacobian of one gradient-descent step is I − ηHh . Its radial
eigenvalue is 1 − ηβ and its tangential eigenvalue is 1 − ηα. The best scalar step for this local
quadratic model is
                                     2              α−β      κ−1
                              η? =       ,    ρ? =         =       .                          (42)
                                   α+β              α+β      κ+1
Consequently − log ρ? ∼ 2/κ. For worst-case local error with components allowed in both
eigenspaces, the e-folding iteration count Te := (− log ρ? )−1 therefore has the exact leading
scaling
                                         3                    3
                            Te,sq ∼            r2 ,  Te,B ∼ 2 r2                          (43)
                                    2(π 2 − 6)               2π
for the optimally tuned stationary scalar-step linearization. This is not a global iteration
bound or an algorithm-independent obstruction: away from the teacher the Hessian contains
residual terms, and nonstationary polynomial methods can exploit the two-point spectrum.
Indeed, the scalar schedule η1 = 1/α, η2 = 1/β makes (I − η2 H)(I − η1 H) = 0 in this exact
local quadratic. Natural-gradient or matrix-preconditioned updates can also remove the local
condition number by acting differently on the two eigenspaces.

8.2   Estimation
For n independent Gaussian-output observations with known variance τ 2 , the Fisher informa-
tion is nHh2 /τ 2 . The Cramér–Rao inequality gives, along any unit tangential vector v ⊥ u
and the radial vector u,
                                        τ2                            τ2
                        Var(v > w)
                                b ≥           ,        Var(u> w)
                                                              b ≥           .                (44)
                                      nα2 (r)                       nβ2 (r)
The ratio of the displayed radial lower bound to the tangential lower bound is κ2 (r). Hence
tangential variance is bounded below at order r/n, while radial variance is bounded below
at order r3 /n. The analogous Bernoulli bounds replace h2 by h1 . The same quadratic ratio
therefore appears in these coordinatewise information lower bounds and in stationary fixed-step
descent, although the latter can be removed by a nonstationary schedule.


9     Bias and universality
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
                                                                .                       (45)
                               E[Zh(rZ + b)]     E[h(rZ + b)]
The centered theorem is therefore not an artifact of omitting the bias; it is the diagonal point
of a fully explicit two-coordinate extension.

                                                  13
```

---

## Page 14

```text
The exponent two is broader than the logistic curve. Theorem 4.1 shows that any localized
sensitivity profile with finite positive m0 and m2 has the same r2 anisotropy, with only the
constant m0 /m2 depending on the activation and observation model. Profiles with heavy
sensitivity tails or vanishing second moment fall outside this universality class and can have
different laws.


10    Relation to prior work
Table 1 states the claim boundary before the detailed discussion.

  Prior result                   Result here                     Exact difference
  Fixed-order                    closed logistic determinant     explicit specialization and
  Löwner/Schwarzian              and certified 2 × 2 witness     certificate; not a new criterion or
  criterion and serial closure                                   closure law
  [3, 4]
  One-unit Gaussian Fisher       spherical local bridge and      new coefficient cross-identification
  split for φ02 [20]             Gaussian all-p laws             and extensions; not a new one-unit
                                                                 decomposition
  Bernoulli exponents and        explicit pointwise              tunable precision, all powers, angle
  finite-sample logistic         block-resolved relative Gram    and slab obstruction; not the first
  Hessian bounds                 bound for every p > 0           bilateral or one-sided Hessian
  [13, 16, 15, 17]                                               bound
  Generalized-logistic           Gamma/polygamma                 transform is classical; the unified
  transforms and cumulants       moments inside neuronal         anisotropy, endpoint laws and
  [22, 21]                       anisotropy                      monotonicity are the contribution
  Lam’s historical v2            Löwner–anisotropy coefficient   different objects and coefficient; no
  Fisher–Schwarzian              identity                        claim to the first general
  construction [23]                                              Fisher–Schwarzian connection

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
explicit certified witness, or the coefficient identity (22) linking the Löwner defect to Gaussian
radial–tangential anisotropy. This is a bounded novelty statement, not a claim that no earlier
source can exist.
    Learning one neuron is already a nontrivial optimization problem. Yehudai and Shamir
study when gradient methods learn a single neuron under broad activations and input dis-
tributions, including positive and negative results [7]. Diakonikolas et al. treat monotone
neurons with adversarial label noise and obtain polynomial learners for logistic activations
under log-concave inputs [8]. Wu extends learnability results to nonmonotone activations [9],
and Vardi et al. show that adding a bias qualitatively changes the ReLU landscape [10]. Recent
single-index work analyzes SGD under anisotropic Gaussian inputs [11]. Under Gaussian


                                                  14
```

---

## Page 15

```text
logistic regression, Hsu and Mazumdar study the signal-dependent difficulty of direction and
temperature estimation [12]. Chen and Mazumdar identify the Bernoulli radial and tangential
Hessian functions, prove their r−3 and r−1 orders and show tangential curvature exceeds radial
                p nonzero signal [13]; they subsequently prove a minimax norm-estimation
curvature for every
rate of order r3 /n [14]. Ostrovskii and Bach prove a uniform bilateral constant-factor
empirical-Hessian sandwich for Gaussian logistic regression [16, Eq. (92)], while Fisher et
al. give a generic fixed-point standardized-Hessian concentration framework [17]. Chardon,
Lerasle and Mourtada prove, for p = 1, a uniform one-sided empirical Hessian lower bound
under the sufficient condition n & r(d + t) [15, Theorem 6]. We therefore do not claim the
Bernoulli exponents, the p = 1 ordering, the effective transition-slab scale, the first bilateral
Hessian concentration, or the first finite-sample lower bound. Our empirical contribution is
the explicit pointwise (1 ± ε) approximation (35) for all p > 0, with separate block errors,
saturation scaling, radial-eigenspace angle and slab obstruction.
    Fisher geometry and natural gradient are classical [18]. Karakida et al. study broad Fisher
spectral statistics for random deep networks [19]; Amari, Karakida and Oizumi also give
the direct one-unit Gaussian φ02 decomposition and bias coupling used here [20]. Our radial
contribution is therefore not the two-eigenspace reduction. It is the profile-generic moment
theorem, nonasymptotic brackets, closed all-power logistic constants, strict global monotonicity,
and their connection through (22) to the Löwner order defect. The generalized-logistic Gamma
transform and its polygamma cumulants in Lemma 6.1 are classical [22, 21]; the claim is
their neural-geometric use, ratio monotonicity and endpoint package, not discovery of the
distributional identity. Lam’s v2 preprint connected Schwarzian curvature with Fisher–Rao
geometry on manifolds of densities [23]. The current v3 explicitly corrects and supersedes v1–v2
and removes that architecture [24]. Neither version contains the one-neuron radial–tangential
coefficient or its equality with the two-point Löwner defect. We cite v2 only as a dated
historical adjacency; its Lp parameter is unrelated to the sensitivity exponent in hp = σ 0p .


11    Reproducibility and hostile checks
The supplied script repro/verify_saturation_law.py performs the following independent
checks:
 1. it spot-checks (3) at separated scales and constructs Proposition 2.2 with 256-bit directed
    Arb balls;

 2. it checks the spherical fourth-moment coefficient for Gaussian and fixed-radius spherical
    inputs;

 3. it compares numerical quadrature of m0 , m2 , m4 with the Gamma/polygamma formula
    for several noninteger and integer p;

 4. it checks the small-r jet through r6 and the refined large-r expansion;

 5. it evaluates α, β directly over a logarithmic radius grid and checks positivity and grid
    monotonicity for p = 1, 2;

 6. it checks (24)–(26) at declared finite scales;

 7. for three declared fixed random seeds it evaluates the empirical radial, tangential and
    cross blocks and verifies that those realized errors lie inside (33);

 8. it checks both sides of (19)–(20) at declared finite radii; and

 9. it regenerates Figure 1 and a JSON certificate with all evaluated values.

                                               15
```

---

## Page 16

```text
The numerical monotonicity and finite-radius checks are performed on declared grids; the
universal statements are proved analytically above. The replay uses Python, python-flint,
NumPy, SciPy, and Matplotlib. It is diagnostic rather than a substitute for the analytic
proofs, which reduce to the Löwner determinant identity, the Schwarzian chain rule, Gaussian
orthogonal decomposition, Bernstein/net bounds, an elementary exponential bound, and closed
Fourier moments. The stable record, versioned source archives, audit reports and manifests
are public at https://arr-research.github.io/papers/ARR-2026-53CTRKDSP685PT51/.


12    Limitations and next theorem
The Löwner theorem concerns spectral matrix functions, not entrywise vector activations; it
does not say that a standard feedforward neuron reverses coordinatewise order. Full global
saturation and empirical results assume Gaussian input. The spherical theorem controls only
the local quadratic jet: covariance isotropy without orthogonal invariance is insufficient, and
qX alone determines neither global monotonicity nor the large-r constant. Elliptical Gaussians
can be whitened, but radial/tangential directions then use the covariance metric.
    The empirical theorem is pointwise for a fixed teacher and raw weighted Gram matrix. It
is not a uniform landscape theorem, an estimator guarantee using labels, or a minimax lower
bound. Its explicit net constants are conservative. The necessary Ω(r log(1/δ)) slab factor and
n ≥ d rank obstruction do not prove a matching Ω(rd) product lower bound. That requires a
smallest-singular-value theorem for a heteroskedastic logistic-weighted Gaussian design and is
the strongest proof-complete successor problem. The optimization result remains local, and
the Cramér–Rao statement concerns regular unbiased estimation.


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
 [7] G. Yehudai and O. Shamir, Learning a Single Neuron with Gradient Methods, Proceedings of
     Machine Learning Research 125 (2020), 3756–3786. https://proceedings.mlr.press/v125/
     yehudai20a.html




                                                  16
```

---

## Page 17

```text
[8] I. Diakonikolas, V. Kontonis, C. Tzamos and N. Zarifis, Learning a Single Neuron with Adversarial
     Label Noise via Gradient Descent, Proceedings of Machine Learning Research 178 (2022), 4313–4361.
     https://proceedings.mlr.press/v178/diakonikolas22c.html
 [9] L. Wu, Learning a Single Neuron for Non-monotonic Activation Functions, Proceedings of Machine
     Learning Research 151 (2022), 4178–4197. https://proceedings.mlr.press/v151/wu22c.html
[10] G. Vardi, G. Yehudai and O. Shamir, Learning a Single Neuron with Bias Using Gradient
     Descent, Advances in Neural Information Processing Systems 34 (2021), 28690–28700. https:
     //arxiv.org/abs/2106.01101
[11] G. Braun, M. H. Quang and M. Imaizumi, Learning a Single Index Model from Anisotropic Data
     with Vanilla Stochastic Gradient Descent, Proceedings of Machine Learning Research 258 (2025),
     1216–1224. https://proceedings.mlr.press/v258/braun25a.html
[12] D. Hsu and A. Mazumdar, On the Sample Complexity of Parameter Estimation in Logistic
     Regression with Normal Design, Proceedings of Machine Learning Research 247 (2024), 2418–2437.
     https://proceedings.mlr.press/v247/hsu24a.html
[13] J. Chen and A. Mazumdar, Finite-Sample Performance of Gradient Descent in Logistic Regression
     with Gaussian Design, arXiv:2606.21683 (2026). https://arxiv.org/abs/2606.21683
[14] J. Chen and A. Mazumdar, Minimax Optimal Estimator and Improved Error Rate for the MLE
     in Logistic Regression with Gaussian Design, arXiv:2608.17260 (2026). https://arxiv.org/abs/
     2608.17260
[15] H. Chardon, M. Lerasle and J. Mourtada, Finite-sample performance of the maximum likelihood
     estimator in logistic regression, arXiv:2411.02137v3 (first posted 2024; v3 2026). https://arxiv.
     org/abs/2411.02137v3
[16] D. M. Ostrovskii and F. Bach, Finite-sample analysis of M-estimators using self-concordance,
     Electronic Journal of Statistics 15(1) (2021), 326–391. https://doi.org/10.1214/20-EJS1780
[17] J. Fisher, L. Liu, K. Pillutla, Y. Choi and Z. Harchaoui, Influence Diagnostics under Self-
     concordance, Proceedings of Machine Learning Research 206 (2023), 10028–10076. https://
     proceedings.mlr.press/v206/fisher23a.html
[18] S.-i. Amari, Natural Gradient Works Efficiently in Learning, Neural Computation 10 (1998),
     251–276. https://doi.org/10.1162/089976698300017746
[19] R. Karakida, S. Akaho and S.-i. Amari, Universal Statistics of Fisher Information in Deep Neural
     Networks: Mean Field Approach, Proceedings of Machine Learning Research 89 (2019), 1032–1041.
     https://proceedings.mlr.press/v89/karakida19a.html
[20] S.-i. Amari, R. Karakida and M. Oizumi, Fisher Information and Natural Gradient Learning
     in Random Deep Networks, Proceedings of Machine Learning Research 89 (2019), 694–702.
     https://proceedings.mlr.press/v89/amari19a.html
[21] C. J. Lee, A. Zito, H. Sang and D. B. Dunson, Logistic-beta processes for dependent random
     probabilities with beta marginals, Bayesian Analysis 20(4) (2025), 1345–1369. https://doi.org/
     10.1214/25-BA1541
[22] M. O. Ojo and A. K. Olapade, On a Six-Parameter Generalized Logistic Distribution,
     Kragujevac Journal of Mathematics 26 (2004), 31–38. https://imi.pmf.kg.ac.rs/kjm/pub/
     12616736649184_5.pdf
[23] H. P. G. Lam, Real Bers embedding on the line: Fisher–Rao linearization, Schwarzian curvature,
     and scattering coordinates, arXiv:2602.07373v2 (2026). https://arxiv.org/abs/2602.07373v2
[24] H. P. G. Lam, Zero-energy scattering and the real Bers image on the line, arXiv:2602.07373v3
     (2026), correcting and superseding v1–v2. https://arxiv.org/abs/2602.07373v3




                                                 17
```
