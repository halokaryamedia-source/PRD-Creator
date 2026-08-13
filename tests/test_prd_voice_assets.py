from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tests.test_prd_contracts import RENDERER, render_data, run_cli


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
    def make_project(self, *, include_voice: bool = True, voice_text: str = VOICE_PRODUCTION) -> Path:
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
        self.assertIn("Voice Production", html)
        self.assertIn("Voice Setup", html)
        self.assertIn("William Shanks - Rich and Deep", html)
        self.assertIn("Clara - Calm and Clear", html)
        self.assertIn("Eleven v3", html)
        self.assertIn("Enter the trial and follow the marked route.", html)
        self.assertIn("The trial is complete. Follow the open exit.", html)
        self.assertIn('data-voice-copy="voice-prompt-vo-intro-01"', html)
        self.assertIn('class="voice-script-panel"', html)
        self.assertIn('class="voice-performance-tag">[warm]</span>', html)
        self.assertIn('.voice-script-text{display:none}', html)
        self.assertIn('id="production-assets-style"', html)
        self.assertIn('id="production-assets-copy-script"', html)
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

    def test_prd_without_voice_keeps_production_assets_absent(self) -> None:
        project = self.make_project(include_voice=False)
        output = project / "output" / "final.html"

        rendered = run_cli(RENDERER, project / "work" / "render-data.json", output)
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)

        html = output.read_text(encoding="utf-8")
        self.assertNotIn('id="production-assets-style"', html)
        self.assertNotIn('id="production-assets-copy-script"', html)
        self.assertNotIn("production-assets-voice-1", html)


if __name__ == "__main__":
    unittest.main()