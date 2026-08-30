# Final mathematical audit: rank-gap frontier certificates

Date: 2026-08-24 (Europe/Stockholm)  
Status: **PASS within the stated finite Horn scope**

## Scope

The canonical replay

```text
python work/paper30-frontier/verify_rank_gap_frontier.py
```

certifies two exact statements:

1. the complete dimension-eight one-parameter rank-gap phase used by the
   Paper 30 manuscript; and
2. a dimension-nine, genuinely two-valued witness showing that three spectral
   levels are not necessary for super-inertial norm-optimal rank.

All arithmetic is performed with `fractions.Fraction`. The script regenerates
the recursive Horn sets, checks every primal inequality, and checks every
sparse dual coefficient and right-hand-side identity. It has no numerical LP
dependency.

This audit does **not** prove any of the following:

- attainment at inertia rank for every target in dimensions `d<=7`;
- that dimension eight is the minimal dimension of failure;
- that optimal rank exceeds inertia by at most one in all dimensions;
- a classification of all failing Horn chambers;
- novelty, priority, peer review, or proof-assistant certification.

Those questions remain open and must not be inferred from the finite
certificates below.

## Normalization

For a traceless Hermitian target `F`, the replay uses

```text
kappa_d(F) = (1/2) min sum_j p_j,
```

where `p_1>=...>=p_(d-1)>=p_d=0` is the squared-singular-value spectrum of a
factor `C` satisfying

```text
CC* - C*C = 2F.
```

Thus the Horn target is `gamma=2 lambda(F)`. A rank-at-most-`r` face is imposed
by setting `p_(r+1)=...=p_(d-1)=0`.

## Certificate A: complete dimension-eight phase

For

```text
lambda_t = (4-3t,t,t,t,-1,-1,-1,-1),   0<=t<=1,
```

the exact unrestricted value is

```text
                 { 10-7t,  0<=t<=1/2,
kappa_8(F_t) =   {
                 {  9-5t,  1/2<=t<=1,
```

whereas the rank-at-most-four value is

```text
kappa_8^(<=4)(F_t) = 10-6t.
```

Consequently

```text
kappa_8^(<=4)(F_t)-kappa_8(F_t) = min(t,1-t).
```

### Exact primals

The final conventional zero `p_8=0` is suppressed:

```text
p_low(t)  = (8-6t,6-6t,4-4t,2,2t,0,0),   0<=t<=1/2;
p_high(t) = (8-6t,4-2t,2,2,2-2t,0,0),    1/2<=t<=1;
p_face(t) = (8-6t,6-4t,4-2t,2,0,0,0),    0<=t<=1.
```

Every Horn residual is affine in `t`. Exact nonnegativity at both endpoints
therefore proves feasibility throughout each closed interval, not merely on a
grid. Their half-sums are respectively `10-7t`, `9-5t`, and `10-6t`.

### Complete Horn count

The recursive counts for `r=1,...,7` are

```text
(36,462,2120,3516,2120,462,36).
```

They total **8,752 Horn rows**. Adding six order rows and one nonnegativity row
gives **8,759 constraints** checked for every affine primal branch.

### Sparse duals

Write `H_r(I;J;K)` for the regenerated Horn row indexed by the displayed
one-based subsets.

For `0<=t<=1/2`, the following nonnegative combination has coefficient vector
exactly `(1/2,...,1/2)` and right side `10-7t`:

| Weight | Row |
| ---: | --- |
| `1/2` | `H_1((1);(1);(1))` |
| `1/4` | `H_2((1,2);(1,8);(1,8))` |
| `1/4` | `H_4((1,2,3,6);(1,2,7,8);(1,4,7,8))` |
| `1/4` | `H_4((1,2,5,6);(1,2,5,8);(1,4,7,8))` |
| `1/4` | `H_5((1,2,3,5,6);(1,2,3,7,8);(1,3,4,7,8))` |
| `3/4` | `H_7((1,2,3,4,5,6,7);(1,2,3,4,6,7,8);(1,2,3,4,6,7,8))` |
| `5/4` | `p_7>=0` |

For `1/2<=t<=1`, the following combination has coefficient vector exactly
`(1/2,...,1/2)` and right side `9-5t`:

| Weight | Row |
| ---: | --- |
| `1/2` | `H_1((1);(1);(1))` |
| `1/2` | `H_4((1,2,5,6);(1,2,5,8);(1,4,7,8))` |
| `1/2` | `H_7((1,2,3,4,5,6,7);(1,2,3,4,5,7,8);(1,2,3,4,5,7,8))` |
| `1` | `H_7((1,2,3,4,5,6,7);(1,2,3,4,6,7,8);(1,2,3,4,6,7,8))` |
| `1` | `p_7>=0` |

On the rank-four face, each of these rows has weight `1/2`:

```text
H_1((1);(1);(1))
H_3((1,2,5);(1,2,8);(1,4,8))
H_5((1,2,3,5,6);(1,2,3,7,8);(1,3,4,7,8))
H_7((1,2,3,4,5,6,7);(1,2,3,4,6,7,8);(1,2,3,4,6,7,8))
```

Their combined full coefficient vector is

```text
(1/2,1/2,1/2,1/2,1,0,-1),
```

which restricts to the half-sum objective when `p_5=p_6=p_7=0`; the right
side is `10-6t`.

### Rank conclusion

For `0<t<1`, the target inertia is `(4,4,0)`. The strict positive gap excludes
every rank-at-most-four factor from the unrestricted optimal face, while the
displayed unrestricted primal has rank five. Hence the minimum optimal rank is
exactly five. At `t=0` and `t=1`, the gap vanishes and the displayed optimum
has rank four.

## Certificate B: genuinely two-valued dimension-nine witness

Take

```text
lambda = (5,5,5,5,-4,-4,-4,-4,-4).
```

It is traceless, genuinely two-valued, and has inertia `(4,5,0)`. Exact
primal/dual equality gives

```text
kappa_9(F) = 29,
kappa_9^(<=5)(F) = 30.
```

The gap is exactly `1`.

### Exact primals

Suppressing `p_9=0`, feasible primal spectra are

```text
p_full = (16,12,10,10,8,2,0,0),
p_face = (16,14,12,10,8,0,0,0).
```

They have ranks six and five and half-sums `29` and `30`, respectively.

### Complete Horn count

For `r=1,...,8`, the recursive Horn counts are

```text
(45,792,5317,13704,13704,5317,792,45).
```

They total **39,716 Horn rows**. Seven order rows and one nonnegativity row
give **39,724 constraints** checked for each primal.

### Unrestricted dual

The following nonnegative combination equals the full half-sum objective and
has right side `29`:

| Weight | Row |
| ---: | --- |
| `1/2` | `H_1((3);(1);(3))` |
| `1` | `H_1((4);(1);(4))` |
| `1/2` | `H_4((2,3,6,7);(1,2,6,7);(3,4,8,9))` |
| `1/2` | `H_7((1,2,3,4,6,7,8);(1,2,3,4,6,7,8);(1,2,3,4,7,8,9))` |
| `1/2` | `H_8((1,2,3,4,5,6,7,8);(1,2,3,4,6,7,8,9);(1,2,3,4,6,7,8,9))` |
| `1` | `p_8>=0` |

The combined coefficient vector is exactly
`(1/2,1/2,1/2,1/2,1/2,1/2,1/2,1/2)`.

### Rank-five-face dual

The following nonnegative combination has right side `30`:

| Weight | Row |
| ---: | --- |
| `1/2` | `H_1((4);(1);(4))` |
| `1/2` | `H_4((3,4,6,7);(1,2,5,6);(3,4,8,9))` |
| `1/2` | `H_6((2,3,4,6,7,8);(1,2,3,5,6,7);(2,3,4,7,8,9))` |
| `1/2` | `H_7((1,2,3,4,6,7,8);(1,2,3,4,6,7,8);(1,2,3,4,7,8,9))` |
| `3/2` | `H_8((1,2,3,4,5,6,7,8);(1,2,3,4,6,7,8,9);(1,2,3,4,6,7,8,9))` |

The combined coefficient vector is

```text
(1/2,1/2,1/2,1/2,1/2,1,1/2,-1/2).
```

On `p_6=p_7=p_8=0`, this is precisely the rank-five half-sum objective.

### Rank conclusion

The strict rank-five-face gap excludes every rank-at-most-five factor from the
global optimal face. The unrestricted primal has rank six. Therefore the
minimum norm-optimal rank is exactly six, one above the inertia lower bound.
This is an exact counterexample with only two distinct eigenvalues.

## Replay verdict

**PASS.** Both packages have exact feasible primals and exact matching dual
lower bounds. The replay confirms all Horn counts, every displayed dual row
and weight, all objective values, both gaps, and both minimum-rank conclusions.

The dimension-eight phase remains the principal continuous theorem. The
dimension-nine witness is a useful second result because it removes a possible
artifact of the three-level dimension-eight spectrum. It does not close the
open `d<=7`, dimensional-minimality, or universal-excess questions.
