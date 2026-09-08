"""Regression: an executing oneshot is activating, and must finish before downtime."""
import subprocess
import unittest
from unittest.mock import patch

from services.intake.deploy import upgrade


class UpgradeCoordinationTests(unittest.TestCase):
    def test_running_oneshots_finish_before_their_dependencies_are_paused(self):
        states = {upgrade.MONITOR + '.service': ['activating', 'deactivating', 'inactive'],
                  upgrade.BACKGROUND[0] + '.service': ['activating', 'inactive']}
        events = []

        def state(unit):
            remaining = states.get(unit, ['inactive'])
            value = remaining.pop(0) if len(remaining) > 1 else remaining[0]
            events.append(('state', unit, value))
            return value

        timers = [unit + '.timer' for unit in [upgrade.MONITOR, *upgrade.BACKGROUND]]
        with patch.object(upgrade, 'unit_state', side_effect=state), \
             patch.object(upgrade, 'run', side_effect=lambda *args: events.append(args)), \
             patch.object(upgrade.time, 'sleep'):
            upgrade.pause_background(timers)
        stop_workers = ('systemctl', 'stop', *timers[1:])
        self.assertLess(events.index(('state', upgrade.MONITOR + '.service', 'inactive')),
                        events.index(stop_workers))
        self.assertGreater(events.index(('state', upgrade.BACKGROUND[0] + '.service', 'inactive')),
                           events.index(stop_workers))

    def test_stuck_monitor_aborts_before_other_services_are_paused(self):
        with patch.object(upgrade, 'unit_state', return_value='activating'), \
             patch.object(upgrade.time, 'monotonic', side_effect=[0, 60]), \
             patch.object(upgrade, 'run') as command:
            with self.assertRaisesRegex(RuntimeError, 'still running'):
                upgrade.pause_background([upgrade.MONITOR + '.timer', 'airr-intake-mail.timer'])
        command.assert_called_once_with('systemctl', 'stop', upgrade.MONITOR + '.timer')

    def test_monitor_resumes_last_and_is_not_left_off_after_worker_failure(self):
        timers = [upgrade.MONITOR + '.timer', 'airr-intake-mail.timer']
        for fails in (False, True):
            calls = []

            def command(*args):
                calls.append(args)
                if fails and args[-1] == 'airr-intake-mail.timer':
                    raise subprocess.CalledProcessError(1, args)

            with patch.object(upgrade, 'run', side_effect=command):
                if fails:
                    with self.assertRaises(subprocess.CalledProcessError):
                        upgrade.resume_background(timers)
                else:
                    upgrade.resume_background(timers)
            self.assertEqual(calls, [('systemctl', 'start', 'airr-intake-mail.timer'),
                                     ('systemctl', 'start', upgrade.MONITOR + '.timer')])

    def test_previously_disabled_monitor_stays_disabled(self):
        with patch.object(upgrade, 'run') as command:
            upgrade.resume_background(['airr-intake-mail.timer'])
        command.assert_called_once_with('systemctl', 'start', 'airr-intake-mail.timer')


if __name__ == '__main__':
    unittest.main()
