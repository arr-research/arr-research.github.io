"""Rerun the fast subset of the author's and the reviewer's checks (13 September 2026).
Each command runs in its own directory (author/ or reviewer/); stdout+stderr go to out/<name>.out;
runtimes and exit codes are collected in out/runtimes.txt.  Usage: python run_fast.py [name ...]"""
import subprocess, sys, time, os
HERE = os.path.dirname(os.path.abspath(__file__))
JOBS = [
 # name, directory, command, timeout (s)
 ("omega_table",            "author",   "python omega_table.py", 120),
 ("cyclotomic_certify_4",   "author",   "python cyclotomic_certify.py 4", 120),
 ("cyclotomic_certify_8",   "author",   "python cyclotomic_certify.py 8", 120),
 ("cyclotomic_certify_9",   "author",   "python cyclotomic_certify.py 9", 120),
 ("cyclotomic_certify_16",  "author",   "python cyclotomic_certify.py 16", 120),
 ("cyclotomic_certify_25",  "author",   "python cyclotomic_certify.py 25", 300),
 ("cyclotomic_certify_27",  "author",   "python cyclotomic_certify.py 27", 300),
 ("cyclotomic_certify_32",  "author",   "python cyclotomic_certify.py 32", 300),
 ("cyclotomic_certify_49",  "author",   "python cyclotomic_certify.py 49", 900),
 ("cyclotomic_certify_81",  "author",   "python cyclotomic_certify.py 81", 1800),
 ("charp_2_2",              "author",   "python charp_order_exhaustive.py 2 2 4", 300),
 ("charp_2_3",              "author",   "python charp_order_exhaustive.py 2 3 8", 300),
 ("charp_3_2",              "author",   "python charp_order_exhaustive.py 3 2 9", 300),
 ("charp_2_4",              "author",   "python charp_order_exhaustive.py 2 4 16", 600),
 ("coset_gaps",             "author",   "python coset_meshulam_vs_omega.py", 300),
 ("composite_trinomials",   "author",   "python composite_trinomials.py 6 8 9 10 12 14 15", 600),
 ("exact_violations_16",    "author",   "python exact_check_firstorder_violations.py", 300),
 ("obstruction_mindist",    "author",   "python obstruction_min_distance_check.py 8 16 9", 900),
 ("obstruction_code_4",     "author",   "python first_order_obstruction_code.py 4", 300),
 ("obstruction_code_8",     "author",   "python first_order_obstruction_code.py 8", 300),
 ("obstruction_code_9",     "author",   "python first_order_obstruction_code.py 9", 300),
 ("firstorder_16",          "author",   "python operator_first_order_checks.py 16 100", 1800),
 ("zerosQ_cyclic_6",        "author",   "python zeros_exact_Q.py cyclic 6 1 6", 600),
 ("zerosQ_cyclic_10_m4",    "author",   "python zeros_exact_Q.py cyclic 10 1 4", 600),
 ("zerosQ_cyclic_14_m3",    "author",   "python zeros_exact_Q.py cyclic 14 1 3", 600),
 ("zerosQ_plane_4_m4",      "author",   "python zeros_exact_Q.py plane 4 1 4", 600),
 ("rev_gap_table",          "reviewer", "python gap_table.py", 300),
 ("rev_thmZ_construction",  "reviewer", "python thmZ_construction.py 4 8 9 16 25 27 32", 900),
 ("rev_clifford_exact",     "reviewer", "python clifford_exact.py 4 8 9", 1800),
 ("rev_codes_minweight",    "reviewer", "python codes_minweight.py", 1800),
 ("rev_zeros_spot_cyclic",  "reviewer", "python zeros_spot.py cyclic", 1800),
 ("rev_zeros_spot_plane",   "reviewer", "python zeros_spot.py plane", 1800),
 ("rev_flats_16_3",         "reviewer", "python flats_check.py 16 3", 900),
 ("rev_flats_16_4",         "reviewer", "python flats_check.py 16 4", 900),
 ("rev_thmA_2_2",           "reviewer", "python thmA_check.py 2 2 4", 300),
 ("rev_thmA_2_3",           "reviewer", "python thmA_check.py 2 3 8", 300),
 ("rev_thmA_3_2",           "reviewer", "python thmA_check.py 3 2 9", 300),
 ("rev_thmA_2_4",           "reviewer", "python thmA_check.py 2 4 16", 900),
]
sel = set(sys.argv[1:])
os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "runtimes.txt"), "a", encoding="utf-8") as rt:
    for name, d, cmd, to in JOBS:
        if sel and name not in sel: continue
        t0 = time.time()
        try:
            p = subprocess.run(cmd, shell=True, cwd=os.path.join(HERE, d), capture_output=True, text=True, timeout=to)
            out, code = p.stdout + p.stderr, p.returncode
        except subprocess.TimeoutExpired as e:
            out, code = (e.stdout or "") + "\n[TIMEOUT]", "TIMEOUT"
        dt = time.time() - t0
        open(os.path.join(HERE, "out", name + ".out"), "w", encoding="utf-8").write(out)
        line = f"{name:26s} {d:9s} exit={code} {dt:8.1f} s  ({cmd})"
        print(line); rt.write(line + "\n"); rt.flush()
