B4_two_planes_fold -- scripts (Python 3.12, sympy 1.14, mpmath 1.3). See ../../report_B4_two_planes_fold.md.
  python sym_reduction.py            symbolic-q verification of (E2), (C1)-(C6), the Lyapunov bracket B, [kappa^3]H_q, g_2, g_3   (6 s)
  python verify_lyapunov.py          numerical sanity checks of every inequality in the proof along trajectories                 (90 s)
  python num_phi.py 4 5 10 30        kappa_f, kappa_Delta, kappa_L, u(kappa_f), T(kappa_f) ...                                    (20 s per q)
  python certify_neg.py 4 5 6        redundant rigorous interval-arithmetic certificate of H_q < 0 on (0, kappa_L]              (60 s for q=4)
  python margins.py / lemma_c_check.py / t_signchange.py   exploratory numerics (pre-proof)
  python write_report.py QMAX        regenerates the report
Logs: certify_4_100.log, certify_101_200.log (final runs); old_runs/ (runs before the z0 rounding fix, same outcomes).
