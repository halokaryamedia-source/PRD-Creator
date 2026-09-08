from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from prd_fixture import write_base_project

ROOT = Path(__file__).resolve().parents[1]
RENDERER = ROOT / "kits" / "prd-creator" / "renderer" / "render.py"


def run_cli(*args: Path | str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *(str(arg) for arg in args)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


class PackageTabNavigationContracts(unittest.TestCase):
    def test_gameplay_overview_marks_current_package_tab(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            project = Path(temp)
            write_base_project(project)
            output = project / "output" / "v1.0.0" / "prd.html"
            rendered = run_cli(RENDERER, project / "work" / "render-data.json", output)
            self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
            html = output.read_text(encoding="utf-8")
            self.assertIn(
                'class="section-tab section-tab-link is-active" '
                'data-section-target="dev-core-requirement" '
                'href="#dev-core-requirement" aria-current="page"',
                html,
            )


if __name__ == "__main__":
    unittest.main()
