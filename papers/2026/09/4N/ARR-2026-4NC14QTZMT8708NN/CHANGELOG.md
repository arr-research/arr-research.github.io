# Final changes from the reviewed cycle-3 source

Lluis Eriksson. Prepared for ARR-2026-4NC14QTZMT8708NN, version 1. No publication is performed by this source package.

1. Added Theorem 2 and equations (28)–(36): complete exact inversion from chordal target delta, with squared target epsilon=delta², to minimum angular peak delay. Below the first nonzero-cap error, one isolated cubic root and a positivity endpoint constraint determine the inverse.
2. Proved all inverse target boundaries: minimum delay zero for squared targets at least 1/2, exactly one from e_1 up to 1/2, a unique delay above one for positive targets below e_1, and no finite attainment at zero. Included reflection, symmetry and transition equality.
3. Derived the elementary active inverse and transition target epsilon_c=v²/Q_c. Added the exact inactive fixture with squared target 35/123 and minimum delay (sqrt(15529)+9sqrt(53))/106. Retained all forward-law fixtures.
4. Distinguished error from squared error in prose and public JSON. Added mutually exclusive `--error` and `--error-squared` inverse targets and exact rational `--inverse-certificate` mode with root isolation.
5. Added a Rayleigh-quotient proof of the T=1 formula for self-containment. Qualified the symmetric formula by T>=1. The previous forward theorem and equation numbers (1)–(27) remain mathematically unchanged.
6. Retained the forward replay; added seven inverse symbolic groups, four exact fixtures, six exact target-boundary checks, a nonrational cubic isolation and twelve numerical round trips. Rationalized the numerical global peak to avoid subtracting nearly equal moduli; used scale-relative branch tolerances.
7. Replaced operational workspace paths with package-relative files and ordinary Python instructions. Preserved prior evidence byte for byte under `evidence/`, with the earlier separate review and original source hashes. Added requirements, manifest, refresh script and unified diff.

The former forward-law review applies to its historical source. A different agent in the same model family reviews the inverse delta separately. Neither self-replay nor internal agent review is external refereeing, and no ARR score is assigned here. Attribution and the bounded external-priority statement are preserved.
