# ARR frontier-model assessment policy — ARR-ASSESS-1.0

**Effective:** 2026-08-30  
**Operator:** Lluis Eriksson  
**Public registry:** `registry/model-assessments.json`

## Purpose and boundary

ARR's defining function is hostile audit by the strongest available frontier
models. They are instructed to attack, rather than merely summarize, each exact
artifact: seek counterexamples, hidden assumptions, proof gaps, unsupported novelty
and reproducibility failures. A paper that survives the gate has passed a materially
harder, more transparent filter than unreviewed repository upload. A model report is
still evidence about one model's inspection, not peer review, a proof certificate,
a priority ruling, an endorsement, or a substitute for qualified human and formal
verification.

For each new admission, the operator declares a version-locked frontier-model audit
set suited to the available services, quota and subject. ARR promises no fixed
provider, model, report count or reasoning tier. Every valid result obtained in the
declared round is retained. An unresolved material objection blocks acceptance: the
editor must request a corrected version or decline the submission. The human editor
decides whether an objection is material and records that decision.
For already published work, a later material objection triggers the correction,
withdrawal or documented-no-change procedure; it is never silently deleted.

Legacy ARR records explicitly labelled `not_assessed` remain so until a real,
version-locked report is imported. ARR never backfills a score from memory, a title,
or an assessment of a different version.

## Administrator workflow

1. Generate the locked prompt with
   `python scripts/prepare_model_assessment.py ARR-ID --version vN`.
2. Before the round, select the frontier service or services available and suitable
   for the case. In each fresh conversation, attach the canonical PDF and paste the
   generated prompt. The selection may remain private while the round is running,
   but every published result must disclose the exact provider and public model
   identifier.
3. Copy the model's single JSON response. Validate it without publication using
   `python scripts/record_model_assessment.py --clipboard`.
4. Inspect the response, resolve obvious transcription or identifier errors by
   obtaining a new model response, and adjudicate every material objection. Never
   edit a model's scientific conclusion while presenting it as the original result.
5. Append the exact structured result with
   `python scripts/record_model_assessment.py --clipboard --publish`, review the Git
   diff, run the repository tests and publish through the protected release flow.

The public response hash detects accidental duplicate imports. ARR does not request
or publish private chain-of-thought. Concise findings and their evidence are enough.

## Independence and aggregation

Each report identifies whether that model was involved in producing the manuscript.
All reports remain visible, but only reports marked `not_involved_in_manuscript`
enter the headline aggregate. ARR reports the median, range and number of eligible
reports; it never hides dispersion behind a lone average. Assessments of different
versions are never pooled. Multiple outputs from closely related models are not
described as statistically independent merely because their product names differ.

The operator may select which frontier services to consult, but cannot conceal the
identity of a published model report. Model identity, assessment time, exact paper
version and artifact hash are part of the public provenance.

Model selection may remain private until the batch is complete to reduce strategic
prompting, but the batch rule must be fixed before the first run. Every valid result
obtained in that batch is recorded, including low scores, rejection recommendations
and disagreements. The operator may not repeatedly sample and publish only the most
favourable response. Invalid JSON may be rerun solely to obtain schema-conforming
output; the invalid-response hash and rerun reason remain in the private audit log.
Later reassessment is a new dated batch, not a silent replacement. Donations,
authorship, personal relationships and an editor's preferred result cannot affect
model selection or report visibility.

## The 0.00–10.00 Millennium scale

This is a high-ceiling research scale, not a school grade and not a probability of
correctness. The public whole-star display is the nearest integer, with a minimum of
one star for a completed assessment.

| Stars | Public label | Interpretation |
|---:|---|---|
| 1 | Critical concerns | Main claims require fundamental re-examination. |
| 2 | Substantial revision needed | There is research value, but major issues remain. |
| 3 | Acceptable | Substantive, inspectable work at the ARR publication floor. |
| 4 | Strong | A clear and technically serious contribution. |
| 5 | Very good | A notably good paper; this is not a mediocre or failing grade. |
| 6 | Excellent | Deep, convincing work with broad technical strength. |
| 7 | Exceptional | Unusually strong and consequential research. |
| 8 | Potentially field-shaping | A result that may materially redirect a field. |
| 9 | Potentially historic | A result that may become a landmark after verification. |
| 10 | Millennium-resolution benchmark | Reserved for an unconditional solution of a recognized Millennium Prize Problem surviving extraordinary independent verification. |

A single model may use 10.00 only as the top anchor defined above. Its output cannot
by itself establish that the benchmark has been met. ARR must display the underlying
reports and any human or formal verification rather than turning the number into a
truth claim.

## Five criterion ratings

Models separately assign one to five stars, each with a concise basis, for:

- correctness confidence;
- rigor and completeness;
- novelty relative to sources actually checked;
- significance if the claims hold; and
- reproducibility or independent inspectability.

These criterion stars diagnose a paper; they are not silently averaged into the
overall score. “Not checked” must be stated in the basis and cannot be presented as
positive evidence.

## Editorial highlights and rankings

The scientific ranking contains only exact-version papers with at least one eligible
published assessment. It orders papers by median score, then assessment count, then
title. Unrated papers remain in the catalogue as `Not yet rated`; zero is never
substituted for missing evidence.

An editorial highlight is a separate, signed human note explaining why a leading
paper matters, its concrete strengths and its caveats. It cannot alter model reports
or buy ranking position. Corrections and later model assessments remain visible so
future systems can compare how evaluations changed over time.

## Error and appeal procedure

Authors may challenge a report by identifying the exact assessment, claim and
evidence. The original model output remains preserved. ARR may append an author
response, a new independent assessment, or an editorial adjudication; substantive
changes to the paper require a new version. The editor cannot characterize a
model-detected issue as resolved without a public, concise basis.
