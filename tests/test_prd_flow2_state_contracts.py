from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from tests.test_prd_contracts import RENDERER, VALIDATOR, render_data, run_cli


class Flow2StateConsistencyContracts(unittest.TestCase):
    def make_project(self) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name)
        (project / "state").mkdir(parents=True)
        (project / "work").mkdir(parents=True)
        (project / "output").mkdir(parents=True)
        (project / "state" / "intake-state.yaml").write_text(
            "status: ready_for_prd\n"
            "ready_for_prd: true\n"
            "next_step: Build canonical PRD content.\n",
            encoding="utf-8",
        )
        (project / "work" / "content.md").write_text(
            "# Contract Fixture\n\nCanonical fixture content with no unresolved placeholders.\n",
            encoding="utf-8",
        )
        data = render_data()
        data["canonical_content_sha256"] = hashlib.sha256(
            (project / "work" / "content.md").read_bytes()
        ).hexdigest()
        (project / "work" / "render-data.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        rendered = run_cli(
            RENDERER,
            project / "work" / "render-data.json",
            project / "output" / "final.html",
        )
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        return project

    def validate(self, project: Path):
        return run_cli(VALIDATOR, project)

    def test_ready_rejects_explicit_requirement_blockers(self) -> None:
        markers = {
            "pending approval": "approval_status: pending",
            "blocked recovery": "recovery_class: blocked",
        }
        for name, marker in markers.items():
            with self.subTest(name=name):
                project = self.make_project()
                (project / "state" / "requirement-register.yaml").write_text(
                    "requirements:\n"
                    "  - id: REQ-001\n"
                    "    area: gameplay\n"
                    "    statement: Material fixture decision.\n"
                    f"    {marker}\n",
                    encoding="utf-8",
                )

                validated = self.validate(project)
                self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
                result = json.loads(validated.stdout)
                joined = "\n".join(result["errors"])
                self.assertIn("flow2_persisted_state_consistent", joined)
                self.assertIn(marker.split(":", 1)[0], joined)

    def test_ready_rejects_explicit_blocked_source_inspection(self) -> None:
        project = self.make_project()
        (project / "state" / "source-inventory.yaml").write_text(
            "sources:\n"
            "  - id: SRC-001\n"
            "    path: source/originals/material-source.docx\n"
            "    role: authoritative\n"
            "    inspection: blocked\n",
            encoding="utf-8",
        )

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        joined = "\n".join(result["errors"])
        self.assertIn("flow2_persisted_state_consistent", joined)
        self.assertIn("inspection='blocked'", joined)

    def test_ready_allows_nonblocking_persisted_state(self) -> None:
        project = self.make_project()
        (project / "state" / "requirement-register.yaml").write_text(
            "requirements:\n"
            "  - id: REQ-001\n"
            "    area: gameplay\n"
            "    statement: Approved fixture decision.\n"
            "    evidence_status: conflict\n"
            "    recovery_class: proposal\n"
            "    approval_status: approved\n"
            "    resolution: Higher-authority decision resolves the source conflict.\n",
            encoding="utf-8",
        )
        (project / "state" / "source-inventory.yaml").write_text(
            "sources:\n"
            "  - id: SRC-001\n"
            "    path: source/originals/material-source.docx\n"
            "    role: authoritative\n"
            "    inspection: targeted\n"
            "    inspection_scope: Current gameplay package only\n",
            encoding="utf-8",
        )

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        consistency = next(
            check for check in result["checks"]
            if check["check"] == "flow2_persisted_state_consistent"
        )
        self.assertEqual(consistency["status"], "pass")


if __name__ == "__main__":
    unittest.main()
