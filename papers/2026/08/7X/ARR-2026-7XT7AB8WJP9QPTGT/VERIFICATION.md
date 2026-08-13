# Verification record for ARR-2026-7XT7AB8WJP9QPTGT v1

Date: 2026-08-13

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- The deposited PDF is 629,879 bytes and has SHA-256 `e4fd12894f2d15bd503370a016f259aa0e2f619810ba309108ca6a1150a02935`, matching the depositor-supplied value.
- PDF inspection found 10 A4 pages, no encryption, no forms, and no embedded JavaScript.
- Visual inspection covered all 10 rendered pages. The document is complete and legible, including two figures, three tables, the source-to-Gram specification, the independent-audit appendix, and the references.
- `paper.md` and `paper.txt` were extracted mechanically from that exact PDF. They are accessibility and machine-reading renditions, not replacements for the canonical mathematical typography.
- The reproducibility ZIP is 1,790,678 bytes and has SHA-256 `b5ace98f5ac8951c3939ee85c4c34563668861b0c23ca3751e7e4d5b17eb2645`.
- Its manifest and frozen inner source archive were accepted by the supplied release verifier. The inner source archive has SHA-256 `6f744332b9b068ec050c9e36b502b3b4241687acb87c7b35c99a5dee926721fb`.

## Supplied terminal verifier — pass

The declared terminal command completed successfully on the ARR ingestion machine in approximately 11 seconds:

```text
python repro/verify_release.py repro
```

The verifier reported:

```text
PASS: hashes, provenance, schemas, interval objects, Arb readjudication, and independent shadow audit
```

The frozen theorem record contains 78 positive and zero unresolved directions in each parity sector. It records coercive lower bounds of approximately `5.890068275105137e-17` (even) and `1.6529959078469627e-13` (odd). The separately written non-Arb shadow audit records positive Weyl margins in both sectors.

## ARR reproducibility label — partial

The deposited terminal verifier reconstructs the canonical aggregate from the allowlisted predecessor, checks hashes and schemas, extracts the frozen v3 source, reruns the multiband adjudicator, and runs the independent shadow implementation. ARR did **not** repeat the full heavy regeneration of the underlying NPZ proof objects, which the supplied documentation says was performed at 512-bit Arb precision on a Colab Pro+ CPU runtime and is not intended as a laptop smoke test. Therefore the public ARR label remains **partial** despite the terminal verifier's PASS.

## Scope and unassessed items

- The certified claim is bounded to support `0 < a <= 0.72`; it is not a proof of the Riemann hypothesis.
- Bibliographic integrity: **not assessed**.
- Frontier-model screening: **not assessed**.
- Lean 4: **not applicable**; no Lean formalization or kernel-checkable certificate was supplied.

## Conflict disclosure

The author and current ARR founder-editor are the same person. No independent editorial or scientific assessment is claimed.
