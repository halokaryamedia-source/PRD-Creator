from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_prd_contracts import render_data as canonical_render_data

ROOT = Path(__file__).resolve().parents[1]
HANDOFF_VALIDATOR = ROOT / "kits" / "prd-creator" / "validator" / "validate_handoff.py"
RENDERER = ROOT / "kits" / "prd-creator" / "renderer" / "render.py"


def run_cli(*args: Path | str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *(str(arg) for arg in args)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


class PrdHandoffContracts(unittest.TestCase):
    def make_project(
        self,
        *,
        current_version: str = "1.0.0",
        accepted_version: str | None = None,
        status: str = "handoff_ready",
    ) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name)
        (project / "state").mkdir(parents=True)
        (project / "work").mkdir(parents=True)
        version_dir = project / "output" / f"v{current_version}"
        version_dir.mkdir(parents=True)

        accepted = accepted_version if accepted_version is not None else current_version
        (project / "state" / "intake-state.yaml").write_text(
            "status: ready_for_prd\nready_for_prd: true\n", encoding="utf-8"
        )
        (project / "state" / "source-inventory.yaml").write_text(
            "sources:\n  - id: SRC-001\n    inspection: full\n", encoding="utf-8"
        )
        (project / "state" / "requirement-register.yaml").write_text(
            "requirements:\n  - id: REQ-001\n    approval_status: approved\n", encoding="utf-8"
        )
        content_path = project / "work" / "content.md"
        content_path.write_text(
            "# Contract PRD\n\nCanonical fixture content with no unresolved placeholders.\n",
            encoding="utf-8",
        )
        data = canonical_render_data()
        data["document"]["version"] = current_version
        data["canonical_content_sha256"] = hashlib.sha256(content_path.read_bytes()).hexdigest()
        (project / "work" / "render-data.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        rendered = run_cli(
            RENDERER,
            project / "work" / "render-data.json",
            version_dir / "prd.html",
        )
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)

        (version_dir / "context.md").write_text(
            f"# Contract — Development Context\n\nPRD Version: v{current_version}\n", encoding="utf-8"
        )
        (version_dir / "index.json").write_text(
            json.dumps({"project": {"prd_version": current_version}}, indent=2) + "\n",
            encoding="utf-8",
        )
        (project / "output" / "README.md").write_text(
            f"# Contract\n\nCurrent PRD Version: `v{accepted}`\n", encoding="utf-8"
        )
        (project / "work" / "acceptance.md").write_text(
            f"# PRD Acceptance\n"
            f"Status: {status}\n"
            "Mechanical: PASS\n"
            "Semantic Readiness: PASS\n"
            "Material Conservation: PASS\n"
            "Visual sanity: NOT PROVEN\n"
            "Critical: 0\n"
            "Major: 0\n",
            encoding="utf-8",
        )
        (project / "state" / "handoff-state.yaml").write_text(
            f"status: {status}\n"
            f"accepted_prd_version: {accepted}\n"
            "content: work/content.md\n"
            "render_data: work/render-data.json\n"
            f"html: output/v{current_version}/prd.html\n"
            f"context: output/v{current_version}/context.md\n"
            f"index: output/v{current_version}/index.json\n"
            "acceptance: work/acceptance.md\n"
            "handoff: output/README.md\n",
            encoding="utf-8",
        )
        return project

    def test_current_handoff_allows_flow5_entry(self) -> None:
        project = self.make_project()
        validated = run_cli(HANDOFF_VALIDATOR, project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        self.assertEqual(json.loads(validated.stdout)["status"], "pass")

    def test_same_version_stale_prd_bytes_cannot_authorize_flow5(self) -> None:
        project = self.make_project()
        (project / "work" / "content.md").write_text(
            "# Contract PRD\n\nChanged after acceptance without regeneration.\n",
            encoding="utf-8",
        )
        validated = run_cli(HANDOFF_VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn(
            "current_prd_mechanical_freshness",
            "\n".join(json.loads(validated.stdout)["errors"]),
        )

    def test_pending_review_cannot_authorize_flow5(self) -> None:
        project = self.make_project(status="pending_review")
        validated = run_cli(HANDOFF_VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("handoff_status_ready", "\n".join(json.loads(validated.stdout)["errors"]))

    def test_stale_handoff_version_cannot_authorize_newer_prd(self) -> None:
        project = self.make_project(current_version="1.1.0", accepted_version="1.0.0")
        validated = run_cli(HANDOFF_VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("handoff_revision_matches_current_prd", "\n".join(json.loads(validated.stdout)["errors"]))

    def test_handoff_requires_existing_current_artifact_references(self) -> None:
        project = self.make_project()
        (project / "output" / "v1.0.0" / "context.md").unlink()
        validated = run_cli(HANDOFF_VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("handoff_artifact_references_current", "\n".join(json.loads(validated.stdout)["errors"]))

    def test_stale_delivery_metadata_cannot_authorize_handoff(self) -> None:
        project = self.make_project()
        index_path = project / "output" / "v1.0.0" / "index.json"
        index_path.write_text(
            json.dumps({"project": {"prd_version": "0.9.0"}}, indent=2) + "\n",
            encoding="utf-8",
        )
        validated = run_cli(HANDOFF_VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn(
            "delivery_revision_matches_current_prd",
            "\n".join(json.loads(validated.stdout)["errors"]),
        )

    def test_nonsemantic_version_cannot_authorize_handoff(self) -> None:
        project = self.make_project(current_version="Final Review")
        validated = run_cli(HANDOFF_VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        errors = "\n".join(json.loads(validated.stdout)["errors"])
        self.assertIn("current_prd_version_semantic", errors)

    def test_required_acceptance_gates_block_handoff_when_failed(self) -> None:
        variants = {
            "Status": "needs_revision",
            "Mechanical": "FAIL",
            "Semantic Readiness": "FAIL",
            "Material Conservation": "FAIL",
            "Visual sanity": "FAIL",
            "Critical": "1",
            "Major": "2",
        }
        for label, value in variants.items():
            with self.subTest(label=label):
                project = self.make_project()
                path = project / "work" / "acceptance.md"
                lines = path.read_text(encoding="utf-8").splitlines()
                path.write_text(
                    "\n".join(f"{label}: {value}" if line.startswith(f"{label}:") else line for line in lines) + "\n",
                    encoding="utf-8",
                )
                validated = run_cli(HANDOFF_VALIDATOR, project)
                self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
                self.assertIn("acceptance_allows_handoff", "\n".join(json.loads(validated.stdout)["errors"]))

    def test_missing_semantic_readiness_cannot_authorize_flow5(self) -> None:
        project = self.make_project()
        path = project / "work" / "acceptance.md"
        path.write_text(
            "\n".join(
                line
                for line in path.read_text(encoding="utf-8").splitlines()
                if not line.startswith("Semantic Readiness:")
            ) + "\n",
            encoding="utf-8",
        )
        validated = run_cli(HANDOFF_VALIDATOR, project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("Semantic Readiness must appear exactly once", validated.stdout)

    def test_visual_not_proven_is_valid_without_claiming_pass(self) -> None:
        project = self.make_project()
        validated = run_cli(HANDOFF_VALIDATOR, project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        self.assertIn("Visual sanity: NOT PROVEN", (project / "work" / "acceptance.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
