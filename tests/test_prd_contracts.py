from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RENDERER = ROOT / "kits" / "project-document-generator" / "renderer" / "render.py"
VALIDATOR = ROOT / "kits" / "project-document-generator" / "validator" / "validate.py"


def run_cli(*args: Path | str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *(str(arg) for arg in args)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def render_data() -> dict:
    return {
        "document": {
            "title": "Contract Fixture",
            "subtitle": "Gameplay & Development Specification",
            "document_type": "Production Specification",
            "version": "1.0",
        },
        "overview": {
            "project_context": "A minimal contract fixture for production verification.",
            "main_experience": "Complete one deterministic gameplay package.",
            "facts": [
                {"label": "Players", "value": "1"},
                {"label": "Mode", "value": "Contract Test"},
            ],
        },
        "gameplay_flow": [],
        "global_development": [],
        "packages": [
            {
                "id": "core",
                "package_label": "Fixture Package",
                "title": "Core Trial",
                "gameplay": {
                    "context": "The player enters a controlled test arena.",
                    "main_objective": "Complete the trial.",
                    "start_condition": "Player enters the arena.",
                    "end_condition": "Trial completion is recorded.",
                    "blocked_or_fail_condition": "The trial is interrupted.",
                    "player_flow": [
                        {
                            "step": 1,
                            "title": "Start",
                            "action": "Begin the trial.",
                            "result": "Trial becomes active.",
                        }
                    ],
                    "result": "The trial records one completion result.",
                },
                "level_design": {
                    "overview": "One readable test space.",
                    "flow": [],
                    "requirements": [],
                },
                "developer": {
                    "overview": "Track one score result deterministically.",
                    "flow": [],
                    "requirements": [],
                    "scoring": {
                        "score_name": "Fixture Score",
                        "components": [
                            {
                                "name": "Completion",
                                "weight": 100,
                                "rule": "Completion contributes the full score.",
                            }
                        ],
                        "timer_start": "Trial activation.",
                        "timer_stop": "Trial completion.",
                        "no_score_condition": "Interrupted run.",
                        "duplicate_prevention": "Record once per run.",
                        "final_result_relationship": "Fixture Score is the package result.",
                    },
                },
            }
        ],
    }


def fingerprint(data: dict) -> str:
    canonical = json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


class ProjectDocumentContracts(unittest.TestCase):
    def make_project(self, data: dict) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name)
        (project / "work").mkdir(parents=True)
        (project / "output").mkdir(parents=True)
        (project / "work" / "content.md").write_text(
            "# Contract Fixture\n\nCanonical fixture content with no unresolved placeholders.\n",
            encoding="utf-8",
        )
        self.write_data(project, data)
        return project

    def write_data(self, project: Path, data: object) -> None:
        (project / "work" / "render-data.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def render(self, project: Path) -> subprocess.CompletedProcess[str]:
        return run_cli(
            RENDERER,
            project / "work" / "render-data.json",
            project / "output" / "final.html",
        )

    def validate(self, project: Path) -> subprocess.CompletedProcess[str]:
        return run_cli(VALIDATOR, project)

    def test_renderer_and_validator_happy_path(self) -> None:
        data = render_data()
        project = self.make_project(data)

        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = (project / "output" / "final.html").read_text(encoding="utf-8")
        self.assertIn(
            f'<meta content="{fingerprint(data)}" name="render-data-sha256"/>',
            html,
        )

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(
            result["expected_pages"],
            [
                "summary",
                "dev-core-requirement",
                "dev-core-level",
                "dev-core-developer",
            ],
        )

    def test_validator_rejects_stale_html_after_render_data_changes(self) -> None:
        data = render_data()
        project = self.make_project(data)
        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)

        data["overview"]["project_context"] = "This projection changed after the last render."
        self.write_data(project, data)

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        joined = "\n".join(result["errors"])
        self.assertIn("render_data_revision_matches_html", joined)

    def test_validator_returns_structured_fail_for_malformed_collection_item(self) -> None:
        data = render_data()
        project = self.make_project(data)
        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)

        malformed = render_data()
        malformed["gameplay_flow"] = ["not-an-object"]
        self.write_data(project, malformed)

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertNotIn("Traceback", validated.stderr)
        result = json.loads(validated.stdout)
        self.assertEqual(result["status"], "fail")
        self.assertIn(
            "gameplay_flow[0]: item must be an object",
            "\n".join(result["errors"]),
        )

    def test_validator_rejects_extra_generated_page(self) -> None:
        project = self.make_project(render_data())
        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)

        html_path = project / "output" / "final.html"
        html = html_path.read_text(encoding="utf-8")
        self.assertIn("</main>", html)
        html_path.write_text(
            html.replace(
                "</main>",
                '<section class="sheet" id="stale-extra"></section></main>',
                1,
            ),
            encoding="utf-8",
        )

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        self.assertIn(
            "generated_page_set_matches_current_render_data",
            "\n".join(result["errors"]),
        )
        self.assertIn("stale-extra", "\n".join(result["errors"]))

    def test_validator_rejects_scoring_completion_conflict_and_bad_weight(self) -> None:
        data = render_data()
        developer = data["packages"][0]["developer"]
        developer["scoring"]["components"][0]["weight"] = 90
        developer["completion_data"] = {
            "produces_score": False,
            "valid_completion_condition": "Trial completes.",
            "recorded_data": "Completion state.",
        }
        project = self.make_project(data)

        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        joined = "\n".join(result["errors"])
        self.assertIn("exactly one of scoring or completion_data", joined)
        self.assertIn("numeric scoring weights total 90", joined)


if __name__ == "__main__":
    unittest.main()
