"""Run every script of this directory (and of reviewer/) in sequence, writing <name>.out,
propagating failures, and recording wall times in runtimes.txt.  Usage: python run_all.py [--fast]
(--fast skips scan_ac.py, checks_bounds.py, reviewer/rev_num.py and tables_ac.py)."""
import subprocess, sys, time, os
here = os.path.dirname(os.path.abspath(__file__))
fast = '--fast' in sys.argv
scripts = ['sym_riccati.py', 'sym_evenpart.py', 'sym_evenpart_ode.py', 'manuscript_checks.py',
           'scan_evenpart.py', 'checks_bounds.py', 'scan_ac.py', 'tables_ac.py',
           'reviewer/rev_sym.py', 'reviewer/rev_last.py', 'reviewer/rev_even.py', 'reviewer/rev_num.py']
slow = {'scan_ac.py', 'checks_bounds.py', 'reviewer/rev_num.py', 'tables_ac.py'}
lines = []
failed = []
for s in scripts:
    if fast and s in slow:
        continue
    d, f = os.path.split(os.path.join(here, s))
    t0 = time.time()
    with open(os.path.join(d, f[:-3] + '.out'), 'w', encoding='utf-8') as out:
        r = subprocess.run([sys.executable, f], cwd=d, stdout=out, stderr=subprocess.STDOUT)
    dt = time.time() - t0
    lines.append(f'{s:28s} exit={r.returncode} {dt:8.1f} s')
    print(lines[-1], flush=True)
    if r.returncode != 0:
        failed.append(s)
open(os.path.join(here, 'runtimes.txt'), 'w').write('\n'.join(lines) + '\n')
print('FAILED:', failed if failed else 'none')
sys.exit(1 if failed else 0)
