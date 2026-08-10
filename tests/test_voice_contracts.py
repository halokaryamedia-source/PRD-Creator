from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from docx import Document

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "kits" / "voice-production-kit" / "builder" / "build_docx.py"
VALIDATOR = ROOT / "kits" / "voice-production-kit" / "validator" / "validate.py"


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

## Intro

### VO-INTRO-01 — Welcome

- Type: {intro_type}
- Speaker: Narrator
- Channel: Direct
- Trigger: Trial start
- Must communicate:
  - Begin the trial.
- Must not add/repeat:
  - No additional project facts.
- Source refs:
  - Contract fixture.

## Ending

### VO-END-01 — Complete

- Type: Direct NPC Dialogue
- Speaker: Guide
- Channel: Direct
- Trigger: Trial completion
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
- Speaker: Narrator
- Channel: Direct
- Trigger: Never
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
Source Voice Requirements: work/voice-requirements.md

## Intro

### VO-INTRO-01 — Welcome
Type: Main Story
Estimated Duration: 2–3 seconds
```performance
[calm]
Begin the trial.
```

## Ending

### VO-END-01 — Complete
Type: Direct NPC Dialogue
Estimated Duration: 2–3 seconds
```performance
[clear]
The trial is complete.
```
"""


class VoiceProductionContracts(unittest.TestCase):
    def make_project(self, requirements_text: str | None = None, script_text: str = SCRIPT) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name)
        (project / "work").mkdir(parents=True)
        (project / "output").mkdir(parents=True)
        (project / "state").mkdir(parents=True)
        (project / "work" / "voice-requirements.md").write_text(
            requirements_text if requirements_text is not None else requirements(),
            encoding="utf-8",
        )
        (project / "work" / "voice-production.md").write_text(script_text, encoding="utf-8")
        (project / "state" / "voice-state.yaml").write_text(
            "status: voice_script_ready\nrevision: contract-1\n",
            encoding="utf-8",
        )
        return project

    def build(self, project: Path) -> subprocess.CompletedProcess[str]:
        return run_cli(
            BUILDER,
            project / "work" / "voice-production.md",
            project / "output" / "Voice Production.docx",
            "--requirements",
            project / "work" / "voice-requirements.md",
        )

    def test_builder_and_validator_happy_path_preserves_section_break_contract(self) -> None:
        project = self.make_project()

        built = self.build(project)
        self.assertEqual(built.returncode, 0, built.stderr or built.stdout)

        validated = run_cli(VALIDATOR, project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        self.assertIn("VOICE VALIDATION PASS", validated.stdout)

        doc = Document(project / "output" / "Voice Production.docx")
        headings = [
            paragraph
            for paragraph in doc.paragraphs
            if paragraph.style.name == "Heading 1"
        ]
        self.assertEqual([paragraph.text for paragraph in headings], ["Intro", "Ending"])
        self.assertIsNot(headings[0].paragraph_format.page_break_before, True)
        self.assertIs(headings[1].paragraph_format.page_break_before, True)

    def test_builder_rejects_missing_voice_id_parity(self) -> None:
        project = self.make_project(requirements(extra_id=True))

        built = self.build(project)
        self.assertEqual(built.returncode, 2)
        self.assertIn("Voice requirement parity failed", built.stderr)
        self.assertIn("missing script IDs: VO-EXTRA-01", built.stderr)

    def test_builder_rejects_type_mismatch(self) -> None:
        project = self.make_project(requirements(type_override="Direct NPC Dialogue"))

        built = self.build(project)
        self.assertEqual(built.returncode, 2)
        self.assertIn(
            "Voice Type differs from Flow 5 requirement for: VO-INTRO-01",
            built.stderr,
        )

    def test_builder_rejects_empty_section_without_traceback(self) -> None:
        script = SCRIPT.replace("## Ending", "## Empty Section\n\n## Ending", 1)
        project = self.make_project(script_text=script)

        built = self.build(project)
        self.assertEqual(built.returncode, 2)
        self.assertNotIn("Traceback", built.stderr)
        self.assertIn("Voice section has no entries: Empty Section", built.stderr)
        self.assertFalse((project / "output" / "Voice Production.docx").exists())


if __name__ == "__main__":
    unittest.main()
