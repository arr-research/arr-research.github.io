# Three-term Weyl rank rigidity in prime-power dimension, and its failure under positive summation

Lluis Eriksson — research draft, 5 September 2026. Exact finite replay completed. Internal mathematical review is tracked in a separate report; no external refereeing or priority certification is claimed.

## Results and scope

Write $X|j\rangle=|j+1\bmod d\rangle$, $Z|j\rangle=e^{2\pi i j/d}|j\rangle$, and $W_{a,b}=X^aZ^b$. Weyl sparsity counts nonzero coefficients in this single cyclic basis indexed by $\mathbb Z_d^2$. The family is not a tensor product of prime-dimensional Pauli bases.

The main algebraic result classifies every possible rank of a nonzero matrix with at most three Weyl coefficients when $d=p^k$ is a prime power. For $p=2$, the proper coranks are exactly

\[
                         1,2,4,\ldots,2^{k-1}.                 \tag{A}
\]

For odd $p$, they are exactly

\[
          \{p^j,2p^j:0\le j<k\}.                              \tag{B}
\]

The proof identifies the entire singularity condition for a noncommuting relative support: each central block has dimension equal to the commutator order, at most two such blocks can be singular, and each singular block contributes exactly one kernel dimension. In particular, every genuinely noncommuting Weyl trinomial in prime-power dimension has nullity at most two. The constant two is attained. The dimension hypothesis matters: $2^{1/4}I+X^3+Z^3$ in dimension 12 is noncommuting and has nullity three.

The operational application concerns one use of all $d^2$ channels $\operatorname{Ad}(W_{a,b})$, pure entangled probes, arbitrary final POVMs, and **exact** Schmidt rank. Let $\mathcal F_3(d)$ be the reduced density matrices permitting a perfect output list of size at most three. For every $d=2^k$, $k\ge3$,

\[
 \{\rho\in\mathcal F_3(d):\operatorname{rank}\rho<3d/4\}
       =\{2P_S/d:S\in\mathscr H_d\},                         \tag{C}
\]

where $\mathscr H_d$ consists of exactly thirty half-dimensional subspaces defined below. Thus every rank strictly between $d/2$ and $3d/4$ is forbidden for three labels, and every feasible state below $3d/4$ has a flat half-rank spectrum.

Positive summation changes the answer outside this interval. For every $d=2^k$, $k\ge4$, three sparse squares explicitly attain rank $13d/16$. Consequently

\[
 \ell_{\min}^{\rm exact}(d,13d/16)=3\quad(k\ge4),\qquad
 \ell_{\min}^{\rm exact}(d,5d/8)=4\quad(k\ge3).                \tag{D}
\]

In dimension 16, the complete set of ranks admitting at most three labels is therefore

\[
                         \{8,12,13,14,15,16\}.                \tag{E}
\]

The dimension-eight value $\ell_{\min}^{\rm exact}(8,5)=4$, its thirty half-rank states, and the two-label corank divisibility theorem were established in the preceding research cycles. They are antecedents, not new claims of this draft. The extensions here are the prime-power algebraic classification, the all-dyadic half-rank stratum, the positive-sum counterexample and the new exact three-label family.

## 1. Two elementary ingredients

**Character multiplicity.** Suppose commuting phased Weyl operators generate a label subgroup $H$ of size $h$. Every simultaneous character space has dimension $d/h$; in particular, $h\mid d$.

To prove this, choose one simultaneous eigenvector and divide each operator by its eigenvalue on that vector. This removes the projective multiplication phases and gives an honest representation $r\mapsto T_r$ of $H$, with no nonidentity scalar operators. The character projectors are

\[
       P_\chi=\frac1h\sum_{r\in H}\overline{\chi(r)}T_r.
\]

Every nonidentity Weyl operator has trace zero, so $\operatorname{Tr}P_\chi=d/h$ for every character. All these projectors are nonzero and have the stated rank. This is the standard stabilizer/character averaging argument, reproduced to fix the composite-dimension phase convention.

**Circle intersection.** If $a,b,c\ne0$, the equation

\[
                    c+as+bt=0,\qquad |s|=|t|=1               \tag{1}
\]

has at most two ordered pairs $(s,t)$. Indeed, $s$ must lie on the unit circle and on $|c+as|=|b|$. The second circle has nonzero center $-c/a$, so the two circles are distinct and meet at most twice. Each $s$ determines $t$.

## 2. Prime-power central blocks

**Lemma 1.** Let $d=p^k$. Let $u,v\in\mathbb Z_d^2$ be Weyl labels whose commutator has order $q=p^\ell>1$. Then

\[
                     |\langle qu,qv\rangle|=d/q.             \tag{2}
\]

**Proof.** Let $s$ be the minimum of the four coordinate valuations of $u,v$, with $v_p(0)=k$. At least one of $u/p^s,v/p^s$ is primitive. Swap the labels if needed. An invertible determinant-one coordinate change over $\mathbb Z_d$ puts

\[
                   u=(p^s,0),\qquad v=(c,e),\qquad p^s\mid c,e.
\]

This coordinate change is used only for label arithmetic; no implementation by a Clifford unitary is required. To construct it, complete the primitive vector $u/p^s$ to a determinant-one matrix using a Bezout identity modulo $d$.

The determinant has valuation $k-\ell<k$, so $v_p(e)=k-\ell-s$. In particular $\ell+2s\le k$. The two generators in (2) become

\[
                 (p^{\ell+s},0),\qquad (p^\ell c,p^\ell e).
\]

The first coordinate of the second generator is an integer multiple of the first generator. Subtracting that multiple leaves $(0,p^\ell e)$, whose nonzero coordinate has valuation $k-s$, interpreted as zero modulo $d$ if $s=0$. The two axis orders are $p^{k-\ell-s}$ and $p^s$. Their product is $p^{k-\ell}=d/q$. QED.

**Theorem 2 (exact noncommuting block rule).** In prime-power dimension, let $U,V$ be phased Weyl operators with $UV=\zeta VU$, where $\zeta$ has order $q>1$. Let

\[
                         D=I+aU+bV,\qquad ab\ne0.
\]

The distinct joint eigenvalue pairs $(s,t)$ of $(U^q,V^q)$ number $d/q$. Each joint eigenspace has dimension $q$. On the corresponding block,

\[
                \det D=1-(-1)^q(a^q s+b^q t).                 \tag{3}
\]

Every singular block has nullity one. Hence

\[
 \dim\ker D
   =|\{(s,t):a^q s+b^q t=(-1)^q\}|\le2.                    \tag{4}
\]

**Proof.** The powers $U^q,V^q$ commute with both $U,V$. Their labels generate the subgroup in Lemma 1. Character multiplicity therefore gives exactly $d/q$ joint spaces, each of dimension $q$. Different joint characters give different pairs $(s,t)$, since the two powers generate the central label group after phases have been removed.

Fix one block. If $\lambda$ is an eigenvalue of $U$, applying $V$ successively gives the $q$ different eigenvalues $\lambda,\zeta\lambda,\ldots,\zeta^{q-1}\lambda$. Their eigenspaces exhaust this $q$-dimensional block, so each is one-dimensional. In this eigenbasis $U$ is diagonal and $V$ is a cyclic weighted shift; the product of its $q$ nonzero shift weights is $t$.

The determinant of the diagonal matrix $I+aU$ plus this shift has only the all-diagonal term and the full-cycle term. Since $\lambda^q=s$, it equals

\[
 \prod_{j=0}^{q-1}(1+a\lambda\zeta^j)+(-1)^{q-1}b^q t
   =1-(-a\lambda)^q+(-1)^{q-1}b^q t,
\]

which is (3). The equations $Dx=0$ determine successive components from any one by dividing only by $b$ and the nonzero shift weights. Thus a block kernel has dimension at most one, even if one of the diagonal entries vanishes. The determinant criterion then gives nullity exactly one on a singular block. Finally, apply the circle bound (1) with coefficients $a^q,b^q$ and nonzero constant $-(-1)^q$. QED.

The determinant identity is the elementary cyclic-block form of the familiar root-of-unity quantum-binomial phenomenon. The proof above includes the signs for both odd and even commutator order rather than importing an odd-order convention.

**Sharpness.** In dimension 8 set $U=X$, $V=X^2Z^4$, choose nonzero square roots $a^2=1-i$, $b^2=i$, and take $D=I+aU+bV$. These operators anticommute, $U^2=X^2$, and $V^2=X^4$. Writing $s\in\{1,i,-1,-i\}$ for an eigenvalue of $X^2$, the block condition is

\[
                   (1-i)s+i s^2=1.
\]

Its roots are exactly $1,i$. Thus $D$ has nullity two, proving that the uniform constant in (4) cannot be improved. For prime dimension $d=p$, there is only one block for every noncommuting pair, and the sharper bound is one.

## 3. Complete individual rank classification

**Theorem 3.** Let $d=p^k$, $k\ge1$. The ranks of nonzero matrices of Weyl sparsity at most three are $d$, together with $d-n$ for $n\in\mathcal N_p$, where

\[
 \mathcal N_2=\{2^j:0\le j<k\},\qquad
 \mathcal N_p=\{p^j,2p^j:0\le j<k\}\quad(p\text{ odd}).        \tag{5}
\]

**Proof.** Right-multiply by the adjoint of one support Weyl and scale a nonzero coefficient to one. This preserves rank and range, and preserves $CC^*$ up to a positive scalar. A one-term matrix is invertible. A two-term matrix is $I+aU$. If the relative label of $U$ has order $m$, its eigenvalues are a phase times the $m$-th roots of unity, each of multiplicity $d/m$. Thus its nonzero corank, when singular, is $d/m$, a power of $p$.

A genuine trinomial is $I+aU+bV$, with distinct nonidentity labels and $ab\ne0$. If the relative Weyls do not commute, Theorem 2 gives corank one or two when singular. For $d=2$, its one block gives corank at most one. All these possibilities are included in (5).

If the relative Weyls commute, let their label group have order $h$. The group order is a power of $p$ dividing $d$, and distinct joint characters have distinct pairs of eigenvalues of $U,V$. The circle bound gives either one or two zero characters. Their common multiplicity is $d/h$. Hence the corank is $d/h$ or $2d/h$. When $p=2$, the presence of three distinct support labels forces $h\ge4$; both possibilities are powers of two strictly below $d$. When $p$ is odd, they have the form in (5).

For attainment of every $p^j$, use $I-Z^{p^j}$. For odd $p$, put $m=d/p^j$, $T=Z^{p^j}$, and $\xi=e^{2\pi i/m}$. The polynomial

\[
                      (T-I)(T-\xi I)
\]

has exactly three nonzero Weyl coefficients, since $m\ge3$ is odd and $1+\xi\ne0$. Its kernel is the sum of two eigenspaces of $T$, giving corank $2p^j$. The identity attains full rank. QED.

This is a rank classification, not a complete classification of the kernels or coefficients at each rank. In the dyadic case it says that allowing one individual third Weyl coefficient does not create any new rank beyond those already attained by binomials. That conclusion must not be transferred to a positive sum of several sparse squares; Section 7 gives a counterexample.

## 4. The dimension hypothesis cannot be removed

**Proposition 4.** In cyclic dimension 12,

\[
                    C=2^{1/4}I+X^3+Z^3                       \tag{6}
\]

has Weyl sparsity three, noncommuting relative support, rank nine and nullity three.

**Proof.** Put $U=X^3,V=Z^3$. Then $UV=iVU$ and $U^4=V^4=I$. Each eigenvalue of $U$ has multiplicity three. Choose a basis of its eigenvalue-one space and apply $V,V^2,V^3$; this decomposes the twelve-dimensional representation into three identical four-dimensional cyclic blocks. On each block, the determinant of $cI+U+V$ is $c^4-2$. For $c=2^{1/4}$ it vanishes, and the invertible-shift recurrence gives a one-dimensional kernel in each block. Hence the total nullity is three. QED.

Here $q=4$ but $\langle qu,qv\rangle$ is trivial, whereas $d/q=3$. This is the precise failure of the prime-power arithmetic step. The replay also computes rank nine directly over the exact number field $\mathbb Q(i,2^{1/4})$.

## 5. Thirty half-rank squares in every dyadic dimension

For $d=2^k$, $k\ge3$, define $\mathscr H_d$ as follows:

* Take either eigenspace of each of the three nonidentity order-two Weyls with labels in $\{0,d/2\}^2$.
* For every order-four Weyl with label in $(d/4)\mathbb Z_d^2$, take the sum of its eigenvalue-$i^j$ and eigenvalue-$i^{j+1}$ spaces, with $j$ modulo four.

Every subspace has dimension $d/2$. The indicated Weyl representatives have fourth power $I$. The family contains six subspaces of the first type and twenty-four of the second, after deduplicating inverse order-four generators.

**Lemma 5 (low-rank square rigidity).** If $C\ne0$, $s_W(C)\le3$, and $\operatorname{rank}C<3d/4$, then

\[
                      CC^*=cP_S,
           \qquad c>0,\quad S\in\mathscr H_d.                \tag{7}
\]

Conversely, every such projector is proportional to a sparse square with at most three terms.

**Proof.** A singular binomial of rank below $3d/4$ must have relative label order two; larger orders give rank at least $3d/4$. Such a binomial is proportional, up to a right unitary, to $I\pm J$ for a phased involution $J$. Its square is proportional to the corresponding half-rank projector.

For a genuine trinomial, a noncommuting relative support has rank at least $d-2\ge3d/4$, by Theorem 2. For commuting support, a group of order at least eight also gives rank at least $3d/4$, by the two-zero-character bound. Thus the group has order four and exactly two characters are zeros.

If this group is $C_2\times C_2$, absorb phases and write the four values as $1+a\epsilon+b\delta$, with $\epsilon,\delta\in\{\pm1\}$. Two zeros differing in just one sign force $a=0$ or $b=0$; two differing in both signs force the identity coefficient to vanish upon addition. Both are impossible. The group is therefore cyclic of order four.

Let $T$ be its generator, with $T^4=I$. A right multiplication by a power of $T$ makes the three supported powers $I,T,T^2$. The two roots of the resulting quadratic among $\{1,i,-1,-i\}$ cannot be opposite, since their sum would vanish and remove the middle coefficient. They are adjacent. The two remaining roots also form an adjacent pair. After a root rotation and a scalar factor it suffices to consider $p(t)=(t-1)(t-i)$. Its two nonzero values satisfy

\[
                   |p(-1)|^2=|p(-i)|^2=8.
\]

This proves (7). Conversely, $(I\pm J)(I\pm J)^*=4P_S$ for the involution spaces. For an adjacent order-four pair, take the quadratic whose roots are the complementary pair; its square is $8P_S$. QED.

**Lemma 6 (incidence and count).** The family $\mathscr H_d$ has exactly thirty distinct members. Distinct members intersect in dimension zero or $d/4$. In dimension 8, among the 435 unordered distinct pairs, 207 have zero intersection and 228 have intersection dimension two. For every $d\ge16$, precisely 15 pairs have zero intersection and 420 have intersection dimension $d/4$.

**Proof.** An involution projector has Weyl support $\{0,j\}$. An adjacent order-four projector has support $\{0,u,-u\}$, with both nonidentity coefficients nonzero. There are twelve order-four labels, six inverse pairs, and four distinct adjacent projectors per cyclic subgroup. This proves the count and separation from the six involution projectors.

For two different involution labels, the joint group has order four, so fixing both eigenvalues gives intersection dimension $d/4$. For equal labels, the spaces are equal or complementary.

For an involution $J$ and an order-four $U$, if the label of $J$ equals that of $U^2$, an adjacent pair selects one $U$ eigenvalue in each square sector. Its intersection with either $J$ sector has dimension $d/4$. Otherwise $\langle J,U\rangle$ has order eight and two allowed joint characters, again giving $d/4$.

For two order-four generators $U,V$ in dimension $d\ge16$, all labels under consideration commute: their determinants are multiples of $d^2/16$, hence of $d$. Their label group has order four, eight or sixteen. In the order-four case, distinct adjacent pairs share either zero or one of the four eigenspaces, each of dimension $d/4$. In the order-eight case, their nonzero squared labels coincide. Rephase $V$ to make $V^2=U^2$; this only permutes its adjacent-pair family. The eight joint characters satisfy $\lambda^2=\mu^2$. Each adjacent pair selects one eigenvalue for each square, giving two allowed joint characters and intersection dimension $2d/8=d/4$. In the order-sixteen case, all sixteen pairs of fourth roots occur, and the two adjacent selections permit four pairs, giving $4d/16=d/4$. Thus disjointness occurs only for complementary members. Every member has one complement, yielding fifteen unordered disjoint pairs.

In dimension 8, two such order-four Weyls either commute or anticommute. In the commuting case their squared labels coincide, and the order-four/eight argument above applies. In the anticommuting case their squared labels are independent involution labels. The four central character spaces have dimension two. An adjacent-pair projector selects one $U$ eigenline in each such space, and the other projector selects one $V$ eigenline. Anticommuting invertible operators have no common eigenvector, so these lines differ and the intersection is zero. The six cyclic order-four subgroups form three classes of two according to their squared label. Generators from different classes anticommute. This adds $\binom32\cdot2^2\cdot4^2=192$ disjoint projector pairs to the fifteen complementary pairs, giving 207. The remaining 228 pairs intersect in dimension two. QED.

## 6. Operational reduction and the complete low-rank stratum

For completeness, the needed covariance reduction is recalled with its normalization. Represent a pure probe by a full-column-rank matrix $A\in\mathbb C^{d\times r}$, with $\rho=AA^*$ and $\operatorname{Tr}\rho=1$. Vectorization is $|A\rangle\!\rangle=\sum_{ij}A_{ij}|i\rangle|j\rangle$. A perfect $\ell$-list decoder exists exactly when

\[
                      \rho=\sum_j C_jC_j^*,
                       \qquad s_W(C_j)\le\ell.              \tag{8}
\]

To see necessity, merge effects reporting the same finite list and spectrally refine into vectors $|B_j\rangle\!\rangle$. Their outcome amplitudes are $\operatorname{Tr}(AB_j^*W_g)$, so each $AB_j^*$ has the reported Weyl support, up to label inversion and phases. POVM normalization gives $\sum_j B_j^*B_j=dI_r$. Setting $C_j=AB_j^*/\sqrt d$ proves (8).

Conversely, positivity implies $\operatorname{ran}C_j\subseteq\operatorname{ran}A$. Set $B_j^*=A^+C_j$. Then $\sum_jB_j^*B_j=I_r$ and $AB_j^*=C_j$. Weyl twirling shows that

\[
 M_{j,g}=\frac1d|W_gB_j\rangle\!\rangle
                    \langle\!\langle W_gB_j|                \tag{9}
\]

sum to $I_{dr}$. For outcome $(j,g)$, report the translate by $g$ of $\{h:\operatorname{Tr}(C_jW_h)\ne0\}$. The trace orthogonality of Weyls makes its cardinality $s_W(C_j)$, and it contains every label with nonzero outcome probability. Thus (8) is a physical achievability criterion, not merely a support count.

**Theorem 7.** Equation (C) holds. Six of the thirty states have minimum fixed-probe list size two; the other twenty-four have minimum fixed-probe list size three.

**Proof.** Let $\rho$ satisfy (8) with $\ell=3$ and $r=\operatorname{rank}\rho<3d/4$. Every summand has range contained in $\operatorname{ran}\rho$, so Lemma 5 applies to every nonzero term. Any two of their half-dimensional ranges, if contained in this same $r$-space, have intersection dimension at least $d-r>d/4$. Lemma 6 therefore forces them to coincide. Equation (7) and trace normalization give $\rho=2P_S/d$. Conversely every such state has the sparse-square realization from Lemma 5, and hence a decoder by (9).

For list size two and rank $d/2$, every nonzero sparse summand must itself have rank $d/2$, and its relative label must be an involution. The same range argument forces the state to be one of the first six. All proper-rank probes require at least two labels, because a nonzero one-sparse matrix is invertible. QED.

The cutoff is strict and optimal for this conclusion: rank $3d/4$ already admits two labels, for instance from a binomial whose relative Weyl has order four.

## 7. Positive summation creates a new rank

**Theorem 8.** For $d=2^k$, $k\ge4$,

\[
                       \ell_{\min}^{\rm exact}(d,13d/16)=3.
\]

**Construction.** Set $m=d/4$, $U=X^m$, $V=Z^m$, and

\[
 p(t)=(t-1)(t-i),\qquad C_1=p(U),\quad C_2=p(V),\quad C_3=p(UV).
\]

These are three-term Weyl matrices. Since $16\mid d$, $U,V$ commute and generate a label group isomorphic to $C_4\times C_4$. Its sixteen joint character spaces $E_{x,y}$, where $U=i^x,V=i^y$, have dimension $d/16$.

Put

\[
                   R=\sum_{j=1}^3 C_jC_j^*,\qquad
                   \rho=R/(12d).                            \tag{10}
\]

The three kernel conditions are

\[
             x\in\{0,1\},\quad y\in\{0,1\},\quad
                         x+y\bmod4\in\{0,1\}.
\]

Their simultaneous solutions are exactly

\[
                            (0,0),(0,1),(1,0).                \tag{11}
\]

Since a positive sum has the intersection of the constituent kernels, $\dim\ker R=3d/16$, giving rank $13d/16$. Each $C_jC_j^*$ is eight times a half-rank projector, so $\operatorname{Tr}R=3\cdot8(d/2)=12d$. Thus (10) is normalized and (8) provides a perfect three-label decoder for any purification of $\rho$.

More explicitly, if $n(x,y)$ counts the failed conditions in (11), then $R|_{E_{x,y}}=8n(x,y)I$. Among the sixteen cells, the multiplicities for $n=0,1,2,3$ are $3,3,9,1$, respectively. Hence the nonzero spectrum of $\rho$ is

\[
  \frac{2}{3d}\;(3d/16\text{ times}),\quad
  \frac{4}{3d}\;(9d/16\text{ times}),\quad
  \frac{2}{d}\;(d/16\text{ times}).                           \tag{12}
\]

For the lower bound, recall the preceding-cycle two-label theorem: a proper exact rank $r$ permits two labels if and only if $d-r\mid d$. Its necessary direction follows directly from (8): every singular binomial square is a positive multiple of $(I-T)(I-T)^*$, where the phased Weyl $T$ fixes the common kernel pointwise. All such $T$'s commute because a nonzero common fixed vector forbids a nontrivial scalar commutator. The common kernel is the fixed space of their finite label group $H$. Character averaging gives its dimension $d/|H|$, proving the divisibility. Here $d-r=3d/16$ does not divide $d$, so two labels are impossible. QED.

This construction is the decisive counterexample to extending (A) to positive sums. Each individual $C_j$ has rank $d/2$, yet their positive sum has corank $3d/16$, which is not a power of two. It also separates an exact-rank optimization from the rank-budget optimization, which may use a single sparse factor.

**Corollary 8.1.** In dimension 16, a probe of exact rank $r$ has some perfect decoder with at most three labels if and only if

\[
                         r\in\{8,12,13,14,15,16\}.
\]

**Proof.** Theorem 7 excludes all ranks below twelve except eight. Theorem 8 supplies thirteen. The ranks eight, twelve, fourteen and fifteen are attained by the binomials with respective coranks eight, four, two and one. The full-rank maximally entangled probe allows one label. These exhaust the sixteen possible positive ranks. QED.

## 8. An infinite exact four-label family

**Theorem 9.** For $d=2^k$, $k\ge3$,

\[
                          \ell_{\min}^{\rm exact}(d,5d/8)=4.
\]

**Proof.** The lower bound is Theorem 7, since $d/2<5d/8<3d/4$. For the upper bound, set $T=Z^{d/8}$, $\omega=e^{2\pi i/8}$, and

\[
                       C=(T-I)(T-\omega I)(T-\omega^2I).
\]

The four coefficients are nonzero. Indeed the two middle elementary symmetric sums are $1+\omega+\omega^2=(1+1/\sqrt2)(1+i)$ and $\omega+\omega^2+\omega^3=i(1+\sqrt2)$. Exactly three of the eight eigenspaces of $T$, each of dimension $d/8$, are killed. Thus $\operatorname{rank}C=5d/8$. Normalize $\rho=CC^*/\operatorname{Tr}(CC^*)$ and use (8). Its exact normalization is $\operatorname{Tr}(CC^*)=4d(2+\sqrt2)$. QED.

The case $d=8$ reproduces the preceding cycle. The new statement supplies every $d\ge16$ in this dyadic family and follows from the general low-rank obstruction rather than a dimension-specific enumeration.

## 9. Exact replay, rejected generalizations and limits

Run from the workspace root:

```text
python work/cycle3/quantum/quantum_dyadic_verify.py
```

The bounded replay takes about seven seconds after interpreter startup on this workspace. It produces `quantum_dyadic_certificate.json` beside the script and records the source SHA-256. It uses integer arithmetic, Gaussian rationals, cyclotomic integer rings, and one explicit algebraic number field. No floating-point rank threshold is used.

The certificate checks:

* all 1,948,590 noncommuting ordered label pairs in dimensions $2,3,4,5,7,8,9,16,25,27,32$, verifying (2) by exact lattice-index arithmetic; for dimensions at most eight it separately enumerates the central label group;
* the formal cyclic determinant product for commutator orders $2,3,4,5,7,8,9,16,25,27,32,64$ in integer cyclotomic arithmetic;
* all 54 labelled sparse-square factorizations, all 30 distinct projectors, and all 435 distinct projector pairs in dimensions eight and sixteen;
* the rank $13d/16$ construction by direct exact matrices for $d=16,32$, including all sixteen character projectors, their ranks, the complete spectrum and trace normalization;
* the four-term rank $5d/8$ construction for $d=8,16,32,64$, including the exact nonzero coefficients and zero positions;
* the dimension-twelve noncommuting counterexample by a direct exact matrix-rank calculation.

The finite checks do not quantify over arbitrary coefficients or prove statements for untested dimensions. Those quantifiers are supplied by Sections 1–8. The determinant formula avoids division by possibly zero diagonal entries; this is essential in the singular cases.

Two tempting generalizations were rejected by explicit examples during this cycle. The first, a dimension-free noncommuting nullity bound of two, fails at dimension twelve. The second, a power-of-two corank law for all positive sums of three-sparse squares in dyadic dimension, fails at dimension sixteen. Neither rejected claim is used elsewhere.

No classification of all higher-rank three-list states for arbitrary dyadic dimension is asserted. In particular, (C) controls ranks strictly below $3d/4$; it does not describe the remaining convex set. No quantitative approximate-decoding error gap, mixed-probe theorem, multiuse theorem, or general composite-dimension classification is asserted. Exact-rank feasibility alone does not imply a uniform approximate error gap, as established in the first cycle.

## 10. Antecedents and contribution map

| Result or tool | Antecedent inspected | Contribution in this draft |
|---|---|---|
| Perfect list decoding and sparse positive factorizations | Johnston, Lovitz, Russo and Sikora, *The complexity of perfect quantum state classification*, Lemma 9 and Corollary 11, [primary full text](https://arxiv.org/html/2510.20789v1) | Equation (8) repeats the preceding cycle's Weyl-covariant normalization. No new general factor-width equivalence is claimed. |
| Equal character multiplicity and stabilizer dimension | Gheorghiu, *Standard Form of Qudit Stabilizer Groups*, Theorem 1, [primary PDF](https://arxiv.org/pdf/1101.1519) | The trace proof is standard. Lemma 1 evaluates the particular two-generator central subgroup in prime-power cyclic dimension. |
| Root-of-unity cyclic representations | Kim, *Finite dimensional quantum Teichmüller space from the quantum torus at root of unity*, Section 2.1, Propositions 2.5–2.6, [primary PDF](https://arxiv.org/pdf/1703.05513) | Cyclic blocks and central characters are prior machinery. The paper uses odd root order. Our even/odd block signs and multiplicity calculation are proved directly; no even-order theorem is inferred from its odd-order convention. |
| Quantum-binomial center phenomenon | Fock and Goncharov, *Cluster ensembles, quantization and the dilogarithm*, Section 3.1.1, [primary PDF](https://smf.emath.fr/download/pdf/43892) | Background for the familiar root-of-unity mechanism. The short determinant proof supplies precisely the identity needed here. No claim is made to invent quantum-binomial identities or quantum-torus representations. |
| Exact two-label rank classification | Eriksson research cycle 1, `outputs/research/quantum_lists.md` | The corank divisibility criterion is an imported result, with its necessary direction recalled in Section 7. |
| Dimension-eight rank-five obstruction and thirty states | Eriksson research cycle 2, `outputs/cycle2/quantum/quantum_rank5_theorem.md`, with its separate review | The $d=8$ endpoint is prior within this programme. The all-prime-power individual rank law, all-dyadic stratum and $13d/16$ three-list family go beyond it. |

Primary-source searches in this cycle targeted Weyl trinomial rank/nullity, finite Weyl rank uncertainty, finite Gabor three-vector dependence, and root-of-unity quantum-torus representations. The searches located the background machinery above but did not locate the specific prime-power rank list (5), all-dyadic thirty-state stratum, or exact $13d/16$ list value. That is a limited search result, not an exhaustive priority determination. Real-line HRT/Gabor results concern different spaces and quantifiers and were not imported. The companion `quantum_sources.md` records the reading scope and limitations.

Lluis Eriksson directed the research programme. OpenAI Codex assisted with conjecture screening, proof development, exact computation, source comparison and drafting. The constructing agent's derivations and exact checks are distinguished from the separate internal review.
