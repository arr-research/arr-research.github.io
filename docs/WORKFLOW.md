# Publication workflow

## 1. Prepare a candidate

Copy `templates/paper` into:

```text
papers/YYYY/MM/ARR-YYYY-NNNNNN/
```

The public repository should receive only candidates already approved for the acceptance workflow. Earlier drafts belong in a separate private intake repository.

## 2. Complete the research object

Keep the canonical manuscript in `paper.tex` or `paper.md`. Always provide `paper.md` as a machine-readable rendition. Add code, tests and reproducibility files where applicable. Do not commit large generated artifacts.

## 3. Validate through a pull request

The pull request runs metadata validation and builds the complete catalogue. Editorial sign-off is represented by approval and merge; it must not be delegated silently to an automated score.

## 4. Publish the version

After merge, run **Create paper release** from GitHub Actions and enter the ARR identifier. The workflow packages the exact source, calculates hashes and uploads generated or heavy files to a versioned GitHub Release.

## 5. Update the catalogue

GitHub Pages rebuilds from the default branch. The paper page links to the exact release and source directory. When a custom domain is adopted later, only the Pages domain configuration and canonical URL need to change.

## 6. Correct without erasing history

Copy the accepted record to a new version, update its metadata and sources, and repeat validation. Never move an existing tag or overwrite its manifest.
