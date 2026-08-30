# Paper 32 reproducibility and release audit

**Audit date:** 2026-08-30 (Europe/Stockholm)  
**Decision:** **PASS for standalone packaging and ARR deposit candidate.**

## Scientific gates

| Gate | Result |
| --- | --- |
| Canonical `d<=7` projected epigraph replay | PASS; regenerated frozen 33-stratum certificate |
| Equality/linearity audit | PASS; both orientations for 46 equalities |
| Dimension-eight phase and integer witness | PASS; full two-ray phase, costs 13 and 14 at the integer witness |
| Dimension-nine seed | PASS; unrestricted 29, rank-five 30, minimum optimal rank 6 |
| Exact order-27 rank faces | PASS; rank 15/16/17/unrestricted costs 90/89/88/87 |
| Symbolic hive coarse-graining | PASS; 6,804 formal rhombus/boundary identities |
| Independent dictionary replay | PASS; 5,805 rhombi, 540 boundary rows, 170 order rows |
| Standalone isolation test | PASS; replay succeeds without a Paper 31 sibling |
| Full default replay | PASS |

The coarse-grid normalization uses `Q_J=A_J-A_N` and the affine adjustment
`H'(I,L)=H(I,L)+A_N(I-L)`.  This preserves every rhombus and the target
boundary while lowering the coarse cost by `N*A_N/2`.  Omitting this step
would invalidate the unrestricted lower bound.

## Mathematical conclusion

For every integer `t>=1`, the exact audited result is

```text
kappa(F_(3t)) = 87t,
17t < r_*(F_(3t)) <= 18t,
r_0(F_(3t)) = 15t.
```

Thus `r_*(F_(3t))-r_0(F_(3t)) >= 2t+1`.  The package does not claim
`r_*=18t`, the full all-`k` intermediate curve, or optimizer classification.

## Priority and consolidation

The bounded primary-source audit found mechanism-adjacent hive, Horn,
saturation, and puzzle-inflation literature but no exact collision with the
unbounded self-commutator rank-excess theorem.  Its verdict is standalone
paper GO.  This is negative search evidence, not proof of novelty.

The final manuscript now compares the adjacent 1986--2026 self-commutator
literature explicitly and identifies the two public ARR precursors by stable
record ID.  The present threshold and unbounded-excess theorem is not contained
in either precursor.

The manuscript explicitly absorbs and supersedes the unpublished local Paper
31 threshold package.  Paper 30's exact family replays are preserved under
`repro/absorbed_paper30/`, preventing the final article from splitting one
scientific contribution across companion deposits.

## Environment

```text
Python 3.12.6
numpy 2.5.1
pycddlib 3.0.2
scipy 1.18.0
sympy 1.14.0
MiKTeX pdfTeX 1.40.28 / MiKTeX 25.12
Poppler 24.04.0
```

The optional WSL/GMP `lcdd` route is preserved with its binaries and licenses;
the default exact Python replay covers the singular strata and the new
coarse-grid theorem.

## Frozen hashes

```text
PDF        17b2361721027649b8ef5b98440032b91b5b04e89e2a9535fcbe7a27954ac1c5
threshold  e5009d579933af66283de296ac8aa46b8f0b35bae1e43dd300768ef625129bd6
JSON       0103a643644977400052a68738102a7633d6371db8717383ddefa687da8a18a0
d8+d9      00bdbbfd8adbf3aff8f847ae3574241fc7bed887573c8fa6142bb242cf874be7
hive JSON  c6b3588a2415db067f7ff34f7e23592ac9d85f3e10399dd0f8838fc244352b69
hive dual  e353f0f65d7edc2b3274ba2842263747fe5a5728f65c0e1ff4cf05407fde09e2
coarse     e3bfc7df692c021b600bd85fa1b8604b5f12b7bc4995e1dee4e0b1ea8c6fef89
endpoints  f7c66a937e100e293ee68794606036afc09e6eb4e603e1a275bfb9f8d3978d80
theorem    b1ea0d5dad40b56d217cbbe32054110a63267ec7be0e862af964b17cf0cda91f
```

## PDF gate

The final PDF has eleven letter-sized pages and no LaTeX/BibTeX warnings.  Every
page was rendered at 120 dpi.  Contact-sheet review and full-resolution checks
of the title/abstract, coarse-graining formulas, theorem, reproducibility
hashes, conclusion, and references found no clipping, overlap, missing glyph,
broken link token, or unreadable formula.

Two consecutive clean MiKTeX builds produced identical pagination and extracted
text but different PDF bytes because of trailer metadata.  Accordingly, this
audit does not claim byte-deterministic PDF compilation; it freezes the exact
deposited PDF hash above and separately verifies source, text, and rendering.

## Package contract

`package_release.py` rejects any non-frozen PDF, runs the scientific replay by
default, creates a deterministic ZIP with fixed member timestamps, includes a
sorted manifest with every member size and SHA-256, and supports a bytewise
`--check` mode.  Caches, discovery-only scripts, LaTeX intermediates, and QA
PNGs are excluded.

The package is not peer review, formal proof-assistant certification, or
unrestricted priority adjudication.
