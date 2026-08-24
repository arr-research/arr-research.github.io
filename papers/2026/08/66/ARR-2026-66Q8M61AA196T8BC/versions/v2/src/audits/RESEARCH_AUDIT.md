# Adversarial research audit — version 2

Date: 2026-08-24
Canonical SHA-256: `17810cc2c07029b913b50665bf72fa569762670cc836900bc3cbfa1bfea0a414`

## Claims reconstructed

For a smooth projective integral `d`-fold over an algebraically closed field,
a very ample `H`, `1 <= s <= m`, and a nonempty finite reduced set `Z` whose
value span absorbs the order-`s` osculating space at every support, the paper
claims:

1. `dim S_Z, |Z| >= N(d,m) = binom(d+m,d)` in arbitrary characteristic.
2. If `m >= 2s+1`, then both quantities are at least
   `max{N(d,m), binom(d+s,d) r_1(Z)}`.
3. For every allowed `(d,m,s)` and characteristic, the exact floor is attained
   by a reduced set with proper point span on a smooth integral hypersurface.

## Proof audit

### Exact floor

The principal-parts filtration embeds every tangent block in the order-`s`
block. Hence higher-order absorption implies tangent absorption. Applying the
exact arbitrary-characteristic tangent theorem gives `N(d,m)`. No derivative
or factorial convention is introduced in this reduction.

### Rank-sensitive blocks

Select `r_1(Z)` supports whose degree-one evaluation lines form a basis. If
the next line escapes the preceding span, a section `e` of `H` vanishes on the
old supports and is nonzero at the new one. The factor `e^(s+1)` kills the old
fat neighbourhoods and is a unit at the new support. The remaining degree
`m-s-1` generates order-`s` jets precisely when `m-s-1 >= s`. Induction gives
a direct sum of `r_1(Z)` blocks, each of length `binom(d+s,d)`, inside `S_Z`.

For necessity of the threshold, take `P^1`, `H=O(1)`, and `m+1` distinct
points. Their degree-`m` evaluations fill the ambient space, so every order is
absorbed and `r_1=2`. When `m <= 2s`, the proposed unthresholded term
`2(s+1)` exceeds the actual span dimension `m+1`.

### Characteristic-free equality examples

Choose `N(d,m)` evaluation lines forming a basis for degree-`m` forms on a
hyperplane `W=P^d`. Such a choice exists over every algebraically closed field
because a nonzero form cannot vanish at every rational point of `P^d` over an
infinite field.

For `E=(s+1)N` and `n>=E+1`, the degree-`n` system vanishing to order `s+1` at
the supports separates first jets at every point of `W\Z`: multiply sections
of degree `n-E` by a product of `(s+1)`-st powers of hyperplanes, one through
each support and none through the test point. The singular-member incidence
has fibre codimension `d+1` over a base of dimension `d`, so the closure of its
image is proper.

After choosing the tangential equation `f`, write `F=f+yG`. On `y!=0`,
multiplication by `y` is a unit on first neighbourhoods. Singularity at a
fixed ambient point has codimension `d+2` over a base of dimension `d+1`, so
the closure of the second incidence image is proper. Simultaneously avoid the
finitely many hyperplanes `G(p)=0`. This gives smoothness on all three strata:
`y!=0`, `W\Z`, and `Z`.

The hypersurface sequence gives `H^0(O_X)=k` because `d+1>=2` and intermediate
cohomology vanishes; smoothness plus connectedness makes `X` integral. At a
support, the ambient lift of `f` lies in the `(s+1)`-st maximal-ideal power and
`G` is a unit, hence `y=-f/G` has order at least `s+1` on `X`.

Since `n>m`, restriction of ambient degree-`m` forms to `X` is an isomorphism.
A form vanishing on the unisolvent supports restricts to zero on `W`, hence is
`yR` and vanishes to order `s+1` on `X`. The annihilator criterion proves
absorption. Unisolvence gives equality, while the ambient degree-`m` space has
strictly larger dimension, so the span is proper.

## Counterexample and quantifier search

- `s<=m` is essential for full local order-`s` rank.
- Completeness of the `H^m` system is used by all separator products.
- Algebraic closure is used for an infinite field and geometric smoothness;
  no nonclosed-field theorem is asserted.
- Smoothness, integrality, reducedness, positive dimension, and nonempty
  support are all used and explicitly quantified.
- The curve example falsifies the rank-sensitive second term throughout the
  entire omitted range `m<=2s`.
- The construction proves existence only at a sufficient hypersurface degree;
  minimality and equality classification remain open.

No counterexample or defective quantifier was found under the printed
hypotheses.

## Literature boundary

Ballico (2013) already defines and studies the `X`-rank of linear subspaces,
including tangent-containing spaces on rational normal curves and Veronese
examples. Beltrametti--Di Rocco--Sommese (1999) supplies adjacent jet-ampleness
technology. Mallavibarrena--Piene (2024) supplies the principal-parts language,
and the cited osculating/secant papers delimit the context. The comparison is
selective and supports no exhaustive priority claim.

## Verdict

The exact-hash re-review found no open P0 or mathematical P1 issue. The main
residual uncertainty is bibliographic priority rather than an identified
logical gap. Exact finite replays and artifact checks support reproducibility
but do not mechanize the geometric proofs. This is an AI audit, not human peer
review or independent certification.
