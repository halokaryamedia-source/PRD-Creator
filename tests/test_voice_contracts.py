from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

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

## Intro

### VO-INTRO-01 — Welcome

- Type: {intro_type}
- Function: briefing
- Necessity: required
- Speaker: Narrator
- Channel: Direct
- Trigger: Trial start before active play begins.
- Purpose: Tell the player to begin the trial.
- Timing Constraint: Must fit the 3-second opening slot.
- Must communicate:
  - Begin the trial.
- Must not add/repeat:
  - No additional project facts.
- Source refs:
  - Contract fixture.

## Ending

### VO-END-01 — Complete

- Type: Direct NPC Dialogue
- Function: completion
- Necessity: required
- Speaker: Guide
- Channel: Direct
- Trigger: Trial completion after the final objective resolves.
- Purpose: Acknowledge that the trial is complete.
- Must communicate:
  - The trial is complete.
- Must not add/repeat:
  - No additional reward.
- Source refs:
  - Contract fixture.
"""
    if extra_id:
        text += """
## Extra

### VO-EXTRA-01 — Unsupported Extra

- Type: Main Story
- Function: reminder
- Necessity: supporting
- Speaker: Narrator
- Channel: Direct
- Trigger: Never
- Purpose: Exercise the missing-ID parity failure.
- Must communicate:
  - This requirement is intentionally missing from the script.
- Must not add/repeat:
  - Nothing.
- Source refs:
  - Contract fixture.
"""
    return text


SCRIPT = """# Contract Fixture Voice Production
Version: 1.0
Source Voice Requirements: 1.0.0 / work/voice-requirements.md | sha256:{requirements_sha}

Voice Cast:
- Narrator: William Shanks - Rich and Deep
- Guide: Clara - Calm and Clear

## Intro

### VO-INTRO-01 — Welcome
Type: Main Story
Speaker: Narrator
Estimated Duration: 2–3 seconds
```performance
[calm]
Begin the trial.
```

## Ending

### VO-END-01 — Complete
Type: Direct NPC Dialogue
Speaker: Guide
Estimated Duration: 2–3 seconds
```performance
[clear]
The trial is complete.
```
"""


def project_html(*, omit_intro_prompt: bool = False) -> str:
    intro = "" if omit_intro_prompt else '<div class="pa-row pa-row-voice"><h4>Narrator — Welcome</h4><pre class="voice-script-text" id="voice-prompt-vo-intro-01">[calm]\nBegin the trial.</pre></div>'
    return f"""<!doctype html>
<html><head><style id="production-assets-style"></style></head><body>
<div class="nav-group production-assets-nav">Production Assets</div>
<section data-page-role="production-assets"><h2>Intro</h2>{intro}</section>
<section data-page-role="production-assets"><h2>Ending</h2>
<div class="pa-row pa-row-voice"><h4>Guide — Complete</h4><pre class="voice-script-text" id="voice-prompt-vo-end-01">[clear]\nThe trial is complete.</pre></div></section>
</body></html>"""


class VoiceProductionContracts(unittest.TestCase):
    def make_project(self, requirements_text: str | None = None, script_text: str = SCRIPT) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name)
        (project / "work").mkdir(parents=True)
        (project / "output").mkdir(parents=True)
        (project / "output" / "v1.0.0").mkdir(parents=True)
        (project / "state").mkdir(parents=True)
        req_text = requirements_text if requirements_text is not None else requirements()
        req_path = project / "work" / "voice-requirements.md"
        req_path.write_text(req_text, encoding="utf-8")
        bound_script = script_text.replace(
            "{requirements_sha}", hashlib.sha256(req_path.read_bytes()).hexdigest()
        )
        (project / "work" / "voice-production.md").write_text(bound_script, encoding="utf-8")
        (project / "work" / "render-data.json").write_text(
            json.dumps({"document": {"version": "1.0.0"}}, indent=2) + "\n",
            encoding="utf-8",
        )
        (project / "state" / "handoff-state.yaml").write_text(
            "status: handoff_ready\naccepted_prd_version: 1.0.0\n",
            encoding="utf-8",
        )
        (project / "state" / "voice-state.yaml").write_text(
            "status: voice_script_ready\n"
            "source_handoff: state/handoff-state.yaml\n"
            "source_prd_revision: 1.0.0\n"
            "project_html: output/v1.0.0/prd.html\n",
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

    def test_validator_accepts_current_project_html_objective_contract(self) -> None:
        project = self.make_project()
        (project / "output/v1.0.0/prd.html").write_text(project_html(), encoding="utf-8")

        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        self.assertIn("project_html=passed", validated.stdout)

    def test_validator_rejects_missing_voice_prompt_in_project_html(self) -> None:
        project = self.make_project()
        (project / "output/v1.0.0/prd.html").write_text(
            project_html(omit_intro_prompt=True),
            encoding="utf-8",
        )

        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 1)
        self.assertIn(
            "Project HTML must contain exact Voice prompt panel once for VO-INTRO-01",
            validated.stdout,
        )

    def test_validator_rejects_same_revision_requirement_bytes_changed_after_script_binding(self) -> None:
        project = self.make_project()
        req = project / "work/voice-requirements.md"
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
        state = project / "state/voice-state.yaml"
        state.write_text(
            state.read_text(encoding="utf-8").replace(
                "source_prd_revision: 1.0.0", "source_prd_revision: 0.9.0"
            ),
            encoding="utf-8",
        )
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("voice-state source_prd_revision='0.9.0'", validated.stdout)

    def test_validator_rejects_nonready_upstream_handoff(self) -> None:
        project = self.make_project()
        handoff = project / "state/handoff-state.yaml"
        handoff.write_text(
            handoff.read_text(encoding="utf-8").replace(
                "status: handoff_ready", "status: needs_revision"
            ),
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

    def test_validator_rejects_empty_section_without_traceback(self) -> None:
        script = SCRIPT.replace("## Ending", "## Empty Section\n\n## Ending", 1)
        project = self.make_project(script_text=script)
        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 2)
        self.assertNotIn("Traceback", validated.stderr)
        self.assertIn("Voice section has no entries: Empty Section", validated.stderr)

    def test_validator_rejects_voice_without_initial_performance_tag(self) -> None:
        script = SCRIPT.replace("[calm]\nBegin the trial.", "Begin the trial.", 1)
        project = self.make_project(script_text=script)

        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 2)
        self.assertIn(
            "VO-INTRO-01 performance must begin with at least one initial [performance direction] tag",
            validated.stderr,
        )

    def test_validator_has_no_docx_runtime_path(self) -> None:
        source = VALIDATOR.read_text(encoding="utf-8")
        self.assertNotIn("from docx import", source)
        self.assertNotIn("def validate_docx(", source)
        self.assertNotIn("Voice Production.docx", source)


if __name__ == "__main__":
    unittest.main()
