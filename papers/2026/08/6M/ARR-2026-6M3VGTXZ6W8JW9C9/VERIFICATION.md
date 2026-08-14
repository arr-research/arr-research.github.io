# Verification record for ARR-2026-6M3VGTXZ6W8JW9C9 v1

Date: 2026-08-14

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- The deposited PDF is 556,578 bytes and has SHA-256 `c0a1b3811dfa50d5bb6872c8973687bc078262e5eda59220e8a6b3a86024c425`, matching the frozen release value.
- PDF inspection found 21 A4 pages, no encryption, no forms, and no embedded JavaScript.
- Visual inspection covered all 21 rendered pages, including both figures, all three tables, equations, references, and the final incremental border-certificate wording.
- `paper.md` and `paper.txt` were extracted mechanically from that exact PDF. They are accessibility and machine-reading renditions, not replacements for the canonical mathematical typography.
- The supplied reproducibility ZIP is 565,138 bytes and has SHA-256 `6c64db3251fc9909ecc793577105273fd4ab0bad0f3aaebb369e725f7dba03f3`.

## Reproducibility — partial

The declared bounded replay commands completed successfully from `src/replay/`:

```text
python verification/verify_global_projective_memory.py --check results/global_projective_memory/certificate.json
python verification/verify_planar_projective_memory.py
```

Observed checks include:

- byte-for-byte equality of the normalized global certificate with SHA-256 `ecfa47a4585bb646716888b93cc0ca4fca6fc2c33c5373786790c6d010af210a`;
- completion of the independent planar replay covering 119 binary cases, 14 detector-gap cases, exact rational fixtures, and the planar phase strata;
- preservation of the frozen planar certificate file with SHA-256 `09e3aa7dc2b2a80ce2222bae0a4a85357d0d36d09e257595b992ceb900db5c47`.

This is labelled **partial**, not pass, because the programs audit finite exact fixtures and symbolic reductions. The global projective-degree equality, block genericity law, deletion theorem, and delay-capped compactness theorem depend on analytic proofs in the manuscript and are not independently formalized by the programs.

## Related record and scope

- `ARR-2026-52B6MSS1W197W9T2` is related prior work on direct-sum spectral routing, not a prior version or duplicate of this research object.
- The paper concerns finite passive rational-inner routing and dimensionless Wigner-Smith/group delay. It does not prove a theorem about resonator quality factor, stored energy, linewidth, fabrication cost, or fundamental quantum memory.

## Not assessed / not applicable

- Bibliographic integrity: **not assessed**.
- Frontier-model screening: **not assessed**.
- Lean 4: **not applicable**; no Lean formalization or kernel-checkable proof was supplied.

## Conflict disclosure

The author and current ARR founder-editor are the same person. No independent editorial or scientific assessment is claimed.
