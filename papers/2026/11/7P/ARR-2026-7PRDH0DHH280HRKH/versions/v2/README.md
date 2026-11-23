# From the Gibbs Weight to the Spectral Gap: A Machine-Checked Transfer-Matrix Identification and Spectral-Gap Chain for the Open Z_2 Ising Chain (v2)

- **AIRR identifier:** `ARR-2026-7PRDH0DHH280HRKH` (`v2`, supersedes `v1`)
- **Record type:** `research_paper`
- **Canonical artifact:** `paper.pdf` (`420318` bytes, SHA-256 `4d76fc64967a49734f5fc3f73811a61d356abf6182cf8137af33d6227e7f7607`)
- **Source repository:** https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/tree/yang-mills-archive-v1.0/papers/os-chain-z2

## Revision Summary (v2)

Corrects Theorem 5.1 conjugation and Remark 7.1 algebra, adds verbatim Lean 4 definitions/signatures, narrows title and scope to open Z2 Ising transfer-matrix identification and time-zero pairing, clarifies negative-beta gap and nontrivial positive-time OS quotient.

## Scope & Disclosure

We report a complete Lean 4 / mathlib verification of the transfer-matrix identification and spectral-gap chain for the one-dimensional open-boundary Z_2 Ising spin chain (one Z_2 spin per time slice, 2x2 transfer operator): from the Boltzmann path weight and an independently defined normalized transfer operator T_beta on C^2, through the computed partition function Z_n = 2(exp(beta)+exp(-beta))^n and the Hermitian identification E_n[conj(A(sigma_0)) B(sigma_n)] = <A Omega, T_beta^n (B Omega)>_C, to the exact correlation E_n[f(sigma_0)f(sigma_n)] = (tanh beta)^n. Responding to v1's assessments, v2 prints the verbatim Lean 4 definitions and theorem signatures (confirming conjugation of A in z2PathSum), narrows the title and scope from gauge chain to open Z_2 Ising spin chain, explicitly separates negative-beta spectral gap 1 - |tanh beta| and rank-one beta = 0 behavior, clarifies that z2_pairing_nondegenerate covers only time-zero single-slice observables whereas the full positive-time Osterwalder-Seiler GNS quotient is nontrivial, corrects Remark 7.1 algebraically, and notes that companion reflection positivity is not a logical dependency of z2_identification.

Author Lluis Eriksson owns and administers AIRR (`airr.science`); accordingly, no independent editorial admission or human peer review is claimed. Exact-PDF OpenRouter assessments (`openai/gpt-6.2-sol` and `anthropic/claude-opus-4.8`) are recorded in `registry/model-assessments.json`.
