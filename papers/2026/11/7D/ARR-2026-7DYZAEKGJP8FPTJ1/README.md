# The Eriksson Programme (Yang-Mills): Machine-Checked Lattice Gauge Foundations, Certified Obstructions, and the Open Frontier

- **AIRR identifier:** `ARR-2026-7DYZAEKGJP8FPTJ1` (`v1`)
- **Record type:** `technical_note`
- **Canonical artifact:** `paper.pdf` (`452774` bytes, SHA-256 `b931d93d770bbc01649150ab2a040782c01834147fe2f4d38e86c6806723649a`)
- **Source repository:** https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/releases/tag/yang-mills-archive-v1.0

## Scope & Disclosure

We present an archival technical synthesis and handoff specification for the Yang-Mills formalization programme inside THE-ERIKSSON-PROGRAMME (archival release yang-mills-archive-v1.0). The repository pins Lean 4 (v4.29.0-rc6) and mathlib (07642720480157414db592fa85b626dafb71355b) and maintains a continuously verified core module, YangMillsCore, whose build and axiom oracle pass in GitHub Actions with zero sorry declarations, zero project-specific axioms, and every headline declaration restricted to Lean's three foundational axioms [propext, Classical.choice, Quot.sound]. Within this verified core, the programme establishes a reusable Kotecky-Preiss and Mayer-Ursell polymer cluster-expansion engine, finite-volume and volume-uniform strong-coupling Wilson-loop area laws and unconditional IR clustering for SU(N) without Peter-Weyl, exact Z_N centre-symmetry rules, machine-checked Amos/Bessel ratio bounds and killed von Mises bridge monotonicity, complete Z_2 Osterwalder-Seiler chains, and certified negative obstructions. No four-dimensional continuum limit, physical SU(N) OS/Wightman reconstruction, or Clay Millennium Prize solution is claimed; historical Clay distance remains ~0% (<0.1%). Open frontiers (hRpoly in draft PR #29, physical SU(N) reflection positivity/transfer, and M4-M5 continuum reconstruction) and 30+ AIRR records are indexed in one citable archival record.

Author Lluis Eriksson owns and administers AIRR (`airr.science`); accordingly, no independent editorial admission or human peer review is claimed for this working-paper deposit. Exact-PDF frontier-model assessments are recorded in `registry/model-assessments.json`.
