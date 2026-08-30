# Version-locked frontier-model screening

- Protocol: `ARR-ASSESS-1.0`
- Assessment: `arr:assessment:a051cc1d-373e-4d75-9b0a-52f8b21b93ce`
- Model: `OpenAI gpt-5.6-sol`
- Assessed at: `2026-08-30T17:40:00.0530557+02:00`
- Version: `arr:version:9995fadc-8487-446c-b368-15ad54297648`
- Canonical SHA-256: `106e6011a9506b6f64ac04fdc6d991e11bae7db3b4bf7c76cad33825e2190337`
- Recommendation: **minor revision**
- ARR screening outcome: **pass**
- Unresolved material objections: **0**
- Millennium comparison score: **4.20 / 10.00**

## Referee findings

The independent referee checked the exact locked PDF, rendered and inspected all
nine pages, audited the reduction, leakage identity, weighted-shift construction,
Horn certificate, signs, factors of two, rank-two boundary case, and arbitrary
zero padding. A separate numerical search in ranks two through five reproduced
the declared endpoint costs with residuals below `1e-11`; no counterexample or
material objection was found.

The referee identified four plausible novelty candidates: the exact sign-cut
leakage identity, the sharp dimension-independent `rank(F)/2` factor, the spectral
classification of both endpoint equality cases, and the `rank(F)-1` uniform Horn
certificate. The report correctly treats priority as non-exhaustive.

## Bounded concerns and disposition

1. **Priority is not exhaustively certified.** The record retains
   `verification.bibliography: partial`, and the manuscript expressly avoids an
   exhaustive-priority claim.
2. **The replay is not embedded in the PDF.** ARR preserves the exact script,
   output, requirements, and instructions under `src/repro/`; clean-extraction
   replay and manifest verification passed independently. It supports indexing
   checks but is not presented as proof of the analytic theorem.
3. **Earlier dimensions 3--5 are cited to related ARR records.** They are labelled
   related work and are not dependencies of the theorem proved here.
4. **“Complete extremizers” could be read too broadly.** The canonical title does
   not use that phrase, and the abstract and limitations restrict completeness to
   the two universal endpoint equality loci, not all minimizing factors or general
   interior spectra.

The full structured response is preserved in `final-assessment.json` and in the
public model-assessment registry. The pass is a version-specific technical gate;
it is not independent peer review or a guarantee of novelty or correctness.
