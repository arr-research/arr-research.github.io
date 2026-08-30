# Independent audit of `verify_low_dimension_minimality_exact.py`

Date: 2026-08-24  
Verdict: **PASS for nonsingular chambers; FAIL as a standalone proof of the
stated all-spectrum scope; repaired by the separate 33-stratum replay**

## What passes

The core projected-epigraph argument is sound.

For a fixed nonsingular sign split `m+(d-m)`, the script constructs:

- the unrestricted Horn epigraph cone;
- the Horn epigraph cone on the face `rank<=max(m,d-m)`;
- the exact projection of the face cone to `(lambda,z)` using GMP cddlib;
- an exact nonnegative Farkas certificate showing every projected face facet
  is valid on the unrestricted cone.

The face feasible set is contained in the unrestricted feasible set, hence
its epigraph projection is contained in the unrestricted projection. The
Farkas certificates prove the reverse containment. Equality of epigraphs then
gives equality of the two optimal values. Since the rank-face Horn LP is a
closed finite-dimensional polyhedral problem and is feasible, this equality
does yield an optimizer at the specified face rank.

The following implementation details are also correct:

- elimination of `lambda_d` using trace zero;
- the final ordered-eigenvalue inequality;
- the coefficient of `-2 sum_(k in K) lambda_k` in every Horn row;
- the suppressed conventional zero in the singular-value spectrum;
- projection indices for `(lambda,z)`;
- preservation of inequality orientation in `primitive_inequality`;
- exact reconstruction and checking of the sparse Farkas weights;
- reflection `F -> -F`, because `C -> C*` preserves singular values and rank.

The floating HiGHS call is used only for support discovery. Every accepted
identity is rechecked over `Fraction`, so the lower certificates do not depend
on floating tolerances.

## P0 scope gap: singular spectra

`chamber_rows(d,m,...)` imposes only

```text
lambda_m >= 0 >= lambda_(m+1)
```

and sets the face rank to

```text
max(m,d-m).
```

This is the inertia rank in the interior of a nonsingular chamber. It need not
be the inertia rank on a boundary containing zero eigenvalues, because the
zeros are counted on one side of the cut.

For example, in dimension seven a target with inertia `(1,1,5)` has inertia
lower bound one. Every chamber cut has

```text
max(m,7-m) >= 4,
```

so none of the six nonsingular chamber closures proves attainment at rank one.
The statement

```text
inertia side 1 has rank d-1, equal to the full p length
```

is valid only when the opposite side has `d-1` nonzero eigenvalues. It does not
cover a one-positive/one-negative target with zero padding.

Allowing boundary points in a chamber therefore does not by itself establish
the claimed scope “all trace-zero Hermitian spectra in dimensions d<=7”. A
general zero-padding invariance theorem would repair this, but no such theorem
is invoked or proved by the script.

## Exact repair and cross-check

The separate verifier

```text
work/paper31-frontier/math/verify_d_le_7_epigraph.py
```

enumerates every inertia triple `(n_+,n_-,n_0)` in dimensions `3<=d<=7`, up
to sign reflection. Each zero eigenvalue is imposed as both rational
inequalities `lambda_i>=0` and `-lambda_i>=0`, and the rank face is set to the
literal value `max(n_+,n_-)`.

It covers **33 exact strata**:

```text
d=3: 2 strata
d=4: 4 strata
d=5: 6 strata
d=6: 9 strata
d=7: 12 strata.
```

For every stratum it:

1. constructs the exact face epigraph;
2. uses floating redundancy removal only as a proposal;
3. verifies every discarded row on every exact GMP generator;
4. computes the exact projected facets;
5. proves every facet valid on the unrestricted cone by a rational
   nonnegative Farkas identity.

That replay passes all 33 strata. Dimensions one and two are elementary, and
reflection covers the omitted order of the positive and negative counts.

Frozen hashes at this audit:

```text
verify_d_le_7_epigraph.py
e5009d579933af66283de296ac8aa46b8f0b35bae1e43dd300768ef625129bd6

results/d_le_7_epigraph_certificate.json
0103a643644977400052a68738102a7633d6371db8717383ddefa687da8a18a0
```

## Final conclusion

The original verifier is a valid independent exact route for its six
nontrivial nonsingular chambers, but its summary overstates that route's
standalone scope. Together with the explicit singular-stratum replay, the
mathematical conclusion is fully supported:

> Every traceless Hermitian target in dimension at most seven has a
> norm-optimal inverse self-commutator factor whose rank equals the inertia
> lower bound.

Combined with the exact strict-gap family in dimension eight from Paper 30,
this proves that dimension eight is the minimal dimension in which
norm-optimal rank can be forced strictly above inertia.
