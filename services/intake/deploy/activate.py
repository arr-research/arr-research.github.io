"""Open an installed pilot using an evidenced, explicitly authorized record.

Run with the intake virtualenv as root. Never creates an operator, changes a
password, sends a message, or restores a database. Failure closes reception
again while preserving any case received during the attempted activation.
"""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import time
import urllib.error
import urllib.request

try:
    from .upgrade import BACKGROUND, MONITOR, pause_background, resume_background, run, unit_state
except ImportError:
    from upgrade import BACKGROUND, MONITOR, pause_background, resume_background, run, unit_state


def replace_settings(contents, settings):
    lines = contents.splitlines()
    for key, value in settings.items():
        matches = [i for i, line in enumerate(lines) if line.startswith(key + '=')]
        if len(matches) > 1:
            raise ValueError('Duplicate configuration key: ' + key)
        line = key + '=' + value
        if matches:
            lines[matches[0]] = line
        else:
            lines.append(line)
    return '\n'.join(lines) + '\n'


def atomic_write(path, contents, mode):
    temporary = path.with_name(path.name + '.activation-next')
    with temporary.open('x', encoding='utf-8') as stream:
        os.chmod(temporary, mode)
        stream.write(contents)
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def status(path):
    try:
        with urllib.request.urlopen('http://127.0.0.1:8000' + path, timeout=10) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('commit')
    parser.add_argument('record', type=Path)
    args = parser.parse_args()
    assert re.fullmatch('[0-9a-f]{40}', args.commit)
    assert os.geteuid() == 0 and os.path.ismount('/srv/airr-private')
    os.umask(0o077)
    current = Path('/opt/airr-intake/current').resolve()
    assert current.name == args.commit, 'Unexpected installed version'
    record = json.loads(args.record.read_text(encoding='utf-8'))
    assert isinstance(record, dict)
    # Verify that the selected contact really is public before recording it as such.
    contact = record['contact_verification']
    assert contact['url'] == 'https://airr.science/contact/'
    with urllib.request.urlopen(contact['url'], timeout=30) as response:
        published = response.read().decode('utf-8')
    assert all(part in published for part in contact['required_text'])
    assert contact['required_text'], 'Missing contact evidence'
    env_path = Path('/etc/airr-intake/intake.env').resolve()
    original = env_path.read_text()
    values = {key: value.strip().strip('\"\'') for line in original.splitlines()
              if '=' in line and not line.lstrip().startswith('#')
              for key, value in [line.split('=', 1)]}
    assert values.get('ARR_INTAKE_OPEN', '0') == '0'
    approval = Path('/srv/airr-private/launch-approval.json')
    assert not approval.exists(), 'Inspect the existing record before replacing it'
    assert status('/readyz') == 200 and status('/account/register') == 503
    environment = os.environ.copy()
    environment.update(values)
    environment['ARR_LAUNCH_APPROVAL_FILE'] = str(args.record.resolve())
    # Execute the application's actual gate as the service user, including MFA.
    check = "from services.intake.app import create_app; a=create_app(); c=a.app_context(); c.push(); assert a.extensions['editorial']['launch_approved']()"
    subprocess.run(['runuser', '-u', 'airr-intake', '--preserve-environment', '--',
                    '/opt/airr-intake/venv/bin/python', '-c', check],
                   cwd=current, env=environment, check=True, stdout=subprocess.DEVNULL)
    run('python3', str(current / 'services/intake/deploy/monitor.py'))
    assert json.loads(Path('/var/lib/airr-monitor/status.json').read_text())['ok']
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    recovery = Path('/srv/airr-private') / ('activation-' + stamp)
    recovery.mkdir(mode=0o700)
    atomic_write(recovery / 'intake.env.before', original, 0o600)
    timers = [unit + '.timer' for unit in [MONITOR, *BACKGROUND]
              if unit_state(unit + '.timer') == 'active']
    assert len(timers) == 5, 'All background timers must be active'
    changed = False
    try:
        pause_background(timers)
        atomic_write(approval, json.dumps(record, ensure_ascii=False, indent=2) + '\n', 0o644)
        updated = replace_settings(original, {'ARR_INTAKE_OPEN':'1',
            'ARR_LAUNCH_APPROVAL_FILE':str(approval)})
        changed = True
        atomic_write(env_path, updated, 0o600)
        run('systemctl', 'restart', 'airr-intake.service')
        for _ in range(30):
            try:
                if status('/readyz') == 200 and status('/account/register') == 200:
                    break
            except OSError:
                pass
            time.sleep(1)
        assert status('/readyz') == 200 and status('/account/register') == 200
        assert status('/submit') == 200 and status('/login') == 200
    except Exception:
        if changed:
            atomic_write(env_path, original, 0o600)
            if approval.exists():
                approval.replace(recovery / 'failed-approval.json')
            run('systemctl', 'restart', 'airr-intake.service')
        raise
    finally:
        resume_background(timers)
    run('python3', str(current / 'services/intake/deploy/monitor.py'))
    health = json.loads(Path('/var/lib/airr-monitor/status.json').read_text())
    proof = {'opened_at':datetime.now(timezone.utc).isoformat(), 'commit':args.commit,
             'registration':status('/account/register'), 'readiness':status('/readyz'),
             'monitor_ok':health['ok'], 'approval_file':str(approval),
             'recovery_directory':str(recovery), 'database_restored':False}
    atomic_write(recovery / 'activation.json', json.dumps(proof, indent=2) + '\n', 0o600)
    print(json.dumps(proof))
    if not health['ok']:
        # Closing never restores an old DB: new cases must survive an incident.
        try:
            pause_background(timers)
            atomic_write(env_path, original, 0o600)
            approval.replace(recovery / 'failed-approval.json')
            run('systemctl', 'restart', 'airr-intake.service')
        finally:
            resume_background(timers)
        raise RuntimeError('Reception closed again after a failed operational check')


if __name__ == '__main__':
    main()
