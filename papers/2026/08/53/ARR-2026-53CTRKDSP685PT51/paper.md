# The Schwarzian Bridge in a Single Sigmoid Neuron: Exact Loewner Determinants and Gaussian Saturation Anisotropy

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
The Schwarzian Bridge in a Single Sigmoid Neuron
     Exact Löwner Determinants and Gaussian Saturation Anisotropy

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
     for a sensitivity hp = (g 0 )p ,

                                  Ehp (rZ)
                                               = 1 − p Sg(0)r2 + O(r4 ),
                                E[Z 2 hp (rZ)]

     whereas the adjacent-point Löwner determinant is g 0 (0)2 Sg(0)δ 2 /6 + O(δ 3 ). Negative
     Schwarzian therefore simultaneously gives local noncommutative order failure and positive
     initial radial–tangential anisotropy.
         For isotropic Gaussian inputs in dimension d ≥ 2, population curvature at a teacher
     of norm r has one radial eigenvalue and d − 1 equal tangential eigenvalues. For any
     nonnegative sensitivity profile h with finite defining expectations, these eigenvalues are
     exactly
                     αh (r) = Eh(rZ),      βh (r) = E[Z 2 h(rZ)],  Z ∼ N (0, 1),
     and, if its zeroth and second Lebesgue moments are finite and positive,

                                          ϕ(0)m0                    ϕ(0)m2
                               αh (r) ∼          ,       βh (r) ∼          .
                                             r                        r3
     Thus saturation suppresses magnitude information by two additional powers: the radial–
     tangential ratio obeys αh (r)/βh (r) ∼ (m0 /m2 )r2 . For the logistic sigmoid this ratio is the
     spectral condition number, and we evaluate its constants in closed form. Squared-output
     loss gives κ(r) ∼ 3r2 /(π 2 − 6), while Bernoulli likelihood gives κ(r) ∼ 3r2 /π 2 . Prior work
     contains the Bernoulli exponents and the one-unit squared-output spectral reduction; our
     additions are the Schwarzian bridge, profile-generic brackets, exact logistic constants, and
     strict ratio monotonicity. In both cases the anisotropy is strictly increasing from one. We
     prove explicit finite-r brackets, translate the law into optimally tuned stationary fixed-step
     local gradient-descent rates and Cramér–Rao lower bounds, and supply a deterministic
     replay. The bridge identifies a shared local source for two effects already present in one
     neuron, while the large-r theorem quantifies the later saturation regime.

Keywords. single neuron; sigmoid; matrix monotonicity; Löwner order; Schwarzian deriva-
tive; Fisher information; Gaussian design.


                                                     1
```

---

## Page 2

```text
1     Question, result, and claim boundary
The scalar logistic curve is
                                        1                     1
                            σ(s) =           ,    σ 0 (s) =     sech2 (s/2).
                                     1 + e−s                  4
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

    3. a Schwarzian bridge equating the local order defect with the leading radial–tangential
       anisotropy of the Gaussian sensitivity matrix at a centered inflection;

    4. a profile-generic two-eigenvalue refinement under Gaussian design, with source-level
       finite-r brackets, closed logistic constants and strict ratio monotonicity for both h = σ 0
       and h = σ 02 ; and

    5. exact local consequences for stationary fixed-step optimization and estimation, plus a
       one-command replay of the identities, interval witness, inequalities, and figure.
    The matrix-order theorem concerns spectral functional calculus σ(A), not entrywise activa-
tion of a vector. The radial theorem is not a claim about deep networks, global optimization,
implicit bias, or arbitrary inputs. The two questions meet at a precise boundary: scalar mono-
tonicity controls neither noncommuting PSD perturbations nor the conditioning of parameter
directions.


2      A sigmoid is not an order-preserving operator
For Hermitian matrices, A  B means that B − A is positive semidefinite. A scalar function
f is matrix-monotone of order two on an interval J if f (A)  f (B) for every pair of 2 × 2
Hermitian matrices with spectra in J and A  B, where f (A) is defined by spectral functional
calculus. If A and B commute, scalar monotonicity is sufficient because they are simultaneously
diagonalizable. The question is what happens without commutativity.
    For distinct x, y ∈ J, define the two-point Löwner matrix
                                                       f (x) − f (y)
                                                                    
                                             f 0 (x)
                           Lf (x, y) =                    x−y                              (1)
                                                                     .
                                                                    
                                         f (x) − f (y)      0
                                                           f (y)
                                             x−y
The fixed-order Löwner criterion says that matrix monotonicity of order two requires Lf (x, y) 
0 for every pair [1, 2]. The equivalent local criterion Sf ≥ 0 for increasing smooth functions

                                                 2
```

---

## Page 3

```text
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
                                sα,b (x) =                  ,            α > 0.
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
                       spec(B) ⊂ [−0.4901000, −0.4900999] ∪ [0.5100999, 0.5101000],             (5)
           spec(σ(B) − σ(A)) ⊂ [−9.9150, −9.9147] 10−5 ∪ [0.0047990, 0.0047992],                (6)
            det(σ(B) − σ(A)) ∈ [−4.7583, −4.7581] 10            −7
                                                                     .                          (7)
Proof. B − A has eigenvalues 0 and 1/50. If a = 1/2, ε = 1/100, and d = (a2 + ε2 )1/2 , then B
has eigenvalues λ± = ε ± d and
                                          σ(λ+ ) + σ(λ− )        σ(λ+ ) − σ(λ− )
           σ(B) = mI + n(B − εI),         m=              , n=                   .
                                                 2                     2d
Substitution reduces the three enclosures to scalar exponential and square-root balls. The
replay evaluates them with directed Arb rounding; the negative eigenvalue in (6) proves the
claim.

                                                   3
```

---

## Page 4

```text
The witness is illustrative, while Theorem 2.1 is the proof for every interval. The derivative
form also explains why an indefinite Löwner matrix produces witnesses: for diagonal A =
diag(x, y), the Fréchet derivative in the all-ones PSD direction is precisely the Schur product
with Lf (x, y).

2.1   Serial depth does not repair the order
For a C 3 function with nonzero derivative, its Schwarzian is
                                                                2
                                          f 000 3        f 00
                                                     
                                      Sf = 0 −                       .                        (8)
                                           f    2        f0

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


3     Two models, one sensitivity matrix
Write r = kw? k and u = w? /r when r > 0. We use two standard observation models.

Squared-output regression.        For the realizable population loss
                                      1 
                                                                                            (12)
                                                           2
                             Lsq (w) = E σ(w> X) − σ(w?> X) ,
                                      2
the residual vanishes at w? , so its Hessian is the Gauss–Newton matrix

                                 Hsq (w? ) = E σ 0 (w?> X)2 XX > .                          (13)
                                                               


The same matrix, divided by a known output-noise variance τ 2 , is the Fisher information of
Y = σ(w?> X) + ε, ε ∼ N (0, τ 2 ).



                                                 4
```

---

## Page 5

```text
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
sition for h = φ02 , including the radial–tangential split and the bias block [18]. We do not claim
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
                              Hh (r, u) = αh (r)(I − uu> ) + βh (r)uu> ,                      (16)
where
                 αh (r) = Eh(rZ),         βh (r) = E[Z 2 h(rZ)],     Z ∼ N (0, 1).            (17)
If m0 , m2 < ∞ and are positive, then
                        ϕ(0)m0                   ϕ(0)m2                  αh (r)   m0 2
             αh (r) ∼          ,      βh (r) ∼          ,    κh (r) :=          ∼    r .      (18)
                           r                       r3                    βh (r)   m2
If m0 , m2 , m4 < ∞, the following nonasymptotic brackets hold for every r > 0:
                             ϕ(0)       m2             ϕ(0)m0
                                    m0 − 2 ≤ αh (r) ≤            ,                            (19)
                               r         2r                  r
                             ϕ(0)       m4             ϕ(0)m2
                                3
                                    m2 −    2
                                              ≤ βh (r) ≤         .                            (20)
                              r          2r                 r3
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

                                                   5
```

---

## Page 6

```text
5    The Schwarzian bridge
The matrix-order and saturation calculations meet exactly at an inflection point. The next
statement applies beyond the logistic curve and turns that meeting into a coefficient identity.
Theorem 5.1 (local order–anisotropy bridge). Let g ∈ C 5 (R) satisfy g 0 > 0 and g 00 (0) = 0.
For p > 0, suppose hp = (g 0 )p is C 4 with bounded fourth derivative, and define
                                                                                       αp (r)
                αp (r) = Ehp (rZ),         βp (r) = E[Z 2 hp (rZ)],         κp (r) =          .
                                                                                       βp (r)
Then
                          κp (r) − 1                 6p      det Lg (0, δ)
                      lim       2
                                     = −p Sg(0) = − 0 2 lim                .                           (22)
                      r↓0     r                    g (0) δ→0      δ2
In particular, Sg(0) < 0 makes Lg (0, δ) indefinite for every sufficiently small δ 6= 0 and makes
κp (r) > 1 for all sufficiently small r > 0.
Proof. Taylor expansion under the Gaussian expectation, with the bounded fourth derivative
controlling the remainder, gives
                               h00p (0) 2                                       3h00p (0) 2
           αp (r) = hp (0) +           r + O(r4 ),         βp (r) = hp (0) +             r + O(r4 ).
                                   2                                              2
Consequently
                                                     h00p (0) 2
                                      κp (r) = 1 −           r + O(r4 ).
                                                     hp (0)
Because log hp = p log g 0 and g 00 (0) = 0,
                                       h00p (0)   g 000 (0)
                                                =p 0        = p Sg(0).
                                       hp (0)     g (0)
Finally, the adjacent-point expansion (11), applied to g at zero, yields the second equality in
(22).

    For the standard logistic sigmoid, Sσ = −1/2. Theorem 5.1 therefore predicts the exact
initial coefficients 1/2 for h1 = σ 0 and 1 for h2 = σ 02 , recovered globally below in (25)–(26).
This equality of coefficients is the promised bridge: it does not merely place two sigmoid facts
side by side, but identifies their common differential invariant.
    For a general h, κh = αh /βh in (18) is an anisotropy ratio; it is the spectral condition
number only after the eigenvalue ordering is known. The two powers are geometric. At large
r, only a score slab of width O(r−1 ) remains unsaturated, producing α  r−1 . A radial
perturbation carries an additional factor Z 2 = O(r−2 ) inside that slab, producing β  r−3 .
Both modes are supported by the near-boundary slab; the radial mode is weaker because it
carries the additional Z 2 factor.


6    The logistic constants and the exact saturation profile
For p ∈ {1, 2} set hp (t) = σ 0 (t)p . The case p = 1 is Bernoulli Fisher curvature and p = 2 is
squared-output curvature.
Lemma 6.1 (closed sensitivity moments). The first three even moments are

                            profile      m0           m2                   m4
                        h1 = σ 0          1         π 2 /3              7π 4 /15
                        h2 = σ 02        1/6    (π 2 − 6)/18      7π 4 /90 − 2π 2 /3

                                                      6
```

---

## Page 7

```text
Proof. For h1 , these are the normalization, variance, and fourth central moment of the standard
logistic density. For h2 (t) = 16
                                1
                                  sech4 (t/2), its Fourier transform is
                                   Z
                                                     1
                          h2 (k) =
                          b           eikt h2 (t)dt = Γ(2 + ik)Γ(2 − ik).                    (23)
                                    R                6

Differentiating at zero and using ψ1 (2) = π 2 /6 − 1 and ψ3 (2) = π 4 /15 − 6 gives the displayed
values.

Theorem 6.2 (strict logistic anisotropy). For p = 1 and p = 2, κp (0) = 1, κp (r) > 1 for
r > 0, and κp is strictly increasing on (0, ∞). Moreover,

                                                                                              3 2                                        3
                                                                                   κ1 (r) ∼      r ,          κ2 (r) ∼                            r2 .                                  (24)
                                                                                              π2                                      π2 − 6

Proof. Normalize the density qp,r (z) ∝ hp (rz)ϕ(z). Then βp (r)/αp (r) = Eqp,r Z 2 . If r2 > r1 ,
the derivative on z > 0 of the log likelihood ratio is

                                                             d      hp (r2 z)                                      
                                                                log           = −p r2 tanh(r2 z/2) − r1 tanh(r1 z/2) < 0.
                                                             dz     hp (r1 z)

Thus the distribution of |Z| under qp,r decreases strictly in monotone-likelihood-ratio order as
r increases, and its strictly increasing statistic Z 2 has decreasing expectation. Hence αp /βp
increases strictly. At r = 0 isotropy gives one, and Lemma 6.1 inserted into Theorem 4.1 gives
(24).

  Figure 1 shows the entire saturation profile. The solid and dashed curves are direct
Gaussian integrals; the dotted curves are the asymptotic constants in (24).

                                             One tangential law, one radial bottleneck                                                 Profile-generic large-r anisotropy: κ ≍ r2
                                                                                                                                103
                                                                                                                                      square loss: h = σ 2
                                                                                                                                                         0




                                     10−1                                                                                             Bernoulli Fisher: h = σ
curvature / information eigenvalue




                                                                                                                                                                0




                                     10−2                                                                                       102
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




                                                   10−1                  100               101                                             10−1                 100               101
                                                            teacher weight norm r = ‖w ⋆ ‖                                                         teacher weight norm r = ‖w ⋆ ‖


Figure 1: Exact curvature/information eigenvalues and their ratio. Saturation leaves d − 1
tangential directions at order r−1 but pushes the radial direction to order r−3 . The quadratic
condition-number law is not a fitted exponent; it follows from Theorem 4.1.

                                      At the nonsaturated endpoint the expansions are also explicit:

                                                                                     κ1 (r) = 1 + 12 r2 − 18 r4 + O(r6 ),                                                               (25)
                                                                                     κ2 (r) = 1 + r    2
                                                                                                           − 14 r4 + O(r6 ).                                                            (26)

They follow by expanding sech2 (rZ/2) and sech4 (rZ/2) and using Gaussian moments.


                                                                                                           7
```

---

## Page 8

```text
7     What the law costs
7.1   Stationary fixed-step gradient descent
For either logistic profile, assume d ≥ 2 and that one constant scalar step size η is reused at
every iteration. At the teacher, the Jacobian of one gradient-descent step is I − ηHh . Its radial
eigenvalue is 1 − ηβ and its tangential eigenvalue is 1 − ηα. The best scalar step for this local
quadratic model is
                                     2              α−β      κ−1
                              η? =       ,    ρ? =         =       .                          (27)
                                   α+β              α+β      κ+1
Consequently − log ρ? ∼ 2/κ. For worst-case local error with components allowed in both
eigenspaces, the e-folding iteration count Te := (− log ρ? )−1 therefore has the exact leading
scaling
                                         3                    3
                            Te,sq ∼            r2 ,  Te,B ∼ 2 r2                          (28)
                                    2(π 2 − 6)               2π
for the optimally tuned stationary scalar-step linearization. This is not a global iteration
bound or an algorithm-independent obstruction: away from the teacher the Hessian contains
residual terms, and nonstationary polynomial methods can exploit the two-point spectrum.
Indeed, the scalar schedule η1 = 1/α, η2 = 1/β makes (I − η2 H)(I − η1 H) = 0 in this exact
local quadratic. Natural-gradient or matrix-preconditioned updates can also remove the local
condition number by acting differently on the two eigenspaces.

7.2   Estimation
For n independent Gaussian-output observations with known variance τ 2 , the Fisher informa-
tion is nHh2 /τ 2 . The Cramér–Rao inequality gives, along any unit tangential vector v ⊥ u
and the radial vector u,
                                        τ2                           τ2
                        Var(v > w)
                                b ≥           ,       Var(u> w)
                                                             b ≥           .                 (29)
                                      nα2 (r)                      nβ2 (r)
The ratio of the displayed radial lower bound to the tangential lower bound is κ2 (r). Hence
tangential variance is bounded below at order r/n, while radial variance is bounded below
at order r3 /n. The analogous Bernoulli bounds replace h2 by h1 . The same quadratic ratio
therefore appears in these coordinatewise information lower bounds and in stationary fixed-step
descent, although the latter can be removed by a nonstationary schedule.


8     Bias and universality
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
                                                                .                       (30)
                               E[Zh(rZ + b)]     E[h(rZ + b)]
The centered theorem is therefore not an artifact of omitting the bias; it is the diagonal point
of a fully explicit two-coordinate extension.

                                                  8
```

---

## Page 9

```text
The exponent two is broader than the logistic curve. Theorem 4.1 shows that any localized
sensitivity profile with finite positive m0 and m2 has the same r2 anisotropy, with only the
constant m0 /m2 depending on the activation and observation model. Profiles with heavy
sensitivity tails or vanishing second moment fall outside this universality class and can have
different laws.


9    Relation to prior work
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
logistic regression, Hsu and Mazumdar study the signal-dependent difficulty of direction and
temperature estimation [12]. Chen and Mazumdar identify the Bernoulli radial and tangential
Hessian functions, prove their r−3 and r−1 orders in a finite-sample gradient-descent      analysis
[13], and subsequently prove a minimax norm-estimation rate of order r3 /n [14]. Chardon,
                                                                            p

Lerasle and Mourtada give complementary finite-sample MLE guarantees [15]. The radial
contribution here is therefore an exact refinement, not discovery of those Bernoulli exponents:
it gives profile-generic moment brackets and closed leading constants, including finite-radius
bounds and strict ratio monotonicity for the squared-output profile h = σ 02 .
    Fisher geometry and natural gradient are classical [16]. Karakida et al. study broad
Fisher spectral statistics for random deep networks [17]; Amari, Karakida and Oizumi also
give the direct one-unit Gaussian φ02 decomposition and bias coupling used here [18]. Our
radial contribution is therefore not the two-eigenspace reduction. It is the profile-generic
moment theorem, nonasymptotic brackets, closed logistic constants, strict global monotonicity,
and their connection through (22) to the Löwner order defect. An earlier version of Lam’s
preprint connects Schwarzian curvature with Fisher–Rao geometry on manifolds of densities
[19]; it does not contain the Gaussian one-neuron radial–tangential coefficient or its equality
with the two-point Löwner defect. The priority claimed here is only that coefficient-level
cross-identification, not the first Schwarzian–Fisher connection in general.




                                                9
```

---

## Page 10

```text
10    Reproducibility and hostile checks
The supplied script repro/verify_saturation_law.py performs six independent checks:

 1. it spot-checks (3) at separated scales and constructs Proposition 2.2 with 256-bit directed
    Arb balls;

 2. it checks the two logistic coefficients in the Schwarzian bridge at three small radii;

 3. it compares numerical quadrature of m0 , m2 , m4 with Lemma 6.1;

 4. it evaluates α, β directly over a logarithmic radius grid and checks positivity and monotone
    anisotropy;

 5. it checks both sides of (19)–(20) at declared finite radii; and

 6. it regenerates Figure 1 and a JSON certificate with all evaluated values.

The numerical monotonicity and finite-radius checks are performed on declared grids; the
universal statements are proved analytically above. The replay uses Python, python-flint,
NumPy, SciPy, and Matplotlib. It is diagnostic rather than a substitute for the analytic
proofs, which reduce to the Löwner determinant identity, the Schwarzian chain rule, Gaussian
orthogonal decomposition, an elementary exponential bound, and closed Fourier moments.


11    Limitations and next theorem
The Löwner theorem concerns spectral matrix functions, not entrywise vector activations;
it does not say that a standard feedforward neuron reverses coordinatewise order. The
radial theorem assumes isotropic Gaussian inputs. Elliptical Gaussians can be whitened,
but the Euclidean notions of “radial” and “tangential” then inherit the covariance metric.
Non-Gaussian inputs need not have a two-eigenvalue matrix. The optimization result is local,
and the Cramér–Rao statement concerns regular unbiased estimation. Finite samples can also
hide the transition slab entirely; quantifying the probability that an empirical Gram resolves
the r−3 population mode is a separate concentration problem and is not implied by the Fisher
parameter-estimation scale. A proof-complete successor should specify the estimator, norm,
dimension dependence, and relative-versus-absolute precision, then give matching concentration
and lower bounds rather than infer sample complexity from population curvature alone.


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

                                                 10
```

---

## Page 11

```text
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
     estimator in logistic regression, arXiv:2411.02137 (2024). https://arxiv.org/abs/2411.02137

[16] S.-i. Amari, Natural Gradient Works Efficiently in Learning, Neural Computation 10 (1998),
     251–276. https://doi.org/10.1162/089976698300017746

[17] R. Karakida, S. Akaho and S.-i. Amari, Universal Statistics of Fisher Information in Deep Neural
     Networks: Mean Field Approach, Proceedings of Machine Learning Research 89 (2019), 1032–1041.
     https://proceedings.mlr.press/v89/karakida19a.html

[18] S.-i. Amari, R. Karakida and M. Oizumi, Fisher Information and Natural Gradient Learning
     in Random Deep Networks, Proceedings of Machine Learning Research 89 (2019), 694–702.
     https://proceedings.mlr.press/v89/amari19a.html

[19] H. P. G. Lam, Real Bers embedding on the line: Fisher–Rao linearization, Schwarzian curvature,
     and scattering coordinates, arXiv:2602.07373v2 (2026). https://arxiv.org/abs/2602.07373v2




                                                  11
```
