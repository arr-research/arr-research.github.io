import unittest

from scripts.check_repository_safety import private_file, shell_input_lines


class RepositorySafetyTests(unittest.TestCase):
    def test_private_files_are_rejected_without_hiding_public_documents(self):
        for path in ('ops/.env', 'ops/.env.production', 'intake.env.before-update',
                     'backup/intake.sqlite3', 'backup/intake.sqlite3-wal',
                     'backup/intake.db', 'backup/snapshot.age', 'keys/id_ed25519',
                     'keys/credentials.pem'):
            with self.subTest(path=path):
                self.assertTrue(private_file(path))
        for path in ('.env.example', 'services/intake/.env.template',
                     'site/indexnow-key.txt', 'tests/test_private_accounts.py',
                     'docs/LEGAL_AND_COMPLAINTS.md', 'papers/record/metadata.json'):
            with self.subTest(path=path):
                self.assertFalse(private_file(path))

    def test_shell_interpolation_is_detected_in_literal_folded_and_inline_runs(self):
        for marker in ('|', '|-', '>', '>-'):
            with self.subTest(marker=marker):
                source = f'    - run: {marker}\n        echo "${{{{ inputs.paper_id }}}}"\n      env:\n        INPUT: ${{{{ inputs.paper_id }}}}\n'
                self.assertEqual(list(shell_input_lines(source)), [2])
        self.assertEqual(list(shell_input_lines('run: echo "${{ github.event.issue.title }}"')), [1])

    def test_env_binding_and_literal_runtime_variables_are_allowed(self):
        source = 'env:\n  PAPER_ID: ${{ inputs.paper_id }}\nsteps:\n  - run: |\n      echo "$PAPER_ID"\n    env:\n      VERSION: ${{ inputs.version }}\n'
        self.assertEqual(list(shell_input_lines(source)), [])
