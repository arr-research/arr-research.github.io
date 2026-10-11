# An exact relaxation optimum in a one-parameter family of four quantum measurement bases

**Working paper - not admitted to the AIRR accepted collection.**

Lluis Eriksson · ARR-2026-3RH54K4NC58MRSX3 · v2 · 11 October 2026.

Canonical PDF: `paper.pdf`, SHA-256 `58fdb7edfe8b5a663512746326134acf59c97a1108c36f45d634d211aa06c4fb`, eight pages. Editable source: `paper.tex`. The `paper.md` and `paper.txt` renditions are extracted from this PDF; consult the PDF for mathematical typography.

V2 supplies the complete generic overlap derivation, corrects the geometric-optimizer decimal, clarifies the twelve product bases in the sharpness example, and includes the reproducibility material omitted from the v1 public release. It also clarifies frame/vectorization identities, invariant sectors, compression, the spectral-moment comparison and the compactness/equality argument. The principal theorem and one-parameter scope are unchanged. See `RESPONSE-TO-REVIEWS.txt`.

## Reproduce the exact checks

Use Python 3.10 or later and SymPy 1.14.0 (`requirements.txt`). From this directory run `python verify.py`, then `python verify_generic.py`. The scripts overwrite their generated JSON outputs with a fresh timestamp; copy the bundle before rerunning if preserving the deposited outputs is important. They require no network and no floating-point tolerance.

The first script passes 20 exact checks; the second passes 10 generic original-matrix check groups. `verification-summary.json` distinguishes author-assisted reproduction from model review. V1 model reports and ratings remain on v1; any v2 reports are separately registered against this PDF. Publication does not grant human scientific acceptance.

Manuscript: CC BY 4.0. Metadata: CC0. The two verifier scripts: Apache 2.0. Generated results: CC0. Scope and AI-assisted provenance are explicit in `LICENSES.json`, `LICENSES/` and `PROVENANCE.json`. Third-party dependencies are not bundled.
