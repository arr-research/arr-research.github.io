# Complete contraction of unital qubit channels and order-constrained depolarization

Rendition of canonical15-page paper.pdf, SHA256 f805a688fb62e9bb34f4c8f107f906c4f85613f831cfda424d1805b797fffe07.

Complete contraction of unital qubit channels and order-constrained
                          depolarization
                                              Lluis Eriksson

                                             27 October 2026


                                                  Abstract
         We determine the complete equal-reference contraction coefficients of the minimal quantum
     Fisher metric, its quadratic chi-square divergence and the finite triangular Petz divergence for
     every unital qubit channel. For a faithful normalized Choi state J, all three equal 1 − 16/ Tr(J −1 );
     for singular J they equal one. An explicit qubit–qutrit lower family matches a harmonic-weight
     upper bound and gives the exact stabilization envelope, including a maximal factor of nine
     between coefficient suprema. For depolarization in dimension d, a commuting Bell family matches
     the order bound λ2 κ/[1 + λ(κ − 1)] for each normalized nonaffine operator-convex Petz generator
     when 1 < κ ≤ d2 /2. A principal-rich rank-two ladder extends SLD and triangular sharpness
     to κ ≤ d(2d − 1)/2, with the budget taken against the actual reference marginal. A separate
     logarithmic analysis gives the complete equal-reference BKM and finite relative-entropy lower
     bound λ2 P/[1 + λ(P − 1)], P = d(d − 1); for d ≥ 3 it improves the endpoint of the specified Bell
     family. In the qubit case we identify exact classical-reference and separable/PPT restrictions
     over the full physical noise range. A localized rational counterexample addresses one printed
     Doeblin equivalence. These results do not determine unrestricted BKM, relative-entropy, actual-
     mutual-information or capacity coefficients; the lower constructions are not unitary phase models.
     Faithful limits, adverse controls, prior-work dependencies and model-review limits are explicit.

Revision status. Expanded continuation of the same evolving contraction problem. Technical
audit1044 supports the new scoped statements; this combined manuscript awaits a full exact-PDF
assessment and inherits no grade.


1    Quantities and scope
Let A and R be finite-dimensional systems. All local maps below are tensored with idR , whether
or not this is written. A state is faithful if it is positive definite. We use the Hilbert–Schmidt
inner product ⟨X, Y ⟩ = Tr X † Y on the complex Hilbert space of matrices. Define La (X) = aX
and Rb (X) = Xb. For faithful a, b, these are commuting positive invertible superoperators. This
statement concerns positivity on Hilbert–Schmidt space, not preservation of the cone of positive
matrices.
    For a faithful state σ and a Hermitian tangent Z, set
                                                              −1
                                 gσSLD (Z) = ⟨Z, (Lσ + Rσ )/2 Z⟩.
                                                
                                                                                               (1)

This is the minimal monotone, or symmetric logarithmic derivative (SLD), quantum Fisher quadratic
form. Its associated finite chi-square divergence is

                                        χ2min (ρ∥σ) = gσSLD (ρ − σ).                                          (2)

                                                       1
For a nonaffine operator-convex f : (0, ∞) → R, f (1) = 0, the Petz divergence is

                                  Df (ρ∥σ) = ⟨σ 1/2 , f (Lρ Rσ−1 )σ 1/2 ⟩.                           (3)

We will also use the distinct finite divergence
                                      (x − 1)2
                           f△ (x) =            ,           D△ (ρ∥σ) = Df△ (ρ∥σ).                     (4)
                                       x+1
Although (2) and (4) have proportional local forms, they are not the same finite divergence. Nor do
we identify either with the Bures distance or its geodesic contraction.
   For a local channel N , define the complete equal-reference coefficient
                                                                 Df (N (ρ)∥N (σ))
                             ηfc (N ) =            sup                            .                  (5)
                                            |R|<∞, ρ,σ>0             Df (ρ∥σ)
                                          ρ̸=σ, TrA ρ=TrA σ

Define its SLD analogue by optimizing gN   SLD (N (Z))/g SLD (Z) over faithful σ, nonzero Hermitian Z
                                             (σ)          σ
with TrA Z = 0, and all finite R. It is also the coefficient of (2): every such tangent is realized by a
sufficiently small faithful pair.
    These restrictions matter. Actual mutual information compares a state with the product of its
own marginals. Conditional coefficients can instead subtract a divergence between unequal reference
marginals. Fixed-point entropy decay compares a state with a conditional expectation. We do not
replace one optimization by another.


2    Known representation and a cancellation bound
The positive resolvent representation of operator-convex functions, and the resulting representation of
Petz divergences, are established facts; see Hiai–Ruskai [1], Proposition 2.1 and equations (12)–(13).
After removing an affine term, any nonaffine operator-convex f as above has
                                                                  (x − 1)2
                                                            Z
                       f (x) = f ′ (1)(x − 1) + c(x − 1)2 +                dµ(t),                   (6)
                                                             [0,∞) x + t

where c ≥ 0, µ is positive and (1 + t)−1 dµ(t) < ∞. Writing Z = ρ − σ, for states of the same trace
                               R

this gives                                        Z
                      Df (ρ∥σ) = c Tr Z 2 σ −1 +                 ⟨Z, (Lρ + tRσ )−1 Z⟩ dµ(t).         (7)
                                                         [0,∞)
We do not claim this representation as a contribution.
Lemma 1. For positive definite Q, the inverse quadratic form F (Q, Z) = ⟨Z, Q−1 Z⟩ is jointly
convex in Q, Z, for arbitrary complex vectors Z.
Proof. Use the variational identity

                               F (Q, Z) = sup{2 Re⟨Z, Y ⟩ − ⟨Y, QY ⟩}.
                                               Y

Each expression inside the supremum is affine in Q, Z. The same identity also shows that for any
trial Y , with e = Z − QY ,

                            F (Q, Z) = 2 Re⟨Z, Y ⟩ − ⟨Y, QY ⟩ + ⟨e, Q−1 e⟩.                          (8)



                                                          2
Theorem 2 (Harmonic cancellation). Let U1 , . . . , Um be local unitaries, m ≥ 2, and let
                         m                      m
                     1 X                        X                                    X
                E=       AdUj ,          Nw =         wj AdUj ,        wj > 0,           wj = 1.
                     m
                        j=1                     j=1                                  j

For faithful states ρ, σ satisfying E(ρ) = E(σ), and every nonaffine operator-convex f with f (1) = 0,

                                                                              m2
                   Df (Nw (ρ)∥Nw (σ)) ≤ h(w)Df (ρ∥σ),             h(w) = 1 − P −1 .                        (9)
                                                                              j wj

The same h(w) applies for every finite R. It also bounds the SLD metric ratio for tangents Z with
E(Z) = 0.

Proof. For a resolvent term in (7), let Q = Lρ + tRσ , Z = ρ − σ, and write Qj = AdUj Q Ad†Uj ,
Zj = Uj ZUj† . The constraint gives j Zj = 0. For every real a,
                                   P

                                         X                    X        wj − a
                              Nw (Z) =       (wj − a)Zj =         wj          Zj .
                                                                         wj
                                         j                    j
                                    P
Since the output superoperator is j wj Qj , Lemma 1, quadratic homogeneity and unitary covariance
give                                          
                             X                     X (wj − a)2
                         F      wj Qj , Nw (Z) ≤              F (Q, Z).
                                                         wj
                                j                         j

The scalar factor is 1 − 2ma + a2 j wj−1 ; its minimum occurs at a = m/ j wj−1 and equals h(w).
                                    P                                         P
The convex weights here are the positive wj . Negative tangent multipliers do not constitute negative
convex weights on states.
    For the quadratic endpoint in (7), use Q = Rσ ; its inverse quadratic form is Tr Z 2 σ −1 . Integrate
the nonnegative resolvent inequalities. Affine terms vanish by equal traces, and the positive
representation justifies this passage. For the SLD metric, use Q = (Lσ + Rσ )/2 directly. No
argument depends on a bound on |R|.

    Cauchy–Schwarz gives j wj−1 ≥ m2 , so 0 ≤ h(w) < 1. A useful exact control is an involution
                             P

U = U † , U 2 = I, with both eigenspaces nonzero. For E = (id + AdU )/2 and N = w id +(1 − w) AdU ,
the bound is (2w − 1)2 . It is sharp for each of the Petz generators under consideration: take σ = I/n,
a nonzero Hermitian Z connecting the two eigenspaces, and ρϵ = σ + ϵZ. Then N (Z) = (2w − 1)Z,
and the scalar second-order expansion of (3) gives the stated limiting ratio. At w = 1/2, the two
outputs coincide.
Remark 3 (Relative entropy at the boundary). For f (x) = x log x, (9) also holds for nonfaithful
pairs with finite relative entropy. Mix both states with the same maximally mixed state. The
equal-E constraint is preserved. Joint convexity and lower semicontinuity imply convergence of both
finite divergences, and the faithful inequality passes to the limit before division. We do not assert a
boundary extension for every f without specifying its boundary conventions.


3    Exact contraction of every unital qubit channel
                                                          P                              P
For the Pauli matrices Pj , j = 0, x, y, z, write Nw =        j wj AdPj , wj ≥ 0,        j wj = 1. The uniform
Pauli twirl is EA (X) = I2 /2 ⊗ TrA X.

                                                      3
Theorem 4 (Complete unital-qubit classification). The complete equal-reference coefficients of SLD,
χ2min and the finite triangular Petz divergence coincide. For positive Pauli weights their common
value is
                                                       16
                                     h(w) = 1 − P             −1 .                              (10)
                                                   j=0,x,y,z wj

If any Pauli weight is zero, the common value is one. A reference of dimension three suffices for
each supremum. No assertion of minimal reference dimension or of a faithful maximizing pair is
made.
    Consequently, for an arbitrary unital√ qubit CPTP channel with normalized Choi state J =
(N ⊗ id)(|Ω⟩⟨Ω|), |Ω⟩ = (|00⟩ + |11⟩)/ 2, the common value is
                                         (
                                          1 − 16/ Tr(J −1 ), J > 0,
                              η c (N ) =                                                     (11)
                                          1,                 J singular.

For every normalized nonaffine operator-convex Petz generator this is an upper bound. Equality for
each individual generator is not asserted.

Proof. Theorem 2 proves the upper for positive weights. We give the matching lower, including its
faithful realization. Put

           A = w0 + wz , B = wx + wy = 1 − A, u = w0 − wz , v = wx − wy , z = A − B,

               U = u2 /A,       V = v 2 /B,     k = 1 − U − V = 4w0 wz /A + 4wx wy /B > 0.
In the basis (00, 01, 02, 10, 11, 12), let

                                                                              aa∗ + bb∗
               a = (1, 0, 0, 0, e, 0)T ,   b = (0, e, 0, 0, 0, 1)T ,   σe =              ,   e > 0.
                                                                              2(1 + e2 )

Define the real Hermitian tangent by

                     D04 = D40 = 1,        D44 = 2e,       D11 = −2e,     D15 = D51 = −1,

with all other entries zero. Then TrA D = 0, P = 2σe is a projection and (I − P )D(I − P ) = 0. The
support/kernel limit of the SLD form is

                              gσSLD
                                 e
                                    (D) = 4 Tr D2 − 2 Tr(P DP )2 = 16(1 + e2 ).                       (12)

Here and below a boundary form denotes this finite limit, not the ordinary inverse of a singular
matrix.
   The two output blocks on coordinates (0, 4, 2) and (3, 1, 5) are W and JW J, where J reverses
three coordinates and                                             
                                                      A ue 0
                                   M
                           W =             , M = ue e2 ve .
                                2(1 + e2 )
                                                       0 ve B
Their tangent blocks are T and −JT J, with
                                                           
                                                   0 u    0
                                              T = u 2ez −v  .
                                                   0 −v 0


                                                          4
The central Schur complement is e2 k, so both output blocks are positive definite. Let Y = Y T solve
M Y + Y M = 4(1 + e2 )T , and put x = Y12 , y = Y23 , c = eY22 . Eliminating the other three entries
gives

                                          A + e2 (1 − u2 /A − v 2 )          −e2 uv
                                                                                           
       x                  u                                                                   u
   Ke y  = 4(1 + e2 ) −v  , Ke =             −e2 uv            B + e2 (1 − v 2 /B − u2 ) v  .
       c                  z                          u                         v              1

Since det K0 = ABk > 0, the scaled unknowns converge to the nonsingular limiting solution

                  c0 = 4(z − U + V )/k,          x0 = u(4 − c0 )/A,   y0 = v(−4 − c0 )/B.

Both blocks contribute equally to the SLD form. Thus
                           SLD
                          gN         (Nw (D))
                             w (σe )                        (z − U + V )2        16
                   lim                          =U +V +                   = 1 − P −1 .               (13)
                    e↓0      16(1 + e2 )                          k              j wj

The last equality is a rational identity using A + B = 1.
    For each fixed e > 0, replace the input by σe,ξ = (1 − ξ)σe + ξI6 /6, 0 < ξ < 1. The kernel–kernel
tangent vanishes, so its input form tends to (12); the output is already faithful and its inverse is
continuous. Take ξ ↓ 0 before e ↓ 0. Every finite tangent is realized by ρt = σe,ξ + tD for sufficiently
small nonzero real t. For triangular Petz take t → 0 first; its local form is g SLD /2. Minimal chi-square
is exactly quadratic in t. These ordered limits prove all three lower suprema. The uniform-weight
channel has zero output tangent and coefficient zero; no division by that coefficient is used.
    For boundary weights set wj (γ) = (1 − γ)wj + γ/4. Since Nγ = (1 − γ)Nw + γEA , joint convexity
and equal reference give, for each of the three quantities, output at Nγ at most (1 − γ) times output
at Nw . Consequently η c (Nw ) ≥ h(w(γ))/(1 − γ) → 1. The upper one is data processing. Faithful
inputs have faithful outputs under any Pauli mixture.
    Finally use the prior signed singular-value normal form of unital qubit channels [9]: pre/post
unitary conjugations reduce the Bloch matrix to a physical Pauli diagonal map. Both rotations
must lie in SO(3); erasing all singular-value signs is not legitimate. These conjugations preserve
the equal-reference constraint, the three ratios and the normalized Choi spectrum. This proves
(11). The normal-form reduction itself is not new. For the unnormalized Choi matrix Γ = 2J, the
coefficient would instead read 1 − 8/ Tr Γ−1 .


4    The exact stabilization envelope
Let s = ∥T ∥∞ ∈ [0, 1] for the real Bloch matrix of a unital qubit channel. The ordinary coefficient
for these metrics/divergences is s2 , by the prior result of Hiai–Ruskai [1, Theorem 6.1].

Theorem 5. At fixed s, the possible complete coefficients in Theorem 4 fill precisely [s2 , F (s)],
where                              (
                                     3s2 /(1 − 2s), 0 ≤ s ≤ 1/3,
                           F (s) =
                                     1,             1/3 ≤ s ≤ 1.
For s > 0 the ratio between complete and ordinary coefficients is at most nine, and nine is attained
as a ratio of channel coefficient suprema. It is undefined at s = 0, where both coefficients vanish.

Proof. After the signed normal form write T = diag(t1 , t2 , t3 ). The Pauli weights are the four affine
functions (1 ± t1 ± t2 ± t3 )/4 with an even number of minus signs. For s < 1/3, the cube [−s, s]3

                                                        5
                                                                     P
is inside the positive-weight CP tetrahedron. The reciprocal sum S = j 1/wj is convex, so its
maximum occurs at a vertex. The two values there are
                                 4       12               4       12
                          S+ =        +      ,   S− =          +     ,
                               1 + 3s 1 − s             1 − 3s 1 + s
and S− − S+ = 192s3 /[(1 − 9s2 )(1 − s2 )] ≥ 0. Since 1 − 16/S increases with S, the upper is achieved
by T = −sI and equals F (s). For s ≥ 1/3, DPI gives one, achieved by the CP boundary map
diag(−s, −(1 − s)/2, −(1 − s)/2).
    The map diag(−s, 0, 0) realizes the lower s2 . A straight segment to the corresponding upper
example remains CP and keeps norm s. The formula in Theorem 4 extends continuously to the
simplex boundary, with value one there. The intermediate value theorem therefore gives every value
of the interval; no monotonicity along the segment is assumed. Dividing F (s) by s2 proves the
factor-nine statement.

    At T = −I/3, the channel chooses a Pauli axis uniformly, measures it and prepares the opposite
eigenstate. It is therefore entanglement breaking. Nevertheless its complete coefficient is one, while
its ordinary coefficient is 1/9. This does not say that all entanglement-breaking channels have
complete coefficient one, nor that a faithful input attains the supremum exactly.


5    Exact order-constrained depolarization in arbitrary dimension
Let EA (X) = Id /d ⊗ TrA X and Nλ = λ id +(1 − λ)EA , where −1/(d2 − 1) ≤ λ ≤ 1, the known
physical range [8, Section 8.1]. For κ > 1 restrict the finite pairs to
                     ρR = σR ,    ρ, σ > 0,    ρ ̸= σ,     ρ ⪯ κEA (ρ),   σ ⪯ κEA (σ).                (14)
For the metric impose the base order bound and TrA D = 0; one may also require a two-sided small
neighborhood satisfying (14). The suprema proved below are unchanged. The budget uses the
actual reference marginal, not an optimized conditional min-entropy reference.
Proposition 6 (Commuting Bell lower and its range). For every d ≥ 2, 1 < κ ≤ d2 /2 and every
nonaffine operator-convex Petz generator normalized by f (1) = 0, the complete pair coefficient under
(14) is λ2 κ/[1+λ(κ−1)] throughout the physical depolarizing range. The SLD and minimal-chi-square
coefficients have the same value. A reference of dimension d suffices for the lower supremum.
Proof. The order upper is proved below. Write n = d2 , B = In /n, and take two orthogonal
maximally entangled Bell projectors P0 , P1 . For 1 < K < κ ≤ n/2, set
         a = K/n,     b = (1 − 2a)/(n − 2),        σK = bIn + (a − b)(P0 + P1 ),      D = P0 − P1 .
Here a > b > 0, EA (σK ) = B, TrA D = 0, and the actual order constant is K. The input and output
commute; their eigenvalues on the two changed rays are a and aλ = λa + (1 − λ)/n > 0. Hence the
SLD ratio is exactly λ2 a/aλ .
   For 0 < |t| < min(a, b, (κ − K)/n), ρt = σK + tD and σK are faithful with identical reference
and both order bounds. Their Petz divergences are
                 a [f (1 + t/a) + f (1 − t/a)] ,       aλ [f (1 + λt/aλ ) + f (1 − λt/aλ )] .
For a normalized nonaffine operator-convex generator, f ′′ (1) > 0, as follows from the nonzero
positive representation in (6). The Taylor ratio as t → 0 is therefore λ2 a/aλ = λ2 K/[1 + λ(K − 1)].
Then let K ↑ κ. At the endpoint κ = n/2, each earlier base remains faithful. The cases λ = 0, 1 are
immediate. The quadratic chi-square equality follows directly from the metric ratio.

                                                       6
    This is a reparametrization of the Bell family already present in our earlier component work,
not an independent invention of Bell-assisted contraction. In particular, when d ≥ 3, the interval
κ ≤ d + 1 is contained in κ ≤ d2 /2; the rank-d ladder previously considered on that interval is an
alternative proof. A conditional-expectation index alone does not imply sharpness: the pinching
E = (id + AdZ )/2 has index two, but its equal-E contraction is λ2 , rather than the larger raw order
comparison, for 0 < λ < 1.
Theorem 7 (Principal-rich rank-two order profile). For d ≥ 2, set Md = d(2d − 1)/2. For
1 < κ ≤ Md , the complete SLD, minimal-chi-square and finite triangular-Petz contraction coefficients
under (14) equal
                                                   λ2 κ
                                    Cκ (λ) =                .                                    (15)
                                              1 + λ(κ − 1)
The complete supremum is over finite reference systems; a reference of dimension 2d − 1 supplies
the lower. The same expression is an upper for each normalized nonaffine operator-convex Petz
generator, sharp uniformly over that class. Equality for each generator outside the Bell range, or
for every fixed reference dimension, is not asserted.
Proof. For each admissible state, the prior order comparison gives Nλ (σ) ⪰ cσ, where c = λ +
(1 − λ)/κ > 0. Indeed 1 + λ(Md − 1) ≥ d/[2(d2 − 1)] > 0. An equal-reference difference obeys
Nλ (D) = λD. Inverse antitonicity for (Lσ + Rσ )/2, or for Lρ + uRσ using both state budgets, gives
the factor λ2 /c. Include the quadratic endpoint and the positive integral in (7). The new lower,
rather than this comparison machinery, is the point of the construction.
    Put a = d − 1, r = 2a + 1, q = a + e2 , e > 0, and use the reference labels 0, . . . , 2a. Define
                        a−1
                        X                                          a−1
                                                                   X
                 v0 =         |j + 1, j⟩ + e|0, 2a⟩,        v1 =         |j, a + j⟩ + e|d − 1, 2a⟩.
                        j=0                                        j=0

Let b0 = |0, 2a⟩, b1 = |d − 1, 2a⟩, and
                                v0 v0∗ + v1 v1∗
                        σe =                    ,      D = v0 b∗0 + b0 v0∗ − v1 b∗1 − b1 v1∗ .
                                       2q
The supports are disjoint, ∥vi ∥2 = q, and Q = 2σe is a projection. All principal–center cross terms
change the A index. The two diagonal center derivatives cancel in the same reference label. Thus
TrA D = 0.
   The actual reference marginal has mass 1/(2q) on its 2a principal labels and e2 /q on the center.
Consequently Be = EA (σe ) > 0 and

                                [v0 , v1 ]∗ Be−1 [v0 , v1 ]
                                                            = d(a + 1/2)I2 = Md I2 .
                                            2q
This proves that the whitened state has two nonzero eigenvalues Md . Also (I − Q)D(I − Q) = 0; its
boundary SLD form, evaluated spectrally without inverting the singular base, is 16q.
   Set se,p = (1 − p)Be + pσe . Each support has an invariant plane spanned by its uniform principal
vector and center coordinate. In orthonormal coordinates the two base blocks are
                                                 √                 √ 
                                 1     Ap     dpe a               0    a
                        Wp =             √           2 , T =     √        ,                     (16)
                                2dq  dpe   a   C p e               a  2e

where Ap = 1 + (da − 1)p, Cp = 2 + (d − 2)p; the tangent blocks are T, −T . Each support has a − 1
additional principal modes with eigenvalue (1 − p)/(2dq) and zero tangent. Outside these supports

                                                           7
the remaining d(2d − 1) − 2d coordinates are diagonal replacement modes with zero tangent. This
accounts for the full dimension. The aligned determinant is

                          e2 (1 − p)[1 + (Md − 1)p]
                                                                            
                                                                  1
                det Wp =                            >0        −        <p<1 .
                                     2d2 q 2                    Md − 1

Both p = θ and p = λθ lie in this domain for 0 < θ < 1 and the entire physical range of λ.
   For Wp Y + Y Wp = 2T , the two-dimensional identity

                                          T + det(Wp )Wp−1 T Wp−1
                                    Y =
                                                  Tr Wp

follows by Cayley–Hamilton and direct substitution. Inserting (16) and taking the limit at fixed
admissible p gives
                                                   8aMd
                               lim Tr(T Y ) =                .                               (17)
                                e↓0           1 + (Md − 1)p
The full ambient SLD form is twice this quantity. At fixed θ < 1, its retention therefore tends to
λ2 [1 + (Md − 1)θ]/[1 + λ(Md − 1)θ].
     Choose 0 < θ < (κ − 1)/(Md − 1). Both se,θ and κBe − se,θ are positive definite, so sufficiently
small bilateral perturbations ρt = se,θ + tD preserve faithfulness, the actual marginal and both
budgets. For triangular divergence take t → 0 first; for minimal chi-square the ratio is exactly
quadratic. Then take e ↓ 0 at fixed θ, finally θ ↑ (κ − 1)/(Md − 1). This reaches (15) as a supremum.
The endpoints λ = 0, 1 are immediate. No exchange of singular limits or finite faithful maximizer is
needed.

    The earlier rank-two allocation achieved the smaller cap Ld = d(d+1)/2 with reference dimension
d + 1. The principal-rich allocation raises the cap by d(d − 2)/2, at the cost of reference dimension
2d − 1; for d = 2 they coincide. This is a development of the same mechanism, not an independently
invented theory or a free reference-size improvement.
Remark 8 (The empty endpoint and the domain of the order bound). At κ = 1, positivity and
equal traces force ρ = EA (ρ) and σ = EA (σ); equal reference then forces equality. There are no
distinct finite pairs, so (15) is not assigned to that empty optimization. The base-only SLD problem
with unrestricted tangents at a product base is a different problem. Likewise the expression λ2 /c
must never be used when c ≤ 0; for example λ = −1/3, κ = 5 gives a negative raw expression in
dimension two, not a contraction bound.


6    Exact qubit resource restrictions
For d = 2, Theorems 4 and 7 combine to give, for every κ > 1,

                                 λ2 K
                  Cκ (λ) =                ,     K = min(κ, 3),      −1/3 ≤ λ ≤ 1.
                             1 + λ(K − 1)

For κ ≥ 3, the upper is the unrestricted isotropic case of Theorem 4, 3λ2 /(1 + 2λ); the same lower
family has order arbitrarily close to three. At the channel endpoints use DPI or the identity directly.
   For a qubit and any finite reference,

                                 2EA (σ) − σ = (σy ⊗ I)σ TA (σy ⊗ I).


                                                  8
Thus PPT bases obey the order-two bound, as do separable bases. The exact complete SLD/minimal-
chi-square/triangular coefficient restricted to PPT or separable models is 2λ2 /(1 + λ). For finite
Petz both states must belong to the class. To prove the matching lower, use the qubit ladder above
(equivalent under a local basis swap to the earlier allocation) with se,θ and θ < 1/2. Its partial
transpose has two blocks with determinant e2 (1−θ −2θ2 )/[8(1+e2 )2 ] > 0 and two positive singletons.
Small bilateral perturbations stay PPT. In dimension 2×3, the prior Horodecki theorem [10] converts
these pairs to separable ones. This uses PPT=SEP only for the lower in 2 × 3, not for arbitrary
references or larger local dimensions.
    For each normalized nonaffine operator-convex Petz generator, the SEP/PPT pair coefficient
is also exactly 2λ2 /(1 + λ). Indeed, the order-two comparison gives the upper, while the qubit
Bell family of Proposition 6, with K < 2, has all Bell probabilities pj strictly below 1/2. The
partial-transpose eigenvalues are 1/2 − pj . Both the base and sufficiently small finite perturbations
are strictly PPT, hence separable in 2 × 2, and approach the stated lower. The same gives the
budget profile inside SEP/PPT for 1 < κ ≤ 2. This restricted-pair statement includes Umegaki but
does not determine the unrestricted coefficient or actual MI, whose second state has an additional
product-marginal requirement.
    A classical-reference family has both states and the tangent block diagonal in one fixed reference
basis, with fixed marginal weights. The forms split into weighted ordinary-qubit forms, whose
coefficient is λ2 by [1]; R = 1 gives equality. Classicality of the base alone is insufficient. For
example at λ = −1/3, the classical base σ = diag(9, 1, 1, 9)/20 with D03 = D30 = 1 gives retention
3/11 > 1/9; the direction creates reference coherences.
    At λ = −1/3 the exact levels are therefore
                                1                     1
    classical-reference family : ,    SEP/PPT family : ,              unrestricted quantum family : 1.
                                9                     3
SLD retention (or minimal-chi-square retention with base σ) above 2λ2 /(1 + λ) is a sufficient
certificate that the input base is NPT. For a general finite Petz pair, the proved implication is only
that exceeding this threshold excludes both input states being PPT; it does not identify which state
is NPT. This mathematical implication is a contrapositive of the prior reduction criterion plus the
quantitative upper; it is not an experimentally demonstrated protocol.


7     A complete equal-reference relative-entropy lower bound
Write Pd = d(d − 1), distinct from Md = d(2d − 1)/2. Define

                  gsBKM (D) = Tr D D(log)s [D],          DU (ρ∥σ) = Tr ρ(log ρ − log σ).

Their complete equal-reference coefficients use exactly the state/tangent restrictions of Section 1.
They do not optimize actual mutual information. The BKM kernel, faithful local expansion and
relative-entropy/BKM comparison mechanisms are prior [1, 4, 12].
Theorem 9 (Principal-rich BKM and Umegaki lower). For depolarization on dimension d ≥ 2
throughout its physical range,
                              c                             c
                             ηBKM (Nλ ) ≥ CPd (λ),         ηU (Nλ ) ≥ CPd (λ).

With both actual-marginal order budgets at κ > 1, put
                                                                         
                                                                 κ−1
                               K∗ (κ) = 1 + (Pd − 1) min                ,1 .
                                                                 Md − 1

                                                     9
Both constrained coefficients are at least
                                  max{Cmin(κ,d2 /2) (λ), CK∗ (κ) (λ)}.
These are lower bounds, not proposed exact optima. The second construction uses a reference of
dimension 2d − 1.
Proof. Use the bases and tangent in (16). Let w+ ≥ w− > 0 be the eigenvalues of Wp , and Z the
matrix of T in that eigenbasis. At fixed −1/(Md − 1) < p < 1,
                        Ap                       (1 − p)[1 + (Md − 1)p] 2
                 w+ =       + O(e2 ),        w− =                       e + O(e4 ).
                        2da                               daAp
                                                                         √
The leading coefficient of w− is positive. The eigenvector rotation is dp a e/Ap + O(e3 ), whence
                    2dpa                          2(1 − p)                        √
            Z++ =        e + O(e3 ),      Z−− =            e + O(e3 ),    Z+− =       a + O(e2 ).
                     Ap                              Ap
The BKM form for one plane is
                                     2   Z2
                                    Z++                 log w+ − log w−
                         He (p) =       + −− + 2|Z+− |2                 .
                                    w+    w−                w+ − w −
The diagonal terms are bounded, whereas the logarithmic term yields
                                              8da2
                              He (p) =                  log(1/e) + O(1).                            (18)
                                          1 + (Pd − 1)p
The full form is 2He (p); all remaining modes have zero tangent. Therefore, with θ < 1 fixed,
                                          He (λθ)       1 + (Pd − 1)θ
                                 lim λ2           = λ2                .
                                 e↓0      He (θ)       1 + λ(Pd − 1)θ
Taking θ ↑ 1 gives the unrestricted lower; taking it up to the budget endpoint gives CK∗ . The
domain also contains the negative physical endpoint. The cases λ = 0, 1 are direct. No uniform
remainder in θ ↑ 1 is asserted.
   For each fixed faithful e, θ, choose the same admissible small perturbations as in Theorem 7.
The prior local identity is
                             DU (se,θ + tD∥se,θ ) = 21 t2 gsBKM
                                                             e,θ
                                                                 (D) + o(t2 ).
Take t → 0 first, then e ↓ 0, then θ to its allowed endpoint. This proves the finite-pair lower in the
stated orientation. The first bound inside the maximum follows from the Bell family of Proposition 6,
since x log x is operator convex; for larger budgets retain its endpoint lower by approximation from
below. It can be stronger than CK∗ at smaller budgets and must not be discarded.

   For d ≥ 3, Pd > d2 /2 and ∂K CK = λ2 (1 − λ)/[1 + λ(K − 1)]2 . Thus, except at λ = 0, 1, the new
unrestricted lower strictly exceeds the endpoint supplied by the specific preceding Bell family. At
the negative physical endpoint this reads
                                                               
                               1          1                   1           1
                     CPd − 2          =      ,     Cd2 /2 − 2       = 2       .
                             d −1       d+1                d −1        d −1
The ratio of these two lower bounds is d − 1. This dimension-dependent comparison is not a claim
of a worldwide-best bound, an exact coefficient or an operational advantage. For d = 2, Pd = 2: it
recovers the Bell lower and does not settle unrestricted qubit relative-entropy contraction.

                                                    10
Finite certified comparisons. For e = 10−30 , t = 10−90 , θ = 99/100, the actual finite pairs
above, with budget Md , yield the following rigorous interval locations of their gaps over the specified
Bell endpoint:

                        d      λ      gap interval (outward decimal bounds)
                        3    −1/8    (0.11255711780015, 0.11255711780017)
                        3     1/2    (0.00593846351695, 0.00593846351696)
                        4    −1/15   (0.11934942272408, 0.11934942272410)
                        4     1/2    (0.00238915978275, 0.00238915978276)

The exact binary/rational interval endpoints, rather than rounded midpoints, are retained in the
supplement. Audit1044 reproduced positivity and both budgets exactly, and enclosed all four
calculations with a separate integer interval implementation. Subblocks must not be normalized
separately: their opposite linear trace terms cancel only in the global divergence. The input
divergences are of order 10−177 , with cancelling block terms of order 10−120 . Such severe conditioning
precludes an inference of laboratory robustness from these mathematical certificates.


8    A localized Doeblin counterexample
We record a discrepancy in a specific printed statement, rather than infer a failure of the surrounding
theory. In the convention of George et al. [3, Definition 4, Eq. (3.1)], the ordinary quantum Doeblin
coefficient has the primal form

                            α(N ) = sup{Tr X : X = X † , IA ⊗ X ⪯ ΓN
                                                                   AB },

where Γ is the unnormalized Choi matrix. Its dual in Proposition 3 admits Y ⪰ 0 with TrA Y = IB ,
minimizing Tr ΓY . Requiring X ⪰ 0 instead defines the different coefficient α+ of Definition 7,
Eq. (3.25); the two optimization problems must not be identified.
    Consider N = (id + AdX + AdY )/3. Its Bloch matrix is diag(1, 1, −1)/3, so its ordinary trace-
distance contraction coefficient is exactly 1/3. Direct calculation gives
                                  2    1
                               Γ = I4 − vv ∗ ,         v = (1, 0, 0, −1)T .
                                  3    3
The primal X = 0 is feasible. The dual Y = vv ∗ is positive, satisfies TrA Y = I2 , and gives
Tr ΓY = 0. Weak duality therefore already proves α(N ) = 0. This contradicts the equivalence
between positive Doeblin coefficient and strict ordinary trace contraction in Theorem 5 as printed
in arXiv:2503.22823v3 and the checked journal PDF. It does not contradict the usual one-sided
Doeblin upper bound or turn ordinary trace contraction into the complete SLD coefficient. The
four-dimensional primal/dual certificate is logically separate from Theorem 4. We do not claim a
global review of that article, priority for the observation, or that no correction exists elsewhere.


9    Finite evidence, adverse controls and operational limits
The proofs above, rather than numerical optimization, establish the proposed universal statements.
The associated evidence separates exact symbolic identities, rational finite-pair certificates, bounded
numerical searches and model-assisted proof inspection. Component audit1012 reconstructed the
Pauli blocks, faithful limits, order profile and envelope; it checked the supplied qubit rational pairs


                                                  11
through full Sylvester systems and added a finite triangular pair with retention above 0.999997 for
the entanglement-breaking channel at −I/3. Its base has an eigenvalue 1/(6 · 1018 ); this proves
neither a uniform usable parameter interval nor robustness to preparation errors. A factor-nine
ratio of coefficient suprema must not be described as a faithful finite-pair maximum.
    The audit preserves three unsuccessful optimizer terminations and an approximately 6.3 ·
10−13 numerical bound excess whose separate recalc changes sign. That discrepancy is not a
certified counterexample. The discovery optimizer was not restarted to obtain a favorable result.
Public controls include negative parameters, Choi-normalization checks and complex noncommuting
resolvent orientation tests. Bounded passing tests are not a universal numerical or priority certificate.
    Some tempting literal extensions are false. Without centering f (1), the generator f (x) =
(x − 1)2 /(x + 1) + 1, input ρ = diag(3/4, 1/4), σ = I2 /2 and λ = 0 give ratio 15/17, not zero. The
requirement f (1) = 0 is substantive. The negative raw order bound and classical-base-only shortcut
were excluded explicitly above. The original rational certificate refuting an auxiliary factor-two
conditional-variance bound is also retained; it does not settle the Umegaki coefficient.

No unitary-encoding interpretation of the displayed lower. Let Qi project onto one ladder
support block. It commutes with the base and its replacement mixture, but Tr Qi D = ±2e =      ̸ 0.
For every Hermitian H, Tr Qi (−i[H, σ]) = −i Tr([σ, Qi ]H) = 0. Thus this tangent is not a
unitary-encoding direction even for a global Hamiltonian. This rules out that interpretation of our
construction, not all other unitary families or known ancilla advantages.
    The NPT implication in Section 6 would require an output-QFI lower and an input-QFI upper
obtained without assuming the entanglement conclusion. Two observed classical Fisher informations
do not supply those two directions of inequality. Full tomography already permits a direct PPT test.
No noncircular experimental advantage, fixed-Hamiltonian optimum, capacity or quantum-error-
correction protocol is established here. Neither an order between metrics nor local SLD exactness
determines a BKM, Umegaki or actual-mutual-information coefficient. For the earlier center-rich
rank-two tangent at fixed θ, audit1025 finds the BKM limit

                                                 1 + (d − 1)θ
                                           λ2                 ,
                                                1 + (d − 1)λθ

which is strictly below its SLD limit when 0 < λ < 1 and θ > 0. This refutes automatic transfer for
this tangent; it is not an upper bound on the optimized BKM coefficient.

Evidence availability. The published first version [13] and its exact-PDF report remain im-
mutable. The version-pinned component supplement contains the complete1012 report, verdict, con-
trols, source-reading scopes and incidents. Its TRANSPORT1019.json separates original C/D hashes
from LF repository hashes; embedded original manifests describe the original dossiers. The public1017
construction in that snapshot is an earlier, weaker general-dimensional candidate, not the principal-
rich range in Theorem 7. The earlier rank-two cap has a separate frozen1021 proof and exact controls,
technically examined in audit1025 together with the Bell/SEP synthesis1024. The immutable ex-
panded supplement contains the full1018/1025 technical reports, selected controls, both proofs and a
portable bundle of five fixed symbolic/rational checks. All65 source-head files checked, including the
unchanged canonical graph files, matched their remote bytes. The repository-transport bundle mani-
fest has SHA256 73b09af49fc3155f02c5e80e53489d258404ba9e47951f75b172e428743b877a. In-
stall bundle/requirements.txt and run python bundle/replay.py --workdir ./runs --out
./receipt.json. The tested runtime was Python3.12.14 with SymPy1.14.0; all five replayed out-
puts matched their expected parsed JSON. The first public-tree replay stopped before computation


                                                    12
because LF transport changed a metadata hash. The original manifest contents, explicit transport re-
binding and incident are preserved. These fixed controls are not a certified computational-campaign
capsule, formal proof or novelty certificate.


10     Prior work and remaining questions
The resolvent representation, inverse-quadratic convexity and ordinary unital-qubit coefficient are
prior [1]. Signed Bloch normal form and local-unitary Choi covariance are prior [9]. The 2 × 3 PPT
criterion used in the separable lower is prior [10]; it is not extended to higher-dimensional bipartitions.
Cao–Lu [2] study chi-square contraction and tensorization with stated product-reference hypotheses.
Hirche–Rouzé–Stilck França [8] develop channel orders, generalized contraction and Weyl-covariant
comparisons; Section 8.1 also records the full physical depolarizing range. These are relevant prior
tools, not new consequences of the present formulas. George–Tomamichel [7] give fixed-base and
ordinary optimized spectral methods. Neither optimization should be silently identified with a
complete equal-reference optimization over arbitrary correlated bases. The unrestricted coefficient
of N ⊗ idR can instead be one simply because a direction is stored in R.
    Gao–Zhao [6] study relative entropy to a conditional expectation, order/index parameters and
index witnesses. Those constructions and the order-comparison machinery are close prior tools.
Theorem 7 concerns two faithful equal-reference states, their individual actual-marginal order
budgets and the specified SLD/triangular quantities. A source covering those same quantifiers
would affect novelty; selected reading does not certify its absence. Belzig et al. [4, Section 4.1,
Lemma 4.1] prove the prior ordinary relative-entropy/BKM equivalence; Han–Li [12, Section 2.2,
Lemma 1] use and attribute it. Their statements must not be repackaged as our discovery. The
faithful segment/local method preserves the present convex budget class, but does not compute its
optimum. Hirche et al. [5] further distinguish reference-assisted information quantities.
    Ancilla-assisted metrology under depolarization is prior; Chapeau-Blondeau [11] considers
unitary-phase probe families. Our nonunitary state model is not a claimed improvement over
such protocols. The bibliographic comparison has been directed, with abstract-only access for one
additional2017 metrology source and selected primary passages for the cited2018 work. It is not an
exhaustive audit of frontier literature or a worldwide originality certificate.
    Theorem 9 supplies lower bounds but no matching general BKM upper. The unrestricted
higher-dimensional coefficient, optimal range beyond Md , minimal sufficient reference dimension,
nonunital classification, unrestricted BKM/Umegaki and actual-MI coefficients, tensorization and
practical robustness remain open in this manuscript. Proposition 6 gives generator-specific equality
only in its stated budget range; it is not transferred to the larger rank-two range. The qubit
classification and order-budget results belong to one evolving contraction problem; we do not count
each corollary or adverse control as a separate paper.

New component evidence. The version-pinned supplement contains the 1033/1035 derivations,
fixed replay scripts and original interval certificates with transport hashes. Technical audit1044
separately reconstructed the geometry, logarithmic coefficient and ordered limits; solved an ambient
rational225-by225 Sylvester system; checked Umegaki orientation without normalizing subblocks; and
verified four finite gaps using directed integer intervals. Its full report, controls, incidents and primary-
reading scope are retained with the working dossier and must accompany any later publication. The
original interval solver and this separate implementation support bounded certificates, not universal
numerical or novelty claims. The frozen1037 grid found no violation of a hypothetical upper in270
fixed points; that inconclusive diagnostic supplies no upper and is not used in a proof.


                                                     13
11     Model assessments and review context
The named author directed substantial OpenAI Codex assistance in derivation, writing and numerical
work. Full review1031 and corrective continuation1042 examined the predecessor drafts; both reports,
all objections and their exact-PDF hashes are retained. Their scores do not evaluate this expanded
combined manuscript. Technical audits1018/1025 and1044 were requested as GPT-6 Astra xhigh,
with reused conversational context and a shared filesystem. Effective model identity, effort, runtime
isolation, blinding and independence are unattested. No independent second voice or human peer
review is claimed.
    Audit1044 supports the principal-rich exact SLD/minimal-chi-square/triangular range and the
separate BKM/Umegaki lower, with the distinction between M and P, complete versus fixed-reference
quantifiers, increased reference cost and no unitary-tangent interpretation preserved. It supplies no
manuscript grade or editorial recommendation. Its directed prior-art comparisons do not certify
priority. A full exact-PDF assessment of this combined version has not been obtained at freezing; no
predicted score, Lean proof of the analytic theorems or worldwide originality certificate is claimed.
Publication as a Working paper would not constitute editorial acceptance. The author remains
responsible for attribution and claims.




                                                 14
References
 [1] F. Hiai and M. B. Ruskai, Contraction coefficients for noisy quantum channels, arXiv:1508.03551v1
     (2015). https://arxiv.org/abs/1508.03551v1.
 [2] Y. Cao and J. Lu, Tensorization of the strong data processing inequality for quantum chi-square
     divergences, Quantum 3, 199 (2019). https://doi.org/10.22331/q-2019-10-28-199.
 [3] I. George, C. Hirche, T. Nuradha and M. M. Wilde, Quantum Doeblin Coefficients: Interpretations and
     Applications, Quantum 10, 2115 (2026), arXiv:2503.22823v3. https://arxiv.org/abs/2503.22823v3.
 [4] P. Belzig, L. Gao, G. Smith and P. Wu, Reverse-type Data Processing Inequality, arXiv:2411.19890v3
     (2025). https://arxiv.org/abs/2411.19890v3.
 [5] C. Hirche, I. George, T. Nuradha and M. M. Wilde, Conditional contraction coefficients and their
     applications to quantum networks, arXiv:2608.27171v1 (2026). https://arxiv.org/abs/2608.27171v1.
 [6] L. Gao and L. Zhao, Tight Entropy Contraction of Generalized Quantum Depolarization,
     arXiv:2608.19685v1 (2026). https://arxiv.org/abs/2608.19685v1.
 [7] I. George and M. Tomamichel, A Unified Approach to Quantum Contraction and Correlation Coefficients,
     arXiv:2505.15281v3 (2026). https://arxiv.org/abs/2505.15281v3.
 [8] C. Hirche, C. Rouzé and D. Stilck França, On contraction coefficients, partial orders and approximation
     of capacities for quantum channels, Quantum 6,862 (2022),arXiv:2011.05949v4. https://arxiv.org/
     abs/2011.05949v4.
 [9] M. B. Ruskai, S. Szarek and E. Werner, An Analysis of Completely-Positive Trace-Preserving Maps on
     2 × 2 Matrices, arXiv:quant-ph/0101003v2. https://arxiv.org/abs/quant-ph/0101003v2.
[10] M. Horodecki, P. Horodecki and R. Horodecki, Separability of mixed states: necessary and sufficient
     conditions, arXiv:quant-ph/9605038v2. https://arxiv.org/abs/quant-ph/9605038v2.
[11] F. Chapeau-Blondeau, Optimized entanglement for quantum parameter estimation from noisy qubits,
     International Journal of Quantum Information 16,1850056 (2018), primary preprint arXiv:1904.01904v1.
     https://arxiv.org/abs/1904.01904v1.
[12] J. Han and Y. Li, Convergence Analysis of the Quantum Blahut-Arimoto Algorithm and the Contraction
     Coefficient of Qubit Amplitude-Damping Channels, arXiv:2610.29373v1 (2026). https://arxiv.org/
     abs/2610.29373v1.
[13] L. Eriksson, Sharp reference-assisted contraction for the minimal quantum Fisher met-
     ric, AIRR.SCIENCE,ARR-2026-77DGRYDGXD8MDSY2,v1 (2026),Working paper. https://airr.
     science/papers/ARR-2026-77DGRYDGXD8MDSY2/versions/v1/.




                                                     15
