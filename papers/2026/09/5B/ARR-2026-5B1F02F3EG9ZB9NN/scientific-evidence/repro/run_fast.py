"""run_fast.py -- the fast verification subset (about 6 minutes; the full run is `python verify_certificates.py`,
about 8 minutes more for gamma_N9..N12, and `python reviewer/rev_B.py 9 10 11 12`).

Runs, in this order, writing <name>.out next to this file and the wall times to runtimes.txt:
  1. verify_certificates.py on a subset directory certs_fast/ (gamma_N3..N8, AB_costs, kappa6, all 13 all-d files)
  2. check_templates_explicit.py           (all 13 all-d files at explicit d = d0..d0+8; Hermitian convention test)
  3. crosscheck_horn_vs_hive.py            (hive LP vs explicit Horn LP vs 22-form formula)
  4. print_alld_certificates.py, kappa6_table.py   (the write-outs of Sections 5 and 6)
  5. reviewer/rev_A.py, rev_C.py, rev_E.py, rev_F.py, rev_B.py (default: N = 3..8 and AB_costs)
Every script exits with status 0 only if all its checks pass; this runner stops at the first failure.
Usage: python run_fast.py [--no-reviewer]
"""
import os, sys, shutil, subprocess, time
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sub = os.path.join(HERE, 'certs_fast')
if os.path.isdir(sub): shutil.rmtree(sub)
os.mkdir(sub)
for f in os.listdir('certs'):
    if f.startswith('alld_lower_') or f in ('AB_costs.json', 'kappa6_certificate.json') or any(f.startswith(f'gamma_N{N}.') for N in range(3, 9)):
        shutil.copy(os.path.join('certs', f), sub)
jobs = [('verify_certificates', [sys.executable, 'verify_certificates.py', sub]),
        ('check_templates_explicit', [sys.executable, 'check_templates_explicit.py']),
        ('crosscheck_horn_vs_hive', [sys.executable, 'crosscheck_horn_vs_hive.py']),
        ('print_alld_certificates', [sys.executable, 'print_alld_certificates.py']),
        ('kappa6_table', [sys.executable, 'kappa6_table.py'])]
if '--no-reviewer' not in sys.argv:
    jobs += [(f'reviewer_{n}', [sys.executable, os.path.join('reviewer', f'{n}.py')]) for n in ('rev_A', 'rev_C', 'rev_E', 'rev_F', 'rev_B')]
rt = open('runtimes.txt', 'w')
for name, cmd in jobs:
    t = time.time()
    with open(f'{name}.out', 'w', encoding='utf-8') as out:
        rc = subprocess.call(cmd, stdout=out, stderr=subprocess.STDOUT)
    line = f"{name}: exit {rc}, {time.time()-t:.1f} s"
    print(line, flush=True); rt.write(line + '\n'); rt.flush()
    if rc != 0: print('FAILED:', name); sys.exit(rc)
shutil.rmtree(sub)
print('ALL OK')
