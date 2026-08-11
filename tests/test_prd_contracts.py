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


def _global_section(section_id: str, title: str, purpose: str) -> dict:
    return {
        "id": section_id,
        "title": title,
        "subtitle": "Project-wide development",
        "overview": f"{title} owns {purpose} for the complete fixture journey.",
        "flow": [
            {
                "step": 1,
                "title": f"Prepare {title}",
                "description": f"Configure the shared {purpose} before package gameplay begins.",
                "result": f"{title} is ready for all packages.",
            }
        ],
        "requirements": [
            {
                "title": title,
                "items": [
                    {
                        "title": f"{title} Ownership",
                        "details": f"Keep the shared {purpose} explicit and isolated to the correct fixture session.",
                        "result": f"All packages use the same approved {purpose} rule.",
                    }
                ],
            }
        ],
        "notes": [
            {
                "title": f"{title} Boundary",
                "description": f"Do not move shared {purpose} behavior into one local package.",
            }
        ],
    }


def render_data() -> dict:
    return {
        "document": {
            "title": "Contract Fixture",
            "subtitle": "Gameplay & Development Specification",
            "document_type": "Production Specification",
            "version": "1.0",
        },
        "overview": {
            "project_context": "A controlled gameplay fixture used to prove the mandatory Golden PRD contract.",
            "main_experience": "The player enters one isolated session, completes the Core Trial, and returns with one valid result.",
            "document_scope": "Gameplay, Level Design, Developer implementation, result handling, and package verification.",
            "intended_use": "Primary production reference for Level Design and Development.",
            "facts": [
                {"key": "session-model", "label": "Session Model", "value": "1 player · 1 isolated session"},
                {"key": "target-playtime", "label": "Target Playtime", "value": "Short controlled run"},
                {"key": "game-structure", "label": "Game Structure", "value": "1 scored gameplay package"},
            ],
            "journey": [
                {"title": "The Journey Begins", "description": "Enter the fixture and learn why the Core Trial is active."},
                {"title": "Core Trial", "description": "Complete the controlled interaction and record one result."},
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
                "narrative_context": "The player arrives outside the controlled trial and can see the marked destination ahead.",
                "beats": [
                    {
                        "title": "Understand the Trial",
                        "description": "A clear fixture cue explains that the route leads to one controlled Core Trial.",
                    },
                    {
                        "title": "Enter the Route",
                        "description": "The player follows the marked path and reaches the trial entrance without another objective interrupting the journey.",
                    },
                ],
                "next_destination": "Core Trial",
            },
            {
                "id": "core",
                "title": "Core Trial",
                "narrative_context": "The player enters the isolated arena with the Core Trial target already visible.",
                "beats": [
                    {
                        "title": "Activate the Trial",
                        "description": "Entering the marked start area activates the Core Trial and confirms that the interaction is ready.",
                    },
                    {
                        "title": "Complete the Interaction",
                        "description": "The player performs the required interaction; the system confirms completion and records the package result once.",
                    },
                    {
                        "title": "Leave the Trial",
                        "description": "The completed state opens the exit and the player leaves with the fixture result already secured.",
                    },
                ],
                "next_destination": "End of fixture journey",
            },
        ],
        "global_development": [
            _global_section("development-overview", "Development Overview", "package topology and handoff"),
            _global_section("game-system", "Session & Runtime System", "session/runtime ownership"),
            _global_section("data-reset", "Data, Recovery & Reset", "result persistence, recovery, and reset"),
            _global_section("gameplay-development", "Gameplay Package Integration", "package lifecycle and integration"),
        ],
        "packages": [
            {
                "id": "core",
                "package_label": "Fixture Package",
                "title": "Core Trial",
                "acceptance": [
                    "Entering the approved start area activates the trial exactly once for the assigned session.",
                    "Completing the Core interaction stores one valid Fixture Score and opens the exit.",
                    "An interrupted run creates no score and reset restores the documented initial state.",
                    "The start, interaction target, and exit remain readable from the approved player route.",
                ],
                "gameplay": {
                    "context": "The player enters a controlled arena where one interaction target is visible from the start.",
                    "main_objective": "Activate and complete the Core Trial once.",
                    "result": "The package stores one valid Fixture Score and opens the exit.",
                    "purpose": "Prove one complete scored gameplay package without unrelated mechanics.",
                    "gameplay_time": "Short controlled run; no separate hard timeout is required for this fixture.",
                    "start_condition": "The player enters the marked trial start area in the assigned session.",
                    "end_condition": "The required interaction completes and the Fixture Score is stored once.",
                    "blocked_or_fail_condition": "No permanent gameplay fail; interruption ends the current run without a score, then reset restores the initial state.",
                    "player_flow": [
                        {
                            "step": 1,
                            "title": "Enter",
                            "action": "Walk into the marked trial area.",
                            "result": "The trial activates.",
                        },
                        {
                            "step": 2,
                            "title": "Complete",
                            "action": "Perform the required Core interaction.",
                            "result": "The result is stored and the exit opens.",
                        },
                    ],
                },
                "level_design": {
                    "overview": "Build one readable arena where the start, interaction target, and exit are understandable at a glance.",
                    "flow": [
                        {
                            "step": 1,
                            "title": "Establish the Route",
                            "details": "Place the start, visible target, and exit in one clear progression path.",
                        }
                    ],
                    "requirements": [
                        {
                            "title": "Trial Area",
                            "items": [
                                {
                                    "object": "Core Trial Space",
                                    "subtitle": "Primary gameplay area",
                                    "area_size": "Not specified — fit one controlled interaction route.",
                                    "build_and_visual": "Keep the start, target, and exit readable without decorative obstruction.",
                                    "gameplay_function": "Supports the complete fixture trial from activation to exit.",
                                }
                            ],
                        }
                    ],
                    "notes": [
                        {
                            "title": "Readable Destination",
                            "description": "The player must understand the interaction target before leaving the start area.",
                        }
                    ],
                },
                "developer": {
                    "overview": "Own activation, one deterministic score result, interruption handling, and reset for the Core Trial.",
                    "flow": [
                        {
                            "step": 1,
                            "trigger": "Player enters the trial",
                            "behavior": "Activate the objective once for the current session.",
                            "data": "Trial active state",
                            "result": "The interaction becomes valid.",
                        },
                        {
                            "step": 2,
                            "trigger": "Required interaction completes",
                            "behavior": "Stop the run, calculate the Fixture Score, store it once, and open the exit.",
                            "data": "Completion and score state",
                            "result": "The package is complete.",
                        },
                    ],
                    "requirements": [
                        {
                            "title": "Mechanic Setup",
                            "items": [
                                {
                                    "title": "Trial Activation",
                                    "details": "Activate only for the assigned session when the player enters the marked start area.",
                                    "result": "The objective starts once for the correct player.",
                                }
                            ],
                        }
                    ],
                    "scoring": {
                        "produces_score": True,
                        "score_name": "Fixture Score",
                        "scale": "0–100",
                        "components": [
                            {
                                "name": "Completion",
                                "weight": 100,
                                "rule": "Valid completion contributes the full package score.",
                            }
                        ],
                        "timer_start": "Trial activation.",
                        "timer_stop": "Valid trial completion.",
                        "no_score_condition": "Interrupted or invalid run.",
                        "duplicate_prevention": "Store at most one Fixture Score per run.",
                        "final_result_relationship": "Fixture Score is the only scored package result in this fixture.",
                        "player_facing_display": "Display completion feedback but do not show a separate score screen.",
                        "telemetry_export": "Store the internal score in the fixture result; no external telemetry export is required.",
                    },
                    "reset": ["Clear active trial state, restore the interaction, close the exit, and release the session for reuse."],
                    "reset_result": "The trial returns to its initial reusable state with no active progress or leftover result state.",
                    "notes": [
                        {
                            "title": "One Result",
                            "description": "A valid run creates one Fixture Score; interruption must not create a duplicate or partial score.",
                        }
                    ],
                },
                "terms": [
                    {
                        "key": "core-trial",
                        "label": "Core Trial",
                        "definition": "The complete fixture gameplay package from activation through result and exit.",
                    },
                    {
                        "key": "fixture-score",
                        "label": "Fixture Score",
                        "definition": "The Objective Score created by a valid Core Trial completion.",
                        "roles": ["gameplay", "developer"],
                    },
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
        (project / "state" / "intake-state.yaml").write_text(
            "status: ready_for_prd\nready_for_prd: true\nnext_step: Build canonical PRD content.\n",
            encoding="utf-8",
        )
        (project / "state" / "source-inventory.yaml").write_text(
            "sources:\n  - id: SRC-001\n    type: instruction\n    role: authoritative\n    origin: user\n    summary: Contract fixture source.\n    inspection: full\n",
            encoding="utf-8",
        )
        (project / "state" / "requirement-register.yaml").write_text(
            "requirements:\n  - id: REQ-001\n    area: gameplay\n    statement: Preserve the complete Golden mandatory fixture contract.\n    provenance: [SRC-001]\n    impact: high\n",
            encoding="utf-8",
        )
        (project / "work" / "content.md").write_text(
            "# Contract Fixture\n\nCanonical fixture content with no unresolved placeholders.\n",
            encoding="utf-8",
        )
        self.write_data(project, data)
        return project

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

    def test_full_golden_contract_renders_and_validates(self) -> None:
        project = self.make_project(render_data())
        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)

        html = (project / "output" / "final.html").read_text(encoding="utf-8")
        for text in (
            "Document Control",
            "document-control-strip",
            "Session &amp; Runtime System",
            "Data, Recovery &amp; Reset",
            "Gameplay Package Integration",
            "Objective Sequence",
            "Failure / Retry / Recovery",
            "Result / Scoring Model",
            "Area / Spatial Constraint",
            "Expected System Result",
            "Critical Constraints &amp; Notes",
            "Acceptance &amp; Verification",
            "Player-Facing Result",
            "Telemetry / Export",
            "flow-orientation",
            "developer-flow",
            "System Behavior",
            "Gameplay Journey",
            "Full Production",
            'data-package="core"',
            'data-glossary-scope="core-gameplay"',
            'data-glossary-scope="core-level-design"',
            'data-glossary-scope="core-developer"',
            'data-page-role="gameplay-flow"',
            "section[data-glossary-scope]",
        ):
            self.assertIn(text, html)

        glossary_match = re.search(r"const glossary = (.*?);\n\s*const tooltip =", html, re.S)
        self.assertIsNotNone(glossary_match)
        glossary_data = json.loads(glossary_match.group(1))
        self.assertEqual(
            {item["key"] for item in glossary_data["core-gameplay"]},
            {"core-trial", "fixture-score"},
        )
        self.assertEqual(
            {item["key"] for item in glossary_data["core-level-design"]},
            {"core-trial"},
        )
        self.assertEqual(
            {item["key"] for item in glossary_data["core-developer"]},
            {"core-trial", "fixture-score"},
        )

        for forbidden in ("aftershock-", "quarry-", "phase-"):
            self.assertNotIn(forbidden, html.lower())

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        result = json.loads(validated.stdout)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(
            result["expected_pages"],
            [
                "summary",
                "flow-journey-begins",
                "flow-core",
                "global-development-overview",
                "global-game-system",
                "global-data-reset",
                "global-gameplay-development",
                "dev-core-requirement",
                "dev-core-level",
                "dev-core-developer",
            ],
        )

    def test_template_has_no_reference_or_patch_history_slop(self) -> None:
        template = APPROVED_TEMPLATE.read_text(encoding="utf-8")
        for forbidden in (
            "aftershock-",
            "quarry-",
            "phase-",
            "V90",
            "V94",
            "V1.2",
            "v14-style",
            "v15-style",
            "v16-style",
            "v17-style",
            "v18-style",
            "golden-sample-version",
            "source-document",
            "template-extraction-version",
        ):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, template)
        self.assertEqual(template.count("<style>"), 1)
        self.assertIn("__PRD_STORAGE_PREFIX__", template)
        self.assertIn('id="prd-document-runtime"', template)
        self.assertIn('id="prd-global-glossary-script"', template)

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
                self.assertIn("Golden mandatory contract", rendered.stderr)
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
        data["packages"][0]["gameplay"]["result"] = "The package records completion only and opens the exit."
        project = self.make_project(data)

        rendered = self.render(project)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = (project / "output" / "final.html").read_text(encoding="utf-8")
        self.assertIn("No Objective Score", html)
        self.assertIn("This package contributes no Objective Score to the final result.", html)
        self.assertIn("Show completion feedback only; there is no score screen.", html)
        self.assertIn("Export completion state only; no Objective Score exists to export.", html)

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
        result = json.loads(validated.stdout)
        self.assertIn("html_matches_current_render_data", "\n".join(result["errors"]))

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

    def test_template_requires_current_golden_shell_markers(self) -> None:
        project = self.make_project(render_data())
        template = APPROVED_TEMPLATE.read_text(encoding="utf-8")
        broken = project / "broken-template.html"
        broken.write_text(
            template.replace('<nav class="sidebar-nav">', '<nav class="sidebar-nav-broken">', 1),
            encoding="utf-8",
        )
        rendered = self.render(project, broken)
        self.assertEqual(rendered.returncode, 2)
        self.assertIn("sidebar navigation marker", rendered.stderr)


if __name__ == "__main__":
    unittest.main()
