from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from shared.localization import document_languages, validate_bilingual_values
from shared.render_schema import RenderData, validated_render_data

from .core import esc, i18n, slug, txt
from .pages import flow_pages, global_pages, glossary, navigation, overview, package_pages
from .template_adapter import TemplateAdapter

OPEN_RE = re.compile(
    r"\b(?:TBD|TODO|FIXME|INSERT\s+(?:TEXT|VALUE)|USE\s+APPROVED\s+AMOUNT)\b|\[OPEN\]",
    re.I,
)
STORAGE_PREFIX_TOKEN = "__PRD_STORAGE_PREFIX__"
TERM_ROLES = {"gameplay", "level_design", "developer"}
MANDATORY_GLOBAL_SECTIONS = (
    ("development-overview", "Development Overview"),
    ("game-system", "Game System"),
    ("data-reset", "Data and Reset"),
    ("gameplay-development", "Gameplay Development"),
)
REQUIRED_OVERVIEW_FACT_KEYS = ("session-model", "target-playtime", "game-structure")
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def script_safe_json(value: Any) -> str:
    text = json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
    return (
        text.replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def _validated(data: dict[str, Any]) -> tuple[RenderData, list[str]]:
    typed = validated_render_data(data)
    languages = document_languages(data)
    if "id" in languages:
        validate_bilingual_values(data)
    _validate_design_invariants(typed)
    _validate_terms(typed)
    if OPEN_RE.search(json.dumps(data, ensure_ascii=False)):
        raise ValueError("Render data contains unresolved placeholder text")
    return typed, languages


def validate(data: dict[str, Any]) -> list[str]:
    _, languages = _validated(data)
    return languages


def _validate_design_invariants(data: RenderData) -> None:
    facts = data["overview"]["facts"]
    fact_keys = tuple(str(item["key"]) for item in facts)
    if fact_keys != REQUIRED_OVERVIEW_FACT_KEYS:
        raise ValueError(
            "overview.facts must contain Session Model, Target Playtime, and Game Structure in canonical order; "
            f"got {fact_keys}"
        )

    packages = data["packages"]
    package_ids = [str(package["id"]) for package in packages]
    for package_id in package_ids:
        if ID_RE.fullmatch(package_id) is None:
            raise ValueError(f"invalid package stable id: {package_id!r}")

    expected_flow_ids = ["journey-begins", *package_ids]
    actual_flow_ids = [str(item["id"]) for item in data["gameplay_flow"]]
    if actual_flow_ids != expected_flow_ids:
        raise ValueError(
            "gameplay_flow must contain journey-begins followed by one page per package; "
            f"expected {expected_flow_ids}, got {actual_flow_ids}"
        )
    if txt(data["gameplay_flow"][0]["title"])["en"].strip() != "The Journey Begins":
        raise ValueError('gameplay_flow[0].title must be "The Journey Begins"')

    expected_global_ids = [section_id for section_id, _ in MANDATORY_GLOBAL_SECTIONS]
    actual_global_ids = [str(item["id"]) for item in data["global_development"]]
    if actual_global_ids != expected_global_ids:
        raise ValueError(
            "global_development must use the four fixed Golden functions in canonical order; "
            f"expected {expected_global_ids}, got {actual_global_ids}"
        )
    for (section_id, title), item in zip(MANDATORY_GLOBAL_SECTIONS, data["global_development"]):
        if txt(item["title"])["en"].strip() != title:
            raise ValueError(f'{section_id}.title must be "{title}"')

    for package in packages:
        result_mode = package["gameplay"]["result_model"]["mode"]
        developer = package["developer"]
        if result_mode == "scored" and developer.get("scoring") is None:
            raise ValueError(f"package {package['id']} scored result requires developer.scoring")
        if result_mode == "completion_only" and developer.get("completion_data") is None:
            raise ValueError(f"package {package['id']} completion_only result requires developer.completion_data")


def _validate_terms(data: RenderData) -> None:
    groups: list[tuple[str, list[Any]]] = []
    if data["gameplay_flow"]:
        groups.append(("gameplay_flow[0].terms", list(data["gameplay_flow"][0].get("terms", []))))
    for index, package in enumerate(data["packages"]):
        groups.append((f"packages[{index}].terms", list(package.get("terms", []))))
    for context, terms in groups:
        for index, term in enumerate(terms):
            aliases = term.get("aliases")
            if aliases is not None:
                _validate_aliases(aliases, f"{context}[{index}]")
            roles = term.get("roles")
            if roles is not None:
                if not isinstance(roles, list) or not all(isinstance(role, str) for role in roles):
                    raise ValueError(f"{context}[{index}].roles must be an array of strings")
                if len(roles) != len(set(roles)):
                    raise ValueError(f"{context}[{index}].roles must not contain duplicates")
                invalid = sorted(set(roles) - TERM_ROLES)
                if invalid:
                    raise ValueError(f"{context}[{index}].roles contains unsupported role: {invalid[0]}")


def _validate_aliases(aliases: Any, context: str) -> None:
    if isinstance(aliases, list):
        if not all(isinstance(alias, str) for alias in aliases):
            raise ValueError(f"{context}.aliases must be an array of strings")
        return
    if isinstance(aliases, dict):
        if not set(aliases).issubset({"en", "id"}) or not aliases:
            raise ValueError(f"{context}.aliases object may define only en and/or id")
        for language, values in aliases.items():
            if not isinstance(values, list) or not all(isinstance(alias, str) for alias in values):
                raise ValueError(f"{context}.aliases.{language} must be an array of strings")
        return
    raise ValueError(f"{context}.aliases must be an array of strings or an en/id object")


def single_language_enforcer(namespace: str) -> str:
    return (
        '<script id="prd-single-language-enforcer">(function(){'
        "document.documentElement.lang='en';"
        "document.querySelector('.language-panel')?.setAttribute('hidden','');"
        "document.querySelectorAll('.i18n-text').forEach(function(node){"
        "if(typeof node.dataset.en==='string'){node.textContent=node.dataset.en;}});"
        f"try{{localStorage.setItem('prd-{namespace}-language','en');}}catch(e){{}}"
        "})();</script>"
    )


def render(template: Path, render_data: Path, output: Path) -> None:
    if not template.is_file():
        raise FileNotFoundError(f"Approved template not found: {template}")

    render_data_bytes = render_data.read_bytes()
    raw = json.loads(render_data_bytes.decode("utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("render-data root must be an object")
    data, languages = _validated(raw)
    render_data_sha = hashlib.sha256(render_data_bytes).hexdigest()

    adapter = TemplateAdapter(template.read_text(encoding="utf-8"))
    adapter.require_once(STORAGE_PREFIX_TOKEN, "storage-prefix template token")
    adapter.set_document_languages(languages)

    pages = [overview(data)] + flow_pages(data) + global_pages(data) + package_pages(data)
    nav = navigation(data)

    title = txt(data["document"]["title"])
    mark = str(data["document"].get("brand_mark") or title["en"][:1] or "P").upper()
    brand = (
        f'<a aria-label="{esc(title["en"])} overview" class="sidebar-brand" href="#summary">'
        f'<span class="brand-mark">{i18n(mark)}</span>'
        f'<span class="brand-copy"><strong>{i18n(title)}</strong>'
        f"<small>{i18n(data['document']['document_type'])}</small></span></a>"
    )
    adapter.set_sidebar_brand(brand)
    adapter.set_navigation(nav)
    adapter.set_document_main("".join(pages))
    adapter.set_glossary_assignment(script_safe_json(glossary(data)))

    document = data["document"]
    namespace = slug(title["en"])
    adapter.replace_token(STORAGE_PREFIX_TOKEN, f"prd-{namespace}-", "storage-prefix template token")
    subtitle = txt(document.get("subtitle") or "Production Specification")["en"]
    page_title = f"{title['en']} — {subtitle}"
    adapter.set_title(page_title)
    description = txt(document.get("description") or data["overview"]["project_context"])["en"]
    adapter.set_description(description)
    adapter.set_specification_version(f"prd-{namespace}-v{document['version']}")
    adapter.inject_head(f'<meta content="{render_data_sha}" name="render-data-sha256"/>')

    if languages == ["en"]:
        adapter.inject_body(single_language_enforcer(namespace))

    source = adapter.source
    section_ids = set(re.findall(r'<section\b[^>]*\bid="([^"]+)"', source))
    targets = set(re.findall(r'data-target="([^"]+)"', nav))
    missing = sorted(targets - section_ids)
    if missing:
        raise ValueError(f"Navigation targets missing from generated pages: {missing}")
    if OPEN_RE.search("".join(pages)):
        raise ValueError("Generated pages contain unresolved placeholders")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(source, encoding="utf-8")
