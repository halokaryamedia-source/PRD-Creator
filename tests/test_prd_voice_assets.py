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
REQ = (
    requirements()
    .replace("## Intro", "## 01. The Journey Begins")
    .replace("## Ending", "## 02. Core Trial")
    .replace(
        "- Trigger: Trial start before active play begins.\n",
        "- Flow: 01 — Arrival\n"
        "- Moment: Entering the Fixture\n"
        "- For: Tell the player to begin the trial.\n"
        "- Trigger: Trial start before active play begins.\n",
        1,
    )
    .replace(
        "- Trigger: Trial completion after the final objective resolves.\n",
        "- Flow: 02 — Completion\n"
        "- Moment: Completing the Core Trial\n"
        "- For: Acknowledge that the trial is complete.\n"
        "- Trigger: Trial completion after the final objective resolves.\n",
        1,
    )
)

ASSETS = """# Production Asset Requirements

## Global / Shared Assets

### Gameplay Flow 01 — Shared Journey

### UI & Information

#### Objective HUD
Flow: 01 — Shared Journey
Moment: Throughout the Journey
Type: UI / TEXT
Function: Shows the current objective update in the shared HUD.
Content:
```text
OBJECTIVE UPDATED
```

## 02. Core Trial

### Gameplay Flow 01 — Trial Ready
### Gameplay Flow 02 — Trial Complete

### 3D Models

#### Trial Console
Flow: 01 — Trial Ready
Moment: Starting the Core Trial
Type: MODEL
Function: Main interaction object used to complete the Core Trial.
Visual Brief: One central trial console with distinct Ready and Complete visual states. The completion light change belongs to the same model setup.

### UI & Information

#### Trial Hologram
Flow: 01 — Trial Ready
Moment: Starting the Core Trial
Type: UI / TEXT
Function: Tells the player when to begin and confirms completion after success.
Content:
```text
BEGIN THE CORE TRIAL

TRIAL COMPLETE
```

### Visual Effects & Presentation

#### Trial Completion Reveal
Flow: 02 — Trial Complete
Moment: Completing the Core Trial
Type: PARTICLE
Function: Gives one short visual confirmation when the trial is completed.
Visual Brief: One brief standalone completion pulse around the trial area.
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

    def test_voice_uses_objective_first_moment_first_production_assets(self) -> None:
        rendered, output = self.render(self.make_project())
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = output.read_text(encoding="utf-8")

        self.assertIn('class="nav-submenu phase-navigation"', html)
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

        self.assertIn('<h2>Introduction · The Journey Begins</h2>', html)
        self.assertIn('<h2>Fixture Package · Core Trial</h2>', html)
        self.assertIn('<h3>Entering the Fixture</h3>', html)
        self.assertIn('<h3>Completing the Core Trial</h3>', html)
        self.assertIn('class="pa-type pa-type-audio">AUDIO</span>', html)
        self.assertIn('<b>Function</b><span>Tell the player to begin the trial.</span>', html)
        self.assertIn('<b>Voice Preset</b><span>William Shanks - Rich and Deep</span>', html)
        self.assertIn('<b>ElevenLabs Model</b><span>Eleven v3</span>', html)
        self.assertIn('<b>Estimated Duration</b><span>2–3 seconds</span>', html)
        self.assertIn('data-pa-copy="voice-prompt-vo-intro-01"', html)
        self.assertNotIn('<b>Speaker</b>', html)
        self.assertNotIn('VoiceLab', html)
        self.assertNotIn('class="pa-summary"', html)
        self.assertNotIn('class="voice-production-block"', html)

    def test_non_voice_assets_merge_into_the_same_reader_first_pages(self) -> None:
        rendered, output = self.render(self.make_project(include_assets=True))
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = output.read_text(encoding="utf-8")

        self.assertEqual(html.count('data-target="production-assets-'), 3)
        self.assertIn('id="production-assets-global-shared"', html)
        self.assertIn('id="production-assets-journey-the-journey-begins"', html)
        self.assertIn('id="production-assets-core"', html)
        self.assertIn('data-en="PA-03" data-id="PA-03">PA-03</span>', html)
        self.assertIn("Global / Shared Assets", html)
        self.assertIn("Trial Console", html)
        self.assertIn("Trial Hologram", html)
        self.assertIn("Trial Completion Reveal", html)
        self.assertIn("BEGIN THE CORE TRIAL", html)
        self.assertIn("TRIAL COMPLETE", html)
        self.assertIn('class="pa-type pa-type-model">MODEL</span>', html)
        self.assertIn('class="pa-type pa-type-ui-text">UI / TEXT</span>', html)
        self.assertIn('class="pa-type pa-type-audio">AUDIO</span>', html)
        self.assertIn('class="pa-type pa-type-particle">PARTICLE</span>', html)
        self.assertIn("Main interaction object used to complete the Core Trial.", html)
        self.assertIn("One central trial console with distinct Ready and Complete visual states.", html)
        self.assertNotIn("3D Models <b>", html)
        self.assertNotIn("UI &amp; Information <b>", html)
        self.assertNotIn("Visual Effects &amp; Presentation <b>", html)
        self.assertNotIn("Cinematic &amp; Presentation", html)
        self.assertNotIn("<b>Requirement</b>", html)
        self.assertNotIn("<b>Usage</b>", html)
        self.assertNotIn("<b>Used At</b>", html)

        core_start = html.index('id="production-assets-core"')
        core_end = html.index("</section>", core_start)
        core_page = html[core_start:core_end]
        self.assertIn("Trial Console", core_page)
        self.assertIn("Trial Hologram", core_page)
        self.assertIn("Trial Completion Reveal", core_page)
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
        self.assertIn("Trial Completion Reveal", html)
        self.assertNotIn('<article class="voice-script-card">', html)

    def test_reader_first_contract_owner_contains_integrated_readiness_gate(self) -> None:
        root = Path(__file__).resolve().parents[1]
        owner = (
            root / "kits" / "project-document-generator" / "PRODUCTION-ASSETS.md"
        ).read_text(encoding="utf-8")
        validation = (
            root / "kits" / "project-document-generator" / "VALIDATION.md"
        ).read_text(encoding="utf-8")

        self.assertIn("## 04 readiness gate", owner)
        for marker in (
            "Coverage",
            "Authority",
            "Actionability",
            "Context",
            "Purity",
            "Exactness",
            "Reader test",
            "Economy",
            "PRD-core protection",
        ):
            self.assertIn(marker, owner)
        self.assertIn("Production Assets", validation)
        self.assertIn("`PRODUCTION-ASSETS.md` readiness gate", validation)

    def test_renderer_rejects_voice_without_initial_performance_tag(self) -> None:
        bad = SCRIPT.replace("[calm]\nBegin the trial.", "Begin the trial.", 1)
        rendered, _ = self.render(self.make_project(voice_text=bad))
        self.assertEqual(rendered.returncode, 2)
        self.assertIn("must begin with at least one initial", rendered.stderr)

    def test_voice_requirement_trigger_is_not_visible_production_metadata(self) -> None:
        rendered, output = self.render(self.make_project())
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        html = output.read_text(encoding="utf-8")
        self.assertNotIn("Trial start before active play begins.", html)
        self.assertNotIn("Trial completion after the final objective resolves.", html)
        self.assertIn("Entering the Fixture", html)
        self.assertIn("Completing the Core Trial", html)

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
        core_section = (
            "# Production Asset Requirements\n\n## 02. Core Trial"
            + ASSETS.split("## 02. Core Trial", 1)[1]
        )
        without_shared, output_without = self.render(
            self.make_project(include_voice=False, include_assets=True, asset_text=core_section)
        )
        self.assertEqual(without_shared.returncode, 0, without_shared.stderr or without_shared.stdout)
        html_without = output_without.read_text(encoding="utf-8")
        self.assertIn('id="production-assets-core"', html_without)

        with_shared, output_with = self.render(
            self.make_project(include_voice=False, include_assets=True)
        )
        self.assertEqual(with_shared.returncode, 0, with_shared.stderr or with_shared.stdout)
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
