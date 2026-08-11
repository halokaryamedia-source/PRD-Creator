from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RENDERER = ROOT / "kits" / "project-document-generator" / "renderer" / "render.py"
VALIDATOR = ROOT / "kits" / "project-document-generator" / "validator" / "validate.py"
APPROVED_TEMPLATE = ROOT / "kits" / "project-document-generator" / "template" / "approved-document.html"
BILINGUAL_SCALAR_FIELDS = {
    "canonical_content_sha256",
    "id",
    "key",
    "code",
    "version",
    "brand_mark",
    "languages",
    "roles",
    "weight",
    "step",
    "no",
    "number",
    "formula",
}


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
        "gameplay_flow": [
            {
                "id": "arrival",
                "title": "Arrival",
                "narrative_context": "The player enters the controlled fixture.",
                "player_experience": "Follow the marked route into the test space.",
                "main_obstacle_or_change": "The trial becomes available.",
                "player_result": "The player reaches the Core Trial.",
                "next_destination": "Core Trial",
            }
        ],
        "global_development": [
            {
                "id": "game-system",
                "title": "Game System",
                "subtitle": "Shared fixture behavior",
                "overview": "One shared system owns the fixture session.",
                "flow": [
                    {
                        "step": 1,
                        "title": "Initialize",
                        "description": "Create the fixture state.",
                        "result": "The trial is ready.",
                    }
                ],
                "requirements": [
                    {
                        "title": "Session Setup",
                        "items": [
                            {
                                "title": "Ownership",
                                "details": ["Use one isolated fixture session."],
                                "result": "State remains isolated.",
                            }
                        ],
                    }
                ],
                "notes": [
                    {"title": "Shared Rule", "description": "Use the same fixture owner for the complete run."}
                ],
            }
        ],
        "packages": [
            {
                "id": "core",
                "package_label": "Fixture Package",
                "title": "Core Trial",
                "gameplay": {
                    "context": "The player enters a controlled test arena.",
                    "main_objective": "Complete the trial.",
                    "purpose": "Prove the Golden Sample package composition with one deterministic trial.",
                    "gameplay_time": "Short controlled run.",
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
                    "overview": "Build one readable test space.",
                    "flow": [
                        {"step": 1, "title": "Build the Trial", "details": "Create the single fixture route."}
                    ],
                    "requirements": [
                        {
                            "title": "Trial Area",
                            "items": [
                                {
                                    "object": "Core Trial Space",
                                    "subtitle": "Primary gameplay area",
                                    "area_size": "Fit one controlled interaction route.",
                                    "build_and_visual": "Keep the route readable and the target visible.",
                                    "gameplay_function": "Supports the complete fixture trial.",
                                }
                            ],
                        }
                    ],
                    "notes": [
                        {"title": "Readable Route", "description": "The player must see the required destination."}
                    ],
                },
                "developer": {
                    "overview": "Track one score result deterministically.",
                    "flow": [
                        {
                            "step": 1,
                            "trigger": "Trial starts",
                            "behavior": "Activate the fixture objective.",
                            "data": "Fixture state",
                            "result": "Trial becomes active.",
                        }
                    ],
                    "requirements": [
                        {
                            "title": "Mechanic Setup",
                            "items": [
                                {
                                    "title": "Trial Activation",
                                    "details": ["Activate once when the player enters the trial."],
                                    "result": "The objective starts once.",
                                }
                            ],
                        }
                    ],
                    "scoring": {
                        "score_name": "Fixture Score",
                        "scale": "0–100",
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
                    "reset": ["Restore the fixture trial to its initial state."],
                    "notes": [
                        {"title": "One Result", "description": "A valid run creates one Fixture Score."}
                    ],
                },
                "terms": [
                    {
                        "key": "fixture-score",
                        "label": "Fixture Score",
                        "definition": "The score created by the Core Trial.",
                    }
                ],
            }
        ],
    }


def bilingual_render_data() -> dict:
    def localized(value: object, field: str | None = None) -> object:
        if isinstance(value, dict):
            keys = set(value)
            if keys and keys.issubset({"en", "id"}):
                return value
            return {key: localized(child, key) for key, child in value.items()}
        if isinstance(value, list):
            return [localized(child, field) for child in value]
        if isinstance(value, str) and value and field not in BILINGUAL_SCALAR_FIELDS:
            return {"en": value, "id": f"ID · {value}"}
        return value

    data = localized(render_data())
    assert isinstance(data, dict)
    data["document"]["languages"] = ["en", "id"]
    return data


class ProjectDocumentContracts(unittest.TestCase):
    def make_project(self, data: dict) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name)
        (project / "state").mkdir(parents=True)
        (project / "work").mkdir(parents=True)
        (project / "output").mkdir(parents=True)
        self.write_intake_state(project)
        (project / "work" / "content.md").write_text(
            "# Contract Fixture\n\nCanonical fixture content with no unresolved placeholders.\n",
            encoding="utf-8",
        )
        self.write_data(project, data)
        return project

    def write_intake_state(
        self,
        project: Path,
        status: str = "ready_for_prd",
        ready: bool = True,
    ) -> None:
        (project / "state" / "intake-state.yaml").write_text(
            f"status: {status}\n"
            f"ready_for_prd: {'true' if ready else 'false'}\n"
            "next_step: Build canonical PRD content.\n",
            encoding="utf-8",
        )

    def write_data(self, project: Path, data: object) -> None:
        if isinstance(data, dict):
            data["canonical_content_sha256"] = hashlib.sha256(
                (project / "work" / "content.md").read_bytes()
            ).hexdigest()
        (project / "work" / "render-data.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def render(self, project: Path, template: Path | None = None) -> subprocess.CompletedProcess[str]:
        args: list[Path | str] = [
            RENDERER,
            project / "work" / "render-data.json",
            project / "output" / "final.html",
        ]
        if template is not None:
            args.extend(["--template", template])
        return run_cli(*args)

    def validate(self, project: Path) -> subprocess.CompletedProcess[str]:
        return run_cli(VALIDATOR, project)

    def write_template(self, project: Path, name: str, text: str) -> Path:
        path = project / name
        path.write_text(text, encoding="utf-8")
        return path

    def test_renderer_and_validator_happy_path(self) -> None:
        project = self.make_project(render_data())

        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = (project / "output" / "final.html").read_text(encoding="utf-8")
        self.assertIn(
            '<meta content="A minimal contract fixture for production verification." name="description"/>',
            html,
        )
        self.assertIn(
            '<meta content="prd-contract-fixture-v1.0" name="specification-version"/>',
            html,
        )
        self.assertIn('data-document-languages="en"', html)
        self.assertIn('id="prd-renderer-contract-style"', html)
        self.assertIn('id="prd-single-language-enforcer"', html)
        self.assertIn('style="--prd-journey-columns:1"', html)
        self.assertIn('style="--prd-flow-columns:1"', html)
        self.assertIn('dev-core-requirement-terms-used-details', html)
        self.assertNotIn('dev-core-level-terms-used-details', html)
        self.assertNotIn('dev-core-developer-terms-used-details', html)
        for marker in (
            "narrative-sequence",
            "section-tabs package-tabs",
            "development-package-title",
            "phase-context-grid",
            "phase-overview-table quarry-overview-table",
            "role-sequence quarry-sequence",
            "context-block section-context",
            "flow quarry-design-flow",
            "production-table quarry-build-table",
            "flow quarry-development-flow",
            "production-table quarry-development-table",
            "quarry-score-summary phase-score-summary",
            "outcome quarry-note-grid",
        ):
            self.assertIn(marker, html)
        self.assertNotIn('<span class="footer-brand">MIVUBI</span>', html)

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        self.assertEqual(result["status"], "pass")
        flow2 = next(check for check in result["checks"] if check["check"] == "flow2_ready_for_prd")
        self.assertEqual(flow2["status"], "pass")
        binding = next(
            check for check in result["checks"] if check["check"] == "render_data_matches_canonical_content"
        )
        self.assertEqual(binding["status"], "pass")
        self.assertEqual(
            result["expected_pages"],
            [
                "summary",
                "flow-arrival",
                "global-game-system",
                "dev-core-requirement",
                "dev-core-level",
                "dev-core-developer",
            ],
        )
        composition = next(check for check in result["checks"] if check["check"] == "golden_page_composition")
        self.assertEqual(composition["status"], "pass")

    def test_renderer_adapts_golden_grid_columns_to_content_count(self) -> None:
        data = render_data()
        data["overview"]["journey"] = [
            {"title": f"Stage {index}", "description": f"Stage {index} result."}
            for index in range(1, 6)
        ]
        data["global_development"][0]["flow"] = [
            {"step": index, "title": f"Step {index}", "description": f"Do step {index}."}
            for index in range(1, 4)
        ]
        project = self.make_project(data)

        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = (project / "output" / "final.html").read_text(encoding="utf-8")
        self.assertIn('style="--prd-journey-columns:5"', html)
        self.assertIn('style="--prd-flow-columns:3"', html)
        self.assertIn(
            '.document-main .journey{grid-template-columns:repeat(var(--prd-journey-columns,6),1fr)}',
            html,
        )
        self.assertIn(
            '.document-main .flow{grid-template-columns:repeat(var(--prd-flow-columns,4),1fr)}',
            html,
        )

    def test_renderer_enforces_explicit_bilingual_localized_values(self) -> None:
        data = bilingual_render_data()
        data["overview"]["project_context"] = {"en": "English only."}
        project = self.make_project(data)

        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 2)
        self.assertNotIn("Traceback", rendered.stderr)
        self.assertIn(
            "render_data.overview.project_context.id is required for bilingual document",
            rendered.stderr,
        )
        self.assertFalse((project / "output" / "final.html").exists())

    def test_renderer_rejects_scalar_user_facing_text_in_bilingual_document(self) -> None:
        data = bilingual_render_data()
        data["packages"][0]["gameplay"]["main_objective"] = "English-only objective."
        project = self.make_project(data)

        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 2)
        self.assertNotIn("Traceback", rendered.stderr)
        self.assertIn(
            "render_data.packages[0].gameplay.main_objective must use an explicit en/id localized value",
            rendered.stderr,
        )
        self.assertFalse((project / "output" / "final.html").exists())

    def test_renderer_keeps_bilingual_switch_only_for_declared_bilingual_document(self) -> None:
        data = bilingual_render_data()
        data["overview"]["project_context"] = {
            "en": "A bilingual contract fixture.",
            "id": "Fixture kontrak bilingual.",
        }
        project = self.make_project(data)

        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = (project / "output" / "final.html").read_text(encoding="utf-8")
        self.assertIn('data-document-languages="en,id"', html)
        self.assertNotIn('id="prd-single-language-enforcer"', html)
        self.assertIn('data-id="Fixture kontrak bilingual."', html)
        self.assertIn('data-id="Gambaran Gameplay"', html)

    def test_renderer_applies_role_specific_terms_visibility(self) -> None:
        data = render_data()
        data["packages"][0]["terms"][0]["roles"] = ["gameplay", "developer"]
        project = self.make_project(data)

        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = (project / "output" / "final.html").read_text(encoding="utf-8")
        self.assertIn('dev-core-requirement-terms-used-details', html)
        self.assertNotIn('dev-core-level-terms-used-details', html)
        self.assertIn('dev-core-developer-terms-used-details', html)

    def test_renderer_rejects_unknown_term_role(self) -> None:
        data = render_data()
        data["packages"][0]["terms"][0]["roles"] = ["qa"]
        project = self.make_project(data)

        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 2)
        self.assertNotIn("Traceback", rendered.stderr)
        self.assertIn("roles contains unsupported role: qa", rendered.stderr)

    def test_validator_requires_flow2_ready_state(self) -> None:
        project = self.make_project(render_data())
        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        self.write_intake_state(project, status="needs_decision", ready=False)

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        self.assertEqual(result["status"], "fail")
        self.assertIn("flow2_ready_for_prd", "\n".join(result["errors"]))
        self.assertIn("status='needs_decision'", "\n".join(result["errors"]))

    def test_validator_rejects_missing_flow2_intake_state(self) -> None:
        project = self.make_project(render_data())
        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        (project / "state" / "intake-state.yaml").unlink()

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        self.assertIn("missing Flow 2 intake state", "\n".join(result["errors"]))

    def test_validator_rejects_stale_render_projection(self) -> None:
        project = self.make_project(render_data())
        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        (project / "work" / "content.md").write_text(
            "# Contract Fixture\n\nCanonical content changed after projection.\n",
            encoding="utf-8",
        )

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        joined = "\n".join(result["errors"])
        self.assertIn("render_data_matches_canonical_content", joined)
        self.assertIn("projection is stale", joined)

    def test_validator_rejects_missing_golden_composition_marker(self) -> None:
        project = self.make_project(render_data())
        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)

        html_path = project / "output" / "final.html"
        html = html_path.read_text(encoding="utf-8")
        generated_marker = 'production-table phase-overview-table quarry-overview-table'
        self.assertIn(generated_marker, html)
        html_path.write_text(
            html.replace(generated_marker, 'production-table phase-overview-table-broken quarry-overview-table', 1),
            encoding="utf-8",
        )

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        self.assertIn("golden_page_composition", "\n".join(result["errors"]))

    def test_renderer_keeps_glossary_script_context_safe(self) -> None:
        data = render_data()
        payload = "Before </script><script>window.injected=true</script> after"
        data["packages"][0]["terms"] = [
            {
                "key": "unsafe-term",
                "label": {"en": "Unsafe Term", "id": "Istilah Tidak Aman"},
                "definition": {"en": payload, "id": payload},
                "aliases": {"en": ["Unsafe Term"], "id": ["Istilah Tidak Aman"]},
            }
        ]
        project = self.make_project(data)

        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = (project / "output" / "final.html").read_text(encoding="utf-8")
        self.assertNotIn(payload, html)
        self.assertIn(
            r"Before \u003c/script\u003e\u003cscript\u003ewindow.injected=true\u003c/script\u003e after",
            html,
        )

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)

    def test_renderer_rejects_malformed_glossary_aliases(self) -> None:
        data = render_data()
        data["packages"][0]["terms"] = [
            {
                "key": "bad-alias",
                "label": "Bad Alias",
                "definition": "Alias shape is intentionally invalid.",
                "aliases": {"en": "not-an-array"},
            }
        ]
        project = self.make_project(data)

        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 2)
        self.assertNotIn("Traceback", rendered.stderr)
        self.assertIn("aliases.en must be an array of strings", rendered.stderr)
        self.assertFalse((project / "output" / "final.html").exists())

    def test_renderer_rejects_missing_or_ambiguous_required_shell_marker(self) -> None:
        project = self.make_project(render_data())
        template = APPROVED_TEMPLATE.read_text(encoding="utf-8")
        marker = '<nav class="sidebar-nav">'
        self.assertEqual(template.count(marker), 1)

        variants = {
            "missing": template.replace(marker, '<nav class="sidebar-nav-broken">', 1),
            "ambiguous": template.replace(marker, '<nav class="sidebar-nav"></nav>' + marker, 1),
        }
        for name, mutated in variants.items():
            with self.subTest(name=name):
                output = project / "output" / "final.html"
                if output.exists():
                    output.unlink()
                template_path = self.write_template(project, f"{name}.html", mutated)
                rendered = self.render(project, template_path)
                self.assertEqual(rendered.returncode, 2)
                self.assertNotIn("Traceback", rendered.stderr)
                self.assertIn("sidebar navigation marker", rendered.stderr)
                self.assertFalse(output.exists())

    def test_renderer_rejects_missing_description_metadata_marker(self) -> None:
        project = self.make_project(render_data())
        template = APPROVED_TEMPLATE.read_text(encoding="utf-8")
        pattern = re.compile(r'<meta\s+content="[^"]*"\s+name="description"\s*/?>', re.I)
        mutated, count = pattern.subn("", template, count=1)
        self.assertEqual(count, 1)
        template_path = self.write_template(project, "missing-description.html", mutated)

        rendered = self.render(project, template_path)
        self.assertEqual(rendered.returncode, 2)
        self.assertNotIn("Traceback", rendered.stderr)
        self.assertIn("description metadata marker", rendered.stderr)

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

    def test_validator_accepts_percentage_string_weights_totaling_100(self) -> None:
        data = render_data()
        data["packages"][0]["developer"]["scoring"]["components"] = [
            {"name": "Completion", "weight": "60%", "rule": "Completion contribution."},
            {"name": "Time", "weight": "40%", "rule": "Time contribution."},
        ]
        project = self.make_project(data)

        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)

    def test_validator_rejects_percentage_string_weights_above_100(self) -> None:
        data = render_data()
        data["packages"][0]["developer"]["scoring"]["components"] = [
            {"name": "Completion", "weight": "60%", "rule": "Completion contribution."},
            {"name": "Time", "weight": "50%", "rule": "Time contribution."},
        ]
        project = self.make_project(data)

        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        self.assertIn("scoring weights total 110", "\n".join(result["errors"]))

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
        self.assertIn("scoring weights total 90", joined)


if __name__ == "__main__":
    unittest.main()
