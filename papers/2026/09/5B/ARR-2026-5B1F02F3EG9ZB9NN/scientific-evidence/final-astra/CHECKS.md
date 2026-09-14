# Exact-candidate local checks: A4

PDF SHA256: `a725d4f88c947f88c03882a6b2e9d663f4c78134a8c5bdc052b240525ebf223b`

Recommendation: accept (local model recommendation only). Overall 4/10; Millennium 4/10.

## Checked

- Exact PDF SHA256 matched; all 12 pages extracted; certificate architecture and corrected dual/chamber proof pages 5-6 visually inspected.
- Analytical Horn-program equivalence via equal-spectrum positive matrices and polar factorization; positivity shift s_d=0; reflection and padding directions checked.
- Finite reduction re-derived conceptually: kappa is convex as a projection-LP value, H_N-kappa-gamma D_* is concave on each affine D_* cell, so nonnegativity at cell vertices suffices. At the two zero-distance vertices a weighted-shift construction gives cost at most H_N.
- Full supplied exact verifier replay passed: TOTAL: 0 failures  [347.9s].
- Independent GMP cell/edge reconstruction reproduced every W_N and the 47,685 positive-distance pairs for N=3..12, and recomputed all D_* and primal-cost ratio bounds.
- Independent LR-tableau enumeration produced exactly 522 Horn triples in d=6. Exact GMP double-description reproduced all 22 chambers and 112 ray incidences; every primal witness and global dual passed, with strict interior dominance checked.
- All 12 active all-d files independently verified structurally: long templates are Lidskii I=1..r,J=K; r<=2 templates satisfy exact affine-slope Horn conditions. All resulting coefficients are <=1 and bounds match.
- All copied certificate byte hashes matched the exact candidate. Buch hive boundary/rhombus convention and Fulton Horn/LR equivalence consulted as primary sources.

## Not checked

- The submitted generators, every historical adversarial script and historical random floating-point scans were not rerun; they are unnecessary for the exact certificate proof.
- No historical byte-provenance authentication or independent audit of every antecedent AIRR manuscript.
- No proof or computation for unrestricted N, all-d AB cost for N>=7, or a uniqueness classification.
- This is not formal proof-assistant verification or human peer review.

## Limitations

- The finite reduction is imported with the explicit set delegated largely to code. A brief convexity proof and a code-independent description of the ordered-simplex cells would make the article more self-contained.
- The specialized numerical extensions do not establish general-N behavior or unique minimizers.
- Historical model identities, run claims and private antecedent priority were not authenticated in this assessment.

## Minor wording

- Minor wording in Section 5, N=8: the N=7 line is already reflected W_7, so say replace reflected W_7 by reflected W_7 plus reflected W_8. The displayed inequality and certificate are correct.

## Independence and execution

Fresh delegated task context with prior assessments, scores, editorial registries, source diffs and provenance files withheld. The underlying model family participated in revision assistance. Prior review narratives inside this candidate were visible; their verdicts and claimed runs were not used as proof. No technical claim of disabled memory.

Supplied verifier and its sole local geometry import inspected before execution. Run from separate workcopy; certificates parsed as JSON/gzip, no pickle. Independently written checker imports no submitted Python modules and uses fractions, exact cdd GMP and a new LR-tableau routine.

Local preassessment only; no SID, private-intake report, human editorial acceptance, deposit or publication authorization is conferred.

## Primary sources

- [Buch, The saturation conjecture, Theorem 1 and Fulton appendix](https://sites.math.rutgers.edu/~asbuch/papers/sat.pdf)
- [Fulton, Eigenvalues, invariant factors, highest weights, and Schubert calculus](https://arxiv.org/pdf/math/9908012)
- [Knutson and Tao, The honeycomb model of GL_n(C) tensor products I](https://arxiv.org/abs/math/9807160)

## Actual logs

- `full-verifier.log`: SHA256 `d438f467929e4337e36d9eea5878d3eb3396a628819396dfbe0ced0cb02c549d`
- `independent.log`: SHA256 `bb1e1890d5ec59817dfeabc399672f353246ff69519d3f25dd46026d9936ff00`
- `independent.py`: SHA256 `2e31668f95956028a5346e835d34048eb72211686d6b593113544ada8b15994f`
