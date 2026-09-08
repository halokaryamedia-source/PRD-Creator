from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from prd_fixture import write_base_project

ROOT = Path(__file__).resolve().parents[1]
PRD_OPERATOR = ROOT / "tools" / "prd.py"


def chrome_driver_available() -> bool:
    configured = shutil.which("chromedriver")
    if configured:
        return True
    return Path("/usr/local/share/chromedriver-linux64/chromedriver").is_file()


def browser_test_enabled() -> bool:
    return chrome_driver_available() or os.environ.get("CI", "").casefold() == "true"


@unittest.skipUnless(browser_test_enabled(), "ChromeDriver is not installed in this local environment")
class PrdBrowserVerificationContracts(unittest.TestCase):
    def test_rendered_prd_passes_real_browser_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            project = Path(temp_dir) / "project"
            write_base_project(project)

            build = subprocess.run(
                [sys.executable, str(PRD_OPERATOR), "build", str(project)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(build.returncode, 0, build.stderr or build.stdout)
            screenshot = project / "work" / "browser-evidence.png"

            verify = subprocess.run(
                [
                    sys.executable,
                    str(PRD_OPERATOR),
                    "browser",
                    str(project),
                    "--screenshot",
                    str(screenshot),
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(verify.returncode, 0, verify.stderr or verify.stdout)
            result = json.loads(verify.stdout)
            self.assertEqual(result["status"], "pass")
            self.assertGreater(result["screenshot_bytes"], 5_000)
            self.assertEqual(result["severe_console_count"], 0)
            self.assertEqual(result["dom"]["duplicateIds"], [])
            self.assertEqual(result["dom"]["missingTargets"], [])
            self.assertEqual(result["dom"]["invalidTabGroups"], [])
            self.assertEqual(result["interaction"]["hashFailures"], [])
            self.assertEqual(result["interaction"]["languageFailures"], [])
            self.assertEqual(
                [(item["requested_width"], item["requested_height"]) for item in result["viewports"]],
                [(1440, 1200), (1024, 900)],
            )
            self.assertTrue(all(item["horizontal_overflow_px"] == 0 for item in result["viewports"]))
            self.assertTrue(all(item["screenshot_bytes"] > 5_000 for item in result["viewports"]))
            self.assertTrue(screenshot.is_file())

            viewport_proof = ",".join(
                f"{item['requested_width']}x{item['requested_height']}:{item['screenshot_sha256']}"
                for item in result["viewports"]
            )
            print(f"BROWSER VERIFY PASSED viewports={viewport_proof} primary_bytes={result['screenshot_bytes']}")


if __name__ == "__main__":
    unittest.main()
