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
NUMBER_RE = re.compile(r"(?<![\w.-])-?\d+(?:\.\d+)?")
STABLE_ID_RE = re.compile(r"\b[A-Z]{2,}(?:-[A-Z0-9]+)+\b")
PERCENT_RE = re.compile(r"(?<![\w.])-?\d+(?:\.\d+)?\s*%")
DIMENSION_RE = re.compile(
    r"(?<![\w.])(-?\d+(?:\.\d+)?)\s*[x×]\s*(-?\d+(?:\.\d+)?)(?:\s*[x×]\s*(-?\d+(?:\.\d+)?))?",
    re.I,
)
COORDINATE_RE = re.compile(
    r"(?<![\w.])(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)(?![\w.])"
)
UNIT_RE = re.compile(
    r"(?<![\w.])(-?\d+(?:\.\d+)?)\s*"
    r"(milliseconds?|millisecond|milidetik|ms|seconds?|second|secs?|sec|detik|s|"
    r"minutes?|minute|mins?|min|menit|hours?|hour|hrs?|hr|jam|h|"
    r"millimeters?|millimetres?|milimeter|mm|centimeters?|centimetres?|sentimeter|cm|"
    r"kilometers?|kilometres?|kilometer|km|meters?|metres?|meter|m|blocks?|blok)\b",
    re.I,
)
EN_NEGATION_RE = re.compile(r"\b(?:must\s+not|do\s+not|does\s+not|cannot|can't|never|without|not)\b", re.I)
ID_NEGATION_RE = re.compile(r"\b(?:tidak\s+boleh|tidak|tanpa|bukan|jangan|dilarang)\b", re.I)

UNIT_ALIASES = {
    "millisecond": "ms",
    "milliseconds": "ms",
    "milidetik": "ms",
    "ms": "ms",
    "second": "s",
    "seconds": "s",
    "sec": "s",
    "secs": "s",
    "detik": "s",
    "s": "s",
    "minute": "min",
    "minutes": "min",
    "min": "min",
    "mins": "min",
    "menit": "min",
    "hour": "h",
    "hours": "h",
    "hr": "h",
    "hrs": "h",
    "jam": "h",
    "h": "h",
    "millimeter": "mm",
    "millimeters": "mm",
    "millimetre": "mm",
    "millimetres": "mm",
    "milimeter": "mm",
    "mm": "mm",
    "centimeter": "cm",
    "centimeters": "cm",
    "centimetre": "cm",
    "centimetres": "cm",
    "sentimeter": "cm",
    "cm": "cm",
    "kilometer": "km",
    "kilometers": "km",
    "kilometre": "km",
    "kilometres": "km",
    "km": "km",
    "meter": "m",
    "meters": "m",
    "metre": "m",
    "metres": "m",
    "m": "m",
    "block": "block",
    "blocks": "block",
    "blok": "block",
}


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
                    f"{path} changes numeric/unit/dimension/coordinate/stable-ID invariants between en and id"
                )
            if len(EN_NEGATION_RE.findall(en)) != len(ID_NEGATION_RE.findall(ind)):
                raise ValueError(f"{path} changes material negation count between en and id")
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
    tokens: list[str] = []
    tokens.extend(f"id:{match.group(0)}" for match in STABLE_ID_RE.finditer(text))
    tokens.extend(f"num:{match.group(0)}" for match in NUMBER_RE.finditer(text))
    tokens.extend(f"pct:{match.group(0).replace(' ', '')}" for match in PERCENT_RE.finditer(text))
    for match in UNIT_RE.finditer(text):
        value, raw_unit = match.groups()
        unit = UNIT_ALIASES[raw_unit.casefold()]
        tokens.append(f"unit:{value}:{unit}")
    for match in DIMENSION_RE.finditer(text):
        values = [part for part in match.groups() if part is not None]
        tokens.append("dim:" + "x".join(values))
    for match in COORDINATE_RE.finditer(text):
        tokens.append("coord:" + ",".join(match.groups()))
    return tuple(sorted(tokens))
