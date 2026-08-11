#!/usr/bin/env python3
"""Render derived PRD JSON into the approved Golden Sample composition."""
from __future__ import annotations
import argparse, hashlib, json, re, sys
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
GLOSSARY_SKIP_TOKEN = ".language-switch,.theme-switch,.view-switch,a,button"
TERM_ROLES = {"gameplay", "level_design", "developer"}
GOLDEN_GLOBAL_SECTIONS = (
    ("development-overview", "Development Overview"),
    ("game-system", "Session & Runtime System"),
    ("data-reset", "Data, Recovery & Reset"),
    ("gameplay-development", "Gameplay Package Integration"),
)
GOLDEN_OVERVIEW_FACT_KEYS = {"session-model", "target-playtime", "game-structure"}
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

RENDERER_CONTRACT_STYLE = """<style id="prd-renderer-contract-style">
/* One renderer-owned reading layer. Keep new PRD UI refinements here instead of stacking template patches. */
@media(min-width:761px){
  .document-main .journey{grid-template-columns:repeat(var(--prd-journey-columns,6),1fr)}
  .document-main .journey article:nth-child(n+7){border-top:1px solid var(--line)}
  .document-main .journey article:nth-child(6n+1){border-left:0}
  .document-main .flow{grid-template-columns:repeat(var(--prd-flow-columns,4),1fr)}
  .document-main .flow article:nth-child(n+5){border-top:1px solid var(--line)}
  .document-main .flow article:nth-child(4n+1){border-left:0}
}
@media screen{
  .document-main .sheet{min-height:0}
}
@media(min-width:981px){
  .document-main .sheet{width:min(1120px,calc(100% - 40px));padding-left:58px;padding-right:58px}
  .phase-navigation .phase-page-list{display:none}
  .phase-navigation .phase-nav-item.is-current .phase-page-list,
  .phase-navigation .phase-nav-item:focus-within .phase-page-list{display:block}
}
html[data-document-languages="en"] .language-panel{display:none!important}

/* Overview: metadata is metadata, not a warning panel. */
.document-control-block{margin:24px 0 4px}
.document-control-title{display:block;margin-bottom:8px;color:var(--muted);font-size:.66rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
.document-control-strip{display:grid;grid-template-columns:minmax(90px,.55fr) minmax(0,1.35fr) minmax(0,1fr);border:1px solid var(--line);background:var(--paper)}
.document-control-strip article{min-width:0;padding:13px 15px}
.document-control-strip article+article{border-left:1px solid var(--line)}
.document-control-strip b{display:block;margin-bottom:5px;color:var(--blue);font-size:.65rem;letter-spacing:.06em;text-transform:uppercase}
.document-control-strip p{margin:0;color:var(--ink);font-size:.82rem;line-height:1.48}
.main-system-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:12px}
.main-system-grid article{padding:15px 17px;border:1px solid var(--line);background:var(--soft)}
.main-system-grid b{display:block;margin-bottom:5px;color:var(--navy);font-size:.79rem}
.main-system-grid p{margin:0;color:var(--muted);font-size:.81rem;line-height:1.5}

/* Gameplay Flow: orient first, then tell the player story. */
.flow-orientation{display:grid;grid-template-columns:1.4fr .8fr .8fr;margin:15px 0 20px;border:1px solid var(--line);background:var(--soft)}
.flow-orientation article{min-width:0;padding:12px 14px}
.flow-orientation article+article{border-left:1px solid var(--line)}
.flow-orientation b{display:block;margin-bottom:5px;color:var(--blue);font-size:.63rem;letter-spacing:.07em;text-transform:uppercase}
.flow-orientation p{margin:0;color:var(--ink);font-size:.81rem;line-height:1.45}
.narrative-page .section-intro{max-width:80ch;color:var(--ink);font-size:.95rem;line-height:1.68}
.narrative-copy p{max-width:82ch;font-size:.89rem;line-height:1.66}
.story-transition{margin-top:20px;padding:15px 17px;border-left:4px solid var(--amber);background:var(--amber-soft)}
.story-transition b{display:block;margin-bottom:4px;color:#7b531f;font-size:.64rem;letter-spacing:.07em;text-transform:uppercase}
.story-transition p{margin:0;line-height:1.5}

/* Developer Flow: never flatten Trigger / Behavior / Data / Result into one sentence. */
.developer-flow{display:grid;gap:12px;margin-top:12px}
.developer-flow-step{border:1px solid var(--line);background:var(--paper)}
.developer-flow-step header{display:flex;align-items:center;gap:11px;padding:12px 15px;border-bottom:1px solid var(--line);background:var(--soft)}
.developer-flow-step header span:first-child{display:grid;place-items:center;flex:0 0 31px;width:31px;height:31px;border:1px solid var(--line);color:var(--blue);font-size:.67rem;font-weight:800}
.developer-flow-step header strong{color:var(--navy);font-size:.86rem}
.developer-flow-step dl{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));margin:0}
.developer-flow-step dl>div{min-width:0;padding:12px 15px}
.developer-flow-step dl>div:nth-child(even){border-left:1px solid var(--line)}
.developer-flow-step dl>div:nth-child(n+3){border-top:1px solid var(--line)}
.developer-flow-step dt{margin:0 0 5px;color:var(--blue);font-size:.62rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase}
.developer-flow-step dd{margin:0;color:var(--ink);font-size:.82rem;line-height:1.53}

/* Tables: retain production-table semantics but give long requirements room to breathe. */
.production-table{font-size:.83rem}
.production-table th{padding:11px 12px;line-height:1.35}
.production-table td{padding:13px 13px;line-height:1.55}
.production-table .compact-cell-list{margin:0;padding-left:17px}
.production-table .compact-cell-list li+li{margin-top:7px}
.production-table .quarry-group-row td{padding-top:10px;padding-bottom:10px;background:#edf3f6;color:var(--navy);border-color:var(--line-strong,var(--line))}
.quarry-development-table tbody tr:not(.quarry-group-row)>td:last-child,
.quarry-dev-table tbody tr:not(.quarry-group-row)>td:last-child{background:rgba(53,120,154,.055)}
.phase-overview-table td:first-child{width:210px;background:var(--soft)}
.phase-overview-table td:first-child b{color:var(--navy)}

/* Acceptance: observable outcomes read as completion checks, not another generic bullet list. */
.acceptance-list{display:grid;gap:8px;margin:0;padding:0;list-style:none}
.acceptance-list li{position:relative;margin:0;padding-left:24px;line-height:1.55}
.acceptance-list li::before{content:"✓";position:absolute;left:0;top:0;color:var(--green);font-weight:900}

/* Glossary index: visible affordance in prose, while the Terms Used panel remains a clean index. */
.glossary-term{padding:0 .08em;border-radius:3px;border-bottom:1px dotted var(--blue);background:rgba(53,120,154,.07);color:var(--navy);font-weight:760;text-decoration:none}
.glossary-term:hover,.glossary-term:focus-visible{background:rgba(53,120,154,.14);color:var(--blue);outline:2px solid transparent}

/* Sidebar: show local depth for the active package instead of expanding every package at once. */
.phase-navigation .phase-nav-item{border-left-color:rgba(255,255,255,.12)}
.phase-navigation .phase-nav-item.is-current{background:rgba(255,255,255,.045);border-left-color:var(--amber)}
.phase-navigation .phase-page-list{margin-top:2px;margin-bottom:7px}
.phase-navigation .phase-page-link{padding-top:7px!important;padding-bottom:7px!important}

body.theme-dark .document-control-strip,
body.theme-dark .developer-flow-step{background:#172a33;border-color:#405761}
body.theme-dark .document-control-strip article+article,
body.theme-dark .developer-flow-step header,
body.theme-dark .developer-flow-step dl>div:nth-child(even),
body.theme-dark .developer-flow-step dl>div:nth-child(n+3){border-color:#405761}
body.theme-dark .developer-flow-step header,
body.theme-dark .main-system-grid article,
body.theme-dark .flow-orientation{background:#1d3039;border-color:#405761}
body.theme-dark .flow-orientation article+article{border-color:#405761}
body.theme-dark .document-control-strip p,
body.theme-dark .flow-orientation p,
body.theme-dark .developer-flow-step dd{color:#d9e5e9}
body.theme-dark .production-table .quarry-group-row td{background:#1c3540;color:#edf6f8}
body.theme-dark .quarry-development-table tbody tr:not(.quarry-group-row)>td:last-child,
body.theme-dark .quarry-dev-table tbody tr:not(.quarry-group-row)>td:last-child{background:rgba(104,199,237,.06)}
body.theme-dark .glossary-term{background:rgba(104,199,237,.09);border-bottom-color:#68c7ed;color:#eef8fb}
body.theme-dark .glossary-term:hover,body.theme-dark .glossary-term:focus-visible{background:rgba(104,199,237,.16);color:#fff}

@media(max-width:900px){
  .document-control-strip,.flow-orientation,.developer-flow-step dl,.main-system-grid{grid-template-columns:1fr}
  .document-control-strip article+article,.flow-orientation article+article,.developer-flow-step dl>div:nth-child(even){border-left:0;border-top:1px solid var(--line)}
}
@media print{
  .document-main .sheet{min-height:1120px}
  .glossary-term{padding:0;background:transparent;border-bottom:0;color:inherit}
  .developer-flow-step,.document-control-strip,.flow-orientation{break-inside:avoid}
}
</style>"""

READING_EXPERIENCE_RUNTIME = """<script id="prd-reading-experience-runtime">
(() => {
  const labels = {
    clean: {en: 'Gameplay Journey', id: 'Alur Gameplay'},
    professional: {en: 'Full Production', id: 'Produksi Lengkap'}
  };
  function syncViewLabels(){
    const language = document.documentElement.lang === 'id' ? 'id' : 'en';
    document.querySelectorAll('[data-mode-label]').forEach((button) => {
      const copy = button.querySelector('.i18n-text');
      const label = labels[button.dataset.modeLabel];
      if (!copy || !label) return;
      copy.dataset.en = label.en;
      copy.dataset.id = label.id;
      copy.textContent = label[language];
    });
  }
  syncViewLabels();
  const observer = new MutationObserver((mutations) => {
    if (mutations.some((mutation) => mutation.type === 'attributes' && mutation.attributeName === 'lang')){
      syncViewLabels();
    }
  });
  observer.observe(document.documentElement, {attributes:true, attributeFilter:['lang']});
})();
</script>"""


def script_safe_json(value: Any) -> str:
    """Serialize JSON for direct insertion into a classic HTML <script> block."""
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
        raise ValueError(
            f"{path} must use an explicit en/id localized value for bilingual document"
        )


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


def _validate_result_contract(dev: dict[str, Any], context: str) -> None:
    scoring = dev.get("scoring") if isinstance(dev.get("scoring"), dict) else None
    completion = dev.get("completion_data") if isinstance(dev.get("completion_data"), dict) else None
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
            raise ValueError(
                f"{context}.scoring requires components or an explicit formula/summary"
            )
    else:
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
    _require_text(overview_data, "project_context", "overview")
    _require_text(overview_data, "main_experience", "overview")
    _require_text(overview_data, "document_scope", "overview")
    _require_text(overview_data, "intended_use", "overview")
    facts = _require_nonempty_list(overview_data, "facts", "overview")
    fact_keys = {
        str(item.get("key"))
        for item in facts
        if isinstance(item, dict) and isinstance(item.get("key"), str)
    }
    missing_fact_keys = sorted(GOLDEN_OVERVIEW_FACT_KEYS - fact_keys)
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
            f"Golden mandatory contract: gameplay_flow must contain The Journey Begins followed by one page per package; expected IDs {expected_flow_ids}, got {actual_flow_ids}"
        )
    if txt(flow[0].get("title"))["en"].strip() != "The Journey Begins":
        raise ValueError('gameplay_flow[0].title must be "The Journey Begins"')
    for index, item in enumerate(flow):
        context = f"gameplay_flow[{index}]"
        _require_text(item, "title", context)
        _require_text(item, "narrative_context", context)
        beats = _require_nonempty_list(item, "beats", context)
        _validate_flow_steps(beats, f"{context}.beats")
        _require_text(item, "next_destination", context)

    global_sections = data["global_development"]
    expected_global_ids = [section_id for section_id, _ in GOLDEN_GLOBAL_SECTIONS]
    actual_global_ids = [item["id"] for item in global_sections]
    if actual_global_ids != expected_global_ids:
        raise ValueError(
            f"Golden mandatory contract: global_development must use the four fixed Golden functions in order; expected IDs {expected_global_ids}, got {actual_global_ids}"
        )
    for index, ((section_id, section_title), item) in enumerate(zip(GOLDEN_GLOBAL_SECTIONS, global_sections)):
        context = f"global_development[{index}]"
        if txt(item.get("title"))["en"].strip() != section_title:
            raise ValueError(f'{context}.title must be "{section_title}" for {section_id}')
        _require_text(item, "overview", context)
        steps = _require_nonempty_list(item, "flow", context)
        _validate_flow_steps(steps, f"{context}.flow")
        requirements = _require_nonempty_list(item, "requirements", context)
        _validate_requirement_groups(requirements, f"{context}.requirements")
        notes = _require_nonempty_list(item, "notes", context)
        _validate_notes(notes, f"{context}.notes")

    for index, pkg in enumerate(packages):
        context = f"packages[{index}]"
        _require_text(pkg, "title", context)
        _require_text(pkg, "package_label", context)
        acceptance = _require_nonempty_list(pkg, "acceptance", context)
        _validate_text_items(acceptance, f"{context}.acceptance")

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
        player_flow = _require_nonempty_list(gameplay, "player_flow", f"{context}.gameplay")
        _validate_flow_steps(player_flow, f"{context}.gameplay.player_flow")

        level = pkg["level_design"]
        _require_text(level, "overview", f"{context}.level_design")
        level_flow = _require_nonempty_list(level, "flow", f"{context}.level_design")
        _validate_flow_steps(level_flow, f"{context}.level_design.flow")
        level_requirements = _require_nonempty_list(level, "requirements", f"{context}.level_design")
        _validate_requirement_groups(level_requirements, f"{context}.level_design.requirements")
        level_notes = _require_nonempty_list(level, "notes", f"{context}.level_design")
        _validate_notes(level_notes, f"{context}.level_design.notes")

        dev = pkg["developer"]
        _require_text(dev, "overview", f"{context}.developer")
        dev_flow = _require_nonempty_list(dev, "flow", f"{context}.developer")
        _validate_flow_steps(dev_flow, f"{context}.developer.flow")
        dev_requirements = _require_nonempty_list(dev, "requirements", f"{context}.developer")
        _validate_requirement_groups(dev_requirements, f"{context}.developer.requirements")
        if not dev.get("reset"):
            raise ValueError(f"{context}.developer.reset is required by the Golden mandatory contract")
        dev_notes = _require_nonempty_list(dev, "notes", f"{context}.developer")
        _validate_notes(dev_notes, f"{context}.developer.notes")
        _validate_result_contract(dev, f"{context}.developer")


def validate(data: dict) -> list[str]:
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
    pids = [pkg["id"] for pkg in packages]
    if len(pids) != len(set(pids)):
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

    data["gameplay_flow"] = collections["gameplay_flow"]
    data["global_development"] = collections["global_development"]
    data["packages"] = packages
    validate_mandatory_contract(data)

    if OPEN_RE.search(json.dumps(data, ensure_ascii=False)):
        raise ValueError("Render data contains unresolved placeholder text")
    return languages


def apply_result_summaries(data: dict[str, Any]) -> None:
    """Make the Gameplay Information result row explicit without inventing meaning."""
    for pkg in data.get("packages", []):
        gameplay = pkg["gameplay"]
        if _has_text(gameplay.get("scoring_criteria")) or _has_text(gameplay.get("scoring_summary")):
            continue
        dev = pkg["developer"]
        completion = dev.get("completion_data") if isinstance(dev.get("completion_data"), dict) else None
        if completion is None:
            continue
        handoff = txt(completion.get("handoff_result"))
        gameplay["scoring_criteria"] = {
            "en": f'No Objective Score — {handoff["en"]}',
            "id": f'Tanpa Objective Score — {handoff["id"]}',
        }


def require_exact_once(src: str, marker: str, label: str) -> None:
    count = src.count(marker)
    if count != 1:
        raise ValueError(f"Template requires exactly one {label}; found {count}")


def replace_regex_once(src: str, pattern: re.Pattern[str], replacement: str, label: str) -> str:
    matches = list(pattern.finditer(src))
    if len(matches) != 1:
        raise ValueError(f"Template requires exactly one {label}; found {len(matches)}")
    return pattern.sub(lambda _: replacement, src, count=1)


def element_range(src: str, marker: str, tag: str, label: str) -> tuple[int, int]:
    require_exact_once(src, marker, label)
    start = src.find(marker)
    open_end = src.find(">", start) + 1
    depth = 0
    for match in re.finditer(rf"</?{tag}\b[^>]*>", src[start:], re.I):
        depth += -1 if match.group(0).startswith("</") else 1
        if depth == 0:
            return open_end, start + match.start()
    raise ValueError(f"Closing tag not found for {label}")


def replace_inner(src: str, marker: str, tag: str, inner: str, label: str) -> str:
    a, b = element_range(src, marker, tag, label)
    return src[:a] + inner + src[b:]


def require_namespace_tokens(src: str) -> None:
    for token, label in (
        ("aftershock-document-", "document local-storage namespace token"),
        ("aftershock-sidebar-collapsed", "sidebar local-storage namespace token"),
    ):
        if token not in src:
            raise ValueError(f"Template missing required {label}: {token}")


def apply_document_runtime_contract(src: str, languages: list[str]) -> str:
    html_matches = list(HTML_TAG_RE.finditer(src))
    if len(html_matches) != 1:
        raise ValueError(f"Template requires exactly one html tag; found {len(html_matches)}")
    opening = html_matches[0].group(0)
    if "data-document-languages=" in opening:
        raise ValueError("Template html tag must not define project language availability")
    language_value = ",".join(languages)
    updated = opening[:-1] + f' data-document-languages="{esc(language_value)}">'
    src = src[:html_matches[0].start()] + updated + src[html_matches[0].end():]

    # Keep glossary indexing out of the Terms Used index itself; otherwise definitions recursively highlight themselves.
    require_exact_once(src, GLOSSARY_SKIP_TOKEN, "glossary skip selector")
    src = src.replace(
        GLOSSARY_SKIP_TOKEN,
        ".language-switch,.theme-switch,.view-switch,.terms-used-collapsible,a,button",
        1,
    )

    require_exact_once(src, "</head>", "head closing marker")
    return src.replace("</head>", RENDERER_CONTRACT_STYLE + "\n</head>", 1)


def single_language_enforcer(namespace: str) -> str:
    return (
        '<script id="prd-single-language-enforcer">(function(){'
        "document.documentElement.lang='en';"
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
    src = template.read_text(encoding="utf-8")
    require_namespace_tokens(src)
    src = apply_document_runtime_contract(src, languages)

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
    src = replace_regex_once(src, SIDEBAR_BRAND_RE, brand, "sidebar brand marker")
    src = replace_inner(src, '<nav class="sidebar-nav">', "nav", nav, "sidebar navigation marker")
    src = replace_inner(src, '<main class="document-main">', "main", "".join(pages), "document main marker")

    glossary_json = script_safe_json(glossary(data))
    src = replace_regex_once(
        src,
        GLOSSARY_ASSIGN_RE,
        f"const glossary = {glossary_json};\n  const tooltip =",
        "glossary script assignment marker",
    )

    doc = data["document"]
    namespace = slug(title["en"])
    page_title = f'{title["en"]} — {txt(doc.get("subtitle", "Production Specification"))["en"]}'
    src = replace_regex_once(src, TITLE_RE, f"<title>{esc(page_title)}</title>", "document title marker")

    desc = txt(doc.get("description") or data["overview"].get("project_context") or page_title)["en"]
    src = replace_regex_once(
        src,
        DESCRIPTION_META_RE,
        f'<meta content="{esc(desc)}" name="description"/>',
        "description metadata marker",
    )
    src = replace_regex_once(
        src,
        SPEC_VERSION_META_RE,
        f'<meta content="prd-{namespace}-v{esc(doc.get("version", "1.0"))}" name="specification-version"/>',
        "specification-version metadata marker",
    )
    require_exact_once(src, "</head>", "head closing marker")
    src = src.replace(
        "</head>",
        f'<meta content="{render_data_sha}" name="render-data-sha256"/>\n</head>',
        1,
    )

    src = src.replace("aftershock-document-", f"prd-{namespace}-")
    src = src.replace("aftershock-sidebar-collapsed", f"prd-{namespace}-sidebar-collapsed")

    runtime_scripts = [READING_EXPERIENCE_RUNTIME]
    if languages == ["en"]:
        runtime_scripts.append(single_language_enforcer(namespace))
    require_exact_once(src, "</body>", "body closing marker")
    src = src.replace("</body>", "\n".join(runtime_scripts) + "\n</body>", 1)

    ids = set(re.findall(r'<section\b[^>]*\bid="([^"]+)"', src))
    targets = set(re.findall(r'data-target="([^"]+)"', nav))
    missing = sorted(targets - ids)
    if missing:
        raise ValueError(f"Navigation targets missing from generated pages: {missing}")
    if OPEN_RE.search("".join(pages)):
        raise ValueError("Generated pages contain unresolved placeholders")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(src, encoding="utf-8")


def main() -> int:
    default = HERE.parent / "template" / "approved-document.html"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("render_data", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--template", type=Path, default=default)
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
