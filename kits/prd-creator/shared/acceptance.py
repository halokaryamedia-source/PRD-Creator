from __future__ import annotations

import re
from collections.abc import Mapping

from .issues import Issue

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def field_values(text: str, label: str) -> list[str]:
    """Return exact line-oriented acceptance values for one label."""

    pattern = re.compile(rf"(?mi)^\s*{re.escape(label)}:\s*(.*?)\s*$")
    return [value.strip() for value in pattern.findall(text)]


def required_value_issues(
    text: str,
    required: Mapping[str, set[str]],
    *,
    owner: str,
    path: str,
    code_prefix: str,
) -> list[Issue]:
    issues: list[Issue] = []
    for label, allowed in required.items():
        values = field_values(text, label)
        code_label = re.sub(r"[^A-Z0-9]+", "_", label.upper()).strip("_")
        if len(values) != 1 or not values[0]:
            issues.append(
                Issue(
                    f"{code_prefix}_{code_label}_MISSING",
                    owner,
                    f"{label} must appear exactly once with a non-empty value",
                    path=path,
                    field=label,
                )
            )
            continue
        if values[0] not in allowed:
            issues.append(
                Issue(
                    f"{code_prefix}_{code_label}_INVALID",
                    owner,
                    f"{label}={values[0]!r}, expected one of {sorted(allowed)}",
                    path=path,
                    field=label,
                )
            )
    return issues


def sha_binding_issues(
    text: str,
    label: str,
    expected: str,
    *,
    owner: str,
    path: str,
    code: str,
    allow_none: bool = False,
) -> list[Issue]:
    values = field_values(text, label)
    if len(values) != 1:
        return [
            Issue(
                f"{code}_MISSING",
                owner,
                f"{label} must appear exactly once",
                path=path,
                field=label,
            )
        ]

    value = values[0]
    if value == "none" and allow_none:
        valid_shape = True
    else:
        valid_shape = SHA256_RE.fullmatch(value) is not None
    if not valid_shape:
        expected_shape = "'none' or a lowercase SHA-256 digest" if allow_none else "a lowercase SHA-256 digest"
        return [
            Issue(
                f"{code}_INVALID",
                owner,
                f"{label} must be {expected_shape}",
                path=path,
                field=label,
            )
        ]
    if value != expected:
        return [
            Issue(
                f"{code}_STALE",
                owner,
                f"{label}={value!r}, expected current binding {expected!r}",
                path=path,
                field=label,
            )
        ]
    return []
