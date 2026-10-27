# Quantum reference activation of classical symmetric channels

Rendition of canonical12-page paper.pdf, SHA256 3a08346e76b1a168aa3759921ae336aa6d97bd739eb61f8b42fa800b3b18f783.

    Quantum reference activation of classical symmetric channels
                                             Lluis Eriksson

                                            27 October 2026


                                                 Abstract
         We determine the complete equal-reference contraction coefficients of a classical symmetric
     channel with an arbitrary finite quantum reference. For an alphabet of size n and stochastic
     parameter −1/(n−1) ≤ λ ≤ 1, the coefficients for the SLD metric, minimal chi-square divergence,
     triangular Petz divergence, BKM metric and Umegaki relative entropy equal (n−1)λ2 /[1+(n−2)λ].
     A cyclic harmonic bound supplies the upper estimate and a separable classical–quantum simplex
     supplies matching faithful limits. The ordinary classical coefficient is nλ2 /[2 + (n − 2)λ]. Every
     restriction to two input symbols retains that ordinary coefficient even with a quantum reference,
     so classical binary-support reduction fails in the complete setting. At the exclusion endpoint,
     the complete coefficient is one although every two-symbol restriction has coefficient 1/(n − 1).
     A family of actual binary measurements, controlled by the classical output, witnesses near-
     unit retention for a fixed three-symbol channel and a fixed three-dimensional reference. Input,
     quantum output and measured output relative entropies all tend to log 2. Conditioning grows
     exponentially and the useful probabilities become rare; no robust communication or capacity
     advantage is claimed. Adverse finite examples and review-context limitations are retained.


1    Problem and relation to prior work
A classical noisy channel acts on probability distributions, but its input may be correlated with a
quantum memory that remains available after transmission. The relevant comparison is then between
two joint states with the same memory marginal. This constraint rules out the trivial strategy
of putting all distinguishing information in an untouched memory. It still permits noncommuting
conditional memory states, even when the input and memory are separable.
    For ordinary classical strong data processing, optimizing over a large input alphabet can be
reduced to a pair of input symbols, by Ordentlich and Polyanskiy [3]. Our question is whether
that reduction remains valid when the unchanged reference is quantum. We answer it for a full
symmetric channel family: two-symbol restrictions obey their ordinary classical bound, whereas the
complete alphabet can do strictly better.
    The definitions of complete and conditional contraction coefficients are prior; we use the
equal-reference complete convention described by Hirche, George, Nuradha and Wilde [5]. Their
characterization using a binary hypothesis label is distinct from restricting the input alphabet to
two symbols. We do not claim a new correspondence between divergence and reference-assisted
information measures. Hiai and Ruskai [1] provide the operator-convex divergence and metric
framework. Classical equivalence of global contraction coefficients is treated by Makur and Zheng [2].
The classical symmetric-channel formula below is a benchmark, not a novelty claim; Lee and
Makur [4] is an additional relevant classical reference whose full proof has not been inspected in our
directed audit.
    Complete entropy decay toward a conditional expectation [6, 7] uses a different restriction on the
second state. Those estimates do not automatically bound two arbitrary correlated hypotheses with

                                                     1
equal reference. Conversely, our pair constructions do not contradict decay toward a fixed-point
state. Recent asymptotic contraction bounds for primitive channels with a fixed faithful stationary
state [9] concern that different quantifier regime. The source-fixed matrix-Φ framework of Wang
and Gohari [8] is also distinct; we do not claim to resolve its open questions. Generic failure of strict
one-step contraction, even for primitive classical channels, already appears in Cohen et al. [10]. The
issue studied here is the exact complete coefficient and the quantum-reference enhancement of a
classical channel whose ordinary coefficient is strictly below one. Our literature search is directed
and does not certify worldwide priority.


2    Definitions and a harmonic upper bound
Let A = Cn be equipped with its stated classical basis, and define
                                                  1−λ                 1
                           Kλ (y | x) = λδxy +        ,          −       ≤ λ ≤ 1.                     (1)
                                                   n                 n−1
The quantum channel Nλ first dephases A in this basis and then applies Kλ to its diagonal. It is
not the quantum depolarizing channel on arbitrary coherences. We suppress idR from notation.
   For a divergence Q, write

                                c                                Q(N ρ∥N σ)
                               ηQ (N ) =           sup                      .                         (2)
                                             dim R<∞, ρ,σ>0       Q(ρ∥σ)
                                           Tr ρ=Tr σ=1, ρR =σR
                                               0<Q(ρ∥σ)<∞

The supremum is over faithful normalized states; no faithful maximizer is asserted. The ordinary
coefficient omits R. All logarithms are natural.
   For operator-convex f : (0, ∞) → R with f (1) = 0, the Petz divergence is

                                  Qf (ρ∥σ) = ⟨σ 1/2 , f (Lρ Rσ−1 )σ 1/2 ⟩HS .                         (3)

Here La X = aX, Rb X = Xb and ⟨X, Y ⟩HS = Tr X ∗ Y . The relevant generators include f (t) = t log t
and f△ (t) = (t − 1)2 /(t + 1). We distinguish Qf△ from the finite minimal chi-square divergence

                     χ2min (ρ, σ) = ⟨ρ − σ, Jσ−1 (ρ − σ)⟩HS ,         Jσ = (Lσ + Rσ )/2.

The SLD metric uses the same quadratic form on a Hermitian tangent D. The BKM metric uses the
derivative of the matrix logarithm. Complete metric coefficients optimize over faithful base states
and nonzero tangents with TrA D = 0; normalization factors common to input and output cancel.

Lemma 2.1 (Cyclic harmonic cancellation). Let Tj , 0 ≤ j < n, be the cyclic permutations of a
classical register, amplified by an identity on a finite reference. Suppose j Tj (ρ −σ) = 0 and wj > 0,
                                                                           P
P                           P
   j wj = 1. The channel       j wj Tj contracts every normalized operator-convex Petz divergence by at
most
                                                            n2
                                            h(w) = 1 − P −1 .
                                                           j wj

The same bound holds for the SLD and BKM metrics on tangents annihilated by the uniform twirl.

Proof. For the resolvent generator gu (t) = (t − 1)2 /(t + u), u ≥ 0, put Z = ρ − σ and Ω = Lρ + uRσ .
Set Zj = Tj Z and Ωj = Tj ΩTj∗ . They satisfy j Zj = 0 and ⟨Zj , Ω−1   j Zj ⟩ = q, independent of j. For
                                               P



                                                      2
                                                 j (wj − c)Zj . The inverse quadratic-form inequality gives
                                             P
any real c, the output difference is
                  *                                   −1                        +
                      X                      X               X                            X (wj − c)2
                          (wj − c)Zj ,          wj Ωj              (wj − c)Zj       ≤                    q.
                      j                      j                   j                        j
                                                                                                  wj

One proof minimizes j ⟨Yj , (wj Ωj )−1 Yj ⟩ subject to a fixed sum j Yj , and substitutes Yj =
                            P                                                                 P

(wj − c)Zj . Minimizing the scalar coefficient over c gives c = n/ j wj−1 and h(w).
                                                                  P

    All operators act on the full complex Hilbert–Schmidt space. In column vectorization Rσ
contains σ T , with no assumption that the states are real or commuting. The positive integral
representation [1]
                                                                   (t − 1)2
                                                             Z
                      f (t) = a(t − 1) + b(t − 1)2 +                        dµ(u),                b ≥ 0,
                                                              [0,∞) t + u

transfers this upper bound to every such f , with µ positive and (1 + u)−1 dµ(u) < ∞. The affine
                                                                                      R

part cancels by equal traces. The quadratic endpoint is proved by the same argument with Ω = Rσ ,
so it is not discarded. Positivity of the measure justifies the integration. Local expansion of the
triangular and Umegaki cases gives the metric bounds.

   For CQ states, j Tj (ρ − σ) = 0 is exactly the equal-reference constraint. The channel (1) is a
                      P

mixture of cyclic shifts with
                                        1 + (n − 1)λ                        1−λ
                                w0 =                 ,               wj =             (j ̸= 0).
                                             n                               n
The lemma therefore gives
                                                              (n − 1)λ2
                                                 Hn (λ) =                .                                      (4)
                                                            1 + (n − 2)λ
At the two stochastic endpoints a weight may vanish. We use ordinary data processing to obtain
the upper bound one, not a singular evaluation of 1/wj . At λ = 0 the output difference vanishes
exactly. Dephasing before the cyclic mixture preserves the common reference and cannot increase
the input divergence, so the upper applies to general quantum inputs as well.


3    Exact complete coefficients
Theorem 3.1. For every n ≥ 2 and physical λ in (1), the complete coefficients for SLD, χ2min , Qf△ ,
BKM and Umegaki relative entropy are all Hn (λ). A reference of dimension n suffices for their
suprema. For every normalized nonaffine operator-convex Petz generator, Hn is an upper bound;
equality for every generator is not asserted.
Proof. Only matching lower bounds remain. In R = Cn put

                             u = (1, . . . , 1)T ,   P = I − uu∗ /n,          vi = ei − u/n.
                          2 = (n − 1)/n and P v v ∗ = P . Define the CQ blocks
        i vi = 0, ∥vi ∥
       P
Then                                         i i i

                          vi vi∗
                 σi =            ,      Di = uvi∗ + vi u∗ ,            σ = diagi σi ,         D = diagi Di .
                          n−1
They give Tr σ = 1, TrA σ = P/(n − 1) and TrA D = 0. Use the common faithful regularization

                                     σξ = (1 − ξ)σ + ξIn2 /n2 ,              0 < ξ < 1.

                                                             3
Its actual reference marginal is (1 − ξ)P/(n − 1) + ξIn /n. In the plane spanned by vi and u, the
block eigenvalues and tangent coherence are
                               1−ξ   ξ                  ξ                         √
                          α=       + 2,         β=         ,       |(Di )12 | =       n − 1.
                                n   n                   n2
The output preserves β, replaces α by

                                           (1 − ξ)[1 + (n − 2)λ]   ξ
                                    α′ =                         + 2,                                   (5)
                                                 n(n − 1)         n

and replaces D by λD. Therefore the SLD ratio is
                                            α+β
                                 Rξ = λ2           −→ Hn (λ)             (ξ ↓ 0).                       (6)
                                            α′ + β

Indeed gσξ (D) = 4n(n − 1)/(α + β). The finite pair ρ = σξ + tD, σ = σξ realizes the same ratio for
minimal chi-square whenever t ̸= 0 is sufficiently small.
   For the triangular divergence choose ρ± = σξ ± tD, where t2 (n − 1) < αβ. These are faithful
normalized states with identical reference. To evaluate a subnormalized active block, write W± =
diag(a, b) ± cS, where S = ( 01 10 ). Then W+ S + SW− = (a + b)S, so

                                                      2c                                        8c2
                (LW+ + RW− )−1 (W+ − W− ) =              S,             Qf△ (W+ ∥W− ) =             .
                                                     a+b                                       a+b
          √
With c = t n − 1 this gives 8t2 (n−1)/(α+β) per input block. At output the coherence is multiplied
by λ and the denominator is α′ + β, so the exact finite ratio is again (6). Positivity also follows from

                                    (1 − ξ)(1 − λ)[1 + (n − 1)λ]
                     α ′ − λ2 α =                                + β(1 − λ2 ) ≥ 0.
                                              n(n − 1)

No active plane is renormalized or postselected.
   For BKM put ℓ(a, b) = (log a − log b)/(a − b), with its continuous extension. The local ratio is

                                                     ℓ(α′ , β)
                                                λ2             .
                                                     ℓ(α, β)

At fixed n, λ, the two first arguments tend to positive constants and β ↓ 0. Their common divergent
logarithm cancels, leaving Hn (λ). For finite Umegaki, first take t → 0 in

                                D(σξ + tD∥σξ ) = 12 t2 gσBKM
                                                          ξ
                                                             (D) + o(t2 )

with ξ fixed, and only then take ξ ↓ 0. This produces faithful finite pairs arbitrarily close to the
same coefficient. Singular inverses and an interchange of limits are not needed.

   These preparations are CQ and therefore separable across A : R. Their conditional reference
blocks generally do not commute. If the reference were classical in one common basis for both
hypotheses, the divergence would decompose into classical terms and the ordinary coefficient would
bound each term. The advantage concerns quantum correlations without requiring entanglement.




                                                       4
4    Why two input symbols no longer suffice
We include the binary upper argument to identify exactly the boundary crossed by Theorem 3.1.
Proposition 4.1. Let a finite binary-input classical channel have nonnegative columns ay , by .
Discard outputs with ay = by = 0, which are outside its active output support. For every normalized
nonaffine operator-convex Petz divergence, and for SLD and minimal chi-square, its complete
equal-reference coefficient is the ordinary classical coefficient
                                                               X      (ay − by )2
                                c(K) = sup x(1 − x)                                 .                  (7)
                                        0<x<1                  y   by + (ay − by )x
Proof. After input dephasing write ρ = diag(ρ0 , ρ1 ), σ = diag(σ0 , σ1 ), with common sum r and
differences Z, −Z. For a resolvent set A = Lρ0 + uRσ0 , B = Lρ1 + uRσ1 , both positive on complex
HS. Each active pencil ay A + by B is positive definite because ay + by > 0, even if one coefficient
vanishes. With S = A + B and X = S −1/2 AS −1/2 , we have 0 < X < I and
                                    A−1 + B −1 = S −1/2 [X −1 + (I − X)−1 ]S −1/2 ,
                                                                  "                      #
                                                 −1        −1/2             (ay − by )2
                                                                                          S −1/2 .
                 X                                                 X
                               2
                      (ay − by ) (ay A + by B)        =S
                  y                                                y   by I + (ay − by )X
The scalar bound (7) applies to every eigenvalue of X; congruence preserves operator order.
Evaluating on Z gives the divergence upper. Positive integration and the quadratic endpoint give
Petz, and using A = Jσ0 , B = Jσ1 gives SLD/minimal chi-square. No simultaneous diagonalization
of A, B is used. For each fixed 0 < x < 1, every active scalar output probability is positive. Faithful
scalar input pairs approaching that x give the lower by the positive local Fisher factor f ′′ (1)/2;
nonaffinity and the positive integral representation ensure f ′′ (1) > 0. Take this local limit first, then
the supremum in x. An optimum need not be attained in the interior when entries vanish. This is a
global optimization over the base state, not a fixed-uniform-source claim.
    For the symmetric family the prior classical coefficient is
                                                           nλ2
                                          Bn (λ) =                  .                                  (8)
                                                       2 + (n − 2)λ
For completeness its scalar reconstruction is short. On two input columns the only informative
output rows have probabilities b + λx and b + λ(1 − x), where b = (1 − λ)/n; all other rows have
identical columns. The expression in (7) is
                                           λ2 (2b + λ)x(1 − x)
                                                                 .
                                          b(b + λ) + λ2 x(1 − x)
In the strict stochastic interior it is maximized at x = 1/2 and equals (8). Classical binary-support
reduction [3], together with the classical equivalence [2], gives the full ordinary benchmark. This is
a reconstruction of a classical quantity, not a claim of first discovery.
    All pairs of columns are equivalent and Proposition 4.1 identifies their complete coefficients with
Bn . BKM follows by local Umegaki expansion. At exclusion, λ = −1/(n − 1), a direct calculation
also makes the boundary transparent. On two inputs i, j, output i is the input block at j divided
by n − 1, output j is the block at i divided by n − 1, and every remaining output is the common
block r/(n − 1). Direct-sum additivity and homogeneity yield exactly
                                                       1
                                      Qf (Kρ∥Kσ) =         Qf (ρ∥σ)
                                                     n−1
for CQ pairs. The metric identities follow likewise. The cases λ = 0, 1 are immediate.

                                                           5
Corollary 4.2. For n > 2 and λ =     ̸ 0, 1 in the physical range, complete optimization for the five
quantities in Theorem 3.1 cannot be reduced to two common input symbols. Every two-symbol
restriction has coefficient Bn , whereas the full coefficient is Hn > Bn . At exclusion Hn /Bn = n − 1.

Proof. For λ ̸= 0,
                                   Hn     (n − 2)(1 − λ)
                                      −1=                 > 0.
                                   Bn     n[1 + (n − 2)λ]
Use the preceding subchannel analysis. At λ = 0 no ratio of zeros is taken.

    This statement concerns a support restriction on A, not a restriction to two hypotheses. It
leaves the prior binary-hypothesis characterizations in [5] intact.


5     A fixed channel and an actual binary readout
5.1   Faithful CQ hypotheses and their output
            √
Write f = u/ n, F = f f ∗ , P = I − F , ψi = n/(n − 1)(ei − u/n) and Πi = ψi ψi∗ . Thus i ψi = 0
                                            p                                          P

and i Πi = nP/(n − 1). For positive α, β, ε and 0 < δ < 1 satisfying
    P


                            α + (n − 2)ε + β = 1/n,            c2 = αβ(1 − δ),

define blocks

                 s±                                 ∗     ∗
                  i = αΠi + ε(P − Πi ) + βF ± c(ψi f + f ψi ),                ρ± = diagi s±
                                                                                          i .      (9)

Every block has trace 1/n, active determinant αβδ > 0, and inactive eigenvalue ε > 0. Both
hypotheses are faithful and normalized, their A marginals are uniform, and their common reference
marginal is
                                        n[α + (n − 2)ε]
                                    r=                  P + nβF.
                                             n−1
A phase flip I − 2F on the reference exchanges the hypotheses. It does not encode a phase on the
noisy classical input.
    Fix the exclusion channel. Its output block at j is (r − s±
                                                              j )/(n − 1). In the plane Πj + F it has
diagonals
                                          α + n(n − 2)ε
                                     a′ =                ,     β,
                                             (n − 1)2
coherence ±λc, λ = −1/(n − 1), and inactive eigenvalue

                                          nα + (n2 − 3n + 1)ε
                                   e′ =                       > 0.
                                               (n − 1)2

Let hi > li and ho > lo be the two active input and output eigenvalues. The full relative entropies,
without active-plane normalization, are

                                     log(hi /li )                        log(ho /lo )
                         Di = 4nc2                ,       Do = 4nλ2 c2                .           (10)
                                       hi − l i                            ho − lo
Indeed the logarithm of a positive 2 × 2 matrix has offdiagonal entry c log(h/l)/(h − l); changing the
sign of c and taking the trace gives the stated formula. Inactive modes are identical and contribute
zero.

                                                      6
   For output label j, let Qj = Πj + F and Wj− = Qj (N ρ− )j Qj . Measure

                                   ho Qj − Wj−
                           Ej =                ,       E = diagj Ej ,    I − E.
                                      ho − lo
The rank-one projector Ej is extended by zero off its plane. This is a binary measurement with
one-way classical feedforward: read j, then measure its specified reference projector. The effect is
fixed by the known pair, not by the unknown sign. With orientation ρ+ ∥ρ− its probabilities are
exactly                                                          !
                                                         4λ2 c2
                                q = nlo ,   p = n lo +             .                           (11)
                                                         ho − lo
For example, the offdiagonal entry of Ej is λc/(ho − lo ); pairing it with the output difference 2λcS
gives the increment 4λ2 c2 /(ho − lo ) in each block. This verifies the orientation and the increment
in (11). The complementary probabilities are 1 − q, 1 − p on the entire state. Thus
                                                              1−p
                           Db = p log(p/q) + (1 − p) log          ≤ Do ≤ Di .
                                                              1−q
There is no postselection, replacement of the quantum input denominator, or label-blind reference
measurement. Each individual marginal carries zero distinguishing information.

5.2   Fixed-alphabet limit
Theorem 5.1. Fix n ≥ 3. For integers k ≥ n, choose
                            1                                      1
                      β=       ,    δ = 2−k ,      ε = βδ,    α=     − (n − 2)ε − β.               (12)
                           4nk                                     n
For the faithful hypotheses (9) and measurement (11),

                    Di −→ log 2,     Do −→ log 2,         Db −→ log 2,   Db /Di −→ 1.

The channel and both system dimensions remain fixed. The input condition number is asymptotic to
4k2k , its trace semidistance to k −1/2 , and p ∼ 1/k, q ∼ 2−k /(4k).
Proof. The restriction k ≥ n gives α ≥ 7/(8n) > 0. The exact output determinant is
                                                 βδ[α + n(n − 2)β]
                                a′ β − λ2 c2 =                     > 0.
                                                      (n − 1)2
At fixed n, α → 1/n, hi → 1/n and ho → 1/[n(n − 1)2 ]. Using l = det /h, both li /(βδ) and lo /(βδ)
tend to one. Consequently

                         log(hi /li ) = k log 2 + log(4k) + o(1),
                         log(ho /lo ) = k log 2 + log(4k) − 2 log(n − 1) + o(1).

The two prefactors in (10), multiplied by k, tend to one. This proves the two quantum relative-
entropy limits. Formula (11) gives kp → 1 and 4k2k q → 1. Therefore log(p/q) = k log 2+log 4+o(1),
so p log(p/q) → log 2. The complementary Bernoulli term is O(p) and tends to zero, proving the
measured limit.
    The input minimum eigenvalue is li = αβδ/hi < βδ = ε, whereas the maximum tends to 1/n.
This gives κi ∼ 4k2k . Finally 12 ∥ρ+ − ρ− ∥1 = 2nc ∼ k −1/2 . All these limits are at fixed n; there is
no uniformity assertion in n, k.

                                                      7
   The common reference in this scaling is explicitly

                                 1 − 1/(4k)     1                     4k − 1
                          rk =              P + F,         κ(rk ) =          .
                                    n−1        4k                     n−1
It is identical for the two hypotheses at each k, but varies with k and approaches rank deficiency.
Its condition grows linearly; the exponentially growing condition in the theorem belongs to the joint
input states.
    For clarity define the binary-measured complete coefficient by

                               c                      D(M2 N ρ∥M2 N σ)
                              ηD,2m (N ) =    sup                      ,
                                             R,ρ,σ,M2     D(ρ∥σ)

where the input domain is the faithful equal-reference domain of (2) and M2 is a two-outcome
measurement on the joint output and reference.

Corollary 5.2. For every exclusion channel with n ≥ 3, ηD,2m  c    (N−1/(n−1) ) = 1. Dimension n of
the reference, separable CQ inputs and classical feedforward to a local reference measurement suffice
for this supremum.

Proof. Data processing bounds the coefficient by one. Theorem 5.1 provides admissible measured
ratios tending to one with a positive input divergence limit.

    This already uses n = 3, whose ordinary coefficient is 1/2. The finite positive limit of relative
entropy is compatible with vanishing trace distance because the states approach a singular boundary;
relative entropy is not uniformly continuous there. The exponentially rare q event and exponentially
bad conditioning are essential limitations of this explicit construction.
    The measurement depends on k. Although Ej → F , replacing Ej by F gives p = q =
nβ = 1/(4k) and zero binary divergence. Thus the limiting effect cannot replace the parameter-
dependent measurement. Likewise reversing only the Bernoulli orientation loses the leading term:
D(Ber(q)∥Ber(p))/Di → 0. No fixed effect or uniformity as n varies is claimed.

5.3   A distinct dimensional regime and a corrected scale condition
The same finite formulas also apply to

                         β = n−5 ,   δ = n−z ,    ε = n−(z+4) ,    z > 0 fixed,

with n → ∞. The same spectral calculation gives

                        Do   z+2         Db    z                  4(z + 4) log n
                           →     ,          →     ,       Di ∼                   .
                        Di   z+4         Di   z+4                      n4
Here absolute divergence vanishes and the channel changes with n. This is distinct from (12). The
relevant sufficient comparison for these constants is n(n − 2)ε = o(αδ). In this family ε/β = n1−z
can grow while that determinant comparison remains valid. Thus ε ≪ β is neither the necessary
comparison nor by itself sufficient. For example, with z = 4 and ε = n−6 in place of n−8 , the same
determinant formula gives limits Do /Di → 5/8 and Db /Di → 3/8, instead of 3/4 and 1/2. The
source supplement retains the earlier incorrect necessity claim and its audit correction.




                                                    8
6    Certified finite evidence and limitations
For the fixed-alphabet construction, nine cases were declared before evaluation. Directed integer
interval arithmetic at 1024 bits uses integer square roots and a range-reduced logarithm with an
explicit atanh-series remainder. No floating-point number establishes an inequality sign. The
arithmetic library is reused from earlier work and is not an independent implementation. Table 1
displays selected values only; integer endpoints and all nine cases are preserved in the supplement.
A component audit recomputed the nine cases at 2048 bits and added eleven adversarial controls
without changing the originals.
    Three separate full 9 × 9 constructions at k = 8, 16, 32, using 400-digit eigendecomposition and
a projector obtained from the full output spectrum, agree with six corresponding interval quantities
each. These are numerical cross-checks, not new interval proofs or independent reviewers. The
general theorem requires its analytical argument, not extrapolation from the table.

Table 1: Rounded displays of certified fixed-alphabet values. All rows shown have n = 3 and
ordinary benchmark 1/2.
                          k              Di              Db           Db /Di
                          8   1.0909434742    0.6511496162      0.5968683361
                         32   0.8384165205    0.6834417750      0.8151578103
                        256   0.7195237121    0.6919467548      0.9616733168

    Adverse results are retained. In the fixed-alphabet family, n = 3, k = 3 and k = 4 give certified
measured retentions about 0.4268407 and 0.4730447, both below 1/2. Among eight earlier symmetric
pairs tested with finite Umegaki divergence, three do not beat the classical comparator, although
their triangular ratios can do so. Further dimensional-regime examples at small n, z also fail to
separate. Changing the regularizer changes the limiting constants, and allowing z to vary with
n invalidates the fixed-z formula in general. Along n = k → ∞, the fixed-alphabet preparation
instead has measured retention asymptotic to 4/n, tending to zero. None of these cases is discarded
or treated as evidence that every finite pair separates.
    This study does not determine minimal reference dimension, an optimal tradeoff between
measurement, preparation and precision, a faithful maximizer, complete equality for every Petz
generator, ordinary mutual-information optima, or classical/quantum capacity. The memory,
known-pair measurement and tail precision are resources. No optimal bound on experimental
copy complexity is proved. Direct frequency estimation of the exponentially small q probability
and discrimination of the hypotheses are different tasks; no exponential lower bound for every
discrimination strategy is inferred. The fixed-alphabet construction removes vanishing input relative
entropy from one family; it does not remove conditioning and rare-event costs or imply small
one-shot error when trace distance vanishes.


7    Fixed-point decay and the scope of a uniform bound
Set n = 3 and regard Φ = N−1/2 ⊗ id3 as one fixed channel on M9 . It is unital and Hilbert–Schmidt
selfadjoint, and its powers converge to

                                       E(T ) = IA /3 ⊗ TrA T.




                                                 9
Its spectrum consists of 1 on IA ⊗ MR , −1/2 on traceless diagonal A ⊗ MR , and zero on offdiagonal
A ⊗ MR . Thus Φ is not primitive, although the three-symbol channel without the reference is
primitive.
    There is a precise distinction between one step and two steps in Theorem 3.1, independently of
the nonvanishing-divergence limit. Composition of the classical symmetric channels multiplies their
parameters, so

                 2                   c                     c   2                     1
                N−1/2 = N1/4 ,      ηD (N−1/2 ) = 1,      ηD (N−1/2 ) = H3 (1/4) =      .
                                                                                     10
Consequently the equal-reference coefficient can be one after one step and strictly below one after
two steps for the same primitive classical dynamics. This concerns arbitrary paired hypotheses; it is
not an entropy-to-fixed-point coefficient.
                                                −
    The constructed pairs satisfy Eρ+   k = Eρk with relative-entropy retention tending to one. No
single constant less than one therefore bounds all such equal-E pairs for this fixed Φ. Their common
E value varies with k and approaches rank deficiency. This is not a counterexample to a bound with
a fixed faithful second state, a fixed spectral floor, contraction toward Eρ, or eventual contraction of
powers.
    The generic failure of strict one-step contraction is classical prior art: Cohen et al. [10, Theorem
4.2 and Remark 4.3] characterize it through scrambling and give primitive channels with coefficient
one. Their support-disjointness argument and faithful limiting construction already prevent treating
a general one-step obstruction as a new resolution of the uniformity question discussed in [6]. No
claim that a historical problem is still open or first resolved here is made. The specific distinction in
the present example is that the exclusion channel has ordinary coefficient 1/2, and that it is the
common quantum reference which raises its complete and binary-measured suprema to one.




                                                   10
A     Model assessments and review context
This manuscript asserts no numerical model grade. Any assessment must be bound to its exact
PDF and exposed with its full report and context; grades attached to other PDFs do not apply.
A technical component audit is distinct from a manuscript assessment, human peer review and
editorial acceptance. None implies either of the others.
    The named author directed substantial OpenAI Codex assistance in derivation, writing and
numerical work. Completed component audits reconstructed the binary and simplex arguments and
preserved both favorable and adverse controls. The requested reviewer configuration was GPT-6
Astra xhigh. The reused evaluator had prior participation, reused context and shared filesystem
access. Effective model identity, effort, runtime isolation and independence were not attested.
These component audits are not independent votes and do not constitute human peer review, Lean
formalization or certified worldwide originality.
    Completed component audits reconstructed the binary extension, the exact simplex coefficients,
the fixed-z regime with its corrected scale condition, and the fixed-alphabet construction. They
also identified the classical antecedent for generic one-step noncontraction and the dependence
of the measurement on its preparation parameter. Full original objections and adverse controls
are retained rather than replaced by this summary. The supplements identify exact file hashes,
frozen inputs, reports, checker incidents and reading levels. A full manuscript assessment cannot be
inherited from a component proof.
    The preserved research dossiers are: binary argument and audit 1092/1093; simplex proof
and controls 1096; finite logarithm certificates 1099; controlled measurement 1101; technical audit
1100; endpoint supplement 1108; fixed-alphabet derivation 1110; source comparison 1112; full-
matrix checks 1113; and technical audit 1115. Their identifiers are reproducibility references, not
independent votes. Portable replay of seven core checkers reproduces six generated outputs byte for
byte and verifies 48 stored rational boundary rows. Two historical dependency paths are adapted
only in disposable execution copies, with original and executed hashes logged. Own derivations,
code, reports and source metadata form the supplement; third-party paper corpora and private
credentials are excluded.
    A provenance correction is retained explicitly: an earlier incident narrative claimed preservation
of malformed serialization bytes, but the saved first-control file is a valid JSON identical to the final
one. Those malformed historical bytes are not evidenced. The original narrative, unchanged files,
auditor objection and correction are all preserved; this discrepancy does not change the mathematical
parameters or certified results.




                                                   11
References
 [1] F. Hiai and M. B. Ruskai, Contraction coefficients for noisy quantum channels,
     arXiv:1508.03551v1 (2015), doi:10.1063/1.4936215.

 [2] A. Makur and L. Zheng, Linear bounds between contraction coefficients for f -divergences,
     arXiv:1510.01844v4 (2018); related published treatment: Comparison of contraction coefficients
     for f -divergences, Problems of Information Transmission 56 (2020), 103–156.

 [3] O. Ordentlich and Y. Polyanskiy, Strong data processing constant is achieved by binary inputs,
     arXiv:2010.01987. The two-page author version and its classical reduction proof were inspected.

 [4] D. Lee and A. Makur, Contraction coefficients of product symmetric channels, Allerton (2024),
     1–8, doi:10.1109/ALLERTON63246.2024.10735307. Bibliographic record consulted; full text
     not audited.

 [5] C. Hirche, I. George, T. Nuradha and M. M. Wilde, Conditional contraction coefficients and
     their applications to quantum networks, arXiv:2608.27171v1 (2026).

 [6] L. Gao and C. Rouzé, Complete entropic inequalities for quantum Markov chains, Archive for
     Rational Mechanics and Analysis 245 (2022), 183–238, doi:10.1007/s00205-022-01785-1.

 [7] L. Gao, M. Junge, N. LaRacuente and H. Li, Complete positivity order and relative entropy
     decay, Forum of Mathematics, Sigma 13 (2025), e31, doi:10.1017/fms.2024.117.

 [8] C. Wang and A. Gohari, Matrix Φ-entropic measures of dependence, arXiv:2610.29576v1 (2026).
     Selected definitions, theorem and proof passages consulted; no claim to resolve its distinct
     source-fixed problem.

 [9] M. S. Tan, M. Tomamichel and I. George, Tight contraction rates for primitive channels
     under quantum f -divergences, arXiv:2605.06452v1 (2026). Abstract, Theorem 1 statement and
     Definition 3 inspected; the full proof was not audited.

[10] J. E. Cohen, Y. Iwasa, Gh. Rautu, M. B. Ruskai, E. Seneta and Gh. Zbăganu, Relative entropy
     under mappings by stochastic matrices, Linear Algebra and its Applications 179 (1993), 211–235,
     doi:10.1016/0024-3795(93)90331-H. Theorem 4.2 and its proof and Remark 4.3 were inspected
     in the author PDF.




                                                12
