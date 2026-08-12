from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from tests.test_prd_contracts import RENDERER, VALIDATOR, render_data, run_cli


ROOT = Path(__file__).resolve().parents[1]
SOURCE_INTAKE = ROOT / "kits" / "project-document-generator" / "SOURCE-INTAKE.md"
KIT_SKILL = ROOT / "kits" / "project-document-generator" / "SKILL.md"


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
        (project / "state" / "source-inventory.yaml").write_text(
            "sources:\n"
            "  - id: SRC-001\n"
            "    type: instruction\n"
            "    role: authoritative\n"
            "    origin: user\n"
            "    summary: Contract fixture source.\n"
            "    inspection: full\n",
            encoding="utf-8",
        )
        (project / "state" / "requirement-register.yaml").write_text(
            "requirements:\n"
            "  - id: REQ-001\n"
            "    area: gameplay\n"
            "    statement: Complete one deterministic fixture trial.\n"
            "    provenance: [SRC-001]\n"
            "    impact: high\n",
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

    def test_flow2_contract_requires_simple_preview_before_build(self) -> None:
        source_intake = SOURCE_INTAKE.read_text(encoding="utf-8")
        skill = KIT_SKILL.read_text(encoding="utf-8")

        for marker in (
            "## 6. Simple Chat Preview and user approval",
            "Apa yang Player Lakukan",
            "Perlu Konfirmasi",
            "preview_approved: true",
            "do not turn the preview into a second PRD",
        ):
            self.assertIn(marker, source_intake)

        self.assertIn("→ SIMPLE PREVIEW\n→ BUILD PRD", skill)
        self.assertIn("the Simple Chat Preview has been approved", skill)
        self.assertIn("The Simple Chat Preview is not a new artifact", skill)

    def test_ready_rejects_missing_or_empty_required_persisted_state(self) -> None:
        variants = {
            "missing source inventory": ("source-inventory.yaml", None),
            "missing requirement register": ("requirement-register.yaml", None),
            "empty source inventory": ("source-inventory.yaml", "sources:\n"),
            "empty requirement register": ("requirement-register.yaml", "requirements:\n"),
        }
        for name, (filename, replacement) in variants.items():
            with self.subTest(name=name):
                project = self.make_project()
                path = project / "state" / filename
                if replacement is None:
                    path.unlink()
                else:
                    path.write_text(replacement, encoding="utf-8")

                validated = self.validate(project)
                self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
                result = json.loads(validated.stdout)
                joined = "\n".join(result["errors"])
                self.assertIn("flow2_persisted_state_consistent", joined)
                self.assertIn(filename, joined)

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
                self.assertEqual(validated.returncode, 1)
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

    def test_ready_ignores_blocked_inspection_on_superseded_source(self) -> None:
        project = self.make_project()
        (project / "state" / "source-inventory.yaml").write_text(
            "sources:\n"
            "  - id: SRC-001\n"
            "    path: source/originals/legacy-source.docx\n"
            "    role: authoritative\n"
            "    status: superseded\n"
            "    inspection: blocked\n"
            "  - id: SRC-002\n"
            "    type: instruction\n"
            "    role: authoritative\n"
            "    origin: user\n"
            "    summary: Current fixture authority.\n"
            "    inspection: full\n",
            encoding="utf-8",
        )

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)

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
