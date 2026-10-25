# Bell and tripartite anchor sectors for finite-copy Werner witnesses

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
Bell and tripartite anchor sectors
                          for finite-copy Werner witnesses
                                                Lluis Eriksson

                                               24 October 2026


                                                   Abstract
          We establish strictly positive sectors of the Werner endpoint partial-trace form on
      rank-at-most-two coefficient matrices. A support plane must contain one specified vector,
      assembled from Bell vectors on pairs of original slots and GHZ vectors on triples of qutrit
      slots; the second vector and both coefficient covectors remain unrestricted. For a Bell pair
      we prove the required signed co-Choi comparison in every local dimension at least three,
      using a polynomial identity in a 24-diagram algebra with the dimension as a parameter. A
      separate rational certificate covers a genuinely tripartite three-qutrit GHZ block. Exact
      kernels and uniform nonunit spectral intervals give an explicit strict lower bound under any
      finite combination of these blocks, including a qutrit sector for every copy count at least two.
      A perturbation bound includes the actual dimension-dependent norm factor. The Schur and
      signed tensor-contraction mechanism is attributed to Wu and Zou; the added inputs are the
      two block comparisons and their quantitative kernels. The proof is computer assisted, with
      exact rational arithmetic and symbolic identities, not numerical spectral extrapolation. The
      support restriction remains substantive and no unrestricted finite-copy positivity or NPT
      bound-entanglement result follows.


1    The endpoint and the support restriction
          Nn     di
Let H =     i=1 C and define

                                                       (−1/2)|S| ∥TrS C∥2F .
                                                X
                                  qn (C) =                                                               (1)
                                             S⊆{1,...,n}

Traces are ordinary unnormalized partial traces over the original slots. Grouping slots does not
replace their map by the one-slot map in the product dimension. For equal local dimensions,
the usual coefficient-matrix vectorization identifies rank C with the global Alice–Bob Schmidt
rank. Nonnegativity of (1) on all rank-at-most-two matrices is the endpoint Werner problem
[1, 4]. Here we restrict one vector in a left or right support plane. The resulting sectors leave
the remaining planes unrestricted.
     Partition the slots into p pairs of dimensions (dj , dj ), dj ≥ 3, and t triples, each of dimensions
(3, 3, 3), where p + t ≥ 1 and n = 2p + 3t. Set
                        d−1                                                         p
           ud = d−1/2                      v = 3−1/2 (e000 + e111 + e222 ),               udj ⊗ v ⊗t .
                        X                                                           O
                              ei ⊗ e i ,                                       a=                        (2)
                        i=0                                                         j=1

The unit vector v does not factorize across any nontrivial cut of its three slots. Neither a Bell
pair nor this GHZ triple is a product ray over the original slots. The coefficient matrix itself
need not factorize over these blocks.




                                                           1
```

---

## Page 2

```text
Theorem 1. For the unit anchor in (2), put
                                                                         17
                       Lp,t = (27/8)p (27/4)t ,         cp,t =                         .         (3)
                                                                 81 2n (1 + 2L2p,t )

If rank C ≤ 2 and a ∈ ran C or a ∈ ran C ∗ , then

                                         qn (C) ≥ cp,t ∥C∥2F .

The same statement holds when a tensor product of original-slot unitaries is applied to a, and
when the slots are permuted together with their dimensions and block assignment.

    All constants are conservative. For every integer n ≥ 2, the uniform-qutrit setting admits
such a sector: take only pairs for even n, or one triple and the remaining pairs for odd n. This
is an existence statement for restricted sectors at those copy counts, not a statement about
every qutrit support plane.

Corollary 2. Define
                                         p
                                         Y
                                    η=         max{1, dj /2 − 1}2 .
                                         j=1

For unit vectors define the projective Euclidean distance by dpr ([z], [a]) = minθ∈R eiθ z − a . If a
left or right support plane of a rank-at-most-two C contains a unit vector z with dpr ([z], [a]) ≤ ε,
then
                                    qn (C) ≥ (cp,t − 2ηε) ∥C∥2F .
In particular ε ≤ cp,t /(4η) gives a positive bound cp,t ∥C∥2F /2.

   The radius is not uniform in dimensions or copy count.

1.1    What is prior, and what is added
The partial-trace formulation is prior [1, 4]. General two-copy results [3, 4] already give
nonnegativity for a single pair without our support restriction. Wu and Zou [5, Section 7.2,
Lemma 7.4 and Theorem 7.3] explicitly use the switched Schur complement and signed co-
Choi tensorization for a fully product support ray. Their displayed tensor argument extends
immediately to any finite number of such factors. Neither that extension nor the abstract tensor
mechanism is claimed here.
    There are also direct precedents for strict subcases: Ðoković [2, Theorem 5.1 and Proposition
4.2] proves strict positivity for the pair (I, Y ) when Y is normal and nonscalar in dimension at
least three, by unitary diagonalization. His generic-pair nonsingularity statement in Conjecture
6.1 remains a conjecture in that source. Proposition 7.1 there concerns a rank-one element in a
two-qutrit matrix plane; a Bell vector corresponds instead to Id , of matrix rank d.
    Bharti, Gajjala and Haug [4, Section 8] factorize the operator itself, with a possible rank-two
factor confined to at most two slots. Our assumption factorizes one support vector and permits
arbitrary remaining coefficient vectors. The new inputs proposed here are the universal Bell
block and the tripartite qutrit block, including their exact kernels and strict estimates. Targeted
comparisons of selected primary sources did not identify equivalent full Bell or GHZ support-
sector theorems. These comparisons are limited to the hypotheses and sections examined; they
do not certify worldwide priority.




                                                    2
```

---

## Page 3

```text
2    Schur identity and the attributed tensor mechanism
We temporarily allow arbitrary finite slot dimensions. Let Fi exchange slot i between two global
copies of H, and write
                     n
                     Y                                 O
              Wn =         (I − Fi /2),        Φn =             Φdi ,   Φd (X) = Tr(X)I − X/2.
                     i=1                                i

The grouped input/output order is fixed throughout. The factors of Wn commute and have
eigenvalues 1/2, 3/2.

Lemma 3. For a nonzero anchor a, set Ha = Φn (aa∗ ). Define Kab by row vectorization,
                                                 X
                                    (Kab )rt =         (Wn )(r,t),(s,j) as bj .                            (4)
                                                 s,j

                                                                                       −1
There is a completely positive map Ψa such that Ψa (bb∗ ) = Kab H a Kab
                                                                     ∗ . With ∆ = Φ − Ψ ,
                                                                               a   n   a

                             qn (xb∗ + ay ∗ ) = x∗ ∆a (bb∗ )x                                              (5)
                                                            1/2         −1/2             2
                                                                                 ∗
                                                 + Ha y + Ha                    Kab x        .

Proof. The swap contraction gives qn (ay ∗ ) = y ∗ Ha y ≥ 2−n ∥a∥2 ∥y∥2 , so Ha > 0. Polarization
of the same contraction gives

                     qn (xb∗ + ay ∗ ) = x∗ Φn (bb∗ )x + y ∗ Ha y + 2 Re(x∗ Kab y).

Since y ∗ Ha y = y ∗ H a y, completing the square proves (5). The bar on Ha cannot be omitted for
a complex anchor.
                                                           −1
    Let Vt b be column t of Kab . Then Ψa (X) = t,v (H a )tv Vt XVv∗ is CP because its coefficient
                                                   P

matrix is positive. With input index first, its Choi matrix is
                                    −1
                    CΨa = Ma H a Ma∗ ,
                                                                        X
                                                  (Ma )(j,r),t =               (Wn )(r,t),(s,j) as .       (6)
                                                                           s

These are identities of maps, hence apply to bb∗ entangled between blocks.

    For a map Λ, use CΛ = ij Eij ⊗ Λ(Eij ) and let Γ transpose its input factor. Positivity of
                               P

CΛΓ is complete copositivity and implies positivity of Λ.
                                                                                                       N
Lemma 4 (Signed block comparison). Suppose an anchor factors as a = j aj over blocks.
                                  Γ . If −A ≤ B ≤ A for every block, then ∆ is completely
Let Aj = CΦΓblock j > 0 and Bj = CΨ aj     j   j   j                       a
copositive.
                                            N                                  N
Proof. Equations (4)–(6) give Ha =              j Haj     j Ψaj , as map identities. Each
                                                            and Ψa =
      −1/2  −1/2
                 is a Hermitian contraction. Therefore I − j Tj ≥ 0. Congruence gives
                                                            N
Tj = Aj Bj Aj
                                          O             O
                                                Aj −             Bj ≥ 0,
                                           j                j

which, after the canonical permutation, is the co-Choi matrix of ∆a . This is the signed
tensor-contraction step already present in [5].




                                                        3
```

---

## Page 4

```text
3     A Bell block in every dimension at least three
                                                           2
                                     i ei ⊗ ei , with D = d .
                                  P
Use the unnormalized ωd =                                                   Nonzero scalar rescaling leaves Ψa
unchanged. Let

         A = (I − F1 /2)(I − F2 /2),                                   H = (d − 1)I + ωd ωdT /4,            (7)
      H −1 = I/(d − 1) − ωd ωdT /[(d − 1)(5d − 4)],                    B = (M H −1 M T )Γ ,    R = A−1 B.

Here A ≥ I/4 and A−1 = (4I/3 + 2F1 /3)(4I/3 + 2F2 /3). The contraction M , with row
(j1 , j2 , r1 , r2 ) and column (t1 , t2 ), is

                            Mjr,t = δr1 r2 δt1 j1 δt2 j2 − 21 δr1 j1 δt1 r2 δt2 j2                          (8)
                                       − 21 δr2 j2 δt2 r1 δt1 j1 + 14 δr1 j1 δr2 j2 δt1 t2 .

Proposition 5. For every integer d ≥ 3, −A ≤ B ≤ A. The matrix R has eigenvalue 1 of
multiplicity exactly d2 ; every other eigenvalue lies in [−8/9, 2/3]. Moreover
                                                              2
                                    ker(A − B) = Cd ⊗ span{ωd }.

3.1    A polynomial identity with the dimension as a parameter
A pairing of the row and column indices denotes the product of its Kronecker deltas. Compose
two pairing operators by identifying the middle indices; each closed component contributes a
factor d. Closing each top index to the corresponding bottom index gives the trace. These rules
follow by summing the repeated indices and hold in every positive integer dimension, even when
different diagrams represent dependent operators.
    Over Q[d] construct the numerator

                                        Nd = 9(d − 1)(5d − 4)R.

Only 24 pairings occur among I, Nd , . . . , Nd8 . The verifier constructs every coefficient and checks
a degree-eight relation coefficient by coefficient. Equivalently, with

              f1 (λ) = 9(d − 1)λ + 5d + 1,
              f2 (λ) = (d − 1)(5d − 4)λ − d2 − d + 4,
              f3 (λ) = 3(d − 1)(5d − 4)λ + d2 − 9d + 4,
              f4 (λ) = 3(d − 1)(5d − 4)λ + 6d2 − 13d + 4,
              f5 (λ) = 9(d − 1)(5d − 4)λ − d2 + 19d − 12,
             Qd (λ) = 27(d − 1)(5d − 4)λ2 + (15d2 − 90d + 24)λ − (6d2 + 19d + 4),

the exact operator identity is
                                                " 5               #
                                                 Y
                                    (R − I)            fi (R) Qd (R) = 0.                                   (9)
                                                 i=1

The supplement supplies the coefficient arrays and the diagram multiplication and trace
algorithms. This is a symbolic identity, not interpolation from finitely many dimensions. The
finite direct-index controls in dimensions 2, 3, 4, 5 check the transcription but are not its universal
proof.




                                                          4
```

---

## Page 5

```text
3.2   Root bounds, multiplicity and kernel
Let ri be the root of fi . Substituting d = s + 3, s ≥ 0, the differences ri + 8/9 and 2/3 − ri
have positive denominators and the following numerators after cancellation:

                            Lower endpoint difference    Upper endpoint difference
                     i=1    s                            11s + 28
                     i=2    49s2 + 231s + 248            7s2 + 21s + 20
                     i=3    37s2 + 177s + 218            11s2 + 39s + 30
                     i=4    22s2 + 99s + 119             16s2 + 65s + 63
                     i=5    41s2 + 155s + 140            29s2 + 139s + 168

For Qd , the leading coefficient is positive and the constant is negative. Its two real roots have
opposite signs. At the proposed endpoints,

                             Qs+3 (−8/9) = 262s2 /3 + 393s + 453 > 0,
                               Qs+3 (2/3) = 64s2 + 197s + 75 > 0.

Thus both roots are inside that interval. Since R is similar to the Hermitian A−1/2 BA−1/2 , (9)
proves the signed order and shows that 1 is isolated from every other possible eigenvalue.
                Q
   Put gd = Qd i fi . The same exact diagram trace verifies the rational identity

                                       Tr gd (R)/gd (1) = d2 .
                                                        
                                                                                              (10)

The root bounds ensure gd (1) ̸= 0. The matrix in (10) is the spectral projector at 1 (not
necessarily orthogonal in the original Euclidean coordinates), proving its multiplicity. To
identify the kernel, use the Schur square with x = ωd , y = −b. Positivity of ∆ makes both
summands nonnegative and forces ωd∗ ∆(bb∗ )ωd = 0. In the co-Choi convention of (6),

                               (b ⊗ x)∗ (A − B)(b ⊗ x) = x∗ ∆(bb∗ )x.

Hence positivity puts every b ⊗ ωd in the kernel; the already established nullity is exactly d2 .
This finishes Proposition 5.
    The lower dimension restriction is substantive for this sufficient comparison. For d = 2,
direct rational calculation gives an eigenvalue −11/9. Its signed gate fails although the two-qubit
endpoint form itself is nonnegative. Failure of this tool is not a negative rank-two Werner
witness.


4     A genuinely tripartite qutrit block
Now take a0 = e000 + e111 + e222 , D = 27, and
                3
                                   H = Φ⊗3     ∗
                                                        B = (M H −1 M T )Γ ,   R = A−1 B.
                Y
          A=        (I − Fi /2),        3 (a0 a0 ),
               i=1

The unnormalized a0 makes all entries rational. The map Ψ and B are unchanged when a0 is
replaced by v.

Proposition 6. For this block, −A ≤ B ≤ A. Eigenvalue 1 of R has multiplicity exactly 27,
and every other eigenvalue lies in [−7/8, 3/4]. Moreover

                                   ker(A − B) = C27 ⊗ span{a0 }.

For the unit anchor, λmin (Hv ) = 1/2.

                                                  5
```

---

## Page 6

```text
Computer-assisted exact proof. Construct H directly by
                                           2
                                               (δij I3 − Eij /2)⊗3 .
                                           X
                                  H=                                                            (11)
                                        i,j=0

Its spectrum is 3/2 with multiplicity 6, 7/4 with multiplicity 18, 9/4 with multiplicity 2, and
15/8 with multiplicity 1. Division by ∥a0 ∥2 = 3 gives the stated minimum. Construct M from
(6), invert H over the rationals, and form B. The verifier checks B = B T and the explicit
commuting-swap inverse of A.
    The nonzero-pattern graph of R partitions every one of its 729 indices into 163 invariant
components. The size counts are
                               size  1 2 4 8 12 14 27
                              count 24 63 45 6 6 18 1.
Each component is checked individually. The complete rational characteristic polynomials,
irreducible factors and multiplicities are supplied. After removing the factor for eigenvalue 1,
exact Sturm counts show that every factor has zero roots at or below −7/8 and at or above 3/4.
One factor has degree ten; it is retained rather than replaced by decimal roots. Total degrees
equal 729 and the factor (λ − 1) has total multiplicity 27. As R is similar to a Hermitian matrix,
these counts prove the asserted interval for its remaining spectrum, and therefore the signed
comparison.
    Finally the rational matrix product (A − B)(I27 ⊗ a0 ) is zero. The columns span a 27-
dimensional subspace; the multiplicity calculation shows that it is the entire kernel. Every check
uses exact arithmetic. Floating-point probes motivated this block but do not supply its sign
proof or any claim for other GHZ dimensions or lengths.


5    Tensor gap and quantitative strictness
                                    −1/2        −1/2
For either block type write Tj = Aj        B j Aj      . The map factorization and the signed tensor
lemma give the co-Choi matrix
                                       1/2          O        1/2
                                 G = Atot I −             Tj Atot ≥ 0.
                                                      j

Every factor has a unit eigenspace of the required input dimension and no other eigenvalue
of modulus one. A positive nonunit spectral product either has a nonnegative factor at most
3/4, or has at least two negative factors, whose product is at most (8/9)2 . Thus every such
product is at most 64/81. The unit product eigenspace has dimension dim H and, by the same
zero-operator Schur argument, ker G = Hin ⊗ span{a}.
    Since Atot ≥ 2−n I, congruence gives
                                                17
                                      G≥            P       ⊥.                                  (12)
                                               81 2n (ker G)
For clarity, congruence is not treated as a unitary similarity: if P projects off the kernel, the
nonzero eigenvalues of S ∗ P S are those of P SS ∗ P on ran P , and are at least σmin (S)2 . This
                                                  1/2
gives the stated gap after the invertible factor Atot .

Proof of Theorem 1. Choose C = xb∗ + ay ∗ with x ⊥ a and ∥b∥ = 1; the component along
a is absorbed in y. If the range is one-dimensional use x = 0. The co-Choi gap implies
x∗ ∆a (bb∗ )x ≥ g ∥x∥2 with g = 17/(81 2n ). For a unit Bell anchor, the minimum of H is
(d − 1)/d ≥ 2/3; for the GHZ block it is 1/2. Hence

                                Ha ≥ hI,            h = (2/3)p (1/2)t .

                                                     6
```

---

## Page 7

```text
The contraction definition and ∥Wn ∥ = (3/2)n give

                           ∥Kab ∥op ≤ ∥Kab ∥F = ∥Wn (a ⊗ b)∥ ≤ (3/2)n .
                  −1∗ x. Then ∥s∥ ≤ L
Set z = y, s = H a Kab                p,t ∥x∥ and the complex Schur square gives

                                   qn (C) ≥ g ∥x∥2 + h ∥z + s∥2 .

The conjugate on y is essential; omitting it does not give a valid complex-vector inequality.
Orthogonality yields

                       ∥C∥2F = ∥x∥2 + ∥y∥2 ≤ (1 + 2L2p,t ) ∥x∥2 + 2 ∥z + s∥2 .

Consequently the lower coefficient is min{g/(1 + 2L2p,t ), h/2} = cp,t . To see the indicated
minimum, note g/h = (17/81)(3/8)p (1/4)t < 1/2 when p + t ≥ 1. Adjunction preserves qn and
the Frobenius norm and gives the right-support case. Conjugation of C by original-slot local
unitaries preserves every partial-trace norm, proving the stated local action on the anchor and
slot symmetries.

Proof of Corollary 2. The Hilbert–Schmidt self-adjoint local superoperator Ld (X) = X −
Tr(X)Id /2 has eigenvalues 1 and 1 − d/2. Thus its norm is max{1, |1 − d/2|} and the tensor
superoperator for qn has norm η. Phase-align z with a. A rotation in their two-dimensional span
gives a global unitary U with U z = a and ∥U − I∥op = ∥z − a∥ ≤ ε. Put D = U C. Its rank
and Frobenius norm are preserved and Theorem 1 applies. Continuity, rather than invariance
under this global one-sided unitary, gives

                  |qn (C) − qn (D)| ≤ η(∥C∥F + ∥D∥F ) ∥C − D∥F ≤ 2ηε ∥C∥2F .

Apply adjunction for a right support plane.


6    An explicit sector beyond product rays and code planes
On three qutrit slots use unnormalized vectors

           a0 = e000 + e111 + e222 ,    x = e012 + e120 + e201 ,     z = e021 + e102 + e210 ,

These are the unnormalized basis vectors of the known Cleve–Gottesman–Lo qutrit secret-
sharing code [6, Eq. (1)]. Its constant single-share reductions and correction of one erasure
are prior properties of that code. Put C = a0 a∗0 + x(x + z)∗ . The two defining vector pairs
are independent, so rank C = 2, with column plane span{a0 , x} and row plane span{a0 , x + z}.
The GHZ anchor belongs to the first plane.
    For each single slot, the reductions of a0 a∗0 , xx∗ , zz ∗ are I3 , while every cross reduction
between the three displayed vectors is zero. Consequently every nonzero vector in either support
plane has a one-slot reduction proportional to I3 . Neither plane contains a product ray over the
original slots. More strongly, the column plane cannot be contained in the span of any family
of product vectors that is locally orthonormal in every slot, the code hypothesis used in [5,
Appendix C.2]. Such a family has at most three elements. In a hypothetical code basis, the
full-rank reduction of a0 a∗0 forces all three coefficients of a0 to be nonzero. The vanishing cross
reduction of a0 x∗ then forces every coefficient of x to vanish, a contradiction. This argument
permits arbitrary changes of local bases.
    The matrix is nonnormal because its row and column ranges differ. Direct original-slot
partial traces give squared norms 27 without a trace, 9 for each one-slot trace, 12 for each
two-slot trace, and 36 for the full trace. Hence

                ∥C∥2F = 27,        q3 (C) = 27 − 12 (3 · 9) + 41 (3 · 12) − 18 (36) = 18.

                                                   7
```

---

## Page 8

```text
Exact realignment has rank 9 across every singleton-versus-pair slot cut, so the operator does
not factorize across any proper slot cut. The executable control is included in the supplement.
These are concrete distinctions between hypotheses of the cited product-ray, code-plane and
operator-factorization results; they are not a proof that no other prior reduction exists.


7    Reproduction, attribution and limits
The supplement contains the diagram algebra, its polynomial coefficient certificate and projector-
trace computation; direct index checks in dimensions 2 through 5; and every component
polynomial and Sturm check for the qutrit GHZ block. The Bell certificate has a symbolic
dimension parameter. The GHZ certificate is one exact finite block; it is not a claim for arbitrary
tripartite dimension, GHZ length or support vector. Every downstream tensor step is analytic
for all finite block counts.
    The programs use Python 3.12.14 and SymPy 1.14.0. No floating-point result is used to
prove the spectral assertions. Development incidents and the uncorrected complex-conjugation
statements in precursor proposals are retained in the research archive. The present square and
kernel arguments use the corrected conjugations. Construction audits and exact-manuscript
assessment remain separate tasks. The certificate is computer assisted and is not a Lean or
independently kernel-checked formalization.
    The constants decay with block count and the perturbation radius shrinks further when
dimensions increase. No optimality, positive measure uniform in dimension, operational distilla-
tion protocol, exclusion of all negative witnesses, or unrestricted finite-copy theorem is claimed.
Existing two-copy nonnegativity and the signed tensor mechanism are not rebranded as new.
A complete historical priority claim would require more than the targeted source comparison
reported here.

AI and responsibility disclosure. The named author directed OpenAI Codex assistance
in derivation, writing and exact computational work. Requested GPT-6 Astra xhigh audits
used shared files and reused context; their model identity and settings were not independently
attested. No runtime isolation, independent human review, Lean formalization or certified
worldwide originality is claimed. The author is responsible for the manuscript and its claims.
Model reports concern exact artifact versions and do not constitute AIRR admission.


References
[1] P. Costa Rico, New partial trace inequalities and distillability of Werner states, Letters in
    Mathematical Physics 115, 47 (2025). doi:10.1007/s11005-025-01935-y.
[2] D. Ž. Ðoković, On two-distillable Werner states,             Entropy 18(6),      216 (2016).
    arXiv:1003.4337v3; doi:10.3390/e18060216.
[3] J. Fu, L. Gao and S.-J. Park, A solution to 2-copy distillability of Werner states,
    arXiv:2607.21367v3 (2026).
[4] K. Bharti, R. Gajjala and T. Haug, Two-copy nondistillability of Werner states: sharp
    partial-trace inequalities and finite-copy extensions, arXiv:2607.24479v1 (2026).
[5] T. Wu and Q. Zou, Sharp Plücker Geometry for Three-Copy Werner Distillation,
    arXiv:2608.02647v1 (2026).
[6] R. Cleve, D. Gottesman and H.-K. Lo, How to share a quantum secret, Physical Review
    Letters 83, 648–651 (1999). arXiv:quant-ph/9901025v1; doi:10.1103/PhysRevLett.83.648.


                                                8
```
