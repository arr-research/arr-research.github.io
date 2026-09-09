# OpenRouter assessment rounds

AIRR can use OpenRouter to obtain exact-version public model assessments from
models that did not help produce the manuscript. OpenRouter is transport and
routing infrastructure; it does not make the editorial decision.

The runner has two deliberate stages. `plan` writes an immutable manifest under
the ignored `work/openrouter-assessment-rounds/` directory. It fixes every paper,
version, SHA-256 and exact model slug before any result is seen. `run` then sends
every pending pair and preserves its complete response or failure. It never edits
the public registry automatically.

## Create a round

Confirm that the selected model families were not involved in creating the papers.
Use exact, currently available OpenRouter slugs rather than `auto`, `latest` or a
multi-model fallback:

```text
python scripts/openrouter_assessment_round.py plan \
  --round-id 2026-09-founder-public-01 \
  --paper ARR-ID-ONE --paper ARR-ID-TWO \
  --model anthropic/EXACT-MODEL --model qwen/EXACT-MODEL \
  --effort anthropic/EXACT-MODEL=max --effort qwen/EXACT-MODEL=xhigh
```

The command checks the live OpenRouter model catalogue and seals the plan. Do not
edit its manifest. If the scientific selection changes before execution, discard
that unexecuted round and create a clearly named new one.

## Execute

Set `OPENROUTER_API_KEY` only in the process environment or a secret manager. Never
put it in Git, a command committed to shell history, a screenshot or an AIRR paper.

```text
python scripts/openrouter_assessment_round.py run --round-id 2026-09-founder-public-01
python scripts/openrouter_assessment_round.py status --round-id 2026-09-founder-public-01
```

Requests use the public canonical PDF URL, structured JSON output, router metadata,
`data_collection: deny`. The public-assessment route does not require zero-data
retention because it transmits only already-public canonical papers and produces
reports intended for publication; never use it for a private submission. PDFs use native model input
where available and Mistral OCR for a selected model without native file input.
Model substitution and model-level fallbacks are disabled. OpenRouter may fail over
between compliant endpoints serving the same exact model; router metadata preserves
the endpoint actually used. A failed request may be retried only for a
transport or schema error, never because its score was unfavorable.

`run` processes one paid request by default and stops immediately if validation
fails. Increase `--max-requests` only after a complete valid canary from every model
configuration. This prevents an incompatible prompt or provider from multiplying
cost across the batch.

## Editorial import

Inspect every outcome and adjudicate every material objection. A material problem
requires correction/withdrawal handling; do not publish a favorable subset. Import
each valid model-authored JSON using `record_model_assessment.py`, review the diff,
run the repository validation and use the protected GitHub publication flow.

Reports marked `not_involved_in_manuscript` enter the median. Reports marked
`involved_in_manuscript` or `unknown` remain visible but do not affect the ranking.
Different model families reached through one aggregator are distinct evaluations,
but AIRR must not describe them as statistically independent merely because their
names or upstream providers differ.
