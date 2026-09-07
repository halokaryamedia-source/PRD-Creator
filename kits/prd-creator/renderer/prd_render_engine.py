#!/usr/bin/env python3
"""Render derived PRD JSON into the generic production-document template."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from core import esc, i18n, slug, txt  # noqa: E402
from pages import flow_pages, global_pages, glossary, navigation, overview, package_pages  # noqa: E402

ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
OPEN_RE = re.compile(r"\b(?:TBD|TODO|FIXME|INSERT\s+(?:TEXT|VALUE)|USE\s+APPROVED\s+AMOUNT)\b|\[OPEN\]", re.I)
SIDEBAR_BRAND_RE = re.compile(r'<a\s+aria-label="[^"]* overview"\s+class="sidebar-brand"\s+href="#summary">.*?</a>', re.S)
TITLE_RE = re.compile(r"<title>.*?</title>", re.S | re.I)
DESCRIPTION_META_RE = re.compile(r'<meta\s+content="[^"]*"\s+name="description"\s*/?>', re.I)
SPEC_VERSION_META_RE = re.compile(r'<meta\s+content="[^"]*"\s+name="specification-version"\s*/?>', re.I)
GLOSSARY_ASSIGN_RE = re.compile(r"const glossary = .*?;\n\s*const tooltip =", re.S)
HTML_TAG_RE = re.compile(r"<html\b[^>]*>", re.I)
STORAGE_PREFIX_TOKEN = "__PRD_STORAGE_PREFIX__"
TERM_ROLES = {"gameplay", "level_design", "developer"}
MANDATORY_GLOBAL_SECTIONS = (
    ("development-overview", "Development Overview"),
    ("game-system", "Game System"),
    ("data-reset", "Data and Reset"),
    ("gameplay-development", "Gameplay Development"),
)
REQUIRED_OVERVIEW_FACT_KEYS = {"session-model", "target-playtime", "game-structure"}
BILINGUAL_SCALAR_FIELDS = {
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
    "no",
    "number",
    "formula",
}


def script_safe_json(value: Any) -> str:
    text = json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
    return (
        text.replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def document_languages(data: dict[str, Any]) -> list[str]:
    raw = data["document"].get("languages", ["en"])
    if raw not in (["en"], ["en", "id"]):
        raise ValueError('document.languages must be ["en"] or ["en", "id"]')
    return list(raw)


def validate_bilingual_values(value: Any, path: str, field: str | None = None) -> None:
    if isinstance(value, dict):
        keys = set(value)
        if keys and keys.issubset({"en", "id"}):
            for language in ("en", "id"):
                current = value.get(language)
                if current in (None, "", []):
                    raise ValueError(f"{path}.{language} is required for bilingual document")
            return
        for key, child in value.items():
            validate_bilingual_values(child, f"{path}.{key}", key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            validate_bilingual_values(child, f"{path}[{index}]", field)
    elif isinstance(value, str) and value and field not in BILINGUAL_SCALAR_FIELDS:
        raise ValueError(f"{path} must use an explicit en/id localized value for bilingual document")


def validate_aliases(aliases: Any, context: str) -> None:
    if aliases is None:
        return
    if isinstance(aliases, list):
        if not all(isinstance(alias, str) for alias in aliases):
            raise ValueError(f"{context}.aliases must be an array of strings")
        return
    if isinstance(aliases, dict):
        supported = [language for language in ("en", "id") if language in aliases]
        if not supported:
            raise ValueError(f"{context}.aliases object must define en and/or id")
        for language in supported:
            values = aliases[language]
            if not isinstance(values, list) or not all(isinstance(alias, str) for alias in values):
                raise ValueError(f"{context}.aliases.{language} must be an array of strings")
        return
    raise ValueError(f"{context}.aliases must be an array of strings or an en/id object")


def validate_term_roles(roles: Any, context: str) -> None:
    if roles is None:
        return
    if not isinstance(roles, list) or not all(isinstance(role, str) for role in roles):
        raise ValueError(f"{context}.roles must be an array")
    if len(roles) != len(set(roles)):
        raise ValueError(f"{context}.roles must not contain duplicates")
    invalid = sorted(set(roles) - TERM_ROLES)
    if invalid:
        raise ValueError(f"{context}.roles contains unsupported role: {invalid[0]}")


def _has_text(value: Any) -> bool:
    return bool(txt(value)["en"].strip())


def _require_text(container: dict[str, Any], field: str, context: str) -> None:
    if not _has_text(container.get(field)):
        raise ValueError(f"{context}.{field} is required by the Golden mandatory contract")


def _require_nonempty_list(container: dict[str, Any], field: str, context: str) -> list[Any]:
    value = container.get(field)
    if not isinstance(value, list) or not value:
        raise ValueError(f"{context}.{field} must be a non-empty array under the Golden mandatory contract")
    return value


def _validate_text_items(items: list[Any], context: str) -> None:
    for index, item in enumerate(items):
        if not _has_text(item):
            raise ValueError(f"{context}[{index}] must contain visible text")


def _validate_flow_steps(items: list[Any], context: str) -> None:
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            raise ValueError(f"{context}[{index}] must be an object")
        title = item.get("title") or item.get("stage") or item.get("trigger")
        description = item.get("description") or item.get("details") or item.get("action") or item.get("behavior")
        if not _has_text(title) or not _has_text(description):
            raise ValueError(f"{context}[{index}] requires title/trigger and description/action")


def _validate_notes(items: list[Any], context: str) -> None:
    for index, item in enumerate(items):
        if isinstance(item, dict):
            title = item.get("title") or item.get("label")
            description = item.get("description") or item.get("details") or item.get("note")
            if not _has_text(title) or not _has_text(description):
                raise ValueError(f"{context}[{index}] requires title and description")
        elif not _has_text(item):
            raise ValueError(f"{context}[{index}] must contain visible note text")


def _validate_requirement_groups(groups: list[Any], context: str) -> None:
    found = False
    for group_index, group in enumerate(groups):
        if not isinstance(group, dict):
            raise ValueError(f"{context}[{group_index}] must be an object")
        items = group.get("items") or group.get("objects")
        if not isinstance(items, list) or not items:
            raise ValueError(f"{context}[{group_index}] must contain requirement items")
        for item_index, item in enumerate(items):
            if not isinstance(item, dict):
                raise ValueError(f"{context}[{group_index}].items[{item_index}] must be an object")
            title = item.get("title") or item.get("requirement") or item.get("object")
            details = item.get("details") or item.get("requirements") or item.get("build_and_visual")
            result = item.get("result") or item.get("expected_result") or item.get("gameplay_function")
            if not _has_text(title) or not _has_text(details) or not _has_text(result):
                raise ValueError(
                    f"{context}[{group_index}].items[{item_index}] requires title/object, details, and result/gameplay_function"
                )
            found = True
    if not found:
        raise ValueError(f"{context} must contain at least one material requirement row")


def _validate_result_contract(developer: dict[str, Any], context: str) -> None:
    scoring = developer.get("scoring") if isinstance(developer.get("scoring"), dict) else None
    completion = developer.get("completion_data") if isinstance(developer.get("completion_data"), dict) else None
    if (scoring is None) == (completion is None):
        raise ValueError(f"{context} must define exactly one of scoring or completion_data")

    if scoring is not None:
        if scoring.get("produces_score") is not True:
            raise ValueError(f"{context}.scoring.produces_score must be true")
        for field in (
            "score_name",
            "timer_start",
            "timer_stop",
            "no_score_condition",
            "duplicate_prevention",
            "final_result_relationship",
            "player_facing_display",
            "telemetry_export",
        ):
            _require_text(scoring, field, f"{context}.scoring")
        components = scoring.get("components")
        if not (isinstance(components, list) and components) and not (
            _has_text(scoring.get("formula")) or _has_text(scoring.get("summary"))
        ):
            raise ValueError(f"{context}.scoring requires components or an explicit formula/summary")
        return

    assert completion is not None
    if completion.get("produces_score") is not False:
        raise ValueError(f"{context}.completion_data.produces_score must be false for explicit No Objective Score")
    for field in (
        "completion_name",
        "valid_completion_condition",
        "recorded_data",
        "interrupted_completion_behavior",
        "duplicate_prevention",
        "handoff_result",
        "final_result_relationship",
        "player_facing_display",
        "telemetry_export",
    ):
        _require_text(completion, field, f"{context}.completion_data")


def validate_mandatory_contract(data: dict[str, Any]) -> None:
    document = data["document"]
    _require_text(document, "document_type", "document")
    _require_text(document, "version", "document")

    overview_data = data["overview"]
    for field in ("project_context", "main_experience", "document_scope", "intended_use"):
        _require_text(overview_data, field, "overview")

    facts = _require_nonempty_list(overview_data, "facts", "overview")
    fact_keys = {
        str(item.get("key"))
        for item in facts
        if isinstance(item, dict) and isinstance(item.get("key"), str)
    }
    missing_fact_keys = sorted(REQUIRED_OVERVIEW_FACT_KEYS - fact_keys)
    if missing_fact_keys:
        raise ValueError(f"overview.facts missing Golden fact keys: {missing_fact_keys}")
    for index, item in enumerate(facts):
        if not isinstance(item, dict) or not _has_text(item.get("label")) or not _has_text(item.get("value")):
            raise ValueError(f"overview.facts[{index}] requires key, label, and value")

    journey = _require_nonempty_list(overview_data, "journey", "overview")
    _validate_flow_steps(journey, "overview.journey")
    systems = _require_nonempty_list(overview_data, "main_systems", "overview")
    for index, item in enumerate(systems):
        if not isinstance(item, dict) or not _has_text(item.get("title")) or not _has_text(item.get("description")):
            raise ValueError(f"overview.main_systems[{index}] requires title and description")

    packages = data["packages"]
    if not packages:
        raise ValueError("packages must contain at least one gameplay package")

    flow = data["gameplay_flow"]
    expected_flow_ids = ["journey-begins", *[pkg["id"] for pkg in packages]]
    actual_flow_ids = [item["id"] for item in flow]
    if actual_flow_ids != expected_flow_ids:
        raise ValueError(
            "Golden mandatory contract: gameplay_flow must contain The Journey Begins followed by one page per package; "
            f"expected IDs {expected_flow_ids}, got {actual_flow_ids}"
        )
    if txt(flow[0].get("title"))["en"].strip() != "The Journey Begins":
        raise ValueError('gameplay_flow[0].title must be "The Journey Begins"')
    for index, item in enumerate(flow):
        context = f"gameplay_flow[{index}]"
        _require_text(item, "title", context)
        _require_text(item, "narrative_context", context)
        _validate_flow_steps(_require_nonempty_list(item, "beats", context), f"{context}.beats")
        _require_text(item, "next_destination", context)

    global_sections = data["global_development"]
    expected_global_ids = [section_id for section_id, _ in MANDATORY_GLOBAL_SECTIONS]
    actual_global_ids = [item["id"] for item in global_sections]
    if actual_global_ids != expected_global_ids:
        raise ValueError(
            "Golden mandatory contract: global_development must use the four fixed Golden functions in order; "
            f"expected IDs {expected_global_ids}, got {actual_global_ids}"
        )
    for index, ((section_id, section_title), item) in enumerate(zip(MANDATORY_GLOBAL_SECTIONS, global_sections)):
        context = f"global_development[{index}]"
        if txt(item.get("title"))["en"].strip() != section_title:
            raise ValueError(f'{context}.title must be "{section_title}" for {section_id}')
        _require_text(item, "overview", context)
        _validate_flow_steps(_require_nonempty_list(item, "flow", context), f"{context}.flow")
        _validate_requirement_groups(
            _require_nonempty_list(item, "requirements", context),
            f"{context}.requirements",
        )
        _validate_notes(_require_nonempty_list(item, "notes", context), f"{context}.notes")

    for index, pkg in enumerate(packages):
        context = f"packages[{index}]"
        _require_text(pkg, "title", context)
        _require_text(pkg, "package_label", context)
        _validate_text_items(_require_nonempty_list(pkg, "acceptance", context), f"{context}.acceptance")

        gameplay = pkg["gameplay"]
        for field in (
            "context",
            "main_objective",
            "result",
            "purpose",
            "gameplay_time",
            "start_condition",
            "end_condition",
            "blocked_or_fail_condition",
        ):
            _require_text(gameplay, field, f"{context}.gameplay")
        _validate_flow_steps(
            _require_nonempty_list(gameplay, "player_flow", f"{context}.gameplay"),
            f"{context}.gameplay.player_flow",
        )

        level = pkg["level_design"]
        _require_text(level, "overview", f"{context}.level_design")
        _validate_flow_steps(
            _require_nonempty_list(level, "flow", f"{context}.level_design"),
            f"{context}.level_design.flow",
        )
        _validate_requirement_groups(
            _require_nonempty_list(level, "requirements", f"{context}.level_design"),
            f"{context}.level_design.requirements",
        )
        _validate_notes(
            _require_nonempty_list(level, "notes", f"{context}.level_design"),
            f"{context}.level_design.notes",
        )

        developer = pkg["developer"]
        _require_text(developer, "overview", f"{context}.developer")
        _validate_flow_steps(
            _require_nonempty_list(developer, "flow", f"{context}.developer"),
            f"{context}.developer.flow",
        )
        _validate_requirement_groups(
            _require_nonempty_list(developer, "requirements", f"{context}.developer"),
            f"{context}.developer.requirements",
        )
        if not developer.get("reset"):
            raise ValueError(f"{context}.developer.reset is required by the Golden mandatory contract")
        _require_text(developer, "reset_result", f"{context}.developer")
        _validate_notes(
            _require_nonempty_list(developer, "notes", f"{context}.developer"),
            f"{context}.developer.notes",
        )
        _validate_result_contract(developer, f"{context}.developer")


def validate(data: dict[str, Any]) -> list[str]:
    if not isinstance(data, dict):
        raise ValueError("render data root must be an object")
    if not isinstance(data.get("document"), dict) or not txt(data["document"].get("title"))["en"].strip():
        raise ValueError("document.title is required")
    if not isinstance(data.get("overview"), dict):
        raise ValueError("overview is required")

    languages = document_languages(data)
    if "id" in languages:
        validate_bilingual_values(data, "render_data")

    collections: dict[str, list[dict[str, Any]]] = {}
    for key in ("gameplay_flow", "global_development", "packages"):
        raw = data.get(key, [])
        if not isinstance(raw, list):
            raise ValueError(f"{key} must be an array")
        items: list[dict[str, Any]] = []
        for index, item in enumerate(raw):
            if not isinstance(item, dict):
                raise ValueError(f"{key}[{index}] must be an object")
            item_id = item.get("id")
            if not isinstance(item_id, str) or not ID_RE.fullmatch(item_id):
                raise ValueError(f"{key}[{index}] has invalid stable id: {item_id!r}")
            items.append(item)
        collections[key] = items

    packages = collections["packages"]
    package_ids = [pkg["id"] for pkg in packages]
    if len(package_ids) != len(set(package_ids)):
        raise ValueError("Duplicate package id")

    for pkg in packages:
        for key in ("gameplay", "level_design", "developer"):
            if not isinstance(pkg.get(key), dict):
                raise ValueError(f'Package {pkg["id"]} requires {key}')
        terms = pkg.get("terms", [])
        if not isinstance(terms, list):
            raise ValueError(f'Package {pkg["id"]}.terms must be an array')
        for index, term in enumerate(terms):
            if not isinstance(term, dict):
                raise ValueError(f'Package {pkg["id"]}.terms[{index}] must be an object')
            context = f'Package {pkg["id"]}.terms[{index}]'
            validate_aliases(term.get("aliases"), context)
            validate_term_roles(term.get("roles"), context)

    opening_terms = collections["gameplay_flow"][0].get("terms", []) if collections["gameplay_flow"] else []
    if opening_terms is not None and not isinstance(opening_terms, list):
        raise ValueError("gameplay_flow[0].terms must be an array when provided")
    for index, term in enumerate(opening_terms or []):
        if not isinstance(term, dict):
            raise ValueError(f"gameplay_flow[0].terms[{index}] must be an object")
        validate_aliases(term.get("aliases"), f"gameplay_flow[0].terms[{index}]")

    data["gameplay_flow"] = collections["gameplay_flow"]
    data["global_development"] = collections["global_development"]
    data["packages"] = packages
    validate_mandatory_contract(data)

    if OPEN_RE.search(json.dumps(data, ensure_ascii=False)):
        raise ValueError("Render data contains unresolved placeholder text")
    return languages


def apply_result_summaries(data: dict[str, Any]) -> None:
    for pkg in data.get("packages", []):
        gameplay = pkg["gameplay"]
        if _has_text(gameplay.get("scoring_criteria")) or _has_text(gameplay.get("scoring_summary")):
            continue
        developer = pkg["developer"]
        completion = developer.get("completion_data") if isinstance(developer.get("completion_data"), dict) else None
        if completion is None:
            continue
        handoff = txt(completion.get("handoff_result"))
        gameplay["scoring_criteria"] = {
            "en": f'No Objective Score — {handoff["en"]}',
            "id": f'Tanpa Objective Score — {handoff["id"]}',
        }


def require_exact_once(source: str, marker: str, label: str) -> None:
    count = source.count(marker)
    if count != 1:
        raise ValueError(f"Template requires exactly one {label}; found {count}")


def replace_regex_once(source: str, pattern: re.Pattern[str], replacement: str, label: str) -> str:
    matches = list(pattern.finditer(source))
    if len(matches) != 1:
        raise ValueError(f"Template requires exactly one {label}; found {len(matches)}")
    return pattern.sub(lambda _: replacement, source, count=1)


def element_range(source: str, marker: str, tag: str, label: str) -> tuple[int, int]:
    require_exact_once(source, marker, label)
    start = source.find(marker)
    open_end = source.find(">", start) + 1
    depth = 0
    for match in re.finditer(rf"</?{tag}\b[^>]*>", source[start:], re.I):
        depth += -1 if match.group(0).startswith("</") else 1
        if depth == 0:
            return open_end, start + match.start()
    raise ValueError(f"Closing tag not found for {label}")


def replace_inner(source: str, marker: str, tag: str, inner: str, label: str) -> str:
    start, end = element_range(source, marker, tag, label)
    return source[:start] + inner + source[end:]


def apply_document_runtime_contract(source: str, languages: list[str]) -> str:
    html_matches = list(HTML_TAG_RE.finditer(source))
    if len(html_matches) != 1:
        raise ValueError(f"Template requires exactly one html tag; found {len(html_matches)}")
    opening = html_matches[0].group(0)
    if "data-document-languages=" in opening:
        raise ValueError("Template html tag must not define project language availability")
    language_value = ",".join(languages)
    updated = opening[:-1] + f' data-document-languages="{esc(language_value)}">'
    return source[:html_matches[0].start()] + updated + source[html_matches[0].end():]


def single_language_enforcer(namespace: str) -> str:
    return (
        '<script id="prd-single-language-enforcer">(function(){'
        "document.documentElement.lang='en';"
        "document.querySelector('.language-panel')?.setAttribute('hidden','');"
        "document.querySelectorAll('.i18n-text').forEach(function(node){"
        "if(typeof node.dataset.en==='string'){node.textContent=node.dataset.en;}});"
        f"try{{localStorage.setItem('prd-{namespace}-language','en');}}catch(e){{}}"
        '})();</script>'
    )


def render(template: Path, render_data: Path, output: Path) -> None:
    if not template.is_file():
        raise FileNotFoundError(f"Approved template not found: {template}")

    render_data_bytes = render_data.read_bytes()
    data = json.loads(render_data_bytes.decode("utf-8"))
    render_data_sha = hashlib.sha256(render_data_bytes).hexdigest()
    languages = validate(data)
    apply_result_summaries(data)

    source = template.read_text(encoding="utf-8")
    require_exact_once(source, STORAGE_PREFIX_TOKEN, "storage-prefix template token")
    source = apply_document_runtime_contract(source, languages)

    pages = [overview(data)] + flow_pages(data) + global_pages(data) + package_pages(data)
    nav = navigation(data)

    title = txt(data["document"]["title"])
    mark = str(data["document"].get("brand_mark") or title["en"][:1] or "P").upper()
    brand = (
        f'<a aria-label="{esc(title["en"])} overview" class="sidebar-brand" href="#summary">'
        f'<span class="brand-mark">{i18n(mark)}</span>'
        f'<span class="brand-copy"><strong>{i18n(title)}</strong>'
        f'<small>{i18n(data["document"].get("document_type", "Production Specification"))}</small></span></a>'
    )
    source = replace_regex_once(source, SIDEBAR_BRAND_RE, brand, "sidebar brand marker")
    source = replace_inner(source, '<nav class="sidebar-nav">', "nav", nav, "sidebar navigation marker")
    source = replace_inner(source, '<main class="document-main">', "main", "".join(pages), "document main marker")

    glossary_json = script_safe_json(glossary(data))
    source = replace_regex_once(
        source,
        GLOSSARY_ASSIGN_RE,
        f"const glossary = {glossary_json};\n  const tooltip =",
        "glossary script assignment marker",
    )

    document = data["document"]
    namespace = slug(title["en"])
    page_title = f'{title["en"]} — {txt(document.get("subtitle", "Production Specification"))["en"]}'
    source = replace_regex_once(source, TITLE_RE, f"<title>{esc(page_title)}</title>", "document title marker")

    description = txt(document.get("description") or data["overview"].get("project_context") or page_title)["en"]
    source = replace_regex_once(
        source,
        DESCRIPTION_META_RE,
        f'<meta content="{esc(description)}" name="description"/>',
        "description metadata marker",
    )
    source = replace_regex_once(
        source,
        SPEC_VERSION_META_RE,
        f'<meta content="prd-{namespace}-v{esc(document.get("version", "1.0"))}" name="specification-version"/>',
        "specification-version metadata marker",
    )
    source = source.replace(STORAGE_PREFIX_TOKEN, f"prd-{namespace}-", 1)

    require_exact_once(source, "</head>", "head closing marker")
    source = source.replace(
        "</head>",
        f'<meta content="{render_data_sha}" name="render-data-sha256"/>\n</head>',
        1,
    )

    if languages == ["en"]:
        require_exact_once(source, "</body>", "body closing marker")
        source = source.replace("</body>", single_language_enforcer(namespace) + "\n</body>", 1)

    section_ids = set(re.findall(r'<section\b[^>]*\bid="([^"]+)"', source))
    targets = set(re.findall(r'data-target="([^"]+)"', nav))
    missing = sorted(targets - section_ids)
    if missing:
        raise ValueError(f"Navigation targets missing from generated pages: {missing}")
    if OPEN_RE.search("".join(pages)):
        raise ValueError("Generated pages contain unresolved placeholders")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(source, encoding="utf-8")


def main() -> int:
    default_template = HERE.parent / "template" / "runtime-template.html"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("render_data", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--template", type=Path, default=default_template)
    args = parser.parse_args()
    try:
        render(args.template, args.render_data, args.output)
        print(args.output)
        return 0
    except (OSError, ValueError) as exc:
        print(f"PRD RENDER FAILED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
