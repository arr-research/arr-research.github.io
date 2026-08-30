# ARR-2026-5QQF95VHTC9GABH8

Canonical research paper: `paper.pdf`. Canonical manuscript source:
`paper.tex`.

This record preserves the exact PDF, LaTeX and BibTeX sources, machine-readable
text renditions, and the complete 88-file reproducibility tree. The latter
contains canonical and independent exact Horn/polyhedral checks, frozen JSON
certificates, symbolic hive coarse-graining checks, an independent dictionary
implementation, and the vendored optional `cddlib` route with upstream license
metadata.

Install the pinned Python dependencies and run the complete default replay:

```text
python -m pip install -r src/repro/requirements.txt
python src/repro/run_scientific_replay.py
```

The replay verifies the universal threshold through dimension seven, the sharp
dimension-eight obstruction, the dimension-nine seed, exact order-18 and
order-27 hive certificates, and the symbolic unbounded-excess transfer. It is
not proof-assistant certification, exhaustive priority adjudication, or peer
review. The author is also ARR's founder-editor.
