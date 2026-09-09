# Runs every verification script in this directory, records stdout to <name>.out and wall time to runtimes.txt.
import subprocess, sys, time, pathlib
scripts=["sym_check.py","check_formula.py","induction_check.py","tail_cases.py","boundary_exact.py","h6_remark63_check.py","chain_numerics.py","workshop_recheck.py","verify_signs.py"]
here=pathlib.Path(__file__).parent
lines=[]
failed=[]
for s in scripts:
    t0=time.time()
    r=subprocess.run([sys.executable,"-X","utf8",str(here/s)],capture_output=True,text=True,encoding="utf-8",cwd=here)
    dt=time.time()-t0
    if r.returncode: failed.append(s)
    (here/(s[:-3]+".out")).write_text(r.stdout+(("\n[stderr]\n"+r.stderr) if r.stderr else ""))
    lines.append(f"{s:22s} exit={r.returncode} wall={dt:8.1f} s")
    print(lines[-1],flush=True)
(here/"runtimes.txt").write_text("\n".join(lines)+"\n")

if failed:
    print("FAILED:", ", ".join(failed))
    raise SystemExit(1)
print("ALL CHECKS PASSED")
