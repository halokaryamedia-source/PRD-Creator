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
Type: MODEL
Function: Central interaction target used to complete the Core Trial.
Visual Brief: Compact trial console with one clear interaction face and a completion light on the same object.
Size: 2 × 1 × 2 blocks
Moment: Entering the Core Trial

"""

ASSETS = f"""# Production Asset Requirements

## Global / Shared Assets

### UI & Information

#### Objective HUD
Type: UI / TEXT
Function: Shows the current objective during the journey.
Moment: During the Journey
Content:
```text
OBJECTIVE UPDATED
```

## 02. Core Trial

### 3D Models

{TRIAL_CONSOLE_BLOCK}### UI & Information

#### Trial Hologram
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

    def section_page(self, html: str, page_id: str) -> str:
        id_position = html.index(f'id="{page_id}"')
        start = html.rfind("<section", 0, id_position)
        end = html.index("</section>", id_position) + len("</section>")
        return html[start:end]

    def production_page(self, html: str, page_id: str) -> str:
        page = self.section_page(html, page_id)
        self.assertIn('data-page-role="production-assets"', page)
        return page

    def test_voice_uses_objective_first_production_assets_navigation(self) -> None:
        rendered, output = self.render(self.make_project())
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = output.read_text(encoding="utf-8")

        self.assertIn('class="nav-submenu phase-navigation"', html)
        self.assertIn('data-section-code="04"', html)
        self.assertIn('class="nav-group is-open professional-nav production-assets-nav"', html)
        self.assertIn('data-full-index="04" data-overview-index="">04</span>', html)
        self.assertEqual(html.count('data-target="production-assets-'), 2)
        self.assertIn('id="production-assets-journey-the-journey-begins"', html)
        self.assertIn('id="production-assets-core"', html)
        self.assertIn('data-en="PA-01" data-id="PA-01">PA-01</span>', html)
        self.assertIn('data-en="PA-02" data-id="PA-02">PA-02</span>', html)
        self.assertNotIn('class="production-assets-category"', html)
        self.assertIn('data-en="Introduction" data-id="Introduction">Introduction</span>', html)
        self.assertIn('data-en="Fixture Package" data-id="Fixture Package">Fixture Package</span>', html)

        intro_page = self.production_page(
            html, "production-assets-journey-the-journey-begins"
        )
        core_page = self.production_page(html, "production-assets-core")

        self.assertIn("<h2>Introduction · The Journey Begins</h2>", intro_page)
        self.assertIn("<h2>Fixture Package · Core Trial</h2>", core_page)
        self.assertIn('<span class="pa-type pa-type-audio">AUDIO</span>', intro_page)
        for label in (
            "Function",
            "Voice Preset",
            "ElevenLabs Model",
            "Estimated Duration",
            "Prompt",
        ):
            self.assertIn(label, intro_page)
        self.assertIn('data-pa-copy="voice-prompt-vo-intro-01"', intro_page)
        self.assertIn("William Shanks - Rich and Deep", intro_page)
        self.assertIn("Eleven v3", intro_page)
        self.assertIn("[calm]", intro_page)
        self.assertIn("Begin the trial.", intro_page)
        self.assertIn("Briefing", intro_page)
        self.assertIn("<h3>Welcome</h3>", intro_page)
        self.assertNotIn("Tell the player to begin the trial.", intro_page)
        self.assertNotIn("Story or character audio for this gameplay moment.", intro_page)
        self.assertNotIn('class="voice-script-context"', intro_page)
        self.assertNotIn('class="voice-production-block"', intro_page)
        self.assertNotIn("<h3>Audio</h3>", intro_page)

    def test_non_voice_assets_merge_into_the_same_objective_pages(self) -> None:
        rendered, output = self.render(self.make_project(include_assets=True))
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = output.read_text(encoding="utf-8")

        self.assertEqual(html.count('data-target="production-assets-'), 3)
        self.assertIn('id="production-assets-global-shared"', html)
        self.assertIn('id="production-assets-journey-the-journey-begins"', html)
        self.assertIn('id="production-assets-core"', html)
        self.assertIn('data-en="PA-03" data-id="PA-03">PA-03</span>', html)

        shared_page = self.production_page(html, "production-assets-global-shared")
        core_page = self.production_page(html, "production-assets-core")

        self.assertIn("Shared Assets", shared_page)
        self.assertIn('<span class="pa-type pa-type-ui-text">UI / TEXT</span>', shared_page)
        self.assertIn("Objective HUD", shared_page)
        self.assertIn("Shows the current objective during the journey.", shared_page)
        self.assertIn("OBJECTIVE UPDATED", shared_page)

        self.assertIn("Trial Console", core_page)
        self.assertIn("Trial Hologram", core_page)
        self.assertIn("Trial Completion Reveal", core_page)
        self.assertIn('<span class="pa-type pa-type-model">MODEL</span>', core_page)
        self.assertIn('<span class="pa-type pa-type-ui-text">UI / TEXT</span>', core_page)
        self.assertIn('<span class="pa-type pa-type-audio">AUDIO</span>', core_page)
        self.assertIn('<span class="pa-type pa-type-particle">PARTICLE</span>', core_page)
        self.assertIn("Central interaction target used to complete the Core Trial.", core_page)
        self.assertIn(
            "Compact trial console with one clear interaction face and a completion light on the same object.",
            core_page,
        )
        self.assertIn("2 × 1 × 2 blocks", core_page)
        self.assertIn("BEGIN THE CORE TRIAL", core_page)
        self.assertIn("TRIAL COMPLETE", core_page)
        self.assertIn("voice-prompt-vo-end-01", core_page)

        for legacy_dashboard in (
            "3D Models <b>",
            "UI &amp; Information <b>",
            "Audio <b>",
            "Visual Effects &amp; Presentation <b>",
            "Cinematic &amp; Presentation",
        ):
            self.assertNotIn(legacy_dashboard, html)

    def test_fresh_approved_fixture_adds_04_without_changing_core(self) -> None:
        baseline_result, baseline_output = self.render(
            self.make_project(include_voice=False, include_assets=False)
        )
        self.assertEqual(
            baseline_result.returncode,
            0,
            baseline_result.stderr or baseline_result.stdout,
        )
        baseline_html = baseline_output.read_text(encoding="utf-8")

        completed_result, completed_output = self.render(
            self.make_project(include_voice=True, include_assets=True)
        )
        self.assertEqual(
            completed_result.returncode,
            0,
            completed_result.stderr or completed_result.stdout,
        )
        completed_html = completed_output.read_text(encoding="utf-8")

        protected_core_ids = (
            "summary",
            "flow-start",
            "flow-core",
            "development-overview",
            "shared-systems",
            "shared-data-reset",
            "phase-development",
            "dev-core-requirement",
            "dev-core-level",
            "dev-core-developer",
        )
        for page_id in protected_core_ids:
            self.assertEqual(
                self.section_page(baseline_html, page_id),
                self.section_page(completed_html, page_id),
                f"04 changed protected core section {page_id}",
            )

        self.assertNotIn('data-page-role="production-assets"', baseline_html)
        self.assertIn('data-page-role="production-assets"', completed_html)

        shared_page = self.production_page(
            completed_html, "production-assets-global-shared"
        )
        intro_page = self.production_page(
            completed_html, "production-assets-journey-the-journey-begins"
        )
        core_page = self.production_page(completed_html, "production-assets-core")
        production_html = shared_page + intro_page + core_page

        for visible_type in (
            ">MODEL<",
            ">UI / TEXT<",
            ">AUDIO<",
            ">PARTICLE<",
        ):
            self.assertIn(visible_type, production_html)
        for moment in (
            "During the Journey",
            "Entering the Core Trial",
            "Completing the Core Trial",
        ):
            self.assertIn(moment, production_html)

        self.assertIn("Visual Brief", core_page)
        self.assertIn("2 × 1 × 2 blocks", core_page)
        self.assertIn("Player Text", shared_page + core_page)
        self.assertIn("Voice Preset", intro_page)
        self.assertIn("ElevenLabs Model", intro_page)
        self.assertIn("Estimated Duration", intro_page)
        self.assertIn("Prompt", intro_page)

        for retired_visible_field in (
            "<b>Requirement</b>",
            "<b>Usage</b>",
            "<b>Used At</b>",
            "<b>Speaker</b>",
            "<b>Context</b>",
            ">SEQUENCE<",
        ):
            self.assertNotIn(retired_visible_field, production_html)

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
        self.assertIn('<span class="pa-type pa-type-model">MODEL</span>', html)
        self.assertNotIn('<article class="voice-script-card">', html)

    def test_empty_compatibility_category_is_ignored_not_rendered(self) -> None:
        without_model = ASSETS.replace(TRIAL_CONSOLE_BLOCK, "")
        rendered, output = self.render(
            self.make_project(
                include_voice=False,
                include_assets=True,
                asset_text=without_model,
            )
        )
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = output.read_text(encoding="utf-8")
        self.assertNotIn("Trial Console", html)
        self.assertNotIn("3D Models <b>", html)
        self.assertIn("Trial Hologram", html)
        self.assertIn("Trial Completion Reveal", html)

    def test_renderer_rejects_voice_without_initial_performance_tag(self) -> None:
        bad = SCRIPT.replace("[calm]\nBegin the trial.", "Begin the trial.", 1)
        rendered, _ = self.render(self.make_project(voice_text=bad))
        self.assertEqual(rendered.returncode, 2)
        self.assertIn("must begin with at least one initial", rendered.stderr)

    def test_voice_rendering_does_not_depend_on_visible_trigger_context(self) -> None:
        without_trigger = REQ.replace(
            "- Trigger: Trial start before active play begins.\n", "", 1
        )
        rendered, output = self.render(
            self.make_project(requirements_text=without_trigger)
        )
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = output.read_text(encoding="utf-8")
        intro_page = self.production_page(
            html, "production-assets-journey-the-journey-begins"
        )
        self.assertIn('<span class="pa-type pa-type-audio">AUDIO</span>', intro_page)
        self.assertIn("Narrator — Welcome", intro_page)
        self.assertNotIn('class="voice-script-context"', intro_page)

    def test_voice_rendering_rejects_missing_function(self) -> None:
        without_function = REQ.replace(
            "- Function: briefing\n", "", 1
        )
        rendered, _ = self.render(
            self.make_project(requirements_text=without_function)
        )
        self.assertEqual(rendered.returncode, 2)
        self.assertIn(
            "Voice requirement Function is required for Production Assets presentation: VO-INTRO-01",
            rendered.stderr,
        )

    def test_moment_order_uses_source_order_not_english_wording(self) -> None:
        ordered_assets = """# Production Asset Requirements

## 02. Core Trial

### UI & Information

#### Entry Message
Type: UI / TEXT
Function: Introduces the trial.
Moment: Entering the Core Trial
Content:
```text
ENTER
```

#### Persistent Status
Type: UI / TEXT
Function: Shows the active trial status.
Moment: Throughout the Core Trial
Content:
```text
ACTIVE
```
"""
        rendered, output = self.render(
            self.make_project(
                include_voice=False,
                include_assets=True,
                asset_text=ordered_assets,
            )
        )
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        page = self.production_page(
            output.read_text(encoding="utf-8"), "production-assets-core"
        )
        self.assertLess(
            page.index("Entering the Core Trial"),
            page.index("Throughout the Core Trial"),
        )

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

    def test_objective_page_id_is_stable_when_shared_assets_are_added(self) -> None:
        core_section = "# Production Asset Requirements\n\n## 02. Core Trial\n\n" + ASSETS.split(
            "## 02. Core Trial\n\n", 1
        )[1]
        without_shared, output_without = self.render(
            self.make_project(
                include_voice=False,
                include_assets=True,
                asset_text=core_section,
            )
        )
        self.assertEqual(
            without_shared.returncode,
            0,
            without_shared.stderr or without_shared.stdout,
        )
        html_without = output_without.read_text(encoding="utf-8")
        self.assertIn('id="production-assets-core"', html_without)

        with_shared, output_with = self.render(
            self.make_project(include_voice=False, include_assets=True)
        )
        self.assertEqual(
            with_shared.returncode,
            0,
            with_shared.stderr or with_shared.stdout,
        )
        html_with = output_with.read_text(encoding="utf-8")
        self.assertIn('id="production-assets-global-shared"', html_with)
        self.assertIn('id="production-assets-core"', html_with)

    def test_voice_helper_module_contains_primitives_not_retired_compositor(self) -> None:
        source = (
            Path(__file__).resolve().parents[1]
            / "kits"
            / "project-document-generator"
            / "renderer"
            / "production_assets.py"
        ).read_text(encoding="utf-8")
        for marker in (
            "def voice_pages(",
            "def _production_assets_navigation(",
            "def augment_project_html(",
            "def _section_shell_html(",
        ):
            self.assertNotIn(marker, source)
        for marker in (
            "def parse_voice_production(",
            "def parse_voice_requirement_triggers(",
            "def _section_setup_html(",
            "def _entry_html(",
            "VOICE_STYLE =",
            "VOICE_COPY_SCRIPT =",
        ):
            self.assertIn(marker, source)


if __name__ == "__main__":
    unittest.main()
