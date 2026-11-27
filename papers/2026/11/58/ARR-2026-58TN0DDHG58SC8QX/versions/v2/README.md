# Complete Classification of Positive-Slope Relative-Bound Equiangular Line Families, Exact Fixed-Angle Thresholds, Consecutive-Dimension Extensions, and Unconditional Leech $d_4(C) = 204$

**Author:** Lluis Eriksson  
**Date:** November 27, 2026 (`v2.0.0`)  
**AIRR Record:** [`ARR-2026-58TN0DDHG58SC8QX`](https://airr.science/papers/ARR-2026-58TN0DDHG58SC8QX/)  
**Target:** V. Djaljapayan, Z.-Q. Liao, and W.-H. Yu, *Real Equiangular Lines in Dimensions 18–20 and Sharp Fixed-Angle Bounds* (`arXiv:2611.34855v1`)  
**Standard:** `AIRR-FOUNDER-1.0` (MIT for code/Lean/certificates; CC-BY-4.0 for manuscript/figures)

## Summary of Main Breakthroughs
1. **Theorem 1 (Complete Classification of Positive-Slope Relative-Bound Seeds):** Proves $M/b = k(a+1)/(k+a)$ and the exact linear-in-$a$ criterion $L_k > M/b \iff a < s + s(s+1)/(k^2 - s - 1)$ ($s = \sqrt{k+3}$), classifying all nontrivial integer relative-bound seeds with positive Bukh–Cox slope: **exactly $k \in \{3, 5, 6, 7\}$ for $a = 3$** and **exclusively $k \in \{a^2 - 3, a^2 - 2\}$ for every odd $a \ge 5$**. Proves the exact rational constant $L_{a^2-3} = \frac{(a^2-2)(a+1)}{(a-1)(a+2)}$ and exact rational slope $\frac{a(a+1)}{(a-1)(a+2)(a^2+a-3)}$.
2. **Theorem 2 (Exact Alternating Bound, Seed-Eigenvector Extension, Six Sharp Families & Zero-Gap Contact):** Proves $\lambda_{\mathrm{alt}}(A) \in \{-3,-2,-1,0,1\}$ (sharpening $Q-2r$ to $Q-6$), replaces $r < t$ with $r \le b-1$, and constructs explicit $\{\pm 1\}^M$ seed eigenvectors $Sv = -av$ enabling odd-$t$ repetitions with constant Schur ratio $\rho = k/a$. Yields **four brand-new infinite families** ($k=3$: $q \ge 7$; $k=5$: $q \ge 155$, $q \ge 11$ for $q \equiv 3 \bmod 4$; $k=6$: $q \ge 161$, $q \ge 89$ for $q \equiv 1 \bmod 4$; $k=22$: $q \ge 8643$), sharpens both DLY Theorem 5.1 thresholds ($k=7$: `319 -> 245`; $k=23$: `5599 -> 5267`), and proves exact zero-gap adjacent contact $d_+^{(6)}+1 = d_-^{(7)}$ ($10 \mid Q$) and $d_+^{(22)}+1 = d_-^{(23)}$ ($112 \mid Q$).
3. **Theorem 3 (Consecutive-Dimension Extensions Beyond Bukh–Cox):** Upgrades DLY Theorem 5.2 (symmetric conference matrices) from a single dimension $d = mt - m/2$ to an entire consecutive interval of length $(\sqrt{m^2+2m}-m)t + O(1)$ for every even $t \ge 2$; generalizes DLY Proposition 5.3 to infinite $s \in \{2, 3\}$ relative-bound block windows for every odd $q \ge 5$ (catching exact Pell jumps at $q=15, d=25$ and $q=35, d=49$) and proves an exact $s \ge 4$ impossibility barrier.
4. **Theorem 4 (New in `v2.0.0` — Unconditional Leech $d_4(C) = 204$ and Five-Level Nested Chain):** Proves unconditionally—independently of the 23-Niemeier classification of $N(19) = 72$—that the fourth generalized Hamming weight of the $\mathrm{Co}_3$-invariant Leech $[276, 23, 100]$ code is $d_4(C) = 204$, eliminating all $420$ isomorphic $\mathrm{PG}(3, 2)$ constraint-satisfaction survivors at support $203$ via the universal fourth-moment integer inequality $t^4 - 4t^2 \ge -3\cdot\mathbf{1}_{t\text{ odd}}$, and explicitly constructs the four-normal section $V_{19} = \ker(y_a, y_{O_1}, y_b, y_{O_2})$ ($O_1 \cap O_2 = \{a, b\}$) of $72 = N(19)$ axes of exact rank $19$, extending the optimal nested Leech chain across all five dimensions $23 \to 19$ ($276 \to 176 \to 126 \to 90 \to 72$) before dropping to $56 < 57 = N(18)$ in $\mathbb{R}^{18}$.

## Verification & Replay
```bash
cd lean && lean -DwarningAsError=true EquiangularFixedAngleSharp.lean
cd .. && python verification/verify_paper106.py
pytest -q tests/test_verify_paper106.py
```
- **Lean 4.36.0:** 24/24 theorems, `0 sorry`, `0 Classical.choice`, `0 custom axioms`, `0 warnings`.
- **Zero-Float Certificates:** 20/20 SHA-256 certificates (`MANIFEST.json` SHA-256: `ae0fa91523864583d8626c7db9d4bd413a60db282f3a456b96d16f98f1f13c86`).
- **Tests:** 64/64 adversarial pytest checks passing.
