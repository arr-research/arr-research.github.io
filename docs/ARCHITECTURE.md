# ARR architecture

## Purpose

ARR separates the lightweight public catalogue from the potentially heavy research artifacts.

### Git history

Git stores files that benefit from inspection and version history:

- canonical LaTeX or Markdown manuscripts;
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

### GitHub Pages

The static site contains only HTML, CSS, JSON and NDJSON catalogue files. Paper pages link to Git sources and Release assets rather than copying heavy files into the website deployment.

### Future preservation

GitHub is the operating surface, not the sole preservation authority. Accepted releases can later be mirrored to Software Heritage, Zenodo or another preservation service without changing the authoring workflow.
