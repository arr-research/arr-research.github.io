# Candidate-2 verification supplement

This supplement belongs to the author-side repair of B4. It is not an independent assessment of the revised PDF. The received `author/` and `reviewer/` directories and their logs remain unchanged.

- `verify_lyapunov_60.py` sets `mp.dps = 60` after importing `num_phi` and prints the effective precision before running.
- `certify_neg_outward.py` evaluates the ratio condition, the deliberately lowered continuation start, and the final mean-value acceptance expression with outward-rounded intervals. A step is accepted only when the interval upper endpoint is negative.

Fresh candidate-2 logs are stored in `fresh-20260914/`. The corrected certificate was rerun for q=4,10,37,60. The received all-q logs for q=4,...,200 were not replayed in full with this corrected control logic; the analytic proof of Theorem 4.1 does not depend on the certificate.
