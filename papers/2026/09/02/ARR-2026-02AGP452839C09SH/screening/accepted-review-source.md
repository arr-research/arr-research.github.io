# A finite geometry of low-rank three-list Weyl probes in ternary dimensions

Lluis Eriksson — 6 September 2026.

Review revision 1, 6 September 2026. This cycle has not been submitted or published.

## Abstract

For the single cyclic Weyl basis in dimension $d=3^k$, $k\ge2$, we classify every reduced probe state of rank strictly below $7d/9$ that permits perfect channel identification with lists of at most three labels. Every such state belongs to a fixed commuting algebra with nine equal-dimensional character cells. The states form exactly 150 disjoint relative interiors: twelve vertices, sixty-six edges and seventy-two triangles, indexed by lines in the affine plane of order three. Their ranks, spectra, unique projector decompositions and minimum numbers of three-sparse positive squares are explicit. Exactly twelve states in this stratum permit two labels. The result gives $\ell_{\min}^{\rm exact}(d,5d/9)=3$ and $\ell_{\min}^{\rm exact}(d,4d/9)=4$, so exact-rank list complexity need not decrease with rank. A three-term example at rank $7d/9$ leaves the fixed commuting algebra, showing that the cutoff for the structural classification is sharp. The proof uses the previously established prime-power trinomial rank reduction and standard character averaging; the new step is a rigidity and positive-sum classification. A standard-library verifier checks all 4,095 nonempty line subsets and exact matrices in dimensions 9, 27 and 81.

## 1. Setting and main statement

Let $X|j\rangle=|j+1\bmod d\rangle$, $Z|j\rangle=e^{2\pi i j/d}|j\rangle$, and $W_{a,b}=X^aZ^b$. The Weyl sparsity $s_W(C)$ is the number of nonzero coefficients of $C$ in this basis, indexed by $\mathbb Z_d^2$. All statements concern this fixed cyclic representation. Replacing it with a tensor product of $k$ qutrit Pauli bases changes the sparsity problem.

Consider one use of the $d^2$ channels $\operatorname{Ad}(W_{a,b})$, a pure entangled probe, and an arbitrary final POVM. A perfect list decoder always reports a set containing the true label. Write $\mathcal F_\ell(d)$ for the reduced density matrices of probes permitting lists of at most $\ell$ labels. Write $\ell_{\min}(\rho)$ for the minimum list size at a fixed reduced state, and $\ell_{\min}^{\rm exact}(d,r)$ for its minimum over states of rank exactly $r$.

Throughout the main theorem, $d=3^k$ and $k\ge2$. Put

\[
 U=X^{d/3},\qquad V=Z^{d/3},\qquad \omega=e^{2\pi i/3}.
 \tag{1}
\]

These operators commute, have order three, and generate nine distinct Weyl labels. Their joint eigenspaces $E_{x,y}$, defined by $U=\omega^x$ and $V=\omega^y$, have dimension $d/9$ for every $(x,y)\in\mathbb F_3^2$.

For an affine line $L=\{(x,y):ax+by=c\}$, with $(a,b)$ represented by one of $(1,0),(0,1),(1,1),(1,2)$, define

\[
 P_L=\sum_{(x,y)\in L}P_{E_{x,y}}
     =\frac13\sum_{t=0}^2\omega^{-ct}(U^aV^b)^t,
 \qquad \sigma_L=\frac3dP_L.
 \tag{2}
\]

There are twelve distinct $P_L$, all of rank $d/3$. A triangle of lines will mean three pairwise nonparallel affine lines with no common intersection point.

**Theorem A (complete low-rank state classification).** Every $\rho\in\mathcal F_3(d)$ with $\operatorname{rank}\rho<7d/9$ has exactly one expression

\[
 \rho=\sum_{L\in S}\lambda_L\sigma_L,
 \qquad \lambda_L>0,\qquad \sum_{L\in S}\lambda_L=1,
 \tag{3}
\]

where $S$ is one of the following line families. Conversely, every state in this table belongs to $\mathcal F_3(d)$ and has the stated rank.

| Family $S$ | Number of families | Rank | Minimum number $\nu_3(\rho)$ of three-sparse squares |
|---|---:|---:|---:|
| One line | 12 | $d/3$ | 1 |
| Two nonparallel lines | 54 | $5d/9$ | 2 |
| Two parallel lines | 12 | $2d/3$ | 1 |
| A triangle of lines | 72 | $2d/3$ | 3 |

The representation is unique among positive convex combinations of the twelve states $\sigma_L$, after zero coefficients are removed. The scalar $\nu_3$ counts nonzero factors in $\rho=\sum_j C_jC_j^*$ with $s_W(C_j)\le3$. It does not count the channel labels on a measurement outcome or the minimum number of POVM outcomes.

The relative interiors in the table are disjoint. Together with their boundary faces they form a finite simplicial complex of twelve vertices, sixty-six edges and seventy-two triangles. This is a description of the low-rank part of $\mathcal F_3(d)$, not of its full convex body.

**Theorem B (list size, rank creation and a four-label family).** In the stratum of Theorem A, exactly the twelve midpoints of the parallel edges permit two labels. Their states are

\[
 \rho=\frac{3}{2d}(I-P_L),\qquad L\text{ an affine line}.
 \tag{4}
\]

Their minimum list size is two. Every other state in Theorem A has minimum list size three. In particular,

\[
 \ell_{\min}^{\rm exact}(d,5d/9)=3,
 \qquad \ell_{\min}^{\rm exact}(d,4d/9)=4.
 \tag{5}
\]

**Theorem C (sharp cutoff).** There is a three-sparse square of rank $7d/9$ that does not belong to the linear span of the nine character projectors $P_{E_{x,y}}$. Thus $7d/9$ cannot be included in the universal conclusion that all feasible states lie in the algebra of (1).

Theorems A–C concern exact zeros, exact Schmidt rank and finite-dimensional pure probes. They make no claim about approximate decoding, arbitrary composite dimensions or the rank strata at and above $7d/9$.

## 2. Sparse positive squares and physical decoding

We recall the operational reduction, including its normalization. This is the Weyl specialization used in the preceding work, consistent with the general learning-width and factor-width correspondence of Johnston, Lovitz, Russo and Sikora, Lemma 9 and Corollary 11 [2].

**Lemma 1 (covariant factorization).** A density matrix $\rho$ belongs to $\mathcal F_\ell(d)$ if and only if

\[
 \rho=\sum_j C_jC_j^*,\qquad s_W(C_j)\le\ell.
 \tag{6}
\]

We fix the vectorization convention

\[
 |A\rangle\!\rangle=\sum_{i=0}^{d-1}\sum_{\alpha=1}^r
 A_{i\alpha}|i\rangle\otimes|\alpha\rangle.
\]

Thus the partial trace over the channel factor of $|B\rangle\!\rangle\langle\!\langle B|$ is $(B^*B)^T$, where the transpose is taken in the displayed ancilla basis.

**Proof.** Write $\rho=AA^*$ with $A\in\mathbb C^{d\times r}$ of full column rank, and use the probe $|A\rangle\!\rangle$. Spectrally refine the measurement effects into vectors $|B_j\rangle\!\rangle$. An outcome amplitude has the form $\operatorname{Tr}(AB_j^*W_g)$. Perfect decoding forces these amplitudes to vanish outside the reported list. Weyl trace orthogonality identifies their support, up to label inversion and phases, with the Weyl support of $AB_j^*$. Taking a partial trace of the POVM normalization gives $\sum_j(B_j^*B_j)^T=dI_r$; transposing yields $\sum_j B_j^*B_j=dI_r$. Hence $C_j=AB_j^*/\sqrt d$ proves (6).

Conversely, positivity in (6) implies $\operatorname{ran}C_j\subseteq\operatorname{ran}A$. Put $B_j^*=A^+C_j$. Then $AB_j^*=C_j$ and $\sum_j B_j^*B_j=I_r$. The twirl identity is

\[
 \sum_g|W_gB\rangle\!\rangle\langle\!\langle W_gB|
 =dI_d\otimes(B^*B)^T.
\]

Consequently Weyl twirling gives the POVM

\[
 M_{j,g}=\frac1d|W_gB_j\rangle\!\rangle
                 \langle\!\langle W_gB_j|,
 \qquad \sum_{j,g}M_{j,g}=I_{dr}.
 \tag{7}
\]

On outcome $(j,g)$, report $\{h:\operatorname{Tr}(C_jW_g^*W_h)\ne0\}$. This has at most $\ell$ labels and contains every label with nonzero outcome probability. QED.

A positive sum satisfies $\ker\sum_j C_jC_j^*=\bigcap_j\ker C_j^*$. In particular every factor has range contained in the range of the sum. This elementary consequence of positivity will enforce the rigidity of all summands at once.

## 3. The rank threshold forces an order-three algebra

For clarity, the needed part of the earlier trinomial reduction [1] is proved here. Character averaging, cyclic Weyl-pair normal forms and their central characters are established tools; see [3,4].

If commuting phased Weyls generate a label group $H$ of order $h$, every joint character space has dimension $d/h$. Indeed, after dividing by one simultaneous character the operators form an honest representation of $H$. Its character projector is $h^{-1}\sum_{g\in H}\overline{\chi(g)}W_g$. All nonidentity Weyl terms have trace zero, so every character projector has trace $d/h$. In particular every character occurs and $h$ divides $d$.

**Lemma 2 (noncommuting ternary trinomials).** A genuine trinomial $cI+aA+bB$ with $abc\ne0$ and noncommuting phased Weyls $A,B$ in cyclic dimension $3^k$ has nullity at most two.

**Proof.** Let $u,v$ be the labels and let the scalar commutator have order $q=3^\ell>1$. The labels $qu,qv$ generate the central subgroup $R$. This is precisely the radical of the commutator pairing on $H=\langle u,v\rangle$: a combination $su+tv$ commutes with both generators exactly when $q$ divides $s,t$.

We verify $|R|=d/q$. Let $s$ be the minimum 3-adic coordinate valuation across $u,v$. A determinant-one change of label coordinates, obtained from a Bezout identity for a primitive vector, puts one generator at $(3^s,0)$ and the other at $(c_0,e)$, with $3^s$ dividing $c_0,e$. The determinant has valuation $k-\ell$, so $e$ has valuation $k-\ell-s$. Subtracting $c_0/3^s$ times $qu$ from $qv$ makes the two generators of $R$ coordinate axes. Their orders are $3^{k-\ell-s}$ and $3^s$, whose product is $3^{k-\ell}=d/q$.

Consequently each joint eigenspace of $A^q,B^q$ has dimension $q$. If their eigenvalues there are $(s_0,t_0)$, a cyclic eigenbasis for $A$ puts $B$ into a weighted cyclic shift. On this block,

\[
 \det(cI+aA+bB)=c^q-(-1)^q(a^q s_0+b^q t_0).
 \tag{8}
\]

The determinant has only its diagonal and full-cycle permutation contributions. The kernel recurrence divides only by the nonzero shift weights and by $b$, so a singular block has nullity exactly one. The pairs $(s_0,t_0)$ are distinct and of unit modulus. The equation in (8) has at most two such pairs: it is the intersection of two distinct circles after one variable is eliminated, and $a,b,c$ are nonzero. At most two blocks are singular. QED.

**Lemma 3 (square rigidity below $7d/9$).** If $C\ne0$, $s_W(C)\le3$, and $\operatorname{rank}C<7d/9$, then

\[
 CC^*=\alpha P_L+\beta P_M,
 \qquad \alpha,\beta\ge0,\quad \alpha+\beta>0,
 \tag{9}
\]

for two distinct parallel lines $L,M$. A coefficient may vanish. Conversely every matrix in (9) is a square of a matrix with at most three Weyl terms.

**Proof.** Right-multiply $C$ by the adjoint of one supported Weyl. This preserves $CC^*$, rank and sparsity, and places the identity in the relative support. One-term matrices are invertible.

A singular two-term matrix is proportional to $I-T$ for a phased Weyl $T$ having eigenvalue one. If its label order is $m$, the kernel has dimension $d/m$. Here $m$ is a positive power of three. The strict inequality $d-d/m<7d/9$ forces $m=3$. Thus its square belongs to the order-three algebra and kills one of its three eigenspaces.

For a genuine trinomial, Lemma 2 excludes noncommuting relative support, since $d-2\ge7d/9$ for $d\ge9$. If the relative support commutes, let its group have order $h$. The three coefficients are nonzero, so the circle argument permits at most two zero characters. If $h\ge9$, this gives rank at least $d-2d/h\ge7d/9$. Three distinct relative labels and $h\mid3^k$ therefore force $h=3$.

The normalized factor is a polynomial $\gamma_0I+\gamma_1T+\gamma_2T^2$ in an order-three phased Weyl. Every order-three label is in $(d/3)\mathbb Z_d^2$, so its eigenspaces are the three parallel lines in (2). The polynomial has at least one zero eigenvalue because it is singular. Its square is therefore a nonnegative combination of at most two of these orthogonal line projectors, proving (9). This establishes the shape of the square, not merely its possible rank.

Conversely, $C=\sqrt\alpha P_L+\sqrt\beta P_M$ satisfies $CC^*=\alpha P_L+\beta P_M$. Since $L,M$ are parallel, both projectors belong to the same three-dimensional span of $I,T,T^2$, so $s_W(C)\le3$. QED.

The joint cells in (1) and the identities in (2) follow from the same character averaging argument: $U,V$ commute because $d$ divides $(d/3)^2$ when $9\mid d$. They generate a group of order nine. Every nonzero order-three direction has precisely three eigenspaces, yielding four directions and twelve distinct line projectors.

## 4. Geometry, uniqueness and spectra

**Lemma 4 (small unions of affine lines).** A nonempty family of distinct lines in $\mathbb F_3^2$ has a union of fewer than seven points exactly when it is a single line, a pair of lines, or a triangle of lines. There are twelve singletons, twelve parallel pairs, fifty-four nonparallel pairs and seventy-two triangles. Each resulting support contains exactly the lines in that family, and each line has a point belonging to no other line of the family.

**Proof.** A single line has three points. Two parallel lines have six; two nonparallel lines have five. Three lines containing a parallel pair have at least seven points. Three distinct directions through one point also have seven points. Three pairwise nonparallel, nonconcurrent lines have six points, since their three pairwise intersections are distinct.

It remains to rule out a fourth line hidden in a six-point union. If the complement of six points is a line, exactly its two parallel companions avoid it. If the three complement points are noncollinear, they lie on nine distinct lines in total: each lies on four lines and their three pairwise joining lines are the only duplications. Exactly three of the twelve lines avoid the complement. Those three have no parallel pair and are nonconcurrent, since their union is contained in six points. Thus every six-point support contains precisely either its two parallel lines or its three triangle lines. A five-point union of two crossing lines contains no further line: a different line parallel to a constituent has at most one point on the union, while any other line has at most two.

There are $4\binom32=12$ parallel pairs and $\binom42\cdot3^2=54$ nonparallel pairs. Triangles are in bijection with the noncollinear triples of complement points, of which there are $\binom93-12=72$. A line in a triangle has two distinct intersection points and one private point. The assertion about private points in the remaining cases is immediate. QED.

**Proof of Theorem A.** Take a factorization (6). Each factor has rank at most $\operatorname{rank}\rho<7d/9$, so Lemma 3 expands its square into line projectors with nonnegative coefficients. Merge repeated lines and normalize the coefficients using $\operatorname{Tr}P_L=d/3$. This gives (3). Since all cell values are nonnegative, the range of the sum is exactly the union of its lines, with rank $d/9$ times its number of points. Lemma 4 gives all listed families and ranks.

Conversely, every $P_L$ is itself three-sparse, so any convex combination in (3) has a factorization (6), for example $C_L=\sqrt{3\lambda_L/d}\,P_L$. For a parallel pair, Lemma 3 combines its two terms into one factor.

To prove uniqueness, the range of $\rho$ determines the support of its nonzero character cells. Any positive line representation can use only lines contained in that support. Lemma 4 says these are exactly the indicated lines. The value on a private cell of $L$ is $3\lambda_L/d$, and therefore determines its coefficient. This proves uniqueness even against decompositions initially allowing all twelve projectors.

For the minimum number of squares, Lemma 3 forces every individual square to use at most two parallel lines. In a crossing pair or triangle, no two available lines are parallel, so each nonzero factor uses only one line. Their respective minimum counts are two and three. A singleton or parallel pair admits one factor, which is minimal. QED.

The spectra can be read directly from the cell values. The following lists all positive eigenvalues, with repetitions indicated; coincident values have their multiplicities added.

| State | Positive eigenvalues |
|---|---|
| $\sigma_L$ | $3/d$, with multiplicity $d/3$ |
| Crossing pair with weights $t,1-t$ | $(3/d)\{1,t,t,1-t,1-t\}$, each displayed entry repeated $d/9$ times |
| Parallel pair with weights $t,1-t$ | $3t/d$ and $3(1-t)/d$, each repeated $d/3$ times |
| Triangle with weights $\lambda_1,\lambda_2,\lambda_3$ | $(3/d)\{\lambda_1,\lambda_2,\lambda_3,1-\lambda_1,1-\lambda_2,1-\lambda_3\}$, each displayed entry repeated $d/9$ times |

**Example (unequal triangle weights).** Take $L_1=\{x=0\}$, $L_2=\{y=0\}$ and $L_3=\{x+y=1\}$ in $\mathbb F_3^2$, with weights $1/2,1/3,1/6$, respectively. Their private cells are $(0,2),(2,0),(2,2)$. The six nonzero cell values of $d\rho/3$ are

\[
 \left\{\frac12,\frac13,\frac16,\frac56,\frac23,\frac12\right\}.
\]

Each cell has dimension $d/9$; the other three cells are zero. The rank is $2d/3$, and both the minimum list size and the minimum number of three-sparse squares are three. The repeated value $1/2$ does not obstruct recovering the weights from the three private cells.

Thus every feasible state below $7d/9$ is scalar on each cell, and all such states commute with one another. The triangle weights can be recovered from their three private cells even when some eigenvalues coincide. This is an operator-level statement; the unordered spectrum alone need not determine which lines carry the state.

## 5. Exact list sizes and rank nonmonotonicity

**Proof of Theorem B.** A nonzero one-sparse matrix is invertible, so every proper-rank state requires at least two labels. For a two-sparse factor below $7d/9$, the proof of Lemma 3 forces an order-three singular binomial. After scaling it is $I-T$, with $T^3=I$. Its two nonzero squared eigenvalues are both $|1-\omega|^2=3$. Thus

\[
 (I-T)(I-T)^*=3(I-P_{T=1}).
 \tag{10}
\]

Every nonzero factor has rank $2d/3$. If a two-list state has rank below $7d/9$, Theorem A forces its rank to equal $2d/3$. Every factor must then have the same range as the state. Equation (10) makes every square proportional to the same range projector. The normalized state is exactly (4). Conversely (10) supplies a two-sparse factor for each of the twelve such states. They are the equal-weight parallel pairs. All remaining states in Theorem A already admit three labels and cannot admit fewer.

Any crossing pair therefore has minimum list size three and rank $5d/9$, proving the first equality in (5). Theorem A excludes rank $4d/9$ for three labels. For four-label attainment, use the commuting order-three Weyls in (1) and set

\[
 C=(I-U)(I-V)=I-U-V+UV.
 \tag{11}
\]

These are four distinct Weyl labels with nonzero coefficients. On $E_{x,y}$, the square vanishes exactly when $x=0$ or $y=0$; it equals nine on the four remaining cells. Hence

\[
 CC^*=9P_{\{x\ne0,\ y\ne0\}},\qquad
 \operatorname{rank}C=4d/9,\qquad \operatorname{Tr}CC^*=4d.
 \tag{12}
\]

The normalized state $CC^*/(4d)$ and Lemma 1 prove the second equality in (5). QED.

This produces an exact-rank nonmonotonicity: $d/3$, $4d/9$, $5d/9$, and $2d/3$ have minimum list sizes three, four, three and two, respectively. The increase at $4d/9$ concerns exact rank; it does not contradict monotonicity when rank is treated as a resource budget.

Positive summation also creates a rank unavailable to a single three-sparse factor. A crossing mixture has corank $4d/9$. Lemma 3 shows directly that an individual factor below $7d/9$ can only have rank $d/3$ or $2d/3$. Thus rank $5d/9$ requires at least two sparse squares, as quantified by $\nu_3$.

**Corollary 5 (dimension nine).** The positive ranks admitting a perfect decoder with at most three labels are exactly

\[
 \{3,5,6,7,8,9\}.
 \tag{13}
\]

Moreover, for exact ranks $r=3,4,5,6,7,8,9$, the minimum list sizes are respectively $3,4,3,2,3,2,1$.

**Proof.** Theorem A excludes ranks one, two and four, and supplies three, five and six. The identity, $I-Z$, and $(Z-I)(Z-e^{2\pi i/9}I)$ supply ranks nine, eight and seven using respectively one, two and three terms. This proves (13).

Only the lower bound of three at rank seven remains. A two-sparse factor in dimension nine has rank six, eight or nine when nonzero. In a rank-seven positive sum only rank-six factors can occur; their squares are flat complements of the twelve rank-three line projectors by (10). If all these excluded lines agree, the sum has rank six. If two differ, their intersection has dimension zero or one, so the common kernel of the sum has dimension at most one and its rank is at least eight. Rank seven is impossible with two labels. The other exact values follow from Theorem B and the proper-rank obstruction to one label. QED.

No exact minimum for ranks one and two is asserted in this corollary.

## 6. Sharpness of the structural cutoff

**Proof of Theorem C.** Put $T=Z^{d/9}$ and $\xi=e^{2\pi i/9}$. The matrix

\[
 C=(T-I)(T-\xi I)=T^2-(1+\xi)T+\xi I
 \tag{14}
\]

has three nonzero Weyl terms. The order-nine operator $T$ has nine distinct eigenvalues, each of multiplicity $d/9$, and (14) kills exactly its eigenvalues $1$ and $\xi$. Thus $C$ has rank $7d/9$.

The coefficient of $T^2$ in $CC^*$ is $\overline\xi\ne0$. There is no aliasing among the powers $T^{-2},\ldots,T^2$, since $T$ has order nine. But the label of $T^2$ is $(0,2d/9)$, outside $(d/3)\mathbb Z_d^2$. Weyl basis uniqueness therefore places $CC^*$ outside the span of the nine Weyls generated by $U,V$, equivalently outside the algebra spanned by $P_{E_{x,y}}$. Normalization does not change this conclusion. QED.

The restriction $k\ge2$ is also essential. In dimension three, $X,Z$ do not commute, and their order-three eigenspaces do not form nine simultaneous character cells. In fact $\rho=(P_{Z=1}+P_{X=1})/2$ is a three-list state of rank two below $7d/9$, whereas the fractions $5d/9$ and $2d/3$ in the higher-power classification do not define the same cell geometry. We therefore exclude $d=3$ rather than applying the table outside its hypotheses.

## 7. Reproducibility and contribution boundary

The supplied `ternary_verify.py` uses only the Python standard library. Run it in a directory containing the manuscript:

```text
python ternary_verify.py
```

It writes `ternary_certificate.json`, with the verifier and manuscript hashes. Its arithmetic uses exact rational pairs in $\mathbb Q(\omega)$ and integers. It checks all 4,095 nonempty subsets of the twelve affine lines, not merely the 150 predicted low-rank families. It verifies the counts, support uniqueness, private-cell recovery and spectral formulas. Separately it constructs the actual cyclic Weyl matrices in dimensions 9, 27 and 81, verifies all twelve line and nine cell projectors, every projector-pair intersection, explicit mixtures and the four-term rank-$4d/9$ construction. It also checks central multiplicity arithmetic for all 6,320 ordered distinct nonzero label pairs in dimension nine. No floating-point singular-value threshold is used.

The infinite-dimensional-family statements rest on the proofs above. The finite enumeration certifies the nine-point geometry and supplies exact representation checks; it does not replace quantification over arbitrary coefficients or arbitrary $k$. This replay was written by the constructing agent and is not labeled an independent audit. Any separate internal review must identify the precise manuscript and certificate hashes it reviewed.

The predecessor [1] established the individual prime-power rank rule and the universal central-sector formula. It also classified a dyadic low-rank stratum. Those results and the sparse-square/POVM reduction are antecedents, not new claims of this manuscript. The contribution here is the complete ternary positive-sum stratum, its unique finite decomposition, exact sparse-square length, fixed-state two/three-label distinction and the four-label family in (5).

Affine-line character projectors and convex mixtures have established finite-phase-space antecedents. Gross [5] and Veitch, Ferrie, Gross and Emerson [6] analyze stabilizer states and their discrete Wigner representations. In particular, the affine-line incidence object underlying the present nine-cell description is classical; it is not presented as a new finite geometry or a new stabilizer representation. Our twelve operators are mutually commuting rank-$d/3$ code projectors in the cyclic dimension-$d$ basis. They must not be identified with twelve noncommuting pure qutrit stabilizer projectors as operators. The new rigidity lemma is what forces arbitrary sparse positive factorizations in this problem into that familiar finite incidence structure.

Focused primary-source searches did not locate the exact ternary classification or the list values in (5). This bounded search does not establish bibliographic priority. The full higher-rank cone, exact list sizes at all ranks, quantitative stability under approximate zeros, and possible extensions to other odd prime powers remain outside this article.

## References

1. L. Eriksson, *Three-term Weyl operators: central multiplicities, rank laws, and exact list decoding*, ARR-2026-0WESHW4YMM9FG8EK, version 1, 5 September 2026. [Published record](https://arr-research.github.io/papers/ARR-2026-0WESHW4YMM9FG8EK/). The source and PDF hashes are recorded in the accompanying reading ledger.
2. N. Johnston, B. Lovitz, V. Russo and J. Sikora, *The complexity of perfect quantum state classification*, arXiv:2510.20789v1, Section 2.1, Lemma 9 and Corollary 11. [Primary text](https://arxiv.org/html/2510.20789v1).
3. V. Gheorghiu, *Standard Form of Qudit Stabilizer Groups*, arXiv:1101.1519, Theorem 1. [Primary PDF](https://arxiv.org/pdf/1101.1519).
4. D. Farenick, O. Ojo and S. Plosker, *Universality of Weyl Unitaries*, arXiv:2101.00129, Lemmas 2.1–2.2. [Primary PDF](https://arxiv.org/pdf/2101.00129).
5. D. Gross, *Hudson's Theorem for finite-dimensional quantum systems*, arXiv:quant-ph/0602001; *J. Math. Phys.* 47, 122107 (2006), Sections II and VII. [Primary PDF](https://arxiv.org/pdf/quant-ph/0602001).
6. V. Veitch, C. Ferrie, D. Gross and J. Emerson, *Negative Quasi-Probability as a Resource for Quantum Computation*, arXiv:1201.1256; *New J. Phys.* 14, 113011 (2012), Section IV. [Primary PDF](https://arxiv.org/pdf/1201.1256).

Lluis Eriksson directed the research programme. OpenAI Codex assisted with conjecture screening, proof development, exact computation, source comparison and drafting. This internal research manuscript is distinct from its author's already published predecessor.
