#!/usr/bin/python3
"""Minimal on-host operational check; never prints SMTP or author data."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import urllib.request


def main():
    checks = {}
    checks['encrypted_volume_mounted'] = os.path.ismount('/srv/airr-private')
    for unit in ('airr-intake.service', 'caddy.service', 'clamav-daemon.service', 'clamav-freshclam.service', 'airr-intake-maintenance.timer', 'airr-intake-mail.timer'):
        checks[unit] = subprocess.run(['systemctl', 'is-active', '--quiet', unit], check=False).returncode == 0
    try:
        with urllib.request.urlopen('http://127.0.0.1:8000/readyz', timeout=10) as response:
            checks['application_readiness'] = response.status == 200
    except (OSError, ValueError):
        checks['application_readiness'] = False
    if checks['encrypted_volume_mounted']:
        database = Path('/srv/airr-private/instance/intake.sqlite3')
        with sqlite3.connect('file:' + str(database) + '?mode=ro', uri=True) as db:
            checks['mail_delivery_state'] = db.execute("SELECT COUNT(*) FROM mail_outbox WHERE state IN ('uncertain','sending')").fetchone()[0] == 0
        latest = sorted(Path('/var/backups/airr').glob('airr-*.tar.gz.age'))
        checks['local_encrypted_backup_recent'] = bool(latest) and datetime.now(timezone.utc).timestamp() - latest[-1].stat().st_mtime < 30 * 3600
    status = {'checked_at': datetime.now(timezone.utc).isoformat(), 'checks': checks, 'ok': all(checks.values())}
    state_dir = Path('/var/lib/airr-monitor')
    state_dir.mkdir(mode=0o700, exist_ok=True)
    (state_dir / 'status.json').write_text(json.dumps(status, indent=2))
    print(json.dumps(status))
    # An operator may enable notifications after inspecting this dry result.
    # A single incident fingerprint suppresses repeated identical alerts.
    if '--notify' in sys.argv and checks['encrypted_volume_mounted']:
        failed = sorted(k for k, v in checks.items() if not v)
        fingerprint = hashlib.sha256(json.dumps(failed).encode()).hexdigest()
        marker = state_dir / 'last-notified'
        if failed and (not marker.exists() or marker.read_text() != fingerprint):
            for line in Path('/etc/airr-intake/intake.env').read_text().splitlines():
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    os.environ[key] = value
            sys.path.insert(0, '/opt/airr-intake/current')
            from services.intake.app import app, send_mail
            from email.message import EmailMessage
            with app.app_context():
                message = EmailMessage()
                message['From'] = 'AIRR.SCIENCE <' + app.config['SMTP_FROM'] + '>'
                message['To'] = app.config['OPERATOR_EMAIL']
                message['Subject'] = 'AIRR server: operational check needs attention'
                message.set_content('The following server checks need attention:\n' + '\n'.join(failed) + '\n\nNo manuscript or author data is included. Review the server and provider logs before retrying deliveries.')
                if send_mail(message):
                    marker.write_text(fingerprint)
        if not failed:
            marker.unlink(missing_ok=True)
    return 0 if status['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
