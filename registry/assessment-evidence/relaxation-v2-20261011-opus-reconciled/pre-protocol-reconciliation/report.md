# Final follow-up referee report: ARR-2026-3RH54K4NC58MRSX3, version v2 (final candidate)

**Title:** An exact relaxation optimum in a one-parameter family of four quantum measurement bases
**Version identifier:** `arr:version:bc5c9f23-b39f-49a1-901c-16f499937caf`
**Assessed artifact (final canonical PDF, SHA-256):** `58fdb7edfe8b5a663512746326134acf59c97a1108c36f45d634d211aa06c4fb` (8 pages, 371,738 bytes)
**Previously fully audited candidate:** `3c60aee3179b0f8d9c7a07960b7b600cca8cac70b5898f710676d8d124ea25ae`
**Rubric / prompt version:** ARR-ASSESS-1.0
**Assessed at:** 2026-10-11T19:15:20+02:00

**Recommendation:** `accept`. There are no unresolved material objections. This is a model recommendation, not human editorial acceptance, and the candidate remains unpublished.
**AIRR `millennium_score`:** 2.6 (`overall_stars` 3)
**Ordinary overall grade:** 6.0 / 10 (Section 7)

---

## 0. Nature of this report, reviewer and controls

- **Type:** a *limited final follow-up* in the same referee session as my full audit of the prior candidate `3c60aee3…25ae`, not an independent new referee.
  - **Newly done here:** verified the final hash, the exact source and script changes, the corrected sentence and the regenerated outputs. Also ran one small new targeted check (Section 3.4).
  - **Reused:** for all unchanged material I rely on my earlier full audit, which is preserved unchanged in the parent directory:
    - `../report.md`, SHA-256 `3b687f3c013cd5889ee907b3f42c3fa1395100d68736b5880cfc8caff007867c`;
    - `../assessment.json`, `0aad6c8ebf2497042f5b25834d61e6bf091df98a712a7ae46336c95fb2a9db93`;
    - scripts and logs in `../referee_work/`, hashed in `../referee_work/MANIFEST.txt`.
  - **Not repeated:** I did not rerun every unchanged numerical calculation and did not run new broad literature searches. I found no reason to; the unchanged material is byte-identical (Section 1).
  - **Earlier deliverables:** I hashed my earlier report and assessment for provenance but did not reopen them. Their content is my own work from this session.
- **Provider / model:** Anthropic, `claude-opus-5-5` (Claude Opus 5.5), in the Claude Code / Agent SDK harness. The operator requested the "max" effort configuration; I cannot independently inspect that runtime setting.
- **Independence:** `involved_in_manuscript`. The operator declares this, and the manuscript states that Claude Opus 5.5 gave v1 advisory feedback that informed the revision. I also performed the full audit whose two required corrections this candidate implements. No technical isolation is claimed.
- **Files read in `final-candidate/`:**
  - `airr-rubric.txt` (locks the final hash);
  - `request.txt` (identical in substance to the operator's message);
  - `changes.diff`;
  - the eight scientific inputs: `paper.pdf`, `paper.tex`, `verify.py`, `verify_generic.py`, `requirements.txt`, `verification.json`, `generic-verification.json` and `exact-gram.json`.
- **Other files compared:** the prior-candidate packet in the parent directory, which is my own review material and was confirmed unchanged against the hashes recorded in my full review.
- **Not read:** other reviews, sibling directories and session streams. No messages, git, publication, credentials or purchases.
- **Input integrity:** all final-candidate inputs were re-hashed after the checks and are unchanged. New work is confined to `final-candidate/followup_checks/`.
- **Software:** Python 3.12.6, SymPy 1.14.0, NumPy 2.5.1, pypdf 6.4.0.

## 1. What changed between the audited candidate and the final candidate (verified)

| Item | Finding | Evidence |
|---|---|---|
| Final PDF | SHA-256 `58fdb7ed…c4fb`, 8 pages, 371,738 bytes; matches the request and the rubric lock | `sha256sum`, pypdf |
| `paper.tex` | Exactly one changed line (line 79, p. 2 sentence); new hash `b9517611…9ad8` | Independent `diff -u` against the prior `paper.tex` (`3e7a8540…faec`); identical to `changes.diff` |
| `verify_generic.py` | Exactly one changed docstring line (line 5). **Executable code is syntax-tree-identical** to the audited version once docstrings are removed. New hash `4ce92f2b…8fe5` | `diff -u`; `followup_checks/compare_candidates.py` |
| `verify.py`, `requirements.txt`, `exact-gram.json` | Byte-identical to the audited packet | `cmp`; hashes `a1a367b2…`, `25f9f1fb…`, `d3df9db5…` |
| PDF text | Only page 2's extracted text differs. The word-level difference is exactly the edited sentence. The only other PDF difference is the timestamp metadata (Creation/ModDate 18:29:06 → 18:50:11 +02:00) | Per-page pypdf comparison; rendered page 2 viewed |
| Dated author outputs | Regenerated (16:50:18Z and 16:50:23Z). Versus the prior candidate's outputs only `files_sha256` changed (new `paper.tex` / `verify_generic.py` hashes). Checks, results and probability blocks are identical | `followup_checks/compare_outputs.py` |

The author's description ("exactly two localized edits … no theorem, proof computation, executable verifier code, reference, or other manuscript text changed … only PDF page 2 has changed extracted text") is **confirmed**.

## 2. The two corrections

**R1. Page-2 sentence (required in my full review): resolved.**
- **Old:** "Its nonzero eigenvalues agree with those of G, including multiplicity." This was false if "Its" meant the full channel ¼Σ|Π)(Π|, which has the extra eigenvalue 1 on I and G-eigenvalues scaled by 1/4.
- **New:** "The centered frame operator 4T|_{H₀} and G have the same nonzero eigenvalues, including multiplicity."
- **Why the new sentence is correct:**
  - For the centered vectors v_jk = Π_jk − I/6, the frame operator S = Σ|v_jk)(v_jk| = VV* annihilates I, because Tr v_jk = 0.
  - By the displayed identity, S equals 4T on H₀.
  - G = V*V, so S and G share their nonzero spectra with multiplicity.
  - Since λ_max ≥ 1 > 0, Eq. (5) γ = 1 − λ_max(G)/4 follows.
- **Rendering:** the sentence typesets correctly and the page-2 layout is otherwise unchanged.
- **Numerical support from the full audit:** a direct 35×35 channel matrix agreed with {0^(35−rank)} ∪ nonzero(G)/4, with multiplicities, to 7.8e-16 in 44 cases. That check is reused here because the mathematics is unchanged.

**R2. Generic-verifier docstring (required, bundle): resolved.**
- **Old:** the docstring claimed "numerical checks form a 36x36 channel", which the code never performed.
- **New:** it says "this script performs exact symbolic checks only".
- **Why this is accurate:** the code (syntax-tree-identical to the audited version) uses only exact arithmetic in Q(u) and its multiquadratic extension.

## 3. Status of all findings from my full review

### 3.1 Main mathematical claims: unchanged and verified (reused from the full audit)
- **Theorem 3.1** (complete 24-eigenvalue Gram spectrum `{0⁴, 1⁵, (1−2s)³, (1+s)⁶, (1+2k)², (1−k)⁴}`, s = (1+4u−8u²)/3, k = 8u²−10u+3) holds identically in u on [1/4,1].
  - The full audit verified symbolically that the proof's 24 u-independent eigenvectors satisfy G(u)v = λ(u)v and are linearly independent.
  - The overlap blocks (10)–(11) were derived for generic u from the displayed matrices by two different exact implementations (the author's and mine), endpoints included.
  - A 50-digit numerical rebuild and a direct channel computation agreed.
- **Theorem 4.1** (equal probabilities, unit rate: max γ = 73/100, uniquely at u = 7/10) is correct. The three-interval proof checks, and an independent semialgebraic computation gives {u ∈ [1/4,1] : h(u) ≤ 2/25} = {7/10}.
- **Corollary 4.2** (channel spectrum `{0¹⁵, (21/100)², (24/100)⁶, (1/4)⁵, (27/100)⁷}`) is exact.
- **Distance comparison:**
  - Eq. (16) is RLE's averaged squared distance.
  - Eq. (17) equals RLE's per-pair formula (Eqs. 17–18 of arXiv:1103.1025v1) symbolically on relation (7).
  - Eq. (18), Table 1 (38513/750000000 and 29/20000) and the decimals are correct: u* = 0.694552035120092…, which matches RLE closed form (21) to 40 digits; γ(u*) = 0.72842497…; the gain is 0.2162%.
- **Proposition 5.1** (γ ≤ 2/3 for any mixture of product-vector bases on C²⊗C³, including non-tensor product bases) is correct.
  - The 12-basis example gives exactly 2/3, with spectrum {1/3 (×3), 1/4 (×8), 1/12 (×24)}.
  - 3,000 random mixtures plus an adversarial search found nothing above 0.584.
- **Bounds (19):** 73/100 ≤ γ*₄(6) ≤ 3/4, with equality iff four MUBs exist (attained by compactness). Correct.
- **Attributions:** the matrices, relation, amplitudes and optimizer match RLE as cited (arXiv v1 numbering). The corrected Roy–Scott DOI 10.1063/1.2748617 was confirmed via Crossref.

### 3.2 Required changes
| ID | Item | Status |
|---|---|---|
| R1 | p. 2 sentence | **Resolved** (Section 2) |
| R2 | `verify_generic.py` docstring | **Resolved** (Section 2) |

**No required change remains.**

### 3.3 Recommended changes (not required): unaddressed, preserved as adverse findings
- **S1. Equal probabilities are binding.** The canonical basis is unbiased to U₁–U₃, so its traceless range is orthogonal to theirs. Weights (27, 25, 25, 25)/102 on the same bases at u = 7/10 give exactly **γ = 25/34 ≈ 0.7353 > 73/100**; this was an exact check in the full audit, and a numerical probe over arbitrary weights found nothing better. This does not contradict any claim, because Theorem 4.1 and the abstract state "equal probabilities". But the paper does not tell readers that the headline value is a constrained optimum the same bases can beat.
- **S2. Verification equivalence and prior art.** Under vectorization, γ equals the Zhu–Hayashi spectral gap for verifying the 6×6 maximally entangled state with these four test bases. The 3/4 bound with its MUB equality case is their g-setting (parsimonious) result. The paper only refers to a "standard connection".

### 3.4 Optional items: unaddressed, one sharpened by a new check
- **O1. Phase branches.** The paper asserts "Equivalent phase branches are not needed for the theorem" without proof. My full review showed all eight arcs of RLE relation (7) share the Theorem 3.1 spectrum.
  - *New targeted check:* `followup_checks/check_branch_blocks.py` made 1,824 block comparisons (76 values of u × 8 arcs × 3 blocks). The overlap-probability blocks P₁₂, P₂₃ and P₃₁ on every arc equal the Eq. (11) ansatz at u = sin²θₓ to 1.3e-15. So the Gram matrices themselves coincide, and the asserted equivalence is true in the relevant sense.
  - It is still unproven in the paper. A short symmetry argument from RLE's amplitude formulas would close this.
- **O2.** Report, as numerical evidence only, that a bounded scan of the two-parameter RLE family in the full review found nothing above 0.73. The refinement converged to the subfamily optimum.
- **O3.** Cite Butterley–Hall (2007) and Bengtsson et al. (2007) for the history and definition of the averaged squared distance.
- **O4.** State that the RLE equation numbers follow arXiv:1103.1025v1, or check them against PRA 83, 062303.
- **O5.** Write out the block placement in (11) rather than "direct multiplication".
- **O6.** Optionally condense the process and AI-disclosure text.

### 3.5 Potential errors still open
The only open item is citation precision: the RLE equation numbers were verified against arXiv v1 only. No mathematical error is known in the final candidate.

## 4. Is any change still required?
**No.** Both corrections I required are implemented exactly and without side effects. No material objection to any main claim exists. The paper is scientifically satisfactory as a narrow working paper.

S1 and S2 remain **recommended** because they affect how readers judge the headline number and its prior-art context. They are not required, since every claim is correctly qualified. This is why I revise my recommendation from `minor_revision` (full review, driven solely by R1 and R2) to `accept`. That change follows the resolution of R1 and R2 and is not inherited mechanically.

## 5. Significance and novelty (re-evaluated, unchanged in substance)
The final edits add no scientific content, so my assessment of novelty and significance is unchanged after re-evaluation.

- **Novelty:** the new content is a narrow but genuine calculation: the closed-form spectrum of a known subfamily and its sharp equal-weight optimum. I located no prior computation of it in a focused, non-exhaustive search. The method (frame/Gram) and the global bound are standard or prior.
- **Significance:** modest.
  - The improvement over RLE's distance optimizer is 0.216%.
  - The equal-weight optimum is exceeded by simple reweighting.
  - The global d = 6 question is untouched.
  - The exact objective reversal and the clean 9.5% margin over product-basis mixtures are tidy but limited.

## 6. AIRR grading (as in `assessment.json`)
| Field | Value | Basis |
|---|---|---|
| correctness_confidence | 5/5 | Full-audit verification of all claims; the corrected sentence is now right; reruns are identical |
| rigor | 4/5 | Complete proofs; branch equivalence asserted without proof (true numerically); block placement delegated |
| novelty | 2/5 | Narrow calculation with standard tools; bound (19) is prior art |
| significance | 2/5 | One-dimensional optimization; small gains; equal-weight constraint binding (25/34) |
| reproducibility | 5/5 | Field-for-field regeneration; documentation now accurate |
| millennium_score | 2.6 (stars 3) | Re-evaluated: correct and acceptable but less substantive than the 3.00 anchor; the edits fix precision, not substance |
| recommendation | accept | No required changes remain; no material objections |

## 7. Ordinary 0–10 grading (separate from the AIRR scale)
| Criterion | Grade | Justification |
|---|---|---|
| Correctness | 10.0 | No incorrect statement remains. The only sentence previously false under its natural reading is fixed, and every theorem, identity, table entry and decimal was verified, several by independent routes. (The full review gave 9.5, solely for that sentence.) |
| Originality | 4.0 | Unchanged: the spectrum and optimum on the RLE subfamily appear new but follow directly from standard methods applied to a published family; the bounds are known or elementary. |
| Significance | 3.5 | Unchanged: a clean exact example of differing geometric and dynamical optimizers, with small gains, a binding equal-weight constraint and no global implications. |
| Clarity | 8.5 | Up from 8.0: the ambiguous frame-spectrum sentence is fixed. Still deducted: the branch-equivalence assertion without argument, the partly delegated block derivation and lengthy process disclosures. |
| **Overall** | **6.0** | Re-derived, not inherited. Weighting originality and significance more heavily than correctness and clarity (0.3/0.3/0.2/0.2) gives about 5.95. The corrections improve precision but add no substance. Verdict: a correct, carefully scoped, exemplary-reproducible short note of modest originality and significance, suitable for a specialized venue. |

## 8. Limits of this follow-up
- **Reused results:** unchanged mathematics is covered by my earlier full audit, not by fresh recomputation. Reuse is justified because the relevant source, verifier code and outputs are byte-identical or syntax-tree-identical.
- **Searches:** no new literature searches were made. Novelty statements rest on the full review's focused, non-exhaustive search, and the published PRA versions were not accessed.
- **Numerical checks:** the scans (product bases, weights, two-parameter family, branch arcs) are bounded checks, not proofs, and cannot establish any global optimum.
- **What I cannot verify:** the runtime "max" configuration, context isolation, and the pending public release and licensing actions. No public release is claimed.

## 9. Follow-up artifacts (`final-candidate/followup_checks/`; SHA-256 in `followup_checks/MANIFEST.txt`)
| File | Purpose | Result |
|---|---|---|
| `compare_candidates.py` (`20e5b99f…f592`) + `logs/compare_candidates.log` | Per-page PDF text diff; metadata diff; docstring-stripped syntax-tree comparison of `verify_generic.py` | Only page 2 changed (the sentence); code identical |
| `final_paper_extracted.txt` | pypdf text of the final PDF | — |
| `author_rerun/` + `logs/author_verify_rerun.log`, `logs/author_verify_generic_rerun.log` | Reruns of the final verifiers on copies | 20/20 and 10/10 PASS |
| `compare_outputs.py` (`03015b15…fb9a`) + `logs/compare_outputs.log` | Reruns vs final dated outputs vs prior outputs | Identical except time / provenance hashes |
| `check_branch_blocks.py` (`c6b90adb…abf9`) + `logs/check_branch_blocks.log` | New targeted check: overlap blocks on all eight arcs of RLE relation (7) | Max deviation 1.3e-15 from the Eq. (11) ansatz |
