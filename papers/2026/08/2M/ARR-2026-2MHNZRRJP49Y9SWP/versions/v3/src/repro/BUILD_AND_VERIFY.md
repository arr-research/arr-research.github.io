# Build and verification — working version 0.7 / ARR v3

## PDF build

From the version root, compile the canonical source with three LaTeX passes:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error -jobname=paper paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -jobname=paper paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -jobname=paper paper.tex
```

Check `paper.log` for errors, undefined references, and overfull/underfull
boxes. The deposited PDF was built with MiKTeX pdfTeX 1.40.28 and visually
inspected after rendering all nine pages.

## Exact replays

From the version root:

```powershell
python src/repro/run_all_replays.py
```

The runner executes all three exact replay scripts in a temporary directory
and requires byte-for-byte agreement with the committed JSON evidence. ARR v3
forces LF output through Python's explicit `newline="\n"` file mode, so this
comparison is stable on LF and CRLF host platforms.

Expected final line:

```text
ALL REPLAYS AND COMMITTED RESULTS MATCH
```

## Scope

The build and replays verify compilation, layout, exact finite matrices, and
specified local algebra. They do not replace the universal proofs, Bertini,
human peer review, independent reproduction, Lean certification, or priority
review.
