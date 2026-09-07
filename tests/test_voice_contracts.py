from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from prd_fixture import handoff_state_text, render_data, write_base_project

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "kits" / "prd-creator" / "validator" / "validate_voice.py"


def run_cli(*args: Path | str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *(str(arg) for arg in args)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def requirements(extra_id: bool = False, type_override: str | None = None) -> str:
    intro_type = type_override or "Main Story"
    text = f"""# Contract Fixture Voice Requirements

Source PRD revision: 1.0.0
Voice system: Narrator and Guide direct communication.

## Intro
Owner ID: journey:journey-begins

### VO-INTRO-01 — Welcome
- Type: {intro_type}
- Function: briefing
- Necessity: required
- Speaker: Narrator
- Channel: Direct
- Trigger: Trial start before active play begins.
- Purpose: Tell the player to begin the trial.
- Moment ID: MOM-INTRO-ARRIVAL
- Moment: Introduction Arrival
- Timing Constraint: Must fit the 3-second opening slot.
- Must communicate:
  - Begin the trial.
- Must not add/repeat:
  - No additional project facts.
- Source refs:
  - REQ-001

## Ending
Owner ID: package:core

### VO-END-01 — Complete
- Type: Direct NPC Dialogue
- Function: completion
- Necessity: required
- Speaker: Guide
- Channel: Direct
- Trigger: Trial completion after the final objective resolves.
- Purpose: Acknowledge that the trial is complete.
- Moment ID: MOM-CORE-COMPLETE
- Moment: Core Trial Completion
- Must communicate:
  - The trial is complete.
- Must not add/repeat:
  - No additional reward.
- Source refs:
  - REQ-001
"""
    if extra_id:
        text += """
### VO-EXTRA-01 — Unsupported Extra
- Type: Main Story
- Function: reminder
- Necessity: supporting
- Speaker: Guide
- Channel: Direct
- Trigger: A later completion reminder would play.
- Purpose: Exercise missing-ID parity.
- Moment ID: MOM-CORE-COMPLETE
- Moment: Core Trial Completion
- Must communicate:
  - The trial remains complete.
- Must not add/repeat:
  - No new reward.
- Source refs:
  - REQ-001
"""
    return text


SCRIPT = """# Contract Fixture Voice Production
Source Voice Requirements: 1.0.0 / work/voice-requirements.md | sha256:{requirements_sha}

Voice Cast:
- Narrator: William Shanks - Rich and Deep
- Guide: Clara - Calm and Clear

## Intro
Owner ID: journey:journey-begins

### VO-INTRO-01 — Welcome
Type: Main Story
Speaker: Narrator
Estimated Duration: 2–3 seconds
```performance
[calm]
Begin the trial.
```

## Ending
Owner ID: package:core

### VO-END-01 — Complete
Type: Direct NPC Dialogue
Speaker: Guide
Estimated Duration: 2–3 seconds
```performance
[clear]
The trial is complete.
```
"""


def voice_state(status: str = "voice_script_ready", *, include_html: bool = False) -> str:
    lines = [
        f"status: {status}",
        "source_handoff: state/handoff-state.yaml",
        "source_prd_revision: 1.0.0",
        "canonical_prd: work/content.md",
        "requirements: work/voice-requirements.md",
        "production: work/voice-production.md",
    ]
    if include_html:
        lines.append("project_html: output/v1.0.0/prd.html")
    return "\n".join(lines) + "\n"


def voice_acceptance(production_path: Path) -> str:
    digest = hashlib.sha256(production_path.read_bytes()).hexdigest()
    return (
        "# Voice Acceptance\n"
        "Status: voice_delivery_ready\n"
        "Mechanical: PASS\n"
        "Voice Script Readiness: PASS\n"
        "Communication Conservation: PASS\n"
        "Project HTML Visual: NOT PROVEN\n"
        "Audio Evidence: not_provided\n"
        "Critical: 0\n"
        "Major: 0\n"
        f"Accepted Voice Production SHA256: {digest}\n"
    )


def project_html(requirements_path: Path, production_path: Path, *, omit_intro_prompt: bool = False) -> str:
    req_sha = hashlib.sha256(requirements_path.read_bytes()).hexdigest()
    prod_sha = hashlib.sha256(production_path.read_bytes()).hexdigest()
    intro = "" if omit_intro_prompt else (
        '<div class="pa-moment" data-moment-id="MOM-INTRO-ARRIVAL">'
        '<div class="pa-row pa-row-voice"><h4>Narrator — Welcome</h4>'
        '<pre class="voice-script-text" id="voice-prompt-vo-intro-01">[calm]\nBegin the trial.</pre></div></div>'
    )
    return f"""<!doctype html>
<html><head>
<style id="production-assets-style"></style>
<meta content="{req_sha}" name="voice-requirements-sha256"/>
<meta content="{prod_sha}" name="voice-production-sha256"/>
</head><body>
<div class="nav-group production-assets-nav">Production Assets</div>
<section id="production-assets-journey-journey-begins" data-page-role="production-assets">{intro}</section>
<section id="production-assets-core" data-page-role="production-assets">
<div class="pa-moment" data-moment-id="MOM-CORE-COMPLETE">
<div class="pa-row pa-row-voice"><h4>Guide — Complete</h4>
<pre class="voice-script-text" id="voice-prompt-vo-end-01">[clear]\nThe trial is complete.</pre></div></div></section>
<script id="production-assets-script"></script>
</body></html>"""


class VoiceProductionContracts(unittest.TestCase):
    def make_project(
        self,
        requirements_text: str | None = None,
        script_text: str = SCRIPT,
        *,
        status: str = "voice_script_ready",
        include_html: bool = False,
        include_acceptance: bool = False,
    ) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name)
        write_base_project(project, render_data())
        (project / "output" / "v1.0.0").mkdir(parents=True, exist_ok=True)

        req_text = requirements_text if requirements_text is not None else requirements()
        req_path = project / "work" / "voice-requirements.md"
        req_path.write_text(req_text, encoding="utf-8")
        bound_script = script_text.replace(
            "{requirements_sha}",
            hashlib.sha256(req_path.read_bytes()).hexdigest(),
        )
        production_path = project / "work" / "voice-production.md"
        production_path.write_text(bound_script, encoding="utf-8")
        (project / "state" / "handoff-state.yaml").write_text(
            handoff_state_text(),
            encoding="utf-8",
        )
        (project / "state" / "voice-state.yaml").write_text(
            voice_state(status, include_html=include_html),
            encoding="utf-8",
        )
        if include_html:
            (project / "output" / "v1.0.0" / "prd.html").write_text(
                project_html(req_path, production_path),
                encoding="utf-8",
            )
        if include_acceptance:
            (project / "work" / "voice-acceptance.md").write_text(
                voice_acceptance(production_path),
                encoding="utf-8",
            )
        return project

    def test_validator_happy_path_needs_no_docx_export(self) -> None:
        project = self.make_project()
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        self.assertIn("VOICE VALIDATION PASS", validated.stdout)
        self.assertIn("project_html=not_provided", validated.stdout)
        self.assertNotIn("docx=", validated.stdout.casefold())

    def test_flow5_requirements_can_be_validated_before_script_readiness(self) -> None:
        project = self.make_project(status="voice_requirements_ready")
        (project / "work" / "voice-production.md").unlink()
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        self.assertIn("status=voice_requirements_ready", validated.stdout)
        self.assertIn("script_entries=0", validated.stdout)

    def test_validator_accepts_current_project_html_identity_contract(self) -> None:
        project = self.make_project(include_html=True)
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        self.assertIn("project_html=passed", validated.stdout)

    def test_validator_rejects_missing_voice_prompt_in_project_html(self) -> None:
        project = self.make_project(include_html=True)
        req_path = project / "work" / "voice-requirements.md"
        production_path = project / "work" / "voice-production.md"
        (project / "output" / "v1.0.0" / "prd.html").write_text(
            project_html(req_path, production_path, omit_intro_prompt=True),
            encoding="utf-8",
        )
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 1)
        self.assertIn("Project HTML must contain exact Voice prompt panel once for VO-INTRO-01", validated.stdout)

    def test_validator_rejects_same_revision_requirement_bytes_changed_after_script_binding(self) -> None:
        project = self.make_project()
        req = project / "work" / "voice-requirements.md"
        req.write_text(
            req.read_text(encoding="utf-8").replace(
                "Tell the player to begin the trial.",
                "Tell the player to begin the trial immediately.",
                1,
            ),
            encoding="utf-8",
        )
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("Source Voice Requirements sha256 does not match", validated.stdout)

    def test_validator_rejects_voice_state_from_stale_prd_revision(self) -> None:
        project = self.make_project()
        state = project / "state" / "voice-state.yaml"
        state.write_text(
            state.read_text(encoding="utf-8").replace(
                "source_prd_revision: 1.0.0",
                "source_prd_revision: 0.9.0",
            ),
            encoding="utf-8",
        )
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("voice-state source_prd_revision='0.9.0'", validated.stdout)

    def test_validator_rejects_unknown_voice_state_field(self) -> None:
        project = self.make_project()
        state = project / "state" / "voice-state.yaml"
        state.write_text(state.read_text(encoding="utf-8") + 'note: "voice #1"\n', encoding="utf-8")
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 2, validated.stderr or validated.stdout)
        self.assertIn("retired/unknown lifecycle field", validated.stderr)

    def test_validator_rejects_unsafe_voice_state_path(self) -> None:
        project = self.make_project()
        state = project / "state" / "voice-state.yaml"
        state.write_text(
            state.read_text(encoding="utf-8").replace(
                "requirements: work/voice-requirements.md",
                "requirements: ../outside.md",
            ),
            encoding="utf-8",
        )
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 2, validated.stderr or validated.stdout)
        self.assertIn("non-canonical path segment", validated.stderr)

    def test_validator_rejects_nonready_upstream_handoff(self) -> None:
        project = self.make_project()
        handoff = project / "state" / "handoff-state.yaml"
        handoff.write_text(
            handoff.read_text(encoding="utf-8").replace("status: handoff_ready", "status: needs_revision"),
            encoding="utf-8",
        )
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("Upstream PRD handoff status is 'needs_revision'", validated.stdout)

    def test_validator_rejects_missing_voice_id_parity(self) -> None:
        project = self.make_project(requirements(extra_id=True))
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("Script missing Voice IDs: VO-EXTRA-01", validated.stdout)

    def test_validator_rejects_type_mismatch(self) -> None:
        project = self.make_project(requirements(type_override="Direct NPC Dialogue"))
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("Type mismatch for VO-INTRO-01", validated.stdout)

    def test_validator_rejects_speaker_mismatch(self) -> None:
        script = SCRIPT.replace("Speaker: Narrator", "Speaker: Guide", 1)
        project = self.make_project(script_text=script)
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("Speaker mismatch for VO-INTRO-01", validated.stdout)

    def test_validator_rejects_owner_mismatch(self) -> None:
        script = SCRIPT.replace("Owner ID: package:core", "Owner ID: shared", 1)
        project = self.make_project(script_text=script)
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("Owner ID mismatch for VO-END-01", validated.stdout)

    def test_validator_rejects_duplicate_owner_id(self) -> None:
        script = SCRIPT.replace("Owner ID: package:core", "Owner ID: journey:journey-begins", 1)
        project = self.make_project(script_text=script)
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 2)
        self.assertIn("Duplicate Voice section Owner ID", validated.stderr)

    def test_validator_rejects_voice_without_initial_performance_tag(self) -> None:
        script = SCRIPT.replace("[calm]\nBegin the trial.", "Begin the trial.", 1)
        project = self.make_project(script_text=script)
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 2)
        self.assertIn("performance must begin", validated.stderr)

    def test_voice_delivery_ready_requires_current_acceptance(self) -> None:
        project = self.make_project(
            status="voice_delivery_ready",
            include_html=True,
            include_acceptance=True,
        )
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)

    def test_voice_delivery_ready_rejects_stale_production_acceptance(self) -> None:
        project = self.make_project(
            status="voice_delivery_ready",
            include_html=True,
            include_acceptance=True,
        )
        production = project / "work" / "voice-production.md"
        production.write_text(
            production.read_text(encoding="utf-8").replace(
                "Estimated Duration: 2–3 seconds",
                "Estimated Duration: 2–4 seconds",
                1,
            ),
            encoding="utf-8",
        )
        req = project / "work" / "voice-requirements.md"
        (project / "output" / "v1.0.0" / "prd.html").write_text(
            project_html(req, production),
            encoding="utf-8",
        )
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("Voice Acceptance is stale", validated.stdout)

    def test_voice_delivery_ready_requires_cast_selection_for_every_speaker(self) -> None:
        script = SCRIPT.replace("- Guide: Clara - Calm and Clear\n", "", 1)
        project = self.make_project(
            script_text=script,
            status="voice_delivery_ready",
            include_html=True,
            include_acceptance=True,
        )
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("requires a Voice Cast selection/profile for speaker: Guide", validated.stdout)

    def test_validator_has_no_docx_runtime_path(self) -> None:
        source = VALIDATOR.read_text(encoding="utf-8")
        self.assertNotIn("from docx import", source)
        self.assertNotIn("def validate_docx(", source)
        self.assertNotIn("Voice Production.docx", source)


if __name__ == "__main__":
    unittest.main()
