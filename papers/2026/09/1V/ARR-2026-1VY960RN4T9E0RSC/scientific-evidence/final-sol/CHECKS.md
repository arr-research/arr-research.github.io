# Fresh Sol Medium checks — B3_onefold_criterion candidate 2

- Exact PDF SHA-256: `810df760794f04ec3d423f157d6c6e4a30f9651545d636994fc5ce35eebdb654` (matched the authorized hash).
- Assessed with `gpt-5.6-sol`, reasoning effort `medium`, in fresh task context.
- Independence: `involved_in_manuscript`. The PDF's AI-assistance statement discloses that earlier Astra and Sol preassessments contributed corrections. This unavoidable embedded history was not treated as proof; no prior assessment file, score, source diff, provenance file, or editorial registry was consulted for the scientific judgment.
- Code inspection: all Python sources under `repro/` were inspected before execution. They use SymPy/mpmath and write only their declared text/JSON outputs. No pickle, unpickle, serialized-object loading, or network call was present.
- Fresh execution was performed in `work/fable-final-sol/B3_onefold_criterion/repro`, not in the source candidate directory.

## Exact and targeted reproduction

- `manuscript_checks.py`: 47 named symbolic checks; final line `ALL OK`. Log: `manuscript_checks.log`, SHA-256 `4450acdc...8eb5ee0`.
- `candidate_checks.py`: eight symbolic correction identities, 18 Beta cases bracketing `c=2a`, and six even-part cases; final line `PASS: all bounded correction checks`. Log: `candidate_checks.log`, SHA-256 `43a082d1...134173a`.
- Machine-readable bounded results: `candidate_checks.json`, SHA-256 `a98a8fe0...d46f0441`.
- The exact symbolic suite confirms the Riccati factorization, crossing derivative, endpoint-series coefficients, fold bounds, Bessel reduction, even-part ODEs, and scalar envelope identities selected by the authors.
- The bounded numerical suite found the predicted 0/1 zero counts on both sides of `c=2a`; the two independent tilted-variance routes agreed to relative discrepancies around `10^-41` to `10^-40` on the tested grids.

## Proof audit

- Theorem 4.1: the phase-plane argument is logically sound. At any zero of `D`, the derivative has the sign of `2m-1`. This rules out a first crossing before `m=1/2`; after `m=1/2`, negativity forces strict increase, and any later zero would have positive derivative. Endpoint expansions provide the required initial and terminal signs. The boundary `c=2a` is handled by the positive cubic term.
- Theorem 5.1: the integration-by-parts identity correctly requires `a>=1`; the manuscript does not extend its upper bound to `a<1` and supplies counterexamples.
- Theorem 6.1: stationary-point counts, coexistence, and the envelope follow from the unique sign change of `H`, `F'=H`, endpoint exclusion, and the active-radius derivative. The manuscript correctly states that a full source rate-distortion interpretation still needs separate orbit-extremum and channel-attainment inputs.
- Sections 7–8: the Bessel no-fold proof is consistent with the Kummer transformation and direct Riccati argument. The oriented-two-plane single-sign-change claim is explicitly numerical and is not promoted to a theorem.

## Literature and novelty check

Primary sources checked: NIST DLMF §§13.2, 13.4, 13.6, 13.7; Karp–Sitnik (arXiv:0902.3073); Kalmykov–Karp (arXiv:1211.2882); Dytso–Cardone (arXiv:2401.04248); Fatkullin–Slastikov, *Nonlinearity* 18 (2005). Targeted exact-phrase and formula searches did not locate the arbitrary-parameter theorem `one fold iff c>2a`. The cited hypergeometric literature focuses on parameter convexity, Turán inequalities, and ratio monotonicity, while Fatkullin–Slastikov covers a special sphere/Maier–Saupe setting. This supports, but cannot conclusively establish, priority.

## Scope

This is a local preassessment. No SID exists. It is not an intake assessment, editorial acceptance, or public authorization.
