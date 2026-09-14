# Reproducibility package for "Exact Hive Certificates for the Balanced-Inertia Stability Constants (N = 3 to 12) in Every Dimension, the (A_N,B) Cost Law, and the Twenty-Two-Form Six-Level Cost Formula" (13 September 2026)

Python 3.12.6 on Windows 11. The verifiers (`verify_certificates.py`, `check_templates_explicit.py`,
`print_alld_certificates.py`, `kappa6_table.py`) use only the standard library (`fractions`); the
generators, the crosscheck and the reviewer's LP tools need `numpy` 2.5.1 and `scipy` 1.18.0 (HiGHS);
`reviewer/rev_E.py` needs `pycddlib`. Every script exits with status 0 only if all of its checks pass.
No proof step depends on floating point: the generators use HiGHS only to *find* rational objects, which
are then re-verified exactly before being written; the verifiers never call an LP solver.

## Provenance

The historical model identities, separate-agent roles and execution chronology below are supplied by the author, not authenticated by the current review. This corrected candidate changes documentation only; certificate and Python-source bytes are preserved. Fresh execution evidence is referenced in the candidate PROVENANCE.json.


* `certs/` — the certificates, copied unchanged from the author agents' working directory
  `cycle2/work/A4_exact_certificates/certs/` (2026-09-12/13); `gamma_N5..N7.json` were gzip-compressed
  here (the verifiers read `.json` and `.json.gz` alike).
* `hive_exact.py`, `geometry.py`, `gen_gamma.py`, `gen_AB_costs.py`, `gen_kappa6.py`, `stable_templates.py`,
  `alld_family.py`, `uz_kappa_scan.py`, `padding_scan.py`, `verify_certificates.py`,
  `check_templates_explicit.py` — copied unchanged from the same working directory. `geometry.py` is
  byte-identical to the file of the ARR-2026-54Q3HMFJ0Z8CZB4T record (checked with `cmp`).
* `crosscheck_horn_vs_hive.py` — copied with one line changed: the `sys.path` entry pointing to the cycle-1
  scratch directory was removed, and `check_horn_lp.py` (the explicit Horn LP of cycle 1, unchanged) was
  copied next to it.
* `logs/` — the author agents' logs (`verify_final.log`, `verify_run1.log`, `verify_run2.log`,
  `check_templates_explicit.log`, `crosscheck.log`, `gen_*.log`, `alld_family_*.log`, `stable_*.log`,
  `uz_kappa_scan.log`) and the superseded (non-tight, 437/270) N = 10 all-d file.
* `reviewer/rev_lib.py`, `rev_A.py`, `rev_B.py`, `rev_C.py`, `rev_E.py`, `rev_F.py` — the independent
  adversarial reviewer's scripts (2026-09-13), unchanged except that the two absolute paths (the reviewer's
  scratchpad and the author's working directory) were replaced by paths relative to the file (lines marked
  `# (repro copy: ...)`). `reviewer/rev_B_9_10_11.log`, `rev_B_12.log`, `author_verify.log` are the reviewer's
  own logs.
* `print_alld_certificates.py`, `kappa6_table.py`, `run_fast.py` — written for the manuscript.

## Certificates (sizes)

| file | size | uncompressed | content |
|---|---|---|---|
| `gamma_N3.json`, `gamma_N4.json` | 7.6 kB, 36 kB | – | hive primal at every pair of W_N with D_* > 0, hive dual at the two minimisers |
| `gamma_N5.json.gz` … `gamma_N7.json.gz` | 12 kB, 36 kB, 104 kB | 140 kB, 411 kB, 1.1 MB | same |
| `gamma_N8.json.gz` … `gamma_N12.json.gz` | 246 kB, 527 kB, 1.0 MB, 1.9 MB, 3.3 MB | 2.6, 5.6, 11, 21, 37 MB | same |
| `AB_costs.json` | 230 kB | – | 34 entries, hive primal and dual each ((A_N,B) N = 3..14; (u_3,z_N) N = 6..12; paddings) |
| `kappa6_certificate.json` | 11 kB | – | 22 forms, chambers (rays, witnesses, global Horn duals) |
| `alld_lower_*.json` (12 active files) | 0.5–1.3 kB | – | all-d template certificates (AB N = 3..6; UZ N = 7..12; `_fam`/`_lean` = structured family, others = generic search) |

In `gamma_N*.json` the field `kappa_upper` (= sum of the stored s) is certified for every pair; the field
`kappa` is certified (by the stored dual) only at the pairs listed in `minimizers` — for the other pairs it
records the generator's dual value, which the verifiers do not check (the dual was not stored to keep the
files small). Formats are documented in the docstrings of `gen_gamma.py`, `gen_AB_costs.py`, `gen_kappa6.py`,
`stable_templates.py`.

## Commands (run from this directory)

    python verify_certificates.py            # full exact replay of every certificate; ~7.5 min; "TOTAL: 0 failures"
    python check_templates_explicit.py       # all-d templates at explicit d = d0..d0+8, convention test; 18 s; "ALL OK: True"
    python crosscheck_horn_vs_hive.py        # hive LP vs explicit Horn LP vs 22-form formula; 8 s
    python print_alld_certificates.py        # the write-outs of Section 5; "ALL OK"
    python kappa6_table.py                   # Table 2 of Section 6; "OK"
    python run_fast.py                       # the fast subset below (~6.5 min); writes <name>.out and runtimes.txt
    python reviewer/rev_B.py 9 10 11 12      # reviewer's checker on the large files (20, 44, 88, 139 s); "problems: NONE"
    python reviewer/rev_A.py                 # conventions: Horn lists vs LR, hive LP vs Horn LP, author's duals judged by the reviewer's checker
    python reviewer/rev_C.py                 # all-d templates: symbolic + explicit d, recursion + LR, write-outs for N = 6, 7
    python reviewer/rev_E.py                 # kappa_6: forms, rays (pycddlib + brute force), witnesses, duals, sampling
    python reviewer/rev_F.py                 # reviewer's float hive LP at (u_3,z_N), (A_N,B), paddings; D_* by the record's definition
    python gen_gamma.py 7                    # regenerate certs/gamma_N7.json (12 s); N = 8..12: 33, 73, 159, 299, 607 s
    python gen_AB_costs.py                   # regenerate certs/AB_costs.json (0.7 s)
    python gen_kappa6.py                     # regenerate certs/kappa6_certificate.json (106 s)
    python alld_family.py 7 7 2 UZ           # regenerate the structured-family all-d certificate (writes certs/alld_lower_UZ_N7_fam.json)
    python alld_family.py 10 10 2 UZ --lean  # N = 10 (18 s); 11: --lean --k1max 7 (74 s); 12: --lean --k0 1,2,3 (2 s); AB N = 3..6: "alld_family.py N N 2 AB"
    python uz_kappa_scan.py                  # exact kappa_{2N}(u_3,z_N), N = 6..16 (0.4 s)

`run_fast.py` executes: `verify_certificates.py` on the subset `gamma_N3..N8` + `AB_costs` + `kappa6` + all
12 active all-d files, `check_templates_explicit.py`, `crosscheck_horn_vs_hive.py`, the two manuscript scripts, and
`reviewer/rev_A.py`, `rev_C.py`, `rev_E.py`, `rev_F.py`, `rev_B.py` (default range N = 3..8 and `AB_costs`).

## Measured wall times (rerun of 2026-09-13 for the manuscript, `runtimes.txt`; `.out` files included)

| step | time | final line |
|---|---|---|
| `verify_certificates.py` (fast subset) | 143.1 s | `TOTAL: 0 failures` |
| `check_templates_explicit.py` | 17.8 s | `ALL OK: True` |
| `crosscheck_horn_vs_hive.py` | 8.2 s | `failures = 0` on both random-spectra lines |
| `print_alld_certificates.py` | 0.1 s | `ALL OK` |
| `kappa6_table.py` | 0.1 s | `... all chambers rank 5.  OK` |
| `reviewer/rev_A.py` | 2.4 s | `kappa_7 padded example 74/7 ... kappa_8 padded 73/7 ...` (all counts/diffs printed) |
| `reviewer/rev_C.py` | 17.6 s | `refl sanity d=7: max |kappa(lam) - kappa(-lam^rev)| = 3.1e-15` |
| `reviewer/rev_E.py` | 176.4 s | `2000 random spectra with zero gaps: max |Horn LP - max of 22 forms| = 1.1e-14` |
| `reviewer/rev_F.py` | 1.3 s | padded kappa_d lines for N = 6, 7, 10 |
| `reviewer/rev_B.py` (N = 3..8, AB) | 14.8 s | `AB_costs.json: 34 entries; problems: NONE` |

Author-side full runs (logs in `logs/`): `verify_final.log` 450.8 s, 0 failures; the reviewer's re-run of
the same verifier (`reviewer/author_verify.log`) 438.5 s, 0 failures; `check_templates_explicit.log` 18.2 s;
`crosscheck.log` 6.2 s. Generation of everything took about 40 minutes (gen_gamma N = 10..12 about 18 min; the
two generic template searches of `stable_templates.py` about 15 min, superseded by `alld_family.py`).
