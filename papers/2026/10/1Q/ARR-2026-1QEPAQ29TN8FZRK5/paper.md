# Removing the binary and ternary factors from cyclic Weyl rank uncertainty

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
Removing the binary and ternary factors
                    from cyclic Weyl rank uncertainty
                                                Lluis Eriksson
                                     Independent researcher, Sweden

                                      24 October 2026
                             Working draft 2; domain clarifications


                                                       Abstract
          For a nonzero complex matrix in the cyclic Weyl basis, let ud (s) be the minimum rank
      under a support budget of s coefficients. We give exact formulas reducing ud to the profile
      in the part of the dimension coprime to 6. Removing a factor 2k uses a minimum over
      binary subgroup costs. Removing a factor 3k uses products of the three costs 1, 2, 3, with
      rank multipliers 3, 2, 1. The lower bounds follow from residue-sector compressions and
      central Fourier blocks; the ternary two-residue case uses a triangular minor on two sectors of
      a directed three-cycle. Upper bounds are attained by scalar cyclic projectors and binomials,
      combined with the Chinese remainder theorem. In particular, in every even dimension
      whose only prime factors are 2 and 3, the exact minimum is d/ max{q : q | d, q ≤ s}. We
      obtain sharp uniform coefficient-erasure budgets for arbitrary complex low-rank matrices.
      Residual profiles with prime factors at least 5, efficient recovery, and numerical stability
      are not determined.


1    Profiles and the main reductions
Put ωd = e2πi/d and

          Xd ej = ej+1 mod d ,     Zd ej = ωdj ej ,       Wd (a, b) = Xda Zdb ,        (a, b) ∈ (Z/d)2 .

These d2 matrices are orthogonal for the Hilbert–Schmidt inner product. For C ̸= 0, let sW (C)
count the nonzero coefficients in its unique Weyl expansion. For every integer s ≥ 1, define

                     ud (s) = min{rank C : C ∈ Md (C), C ̸= 0, sW (C) ≤ s}.

The minimum exists: the admissible set is nonempty and its ranks form a nonempty subset of
{1, . . . , d}. Thus no compactness argument is needed. The profile is nonincreasing, ud (1) = d,
and ud (s) = 1 for s ≥ d, by the diagonal rank-one projector. We use u1 (s) = 1.
Theorem 1 (Binary transfer). For odd m ≥ 1, k ≥ 0 and s ≥ 1,

                                  u2k m (s) = min 2k−a um (⌊s/2a ⌋) .
                                                   0≤a≤k
                                                    2a ≤s

    For ternary transfer define, for 3 ∤ m,
                                                        k
                                                                     !
                                                        Y
                    Fk,m (s) =         min                  (4 − ri ) um (⌊s/(r1 · · · rk )⌋) .
                                 r1 ,...,rk ∈{1,2,3}
                                      r1 ···rk ≤s       i=1


The empty tuple gives F0,m (s) = um (s).

                                                          1
```

---

## Page 2

```text
Theorem 2 (Ternary transfer). For 3 ∤ m, m ≥ 1, k ≥ 0 and s ≥ 1,

                                        u3k m (s) = Fk,m (s).

   The unknown residual profiles are retained as functions, not replaced by an assumed
uncertainty conjecture. All coefficients are arbitrary complex numbers, and sharpness means a
support budget, not exactly s terms.
Corollary 3 (An even residual formula). Let h = 2a 3b with a ≥ 1, b ≥ 0, and let gcd(m, 6) = 1.
Then
                                              h
                                uhm (s) = min um (⌊s/q⌋) .
                                          q|h q
                                               q≤s

In particular, if d = 2a 3b is even and Qd (s) = max{q : q | d, q ≤ s}, then

                                         ud (s) = d/Qd (s).

    The scalar uncertainty profile in prime-power dimension is classical [2]; Meshulam’s
subgroup–quotient argument explicitly uses a smallest occupied coset and a product con-
straint on support sizes [1, Proposition 1.3 and Section 2]. We credit that architecture. The
proposed operator contribution is the exact transfer of the rank profile through the noncom-
muting cyclic representation, using the block identities below. Earlier work in the author’s
programme covers low prime-power sparsity and a binary seven-term range [3, 4]. The present
argument replaces the binary overlap classification and treats the ternary profile in every
sparsity range.
    Yin studies the closely related Hermitian traceless rank-two problem in all cyclic dimensions,
together with phase-retrieval and equality statements [5]. Our profile allows arbitrary complex
matrices and all rank bounds, but does not give the stronger positivity, trace, or phase-retrieval
classifications of that setting. The reference’s formalization claims have not been replayed
here. These comparisons are limited readings, not an exhaustive certificate of priority. The
cyclic basis is not being identified with a tensor-qubit Pauli basis.


2    Compression identities and small Fourier bounds
Left multiplication by a Weyl unitary translates the support, up to nonzero phases, and
preserves rank. Discrete Fourier conjugation interchanges the two label coordinates, up to a
sign and phases.
Lemma 4 (Residue sectors). Let d = pn for p = 2 or 3 and Ej = span{ej+pu : u ∈ Z/n},
0 ≤ j < p. For a = pA + δ, 0 ≤ δ < p, put j ′ = (j + δ) mod p and κ = ⌊(j + δ)/p⌋. Then

                                 Wd (a, b)|Ej →Ej ′ = ωdbj XnA+κ Znb .

Within a fixed first-coordinate residue class, distinct labels merge precisely in cosets of ⟨(0, n)⟩.
An occupied class gives a nonzero block somewhere. A coset with r occupied labels activates at
least p − r + 1 blocks, for 1 ≤ r ≤ p.
Proof. The output index on ej+pu is j ′ + p(u + A + κ) modulo d, and the phase is ωdbj+pbu .
This is the displayed formula. The compressed label is (A mod n, b mod n) after factoring the
common carry. In a merging coset, write b = β + nℓ; its coefficient, after a nonzero common
factor, is p−1        2πiℓj/p . Different cosets give different compressed Weyl labels. Thus an
           P
             ℓ=0 cℓ e
occupied class cannot vanish in all blocks, by invertibility of this transform.
    For p = 2, one input activates both outputs and two inputs activate at least one. For
p = 3, one input activates three outputs; two inputs cannot have just one output, because the

                                                  2
```

---

## Page 3

```text
inverse of a single Fourier spike has all three entries nonzero; three inputs activate at least one.
These are precisely the claimed bounds. No assumption on coefficient signs or algebraicity is
used.

Lemma 5 (Central blocks). Let d = p2 n, p = 2 or 3, and suppose the support lies in
p(Z/d)2 . The commuting unitaries Xdpn , Zdpn are central on this support algebra. Their p2 joint
eigenspaces have dimension n, are invariant under C, and carry cyclic Weyl representations.
Distinct cosets of H = ⟨(pn, 0), (0, pn)⟩ give distinct Weyl labels in every block. Within an
H-coset the coefficients transform by ordinary Fourier transform on (Z/p)2 , apart from nonzero
scalar factors.

Proof. Let ζp = e2πi/p . For α, β ∈ {0, . . . , p − 1}, the joint eigenspace has the orthogonal basis
                                          p−1
                         vtα,β = ωd−pβt         ζp−βℓ eα+pt+pnℓ ,
                                          X
                                                                             0 ≤ t < n.
                                          ℓ=0
                       √
Its vectors have norm p; normalizing gives orthonormal bases. The two eigenvalues are ζpβ
and ζpα . The bases exhaust Cd . Direct action, including wrap-around, gives

                              Wd (pA, pB)|Eα,β = ωdpβA+pαB XnA ZnB .                              (1)
              2
The factor ωdp is primitive of order n, also for arbitrary n. Representatives 0 ≤ A, B < n label
the n2 distinct compressed Weyls.
   The labels in one coset are (pA + pnϵ, pB + pnη), 0 ≤ ϵ, η < p. By (1) its compressed
coefficient is
                                                     p−1
                                      ωdpβA+pαB
                                                     X
                                                            cϵ,η ζpβϵ+αη .
                                                    ϵ,η=0

This proves both the Fourier assertion and injectivity between cosets. The formula remains
valid when n = 1.

   Put D(r) = 2⌊log2 r⌋ for r ≥ 1, and define

                        ϕ9 (r) =      min       (4 − u)(4 − v),              1 ≤ r ≤ 9.
                                   u,v∈{1,2,3}
                                      uv≤r

Lemma 6 (Central Fourier support). A nonzero vector on (Z/2)2 with r occupied entries
has at least 4/D(r) nonzero Fourier coefficients. On (Z/3)2 , the corresponding lower bound is
ϕ9 (r).

Proof. For four entries, r = 1 gives four outputs. For r = 2, 3, a single output is impossible
because its inverse has all four entries nonzero. For r = 4, invertibility suffices. The bound at
r = 3 is deliberately not sharpened.
    For nine entries, group by one coordinate. Let v be the number of occupied fibers and u
the smallest fiber support; then uv ≤ r. Transform that fiber first: at least 4 − u coordinate
frequencies remain. Each such nonzero vector along the other coordinate has support at most
v, and hence at least 4 − v Fourier outputs by Lemma 4’s three-point argument. Thus there
are at least (4 − u)(4 − v) ≥ ϕ9 (r) outputs. This is the elementary coset argument credited
above.

Lemma 7 (Two shifts on three sectors). Suppose a matrix on three equal-sized input/output
sectors has exactly two possible block shifts. If one shift has L nonzero blocks, each of rank at
least ρ, then the whole matrix has rank at least min(L, 2)ρ.

                                                      3
```

---

## Page 4

```text
Proof. Permute output sectors to place the chosen shift on the diagonal. The other shift
is a nonzero translation on Z/3, a directed three-cycle. Any two sectors induce at most
one off-diagonal direction, so their block submatrix is triangular after an ordering. Select
a nonsingular minor of full rank in each of its two diagonal blocks. Together these give a
triangular minor with nonzero determinant, even when the full diagonal blocks are singular. If
L = 1, use that block alone.


3     Upper bounds and attainable costs
For coprime r, m, the CRT unitary ej 7→ ej mod r ⊗ ej mod m sends
                                                            −1 mod r         −1 mod m
                   Xrm 7→ Xr ⊗ Xm ,          Zrm 7→ Zrm                    r
                                                                        ⊗ Zm            .

Consequently it bijectively identifies Weyl labels with pairs of labels. Tensor products multiply
ranks and support sizes. A factor of dimension one is treated directly, without modular-inverse
notation.
   For q | N , let
                                                q−1
                                                X        ℓN/q
                                         Pq =         ZN        .
                                                ℓ=0

It equals q on diagonal positions divisible by q, and zero elsewhere. Thus it has support q and
rank N/q. This proves the upper bound in Theorem 1 by taking N = 2k , q = 2a and tensoring
a matrix attaining the residual budget.
    For ternary transfer, two entries ri = rj = 2 in the product defining Fk,m may be replaced
by 3, 1: cost drops from 4 to 3, the rank multiplier drops from 4 to 3, and the residual budget
increases. Hence the minimum is attained with at most one 2. It is the minimum of the
following two families, retaining only positive residual budgets:

                3k−a um (⌊s/3a ⌋),                                  0 ≤ a ≤ k,   3a ≤ s,
                2 3k−a−1 um (⌊s/(2 3a )⌋),                          0 ≤ a < k,   2 3a ≤ s.

The first is attained by P3a on N = 3k . For the second use
                                             N/(3·3a )              
                                      P3a ZN             − ζ3 I .

The two exponent sets are disjoint modulo N , giving exactly 2 3a terms. Among the N/3a
nonzero positions of P3a , one third vanish in the second factor. Its rank is 2N/(3 · 3a ). CRT
and a residual minimizer now prove the upper bound of Theorem 2.


4     Lower bounds by induction
We prove the two transfer theorems separately by induction on k, holding m fixed. It suffices
to treat actual support s0 , because both proposed minima are nonincreasing in the budget.

4.1   Binary transfer
The base k = 0 is the definition of um . If some coordinate has both parities, exchange
coordinates if necessary and take the smaller first-coordinate class. Lemma 4 gives a nonzero
block of dimension d/2 with support at most ⌊s0 /2⌋. Induction   j       bounds
                                                                          k     its rank by the
                              ′           a′            k−a′           a′
minimum over indices 1 ≤ a ≤ k with 2 ≤ s0 of 2              um ( s0 /2 ). This is at least the
                                                 ′
desired minimum, which additionally permits a = 0.

                                                 4
```

---

## Page 5

```text
Otherwise translate the support to even labels. If k = 1, d = 2m, the two invariant sectors
carry
                                           Bj A 2B
                          Wd (2A, 2B) 7→ ωm   Xm Zm ,       j = 0, 1.
Multiplication by 2 is invertible modulo m. The blocks are equivalent: conjugation by Xm     h

with −2h ≡ 1 (mod m) changes the first into the second. Thus rank C ≥ 2um (s0 ), the a′ = 0
candidate. For m = 1 this case has only one label and is immediate. These are two equivalent
representations, not two independently variable algebra blocks.
    If k ≥ 2, put n = d/4 and apply Lemma 5. Let t be the number of occupied central cosets
and r their minimum occupancy, so rt ≤ s0 and 1 ≤ r ≤ 4. At least 4/2ℓ blocks are nonzero,
where ℓ = ⌊log2 r⌋. Each has support at most t. Its rank is at least un (t), and ranks add over
invariant blocks. For every index a in the inductive formula for un (t), put a′ = a + ℓ. Then
                                     ′                                       ′
                                                                    j            k
                       a′ ≤ k,     2a ≤ rt ≤ s0 ,       ⌊t/2a ⌋ ≤ s0 /2a .

                                                    ′
                                                          j     ′
                                                                    k
Its scaled rank candidate is therefore at least 2k−a um ( s0 /2a ), and hence at least the desired
minimum. All arguments of the profiles are positive. Their definition for every positive budget
handles t ≥ n without an out-of-domain induction. This proves the lower bound of Theorem 1.

4.2   Ternary transfer
The base is again k = 0. Suppose some coordinate varies modulo 3, and make it the first. If
all three first-coordinate residues occur, a smallest class has at most ⌊s0 /3⌋ terms and supplies
a nonzero block. Thus
                               rank C ≥ Fk−1,m (⌊s0 /3⌋) ≥ Fk,m (s0 ).
The last inequality follows by prepending r = 3 to each eligible tuple.
   If exactly two residues occur, choose a smaller class of size M ≤ ⌊s0 /2⌋. Let it occupy t
cosets of ⟨(0, d/3)⟩, and let r ≤ 3 be the smallest coset size. Then rt ≤ M . At least 4 − r
blocks are nonzero, each of rank at least ud/3 (t). By Lemma 7, r = 1 or 2 gives

                            rank C ≥ 2Fk−1,m (⌊s0 /2⌋) ≥ Fk,m (s0 ),

by monotonicity and prepending r = 2. If r = 3, necessarily s0 ≥ 6, and a single nonzero block
yields
                  rank C ≥ Fk−1,m (⌊s0 /6⌋) ≥ Fk−1,m (⌊s0 /3⌋) ≥ Fk,m (s0 ).
Thus neither existence nor rank additivity for arbitrary blocks is assumed.
   It remains that both coordinates have fixed residues. Translate to 3G. When k = 1, 3 ∤ m,
the three invariant sectors carry
                                          Bj A 3B
                          Wd (3A, 3B) 7→ ωm Xm Zm ,           j = 0, 1, 2.

These have distinct labels, and are conjugate by Xm    h with −3h ≡ j (mod m). Their equal

ranks sum to at least 3um (s0 ), the all-ri = 1 candidate. The case m = 1 is immediate.
   For k ≥ 2, put n = d/9. Lemmas 5 and 6 give nine invariant blocks. If t cosets are occupied
and r is their minimum occupancy, at least ϕ9 (r) blocks are nonzero. Thus

                             rank C ≥ ϕ9 (r)Fk−2,m (t),       rt ≤ s0 .

Choose u, v attaining ϕ9 (r), and a tuple attaining Fk−2,m (t) with cost w ≤ t. The concatenated
tuple is eligible for Fk,m (s0 ), because uv ≤ r and uvw ≤ s0 . Also ⌊t/w⌋ ≤ ⌊s0 /(uvw)⌋.
Monotonicity of um makes that candidate at most ϕ9 (r)Fk−2,m (t), proving the required bound.
This completes Theorem 2 in its entire stated domain.

                                                5
```

---

## Page 6

```text
5    Removing both factors and the divisor law
Proof of Corollary 3. Apply Theorem 1 with odd residual 3b m, then Theorem 2. Floor
composition is exact for positive integer costs. Candidates without a ternary cost 2 are
                                     j          k
                       2a−i 3b−j um ( s/(2i 3j ) ),        0 ≤ i ≤ a, 0 ≤ j ≤ b.

These are precisely the divisor candidates in the corollary. A candidate with a ternary cost 2
has cost 2i+1 3j and multiplier 2a−i+1 3b−j−1 , with j < b.
    If i < a, replace it by the divisor candidate at cost 2i+1 3j : its multiplier is 2a−i−1 3b−j ,
smaller by a factor 3/4, and its residual budget is unchanged. If i = a, use instead the divisor
cost q ′ = 2a−1 3j+1 , which is 3/4 of the former cost. Its multiplier is the same, 2 3b−j−1 , and
its residual budget is larger. Thus every additional candidate is dominated. For m = 1 the
residual profile is constant one, and minimizing d/q chooses the largest eligible divisor.

    For a purely ternary dimension d = 3k , the same proof also gives
            ud (s) = (4 − c)3k−t−1       when   c3t ≤ s < (c + 1)3t ,         c ∈ {1, 2}, s < d,
and ud (s) = 1 for s ≥ d. For a purely binary dimension it gives d/2min(k,⌊log2 s⌋) . The scalar
profiles are recovered as operator profiles here; no scalar theorem is silently used to justify the
noncommuting lower bound.

               d   budget s     product bound ⌈d/s⌉            exact ud (s)     subgroup cost
              54           8                               7             9                   6
              72          11                               7             8                   9
             108           8                              14            18                   6
             108          17                               7             9                  12

The elementary product bound follows from ∥C∥2F = d |cg |2 and ∥C∥2op ≤ s |cg |2 . The
                                                                   P                          P

divisor law is specific to the stated dimensions. For example, in dimension 10, a degree-three
polynomial in Z10 2 with three distinct fifth roots as zeros has at most four Weyl terms and

rank four. This is below 10/ max{q | 10 : q ≤ 4} = 5. There is no claim of a divisor-step law
for all composite dimensions.


6    Sharp erasure budgets
Let d be even with only prime factors 2, 3. For an integer R ∈ {1, . . . , d}, set
                                 qd (R) = min{q : q | d, qR ≥ d}.
Corollary 8. The minimum support of a nonzero complex matrix of rank at most R is qd (R).
On the set of all complex matrices of rank at most R, the largest universally safe number of
omitted Weyl coefficients is qd (2R) − 1 if 2R < d, and zero if 2R ≥ d.
Proof. The first statement is the inverse of the divisor profile; the witness Pqd (R) attains it. If
two matrices of rank at most R have the same retained coefficients, their difference has rank
at most 2R and support contained in the omissions. A nonzero difference needs at least qd (2R)
coefficients.
    For failure at that number, use Pq , q = qd (2R), whose rank is d/q ≤ 2R. Split its nonzero
diagonal positions into two groups of size at most R. Put A = Pq on the first group and
B = −Pq on the second, zero elsewhere. Then A − B = Pq , while both ranks are at most R.
If 2R ≥ d, the same split of Id shows failure on erasing its single Weyl label. No omissions
retains a basis and is injective.

                                                      6
```

---

## Page 7

```text
For d = 108 and R = 4, the sharp budget is 17, with failure at 18. The product bound
alone guarantees 13. This is exact noiseless identifiability of arbitrary complex matrices. It
does not establish a recovery algorithm, conditioning estimate, or a positivity-constrained
density-matrix threshold.


7    Checks, dependencies and status
The proof is analytic for all stated dimensions. Exact auxiliary checks compare root-of-unity
monomial exponents, CRT label maps and the integer minimum identities. Finite checks do
not establish the universal quantifiers. In particular, test residual functions used for minimum
bookkeeping are explicitly artificial monotone functions, not asserted physical Weyl rank
profiles.
    The binary and ternary transfer arguments have received dependent mathematical audits.
A full assessment of draft 1 requested two domain clarifications: integer rank budgets in
Corollary 8, and admissible positive budgets in the binary induction. Both are explicit in this
revision. That assessment and its findings are preserved separately; the revised artifact has
not yet received its own assessment. An assessment of the earlier binary-only PDF does not
apply to this text.
    The residual profile for dimensions with prime factors at least 5 is not determined in
general. The two-shift proof uses the special directed three-cycle on the sector labels; it is
not asserted for an arbitrary prime number of sectors. All sharpness assertions are budget
statements, not classifications of exact-support minimizers or of all equality cases.

AI and responsibility disclosure. The named author directed OpenAI Codex assistance
in derivation, writing and exact checks. GPT-6 Astra xhigh audits used shared filesystem
and declared reused task context. No runtime isolation, independent human review, Lean
formalization, certified worldwide originality or predicted assessment score is claimed. Reports
on other exact artifacts are preserved separately and their grades are not transferred.


References
[1] R. Meshulam, An uncertainty inequality for finite abelian groups, European J. Combin. 27
    (2006), 63–67. https://arxiv.org/abs/math/0312407v1.

[2] S. Delvaux and M. Van Barel, Rank-deficient submatrices of Fourier matrices, Linear
    Algebra Appl. 429 (2008), 1587–1605. doi:10.1016/j.laa.2008.04.043. Author report TW470
    (2006): https://www.cs.kuleuven.be/publicaties/rapporten/tw/TW470.pdf.

[3] L. Eriksson, Sparse cyclic Weyl operators in prime-power dimension: an operator exten-
    sion of the scalar uncertainty law through sparsity 2p − 1, AIRR.SCIENCE, ARR-2026-
    1KTM07SEEV968BCB, v1 (2026). Version record.

[4] L. Eriksson, Sparse Weyl operators: a uniform binary rank theorem and sharp erasure
    thresholds, AIRR.SCIENCE, ARR-2026-161TZ0CP488XTTBN, v1 (2026). Version record.

[5] P. Yin, A Sharp Rank-Two Uncertainty Principle for Finite Weyl Transforms, public
    manuscript, commit 39af48a5cf2e014a14f20e3d0ce836a430fea394, pinned source, ac-
    cessed 24 October 2026.




                                               7
```
