# Hive coarse-graining and unbounded optimal-rank excess

## Status

The argument below is a theorem-level route, conditional only on the standard
Horn--hive equivalence and the frozen exact `k=3`, rank-17 certificate.  It
does **not** prove the conjectured complete formula
`kappa^(<=5k+j)=30k-j` for every `k,j`, nor does it determine the exact
minimum optimal rank on the amplified subsequence.

## Hive convention

For order `N`, write hive vertices as `h(i,l)` with
`0 <= i <= l <= N`.  The three elementary rhombus slacks are

```text
R1(i,l) = h(i,l+1)+h(i-1,l)-h(i-1,l+1)-h(i,l),
R2(i,l) = h(i,l+1)+h(i,l)-h(i+1,l+1)-h(i-1,l),
R3(i,l) = h(i,l)+h(i-1,l)-h(i,l+1)-h(i-1,l-1),
```

for `1 <= i <= l < N`.  A hive has all three families nonnegative.

## Coarse-grid lemma

Let `N=nt` and define `H(I,L)=h(tI,tL)`.  Then `H` is an order-`n`
hive.  Each coarse slack is a nonnegative sum of fine slacks:

```text
R1_H(I,L)
 = sum_{a=t(I-1)+1}^{tI} sum_{q=0}^{t-1} R1_h(a,tL+q),

R2_H(I,L)
 = sum_{a=t(I-1)+1}^{tI} sum_{q=0}^{t-1} R2_h(a+q,tL+q),

R3_H(I,L)
 = sum_{a=1}^{t} sum_{q=0}^{t-1}
     R3_h(t(I-1)+a,t(L-1)+a+q).
```

The identities follow by telescoping directional edge differences.  They
also prove the claim on boundary cases `I=L`; every fine row appearing above
lies in its valid triangular range.

If a fine boundary list is constant on consecutive blocks of length `t`, the
corresponding coarse boundary increment is `t` times the base entry.  For the
self-commutator boundary

```text
alpha=(p_1,...,p_N),
beta=(-p_N,...,-p_1),
gamma=2 lambda,
```

the coarse positive boundary is

```text
P_s = sum_{q=(s-1)t+1}^{st} p_q.
```

The negative boundary is `(-P_n,...,-P_1)`.  Since `p` is nonincreasing, so
is `P`.  If `rank(p) <= rt`, then `P_(r+1)=...=P_n=0`; hence the coarse point
lies literally on the order-`n`, rank-`r` face.  Moreover

```text
(1/2) sum_s P_s = (1/2) sum_i p_i.
```

Without a rank cap, `P_n` may be positive.  Subtracting `P_n` from both
isospectral positive boundaries leaves `gamma` unchanged and weakly lowers
the cost, so an order-`n` lower bound still transfers to the fine problem.

## Exact base fixtures

Let `F_k` have spectrum

```text
(5 repeated 4k times, -4 repeated 5k times),  d=9k.
```

The order-nine exact certificate gives

```text
kappa_9(F_1)=29,
```

attained at rank six.  The frozen dependency-free hive certificate for
`k=3` proves

```text
kappa_27^(<=17)(F_3)=88,
```

while three direct-sum order-nine primals attain unrestricted cost `87` at
rank `18`.

## Unbounded-excess theorem

For every integer `t>=1`,

```text
kappa_(27t)(F_(3t)) = 87t,
kappa_(27t)^(<=17t)(F_(3t)) >= 88t,
17t+1 <= r_*(F_(3t)) <= 18t.
```

Proof of the unrestricted equality: coarse-grain any order-`27t` hive all the
way to order nine using blocks of length `3t`, apply the homogeneous base
lower bound `29*(3t)=87t`, and use the direct sum of `3t` base primals for the
reverse inequality.

Proof of the rank statement: if a feasible fine point has rank at most
`17t`, coarse-grain it to order 27 in blocks of length `t`.  The resulting
point has rank at most 17 and target boundary `t gamma_3`; homogeneity of the
exact base certificate gives cost at least `88t`.  This is strictly larger
than the unrestricted optimum `87t`, so no norm minimizer has rank at most
`17t`.  The direct-sum construction has rank `18t`.

The inertia lower bound is `15t`.  Consequently

```text
r_*(F_(3t)) - r_0(F_(3t)) >= 2t+1,
```

so the additive excess is unbounded.  The theorem does not claim the exact
value of `r_*` between `17t+1` and `18t`.

## Reproducibility boundary

- `repro/verify_exact_hive_duals.py` checks the exact order-27 rank-17
  primal/dual certificate over `Fraction`.
- `repro/verify_hive_coarse_graining.py` checks the three displayed
  telescoping identities and the boundary/rank block map for arbitrary input
  parameters supplied to the script.
- The universal quantifier in the coarse-grid lemma is proved algebraically
  by the displayed telescoping formulas; finite script runs are regression
  checks, not the source of that universal quantifier.
