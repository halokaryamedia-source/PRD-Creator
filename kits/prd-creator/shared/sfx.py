"""Read-only ElevenLabs SFX request preflight; no network, authorization or reservation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .issues import Issue

# Reviewed API contract: 2026-09-09. See the SFX contracts-and-sources reference.
MODEL = "eleven_text_to_sound_v2"
MAX_DURATION = 30.0
REQUEST_FIELDS = frozenset({"text", "model_id", "duration_seconds", "loop", "prompt_influence"})
# Local parser/diagnostic bounds, NOT ElevenLabs API limits.
MAX_INPUT_BYTES = 64 * 1024
MAX_COUNTER = 2**31 - 1


def _issue(code: str, message: str, field: str = "") -> Issue:
    return Issue(code, "production_assets.sfx_preflight", message, field=field)


def _number(value: Any, low: float, high: float) -> bool:
    # bool is an int subclass; strict types also reject strings, NaN and infinities.
    return type(value) in (int, float) and low <= value <= high


def _counter(value: Any) -> bool:
    return type(value) is int and 0 <= value <= MAX_COUNTER


def _object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            # Do not echo input values or arbitrary field names (possibly secrets).
            raise ValueError("Duplicate JSON member; remove the ambiguity before review.")
        result[key] = value
    return result


def _constant(_: str) -> None:
    raise ValueError("Non-finite JSON constant is not allowed.")


def read_request(path: Path) -> tuple[Any, str]:
    """Read bounded UTF-8 JSON without rewriting, trimming or normalizing the payload."""
    if not path.is_file():
        raise ValueError("Request must be an existing regular UTF-8 JSON file.")
    with path.open("rb") as stream:
        raw = stream.read(MAX_INPUT_BYTES + 1)
    if len(raw) > MAX_INPUT_BYTES:
        raise ValueError("Request exceeds the local 64 KiB preflight input bound.")
    try:
        text = raw.decode("utf-8")
        body = json.loads(text, object_pairs_hook=_object, parse_constant=_constant)
    except (UnicodeDecodeError, json.JSONDecodeError, RecursionError) as exc:
        raise ValueError("Request must be valid, bounded UTF-8 JSON without a BOM.") from exc
    return body, hashlib.sha256(raw).hexdigest()


def validate_request(body: Any) -> list[Issue]:
    """Validate the reviewed SFX-v2 body, not speech, API entitlement or audio quality."""
    issues: list[Issue] = []
    if not isinstance(body, dict):
        return [_issue("SFX_REQUEST_OBJECT", "The request body must be one JSON object.")]
    if set(body) - REQUEST_FIELDS:
        issues.append(
            _issue(
                "SFX_REQUEST_FIELDS",
                "Unsupported body fields. output_format belongs in the query; "
                "TTS/seed/reference controls are not SFX-v2 fields.",
            )
        )
    text = body.get("text")
    if not isinstance(text, str) or not text.strip():
        issues.append(_issue("SFX_TEXT", "A nonempty text description is required.", "text"))
    else:
        try:
            text.encode("utf-8")
        except UnicodeEncodeError:
            issues.append(_issue("SFX_TEXT", "Text must contain valid Unicode characters.", "text"))
    if body.get("model_id", MODEL) != MODEL:
        issues.append(_issue("SFX_MODEL", "This preflight supports only the reviewed SFX-v2 model.", "model_id"))
    if type(body.get("loop", False)) is not bool:
        issues.append(_issue("SFX_LOOP", "loop must be a JSON boolean, not a string or number.", "loop"))
    duration = body.get("duration_seconds")
    if duration is not None and not _number(duration, 0.5, MAX_DURATION):
        issues.append(
            _issue("SFX_DURATION", "duration_seconds must be null or a number from 0.5 to 30.", "duration_seconds")
        )
    influence = body.get("prompt_influence", 0.3)
    if influence is not None and not _number(influence, 0.0, 1.0):
        issues.append(
            _issue("SFX_INFLUENCE", "prompt_influence must be null or a number from 0 to 1.", "prompt_influence")
        )
    return issues


def check_budget(
    *,
    request_limit: Any,
    requests_used: Any,
    unresolved_requests: Any,
    max_duration_seconds: Any,
    duration_seconds: Any,
) -> tuple[list[Issue], dict[str, Any]]:
    """Check ONE next API attempt against an operator-supplied snapshot, without reserving it.

    Used includes every dispatched attempt, including unresolved ones. Unresolved is
    a subset of used, not an additional debit. It blocks further work until reconciled.
    """
    issues: list[Issue] = []
    for field, value in (
        ("request_limit", request_limit),
        ("requests_used", requests_used),
        ("unresolved_requests", unresolved_requests),
    ):
        if not _counter(value):
            issues.append(_issue("SFX_BUDGET_VALUE", "An explicit nonnegative 32-bit integer is required.", field))
    if not _number(max_duration_seconds, 0.5, MAX_DURATION):
        issues.append(
            _issue(
                "SFX_BUDGET_DURATION",
                "The explicit per-attempt duration cap must be from 0.5 to 30.",
                "max_duration_seconds",
            )
        )
    if duration_seconds is not None and not _number(duration_seconds, 0.5, MAX_DURATION):
        issues.append(_issue("SFX_DURATION", "Cannot evaluate an invalid requested duration.", "duration_seconds"))
    if issues:
        return issues, {"status": "fail"}

    worst_seconds = MAX_DURATION if duration_seconds is None else float(duration_seconds)
    remaining = max(0, request_limit - requests_used)
    if unresolved_requests > requests_used:
        issues.append(_issue("SFX_BUDGET_ACCOUNTING", "Unresolved requests must already be included in requests_used."))
    if unresolved_requests:
        issues.append(
            _issue("SFX_UNRESOLVED_REQUEST", "Reconcile earlier request outcomes/charges; do not resend blindly.")
        )
    if requests_used >= request_limit:
        issues.append(_issue("SFX_REQUEST_LIMIT", "No request slot remains in the supplied batch snapshot."))
    if worst_seconds > max_duration_seconds:
        issues.append(
            _issue("SFX_DURATION_LIMIT", "Requested or worst-case auto duration exceeds the supplied per-attempt cap.")
        )
    return issues, {
        "status": "fail" if issues else "pass",
        "unit": "API attempts (not website Generate clicks or candidate files)",
        "request_limit": request_limit,
        "requests_used": requests_used,
        "unresolved_requests": unresolved_requests,
        "remaining_request_slots": remaining,
        "max_duration_seconds": max_duration_seconds,
        "next_request_worst_case_seconds": worst_seconds,
        "monetary_limit_verified": False,
        "reservation_created": False,
    }


def preflight(
    request: Path,
    *,
    request_limit: int,
    requests_used: int,
    unresolved_requests: int,
    max_duration_seconds: float,
) -> dict[str, Any]:
    """Report mechanical blockers only. Even a PASS grants no paid execution permission."""
    issues: list[Issue] = []
    summary: dict[str, Any] = {}
    budget: dict[str, Any] = {"status": "not_checked"}
    digest: str | None = None
    try:
        body, digest = read_request(request)
        issues.extend(validate_request(body))
        if not issues:
            summary = {
                "text_characters": len(body["text"]),
                "model_id": body.get("model_id", MODEL),
                "duration_seconds": body.get("duration_seconds"),
                "loop": body.get("loop", False),
                "prompt_influence": body.get("prompt_influence", 0.3),
            }
            budget_issues, budget = check_budget(
                request_limit=request_limit,
                requests_used=requests_used,
                unresolved_requests=unresolved_requests,
                max_duration_seconds=max_duration_seconds,
                duration_seconds=body.get("duration_seconds"),
            )
            issues.extend(budget_issues)
    except (OSError, ValueError) as exc:
        # No path, prompt or provider credential is echoed in error diagnostics.
        message = str(exc) if isinstance(exc, ValueError) else "The request file could not be read."
        issues.append(_issue("SFX_REQUEST_READ", message))

    return {
        "status": "fail" if issues else "pass",
        "mode": "offline_preflight",
        "surface": "api",
        "request_sha256": digest,
        "summary": summary,
        "budget_snapshot": budget,
        "issues": [issue.as_dict() for issue in issues],
        "paid_requests_made": 0,
        "generation_authorized": False,
        "audio_verified": False,
        "not_checked": [
            "AST meaning and acceptance; reusable assets and existing candidates",
            "user generation consent, actual ledger freshness and concurrent reservations",
            "live executor support, hidden retries, account rights and format entitlement",
            "prices, monetary ceiling, actual charges and heard audio quality",
        ],
        "next_action": (
            "Stop; correct the listed blockers without generation."
            if issues
            else "Offline checks pass only. Complete unchecked production gates and reserve in the "
            "shared execution record before any authorized paid request."
        ),
    }
