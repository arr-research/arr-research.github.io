# Sharp marginal-erasure bounds and positive completion of nonunital quantum channels

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
Sharp marginal-erasure bounds and positive completion
                 of nonunital quantum channels
                                          Lluis Eriksson

                                         24 October 2026


                                              Abstract

                                                                             p part of one local
         We determine the exact Frobenius conditioning of deleting the traceless
     matrix algebra on Cm ⊗ Ck . For p1 ≤  r < m, the  inverse constants are  m/(m − r) for two
     states of rank at most r, and (m + r)/(m − r) for one such state against an arbitrary
     density matrix. Both are attained, independently of k ≥ 2; at rank m exact collisions
     occur. The one-sided estimate follows from a scalar optimization combining positivity,
     trace control and the partial-trace norm. It yields a noise and spectral-tail bound for
     convex positive completion. For normalized Choi matrices, the retained coordinates are the
     action of a trace-preserving channel on traceless inputs. Consequently this action identifies
     every channel of Kraus rank below its input dimension among all channels, without a
     unitality assumption. For square channels we express the same conclusion through a
     complete exact unitary 2-design of average gate fidelities. The rank threshold is sharp,
     whereas optimal conditioning within the trace-preserving subclass is left open. The fidelity
     frame identities and general kernel/inertia method are prior work; no compressed-sampling
     or new randomized-benchmarking noise guarantee is asserted.


1    Question, contribution and antecedents
Average gate fidelities with unitary reference gates do not linearly determine an arbitrary
quantum channel: they miss its translation, or action on the maximally mixed input. Positivity
can nevertheless make that missing part unique when the channel has sufficiently small Kraus
rank. We quantify this mechanism by first solving an unrestricted state-space problem exactly.
   Let Sm,k denote the density matrices on Cm ⊗ Ck , and set

                           K = {Im ⊗ B : B ∈ Herm(Ck ), Tr B = 0}.

Here K is the traceless Hermitian part of a local algebra, not itself an algebra under multi-
plication. Let P be its Frobenius-orthogonal projection and Q = id −P . Our principal result
computes the largest ratio ∥ρ − σ∥F / ∥Q(ρ − σ)∥F under either one or two rank constraints.
This distinction matters: positivity-constrained reconstruction usually produces a competitor
with unrestricted rank.
    The reduction of low-rank identification to the inertia of a measurement kernel is classical
in state tomography [1] and channel tomography [2]. In particular, Gutoski and Johnston
construct small families of interactive observables identifying low-Kraus-rank channels among
all channels. We do not improve their observable counts; we study the conditioning of a
particular fixed omitted subspace. Kimmel et al. recover the unital block using randomized
benchmarking [3]; their single-qubit complete-positivity lemma has a corrected proof [4]. Roth
et al. provide a unitary-design frame for unital trace-preserving maps and compressed recovery
guarantees for quantum gates [5]. We use the classical second-moment identity explicitly and
separately from our completion inequality.


                                                  1
```

---

## Page 2

```text
The proposed contribution is the pair of exact local-erasure constants, their state attain-
ers, and the resulting quantitative completion statement without a unitality promise. The
elementary proof is included in full. These comparisons delimit the claim; they do not certify
worldwide priority.


2    Exact conditioning in state space
All matrix spaces below are real Hilbert spaces of Hermitian matrices with inner product
Tr(XY ). The Frobenius norm is ∥X∥F . A zero denominator and nonzero numerator mean an
                       (r)
infinite ratio. Write Sm,k for states of rank at most r.
Theorem 1 (Exact local-erasure constants). Let m ≥ 1, k ≥ 2 and r ≥ 1 be integers. For
1 ≤ r < m,
                                            ∥ρ − σ∥F                     m
                                                                    r
                                     sup               =                    ,                     (1)
                                       (r) ∥Q(ρ − σ)∥F                  m−r
                                 ρ,σ∈S  m,k
                                     ρ̸=σ
                                                                             s
                                               ∥ρ − σ∥F                          m+r
                               sup                        = Cm,r :=                  .            (2)
                           (r)
                       ρ∈Sm,k , σ∈Sm,k
                                              ∥Q(ρ − σ)∥F                        m−r
                            ρ̸=σ

Both suprema are attained. For r ≥ m both are infinite. Thus m = 1 has no finite positive-rank
regime.
   We first record the projection and the standard inertia reduction. The notation n+ (D)
and n− (D) counts positive and negative eigenvalues with multiplicity.
Lemma 2. For any Hermitian D,
                                       Im           Tr D
                                                                            
                                  PD =    ⊗ TrA D −      Ik .
                                       m             k
In particular, for Tr D = 0,
                                 Im                                      1
                       PD =         ⊗ TrA D,               ∥P D∥2F =       ∥TrA D∥2F .            (3)
                                 m                                       m
                                          √
For arbitrary matrices X, ∥TrA X∥F ≤ m ∥X∥F . If D = ρ − σ with rank ρ ≤ r, then
n+ (D) ≤ r. If also rank σ ≤ r, then n− (D) ≤ r.
Proof. The proposed P D belongs to K, and its difference from D is orthogonal to every Im ⊗ B
with Tr B = 0, by the defining identity of partial trace. This proves the projection formula.
For the norm estimate, in a product basis Cauchy–Schwarz gives
                                               2
                                                                |Xai,aj |2 ≤ m ∥X∥2F .
                         X X                            X
                                      Xai,aj       ≤m
                         i,j     a                      a,i,j

If a positive eigenspace of ρ − σ had dimension greater than r, it would meet ker ρ nontrivially.
On that kernel its quadratic form is nonpositive, a contradiction. Changing sign proves the
last claim.

                          ̸ 0 be Hermitian with Tr D = 0, and write its spectral decompo-
Proof of Theorem 1. Let D =
sition as D = D+ − D− with orthogonal positive parts. Set

                 τ = Tr D+ = Tr D− > 0,                    a2 = ∥D+ ∥2F ,        b2 = ∥D− ∥2F .

                                                         2
```

---

## Page 3

```text
If n+ (D) ≤ r, then a2 ≥ τ 2 /r. The positive matrices R = TrA D+ and S = TrA D− both have
trace τ . Positivity implies Tr(RS) ≥ 0 and ∥R∥2F , ∥S∥2F ≤ τ 2 . Lemma 2 also gives ∥S∥2F ≤ mb2 .
Consequently
                           ∥TrA D∥2F = ∥R − S∥2F ≤ τ 2 + min{τ 2 , mb2 }.                     (4)
No commutation or orthogonality of the two marginals is assumed.
   Put t = b2 /τ 2 . Equations (3)–(4) yield

                           ∥P D∥2F 1/m + min{1/m, t}    2r
                               2 ≤      1/r + t
                                                     ≤
                                                       m+r
                                                           .                                        (5)
                            ∥D∥F

Indeed the middle expression is increasing for 0 ≤ t ≤ 1/m and decreasing for t ≥ 1/m, since
r < m. Its maximum is at t = 1/m. Orthogonality of P and Q now proves (2) as an upper
bound for every difference in its stated domain.
   For sharpness, choose a rank-r input projector R0 and orthogonal output unit vectors u, v.
The states
                                 R0                   Im
                            ρ=       ⊗ |u⟩⟨u|,    σ=     ⊗ |v⟩⟨v|                         (6)
                                  r                    m
have ranks r, m. For their difference,
                               1  1                  2                    1  1
                     ∥D∥2F =     + ,     ∥P D∥2F =     ,    ∥QD∥2F =        − .
                               r m                   m                    r m
They attain (2) and all bounds in (5).
   If both inertia indices are at most r, then a2 , b2 ≥ τ 2 /r. Instead of (4) use

                                  ∥TrA D∥2F ≤ 2τ 2 ≤ r(a2 + b2 ).

The hidden fraction is at most r/m, which proves the upper bound in (1). It is attained by

                                  R0                       R0
                             ρ=      ⊗ |u⟩⟨u|,       σ=       ⊗ |v⟩⟨v|,
                                  r                        r

for which ∥D∥2F = 2/r and ∥P D∥2F = 2/m. Finally, take R0 = Im and r = m. These distinct
rank-m states have QD = 0. They remain admissible for every r ≥ m, establishing the infinite
regime, including m = 1.

   Every nonzero member of K has at least m positive and m negative eigenvalues. Thus
the qualitative threshold also follows immediately from the classical kernel/inertia criterion.
The estimates above quantify the angle between that kernel and the relevant difference cones,
rather than merely showing they do not intersect.


3    Approximate rank and convex completion
                                                                                  P
For a density matrix ρ with eigenvalues in decreasing order, define τr (ρ) =          i>r λi (ρ).

Proposition 3 (Spectral tails). For 1 ≤ r < m, every pair of density matrices ρ, σ obeys
                                                   √
                  ∥σ − ρ∥F ≤ Cm,r ∥Q(σ − ρ)∥F + 2(Cm,r + 1)τr (ρ).                       (7)

Let F be any compact convex subset of density matrices containing ρ. If y = Qρ + e, ∥e∥F ≤ ϵ,
then every minimizer ρb of ∥Qσ − y∥F over σ ∈ F satisfies
                                                √
                           ∥ρb − ρ∥F ≤ 2Cm,r ϵ + 2(Cm,r + 1)τr (ρ).                       (8)


                                                 3
```

---

## Page 4

```text
Proof. Let s = 1 − τr (ρ) > 0, and let ρr be the top-r spectral truncation of ρ divided by s. At
an eigenvalue tie any spectral choice is allowed. Then
                                               X  λ i 2
                       ∥ρ − ρr ∥2F = τr (ρ)2
                                                                X
                                                            +         λ2i ≤ 2τr (ρ)2 .
                                               i≤r
                                                     s          i>r

Apply (2) to ρr , σ, then use the triangle inequality and the contraction property of Q to obtain
(7). A minimizer exists by compactness. Its residual is at most that of the feasible truth, hence
∥Q(ρb − ρ)∥F ≤ 2ϵ. Substitution proves (8).

   The truncation ρr need not belong to F. The proof is valid because (2) compares it with
every density matrix. This detail matters for Choi matrices: normalized spectral truncation
does not in general preserve trace preservation. For example, the 3 → 2 channel with Kraus
operators                                  !                       !
                                    1 0 0                  0 0 1
                           K0 =              ,     K1 =
                                    0 1 0                  0 0 0
                                                                                             √
has Choi eigenvalues 2/3, 1/3. Its normalized top-one truncation is the state of (|00⟩+|11⟩)/ 2,
whose input marginal is diag(1/2, 1/2, 0) rather than I3 /3. Convexity makes the optimization
a convex problem; the proof of the error bound uses compactness and feasibility, without
imposing a rank constraint on the minimizer.


4    Channel completion from the traceless-input action
Let Φ : Mm → Mk be completely positive and trace preserving (CPTP). Use input–output
tensor order and the normalized Choi matrix

                                                                  1 m−1
                                                                     X
                     JΦ = (id ⊗Φ)(|Ωm ⟩⟨Ωm |),           |Ωm ⟩ = √       |a, a⟩.
                                                                   m a=0

Then JΦ ≥ 0, Tr JΦ = 1, Trout JΦ = Im /m, and rank JΦ is the minimum Kraus rank.
   Choose Frobenius-orthonormal bases Fi and Gj of the real spaces of traceless Hermitian
input and output matrices. Define

                                     T (Φ)ji = Tr[Gj Φ(Fi )].

These bases can contain imaginary entries. The input transpose in
                                                            1
                                  Tr[JΦ (FiT ⊗ Gj )] =        T (Φ)ji                         (9)
                                                            m
is essential. It follows by expanding JΦ = m−1 a,b |a⟩⟨b| ⊗ Φ(|a⟩⟨b|).
                                                     P

    For two TP maps the identity and input-only coefficients of D = JΦ − JΨ vanish. The
projection P removes precisely the output-only traceless coefficients, so orthonormal expansion
gives
                                              1
                             ∥Q(JΦ − JΨ )∥F =    ∥T (Φ) − T (Ψ)∥F .                        (10)
                                              m
Thus T is exactly the retained nonconstant Choi information. The omitted translation is
Φ(Im /m).

Theorem 4 (Low-Kraus-rank completion). If rank JΦ ≤ r < m, then for every CPTP
Ψ : Mm → Mk ,
                                   Cm,r
                     ∥JΦ − JΨ ∥F ≤      ∥T (Φ) − T (Ψ)∥F .                  (11)
                                    m

                                                     4
```

---

## Page 5

```text
In particular T (Φ) identifies Φ among all CPTP maps. The uniform rank threshold r < m is
sharp for every k ≥ 2. For Tobs = T (Φ) + N with ∥N ∥F ≤ δ, every least-squares fit over all
CPTP maps satisfies, for every 1 ≤ r < m,
                                            2Cm,r    √
                          b − JΦ
                         JΦ
                                    F
                                        ≤
                                             m
                                                  δ + 2(Cm,r + 1)τr (JΦ ).                 (12)

Proof. Combine Theorem 1 and (10). For the endpoint consider the pure-output replacers
Φu (X) = Tr(X)|u⟩⟨u|. Each has T = 0 and Choi rank m; distinct output states give distinct
channels with identical data.
    For the noisy result, the feasible Choi matrices form a compact convex set with marginal
Im /m. Insert Tobs /m into the correlation coordinates, together with the known identity coeffi-
cient and zero input-only coefficients. This is QJΦ + e with ∥e∥F ≤ δ/m. The residual problem
differs from the displayed least-squares problem only by the factor 1/m, so Proposition 3
applies.

    The state-space constants are exact; (11) is a valid upper bound on the smaller fixed-
marginal class, not an optimal channel constant proved here. In (6) the first input marginal
is R0 /r, so that attainer is not TP for r < m. For rectangular maps some rank classes are
empty: r Kraus operators of size k by m require rk ≥ m. For square maps Kraus rank one
means a unitary channel, whose translation is zero.

4.1   Why one must not impose unitality
For square dimensions let the conventional unital part be the Hermiticity-preserving TP map
                                                     Tr X
                             Φu (X) = Φ(X) −
                                                                     
                                                          Φ(Im ) − Im .                    (13)
                                                      m
It fixes Im and agrees with Φ on traceless inputs.

Corollary 5. If Φ : Mm → Mm is nonunital and has Kraus rank less than m, then Φu is not
completely positive.

Proof. Otherwise Φu would be a distinct CPTP channel with T (Φu ) = T (Φ), contradicting
Theorem 4.

   For a concrete family, let m ≥ 3 and

                     K0 = diag(1, . . . , 1, 3/5),       K1 = (4/5)|0⟩⟨m − 1|.

The two linearly independent Kraus operators satisfy a Ka† Ka = Im and define a nonunital
                                                            P

channel of rank two. Writing B = Φ(Im )−Im = (16/25)(|0⟩⟨0|−|m−1⟩⟨m−1|), its unital-part
Choi matrix is JΦu = JΦ − Im ⊗ B/m2 . For any 1 ≤ i ≤ m − 2,
                                                          16
                                  ⟨i, 0|JΦu |i, 0⟩ = −        < 0.
                                                         25m2
This illustrates the failure of an unjustified unital constraint. It is not a claim that higher-
dimensional failure of complete positivity was previously unknown. There is no conflict with
the corrected qubit lemma of [4]: below the qubit threshold the only square channels are
unitary, and the interior index in this example does not exist for m = 2.




                                                     5
```

---

## Page 6

```text
5    Complete average-gate-fidelity data
In this section input and output dimensions both equal m ≥ 2. Let U1 , . . . , UN be a finite
exact unitary 2-design with uniform weights, and put
                                                                                    1 X
                                    Z
         fℓ (Φ) = Favg (Uℓ , Φ) =       ⟨ψ|Uℓ† Φ(|ψ⟩⟨ψ|)Uℓ |ψ⟩ dψ,      ∥z∥2rms =       |zℓ |2 .
                                                                                    N ℓ
                                                                                     P
For a weighted design the same statements use positive weights wℓ with ℓ wℓ = 1 and the
matched norm ∥z∥2rms,w = ℓ wℓ |zℓ |2 . No random subset of this design is used.
                         P

Lemma 6 (Classical design frame, with normalization). For any two CPTP maps on Mm ,
                                                     p
                    ∥Q(JΦ − JΨ )∥F = (m + 1) m2 − 1 ∥f (Φ) − f (Ψ)∥rms .                           (14)

Proof. Set p = m2 − 1 and use the same orthonormal traceless basis Fi on input and output.
Let O(U )ji = Tr[Fj U Fi U † ]. The standard pure-state second moment |ψ⟩⟨ψ|⊗2 dψ = (I +
                                                                      R

SWAP)/[m(m + 1)] gives, for a TP map,

                                                 1   Tr[O(U )T T (Φ)]
                              Favg (U, Φ) =        +                  .                            (15)
                                                 m      m(m + 1)
For completeness the design second moment follows from
                                                      δib        I
                       Z                                                   
                                    †            †
                           (U Fi U ) ⊗ (U Fb U ) dU =     SWAP −   .
                                                       p         m
The Haar twirl lies in the span of I and SWAP; its trace is zero and its trace against SWAP is
δib , which fixes these coefficients. Pairing against Fj ⊗ Fa yields

                                    1 X                     δja δib
                                        O(Uℓ )ji O(Uℓ )ab =         .
                                    N ℓ                       p

A unitary 2-design reproduces this polynomial moment. Apply this identity to ∆T = T (Φ) −
T (Ψ) in (15):
                                                   ∥∆T ∥2F
                         ∥f (Φ) − f (Ψ)∥2rms = 2                  .
                                              m (m + 1)2 (m2 − 1)
Equation (10) proves the claim.

    The frame mechanism is the established unitary-design tomography of [5], with conventions
displayed to prevent a norm or dimension factor from being imported incorrectly.

Corollary 7 (Positive completion from complete design fidelities). If Φ has Kraus rank at
most r < m, then its complete exact-design fidelities identify it among all CPTP maps. For
every such competitor,
                                                     p
                    ∥JΦ − JΨ ∥F ≤ Cm,r (m + 1) m2 − 1∥f (Φ) − f (Ψ)∥rms .

If fobs = f (Φ) + e and ∥e∥rms ≤ ϵ, every minimizer of ∥f (Ψ) − fobs ∥rms over all CPTP maps
obeys
                                                              p
                               b − JΦ
                              JΦ              ≤ 2Cm,r (m + 1) m2 − 1 ϵ
                                            F
                                                  √
                                                + 2(Cm,r + 1)τr (JΦ ).                             (16)

The uniform rank threshold is sharp.

                                                     6
```

---

## Page 7

```text
Proof. The exact-rank statement follows from Theorem 4 and Lemma 6. A residual minimizer
        b − f (Φ)∥rms ≤ 2ϵ; apply (7) and (14) for the approximate-rank statement. Replacers
has ∥f (Φ)
have rank m and fℓ = 1/m for every reference unitary, establishing the endpoint obstruction.


    There is no linear reconstruction of the translation in these fidelities. The additional
conclusion is a nonlinear uniqueness and stability consequence of positivity and rank. The
feasible set in Corollary 7 is all CPTP maps; imposing a unital constraint would discard the
nonunital examples above.


6    Verification, scope and open questions
The analytic proofs establish statements in all declared dimensions. Separate finite exact-
arithmetic controls check the projection, attainers, coherent directions, complex Hermitian
basis transposes, rectangular channels and spectral tails. Such controls are diagnostics, not
substitutes for the proofs. The derivation and this combined manuscript have different review
scopes; no score from an earlier manuscript is assigned to this one.
    Three limitations are central. First, the exact constants are for unrestricted density
matrices; optimal constants on the fixed-input- marginal Choi class remain open. Second,
complete-design fidelities may be numerous. We do not show that a small random Clifford
subset has the required uniform one-sided conditioning for arbitrary low-Kraus-rank nonunital
channels. Third, a deterministic perturbation bound for calibrated fidelities is not a SPAM-
robust experimental protocol. Noise extraction, gauge and calibration must be justified
separately; the guarantees of [3, 5] do not automatically transfer to a larger feasible class.
    These distinctions suggest concrete further problems: determine the optimal fixed-marginal
constants, find sparse fidelity frames with uniform positive-completion guarantees, and obtain
sharper spectral-tail terms under additional channel structure. The present paper establishes
the local-erasure law and its complete-data consequence only.

AI and responsibility disclosure. The named author directed OpenAI Codex assistance
in derivation, writing and exact arithmetic. Requested GPT-6 Astra xhigh audits examined
component arguments with reused context and shared files. Runtime identity and isolation
were not independently attested. No independent human review, Lean formalization, certified
worldwide originality or predicted assessment score is claimed. A full assessment of this exact
combined manuscript has not yet been obtained.

References
[1] C. Carmeli, T. Heinosaari, J. Schultz and A. Toigo, Tasks and premises in quantum state determi-
    nation, J. Phys. A: Math. Theor. 47, 075302 (2014). arXiv:1308.5502.
[2] G. Gutoski and N. Johnston, Process tomography for unitary quantum channels, J. Math. Phys.
    55, 032201 (2014). doi:10.1063/1.4867625.
[3] S. Kimmel, M. P. da Silva, C. A. Ryan, B. R. Johnson and T. Ohki, Robust extraction
    of tomographic information via randomized benchmarking, Phys. Rev. X 4, 011050 (2014).
    doi:10.1103/PhysRevX.4.011050.
[4] S. Kimmel et al., Erratum: Robust extraction of tomographic information via randomized bench-
    marking, Phys. Rev. X 6, 029902 (2016). doi:10.1103/PhysRevX.6.029902.
[5] I. Roth, R. Kueng, S. Kimmel, Y.-K. Liu, D. Gross, J. Eisert and M. Kliesch, Recover-
    ing quantum gates from few average gate fidelities, Phys. Rev. Lett. 121, 170502 (2018).
    doi:10.1103/PhysRevLett.121.170502.



                                                 7
```
