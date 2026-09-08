from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from prd_fixture import acceptance_text, handoff_state_text, write_base_project

from tools import prd as prd_operator

ROOT = Path(__file__).resolve().parents[1]
OPERATOR = ROOT / "tools" / "prd.py"


def run_operator(*args: Path | str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(OPERATOR), *(str(arg) for arg in args)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


class PrdOperatorCliContracts(unittest.TestCase):
    def make_project(self) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name)
        write_base_project(project)
        return project

    def test_status_reports_first_wrong_owner_before_delivery(self) -> None:
        project = self.make_project()
        status = run_operator("status", project, "--json")
        self.assertEqual(status.returncode, 1, status.stderr or status.stdout)
        payload = json.loads(status.stdout)
        self.assertEqual(payload["mechanical_status"], "blocked")
        self.assertEqual(payload["prd"]["status"], "fail")
        self.assertEqual(payload["first_issue"]["code"], "PRD_HTML_MISSING")
        self.assertEqual(payload["first_issue"]["owner"], "flow3.renderer")
        self.assertIn("first wrong owner", payload["next_action"])

    def test_build_then_status_is_compact_and_clear(self) -> None:
        project = self.make_project()
        built = run_operator("build", project)
        self.assertEqual(built.returncode, 0, built.stderr or built.stdout)
        outputs = json.loads(built.stdout)["outputs"]
        self.assertEqual(outputs["prd"], "output/v1.0.0/prd.html")
        self.assertEqual(outputs["context"], "output/v1.0.0/context.md")
        self.assertEqual(outputs["index"], "output/v1.0.0/index.json")

        status = run_operator("status", project, "--json")
        self.assertEqual(status.returncode, 0, status.stderr or status.stdout)
        payload = json.loads(status.stdout)
        self.assertEqual(payload["mechanical_status"], "clear")
        self.assertEqual(payload["prd"]["status"], "pass")
        self.assertEqual(payload["handoff"]["status"], "not_present")
        self.assertEqual(payload["voice"]["status"], "not_present")
        self.assertIsNone(payload["first_issue"])
        self.assertIn("no handoff readiness is claimed", payload["next_action"])

    def test_status_reuses_handoff_prd_proof(self) -> None:
        project = self.make_project()
        self.assertEqual(run_operator("build", project).returncode, 0)
        (project / "work" / "acceptance.md").write_text(acceptance_text(project), encoding="utf-8")
        (project / "state" / "handoff-state.yaml").write_text(handoff_state_text(), encoding="utf-8")

        original_validate = prd_operator.prd_api.validate
        with patch.object(prd_operator.prd_api, "validate", wraps=original_validate) as validate_prd:
            payload = prd_operator.status_payload(project)

        self.assertEqual(payload["mechanical_status"], "clear")
        self.assertEqual(payload["prd"]["status"], "pass")
        self.assertEqual(payload["handoff"]["status"], "pass")
        self.assertEqual(validate_prd.call_count, 1)

    def test_impact_routes_only_affected_domains(self) -> None:
        impact = run_operator(
            "impact",
            "work/voice-production.md",
            "kits/prd-creator/renderer/static/production-assets.css",
            "--json",
        )
        self.assertEqual(impact.returncode, 0, impact.stderr or impact.stdout)
        payload = json.loads(impact.stdout)
        self.assertEqual(payload["recommended_checks"], ["repository", "prd", "voice", "browser"])
        self.assertTrue(payload["browser_required"])
        self.assertFalse(payload["full_regression_required"])

    def test_impact_rejects_direct_derived_output_as_work_owner(self) -> None:
        impact = run_operator("impact", "output/v1.0.0/prd.html", "--json")
        self.assertEqual(impact.returncode, 0, impact.stderr or impact.stdout)
        payload = json.loads(impact.stdout)
        self.assertEqual(payload["derived_edits"], ["output/v1.0.0/prd.html"])
        self.assertIn("canonical owner", payload["next_action"])

    def test_validate_command_preserves_canonical_validator_exit(self) -> None:
        project = self.make_project()
        self.assertEqual(run_operator("build", project).returncode, 0)
        validated = run_operator("validate", project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        payload = json.loads(validated.stdout)
        self.assertEqual(payload["status"], "pass")

    def test_browser_refuses_visual_proof_until_current_prd_validates(self) -> None:
        project = self.make_project()
        browser = run_operator("browser", project)
        self.assertEqual(browser.returncode, 1, browser.stderr or browser.stdout)
        payload = json.loads(browser.stdout)
        self.assertEqual(payload["status"], "fail")
        self.assertEqual(payload["issues"][0]["code"], "PRD_HTML_MISSING")
        self.assertEqual(payload["issues"][0]["owner"], "flow3.renderer")


if __name__ == "__main__":
    unittest.main()
