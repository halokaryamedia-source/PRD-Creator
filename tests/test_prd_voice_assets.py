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

TRIAL_CONSOLE_BLOCK = """#### Trial Console
ID: AST-CORE-CONSOLE
Type: MODEL
Function: Central interaction target used to complete the Core Trial.
Visual Brief: Compact trial console with one clear interaction face and a completion light on the same object.
Size: 2 × 1 × 2 blocks
Moment: Entering the Core Trial

"""

ASSETS = f"""# Production Asset Requirements

## Global / Shared Assets
Owner ID: shared

### UI & Information

#### Objective HUD
ID: AST-SHARED-OBJECTIVE-HUD
Type: UI / TEXT
Function: Shows the current objective during the journey.
Moment: During the Journey
Content:
```text
OBJECTIVE UPDATED
```

## 02. Core Trial
Owner ID: package:core

### 3D Models

{TRIAL_CONSOLE_BLOCK}### UI & Information

#### Trial Hologram
ID: AST-CORE-HOLOGRAM
Type: UI / TEXT
Function: Shows the current Core Trial instruction and its completion copy.
Moment: Entering the Core Trial
Content:
```text
BEGIN THE CORE TRIAL

TRIAL COMPLETE
```

### Visual Effects & Presentation

#### Trial Completion Reveal
ID: AST-CORE-COMPLETE-FX
Type: PARTICLE
Function: Marks successful completion of the Core Trial.
Visual Brief: Brief ring of particles around the trial console after valid completion.
Moment: Completing the Core Trial
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
            (project / "work/voice-requirements.md").write_text(requirements_text, encoding="utf-8")
            (project / "work/voice-production.md").write_text(voice_text, encoding="utf-8")
        if include_assets:
            (project / "work/asset-requirements.md").write_text(asset_text, encoding="utf-8")
        return project

    def render(self, project: Path):
        output = project / "output/final.html"
        return run_cli(RENDERER, project / "work/render-data.json", output), output

    @staticmethod
    def section_page(html: str, page_id: str) -> str:
        id_position = html.index(f'id="{page_id}"')
        start = html.rfind("<section", 0, id_position)
        end = html.index("</section>", id_position) + len("</section>")
        return html[start:end]

    def production_page(self, html: str, page_id: str) -> str:
        page = self.section_page(html, page_id)
        self.assertIn('data-page-role="production-assets"', page)
        return page

    def test_voice_uses_stable_owner_identity_for_objective_pages(self) -> None:
        rendered, output = self.render(self.make_project())
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = output.read_text(encoding="utf-8")
        self.assertIn('id="production-assets-journey-journey-begins"', html)
        self.assertIn('id="production-assets-core"', html)
        self.assertEqual(html.count('data-target="production-assets-'), 2)
        intro_page = self.production_page(html, "production-assets-journey-journey-begins")
        core_page = self.production_page(html, "production-assets-core")
        self.assertIn("<h2>Introduction · The Journey Begins</h2>", intro_page)
        self.assertIn("<h2>Fixture Package · Core Trial</h2>", core_page)
        self.assertIn("Narrator — Welcome", intro_page)
        self.assertIn("Guide — Complete", core_page)
        self.assertIn("Briefing", intro_page)

    def test_non_voice_assets_merge_by_owner_id_and_stable_asset_id(self) -> None:
        rendered, output = self.render(self.make_project(include_assets=True))
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = output.read_text(encoding="utf-8")
        shared_page = self.production_page(html, "production-assets-global-shared")
        core_page = self.production_page(html, "production-assets-core")
        self.assertIn("Objective HUD", shared_page)
        self.assertIn("AST-SHARED-OBJECTIVE-HUD".lower().replace("_", "-"), shared_page.lower())
        self.assertIn("Trial Console", core_page)
        self.assertIn("Trial Hologram", core_page)
        self.assertIn("Trial Completion Reveal", core_page)
        self.assertIn("BEGIN THE CORE TRIAL", core_page)
        self.assertIn("voice-prompt-vo-end-01", core_page)

    def test_04_does_not_change_protected_core_pages(self) -> None:
        baseline_result, baseline_output = self.render(self.make_project(include_voice=False, include_assets=False))
        completed_result, completed_output = self.render(self.make_project(include_voice=True, include_assets=True))
        self.assertEqual(baseline_result.returncode, 0, baseline_result.stderr or baseline_result.stdout)
        self.assertEqual(completed_result.returncode, 0, completed_result.stderr or completed_result.stdout)
        baseline_html = baseline_output.read_text(encoding="utf-8")
        completed_html = completed_output.read_text(encoding="utf-8")
        for page_id in (
            "summary", "flow-start", "flow-core", "development-overview", "shared-systems",
            "shared-data-reset", "phase-development", "dev-core-requirement", "dev-core-level",
            "dev-core-developer",
        ):
            self.assertEqual(self.section_page(baseline_html, page_id), self.section_page(completed_html, page_id))

    def test_asset_only_project_can_publish_production_assets(self) -> None:
        rendered, output = self.render(self.make_project(include_voice=False, include_assets=True))
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = output.read_text(encoding="utf-8")
        self.assertIn('id="production-assets-style"', html)
        self.assertIn('id="production-assets-objective-style"', html)
        self.assertIn("Trial Console", html)
        self.assertNotIn('class="pa-row pa-row-voice"', html)

    def test_renderer_rejects_duplicate_asset_id(self) -> None:
        duplicate = ASSETS.replace("AST-CORE-HOLOGRAM", "AST-CORE-CONSOLE")
        rendered, _ = self.render(self.make_project(include_voice=False, include_assets=True, asset_text=duplicate))
        self.assertEqual(rendered.returncode, 2)
        self.assertIn("Duplicate Production Asset ID: AST-CORE-CONSOLE", rendered.stderr)

    def test_renderer_rejects_duplicate_owner_id(self) -> None:
        duplicate = ASSETS.replace("Owner ID: package:core", "Owner ID: shared")
        rendered, _ = self.render(self.make_project(include_voice=False, include_assets=True, asset_text=duplicate))
        self.assertEqual(rendered.returncode, 2)
        self.assertIn("Duplicate Production Asset Owner ID: shared", rendered.stderr)

    def test_renderer_rejects_missing_asset_id(self) -> None:
        missing = ASSETS.replace("ID: AST-CORE-HOLOGRAM\n", "", 1)
        rendered, _ = self.render(self.make_project(include_voice=False, include_assets=True, asset_text=missing))
        self.assertEqual(rendered.returncode, 2)
        self.assertIn("requires stable ID", rendered.stderr)

    def test_voice_rendering_does_not_require_trigger_for_presentation(self) -> None:
        without_trigger = REQ.replace("- Trigger: Trial start before active play begins.\n", "", 1)
        rendered, output = self.render(self.make_project(requirements_text=without_trigger))
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        self.assertIn("Narrator — Welcome", output.read_text(encoding="utf-8"))

    def test_voice_rendering_rejects_missing_function(self) -> None:
        without_function = REQ.replace("- Function: briefing\n", "", 1)
        rendered, _ = self.render(self.make_project(requirements_text=without_function))
        self.assertEqual(rendered.returncode, 2)
        self.assertIn(
            "Voice requirement Function is required for Production Assets presentation: VO-INTRO-01",
            rendered.stderr,
        )

    def test_moment_order_uses_source_order_not_english_wording(self) -> None:
        ordered_assets = """# Production Asset Requirements

## 02. Core Trial
Owner ID: package:core

### UI & Information

#### Entry Message
ID: AST-CORE-ENTRY
Type: UI / TEXT
Function: Introduces the trial.
Moment: Entering the Core Trial
Content:
```text
ENTER
```

#### Persistent Status
ID: AST-CORE-STATUS
Type: UI / TEXT
Function: Shows the active trial status.
Moment: Throughout the Core Trial
Content:
```text
ACTIVE
```
"""
        rendered, output = self.render(
            self.make_project(include_voice=False, include_assets=True, asset_text=ordered_assets)
        )
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        page = self.production_page(output.read_text(encoding="utf-8"), "production-assets-core")
        self.assertLess(page.index("Entering the Core Trial"), page.index("Throughout the Core Trial"))

    def test_objective_page_id_is_stable_when_shared_assets_are_added(self) -> None:
        core_section = "# Production Asset Requirements\n\n## 02. Core Trial\nOwner ID: package:core\n\n" + ASSETS.split(
            "## 02. Core Trial\nOwner ID: package:core\n\n", 1
        )[1]
        without_shared, output_without = self.render(
            self.make_project(include_voice=False, include_assets=True, asset_text=core_section)
        )
        with_shared, output_with = self.render(self.make_project(include_voice=False, include_assets=True))
        self.assertEqual(without_shared.returncode, 0, without_shared.stderr or without_shared.stdout)
        self.assertEqual(with_shared.returncode, 0, with_shared.stderr or with_shared.stdout)
        self.assertIn('id="production-assets-core"', output_without.read_text(encoding="utf-8"))
        html_with = output_with.read_text(encoding="utf-8")
        self.assertIn('id="production-assets-global-shared"', html_with)
        self.assertIn('id="production-assets-core"', html_with)

    def test_voice_helper_uses_shared_parser_instead_of_duplicate_grammar(self) -> None:
        source = (
            ROOT / "kits" / "prd-creator" / "renderer" / "production_assets.py"
        ).read_text(encoding="utf-8")
        self.assertIn("from shared.voice import", source)
        self.assertNotIn("def parse_voice_production(", source)
        self.assertNotIn("ENTRY_RE = re.compile", source)


ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    unittest.main()
