# Verification record for ARR-2026-7H9FAPTBZA897AMJ v1

Date: 2026-08-14

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- The deposited PDF is 372,127 bytes and has SHA-256 `ef6e3fd745ffda790c50fcfa265391fc8ddad9a010e350d3bce2db6c2efa33cf`, matching the supplied values.
- PDF inspection found 10 A4 pages, no encryption, no forms, and no embedded JavaScript.
- Visual inspection covered all 10 rendered pages, with pages 2 and 9 additionally inspected at full resolution. The document is complete and legible, including its companion-scope table, vector figure, equations, reproducibility statement, and references.
- `paper.md` and `paper.txt` were extracted mechanically from that exact PDF. They are accessibility and machine-reading renditions, not replacements for the canonical mathematical typography.
- The supplied source ZIP is 43,243 bytes and has SHA-256 `bfaae0014e12bc60162f364b26c01948ee99241c5ee17a6b4398111dd21f6cde`.
- The supplied replay manifest has SHA-256 `16be07c5377ecd94b78a9d230341664c832be893394a71c55e2bc0719b89d6f7`.

## Reproducibility — partial

The two declared bounded replay commands completed successfully on the ARR ingestion machine:

```text
python verify_oriented_plucker_rdf.py --samples 60000
python reproduce_plucker_frontier.py
```

Observed checks include:

- 18 exact symbolic coefficient cases for dimensions 3 through 20;
- four deterministic Monte Carlo normalization checks;
- six covariant-branch diagnostics;
- byte-for-byte equality of the regenerated `oriented_plucker_rdf_verification.json` with SHA-256 `0189a7b203bdd188c517beb566d6e24e6ac8355e5975ed5d9db208aff6a21fbe`;
- byte-for-byte equality of the regenerated `plucker_frontier_diagnostics.json` with SHA-256 `f3a46ea8a45362b0ce1040593e716de4b72b8961c6afd4d9c1d306ad3daa4a86`.

This is labelled **partial**, not pass, because both programs explicitly identify themselves as diagnostic replays. The global all-field theorem and rate–distortion claims depend on analytic proofs in the manuscript and are not independently formalized by the programs.

## Related record and scope

- `ARR-2026-61Y0FFA39M8KMBJ5` is a related complex rank-two companion, not a prior version or the same research object.
- The present work concerns signed Plucker-coordinate compression, not quantum rate–distortion, Born-probability prediction, or a derivation of Born's rule.

## Not assessed / not applicable

- Bibliographic integrity: **not assessed**.
- Frontier-model screening: **not assessed**.
- Lean 4: **not applicable**; no Lean formalization or kernel-checkable certificate was supplied.

## Conflict disclosure

The author and current ARR founder-editor are the same person. No independent editorial or scientific assessment is claimed.
