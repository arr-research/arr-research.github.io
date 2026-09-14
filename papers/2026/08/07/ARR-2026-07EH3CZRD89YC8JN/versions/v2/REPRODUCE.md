# Reproduce this exact corrected candidate

The current manuscript is root paper.tex, references.bib and figures/memory_law.pdf. The scientific-source/paper_calibration_memory/main.tex belongs to the historical checkpoint and is not the source of this corrected PDF. Compile the root manuscript with Tectonic 0.16.9:

    tectonic --untrusted --keep-logs --keep-intermediates paper.tex

Historical scientific checkpoint a52d6e74dba697477acf9204077a1b67ffe56dfc remains unchanged. From the package root run this single command (Python with NumPy, SciPy and Matplotlib installed):

    python -B reproduce.py --output ../calibration-replay

Use a NEW directory outside the preserved package. The script refuses existing output and package descendants or ancestors. It copies the scientific sources into output/scratch, applies the corrected verifier only there, runs generator and validator, and saves actual environment versions, timestamps, exit codes, stdout/stderr and input hashes in output/RESULT.json. It disables bytecode writes, retains failures and installs no dependencies. A failed replay returns a nonzero exit code. Choose a different new output directory for each run.

Corrected verifier SHA-256: bd5474fa161578b037415e4d4cbf0ee4ff4ed9d69e4bdc5dbc9b73e2dabb214d. Original verifier and historical ledgers remain preserved. The verifier checks the ledger; it does not authenticate how it was generated or continuously certify contours. Actual new executions must retain their own versions, timestamps, commands, failures and outputs.

The root current figure uses calibration charge K. The historical generator uses M. The separately supplied presentation-overlay/research/calibration_memory_certificate.py changes precisely this one legend; its companion quantum_reservoir_filter.py is an unchanged copy. From the candidate root, regenerate the current figure into a NEW scratch output location:

    python presentation-overlay/research/calibration_memory_certificate.py --figure new-scratch/memory_law.pdf --output new-scratch/certificate.json

Scientific formulae and data-generation logic are unchanged in this presentation overlay. The packet includes scientific sources, not a complete GitHub release checkout; missing release workflows/assets are not evidence that they are absent publicly. There is no Lean theorem or continuous interval contour certificate claimed.


## PDF identity and build reproducibility

The exact PDF hash identifies the deposited bytes, not every future compilation.
An ordinary Tectonic rebuild can give the same page rendering while differing in
creation metadata and document identifiers. No byte-deterministic build is claimed
without fixing/normalizing those fields. Preserve the actual reviewed PDF; do not
substitute a recompiled PDF under its hash.

The separately supplied historical-validator-execution directory preserves the
dated three-positive-ledger/32-negative-case execution referenced in Section 10,
including its inputs, outputs, failures and provenance. These are preceding
execution records, not a newly performed generator campaign or a new model review.


Degree entries in numerical ledgers and figures are values of the manuscript's
proved analytic formulas. Replaying them does not compute or certify an independent
minimal state-space realization. Continuous contour bounds are not certified by
the sampled numerical audit. The perturbation theorem is restricted to the stated
rational-inner, pole-free, disjoint-region and strict-margin hypotheses.
