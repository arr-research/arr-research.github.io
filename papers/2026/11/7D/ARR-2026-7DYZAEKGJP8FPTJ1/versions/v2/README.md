# The Eriksson Programme (Yang-Mills): Auditable Claim-to-Theorem Manifest, Certified Obstructions, and Continuation Frontier (Release yang-mills-archive-v1.0) (v2)

- **AIRR identifier:** `ARR-2026-7DYZAEKGJP8FPTJ1` (`v2`, supersedes `v1`)
- **Record type:** `technical_note`
- **Canonical artifact:** `paper.pdf` (`535096` bytes, SHA-256 `c1fd413208ccd66d1796a77ad4572b04ac6f71439c14106b3ad9da5d8c0e689e`)
- **Source repository:** https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/releases/tag/yang-mills-archive-v1.0

## Revision Summary (v2)

Replaces directory-level prose with an auditable claim-to-theorem manifest containing exact Lean 4 signatures, explicit coupling/domain hypotheses, non-vacuity witnesses, obstruction operator classes, and resolved AIRR cross-references.

## Scope & Disclosure

This archival technical note provides a self-contained, auditable claim-to-theorem specification and continuation handoff for the Yang-Mills Lean 4 formalization inside THE-ERIKSSON-PROGRAMME at archival release yang-mills-archive-v1.0 (commit 6b54eca695e96b3038ceda18276c4e28fb45983f; canonical Lean core checkpoint 02fae0ad, Lean v4.29.0-rc6, pinned mathlib 07642720480157414db592fa85b626dafb71355b). Responding to v1's assessments, this v2 revision replaces directory-level summaries with exact fully-qualified Lean 4 theorem statements, explicit coupling and geometric hypotheses, concrete strictly-interacting SU(2) non-vacuity witnesses (0 < |beta| <= 1e-5), exact operator classes and volume quantifiers for the certified obstructions (volume-uniform Poincare walls and flat Hodge factorized-penalty walls), a strict separation of YangMillsCore-compiled, oracle_check-audited, and standalone declarations, and resolved AIRR identifiers for all 32 indexed mathematical-physics records. No four-dimensional continuum limit, physical SU(N) OS/Wightman reconstruction, or Clay Millennium Prize solution is claimed; open formalization tasks (fixed-spacing Wilson reflection positivity and hRpoly in draft PR #29) are distinguished from open mathematics.

Author Lluis Eriksson owns and administers AIRR (`airr.science`); accordingly, no independent editorial admission or human peer review is claimed. Exact-PDF OpenRouter assessments (`openai/gpt-6.2-sol` and `anthropic/claude-opus-4.8`) are recorded in `registry/model-assessments.json`.
