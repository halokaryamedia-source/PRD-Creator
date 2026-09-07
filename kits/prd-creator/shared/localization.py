from __future__ import annotations

import re
from typing import Any

BILINGUAL_SCALAR_FIELDS = {
    "approved_requirement_sha256",
    "canonical_content_sha256",
    "id",
    "key",
    "code",
    "version",
    "brand_mark",
    "languages",
    "roles",
    "weight",
    "step",
    "formula",
    "mode",
}
INVARIANT_TOKEN_RE = re.compile(r"(?<![\w])\d+(?:\.\d+)?%?|\b[A-Z]{2,}(?:-[A-Z0-9]+)+\b")


def document_languages(data: dict[str, Any]) -> list[str]:
    raw = data["document"].get("languages", ["en"])
    if raw not in (["en"], ["en", "id"]):
        raise ValueError('document.languages must be ["en"] or ["en", "id"]')
    return list(raw)


def validate_bilingual_values(value: Any, path: str = "render_data", field: str | None = None) -> None:
    if isinstance(value, dict):
        keys = set(value)
        if keys and keys.issubset({"en", "id"}):
            for language in ("en", "id"):
                current = value.get(language)
                if current in (None, "", []):
                    raise ValueError(f"{path}.{language} is required for bilingual document")
            en = str(value["en"])
            ind = str(value["id"])
            if _invariant_tokens(en) != _invariant_tokens(ind):
                raise ValueError(
                    f"{path} changes numeric/percentage/stable-ID tokens between en and id"
                )
            return
        for key, child in value.items():
            validate_bilingual_values(child, f"{path}.{key}", key)
        return
    if isinstance(value, list):
        for index, child in enumerate(value):
            validate_bilingual_values(child, f"{path}[{index}]", field)
        return
    if isinstance(value, str) and value and field not in BILINGUAL_SCALAR_FIELDS:
        raise ValueError(f"{path} must use an explicit en/id localized value for bilingual document")


def _invariant_tokens(text: str) -> tuple[str, ...]:
    return tuple(INVARIANT_TOKEN_RE.findall(text))
