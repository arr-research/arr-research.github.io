# Claim ledger

Status vocabulary: `PROVED` means a paper-level proof is in the manuscript;
`VERIFIED` adds an independent exact-arithmetic replay; `BOUNDARY` marks an
explicit limitation.

| ID | Claim | Status | Evidence |
|---|---|---|---|
| C1 | For a projective oracle family, the causal forward-query support equals its degree-k Hilbert function | PROVED | Theorem 3.1, Veronese annihilator proof |
| C2 | Compact transitive unitary orbits obey `J_x^k <= D_k Jbar_k` with minimal uniform constant `D_k` | PROVED | Lemma 4.1, constant leverage proof |
| C3 | Every Bavaresco-style general tester on a uniform finite subset obeys `P_succ <= min(1,D_k/M)` | PROVED | Theorem 4.2; the replay checks harmonic rank/leverage values, not the operator/tester theorem |
| C4 | Fixed-angle qubit ranks are `(k+1)^2`, `binom(k+2,2)`, and `1` on the interior, traceless, and central branches | PROVED, VERIFIED | Quadric Hilbert series and Fischer decomposition |
| C5 | Rank-one phase oracles in dimension `d` have generic support `binom(k+d-1,d-1)^2`, with the stated central and qubit-exceptional branches | PROVED, VERIFIED | Theorem 6.1; Segre coordinate ring and exact replay |
| C6 | The sphere and planar-axis Bell spectra are the stated Funk-Hecke and Fourier sums | PROVED, VERIFIED | Theorems 8.1 and 10.1 |
| C7 | Full-sphere purity and effective rank have the stated closed form | PROVED, VERIFIED | Proposition 8.2 and rational replay |
| C8 | Interior Bell tightness occurs only at `k=1,q^2=1/4`; no positive orbit reweighting restores it for `k>=2` | PROVED, VERIFIED | Theorem 9.1, Corollary 9.2 |
| C9 | Planar-axis support has ranks `2k+1`, `k+1`, and `1` on the three branches | PROVED, VERIFIED | Conic Hilbert function and Fourier spectrum |
| B1 | The Hilbert-function GEN cap holds for arbitrary nontransitive varieties | BOUNDARY: NOT CLAIMED | Constant leverage can fail without transitivity |
| B2 | The result covers controlled-U, U-dagger, postselection, or a changed oracle model | BOUNDARY: NOT CLAIMED | These resources require a different feature space |
| B3 | Every full-rank finite ensemble attains the rank cap | BOUNDARY: NOT CLAIMED | Equality needs the tester kernel/normalization certificate |
| B4 | The orbit-domination/tester mechanism is historically new | BOUNDARY: NOT CLAIMED | It is explicitly credited to prior covariant and general-tester work |

The exact verifier is diagnostic evidence for finite identities; it is not a
substitute for the general proofs.
