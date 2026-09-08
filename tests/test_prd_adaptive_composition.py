from __future__ import annotations

import hashlib
import json
import re
import tempfile
import unittest
from pathlib import Path

from tests.test_prd_contracts import (
    GOLDEN_TEMPLATE,
    RENDERER,
    VALIDATOR,
    render_data,
    run_cli,
)


def section_html(document: str, section_id: str) -> str:
    match = re.search(
        rf'<section\b[^>]*\bid="{re.escape(section_id)}"[^>]*>(.*?)</section>',
        document,
        re.S,
    )
    if match is None:
        raise AssertionError(f"Rendered section not found: {section_id}")
    return match.group(1)


class AdaptiveSemanticCompositionContracts(unittest.TestCase):
    def make_project(self, data: dict) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name)
        for name in ("state", "work", "output"):
            (project / name).mkdir(parents=True)

        (project / "state" / "source-inventory.yaml").write_text(
            "sources:\n"
            "  - id: SRC-001\n"
            "    type: instruction\n"
            "    role: authoritative\n"
            "    origin: user\n"
            "    summary: Adaptive composition contract fixture.\n"
            "    inspection: full\n",
            encoding="utf-8",
        )
        requirement_path = project / "state" / "requirement-register.yaml"
        requirement_path.write_text(
            "requirements:\n"
            "  - id: REQ-001\n"
            "    area: gameplay\n"
            "    statement: Preserve all material steps without forcing sample cardinality.\n"
            "    provenance: [SRC-001]\n"
            "    impact: high\n",
            encoding="utf-8",
        )
        requirement_sha = hashlib.sha256(requirement_path.read_bytes()).hexdigest()
        (project / "state" / "intake-state.yaml").write_text(
            f"status: ready_for_prd\npreview_approved: true\napproved_requirement_sha256: {requirement_sha}\n",
            encoding="utf-8",
        )
        content_path = project / "work" / "content.md"
        content_path.write_text(
            "# Adaptive Composition Fixture\n\n"
            "The semantic sequence cardinality follows project meaning rather than sample counts.\n",
            encoding="utf-8",
        )
        data["approved_requirement_sha256"] = requirement_sha
        data["canonical_content_sha256"] = hashlib.sha256(content_path.read_bytes()).hexdigest()
        (project / "work" / "render-data.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return project

    def test_variable_flow_and_note_counts_render_and_validate(self) -> None:
        data = render_data()

        data["global_development"][0]["flow"] = data["global_development"][0]["flow"][:3]
        data["global_development"][0]["notes"] = data["global_development"][0]["notes"][:2]

        gameplay = data["packages"][0]["gameplay"]
        gameplay["player_flow"].extend(
            [
                {
                    "step": 6,
                    "title": "Confirm Result",
                    "action": "Read the final completion feedback.",
                    "result": "The player can confirm the accepted result.",
                },
                {
                    "step": 7,
                    "title": "Clear Route",
                    "action": "Leave through the final marked route.",
                    "result": "The package exits without hiding the extra semantic step.",
                },
            ]
        )

        level = data["packages"][0]["level_design"]
        level["flow"] = level["flow"][:3]
        level["notes"].append(
            {
                "title": "Additional Readability Note",
                "description": "Keep the final feedback readable from the exit route.",
            }
        )

        developer = data["packages"][0]["developer"]
        developer["flow"].extend(
            [
                {
                    "step": 5,
                    "title": "Confirm Cleanup",
                    "description": "Verify transient package state is cleared before reuse.",
                },
                {
                    "step": 6,
                    "title": "Release Session",
                    "description": "Release the fixture only after cleanup verification succeeds.",
                },
            ]
        )
        developer["notes"] = developer["notes"][:2]

        project = self.make_project(data)
        html_path = project / "output" / "v1.0.0" / "prd.html"
        rendered = run_cli(RENDERER, project / "work" / "render-data.json", html_path)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)

        html = html_path.read_text(encoding="utf-8")
        global_page = section_html(html, "development-overview")
        gameplay_page = section_html(html, "dev-core-requirement")
        level_page = section_html(html, "dev-core-level")
        developer_page = section_html(html, "dev-core-developer")

        self.assertEqual(global_page.count("<article"), 5)  # 3 flow + 2 notes
        self.assertEqual(gameplay_page.count('class="role-step"'), 7)
        self.assertEqual(level_page.count('<div class="flow quarry-design-flow"'), 1)
        self.assertEqual(level_page.count("<article"), 8)  # 3 flow + 5 notes
        self.assertEqual(developer_page.count("<article"), 8)  # 6 flow + 2 notes

        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)

    def test_adaptive_cardinality_does_not_modify_golden_artifact(self) -> None:
        golden_before = GOLDEN_TEMPLATE.read_bytes()
        data = render_data()
        data["global_development"][0]["flow"] = data["global_development"][0]["flow"][:3]
        project = self.make_project(data)
        html_path = project / "output" / "v1.0.0" / "prd.html"
        rendered = run_cli(RENDERER, project / "work" / "render-data.json", html_path)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        self.assertEqual(GOLDEN_TEMPLATE.read_bytes(), golden_before)


if __name__ == "__main__":
    unittest.main()
