# Final priority re-audit

**Manuscript:** *One-Spike Inverse Self-Commutators and Exact Three-versus-Four-Kick Curvature Synthesis*  
**Original audit date:** 2026-08-24 (Europe/Stockholm)  
**Final bibliography recheck:** 2026-08-30 (Europe/Stockholm)  
**Files audited:**

- `paper.tex` — SHA-256 `9D7E1A2E32B395343D66A7FEB80A9B06B694D03607D3755587422B4A5451C2BA`
- `references.bib` — SHA-256 `4394154D1C6B21BC9C6CC1DE948D9A287B7C22CA0F93C25D1B52D1464752FBBC`

## Final verdict

**PASS — unconditional for the priority and bibliography gate.**

All eight mandatory changes from `PRIORITY_AUDIT_INDEPENDENT.md` are implemented. The four defects identified in the preceding re-audit are also corrected: the Cheng/Vong and Xu author names, the separation of kick-mechanism and sign-paired-equality attribution, and disclosure of the separate local rank-adaptive package.

This PASS certifies the scope and accuracy of the priority presentation against the evidence searched; it is not peer review, a proof-correctness certificate, or an exhaustive global novelty guarantee.

The final recheck replaces local or secondary self-citations with stable public
ARR records for the qutrit, four-level, five-level, operational-curvature,
matrix-isoperimetry, and rank-adaptive antecedents.  The manuscript now cites
ARR-2026-1D2QV1RP1292JREW as public complementary work and explicitly states
that it does not contain the arbitrary one-spike formula, every-optimizer
singular rigidity, the sharp stability theorem, or the all-target kick laws.
The added Schur-concavity corollary is an internal consequence of the exact
formula and does not alter the literature-search boundary.  No new priority
claim was introduced.

## Eight mandatory-change checks

| No. | Requirement | Result | Current evidence |
|---:|---|:---:|---|
| 1 | Add a self-prior-art subsection citing the public \(d=3,4,5\), operational-curvature, and matrix-isoperimetry records | **PASS** | `paper.tex` 479–507 contains a dedicated provenance section. Lines 481–487 cite and distinguish all five public records. |
| 2 | Disclose consolidation of the local one-spike theorem package | **PASS** | Lines 492–499 name the local one-spike package, delimit its formula/rigidity/stability overlap, preserve hashes/chronology externally, and state that prepared submission material is not public disclosure. |
| 3 | Qualify \(A_4=16\kappa_d\) as an all-target extension of the known sign-paired face | **PASS** | Abstract 76–80, scope 120–122, and provenance 485–490 consistently identify the advance as extension from the sign-paired equality face to arbitrary traceless Hermitian targets. |
| 4 | Qualify the inverse-cost contribution as dimension-free/arbitrary-dimensional | **PASS** | Lines 101–104 and 109–130 distinguish the arbitrary-dimensional one-spike result from earlier \(d=3,4,5\) formulas and disclaim novelty for weighted shifts and Horn feasibility. |
| 5 | Cite Gini/MAD literature and isolate the new spectral normalization | **PASS** | Lines 287–292 cite Cerone–Dragomir and scope the result to exact constants/equality families for the ordered, nonnegative, fixed-mass spectral normalization. |
| 6 | Present the universal ratio as a corollary and distinguish it from the inverse spectral theorem | **PASS** | The ratio remains a corollary; the inverse Horn/rigidity theorem, stability theorem, and triangle/four-kick reductions are separated into their own sections and proofs. |
| 7 | Avoid exhaustive priority language | **PASS** | Lines 124–130 disclaim known mechanisms and exhaustive novelty; lines 497–499 and 551–553 explicitly state the limits of the public search and novelty conclusion. |
| 8 | Keep local chronology distinct from public priority | **PASS** | Lines 492–507 separately describe two local development packages and explicitly refuse to infer public disclosure from prepared submission material. |

## Four corrective rechecks

### 1. Cheng/Vong author metadata — PASS

`references.bib` now records:

```bibtex
author = {Cheng, Che-Man and Vong, Seak-Weng and Wenzel, David}
```

This agrees with the publisher record for *Commutators with maximal Frobenius norm*: <https://www.sciencedirect.com/science/article/pii/S0024379509004145>.

### 2. Chen et al. author metadata — PASS

`references.bib` now gives the final author as `Xu, Yijia`. The complete author list agrees with the APS record: <https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.4.013191>.

### 3. Kick-mechanism versus sign-paired attribution — PASS

The introductory relation-to-literature sentence now separates:

- earlier balanced-kick mechanisms, cited to `erikssonOperational`; and
- the earlier sign-paired matrix-polygon equality face, cited to `erikssonIsoperimetry`.

The dedicated provenance section makes the same distinction. There is no remaining implication that the operational-curvature record independently established the sign-paired equality face.

Public records:

- <https://ai.vixra.org/abs/2608.0037>
- <https://ai.vixra.org/abs/2608.0035>

### 4. Rank-adaptive local package — PASS

Lines 501–507 disclose *Sharp Rank-Adaptive Bounds for Inverse Self-Commutators*. They correctly identify its overlap—general rank-adaptive bounds, the uniform one-spike endpoint, and Horn-certificate architecture—and distinguish what it does not contain: the arbitrary one-spike formula, every-optimizer rigidity, or the sharp stability theorem. Prepared submission material is again kept separate from verified public priority.

## Requested final confirmations

- **Self-prior-art disclosure:** PASS. Both material local packages and all relevant public author records are disclosed and delimited.
- **Low-dimensional/public antecedents:** PASS. The dimension-three, -four, and -five formulas and triangular identities are expressly treated as earlier results.
- **Sign-paired \(A_4\) scope:** PASS. The manuscript claims only the all-target extension beyond the earlier sign-paired equality face.
- **Gini citation:** PASS. The classical comparison is cited and the paper's specialized constants/equality cases are scoped precisely.
- **Conservative language:** PASS. No unqualified historical “first,” “unprecedented,” or exhaustive nonexistence claim remains.
- **Bibliography accuracy:** PASS. The two previously wrong author names are corrected; the cited primary and public self-record metadata checked in this audit are consistent with their records.

## Build/citation check

The post-correction PDF was rebuilt at 2026-08-24 12:18:45 local time. The corresponding BibTeX log reports 21 used entries and no BibTeX warnings; the LaTeX log contains no undefined-citation or undefined-reference warning.

## Disposition

No priority or bibliography edit remains required. On this audit's scope, the manuscript is ready to proceed to the remaining mathematical, reproducibility, visual, and publication gates.
