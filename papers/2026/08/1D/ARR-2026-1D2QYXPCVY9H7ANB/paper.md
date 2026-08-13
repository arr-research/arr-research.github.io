# Exact Rate–Distortion Theory for Complex-Projective Born Prediction: Finite-Dimensional Bingham Frontiers, Thermodynamic Coexistence, and Worst-State Capacity

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
Exact Rate–Distortion Theory for
         Complex-Projective Born Prediction:
        Finite-Dimensional Bingham Frontiers,
     Thermodynamic Coexistence, and Worst-State
                      Capacity
                                            Lluis Eriksson

                                          August 11, 2026


                                               Abstract
          We give a unified exact rate–distortion theory for retaining the complete rank-one Born-
     probability field of a Haar-random pure state in CPd−1 . First, a constrained root count, a
     sharp centered power-sum theorem, and Newton’s expansion prove an all-degree spectral
     result: at fixed traceless Frobenius norm the projective Laplace transform is maximized by a
     one-positive-spike spectrum. This reduces the unrestricted Shannon rate–distortion function
     to an exact scalar complex-Bingham envelope in every dimension, with covariant channels and
     independently flagged coexistence mixtures attaining every distortion. For d ≥ 3 directional
     information turns on discontinuously; the qubit curve and the all-dimensional high-fidelity
     constant are explicit.
          We then solve the full fixed-normalized-distortion limit d → ∞. If y∗ > 2 solves
     y∗ − 1 = 2 log y∗ , then the limiting free energy has a unique coexistence point with α∗ =
     y∗2 /[2(y∗ − 1)] = 2.455407482 . . . and b∗ = 1 − y∗−1 = 0.715331863 . . .. The information cost
     per dimension is                  (             √
                                          − log(1 − 1 − δ), 0 < δ ≤ 1 − b2∗ ,
                             r∞ (δ) =
                                          α∗ (1 − δ),          1 − b2∗ ≤ δ ≤ 1,
     and the finite-dimensional onset multiplier obeys λc,d = α∗ d − [α∗ /(2 log y∗ )] log d + O(1).
        Finally, a pointwise Hilbert projection converts every measurable scalar reporter into
     a physical density-matrix reporter without increasing risk for any pure input. Hence the
     exact worst-state channel capacity equals the Haar rate–distortion function, arbitrary joint
     n-state memories cost exactly nRd (D), and transitivity forces zero rate dispersion with an
     exponential finite-blocklength strong converse. These results concern reusable calibrated
     probability fields, not click-only simulation, state update, or intrinsic randomness.


1    Introduction
Let x ∈ CPd−1 label a pure state ρx = |x⟩⟨x|. A classical representation of x is asked for the
Born probability
                                     px (y) = tr(ρx ρy )                                    (1)
of every rank-one query y. The question is not how many outcomes a single measurement can
generate, but how much classical information is required to retain an entire calibrated probability
field to prescribed accuracy.
    For a Haar source, integrated squared calibration loss reduces exactly to squared Frobenius
reconstruction of a Haar rank-one projector. The resulting complex-projective Shannon rate–
distortion problem has two linked layers. At finite d, the reproduction alphabet is the full


                                                    1
```

---

## Page 2

```text
density-matrix body and must first be reduced globally to a scalar complex-Bingham envelope.
We prove that reduction in all dimensions and show that the first directional phase is discontinuous
for every d ≥ 3. At large d, the active Bingham field is of order d, so small-parameter expansions
do not apply directly [1]. The second layer is the global thermodynamic optimization of that
exact finite-dimensional envelope.
     Large-parameter Kummer asymptotics themselves are classical [2, 3]; our contribution
begins with their global radius optimization, convex conjugate, coexistence law, and finite-size
shift. A uniform Laplace principle produces the limiting free energy with coexistence root
y∗ − 1 = 2 log y∗ . General metric-space and complex-Grassmann results provide bounds or
high-resolution dimensions, while direct complex-projective and Grassmann quantization treats
finite codebooks or metric-ball asymptotics [4, 5, 6, 7]; these works do not evaluate the stochastic
all-distortion radial envelope. The exact real-sphere analysis of Dytso and Cardone is the closest
symmetry-reduction template, but its Bessel/von-Mises–Fisher partition and full-sphere orbit do
not reduce to the Beta/Kummer projective orbit [8].
     The centered-projector map embeds CPd−1 as a proper U (d) orbit of real dimension 2d − 2 in
the (d2 − 1)-dimensional traceless-Hermitian space. Its invariant overlap has law Beta(1, d − 1),
not the symmetric coordinate law of a uniform real sphere. Thus the real-sphere RDF cannot be
imported by setting the sphere dimension to 2d − 2; in particular its limiting convex geometry
has no counterpart of the projective coexistence face.
     We also strengthen the operational scope. We call the resulting worst-input channel-capacity
frontier “source-universal” only in this defined sense; it is not a claim of a single finite-block
universal code for an unknown source distribution. Compound-source, invariant, and minimax
rate–distortion theories have a substantial prior literature [9, 10, 11]. The new content here is
the pointwise arbitrary-reporter projection and exact complex-projective evaluation. The same
argument gives an exact equality for arbitrary joint memories. Finally, the invariant optimal
channel has constant D-tilted information, so general nonasymptotic lossy-source converses
specialize to a zero-dispersion exponential bound [12].
     Our contributions are:

 1. an all-degree one-spike projective partition theorem obtained from an exactly identified
    centered power-sum input, a global constrained root count, parity closure, and Newton’s
    expansion;

 2. the exact unrestricted finite-dimensional RDF, attained by covariant complex-Bingham
    channels and flagged coexistence mixtures;

 3. a discontinuous finite-dimensional onset for every d ≥ 3, together with the qubit specializa-
    tion and exact high-fidelity constant;

 4. an exact thermodynamic free energy, a closed limiting RDF at every fixed normalized
    distortion, and dimension-independent coexistence constants α∗ , b∗ , δ∗ ;

 5. convergence of first contact with the finite-size correction λc,d = α∗ d − c∗ log d + O(1);

 6. a pointwise projection of arbitrary probability reporters onto physical density reports, valid
    for Haar and exact projective 2-design queries;

 7. an exact worst-state channel-capacity equality and its finite-block tensorization; and

 8. zero rate dispersion and an exponential strong converse.

   We do not claim a unique positive branch at every finite d, a matching third-order coding
theorem, or a rank-r Grassmann extension. The last would require a new global matrix-
Bingham/HCIZ spectral extremum.


                                                 2
```

---

## Page 3

```text
This manuscript supersedes the earlier unpublished drafts entitled Exact Information–
Accuracy Frontiers for Born-Probability Prediction: Complex-Bingham Rate–Distortion and a
Discontinuous Directional-Information Onset and Thermodynamic Limit of Complex-Projective
Born-Prediction Rate–Distortion: Exact Coexistence and a Logarithmic Onset Shift. Their
finite-dimensional and thermodynamic results are incorporated here into one self-contained
article; they are not intended as separate overlapping publications.


2    Finite-dimensional starting point
Let X be Haar on CPd−1 and set

                                                 2                  1
                          SX = ρX − I/d,        R0,d = ∥SX ∥2F = 1 − .                           (2)
                                                                    d
For a density-matrix reproduction ρb, use distortion ∥ρX − ρb∥2F . Denote the unrestricted classical
rate–distortion function by

                           Rd (D) = inf I(X; ρb),        E∥ρX − ρb∥2F ≤ D.                       (3)

The infimum ranges over arbitrary standard-Borel stochastic reproductions.
   Let
                                          Z 1
                                                                                      s
        Md (s) = 1 F1 (1; d; s) = (d − 1)     est (1 − t)d−2 dt, Kd (s) = log Md (s) − .         (4)
                                           0                                          d

The complex-Bingham and complex-Watson families and their normalizers are established
directional-statistics objects [13, 14]. Here Kd is the cumulant generating function of Td − 1/d
for Td ∼ Beta(1, d − 1). Define
                                                  2 2
                          Gd,λ (b) = Kd (2λb) − λR0,d b ,       0 ≤ b ≤ 1.                       (5)

It is convenient to denote the optimized Gibbs log partition by
                                             2
                                 cd (λ) = −λR0,d + max Gd,λ (b).                                 (6)
                                                        0≤b≤1

     We use the following exact finite-dimensional theorem as the starting point. Its nontrivial
spectral input is an all-degree Dirichlet partition extremum: among traceless Hermitian matrices
of fixed Frobenius norm, the projective Laplace transform is maximized by one positive eigenvalue
and d − 1 equal negative eigenvalues [15].
                                                                   2 ,
Theorem 2.1 (Finite-dimensional projective envelope). For 0 ≤ D ≤ R0,d
                                                               
                                         2
                         Rd (D) = sup λ(R0,d − D) − max Gd,λ (b) .                               (7)
                                    λ≥0                     0≤b≤1


Every positive active radius is attained by a covariant complex-Bingham channel whose posterior
mean is I/d + b(ρu − I/d). Independent revealed mixtures of active radii attain every nonexposed
distortion.

   Appendix A proves the spectral reduction and the complete Gibbs equality mechanism
needed by Theorem 2.1, including the normalization interface to the external centered power-sum
theorem.




                                                    3
```

---

## Page 4

```text
3    Finite-dimensional phase structure and endpoint regimes
The exact envelope already implies a qualitative transition that is absent in the qubit case. The
active radii are precisely the maximizers of Gd,λ .
Theorem 3.1 (Discontinuous finite-dimensional onset). For every d ≥ 3, there exists
                                                          d(d + 1)
                                     0 < λc,d < λ0,d :=                                         (8)
                                                             2
such that b = 0 and at least one bc,d > 0 are global maximizers of Gd,λc,d . The positive maximizer
cannot approach zero at first contact. Consequently the exact frontier has a nontrivial linear face
                         2 , 0), and optimal directional information turns on discontinuously.
adjacent to (D, R) = (R0,d
Proof. Put W = Td − 1/d. It is centered and lies in an interval of length one. Hoeffding’s lemma
gives Kd (s) ≤ s2 /8 for every real s. Hence, uniformly in b ∈ [0, 1],
                                            
                                    λ
                   Gd,λ (b) ≤ λb2         2                                2
                                                                             
                                      − R0,d   <0       b > 0, 0 < λ < 2R0,d   .              (9)
                                    2
                                                                    2 on a nonzero interval.
Thus b = 0 is initially the unique global maximizer and cd (λ) = −λR0,d
   The variance and third centered moment of Td ∼ Beta(1, d − 1) are
                                    d−1                    2(d − 1)(d − 2)
                           vd =              ,   µ3,d =                      .                 (10)
                                  d2 (d + 1)               d3 (d + 1)(d + 2)
Expansion at b = 0 gives

                                    2                4
                                        + 2λ2 vd b2 + λ3 µ3,d b3 + O(b4 ).
                                                
                      Gd,λ (b) = −λR0,d                                                        (11)
                                                     3
The quadratic coefficient vanishes at λ0,d = d(d + 1)/2. For d ≥ 3, µ3,d > 0, so a sufficiently
small positive b has positive gain at λ0,d , and the same remains true just below it.
    Let λc,d be the infimum of multipliers whose global argmax contains a positive radius.
Estimate (9) makes it positive, and the preceding expansion makes it strictly smaller than λ0,d .
Choose positive active radii bn at λn ↓ λc,d . Since Kd (s)/s2 → vd /2 as s → 0 and λc,d < λ0,d ,
there exist ε, η > 0 such that Gd,λ (b) ≤ −ηb2 for 0 < b ≤ ε and λ near λc,d . Thus every bn is at
least ε. Compactness and continuity yield a limiting bc,d ≥ ε coexisting globally with 0. Finally,
Danskin’s relation (112) and an independently revealed mixture of the two active channels give
the linear face.

Remark 3.2. The theorem proves first contact and its nonzero jump. It does not assert uniqueness
of the positive maximizer for every larger multiplier or exclude a later branch exchange. The
exact envelope and flagged mixtures already cover such possibilities.
   For d = 2, the Bloch representation maps centered projectors to the real unit two-sphere
                     √ exact result is therefore the n = 3 real-sphere theorem of Dytso and
up to a factor 1/2. The
Cardone [8]. Put r = 1 − 2D and choose η ≥ 0 from
                                                        1
                                            r = coth η − .                                     (12)
                                                        η
For 0 < D < 1/2, such an η exists uniquely and
                                                           sinh η
                                       R2 (D) = ηr − log          .                            (13)
                                                              η
Moreover R2 (0) = +∞ by the limit η → ∞, while R2 (D) = 0 for D ≥ 1/2. This is a consistency
check and operational specialization, not a new real-sphere theorem.

                                                  4
```

---

## Page 5

```text
Numerical Legendre envelope                                                    Selected global radial maximizer
                                                                                             1.0
                             d=2
                     14
                             d=3
                     12      d=4                                                             0.8




                                                                     active radius b * (λ)
                             d=5
 rate Rd(D) (nats)




                     10
                                                                                             0.6
                     8

                     6                                                                       0.4

                     4
                                                                                             0.2
                     2

                     0                                                                       0.0
                      1.0      0.8       0.6        0.4        0.2                                 0         1       2      3        4     5     6
                                 normalized distortion D/R02                                                       scaled multiplier λ/d



Figure 1: Numerical evaluation of the exact finite-dimensional scalar envelope for d = 2, 3, 4, 5.
Left: Rd (D) versus normalized distortion. Right: one selected globally active radius versus
scaled multiplier. The qubit radius emerges continuously, while the higher-dimensional curves
show the finite jump proved in Theorem 3.1. The bounded scalar computation is a reproducibility
diagnostic, not a proof input.

Proposition 3.3 (Exact fixed-dimensional high-fidelity asymptotic). For every fixed d ≥ 2,
                                 2(d − 1)
                                          − (d − 1) − log Γ(d) + o(1),
                              Rd (D) = (d − 1) log                                                                             D ↓ 0.           (14)
                                     D
Proof. Put m = d − 1. For integer d,
                                                             
                                                      m−1
                                                      X sj
                             Md (s) = Γ(d)s−m es −           .                                                                                (15)
                                                           j!
                                                                                                       j=0
                                                      Pm−1 j
For s > 0 let ℓd (s) = log(1 − e−s                      j=0 s /j!) ≤ 0. For a traceless Hermitian report A, define
                                                          Z
                                                 Qλ (A) = exp{−λ∥Sx − A∥2F } dµd (x).                           (16)

For the axial reproduction Ab,u = b(ρu − I/d),
                                                                       2
                            log Qλ (Ab,u ) = −m log(2λ) + log Γ(d) − λR0,d (1 − b)2 − m log b + ℓd (2λb).                                       (17)
                                                                                       2 s for
Taking b = 1 gives a lower bound with vanishing error. For the upper bound, Kd (s) ≤ R0,d
                                                                                         2 /4.
s ≥ 0, so radii b ≤ 1/2 are eventually excluded because their radial gain is at most −λR0,d
On b ≥ 1/2, use − log b ≤ 2(1 − b) and ℓd ≤ 0 to bound the remaining correction by
                                                  2                                                     m2
                                               −λR0,d (1 − b)2 + 2m(1 − b) ≤                             2 = o(1).                              (18)
                                                                                                       λR0,d
Consequently
                                                  cd (λ) = −m log(2λ) + log Γ(d) + o(1).                                                        (19)
Secant inequalities for the convex function cd imply −λgλ → m for every gλ ∈ ∂cd (λ). If λD
maximizes the exact conjugate, then −D ∈ ∂cd (λD ) and λD D → m. Therefore
                                               Rd (D) = −λD D − cd (λD )                                                                        (20)
                                                      = −m + m log(2λD ) − log Γ(d) + o(1)                                                      (21)
                                                              2m
                                                      = m log    − m − log Γ(d) + o(1),                                                         (22)
                                                               D

                                                                     5
```

---

## Page 6

```text
which proves (14).

    The limits d → ∞ at fixed normalized distortion and D ↓ 0 at fixed d are distinct. The
following sections resolve the first regime; a uniform double-scaling theory remains open.


4    Uniform projective Laplace principle
The transition occurs at λ of order d. We first isolate the corresponding asymptotic partition.

Lemma 4.1 (Uniform beta Laplace principle). For y ≥ 0, put
                                                   1
                                       Fd (y) =      log Md (dy).                                (23)
                                                   d
Then Fd → Φ locally uniformly on [0, ∞), where
                                    (
                                      0,                     0 ≤ y ≤ 1,
                            Φ(y) =                                                               (24)
                                      y − 1 − log y,         y > 1.

Proof. Rewrite the beta integral as
                                          Z 1
                      Md (dy) = (d − 1)         exp{dyt + (d − 2) log(1 − t)} dt.                (25)
                                           0

For fixed ε > 0, the usual compact-interval Laplace bounds apply on [0, 1 − ε]. On the remaining
interval the original factor (1 − t)d−2 supplies exponential control; letting ε decrease after d → ∞
gives the pointwise limit
                                         sup {yt + log(1 − t)}.                                   (26)
                                      0≤t<1

The maximizer is t = 0 for y ≤ 1 and t = 1 − y −1 for y > 1, which yields (24). Moreover,

                                      Fd′ (y) = Ed,y Td ∈ [0, 1],                                (27)

where Ed,y is expectation under exponential tilt dy. Hence the family is equi-Lipschitz. A
finite-net argument upgrades pointwise convergence to local-uniform convergence because Φ is
continuous.

    For α ≥ 0, define the normalized optimized gain
                                                 1
                                     gd (α) =       max Gd,αd (b).                               (28)
                                                 d 0≤b≤1

Corollary 4.2 (Thermodynamic free-energy convergence). The functions gd converge locally
uniformly to
                           g(α) = max {Φ(2αb) − αb2 }.                              (29)
                                           0≤b≤1

                    2 → 1, and d−1 K (2αdb) = F (2αb) − 2αb/d give uniform convergence of
Proof. Lemma 4.1, R0,d                 d             d
the objective on compact α intervals and b ∈ [0, 1]. Taking a maximum preserves it.




                                                    6
```

---

## Page 7

```text
5    Global coexistence and the dimension-independent constants
The limiting scalar problem is globally solvable.

Theorem 5.1 (Exact limiting phase diagram). Let y∗ > 2 be the unique nontrivial root of

                                           y∗ − 1 = 2 log y∗ .                                   (30)

Define
                                           y∗2                       1
                                 α∗ =             ,       b∗ = 1 −      .                        (31)
                                        2(y∗ − 1)                    y∗
Then g(α) = 0 for 0 ≤ α ≤ α∗ . At α∗ the global maximizers in (29) are exactly 0 and b∗ . For
α > α∗ the positive global maximizer is unique and equals
                                         1                           p
                        b+ (α) = 1 −          ,       y+ (α) = α +       α(α − 2).               (32)
                                       y+ (α)

Proof. Set y = 2αb. The optimization becomes

                                               y2
                                                 
                                    max Φ(y) −      .                                            (33)
                                   0≤y≤2α      4α

For y ≤ 1 the objective is nonpositive and vanishes only at y = 0. For y > 1, an interior
stationary point obeys
                                1    y                  y2
                            1− −        = 0,    α=            .                      (34)
                                y 2α                 2(y − 1)
The two positive stationary points appear at α = 2; the larger root is y+ (α) and is the local
maximum. At any stationary point the gain is

                                             y2   y−1
                                    Φ(y) −      =     − log y.                                   (35)
                                             4α    2
The function y − 1 − 2 log y decreases on (1, 2), increases on (2, ∞), and has exactly the roots 1
and y∗ . Thus the larger stationary point first ties the zero-radius solution at y∗ . More explicitly,
for y > 1,
                                          y2
                                            
                              d                       (y − y− )(y − y+ )
                                  Φ(y) −        =−                       .                       (36)
                             dy          4α                 2αy
For α < 2 the derivative is strictly negative. For α ≥ 2, y− is a local minimum and y+ is the
only local maximum; the objective decreases after y+ , so the endpoint y = 2α cannot improve it.
Equation (35) then decides exactly when that maximum beats zero and proves the complete
statement.

    Numerically,

                                           y∗ = 3.512862417252 . . . ,
                                           α∗ = 2.455407482284 . . . ,
                                                                                                 (37)
                                            b∗ = 0.715331862959 . . . ,
                                δ∗ := 1 − b2∗ = 0.488300325835 . . . .




                                                      7
```

---

## Page 8

```text
6    Closed thermodynamic information–accuracy frontier
                                                       2 .
We normalize distortion by the zero-information value R0,d

Theorem 6.1 (Thermodynamic Born-prediction frontier). For each fixed 0 < δ ≤ 1,
                                           1       2
                                       lim   Rd (δR0,d ) = r∞ (δ),                               (38)
                                       d→∞ d

where                                  (         √
                                        − log(1 − 1 − δ),          0 < δ ≤ δ∗ ,
                            r∞ (δ) =                                                             (39)
                                         α∗ (1 − δ),               δ∗ ≤ δ ≤ 1.
The branches agree at δ∗ , where r∞ (δ∗ ) = log y∗ .

Proof. Theorem 2.1, with λ = αd, gives
                             1       2             2
                               Rd (δR0,d ) = sup{αR0,d (1 − δ) − gd (α)}.                        (40)
                             d               α≥0

We first justify passage of the supremum to the limit. Fix δ > 0 and put η = δ/8. The beta tail
is exact: P{Td ≥ 1 − η} = η d−1 . Evaluating the partition on this event and choosing b = 1 gives
                                                            
                                                 1           1
                            gd (α) ≥ α 1 − 2η −     + 1−         log η.                      (41)
                                                 d           d

Consequently, for every d ≥ 2 and α ≥ 0,
                                                                         
                            2                       δ                 1
                          αR0,d (1 − δ) − gd (α) ≤ − α −           1−         log η.             (42)
                                                           4          d

Thus all maximizing multipliers lie in a common compact interval. Local uniform convergence
from Corollary 4.2 now yields

                                  r∞ (δ) = sup{α(1 − δ) − g(α)}.                                 (43)
                                             α≥0

     The right derivative of g jumps at α∗ from 0 to b2∗ . Therefore gains 1 − δ ≤ b2∗ lie on the
coexistence face and give α∗ (1 − δ). If 1 − δ > b2∗ , envelope differentiation on the unique positive
branch gives
                                      1 − δ = g ′ (α) = b+ (α)2 .                                 (44)
         √
Put b = 1 − δ and y = (1 − b)−1 . Substitution into the conjugate is explicit: at a stationary
point
                        αb2 − g(α) = 2αb2 − Φ(y) = y − 1 − Φ(y) = log y.                          (45)
                                        √
Thus it reduces to log y = − log(1 − 1 − δ). At coexistence, (30) makes this value log y∗ =
α∗ b2∗ .

    The fixed-δ order of limits is essential. The theorem does not assert uniformity as δ ↓ 0; the
fixed-dimensional high-resolution limit is a different asymptotic regime.




                                                       8
```

---

## Page 9

```text
5                                                                                       2.4
( ) (nats per dimension)


                                                                                                                   2.3




                                                                                         scaled onset multiplier
                           4
                                                                                                                   2.2
                           3
                                                                                                                   2.1
                           2
                                                                                                                   2.0
    r∞ δ




                           1                                                                                       1.9                           exact scalar λc, d/d
                                                                                                                                                 α * − c * log(d)/d
                                                                                                                                                 α*
                           0                                                                                       1.8
                            0.0      0.2       0.4        0.6          0.8         1.0                                      101                                 102
                                           normalized distortion δ                                                       Hilbert-space dimension d

Figure 2: Left: the exact limiting information–accuracy curve and its coexistence point δ∗ . Right:
finite-dimensional first-contact multipliers from the exact scalar problem, the leading logarithmic
approximation, and the limit α∗ . The plotted finite-dimensional values are reproducibility
diagnostics, not proof inputs.

7                              Thermodynamic first contact and its logarithmic finite-size
                               correction
Retain the first multiplier λc,d at which a positive radius is a global maximizer of (5), and choose
any positive active radius bc,d there.
Lemma 7.1 (Beta-mgf exclusion bound). For 0 ≤ s < d,
                                                                Kd (s) ≤ − log(1 − s/d) − s/d.                                                                   (46)
Consequently a minimizing first-contact tilt cannot satisfy s/d → 0.
Proof. The hypergeometric series and (d)k ≥ dk give
                                                                     X sk             X
                                                     Md (s) =                     ≤    (s/d)k = (1 − s/d)−1 .                                                    (47)
                                                                           (d)k
                                                                     k≥0              k≥0

After centering, this is (46). If u = s/d → 0, then the right side is u2 /2 + O(u3 ), so the ratio term
                        2 d2 /2. On the other hand, evaluating (60) at s = dy gives λ
is at least (1 + o(1))R0,d                                                       ∗          c,d = O(d).
Therefore a minimizing tilt cannot have s/d → 0.

Lemma 7.2 (Uniform interior Kummer–Laplace expansion). Let J ⋐ (1, ∞) be compact.
Uniformly for y ∈ J,                     √
                       Md (dy) = edΦ(y) y 2πd [1 + OJ (d−1 )],               (48)
and hence
                                                                                  1              √
                                               log Md (dy) = dΦ(y) +                log d + log(y 2π) + OJ (d−1 ).                                               (49)
                                                                                  2
Proof. Write
                                                   Z 1
                               Md (dy) = (d − 1)         edfy (t) g(t) dt,         fy (t) = yt + log(1 − t),                      g(t) = (1 − t)−2 .             (50)
                                                     0

The unique maximizer is ty = 1 − y −1 , and as y ranges over J the points ty remain in a fixed
compact subinterval of (0, 1). Choose ρ > 0 so that [ty − ρ, ty + ρ] ⊂ (0, 1) for every y ∈ J.
Compactness and strict concavity give a uniform cJ > 0 such that
                                                    fy (t) ≤ Φ(y) − cJ            whenever |t − ty | ≥ ρ, y ∈ J.                                                 (51)

                                                                                         9
```

---

## Page 10

```text
Thus the exterior integral is exponentially smaller than the main term.
   On the interior neighborhood,

            fy′′ (ty ) = −y 2 ,   fy′′′ (ty ) = −2y 3 ,         fy(4) (ty ) = −6y 4 ,   g(ty ) = y 2 .   (52)

All derivatives of√fy through order five and of g through order three are uniformly bounded
there. With z = d (t − ty ), Taylor’s theorem through fourth order gives a Gaussian integrand
    2 2
e−y z /2 times a factor whose even contribution is 1 + OJ (d−1 )(1 + |z|6 ); the order-d−1/2 term
is odd and integrates to zero on the symmetric neighborhood. On |z| ≤ d1/10 the remainder is
uniformly dominated by an integrable Gaussian times OJ (d−1 )(1 + |z|10 ); on the remainder of
the interior neighborhood strict concavity gives an exponentially small bound. Therefore
                                                     s
                                                           2π
                     Md (dy) = (d − 1)e dΦ(y)
                                              g(ty )                 [1 + OJ (d−1 )]          (53)
                                                       d|fy′′ (ty )|
                                                r
                                                     2π
                             = (d − 1)e dΦ(y) 2
                                              y          [1 + OJ (d−1 )]                      (54)
                                                    dy 2
                                       √
                             = edΦ(y) y 2πd [1 + OJ (d−1 )].                                  (55)

Taking logarithms proves (49).

Theorem 7.3 (First-contact asymptotics). As d → ∞,

                                       λc,d
                                            → α∗ ,              bc,d → b∗ .                              (56)
                                        d
The coexistence distortion and rate satisfy
                                    Dc,d                      Rc,d
                                     2 → δ∗ ,
                                    R0,d                       d
                                                                   → log y∗ .                            (57)

More sharply,

                                                                           α∗          y∗2
                   λc,d = α∗ d − c∗ log d + O(1) ,               c∗ =            =            .          (58)
                                                                        2 log y∗   2(y∗ − 1)2

Proof. Write s = 2λb. Nonnegative radial gain and b ≤ 1 are equivalent to
                                                2 s2
                                               R0,d                 s
                                        λ≥                ,       λ≥ .                                   (59)
                                              4Kd (s)               2

Hence                                                     (                )
                                                                   2   2
                                                               s R0,d s
                                    λc,d = inf max              ,              .                         (60)
                                             s>0               2 4Kd (s)
Evaluating this expression at s = dy∗ and using local-uniform Laplace convergence gives
lim supd λc,d /d ≤ α∗ . This comparison will be used below to localize every minimizing sequence.
For s = dy with y > 1, Lemma 4.1 makes the second term divided by d converge locally uniformly
to
                                                    y2
                                         A(y) =         .                                    (61)
                                                  4Φ(y)
Its unique global minimizer is y∗ : the equation A′ (y) = 0 is exactly (30), A(y∗ ) = α∗ , and
y∗ /2 < α∗ . Lemma 7.1 excludes s/d → 0. If instead s/d → y ∈ (0, 1], local-uniform Laplace
convergence gives Kd (s)/d → Φ(y) = 0, so the ratio term in (60), after division by d, diverges.
The term s/2 excludes s/d → ∞. Thus every minimizing sequence lies in a compact subset of

                                                          10
```

---

## Page 11

```text
(1, ∞), where uniform convergence and uniqueness imply sc,d /d → y∗ and λc,d /d → α∗ . For all
large d the second term in (60) is active, so

                                      sc,d   2Kd (sc,d )    2Φ(y∗ )
                            bc,d =         =   2         −→         = b∗ .                       (62)
                                     2λc,d    R0,d sc,d       y∗

                                                2 (1 − b2 ) and R = λR2 b2 at coexistence.
The distortion and rate limits follow from D = R0,d                   0,d
   It remains to refine the multiplier. Apply Lemma 7.2 on a compact neighborhood of y∗ .
                                       2 = 1 − d−1 gives
Using Kd (dy) = log Md (dy) − y and R0,d

                               2 d2 y 2
                              R0,d                       A(y)
                                          = dA(y) −            log d + O(1)                      (63)
                              4Kd (dy)                   2Φ(y)

uniformly there. Put q(y) = A(y)/(2Φ(y)). On a fixed neighborhood U of y∗ there are constants
c, L, C > 0 such that A(y) ≥ A(y∗ ) + c|y − y∗ |2 , |q(y) − q(y∗ )| ≤ L|y − y∗ |, and the remainder in
(63) has absolute value at most C. Thus, with z = y − y∗ , the right side is bounded below by

                           dA(y∗ ) − q(y∗ ) log d + dcz 2 − L(log d)|z| − C.                     (64)

The variable terms are at least −L2 (log d)2 /(4cd) = o(1). Evaluation at y = y∗ gives the
matching upper bound up to O(1). Since the global minimizer has already been shown to enter
U , we obtain λc,d = dA(y∗ ) − q(y∗ ) log d + O(1). Finally A(y∗ ) = α∗ and Φ(y∗ ) = log y∗ prove
(58).


8    Pointwise physical projection and source universality
So far the source is Haar. We now allow every pure input state and charge a representation
channel by its Shannon capacity over all input priors.
   Let ν be Haar measure on rank-one queries, or a weighted exact complex projective 2-design.
For a scalar report q ∈ L2 (ν), define its risk against x by
                                         Z
                                ℓx (q) = |q(y) − tr(ρx ρy )|2 dν(y).                     (65)

Theorem 8.1 (Pointwise projection to a physical Born reporter). For every q ∈ L2 (ν) there
exists a density matrix σ(q) such that
                                                     
                                  ℓx y 7→ tr(σ(q)ρy ) ≤ ℓx (q)                        (66)

simultaneously for every pure x. The map q 7→ σ(q) may be chosen Borel measurable. Moreover,

                                                           ∥ρx − σ∥2F
                            Z
                               | tr[(ρx − σ)ρy ]|2 dν(y) =            .                 (67)
                                                            d(d + 1)

Proof. Let
                              B = {y 7→ tr(Aρy ) : A = A∗ } ⊂ L2 (ν).                            (68)
The 2-design identity makes this a finite-dimensional closed subspace with matrix norm

                                                 tr(A2 ) + (tr A)2
                                       ∥A∥2∗ =                     .                             (69)
                                                     d(d + 1)

Let fA be the orthogonal projection of q onto B. Because fρx ∈ B,

                              ∥fρx − q∥22 = ∥fρx − fA ∥22 + ∥q − fA ∥22 .                        (70)

                                                    11
```

---

## Page 12

```text
Next let σ be the metric projection of A in the norm (69) onto the compact convex density-matrix
body. Since ρx belongs to that body, the Hilbert projection inequality gives

                                  ∥fρx − fσ ∥2 ≤ ∥fρx − fA ∥2 .                              (71)

This proves (66). Orthogonal projection onto a finite-dimensional subspace is continuous in L2 ,
and metric projection onto a closed convex set in finite dimension is continuous, establishing
the measurable choice. Finally, both matrices in (67) have trace one, so the trace term in (69)
vanishes.

    Consider a channel W from pure states to an arbitrary standard-Borel classical memory Z,
followed by jointly measurable probability reports qZ (y) ∈ [0, 1]; bounded joint measurability
makes z 7→ qz a Borel L2 (ν)-valued map. Its worst-state Born risk is supx E[ℓx (qZ )|X = x]. Its
information cost is its channel capacity

                                     C(W ) = sup IP (X; Z),                                  (72)
                                                 P
                                                                     2 , let
where the supremum ranges over all pure-state priors. For 0 ≤ D ≤ R0,d
                                                                      
                                                                 D
                  Wd (D) = (W, q) : sup E[ℓx (qZ )|X = x] ≤              .                   (73)
                                       x                      d(d + 1)
Define the source-universal frontier by

                             Cduniv (D) =       inf    sup IP (X; Z).                        (74)
                                            (W,q)∈Wd (D) P

                                                                          2 , the
Theorem 8.2 (Exact source-universal minimax capacity). For every 0 ≤ D ≤ R0,d
minimum channel capacity in (74) is exactly

                                        Cduniv (D) = Rd (D) .                                (75)

The Haar prior is least favorable for an optimal covariant channel.
Proof. Theorem 8.1 lets us replace every report by a density report without increasing any
statewise risk or channel capacity. Every uniformly feasible channel is therefore feasible under
Haar input, so
                                C(W ) ≥ IHaar (X; Z) ≥ Rd (D).                              (76)
    Conversely, Theorem 2.1 supplies a covariant complex-Bingham channel WD , or an inde-
pendently flagged mixture of active channels on a coexistence face, with constant statewise
distortion D. Let QD be its output law under Haar input. For one active orbit, covariance
makes the divergence below independent of x, and Haar averaging identifies its value with the
              P information. On a coexistence
attained mutual                       P       face, write the revealed-flag channel and output
law as WD = j aj δj ⊗ Wj and QD = j aj δjP    ⊗ Qj . The flag is independent of x, so the same
conclusion follows from DKL (WD (·|x)∥QD ) = j aj DKL (Wj (·|x)∥Qj ). Thus

                                  DKL (WD (·|x)∥QD ) = Rd (D)                                (77)

independent of x. For every input prior P , the classical information-radius identity [16] gives
                             Z
                 IP (X; Z) = DKL (WD (·|x)∥QD ) dP (x) − DKL (P WD ∥QD )                      (78)

                            ≤ Rd (D).                                                        (79)
                                                                                      2 .
Haar input attains equality, proving both capacity and minimax equality for 0 < D < R0,d
          2 the constant report has zero capacity. At D = 0, exact reconstruction of the
At D = R0,d
non-atomic projective source has infinite capacity, matching Rd (0) = ∞.

                                                 12
```

---

## Page 13

```text
This specialization is not a novelty claim for invariant, compound-source, or minimax rate–
distortion theory itself; such formulations go back at least to Sakrison, with compact-group and
modern universal-coding developments in [9, 10, 11]. The result here is the exact evaluation of
the stated projective worst-state frontier.


9    Exact finite-block cost and zero dispersion
For convenience extend Rd (D) by zero for D ≥ R0,d2 ; this preserves convexity and monotonicity.

    Allow an arbitrary joint channel from n pure input states to a shared classical memory with
a standard-Borel output alphabet and n joint reports, each Borel as a map from the memory
into L2 (ν). Define
                                 univ
                               Cd,n   (D) = inf sup IP (X n ; Z),                          (80)
                                                 (Wn ,q n ) PX n

where the infimum is subject to
                                  n
                              "                        #
                                1X               n   n      D
                          sup E     ℓxt (qt,Z ) X = x ≤           .                           (81)
                           x n  n                        d(d + 1)
                                     t=1

Theorem 9.1 (Exact arbitrary-joint-memory finite-block law). For every integer n ≥ 1 and
         2 ,
0 ≤ D ≤ R0,d
                                            univ
                                           Cd,n  (D) = nRd (D) .                              (82)

Arbitrary correlations in the representation do not lower the cost; a memoryless causal product
of covariant complex-Bingham channels attains it.

Proof. For the lower bound, choose the iid Haar prior and apply the pointwise projection
coordinatewise. If Dt is the marginal mean projector distortion, independence and the mutual-
information chain rule give
                                    X             X
                       I(X n ; Z) −   I(Xt ; Z) =   I(Xt ; X t−1 |Z) ≥ 0.                (83)
                                       t                     t

Data processing and the one-letter converse therefore give
                               n                      n
                                                                                      !
                      n
                               X                      X                      1X
                  I(X ; Z) ≥         I(Xt ; ρbt ) ≥         Rd (Dt ) ≥ nRd       Dt       ,   (84)
                                                                             n t
                               t=1                    t=1

where the last step is convexity. The worst-sequence constraint implies n−1 t Dt ≤ D under
                                                                             P
iid Haar input, so monotonicity yields the claimed lower bound. For the upper bound use WD⊗n .
Relative to Q⊗n
             D , every input sequence has divergence nRd (D) by (77); the information-radius
identity upper-bounds capacity by that value, and iid Haar input attains it.

   We next turn from stochastic representations to fixed-length lossy codes. An (n, M, D, ϵ)
code maps an iid Haar source X n to one of M messages and then to physical density reports ρbn ,
with                            ( n                       )
                                  1X
                              P         ∥ρXt − ρbt ∥2F > D ≤ ϵ.                           (85)
                                  n
                                           t=1

Theorem 9.2 (Zero dispersion and exponential strong converse). Let 0 < D < R0,d            2  be a
differentiability point of Rd ; this includes the relative interior of every linear face. Then the
corresponding D-tilted information is constant:

                          ȷX (x, D) = Rd (D)          for Haar-almost every x.                (86)

                                                      13
```

---

## Page 14

```text
Hence the rate dispersion is zero. Every fixed-length n-state code obeys

                                   ϵ ≥ [1 − exp{log M − nRd (D)}]+ .                            (87)

In particular, if log M ≤ n(Rd (D) − η), then ϵ ≥ 1 − e−nη .

Proof. Compactness of the source and physical reproduction spaces and continuity of the
bounded distortion give an attaining invariant KKT reproduction law Pρb∗ at every stated D. Set
λ = −R′d (D) > 0 and define
                                                Z
                                                           2
                         ȷX (x, D) = −λD − log e−λ∥ρx −bρ∥F dPρb∗ (b
                                                                   ρ).                     (88)

On a linear face take the invariant mixture of the supporting active physical orbit laws. By
transitivity, (88) is independent of x; its Haar mean is Rd (D) by dual equality. This proves
(86) and zero variance. Additivity makes the n-letter tilted information identically nRd (D).
Theorem 7 of Kostina and Verdú [12] states that, for every γ ≥ 0,

                            ϵ ≥ P{ȷX n (X n , nD) ≥ log M + γ} − e−γ .                          (89)

Taking γ = nRd (D) − log M when positive gives (87).

    Zero dispersion is a symmetry consequence, not a uniquely quantum effect. The theorem is
a converse; it does not assert a matching constant or 12 log n third-order achievability term.


10     Causal and finite-query consequences
Exact weighted complex projective 2-designs replace Haar query integration in Theorem 8.1
without changing any constants. This makes the probability-field risk finitely witnessable.
Sequential extensions require an explicit isotropy condition: a policy that always asks one fixed
ray tests only one overlap and cannot force full-state information.

Corollary 10.1 (History-dependent conditional-design tensorization). Let X1 , . . . , Xn be fresh
independent Haar preparations. At time t, a causal classical encoder produces Zt from (X t , Z t−1 ),
and the reporter may use Z t ; any externally randomized menu or seed visible to the reporter is
included in this transcript. For every allowed history on which the menu may depend, suppose
its conditional scoring measure is a weighted exact projective 2-design and the random query
draw has no additional access to the fresh Xt . Let ρbt (Z t ) be the measurable physical projection
of the current report and define

                                         Dt = E∥ρXt − ρbt (Z t )∥2F .                           (90)

Then
                                            n
                                                                                    !
                               n     n
                                            X                            1X
                          I(X ; Z ) ≥             Rd (Dt ) ≥ nRd             Dt         .       (91)
                                                                         n t
                                            t=1

For the causal factorization W ( dz n ∥xn ) =                        t−1 , xt ), define
                                                   Q
                                                     t Wt ( dzt |z

                                                       n
                                                       X
                                I(X n → Z n ) =              I(X t ; Zt |Z t−1 ).               (92)
                                                       t=1

For this exogenous iid source, Massey’s conservation identity [17] gives I(X n → Z n ) =
I(X n ; Z n ).



                                                       14
```

---

## Page 15

```text
Proof. Apply the conditional 2-design projection and the one-letter converse at each history.
Independence gives
                                              X
                              I(X n ; Z n ) =   I(Xt ; Z n |X t−1 )                     (93)
                                                  t
                                                  X
                                              ≥       I(Xt ; Z t |X t−1 )                          (94)
                                                  t
                                                  X
                                              =       I(Xt ; Z t , X t−1 )                         (95)
                                                  t
                                                  X
                                              ≥       I(Xt ; Z t ),                                (96)
                                                  t

and the one-letter bounds plus convexity complete the proof. Because the source law has no
feedback dependence on past Z, reverse directed information vanishes.

    At fixed 0 < δ < 1, Theorem 6.1 also implies a classical predictive information cost of
d r∞ (δ)/ log 2 + o(d) bits per state. A direct d-level quantum system has logarithmic Hilbert-
space size, but this comparison must not be misread: a single quantum specimen is not an exact
reusable classical probability oracle, and remote-state preparation or shared entanglement is a
different resource model [18, 19].


11     Operational boundary and open Grassmann frontier
The theorems concern probability-field calibration. They do not derive Born’s rule, simulate
state update, certify intrinsic randomness, or exclude click-only hidden-variable models. Indeed,
reproducing sampled clicks can require far less information than retaining calibrated probabilities
for all queries. Channel capacity is an operational asymptotic information resource; it is not a
literal count of physical memory states in one realization.
    The natural mathematical extension replaces a ray by a Haar rank-r projector. Axial
overlaps then have beta law Beta(r, d − r), and the skewness changes sign under r ↔ d − r.
However, the full partition is matrix-Jacobi rather than scalar Dirichlet. An axial ansatz is not
a proof: exact rank-r rate–distortion requires showing that a specified reconstruction spectrum
globally maximizes a matrix-Bingham/HCIZ integral at fixed Frobenius norm. Existing complex-
projective and Grassmann quantization results, arbitrary-radius metric-ball asymptotics, and
general rate–distortion bounds do not supply that extremum [4, 5, 6, 7]. We therefore leave it as
an explicit open problem.


12     Conclusion
We have given a self-contained rate–distortion theory for calibrated Born prediction on complex
projective space. The all-degree one-spike partition theorem reduces the unrestricted finite-
dimensional problem to an exact scalar complex-Bingham envelope, including flagged mixtures
at coexistence. It yields a discontinuous directional-information onset for every d ≥ 3, the
exact qubit specialization, and the sharp fixed-d high-fidelity constant. In the thermodynamic
regime, a uniform projective Laplace principle gives the closed two-piece frontier, the nontrivial
coexistence root y − 1 = 2 log y, and the finite-size correction λc,d = α∗ d − c∗ log d + O(1). Finally,
a pointwise physical-report projection upgrades Haar-average optimality to exact worst-state
channel capacity, arbitrary-joint-memory tensorization, zero dispersion, and an exponential
strong converse. The resulting theorem package connects exact finite-dimensional probability
prediction to its high-dimensional phase law without identifying calibrated prediction with click
generation or particle dynamics.


                                                  15
```

---

## Page 16

```text
Data and code availability
The accompanying archive repro_v1.zip is supplied as supplementary material with this
manuscript. It has the immutable content identifier SHA-256
                 54a0fd17a2b68bdfc62a188043be104ef533b1b20581789a9992ba912902821e.

From the extracted directory, the exact replay commands are
python verify_frontier.py
python verify_thermodynamic_limit.py --max-d 100 --output-dir .
They evaluate the finite-dimensional scalar envelope, the coexistence root, the bounded first-
contact problem, and the limiting curve using one process, without branch-and-bound or heavy
search. The generated JSON files record the environment, grids, residuals, and runtime. These
outputs are diagnostic; all headline results are analytic.


AI assistance and author responsibility
AI tools assisted with literature search, algebraic stress testing, editing, and reproducibility checks.
The author is responsible for the definitions, proofs, claims, citations, and final manuscript.


A     Finite-dimensional spectral reduction
We give the complete reduction so that every finite-dimensional input used in the main text is
verifiable within this manuscript.
Proposition A.1 (Brazitikos–Pandis normalized interface). Let d ≥ 2, let γ1 , γ2 , γ3 be nonneg-
ative integer multiplicities with γ1 + γ2 + γ3 = d, and let u, v, w ∈ R satisfy
                        γ1 u + γ2 v + γ3 w = 0,             γ1 u2 + γ2 v 2 + γ3 w2 = 1.              (97)
For the grouped vector
                                   x = (u, . . . , u, v, . . . , v , w, . . . , w),                  (98)
                                        | {z } | {z } | {z }
                                               γ1          γ2            γ3
and every positive integer m,
                                                r                                           !
                                                    d−1       1                    1
             pm (x) ≤ pm (a∗1 ),      a∗1 =             , −p         , . . . , −p               .    (99)
                                                     d      d(d − 1)             d(d − 1)
Here zero multiplicities cover the two-value case. This is precisely Proposition 5.5 of Brazitikos
and Pandis in their unit-norm normalization [15]. Homogeneity gives radius r by multiplying
the right side by rm .
Remark A.2. Proposition A.1 is the only external extremal inequality used below. It asserts the
grouped power-sum maximum. The reduction of an arbitrary spectrum to at most three values,
the odd-sign closure, the Newton step, the projective Laplace theorem, and the rate–distortion
application are proved here.
Lemma     A.3 P(All-degree centered power sums). Let d ≥ 3, r > 0, and let a ∈ Rd satisfy
                    2    2
P
  i ai = 0 and   i ai = r . Put
                              r                                         !
                       ∗         d−1        1                    1
                      a =r           , −p          , . . . , −p           .        (100)
                                  d       d(d − 1)             d(d − 1)
Then, for every integer m ≥ 2,
                                                                              X
                               |pm (a)| ≤ pm (a∗ ),             pm (a) =          am
                                                                                   i .              (101)
                                                                              i


                                                         16
```

---

## Page 17

```text
Proof. For m = 2, the assertion is immediate because p2 (a) = r2 = p2 (a∗ ) is fixed by the norm
constraint. Hence assume m ≥ 3. The centered sphere is compact. Its constraint gradients 1
and 2a are independent because a is nonzero and centered. At a constrained global maximum or
minimum of pm , Lagrange multipliers give

                                          mxm−1 − 2ξx − ζ = 0                                    (102)

for every coordinate value x. The derivative of this sparse polynomial is m(m − 1)xm−2 − 2ξ.
It has at most one real zero when m is odd and at most two when m is even. Rolle’s theorem
therefore leaves at most two, respectively three, distinct coordinate values at every global
extremum. Proposition A.1, applied precisely to this grouped centered fixed-norm class, places
the maximum of pm at a∗ . For odd m, the map a 7→ −a converts the minimum to minus the
maximum; for even m, pm (a) ≥ 0. This proves (101). The external proposition supplies the
grouped power-sum extremum, not the all-degree Laplace conclusion below.

   If P ∼ Dirichlet(1, . . . , 1), then

                                                   k!(d − 1)!
                                    E⟨a, P ⟩k =                hk (a),                           (103)
                                                  (d + k − 1)!

where hk is the complete homogeneous symmetric polynomial. Since p1 (a) = 0, Newton’s
expansion becomes
                                                 k
                                       X        Y  pj (a)mj
                          hk (a) =                          .                   (104)
                                                   mj !j mj
                                          m1 +2m2 +···+kmk =k j=2
                                                m1 =0

For d ≥ 3, every pj (a∗ ) with j ≥ 2 is positive. Hence
                                                              k
                                                 X            Y |pj (a)|mj
                   hk (a) ≤ |hk (a)| ≤                                             ≤ hk (a∗ ).   (105)
                                                                    mj !j mj
                                          m1 +2m2 +···+kmk =k j=2
                                                m1 =0

Equations (103) and (105), summed termwise in the entire exponential series, prove the axial
                                             √ When
projective partition inequality in every degree.     √ d = 2, the centered fixed-radius sphere
consists only of the two permutations of (r/ 2, −r/ 2), so the result is immediate.
   It remains to derive and attain the scalar envelope. Write a density reproduction as I/d + A,
where tr A = 0 and ∥A∥F ≤ R0,d . For
                                          Z
                                                       2
                                Qλ (A) = e−λ∥Sx −A∥F dµd (x),                              (106)

conditional Gibbs duality, applied to every posterior given A, gives

                     I(X; A) ≥ −λD − E log Qλ (A) ≥ −λD − log sup Qλ (A).                        (107)
                                                                               A

At fixed ∥A∥F , diagonalization and the all-degree partition inequality replace its spectrum by
the valid axial density comparator A = b(ρu − I/d), 0 ≤ b ≤ 1. For this comparator,
                                 2                  2 2        2
                 log Qλ (A) = −λR0,d + Kd (2λb) − λR0,d b = −λR0,d + Gd,λ (b).                   (108)

Maximizing first over b and then over λ proves the converse in Theorem 2.1.
  For equality, let b > 0 be active, put κ = 2λb, and take
                                                          2
                                dPX|U =u       eκ|⟨x,u⟩|
                                         (x) =           ,          U ∼ µd .                     (109)
                                  dµd           Md (κ)

                                                     17
```

---

## Page 18

```text
Invariance makes the source marginal Haar. If md (κ) = ∂κ log Md (κ), stationarity of the active
radius is
                                         dmd (κ) − 1
                                      b=              .                                    (110)
                                             d−1
Thus the conditional mean is exactly (1 − b)I/d + bρu , so the channel is its own posterior-mean
reproduction. It attains
          2
    Db = R0,d (1 − b2 ),                                   2
                            Ib = κmd (κ) − log Md (κ) = λ(R0,d − Db ) − max Gd,λ (v).      (111)
                                                                         0≤v≤1

                                        2 + max G
The optimized log partition cd (λ) = −λR0,d       b d,λ (b) is convex, and Danskin’s theorem
gives
                           −∂cd (λ) = conv{Db : b is active at λ}.                      (112)
Independently flagged mixtures of the corresponding invariant channels attain every distortion in
this interval. The independent channel gives D = R0,d 2 , I = 0; exact reconstruction is obtained
                                                                           2 are covered without
as the limiting endpoint and has infinite information. Thus all 0 ≤ D ≤ R0,d
assuming uniqueness of the finite-dimensional radial maximizer.


References
 [1] Armine Bagyan and Donald Richards. “Complete Asymptotic Expansions and the High-
     Dimensional Bingham Distributions”. In: TEST 33.2 (2024), pp. 540–563. doi: 10.1007/
     s11749-023-00910-w. eprint: 2303.10290. url: https://doi.org/10.1007/s11749-
     023-00910-w.
 [2] Nico M. Temme. “Uniform Asymptotic Expansions of Confluent Hypergeometric Functions”.
     In: IMA Journal of Applied Mathematics 22.2 (1978), pp. 215–223. doi: 10.1093/imamat/
     22.2.215. url: https://doi.org/10.1093/imamat/22.2.215.
 [3] José L. López and Pedro J. Pagola. “The Confluent Hypergeometric Functions M (a, b; z)
     and U (a, b; z) for Large b and z”. In: Journal of Computational and Applied Mathematics
     233.6 (2010), pp. 1570–1576. doi: 10.1016/j.cam.2009.02.072. url: https://doi.org/
     10.1016/j.cam.2009.02.072.
 [4] Bishwarup Mondal, Satyaki Dutta, and Robert W. Heath Jr. “Quantization on the
     Complex Projective Space”. In: Proceedings of the Data Compression Conference. 2006.
     doi: 10.1109/DCC.2006.68. url: https://doi.org/10.1109/DCC.2006.68.
 [5] Wei Dai, Youjian Liu, and Brian Rider. “Quantization Bounds on Grassmann Manifolds
     and Applications to MIMO Communications”. In: IEEE Transactions on Information
     Theory 54.3 (2008), pp. 1108–1123. doi: 10.1109/TIT.2007.915691. eprint: cs/0603039.
     url: https://doi.org/10.1109/TIT.2007.915691.
 [6] Renaud-Alexandre Pitaval, Lu Wei, Olav Tirkkonen, and Jukka Corander. “Volume of
     Metric Balls in High-Dimensional Complex Grassmann Manifolds”. In: IEEE Transactions
     on Information Theory 62.9 (2016), pp. 5105–5116. doi: 10.1109/TIT.2016.2594289.
     arXiv: 1508.00256. url: https://doi.org/10.1109/TIT.2016.2594289.
 [7] Erwin Riegler, Günther Koliander, and Helmut Bölcskei. “Lossy Compression of General
     Random Variables”. In: Information and Inference: A Journal of the IMA 12.3 (2023),
     pp. 1759–1829. doi: 10.1093/imaiai/iaac035. eprint: 2111.12312. url: https://doi.
     org/10.1093/imaiai/iaac035.
 [8] Alex Dytso and Martina Cardone. Uniform Distribution on (n − 1)-Sphere: Rate-Distortion
     under Squared Error Distortion. 2024. arXiv: 2401.04248 [cs.IT]. url: https://arxiv.
     org/abs/2401.04248.


                                               18
```

---

## Page 19

```text
[9] David J. Sakrison. “The Rate Distortion Function for a Class of Sources”. In: Information
     and Control 15.2 (1969), pp. 165–195. doi: 10.1016/S0019- 9958(69)90403- 3. url:
     https://doi.org/10.1016/S0019-9958(69)90403-3.
[10] Peter Harremoës. “Maximum Entropy on Compact Groups”. In: Entropy 11.2 (2009),
     pp. 222–237. doi: 10.3390/e11020222. url: https://doi.org/10.3390/e11020222.
[11] Adeel Mahmood and Aaron B. Wagner. Minimax Rate-Distortion. 2022. arXiv: 2202.04481
     [cs.IT]. url: https://arxiv.org/abs/2202.04481.
[12] Victoria Kostina and Sergio Verdú. “Fixed-Length Lossy Compression in the Finite
     Blocklength Regime”. In: IEEE Transactions on Information Theory 58.6 (2012), pp. 3309–
     3338. doi: 10.1109/TIT.2012.2186786. eprint: 1102.3944. url: https://doi.org/10.
     1109/TIT.2012.2186786.
[13] John T. Kent. “The Complex Bingham Distribution and Shape Analysis”. In: Journal of the
     Royal Statistical Society: Series B 56.2 (1994), pp. 285–299. doi: 10.1111/j.2517-6161.
     1994.tb01978.x. url: https://doi.org/10.1111/j.2517-6161.1994.tb01978.x.
[14] Kanti V. Mardia and Ian L. Dryden. “The Complex Watson Distribution and Shape
     Analysis”. In: Journal of the Royal Statistical Society: Series B 61.4 (1999), pp. 913–926.
     doi: 10.1111/1467-9868.00210. url: https://doi.org/10.1111/1467-9868.00210.
[15] Silouanos Brazitikos and Christos Pandis. Sharp Inequalities for Symmetric Polynomials,
     Hunter’s Conjecture, and Moments of Exponential Random Variables. 2025. arXiv: 2512.
     12254 [math.PR]. url: https://arxiv.org/abs/2512.12254.
[16] Imre Csiszár and Paul C. Shields. “Information Theory and Statistics: A Tutorial”. In:
     Foundations and Trends in Communications and Information Theory 1.4 (2004), pp. 417–
     528. doi: 10.1561/0100000004. url: https://doi.org/10.1561/0100000004.
[17] James L. Massey. “Causality, Feedback and Directed Information”. In: Proceedings of the
     International Symposium on Information Theory and Its Applications. 1990, pp. 303–305.
     url: https://www.isiweb.ee.ethz.ch/archive/massey_pub/pdf/BI532.pdf.
[18] Charles H. Bennett, David P. DiVincenzo, Peter W. Shor, John A. Smolin, Barbara
     M. Terhal, and William K. Wootters. “Remote State Preparation”. In: Physical Review
     Letters 87.7 (2001), p. 077902. doi: 10.1103/PhysRevLett.87.077902. eprint: quant-
     ph/0006044. url: https://doi.org/10.1103/PhysRevLett.87.077902.
[19] Charles H. Bennett, Patrick Hayden, Debbie W. Leung, Peter W. Shor, and Andreas Winter.
     “Remote Preparation of Quantum States”. In: IEEE Transactions on Information Theory
      51.1 (2005), pp. 56–74. doi: 10.1109/TIT.2004.839476. eprint: quant-ph/0307100. url:
      https://doi.org/10.1109/TIT.2004.839476.




                                              19
```
