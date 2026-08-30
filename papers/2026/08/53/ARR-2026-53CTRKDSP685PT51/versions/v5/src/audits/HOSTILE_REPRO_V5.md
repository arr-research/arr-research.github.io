# Hostile reproducibility audit — v5

Verdict: **PASS for the declared computational checks**. The scripts test formulas and finite-dimensional diagnostics; they do not substitute for the proofs.

## Clean replay

The following sequence completed successfully in the pinned Python environment:

1. `verify_saturation_law.py`
2. `finite_sample_phase_diagram.py`
3. `verify_v3_additions.py`
4. `radial_phase_transition.py`
5. `spectral_lexicography.py`
6. `verify_v4_additions.py`
7. `joint_spectral_resolution.py`
8. `verify_v5_additions.py`

The v5 verifier checks the joint-threshold constants, 117 randomized deterministic-hierarchy cases, and the angular variance formula for \(p=1,2\). The joint diagnostic evaluates 56 radii with \(\eta<1\); its last projector error is approximately \(3.65\times10^{-8}\).

## Stable generated artifacts

- `joint_spectral_resolution.pdf`: `1dd16ea599c78a46645a544641274b0e8236d7d2424572db932a5c25b68d4eb5`
- `joint_spectral_resolution.json`: `a961a7b695707d24315473aa228e2690d2a84621cff286238cc3319276e4a493`

All earlier v2--v4 figure and certificate hashes remained unchanged under replay.

## PDF build audit

- four settled LuaLaTeX passes produced identical bytes on the last two passes;
- final SHA-256: `f90a308999b00697245dc87b0588efa162f8e380ed69f5c7454eff660b381e0d`;
- 660,109 bytes, 33 A4 pages, unencrypted;
- no overfull boxes, underfull boxes, undefined references, or LaTeX/package warnings in the settled log;
- all 33 pages were rasterized at 110 dpi and visually inspected through four contact sheets, with page 20 separately checked after the measurable-rotation correction; and
- no clipping, overlap, missing glyphs, or malformed figures were observed.

The local MiKTeX installation emits only its external update-status notice; that notice is not a manuscript or layout warning.
