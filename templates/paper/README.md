# ARR research-record package

This directory is a template, not a published ARR record.

Required publication files:

- `metadata.json`
- `paper.tex`, `paper.md`, or a hash-identified `paper.pdf` as the declared source of truth
- a machine-readable `paper.md`
- `paper.txt` for PDF-origin records
- `PROVENANCE.json`
- `CITATION.cff`
- `LICENSES.json` with machine-readable scope and SPDX identifiers
- `references.bib` for LaTeX manuscripts
- `LICENSES/` containing the applicable license texts

Optional reproducibility material belongs under `src/`, `tests/`, `data/`, and `expected-results/`. Generated PDFs and large datasets are release assets and should not be committed to Git.

Do not invent an identifier by hand. Run `python scripts/new_record.py --author "Name" --type research-paper` or `--type technical-note`; the generator creates a concurrent-safe record UUID, version UUID, public ID, and sharded path. Technical notes must complete the generated `technical_note` profile before publication.

For `v2`, `v3`, and later, do not copy this template and do not create a new ARR identifier. Run `python scripts/new_version.py ARR-... --change-size minor|major --summary "..."` so the predecessor link, new version UUID, assessment reset and `versions/vN/` path are generated consistently.
