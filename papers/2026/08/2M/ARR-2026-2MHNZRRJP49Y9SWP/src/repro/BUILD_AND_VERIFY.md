# Build and verification — version 0.6

## PDF build

The canonical source is `manuscript.tex`. Compile with three LaTeX passes:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error -jobname=exact_floor_v06 manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -jobname=exact_floor_v06 manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -jobname=exact_floor_v06 manuscript.tex
```

The release PDF is built with MiKTeX pdfTeX 1.40.28. The build log is checked
for undefined references, LaTeX errors, and overfull/underfull boxes.

## Exact replays

```powershell
python repro/verify_exact_projection_floor.py `
  --output repro/last_exact_projection_floor_v0.6.json
python repro/verify_common_tangent_extremizer.py `
  --output repro/last_common_tangent_extremizer_v0.6.json
```

Expected result: `ALL ASSERTIONS PASSED` for both scripts.

## PDF inspection

All pages are rendered to PNG with Poppler/MiKTeX `pdftoppm` and inspected for
cropping, overlap, unreadable mathematics, missing glyphs, broken links, and
layout defects. `pdfinfo` supplies the page count and `pdftotext` supplies the
preserved text extraction.

## Scope

The build and replays verify compilation, layout, exact finite matrices, and
specified local algebra. They do not replace the universal proofs, Bertini,
human peer review, independent reproduction, Lean certification, or priority
review.
