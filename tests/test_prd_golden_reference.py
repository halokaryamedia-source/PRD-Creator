from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "kits" / "project-document-generator"
GOLDEN = KIT / "template" / "golden-sample.html"
RUNTIME = KIT / "template" / "approved-document.html"


class GoldenReferenceArtifactTests(unittest.TestCase):
    def test_full_approved_golden_reference_is_retained(self) -> None:
        html = GOLDEN.read_text(encoding="utf-8")

        self.assertIn("AFTERSHOCK — Full Production Development Document V1.3", html)
        self.assertIn('name="golden-sample-id" content="aftershock"', html)
        self.assertIn('name="golden-sample-version" content="1.0"', html)

        # Canonical navigation/page vocabulary from the approved artifact.
        for marker in (
            'id="flow-start"',
            'id="development-overview"',
            'id="shared-systems"',
            'id="shared-data-reset"',
            'id="phase-development"',
            'class="nav-submenu phase-navigation"',
            'class="phase-nav-item"',
            'class="phase-page-link professional-nav-item"',
        ):
            self.assertIn(marker, html)

        # Representative page prototypes must stay available as actual reference evidence.
        for marker in (
            'class="sheet clean-visible story-page glossary-enabled-page"',
            'class="sheet professional-only quarry-package-page phase-package-page global-development-page glossary-enabled-page"',
            'class="phase-context-grid"',
            'class="flow quarry-development-flow"',
            'class="production-table quarry-build-table"',
            'class="production-table quarry-development-table"',
            'class="outcome quarry-note-grid"',
            'class="role-sequence quarry-sequence"',
            'class="definition-list quarry-definition-list glossary-definition-list"',
        ):
            self.assertIn(marker, html)

        # Keep dense approved examples, not only empty shells with the same headings.
        self.assertIn("Repairing the Broken Gangway", html)
        self.assertIn("Game System Setup", html)
        self.assertIn("Support several active players at the same time", html)

    def test_runtime_shell_is_not_allowed_to_replace_the_reference(self) -> None:
        golden = GOLDEN.read_text(encoding="utf-8")
        runtime = RUNTIME.read_text(encoding="utf-8")

        self.assertIn("__PRD_STORAGE_PREFIX__", runtime)
        self.assertNotEqual(golden, runtime)
        self.assertNotIn("__PRD_STORAGE_PREFIX__", golden)


if __name__ == "__main__":
    unittest.main()
