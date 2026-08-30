# Final re-audit of the integrated Paper 31 manuscript

Audited source: `work/paper31-frontier/paper.tex`  
Source SHA-256: `43f1dfbd30520e23e8fa6668f7de23d1339531244977bf190fa494754e7691e3`  
Date: 2026-08-24  
Verdict: **UNCONDITIONAL PASS — final mathematical release gate**

## Result

The manuscript's mathematics is correct:

- the Horn normalization and inertia obstruction are consistent;
- all 33 sign-zero strata through dimension seven are covered at the literal
  inertia rank;
- the certificate census `272` projected H rows and `813` face generators is
  correct;
- the dimension-eight phase, integer witness, and dimension-nine witness have
  the stated costs, gaps, and ranks;
- the zero-padding fixture is correct;
- the scope and priority language no longer overclaim.

All P1 items in the preceding audits have been repaired.  In particular, the
independent both-orientation equality checker is now integrated into the
canonical reproduction tree, cited in the manuscript, and protected by a
frozen source hash.

## P0 — mathematical errors

**None.**

## Final former P1 — projected equalities — resolved

The canonical script `verify_d_le_7_epigraph.py` computes the exact projected
H-representation with pycddlib. In singular strata, some H rows belong to
`facets.lin_set`, so they are equalities and both orientations are required.

The current canonical serializer converts the H rows to an ordinary tuple and
stores their coefficients, but does not store `facets.lin_set`. It then calls
`exact_farkas` only for the recorded orientation. Across the 33 strata there
are exactly **46 projected equality rows**. Consequently, the canonical JSON
alone proves only one orientation of those 46 equalities; it does not by itself
prove that unrestricted projected points satisfy the opposite orientation.

The independent checker

```text
math/audit_d_le_7_equalities.py
```

preserves `lin_set` and has passed exact verification of both orientations:

```text
PASS: 33 sign/zero strata audited through d=7
PASS: exact face generators=813, projected H rows=272
PASS: preserved lin_set and verified both exact Farkas orientations
      for 46 projected equalities
PASS: Horn orientation, epigraph sign, inertia face and saved census agree
```

Its integrated SHA-256 is

```text
0362a3dae16a027b87b3e39c360dfa657f42fd686401c2340d46013bd7bfb95e.
```

Section 6 now accurately distinguishes the canonical script's serialized
orientation from the integrated equality audit, states the latter's role,
reports all 46 equality rows, and freezes the same hash reproduced above.  The
declared proof boundary therefore matches the scripts actually needed for the
finite exact proof.

## Previously reported P1 items — resolved

### Local dimension-eight/dimension-nine replay — PASS

`math/verify_rank_gap_frontier.py` is now present locally and passes the exact
dimension-eight affine phase plus the dimension-nine witness.

```text
SHA-256 00bdbbfd8adbf3aff8f847ae3574241fc7bed887573c8fa6142bb242cf874be7
```

It verifies:

```text
d=8: 8,752 Horn rows; 8,759 total constraints;
kappa=10-7t / 9-5t; rank-4 value=10-6t;
gap=min(t,1-t); r*=5 on 0<t<1.

d=9: 39,716 Horn rows; 39,724 total constraints;
kappa=29; rank-5 value=30; r*=6.
```

### Zero-padding fixture — PASS

`math/verify_zero_padding_fixture.py` is present, cited, hashed, and passes:

```text
d=7 unrestricted = 74/7;
d=8 padded unrestricted = 73/7;
d=8 padded rank<=4 = 74/7.
```

SHA-256:

```text
6c8a804a3b7b8d77acac9d7e000dd48857858b7c616c11565b06efc38075fa2d
```

### Self-prior provenance — PASS

Lines 98–111 now identify the three unpublished predecessor packages, state
that the present manuscript absorbs and supersedes the two strict-gap drafts,
and require an explicit citation update if a predecessor acquires a public
identifier before deposit. This matches the priority audit.

## Earlier P2 items — resolved

- Proposition 3.2 is now scoped to `3<=d<=7`.
- The relative `14/13` statement is explicitly qualified as sharp within the
  displayed cone.
- The phase, integer-witness, and padding-script hashes are frozen.
- The conclusion refers to the displayed projective segment rather than a
  globally extremal cone.

It would still be helpful, but is not blocking, to say explicitly that the
dimension-nine proposition is auxiliary and is not used in the threshold
proof.

## Equation and theorem audit

### Horn reduction — PASS

The convention

```text
alpha=(p_1,...,p_(d-1),0),
beta=(0,-p_(d-1),...,-p_1),
gamma=2lambda
```

and objective `(1/2)sum p_j` agree with
`CC*-C*C=2F` and `kappa=(1/2)||C||_HS^2`. The rank face and converse
constructor are correct.

### Low-dimensional theorem — PASS after both-orientation checker

The adjacent-gap formula, zero-eigenvalue equalities, sign edges, and rank
`max(n_+,n_-)` are correct. Face feasibility gives one epigraph inclusion;
exact unrestricted Farkas certificates for every projected inequality and
both orientations of every projected equality give the reverse inclusion.
The inertia obstruction then makes the optimal rank exactly the inertia rank.

### Certificate table — PASS

The exact totals remain:

| `d` | strata | projected H rows | face generators | maximum full rows |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 2 | 6 | 9 | 17 |
| 4 | 4 | 18 | 28 | 39 |
| 5 | 6 | 37 | 69 | 103 |
| 6 | 9 | 77 | 189 | 310 |
| 7 | 12 | 134 | 518 | 1,063 |
| total | 33 | 272 | 813 | — |

Of the 272 projected H rows, 46 are equalities; the supplementary checker
certifies both orientations exactly.

### Dimension eight — PASS

For

```text
lambda(b,c)=(4c-3b,b,b,b,-c,-c,-c,-c), 0<=b<=c,
```

the values are

```text
kappa=10c-7b for b<=c/2,
kappa=9c-5b for b>=c/2,
kappa^(<=4)=10c-6b,
gap=min(b,c-b).
```

The integer spectrum `(5,1,1,1,-2,-2,-2,-2)` has costs `13` and `14` and
minimum optimal rank five. `math/verify_d8_sharpness.py` passes with SHA-256

```text
979605969b0c6df628d619b8255ba9f8ab2bef5f4f63d790d2ca4b48e1a2fa9c.
```

### Dimension nine — PASS

For `(5^4,-4^5)`, the exact costs are `29` and `30`; inertia rank is five and
minimum optimal rank is six. No amplification or unbounded-excess statement
is made.

## Build gate

The current manuscript rebuilt successfully:

```text
7 pages
430,828 bytes
PDF SHA-256 78599b909ac1932aecb6ab00250eb543b4fae71eeaf76874a74e43795d7ae2ad
```

The build script found no LaTeX, bibliography, undefined-reference,
overfull, or underfull warning.

## Final release gate

**UNCONDITIONAL PASS.**  The theorem statements, displayed formulas, exact
certificate census, dimension-eight phase, dimension-nine auxiliary witness,
zero-padding warning, hashes, and declared proof boundary are mutually
consistent.  The integrated equality checker closes the last bookkeeping gap.
No mathematical P0, P1, or release-blocking P2 remains.
