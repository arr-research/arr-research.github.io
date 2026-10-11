# Protocol-reconciled final assessment: ARR-2026-3RH54K4NC58MRSX3, version v2

**Title:** An exact relaxation optimum in a one-parameter family of four quantum measurement bases
**Version identifier:** `arr:version:bc5c9f23-b39f-49a1-901c-16f499937caf`
**Canonical PDF (unchanged), SHA-256:** `58fdb7edfe8b5a663512746326134acf59c97a1108c36f45d634d211aa06c4fb` (8 pages, 371,738 bytes)
**Assessed at:** 2026-10-11T19:24:44+02:00
**Reviewer:** Anthropic `claude-opus-5-5`, the same referee session as the full audit and the final correction check. Independence: `involved_in_manuscript`.

## Final verdict

| Question | Answer |
|---|---|
| Is the paper scientifically correct? | **Yes.** All main claims were verified. No error, no compulsory correction and no material objection remains. |
| Is it scientifically suitable for release as a narrow working paper? | **Yes**, in my judgment. Licensing and release actions are outside my assessment and remain pending. |
| Does it meet AIRR's substantive-admission floor (3.00, "acceptable and substantive")? | **No.** My AIRR score is **2.6** (3 stars), unchanged. |
| Native AIRR recommendation | **`major_revision`**, used *only* in AIRR's admission sense: admission to the accepted collection would require a substantive extension of scope, not minor edits. It is **not** a claim of error and **not** a compulsory correction. |
| Ordinary grade | **6.0 / 10**, unchanged (Section 4). |

**Limitation of the categories.** No single native category faithfully expresses this judgment by itself. The four categories combine scientific soundness and admission level in one label, while my verdict is "sound, but below the admission floor". I state this explicitly rather than choosing a label that hides either half. Section 2 explains why `major_revision` is the least unfaithful choice.

## 0. Scope and provenance of this addendum

- **Administrative only:** no manuscript or scientific input changed.
  - The ten carried-over files are byte-identical to the final-candidate packet: `paper.pdf`, `paper.tex`, both verifiers, `requirements.txt`, the three dated outputs, `changes.diff` and `airr-rubric.txt` (`admin_checks/hash_comparison.log`).
  - New inputs read: `protocol-clarification.txt` and `request.txt`.
  - No mathematical rerun and no literature search was performed or needed.
- **This addendum relies explicitly on two immutable earlier deliverables from this session, both hash-verified unchanged:**
  - **Full audit** of the prior candidate `3c60aee3…`: `../../report.md` (`3b687f3c013cd5889ee907b3f42c3fa1395100d68736b5880cfc8caff007867c`), `../../assessment.json` (`0aad6c8ebf2497042f5b25834d61e6bf091df98a712a7ae46336c95fb2a9db93`), and scripts and logs in `../../referee_work/`.
  - **Final correction check** of this PDF: `../report.md` (`88fe067c1009cb580230c7d932fa28862c6c3ebd00dea81b1075589ac50b89ba`), `../assessment.json` (`b4910f568793c080a18ccc90bb2aff1fd49885dc487b382051e36a48182ad318`), and `../followup_checks/`.
- **How the new `assessment.json` was built:** its scientific fields (criteria and bases, strengths, weaknesses, potential errors, novelty candidate, material objections, score and stars) were copied **verbatim and programmatically** from `../assessment.json`, which was read and not modified. Only `recommendation`, `assessed_at` and `summary` changed (`admin_checks/build_assessment.log`).
- **Validation:** the new file passes the rubric template and the native validator rules quoted in `protocol-clarification.txt` (`admin_checks/validate.log`).
- **Controls:** no other review was read, and no credentials, configuration, git, publication, messages or agents were used. No human acceptance and no technical isolation is claimed.

## 1. The protocol issue

The native validator accepts recommendations in {accept, minor_revision, major_revision, reject} and rejects `accept` unless `millennium_score >= 3.00` and `overall_stars >= 3`. My final-correction-check assessment paired `accept` with 2.6 and was therefore rejected at import.

The generated rubric I was given described 3.00 as "acceptable and substantive" but did not state the gate. The clarification also states that working-paper release and admission to the accepted collection are distinct states. I accept the operator's description that this was an omission in the generated rubric, not a scientific error.

I also own my part. My earlier recommendations were expressed in conventional journal-referee semantics, where the recommendation follows required corrections:
- **Full audit:** `minor_revision`, driven solely by two small required fixes.
- **Final check:** `accept`, once those fixes were made.

I had myself described 2.6 as "somewhat less substantive than the 3.00 anchor". Under native admission semantics, both earlier labels therefore conflicted with my own score, and I should have flagged that tension rather than resolving it silently in the conventional sense.

## 2. Reconciliation

**The score is re-examined and not changed.** I did not raise 2.6 to clear the gate, and I found no reason to lower it.
- The contribution is a correct, exact, fully reproducible calculation on a known family: the complete spectrum of the Raynal–Lü–Englert (RLE) one-parameter subfamily and its sharp equal-weight optimum 73/100.
- Its originality and significance are modest:
  - it is a one-dimensional optimization of a max of five quadratics using the standard frame/Gram method;
  - the gain over RLE's distance optimizer is 0.216%;
  - the equal-weight optimum is exceeded by reweighting the same bases ((27,25,25,25)/102 gives 25/34);
  - the two-parameter and global questions remain open;
  - the 3/4 bound with its MUB equality case is Zhu–Hayashi's g-setting result;
  - the 2/3 product ceiling is elementary.
- That is "acceptable" but below "acceptable and substantive".

**Mapping to the native categories:**
- **`accept`:** inconsistent with my own 2.6 under the 3.00 admission floor. Clearing the floor would require a score I do not believe.
- **`minor_revision`:** would imply that small edits lead to admission. No compulsory correction remains. The recommended additions (stating that equal weights are binding; developing the verification-gap equivalence) would improve the paper, but in my judgment would not lift it to 3.00.
- **`reject`:** would misrepresent a scientifically sound paper that is suitable as a working paper, and would deny a plausible route to admission.
- **`major_revision`:** consistent with the admission verdict and with such a route. Admission would need a substantive extension of scope, which is the author's option and is **not required** for scientific soundness or working-paper release. Examples that I judge could plausibly reach the floor, though I cannot promise that without a new assessment:
  1. a proof that u = 7/10 is optimal over the **full two-parameter RLE family** (my bounded scan found no better point; numerical evidence only);
  2. the **optimal measurement probabilities** within the family (25/34 is attained; a numerical probe found nothing better; optimality over all weights is unproven);
  3. developing the exact equivalence with **Zhu–Hayashi verification of the 6×6 maximally entangled state** into an application, positioned against other four-setting constructions in d = 6;
  4. written derivations of the **branch equivalence** (numerically confirmed: identical overlap blocks on all eight arcs) and the **block placement** in Eq. (11).

## 3. Preserved scientific findings (unchanged; verbatim in `assessment.json`)

- **Verified correct:**
  - Theorem 3.1 (complete Gram spectrum, identically in u on [1/4,1]);
  - Theorem 4.1 (73/100, uniquely at u = 7/10, for equal probabilities and unit rate);
  - Corollary 4.2;
  - Eqs. (16)–(18) and Table 1, including agreement with RLE's closed forms;
  - Proposition 5.1 (2/3 product-vector ceiling, sharp via the 12-basis example);
  - the bounds 73/100 ≤ γ*₄(6) ≤ 3/4, with equality iff four MUBs exist.
- **Reproducibility:** both author verifiers regenerate their dated outputs field-for-field, and the corrected docstring is accurate.
- **Weaknesses (all preserved):**
  - the contribution is narrow;
  - the binding equal-weight restriction is not discussed;
  - prior art is understated (Zhu–Hayashi verification gap and g-setting bound);
  - the product ceiling is elementary;
  - branch equivalence is asserted without proof;
  - the block placement in (11) is delegated;
  - the two-parameter family is not analyzed.
- **Potential error (preserved):** the RLE equation numbers were verified against arXiv:1103.1025v1 only.
- **Novelty candidate (narrow):** the closed-form spectrum and the sharp equal-weight optimum on the RLE subfamily.
- **Unresolved material objections:** none.

## 4. Grades (unchanged)

**AIRR:**

| Field | Value |
|---|---|
| millennium_score | **2.6** (overall_stars 3), below the 3.00 admission floor |
| correctness_confidence | 5/5 |
| rigor | 4/5 |
| novelty | 2/5 |
| significance | 2/5 |
| reproducibility | 5/5 |
| recommendation | `major_revision` (admission sense only; see Final verdict and Section 2) |

**Ordinary 0–10 grades (separate scale):**

| Criterion | Grade |
|---|---|
| Correctness | 10.0 |
| Originality | 4.0 |
| Significance | 3.5 |
| Clarity | 8.5 |
| **Overall** | **6.0** |

The overall grade weights originality and significance more heavily (0.3/0.3/0.2/0.2), which gives about 5.95.

The two scales are consistent. On the ordinary scale, 6.0 means a sound short note of modest originality and significance, suitable for a specialized venue or as a working paper. On the AIRR comparison scale, 2.6 places the same work just below the archive's "acceptable and substantive" admission anchor.

## 5. Limits

- This addendum performed no new mathematics or literature work. All scientific statements rest on the two earlier deliverables listed in Section 0, with the limits stated there:
  - numerical scans are not proofs;
  - the literature search was focused and not exhaustive;
  - the published PRA versions were not accessed;
  - the runtime configuration and context isolation cannot be verified.
- The recommendation category is used in AIRR's native admission sense as defined in `protocol-clarification.txt`. Readers should rely on the Final verdict table, not on the single label.

## 6. Files in this directory

- `assessment.json`: new, validated against the rubric and the native rules.
- `report.md`: this file.
- `admin_checks/`:
  - `hash_comparison.log`: input identity and hashes of prior deliverables;
  - `build_assessment.py` and `.log`: verbatim field copy;
  - `validate.py` and `.log`: rubric and native validator checks.
