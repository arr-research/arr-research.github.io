# Publication workflow

## 1. Publish a citable working paper

A clean manuscript may enter the public catalogue as `working_paper` after the
depositor authorizes worldwide release of that exact SHA-256 version and chooses
its manuscript license. The record immediately receives its stable AIRR identifier,
immutable version URL and BibTeX, RIS, CSL JSON and plain-text citations. Every
surface must display **Working paper — not admitted to the AIRR accepted
collection** until the admission process is complete.

Public working-paper release is not editorial acceptance. Malware, rights,
impersonation or clearly unlawful-content checks may block publication. Scientific
objections lead to `changes_requested` and a new immutable version, not silent
replacement. Withdrawal leaves a public tombstone because open copies may already
exist.

## 2. Prepare a candidate

Generate the candidate with:

```bash
python scripts/new_record.py --author "Author Name" --type research-paper
python scripts/new_record.py --author "Author Name" --type technical-note
```

This creates `papers/YYYY/MM/PP/ARR-YYYY-<16 characters>/`, stable record/version UUIDs, and the correct shard. The storage path is retained for compatibility, while `record_type` and the public `/papers/` or `/notes/` route determine the publication type. The public repository receives only candidates already approved for publication. Earlier drafts and all future external submissions belong in a separate private intake system.

Research papers use `record_type: research_paper`. Technical notes use `record_type: technical_note` and must additionally declare `kind`, `maturity`, `scope_statement`, and `limitations`. Notes are narrower in scope, not exempt from integrity, provenance, licensing or evidence requirements.

## 3. Complete the research object

Keep the canonical manuscript in `paper.tex`, `paper.md`, or, for a PDF-origin deposit, `paper.pdf`. Always provide `paper.md` as a machine-readable rendition; PDF-origin deposits also require `paper.txt` plus the canonical byte count and SHA-256. Add code, tests and reproducibility files where applicable. Complete `LICENSES.json`, `PROVENANCE.json`, deposit attestations and disclosure fields. Do not commit large generated artifacts; use immutable release assets once the pilot moves beyond small canonical PDFs.

## 4. Validate through a pull request

The pull request runs metadata validation and builds the complete catalogue. Editorial sign-off is represented by approval and merge; it must not be delegated silently to an automated score. `not_assessed` remains visible and is never converted into a pass.

## 5. Publish the version

After merge, run **Create AIRR record release** from GitHub Actions and enter the AIRR identifier. The workflow packages the exact source, calculates hashes and uploads generated or heavy files to a versioned GitHub Release.

## 6. Update the catalogue

GitHub Pages rebuilds from the default branch. Research papers appear under `/papers/`; technical notes appear under `/notes/`. Every record page links to the exact release and source directory. When a custom domain is adopted later, only the Pages domain configuration and canonical URL need to change.

## 7. Correct without erasing history

Create the next version with:

```bash
python scripts/new_version.py ARR-2026-XXXXXXXXXXXXXXXX \
  --change-size minor \
  --summary "Corrects notation and adds a missing reproducibility detail."
```

Use `minor` for corrections, clarifications, metadata repairs and bounded additions that do not replace the central contribution. Use `major` when principal claims, proofs, methods, datasets or conclusions change substantially. Both may produce `v2`, `v3`, and later versions; AIRR deliberately does not use decimal versions.

A major revision must still be recognizably the same evolving work. A different research question or an independent contribution receives a new AIRR identifier and a `related_work`, `companion` or `extends` relation instead of being hidden as a new version.

When an unchanged Working paper completes the admission gate, create its accepted
metadata version with `scripts/admit_working_paper.py`. The command preserves the
canonical PDF bytes and assessment, records a new immutable version identifier and
creates `vN+1` so the earlier Working-paper snapshot and citation remain truthful.
The stable record page then points to the accepted version. If the manuscript itself
changes first, use `new_version.py`; the corrected PDF remains a Working paper until
that exact version passes.

The generator retains the public `id` and `record_id`, creates a new `version_id`, increments `version`, records `supersedes_version_id`, resets version-specific assessments and writes the candidate under `versions/vN/`. Replace or edit the copied research object, recalculate integrity fields and rerun every claimed check. Then repeat PR validation, release and exact-timestamp recording for that version.

The stable page `/papers/{ARR-ID}/` or `/notes/{ARR-ID}/` always displays the latest version. Every source-backed version also has `/versions/vN/`, and every published version has an immutable `{ARR-ID}-vN` release. Never move an existing tag, overwrite a release asset or delete an earlier timestamp entry.
