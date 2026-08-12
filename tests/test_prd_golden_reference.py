from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "kits" / "project-document-generator"
GOLDEN = KIT / "template" / "golden-reference.html"
RUNTIME = KIT / "template" / "runtime-template.html"
APPROVED_GIT_BLOB = "e1dccd77d7a5335213caea7a09d74ba78b2ae8e1"
PACKAGES = ("docks", "quarry", "ascent", "beacon", "relay", "ending")
GLOBAL_PAGES = ("development-overview", "shared-systems", "shared-data-reset", "phase-development")


def section_html(document: str, section_id: str) -> str:
    match = re.search(
        rf'<section\b[^>]*\bid="{re.escape(section_id)}"[^>]*>(.*?)</section>',
        document,
        re.S,
    )
    if match is None:
        raise AssertionError(f"Golden section not found: {section_id}")
    return match.group(1)


def article_count_in_class(section: str, class_value: str) -> int:
    match = re.search(
        rf'<div class="{re.escape(class_value)}">(.*?)</div>',
        section,
        re.S,
    )
    if match is None:
        raise AssertionError(f"Golden component not found: {class_value}")
    return match.group(1).count("<article")


class GoldenReferenceArtifactTests(unittest.TestCase):
    def test_full_approved_golden_reference_is_retained(self) -> None:
        html = GOLDEN.read_text(encoding="utf-8")

        self.assertIn("AFTERSHOCK — Full Production Development Document V1.3", html)
        self.assertIn('name="golden-sample-id" content="aftershock"', html)
        self.assertIn('name="golden-sample-version" content="1.0"', html)

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

        self.assertIn("Repairing the Broken Gangway", html)
        self.assertIn("Game System Setup", html)
        self.assertIn("Support several active players at the same time", html)

    def test_reverse_maps_the_fixed_golden_fill_pattern(self) -> None:
        """Prove the fill contract from the exact approved Sample before testing generation."""
        html = GOLDEN.read_text(encoding="utf-8")

        summary = section_html(html, "summary")
        for marker in (
            'class="facts three"',
            "Session Model",
            "Target Playtime",
            "Game Structure",
            "Complete Gameplay Journey",
            "Global Gameplay Direction",
        ):
            self.assertIn(marker, summary)
        self.assertEqual(article_count_in_class(summary, "journey"), len(PACKAGES))

        flow_pages = ("flow-start",) + tuple(f"flow-{package}" for package in PACKAGES)
        for page_id in flow_pages:
            flow = section_html(html, page_id)
            self.assertIn('class="section-intro"', flow)
            self.assertIn('class="story-flow"', flow)
            self.assertIn('class="terms-used-collapsible"', flow)

        for page_id in GLOBAL_PAGES:
            page = section_html(html, page_id)
            self.assertEqual(article_count_in_class(page, "flow quarry-development-flow"), 4)
            self.assertEqual(article_count_in_class(page, "outcome quarry-note-grid"), 4)
            self.assertIn('class="production-table quarry-dev-table"', page)
            for heading in ("No.", "Setup", "Development Requirements", "System Result"):
                self.assertIn(heading, page)
            self.assertIn('class="terms-used-collapsible"', page)

        gameplay_information = (
            "Game Purpose",
            "Gameplay Time",
            "Starting Condition",
            "End Condition",
            "Fail Condition",
            "Scoring Criteria",
        )
        build_headers = (
            "No.",
            "Object",
            "Area Size",
            "Build and Visual Requirements",
            "Gameplay Function",
        )
        developer_headers = ("No.", "Setup", "Development Requirements", "Gameplay Function")

        for package in PACKAGES:
            gameplay = section_html(html, f"dev-{package}-requirement")
            self.assertEqual(article_count_in_class(gameplay, "phase-context-grid"), 3)
            for marker in ("Gameplay Context", "Main Objective", "Result", *gameplay_information):
                self.assertIn(marker, gameplay)
            self.assertEqual(gameplay.count('class="role-step"'), 5)
            self.assertIn('class="production-table phase-overview-table quarry-overview-table"', gameplay)
            self.assertIn('class="terms-used-collapsible"', gameplay)

            level = section_html(html, f"dev-{package}-level")
            self.assertEqual(article_count_in_class(level, "flow quarry-design-flow"), 4)
            self.assertEqual(article_count_in_class(level, "outcome quarry-note-grid"), 4)
            self.assertIn('class="production-table quarry-build-table"', level)
            for heading in build_headers:
                self.assertIn(heading, level)
            self.assertNotIn('class="terms-used-collapsible"', level)

            developer = section_html(html, f"dev-{package}-developer")
            self.assertEqual(article_count_in_class(developer, "flow quarry-development-flow"), 4)
            self.assertEqual(article_count_in_class(developer, "outcome quarry-note-grid"), 4)
            self.assertIn('class="production-table quarry-development-table"', developer)
            for heading in developer_headers:
                self.assertIn(heading, developer)
            self.assertNotIn('class="terms-used-collapsible"', developer)

        # Exact Sample signature. These counts verify our derived pattern, not new-project facts.
        self.assertEqual(html.count('class="story-flow"'), 7)
        self.assertEqual(html.count('class="phase-context-grid"'), 6)
        self.assertEqual(html.count('class="role-step"'), 30)
        self.assertEqual(html.count('class="flow quarry-design-flow"'), 6)
        self.assertEqual(html.count('class="flow quarry-development-flow"'), 10)
        self.assertEqual(html.count('class="outcome quarry-note-grid"'), 16)
        self.assertEqual(html.count('class="terms-used-collapsible"'), 17)

    def test_runtime_template_is_byte_identical_to_canonical_golden(self) -> None:
        golden = GOLDEN.read_bytes()
        runtime = RUNTIME.read_bytes()
        self.assertEqual(golden, runtime)
        self.assertNotIn(b"__PRD_STORAGE_PREFIX__", runtime)

        # Git blob SHA-1: sha1("blob <len>\0" + content)
        digest = hashlib.sha1(f"blob {len(golden)}\0".encode("ascii") + golden).hexdigest()
        self.assertEqual(digest, APPROVED_GIT_BLOB)


if __name__ == "__main__":
    unittest.main()
