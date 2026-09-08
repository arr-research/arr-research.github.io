"""A live daemon is insufficient: the service must actually scan private bytes."""
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from flask import Flask
from services.intake.app import scanner_is_ready


class ScannerReadinessTests(unittest.TestCase):
    def test_daemon_file_rejection_is_unhealthy_and_probe_is_removed(self):
        with tempfile.TemporaryDirectory() as directory:
            app = Flask(__name__)
            app.config.update(QUARANTINE=directory, SCANNER='')
            commands = []

            def reject_file(command, **options):
                commands.append(command)
                self.assertTrue(Path(command[-1]).is_file())
                self.assertEqual(Path(command[-1]).parent, Path(directory))
                self.assertNotIn('--ping=1', command)
                self.assertEqual(options['timeout'], 4)
                return subprocess.CompletedProcess(command, 2)

            with app.app_context(), patch('services.intake.app.shutil.which', return_value='/usr/bin/clamdscan'), \
                 patch('services.intake.app.subprocess.run', side_effect=reject_file):
                self.assertFalse(scanner_is_ready())
            self.assertEqual(len(commands), 1)
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_scan_success_and_timeout_are_distinguished_without_leaving_probe(self):
        with tempfile.TemporaryDirectory() as directory:
            app = Flask(__name__)
            app.config.update(QUARANTINE=directory, SCANNER='')
            for result, expected in ((subprocess.CompletedProcess([], 0), True),
                                     (subprocess.TimeoutExpired('clamdscan', 4), False)):
                with app.app_context(), patch('services.intake.app.shutil.which', return_value='/usr/bin/clamdscan'), \
                     patch('services.intake.app.subprocess.run', side_effect=[result]):
                    self.assertEqual(scanner_is_ready(), expected)
                self.assertEqual(list(Path(directory).iterdir()), [])
