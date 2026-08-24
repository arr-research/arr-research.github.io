# Independent Codex referee report — draft 0.2

Date: 2026-08-24  
Role: independent adversarial Codex referee  
Scope: manuscript and exact replays, read independently of earlier audits  
Human peer review: **no**

## Verdict before revision

No P0 mathematical defect was detected. The main theorem was judged likely
correct. The referee assigned **6.4/10 with uncertainty ±0.9** on the scale in
which 10.0 denotes an unconditional correct solution of a Millennium Prize
Problem.

| Dimension | Score |
|---|---:|
| Correctness | 8.7 |
| Novelty | 4.0 |
| Depth | 5.4 |
| Applications | 3.5 |
| Reproducibility | 7.3 |
| External validation | 1.5 |

The numerical assessment is a Codex evaluation, not certification of
correctness, novelty, or priority.

## P1 findings

1. The combined tangent/osculating corollary depended entirely on the author's
   earlier ARR paper and was therefore not an independent contribution.
2. Priority was not established; the core interpolation input is standard
   jet-ampleness technology followed by a convex packing argument.
3. Applications and nontrivial sharpness examples for `d >= 2, s < m` were
   limited.

## P2 findings

1. The support-threshold proof did not separately treat `q=1, r=0`; in that
   boundary case its contradictory assumption allows only `n=0`.
2. The mixed-interpolation statement needed the explicit quantifier `t >= 1`.
3. The statement that tangent absorption does not imply higher absorption had
   no geometric counterexample in the manuscript and should be removed or
   softened.
4. The packing proof should define `f(0)=0` so that disappearance of a
   weight-one block is formally covered.

## Replay assessment

The replay uses exact rational and integer arithmetic and is reproducible for
the listed finite fixtures. It does not validate the theorem in arbitrary
characteristic, and in the displayed full-rank fixtures the value rows already
span the complete target, so appending jet rows cannot add rank. The replay is
supporting evidence only, not a proof checker.

## Revision status

The manuscript removes the citation-dependent combined corollary and adds a
self-contained jet-ample-polarization variant. It also separates the boundary
case, adds the missing nonempty-list quantifiers, defines the packing objective
at zero, removes the unsupported implication claim, and narrows the sharpness
and novelty language. These changes still require focused re-review and fresh
artifact verification.

## Focused re-review

The same independent Codex referee re-audited only the revised corollary and
boundary repairs. No P0 or internal-correctness P1 issue was found. The
reduction from weight below `M+1`, the support threshold, the cases `R=0` and
`q=1,r=0`, and the tensor-power deduction all survived adversarial checks. Two
P2 wording requests—quantifying `a,l` and using fat-point restriction
notation—were incorporated. The revised score is **7.2/10 with uncertainty
±0.8**. The remaining P1-level scientific reservation is the absence of an
exhaustive literature comparison establishing novelty or priority; the paper
states this limitation explicitly.
