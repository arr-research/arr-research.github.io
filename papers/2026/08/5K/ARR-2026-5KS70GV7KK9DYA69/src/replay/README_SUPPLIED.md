# Two-Query Chirality in Tetrahedral Quantum Echoes

This directory contains the final Paper 18 manuscript and its lightweight
verification package. The causal certificate is exact; the word/collision and
representation replays combine symbolic checks with numerical diagnostics.

## Replay

From this directory on Python 3.12 with the pinned SymPy and NumPy dependencies:

```powershell
python -m pip install -r requirements.txt
```

Then run:

```powershell
python .\verification\verify_coherent_order_echo.py
python .\verification\verify_two_use_a4.py
python .\verification\verify_two_use_causal_qhalf.py
```

The checks reconstruct all 24 echo words, audit the one- and two-query
representation formulas, and prove the `q=1/2` causal certificate exactly in
the quotient field. The first two scripts include floating-point diagnostics
and tolerances; the universal formulas and collision completeness are proved
analytically in the manuscript. No SDP, random seed, network access, or heavy
computation is used.

## Files

- `Two_Query_Chirality_in_Tetrahedral_Quantum_Echoes.pdf`: submission PDF.
- `paper/two_query_tetrahedral_echo.tex`: manuscript source.
- `paper/references.bib`: bibliography.
- `verification/`: three replay scripts, including one exact quotient-field certificate.
- `requirements.txt`: pinned Python dependencies used for the frozen replay.
- `CLAIM_LEDGER.md`: proved, scoped, and prohibited claims.
- `SUBMISSION_SHEET.md`: ARR metadata.
- `MANIFEST.sha256`: release hashes.
