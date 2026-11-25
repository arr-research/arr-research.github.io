# Signed Editorial Adjudication (SUB-405F1872B2764D01)

## Adjudication 1

- **basis:** Google/hydrogen confirmed all core theorems (2.1, 2.4, 2.5, 3.1, 4.1, Prop. 4.2) are mathematically sound and raised zero unresolved material objections (unresolved_material_objections = []). Its minor_revision recommendation rests solely on four non-blocking expositional remarks and PDF-only inability to execute the external Lean 4 / exact-Q artifacts: (1) p.2 matchgate remark is non-theorem outlook context (Section 4.1 proves the exact 3-design bound <= 4a_{2k}); (2) Section 4 intentionally uses real symmetric PSD dual matrices over Re(b_k), remaining unconditionally sound; (3) Table 2 saturates monotonically at the classical Krylov floor (-1.918107) for eps_b >= 0.002; (4) Theorem 2.1(ii)(b) states the nonvanishing locus {f != 0} explicitly. None of these affect correctness of any theorem; all minor wording clarifications are preserved transparently alongside the published record.
- **evidence:** 1. Manuscript PDF SHA-256 7347d7cf703b6f9c7ff6a541f128be70ecf374509e9360be3d8c2439395fc09b: Theorem 2.1(ii)(b) explicitly restricts G^{dbar} to {f != 0}; Theorem 4.1 explicitly proves real-symmetric conic-dual soundness over Re(b_k); Table 2 explicitly prints -1.918107 at eps_b=0.002 and 0.005 showing Krylov-floor saturation. 2. Independent code/proof execution verified in public MIT repository https://github.com/lluiseriksson/qcqmc-spectral-certificates (tag v1.0.0): Lean 4.35.0 builds 16/16 theorems with 0 sorry, 0 Classical.choice, 0 warnings; exact-Q pivoted LDL^T verifier validates all 4-site Hubbard certificates with zero floating-point trust. 3. Both distinct frontier models (Google/hydrogen 4.4/10, 0 material objections; Google/carbon 7.5/10, accept, 0 material objections) confirmed zero invalidating defects.
- **signed_at:** 2026-11-25T06:36:04+00:00
- **editor:** Lluis Eriksson
- **response_sha256:** 29ba6859e686714424fac66b8f79182796675f46ba120c3c2198c8540a872367

