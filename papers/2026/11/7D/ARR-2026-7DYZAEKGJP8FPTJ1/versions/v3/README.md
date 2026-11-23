# The Eriksson Programme (Yang-Mills): Auditable Claim-to-Theorem Manifest, Certified Obstructions, and Continuation Frontier (Release yang-mills-archive-v1.0) (v3)

- **AIRR identifier:** `ARR-2026-7DYZAEKGJP8FPTJ1` (`v3`, supersedes `v2`)
- **Record type:** `technical_note`
- **Canonical artifact:** `paper.pdf` (`556162` bytes, SHA-256 `fdcd834861d3e7446900b105209a4379ee2af0b8cbf5e11f92e67d76582db10b`)
- **Source repository:** https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/releases/tag/yang-mills-archive-v1.0

## Revision Summary (v3)

v3 resolves all remaining gpt-6.2-sol objections on v2: adds literal Lean 4 signatures (complex modulus, four KP inequalities, chainAreaA unspannable-chain behavior), explicit beta > 0 and SingleScaleUVDecay/covUV_concrete definitions in the RG conditional, exact unweighted Poincare predicate vs penalized coercivity and scale quantifiers, explicit transverse periodic Fourier witness A^(l) in ker Q_l for flat Hodge obstructions, explicit AmosBound inequality and CompatibleLocalObservable substrate, a declaration-level oracle coverage table including check_oracle_output.py, explicit W = 2(F_a'F_b - F_aF_b') normalization, and reconciles Table 1 to 33 companion rows.

## Scope & Disclosure

This archival technical note provides a self-contained, auditable claim-to-theorem specification and continuation handoff for the Yang-Mills Lean 4 formalization inside THE-ERIKSSON-PROGRAMME at archival release yang-mills-archive-v1.0 (commit 6b54eca695e96b3038ceda18276c4e28fb45983f; canonical Lean core checkpoint 02fae0ad, Lean v4.29.0-rc6, pinned mathlib 07642720480157414db592fa85b626dafb71355b). Responding to hostile assessments of v1 and v2, this v3 revision prints exact Lean 4 theorem statements and complete hypotheses (complex modulus and all four KP inequalities in the exact-action Wilson-loop area law, unspannable-chain behavior of chainAreaA, beta > 0 and literal definitions of SingleScaleUVDecay and covUV_concrete in the marginal RG conditional, unweighted Poincare predicate vs penalized coercivity and exact scale quantifiers, explicit transverse periodic Fourier witness A^(l) in ker Q_l for the flat Hodge factorized-penalty wall, explicit AmosBound inequality, and CompatibleLocalObservable thermodynamic-limit substrate), a declaration-level audit-coverage table distinguishing root oracle_check.lean (2,851 readouts across 46 imports), per-module oracles, and compiled-only modules, and a reconciled cross-reference of all 33 companion repository folders to their 33 live AIRR identifiers. No 4D continuum limit, physical SU(N) OS/Wightman reconstruction, or Clay Millennium Prize solution is claimed.

Author Lluis Eriksson owns and administers AIRR (`airr.science`); accordingly, no independent editorial admission or human peer review is claimed. Exact-PDF OpenRouter assessments (`openai/gpt-6.2-sol` and `anthropic/claude-opus-4.8`) are recorded in `registry/model-assessments.json`.
