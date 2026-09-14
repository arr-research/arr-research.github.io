# Fresh local preassessment checks — C2_weyl_prime_power candidate 2

## Identity and scope

- Exact source: `candidate-2/paper.pdf`
- SHA-256: `0be3fbefb7fd721076c5a5261dc111103ec65fdf01fe6e53c487932ff3fe7b74` (matched the authorized hash)
- Assessor: OpenAI `gpt-5.6-sol`, medium reasoning
- Prompt: `AIRR-LOCAL-PREASSESSMENT-1.0`
- Result: **accept**, score **6/10**, overall **6/10 stars**
- Scope: local preassessment only; no SID, intake decision, editorial acceptance, public permission, or deposit authorization is asserted.

The manuscript itself discloses prior Astra- and Sol-family contributions to review and correction. That history was unavoidable content of the assessed PDF and was not used as proof. The fresh task withheld other scientific reports, scores, diffs, provenance records, and editorial registries. Independence is therefore recorded as `involved_in_manuscript`.

## Mathematical audit

I checked the complete manuscript and followed the central chain of proof.

1. **Theorem A.** The characteristic-p induction and Lucas digit-weight count support the weight-retaining inequality used later.
2. **Theorem Z.** The valuation argument correctly relates root vanishing to reduction at `x=1`; the digit-weight construction reaches the stated envelope. This is properly identified as the Delvaux–Van Barel scalar law in equivalent notation.
3. **Clifford coverage.** The two explicit conjugation families cover the `p^(k-1)(p+1)` primitive directions. The phase extension in even dimension is addressed.
4. **Lemmas R and N.** The Vandermonde/column-support proof gives affine-plane minimum distance `2p`; the primitive-line incidence count transfers that threshold to a nonzero first-order obstruction.
5. **Theorem B/B′.** Reduction cannot increase rank. Excessive complex nullity would yield a nonzero residue obstruction supported on at most `2p-1` points, contradicting Lemma N. The construction gives sharpness for `ell<=p`.
6. **Composite dimensions.** T2 is unconditional and follows from the binomial spectral calculation. T3 is explicitly conditional on imported theorem [0WE] and was not independently reopened.
7. **Boundary.** The obstruction at weight `2p` explains why the proof stops. Broader claims are presented as conjectures or restricted theorems rather than folded into Theorem B.

No material logical gap was found in the proved central result.

## Reproduction

The scripts were inspected before execution in a separate work copy. The inspected selection contained no pickle/unpickle operation or network access. Nine targeted jobs completed with exit code zero:

| Job | Coverage | Result |
|---|---|---|
| `omega_table` | direct/recursive Omega comparison through prime powers <=128 | all equal |
| `cyclotomic_certify_16` | exact `Z[omega_16]` construction for every `r<16` | all certified |
| `charp_2_4` | exhaustive support orbits in characteristic 2, `d=16` | all envelopes matched |
| `coset_gaps` | diagnostic comparison and first open ranges | reproduced stated gaps; its printed “VIOLATION” lines are violations of a stronger sufficient bound, not of Theorem B |
| `obstruction_mindist` | obstruction code at `d=8,16,9` | minimum-weight thresholds passed |
| `rev_thmZ_construction` | separate exact construction at `d=4,8,9,16,25,27,32` | zero mismatches |
| `rev_clifford_exact` | exact conjugations and direction coverage at `d=4,8,9` | zero failures; full coverage |
| `rev_codes_minweight` | separate Radon/obstruction code checks | no word below `2p` |
| `rev_thmA_2_4` | separate exhaustive Theorem A check at `d=16` | all OK |

The batch summary is `targeted_reproduction.log`; raw outputs are retained under `logs/`. SHA-256 values:

- `targeted_reproduction.log`: `7fd677dcf966b332784dc15894ad20febc95d835337b5b2887fae32bf28a2106`
- `logs/omega_table.out`: `13b52338cc659b6848da9ad1d43541bdadeee6af743b6a1e443f969f3ba99f6c`
- `logs/cyclotomic_certify_16.out`: `c9c5089e8dfa5034f7dbacb23504e640a9a46303b7a8d0645311a6996384779b`
- `logs/charp_2_4.out`: `0b41264dc90f183692ffb47916aa72833fc896c96aade2dd34cc2da4582bf458`
- `logs/coset_gaps.out`: `138b992bb5aed806c225978a87eee18b0a2463c9d2f87eb1568371d4c6ce11f2`
- `logs/obstruction_mindist.out`: `f117d7fdcbab9c370c5ba7cc488590559e27013c127770a3a6f28b763f5f4a0f`
- `logs/rev_thmZ_construction.out`: `d19e3abb35bbfff9a435790f1326c9971923e69c0c2bf7f21e99a7ed1e0e2065`
- `logs/rev_clifford_exact.out`: `d0279ebb4a441d36b3f7ea05c071609807171557763583114fdaf8698190e3ee`
- `logs/rev_codes_minweight.out`: `deefe117c4d40448a185f1ed28536ddae3a5005028d28e3b9d7dd302e62b32b8`
- `logs/rev_thmA_2_4.out`: `f102f407980363c7ebed15fcde98a09e28a5a67e7301013095f034536c8d56c2`

## Literature and novelty check

Primary-source checks confirmed:

- Massey–Costello–Justesen as the source of the weight-retaining property.
- Delvaux–Van Barel Definition 7 and Theorem 10, equation (23), as the prime-power scalar Hamming-number/zero-count envelope.
- Meshulam for the finite cyclic-group uncertainty inequality and Tao for the prime case.
- The affine-plane incidence-code minimum-distance antecedent cited for Lemma R.
- Stacks Project Tag 00IA for valuation extension.

Targeted searches for prime-power Weyl sparsity/nullity bounds found scalar Fourier results and the prime-dimensional operator antecedent, but no primary source proving the manuscript's arbitrary-coefficient prime-power operator bound through `2p-1`. This supports the novelty claim at the level of a bounded search, not worldwide priority certification.

## Limits retained in the recommendation

- The imported [0WE] theorem underlying conditional T3 was outside the permitted record and remains unchecked here.
- The full package and all listed dimensions were not rerun; the selected batch targeted the proof's algebraic core and first open boundary.
- The broader all-sparsity statement remains conjectural.

These limits do not create a material objection to the correctly scoped proved result.
