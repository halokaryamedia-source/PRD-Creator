from __future__ import annotations

import hashlib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "kits" / "project-document-generator"
GOLDEN = KIT / "template" / "golden-sample.html"
RUNTIME = KIT / "template" / "approved-document.html"
APPROVED_GIT_BLOB = "e1dccd77d7a5335213caea7a09d74ba78b2ae8e1"


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
