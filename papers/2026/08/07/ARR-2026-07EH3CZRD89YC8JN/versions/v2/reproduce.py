"""Run the documented numerical replay in a new directory outside this package."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
import shutil
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True,
                        help='New output directory outside the preserved package')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    output = args.output.resolve()
    if output == root or root in output.parents or output in root.parents:
        parser.error('Output must be outside the package and cannot be its ancestor.')
    if output.exists():
        parser.error('Output already exists; use a new directory to preserve past runs.')
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    now = lambda: datetime.now(timezone.utc).isoformat()
    source = root/'scientific-source'
    overlay = root/'proposed-verification-overlay/verification/verify_calibration_memory.py'
    inputs = sorted(p for p in source.rglob('*') if p.is_file()) + [overlay, Path(__file__).resolve()]
    before = {str(p.relative_to(root)): sha(p) for p in inputs}
    output.mkdir(parents=True, exist_ok=False)
    record = {'started_at': now(), 'python': sys.version, 'executable': sys.executable,
              'platform': platform.platform(), 'input_hashes': before, 'commands': [],
              'scope': 'Numerical formula and sampled falsification replay. No continuous contour certificate, independent minimal realization, or historical execution authentication.'}
    exit_code = 1
    try:
        record['packages'] = {name: importlib.metadata.version(name)
                              for name in ['numpy', 'scipy', 'matplotlib']}
        scratch = output/'scratch'
        shutil.copytree(source, scratch, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        shutil.copy2(overlay, scratch/'verification/verify_calibration_memory.py')
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', MPLBACKEND='Agg',
                   MPLCONFIGDIR=str(output/'matplotlib-config'))
        for name, script in [('generator', 'research/calibration_memory_certificate.py'),
                             ('validator', 'verification/verify_calibration_memory.py')]:
            command = [sys.executable, '-B', script]
            started = now()
            result = subprocess.run(command, cwd=scratch, env=env, capture_output=True)
            (output/(name+'.stdout')).write_bytes(result.stdout)
            (output/(name+'.stderr')).write_bytes(result.stderr)
            record['commands'].append({'command': command, 'cwd': str(scratch),
                                       'started_at': started, 'finished_at': now(),
                                       'exit_code': result.returncode})
            if result.returncode:
                raise RuntimeError(name+' failed; preserved stdout/stderr contain the result.')
        record['generated_files'] = {str(p.relative_to(scratch)): sha(p)
                                     for p in sorted(scratch.rglob('*')) if p.is_file()
                                     and (str(p.relative_to(scratch)) not in
                                          {str(q.relative_to(source)) for q in source.rglob('*') if q.is_file()}
                                          or sha(p) != sha(source/p.relative_to(scratch)))}
        exit_code = 0
    except Exception as error:
        record['failure'] = type(error).__name__+': '+str(error)
    finally:
        record['finished_at'] = now()
        record['input_bytes_unchanged'] = all(p.is_file() and sha(p) == before[str(p.relative_to(root))] for p in inputs)
        if not record['input_bytes_unchanged']:
            exit_code = 1
        record['exit_code'] = exit_code
        (output/'RESULT.json').write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'exit_code': exit_code, 'result': str(output/'RESULT.json')}))
    return exit_code


if __name__ == '__main__':
    raise SystemExit(main())
