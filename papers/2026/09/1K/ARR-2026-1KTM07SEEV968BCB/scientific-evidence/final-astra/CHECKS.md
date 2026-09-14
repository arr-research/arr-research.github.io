# Exact-candidate local checks: C2

PDF SHA256: `0be3fbefb7fd721076c5a5261dc111103ec65fdf01fe6e53c487932ff3fe7b74`

Recommendation: accept (local model recommendation only). Overall 4/10; Millennium4/10.

## Checked

- Exact PDF SHA256 matched; 15 pages extracted; Clifford and valuation proof page 7 visually inspected.
- Full analytic arguments A,Z,B-prime,R,N,B checked, including field extension/valuation domination, characteristic-two phase reduction, Fourier-circulant reduction and sharpness family.
- The binomial spectral-multiplicity proof T2 checked; T3 case split and attainment checked conditional on its explicitly imported trinomial rule.
- Field-free bound re-derived from Hilbert-Schmidt norm, operator norm and coefficient Cauchy-Schwarz; all displayed open-gap ranges recomputed.
- Supplied inspected thmZ_construction.py rerun for every r<d at d=4,8,9,16,25,27: 89 exact constructions, zero mismatches.
- Supplied inspected clifford_exact.py rerun for d=4,8,9: 96+768+972=1836 exact conjugation identities, zero failures, all 6/12/12 directions present.
- Supplied inspected plane4_check rerun at m=2,3: exact zero maximum 8 in both cases; this and Fourier duality suffice for the stated 4-torsion consequence.
- New independent code checked all 65,535 nonzero F2 polynomials below degree16, 19,682 F3 polynomials below degree9 and 3,124 F5 polynomials below degree5. These tests do not replace the proof over arbitrary characteristic-p fields.
- Independent integer checks verified Omega/Hamming formula through prime powers<=2401 (p=2,3,5,7); incidence multiplicities and sharp obstruction words for d=4,8,9,16,25,27; binary obstruction minimum4 for d=4,8,16; exhaustive Radon minima4,6 for p=2,3; wrapped quadratic-phase identities for all (s,a,j) in those six dimensions.
- Primary Delvaux–Van Barel Definition7/Theorem10, Massey–Costello–Justesen, Key–McDonough–Mavron Result1, Meshulam inequality and Stacks00IA consulted.

## Not checked

- All large exact tables in Section5.3, full d=27,m=4 flats computation, p=5 Radon minimum enumeration and high-dimensional obstruction distributions were not rerun.
- Historical model identities, isolation, prior-review narratives and every supplied log were not authenticated.
- The private antecedent 0WE trinomial rank theorem was not independently proved or audited here; T3 remains conditional exactly as the manuscript says.
- No complete search for counterexamples to Conjectures C or U and no proof for their open ranges.

## Limitations

- Section 8 item 5 suggests a similar argument for order pq, although Section 5.3 explains that the all-roots-to-one valuation does not exist there. This is a speculative research direction, not a consequence of the current proof, and should be phrased accordingly.
- The exact composite tables and numerical searches occupy considerable space relative to the principal new theorem; several large entries rely on supplied historical computations not rerun here.
- Novelty is bounded: no global literature priority certification, and scalar/Radon ingredients themselves are not new.

## Potential errors

- No material error found in the principal theorem or its proof. The phrases true envelope beyond ell=p should continue to be read as the conjectured all-sparsity operator envelope, as the later formal statements specify.

## Independence and execution

Fresh delegated task context, other reports/scores/source diffs/provenance/editorial registries withheld. The configured model family participated in manuscript revision assistance. This candidate itself recounts earlier review findings; that narrative was visible and was not treated as evidence. No technical claim that model memory is disabled.

All supplied modules executed were first inspected (cyclo, Clifford, constructions, exact_zeros, zeros_spot). Separate workcopy only; no pickle, candidate source mutation or server changes. Print-only diagnostic scripts were assessed by their actual mismatch/confirmation output, not exit status alone. The new independent.py imports no submitted Python modules.

Local preassessment only, with no SID or private-intake assessment; neither human acceptance nor deposit/publication permission follows from this report.

## Primary sources

- [Delvaux and Van Barel, Rank-deficient submatrices of Fourier matrices, TW470, Definition7 and Theorem10](https://www.cs.kuleuven.be/publicaties/rapporten/tw/TW470.pdf)
- [Massey, Costello and Justesen, Polynomial weights and code constructions](https://www.isiweb.ee.ethz.ch/archive/massey_pub/pdf/BI419.pdf)
- [Key, McDonough and Mavron, minimum weight of dual codes, Result1](https://users.aber.ac.uk/tpd/papers/min-weight-upper-bound-postprint.pdf)
- [Stacks Project, valuation domination lemma00IA](https://stacks.math.columbia.edu/tag/00IA)
- [Meshulam, An uncertainty inequality for finite abelian groups](https://arxiv.org/abs/math/0312407)

## Actual logs

- `independent.py`: SHA256 `d38250027a97d563d264885461ab2169adcaee400bbae33c8c0cc7b8fb68c4db`
- `independent.log`: SHA256 `92bcad160c30cb3da4ecea90fe9eec3f14ef00189d50b9552ff5a747aa59a697`
- `clifford.log`: SHA256 `d0279ebb4a441d36b3f7ea05c071609807171557763583114fdaf8698190e3ee`
- `constructions.log`: SHA256 `c241b75ddc72e21288be72a7817127f6f92b38a88c34aaa4e3f377c58061f3ef`
- `plane4.log`: SHA256 `ebd502dff455ba3f62284651b8c583adf150111a6ed5a8ac95b9a42a7d93de64`
