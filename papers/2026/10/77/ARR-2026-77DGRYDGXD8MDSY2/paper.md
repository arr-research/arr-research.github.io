# Sharp reference-assisted contraction for the minimal quantum Fisher metric

Machine-readable rendition of canonical eight-page paper.pdf. SHA256 b4728f44f7af59809be26e0eba957336695ff34cfc3cb10c17fcfa06ffb93381.

Sharp reference-assisted contraction for the minimal quantum Fisher
                               metric
                                            Lluis Eriksson

                                           27 October 2026


                                                   Abstract
         We derive a harmonic-weight contraction bound for random-unitary channels on pairs with
     the same uniform-twirl image. It applies to every operator-convex Petz divergence on faithful
     states and is uniform over finite quantum reference systems. For a qubit depolarizing channel
     with retained amplitude 0 < λ < 1, we identify the exact complete equal-reference contraction
     coefficient of both the minimal quantum Fisher metric and the triangular Petz divergence:
     3λ2 /(1 + 2λ). The lower bound uses an explicit qubit–qutrit ladder state, a partial-trace-zero
     tangent, and an ordered faithful regularization. Thus the general Petz upper bound is sharp as a
     bound uniform over that family. At λ = 1/2 it equals 3/8. This does not determine the relative-
     entropy or mutual-information coefficient. We include a finite rational triangular-divergence
     witness above 1/3, explain a limitation of scalar-centering proofs, and preserve failed auxiliary
     variance and numerical routes.


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

                                       χ2min (ρ∥σ) = gσSLD (ρ − σ).                                      (2)

For an operator-convex f : (0, ∞) → R, f (1) = 0, the Petz divergence is

                                  Df (ρ∥σ) = ⟨σ 1/2 , f (Lρ Rσ−1 )σ 1/2 ⟩.                               (3)

We will also use the distinct finite divergence

                                      (x − 1)2
                           f△ (x) =            ,       D△ (ρ∥σ) = Df△ (ρ∥σ).                             (4)
                                       x+1

                                                      1
Although (2) and (4) have proportional local forms, they are not the same finite divergence. Nor do
we identify either with the Bures distance or its geodesic contraction.
   For a local channel N , define the complete equal-reference coefficient

                                                                   Df (N (ρ)∥N (σ))
                               ηfc (N ) =            sup                            .                 (5)
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
                                ′                     2
                       f (x) = f (1)(x − 1) + c(x − 1) +                  dµ(t),                    (6)
                                                           [0,∞) x + t

where c ≥ 0, µ is positive and (1 + t)−1 dµ(t) < ∞. Writing Z = ρ − σ, for states of the same trace
                              R

this gives                                     Z
                      Df (ρ∥σ) = c Tr Z 2 σ −1 +                   ⟨Z, (Lρ + tRσ )−1 Z⟩ dµ(t).        (7)
                                                           [0,∞)

We do not claim this representation as a contribution.

Lemma 1. For positive definite Q, the inverse quadratic form F (Q, Z) = ⟨Z, Q−1 Z⟩ is jointly
convex in Q, Z, for arbitrary complex vectors Z.

Proof. Use the variational identity

                                 F (Q, Z) = sup{2 Re⟨Z, Y ⟩ − ⟨Y, QY ⟩}.
                                                 Y

Each expression inside the supremum is affine in Q, Z. The same identity also shows that for any
trial Y , with e = Z − QY ,

                              F (Q, Z) = 2 Re⟨Z, Y ⟩ − ⟨Y, QY ⟩ + ⟨e, Q−1 e⟩.                         (8)



Theorem 2 (Harmonic cancellation). Let U1 , . . . , Um be local unitaries, m ≥ 2, and let
                         m                           m
                     1 X                             X                                  X
                E=       AdUj ,             Nw =           wj AdUj ,         wj > 0,        wj = 1.
                     m
                        j=1                          j=1                                j



                                                            2
For faithful states ρ, σ satisfying E(ρ) = E(σ), and every nonaffine operator-convex f with f (1) = 0,

                                                                             m2
                   Df (Nw (ρ)∥Nw (σ)) ≤ h(w)Df (ρ∥σ),            h(w) = 1 − P −1 .                   (9)
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
                                j                        j

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


3    Depolarization and the exact minimal-metric coefficient
For a d-dimensional unitary error basis, m = d2 , the uniform twirl is the local replacer EA (X) =
IA /d ⊗ TrA X. With w0 = [1 + (m − 1)λ]/m and wj = (1 − λ)/m for j ̸= 0, Theorem 2 gives

                                                     (d2 − 1)λ2
                                        hd (λ) =                 .                                  (10)
                                                   1 + (d2 − 2)λ
Equal twirl images are precisely equal reference marginals. For qubits, (10) is sharp for the minimal
metric and (4).

                                                     3
Theorem 4 (Exact complete coefficients for a qubit). Let 0 < λ < 1 and Nλ (X) = λX + (1 −
λ)IA /2 ⊗ TrA X, with |A| = 2. Then

                              c                                                3λ2
                             ηSLD                        c
                                  (Nλ ) = ηχc 2 (Nλ ) = η△ (Nλ ) =                  .              (11)
                                               min                           1 + 2λ
A reference of dimension three suffices to approach these suprema. No assertion is made that three
is the smallest sufficient dimension.

Proof. The upper bounds follow from Theorem 2 with the four Pauli conjugations and their
depolarizing weights. It remains to prove the lower bounds.
   In the ordered basis (|00⟩, |01⟩, |02⟩, |10⟩, |11⟩, |12⟩), fix e > 0 and define

                                                                                    aa† + bb†
                   a = (1, 0, 0, 0, e, 0)T ,   b = (0, e, 0, 0, 0, 1)T ,     σe =              .
                                                                                    2(1 + e2 )

The vectors are orthogonal and have the same norm, so Pe = 2σe is a rank-two projection. Let Ze
and J be                                                   
                                     0    −1              0 1
                             Ze =              ,    J=          .
                                    −1 −2e                1 0

      the Hermitian 6 × 6 matrix ∆e by its two nonzero blocks: Ze on indices (0, 4) and −JZe J =
Define
 2e 1 on (1, 5). All other entries vanish. Direct multiplication gives
 1 0

                  TrA ∆e = 0,                                  (I − Pe )∆e (I − Pe ) = 0,          (12)
                    Tr ∆2e = 4 + 8e2 ,                                                  2
                                                                          Tr(Pe ∆e Pe ) = 8e .2
                                                                                                   (13)

The SLD form at this nonfaithful base is understood by retaining the support–support and support–
kernel terms; the kernel–kernel terms vanish by (12). The two positive eigenvalues are 1/2, so (13)
yields
                        gσSLD
                           e
                              (∆e ) = 4 Tr ∆2e − 2 Tr(Pe ∆e Pe )2 = 16(1 + e2 ).               (14)
   The reference marginal is
                                                     diag(1, 2e2 , 1)
                                           σe,R =                     .
                                                       2(1 + e2 )
On indices (0, 4), the output base is
                                                                  
                                              1           1 + λ 2λe
                                     We =                            .                             (15)
                                          4(1 + e2 )       2λe 2e2

On (1, 5) it is JWe J. The other two singleton directions have zero tangent. For e > 0 and 0 < λ < 1,
the output is faithful: the block determinant is positive because 1 + λ − 2λ2 = (1 − λ)(1 + 2λ) > 0,
and the singleton entries are positive.
    Solving the two-dimensional Sylvester equation We Y + Y We = 2Ze , and using the two mirrored
blocks, gives
                          SLD                 16λ2 (1 + e2 )(4e2 λ + 2e2 + 3λ + 3)
                         gN λ (σe )
                                    (λ∆ e ) =                                      .             (16)
                                                     (2λ + 1)(2e2 + λ + 1)
This is a 2 × 2 linear calculation, not an optimization claim. Dividing by (14) gives

                                               λ2 (4e2 λ + 2e2 + 3λ + 3)
                                   Re (λ) =                              .                         (17)
                                                (2λ + 1)(2e2 + λ + 1)

                                                        4
In particular,
                        3λ2                 4e2 λ2 (1 − λ)
                             − Re (λ) =                       −→ 0           (e ↓ 0).            (18)
                      1 + 2λ            (2λ + 1)(2e2 + λ + 1)
    We now realize the limits through faithful inputs. For fixed e > 0, set σe,ξ = (1 − ξ)σe + ξI6 /6,
0 < ξ < 1. Its eigenspaces are those of σe . Equation (12) implies that its input SLD form converges
to (14) as ξ ↓ 0; there are no diverging kernel–kernel contributions. The output tends to the faithful
Nλ (σe ), so its SLD form converges by finite-dimensional continuity. Consequently faithful tangent
ratios approach Re (λ). Sending e ↓ 0 afterwards proves the SLD lower bound. The equality with the
complete chi-square coefficient follows from the exact quadratic dependence in (2) and sufficiently
small faithful perturbations.
    For the triangular Petz divergence, at each fixed faithful σe,ξ choose ρt = σe,ξ + t∆e . For
sufficiently small nonzero real t, this is a faithful density matrix with the same reference marginal.
Its resolvent representation gives

                          D△ (ρt ∥σe,ξ )                                  1
                    lim                  = ⟨∆e , (Lσe,ξ + Rσe,ξ )−1 ∆e ⟩ = gσSLD (∆e ),
                    t→0        t2                                         2 e,ξ
and the corresponding output limit is analogous. Thus take t → 0, then ξ ↓ 0, and finally e ↓ 0.
This supplies the lower supremum over faithful finite pairs in (5). There is no exchange of these
limits and no assumed uniform continuity at a singular reference.

Corollary 5. For the qubit depolarizing channel, 3λ2 /(1 + 2λ) is the smallest bound valid uniformly
over all nonaffine operator-convex Petz generators and faithful equal-reference pairs.

Proof. Theorem 2 gives the uniform upper; the member f△ attains the supremum in Theorem 4.
This does not assert that every generator has that coefficient.

   At λ = 1/2, (11) equals 3/8. The ordinary unital-qubit contraction coefficient is λ2 , by Hiai–
Ruskai [1], Theorem 6.1. At λ = 1/2, the ordinary value is 1/4, compared with the complete
equal-reference value 3/8. The stabilization considered here retains equal reference marginals and
optimizes over their quantum correlations.


4    A limitation of changing the unitary decomposition
A narrow method limitation helps distinguish the remaining relative-entropy problem from a
representation search.
                                                                                   Pn
Proposition 6. Fix 0 < λ < 1 and let E(X)    P = Tr(X)I/d. Represent E = j=1 qj AdUj as a
finite convex combination, with qj ≥ 0 and j qj = 1; discard zero-weight atoms. Consolidate all
identity conjugations into an atom of total weight r; if absent, take r = 0. Use the induced common
representation of N = λ id +(1 − λ)E. Among all such representations, a single scalar cancellation
of the form wj − aqj , optimized by inverse-quadratic convexity, cannot give an upper smaller than
(10). An error basis attains that method-family minimum.

Proof. The scalar minimum is 1 − 1/S, S = j qj2 /wj , because j (wj − aqj )2 /wj = 1 − 2a + a2 S.
                                             P                     P
The induced weights are w0 = λ + (1 − λ)r and wj = (1 − λ)qj otherwise. Hence

                                   r2       1−r                       λ2 (1 − r)
                       S=                 +      ,         h(r) =                 .
                              λ + (1 − λ)r 1 − λ                    λ + (1 − 2λ)r


                                                     5
Using normalized Choi states, J(E) = Id2 /d2 and J(id) = |Ω⟩⟨Ω|. Positivity of the other Choi terms
gives J(E) − r|Ω⟩⟨Ω| ⪰ 0, so r ≤ 1/d2 . On this interval,

                                                   λ2 (1 − λ)
                                   h′ (r) = −                    < 0.
                                                [λ + (1 − 2λ)r]2

The smallest possible scalar bound therefore occurs at r = 1/d2 and equals (10), attained by a
unitary error basis.

   This concerns the specified common-representation scalar method. It does not exclude other
representations, state-dependent cancellations, stronger operator inequalities, or a smaller true
coefficient for relative entropy.


5    Finite certificates, failures, and unresolved questions
The accompanying evidence distinguishes analytical arguments from finite diagnostics. The exact
symbolic checks verify the projector and partial-trace identities in (12)–(13), the channel block (15),
the Sylvester equation, and the rational ratio and gap. Nine faithful finite pairs were also evaluated
at 75 decimal digits. They are controls on the construction, not the proof of its universal upper or
sharp supremum.
    A separate finite rational certificate at λ = 1/2 gives faithful qubit–qutrit states with the same
reference marginal and
                              D△ (N (ρ)∥N (σ))                         1
                                                 > 0.348913969797 > .                              (19)
                                  D△ (ρ∥σ)                             3
The certificate stores the matrices and rational trial Sylvester solutions. If Q ⪰ cI, (8) bounds the
remainder by ∥e∥22 /c. Exact rational input/output intervals then certify (19), without treating a
floating-point eigenvalue as a certificate.
    We also preserve a failed route through conditional variance. For

                         Vσ (H) = inf Tr σ(H − IA ⊗ B)2 ,          TrA H = 0,
                                  B=B †

a proposed sufficient inequality was Vσ (H) ≤ 2 Tr[EA (σ)H 2 ]. A rational qubit–qutrit certificate
instead proves a ratio greater than 2.99311283224. The minimizer solves a reference Sylvester
equation, and the same residual method certifies the violation. This refutes the auxiliary inequality;
it does not directly refute an SLD channel coefficient or the relative-entropy conjecture.
    Exploration included fixed-budget local optimizations, some terminating at their limits or
abnormally, and unsuccessful simpler families. These outcomes are retained. The reversed ladder
and the proof above replace reliance on optimized values. No exhaustive computational search or
independently certified computational campaign is claimed.
    The relative-entropy complete coefficient at λ = 1/2 is not determined here. In particular, the
triangular example cannot be transferred to BKM by comparing the sizes of their metrics: ordering
metrics does not order their contraction ratios. Our results identify an obstruction to a bound
uniform over all Petz generators, while leaving a generator-specific relative-entropy improvement
open. No capacity, tensorization, optimal statistical protocol, geodesic-distance contraction or
attained singular maximum is asserted.




                                                    6
Evidence availability and replay. A version-pinned public supplement contains the scripts,
rational certificates, complete component report and retained objections. Its MANIFEST1001.json
binds the LF transport files to their sealed-original hashes. Copy the files to a temporary directory,
install the pinned requirements.txt, and run python symbolic993.py, python verify993.py,
and python verify-certificates991.py. These programs write their reports beside the scripts.
The later, explicitly speculative Pauli extension in the same research collection is outside the claims
and assessment of this manuscript.


6    Relation to prior work
Hiai–Ruskai [1] develop contraction comparisons, monotone metrics and ordinary qubit formulas.
Their resolvent representation is the starting tool here. Cao–Lu [2] study quantum chi-square SDPIs,
tensorization with specified product reference states and ordinary qubit examples. Those hypotheses
are distinct from optimization over arbitrary quantum references in (5). George et al. [3] formulate
equal-reference coefficients and bound complete trace-distance contraction through quantum Doeblin
coefficients. George–Tomamichel [7] treat fixed-base and ordinary optimized chi-square coefficients
and associated spectral algorithms. Their fixed-base optimization does not itself determine the
supremum over correlated bases and all reference dimensions under TrA Z = 0. The unrestricted
ordinary coefficient of N ⊗ idR can instead equal one because a tangent may reside solely in R;
it is not the coefficient in (5). Belzig et al. [4] distinguish ordinary channel comparisons from
quantum-reference mutual-information questions. Hirche et al. [5] distinguish mutual-information,
complete equal-reference and conditional coefficients; these distinctions prevent interpreting our
triangular result as a relative-entropy or mutual-information solution. Gao–Zhao [6] concern entropy
contraction toward a conditional expectation, another important nearby optimization that is not
identified with (5).
    These references are included to delimit the quantities and established machinery, not to suggest
that the surrounding literature was exhaustively audited. The bibliographic search was directed.
Certified worldwide originality, independent human review and formal proof verification are not
claimed.


7    Model assessments and review context
The named author directed substantial OpenAI Codex assistance in derivation, writing and numerical
work. Technical audit 988 and full-draft review 998 were requested with GPT-6 Astra at xhigh effort
in reused conversational contexts and a shared filesystem. Requested configuration does not attest
effective runtime identity, isolation or independence. Review 998 evaluated the earlier exact seven-
page draft; the present corrections address its supplement, bibliography and hypothesis-precision
objections. Its score is not automatically assigned to this corrected PDF. Component checks do not
constitute a full assessment of this exact manuscript. Any actual reports must identify their exact
input hashes, retained objections, context reuse and scope. No score from an earlier manuscript is
transferred to this text; no predicted assessment score is claimed. The author remains responsible
for the claims, attribution and publication decision. This section distinguishes AI assessment,
arithmetic replay, formal verification, human peer review and editorial acceptance.




                                                  7
References
[1] F. Hiai and M. B. Ruskai, Contraction coefficients for noisy quantum channels, arXiv:1508.03551v1 (2015).
    https://arxiv.org/abs/1508.03551v1.
[2] Y. Cao and J. Lu, Tensorization of the strong data processing inequality for quantum chi-square divergences,
    Quantum 3, 199 (2019). https://doi.org/10.22331/q-2019-10-28-199.
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




                                                       8
