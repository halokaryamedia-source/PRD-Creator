from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HANDOFF_VALIDATOR = (
    ROOT / "kits" / "project-document-generator" / "validator" / "validate_handoff.py"
)


def run_cli(*args: Path | str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *(str(arg) for arg in args)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


class PrdHandoffContracts(unittest.TestCase):
    def make_project(
        self,
        *,
        current_version: str = "1.0",
        accepted_version: str | None = None,
        status: str = "handoff_ready",
    ) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name)
        (project / "state").mkdir(parents=True)
        (project / "work").mkdir(parents=True)
        (project / "output").mkdir(parents=True)

        accepted = accepted_version if accepted_version is not None else current_version
        (project / "work" / "content.md").write_text("# Contract PRD\n", encoding="utf-8")
        (project / "work" / "render-data.json").write_text(
            json.dumps({"document": {"version": current_version}}, indent=2) + "\n",
            encoding="utf-8",
        )
        (project / "output" / "final.html").write_text("<!doctype html><title>Contract</title>\n", encoding="utf-8")
        (project / "work" / "acceptance.md").write_text(
            f"# PRD Acceptance\n"
            f"Status: {status}\n"
            "Mechanical: PASS\n"
            "Visual sanity: NOT PROVEN\n"
            "New Reader: PASS\n"
            "Level Designer: PASS\n"
            "Developer: PASS\n"
            "Acceptance: PASS\n"
            "Project Consistency: PASS\n"
            "Golden Fidelity: PASS\n"
            "Critical: 0\n"
            "Major: 0\n",
            encoding="utf-8",
        )
        (project / "output" / "team-handoff.md").write_text(
            f"# Team Handoff\nPRD Version: {accepted}\n",
            encoding="utf-8",
        )
        (project / "state" / "handoff-state.yaml").write_text(
            f"status: {status}\n"
            f"accepted_prd_version: {accepted}\n"
            "content: work/content.md\n"
            "render_data: work/render-data.json\n"
            "html: output/final.html\n"
            "acceptance: work/acceptance.md\n"
            "handoff: output/team-handoff.md\n"
            "next_step: flow_5_voice_requirement_extraction\n",
            encoding="utf-8",
        )
        return project

    def test_current_handoff_allows_flow5_entry(self) -> None:
        project = self.make_project()
        validated = run_cli(HANDOFF_VALIDATOR, project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        self.assertEqual(result["status"], "pass")
        revision = next(check for check in result["checks"] if check["check"] == "handoff_revision_matches_current_prd")
        self.assertEqual(revision["status"], "pass")
        acceptance = next(check for check in result["checks"] if check["check"] == "acceptance_allows_handoff")
        self.assertEqual(acceptance["status"], "pass")

    def test_pending_review_cannot_authorize_flow5(self) -> None:
        project = self.make_project(status="pending_review")
        validated = run_cli(HANDOFF_VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        self.assertIn("handoff_status_ready", "\n".join(result["errors"]))
        self.assertIn("pending_review", "\n".join(result["errors"]))

    def test_stale_handoff_version_cannot_authorize_newer_prd(self) -> None:
        project = self.make_project(current_version="1.1", accepted_version="1.0")
        validated = run_cli(HANDOFF_VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        joined = "\n".join(json.loads(validated.stdout)["errors"])
        self.assertIn("handoff_revision_matches_current_prd", joined)
        self.assertIn("accepted_prd_version='1.0'", joined)
        self.assertIn("current document.version='1.1'", joined)

    def test_handoff_requires_existing_current_artifact_references(self) -> None:
        project = self.make_project()
        (project / "output" / "team-handoff.md").unlink()
        validated = run_cli(HANDOFF_VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        joined = "\n".join(json.loads(validated.stdout)["errors"])
        self.assertIn("handoff_artifact_references_current", joined)
        self.assertIn("missing referenced artifact: output/team-handoff.md", joined)

    def test_acceptance_failure_cannot_authorize_flow5(self) -> None:
        variants = {
            "needs revision": "Status: needs_revision",
            "mechanical failure": "Mechanical: FAIL",
            "visual failure": "Visual sanity: FAIL",
            "developer failure": "Developer: FAIL",
            "acceptance failure": "Acceptance: FAIL",
            "golden fidelity failure": "Golden Fidelity: FAIL",
            "critical blocker": "Critical: 1",
            "major blocker": "Major: 2",
        }
        for name, replacement in variants.items():
            with self.subTest(name=name):
                project = self.make_project()
                path = project / "work" / "acceptance.md"
                text = path.read_text(encoding="utf-8")
                label = replacement.split(":", 1)[0]
                text = "\n".join(
                    replacement if line.startswith(f"{label}:") else line
                    for line in text.splitlines()
                ) + "\n"
                path.write_text(text, encoding="utf-8")
                validated = run_cli(HANDOFF_VALIDATOR, project)
                self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
                self.assertIn("acceptance_allows_handoff", "\n".join(json.loads(validated.stdout)["errors"]))

    def test_acceptance_allows_visual_not_proven_without_claiming_pass(self) -> None:
        project = self.make_project()
        validated = run_cli(HANDOFF_VALIDATOR, project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        self.assertIn("NOT PROVEN", (project / "work" / "acceptance.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
