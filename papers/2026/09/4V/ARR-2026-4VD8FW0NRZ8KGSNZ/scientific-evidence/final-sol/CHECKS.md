# Scientific checks — B5_born_rigidity_d4 candidate 2

**UTC review window:** 2026-09-14T17:33Z–2026-09-14T17:38Z  
**Exact PDF SHA-256:** `35395ec4804dfd18f8a5319f1ccdcce1ae6618675684acdcb76b3d8d78a71c05`  
**Recommendation:** accept

## Proof audit

For Lemma T, DLMF 18.10.3 with `alpha=d-2`, `beta=0`, and `x=2t-1` gives the stated complex-moment representation. The normalization reduces to the product of a uniform phase and `u~Beta(1,d-2)`. Its integrand has modulus at most `t+(1-t)u`; integrating this majorant gives exactly

`|Q_{n,d}(t)| <= (1-t)^(-(d-2))/binom(n+d-2,n)`.

The equality at `t=0` follows from the beta moment and agrees with the Jacobi endpoint value. The primary DLMF formula supports the constants. Haagerup–Schlichtkrull's primary paper covers nonnegative Jacobi parameters and is correctly presented as supplying a stronger established estimate, so the manuscript does not overclaim novelty for the bound.

For d=4, an equal-trace N=5 tight frame has Gram matrix `(5/4)P`, where `I-P` is rank one with constant diagonal `1/5`. This forces all off-diagonal squared overlaps to `1/16`, proving simplex rigidity. N=4 is an ONB; N>=6 has `gamma<=16/N<=8/3`. Exact Jacobi evaluation gives the simplex minimum

`g_6=22018975/7340032=2.999847275870187...`,

which exceeds `14/5` and `8/3`. The exact range k=2,...,10 plus Lemma T from k=11 onward proves both the global value and uniqueness.

For d=3, the zero-sum Bloch-vector construction is correct and yields a compact four-dimensional N=5 family. The exact certified frame has unit norms and zero sum in `Q(sqrt(q))`. The recurrence computes lower bounds for k=2,...,600 using an integer enclosure of the square root; Lemma T controls all k>600. The manuscript correctly distinguishes the certified lower bound from the unproved numerical optimum.

## Fresh execution

The selected scripts were inspected before execution. They contain no pickle/cache deserialization, subprocess launch, or shell execution. JSON inputs are parsed as rational strings or decimal strings. All runs used a separate workcopy and `C:/Python312/python.exe -X utf8`.

Between `2026-09-14T17:32:38.4679392Z` and `2026-09-14T17:32:48.5408866Z`:

```text
d=3 simplex: exact minimum 77/45 at k=4; tail threshold k>=14 [OK]
d=4 simplex: exact minimum 22018975/7340032 at k=6; tail threshold k>=11 [OK]
exact d=3 frame, k=2..600: minimum lower bound at k=9
CERTIFIED gamma(F) >= 177600993796473305296398794157/10^29
tail k>600: g_k >= 1.78533803
recurrence vs mpmath.jacobi maximum reported errors: 1.1e-42 to 1.0e-44
exact-frame independent evaluation: g_9=1.776009937964733053
numerical point B: five tied degrees reproduce 1.77600994299966361808274335434
```

PDF extraction at `2026-09-14T17:33:00.5530551Z` succeeded: 13 pages and 45,560 characters. The exact theorem statements, the numerical/proved boundary, and the AI statement are present.

## Scope limits

The earlier AIRR record supplying the operator-theoretic interpretation of `g_k` was withheld and not inspected. The long global searches were not replayed because they support only the explicitly numerical conjecture. The exact d=3 lower bound does not depend on them once the rational frame specification is supplied.

The primary-source checks support the corrected Jacobi attribution and the distinction from the Born-sector completeness-stability objective. They do not establish exhaustive priority.

## Disclosure

`independence=involved_in_manuscript`. The same model family participated in manuscript revision. This assessment used a fresh delegated task context with other reports withheld. That is not technical memory isolation or an independent human review. This is a local scientific preassessment only and does not accept, deposit, publish, authorize public release, or create an intake receipt.
