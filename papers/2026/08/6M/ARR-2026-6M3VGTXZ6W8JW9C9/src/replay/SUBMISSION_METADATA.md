# Submission metadata

- Type: new submission (not a replacement)
- Title: Projective Memory and Resonant Bottlenecks in Passive Multiport Routing: Exact Global Laws, Robust Error Floors, and High-Delay Border Phases
- Author: Lluis Eriksson
- Primary category: Mathematical Physics
- Secondary category: General Mathematics
- Length: 21 pages, 2 figures, 3 tables
- Keywords: rational inner matrix; projective interpolation; McMillan degree; passive memory; border memory; resonant approximation; chordal error; Wigner--Smith delay
- Comment: Global projective state law, exact multiband max--min split, incremental border certificates, determinantal closure, robust error floors, and forced high-delay border phases.

## Abstract

At distinct boundary frequencies, let a square rational-inner multiport route
one fixed input ray to prescribed output rays. We prove that the minimum
McMillan degree equals the least degree of a base-point-free projective curve
through the ordered target rays, independently of ambient port count. For
orthogonal target bands we solve line-to-subspace incidence constraints by
full-support Lagrange kernels and derive a closed generic codimension law.
Exact memory is the maximum shifted band cost, whereas border memory is the
minimum and may be arbitrarily smaller. An intrinsic incidence matrix gives a
calibrated singular-value error floor and an all-data base-point deletion law.
Finally, every zero-error sequence below exact memory has divergent peak
dimensionless Wigner--Smith delay; any finite delay cap restores compactness,
a positive attained error, and a three-phase operational classification.
Explicit planar strata and exact rational certificates audit the results.
The planar specialization is incorporated here and is not a separate
submission.

## AI assistance disclosure

AI tools assisted literature discovery, symbolic fixture generation, code
review, and language editing. The author selected and checked the claims,
proofs, and certificates and takes responsibility for the content.

## Immutable artifacts

- Source base commit: `b2a7f3268de19683573325c5a63d4ce0030ed955`
- PDF: `Projective_Memory_and_Resonant_Bottlenecks.pdf`
- PDF SHA-256: `C0A1B3811DFA50D5BB6872C8973687BC078262E5EDA59220E8A6B3A86024C425`
- Reproducibility archive: `Projective_Memory_Reproducibility.zip`
- ZIP SHA-256: `6C64DB3251FC9909ECC793577105273FD4AB0BAD0F3AAEBB369E725F7DBA03F3`
- Global certificate SHA-256: `ECFA47A4585BB646716888B93CC0CA4FCA6FC2C33C5373786790C6D010AF210A`
- Planar certificate SHA-256: `09E3AA7DC2B2A80CE2222BAE0A4A85357D0D36D09E257595B992CEB900DB5C47`

Replay after extracting the ZIP:

```powershell
python verification\verify_global_projective_memory.py --check results\global_projective_memory\certificate.json
python verification\verify_planar_projective_memory.py
```
