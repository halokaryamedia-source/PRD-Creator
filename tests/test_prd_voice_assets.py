from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tests.test_prd_contracts import RENDERER, render_data, run_cli


VOICE_REQUIREMENTS = """# Contract Fixture Voice Requirements

## 01. The Journey Begins

### VO-INTRO-01 — Welcome
- Type: Main Story
- Speaker: Narrator
- Trigger: The player enters the fixture and receives the first route cue.

## 02. Core Trial

### VO-CORE-01 — Trial Complete
- Type: Direct NPC Dialogue
- Speaker: Guide
- Trigger: The required Core interaction completes and the exit opens.
"""

VOICE_PRODUCTION = """# Contract Fixture Voice Production
Version: 1.0
Source Voice Requirements: work/voice-requirements.md

Voice Cast:
- Narrator: William Shanks - Rich and Deep
- Guide: Clara - Calm and Clear

## 01. The Journey Begins

### VO-INTRO-01 — Welcome
Type: Main Story
Speaker: Narrator
Estimated Duration: 3–4 seconds
```performance
[warm]
Enter the trial and follow the marked route.
```

## 02. Core Trial

### VO-CORE-01 — Trial Complete
Type: Direct NPC Dialogue
Speaker: Guide
Estimated Duration: 2–3 seconds
```performance
[clear]
The trial is complete. Follow the open exit.
```
"""


class ProjectHtmlVoiceAssets(unittest.TestCase):
    def make_project(
        self,
        *,
        include_voice: bool = True,
        voice_text: str = VOICE_PRODUCTION,
        requirements_text: str = VOICE_REQUIREMENTS,
    ) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name)
        (project / "work").mkdir(parents=True)
        (project / "output").mkdir(parents=True)
        (project / "work" / "render-data.json").write_text(
            json.dumps(render_data(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        if include_voice:
            (project / "work" / "voice-requirements.md").write_text(
                requirements_text,
                encoding="utf-8",
            )
            (project / "work" / "voice-production.md").write_text(
                voice_text,
                encoding="utf-8",
            )
        return project

    def test_voice_production_is_composed_into_same_prd_html(self) -> None:
        project = self.make_project()
        output = project / "output" / "final.html"

        rendered = run_cli(RENDERER, project / "work" / "render-data.json", output)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)

        html = output.read_text(encoding="utf-8")
        self.assertIn("Production Assets", html)
        self.assertIn("Voice Setup", html)
        self.assertIn("William Shanks - Rich and Deep", html)
        self.assertIn("Clara - Calm and Clear", html)
        self.assertIn("Eleven v3", html)
        self.assertIn("Enter the trial and follow the marked route.", html)
        self.assertIn("The trial is complete. Follow the open exit.", html)
        self.assertIn("The player enters the fixture and receives the first route cue.", html)
        self.assertIn("The required Core interaction completes and the exit opens.", html)
        self.assertIn("Voice Line", html)
        self.assertIn("1/1", html)
        self.assertIn('class="voice-objective-shell"', html)
        self.assertIn('class="voice-script-context"', html)
        self.assertIn('data-voice-copy="voice-prompt-vo-intro-01"', html)
        self.assertIn('class="voice-copy-label"', html)
        self.assertIn('data-en="Copy Prompt"', html)
        self.assertIn('class="voice-script-card"', html)
        self.assertIn('class="voice-performance-tag">[warm]</span>', html)
        self.assertIn(".voice-script-text{display:none}", html)
        self.assertIn(".voice-script-line{max-width:74ch", html)
        self.assertNotIn("ElevenLabs Text", html)
        self.assertIn('id="production-assets-style"', html)
        self.assertIn('id="production-assets-copy-script"', html)

        # Consolidated navigation: Production Assets is top-level 04,
        # then gameplay packages begin at 05.
        self.assertIn('class="nav-group is-open professional-nav production-assets-nav"', html)
        self.assertIn('data-full-index="04" data-overview-index="">04</span>', html)
        self.assertIn('class="nav-group is-open professional-nav production-objective-nav"', html)
        self.assertIn('data-full-index="05" data-overview-index="">05</span>', html)
        self.assertLess(
            html.index('data-full-index="04" data-overview-index="">04</span>'),
            html.index('data-full-index="05" data-overview-index="">05</span>'),
        )

        # Package page footer codes shift by one only in the consolidated
        # Production Assets document.
        self.assertIn('data-en="05A" data-id="05A">05A</span>', html)

        self.assertLess(
            html.index("Enter the trial and follow the marked route."),
            html.index("The trial is complete. Follow the open exit."),
        )

    def test_renderer_rejects_voice_without_initial_performance_tag(self) -> None:
        voice_text = VOICE_PRODUCTION.replace(
            "[warm]\nEnter the trial and follow the marked route.",
            "Enter the trial and follow the marked route.",
            1,
        )
        project = self.make_project(voice_text=voice_text)
        output = project / "output" / "final.html"

        rendered = run_cli(RENDERER, project / "work" / "render-data.json", output)
        self.assertEqual(rendered.returncode, 2)
        self.assertIn(
            "VO-INTRO-01 performance must begin with at least one initial [performance direction] tag",
            rendered.stderr,
        )

    def test_renderer_rejects_missing_requirement_trigger_context(self) -> None:
        requirements_text = VOICE_REQUIREMENTS.replace(
            "- Trigger: The player enters the fixture and receives the first route cue.\n",
            "",
            1,
        )
        project = self.make_project(requirements_text=requirements_text)
        output = project / "output" / "final.html"

        rendered = run_cli(RENDERER, project / "work" / "render-data.json", output)
        self.assertEqual(rendered.returncode, 2)
        self.assertIn(
            "Voice requirement Trigger missing for canonical production entry: VO-INTRO-01",
            rendered.stderr,
        )

    def test_prd_without_voice_keeps_production_assets_absent(self) -> None:
        project = self.make_project(include_voice=False)
        output = project / "output" / "final.html"

        rendered = run_cli(RENDERER, project / "work" / "render-data.json", output)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)

        html = output.read_text(encoding="utf-8")
        self.assertNotIn('id="production-assets-style"', html)
        self.assertNotIn('id="production-assets-copy-script"', html)
        self.assertNotIn("production-assets-voice-1", html)

        # No-Voice PRD keeps the original core navigation/page numbering.
        self.assertIn('data-section-code="04"', html)
        self.assertIn('data-en="04A" data-id="04A">04A</span>', html)


if __name__ == "__main__":
    unittest.main()
