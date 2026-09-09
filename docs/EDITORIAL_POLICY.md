# AIRR editorial policy — direct private-submission pilot

**Founder-authored rule updated: 2026-09-09 — AIRR-FOUNDER-1.0.**

## Scope

AIRR is a curated archive of research papers and technical notes with preserved canonical artifacts and machine-readable renditions. It is not a journal, and publication does not imply peer review, correctness, novelty or importance. When AIRR publishes a frontier-model assessment, that report describes only the identified model's inspection of the exact identified version.

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
8. an `AI screened: pass` label requires a declared, version-specific frontier-model audit record and no unresolved critical objection; AIRR promises no fixed provider, model or reasoning tier; founder-authored cases require two distinct identified models;
9. a human editor signs off on the exact version;
10. the final decision is tied to stable record/version identifiers, a SHA-256 manifest and protocol version;
11. deposit authority, scoped licenses and third-party material disclosures are recorded.

## Claims AIRR makes

AIRR may state that a particular check passed. It must not convert that result into a broader claim that the record is universally true, novel, important or peer reviewed.

A technical note may later be extended into a research paper. Both records remain persistent and are linked with `extends` and `is_extended_by`; the earlier note is not silently overwritten.

AIRR may publish the model-derived Millennium score and star profile defined in [`MODEL_ASSESSMENT_POLICY.md`](MODEL_ASSESSMENT_POLICY.md). It always exposes the component reports, count, range, version and limitations; it does not turn an aggregate into a correctness certificate.

## Corrections and withdrawals

Published files are not silently replaced. Corrections produce a new version. Withdrawn records retain a tombstone explaining the reason unless legal or safety obligations require a different response.

## Founder conflict

For founder-authored submissions, Lluis Eriksson may sign acceptance after documented review by two identified models. The public record must disclose his author-editor role, the models and their prior involvement, the exact version reviewed and the resolution of material objections. This does not constitute independent human review. Other conflicts and appeals remain subject to the controls in [`GOVERNANCE.md`](GOVERNANCE.md).

## Intake boundary

Direct private submission currently carries no AIRR fee and requires no invitation or author account. Manuscript intake is rate-limited, quarantined and separate from the accepted archive. Any future fee requires advance notice and new terms and cannot purchase an editorial outcome. The public receiver may open only after the operator authorizes the documented reception-readiness record. An independent editor is required for other conflicted final decisions and appeals; the founder-authored exception is defined above. Neither requirement applies to initial receipt of ordinary cases. Submission does not create a right to publication, indefinite storage or evaluation, and no automated system makes the editorial decision.
