from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from tests.test_prd_contracts import RENDERER, render_data, run_cli


class PrdHierarchyContracts(unittest.TestCase):
    def make_project(self, data: dict) -> tuple[Path, object]:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name)
        (project / "work").mkdir(parents=True)
        (project / "output").mkdir(parents=True)
        content_path = project / "work" / "content.md"
        content_path.write_text("# Hierarchy Contract Fixture\n", encoding="utf-8")
        data["canonical_content_sha256"] = hashlib.sha256(content_path.read_bytes()).hexdigest()
        data_path = project / "work" / "render-data.json"
        data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        rendered = run_cli(RENDERER, data_path, project / "output" / "final.html")
        return project, rendered

    def test_renderer_rejects_collapsed_golden_hierarchy(self) -> None:
        variants = {
            "missing gameplay flow": lambda data: data.update({"gameplay_flow": []}),
            "missing global development": lambda data: data.update({"global_development": []}),
            "wrong global order": lambda data: data["global_development"].reverse(),
        }
        for name, mutate in variants.items():
            with self.subTest(name=name):
                data = render_data()
                mutate(data)
                project, rendered = self.make_project(data)
                self.assertEqual(rendered.returncode, 2)
                self.assertIn("PRD RENDER FAILED", rendered.stderr)
                self.assertFalse((project / "output" / "final.html").exists())


if __name__ == "__main__":
    unittest.main()
