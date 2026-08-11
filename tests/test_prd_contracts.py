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
GOLDEN_TEMPLATE = ROOT / "kits" / "project-document-generator" / "template" / "golden-sample.html"
BILINGUAL_SCALAR_FIELDS = {
    "canonical_content_sha256", "id", "key", "code", "version", "brand_mark",
    "languages", "roles", "weight", "step", "no", "number", "formula",
}


def run_cli(*args: Path | str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *(str(arg) for arg in args)], cwd=ROOT,
        capture_output=True, text=True, check=False,
    )


def _four_flow(prefix: str) -> list[dict]:
    return [
        {"step": index, "title": f"{prefix} {index}", "description": f"Complete {prefix.lower()} stage {index}."}
        for index in range(1, 5)
    ]


def _four_notes(prefix: str) -> list[dict]:
    return [
        {"title": f"{prefix} Note {index}", "description": f"Keep {prefix.lower()} rule {index} explicit and consistent."}
        for index in range(1, 5)
    ]


def _global_section(section_id: str, title: str, purpose: str) -> dict:
    return {
        "id": section_id,
        "title": title,
        "subtitle": "Project-wide development",
        "overview": f"{title} owns {purpose} for the complete fixture journey.",
        "flow": _four_flow(title),
        "requirements": [{
            "title": title,
            "items": [{
                "title": f"{title} Ownership",
                "details": f"Keep the shared {purpose} explicit for the correct fixture session.",
                "result": f"All packages use the same approved {purpose} rule.",
            }],
        }],
        "notes": _four_notes(title),
    }


def render_data() -> dict:
    return {
        "document": {
            "title": "Contract Fixture",
            "subtitle": "Gameplay & Development Specification",
            "document_type": "Adventure Map",
            "version": "1.0",
        },
        "overview": {
            "project_context": "A controlled gameplay fixture proving the locked Golden PRD prototypes.",
            "main_experience": "The player enters one isolated session, completes the Core Trial, and returns with one valid result.",
            "document_scope": "Gameplay, Level Design, Developer implementation, result handling, and package verification.",
            "intended_use": "Primary production reference for Level Design and Development.",
            "facts": [
                {"key": "session-model", "label": "Session Model", "value": "1 player · 1 isolated session"},
                {"key": "target-playtime", "label": "Target Playtime", "value": "Short controlled run"},
                {"key": "game-structure", "label": "Game Structure", "value": "1 scored gameplay package"},
            ],
            "journey": [
                {"title": "The Journey Begins", "description": "Enter the fixture and approach the Core Trial."},
                {"title": "Core Trial", "description": "Complete the interaction and record one result."},
            ],
            "main_systems": [
                {"title": "Session Ownership", "description": "One player owns one isolated fixture session."},
                {"title": "Result Handling", "description": "One valid run creates one package result and resets cleanly."},
            ],
        },
        "gameplay_flow": [
            {
                "id": "journey-begins",
                "title": "The Journey Begins",
                "eyebrow": "Enter the controlled fixture",
                "narrative_context": "The player starts outside the trial and can already see the marked destination.",
                "beats": [
                    {"title": "Arrival", "description": "The player receives the first clear cue and follows the marked route."},
                    {"title": "Trial Entrance", "description": "The route ends at the Core Trial entrance with no competing objective."},
                ],
                "next_destination": "Core Trial",
            },
            {
                "id": "core",
                "title": "Core Trial",
                "eyebrow": "Complete one controlled interaction",
                "narrative_context": "The Core Trial is visible as soon as the player enters the isolated arena.",
                "beats": [
                    {"title": "Start the Trial", "description": "Entering the marked area activates the objective for the current session."},
                    {"title": "Complete the Interaction", "description": "The player performs the required interaction and receives immediate completion feedback."},
                    {"title": "Leave the Trial", "description": "The completed state opens the exit after the result is stored once."},
                ],
                "next_destination": "End of fixture journey",
            },
        ],
        "global_development": [
            _global_section("development-overview", "Development Overview", "package topology and handoff"),
            _global_section("game-system", "Game System", "session/runtime ownership"),
            _global_section("data-reset", "Data and Reset", "result persistence, recovery, and reset"),
            _global_section("gameplay-development", "Gameplay Development", "package lifecycle and integration"),
        ],
        "packages": [{
            "id": "core",
            "package_label": "Fixture Package",
            "title": "Core Trial",
            "acceptance": [
                "The approved start area activates the trial exactly once for the assigned session.",
                "Valid completion stores one Fixture Score and opens the exit.",
                "An interrupted run creates no score and reset restores the initial state.",
                "The start, interaction target, and exit remain readable from the player route.",
            ],
            "gameplay": {
                "context": "The player enters an isolated arena with one visible trial target.",
                "main_objective": "Activate and complete the Core Trial once.",
                "result": "One valid Fixture Score is stored and the exit opens.",
                "purpose": "Prove one complete scored gameplay package with a simple interaction.",
                "gameplay_time": "Short controlled run with no separate hard timeout.",
                "start_condition": "The player enters the marked start area in the assigned session.",
                "end_condition": "The required interaction completes and the Fixture Score is stored once.",
                "blocked_or_fail_condition": "There is no permanent fail state; interruption ends the run without a score.",
                "player_flow": [
                    {"step": 1, "title": "Enter", "action": "Walk into the marked trial area.", "result": "The trial becomes ready."},
                    {"step": 2, "title": "Activate", "action": "Cross the approved start boundary.", "result": "The trial activates once."},
                    {"step": 3, "title": "Interact", "action": "Perform the required Core interaction.", "result": "The interaction is accepted."},
                    {"step": 4, "title": "Complete", "action": "Finish the valid interaction state.", "result": "The Fixture Score is stored once."},
                    {"step": 5, "title": "Exit", "action": "Follow the opened exit route.", "result": "The package hands off cleanly."},
                ],
            },
            "level_design": {
                "overview": "Build one readable arena with a clear start, interaction target, and exit.",
                "flow": _four_flow("Design"),
                "requirements": [{
                    "title": "Trial Area",
                    "items": [{
                        "object": "Core Trial Space",
                        "subtitle": "Primary gameplay area",
                        "area_size": "One compact interaction route",
                        "build_and_visual": "Keep the start, target, and exit readable without decorative obstruction.",
                        "gameplay_function": "Supports the complete fixture trial from activation to exit.",
                    }],
                }],
                "notes": _four_notes("Build"),
            },
            "developer": {
                "overview": "Implement activation, result storage, interruption handling, and reset for the Core Trial.",
                "flow": [
                    {"step": 1, "title": "Activate", "description": "Start the objective once for the assigned session."},
                    {"step": 2, "title": "Validate", "description": "Accept only the required Core interaction."},
                    {"step": 3, "title": "Store Result", "description": "Calculate and store one valid Fixture Score."},
                    {"step": 4, "title": "Handoff", "description": "Open the exit and prepare the package for reset."},
                ],
                "requirements": [{
                    "title": "Mechanic Setup",
                    "items": [{
                        "title": "Trial Activation",
                        "details": "Activate only for the assigned session when the player enters the marked start area.",
                        "result": "The objective starts once for the correct player.",
                    }],
                }],
                "scoring": {
                    "produces_score": True,
                    "score_name": "Fixture Score",
                    "scale": "0–100",
                    "components": [{"name": "Completion", "weight": 100, "rule": "Valid completion contributes the full package score."}],
                    "timer_start": "Trial activation.",
                    "timer_stop": "Valid trial completion.",
                    "no_score_condition": "Interrupted or invalid run.",
                    "duplicate_prevention": "Store at most one Fixture Score per run.",
                    "final_result_relationship": "Fixture Score is the only scored package result in this fixture.",
                    "player_facing_display": "Show completion feedback but no separate score screen.",
                    "telemetry_export": "Keep the internal score out of external telemetry export.",
                },
                "reset": ["Clear active trial state, restore the interaction, close the exit, and release the session for reuse."],
                "reset_result": "The Core Trial returns to its initial reusable state.",
                "notes": _four_notes("Development"),
            },
            "terms": [
                {"key": "core-trial", "label": "Core Trial", "definition": "The complete fixture gameplay package from activation through exit."},
                {"key": "fixture-score", "label": "Fixture Score", "definition": "The Objective Score created by valid Core Trial completion.", "roles": ["gameplay", "developer"]},
            ],
        }],
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
        for name in ("state", "work", "output"):
            (project / name).mkdir(parents=True)
        (project / "state" / "intake-state.yaml").write_text(
            "status: ready_for_prd\nready_for_prd: true\nnext_step: Build canonical PRD content.\n", encoding="utf-8"
        )
        (project / "state" / "source-inventory.yaml").write_text(
            "sources:\n  - id: SRC-001\n    type: instruction\n    role: authoritative\n    origin: user\n    summary: Contract fixture source.\n    inspection: full\n", encoding="utf-8"
        )
        (project / "state" / "requirement-register.yaml").write_text(
            "requirements:\n  - id: REQ-001\n    area: gameplay\n    statement: Preserve the locked Golden prototype.\n    provenance: [SRC-001]\n    impact: high\n", encoding="utf-8"
        )
        (project / "work" / "content.md").write_text(
            "# Contract Fixture\n\nCanonical fixture content with no unresolved placeholders.\n", encoding="utf-8"
        )
        self.write_data(project, data)
        return project

    def write_data(self, project: Path, data: object) -> None:
        if isinstance(data, dict):
            data["canonical_content_sha256"] = hashlib.sha256((project / "work" / "content.md").read_bytes()).hexdigest()
        (project / "work" / "render-data.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def render(self, project: Path, template: Path | None = None) -> subprocess.CompletedProcess[str]:
        args: list[Path | str] = [RENDERER, project / "work" / "render-data.json", project / "output" / "final.html"]
        if template is not None:
            args.extend(["--template", template])
        return run_cli(*args)

    def validate(self, project: Path) -> subprocess.CompletedProcess[str]:
        return run_cli(VALIDATOR, project)

    def test_full_golden_contract_renders_and_validates(self) -> None:
        project = self.make_project(render_data())
        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = (project / "output" / "final.html").read_text(encoding="utf-8")

        required = (
            "Global Gameplay Direction", "Game System", "Data and Reset", "Gameplay Development",
            "Gameplay Context", "Main Objective", "Result", "Gameplay Information", "Gameplay Flow",
            "Fail Condition", "Scoring Criteria", "Area Size", "Build and Visual Requirements",
            "Important Build Notes", "Development Flow", "Development Requirements",
            "Gameplay Function", "Important Development Notes", "story-flow", "Terms Used",
            'id="flow-start"', 'id="development-overview"', 'id="shared-systems"',
            'id="shared-data-reset"', 'id="phase-development"',
            'data-phase="dev-flow"', 'data-phase="dev-core"',
            'class="nav-submenu phase-navigation"', 'class="phase-nav-item"',
            'class="phase-nav-main"', 'class="phase-page-link professional-nav-item"',
            'class="phase-context-grid"', 'class="flow quarry-development-flow"',
            'class="production-table phase-overview-table quarry-overview-table"',
            'class="role-sequence quarry-sequence"', 'class="production-table quarry-build-table"',
            'class="production-table quarry-development-table"', 'class="outcome quarry-note-grid"',
            'class="quarry-score-summary"',
        )
        for text in required:
            self.assertIn(text, html)

        forbidden = (
            "Document Control", "document-control-strip", "Session &amp; Runtime System",
            "Data, Recovery &amp; Reset", "Gameplay Package Integration", "Objective Sequence",
            "Failure / Retry / Recovery", "Result / Scoring Model", "Area / Spatial Constraint",
            "Expected System Result", "Critical Constraints &amp; Notes", "Acceptance &amp; Verification",
            "flow-orientation", "developer-flow", "System Behavior",
            "package-context-grid", "package-nav-main", "package-page-link", "package-navigation",
            "development-flow-grid", "design-flow-grid", "build-requirements-table",
            "development-requirements-table", "objective-sequence", 'data-glossary-scope=',
        )
        for text in forbidden:
            self.assertNotIn(text, html)

        level_section = re.search(r'<section[^>]+id="dev-core-level".*?</section>', html, re.S)
        developer_section = re.search(r'<section[^>]+id="dev-core-developer".*?</section>', html, re.S)
        gameplay_section = re.search(r'<section[^>]+id="dev-core-requirement".*?</section>', html, re.S)
        self.assertIsNotNone(level_section)
        self.assertIsNotNone(developer_section)
        self.assertIsNotNone(gameplay_section)
        self.assertNotIn("Terms Used", level_section.group(0))
        self.assertNotIn("Terms Used", developer_section.group(0))
        self.assertIn("Fixture Score", gameplay_section.group(0))

        glossary_match = re.search(r"const glossary = (.*?);\n\s*const tooltip =", html, re.S)
        self.assertIsNotNone(glossary_match)
        glossary_data = json.loads(glossary_match.group(1))
        self.assertEqual(set(glossary_data), {"core"})
        self.assertEqual({item["key"] for item in glossary_data["core"]}, {"core-trial", "fixture-score"})

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(
            result["expected_pages"],
            [
                "summary", "flow-start", "flow-core", "development-overview", "shared-systems",
                "shared-data-reset", "phase-development", "dev-core-requirement", "dev-core-level",
                "dev-core-developer",
            ],
        )

    def test_runtime_template_is_the_exact_golden_artifact(self) -> None:
        self.assertEqual(APPROVED_TEMPLATE.read_bytes(), GOLDEN_TEMPLATE.read_bytes())
        template = APPROVED_TEMPLATE.read_text(encoding="utf-8")
        self.assertIn('name="golden-sample-id" content="aftershock"', template)
        self.assertIn("quarry-", template)
        self.assertIn("phase-nav-", template)
        self.assertNotIn("__PRD_STORAGE_PREFIX__", template)
        self.assertGreater(template.count("<style"), 1)

    def test_renderer_rejects_missing_mandatory_golden_functions(self) -> None:
        variants = {
            "missing global function": lambda data: data["global_development"].pop(2),
            "missing package flow page": lambda data: data["gameplay_flow"].pop(),
            "missing document scope": lambda data: data["overview"].update({"document_scope": ""}),
            "missing gameplay time": lambda data: data["packages"][0]["gameplay"].update({"gameplay_time": ""}),
            "missing design flow": lambda data: data["packages"][0]["level_design"].update({"flow": []}),
            "missing developer reset": lambda data: data["packages"][0]["developer"].update({"reset": []}),
            "missing reset result": lambda data: data["packages"][0]["developer"].update({"reset_result": ""}),
            "missing acceptance": lambda data: data["packages"][0].update({"acceptance": []}),
        }
        for name, mutate in variants.items():
            with self.subTest(name=name):
                data = render_data()
                mutate(data)
                project = self.make_project(data)
                rendered = self.render(project)
                self.assertEqual(rendered.returncode, 2)
                self.assertFalse((project / "output" / "final.html").exists())

    def test_non_scored_package_is_explicit_not_omitted(self) -> None:
        data = render_data()
        developer = data["packages"][0]["developer"]
        developer.pop("scoring")
        developer["completion_data"] = {
            "produces_score": False,
            "completion_name": "Core Trial Completion",
            "valid_completion_condition": "The player completes the required Core interaction.",
            "recorded_data": "Store completion state for the current session.",
            "interrupted_completion_behavior": "Interrupted run stores no completion result.",
            "duplicate_prevention": "Record completion once per run.",
            "handoff_result": "Open the fixture exit and continue to the ending.",
            "final_result_relationship": "This package contributes no Objective Score to the final result.",
            "player_facing_display": "Show completion feedback only; there is no score screen.",
            "telemetry_export": "Export completion state only; no Objective Score exists to export.",
        }
        project = self.make_project(data)
        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = (project / "output" / "final.html").read_text(encoding="utf-8")
        self.assertIn("No Objective Score", html)
        self.assertIn("quarry-score-summary phase-score-summary", html)
        self.assertIn("score-table-wrap quarry-inline-score-table phase-inline-score-table", html)

    def test_percentage_string_does_not_render_double_percent(self) -> None:
        data = render_data()
        data["packages"][0]["developer"]["scoring"]["components"][0]["weight"] = "100%"
        project = self.make_project(data)
        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = (project / "output" / "final.html").read_text(encoding="utf-8")
        self.assertIn("100% Completion", html)
        self.assertNotIn("100%%", html)

    def test_bilingual_document_rejects_implicit_translation(self) -> None:
        data = bilingual_render_data()
        data["packages"][0]["gameplay"]["main_objective"] = "English-only objective."
        project = self.make_project(data)
        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 2)
        self.assertIn("must use an explicit en/id localized value", rendered.stderr)

    def test_validator_rejects_stale_html_after_projection_change(self) -> None:
        project = self.make_project(render_data())
        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        updated = render_data()
        updated["document"]["version"] = "1.1"
        self.write_data(project, updated)
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("html_matches_current_render_data", "\n".join(json.loads(validated.stdout)["errors"]))

    def test_glossary_json_is_script_safe(self) -> None:
        data = render_data()
        payload = "Before </script><script>window.injected=true</script> after"
        data["packages"][0]["terms"][0]["definition"] = payload
        project = self.make_project(data)
        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = (project / "output" / "final.html").read_text(encoding="utf-8")
        self.assertNotIn(payload, html)
        self.assertIn(r"\u003c/script\u003e", html)

    def test_default_runtime_strips_sample_identity_but_keeps_golden_runtime(self) -> None:
        project = self.make_project(render_data())
        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = (project / "output" / "final.html").read_text(encoding="utf-8")
        self.assertNotIn('name="golden-sample-id"', html)
        self.assertNotIn('name="source-document"', html)
        self.assertIn("prd-contract-fixture-document-theme", html)
        self.assertNotIn("aftershock-document-theme", html)

    def test_template_requires_current_golden_shell_markers(self) -> None:
        project = self.make_project(render_data())
        broken = project / "broken-template.html"
        broken.write_text(
            APPROVED_TEMPLATE.read_text(encoding="utf-8").replace('<nav class="sidebar-nav">', '<nav class="sidebar-nav-broken">', 1),
            encoding="utf-8",
        )
        rendered = self.render(project, broken)
        self.assertEqual(rendered.returncode, 2)
        self.assertIn("sidebar navigation marker", rendered.stderr)


if __name__ == "__main__":
    unittest.main()
