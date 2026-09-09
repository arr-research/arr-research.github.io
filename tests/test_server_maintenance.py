from datetime import datetime, timezone
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from services.intake.deploy import monitor


class ServerMaintenanceMonitorTests(unittest.TestCase):
    def test_recent_success_active_timer_and_no_reboot_are_healthy(self):
        now = datetime.now(timezone.utc)
        with tempfile.TemporaryDirectory() as directory:
            marker = Path(directory) / "last-success"
            marker.touch()
            with (
                patch.object(monitor, "SECURITY_SUCCESS", marker),
                patch("services.intake.deploy.monitor.subprocess.run") as run,
                patch("services.intake.deploy.monitor.Path.exists", return_value=False),
            ):
                run.return_value.returncode = 0
                self.assertEqual(
                    monitor.security_update_checks(now),
                    {
                        "security_update_timer_active": True,
                        "security_updates_recent": True,
                        "reboot_not_pending": True,
                    },
                )

    def test_missing_success_inactive_timer_and_pending_reboot_fail_closed(self):
        now = datetime.now(timezone.utc)
        with tempfile.TemporaryDirectory() as directory:
            marker = Path(directory) / "missing"
            with (
                patch.object(monitor, "SECURITY_SUCCESS", marker),
                patch("services.intake.deploy.monitor.subprocess.run") as run,
                patch("services.intake.deploy.monitor.Path.exists", return_value=True),
            ):
                run.return_value.returncode = 3
                self.assertEqual(
                    monitor.security_update_checks(now),
                    {
                        "security_update_timer_active": False,
                        "security_updates_recent": False,
                        "reboot_not_pending": False,
                    },
                )


if __name__ == "__main__":
    unittest.main()
