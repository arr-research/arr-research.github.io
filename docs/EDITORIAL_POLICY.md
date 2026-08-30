# ARR editorial policy — direct private-submission pilot

## Scope

ARR is a curated archive of research papers and technical notes with preserved canonical artifacts and machine-readable renditions. It is not a journal, and publication does not imply peer review, correctness, novelty or importance. When ARR publishes a frontier-model assessment, that report describes only the identified model's inspection of the exact identified version.

## Publication types

- **Research paper:** a paper-scale scholarly argument with its question, method, principal results, limitations and supporting research object.
- **Technical note:** a narrower research communication such as a result, proof, formalization, computation, replication, negative result, method, data description, software contribution or protocol. It must state its contribution boundary, maturity and limitations explicitly.

Technical notes are not a lower-integrity channel. They may be shorter or narrower, but the same authorship, rights, source-integrity, provenance, licensing, disclosure and evidence-label rules apply. The record type must remain visible in the catalogue and citation context.

## Acceptance standard

A record may be accepted only when:

1. its authorship, rights, licenses and AI-assistance statement are complete;
2. the canonical manuscript and machine-readable rendition are present;
3. citations and key factual dependencies have been checked under the applicable protocol;
4. code, data descriptions and formal proofs needed to support the stated result are supplied when applicable;
5. automated checks succeed;
6. every performed assessment is labelled with its actual outcome and legacy `not_assessed` records remain visible rather than being retrospectively scored;
7. new admissions under ARR-ASSESS-1.0 require declared, version-specific frontier-model screening, and any unresolved material objection blocks acceptance pending correction or a signed human adjudication;
8. an `AI screened: pass` label requires three declared, version-specific evaluator reports and no unresolved critical objection;
9. a human editor signs off on the exact version;
10. the final decision is tied to stable record/version identifiers, a SHA-256 manifest and protocol version;
11. deposit authority, scoped licenses and third-party material disclosures are recorded.

## Claims ARR makes

ARR may state that a particular check passed. It must not convert that result into a broader claim that the record is universally true, novel, important or peer reviewed.

A technical note may later be extended into a research paper. Both records remain persistent and are linked with `extends` and `is_extended_by`; the earlier note is not silently overwritten.

ARR may publish the model-derived Millennium score and star profile defined in [`MODEL_ASSESSMENT_POLICY.md`](MODEL_ASSESSMENT_POLICY.md). It always exposes the component reports, count, range, version and limitations; it does not turn an aggregate into a correctness certificate.

## Corrections and withdrawals

Published files are not silently replaced. Corrections produce a new version. Withdrawn records retain a tombstone explaining the reason unless legal or safety obligations require a different response.

## Founder conflict

When an editor, founder or operator is also an author or directly conflicted, that relationship is visible and his acceptance is provisional. A named, unconflicted independent editor must sign the exact version before publication. Editors cannot decide their own submissions, and appeals do not return to the sole original decision-maker. The binding controls are in [`GOVERNANCE.md`](GOVERNANCE.md).

## Intake boundary

Direct private submission currently carries no ARR fee and requires no invitation or author account. Manuscript intake is rate-limited, quarantined and separate from the accepted archive. Any future fee requires advance notice and new terms and cannot purchase an editorial outcome. The public receiver may open only after the production launch checklist is signed. Submission does not create a right to publication, indefinite storage or evaluation, and no automated system makes the editorial decision.
