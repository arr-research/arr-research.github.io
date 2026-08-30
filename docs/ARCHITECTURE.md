# ARR architecture

## Purpose

ARR separates private intake, the lightweight public registry projection, and potentially heavy research artifacts.

### Private intake

Untrusted submissions must never arrive through pull requests to the accepted archive. The direct private service in `services/intake/` accepts author uploads without an account, while editor access uses password plus TOTP. It applies CSRF, bot and persistent IP/email rate controls, non-public quarantine storage, retention deadlines and fail-closed malware checks. Rejected or expired intake data can be deleted without altering the public record. The service cannot write to `papers/` or create releases.

### Git history

Git stores files that benefit from inspection and version history:

- canonical LaTeX or Markdown manuscripts during the pilot;
- machine-readable Markdown and plain text;
- Lean and Python source;
- metadata, provenance and citation files;
- compact tests and small data fixtures;
- editorial protocol and validation code.

Generated PDFs, full source bundles, large datasets and build logs should not inflate Git history. The release workflow builds a PDF from canonical LaTeX in its temporary runner and uploads the result without committing it.

### GitHub Releases

Each accepted version receives a tag named `{ARR-ID}-{version}` and a GitHub Release containing:

- the PDF, when available;
- a ZIP snapshot of all source files;
- `MANIFEST.sha256`;
- the exact metadata record;
- optional large data or reproducibility artifacts.

Release URLs remain version-specific. A correction creates a new version and tag.

The first source snapshot remains at the record root for backward compatibility. Later source-backed versions are stored under `versions/vN/`. The stable public record URL resolves to the latest version, while `/versions/vN/` pages and `{ARR-ID}-vN` releases remain permanent. Older release-only versions may appear in the history even when their Git snapshot predates this layout.

### GitHub Pages

The static site contains only HTML, CSS, JSON and NDJSON catalogue files. Paper pages link to Git sources and Release assets rather than copying heavy files into the website deployment.

### Future preservation

GitHub is the pilot operating surface, not the permanent database or sole preservation authority. Stable `record_id` and `version_id` values do not contain a GitHub URL. Accepted releases can later be stored under provider-independent object keys and mirrored to Software Heritage, Zenodo or another preservation service without changing citations.

At public-service scale, PostgreSQL becomes the authoritative metadata registry, object storage holds artifacts, queue workers perform isolated processing, and the static catalogue becomes a rebuildable projection. See `SCALE_READINESS.md`.
