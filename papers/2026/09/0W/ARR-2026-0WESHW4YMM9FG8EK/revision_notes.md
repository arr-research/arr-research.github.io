# Quantum final revision: precise change list

5 September 2026. The article is prepared for ARR record ARR-2026-0WESHW4YMM9FG8EK, version 1. This preparation has performed no publication action.

The earlier cycle-3 outputs are unchanged. Exact copies of all seven earlier quantum files are under `evidence/cycle3/`. The earlier manuscript hash is `7ca7429c82c2139f36fbbc50a7bc9fe1a71a9f9de48af76069c0bcf5278bfe7c`. Its separate mathematical screening applies to that edition. The new universal delta and the final thirteen-page PDF also passed separate internal screening, recorded in `quantum_final_independent_review.md` and its JSON. The new report identifies source hash `35f9741025f3eab91a73e3c9e71db7f4612423656ee826131f5e35dcac372559` and PDF hash `f777ae1be0bce53d34394c3cc823b4d21779156f43e2414a28cae7324cfcdd2f`. It is separate-agent internal screening, not an external referee report or an ARR score. The reviewer's separate exact checker and JSON are included.

## Mathematical changes

1. Section 2 replaces the prime-power central-sector theorem by a theorem in every fixed cyclic Weyl dimension. For H=<u,v>, q the order of the commutator and R=qH, it proves |H|=q^2|R| and a common multiplicity m=d/(q|R|). Every central sector is m identical q-dimensional cyclic copies.
2. The exact determinant and nullity formulas now allow q=1 and zero constant coefficient, with both nonconstant coefficients nonzero. The equivalent commuting central-polynomial rank reduction is explicit. A genuine trinomial has at most two singular sectors, hence nullity at most m min(2,h).
3. The hypotheses and degeneracies are specified: a scalar central power or an exponent-two center permits only one singular sector when all coefficients are nonzero; a zero constant can allow more than two. The equal common m is restricted to the fixed cyclic Weyl representation, not arbitrary representations of a Weyl relation.
4. An optional gcd formula computes m from the two labels. The prime-power noncommuting case is recovered as multiplicity one, with an alternative valuation proof. The existing prime-power rank and dyadic list classifications are preserved; no composite all-support rank classification is inferred.
5. Section 4 explains the existing dimension-12 nullity-three example by multiplicity three, adds a dimension-36 genuine trinomial attaining nullity six=2m, and adds a dimension-12 zero-constant negative control with six singular sectors and m=1.
6. Section 7 now proves both directions of the exact two-label corank divisibility criterion, so the operational lower bound has no dependency on an inaccessible earlier note.

## Verification and editorial changes

7. Added exhaustive exact label-arithmetic checks for all 714,096 distinct nonzero ordered pairs in dimensions 2 through 20, including commuting pairs. Retained the earlier 1,948,590 prime-power noncommuting support checks and all projector, incidence, spectrum and operational construction checks. Extended formal cyclic determinant checks to nineteen orders.
8. Added `composite_matrix_checks.py`, using direct group closure and exact matrix ranks without importing the main verifier. Its seven exact composite fixtures verify the original and central-polynomial ranks, the multiplicity, degeneracies and negative control. This method was written by the constructing agent and is not labeled a separate agent review.
9. Updated the title, opening results, scope, source comparison and reproducibility instructions to match the universal theorem. Removed research-draft labeling and internal workspace paths from the article. Explicitly credited the classical cyclic normal form through Farenick, Ojo and Plosker, alongside the prior stabilizer, quantum-torus and factor-width sources.
10. Added a portable README, preserved baseline evidence, a unified source/verifier diff, and source/version hashes in the new exact certificate. The literature comparison remains bounded and does not claim external priority or refereeing.

Both exact replays pass. The full replay's measured runtime is about eight seconds after interpreter startup in this environment; the manuscript gives approximately nine seconds as a descriptive bound. Finite samples are validation of the supplied proofs, not replacements for their arbitrary-coefficient and arbitrary-dimension quantifiers.
