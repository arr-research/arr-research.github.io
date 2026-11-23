# From the Gibbs Weight to the Spectral Gap: A Machine-Checked Transfer-Matrix Identification and Spectral-Gap Chain for the Open Z_2 Ising Spin Chain (v3)

- **AIRR identifier:** `ARR-2026-7PRDH0DHH280HRKH` (`v3`, supersedes `v2`)
- **Record type:** `research_paper`
- **Canonical artifact:** `paper.pdf` (`447611` bytes, SHA-256 `545fe80aa659ce2b16296f6963b5240f14fa1a775b668efa80fd07fd649e4781`)
- **Source repository:** https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/tree/yang-mills-archive-v1.0/papers/os-chain-z2

## Revision Summary (v3)

v3 resolves both remaining gpt-6.2-sol objections and all potential errors on v2: prints verbatim Lean 4 definitions of z2TransferOp, z2Vac, z2SignObs, vacuumProjectionC, projectedTransferC, connCorrC, and z2Partition_eq; strictly separates machine-checked Lean 4 declarations from elementary analytic consequences proved in prose (all-beta spectrum, beta < 0 absolute gap 1-|tanh beta| vs algebraic eigenvalue gap 1-tanh beta, and beta = 0 rank-one obstruction to a finite Hermitian H); uses explicit conj(...) notation so plain-text PDF extraction preserves conjugation; specifies sign/connected correlations at beta = 0; pins checkpoint-to-release mapping and oracle_check.lean coverage.

## Scope & Disclosure

We report a Lean 4 / mathlib formalization of the transfer-matrix identification and spectral-gap chain for the one-dimensional open-boundary Z_2 Ising spin chain (one Z_2 spin per time slice, 2x2 transfer operator): from the Boltzmann path weight and an independently defined normalized transfer operator T_beta on C^2, through the computed partition function Z_n = 2(exp(beta)+exp(-beta))^n and the Hermitian identification E_n[conj(A(sigma_0)) B(sigma_n)] = <A Omega, T_beta^n (B Omega)>_C, to the exact correlation E_n[f(sigma_0)f(sigma_n)] = (tanh beta)^n. This v3 revision prints verbatim all core Lean 4 definitions (z2TransferOp, z2Vac, z2SignObs, vacuumProjectionC, projectedTransferC, connCorrC, and z2Partition_eq), strictly separates machine-checked Lean 4 declarations from elementary analytic consequences proved in prose (exact all-beta spectrum, beta < 0 absolute spectral gap 1 - |tanh beta| vs algebraic eigenvalue gap 1 - tanh beta, and beta = 0 rank-one obstruction to a finite Hermitian H), uses explicit conj(...) notation so plain-text PDF extraction preserves conjugation, clarifies that z2_pairing_nondegenerate covers only time-zero single-slice observables whereas the full positive-time OS quotient is nontrivial, and pins the checkpoint-to-release mapping and oracle_check.lean coverage.

Author Lluis Eriksson owns and administers AIRR (`airr.science`); accordingly, no independent editorial admission or human peer review is claimed. Exact-PDF OpenRouter assessments (`openai/gpt-6.2-sol` and `anthropic/claude-opus-4.8`) are recorded in `registry/model-assessments.json`.
