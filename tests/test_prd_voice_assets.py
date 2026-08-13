from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tests.test_prd_contracts import RENDERER, render_data, run_cli
from tests.test_voice_contracts import SCRIPT as BASE_SCRIPT, requirements

SCRIPT = BASE_SCRIPT.replace("## Intro", "## 01. The Journey Begins").replace(
    "## Ending", "## 02. Core Trial"
)
REQ = requirements().replace("## Intro", "## 01. The Journey Begins").replace(
    "## Ending", "## 02. Core Trial"
)
ASSETS = """# Production Asset Requirements

## Global / Shared Assets

### UI & Information

#### Objective HUD
Requirement: Show the current objective in one shared HUD surface used across the complete journey.
Content:
```text
OBJECTIVE UPDATED
```

## 02. Core Trial

### 3D Models

#### Trial Console
Requirement: Create one central trial console with clearly different Ready and Complete states. When completed, the console lights and plays its short completion sound as one combined object response.
Usage: Ready during active play; Complete after the valid interaction resolves.

### UI & Information

#### Trial Hologram
Requirement: Show the active trial instruction beside the console and replace it with the completion state after success.
Content:
```text
BEGIN THE CORE TRIAL

TRIAL COMPLETE
```
"""


class ProjectHtmlProductionAssets(unittest.TestCase):
    def make_project(
        self,
        *,
        include_voice: bool = True,
        include_assets: bool = False,
        voice_text: str = SCRIPT,
        requirements_text: str = REQ,
        asset_text: str = ASSETS,
    ) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name)
        (project / "work").mkdir(parents=True)
        (project / "output").mkdir(parents=True)
        (project / "work/render-data.json").write_text(
            json.dumps(render_data(), ensure_ascii=False), encoding="utf-8"
        )
        if include_voice:
            (project / "work/voice-requirements.md").write_text(
                requirements_text, encoding="utf-8"
            )
            (project / "work/voice-production.md").write_text(
                voice_text, encoding="utf-8"
            )
        if include_assets:
            (project / "work/asset-requirements.md").write_text(
                asset_text, encoding="utf-8"
            )
        return project

    def render(self, project: Path):
        output = project / "output/final.html"
        result = run_cli(RENDERER, project / "work/render-data.json", output)
        return result, output

    def test_voice_uses_objective_first_production_assets_navigation(self) -> None:
        rendered, output = self.render(self.make_project())
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = output.read_text(encoding="utf-8")

        self.assertIn('class="nav-submenu phase-navigation"', html)
        self.assertIn('data-section-code="04"', html)
        self.assertIn('class="nav-group is-open professional-nav production-assets-nav"', html)
        self.assertIn('data-full-index="04" data-overview-index="">04</span>', html)
        self.assertEqual(html.count('data-target="production-assets-'), 2)
        self.assertNotIn('class="production-assets-category"', html)
        self.assertIn('data-en="Introduction" data-id="Introduction">Introduction</span>', html)
        self.assertIn('data-en="Fixture Package" data-id="Fixture Package">Fixture Package</span>', html)

        self.assertIn('<h2>Core Trial</h2>', html)
        self.assertIn('class="pa-summary"', html)
        self.assertIn('<h3>Audio</h3>', html)
        self.assertIn('class="voice-production-block"', html)
        self.assertIn('class="voice-script-context"', html)
        self.assertIn('data-voice-copy="voice-prompt-vo-intro-01"', html)
        self.assertIn("William Shanks - Rich and Deep", html)
        self.assertIn("Trial start before active play begins.", html)

    def test_non_voice_assets_merge_into_the_same_objective_pages(self) -> None:
        rendered, output = self.render(self.make_project(include_assets=True))
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = output.read_text(encoding="utf-8")

        self.assertEqual(html.count('data-target="production-assets-'), 3)
        self.assertIn("Global / Shared Assets", html)
        self.assertIn("Trial Console", html)
        self.assertIn("Trial Hologram", html)
        self.assertIn("BEGIN THE CORE TRIAL", html)
        self.assertIn("TRIAL COMPLETE", html)
        self.assertIn("3D Models <b>1</b>", html)
        self.assertIn("UI &amp; Information <b>1</b>", html)
        self.assertIn("Audio <b>1</b>", html)
        self.assertNotIn("Cinematic &amp; Presentation <b>0</b>", html)

        core_start = html.index("<h2>Core Trial</h2>")
        core_end = html.index('</section><div class="page-foot">', core_start)
        core_page = html[core_start:core_end]
        self.assertIn("Trial Console", core_page)
        self.assertIn("Trial Hologram", core_page)
        self.assertIn("voice-prompt-vo-end-01", core_page)

    def test_asset_only_project_can_publish_production_assets(self) -> None:
        rendered, output = self.render(
            self.make_project(include_voice=False, include_assets=True)
        )
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = output.read_text(encoding="utf-8")
        self.assertIn('id="production-assets-style"', html)
        self.assertIn('id="production-assets-objective-style"', html)
        self.assertNotIn('id="production-assets-copy-script"', html)
        self.assertIn("Trial Console", html)
        self.assertNotIn('<article class="voice-script-card">', html)

    def test_renderer_rejects_empty_asset_category(self) -> None:
        bad = ASSETS.replace(
            "#### Trial Console\nRequirement: Create one central trial console with clearly different Ready and Complete states. When completed, the console lights and plays its short completion sound as one combined object response.\nUsage: Ready during active play; Complete after the valid interaction resolves.\n\n",
            "",
        )
        rendered, _ = self.render(
            self.make_project(include_voice=False, include_assets=True, asset_text=bad)
        )
        self.assertEqual(rendered.returncode, 2)
        self.assertIn("contains empty categories", rendered.stderr)

    def test_renderer_rejects_voice_without_initial_performance_tag(self) -> None:
        bad = SCRIPT.replace("[calm]\nBegin the trial.", "Begin the trial.", 1)
        rendered, _ = self.render(self.make_project(voice_text=bad))
        self.assertEqual(rendered.returncode, 2)
        self.assertIn("must begin with at least one initial", rendered.stderr)

    def test_renderer_rejects_missing_requirement_trigger_context(self) -> None:
        bad = REQ.replace("- Trigger: Trial start before active play begins.\n", "", 1)
        rendered, _ = self.render(self.make_project(requirements_text=bad))
        self.assertEqual(rendered.returncode, 2)
        self.assertIn("Trigger missing", rendered.stderr)

    def test_prd_without_downstream_assets_keeps_production_assets_absent(self) -> None:
        rendered, output = self.render(
            self.make_project(include_voice=False, include_assets=False)
        )
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = output.read_text(encoding="utf-8")
        self.assertNotIn('id="production-assets-style"', html)
        self.assertNotIn('class="production-assets-nav"', html)
        self.assertIn('data-section-code="04"', html)
        self.assertIn('data-en="04A" data-id="04A">04A</span>', html)


if __name__ == "__main__":
    unittest.main()
