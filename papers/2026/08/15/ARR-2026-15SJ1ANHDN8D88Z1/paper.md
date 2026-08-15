Bayesian Matroid-Union Bounds for Quantum List
                   Discrimination
   Support Congestion, Process Compression, and Exact
               Adaptive–Parallel Phases
                                        Lluis Eriksson

                                         August 2026


                                           Abstract
     In quantum list discrimination a measurement returns at most ℓ candidate labels and
 succeeds when the true hypothesis belongs to the returned list. We derive a hierarchy
 of upper bounds that retains the complete labeled dependence pattern of mixed quantum
 hypotheses and arbitrary priors. To the support subspaces of the hypotheses we associate their
 Rado independent-transversal matroid R. We prove that the vector of true-label inclusion
 probabilities of every ℓ-list measurement belongs to the independence polytope of the ℓ-fold
 matroid union R∨ℓ . Its rank has the closed support-congestion formula
                                                          X        
                             rℓ (A) = min |A \ C| + ℓ dim   ran ρi .
                                    C⊆A
                                                             i∈C

 Thus the Bayes list success is at most the maximum prior weight of a set partitionable into ℓ
 independent support transversals. The result also covers soft lists whose fractional rewards
 have total budget at most ℓ per outcome. A prefix formula gives the bound for arbitrary
 priors and an exact rank-saturation audit for equality of any proposed strategy.
     For uniform priors the rank formula yields an integer failure certificate ∆ℓ = maxC (|C| −
 ℓd(C)) and the precise list size at which this support obstruction disappears. Within
 any process-tester class satisfying the stated unnormalised-Choi trace interface, canonical
 compression transfers the hierarchy without adding a causal-order assumption. We exhibit
 exact attainment families. Orthogonal classes of repeated states attain the arbitrary-prior
 bound for every ℓ. More geometrically, m equiprobable regular-simplex states have exact one-
 guess optimum (m − 1)/m but perfect two-list success: a root-frame POVM reports an edge
 of the simplex and never omits the true vertex. Finally, an exact three-qubit-state example
 shows that a full union matroid does not √   imply the existence of a perfect-list measurement;
 its uniform two-list optimum is (2 + 1/ 3)/3 < 1. The theorem is therefore a support
 obstruction with exact attainments, not a general solution of state exclusion. The proof
 combines standard Rado–Edmonds theory with quantum support inequalities; the ingredients
 themselves are not claimed as new.
     The process extension becomes exact for a complete input-dependent family whose channels
 dephase before preparing a classical output. For M = 2h equiprobable hypotheses, list size
 ℓ = 2s , and q uses, we prove against arbitrary entangled parallel inputs and adaptive quantum
 memories that
                  (ℓ)                                  (ℓ)
                 Ppar (q) = min{1, ℓ(q + 1)/M },     Pad (q) = min{1, ℓ2q /M }.

 Thus perfect list identification needs exactly M/ℓ−1 parallel calls but only log2 (M/ℓ) adaptive
 calls. The fixed parallel transcripts induce partition matroids whose union caps are attained
 cell by cell. This is an exact list/feedback tradeoff in classical channels embedded quantumly,
 not a claim of quantum or indefinite-causal-order advantage.
     For a complete unitary-error ensemble and fixed pure probe, we translate the known optimal
                                                                                       √
 approximate dense-coding law into the present process-list language, Pguess = (Tr ρR )2 /D.


                                                1
      It yields the sharp Schmidt-rank cap r/D and, for independent Weyl histories, exact list
      optima for carrier-only serial, unreferenced parallel, and Bell-assisted wirings. These channel
      theorems turn process compression into resource-resolved exact statements while retaining
      explicit boundaries on prior art and scope.


1    Introduction
Minimum-error quantum discrimination normally asks a measurement to output one label. A
different and useful task permits a set-valued decision: the measurement may return a short
list, and it succeeds whenever the true label is contained in that list. Taking complements turns
this into quantum state exclusion or elimination. That subject has a well-developed semidefinite
formulation and includes unambiguous, minimum-error, and worst-case variants [1]. Multi-state
elimination has also been implemented experimentally [2]. We do not claim the operational task
as new.
     The question addressed here is structural. Suppose the hypotheses are mixed and their
support subspaces overlap in a complicated labeled pattern. How large can the total probability
be that the correct label appears in a list of size at most ℓ? A total Hilbert-space dimension
records only one number. It does not distinguish a dense cluster of dependent, high-prior
labels from independent, low-prior outliers. In the one-label problem this loss is repaired by a
Rado-matroid Bayes bound [3]. Here we show that the full list hierarchy is governed not by an
ad hoc multiple of that bound, but by the successive union powers of the same matroid.
     The connection is exact at the polyhedral level. If si is the conditional probability that label
i appears in the reported list, then for each set A of labels,
                                          X              X
                                 s(A) :=     si ≤ ℓ dim       ran ρi .
                                            i∈A             i∈A

Combining these support inequalities with si ≤ 1 and minimizing over a subset produces precisely
the rank inequalities of the ℓ-fold union of the Rado matroid. Edmonds’ union theorem and
independence-polytope theorem then convert the quantum inequality into a maximum-weight
independent-set bound. This provides, in one statement, arbitrary priors, every finite list budget,
mixed supports, and soft fractional rewards.
   Three consequences make the hierarchy operational rather than merely formal. First, for
equal priors its failure deficit is the integer
                                                              X
                        ∆ℓ = max |C| − ℓd(C) ,     d(C) = dim      ran ρi .
                                C
                                                                       i∈C

Second, this matroid support obstruction vanishes at the explicit density threshold
                                                  
                                               |C|
                                        max          .
                                         C    d(C)
Third, canonical inverse-square-root compression carries the argument unchanged to quantum-
process testers. A fixed tester normalization may describe parallel circuits, adaptive combs, or
more general process-matrix strategies [4, 5, 6].
    Compression by itself is only a converse and does not compare architectures. We therefore
solve one input-dependent channel family exactly. The unknown channel measures a query from
a binary-prefix alphabet and returns membership in the corresponding right-child cylinder. These
cylinders are laminar. For a fixed parallel query tuple, their response fibres form a partition
matroid, so the union bound is attained by reporting the largest-prior labels in each fibre. A
flag-genie argument proves that coherent or entangled inputs cannot improve this value, while
backward induction reduces every adaptive quantum strategy to a classical decision tree. The
resulting all-depth phase diagram separates the linear growth of parallel transcript cells from

                                                    2
the doubling supplied by feedback. Adaptive advantages for channel discrimination, including
entanglement-breaking examples, are established in the literature [7, 8]; our contribution is not
the existence of adaptivity, but the closed list-valued law and its exact matroid-union realization.
    The disappearance threshold of this obstruction is necessary, not sufficient, for perfect list
discrimination. Geometry inside the support remains relevant. We make that limitation exact:
three pairwise independent qubit states have a free two-fold union matroid but cannot be perfectly
two-list discriminated because their Bloch vectors lie in one strict hemisphere. Conversely, regular
simplices attain a striking sharp transition. Their one-guess optimum loses exactly 1/m, whereas
a two-list root-frame measurement succeeds with certainty for every m ≥ 3. The channel
sections then go beyond static attainment: one family isolates feedback exactly, while complete
unitary-error ensembles expose how the full Schmidt spectrum and the multitime wiring alter
the achievable list probability.
    The paper is organized as follows. Section 2 defines list and soft reward decisions. Section 3
reviews only the Rado and union facts needed later. Section 4 proves the polytope theorem and
the nonuniform Bayes formula. Section 5 gives the process-tester extension. Section 6 derives
the exact parallel–adaptive channel phase. Section 7 derives the process-list consequences of the
dense-coding spectrum law and proves the unitary-history wiring laws. Section 8 derives the
congestion deficit and obstruction threshold. Section 9 proves exact attainment families, and
Section 10 proves the insufficiency counterexample. We close with computational certificates,
related work, and explicit limitations.


2    List decisions and soft rewards

          P. . . , M } label density operators ρi on a finite-dimensional Hilbert space K. Let
Let E = {1,
pi ≥ 0 and i pi = 1. Zero priors are allowed.

Definition 2.1 (Deterministic list measurement). For an integer 1 ≤ ℓ ≤ M , an ℓ-list measure-
ment is a POVM (ML )L∈L indexed by a family L ⊆ {L ⊆ E : |L| ≤ ℓ}. Outcome L reports the
labels in L. Its true-label inclusion probabilities and Bayes list success are
                                    X                          X
                              si =     Tr(ML ρi ),     Plist =    pi si .                  (1)
                                   L∋i                         i

Empty lists may be omitted without changing any statement.

   This convention includes ordinary minimum-error discrimination at ℓ = 1. At ℓ = M − 1,
perfect list success is the usual conclusive exclusion of at least one label. Intermediate values
quantify multi-label elimination.
   The proof needs only a fractional reward budget, not deterministic membership.

Definition 2.2 (Soft-list reward rule). Let (Ma )a be a POVM. A soft-list reward rule assigns
numbers wia ∈ [0, 1] such that for each outcome a,
                                          X
                                             wia ≤ ℓ.                                      (2)
                                              i

Define                             X                           X
                            si =       wia Tr(Ma ρi ),   P =           pi si .                  (3)
                                   a                               i

   A deterministic list is recovered from wiL = 1{i∈L} . Fractional wia allow randomized
postprocessing or partial rewards. The budget (2) is strictly more general than requiring at most
ℓ nonzero rewards. The assumption wia ≤ 1 is essential for the singleton bound si ≤ 1.



                                                  3
Lemma 2.3 (Lists and exclusion). For a nonnegative inclusion reward, an at-most-ℓ list may
be padded to an exactly-ℓ list without decreasing success. Complementing that list is therefore
equivalent to reporting exactly k = M − ℓ excluded labels. In particular, perfect at-most-ℓ list
discrimination is equivalent to perfect weak k-state exclusion after padding.
Proof. For every outcome list L with |L| < ℓ, add arbitrary labels from E \ L until its size is
ℓ. A true label already in L remains present, and some previously omitted labels may become
successful, so the inclusion reward cannot decrease. The complement of the padded list has
cardinality M − ℓ, and the true label lies in the list exactly when it is not among the excluded
labels. Complementation is reversible.

   This elementary dictionary aligns our convention with k-state exclusion and zero-error list
decoding [9, 10]. Stronger exclusion notions that require exhaustive elimination of every tuple
impose additional conditions and are not identified with the present average-reward task [11].


3    Rado matroids and their union powers
Put Si = ran ρi and, for A ⊆ E, define
                                             X
                                d(A) = dim         Si ,   d(∅) = 0.                            (4)
                                             i∈A

Definition 3.1 (Support Rado matroid). The support Rado matroid R on E declares I ⊆ E
independent when vectors vi ∈ Si can be chosen so that (vi )i∈I is linearly independent.
    Rado’s independent-transversal theorem [12] gives the rank formula
                                                             
                               rR (A) = min |A \ C| + d(C) .                                   (5)
                                          C⊆A

Equivalently, I is independent iff |C| ≤ d(C) for every C ⊆ I. For rank-one states, R is simply
the vector matroid of the state vectors.
    The union M1 ∨ M2 of two matroids on the same ground set has as independent sets the
unions I1 ∪ I2 with Ij independent in Mj . Let R∨ℓ denote the union of ℓ copies of R. Thus I
is independent in R∨ℓ iff it can be partitioned into at most ℓ R-independent sets. Edmonds’
matroid-union theorem [13, 14] states
                                                               
                              rR∨ℓ (A) = min |A \ B| + ℓrR (B) .                            (6)
                                          B⊆A

    For the present subspace family this formula collapses to one minimization.
Lemma 3.2 (Closed union-rank law). For every A ⊆ E,
                                                                   
                           rℓ (A) := rR∨ℓ (A) = min |A \ C| + ℓd(C) .                          (7)
                                                   C⊆A

Proof. Insert (5) into (6). The resulting minimum is over C ⊆ B ⊆ A. Write B = C ∪˙ F . Then

                   |A \ B| + ℓ|B \ C| + ℓd(C) = |A \ C| + (ℓ − 1)|F | + ℓd(C).

For fixed C this is minimized at F = ∅. Minimizing over C proves the claim. The argument
also covers ℓ = 1, when every F gives the same value.

    For a matroid M with rank r, its independence polytope is

                       P(M) = {x ∈ RE
                                    ≥0 : x(A) ≤ r(A) for all A ⊆ E}.                           (8)

Edmonds proved that this polytope is the convex hull of incidence vectors of independent sets [15].
Consequently a nonnegative linear functional is maximized by the matroid greedy algorithm.

                                                   4
4      The matroid-union list theorem
Theorem 4.1 (Support-congestion law). For every density ensemble (pi , ρi ), every ℓ ≥ 1, and
every soft-list reward rule of budget ℓ, the vector s = (si ) in (3) belongs to P(R∨ℓ ). Equivalently,
for all A ⊆ E,                 X                                        
                                  si ≤ rℓ (A) = min |A \ C| + ℓd(C) .                             (9)
                                                        C⊆A
                              i∈A

In particular, the statement holds for deterministic ℓ-list measurements.
                                                     P
Proof. Let PA denote the orthogonal projector onto i∈A Si . Since ρi is positive with trace one,
all its eigenvalues lie in [0, 1]. Therefore

                                         0 ≤ ρi ≤ PA                (i ∈ A).                      (10)

For each outcome a, (10) and (2) give
                                                                      !
                                     X                    X
                               0≤            wia ρi ≤           wia       PA ≤ ℓPA .
                                     i∈A                  i∈A

It follows that
                                                                        !
                                      X                  X
                            s(A) =               Tr Ma         wia ρi
                                         a               i∈A
                                         X
                                    ≤ℓ           Tr(Ma PA ) = ℓ Tr PA = ℓd(A).                    (11)
                                             a

Also                                                                        !
                                                          X
                                    0 ≤ si = Tr ρi              wia Ma          ≤ 1,
                                                           a
          P             P
because    a wia Ma ≤     a Ma = I. Hence for arbitrary C ⊆ A,

                            s(A) = s(C) + s(A \ C) ≤ ℓd(C) + |A \ C|.

Minimizing over C and applying Theorem 3.2 proves (9). Nonnegativity of s and the rank-
inequality description (8) finish the proof.

    The raw inequality (11) alone is not generally a matroid rank inequality because it can exceed
|A|. The singleton constraints are what perform the exact submodular truncation in (7).

Corollary 4.2 (Arbitrary-prior Bayes cap). Every soft-list rule of budget ℓ obeys
                                            (                     )
                                             X
                       P ≤ βℓ (p, S) := max      pi : I ∈ I(R∨ℓ ) .                               (12)
                                                              i∈I

Thus the cap is the maximum prior mass of a set partitionable into at most ℓ independent support
transversals.

Proof. By Theorem 4.1, s ∈ P(R∨ℓ ). The vertices of this polytope are incidence vectors of
independent sets, so maximizing p · s over it gives (12).

   The cap has a useful formula that avoids choosing a maximizing independent set explicitly.
Order the labels so that p(1) ≥ · · · ≥ p(M ) and put Ej = {(1), . . . , (j)}, E0 = ∅, and p(M +1) = 0.



                                                          5
Proposition 4.3 (Prefix formula and equality audit). One has
                                               M
                                               X                  
                                 βℓ (p, S) =         p(j) − p(j+1) rℓ (Ej ).                      (13)
                                               j=1

For a fixed soft-list rule with inclusion vector s, equality p · s = βℓ holds iff
                              s(Ej ) = rℓ (Ej )      whenever p(j) > p(j+1) .                     (14)
The condition is independent of how labels are ordered inside a prior tie.
Proof. The matroid greedy theorem selects label (j) precisely when rℓ (Ej ) − rℓ (Ej−1 ) = 1.
Summation by parts gives (13). The same identity for an arbitrary vector is
                                             M
                                             X
                                    p·s=       (p(j) − p(j+1) )s(Ej ).
                                             j=1

Every coefficient and every deficit rℓ (Ej ) − s(Ej ) is nonnegative. Their weighted sum vanishes
exactly at the strict prior breakpoints, proving (14). At a tie the coefficient is zero, so rearranging
tied labels has no effect.

Remark 4.4 (Hierarchy). The matroids satisfy R ⪯ R∨2 ⪯ · · · , so β1 ≤ β2 ≤ · · · ≤ 1. The case
ℓ = 1 is the previously derived one-label Rado bound [3]. The new content is the union hierarchy,
its soft-decision meaning, and the exact obstruction threshold and attainment results below.


5     General quantum-process testers
We use unnormalised Choi operators throughout this section. This avoids an input-dimension
factor in the tester normalization.
    Let Ji ≥ 0 be the Choi operators of a finite family of deterministic processes.
                                                                               P        A tester
with list-valued outcomes consists of positive operators TL whose sum T = L TL is a valid
deterministic tester normalization. For every candidate process in the stated tester interface,
                                               Tr(T Ji ) = 1,                                     (15)
and the conditional probability of outcome L is Tr(TL Ji ). The linear constraints selecting parallel,
sequential, or general testers affect the admissible set of T , but not the following compression.
Lemma 5.1 (Canonical compression). Let K = supp T and let T −1/2 be the Moore–Penrose
inverse on K. Define
                           ρi = T 1/2 Ji T 1/2 ,      ML = T −1/2 TL T −1/2 K .                   (16)
Then (ρi ) are density operators on K, (ML ) is a POVM on K, and
                                          Tr(ML ρi ) = Tr(TL Ji )                                 (17)
for all i, L.
Proof. Positivity is immediate and (15) gives Tr ρi = 1. Since 0 ≤ TL ≤ T , the support of every
TL is contained in K, and        X
                                    ML = T −1/2 T T −1/2 = IK .
                                      L

Using the support projection PK = T −1/2 T 1/2 , cyclicity of trace, and TL = PK TL PK gives
                             Tr(ML ρi ) = Tr(T −1/2 TL T −1/2 T 1/2 Ji T 1/2 )
                                          = Tr(PK TL PK Ji ) = Tr(TL Ji ).



                                                       6
Theorem 5.2 (Process-list matroid bound). Fix any admissible tester normalization T satisfying
(15). Let SiT = ran(T 1/2 Ji T 1/2 ). Every ℓ-list tester with this normalization obeys Theorems 4.1
to 4.3 for the Rado matroid of (SiT ). P
    Let Si0 = ran Ji and d0 (A) = dim i∈A Si0 . Then a tester-independent bound is obtained by
replacing dT by d0 in (7). In particular, it holds after optimizing over all admissible general
testers.
Proof. The fixed-T statement follows from Theorems 4.1 and 5.1. Moreover,

                                  ran(T 1/2 Ji T 1/2 ) ⊆ T 1/2 ran Ji ,

so a common linear map can only decrease the dimension of every support sum: dT (A) ≤ d0 (A).
Formula (7) is monotone in d, and so are the prefix and maximum-weight bounds. The resulting
cap does not depend on T and survives the outer optimization.

    For rank-one Choi operators Ji = |Ui ⟩⟩⟨⟨Ui |, the oracle matroid is the vector matroid of the
Choi vectors. The theorem therefore bounds list discrimination of unitary channels by the union
powers of their labeled linear-dependence matroid. We make no claim that the tester-independent
cap is always attainable, or that indefinite causal order is irrelevant to the actual optimum.
    For clarity, equality in the effective and original-support caps are different claims. For fixed
T , Theorem 4.3 characterizes equality in the cap built from SiT . Equality in the coarser cap built
from Si0 additionally requires that compression cause no weighted prefix-rank loss. We never
infer the latter from saturation of the former.

5.1    A robust core-and-tail certificate
Exact support can change discontinuously under a small full-rank perturbation. The following
secondary result retains a low-rank union-matroid core and pays explicitly for the discarded tail.
It extends the one-label robust certificate of Ref. [3] to every list budget.
Corollary 5.3 (Robust process cores). Let 0 ≤ Li ≤ Ji and Ri = Ji − Li . For a fixed
deterministic tester normalization T , put

                                λi = T 1/2 Li T 1/2 ,       SiL = ran λi ,

and form the union-matroid cap βℓ (T, L, p) from the subspaces (SiL ). Every deterministic ℓ-list
tester with normalization T obeys
                                    (                                )
                                                       X
                         Plist ≤ min 1, βℓ (T, L, p) +   pi Tr(T Ri ) .                     (18)
                                                              i

Consequently, for an architecture class T of deterministic normalizations,
                                (                                         )
                                                       X
                       T
                     Plist ≤ min 1, sup βℓ (T, L, p) +    pi sup Tr(T Ri ) .                   (19)
                                       T ∈T                   i    T ∈T

The first supremum may be replaced by the coarser cap computed from the uncompressed core
supports ran Li .
Proof. Decompose si = sL       R
                          i + si using Ji = Li + Ri . The compressed core obeys 0 ≤ λi ≤ ρi ,
where ρi is the density operator from Theorem 5.1. Thus λi is bounded by the projector onto
any core support sum containing it. The proofPof Theorem 4.1 applies to the core contributions
even though Tr λi need not be one, and gives i pi sLi ≤ βℓ (T, L, p).
   For the tail,                     X       X
                                        TL ≤     TL = T,
                                        L∋i             L


                                                    7
so positivity gives sR
                     i ≤ Tr(T Ri ). Summing with the priors and capping a success probability
by one proves (18). Taking the architecture supremum and bounding each tail term separately
proves (19). Common congruence can only lower core support-sum ranks, proving the final
statement.

Remark 5.4. The tail term in (19) deliberately contains separate suprema. It does not assert that
one tester normalization simultaneously
                                  P      maximizes all tails. For ordinary state discrimination,
T = I and the penalty reduces to i pi Tr Ri .


6    Input-dependent channels and an exact architecture phase
The tester theorem above bounds each architecture after its deterministic normalization has
been chosen. It does not normally optimize that choice or compare architectures. We now give a
channel family for which both tasks close exactly, including arbitrary entangled parallel probes
and arbitrary adaptive quantum memories.
   Let X and Y be finite alphabets. Hypothesis i specifies a deterministic function fi : X → Y
and the entanglement-breaking channel
                                         X
                               Φi (τ ) =   ⟨x|τ |x⟩ |fi (x)⟩⟨fi (x)|.                        (20)
                                                x∈X

The same unknown channel may be called repeatedly. A parallel strategy uses q copies simulta-
neously and may prepare an arbitrary state entangled across the q inputs and a reference. An
adaptive strategy may retain an arbitrary quantum memory and choose each later input after
the earlier classical outputs. No indefinite-causal-order strategy is included in the comparison.
   For a deterministic query tuple x = (x1 , . . . , xq ), set

                    cx (i) = (fi (x1 ), . . . , fi (xq )),         Cz (x) = {i : cx (i) = z}.

If w = (wi )i∈E is a nonnegative weight vector, write

                                                        Xz (x)|}
                                                  X min{ℓ,|C              ↓
                                 Bℓ (x; w) =                             wC z (x),j
                                                                                    ,             (21)
                                                   z             j=1

       ↓
where wC,j is the jth largest weight in C.
Theorem 6.1 (Exact reduction of classical channels). For the channels in (20) and arbitrary
priors p, the optimum of every q-use parallel quantum strategy is
                                           (ℓ)
                                          Ppar (q) = maxq Bℓ (x; p).                              (22)
                                                        x∈X

The adaptive optimum is the exact Bellman value
                             min{ℓ,| supp w|}
                                                wj↓ ,
                                    X
                  V0 (w) =                                                                        (23)
                                    j=1
                                                                                 (ℓ)
                                    X                            
                  Vq (w) = max            Vq−1 (wi 1{fi (x)=y} )i ,           Pad (q) = Vq (p).   (24)
                              x∈X
                                    y∈Y

For fixed x, the effective supports form the partition matroid
                                          M
                                              U1,|Cz (x)| .                                       (25)
                                                    z

Its ℓ-fold union bound is exactly (21) and is attained by reporting the ℓ largest-prior labels in
each response cell.

                                                             8
Proof. For deterministic basis inputs, the output word is the orthogonal classical state |cx (i)⟩.
Labels in one cell are identical and different cells are perfectly distinguishable. The cellwise
decision just described is therefore optimal. Its support matroid is (25); taking ℓ union copies
changes every class capacity from one to min{ℓ, |Cz |}, and matroid greedy optimization gives
(21).
    For a general parallel input on X⊗q ⊗ R, each call first measures its input in the fixed basis.
Give the decoder a genie flag containing the resulting tuple x. Conditional on this flag, the
reference operator is independent of i and all label dependence lies in cx (i). Revealing a flag
cannot lower success, so the original strategy is bounded by a convex combination of the values
Bℓ (x; p) and hence by their maximum. A deterministic basis tuple attains that maximum,
proving (22).
    The same flag may be revealed after every call of a sequential strategy. Conditional on the
complete prior input–output transcript, induction shows that the retained quantum state is
fixed by the strategy and independent of the label inside the surviving response cell. Thus every
quantum strategy is bounded by a randomized classical query tree with the same transcript. At
each node the value is affine in the randomized next query, so an extreme deterministic query is
optimal. The terminal reward is the sum of the ℓ largest surviving weights, and conditioning
on the next output gives (23)–(24). Conversely, every deterministic query tree is an admissible
adaptive quantum strategy, so the bound is exact.

    We now choose a family on which the recursion and the parallel cell problem both have
closed forms. Fix h ≥ 1 and label M = 2h channels by the binary leaves u ∈ {0, 1}h . The input
alphabet consists of all prefixes v with |v| < h, and

                                     fu (v) = 1{v1 is a prefix of u} .                                   (26)

Thus query v asks membership in the right child below v. The queried cylinders Av = {u :
fu (v) = 1} are laminar: any two are nested or disjoint.

Theorem 6.2 (Complete parallel–adaptive list phase). Let the channels (26) have uniform
priors, let ℓ = 2s with 0 ≤ s ≤ h, and let q ≥ 0. Then

                                                                     ℓ2q
                                                                      
                     (ℓ)              ℓ(q + 1)         (ℓ)
                    Ppar (q) = min 1,            ,   Pad (q) = min 1, h .           (27)
                                         2h                          2
Consequently the exact numbers of calls required for perfect list success are

                       ∗                   M                 ∗                   M
                      qpar = 2h−s − 1 =      − 1,           qad = h − s = log2     .                     (28)
                                           ℓ                                     ℓ
In particular, one-label identification needs 2h − 1 parallel calls but only h adaptive calls.


Table 1: Exact resource phase for the laminar channel family, with M = 2h and ℓ = 2s . “Cells”
denotes the maximum number of classical response cells before saturation.
     Architecture              cells after q calls           list success        calls for success one
     parallel, no feedback           q+1                 min{1, ℓ(q + 1)/M }            M/ℓ − 1
     adaptive feed-forward            2q                   min{1, ℓ2q /M }             log2 (M/ℓ)


Proof. Any q fixed queries select q sets from a laminar family. Such sets have at most q + 1
nonempty membership cells: insert them in an order compatible with inclusion; a new set lies
inside one old cell and can split only that cell. For uniform priors, Theorem 6.1 assigns at most
ℓ/2h success to each cell. This proves the parallel upper bound.

                                                     9
    Put d = h − s. Query the prefixes of lengths below d in breadth-first order. Each new
right-child cylinder splits one current prefix block into two, and until all 2d − 1 queries have been
used every resulting block contains at least 2s = ℓ leaves. After q ≤ 2d − 1 queries there are
therefore exactly q + 1 cells, each contributing ℓ/2h . At q = 2d − 1 the cells are the 2d length-d
prefix blocks, each of size ℓ; later calls can be ignored. This attains the first formula.
    A binary adaptive tree of depth q has at most 2q transcripts, and each terminal list covers at
most ℓ labels. Hence its uniform success is at most the second expression in (27). To attain it,
start at the empty prefix and query the currently certified prefix v. Output one selects child
v1, while output zero selects v0. After q rounds the transcript identifies the first q bits and the
surviving cell has size 2h−q . At q = d this size is ℓ, proving both the second formula and (28).

    The depth-two member has four channels with function tables

                                 000,       010,          100,         101.

With two calls, Theorem 6.2 gives

                               (1)  3              (2)                 (1)
                              Ppar = ,            Ppar = 1,       Pad = 1.                      (29)
                                    4
Thus one feedback bit and one extra reported label close the same parallel one-guess deficit. The
example is entirely classical after the input measurement; it proves neither a quantum-memory
advantage nor an indefinite-causal-order advantage. Binary search, membership-query learning,
and adaptive channel advantages are classical or established mechanisms [16, 7]. The result here
is the exact list-valued phase against the full parallel and adaptive quantum strategy classes
specified above, together with its attained union-matroid interpretation.


7    Entanglement spectra and multitime unitary histories
The preceding family isolates feedback but is classical after dephasing. We next give an input-
sensitive quantum family in which the complete Schmidt spectrum, rather than only support
rank, determines the optimum. The result also separates three precisely delimited multitime
wirings.
                                 2
    Let dim A = D and let (Ug )D
                               g=1 be a complete unitary error basis, so

                                         Tr(Ug∗ Ug′ ) = Dδgg′ .                                 (30)

For a pure probe ψ ∈ A ⊗ R, put ρR = TrA |ψ⟩⟨ψ| and ψg = (Ug ⊗ I)ψ.

Theorem 7.1 (Dense-coding spectrum law in process form). For uniform discrimination of the
D2 channels Φg = AdUg with the fixed probe ψ,
                                                      √
                                                   (Tr ρR )2
                                      Pguess (ψ) =           .                                  (31)
                                                      D
Consequently, among probes of Schmidt rank at most r ≤ D,
                                                                 r
                                         max Pguess (ψ) =          ,                            (32)
                                        SR(ψ)≤r                  D

with equality exactly for a flat nonzero Schmidt spectrum. Every ℓ-list measurement for the same
fixed probe satisfies                                    √
                                                     ℓ(Tr ρR )2
                                                               
                                    (ℓ)
                                  Plist (ψ) ≤ min 1,              .                          (33)
                                                         D



                                                     10
    The one-guess identity (31), including optimality for an arbitrary pure entangled resource, is
the approximate dense-coding result of Feng, Duan, and Ji [17]. We include the short frame/dual
proof to fix conventions and to make the list and multitime consequences below self-contained;
we do not claim the identity itself as new.

Proof. Hilbert–Schmidt completeness gives the depolarizing identity
                                X
                                    Ug XUg∗ = D Tr(X)IA .
                                      g

Therefore, on A ⊗ supp ρR ,                 X
                                   S :=      |ψg ⟩⟨ψg | = DIA ⊗ ρR .                              (34)
                                             g

The square-root measurement Mg = S −1/2 |ψg ⟩⟨ψg |S −1/2 sums to the identity on this support.
Moreover                                                 √
                                         −1/2         Tr ρR
                             c := ⟨ψg |S      |ψg ⟩ = √
                                                          D
is independent of g, so its success is c2 .
    For the dual minimum-error SDP, set Y = (c/D2 )S 1/2 . The rank-one domination criterion
gives Y ⪰ |ψg ⟩⟨ψg |/D2 , because
                                       ⟨ψg |(cS 1/2 )−1 |ψg ⟩ = 1.
                  √
Also Tr Y = (Tr ρR )2 /D,     p 2 optimality. If the nonzero Schmidt coefficients are λ1 , . . . , λr ,
                          P proving
Cauchy–Schwarz gives ( j λj ) ≤ r, with equality exactly when they are all 1/r.
    Finally, for a list POVM (ML ) define Ng = ℓ−1 L∋g ML . Then g Ng ⪯ I; completing this
                                                         P         P
                                                          (ℓ)
sub-POVM to a one-label POVM shows Pguess ≥ Plist /ℓ. Combining with (31) and the trivial
cap one proves (33).

   The formula is stable under independent Qtime slots. A tensor product of complete unitary error
bases is a complete basis on dimension D = t dt , so Theorem 7.1 already allows inputs entangled
across different times. In particular, without a retained reference every pure parallel input has
success 1/D, whereas a global Schmidt-rank budget r gives exact optimum min{r, D}/D.
   For a list-valued wiring comparison, let each of n time slots carry an independent uniformly
labeled Weyl operator X at Z bt on Cd . There are M = d2n history hypotheses. We compare:

    SER0 : one d-dimensional carrier is reused, with known interleaving unitaries but no side
     memory, intermediate measurement, or retained transcript;

    PAR0 : n fresh inputs are used in parallel and may be entangled with each other, but no
     reference is retained;

    PARBell : every input has a retained d-dimensional Bell reference.

Theorem 7.2 (Exact multitime wiring trichotomy). For the uniform Weyl histories above,
                                          (ℓ)
                                      PSER0 = min{1, ℓ/d2n−1 },
                                          (ℓ)
                                      PPAR0 = min{1, ℓ/dn },                                      (35)
                                      (ℓ)
                                    PPARBell = 1.

Before saturation, fresh parallel inputs improve on a carrier-only serial wiring by the exact factor
dn−1 .




                                                    11
Table 2: Exact list values for M = d2n independent Weyl histories. The resource restrictions are
part of the architecture definitions preceding Theorem 7.2.
                Architecture       terminal support dimension     optimal list success
                SER0                          d                     min{1, ℓ/d2n−1 }
                PAR0                         dn                      min{1, ℓ/dn }
                PARBell                2n
                                      d orthogonal labels                  1

                                                                             (ℓ)
Proof. A uniform ensemble of M pure states in dimension q0 obeys Plist ≤ min{1, ℓq0 /M } by
Theorem 4.1. Every SER0 output occupies only the terminal d-dimensional P     P carrier. With no
interleaving, Weyl multiplication produces the net label (A, B) = ( t at , t bt ) modulo d; input
|0⟩ and a computational measurement reveal A. Each value leaves exactly d2n−1 histories, so
reporting any ℓ of them attains the first formula.
    Every PAR0 output occupies dimension dn , even when its inputs are entangled across slots.
The product input |0⟩⊗n reveals the full shift vector (a1 , . . . , an ) and leaves exactly dn phase
histories, attaining the second formula. Local Bell inputs turn the Weyl outputs into an
orthonormal product Bell basis and prove the third.

    The support-rank upper bound in (33) need not be attained for an intermediate
                                                                             √     entanglement
spectrum. For example, take D = 4 and the rank-two probe (|00⟩ + |11⟩)/ 2 for the 16 Weyl
channels. The outputs split into four orthogonal shift sectors, each containing the phase states
                                                √
                            ϕb = (|0⟩ + ib |1⟩)/ 2,    b = 0, 1, 2, 3.
                                                             √
Adjacent-pair reward operators have largest eigenvalue
                                               √       1 + 1/ 2 and their top eigenvectors form
a tight frame; the covariant dual is (1 + 1/ 2)I/4. Pinching over the shift sectors therefore
proves the exact fixed-probe value
                                                   √
                                        (2)    2+ 2
                                      Plist =         < 1,                                  (36)
                                                  4
although the coarse right-hand side of (33) equals one. This is a fixed-probe statement, not a
resource-optimized impossibility theorem.
    Unitary-error bases, dense coding, group-covariant discrimination, and parallel treatment of
independent unitary channels are established subjects [17, 18, 19, 20, 21, 6]. We claim neither
those ingredients, the one-guess spectrum formula, nor the dimension bound as new. The
contribution of this section is narrower: the list-cap embedding, the exact multitime wiring
trichotomy, and the explicit intermediate-spectrum failure of the coarse list cap.


8    Uniform congestion, deficits, and obstruction thresholds
For equal priors, Theorem 4.2 depends only on the rank of the full ground set.
Corollary 8.1 (Exact support deficit). For pi = 1/M ,
                               rℓ (E)     ∆ℓ                               
                     Plist ≤          =1−    ,         ∆ℓ = max |C| − ℓd(C) .                  (37)
                                 M        M                 C⊆E

The maximum includes C = ∅, so ∆ℓ ≥ 0.
Proof. Taking A = E in (7),

                   rℓ (E) = min(M − |C| + ℓd(C)) = M − max(|C| − ℓd(C)).
                               C                                C

Divide by M .

                                                  12
    The integer ∆ℓ counts the rank deficit of the union matroid, not a continuous geometric error.
It gives a fail-closed certificate: if any label cluster has more than ℓ labels per available support
dimension, uniform perfect-list discrimination is impossible.
Corollary 8.2 (Disappearance threshold of the matroid obstruction). The support bound permits
Plist = 1 exactly when
                              |C| ≤ ℓd(C)      for all C ⊆ E.                            (38)
The smallest list budget for which this happens is
                                                                 
                                                              |C|
                                     ℓsupp = max                    .                           (39)
                                                ∅̸=C⊆E       d(C)
Equivalently, E can then be partitioned into ℓsupp independent sets of the support Rado matroid.
Proof. The cap equals one iff rℓ (E) = M , equivalently iff ∆ℓ = 0. This is exactly (38); minimizing
the integer ℓ gives (39). The final statement is Edmonds’ matroid-partition criterion applied to
R, or directly the condition that E be independent in R∨ℓ .

    The adjective “support” in ℓsupp is essential. It is a lower bound on the list budget required
for perfect physical success, but equality need not hold; Section 10 gives an exact failure.
    It is also not the strongest known feasibility obstruction. The projector test for conclusive
k-state exclusion of Stratton, Hsieh, and Skrzypczyk [9], applied after Theorem 2.3 and then to
each restricted label set C, requires     X
                                              Πi ≤ ℓPC ,                                      (40)
                                            i∈C
                                           P
where Πi projects onto Si and PC onto i∈C Si . For pure states, taking the trace recovers
|C| ≤ ℓd(C). For mixed states, and even geometrically for pure states, the operator inequality
can be strictly stronger. Thus (39) is precisely the disappearance threshold of the matroid
obstruction, not a new feasibility characterization.
Proposition 8.3 (Strict improvement over total dimension). Let five distinct pure states lie
in a common two-dimensional subspace and let a sixth pure state span an orthogonal line. Give
the five coplanar labels prior a = 19/100 each and the orthogonal label prior b = 5/100. For list
budget ℓ = 2, the total-dimension relaxation is one, whereas the matroid-union cap is
                                                             81
                                        β2 = 4a + b =            .                              (41)
                                                             100
                                                p
Proof. Choose, for example, ϕj = (e0 + je1 )/ 1 + j 2 for j = 0, . . . , 4, and ϕ5 = e2 . The vector
matroid is U2,5 ⊕ U1,1 . Its two-fold union is U4,5 ⊕ U1,1 , so a maximum-weight independent set
retains four coplanar labels and the coloop, proving (41). The total dimension is D = 3 and
ℓD = 6 = M ; hence the relaxation that keeps only D and the singleton bounds gives one. No
attainability claim is made for the value 81/100.


9    Sharp families
We first show that the arbitrary-prior theorem is exactly attainable for a complete family of
partition matroids.
Proposition 9.1 (Orthogonal parallel classes). Let (ea )qa=1 be orthonormal. Partition E into
nonempty classes Ea , and set ρi = |ea ⟩⟨ea | for i ∈ Ea . For every prior and list budget ℓ,
                                           q
                                   opt
                                           X             X
                                 Plist =                                 pi .                   (42)
                                           a=1 i∈Topmin(ℓ,|Ea |) (Ea )

This equals the matroid-union cap.

                                                    13
Proof. The support matroid is the partition matroid with capacity one in each class; its ℓ-fold
union has capacity ℓ in each class. The maximum-weight independent set therefore selects
the min(ℓ, |Ea |) largest priors in each class, proving the upper bound. Measure the orthogonal
projectors |ea ⟩⟨ea | and, on outcome a, report precisely those top-prior labels. This attains
(42).

    Repeated states make Theorem 9.1 combinatorially transparent. The next family uses only
distinct, pairwise nonorthogonal pure states.

9.1   The regular-simplex transition
Let m ≥ 3 and let unit vectors ϕ1 , . . . , ϕm ∈ Cm−1 satisfy
                                                       1
                                     ⟨ϕi , ϕj ⟩ = −          (i ̸= j).                            (43)
                                                      m−1
Their Gram matrix has one zero eigenvalue and eigenvalue m/(m − 1) with multiplicity m − 1.
Consequently
                           m               m
                           X              X                m
                              ϕi = 0,        |ϕi ⟩⟨ϕi | =     I.                       (44)
                                                          m−1
                               i=1                 i=1
Every proper subset is linearly independent, so their vector matroid is the uniform matroid
Um−1,m .
Theorem 9.2 (Exact one-to-two-list jump). For the equiprobable regular-simplex ensemble,
                                      (1)     m−1            (2)
                                     Popt =       ,         Popt = 1.                             (45)
                                               m
An optimal one-guess POVM is
                                         m−1
                                               |ϕi ⟩⟨ϕi |.
                                            Ni =                                                  (46)
                                           m
An optimal two-list POVM is indexed by unordered pairs i < j:
                                  ϕi − ϕ j                         2
                          ψij = p           ,              Mij =     |ψij ⟩⟨ψij |,                (47)
                                 2m/(m − 1)                        m
and outcome (i, j) reports {i, j}.
Proof. For one guess, the matroid cap is r1 (E)/m = (m − 1)/m. Equations (44) and (46) show
that (Ni ) is a POVM, and its conditional correct probability is (m − 1)/m for every label. Hence
the cap is attained.
   For two guesses, first note that
                 X                          X               X       X         m2
                   |ϕi − ϕj ⟩⟨ϕi − ϕj | = m  |ϕi ⟩⟨ϕi | − |   ϕi ⟩⟨   ϕi | =     I.          (48)
                                                                             m−1
                 i<j                           i               i         i

Since ∥ϕi − ϕj ∥2 = 2m/(m − 1), substituting (47) into (48) gives
                                                                             P
                                                                               i<j Mij = I.
        / {i, j}, then (43) gives
   If k ∈
                                      ⟨ϕi − ϕj , ϕk ⟩ = 0.
Thus an outcome whose reported pair omits k has zero probability on state ϕk . Every possible
outcome contains the true label, and the two-list success is one. No probability can exceed one,
completing the proof.

    The pair differences in (47) form the normalized root frame of type Am−1 . For m = 3, the
construction is the usual trine exclusion measurement. Antidistinguishability and conclusive
exclusion are established subjects [1]; novelty is not claimed for that isolated fact. Its role here is
to prove exact attainment of the first nontrivial union step for an all-distinct family of arbitrary
size.

                                                      14
10     A full union matroid is not sufficient
The condition rℓ (E) = M says that the support inequalities alone do not forbid perfect list
success. It does not construct a POVM. The following exact example prevents the combinatorial
theorem from being misread as a geometric characterization.

Proposition 10.1 (Hemisphere obstruction). Consider the three pure qubit states
                                                            
                         1              1 2                 1 2
                   ϕ1 =     ,     ϕ2 = √       ,     ϕ3 = √         .                             (49)
                         0                5 1                5 i

Their support matroid is U2,3 , so rR∨2 (E) = 3 and the two-list support cap equals one. Nevertheless
no perfect two-list measurement exists. For uniform priors its exact optimum is
                                                      √
                                          opt   2 + 1/ 3
                                        Plist =           < 1.                                   (50)
                                                    3
Proof. The squared pairwise overlaps are
                                      4                       4                         17
                       |⟨ϕ1 , ϕ2 ⟩|2 = ,       |⟨ϕ1 , ϕ3 ⟩|2 = ,      |⟨ϕ2 , ϕ3 ⟩|2 =      .      (51)
                                      5                       5                         25
Every pair is therefore linearly independent. The matroid is U2,3 , whose two-fold union is the
free matroid on three labels.
    Suppose a perfect two-list measurement existed. Every outcome list omits at least one of
the three labels. Assign each outcome to    Pone omitted label and sum the corresponding POVM
effects, obtaining effects F1 , F2 , F3 with i Fi = I. Perfect inclusion implies that every outcome
omitting i has zero probability on ϕi , so

                                                   Fi ϕi = 0.                                     (52)

Thus (Fi ) would antidistinguish the three states.
   Let ni ∈ R3 be their Bloch vectors. A positive qubit operator annihilating ϕi has the form
Fi = ai |ϕ⊥    ⊥
          i ⟩⟨ϕi | with ai ≥ 0. Completeness requires
                                   X               X
                                      ai = 2,         ai ni = 0.                          (53)
                                     i                          i

For (49), the z coordinates of the Bloch vectors are
                                                                        3
                                 (n1 )z = 1,           (n2 )z = (n3 )z = .                        (54)
                                                                        5
They lie in a strict open hemisphere. The second equation in (53) cannot hold with nonnegative
ai whose sum is two. This contradicts (52) and proves nonperfectness.
    It remains to prove the exact value (50). For three labels, minimum list failure equals minimum
exclusion error. An exclusion POVM (Fi ) yields the list E \ {i} on outcome i. Conversely, from
any two-list POVM assign each outcome to one label omitted by its list; the resulting exclusion
error is no larger than the original list failure. Taking infima in the two directions proves equality.
    The uniform exclusion SDP and its dual are
                                                 1X
                          e∗ =       min             Tr(Fi ρi ) = max Tr Y.                      (55)
                                         i Fi =I 3
                                       P
                                Fi ≥0,                           Y ≤ρi /3
                                                       i

Put                                                   
                                               1 1 2                    1
                                   u=           , ,         ,       R= √ .
                                               3 3 3                     3

                                                           15
The Bloch vectors are

                      n1 = (0, 0, 1),   n2 = (4/5, 0, 3/5),    n3 = (0, 4/5, 3/5),

and satisfy |u − ni | = R and u · ni = 2/3. The dual operator
                                              1                 
                                        Y =     (1 − R)I + u · σ                             (56)
                                              6
is feasible because
                                1         1                
                                  ρi − Y = RI + (ni − u) · σ ≥ 0.
                                3         6
Its trace is (1 − R)/3.
    For primal attainment, define
                                                         
                  u − ni                           1 5 5                wi
             mi =        ,     (w1 , w2 , w3 ) =    , ,     ,    Fi =      (I + mi · σ).
                    R                              3 6 6                2
               P                P                        P
Here |mi | = 1, i wi = 2, and i wi ni = 2u, hence i Fi = I. Moreover mi · ni = −R, and
therefore
                           1X                  1 X wi            1−R
                                Tr(Fi ρi ) =           (1 − R) =         .
                           3                   3     2              3
                             i                   i
                                                       √            opt
Primal and dual values coincide. Thus e∗ = (1 − 1/ 3)/3 and Plist       = 1 − e∗ , proving (50).

    The example also shows why perturbing a degenerate support arrangement can change attain-
ability without changing the matroid. Support ranks are piecewise constant; antidistinguishability
is controlled by a convex geometric condition inside that rank stratum.


11     Computation and exact certificates
For a represented subspace family, the cap is finite and combinatorial. One may evaluate d(C) by
exact matrix rank and use (7) directly for small M . For larger instances, standard matroid-union
and submodular-minimization algorithms apply; no quantum SDP is needed to certify the
cap. Cunningham gives improved algorithms for matroid partition and intersection [22]. This
computational observation concerns the upper bound, not construction of an optimal POVM.
    The accompanying verifiers use the Python standard library and exact rational or algebraic
arithmetic. They perform the following fail-closed checks:

  1. exhaustive comparison of (7) with a brute-force coloring definition on 240 small subspace
     instances;

  2. all subset inequalities for an exact list-measurement fixture;

  3. the one-guess and edge-root POVMs for regular simplices m = 3, . . . , 8 through rational
     Gram identities;

  4. exhaustive laminar-channel phase values for 70 small (h, s, q) instances, including the
     partition-matroid cell formula;

  5. complete-unitary-basis frame spectra, Schmidt-rank caps, Weyl wiring values, and the
     rank-two fixed-probe list certificate;

  6. the exact overlaps, free union matroid, strict-hemisphere obstruction, and primal–dual
     optimum of Theorem 10.1;

  7. the strict-flat value 81/100 versus the total-dimension value one;

                                                    16
   8. monotonicity of support-sum ranks under a common process compression.

   The finite tests are not a proof of the general theorem. They guard the rank formula,
normalizations, and fixtures against transcription and convention errors. The general proofs are
Theorems 3.2, 4.1, 5.2 and 6.1 and Theorems 6.2, 7.1 and 7.2.


12     Related work and priority boundary
Quantum minimum-error discrimination is classically formulated through the Holevo–Yuen–
Kennedy–Lax optimality conditions [23, 24] and is reviewed in standard texts and surveys [25,
26]. State exclusion reverses the decision: an outcome rules out one or more hypotheses.
Bandyopadhyay et al. give an SDP, optimality conditions, and variants including unambiguous and
worst-case exclusion [1]. Experimental elimination of multiple states is demonstrated by Webb et
al. [2]. Stratton, Hsieh, and Skrzypczyk derive projector and rank conditions for weak and strong
k-state exclusion [9]. Johnston, Russo, and Sikora characterize pure-state antidistinguishability
through Gram-matrix incoherence and give tight overlap bounds [27]. Recent work studies group-
generated exclusion [28], global-versus-LOCC higher-order exclusion [11], and zero-error list
decoding of classical–quantum channels, including the trine at list size two [10]. By Theorem 2.3,
our list success is the complementary set-valued formulation with k = M − ℓ. Therefore neither
list decoding, the simplex/trine measurement, state exclusion, nor the nonsufficiency of rank
conditions is presented as new.
     Rado’s theorem on independent representatives is classical [12]. Edmonds established the
minimum-partition criterion and matroid union [13, 14], as well as the rank-inequality description
of matroid polyhedra [15]. Our use of these results is direct and fully credited. The potentially new
point is narrower: the all-subset Bayesian inequality that places the entire inclusion-probability
vector in an exact union-matroid polytope, together with arbitrary priors, soft rewards, the
robust core-tail version, and canonical process-tester compression.
     Quantum testers and combs provide a common language for discrimination of multi-time
processes [4]. Canonical inverse-square-root normalization is standard [5]; general and indefinite-
order strategies have been compared in concrete unitary discrimination problems [8, 6], and
restricted tester classes have a general convex formulation [29]. Entanglement-breaking channels
can already exhibit finite-query adaptive advantages [7]; asymptotic comparisons obey different
laws [30]. Theorem 5.1 recalls the normalization only to make the list theorem convention-safe.
The input-dependent application does not claim adaptivity, binary search, or membership queries
as new. Its specific contribution is the exact all-depth list phase and the proof that arbitrary
quantum parallel probes and memories reduce to the stated cell and decision-tree optimizations
for this family.
     Complete unitary-error bases, dense coding, and symmetric operation discrimination are
likewise established [17, 18, 19, 21]. In particular, Feng, Duan, and Ji already derive and attain
the approximate dense-coding success law that becomes (31) in our notation. Independent
unitary histories admit strong parallel reductions [20]. Accordingly, Theorems 7.1 and 7.2 do
not claim the twirl, dense-coding protocol, spectrum formula, or support-dimension converse as
new. The narrower addition is the process-list translation, its Schmidt-rank equality audit, the
list-wiring trichotomy, and the explicit intermediate-rank failure of the coarse list cap.
     The one-label Rado-matroid support bound was developed separately in Ref. [3]. The present
paper cites that work rather than repackaging it. Its distinct contribution is the operational
list hierarchy, the closed union-rank law, soft rewards, obstruction threshold, exact attain-
ment/insufficiency pair, and the two architecture-sensitive channel theorems above. Targeted
searches did not locate this combined theorem package. Absence from a search is not proof of
priority; no claim of being first is made.



                                                 17
13     Limitations and conclusions
Several boundaries are essential.
    First, the theorem is an upper bound. The inclusion vector belongs to a matroid polytope,
but not every point of that polytope is generated by a POVM. Theorem 10.1 shows that even a
free union matroid need not permit perfect list discrimination.
    Second, the theorem uses exact support. An arbitrarily small full-rank noise component can
enlarge every support and weaken the raw cap discontinuously. Theorem 5.3 mitigates this with
chosen positive cores and an explicit tail penalty, but it does not canonically choose those cores
or guarantee that the resulting certificate improves an SDP bound.
    Third, the tester-independent process cap uses the uncompressed Choi support. A fixed tester
normalization can lower the Rado-union rank and give a stronger certificate. Conversely, the cap
does not determine which causal architecture attains the actual optimum. The exact architecture
formulas proved here rely on either complete dephasing with a common input measurement
or a complete unitary-error frame; they do not extend automatically to noisy, incomplete, or
nonuniform channel families.
    Fourth, the adaptive channel comparison excludes indefinite causal order, coherent phase-
oracle access, inverse calls, and controlled bypass. The SER0 wiring excludes side memory,
intermediate measurements, and retained transcripts. These resource definitions are part of the
theorems, not incidental implementation details.
    Fifth, the soft-list extension assumes rewards in [0, 1] and total reward budget at most ℓ for
each outcome. General cost matrices with negative entries or larger column sums are outside the
theorem.
    Within these limits, the result gives a closed answer to a precise question: what can support
dependence alone certify about quantum list decisions? The answer is the independence polytope
of a matroid union. It yields arbitrary prior bounds, an integer congestion deficit, an exact
obstruction-disappearance threshold, and a process-tester version under the stated Choi interface.
The simplex and hemisphere examples show both sides of the boundary: the cap can be exactly
attained by an all-distinct nonorthogonal family, but support combinatorics alone cannot replace
quantum geometry. The channel theorems then identify two settings in which architecture
optimization does close exactly: feedback doubles the number of resolved laminar cells at every
call, while complete unitary frames convert the Schmidt spectrum and wiring dimension into
exact success laws.


Data and code availability
The accompanying source package contains the LATEX manuscript, bibliography, claim ledger,
priority audit, research memo, and four standard-library Python verifiers. They perform exact
rational or algebraic checks and require no network access or external data.


AI-assistance disclosure
The author used AI assistance for literature triage, algebraic cross-checks, code generation, and
editorial revision. The mathematical claims, conventions, and final responsibility remain with
the author.


References
 [1] Somshubhro Bandyopadhyay, Rahul Jain, Jonathan Oppenheim, and Christopher Perry.
     Conclusive exclusion of quantum states. Physical Review A, 89:022336, 2014.



                                               18
 [2] Jonathan W. Webb, Ittoop V. Puthoor, Joseph Ho, Jonathan Crickmore, Emma Blakely,
     Alessandro Fedrizzi, and Erika Andersson. Experimental demonstration of optimal unam-
     biguous two-out-of-four quantum state elimination. Physical Review Research, 5:023094,
     2023.

 [3] Lluis Eriksson. Matroidal Bayes bounds for general quantum process discrimination: Canon-
     ical compression, support congestion, and exact qubit phase families. Archive for Rigorous
     Research, ARR-2026-7CCV86W3Y59VS8PN, 2026.

 [4] Giulio Chiribella, Giacomo Mauro D’Ariano, and Paolo Perinotti. Theoretical framework
     for quantum networks. Physical Review A, 80:022339, 2009.

 [5] Michal Sedlak, Daniel Reitzner, Giulio Chiribella, and Mario Ziman. Incompatible measure-
     ments on quantum causal networks. Physical Review A, 93:052323, 2016.

 [6] Jessica Bavaresco, Mio Murao, and Marco Túlio Quintino. Unitary channel discrimination
     beyond group structures: Advantages of sequential and indefinite-causal-order strategies.
     Journal of Mathematical Physics, 63:042203, 2022.

 [7] Aram W. Harrow, Avinatan Hassidim, Debbie W. Leung, and John Watrous. Adaptive
     versus nonadaptive strategies for quantum channel discrimination. Physical Review A,
     81:032339, 2010.

 [8] Jessica Bavaresco, Mio Murao, and Marco Túlio Quintino. Strict hierarchy between parallel,
     sequential, and indefinite-causal-order strategies for channel discrimination. Physical Review
     Letters, 127:200504, 2021.

 [9] Benjamin J. Stratton, Chung-Yun Hsieh, and Paul Skrzypczyk. Operational interpretation
     of the Choi rank through exclusion tasks. Physical Review A, 110:L050601, 2024.

[10] Marco Dalai, Filippo Girardi, and Ludovico Lami. Zero-error list decoding for classical–
     quantum channels, 2026. Version 2.

[11] Satyaki Manna and Anandamay Das Bhowmik. Nonlocality without entanglement in
     exclusion of quantum states, 2026.

[12] Richard Rado. A theorem on independence relations. The Quarterly Journal of Mathematics,
     os-13(1):83–89, 1942.

[13] Jack Edmonds. Minimum partition of a matroid into independent subsets. Journal of
     Research of the National Bureau of Standards, Section B, 69B:67–72, 1965.

[14] Jack Edmonds. Matroid partition. In George B. Dantzig and Arthur F. Veinott, editors,
     Mathematics of the Decision Sciences, Part I, volume 11 of Lectures in Applied Mathematics,
     pages 335–345. American Mathematical Society, 1968.

[15] Jack Edmonds. Submodular functions, matroids, and certain polyhedra. In Richard Guy,
     Haim Hanani, Norbert Sauer, and J. Schönheim, editors, Combinatorial Structures and
     Their Applications, pages 69–87, New York, 1970. Gordon and Breach.

[16] Dana Angluin. Queries and concept learning. Machine Learning, 2:319–342, 1988.

[17] Yuan Feng, Runyao Duan, and Zhengfeng Ji. Optimal dense coding with arbitrary pure
     entangled states. Physical Review A, 74:012310, 2006.

[18] Massimiliano F. Sacchi. Optimal discrimination of quantum operations. Physical Review A,
     71:062340, 2005.


                                                19
[19] Shengjun Wu, Scott M. Cohen, Yuqing Sun, and Robert B. Griffiths. Deterministic and
     unambiguous dense coding. Physical Review A, 73:042311, 2006.
[20] Giulio Chiribella, Giacomo Mauro D’Ariano, and Paolo Perinotti. Memory effects in quantum
     channel discrimination. Physical Review Letters, 101:180501, 2008.
[21] Quntao Zhuang and Stefano Pirandola. Ultimate limits for multiple quantum channel
     discrimination. Physical Review Letters, 125:080505, 2020.
[22] William H. Cunningham. Improved bounds for matroid partition and intersection algorithms.
     SIAM Journal on Computing, 15(4):948–957, 1986.
[23] Alexander S. Holevo. Statistical decision theory for quantum systems. Journal of Multivariate
     Analysis, 3(4):337–394, 1973.
[24] Horace P. Yuen, Robert S. Kennedy, and Melvin Lax. Optimum testing of multiple hypotheses
     in quantum detection theory. IEEE Transactions on Information Theory, 21(2):125–134,
     1975.
[25] Carl W. Helstrom. Quantum Detection and Estimation Theory. Academic Press, New York,
     1976.
[26] Stephen M. Barnett and Sarah Croke. Quantum state discrimination. Advances in Optics
     and Photonics, 1(2):238–278, 2009.
[27] Nathaniel Johnston, Vincent Russo, and Jamie Sikora. Tight bounds for antidistinguishability
     and circulant sets of pure quantum states. Quantum, 9:1622, 2025.
[28] Hongshun Yao and Xin Wang. Conclusive exclusion of quantum states with group action.
     Physical Review A, 113:022205, 2026.
[29] Kenji Nakahira. Quantum process discrimination with restricted strategies. Physical Review
     A, 104:062609, 2021.
[30] Farzin Salek, Masahito Hayashi, and Andreas Winter. Usefulness of adaptive strategies in
     asymptotic quantum channel discrimination. Physical Review A, 105:022419, 2022.


A     A direct derivation for deterministic lists
For completeness, specialize Theorem 4.1 to a deterministic list POVM. For A ⊆ E,
                                     XX
                              s(A) =        Tr(ML ρi )
                                        i∈A L∋i
                                                                    !
                                        X               X
                                    =       Tr ML              ρi
                                        L              i∈A∩L
                                        X
                                    ≤       |A ∩ L| Tr(ML PA )
                                        L
                                                            !
                                                  X
                                    ≤ ℓ Tr PA          ML       = ℓd(A).
                                                   L

For C ⊆ A, split A = C ∪˙ (A \ C) and use si ≤ 1 on the second part. This gives
                                    s(A) ≤ ℓd(C) + |A \ C|.
The minimization over C is not an optional relaxation: by Theorem 3.2, it is exactly the rank of
R∨ℓ .

                                                  20
