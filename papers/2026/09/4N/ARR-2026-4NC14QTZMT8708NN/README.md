# Complete one-state error–delay law — portable source package

Lluis Eriksson, 5 September 2026. Final source edition prepared for ARR-2026-4NC14QTZMT8708NN, version 1. This package itself performs no publication.

Read `active_delay.md` for the self-contained proof and precise scope. OpenAI Codex assisted with derivation, computation, source comparison and drafting. Separate internal reviews use agents in the same model family and are not external or human refereeing. No ARR review score is asserted here.

The manuscript variable `e_opt` is the **squared chordal error**. The public constructor returns `error_squared` and `chordal_error` separately. An inverse target uses either `--error` or `--error-squared`; these options are mutually exclusive.

Reproduce the exact identities, rational active/boundary certificates, radical obstruction certificate, and supplementary numerical constructors:

```text
python -m pip install -r requirements.txt
python verify_active_delay.py
```

Use Python 3.10 or later from this directory. The run writes `active_delay_certificate.json` beside the script. It retains every earlier forward replay and adds seven inverse symbolic groups, four exact fixtures, six exact target-boundary checks, an isolated nonrational cubic and twelve numerical forward/inverse round trips. It performs no network access, SDP solve, frequency grid, publication or external contact.

Construct the two-port coefficients for a specified rational or decimal input:

```text
python verify_active_delay.py --construct --u 3 --v 1/3 --T 2
```

For T>=1, `p_z`, `q_z`, and `h_z` are coefficient arrays in ascending powers of z; combine them by manuscript equation (23), with `completion_degree=1`. For T<1 the output instead contains the constant matrix `S_constant`, `completion_degree=0`, and peak zero. Use that matrix directly. Applying the degree-one sharp operation to the constant branch would create a spurious delay-one factor.

Compute minimum delay and an attaining router from a squared target, or from a chordal target:

```text
python verify_active_delay.py --minimum-delay --u 2 --v 1 --error-squared 35/123
python verify_active_delay.py --minimum-delay --u 2 --v 1 --error 1/2
```

These commands intentionally have different targets. The first targets squared error 35/123 and gives minimum delay approximately 1.7937395977414851561. The second targets squared error 1/4. Squared targets at least 1/2 permit a constant router. Targets from `e_1` up to values below 1/2 require minimum delay exactly 1; the returned router may beat the target there. Target zero is reported as unattainable at any finite delay.

For rational positive u,v and a rational squared target, obtain an exact inverse certificate:

```text
python verify_active_delay.py --inverse-certificate --u 2 --v 1 --error-squared 1/4
```

This mode uses exact rational branch comparisons and a rational isolating interval for the unique admissible cubic root. It returns exact coefficient and minimum-delay expressions. If `y` appears, it means precisely the root in the returned interval. Rational roots, the active phase and target boundaries simplify without an unresolved root. A rational `--error` target is squared exactly first. The certificate implements Theorem 2 and is not a proof-assistant check.

Numerical modes use 90-digit arithmetic and report decimal coefficients and near-boundary phase labels. They are numerical realizations of the proved recipes, not an arbitrary-input interval-arithmetic API. The exact inverse mode avoids floating-point branch decisions. Exact forward certification uses the displayed radicals or isolated unsquared quartic root and the proved positivity and functional identities.

The optional `check_math_rendering.py` requires Matplotlib and parses the LaTeX formulas for the compositor. It generates no PDF or image. No exploratory solver or one-time source-conversion script is needed.

`evidence/cycle2/` and `evidence/cycle3/` preserve earlier manuscripts, scripts, certificates and separate internal review byte for byte. Historical workspace paths in those frozen records are provenance labels, not runtime dependencies; portable counterparts are in the named evidence directories. The cycle-3 review applies to its frozen source hash. `final_independent_review.md` records the separate final review with outcome PASS, including the inverse and PDF correspondence. Its independent inverse checker passes 74 exact Sturm cases and four exact fixtures, without importing the deriving verifier. `independent_review_checks.py` separately repeats the earlier forward checks against the final source. The JSON records identify source and PDF hashes. Replaying an evidence script writes a new result beside it; retain the supplied certificate if its original hash matters.

`CHANGELOG.md` states the final delta. `changes_from_cycle3.diff` compares the manuscript and verifier with the reviewed edition. `source_manifest.json` lists hashes and original reviewed identities. Run `python refresh_manifest.py` after a deliberate final edit to refresh the diff and manifest; it does not modify mathematical evidence or publish anything.

New mathematical structure relative to the inspected cycle-2 corpus: a complete two-branch law for positive cotangents u,v, one finite positivity transition exactly when max(u,v)>3 min(u,v), an explicit active formula with pinned denominator coefficient, a positive dual certificate and a two-port construction. External priority is not established. The dimensionless angular model does not by itself synthesize laboratory circuit components or calibrate physical time.


## Published assets and safe replay

ARR releases the canonical PDF separately from the source ZIP. Extract the sources and save the separate PDF in that directory as `paper.pdf` before checking the complete `MANIFEST.sha256`. The canonical PDF hash is also recorded in metadata.json. `paper.md` contains all machine-readable mathematics; ordinary extraction into `paper.txt` omits embedded formula images.

Verify the supplied hashes before running the scripts. Scientific replays write result JSON files, sometimes including runtime measurements, so run them in a working copy if you wish to preserve the deposited certificates and their hashes. A different elapsed time does not alter an exact mathematical result. The final, version-specific internal report is in `screening/final-internal-review.md`; the author-editor decision and pending subsequent Astra review are documented separately. `AUDIT_PROMPT_ASTRA.md` is ready for that future review and contains this PDF's exact identity.

The final reviewer's separate scientific replays are `python inverse_independent_checks.py` and `python independent_review_checks.py`, using SymPy. Their scope and execution are recorded in the final internal report. CHECKPOINT.md records the preparatory stage; the final status is in screening/ and metadata.json.
