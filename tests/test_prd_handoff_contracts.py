from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from prd_fixture import (
    acceptance_text,
    asset_model_text,
    handoff_state_text,
    render_data,
    write_base_project,
    write_render_data,
)

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
        with_assets: bool = False,
    ) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        project = Path(temp.name)
        data = render_data()
        data["document"]["version"] = current_version
        write_base_project(project, data)
        if with_assets:
            (project / "work" / "asset-requirements.md").write_text(
                asset_model_text(),
                encoding="utf-8",
            )

        version_dir = project / "output" / f"v{current_version}"
        version_dir.mkdir(parents=True, exist_ok=True)
        rendered = run_cli(
            RENDERER,
            project / "work" / "render-data.json",
            version_dir / "prd.html",
        )
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)

        accepted = accepted_version if accepted_version is not None else current_version
        (version_dir / "context.md").write_text(
            f"# Contract — Development Context\n\nPRD Version: v{current_version}\n",
            encoding="utf-8",
        )
        (version_dir / "index.json").write_text(
            json.dumps({"project": {"prd_version": current_version}}, indent=2) + "\n",
            encoding="utf-8",
        )
        (project / "output" / "README.md").write_text(
            f"# Contract\n\nCurrent PRD Version: `v{accepted}`\n",
            encoding="utf-8",
        )
        acceptance = acceptance_text(project, status=status)
        (project / "work" / "acceptance.md").write_text(acceptance, encoding="utf-8")
        state_text = (
            handoff_state_text(current_version)
            .replace(
                "status: handoff_ready",
                f"status: {status}",
                1,
            )
            .replace(
                f"accepted_prd_version: {current_version}",
                f"accepted_prd_version: {accepted}",
                1,
            )
        )
        (project / "state" / "handoff-state.yaml").write_text(state_text, encoding="utf-8")
        return project

    def validate(self, project: Path):
        return run_cli(HANDOFF_VALIDATOR, project)

    def test_current_handoff_allows_flow5_entry(self) -> None:
        project = self.make_project()
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        self.assertEqual(json.loads(validated.stdout)["status"], "pass")

    def test_same_version_stale_prd_content_cannot_authorize_flow5(self) -> None:
        project = self.make_project()
        (project / "work" / "content.md").write_text(
            "# Contract PRD\n\nChanged after acceptance without regeneration.\n",
            encoding="utf-8",
        )
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("current_prd_complete_validation", validated.stdout)

    def test_same_version_regenerated_projection_requires_new_acceptance_binding(self) -> None:
        project = self.make_project()
        data_path = project / "work" / "render-data.json"
        data = json.loads(data_path.read_text(encoding="utf-8"))
        data["overview"]["project_context"] = "Changed projection under the same semantic version."
        write_render_data(project, data)
        rendered = run_cli(RENDERER, data_path, project / "output" / "v1.0.0" / "prd.html")
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("Accepted Render Data SHA256", validated.stdout)

    def test_same_version_asset_edit_requires_new_acceptance_binding(self) -> None:
        project = self.make_project(with_assets=True)
        asset_path = project / "work" / "asset-requirements.md"
        asset_path.write_text(
            asset_model_text().replace("Central interaction target", "Updated interaction target"),
            encoding="utf-8",
        )
        rendered = run_cli(
            RENDERER,
            project / "work" / "render-data.json",
            project / "output" / "v1.0.0" / "prd.html",
        )
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("Accepted Asset Requirements SHA256", validated.stdout)

    def test_content_purity_failure_cannot_authorize_handoff(self) -> None:
        project = self.make_project()
        data_path = project / "work" / "render-data.json"
        data = json.loads(data_path.read_text(encoding="utf-8"))
        data["overview"]["project_context"] = "Follow the Golden HTML Reference exactly."
        write_render_data(project, data)
        rendered = run_cli(RENDERER, data_path, project / "output" / "v1.0.0" / "prd.html")
        self.assertEqual(rendered.returncode, 0, rendered.stderr or rendered.stdout)
        acceptance = project / "work" / "acceptance.md"
        text = acceptance.read_text(encoding="utf-8")
        new_sha = hashlib.sha256(data_path.read_bytes()).hexdigest()
        old_line = next(line for line in text.splitlines() if line.startswith("Accepted Render Data SHA256:"))
        acceptance.write_text(
            text.replace(old_line, f"Accepted Render Data SHA256: {new_sha}"),
            encoding="utf-8",
        )
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("content_purity", validated.stdout)

    def test_pending_review_cannot_authorize_flow5(self) -> None:
        project = self.make_project(status="needs_revision")
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("handoff_status_ready", validated.stdout)

    def test_stale_handoff_version_cannot_authorize_newer_prd(self) -> None:
        project = self.make_project(current_version="1.1.0", accepted_version="1.0.0")
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("handoff_revision_matches_current_prd", validated.stdout)

    def test_handoff_requires_existing_current_artifact_references(self) -> None:
        project = self.make_project()
        (project / "output" / "v1.0.0" / "context.md").unlink()
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("handoff_artifact_references_current", validated.stdout)

    def test_stale_delivery_metadata_cannot_authorize_handoff(self) -> None:
        project = self.make_project()
        index_path = project / "output" / "v1.0.0" / "index.json"
        index_path.write_text(
            json.dumps({"project": {"prd_version": "0.9.0"}}, indent=2) + "\n",
            encoding="utf-8",
        )
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("delivery_revision_matches_current_prd", validated.stdout)

    def test_nonsemantic_version_cannot_authorize_handoff(self) -> None:
        project = self.make_project(current_version="Final Review")
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("current_prd_version_semantic", validated.stdout)

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
                validated = self.validate(project)
                self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
                self.assertIn("acceptance_allows_handoff", validated.stdout)

    def test_missing_asset_acceptance_binding_cannot_authorize_flow5(self) -> None:
        project = self.make_project()
        path = project / "work" / "acceptance.md"
        path.write_text(
            "\n".join(
                line
                for line in path.read_text(encoding="utf-8").splitlines()
                if not line.startswith("Accepted Asset Requirements SHA256:")
            )
            + "\n",
            encoding="utf-8",
        )
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("Accepted Asset Requirements SHA256", validated.stdout)

    def test_handoff_rejects_unsafe_project_path(self) -> None:
        project = self.make_project()
        path = project / "state" / "handoff-state.yaml"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "content: work/content.md",
                "content: ../outside.md",
            ),
            encoding="utf-8",
        )
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("non-canonical path segment", validated.stdout)

    def test_handoff_rejects_unknown_state_field(self) -> None:
        project = self.make_project()
        path = project / "state" / "handoff-state.yaml"
        path.write_text(
            path.read_text(encoding="utf-8") + "next_step: flow_5\n",
            encoding="utf-8",
        )
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 1, validated.stderr or validated.stdout)
        self.assertIn("unsupported field", validated.stdout)

    def test_visual_not_proven_is_valid_without_claiming_pass(self) -> None:
        project = self.make_project()
        validated = self.validate(project)
        self.assertEqual(validated.returncode, 0, validated.stderr or validated.stdout)
        self.assertIn(
            "Visual sanity: NOT PROVEN",
            (project / "work" / "acceptance.md").read_text(encoding="utf-8"),
        )


if __name__ == "__main__":
    unittest.main()
