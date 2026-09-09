"""Optional longer reviewer checks (not part of run_all.py): adversarial.py (2708 exact boundary points, 400 matrices)
and lp_checks.py (5400 float Horn-LP points + uniqueness scans). Run: python run_extra.py  -> logs/, logs/timings_extra.txt"""
import subprocess, sys, time, os
os.chdir(os.path.dirname(os.path.abspath(__file__))); os.makedirs("logs", exist_ok=True)
with open("logs/timings_extra.txt", "w") as T:
    for name in ("adversarial", "lp_checks"):
        t0 = time.time()
        with open(f"logs/{name}.log", "w") as L:
            rc = subprocess.call([sys.executable, name + ".py"], stdout=L, stderr=subprocess.STDOUT)
        T.write(f"{name:24s} rc={rc}  {time.time()-t0:7.1f} s\n"); T.flush()
    T.write("DONE\n")
