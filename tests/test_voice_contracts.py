from __future__ import annotations

import hashlib
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


def text_fingerprint(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def revision_identifier(requirements_text: str, script_text: str) -> str:
    return (
        f"voice-requirements-sha256={text_fingerprint(requirements_text)};"
        f"voice-script-sha256={text_fingerprint(script_text)}"
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


def script_for(requirements_text: str, intro_performance: str = "[calm]\nBegin the trial.") -> str:
    requirements_sha256 = text_fingerprint(requirements_text)
    return f"""# Contract Fixture Voice Production
Version: 1.0
Source Voice Requirements: work/voice-requirements.md
Source Voice Requirements SHA-256: {requirements_sha256}

## Intro

### VO-INTRO-01 — Welcome
Type: Main Story
Estimated Duration: 2–3 seconds
```performance
{intro_performance}
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
    def make_project(
        self,
        requirements_text: str | None = None,
        script_text: str | None = None,
    ) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name)
        (project / "work").mkdir(parents=True)
        (project / "output").mkdir(parents=True)
        (project / "state").mkdir(parents=True)

        req_text = requirements_text if requirements_text is not None else requirements()
        scr_text = script_text if script_text is not None else script_for(req_text)
        (project / "work" / "voice-requirements.md").write_text(req_text, encoding="utf-8")
        (project / "work" / "voice-production.md").write_text(scr_text, encoding="utf-8")
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

    def validate(self, project: Path) -> subprocess.CompletedProcess[str]:
        return run_cli(VALIDATOR, project)

    def test_builder_and_validator_happy_path_preserves_section_break_contract(self) -> None:
        req_text = requirements()
        scr_text = script_for(req_text)
        project = self.make_project(req_text, scr_text)

        built = self.build(project)
        self.assertEqual(built.returncode, 0, built.stderr or built.stdout)

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        self.assertIn("VOICE VALIDATION PASS", validated.stdout)
        self.assertIn("revision_integrity=passed", validated.stdout)
        self.assertIn("docx_entry_binding=passed", validated.stdout)

        doc = Document(project / "output" / "Voice Production.docx")
        self.assertEqual(
            doc.core_properties.identifier,
            revision_identifier(req_text, scr_text),
        )
        headings = [
            paragraph
            for paragraph in doc.paragraphs
            if paragraph.style.name == "Heading 1"
        ]
        self.assertEqual([paragraph.text for paragraph in headings], ["Intro", "Ending"])
        self.assertIsNot(headings[0].paragraph_format.page_break_before, True)
        self.assertIs(headings[1].paragraph_format.page_break_before, True)

    def test_builder_rejects_missing_voice_id_parity(self) -> None:
        req_text = requirements(extra_id=True)
        project = self.make_project(req_text, script_for(req_text))

        built = self.build(project)
        self.assertEqual(built.returncode, 2)
        self.assertIn("Voice requirement parity failed", built.stderr)
        self.assertIn("missing script IDs: VO-EXTRA-01", built.stderr)

    def test_builder_rejects_type_mismatch(self) -> None:
        req_text = requirements(type_override="Direct NPC Dialogue")
        project = self.make_project(req_text, script_for(req_text))

        built = self.build(project)
        self.assertEqual(built.returncode, 2)
        self.assertIn(
            "Voice Type differs from Flow 5 requirement for: VO-INTRO-01",
            built.stderr,
        )

    def test_builder_rejects_stale_requirements_revision_metadata(self) -> None:
        old_requirements = requirements()
        current_requirements = old_requirements.replace(
            "Begin the trial.",
            "Begin the updated trial.",
            1,
        )
        project = self.make_project(current_requirements, script_for(old_requirements))

        built = self.build(project)
        self.assertEqual(built.returncode, 2)
        self.assertIn("Voice Requirements SHA-256 does not match", built.stderr)
        self.assertFalse((project / "output" / "Voice Production.docx").exists())

    def test_validator_rejects_requirements_changed_without_downstream_rebuild(self) -> None:
        req_text = requirements()
        scr_text = script_for(req_text)
        project = self.make_project(req_text, scr_text)
        built = self.build(project)
        self.assertEqual(built.returncode, 0, built.stderr or built.stdout)

        changed = req_text.replace(
            "The trial is complete.",
            "The updated trial is complete.",
            1,
        )
        (project / "work" / "voice-requirements.md").write_text(changed, encoding="utf-8")

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("Script Voice Requirements revision mismatch", validated.stdout)
        self.assertIn("DOCX revision identifier mismatch", validated.stdout)

    def test_validator_rejects_script_changed_without_docx_rebuild(self) -> None:
        req_text = requirements()
        original_script = script_for(req_text)
        project = self.make_project(req_text, original_script)
        built = self.build(project)
        self.assertEqual(built.returncode, 0, built.stderr or built.stdout)

        changed_script = original_script.replace(
            "Begin the trial.",
            "Begin the trial now.",
            1,
        )
        (project / "work" / "voice-production.md").write_text(changed_script, encoding="utf-8")

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("DOCX revision identifier mismatch", validated.stdout)
        self.assertIn("DOCX performance text differs for VO-INTRO-01", validated.stdout)

    def test_validator_rejects_swapped_docx_performance_even_when_global_tokens_remain(self) -> None:
        req_text = requirements()
        scr_text = script_for(req_text)
        project = self.make_project(req_text, scr_text)
        built = self.build(project)
        self.assertEqual(built.returncode, 0, built.stderr or built.stdout)

        docx_path = project / "output" / "Voice Production.docx"
        doc = Document(docx_path)
        intro = next(paragraph for paragraph in doc.paragraphs if "Begin the trial." in paragraph.text)
        ending = next(paragraph for paragraph in doc.paragraphs if "The trial is complete." in paragraph.text)
        intro_text, ending_text = intro.text, ending.text
        intro.text = ending_text
        ending.text = intro_text
        doc.save(docx_path)

        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("DOCX performance text differs for VO-INTRO-01", validated.stdout)
        self.assertIn("DOCX performance text differs for VO-END-01", validated.stdout)
        self.assertNotIn("DOCX missing Voice ID tokens", validated.stdout)
        self.assertNotIn("DOCX has unexpected Voice ID tokens", validated.stdout)


if __name__ == "__main__":
    unittest.main()
