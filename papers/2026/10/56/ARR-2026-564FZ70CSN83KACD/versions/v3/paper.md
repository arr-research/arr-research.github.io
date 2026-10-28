# Common support and complete contraction with quantum side information

Machine-readable rendition of canonical21-page PDF SHA256 6d4f64b0b9423852ad2831e551edf467a6fbca14d30991b517084978573455c5.

    Common support and complete contraction with quantum side
                         information
                                             Lluis Eriksson

                                            28 October 2026


                                                 Abstract
         For a finite classical–quantum channel i 7→ τi , we prove that its complete equal-reference
     Umegaki contraction coefficient is one exactly when the intersection of the prepared-state supports
     is zero. The known positive-replacer bound supplies strict contraction in the complementary case.
     An operator-valued simplex factorization and a normalized graph projector give the converse
     with faithful separable hypotheses, uniform classical input, reference dimension equal to the
     input alphabet size and a joint binary readout. For every fixed channel, input, output and
     measured relative entropies tend to log 2. Two nonorthogonal pure outputs already exhibit the
     phenomenon: a certified finite binary retention exceeds the complete trace-distance coefficient,
     so a Hermitian Doeblin or trace bound cannot be substituted for the positive-replacer Umegaki
     bound. The graph effect can be nonseparable, and its convergence is not uniform over prepared
     states approaching equality. For classical outputs, a separate weight-independent Schur argument
     yields uniform convergence over all zero-Doeblin channels at fixed input size. We also determine
     exact SLD, minimal chi-square, triangular, BKM and Umegaki coefficients for symmetric classical
     channels, and distinguish binary input support from binary hypotheses or readout. Exponential
     conditioning, rare events, adaptive measurements and the quantum input denominator delimit
     the result. No capacity advantage, robust implementation, minimal reference dimension, general
     LOCC realization or worldwide priority is claimed.


1    Problem and relation to prior work
A classical noisy channel acts on probability distributions, but its input may be correlated with a
quantum memory that remains available after transmission. The relevant comparison is then between
two joint states with the same memory marginal. This constraint rules out the trivial strategy
of putting all distinguishing information in an untouched memory. It still permits noncommuting
conditional memory states, even when the input and memory are separable.
    Our main support criterion allows noncommuting prepared output states: for a finite CQ channel
i 7→ τi , strict complete Umegaki contraction holds precisely when all output supports contain a
common nonzero vector (Theorem 6.1). The positive-replacer upper is prior. The converse uses a
common input family and a channel-dependent joint binary effect; it is a pointwise statement for the
fixed channel. For commuting classical outputs we prove a stronger uniform-in-channel realization
at fixed input dimension (Theorem 7.1). Those quantifiers are not interchangeable.
    For ordinary classical strong data processing, optimizing over a large input alphabet can be
reduced to a pair of input symbols, by Ordentlich and Polyanskiy [3]. We first quantify the failure of
that reduction with a quantum reference for a full symmetric family. We characterize strict complete
Umegaki contraction for finite CQ channels in Theorem 6.1, and strengthen its classical-output
specialization in Theorem 7.1. Its converse uses a channel-independent input family and explicit


                                                     1
binary measurements. The input alphabet and reference dimension are fixed; the common reference
marginal and measurement may vary with the preparation parameter.
    Complete channel comparisons and their estimation representations are studied in [13]. We
do not infer a degradation or capacity statement from a contraction ratio. The definitions of
complete and conditional contraction coefficients are prior; we use the equal-reference complete
convention described by Hirche, George, Nuradha and Wilde [5]. Their characterization using a
binary hypothesis label is distinct from restricting the input alphabet to two symbols. We do not
claim a new correspondence between divergence and reference-assisted information measures. Hiai
and Ruskai [1] provide the operator-convex divergence and metric framework. Classical equivalence
of global contraction coefficients is treated by Makur and Zheng [2]. The classical symmetric-channel
formula below is a benchmark, not a novelty claim; Lee and Makur [4] is an additional relevant
classical reference whose full proof has not been inspected in our directed audit.
    Complete entropy decay toward a conditional expectation [6, 7] uses a different restriction on the
second state. Those estimates do not automatically bound two arbitrary correlated hypotheses with
equal reference. Conversely, our pair constructions do not contradict decay toward a fixed-point
state. Recent asymptotic contraction bounds for primitive channels with a fixed faithful stationary
state [9] concern that different quantifier regime. The source-fixed matrix-Φ framework of Wang
and Gohari [8] is also distinct; we do not claim to resolve its open questions. Generic failure of strict
one-step contraction, even for primitive classical channels, already appears in Cohen et al. [10]. The
issue studied here is the exact complete coefficient and the quantum-reference enhancement of a
classical channel whose ordinary coefficient is strictly below one. Our literature search is directed
and does not certify worldwide priority.
    The classical Doeblin decomposition and complete contraction definitions are prior [11, 5].
Classical scrambling uses pairwise column overlap [10]; the complete criterion below instead requires
a positive row common to all columns. Nonlinear classical multi-way Doeblin curves [12] address
another contraction question. Selected primary passages, rather than entire source corpora, were
inspected. The general converse here extends the same simplex mechanism used for the symmetric
examples; it is not a new data-processing principle or an independently invented construction.


2    Definitions and a harmonic upper bound
Let A = Cn be equipped with its stated classical basis, and define
                                                 1−λ                  1
                          Kλ (y | x) = λδxy +        ,           −       ≤ λ ≤ 1.                    (1)
                                                  n                  n−1
The quantum channel Nλ first dephases A in this basis and then applies Kλ to its diagonal. It is
not the quantum depolarizing channel on arbitrary coherences. We suppress idR from notation.
   For a divergence Q, write

                                c                                Q(N ρ∥N σ)
                               ηQ (N ) =          sup                       .                        (2)
                                             dim R<∞, ρ,σ>0       Q(ρ∥σ)
                                           Tr ρ=Tr σ=1, ρR =σR
                                               0<Q(ρ∥σ)<∞

The supremum is over faithful normalized states; no faithful maximizer is asserted. The ordinary
coefficient omits R. All logarithms are natural.
   For operator-convex f : (0, ∞) → R with f (1) = 0, the Petz divergence is

                                 Qf (ρ∥σ) = ⟨σ 1/2 , f (Lρ Rσ−1 )σ 1/2 ⟩HS .                         (3)

                                                     2
Here La X = aX, Rb X = Xb and ⟨X, Y ⟩HS = Tr X ∗ Y . The relevant generators include f (t) = t log t
and f△ (t) = (t − 1)2 /(t + 1). We distinguish Qf△ from the finite minimal chi-square divergence

                     χ2min (ρ, σ) = ⟨ρ − σ, Jσ−1 (ρ − σ)⟩HS ,            Jσ = (Lσ + Rσ )/2.

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

any real c, the output difference is j (wj − c)Zj . The inverse quadratic-form inequality gives
                                    P

                 *                                −1                        +
                     X                    X              X                            X (wj − c)2
                         (wj − c)Zj ,        wj Ωj             (wj − c)Zj       ≤                    q.
                     j                    j                  j                        j
                                                                                              wj

One proof minimizes j ⟨Yj , (wj Ωj )−1 Yj ⟩ subject to a fixed sum j Yj , and substitutes Yj =
                          P                                                               P

(wj − c)Zj . Minimizing the scalar coefficient over c gives c = n/ j wj−1 and h(w).
                                                                  P

    All operators act on the full complex Hilbert–Schmidt space. In column vectorization Rσ
contains σ T , with no assumption that the states are real or commuting. The positive integral
representation [1]
                                                               (t − 1)2
                                                         Z
                     f (t) = a(t − 1) + b(t − 1)2 +                     dµ(u),                b ≥ 0,
                                                          [0,∞) t + u

transfers this upper bound to every such f , with µ positive and (1 + u)−1 dµ(u) < ∞. The affine
                                                                                  R

part cancels by equal traces. The quadratic endpoint is proved by the same argument with Ω = Rσ ,
so it is not discarded. Positivity of the measure justifies the integration. Local expansion of the
triangular and Umegaki cases gives the metric bounds.

   For CQ states, j Tj (ρ − σ) = 0 is exactly the equal-reference constraint. The channel (1) is a
                     P

mixture of cyclic shifts with
                                     1 + (n − 1)λ                       1−λ
                              w0 =                ,              wj =             (j ̸= 0).
                                          n                              n
The lemma therefore gives
                                                           (n − 1)λ2
                                              Hn (λ) =                .                                     (4)
                                                         1 + (n − 2)λ
At the two stochastic endpoints a weight may vanish. We use ordinary data processing to obtain
the upper bound one, not a singular evaluation of 1/wj . At λ = 0 the output difference vanishes
exactly. Dephasing before the cyclic mixture preserves the common reference and cannot increase
the input divergence, so the upper applies to general quantum inputs as well.

                                                          3
3    Exact complete coefficients
Theorem 3.1. For every n ≥ 2 and physical λ in (1), the complete coefficients for SLD, χ2min , Qf△ ,
BKM and Umegaki relative entropy are all Hn (λ). A reference of dimension n suffices for their
suprema. For every normalized nonaffine operator-convex Petz generator, Hn is an upper bound;
equality for every generator is not asserted.
Proof. Only matching lower bounds remain. In R = Cn put

                             u = (1, . . . , 1)T ,     P = I − uu∗ /n,           vi = ei − u/n.
                          2 = (n − 1)/n and P v v ∗ = P . Define the CQ blocks
        i vi = 0, ∥vi ∥
       P
Then                                         i i i

                          vi vi∗
                 σi =            ,      Di = uvi∗ + vi u∗ ,            σ = diagi σi ,          D = diagi Di .
                          n−1
They give Tr σ = 1, TrA σ = P/(n − 1) and TrA D = 0. Use the common faithful regularization

                                     σξ = (1 − ξ)σ + ξIn2 /n2 ,                0 < ξ < 1.

Its actual reference marginal is (1 − ξ)P/(n − 1) + ξIn /n. In the plane spanned by vi and u, the
block eigenvalues and tangent coherence are
                                     1−ξ   ξ                    ξ                         √
                               α=        + 2,           β=         ,       |(Di )12 | =       n − 1.
                                      n   n                     n2
The output preserves β, replaces α by
                                                (1 − ξ)[1 + (n − 2)λ]   ξ
                                         α′ =                         + 2,                                      (5)
                                                      n(n − 1)         n
and replaces D by λD. Therefore the SLD ratio is
                                                     α+β
                                       Rξ = λ2              −→ Hn (λ)            (ξ ↓ 0).                       (6)
                                                     α′ + β
Indeed gσξ (D) = 4n(n − 1)/(α + β). The finite pair ρ = σξ + tD, σ = σξ realizes the same ratio for
minimal chi-square whenever t ̸= 0 is sufficiently small.
   For the triangular divergence choose ρ± = σξ ± tD, where t2 (n − 1) < αβ. These are faithful
normalized states with identical reference. To evaluate a subnormalized active block, write W± =
diag(a, b) ± cS, where S = ( 01 10 ). Then W+ S + SW− = (a + b)S, so

                                                              2c                                        8c2
                (LW+ + RW− )−1 (W+ − W− ) =                      S,             Qf△ (W+ ∥W− ) =             .
                                                             a+b                                       a+b
          √
With c = t n − 1 this gives 8t2 (n−1)/(α+β) per input block. At output the coherence is multiplied
by λ and the denominator is α′ + β, so the exact finite ratio is again (6). Positivity also follows from
                                        (1 − ξ)(1 − λ)[1 + (n − 1)λ]
                        α ′ − λ2 α =                                 + β(1 − λ2 ) ≥ 0.
                                                  n(n − 1)
No active plane is renormalized or postselected.
   For BKM put ℓ(a, b) = (log a − log b)/(a − b), with its continuous extension. The local ratio is
                                                             ℓ(α′ , β)
                                                        λ2             .
                                                             ℓ(α, β)

                                                               4
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


4    Why two input symbols no longer suffice
We include the binary upper argument to identify exactly the boundary crossed by Theorem 3.1.

Proposition 4.1. Let a finite binary-input classical channel have nonnegative columns ay , by .
Discard outputs with ay = by = 0, which are outside its active output support. For every normalized
nonaffine operator-convex Petz divergence, and for SLD and minimal chi-square, its complete
equal-reference coefficient is the ordinary classical coefficient
                                                               X      (ay − by )2
                                c(K) = sup x(1 − x)                                 .                  (7)
                                         0<x<1                 y   by + (ay − by )x

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
                                           Bn (λ) =                 .                                  (8)
                                                       2 + (n − 2)λ




                                                           5
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
                                   Qf (Kρ∥Kσ) =             Qf (ρ∥σ)
                                                        n−1
for CQ pairs. The metric identities follow likewise. The cases λ = 0, 1 are immediate.

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


                            α + (n − 2)ε + β = 1/n,         c2 = αβ(1 − δ),

define blocks

                 s±                                 ∗     ∗
                  i = αΠi + ε(P − Πi ) + βF ± c(ψi f + f ψi ),         ρ± = diagi s±
                                                                                   i .              (9)

For n ≥ 2, every block has trace 1/n, active determinant αβδ > 0, and inactive eigenvalue ε > 0
of multiplicity n − 2 (absent when n = 2). Both hypotheses are faithful and normalized, their A
marginals are uniform, and their common reference marginal is
                                         n[α + (n − 2)ε]
                                    r=                   P + nβF.
                                             n−1

                                                    6
A phase flip I − 2F on the reference exchanges the hypotheses. It does not encode a phase on the
noisy classical input.
    Fix the exclusion channel. Its output block at j is (r − s±
                                                              j )/(n − 1). In the plane Πj + F it has
diagonals
                                          α + n(n − 2)ε
                                     a′ =                ,     β,
                                             (n − 1)2
coherence ±λc, λ = −1/(n − 1), and, only for n ≥ 3, inactive eigenvalue
                                            nα + (n2 − 3n + 1)ε
                                     e′ =                       > 0.
                                                 (n − 1)2
Let hi > li and ho > lo be the two active input and output eigenvalues. The full relative entropies,
without active-plane normalization, are
                                      log(hi /li )                        log(ho /lo )
                         Di = 4nc2                 ,       Do = 4nλ2 c2                .          (10)
                                        hi − l i                            ho − lo
Indeed the logarithm of a positive 2 × 2 matrix has offdiagonal entry c log(h/l)/(h − l); changing the
sign of c and taking the trace gives the stated formula. Inactive modes are identical and contribute
zero.
    For output label j, let Qj = Πj + F and Wj− = Qj (N ρ− )j Qj . Measure

                                   ho Qj − Wj−
                           Ej =                ,       E = diagj Ej ,        I − E.
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
                           Db = p log(p/q) + (1 − p) log           ≤ Do ≤ Di .
                                                               1−q
There is no postselection, replacement of the quantum input denominator, or label-blind reference
measurement. Each individual marginal carries zero distinguishing information.

5.2   Fixed-alphabet limit
Theorem 5.1. Fix n ≥ 3. For integers k ≥ n, choose
                            1                                       1
                      β=       ,    δ = 2−k ,      ε = βδ,     α=     − (n − 2)ε − β.             (12)
                           4nk                                      n
For the faithful hypotheses (9) and measurement (11),
                   Di −→ log 2,      Do −→ log 2,          Db −→ log 2,      Db /Di −→ 1.
The channel and both system dimensions remain fixed. The input condition number is asymptotic to
4k2k , its trace semidistance to k −1/2 , and p ∼ 1/k, q ∼ 2−k /(4k).

                                                       7
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

   The common reference in this scaling is explicitly

                                  1 − 1/(4k)     1                       4k − 1
                           rk =              P + F,           κ(rk ) =          .
                                     n−1        4k                       n−1
It is identical for the two hypotheses at each k, but varies with k and approaches rank deficiency.
Its condition grows linearly; the exponentially growing condition in the theorem belongs to the joint
input states.
    For clarity define the binary-measured complete coefficient by

                                c                      D(M2 N ρ∥M2 N σ)
                               ηD,2m (N ) =        sup                  ,
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



                                                         8
5.3   A distinct dimensional regime and a corrected scale condition
The same finite formulas also apply to

                         β = n−5 ,   δ = n−z ,       ε = n−(z+4) ,       z > 0 fixed,

with n → ∞. The same spectral calculation gives

                        Do   z+2         Db    z                        4(z + 4) log n
                           →     ,          →     ,              Di ∼                  .
                        Di   z+4         Di   z+4                            n4
Here absolute divergence vanishes and the channel changes with n. This is distinct from (12). The
relevant sufficient comparison for these constants is n(n − 2)ε = o(αδ). In this family ε/β = n1−z
can grow while that determinant comparison remains valid. Thus ε ≪ β is neither the necessary
comparison nor by itself sufficient. For example, with z = 4 and ε = n−6 in place of n−8 , the same
determinant formula gives limits Do /Di → 5/8 and Db /Di → 3/8, instead of 3/4 and 1/2. The
source supplement retains the earlier incorrect necessity claim and its audit correction.


6     Noncommuting prepared outputs and common support
The classical output assumption can be removed if the convergence is required for each fixed channel.
Let                                       n  X
                                  N (X) =          ⟨i|X|i⟩τi ,       n ≥ 2,
                                             i=1
                                                                                           P
where the τi are density operators on a finite-dimensional output space. Write S = i τi and
compress the output space to B = supp S, so that S > 0 on B. All inverses below use that
compressed space. Define the positive common-component weight

                           a+ (N ) = max{Tr X : 0 ≤ X ≤ τi for every i}.

This is the positive-replacer coefficient, not the optimization over Hermitian, possibly nonpositive,
operators in the other quantum Doeblin coefficient of [11].

Theorem 6.1. For the finite classical–quantum channel above,
                                                           n
                                                           \
                                c
                               ηD (N ) = 1    ⇐⇒                 supp τi = {0}.
                                                           i=1

If the intersection is nonzero, the known estimate is ηD c (N ) ≤ 1 − a (N ) < 1. If the intersection
                                                                       +
is zero, a single family of faithful separable CQ inputs, independent of the prepared states, suffices
with reference dimension n and uniform classical marginal. For each fixed channel it admits
channel-dependent joint binary effects with

                         Di −→ log 2,        Do −→ log 2,               Db −→ log 2.

The common reference marginal and the effect vary with the preparation parameter. This is a
pointwise statement in the prepared states; no uniform resource bound over such states is asserted.
The effects are joint measurements on R ⊗ B and need not be implementable by local operations and
classical communication (LOCC).



                                                       9
6.1   The known direction and the operator-valued simplex
The maximum defining a+ exists by compactness. If a nonzero X is feasible, its range lies in every
support. Conversely, a unit vector v in the common support gives tvv ∗ ≤ τi for all i when

                                               0 < t ≤ min⟨v, τi+ v⟩−1 ,
                                                             i

where τi+ is its support inverse. Thus a+ > 0 exactly when the intersection is nonzero. The
positive-replacer decomposition, joint convexity and DPI give the stated upper [11, 5]. If a+ = 1,
all prepared states coincide and the coefficient is zero. These facts are prior; the converse below
supplies the witness when the upper becomes trivial.
    Use f, F, P, ψi , Πi from Section 5. On P R ⊗ B set
                             X                               X
                       T =        Πi ⊗ τ i ,        Z=               ψi ⊗ τi ,       G = IP R ⊗ S.
                              i                                  i

Here Z maps B to P R ⊗ B, 0 ≤ T ≤ G, and T may have a kernel.

Lemma 6.2. If the common support is zero, then

                                       ran Z ⊆ ran T,                  Z ∗ T + Z = S.

For T0 = G−1/2 T G−1/2 and Z0 = G−1/2 Z, the corresponding identities hold with T0 , Z0 in place of
T, Z, and 0 ≤ T0 ≤ I.

Proof. On H =
                L
                    i supp τi define
                                         X            √                              X√
                             W (vi ) =         ψi ⊗       τi vi ,        U (vi ) =        τi vi .
                                          i                                           i

Then T = W W ∗ , Z = W U ∗ and S = U U ∗ . The only linear relation among the simplex vectors has
all coefficients equal. Applying its coordinate functionals shows that W (vi ) = 0 exactly when all
√
  τi vi are one common vector w. Such a vector belongs to every support. With zero intersection it
is zero, hence all vi = 0 on their restricted domains. Thus W is injective, although it need not be
onto, and
                                         W ∗ (W W ∗ )+ W = IH .
This gives Z ∗ T + Z = U U ∗ = S and the range inclusion. For the whitened statement apply the same
argument to G−1/2 W , which is still injective. No general congruence rule for a Moore–Penrose
inverse is used.

   If the intersection is nonzero, ker W consists of the corresponding common vectors and U (vi ) = nw
there. Consequently S − Z ∗ T + Z = U Pker W U ∗ is positive and nonzero. The zero-intersection
hypothesis is substantive.

6.2   Faithful inputs and a resolvent on the correct range
For integers k ≥ max(n, 2) take
                  1                                                  1
            β=       ,    δ = 2−k ,      ε = βδ,          α=           − (n − 2)ε − β,       c2 = αβ(1 − δ),
                 4nk                                                 n



                                                              10
and the blocks s±
                i of (9). The same formula also works for n = 2, where the inactive sector is absent.
In this range α ≥ 1/(2n). Each block has trace 1/n, active determinant αβδ > 0 and n − 2 common
inactive eigenvalues ε. The equal reference marginal is
                                              1 − 1/(4k)     1
                                       rk =              P + F.
                                                 n−1        4k
The two active input eigenvalues satisfy h + l = α + β, hl = αβδ, and
                                                   log(h/l)
                                    Di = 4nc2               −→ log 2.
                                                     h−l
Indeed h ∼ 1/n, l ∼ βδ, the logarithm equals k log 2 + log(4k) + o(1), and the prefactor is asymptotic
to 1/k. This calculation includes n = 2 directly and does not import a theorem restricted to larger
alphabets.
    In the decomposition (P R ⊗ B) ⊕ (f ⊗ B) the outputs are
                                               !
                                 A    ±cZ
                       M± =               ,               A = αT + ε(G − T ) > 0.
                                ±cZ ∗ βS

Put Bε = Z ∗ A−1 Z. Let µ∗ > 0 be the smallest positive eigenvalue of T0 , and take a0 = 1/(2n).
The range statement of Lemma 6.2 removes the kernel from the resolvent

                                        [αT0 + ε(I − T0 )]−1 Z0 .

For 0 < µ ≤ 1 its scalar denominator is αµ + ε(1 − µ). Therefore, for this fixed channel,

                                                               ∥G−1/2 ∥ ∥Z0 ∥
                                                ∥A−1 Z∥ ≤ K1 :=               ,
                                                                   a0 µ∗
                                                                      ∥Z0 ∥2
                      0 ≤ S/α − Bε ,       ∥S/α − Bε ∥ ≤ K2 ε, K2 := 2 2 .
                                                                       a0 µ∗
The second estimate follows by subtracting the two scalar resolvents on the positive spectrum, using
Z0∗ T0+ Z0 = S. The constants depend on the channel, including the conditioning of S. Boundedness
of the product A−1 Z does not assert boundedness of A−1 on the kernel sector.
     The Schur complement satisfies

                                    Q = βS − c2 Bε ≥ βδS > 0.

Thus both output states are faithful on R ⊗ B, even when T is singular; their trace is one. The
inputs and outputs remain separable, since they are sums of positive products with the classical
input flag or with τi .

6.3      A joint binary graph projector
Define                                    !
                                       X
              X = cA−1 Z,      H=         ,          C = (IB + X ∗ X)−1 ,     E = HCH ∗ .
                                       IB
This is an orthogonal projector of rank dim B, so E, I − E is a physical binary measurement. In
particular, the normalizer C cannot be dropped. Direct multiplication, without commuting C with
other matrices, gives

              q = Tr(EM− ) = Tr(CQ),           p − q = Tr(E(M+ − M− )) = 4c2 Tr(CBε ).

                                                     11
Both probabilities and their complements are strictly between zero and one. With Rε = S/α−Bε ≥ 0
we have Q = βδS + c2 Rε , hence, writing d = dim B,
                                       nβδ
                                               ≤ q ≤ nβδ + dc2 K2 ε.
                                    1 + c2 K12

Since c2 = O(β) and ε = βδ, this yields

                      q = nβδ(1 + O(β)),          p − q = 4nβ(1 + O(β) + O(δ)).

All errors here are for the fixed channel. Consequently p ∼ 1/k, q ∼ 2−k /(4k), and Db → log 2. The
complement term is retained and tends to zero; the dominant term is p log(p/q). Finally

                                           Db ≤ Do ≤ Di −→ log 2

proves Theorem 6.1. Dephasing a general quantum input preserves its reference and output while
decreasing its input divergence, so the CQ calculation also gives the complete coefficient of the
stated dephasing channel.

6.4   Two nonorthogonal pure outputs: a certified separation
Let n = 2 and
                                                                    (1, 2i/3)T
                            τ0 = |0⟩⟨0|,      τ1 = |v⟩⟨v|,       v= p          .
                                                                      1 + 4/9
Their support intersection is zero although the states are not orthogonal. The complete equal-
reference trace-distance coefficient is
                              c                           2
                             ηTr (N ) = 12 ∥τ0 − τ1 ∥1 = √ < 0.55470020.
                                                          13
Indeed equal-reference CQ differences have blocks ∆, −∆, so the output difference is ∆ ⊗ (τ0 − τ1 ).
Multiplicativity of trace norm and dephasing give the upper, attained by faithful binary scalar pairs.
This observation does not transfer a trace upper to Umegaki with equal quantum reference.
   At k = 16 the graph effect gives exactly
                                7696491479061                      29360121
                         p=                    ,          q=                   .
                               142416973893184                 142416973893184
Directed integer intervals for the full quantum input denominator and binary numerator certify the
following outward coarsenings:

                        k     lower bound for Db /Di         upper bound for Db /Di
                       16                    0.66199617                  0.66199618
                       64                    0.86637095                  0.86637096
                      128                    0.92221644                  0.92221645

Already the first faithful finite case exceeds the complete trace coefficient. The Hermitian common-
component coefficient and the positive coefficient a+ therefore cannot be interchanged in a Umegaki
upper. Their distinction and the trace comparator are prior [11]; the present example does not
contradict that source. The reference cancellation for ρ − σ does not extend without an argument
to ρ − γσ.

                                                    12
    There is also a limitation on implementation. For this k = 16 effect, an exact partial-transpose
calculation gives
                             379198357755215264698242663046681136177401036800
           det(E TB ) = −                                                      < 0.
                            24520375593929253018522589845522864250466367834721
A local change of reference basis preserves this sign. This effect is not separable and hence not
LOCC. Separable input and output states do not remove the joint-readout requirement. This is not
a proof that every alternative effect approaching the supremum must be nonlocal.

6.5   Why the pointwise qualifier matters
For real pure outputs proportional to (1, 0) and (1, t), t > 0, the binary case has T = G = S, so
T0 = IB for every t. It is incorrect to attribute this example’s loss of uniformity to a vanishing
positive eigenvalue of T0 . Instead
                                                                          !
                                        −1                       1    0
                                    S        (τ0 − τ1 ) =
                                                                −2/t −1

can diverge with the conditioning of S. If r = c2 /α2 , direct algebra gives

                                                       2t2 (1 + r)
                  h0 = Tr[(I + rJ ∗ J)−1 S] =                       ,     J = S −1 (τ0 − τ1 ),
                                                   t2 (1 + r)2 + 4r
with q = βδh0 , p = β(4 − 3δ)h0 . At fixed t, h0 → 2. For tk = 1/k, however, h0 ∼ 2/k, so the
binary retention of this graph construction tends to zero. Each fixed channel still has optimized
coefficient one. The example refutes a uniform rate for the specified construction, not every possible
preparation or readout.
    The exact derivations, seven directed interval cases, mixed-rank/kernel controls and adverse
measurements are retained in dossier1157. High-precision ambient controls are diagnostics, not
interval certificates. The input condition grows as 4k2k , the effect depends on τi , k, and rare
probabilities require increasing precision. No optimal resource bound, stable experimental advantage,
capacity formula or extension to arbitrary quantum-input channels is established. The classical
uniform result below is stronger in its channel quantifier and requires its separate weight-independent
argument.


7     A support criterion for arbitrary classical channels
The symmetric family is not required for the boundary value one. We now let K = (K(y | i)) be
any finite column-stochastic matrix with n ≥ 2 inputs. Its quantum extension first dephases A and
retains the same finite quantum reference as before. Put
                                                    X
                                        d(K) =           min K(y | i).
                                                            i
                                                     y

This is the classical Doeblin common-component coefficient. The decomposition giving the upper
bound below is prior [11, 5]; the converse is the issue addressed here.
Theorem 7.1 (Strict complete contraction and common support). For every such K, with the
faithful equal-reference Umegaki domain of (2),
                                    c
                                   ηD (K) < 1            ⇐⇒      d(K) > 0.

                                                         13
Equivalently, ηDc (K) = 1 exactly when each nonzero output row has a zero entry. The same criterion
            c
holds for ηD,2m  (K), whose denominator remains quantum. When d(K) = 0, dimension n of the
reference and separable CQ hypotheses with uniform classical marginal suffice. The hypotheses can
be chosen independently of K: for fixed n, their input, output and binary-measured relative entropies
tend to log 2, uniformly over all finite K with n inputs and d(K) = 0. The output measurement is
allowed to depend on K and the preparation parameter.
    A common row of positive entries is a stronger support condition than pairwise column over-
lap. The latter characterizes strict ordinary relative-entropy contraction through scrambling [10,
Theorems 4.1–4.2]. Thus the theorem distinguishes two support tests, rather than claiming a new
definition of complete contraction or of Doeblin minorization. For n = 2 the tests coincide. No
claim of strict quantum-reference enhancement is made for channels whose ordinary coefficient is
already one.

7.1   The known upper and the proper-support inverse
If 0 < d < 1, set ay = mini K(y | i) and write

                                 K = dQ + (1 − d)L,        Q(y | i) = ay /d,

where L is stochastic and Q is replacement. Equal reference marginals give Qρ = Qσ. Joint
convexity and data processing imply

                         D(Kρ∥Kσ) ≤ (1 − d)D(Lρ∥Lσ) ≤ (1 − d)D(ρ∥σ).                                (13)

For d = 1, K itself is replacement and the coefficient is zero. Consequently d > 0 implies strict
contraction for every finite reference, including the binary-measured coefficient. General quantum
inputs reduce to CQ by dephasing, as in Section 2.
   For the converse use exactly the hypotheses (9) and scale (12); these also define valid states for
n = 2, with no inactive input modes. Their construction and their input divergence do not depend
on K. The input calculation in Theorem 5.1 proves Di → log 2 also for n = 2; the exclusion-specific
output calculation is not needed.
   Discard an identically zero output row only as a common null support. If d = 0, every remaining
row wi = K(y | i) has a proper support S, with 1 ≤ m = |S| ≤ n − 1. Write
                   X                                               X                  X
              t=       wi > 0,     V = span{ψi : i ∈ S},     T =       wi Πi ,   z=       wi ψi .
                   i                                               i                  i

All inverses involving T below are restricted to V .
Lemma 7.2. The space V has dimension m, T |V > 0, and
                                                           m(n − 1)
                         z ∗ TV−1 z = t,    ∥TV−1 z∥2 =             ≤ (n − 1)2 .
                                                            n−m
Proof. Let B have columns ψi , i ∈ S, and W = diag(wi : i ∈ S) > 0. The Gram matrix is
                                                  nIm − 1m 1∗m
                                     G = B∗B =                 > 0.
                                                     n−1
Its eigenvalue on 1m is (n − m)/(n − 1), and its other eigenvalues are n/(n − 1). Thus B has full
column rank. Since T = BW B ∗ and z = BW 1m , the vector v = BG−1 1m satisfies T v = z. It
follows that z ∗ v = t and ∥v∥2 = 1∗m G−1 1m = m(n − 1)/(n − m). In particular this norm bound has
no reciprocal minimum weight.

                                                   14
7.2   A controlled eigenvalue, with bounds independent of the row
On V ⊕ Cf , the minus output block is
                                      !
                           A −gy
                 M− =            ,         A = (α − ε)T + εtIV ,       gy = cz,      b = βt.
                          −gy∗ b

On P ⊖ V , both output blocks equal εtI. These common modes remain in the physical state. Since
T ≤ tIV , we have A ≥ αT and A > εtIV . Also α − ε > 0 for (12).
   For 0 ≤ x ≤ εt, define the Schur function

                                 H(x) = b − x − gy∗ (A − xIV )−1 gy .

Lemma 7.2 yields

                               H(0) ≥ βtδ > 0,
                                          tβε(1 − δ)
                               H(εt) = −             < 0,
                                             α−ε
                               H ′ (x) = −1 − ∥(A − xIV )−1 gy ∥2 < 0.

There is a unique root ℓy ∈ (0, εt). Interlacing places the other active eigenvalues above εt; inactive
eigenvalues equal εt. Therefore ℓy is the unique global minimum eigenvalue of this nonzero output
block for the stated scale. This conclusion is proved here, rather than inferred from a numerical
selector.
    The operators A − xIV and T commute, and

                                 A − xIV = (α − ε)T + (εt − x)IV .

Consequently
                                                                     c2 (n − 1)2
                          ∥(A − xIV )−1 gy ∥2 ≤ Cnk ,        Cnk =               .
                                                                      (α − ε)2
Integrating −H ′ from zero to ℓy gives

                                            βtδ
                                                  ≤ ℓy < βtδ.                                       (14)
                                          1 + Cnk
For a normalized minimum eigenvector uy = (xy , sy ) of M− , with sy > 0, the eigenvalue equation
gives
                                                         1
                         xy = (A − ℓy IV )−1 gy sy ,          ≤ s2y ≤ 1.
                                                      1 + Cnk
These estimates are independent of S, the positive row weights and the number of output rows.
They do not assert a well-conditioned eigenvector computation.

7.3   One binary readout and the uniform limit
Choose Ey = uy u∗y on V ⊕Cf , extended by zero on the inactive subspace, and measure E = diagy Ey ,
I − E. This is a two-outcome measurement implemented by classical feedforward to a reference
measurement. It uses the known hypotheses and K, not the unknown sign. For the orientation plus
versus minus,

             qy = Tr(Ey M− ) = ℓy ,       py − qy = 4s2y gy∗ (A − ℓy IV )−1 gy = 4s2y (βt − ℓy ).

                                                    15
                    P                                P             P
Summing uses only      y ty = n. Thus, with p =       y py , q =       y qy ,

                                          nβδ
                                    qL =        ≤ q ≤ qU = nβδ,                                  (15)
                                        1 + Cnk
                                     4nβ(1 − δ)
                           pL = qL +            ≤ p ≤ pU = qU + 4nβ.
                                      1 + Cnk
The complement probabilities are 1−p, 1−q on the full normalized states. There is no active-subspace
normalization or postselection.
   At fixed n, Cnk = On (1/k). These scalar bounds imply, uniformly in the channel,

                                                               2−k
                        p = k −1 (1 + On (k −1 )),        q=       (1 + On (k −1 )).
                                                                4k
Therefore log(p/q) = k log 2+log 4+o(1) and p log(p/q) → log 2, while (1−p) log[(1−p)/(1−q)] → 0.
This proves Db → log 2. The inequalities Db ≤ Do ≤ Di , with Di → log 2, prove the output limit
and both ratios. Data processing supplies the upper bound one, establishing Theorem 7.1.
   More explicitly, when pL > qU , put

                                            D(Ber(pL )∥Ber(qU ))
                                    Lnk =                        ,
                                                 Di (n, k)

and put Lnk = 0 otherwise. Monotonicity of Bernoulli KL in p and q for p > q gives simultaneously

                                 Db (K, k)   Do (K, k)
                         Lnk ≤             ≤           ≤ 1,              Lnk −→ 1.
                                 Di (n, k)   Di (n, k)

Hence the same input preparation works for a sequence Kk with changing supports, weights and
finite output cardinalities, provided n is fixed and d(Kk ) = 0. The effects Ey (Kk , k) change with
the channel. This is neither a channel-independent effect nor uniformity of measurement precision,
computational cost, a spectral floor or growing n.

7.4   A certified asymmetric separation and falsifiers
For example, consider the fixed channel
                                                                  
                                             0 1/3 2/5
                                       K = 3/4 0 3/5 .
                                                      
                                            1/4 2/3 0

Its Doeblin coefficient is zero, while its classical Dobrushin coefficient is 3/4; hence its ordinary
Umegaki coefficient is at most 3/4. Directed integer bounds from (15) certify Db /Di > 0.8860189
at k = 64 and Db /Di > 0.9328480 at k = 128. These certificates establish finite separations, not the
general theorem.
    The rule “choose the eigenvector of maximal overlap with f ” is not a universal finite-k implemen-
tation of the minimum eigenprojector. In exclusion with n = k = 16 it chooses a different branch:
the measured ratios are about 0.006905 for that rule and 0.145103 for the correct minimum. Both
original numerical controls and this falsifier are retained. The proof and readout definition use the
minimum established by (14).
    The scale condition is also substantive. In a four-input cycle with two inputs in each output
support, replacing ε = βδ by ε = βδ 1/2 changes the measured limiting retention to 1/2. Replacing it

                                                     16
by ε = βδ 2 can instead make a common inactive mode the global minimum; measuring that mode
gives zero divergence. These tests do not refute the sealed scale and do not justify an arbitrary
small-regularizer substitution.
    Finally, the theorem does not give ηD     c = 1 − d away from d = 0. The binary channel with

columns (0.9, 0.1) and (0.2, 0.8) has complete coefficient 1/2, whereas 1−d = 7/10. The known upper
can be strict. Likewise, appending a marked replacement outcome of mass 0.1 to a zero-Doeblin
channel invalidates measuring a near-f event on every output: that common outcome masks the rare
probability. Setting its effect to zero retains its entire mass in the complement and gives a measured
limit 0.9 log 2 for this marked example. The failed first protocol remains in the supplement. No
formula for a general positive-d optimum, robust communication advantage, capacity or optimal
copy complexity is inferred.


8    Certified finite evidence and limitations
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
                          k              Di               Db          Db /Di
                          8   1.0909434742     0.6511496162    0.5968683361
                         32   0.8384165205     0.6834417750    0.8151578103
                        256   0.7195237121     0.6919467548    0.9616733168

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


                                                 17
and discrimination of the hypotheses are different tasks; no exponential lower bound for every
discrimination strategy is inferred. The fixed-alphabet construction removes vanishing input relative
entropy from one family; it does not remove conditioning and rare-event costs or imply small
one-shot error when trace distance vanishes.


9    Fixed-point decay and the scope of a uniform bound
Set n = 3 and regard Φ = N−1/2 ⊗ id3 as one fixed channel on M9 . It is unital and Hilbert–Schmidt
selfadjoint, and its powers converge to

                                        E(T ) = IA /3 ⊗ TrA T.

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




                                                   18
A     Model assessments and review context
Earlier exact-PDF assessments of preceding versions are public at AIRR version1 and AIRR version2.
They do not assess this new manuscript. The present exact PDF still requires a full assessment; no
preceding numerical score is inherited. The earlier version, complete report and objections remain
immutable.
    The added general-support derivation and technical audit are dossiers1134/1136. The latter
reconstructed the support inverse, exact Schur bounds and binary readout, and established the
uniform-in-channel corollary at fixed input dimension. It also refuted the universal maximum-
overlap selector and retained the first failed full-support measurement extension, altered-regularizer
examples and checker incidents. These are technical evidence with shared context and filesystem,
not an independent manuscript grade. Twenty rational support controls, nine directed interval cases
and ten complex high-precision cases have their bounded scopes stated in that report; numerical
diagnostics are not retrospectively relabelled as certificates.
    The CQ extension is derived in dossier1152 and technically audited in dossier1157. That audit
reconstructed the operator-valued factorization, the range-restricted resolvent and the joint graph
measurement, including mixed ranks and a kernel of T . It supplied directed finite comparisons with
the trace coefficient and an exact NPT effect. It also refuted an early explanation of nonuniformity:
the binary whitened Gram is the identity, while S and A−1 Z carry the problematic conditioning.
The corrected argument appears in Section 6; the false earlier statement remains in the archived
input. A claimed stopped-process receipt was not present in that input. A later poll returned
successful completion of the original symbolic run; correction1164 records the observation and the
missing original-output hash without inventing a termination record. These corrections do not alter
the frozen older versions or create independent votes.
    This manuscript asserts no numerical model grade. Any assessment must be bound to its exact
PDF and exposed with its full report and context; grades attached to other PDFs do not apply.
A technical component audit is distinct from a manuscript assessment, human peer review and
editorial acceptance. None implies either of the others.
    The named author directed substantial OpenAI Codex assistance in derivation, writing and
numerical work. Completed component audits reconstructed the binary and simplex arguments
and preserved both favorable and adverse controls. The requested reviewer configuration was
GPT-6 Astra xhigh. The evaluators had prior participation, reused contexts and shared filesystem
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


                                                 19
only in disposable execution copies, with original and executed hashes logged. Own derivations,
code, reports and source metadata form the supplement; third-party paper corpora and private
credentials are excluded.
    A provenance correction is retained explicitly: an earlier incident narrative claimed preservation
of malformed serialization bytes, but the saved first-control file is a valid JSON identical to the final
one. Those malformed historical bytes are not evidenced. The original narrative, unchanged files,
auditor objection and correction are all preserved; this discrepancy does not change the mathematical
parameters or certified results.


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

[11] I. George, C. Hirche, T. Nuradha and M. M. Wilde, Quantum Doeblin coefficients: in-
     terpretations and applications, Quantum 10 (2026), 2115, doi:10.22331/q-2026-05-22-2115;
     arXiv:2503.22823v3. Selected definitions and contraction propositions inspected, not the entire
     article.

                                                   20
[12] D. Lee, W. Lu, A. Makur and J. Singh, Doeblin curves, IEEE Transactions on Information
     Theory 72 (2026), 3556–3596; arXiv:2606.19859v1. Abstract, introduction and selected initial
     definitions inspected; full proofs not audited.

[13] C. Hirche, Quantum estimation, channel orders, and private capacity, arXiv:2610.03706v1 (2026).
     Selected order and coherent-estimation passages inspected in audit1157; not the complete
     article or Appendix A.1.




                                                21
