# Mathematical audit: the exact dimension-eight threshold

Date: 2026-08-24 (Europe/Stockholm)  
Verdict: **PASS, computer-assisted exact theorem**

## Main viable claim

Let

```text
kappa_d(F) = (1/2) min ||C||_HS^2
             subject to CC* - C*C = 2F,
```

and put

```text
r_0(F)=max(n_+(F),n_-(F)).
```

Then every traceless Hermitian target in dimension `d<=7` has a
norm-minimizing factor `C` of rank exactly `r_0(F)`.

The elementary inertia obstruction gives `rank(C)>=r_0(F)` for every feasible
factor. The exact replay proves that restricting the Horn program to
`rank(C)<=r_0(F)` does not change its optimum. Hence the minimum rank on the
norm-optimal face is exactly `r_0(F)`.

Combined with the strict dimension-eight family from Paper 30, this proves:

> Dimension eight is the smallest ambient dimension in which every
> norm-optimal inverse self-commutator factor can be forced to have rank
> strictly larger than the inertia lower bound.

This is the strongest viable Paper 31 claim found in the mathematical sweep.

## Why deleting or padding zeros is not a proof

The inverse cost is not invariant under changing the ambient dimension.
Adding a zero eigenvalue creates additional Horn coupling directions and can
strictly lower the optimum.

An exact example is

```text
lambda_7=(25,18,18,-10,-17,-17,-17)/7.
```

In dimension seven,

```text
kappa_7(lambda_7)=74/7,
```

with feasible squared singular spectrum

```text
p_7=(54,36,36,20,2,0)/7.
```

A matching exact lower certificate uses weight `1/2` on each of

```text
H_1((3);(1);(3)),
H_3((2,3,5);(1,2,5);(2,3,7)),
H_5((1,2,3,5,6);(1,2,3,5,6);(1,2,3,6,7)),
H_6((1,2,3,4,5,6);(1,2,3,5,6,7);(1,2,3,5,6,7)),
```

and weight `1` on `p_6>=0`.

Pad the same target by one zero and reorder:

```text
lambda_8=(25,18,18,0,-10,-17,-17,-17)/7.
```

Now

```text
kappa_8(lambda_8)=73/7,
```

attained by

```text
p_8=(52,36,36,20,2,0,0)/7.
```

The exact lower certificate has weights

```text
1, 1/4, 1/4, 1/4, 1/2, 1/4, 5/4
```

on, respectively,

```text
H_1((3);(1);(3)),
H_2((2,5);(1,6);(3,8)),
H_3((1,2,6);(1,2,6);(1,3,8)),
H_5((1,2,3,5,6);(1,2,3,6,7);(1,2,3,7,8)),
H_7((1,2,3,4,5,6,7);(1,2,3,4,6,7,8);(1,2,3,4,6,7,8)),
order:6,
p_7>=0.
```

Thus one zero of ambient padding lowers the cost by exactly `1/7`. In fact,
the rank-four face retains value `74/7`, while the new unrestricted optimum
has rank five.  The rank-four lower certificate uses weights
`1,1/2,1/2,1/2` on

```text
H_1((3);(1);(3)),
H_2((2,5);(1,6);(3,8)),
H_5((1,2,3,5,6);(1,2,3,6,7);(1,2,3,7,8)),
H_7((1,2,3,4,5,6,7);(1,2,3,4,6,7,8);(1,2,3,4,6,7,8)).
```

Its combined coefficient vector is
`(1/2,1/2,1/2,1/2,1,0,-1/2)`, so it is the half-sum objective on the
rank-four face, and its right side is `74/7`. Therefore neither deleting zero
eigenvalues nor taking chamber closures proves the singular cases in lower
dimensions.

## Complete inertia-stratum coverage

The canonical verifier is

```text
python work/paper31-frontier/math/verify_d_le_7_epigraph.py
```

It treats every inertia triple `(n_+,n_-,n_0)` with `n_+,n_->=1`, up to the
reflection exchanging the positive and negative counts. Every prescribed
zero eigenvalue is imposed by the exact pair

```text
lambda_i>=0,  -lambda_i>=0.
```

The rank face is always the literal value `max(n_+,n_-)`; zeros are never
assigned artificially to either sign.

The replay covers **33 strata**:

| Dimension | Strata up to reflection |
| ---: | ---: |
| 3 | 2 |
| 4 | 4 |
| 5 | 6 |
| 6 | 9 |
| 7 | 12 |

Dimensions one and two are elementary. For `d=1`, trace zero forces `F=0`.
For `d=2`, a nonzero target has inertia `(1,1,0)` and the standard one-step
factor has rank one.

The recursive Horn counts used in each ambient dimension are:

| `d` | Counts by `r=1,...,d-1` | Horn total | Horn plus order/nonnegativity |
| ---: | --- | ---: | ---: |
| 3 | `(6,6)` | 12 | 14 |
| 4 | `(10,21,10)` | 41 | 44 |
| 5 | `(15,56,56,15)` | 142 | 146 |
| 6 | `(21,126,228,126,21)` | 522 | 527 |
| 7 | `(28,252,751,751,252,28)` | 2,062 | 2,068 |

Exact duplicate coefficient/right-side rows are collapsed before the
polyhedral conversion. This does not remove a distinct inequality.

## Exact proof architecture

For each stratum the verifier performs the following finite proof.

1. Parameterize the ordered trace-zero target spectrum by its nonnegative
   adjacent gaps `g`.
2. Regenerate every recursive Horn inequality for
   `alpha=(p_1,...,p_(d-1),0)`,
   `beta=(0,-p_(d-1),...,-p_1)`, and `gamma=2lambda(g)`.
3. Add the exact inertia-stratum equations, including every zero eigenvalue.
4. Form the epigraph cone with `z>=(1/2)sum p_j` on the face
   `p_(r_0+1)=...=p_(d-1)=0`.
5. Use floating cdd only to propose redundant rows. Convert the retained cone
   with GMP-rational cdd and verify every discarded row on every exact
   generator. A bad floating proposal therefore makes the replay fail.
6. Project the exact face generators to `(g,z)` and regenerate the exact
   facet description.
7. For every projected facet, use HiGHS only to propose a sparse support and
   reconstruct a nonnegative rational Farkas combination of unrestricted
   Horn-cone rows with SymPy.
8. Check the complete coefficient identity and nonnegativity over exact
   `Fraction` arithmetic.

The face epigraph is automatically contained in the unrestricted epigraph,
because every face-feasible `p` is unrestricted-feasible. The exact Farkas
certificates prove every face-epigraph facet on the unrestricted cone, giving
the reverse containment. The projected epigraphs are therefore equal on the
whole continuous stratum, not merely on sampled spectra.

The largest checked case is the nonsingular `(3,4,0)` stratum in dimension
seven. Its face projection has 26 exact facets, all with exact unrestricted
Farkas certificates.

## Independent-route audit

`verify_low_dimension_minimality_exact.py` supplies an independent
WSL/lcdd-GMP route for the six nontrivial **nonsingular** chambers. Its Horn
normalization, epigraph projection, Farkas containment, and sign reflection
are correct.

Its standalone summary does not cover singular strata at the true inertia
rank: a chamber boundary uses `max(m,d-m)`, which may count zero eigenvalues.
For example, inertia `(1,1,5)` in `d=7` has true lower bound one, whereas every
ordinary chamber cut has rank at least four. The 33-stratum verifier above is
the exact repair and complete route.

## Dimension-eight normalization check

For the Paper 30 midpoint target

```text
lambda=(5/2,1/2,1/2,1/2,-1,-1,-1,-1),
```

the certified values are

```text
kappa_8=13/2,
kappa_8^(<=4)=7,
gap=1/2,
minimum optimal rank=5.
```

For the integer-scaled spectrum requested in the audit,

```text
lambda=(5,1,1,1,-2,-2,-2,-2),
```

homogeneity doubles both costs:

```text
kappa_8=13,
kappa_8^(<=4)=14,
gap=1,
minimum optimal rank=5.
```

Associating `13/2` and `7` with the integer spectrum would be a factor-two
normalization error under `CC*-C*C=2F`.

## Frozen artifacts

```text
verify_d_le_7_epigraph.py
SHA-256 e5009d579933af66283de296ac8aa46b8f0b35bae1e43dd300768ef625129bd6

results/d_le_7_epigraph_certificate.json
SHA-256 0103a643644977400052a68738102a7633d6371db8717383ddefa687da8a18a0
```

## Limitations

- This is a computer-assisted exact polyhedral proof, not a hand
  classification of all low-dimensional optimizer matrices.
- It depends on the classical Horn eigenvalue-sum theorem.
- It does not prove an upper bound on rank excess in dimensions above seven.
- The proposed amplified bivalued family suggesting unbounded excess remains
  numerical on its lower-bound side and is not used in this theorem.
- Novelty and literature priority require a separate primary-source audit.

Subject to that priority audit and one further independent execution of the
33-stratum replay, the mathematical theorem is ready for manuscript drafting.
