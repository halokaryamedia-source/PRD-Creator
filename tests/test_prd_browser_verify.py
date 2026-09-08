from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from prd_fixture import write_base_project

ROOT = Path(__file__).resolve().parents[1]
BROWSER_VERIFY = ROOT / "tools" / "browser_verify.py"
PRD_OPERATOR = ROOT / "tools" / "prd.py"


def chrome_driver_available() -> bool:
    configured = shutil.which("chromedriver")
    if configured:
        return True
    return Path("/usr/local/share/chromedriver-linux64/chromedriver").is_file()


@unittest.skipUnless(chrome_driver_available(), "ChromeDriver is not installed in this environment")
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
            build_result = json.loads(build.stdout)
            html = project / build_result["outputs"]["html"]
            screenshot = project / "work" / "browser-evidence.png"

            verify = subprocess.run(
                [sys.executable, str(BROWSER_VERIFY), str(html), "--screenshot", str(screenshot)],
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
            self.assertTrue(screenshot.is_file())

            print(
                "BROWSER VERIFY PASSED "
                f"screenshot_sha256={result['screenshot_sha256']} "
                f"bytes={result['screenshot_bytes']}"
            )


if __name__ == "__main__":
    unittest.main()
