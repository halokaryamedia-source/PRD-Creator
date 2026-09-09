"""Executable dry-run checks, never paid audio tests or a provider-side billing guard."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
KIT_ROOT = ROOT / "kits" / "prd-creator"
if str(KIT_ROOT) not in sys.path:
    sys.path.insert(0, str(KIT_ROOT))

from shared.sfx import MAX_INPUT_BYTES, MODEL, check_budget, preflight, read_request, validate_request  # noqa: E402


def codes(issues: list) -> set[str]:
    return {issue.code for issue in issues}


class SfxRequestValidation(unittest.TestCase):
    def test_minimal_explicit_and_nullable_requests(self) -> None:
        for body in (
            {"text": "One dry wooden knock."},
            {"text": "Motor hum.", "model_id": MODEL, "duration_seconds": 0.5, "loop": True, "prompt_influence": 0},
            {"text": "Motor hum.", "duration_seconds": 30, "prompt_influence": 1},
            {"text": "Motor hum.", "duration_seconds": None, "prompt_influence": None},
        ):
            with self.subTest(body=body):
                self.assertEqual(validate_request(body), [])

    def test_empty_or_non_object_request(self) -> None:
        for body in (None, [], "text", 0, True):
            with self.subTest(body=body):
                self.assertEqual(codes(validate_request(body)), {"SFX_REQUEST_OBJECT"})
        for text in (None, "", " \n ", 1, True, [], "\ud800"):
            with self.subTest(text=repr(text)):
                self.assertIn("SFX_TEXT", codes(validate_request({"text": text})))

    def test_unsupported_fields_are_not_silently_dropped(self) -> None:
        for field in ("seed", "voice_id", "negative_prompt", "reference_audio", "output_format", "n", "api_key"):
            with self.subTest(field=field):
                self.assertIn("SFX_REQUEST_FIELDS", codes(validate_request({"text": "Knock.", field: "secret"})))

    def test_strict_types_and_finite_bounds(self) -> None:
        cases = {
            "duration_seconds": (True, False, "2", -1, 0.1, 30.01, float("nan"), float("inf"), 10**400),
            "prompt_influence": (True, "0.3", -0.01, 1.01, float("nan"), float("-inf"), []),
            "loop": (None, 0, 1, "false", []),
            "model_id": (None, "eleven_v3", "eleven_text_to_sound_v1", 1),
        }
        for field, values in cases.items():
            for value in values:
                with self.subTest(field=field, value=value):
                    self.assertTrue(validate_request({"text": "Knock.", field: value}))

    def test_website_limit_does_not_become_api_limit(self) -> None:
        self.assertEqual(validate_request({"text": "x" * 451}), [])

    def test_validation_does_not_mutate_request(self) -> None:
        body = {"text": "  A dry knock.  ", "prompt_influence": None}
        before = dict(body)
        validate_request(body)
        self.assertEqual(body, before)


class SfxBudgetSnapshot(unittest.TestCase):
    def check(self, **overrides):
        values = {
            "request_limit": 3,
            "requests_used": 0,
            "unresolved_requests": 0,
            "max_duration_seconds": 2,
            "duration_seconds": 1,
        }
        values.update(overrides)
        return check_budget(**values)

    def test_next_attempt_boundary_and_no_reservation(self) -> None:
        for used in (0, 1, 2):
            issues, result = self.check(requests_used=used)
            self.assertEqual(issues, [])
            self.assertEqual(result["remaining_request_slots"], 3 - used)
            self.assertFalse(result["reservation_created"])
            self.assertFalse(result["monetary_limit_verified"])
        for used in (3, 4):
            self.assertIn("SFX_REQUEST_LIMIT", codes(self.check(requests_used=used)[0]))
        self.assertIn("SFX_REQUEST_LIMIT", codes(self.check(request_limit=0)[0]))

    def test_unresolved_blocks_even_when_allowance_remains(self) -> None:
        issues, result = self.check(requests_used=1, unresolved_requests=1)
        self.assertIn("SFX_UNRESOLVED_REQUEST", codes(issues))
        self.assertEqual(result["remaining_request_slots"], 2, "Unresolved is already debited in used")
        self.assertIn("SFX_BUDGET_ACCOUNTING", codes(self.check(unresolved_requests=1)[0]))

    def test_auto_reserves_no_less_than_documented_worst_case(self) -> None:
        self.assertIn("SFX_DURATION_LIMIT", codes(self.check(duration_seconds=None)[0]))
        issues, result = self.check(duration_seconds=None, max_duration_seconds=30)
        self.assertEqual(issues, [])
        self.assertEqual(result["next_request_worst_case_seconds"], 30)
        self.assertFalse(result["reservation_created"], "This is only a preview of exposure")

    def test_duration_cap_is_inclusive(self) -> None:
        self.assertEqual(self.check(duration_seconds=2)[0], [])
        self.assertIn("SFX_DURATION_LIMIT", codes(self.check(duration_seconds=2.01)[0]))

    def test_missing_invalid_and_boolean_budget_values(self) -> None:
        for field in ("request_limit", "requests_used", "unresolved_requests"):
            for value in (None, True, -1, 0.5, "1", float("nan"), 2**31):
                with self.subTest(field=field, value=value):
                    self.assertIn("SFX_BUDGET_VALUE", codes(self.check(**{field: value})[0]))
        for value in (None, True, 0.1, 31, "2", float("inf")):
            self.assertIn("SFX_BUDGET_DURATION", codes(self.check(max_duration_seconds=value)[0]))
        self.assertIn("SFX_DURATION", codes(self.check(duration_seconds=True)[0]))

    def test_resumed_snapshot_does_not_reset_used_count(self) -> None:
        self.assertEqual(self.check(requests_used=2)[1]["remaining_request_slots"], 1)
        issues, result = self.check(requests_used=3)
        self.assertIn("SFX_REQUEST_LIMIT", codes(issues))
        self.assertEqual(result["remaining_request_slots"], 0)


class SfxReadOnlyPreflight(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "request.json"
        self.raw = b'{"text":"One dry knock.","duration_seconds":1}'
        self.path.write_bytes(self.raw)

    def run_check(self, **overrides):
        values = dict(request_limit=3, requests_used=0, unresolved_requests=0, max_duration_seconds=2)
        values.update(overrides)
        return preflight(self.path, **values)

    def test_success_is_offline_and_preserves_bytes(self) -> None:
        before = set(self.path.parent.iterdir())
        with patch("socket.socket", side_effect=AssertionError("No network allowed")):
            result = self.run_check()
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["mode"], "offline_preflight")
        self.assertEqual(result["paid_requests_made"], 0)
        self.assertFalse(result["generation_authorized"])
        self.assertFalse(result["audio_verified"])
        self.assertEqual(result["request_sha256"], hashlib.sha256(self.raw).hexdigest())
        self.assertEqual(self.path.read_bytes(), self.raw)
        self.assertEqual(set(self.path.parent.iterdir()), before)
        self.assertNotIn("One dry knock", json.dumps(result), "Do not echo full prompts by default")

    def test_duplicates_invalid_encoding_nonfinite_and_malformed_json(self) -> None:
        for raw in (
            b'{"text":"knock","duration_seconds":1,"duration_seconds":30}',
            b'{"text":"knock","loop":false,"loop":true}',
            b'{"text":"knock","prompt_influence":NaN}',
            b'{"text":"knock","duration_seconds":Infinity}',
            b"\xff",
            b'\xef\xbb\xbf{"text":"knock"}',
            b"{",
            b"[" * 1100,
        ):
            with self.subTest(raw=raw[:60]):
                self.path.write_bytes(raw)
                self.assertEqual(self.run_check()["issues"][0]["code"], "SFX_REQUEST_READ")

    def test_unreadable_nonfile_and_oversized_inputs(self) -> None:
        self.path.unlink()
        self.assertEqual(self.run_check()["status"], "fail")
        self.path.mkdir()
        self.assertEqual(self.run_check()["status"], "fail")
        self.path.rmdir()
        self.path.write_bytes(b" " * (MAX_INPUT_BYTES + 1))
        self.assertEqual(self.run_check()["status"], "fail")
        with patch("pathlib.Path.open", side_effect=OSError("secret-location")):
            self.assertNotIn("secret-location", json.dumps(self.run_check()))

    def test_invalid_request_does_not_claim_budget_pass(self) -> None:
        self.path.write_text('{"text":"knock","api_key":"PRIVATE-KEY"}', encoding="utf-8")
        result = self.run_check()
        self.assertEqual(result["budget_snapshot"]["status"], "not_checked")
        self.assertNotIn("PRIVATE-KEY", json.dumps(result))

    def test_read_returns_original_nullable_fields(self) -> None:
        self.path.write_text('{"text":"  knock  ","duration_seconds":null}', encoding="utf-8")
        body, _ = read_request(self.path)
        self.assertEqual(body, {"text": "  knock  ", "duration_seconds": None})


class SfxOperatorIntegration(unittest.TestCase):
    def test_cli_requires_explicit_counters_and_returns_json_without_writes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            request = Path(temp) / "request.json"
            raw = b'{"text":"Knock.","duration_seconds":1}'
            request.write_bytes(raw)
            base = [sys.executable, str(ROOT / "tools" / "prd.py"), "sfx-check", str(request)]
            missing = subprocess.run(base, capture_output=True, text=True, check=False)
            self.assertEqual(missing.returncode, 2)
            limits = ["--request-limit", "3", "--unresolved-requests", "0", "--max-duration-seconds", "2"]
            for used, expected_exit in ((0, 0), (3, 1)):
                process = subprocess.run(
                    [*base, *limits, "--requests-used", str(used)], capture_output=True, text=True, check=False
                )
                with self.subTest(used=used):
                    self.assertEqual(process.returncode, expected_exit, process.stderr)
                    payload = json.loads(process.stdout)
                    self.assertEqual(payload["paid_requests_made"], 0)
                    self.assertFalse(payload["generation_authorized"])
            self.assertEqual(request.read_bytes(), raw)
            self.assertEqual(list(Path(temp).iterdir()), [request])


if __name__ == "__main__":
    unittest.main()
