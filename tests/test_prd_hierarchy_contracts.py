from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from tests.test_prd_contracts import RENDERER, VALIDATOR, render_data, run_cli


class PrdHierarchyContracts(unittest.TestCase):
    def make_project(self, data: dict) -> Path:
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
            "    summary: Hierarchy contract fixture.\n"
            "    inspection: full\n",
            encoding="utf-8",
        )
        (project / "state" / "requirement-register.yaml").write_text(
            "requirements:\n"
            "  - id: REQ-001\n"
            "    area: gameplay\n"
            "    statement: Preserve the required gameplay PRD hierarchy.\n"
            "    provenance: [SRC-001]\n"
            "    impact: high\n",
            encoding="utf-8",
        )
        content_path = project / "work" / "content.md"
        content_path.write_text(
            "# Hierarchy Contract Fixture\n\nCanonical fixture content.\n",
            encoding="utf-8",
        )
        data["canonical_content_sha256"] = hashlib.sha256(content_path.read_bytes()).hexdigest()
        data_path = project / "work" / "render-data.json"
        data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        rendered = run_cli(RENDERER, data_path, project / "output" / "final.html")
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        return project

    def test_validator_rejects_missing_required_hierarchy_collection(self) -> None:
        variants = {
            "gameplay_flow": "gameplay_flow_array",
            "global_development": "global_development_array",
        }
        for collection, expected_check in variants.items():
            with self.subTest(collection=collection):
                data = render_data()
                data[collection] = []
                project = self.make_project(data)

                validated = run_cli(VALIDATOR, project)
                self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
                result = json.loads(validated.stdout)
                joined = "\n".join(result["errors"])
                self.assertIn(expected_check, joined)


if __name__ == "__main__":
    unittest.main()
