"""Offsite boundaries: encrypted inputs, integrity, transfer limits and stale alerts."""
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from services.intake.deploy import offsite, monitor


class OffsiteTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.now = datetime(2026, 9, 7, 20, 0, tzinfo=timezone.utc)
        self.clock = patch.object(offsite, 'utcnow', return_value=self.now)
        self.clock.start()
        self.settings = {'enabled':True, 'bucket':'airr-intake-backups-eu-test',
            'prefix':'intake/', 'region':'eu-central-003', 'max_snapshot_bytes':500_000_000,
            'key_expires_at':(self.now + timedelta(days=365)).isoformat()}

    def tearDown(self):
        self.clock.stop()
        self.temp.cleanup()

    def snapshot(self, content=b'age-encryption.org/v1\nsynthetic-encrypted-fixture', hours=0):
        stamp = (self.now - timedelta(hours=hours)).strftime('%Y%m%dT%H%M%SZ')
        path = self.root / f'airr-{stamp}.tar.gz.age'
        path.write_bytes(content)
        sidecar = path.with_suffix(path.suffix + '.sha256')
        expected = hashlib.sha256(content).hexdigest()
        sidecar.write_text(expected + '  ' + path.name + '\n')
        return path, sidecar, expected

    def test_completed_snapshot_is_checked_before_transfer(self):
        path, _, expected = self.snapshot()
        selected = offsite.latest_snapshot(self.root, 500_000_000)
        self.assertEqual(selected[0], path)
        self.assertEqual(selected[2], expected)

    def test_plaintext_even_with_matching_checksum_is_refused(self):
        self.snapshot(b'%PDF-secret manuscript')
        with self.assertRaisesRegex(RuntimeError, 'Only binary age'):
            offsite.latest_snapshot(self.root, 500_000_000)

    def test_changed_encrypted_bytes_are_refused(self):
        path, _, _ = self.snapshot()
        with path.open('ab') as handle:
            handle.write(b'changed')
        with self.assertRaisesRegex(RuntimeError, 'integrity'):
            offsite.latest_snapshot(self.root, 500_000_000)

    def test_missing_or_wrong_checksum_is_refused(self):
        _, sidecar, expected = self.snapshot()
        sidecar.write_text(expected + '  different-file.age')
        with self.assertRaisesRegex(RuntimeError, 'checksum record'):
            offsite.latest_snapshot(self.root, 500_000_000)
        sidecar.unlink()
        with self.assertRaisesRegex(RuntimeError, 'unsafe or incomplete'):
            offsite.latest_snapshot(self.root, 500_000_000)

    def test_partial_snapshot_never_becomes_a_completed_backup(self):
        (self.root / 'airr-20260907T200000Z.tar.gz.partial').write_bytes(b'partial')
        with self.assertRaisesRegex(RuntimeError, 'No completed'):
            offsite.latest_snapshot(self.root, 500_000_000)

    def test_stale_and_future_snapshots_are_refused(self):
        for hours in (31, -1):
            with self.subTest(hours=hours):
                path, sidecar, _ = self.snapshot(hours=hours)
                with self.assertRaisesRegex(RuntimeError, 'timestamp'):
                    offsite.latest_snapshot(self.root, 500_000_000)
                path.unlink()
                sidecar.unlink()

    def test_quota_guard_blocks_the_upload(self):
        self.snapshot()
        with self.assertRaisesRegex(RuntimeError, 'transfer limit'):
            offsite.latest_snapshot(self.root, 10)

    def test_unexpected_destinations_are_refused(self):
        for changes in ({'prefix':'other/'}, {'bucket':'elsewhere'}, {'region':'us-east-005'},
                        {'enabled':False}, {'max_snapshot_bytes':1_000_000_000}):
            with self.subTest(changes=changes), self.assertRaises(RuntimeError):
                offsite.remote_for(self.settings | changes)

    def test_download_hash_mismatch_does_not_mark_a_success_or_upload_sidecar(self):
        path, _, _ = self.snapshot()
        with (patch.object(offsite, 'SNAPSHOTS', self.root), patch.object(offsite, 'rclone',
                side_effect=['', json.dumps({'IsDir':False,'Size':path.stat().st_size})]) as runner,
                patch.object(offsite, 'downloaded_checksum', return_value='0' * 64)):
            with self.assertRaisesRegex(RuntimeError, 'Downloaded B2 bytes'):
                offsite.transfer(self.settings)
            self.assertEqual(runner.call_count, 2)
            self.assertIn('--immutable', runner.call_args_list[0].args)

    def test_success_requires_matching_download_and_preserves_remote_objects(self):
        path, sidecar, expected = self.snapshot()
        with (patch.object(offsite, 'SNAPSHOTS', self.root), patch.object(offsite, 'rclone',
                side_effect=['', json.dumps({'IsDir':False,'Size':path.stat().st_size}), '']) as runner,
                patch.object(offsite, 'downloaded_checksum', return_value=expected)):
            status = offsite.transfer(self.settings)
        self.assertTrue(status['download_verified'])
        self.assertEqual(status['sha256'], expected)
        self.assertEqual(runner.call_args_list[-1].args[1], str(sidecar))
        self.assertEqual([call.args[0] for call in runner.call_args_list], ['copyto','lsjson','copyto'])

    def test_monitor_detects_stale_failed_and_expiring_offsite_copies(self):
        config = self.root / 'offsite.json'
        state = self.root / 'status.json'
        config.write_text(json.dumps(self.settings))
        valid = {'ok':True,'download_verified':True,'bucket':self.settings['bucket'],
            'verified_at':self.now.isoformat(), 'snapshot_at':self.now.isoformat()}
        for changes in ({'ok':False}, {'download_verified':False},
                        {'snapshot_at':(self.now - timedelta(hours=31)).isoformat()}, {'bucket':'wrong'}):
            state.write_text(json.dumps(valid | changes))
            self.assertFalse(monitor.offsite_checks(config,state,self.now)['offsite_copy_verified'])
        state.write_text(json.dumps(valid))
        self.assertTrue(monitor.offsite_checks(config,state,self.now)['offsite_copy_verified'])
        config.write_text(json.dumps(self.settings | {'key_expires_at':(self.now + timedelta(days=20)).isoformat()}))
        self.assertFalse(monitor.offsite_checks(config,state,self.now)['offsite_key_valid'])
        config.unlink()
        self.assertFalse(monitor.offsite_checks(config,state,self.now)['offsite_copy_verified'])
