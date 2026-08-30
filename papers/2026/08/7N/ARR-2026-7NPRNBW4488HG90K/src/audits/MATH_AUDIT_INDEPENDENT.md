# Independent mathematical audit

Date: 2026-08-24  
Scope: the theorem package proposed in
`work/paper27-one-spike-four-kick/VIABILITY_MEMO.md`, cross-checked against the
current Paper 28 source.  This audit does not assess priority and does not
authorize publication.

## Verdict

**PASS AFTER MANDATORY PROOF AND WORDING CORRECTIONS.**

The corrected headline results are true:

\[
 \kappa_d(F)=\sum_{j=1}^n j b_j,
 \qquad
 \mathcal A_3(F)=12\sqrt3\,\kappa_d(F),
 \qquad
 \mathcal A_4(F)=16\,\kappa_d(F).
\]

The one-spike singular spectrum, rank rigidity, sign reflection, arbitrary
zero padding, repeated eigenvalues, and the two stability constants also
survive the audit.  However, the original proof of the four-kick lower bound
in the viability memo contains a false inequality.  The theorem survives only
after replacing that step by the Gram-determinant argument below.  The current
`paper.tex` already uses the corrected Gram argument.

Three further corrections are required for a complete manuscript proof:

1. State singular-spectrum rigidity only for minimizers of the one-matrix
   problem, equivalently for product-optimal Hermitian pairs **after norm
   balancing**.  It is false for unbalanced product optimizers.
2. In the proof that the least squared singular value vanishes, construct the
   new factor by polar decomposition; merely subtracting a scalar from
   `CC*` and `C*C` does not by itself produce a feasible matrix.
3. Either prove the equality classification behind “every optimal square” or
   weaken it to “the displayed optimizer is a square.”  The classification is
   true and a short proof is supplied below.
4. In the all-target one-matrix lemma, do not cite “the finite weighted shift
   below,” because the displayed later shift is only the one-spike
   constructor.  Cite finite-dimensional self-commutator existence or insert
   the general cumulative-sum shift described in Section 1 below.

The sharpness claim in the stability theorem must be restricted to `n>=2`.
For `n=1` the distance and deficit are identically zero, so the inequalities
hold but the numerical constants are not meaningfully sharp.  The current
source already makes this restriction.

## 1. One-matrix reduction and attainment

For `C=H+iK`, with `H,K` Hermitian,

\[
 CC^*-C^*C=-2i[H,K].
\]

Reciprocal scaling of a feasible pair makes its two Hilbert--Schmidt norms
equal without changing either the commutator or their product.  Conversely,
the Hermitian real and imaginary parts `X,Y` of a feasible `C` obey

\[
 \|X\|_{\rm HS}\|Y\|_{\rm HS}
 \le \frac{\|X\|_{\rm HS}^2+\|Y\|_{\rm HS}^2}{2}
 =\frac12\|C\|_{\rm HS}^2.
\]

Hence

\[
 \kappa_d(F)=\frac12\min_{CC^*-C^*C=2F}\|C\|_{\rm HS}^2.
\]

For a self-contained all-target feasibility proof, diagonally order the
eigenvalues of `F` with all positive values first, then the zeros, then the
negative values.  Every partial sum `s_j` is nonnegative and the final one is
zero.  The weighted shift with squared weights `2s_j` then satisfies
`(CC*-C*C)/2=F`.  Thus the feasible set is nonempty for every traceless
Hermitian target, not only on the one-spike cone.  Its intersection with a
closed norm sublevel set is compact, so the minimum is attained.
Decomposing a minimizing `C` also gives an attained product optimum.

Every product-optimal pair is Hilbert--Schmidt orthogonal: if
`<H,K> != 0`, the shear

\[
 K\longmapsto K-\frac{\langle H,K\rangle}{\|H\|^2}H
\]

preserves the commutator and strictly lowers the second norm.  Reciprocal
scaling then gives

\[
 \langle H,K\rangle=0,
 \qquad \|H\|=\|K\|=\sqrt{\kappa_d(F)}.
\]

This proves the normalization used in both polygon constructors.

## 2. Exact one-spike cost and singular rigidity

Let the nonzero spectrum be

\[
 (P,-b_1,\ldots,-b_n),\qquad
 b_1\ge\cdots\ge b_n>0,\qquad \sum_jb_j=P,
\]

with `z>=0` additional zero eigenvalues.  Let
`p_1>=...>=p_d>=0` be the squared singular values of a minimizing `C`, where
`d=n+1+z`.

### Removing the singular floor

The manuscript needs the following explicit realization.  If `p_d=t>0`,
write the polar decomposition `C=U S^(1/2)`, where `S=C*C`; invertibility
makes `U` unitary.  Then

\[
 C'=U(S-tI)^{1/2}
\]

satisfies

\[
 C'C'^*=CC^*-tI,\qquad C'^*C'=C^*C-tI.
\]

It has the same self-commutator and strictly smaller squared norm.  Therefore
`p_d=0` at every minimizer.

### Horn tails

For `1<=ell<=n`, use the Horn triple

\[
 I_\ell=\{1,\ldots,\ell\},\qquad
 J_\ell=K_\ell=\{1,d-\ell+2,\ldots,d\}.
\]

The partition attached to `I_ell` is zero and the relevant
Littlewood--Richardson coefficient is therefore one.  With the ordered
spectra of `CC*`, `-C*C`, and `2F`, the inequality is exactly

\[
 p_\ell\ge 2\left(P-\sum_{j<\ell}b_j\right)
 =2\sum_{j=\ell}^n b_j.                         \tag{2.1}
\]

Zero padding lies between the positive eigenvalue and the negative block and
does not alter the selected entries.  Repeated `b_j` also cause no problem.
Summing (2.1) gives

\[
 \frac12\|C\|_{\rm HS}^2\ge
 \sum_{\ell=1}^n\sum_{j=\ell}^n b_j
 =\sum_{j=1}^n j b_j.
\]

The shift

\[
 Ce_{\ell+1}=\sqrt{2\sum_{j=\ell}^n b_j}\,e_\ell
\]

attains equality.  At any minimum, equality of the total sum, together with
the nonnegativity of all unused `p_r`, forces equality in every (2.1) and
forces all remaining squared singular values to vanish.  Thus every
one-matrix minimizer has nonzero squared singular spectrum

\[
 \left(2\sum_{j=\ell}^n b_j\right)_{\ell=1}^n
\]

and rank exactly `n`.

### Mandatory scope of “every optimum”

The preceding rigidity does **not** apply to `C=H+iK` formed from an
unbalanced product-optimal pair.  Already for
`F=diag(P,-P)`, let

\[
 C_0=\begin{pmatrix}0&\sqrt{2P}\\0&0\end{pmatrix},
 \qquad C_0=H+iK.
\]

For every `t>0`, `(tH,t^{-1}K)` is still product-optimal, but for `t!=1`
the squared singular values of

\[
 C_t=tH+i t^{-1}K
\]

are

\[
 \frac P2(t+t^{-1})^2,qquad
 \frac P2(t-t^{-1})^2.
\]

Both are nonzero.  The correct statement is therefore: every minimizer `C`
of the one-matrix problem, or every product optimum after norm balancing, has
the rigid spectrum.  The current theorem statement uses this corrected
scope.

### Reflection and boundary cases

Replacing `F` by `-F` replaces a minimizing `C` by `C*`, preserving all
singular values and the rank.  Hence the one-negative-eigenvalue case follows
without a new Horn argument.  For `n=1`, the formulas reduce to
`kappa=P`, squared singular spectrum `(2P)`, and rank one.  Arbitrary zero
padding and repeated negative eigenvalues were checked both analytically and
by exact matrix constructors.

## 3. Deficit identity and sharp stability

With `u=P/n`, direct substitution gives

\[
 D=\frac{n+1}{2}P-\sum_{j=1}^n j b_j
 =\frac12\sum_{i<j}(b_i-b_j).                    \tag{3.1}
\]

Put `y_j=b_j-u`, so `sum y_j=0`, and `L=sum |y_j|`.  The triangle inequality

\[
 |y_i|=\left|\frac1n\sum_j(y_i-y_j)\right|
 \le\frac1n\sum_j|y_i-y_j|
\]

summed over `i` yields

\[
 \sum_{i<j}|y_i-y_j|\ge\frac n2L.
\]

Since the `y_j` are decreasing, (3.1) is one half of this pairwise sum, so

\[
 D\ge\frac n4L.
\]

The opposite triangle inequality
`|y_i-y_j|<=|y_i|+|y_j|`, summed over pairs, gives

\[
 D\le\frac{n-1}{2}L.
\]

Both constants are attained for every `n>=2`: the lower one by any two-level
deviation profile, and the upper one by
`(a,0,...,0,-a)` around a sufficiently large positive baseline `u`.  Thus the
constants and the unique uniform fixed-mass maximizer are correct.  For
`n=1`, `D=L=0`; the assertion is true but sharpness is vacuous.

## 4. The original four-kick proof fails

Let

\[
 D_1=x_1+x_2,\qquad D_2=x_2+x_3.
\]

Balance does give

\[
 H_{\rm geo}=-\frac i2[D_1,D_2]
\]

and

\[
 S_2\ge\|D_1+D_2\|+\|D_1-D_2\|.
\]

But the next inequality in the viability memo,

\[
 (\|D_1+D_2\|+\|D_1-D_2\|)^2
 \ge4(\|D_1\|^2+\|D_2\|^2),
\]

is false.  The elementary error is that
`(a+b)^2 <= 2(a^2+b^2)`, not `>=`.

There are nonzero-target counterexamples.  Take Pauli matrices
`A=sigma_z`, `B=sigma_x`, put

\[
 D_1=A,\qquad D_2=A+\varepsilon B,qquad \varepsilon=1/10,
\]

and use

\[
 x_1=(D_1-D_2)/2,\quad x_2=(D_1+D_2)/2,
 \quad x_3=-x_1,\quad x_4=-x_2.
\]

Then `H_geo=epsilon sigma_y` is nonzero, while

\[
 S_2^2=2\bigl(\varepsilon+\sqrt{4+\varepsilon^2}\bigr)^2
 <16+8\varepsilon^2
 =4(\|D_1\|^2+\|D_2\|^2).
\]

Therefore the proof in the viability memo is **FAIL**, even though its final
constant is correct.

## 5. Correct proof of the universal four-kick theorem

Set

\[
 r=\|D_1\|,\qquad s=\|D_2\|,qquad
 c=\langle D_1,D_2\rangle,qquad
 q=\sqrt{r^2s^2-c^2}.
\]

For a nonzero target, `r>0`.  Replace `D_2` by its orthogonal component

\[
 D_2^\perp=D_2-\frac c{r^2}D_1.
\]

The commutator is unchanged, and the Hermitian pair
`D_1/sqrt(2),D_2^perp/sqrt(2)` is feasible.  Consequently

\[
 \kappa_d(F)\le\frac12r\|D_2^\perp\|=\frac q2.   \tag{5.1}
\]

Let `T=r^2+s^2`.  The diagonal lower bound gives

\[
 \begin{aligned}
 S_2^2
 &\ge 2T+2\sqrt{T^2-4c^2}\\
 &=2T+2\sqrt{(r^2-s^2)^2+4q^2}.
 \end{aligned}
\]

Now `T>=2rs>=2q`, and the square root is at least `2q`.  Hence

\[
 S_2^2\ge8q\ge16\kappa_d(F).                    \tag{5.2}
\]

For attainment, choose an orthogonal equal-norm optimal pair `H,K` and put

\[
 D_1=\sqrt2H,\qquad D_2=\sqrt2K,
\]

\[
 x_1=(D_1-D_2)/2,\quad x_2=(D_1+D_2)/2,
 \quad x_3=-x_1,\quad x_4=-x_2.
\]

The loop has the correct sign,
`H_geo=-i[D_1,D_2]/2=-i[H,K]=F`.  Each edge has norm
`sqrt(kappa_d(F))`; therefore `S_2^2=16 kappa_d(F)`.  For `F=0`, the all-zero
loop proves the formula separately.  This establishes the theorem including
all spectral degeneracies and zero padding.

### Equality classification

For `F!=0`, equality in (5.2) forces `r=s` and `c=0`.  Equality in the two
triangle inequalities, together with balance and the linear independence of
the two diagonal directions, forces `x_3=-x_1` and `x_4=-x_2`.  The diagonal
conditions then force `||x_1||=||x_2||` and `<x_1,x_2>=0`.  Thus every
four-kick optimizer is a Hilbert-space square.  Its two normalized diagonals
form an orthogonal equal-norm optimal Hermitian pair.  On the one-spike cone,
the associated `C=H+iK` therefore has rank `n` by Section 2.  This short
equality argument should be inserted if the manuscript retains the phrase
“every optimal square.”

## 6. Three-kick law and switching ratio

For a balanced triple, the convention in the candidate source gives

\[
 H_{\rm geo}=-\frac i2[x_1,x_2].
\]

Removing the component of `x_2` parallel to `x_1` shows that
`kappa_d(F)` is at most the Euclidean area `Delta` of the matrix triangle.
The sharp Hilbert-space triangle inequality

\[
 S_2^2\ge12\sqrt3\,\Delta
\]

gives the lower bound.  If `H,K` are orthogonal equal-norm optimal factors,
set `alpha=2/3^(1/4)` and

\[
 x_1=\alpha H,\qquad
 x_2=\alpha(-H/2+\sqrt3K/2),\qquad
 x_3=\alpha(-H/2-\sqrt3K/2).
\]

This orientation is important under the displayed convention.  It gives
`H_geo=F`, three equal edge norms, and

\[
 S_2^2=12\sqrt3\,\kappa_d(F).
\]

Combining the corrected three- and four-kick theorems gives

\[
 \frac{\mathcal A_4(F)}{\mathcal A_3(F)}
 =\frac{4}{3\sqrt3}<1
\]

for every nonzero finite-dimensional target.  On the one-spike cone, inserting
the exact spectral cost yields the claimed switch laws.

## 7. Computational adversarial checks

The audit ran the two existing replays and additional independent tests:

- exact one-spike cost, Horn tails, singular data, stability extremizers, and
  the multispike nonextension example through `n=20`: PASS;
- exact symbolic four-kick flux identities and square constructors through
  `n=6`: PASS;
- 9,000 random rational stability tests for `1<=n<=30`, plus every displayed
  equality family through `n=30`: PASS;
- repeated spectra, sign reflection, three ambient zero eigenvalues, and the
  `n=1` boundary: PASS;
- 40,000 random Hermitian-loop tests of the corrected Gram inequality: PASS;
- 4,040,000 scalar `(r,s,cos(theta))` tests of the reduced sharp inequality:
  PASS;
- explicit unbalanced qubit optimizers: they disprove unqualified
  product-optimum singular rigidity, as described above;
- `diag(5,1,-3,-3)` constructor: exact self-commutator and cost `8`: PASS.

These computations are diagnostic support.  The arbitrary-dimensional proof
is the analytic argument in Sections 1--6.

## Final disposition

**Mathematical package: PASS once the mandatory proof details above are in
the canonical source.**  The headline constant `16`, its attainment, the
universal switching ratio, and the complete one-spike formula are not refuted.
The obsolete parallelogram chain from the viability memo must never reappear.
No claim for five or more kicks, no unrestricted all-sign spectral formula,
and no publication action is authorized by this audit.
