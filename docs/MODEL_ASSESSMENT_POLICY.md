# AIRR frontier-model assessment policy — ARR-ASSESS-1.0

**Founder-authored rule updated: 2026-09-09 — AIRR-FOUNDER-1.0.**

**Review eligibility and rating revision: 2026-09-12 — AIRR-RATING-1.0.**
This revision takes effect when this commit is released. The
assessment response format remains ARR-ASSESS-1.0. The aggregation method has its
own version so that original reports do not need to be rewritten.

**Effective:** 2026-08-30  
**Operator:** Lluis Eriksson  
**Public registry:** `registry/model-assessments.json`

## Purpose and boundary

AIRR's defining function is hostile audit by the strongest available frontier
models. They are instructed to attack, rather than merely summarize, each exact
artifact: seek counterexamples, hidden assumptions, proof gaps, unsupported novelty
and reproducibility failures. A paper that survives the gate has passed a materially
harder, more transparent filter than unreviewed repository upload. A model report is
still evidence about one model's inspection, not peer review, a proof certificate,
a priority ruling, an endorsement, or a substitute for qualified human and formal
verification.

For each new admission, the operator declares a version-locked frontier-model audit
set suited to the available services, quota and subject. AIRR promises no fixed
provider, model or reasoning tier. Founder-authored admission requires two distinct
identified models. Every valid result obtained in the
declared round is retained. An unresolved material objection blocks acceptance: the
editor must request a corrected version or decline the submission. The human editor
decides whether an objection is material and records that decision.
For already published work, a later material objection triggers the correction,
withdrawal or documented-no-change procedure; it is never silently deleted.

Legacy AIRR records explicitly labelled `not_assessed` remain so until a real,
version-locked report is imported. AIRR never backfills a score from memory, a title,
or an assessment of a different version.

## Administrator workflow

1. Generate the locked prompt with
   `python scripts/prepare_model_assessment.py ARR-ID --version vN`.
2. Before the round, select the frontier service or services available and suitable
   for the case. In each fresh conversation, attach the canonical PDF and paste the
   generated prompt with `--prior-involvement` set to the factual declaration
   for that model. Verify and record fresh-context controls before supplying the
   paper. The selection may remain private while the round is running,
   but every published result must disclose the exact provider and public model
   identifier.
3. Copy the model's single JSON response. Validate it without publication using
   `python scripts/record_model_assessment.py --clipboard`.
4. Inspect the response, resolve obvious transcription or identifier errors by
   obtaining a new model response, and adjudicate every material objection. Never
   edit a model's scientific conclusion while presenting it as the original result.
5. Append the exact structured result with
   `python scripts/record_model_assessment.py --clipboard --review-context context.json --runtime-provenance runtime.json --publish`, review the Git
   diff, run the repository tests and publish through the protected release flow.

The separate context JSON follows `review_context` in the public assessment schema;
its digest refers to retained operator evidence, not an assertion by the reviewer.
The public response hash detects accidental duplicate imports. AIRR does not request
or publish private chain-of-thought. Concise findings and their evidence are enough.
The separate runtime JSON follows `runtime_provenance` in the schema. Omit either
operator file when the corresponding evidence is unavailable; never fill it with
an inferred model configuration or invented isolation controls.

### Runtime identity corrections

The model-authored JSON and its response hash remain immutable. When independently
verifiable platform runtime metadata or a contemporaneous operator/author UI record
establishes that the response self-reported the wrong model identifier, AIRR appends
a separate `runtime_provenance` object. It records the effective provider, exact
model identifier, reasoning-effort tier, evidentiary basis, and evidence SHA-256.
The public heading uses this independently evidenced runtime identity; the original
self-report remains preserved beneath the unchanged response hash. Reasoning effort
is published only when directly evidenced and is never inferred from response style.

### Preserved public intake reports

An already-public ARR-INTAKE-ASSESS-1.1 report may be projected into the assessment
registry with `scripts/import_public_intake_assessment.py`. The importer requires
this public version's screening file and exactly matching PDF. It retains the
native protocol, assessment date, score, findings and participation declaration;
`intake_source` binds the unchanged source path, raw file digest and submission ID.
The structured response hash is calculated from the original intake response,
not a fabricated ARR-ASSESS response. Validation checks both the raw bytes and a
lossless reconstruction against the public file. No new review, runtime identity,
context isolation or editorial decision is asserted by the import.

## Prior participation, separate review context and aggregation

Each report identifies whether that model was involved in producing the manuscript.
Prior participation does not disqualify a model from reviewing, recommending
acceptance or contributing its score. This supersedes the former exclusion of
involved models from the headline aggregate. Participation has no numerical penalty.
The declaration is preserved: a new conversation does not change an involved model
into a model that was not involved.

New review rounds use fresh conversations, without inherited manuscript-development
history, saved memory, access to the author's development workspace, or the other
reviewers' reports. Supply the locked manuscript, the standard rubric, relevant
public sources and a factual declaration of prior model involvement. Do not supply
earlier scores, desired acceptance outcomes or the author's rebuttals to earlier
reviewers. Select the round before it starts. Three or four distinct suitable models
are a useful target when available; founder-authored admission still requires at
least two. Separate effort settings or new threads of one model do not create
additional model identities.

The operator records the verified controls separately in `review_context` and
retains the underlying evidence. A `fresh_blind` record requires all three controls:
history isolation (including workspace access), disabled memory, and withheld
other reports. A model cannot write this operator-controlled object itself.
Unverified controls must not be marked true. If a service does not expose a control,
record that limitation and instruct the reviewer not to use the unavailable context;
an instruction is not technical verification. Reports with incomplete context evidence,
including legacy reports, remain usable as explicitly limited evidence. Missing
context metadata is shown as unknown, not retrospectively certified. A documented
review with verified controls is required for the stronger evidence description.
Statistical independence is not implied
by separate conversations, different product names or different providers.

AIRR publishes a bounded capability-weighted mean, score range and model count.
Only the latest report for each provider and base model contributes numerically,
across all its effort settings. Earlier reports and objections remain visible;
an unresolved adverse report still requires an editorial disposition. Conflicting
reports at the same time are an error requiring investigation, not a best-score
selection. Different papers, versions and PDF hashes are never pooled.

### Provisional capability weighting and evidence description

For a mathematical paper with an exact evidenced runtime model and effort match in
the pinned Epoch AI FrontierMath Tier 4 v2 snapshot, let `p` be benchmark accuracy
and `SE` its reported standard error, both as proportions. Define:

```
q = max(0, p - SE)
w = 1 + 2*q                         # 1 <= w <= 3
paper_score = sum(w * original_score) / sum(w)
```

The subtraction of one standard error and the coefficient 2 are provisional AIRR
policy choices. They are not fitted estimates of referee reliability. The benchmark
measures solving difficult mathematics, not reviewing papers, novelty judgment or
truth. Unknown configurations receive neutral weight 1, without inventing a zero
benchmark score or borrowing another model's effort tier. Mathematical scope is the curated Mathematics subject hierarchy plus explicit
Mathematical Physics; other subjects receive no adjustment. Keywords do not
activate it. A single report keeps its original
score; with several models, the stronger measured configuration has more influence
when they disagree. Raw reports are never numerically altered.

The initial snapshot was retrieved on 12 September 2026 from [Epoch AI's native
benchmark data](https://epoch.ai/data/benchmark_data.zip), under CC-BY-4.0. Its CSV,
normalized values, source links, retrieval time and hashes are preserved in
`registry/benchmarks/`. [Epoch AI's methodology](https://epoch.ai/benchmarks/about)
describes its error bars as one standard error. For example, Astra High's 0.976
accuracy and 0.024 standard error produce weight 2.904. Sol High has no exact row
in this snapshot and receives weight 1; Sol Max's result is not substituted.
Two hypothetical scores of 6 (Astra High) and 8 (Sol High) therefore yield 6.51.

Each score has a qualitative evidence description. It remains **Limited** if there
is only one distinct model or provider, unverified fresh context, incomplete
benchmark matching, disagreement exceeding one point, or an adverse report needing
disposition. Otherwise it may say **Broader model support**. These labels describe
the observed evidence, not a calibrated confidence interval or probability of
correctness. Models alone do not establish high confidence. Strengthening the
claim requires independent expert review, formal verification where applicable,
reproduction and subsequent scrutiny. The public machine-readable record explicitly
leaves `confidence_probability` null.

Benchmark snapshots are pinned, not fetched during a site build. A future benchmark
or formula revision requires a new identified snapshot and an explicit policy
change; preserve the old rating snapshot before release. A newly leading model does
not automatically depreciate old scores. New scientific reports are dated
reassessments of the same exact artifact, or separate assessments of a new version.
Before offering numerical correctness probabilities, validate the method against
held-out papers with known errors and independently adjudicated results, including
false acceptance rates, shared errors and calibration by subject.

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

### Founder-authored admission and prior model involvement

Founder-authored admission requires documented review by two identified models.
Reports from models involved in preparation may support that admission decision
when their involvement is accurately declared. Their scores also enter the
aggregate under the review-context policy above. This does not relabel them as
`not_involved_in_manuscript` or establish statistical independence. A fresh reviewing
conversation is a distinct evaluation context, not a different model. Draft
generation alone is not a review report.
The version-locking, actual-response provenance, retention and material-objection
rules above continue to apply. The human decision follows GOVERNANCE.md.

## The 0.00–10.00 Millennium scale

This is a high-ceiling research scale, not a school grade and not a probability of
correctness. The public whole-star display is the nearest integer, with a minimum of
one star for a completed assessment.

| Stars | Public label | Interpretation |
|---:|---|---|
| 1 | Critical concerns | Main claims require fundamental re-examination. |
| 2 | Substantial revision needed | There is research value, but major issues remain. |
| 3 | Acceptable | Substantive, inspectable work at the AIRR publication floor. |
| 4 | Strong | A clear and technically serious contribution. |
| 5 | Very good | A notably good paper; this is not a mediocre or failing grade. |
| 6 | Excellent | Deep, convincing work with broad technical strength. |
| 7 | Exceptional | Unusually strong and consequential research. |
| 8 | Potentially field-shaping | A result that may materially redirect a field. |
| 9 | Potentially historic | A result that may become a landmark after verification. |
| 10 | Millennium-resolution benchmark | Reserved for an unconditional solution of a recognized Millennium Prize Problem surviving extraordinary independent verification. |

A single model may use 10.00 only as the top anchor defined above. Its output cannot
by itself establish that the benchmark has been met. AIRR must display the underlying
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
published assessment. It orders papers by weighted score, then distinct model count, then
title. Unrated papers remain in the catalogue as `Not yet rated`; zero is never
substituted for missing evidence.

Every current catalogue paper appears in assessment coverage, including accepted,
corrected and historical records. An editorial acceptance does not invent a modern
score. Private candidate preassessments cannot be attached to their public
predecessors. Missing reports are queued for real exact-version assessment.

An editorial highlight is a separate, signed human note explaining why a leading
paper matters, its concrete strengths and its caveats. It cannot alter model reports
or buy ranking position. Corrections and later model assessments remain visible so
future systems can compare how evaluations changed over time.

## Error and appeal procedure

Authors may challenge a report by identifying the exact assessment, claim and
evidence. The original model output remains preserved. AIRR may append an author
response, a new independent assessment, or an editorial adjudication; substantive
changes to the paper require a new version. The editor cannot characterize a
model-detected issue as resolved without a public, concise basis.
