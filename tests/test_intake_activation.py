"""Opening must preserve unrelated secrets and fail before ambiguous config edits."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from services.intake.deploy.activate import atomic_write, replace_settings


class ActivationTests(unittest.TestCase):
    def test_only_opening_settings_change_and_literal_secrets_survive(self):
        original = '# preserved\nSMTP_PASSWORD="a $literal `text`"\nARR_INTAKE_OPEN=0\n'
        changed = replace_settings(original, {'ARR_INTAKE_OPEN':'1',
            'ARR_LAUNCH_APPROVAL_FILE':'/private/approval.json'})
        self.assertIn('SMTP_PASSWORD="a $literal `text`"\n', changed)
        self.assertTrue(changed.startswith('# preserved\n'))
        self.assertEqual(changed.count('ARR_INTAKE_OPEN='), 1)
        self.assertIn('ARR_INTAKE_OPEN=1\n', changed)
        with self.assertRaises(ValueError):
            replace_settings('ARR_INTAKE_OPEN=0\nARR_INTAKE_OPEN=1\n', {'ARR_INTAKE_OPEN':'1'})

    def test_failed_atomic_replacement_preserves_existing_configuration(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'intake.env'
            target.write_text('original\n')
            with patch.object(Path, 'replace', side_effect=OSError('simulated failure')):
                with self.assertRaises(OSError):
                    atomic_write(target, 'changed\n', 0o600)
            self.assertEqual(target.read_text(), 'original\n')


if __name__ == '__main__':
    unittest.main()
