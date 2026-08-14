from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

import sys
RENDERER = ROOT / "kits" / "project-document-generator" / "renderer"
if str(RENDERER) not in sys.path:
    sys.path.insert(0, str(RENDERER))

import delivery  # noqa: E402


class PrdDeliveryContracts(unittest.TestCase):
    def make_project(self, *, version: str = "1.2.0") -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name) / "clockwork"
        (project / "work").mkdir(parents=True)
        (project / "state").mkdir(parents=True)
        (project / "output").mkdir(parents=True)

        (project / "work" / "render-data.json").write_text(
            json.dumps(
                {
                    "document": {
                        "title": "The Clockwork Vault",
                        "version": version,
                    }
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        (project / "work" / "content.md").write_text(
            "# The Clockwork Vault\n"
            "## 01. Overview\n"
            "A compact accepted overview.\n"
            "## 02. Gameplay Flow\n"
            "### The Broken Gallery\n"
            "Cross the gallery.\n"
            "## 03. Global Development\n"
            "### Data and Reset\n"
            "Reset must remain recoverable.\n"
            "## 04. The Broken Gallery\n"
            "### Gameplay Overview\n"
            "Three checkpoints.\n"
            "### Level Design\n"
            "Readable upper, lower, and side routes.\n"
            "### Developer\n"
            "Collapse occurs only in the final checkpoint.\n",
            encoding="utf-8",
        )
        (project / "work" / "voice-requirements.md").write_text(
            "# The Clockwork Vault Voice Requirements\n"
            "## 01. The Broken Gallery\n"
            "### VO-GAL-01\n"
            "- Trigger: The player enters the Broken Gallery.\n",
            encoding="utf-8",
        )
        (project / "state" / "handoff-state.yaml").write_text(
            "status: handoff_ready\n", encoding="utf-8"
        )
        return project

    @staticmethod
    def fake_html_renderer(template: Path | None, render_data: Path, output: Path) -> None:
        output.write_text("<!doctype html><title>Clockwork</title>\n", encoding="utf-8")

    def test_build_delivery_writes_short_versioned_bundle(self) -> None:
        project = self.make_project()
        outputs = delivery.build_delivery(project, html_renderer=self.fake_html_renderer)

        version_dir = project / "output" / "v1.2.0"
        self.assertEqual(outputs["prd"], version_dir / "prd.html")
        self.assertEqual(outputs["context"], version_dir / "context.md")
        self.assertEqual(outputs["index"], version_dir / "index.json")
        self.assertEqual(outputs["readme"], project / "output" / "README.md")
        for path in outputs.values():
            self.assertTrue(path.is_file(), path)

    def test_context_is_reasoning_surface_not_html_copy(self) -> None:
        project = self.make_project()
        delivery.build_delivery(project, html_renderer=self.fake_html_renderer)
        context = (project / "output" / "v1.2.0" / "context.md").read_text(encoding="utf-8")

        self.assertIn("## Reading Guidance", context)
        self.assertIn("### 04. The Broken Gallery", context)
        self.assertIn("#### Developer", context)
        self.assertIn("### Voice Requirements", context)
        self.assertIn("VO-GAL-01", context)
        self.assertNotIn("<!doctype html>", context)

    def test_index_is_compact_navigation_with_context_line_ranges(self) -> None:
        project = self.make_project()
        delivery.build_delivery(project, html_renderer=self.fake_html_renderer)
        version_dir = project / "output" / "v1.2.0"
        index_text = (version_dir / "index.json").read_text(encoding="utf-8")
        index = json.loads(index_text)
        context = (version_dir / "context.md").read_text(encoding="utf-8").splitlines()

        self.assertEqual(index["reading"]["primary"], "index.json")
        self.assertEqual(index["project"]["prd_version"], "1.2.0")
        self.assertNotIn("Collapse occurs only in the final checkpoint.", index_text)

        root = index["navigation"][0]
        accepted = next(child for child in root["children"] if child["title"] == "Accepted PRD")
        gallery = next(child for child in accepted["children"] if child["title"] == "04. The Broken Gallery")
        developer = next(child for child in gallery["children"] if child["title"] == "Developer")
        start, end = developer["lines"]
        excerpt = "\n".join(context[start - 1 : end])
        self.assertIn("Collapse occurs only in the final checkpoint.", excerpt)

    def test_readme_is_resume_entrypoint_and_lists_versions(self) -> None:
        project = self.make_project()
        (project / "output" / "v1.1.0").mkdir()
        delivery.build_delivery(project, html_renderer=self.fake_html_renderer)
        readme = (project / "output" / "README.md").read_text(encoding="utf-8")

        self.assertIn("Current PRD Version: `v1.2.0`", readme)
        self.assertIn("open `v1.2.0/index.json` first", readme)
        self.assertIn("`v1.2.0` — current", readme)
        self.assertIn("`v1.1.0`", readme)

    def test_delivery_requires_semantic_document_version(self) -> None:
        project = self.make_project(version="Final Review")
        with self.assertRaisesRegex(ValueError, "X.Y.Z"):
            delivery.build_delivery(project, html_renderer=self.fake_html_renderer)


if __name__ == "__main__":
    unittest.main()
