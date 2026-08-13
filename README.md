# ARR — Archive for Rigorous Research

ARR is a curated, source-first archive for research that has passed a documented screening and verification protocol.

This repository is the technical foundation for the archive. It keeps lightweight, inspectable sources in Git and publishes large generated artifacts—PDFs, complete source bundles, datasets, and build logs—as GitHub Release assets.

## Current status

ARR is in its private prototype phase. No paper is considered published merely because it appears in a branch or pull request. A paper becomes an ARR publication only after the acceptance workflow completes and a versioned release is created.

## Local checks

```bash
python scripts/validate_papers.py
python scripts/build_site.py
python -m http.server 8000 --directory _site
```

## Repository layout

```text
papers/                 Accepted paper sources, grouped by year and month
templates/paper/        Template for a new candidate
schema/                 Machine-readable metadata contract
scripts/                Validation, packaging and site generation
site/                   Static presentation assets
docs/                   Editorial and operational documentation
.github/workflows/       GitHub validation, Pages and Release automation
```

See [docs/WORKFLOW.md](docs/WORKFLOW.md) for the publication procedure.
