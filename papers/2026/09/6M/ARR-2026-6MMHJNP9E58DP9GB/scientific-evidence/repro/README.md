# Reproducibility package for "One Fold for Haar Oriented Two-Planes in Every Dimension n >= 6: A Phase-Space Proof through a Fano Factor, an Integrating Factor and the Threshold L_q = q(q-1)/8" (14 September 2026)

Layout:

- `author/` — verbatim copy of the author's working directory `cycle3/work/B4_two_planes_fold/` (scripts, JSON results,
  the certificate logs `certify_4_100.log` and `certify_101_200.log` covering 4 <= q <= 200, the earlier runs in `old_runs/`
  made before a rounding fix of z0 in `certify_neg.py`, the exploratory logs `num_phi_large*.log`, and `write_report.py`,
  which regenerates the working report). The scripts import each other by plain `import` (`num_phi.py` is imported by
  `verify_lyapunov.py`, `lemma_c_check.py`, `t_signchange.py`) and write JSON files in their own directory, so run them
  **from inside `author/`** (or from a copy, as `run_fast.sh` does).
- `reviewer/` — the adversarial reviewer's independent scripts and logs, copied unchanged from the review session:
  `rev_sym.py` (symbolic-q re-derivation of (E2), (C1)-(C6), the bracket B for symbolic c, the two derivative facts used
  in Steps 1-2, [kappa^3]H_q, g_2, g_3, G = S0^2 kappa H/4 to O(z^6)); `rev_num.py` (mpmath 50 digits: kappa_L < kappa_f,
  the inequalities of the proof on 300+200-point grids, T(kappa_f) = kappa_f^2 H'(kappa_f), sign changes of H, q = 2, 3,
  the Poisson identity) with its full log `rev_num.log` (q = 4..60, 80, 100, 150, 200, 400); `rev_fast.py` (30 digits:
  kappa_L < kappa_f and H(kappa_L) < 0 for q = 4..60, 80, ..., 1000; q = 2, 3); `certify_neg_copy.py` (byte-identical copy of
  `author/certify_neg.py`, rerun for q = 4, 10, 37, 60: `rev_certify.log`, `certify_neg_4_10_37_60.json`);
  `certify_neg_steps.py` (the same script patched to dump the node list; `rev_steps_q4.json` holds the 52,820 nodes for
  q = 4, `rev_certify_q4_steps.log`, `rev_certify_4.json`); `rev_spot.py` (80-digit plain-arithmetic spot checks of the
  q = 4 certificate: node chaining, three nodes, Lemma S on 39 points for q = 4, 10, S0(z_L^+) - 3/2). Run these
  **from inside `reviewer/`** (`rev_spot.py` reads `rev_steps_q4.json` from the current directory). The only
  modification is one marked line (`REPRO`) in `rev_spot.py`: the copy saved by the review session assigned its
  node-index list to `_`, so the per-node checks did not run; with the list restored the rerun reproduces the
  three-node values quoted in the review and in Section 6 of the paper.
- `run_fast.sh` — the fast reruns made for the manuscript. It copies `author/` and `reviewer/` to `logs/_work/`, runs
  the commands below there (so the verbatim directories are not modified), writes `logs/<name>.log` and the wall-clock
  times to `logs/timings.txt`, and deletes the scratch copies.

Dependencies: Python 3.12, `sympy` 1.14, `mpmath` 1.3. Everything labelled exact uses sympy with symbolic `q` or Python
`Fraction`; the certificate uses `mpmath.iv` (outward-rounded interval arithmetic, 40 digits) with the two floating-point
comparisons described in Section 6 of the paper; the remaining numerics are mpmath at 30-80 digits.

## Quick start (about 10 minutes)

    bash run_fast.sh      # writes logs/*.log and logs/timings.txt

## Commands, runtimes (one core, measured by run_fast.sh), expected output

| directory | command | s | role (paper section) | expected output |
|---|---|---|---|---|
| author | `python sym_reduction.py` | 5 | (E2) termwise, (E3) = (E2)', (C1)-(C6), B3 (8.2), the bracket B, [kappa^3]H_q, g_2, g_3 (Sections 2-3) | every line `OK`; `Lemma A bracket = q**2 - q + 1/4 + ...`; `[kappa^3] H_q = -4*(q**2 - q - 8)/(...)`; `z^3: -4*(q - 4)/(...)` |
| author | `python verify_lyapunov.py` | 7 | sanity checks of every inequality of the proof (Section 7) | for q = 4, 5, 6, 10, 30, 60: `(a)...(e)` all `True`, `identity vs FD rel.err` <= 3e-57; q = 2, 3: all `True` |
| author | `python num_phi.py 4 5 6 10` | 64 | table values (Section 7) | `"nH": 1`, `kappa_f` 4.415714051354579, 7.613543394072212, 10.254633771964322, 19.373531911973124; `kappa_L` 3.4690511954905277, ... |
| author | `python certify_neg.py 4 5 6` | 64 | interval certificate (Section 6) | `"ok": true` with `nsteps` 52820, 10377, 5139 and `max_G_upper` -8.818e-08, -1.110e-06, -3.478e-06 |
| author | `python lemma_c_check.py` | 1 | exploratory (pre-proof estimate Lemma C) | `Lemma C covers ... 0.3278 q` (q=4) ... `0.4426 q` (q=100000), no assertion failure |
| author | `python t_signchange.py` | 141 | exploratory (sign change of T) | one sign change of T per q, at 4.11 (q=4), ..., 119.5 (q=60) |
| author | `python margins.py 4 10` | 1 | exploratory (Fano margins) | `kappa_L` 3.469051195490529 (q=4), 15.38499902045209 (q=10) |
| reviewer | `python rev_sym.py` | 177 | independent symbolic re-derivation (Sections 2-3) | every identity `OK`; `Lemma L bracket B OK`; `G - S0^2 kappa H/4 to O(z^6): 0` |
| reviewer | `python rev_fast.py` | 21 | kappa_L < kappa_f, H(kappa_L) < 0 up to q = 1000; q = 2, 3 | final line `... for all q in 4..60, 80,100,150,200,400,1000: True`; `q=2: min H ... = 5.553e-06`, `q=3: ... 4.765e-07` |
| reviewer | `python rev_num.py 4 5 6` | 18 | independent grid checks (Section 7) | `"pre": [true, true, true], "post": [true, true, true]`, `"nsignchanges_H": 1`, `T_eq_k2Hp` <= 1e-25; q = 2, 3 line `True`; Poisson identity residuals ~1e-49 |
| reviewer | `python rev_spot.py` | 3 | 80-digit spot checks of the q = 4 certificate (Section 6) | `nsteps 52820`, `max |a_{i+1} - b_i| ...: 0.0`; node 0: `Ga(cert)=-8.818329e-08`, `M(b)=6.712938e-02`, `sup|G'| sampled=5.291094e-06`, `G(a)+(b-a)M = -4.409077e-08 <0: True`; node 52819: `Ga(cert)=-8.096744e-03`, `G(a) 80-digit=-8.109925e-03`; `Ga>=G(a): True`, `M>=sup: True` at every node; Lemma S `True` for q = 4, 10; `S0(zL_plus) - q(q-1)/8 = 1.414868816e-7` |
| reviewer | `python certify_neg_copy.py 4` | 59 | byte-identical rerun of the certificate | identical to the author's q = 4 line (`nsteps 52820`, `max_G_upper -8.818328881930461e-08`) |

Not rerun (slow, original logs kept): `author/certify_neg.py` for 7 <= q <= 200 (`certify_4_100.log`, `certify_101_200.log`,
about 1.75 h in total, every line `"ok": true`); `reviewer/rev_num.py` with its default list (q = 4..60, 80, ..., 400;
`rev_num.log`). In `rev_num.log` the first entry of `"post"` is `false` for some q: it is the test `h >= 0` evaluated *at*
the bisected zero kappa_f itself, where h is at rounding level (about 1e-30) and may come out negative; the substantive
checks (Q > 0 and the derivative of e^{c tau} Q positive on [kappa_f, 4q+60], one sign change of H) are `true` for every q.

Nothing here was published or pushed; `cycle2/arr` was not modified.
