# Final manuscript priority audit — integrated Paper 31

**Audit date:** 24 August 2026 (Europe/Stockholm)  
**Audited source:** `work/paper31-frontier/paper.tex`  
**Audited bibliography:** `work/paper31-frontier/references.bib`

## Final gate

**PASS / GO. No priority, self-prior-art, salami-slicing, scope, or
bibliographic correction remains in the audited source.**

Paper 31 is now a single coherent sharp-threshold paper. It absorbs the
dimension-eight family and dimension-nine witness from Paper 30, identifies
Paper 29 as the earlier isolated witness, discloses Paper 28 as the one-spike
and rank-adaptive antecedent, and adds the genuinely new universal theorem
through dimension seven. Separate Paper 29 and Paper 30 deposits remain
**NO-GO** while this integrated manuscript is the intended research object.

The central priority claim is conservatively and correctly stated:

> Dimension eight is the least dimension in which Hilbert--Schmidt norm
> optimality can force the rank of a self-commutator factor strictly above the
> inertia lower bound.

This does not claim that eight is the least dimension for self-commutator
existence or for an unqualified algebraic representation-rank phenomenon.

## Resolution of the three prior holds

### 1. Self-prior art and consolidation — PASS

The introduction now contains a dedicated “Development history and
consolidation” paragraph. It identifies all three local predecessors and
their exact roles:

- *One-Spike Inverse Self-Commutators and Exact Three-versus-Four-Kick
  Curvature Synthesis* supplies the one-spike antecedent and rank-adaptive
  architecture;
- *Minimum-Norm Self-Commutators Can Require Rank Above the Inertia Bound*
  supplies one interior dimension-eight witness;
- *An Exact Rank--Norm Phase Diagram for Three-Level Self-Commutator Targets*
  replaces that point by the full displayed parametric family and adds the
  dimension-nine witness.

The manuscript explicitly says that it absorbs and supersedes the latter two
local drafts instead of treating them as separate publications. It also says
that prepared local release/submission material is not public disclosure and
requires any predecessor that later acquires a public identifier to be cited
with an updated relationship. This is adequate and unusually transparent
self-prior-art disclosure.

### 2. Dimension-eight scope — PASS

The formerly ambiguous “full/complete dimension-eight cone/phase” language
has been removed from the headline locations. The manuscript now consistently
uses:

- “the entire explicit two-ray cone” in the abstract;
- “the entire explicit two-ray dimension-eight cone” in the introduction;
- “Sharpness on an explicit dimension-eight cone” as the section title;
- “the entire displayed projective segment” for persistence of the gap.

Immediately after defining the family, the text states that it is
two-dimensional before quotienting by positive scale and one-dimensional
projectively, and explicitly disclaims a classification of all
dimension-eight spectra. The `14/13` relative tax is scoped to “this explicit
cone.” No full-dimensional Horn chamber, global dimension-eight tax, or
higher-dimensional extremality is claimed.

### 3. Classical trace-zero citation — PASS

The opening historical statement now cites Albert--Muckenhoupt directly. The
new bibliography entry is accurate:

- A. Adrian Albert and Benjamin Muckenhoupt, “On Matrices of Trace Zero,”
  *Michigan Mathematical Journal* **4** (1957), no. 1, 1--3,
  <https://doi.org/10.1307/mmj/1028990168>.

The ordinary commutator theorem is therefore separated cleanly from
Fan--Fong self-commutator existence, compact-operator theory, and forward
commutator-norm inequalities.

## Theorem and scope audit

| Component | Final finding | Gate |
|---|---|---|
| `r_*(F)=max(n_+,n_-)` for every traceless Hermitian target in `d<=7` | Correctly universal and includes singular spectra and the zero target | **PASS** |
| Projected-epigraph proposition | Now correctly restricted to `3<=d<=7`, matching the 33 enumerated nontrivial sign--zero strata | **PASS** |
| Dimensions `d<=2` | Handled separately as elementary in the theorem proof | **PASS** |
| Singular targets | Explicit zero-eigenvalue equalities are required and described; no invalid zero-padding inference | **PASS** |
| Dimension-eight family | Exact two-regime unrestricted value, rank-four value and interior rank-five conclusion; correctly scoped to the displayed cone | **PASS** |
| Sharp threshold | Follows from the universal low-dimensional theorem plus an exact `d=8` witness | **PASS** |
| Dimension-nine target | Presented as an adjacent two-valued check, not as evidence for a universal higher-dimensional theorem | **PASS** |
| Computer assistance | Exact rational objects are distinguished from floating support discovery | **PASS** |

Restricting Proposition 3.2 to `3<=d<=7` removes the earlier formal mismatch
between a proposition quantified over all `d<=7` and a stratum definition
requiring both positive and negative counts. It remains fully sufficient for
Theorem 3.1 because the zero target and dimensions one and two are handled
separately.

## Priority and overclaim audit

The manuscript passes every claim boundary set in the independent priority
audit:

- it does not call the result “the first” or claim absolute novelty;
- it reports only that a bounded search found no exact antecedent and states
  explicitly that this is not proof of novelty;
- it attributes the Horn/Klyachko/Knutson--Tao/Fulton mechanism rather than
  claiming a new additive-eigenvalue theorem;
- it treats the inertia obstruction and finite self-commutator existence as
  background;
- it does not classify optimizer matrices;
- it does not classify all dimension-eight spectra;
- it does not claim a universal rank-excess bound above dimension seven;
- it does not claim that the displayed cone is extremal among
  higher-dimensional targets;
- it does not infer persistence in all higher dimensions by zero-padding.

The phrases “exact low-dimensional classification” and “sharp dimension
threshold” are justified: the first refers to every target through dimension
seven, and the second has both the universal lower-dimensional half and an
exact dimension-eight sharpness example.

## Bibliography audit

The inspected bibliography is adequate for the claims actually made.
Authors, titles, venues, years, pages and identifiers pass for:

- Albert--Muckenhoupt;
- Horn;
- Klyachko;
- Knutson--Tao;
- Fulton;
- Fan--Fong;
- Weiss;
- Böttcher--Wenzel;
- Fukuda--Prodon;
- cddlib;
- the three cited public Eriksson ai.viXra records.

No citation to a merely local Paper 29 or Paper 30 draft is necessary after
the explicit development-history disclosure, because neither is treated as a
public scholarly record. If that status changes before deposit, the
manuscript itself already commits to updating the citation and relationship.

Recent adjacent works on a new honeycomb proof or forward Aluthge
self-commutator norms are not exact antecedents and are not mandatory
bibliography additions for this narrowly framed theorem.

## Anti-salami and deposit instruction

The current integrated object passes the anti-salami gate under the stated
publication status:

1. deposit Paper 31 as the single research paper;
2. do not deposit Papers 29 or 30 separately;
3. preserve their local hashes and chronology as development provenance;
4. if an external identifier for a predecessor is discovered before deposit,
   cite it and encode the actual `extends`/`supersedes` relation rather than
   silently replacing it.

This instruction concerns transparent scholarly provenance. It does not by
itself authorize publication or assert independent peer review.

## Frozen hashes

```text
paper.tex
43f1dfbd30520e23e8fa6668f7de23d1339531244977bf190fa494754e7691e3

references.bib
0a058f5d0c557fbd9821181bd941cf8c4b482bbd10472feac88569509177832d

math/audit_d_le_7_equalities.py
0362a3dae16a027b87b3e39c360dfa657f42fd686401c2340d46013bd7bfb95e

build/paper.pdf
78599b909ac1932aecb6ab00250eb543b4fae71eeaf76874a74e43795d7ae2ad
```

The source change after the preceding PASS was bookkeeping-only. The
reproducibility section now states that the canonical JSON serializes one
orientation of each projected row and separately cites the fail-closed
equality auditor, which preserves `cdd.gmp`'s linearity set and checks both
exact Farkas orientations for all 46 projected equalities. This clarification
does not enlarge or alter any theorem, priority statement, cone scope, or
self-prior-art relation. The **PASS / GO** gate is unchanged.

Any later source or bibliography edit invalidates this final gate and requires
a focused re-audit.

## Final decision

**PASS / GO for the integrated Paper 31. No remaining manuscript priority
edits.** The novelty statement remains appropriately conditional on a bounded
search, the exact theorem is correctly scoped, all known self-prior art is
disclosed, and the manuscript eliminates the Paper 29/Paper 30 salami-slicing
risk by absorbing both into one sharp dimensional-threshold result.
