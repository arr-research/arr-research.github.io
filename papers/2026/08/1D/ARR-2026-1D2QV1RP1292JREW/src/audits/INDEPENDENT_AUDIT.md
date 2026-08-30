# Independent audit of the dimension-sharp self-commutator tax

## Verdict

**PASS after mandatory statement/proof corrections.** I found no counterexample
to the corrected theorem. The attainment argument, leakage lower bound,
block-order average, strict equality-face argument, one-spike upper equality,
and zero-padded Horn certificate all close in finite dimension.

The defects described below belonged to the audited draft. The release
manuscript incorporates every mandatory correction: the lower equality uses
half-rank pairs, the residual is indexed by the Horn subset size, attainment
and floor removal are proved, zero padding remains explicit, and the final
subset-to-partition convention is written out in Section 6.

## 1. Literal counterexample to the displayed lower equality classification

The memo first sets `r=rank(F)` and then writes the centrally symmetric equality
spectrum as

```text
{a_1,...,a_r,0,...,0,-a_r,...,-a_1}.
```

Read literally, this has `2r` nonzero eigenvalues. For

```text
F=diag(1,-1),  r=2,
```

one has `kappa_2(F)=P(F)=1`, but the displayed classification would require four
nonzero eigenvalues. The corrected statement is:

```text
kappa_d(F)=P(F)
iff spec(F)={a_1,...,a_s,0,...,0,-a_s,...,-a_1}, a_i>0,
```

where `s=r/2`. In particular, lower equality forces even rank. Equivalently,
state only that the spectrum is centrally symmetric, including multiplicity.

The rank-restricted supremum should also be stated for `2<=r<=d`; there is no
nonzero traceless Hermitian matrix of rank one.

## 2. Attainment gate: PASS, but the proof must be inserted

The feasible set is nonempty: order the positive eigenvalues first and the
negative eigenvalues next, and use the weighted shift from the memo. Let
`C_n` be a minimizing sequence for

```text
(1/2)||C||_HS^2,  [C,C*]=2F.
```

Its norms are bounded. In finite dimension a subsequence converges to `C`, and
the polynomial constraint is closed, so `C` is an optimizer. This justifies
both occurrences of “equality forces” and the later phrase “at an optimum.”

The reduction from the Hermitian product cost also attains: decomposing
`C=H+iK` and rescaling `H -> tH`, `K -> t^{-1}K` balances their norms while
preserving the commutator.

## 3. Leakage identity and lower equality: PASS

Let `A=CC*`, `B=C*C`, and let `Q` be the positive spectral projection of
`A-B=2F`. Since `Tr Q(A-B)=2P(F)`, every feasible `C` satisfies

```text
(1/2)Tr A-P(F)
= (1/2){Tr((I-Q)A)+Tr(QB)}
= (1/2){||(I-Q)C||_HS^2+||CQ||_HS^2}.
```

Both terms are nonnegative. At an optimizer, equality with `P(F)` forces
`supp(A)<=Q` and `supp(B)<=I-Q`. Thus `AB=0`. Since `A` and `B` have identical
nonzero spectra, `A-B` has paired positive and negative eigenvalues. The
converse rank-one-pair construction in the memo is correct.

## 4. Average of weighted shifts: PASS with a sign clarification

For an order `mu_1,...,mu_r`, the shift cost is

```text
sum_{k=1}^{r-1} S_k = sum_{j=1}^r (r-j)mu_j.
```

If positive and negative entries are permuted independently inside their two
blocks, their average contributions are

```text
[r-(m+1)/2]P  - [(n-1)/2]P = (r/2)P.
```

The minus sign before the negative-magnitude contribution should be explicit.
Zeros placed last add no cost. Hence at least one valid shift has cost at most
`rP/2`.

## 5. Necessity in the upper equality classification: PASS

If `kappa=rP/2`, every positive-block/negative-block ordering must equal the
average, because each is feasible and hence has cost at least `kappa`. Adjacent
swaps inside each block then force all positive eigenvalues to be equal and all
negative magnitudes to be equal.

If `m,n>=2`, swapping the last positive and first negative preserves all
partial sums. The only new minimum is

```text
P(1-1/m-1/n)>=0,
```

and the cost drops by `P(1/m+1/n)>0`. This contradicts upper equality. Thus one
sign multiplicity is one, and internal flatness gives the one-spike spectrum,
up to sign and zero padding.

## 6. Removing the least singular value: PASS after one justification

At an optimizer let the common eigenvalues of `A,B` be
`p_1>=...>=p_d`. If `p_d=t>0`, then `A'=A-tI` and `B'=B-tI` are positive,
isospectral, and have the same difference. They are unitarily equivalent, so
if `A'=UB'U*`, then `C'=U sqrt(B')` satisfies

```text
C'C'^*=A',  C'^*C'=B',  [C',C'^*]=2F,
```

with strictly smaller cost. Therefore every optimizer has `p_d=0`.

## 7. Horn zero-padding gate: PASS; correct the index typo

For the normalized positive one-spike target, the decreasing spectrum of
`2F` is

```text
mu=(2P, 0 repeated d-r times,
        -2P/(r-1) repeated r-1 times).
```

For each `s=1,...,r-1`, take the size-`s` triple

```text
I={1,...,s},
J=K={1,d-s+2,...,d}.
```

It is a valid Horn--LR triple in every dimension: the partition attached to
`I` is zero and therefore `c_{0,lambda(J)}^{lambda(J)}=1`.

With `alpha=(p_1,...,p_d)` and
`beta=(-p_d,...,-p_1)`, its Horn residual is exactly

```text
sum_I alpha + sum_J beta - sum_K mu
= p_s - 2P(r-s)/(r-1) >= 0.
```

Thus the memo's phrase “telescopes to `p_r`” must be “telescopes to `p_s`.”
Zero padding causes no problem: `K` uses the first positive eigenvalue and the
last `s-1` entries, which are negative entries even when zeros are inserted in
the middle. Summing the inequalities gives

```text
sum_{s=1}^{r-1}p_s >=
2P/(r-1) sum_{s=1}^{r-1}(r-s)=rP.
```

Hence `(1/2)sum_i p_i>=rP/2`. The positive-first weighted shift has equality,
so the zero-padded one-spike spectrum really attains the upper constant.

The specified triples were also found in the recursively generated Horn lists
for every `d=2,...,7`; their general validity follows from the zero-partition
argument above, not from that finite check.

## Final corrected theorem

For every nonzero traceless Hermitian `F` of rank `2<=r<=d`,

```text
P(F)<=kappa_d(F)<=(r/2)P(F).
```

The lower equality holds exactly for centrally symmetric spectra and forces
even rank. The upper equality holds exactly, up to scaling, sign, and zero
padding, for the nonzero spectrum `(r-1,-1,...,-1)`. Both extrema are attained,
and the leakage identity is an exact minimum identity.
