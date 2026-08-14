# Publication workflow

## 1. Prepare a candidate

Generate the candidate with:

```bash
python scripts/new_record.py --author "Author Name" --type research-paper
python scripts/new_record.py --author "Author Name" --type technical-note
```

This creates `papers/YYYY/MM/PP/ARR-YYYY-<16 characters>/`, stable record/version UUIDs, and the correct shard. The storage path is retained for compatibility, while `record_type` and the public `/papers/` or `/notes/` route determine the publication type. The public repository receives only candidates already approved for publication. Earlier drafts and all future external submissions belong in a separate private intake system.

Research papers use `record_type: research_paper`. Technical notes use `record_type: technical_note` and must additionally declare `kind`, `maturity`, `scope_statement`, and `limitations`. Notes are narrower in scope, not exempt from integrity, provenance, licensing or evidence requirements.

## 2. Complete the research object

Keep the canonical manuscript in `paper.tex`, `paper.md`, or, for a PDF-origin deposit, `paper.pdf`. Always provide `paper.md` as a machine-readable rendition; PDF-origin deposits also require `paper.txt` plus the canonical byte count and SHA-256. Add code, tests and reproducibility files where applicable. Complete `LICENSES.json`, `PROVENANCE.json`, deposit attestations and disclosure fields. Do not commit large generated artifacts; use immutable release assets once the pilot moves beyond small canonical PDFs.

## 3. Validate through a pull request

The pull request runs metadata validation and builds the complete catalogue. Editorial sign-off is represented by approval and merge; it must not be delegated silently to an automated score. `not_assessed` remains visible and is never converted into a pass.

## 4. Publish the version

After merge, run **Create ARR record release** from GitHub Actions and enter the ARR identifier. The workflow packages the exact source, calculates hashes and uploads generated or heavy files to a versioned GitHub Release.

## 5. Update the catalogue

GitHub Pages rebuilds from the default branch. Research papers appear under `/papers/`; technical notes appear under `/notes/`. Every record page links to the exact release and source directory. When a custom domain is adopted later, only the Pages domain configuration and canonical URL need to change.

## 6. Correct without erasing history

Create a new version with the same `record_id` and public `id`, a new `version_id`, an incremented `version`, and `supersedes_version_id`. Repeat validation. Never move an existing tag or overwrite its manifest.
