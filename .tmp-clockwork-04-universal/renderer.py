from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from core import bi, esc, i18n, page, slug, txt
import production_assets as voice

ASSET_CATEGORIES = ("3D Models", "UI & Information", "Audio", "Visual Effects & Presentation")
SHARED_SECTION = "Global / Shared Assets"
OBJECTIVE_STYLE_MARKER = 'id="production-assets-objective-style"'

TYPE_PRIORITY = {
    "ENTITY / MODEL": 10,
    "ITEM": 20,
    "ITEM / PROJECTILE": 21,
    "BLOCK / PROP": 30,
    "UI / TEXT": 40,
    "VOICE": 50,
    "SOUND": 60,
    "PARTICLE": 70,
    "SEQUENCE": 80,
}


@dataclass
class AssetEntry:
    title: str
    category: str = ""
    flow: str = ""
    type_label: str = ""
    create_text: str = ""
    used: str = ""
    includes: str = ""
    moment: str = ""
    for_text: str = ""
    requirement: str = ""
    usage: str = ""
    content: str = ""
    order: int = 0


@dataclass
class AssetSection:
    title: str
    categories: dict[str, list[AssetEntry]] = field(default_factory=dict)
    flow_order: dict[str, int] = field(default_factory=dict)


@dataclass
class AssetRequirements:
    sections: list[AssetSection]


@dataclass
class SectionPresentation:
    title: str
    package_label: Any
    context: Any
    goal: Any
    completion: Any
    page_id: str


@dataclass
class ProductionItem:
    item_id: str
    title: str
    type_label: str
    create_text: str
    used: str
    includes: str
    moment: str
    flow: str
    flow_order: int
    sort_order: int
    content: str = ""
    speaker: str = ""
    selected_voice: str = ""
    duration: str = ""
    is_voice: bool = False


def _default_type(category: str) -> str:
    return {
        "3D Models": "ENTITY / MODEL",
        "UI & Information": "UI / TEXT",
        "Audio": "SOUND",
        "Visual Effects & Presentation": "SEQUENCE",
    }.get(category, category.upper())


def _plain_flow(value: str) -> str:
    return re.sub(r"^\s*\d+\s*[—-]\s*", "", value).strip()


def _first_sentence(value: str) -> str:
    value = " ".join(value.split()).strip()
    if not value:
        return ""
    match = re.match(r"(.+?[.!?])(?:\s|$)", value)
    return match.group(1).strip() if match else value


def _default_create(entry: AssetEntry) -> str:
    first = _first_sentence(entry.requirement)
    if first.lower().startswith(("create ", "use ", "provide ", "build ", "make ")):
        return first
    if entry.category == "UI & Information":
        return f"Create the exact player-facing {entry.title}."
    if entry.category == "Audio":
        return f"Create the standalone sound for {entry.title}."
    if entry.category == "Visual Effects & Presentation":
        return f"Create the authored sequence for {entry.title}."
    return f"Create the reusable {entry.title} setup."


def parse_asset_requirements(path: Path) -> AssetRequirements:
    text = path.read_text(encoding="utf-8")
    if voice.PLACEHOLDER_RE.search(text):
        raise ValueError("Production Asset requirements contain an unresolved placeholder.")

    sections: list[AssetSection] = []
    current_section: AssetSection | None = None
    current_category: str | None = None
    entry_order = 0
    lines = text.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()

        if line.startswith("## "):
            title = line[3:].strip()
            if not title:
                raise ValueError("Production Asset section title cannot be empty.")
            current_section = AssetSection(title)
            sections.append(current_section)
            current_category = None
            entry_order = 0
            i += 1
            continue

        if line.startswith("### Gameplay Flow "):
            if current_section is None:
                raise ValueError("Gameplay Flow metadata appears before a Production Asset section.")
            flow_title = line[len("### Gameplay Flow "):].strip()
            if not flow_title:
                raise ValueError("Gameplay Flow title cannot be empty.")
            if flow_title not in current_section.flow_order:
                current_section.flow_order[flow_title] = len(current_section.flow_order) + 1
            i += 1
            while i < len(lines) and not lines[i].startswith(("## ", "### ", "#### ")):
                i += 1
            current_category = None
            continue

        if line.startswith("### "):
            if current_section is None:
                raise ValueError("Production Asset category appears before a section.")
            category = line[4:].strip()
            if category not in ASSET_CATEGORIES:
                raise ValueError(
                    f"Unsupported Production Asset category: {category}. Use one of: {', '.join(ASSET_CATEGORIES)}"
                )
            current_section.categories.setdefault(category, [])
            current_category = category
            i += 1
            continue

        if line.startswith("#### "):
            if current_section is None or current_category is None:
                raise ValueError("Production Asset entry appears before its section/category.")
            entry_order += 1
            entry = AssetEntry(title=line[5:].strip(), category=current_category, order=entry_order)
            if not entry.title:
                raise ValueError("Production Asset name cannot be empty.")
            i += 1
            while i < len(lines):
                meta = lines[i].rstrip()
                if meta.startswith(("## ", "### ", "#### ")):
                    break
                if meta.startswith("Flow:"):
                    entry.flow = meta.split(":", 1)[1].strip()
                elif meta.startswith("Type:"):
                    entry.type_label = meta.split(":", 1)[1].strip()
                elif meta.startswith("Create:"):
                    entry.create_text = meta.split(":", 1)[1].strip()
                elif meta.startswith("Used:"):
                    entry.used = meta.split(":", 1)[1].strip()
                elif meta.startswith("Includes:"):
                    entry.includes = meta.split(":", 1)[1].strip()
                elif meta.startswith("Moment:"):
                    entry.moment = meta.split(":", 1)[1].strip()
                elif meta.startswith("For:"):
                    entry.for_text = meta.split(":", 1)[1].strip()
                elif meta.startswith("Requirement:"):
                    entry.requirement = meta.split(":", 1)[1].strip()
                elif meta.startswith("Usage:"):
                    entry.usage = meta.split(":", 1)[1].strip()
                elif meta.strip() == "Content:":
                    i += 1
                    if i >= len(lines) or not lines[i].strip().startswith("```"):
                        raise ValueError(f"Production Asset Content for {entry.title} must use a fenced text block.")
                    i += 1
                    body: list[str] = []
                    while i < len(lines) and lines[i].strip() != "```":
                        body.append(lines[i].rstrip())
                        i += 1
                    if i >= len(lines):
                        raise ValueError(f"Unclosed Content block for Production Asset: {entry.title}")
                    entry.content = "\n".join(body).strip()
                i += 1

            entry.type_label = entry.type_label or _default_type(entry.category)
            entry.create_text = entry.create_text or _default_create(entry)
            entry.used = entry.used or entry.usage or entry.flow or "This gameplay section."
            entry.moment = entry.moment or _plain_flow(entry.flow) or "Gameplay Use"
            if entry.flow and current_section.flow_order and entry.flow not in current_section.flow_order:
                raise ValueError(
                    f"Production Asset Flow does not match a defined Gameplay Flow: {current_section.title} / {entry.title} / {entry.flow}"
                )
            current_section.categories[current_category].append(entry)
            continue

        i += 1

    if not sections:
        raise ValueError("Production Asset requirements contain no sections.")
    total = sum(len(entries) for section in sections for entries in section.categories.values())
    if not total:
        raise ValueError("Production Asset requirements contain no asset entries.")
    return AssetRequirements(sections)


def _presentation(render_data: dict[str, Any], section_title: str) -> SectionPresentation:
    title = voice._plain_section_title(section_title)
    key = voice._title_key(title)
    if key == voice._title_key(SHARED_SECTION):
        return SectionPresentation(
            SHARED_SECTION,
            bi("Shared", "Shared"),
            bi("Reusable production assets used across multiple gameplay sections.", "Asset produksi reusable untuk beberapa bagian gameplay."),
            bi("Keep shared production setups reusable.", "Jaga setup produksi bersama tetap reusable."),
            bi("Shared assets can be reused wherever referenced.", "Asset bersama dapat digunakan ulang di semua referensi."),
            "production-assets-global-shared",
        )

    for index, package in enumerate(render_data.get("packages", [])):
        if voice._title_key(txt(package.get("title", ""))["en"]) == key:
            package_id = str(package.get("id") or slug(title))
            gameplay = package.get("gameplay", {})
            return SectionPresentation(
                title,
                package.get("package_label", f"Gameplay {index + 1}"),
                gameplay.get("context", ""),
                gameplay.get("main_objective", ""),
                gameplay.get("end_condition", "") or gameplay.get("result", ""),
                f"production-assets-{slug(package_id)}",
            )

    journey = render_data.get("overview", {}).get("journey", [])
    flow_pages = render_data.get("gameplay_flow", [])
    for index, item in enumerate(journey):
        if voice._title_key(txt(item.get("title", ""))["en"]) == key:
            label = "Introduction" if index == 0 else "Ending" if index == len(journey) - 1 else "Journey"
            matching_flow = next(
                (flow for flow in flow_pages if voice._title_key(txt(flow.get("title", ""))["en"]) == key),
                {},
            )
            return SectionPresentation(
                title,
                bi(label, label),
                item.get("description", ""),
                item.get("description", ""),
                matching_flow.get("next_destination", ""),
                f"production-assets-journey-{slug(title)}",
            )

    raise ValueError(f"Production Asset section does not match an accepted PRD gameplay/journey section: {section_title}")


def _ordered_titles(
    render_data: dict[str, Any],
    assets: AssetRequirements | None,
    voice_doc: voice.VoiceProduction | None,
) -> list[str]:
    asset_map = {voice._title_key(section.title): section.title for section in (assets.sections if assets else [])}
    voice_map = {voice._title_key(section.title): section.title for section in (voice_doc.sections if voice_doc else [])}
    source_keys = set(asset_map) | set(voice_map)
    ordered: list[str] = []
    seen: set[str] = set()

    shared_key = voice._title_key(SHARED_SECTION)
    if shared_key in asset_map:
        ordered.append(asset_map[shared_key])
        source_keys.discard(shared_key)

    for item in render_data.get("overview", {}).get("journey", []):
        key = voice._title_key(txt(item.get("title", ""))["en"])
        if key in source_keys and key not in seen:
            ordered.append(asset_map.get(key) or voice_map[key])
            seen.add(key)

    for package in render_data.get("packages", []):
        key = voice._title_key(txt(package.get("title", ""))["en"])
        if key in source_keys and key not in seen:
            ordered.append(asset_map.get(key) or voice_map[key])
            seen.add(key)

    unresolved = sorted(source_keys - seen)
    if unresolved:
        names = [asset_map.get(key) or voice_map.get(key) or key for key in unresolved]
        raise ValueError("Production Assets contain section(s) that do not map to accepted PRD order: " + ", ".join(names))
    return ordered


def _asset_entries(section: AssetSection | None) -> list[AssetEntry]:
    if section is None:
        return []
    return [entry for category in ASSET_CATEGORIES for entry in section.categories.get(category, [])]


def _voice_requirement_meta(path: Path, label: str) -> dict[str, str]:
    if not path.is_file():
        return {}
    values: dict[str, str] = {}
    current_id: str | None = None
    prefix = f"- {label}:"
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        match = voice.ENTRY_RE.match(line)
        if match:
            current_id = match.group(1)
            continue
        if current_id and line.startswith(prefix):
            value = line.split(":", 1)[1].strip()
            if value:
                values[current_id] = value
    return values


def _flow_order(section: AssetSection | None, flow: str) -> int:
    if not flow:
        return 999
    if section and flow in section.flow_order:
        return section.flow_order[flow]
    match = re.match(r"^\s*(\d+)", flow)
    return int(match.group(1)) if match else 999


def _copy_button(target_id: str, label: str) -> str:
    return (
        f'<button class="pa-copy-button" data-pa-copy="{esc(target_id)}" type="button">'
        f'<span class="pa-copy-label">{esc(label)}</span></button>'
    )


def _asset_to_item(entry: AssetEntry, section: AssetSection | None, page_id: str) -> ProductionItem:
    return ProductionItem(
        item_id=f"{page_id}-build-{slug(entry.title)}",
        title=entry.title,
        type_label=entry.type_label,
        create_text=entry.create_text,
        used=entry.used,
        includes=entry.includes,
        moment=entry.moment,
        flow=entry.flow,
        flow_order=_flow_order(section, entry.flow),
        sort_order=entry.order,
        content=entry.content,
    )


def _voice_to_item(
    entry: voice.VoiceEntry,
    doc: voice.VoiceProduction,
    section: AssetSection | None,
    page_id: str,
    flow: str,
    used: str,
    moment: str,
    create_text: str,
    order: int,
) -> ProductionItem:
    return ProductionItem(
        item_id=f"{page_id}-build-{slug(entry.voice_id)}",
        title=f"{entry.speaker} — {entry.title}",
        type_label="VOICE",
        create_text=create_text or f"Create one {entry.speaker} dialogue line for this gameplay moment.",
        used=used or _plain_flow(flow) or "This gameplay section.",
        includes="",
        moment=moment or _plain_flow(flow) or "Gameplay Use",
        flow=flow,
        flow_order=_flow_order(section, flow),
        sort_order=order,
        content=entry.performance,
        speaker=entry.speaker,
        selected_voice=voice._voice_for(doc.cast, entry.speaker),
        duration=entry.duration,
        is_voice=True,
    )


def _item_sort_key(item: ProductionItem) -> tuple[int, int, int, str]:
    return (
        TYPE_PRIORITY.get(item.type_label.upper(), 500),
        item.flow_order,
        item.sort_order,
        item.title.casefold(),
    )


def _moment_sort_key(moment: str, items: list[ProductionItem]) -> tuple[int, int, str]:
    lowered = moment.casefold()
    if "throughout" in lowered:
        return (0, 0, lowered)
    return (1, min((item.flow_order for item in items), default=999), lowered)


def _build_item_html(item: ProductionItem) -> str:
    exact = ""
    if item.content:
        copy_id = f"{item.item_id}-copy"
        label = "Copy Prompt" if item.is_voice else "Copy Text"
        heading = "Prompt" if item.is_voice else "Player Text"
        exact = (
            '<div class="pa-exact">'
            '<div class="pa-exact-head">'
            f'<span>{esc(heading)}</span>{_copy_button(copy_id, label)}'
            '</div>'
            f'<pre class="{"voice-script-text" if item.is_voice else "pa-content"}" id="{esc(copy_id if not item.is_voice else "voice-prompt-" + item.item_id.split("-build-")[-1])}">{esc(item.content)}</pre>'
            '</div>'
        )
        if item.is_voice:
            # Voice validator requires canonical prompt IDs based on Voice ID. Replace the generic id above.
            voice_slug = item.item_id.split("-build-")[-1]
            exact = exact.replace(f'data-pa-copy="{esc(copy_id)}"', f'data-pa-copy="voice-prompt-{voice_slug}"')

    rows = [
        ('Create', item.create_text),
        ('Used', item.used),
    ]
    if item.includes:
        rows.append(('Includes', item.includes))
    if item.is_voice:
        rows.append(('Voice', f"{item.selected_voice} · {item.duration}"))
    meta = ''.join(
        f'<div class="pa-build-meta-row"><b>{esc(label)}</b><span>{esc(value)}</span></div>'
        for label, value in rows if value
    )
    classes = "pa-build-row pa-row pa-row-voice" if item.is_voice else "pa-build-row pa-row"
    return (
        f'<article class="{classes}" id="{esc(item.item_id)}">'
        '<div class="pa-build-head">'
        f'<span class="pa-type">{esc(item.type_label)}</span>'
        f'<h4>{esc(item.title)}</h4>'
        '</div>'
        f'<div class="pa-build-meta">{meta}</div>'
        f'{exact}'
        '</article>'
    )


def _usage_map_html(items: list[ProductionItem], page_id: str) -> str:
    grouped: dict[str, list[ProductionItem]] = {}
    for item in items:
        grouped.setdefault(item.moment, []).append(item)
    moments = sorted(grouped, key=lambda moment: _moment_sort_key(moment, grouped[moment]))
    blocks: list[str] = []
    for index, moment in enumerate(moments, 1):
        links = []
        for item in sorted(grouped[moment], key=_item_sort_key):
            links.append(
                f'<a class="pa-use-item" href="#{esc(item.item_id)}">'
                f'<span class="pa-use-type">{esc(item.type_label)}</span>'
                f'<span>{esc(item.title)}</span></a>'
            )
        blocks.append(
            '<div class="pa-moment">'
            f'<span class="pa-moment-index">{index:02d}</span>'
            '<div class="pa-moment-body">'
            f'<h4>{esc(moment)}</h4>'
            f'<div class="pa-use-items">{"".join(links)}</div>'
            '</div></div>'
        )
    return ''.join(blocks)


def _pages_and_nav(
    render_data: dict[str, Any],
    assets: AssetRequirements | None,
    voice_doc: voice.VoiceProduction | None,
    requirements_path: Path,
) -> tuple[str, str]:
    asset_map = {voice._title_key(section.title): section for section in (assets.sections if assets else [])}
    voice_map = {voice._title_key(section.title): section for section in (voice_doc.sections if voice_doc else [])}
    voice_flows = _voice_requirement_meta(requirements_path, "Flow")
    voice_used = _voice_requirement_meta(requirements_path, "Used")
    voice_moments = _voice_requirement_meta(requirements_path, "Moment")
    voice_create = _voice_requirement_meta(requirements_path, "Create")

    brand = render_data["document"].get("brand") or render_data["document"]["title"]
    pages: list[str] = []
    links: list[str] = []

    for title in _ordered_titles(render_data, assets, voice_doc):
        key = voice._title_key(title)
        asset_section = asset_map.get(key)
        voice_section = voice_map.get(key)
        meta = _presentation(render_data, title)

        items: list[ProductionItem] = [
            _asset_to_item(entry, asset_section, meta.page_id)
            for entry in _asset_entries(asset_section)
        ]
        if voice_section and voice_doc:
            for order, entry in enumerate(voice_section.entries, 1):
                flow = voice_flows.get(entry.voice_id, "")
                items.append(
                    _voice_to_item(
                        entry,
                        voice_doc,
                        asset_section,
                        meta.page_id,
                        flow,
                        voice_used.get(entry.voice_id, ""),
                        voice_moments.get(entry.voice_id, ""),
                        voice_create.get(entry.voice_id, ""),
                        order,
                    )
                )
        if not items:
            continue

        body = (
            '<header class="pa-shell">'
            '<small>Production Assets</small>'
            f'<h2>{esc(meta.title)}</h2><strong>{i18n(meta.package_label)}</strong>'
            '<p class="pa-section-note">Concrete Minecraft production deliverables. Gameplay behavior and logic stay in 03 Development.</p>'
            '</header>'
            '<nav class="pa-page-jump" aria-label="Production Assets sections">'
            f'<a href="#{esc(meta.page_id)}-what">What to Build</a>'
            f'<a href="#{esc(meta.page_id)}-where">Where It Is Used</a>'
            '</nav>'
            f'<section class="pa-part" id="{esc(meta.page_id)}-what">'
            '<div class="pa-part-head"><small>01</small><h3>What to Build</h3>'
            '<p>Only concrete production setups and exact in-game content.</p></div>'
            '<div class="pa-build-list">'
            + ''.join(_build_item_html(item) for item in sorted(items, key=_item_sort_key))
            + '</div></section>'
            f'<section class="pa-part pa-where" id="{esc(meta.page_id)}-where">'
            '<div class="pa-part-head"><small>02</small><h3>Where It Is Used</h3>'
            '<p>Gameplay moments that actually require the production items above.</p></div>'
            '<div class="pa-moments">'
            + _usage_map_html(items, meta.page_id)
            + '</div></section>'
        )

        index = len(pages)
        pid = meta.page_id
        pages.append(
            page(
                pid,
                f"PA-{index + 1:02d}",
                bi("Production Assets", "Aset Produksi"),
                body,
                context=meta.title,
                header=bi("Production Assets", "Aset Produksi"),
                footer_title=bi("Production Assets", "Aset Produksi"),
                brand=brand,
                role="production-assets",
                classes="sheet professional-only production-assets-page",
            )
        )
        links.append(
            f'<a data-target="{pid}" href="#{pid}">'
            f'<span class="production-assets-objective-name">{esc(meta.title)}</span>'
            f'<small>{i18n(meta.package_label)}</small></a>'
        )

    if not pages:
        raise ValueError("Production Assets contain no renderable accepted sections.")

    nav = (
        '<div class="nav-group is-open professional-nav production-assets-nav">'
        '<button aria-expanded="true" class="nav-group-toggle" type="button">'
        '<span class="nav-index" data-full-index="04" data-overview-index="">04</span>'
        f'<span class="nav-copy">{i18n(bi("Production Assets", "Aset Produksi"))}</span>'
        '<span aria-hidden="true" class="group-chevron"></span></button>'
        '<div class="nav-submenu">' + ''.join(links) + '</div></div>'
    )
    return ''.join(pages), nav


OBJECTIVE_STYLE = r'''<style id="production-assets-objective-style">
.pa-shell{margin:0 0 12px}.pa-shell>small{display:block;margin-bottom:5px;color:var(--blue);font-size:.61rem;font-weight:850;letter-spacing:.09em;text-transform:uppercase}.pa-shell h2{margin:0;color:var(--navy);font-size:1.9rem;line-height:1.12;letter-spacing:-.025em}.pa-shell>strong{display:block;margin:5px 0 7px;color:var(--amber);font-size:.68rem;letter-spacing:.06em;text-transform:uppercase}.pa-section-note{max-width:82ch;margin:0;color:var(--muted);font-size:.72rem;line-height:1.45}
.pa-page-jump{display:flex;gap:6px;flex-wrap:wrap;margin:13px 0 18px}.pa-page-jump a{padding:6px 9px;border:1px solid var(--line);border-radius:3px;color:var(--navy);font-size:.64rem;font-weight:800;text-decoration:none;background:var(--paper)}.pa-page-jump a:hover,.pa-page-jump a:focus-visible{border-color:var(--blue);color:var(--blue);outline:0}
.pa-part{scroll-margin-top:74px}.pa-part+.pa-part{margin-top:26px;padding-top:22px;border-top:2px solid var(--line)}.pa-part-head{margin-bottom:10px}.pa-part-head small{display:block;color:var(--amber);font-size:.56rem;font-weight:900;letter-spacing:.08em}.pa-part-head h3{margin:1px 0 3px;color:var(--navy);font-size:1.14rem;line-height:1.25;text-transform:uppercase;letter-spacing:.025em}.pa-part-head p{margin:0;color:var(--muted);font-size:.7rem;line-height:1.4}
.pa-build-list{border-top:1px solid #cbd7dd}.pa-build-row{padding:12px 7px 13px;border-bottom:1px solid #cbd7dd;background:var(--paper);scroll-margin-top:74px}.pa-build-head{display:grid;grid-template-columns:126px minmax(0,1fr);gap:12px;align-items:center}.pa-type{display:inline-flex;width:max-content;max-width:120px;align-items:center;padding:4px 7px;border-radius:3px;background:var(--soft);color:var(--blue);font-size:.58rem;font-weight:900;letter-spacing:.05em;line-height:1.25;text-transform:uppercase}.pa-build-head h4{margin:0;color:var(--navy);font-size:.88rem;line-height:1.3;text-transform:none}.pa-build-meta{margin:8px 0 0 138px}.pa-build-meta-row{display:grid;grid-template-columns:62px minmax(0,1fr);gap:8px;margin-top:4px;font-size:.71rem;line-height:1.42}.pa-build-meta-row:first-child{margin-top:0}.pa-build-meta-row b{color:var(--blue);font-size:.57rem;letter-spacing:.055em;text-transform:uppercase}.pa-build-meta-row span{color:#52616a}
.pa-exact{margin:10px 0 0 138px}.pa-exact-head{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:5px}.pa-exact-head>span{color:var(--blue);font-size:.58rem;font-weight:900;letter-spacing:.06em;text-transform:uppercase}.pa-copy-button{display:inline-flex;align-items:center;justify-content:center;min-height:27px;padding:6px 8px;border:1px solid var(--navy);border-radius:3px;background:var(--navy);color:#fff;font:800 .56rem/1 var(--font);letter-spacing:.04em;text-transform:uppercase;cursor:pointer}.pa-copy-button:hover,.pa-copy-button:focus-visible{background:var(--blue);border-color:var(--blue);outline:0}.pa-copy-button.is-copied{background:var(--green);border-color:var(--green)}.pa-content,.pa-build-row .voice-script-text{display:block!important;margin:0;padding:10px 12px;border:1px solid var(--line);border-left:3px solid var(--blue);border-radius:3px;background:#f8fafb;color:var(--navy);font:700 .75rem/1.5 var(--font);white-space:pre-wrap;overflow-wrap:anywhere}.pa-build-row .voice-script-text{border-left-color:var(--amber)}
.pa-moments{border-top:1px solid #cbd7dd}.pa-moment{display:grid;grid-template-columns:42px minmax(0,1fr);gap:12px;padding:12px 7px;border-bottom:1px solid #cbd7dd}.pa-moment-index{display:flex;align-items:flex-start;justify-content:center;padding-top:2px;color:var(--amber);font-size:.61rem;font-weight:900}.pa-moment-body h4{margin:0 0 7px;color:var(--navy);font-size:.86rem;line-height:1.3;text-transform:uppercase;letter-spacing:.02em}.pa-use-items{display:grid;gap:5px}.pa-use-item{display:grid;grid-template-columns:118px minmax(0,1fr);gap:9px;align-items:center;color:var(--navy);font-size:.7rem;text-decoration:none}.pa-use-item:hover,.pa-use-item:focus-visible{color:var(--blue);outline:0}.pa-use-type{display:inline-flex;width:max-content;max-width:112px;padding:3px 6px;border-radius:2px;background:var(--soft);color:var(--blue);font-size:.54rem;font-weight:850;letter-spacing:.045em;text-transform:uppercase}
body.theme-dark .pa-section-note,body.theme-dark .pa-part-head p,body.theme-dark .pa-build-meta-row span{color:#c8d7dc}body.theme-dark .pa-build-row,body.theme-dark .pa-page-jump a{background:#17262d}body.theme-dark .pa-type,body.theme-dark .pa-use-type{background:#1d2f37}body.theme-dark .pa-content,body.theme-dark .pa-build-row .voice-script-text{background:#1d2f37;color:#e8eff3}
@media(max-width:760px){.pa-build-head{grid-template-columns:1fr}.pa-build-meta,.pa-exact{margin-left:0}.pa-use-item{grid-template-columns:1fr}.pa-moment{grid-template-columns:32px 1fr}}
@media print{.pa-page-jump,.pa-copy-button{display:none!important}.pa-build-row,.pa-moment{break-inside:avoid}}
</style>'''

OBJECTIVE_COPY_SCRIPT = r'''<script id="production-assets-flow-copy-script">(function(){
  function fallbackCopy(text){var area=document.createElement('textarea');area.value=text;area.setAttribute('readonly','');area.style.position='fixed';area.style.opacity='0';document.body.appendChild(area);area.select();try{document.execCommand('copy');}finally{document.body.removeChild(area);}}
  document.addEventListener('click',function(event){var button=event.target.closest('[data-pa-copy]');if(!button)return;var source=document.getElementById(button.getAttribute('data-pa-copy'));if(!source)return;var text=source.textContent||'';var label=button.querySelector('.pa-copy-label');var original=label?label.textContent:'Copy';var done=function(){button.classList.add('is-copied');if(label)label.textContent='Copied ✓';setTimeout(function(){button.classList.remove('is-copied');if(label)label.textContent=original;},1400);};if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(done,function(){fallbackCopy(text);done();});}else{fallbackCopy(text);done();}});
})();</script>'''


def _insert(source: str, closing: str, addition: str, label: str) -> str:
    if source.count(closing) != 1:
        raise ValueError(f"Rendered HTML requires exactly one {label} closing marker.")
    return source.replace(closing, addition + "\n" + closing, 1)


def augment_project_html(render_data_path: Path, output: Path, voice_production_path: Path) -> None:
    asset_path = voice_production_path.parent / "asset-requirements.md"
    has_assets = asset_path.is_file()
    has_voice = voice_production_path.is_file()
    if not has_assets and not has_voice:
        return

    render_data = json.loads(render_data_path.read_text(encoding="utf-8"))
    assets = parse_asset_requirements(asset_path) if has_assets else None
    voice_doc = voice.parse_voice_production(voice_production_path) if has_voice else None
    requirements_path = voice_production_path.parent / "voice-requirements.md"
    source = output.read_text(encoding="utf-8")

    if voice.STYLE_MARKER in source or OBJECTIVE_STYLE_MARKER in source:
        raise ValueError("Production Assets extension already exists in rendered HTML.")

    pages, nav = _pages_and_nav(render_data, assets, voice_doc, requirements_path)
    nav_pattern = re.compile(r'(<nav class="sidebar-nav">)(.*?)(</nav>)', re.S)
    main_pattern = re.compile(r'(<main class="document-main">.*?)(</main>)', re.S)
    if len(nav_pattern.findall(source)) != 1:
        raise ValueError("Rendered HTML requires exactly one sidebar navigation container.")
    if len(main_pattern.findall(source)) != 1:
        raise ValueError("Rendered HTML requires exactly one document main container.")

    source = nav_pattern.sub(lambda match: match.group(1) + match.group(2) + nav + match.group(3), source, count=1)
    source = main_pattern.sub(lambda match: match.group(1) + pages + match.group(2), source, count=1)
    head_additions = voice.VOICE_STYLE + OBJECTIVE_STYLE
    if has_assets:
        asset_sha = hashlib.sha256(asset_path.read_bytes()).hexdigest()
        head_additions += f'\n<meta content="{asset_sha}" name="asset-requirements-sha256"/>'
    source = _insert(source, "</head>", head_additions, "head")

    body_additions = OBJECTIVE_COPY_SCRIPT
    if has_voice:
        body_additions += "\n" + voice.VOICE_COPY_SCRIPT
    source = _insert(source, "</body>", body_additions, "body")

    section_ids = set(re.findall(r'<section\b[^>]*\bid="([^"]+)"', source))
    targets = set(re.findall(r'data-target="([^"]+)"', nav))
    missing = sorted(targets - section_ids)
    if missing:
        raise ValueError(f"Production Assets navigation targets missing from generated pages: {missing}")

    output.write_text(source, encoding="utf-8")
