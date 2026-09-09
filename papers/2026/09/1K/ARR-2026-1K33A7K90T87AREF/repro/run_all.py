"""Reruns for the A2 manuscript. Run from the repro/ directory: python run_all.py
Writes logs/<name>.log and logs/timings.txt. Requires numpy, scipy, sympy (my_cert/rank_test/rank_more also import
the author's modules from this directory)."""
import subprocess, sys, time, os
os.chdir(os.path.dirname(os.path.abspath(__file__))); os.makedirs("logs", exist_ok=True)
jobs = [("lr", ["lr.py"]), ("verify_mn2_8", ["verify_mn2.py", "8"]), ("layer_chain_13_300", ["layer_chain.py", "13", "300"]),
        ("my_construct", ["my_construct.py"]), ("rank_test", ["rank_test.py"]), ("rank_more", ["rank_more.py"]),
        ("my_cert", ["my_cert.py"]), ("symbolic", ["symbolic.py"]), ("nonunique_check", ["nonunique_check.py"]),
        ("d5_dominated_terms", ["d5_dominated_terms.py"]),
        ("exact_rank4_matrix", ["exact_rank4_matrix.py"]), ("coverage_exact_10_40", ["coverage_exact.py", "10", "40"]),
        ("pieri_triples_search_9", ["pieri_triples_search.py", "9"]), ("taller_check_horn", ["taller_check_horn.py"])]
with open("logs/timings.txt", "w") as T:
    for name, args in jobs:
        t0 = time.time()
        with open(f"logs/{name}.log", "w") as L:
            rc = subprocess.call([sys.executable] + args, stdout=L, stderr=subprocess.STDOUT)
        T.write(f"{name:24s} rc={rc}  {time.time()-t0:7.1f} s\n"); T.flush()
    T.write("DONE\n")
if os.path.exists("checks-horn.json"): os.replace("checks-horn.json", "logs/taller_check_horn.json")
