# ARR state and evidence model

Submission state and public record status are deliberately separate. A submission is not an ARR publication.

## Private intake states

`received → quarantined → eligible → under_assessment → accepted_for_publication`

Terminal alternatives are `declined`, `expired`, `removed`, and `legal_hold`. Intake states are private operational data and must not be presented as quality labels.

## Public record statuses

- `accepted`: first public version.
- `corrected`: a new version that identifies `supersedes_version_id`.
- `withdrawn`: a persistent tombstone; files are retained unless law or safety requires removal.

## Public record types

- `research_paper`: a paper-scale research contribution.
- `technical_note`: a concise, explicitly bounded technical contribution. Schema 1.1 requires a note kind, maturity, scope statement and limitations.

Schema 1.0 records predate this distinction and are interpreted as `research_paper`; their published metadata is not rewritten. Type and status are independent: for example, a technical note can be accepted, corrected or withdrawn.

## Independent evidence labels

Labels report evidence, not a single quality score:

- **Source integrity:** required for every public record.
- **AI screened:** only when at least three declared, version-specific evaluator reports passed with no unresolved critical objection.
- **Computationally reproduced:** only when the declared commands ran successfully in a pinned environment.
- **Lean L0–L3:** reports source supplied, build status, kernel/axiom audit, and manuscript correspondence at increasing levels.
- **Human reviewed:** only when the scope and reviewer role are disclosed.

`not_assessed` is a valid and visible result. It must never be rendered as failure or pass. ARR acceptance does not imply truth, novelty, importance, peer review, or correctness beyond the checks explicitly recorded.

State transitions will become append-only registry events when ARR leaves the Git pilot. The metadata schema already uses stable record and version identifiers so that migration does not alter public citations.
