from __future__ import annotations

import hashlib
import json
from pathlib import Path


def four_flow(prefix: str) -> list[dict]:
    return [
        {"step": index, "title": f"{prefix} {index}", "description": f"Complete {prefix.lower()} stage {index}."}
        for index in range(1, 5)
    ]


def four_notes(prefix: str) -> list[dict]:
    return [
        {
            "title": f"{prefix} Note {index}",
            "description": f"Keep {prefix.lower()} rule {index} explicit and consistent.",
        }
        for index in range(1, 5)
    ]


def global_section(section_id: str, title: str, purpose: str) -> dict:
    return {
        "id": section_id,
        "title": title,
        "subtitle": "Project-wide development",
        "overview": f"{title} owns {purpose} for the complete fixture journey.",
        "flow": four_flow(title),
        "requirements": [
            {
                "title": title,
                "items": [
                    {
                        "title": f"{title} Ownership",
                        "details": f"Keep the shared {purpose} explicit for the correct fixture session.",
                        "result": f"All packages use the same approved {purpose} rule.",
                    }
                ],
            }
        ],
        "notes": four_notes(title),
    }


def render_data() -> dict:
    return {
        "canonical_content_sha256": "0" * 64,
        "document": {
            "title": "Contract Fixture",
            "subtitle": "Gameplay & Development Specification",
            "document_type": "Adventure Map",
            "version": "1.0.0",
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
                {
                    "title": "Result Handling",
                    "description": "One valid run creates one package result and resets cleanly.",
                },
            ],
        },
        "gameplay_flow": [
            {
                "id": "journey-begins",
                "title": "The Journey Begins",
                "eyebrow": "Enter the controlled fixture",
                "narrative_context": "The player starts outside the trial and can already see the marked destination.",
                "beats": [
                    {
                        "title": "Arrival",
                        "description": "The player receives the first clear cue and follows the marked route.",
                    },
                    {
                        "title": "Trial Entrance",
                        "description": "The route ends at the Core Trial entrance with no competing objective.",
                    },
                ],
                "next_destination": "Core Trial",
            },
            {
                "id": "core",
                "title": "Core Trial",
                "eyebrow": "Complete one controlled interaction",
                "narrative_context": "The Core Trial is visible as soon as the player enters the isolated arena.",
                "beats": [
                    {
                        "title": "Start the Trial",
                        "description": "Entering the marked area activates the objective for the current session.",
                    },
                    {
                        "title": "Complete the Interaction",
                        "description": "The player performs the required interaction and receives immediate completion feedback.",
                    },
                    {
                        "title": "Leave the Trial",
                        "description": "The completed state opens the exit after the result is stored once.",
                    },
                ],
                "next_destination": "End of fixture journey",
            },
        ],
        "global_development": [
            global_section("development-overview", "Development Overview", "package topology and handoff"),
            global_section("game-system", "Game System", "session/runtime ownership"),
            global_section("data-reset", "Data and Reset", "result persistence, recovery, and reset"),
            global_section("gameplay-development", "Gameplay Development", "package lifecycle and integration"),
        ],
        "packages": [
            {
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
                    "result_model": {
                        "mode": "scored",
                        "summary": "Fixture Score uses 100% Completion for a valid run.",
                    },
                    "player_flow": [
                        {
                            "step": 1,
                            "title": "Enter",
                            "action": "Walk into the marked trial area.",
                            "result": "The trial becomes ready.",
                        },
                        {
                            "step": 2,
                            "title": "Activate",
                            "action": "Cross the approved start boundary.",
                            "result": "The trial activates once.",
                        },
                        {
                            "step": 3,
                            "title": "Interact",
                            "action": "Perform the required Core interaction.",
                            "result": "The interaction is accepted.",
                        },
                        {
                            "step": 4,
                            "title": "Complete",
                            "action": "Finish the valid interaction state.",
                            "result": "The Fixture Score is stored once.",
                        },
                        {
                            "step": 5,
                            "title": "Exit",
                            "action": "Follow the opened exit route.",
                            "result": "The package hands off cleanly.",
                        },
                    ],
                },
                "level_design": {
                    "overview": "Build one readable arena with a clear start, interaction target, and exit.",
                    "flow": four_flow("Design"),
                    "requirements": [
                        {
                            "title": "Trial Area",
                            "items": [
                                {
                                    "object": "Core Trial Space",
                                    "subtitle": "Primary gameplay area",
                                    "area_size": "One compact interaction route",
                                    "build_and_visual": "Keep the start, target, and exit readable without decorative obstruction.",
                                    "gameplay_function": "Supports the complete fixture trial from activation to exit.",
                                }
                            ],
                        }
                    ],
                    "notes": four_notes("Build"),
                },
                "developer": {
                    "overview": "Implement activation, result storage, interruption handling, and reset for the Core Trial.",
                    "flow": [
                        {
                            "step": 1,
                            "title": "Activate",
                            "description": "Start the objective once for the assigned session.",
                        },
                        {"step": 2, "title": "Validate", "description": "Accept only the required Core interaction."},
                        {
                            "step": 3,
                            "title": "Store Result",
                            "description": "Calculate and store one valid Fixture Score.",
                        },
                        {
                            "step": 4,
                            "title": "Handoff",
                            "description": "Open the exit and prepare the package for reset.",
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
                        "player_facing_display": "Show completion feedback but no separate score screen.",
                        "telemetry_export": "Keep the internal score out of external telemetry export.",
                    },
                    "reset": [
                        "Clear active trial state, restore the interaction, close the exit, and release the session for reuse."
                    ],
                    "reset_result": "The Core Trial returns to its initial reusable state.",
                    "notes": four_notes("Development"),
                },
                "terms": [
                    {
                        "key": "core-trial",
                        "label": "Core Trial",
                        "definition": "The complete fixture gameplay package from activation through exit.",
                    },
                    {
                        "key": "fixture-score",
                        "label": "Fixture Score",
                        "definition": "The Objective Score created by valid Core Trial completion.",
                        "roles": ["gameplay", "developer"],
                    },
                ],
            }
        ],
    }


def set_completion_only(data: dict) -> None:
    package = data["packages"][0]
    package["gameplay"]["result_model"] = {
        "mode": "completion_only",
        "summary": "No Objective Score — valid completion opens the fixture exit.",
    }
    developer = package["developer"]
    developer.pop("scoring", None)
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


def content_text() -> str:
    return "# Contract Fixture\n\nCanonical fixture content with no unresolved placeholders.\n"


def requirement_text() -> str:
    return (
        "requirements:\n"
        "  - id: REQ-001\n"
        "    area: gameplay\n"
        "    statement: Preserve the approved fixture experience.\n"
        "    provenance: [SRC-001]\n"
        "    impact: high\n"
    )


def source_text() -> str:
    return (
        "sources:\n"
        "  - id: SRC-001\n"
        "    type: instruction\n"
        "    role: authoritative\n"
        "    status: current\n"
        "    origin: user\n"
        "    summary: Contract fixture source.\n"
        "    inspection: full\n"
    )


def write_base_project(project: Path, data: dict | None = None) -> dict:
    for name in ("state", "work", "output"):
        (project / name).mkdir(parents=True, exist_ok=True)
    (project / "state" / "source-inventory.yaml").write_text(source_text(), encoding="utf-8")
    requirements = requirement_text()
    requirement_path = project / "state" / "requirement-register.yaml"
    requirement_path.write_text(requirements, encoding="utf-8")
    requirement_sha = hashlib.sha256(requirement_path.read_bytes()).hexdigest()
    (project / "state" / "intake-state.yaml").write_text(
        f"status: ready_for_prd\npreview_approved: true\napproved_requirement_sha256: {requirement_sha}\n",
        encoding="utf-8",
    )
    content_path = project / "work" / "content.md"
    content_path.write_text(content_text(), encoding="utf-8")
    payload = data if data is not None else render_data()
    payload["canonical_content_sha256"] = hashlib.sha256(content_path.read_bytes()).hexdigest()
    write_render_data(project, payload)
    return payload


def write_render_data(project: Path, data: dict) -> None:
    content_path = project / "work" / "content.md"
    data["canonical_content_sha256"] = hashlib.sha256(content_path.read_bytes()).hexdigest()
    (project / "work" / "render-data.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def asset_model_text() -> str:
    return (
        "# Production Asset Requirements\n\n"
        "## Core Trial\n"
        "Owner ID: package:core\n\n"
        "### 3D Models\n\n"
        "#### Trial Console\n"
        "ID: AST-CORE-CONSOLE\n"
        "Moment ID: MOM-TRIAL-INTERACTION\n"
        "Moment: Core Trial Interaction\n"
        "Type: MODEL\n"
        "Function: Central interaction target for the accepted Core Trial.\n"
        "Visual Brief: Readable trial console for the accepted Core Trial interaction.\n"
    )


def asset_ui_text() -> str:
    return (
        "# Production Asset Requirements\n\n"
        "## Core Trial\n"
        "Owner ID: package:core\n\n"
        "### UI & Information\n\n"
        "#### Trial Prompt\n"
        "ID: AST-CORE-PROMPT\n"
        "Moment ID: MOM-TRIAL-INTERACTION\n"
        "Moment: Core Trial Interaction\n"
        "Type: UI / TEXT\n"
        "Function: Shows the current Core Trial instruction.\n"
        "Content:\n"
        "```text\n"
        "BEGIN TRIAL\n"
        "```\n"
    )


def acceptance_text(project: Path, *, status: str = "handoff_ready") -> str:
    render_sha = hashlib.sha256((project / "work" / "render-data.json").read_bytes()).hexdigest()
    asset_path = project / "work" / "asset-requirements.md"
    asset_sha = hashlib.sha256(asset_path.read_bytes()).hexdigest() if asset_path.is_file() else "none"
    return (
        "# PRD Acceptance\n"
        f"Status: {status}\n"
        "Mechanical: PASS\n"
        "Semantic Readiness: PASS\n"
        "Material Conservation: PASS\n"
        "Visual sanity: NOT PROVEN\n"
        "Critical: 0\n"
        "Major: 0\n"
        f"Accepted Render Data SHA256: {render_sha}\n"
        f"Accepted Asset Requirements SHA256: {asset_sha}\n"
    )


def handoff_state_text(version: str = "1.0.0") -> str:
    base = f"output/v{version}"
    return (
        "status: handoff_ready\n"
        f"accepted_prd_version: {version}\n"
        "content: work/content.md\n"
        "render_data: work/render-data.json\n"
        f"html: {base}/prd.html\n"
        f"context: {base}/context.md\n"
        f"index: {base}/index.json\n"
        "acceptance: work/acceptance.md\n"
        "handoff: output/README.md\n"
    )