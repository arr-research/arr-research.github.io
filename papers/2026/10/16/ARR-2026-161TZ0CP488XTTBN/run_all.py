"""Replay finite diagnostics. This does not formally verify the analytic proofs."""
from pathlib import Path
import hashlib, json, platform, subprocess, sys, time
import numpy, sympy

ROOT = Path(__file__).resolve().parent
SCRIPTS = [
    'verify_overlap.py', 'verify_two_runs.py', 'verify_erasure.py',
    'astra-independent-checks.py', 'astra-s8-checks.py',
    'astra-binary-plateau-checks.py',
]
results = []
for name in SCRIPTS:
    started = time.monotonic()
    proc = subprocess.run([sys.executable, '-X', 'utf8', str(ROOT / name)],
                          cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
    (ROOT / (name + '.replay.txt')).write_text(proc.stdout + proc.stderr, encoding='utf-8')
    entry = dict(script=name, returncode=proc.returncode,
                 elapsed_seconds=round(time.monotonic()-started, 3),
                 script_sha256=hashlib.sha256((ROOT/name).read_bytes()).hexdigest())
    if proc.returncode == 0:
        try:
            entry['reported_status'] = json.loads(proc.stdout)['status']
        except (ValueError, KeyError):
            entry['reported_status'] = 'unparseable'
    results.append(entry)
    print(json.dumps(entry), flush=True)

passed = all(x['returncode'] == 0 and x.get('reported_status') == 'PASS' for x in results)
report = dict(status='PASS' if passed else 'FAIL',
              python=platform.python_version(), numpy=numpy.__version__,
              sympy=sympy.__version__, results=results,
              scope='Finite exact and numerical diagnostics; not a formal proof checker.')
(ROOT/'replay-summary.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
raise SystemExit(0 if passed else 1)
