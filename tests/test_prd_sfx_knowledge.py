"""Offline SFX documentation contracts; not a billing guard or acoustic test."""

from __future__ import annotations

import json
import math
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KIT_ROOT = ROOT / "kits" / "prd-creator"
if str(KIT_ROOT) not in sys.path:
    sys.path.insert(0, str(KIT_ROOT))

from shared.sfx import validate_request  # noqa: E402

ASSETS = KIT_ROOT / "production-assets"
COORDINATOR = ASSETS / "SOUND-EFFECTS.md"
REFERENCES = ASSETS / "sfx" / "references"
REFERENCE_NAMES = {
    "elevenlabs-contracts-and-sources.md",
    "prompting-archetypes.md",
    "families-and-variation.md",
    "timing-loops-and-layering.md",
    "execution-and-cost-control.md",
    "validation-and-delivery.md",
    "minecraft-bedrock-delivery.md",
}
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
JSON_RE = re.compile(r"```json\n(.*?)\n```", re.DOTALL)


def read_reference(name: str) -> str:
    return (REFERENCES / name).read_text(encoding="utf-8")


class SfxKnowledgeContracts(unittest.TestCase):
    def test_coordinator_is_bounded_and_routes_each_reference(self) -> None:
        text = COORDINATOR.read_text(encoding="utf-8")
        self.assertLessEqual(len(text.split()), 950, "Keep detail in selectively loaded references")
        targets = {Path(link).name for link in LINK_RE.findall(text) if link.startswith("sfx/references/")}
        self.assertEqual(targets, REFERENCE_NAMES)
        self.assertIn("do not load the entire reference collection", text)
        self.assertIn("Explicit Minecraft Bedrock target only", text)

    def test_reference_inventory_and_context_bounds(self) -> None:
        self.assertEqual({path.name for path in REFERENCES.glob("*.md")}, REFERENCE_NAMES)
        for path in REFERENCES.glob("*.md"):
            with self.subTest(path=path.name):
                self.assertLessEqual(len(path.read_text(encoding="utf-8").split()), 1600)

    def test_relative_links_resolve_inside_repository(self) -> None:
        for path in [COORDINATOR, *sorted(REFERENCES.glob("*.md"))]:
            for link in LINK_RE.findall(path.read_text(encoding="utf-8")):
                if "://" in link or link.startswith("#"):
                    continue
                with self.subTest(path=path.name, link=link):
                    target = (path.parent / link.split("#", 1)[0]).resolve()
                    self.assertTrue(target.is_relative_to(ROOT.resolve()))
                    self.assertTrue(target.is_file(), f"Broken local reference: {link}")

    def test_markdown_fences_are_balanced(self) -> None:
        for path in [COORDINATOR, *sorted(REFERENCES.glob("*.md"))]:
            with self.subTest(path=path.name):
                fences = re.findall(r"(?m)^```[^\n]*$", path.read_text(encoding="utf-8"))
                self.assertEqual(len(fences) % 2, 0)

    def test_unheard_examples_are_valid_portable_request_bodies(self) -> None:
        text = read_reference("prompting-archetypes.md")
        self.assertIn("UNTESTED examples", text)
        self.assertIn("output_format` is a separate query choice", text)
        examples = JSON_RE.findall(text)
        self.assertEqual(len(examples), 6)
        allowed = {"text", "model_id", "duration_seconds", "loop", "prompt_influence"}
        for index, raw in enumerate(examples):
            with self.subTest(example=index):
                request = json.loads(raw)
                self.assertEqual(validate_request(request), [])
                self.assertEqual(set(request), allowed)
                self.assertIsInstance(request["text"], str)
                self.assertTrue(request["text"].strip())
                self.assertLessEqual(len(request["text"]), 450)
                self.assertEqual(request["model_id"], "eleven_text_to_sound_v2")
                self.assertIs(type(request["loop"]), bool)
                duration = request["duration_seconds"]
                self.assertIn(type(duration), (int, float))
                self.assertTrue(math.isfinite(duration))
                self.assertGreaterEqual(duration, 0.5)
                self.assertLessEqual(duration, 30)
                influence = request["prompt_influence"]
                self.assertIn(type(influence), (int, float))
                self.assertTrue(math.isfinite(influence))
                self.assertGreaterEqual(influence, 0)
                self.assertLessEqual(influence, 1)

    def test_independent_production_dimensions_remain_explicit(self) -> None:
        text = COORDINATOR.read_text(encoding="utf-8")
        for term in ("Temporal form", "Relationship", "Composition", "not as mutually exclusive modes"):
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_authorization_retry_and_resume_policy_is_present(self) -> None:
        text = read_reference("execution-and-cost-control.md")
        clauses = (
            "zero paid requests",
            "explicit generation authorization",
            "maximum provider requests",
            "Disable automatic generation retries",
            "do not execute through that adapter",
            "Another chat/session resumes from prior evidence",
            "Do not automatically resend",
            "not a guaranteed dollar cap",
            "never auto-top-up or upgrade",
            "Parent and delegated agents share the same remaining budget",
        )
        for clause in clauses:
            with self.subTest(clause=clause):
                self.assertIn(clause, text)

    def test_request_accounting_examples_do_not_overspend(self) -> None:
        text = read_reference("execution-and-cost-control.md")
        rows = re.findall(
            r"(?m)^\| ([^|]+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (ALLOW|STOP) \|$",
            text,
        )
        self.assertEqual(len(rows), 4)
        for case, cap, attempted, reserved, following, decision in rows:
            with self.subTest(case=case):
                total = int(attempted) + int(reserved) + int(following)
                self.assertEqual(decision, "ALLOW" if total <= int(cap) else "STOP")
        self.assertIn("not generation authorization", text)
        self.assertIn("count each attempt once", text)
        self.assertIn("every other gate must still pass", text)

    def test_proof_levels_are_not_audio_or_billing_claims(self) -> None:
        main = COORDINATOR.read_text(encoding="utf-8")
        delivery = read_reference("validation-and-delivery.md")
        self.assertIn("not an executable billing firewall", main)
        self.assertIn("Accepted candidate = stop", main)
        self.assertIn("No benchmark generation runs in CI", delivery)
        for evidence in ("Prepared", "Generated, unreviewed", "Audio accepted", "Target verified"):
            self.assertIn(evidence, delivery)
        self.assertIn("not a new persisted status schema", delivery)

    def test_sources_distinguish_facts_policy_and_calibration(self) -> None:
        text = read_reference("elevenlabs-contracts-and-sources.md")
        for term in ("2026-09-09", "Official fact", "Repository policy", "Calibration"):
            self.assertIn(term, text)
        self.assertIn("0.1-second minimum", text)
        self.assertIn("0.5-second minimum", text)
        self.assertIn("No fixed numeric rate is stored", text)
        for control in ("seed", "voice_id", "negative_prompt"):
            self.assertIn(f"`{control}`", text)

    def test_repository_ci_runs_offline_contracts_on_documentation_changes(self) -> None:
        text = (ROOT / ".github" / "workflows" / "repository-verify.yml").read_text(encoding="utf-8")
        self.assertIn('python -m unittest discover -s tests -p "test_prd_sfx_knowledge.py" -v', text)
        self.assertNotIn("paths:", text, "Documentation-only edits must keep running the SFX checks")
        self.assertNotIn("ELEVENLABS_API_KEY", text)


if __name__ == "__main__":
    unittest.main()
