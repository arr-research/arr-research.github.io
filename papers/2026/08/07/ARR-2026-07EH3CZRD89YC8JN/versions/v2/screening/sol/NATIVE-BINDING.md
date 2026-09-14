# Native administrative intake binding

This addendum binds the completed OpenAI `gpt-5.6-sol` scientific assessment to the actual private intake case `SUB-ADD76F3A7B0B4967`. The intake receipt records `2026-09-14T06:13:22Z`, clean and eligible. The received manuscript has SHA-256 `341c673d6613533931cbc0fc817cf946d178e390cde818221c19b33c304a4167`, identical to the manuscript reviewed in the preserved sixth-candidate assessment.

This is an administrative same-model, same-hash follow-up. It does not repeat or extend the scientific review. Prior involvement remains declared as `involved_in_manuscript`. The scientific recommendation remains `accept`, the Millennium score remains `4.4`, and `overall_stars` remains `4`, rounded on the intake schema's 0-10 overall scale. Criterion stars remain on their separate 1-5 scales.

## Time binding

- Original scientific review timestamp: `2026-09-13T20:11:37.1158404+02:00`.
- Administrative binding timestamp: `2026-09-14T08:16:55.7984704+02:00`.
- Intake receipt timestamp: `2026-09-14T06:13:22Z`.

The `assessed_at` value in `intake-assessment.native.json` preserves the original scientific review timestamp. The newer administrative timestamp is recorded here so the binding action is not misrepresented as a new scientific assessment.

## Preserved native evidence

- Original assessment JSON SHA-256: `fcb89725e4f1e19e6542d3b63253994700b47da4fe0922dd56cecbe1b5856324`.
- Original referee report SHA-256: `3fa8bcf1e9b38da6e51527a6d6a0ce171ebd2d51fe0f6e4dec1f19bf658b4051`.
- Original checks SHA-256: `63ceedaa9b6c63a07d0dce709fc596839366e048de978ba473ef36d5bdf5795f`.
- Original clarification JSON SHA-256: `47efd712552a9fed86c91cbd680b6109153efb0923ee6fba636283ef98b6fa7b`.

Those native files remain unchanged. The exact manuscript hash was rechecked immediately before creating this addendum and still matched.

## Intake-schema mapping

The intake template is exact and does not permit additional keys. The administrative native JSON therefore applies these schema mappings:

- `score` becomes `millennium_score` with the unchanged value `4.4`.
- `submission_id` uses the actual intake case identifier. The prior assessment's `paper_id` and `candidate_id` are omitted because the intake template has no such fields; the candidate remains `f9a95623-ad1e-4174-9b32-dec9d2dcbe5d`.
- `required_corrections` is omitted because the intake template has no such field. Its preserved value and the clarification's effective value are both empty.
- The original summary and one novelty finding are wording-corrected according to `clarification.json`: the family is within **at most** six states of the unknown optimum, since the proof gives `3S <= n_min <= 3S+6`.
- The five allowed findings arrays preserve the original scientific findings. No unresolved material objection has been added or removed.

Template SHA-256: `617e363169d3fb8123abe20659c8add61791d94d087c622ef7c6c93b85d7f651`. Validator source SHA-256: `1087da21d37f39e3e687780688ab2145b8ab18a8fc8ebfba22ba09ec9057ff0e`.

This model recommendation is not a human editorial acceptance, publication authorization, public release, or submission action. No publication or submission was performed by this addendum.
