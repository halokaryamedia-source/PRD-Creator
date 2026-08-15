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


@dataclass
class AssetEntry:
    title: str
    category: str = ""
    flow: str = ""
    requirement: str = ""
    usage: str = ""
    content: str = ""


@dataclass
class FlowDefinition:
    title: str
    trigger: str = ""
    experience: str = ""
    uses: list[str] = field(default_factory=list)
    done_when: list[str] = field(default_factory=list)


@dataclass
class AssetSection:
    title: str
    categories: dict[str, list[AssetEntry]] = field(default_factory=dict)
    flows: dict[str, FlowDefinition] = field(default_factory=dict)


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


def parse_asset_requirements(path: Path) -> AssetRequirements:
    text = path.read_text(encoding="utf-8")
    if voice.PLACEHOLDER_RE.search(text):
        raise ValueError("Production Asset requirements contain an unresolved placeholder.")

    sections: list[AssetSection] = []
    current_section: AssetSection | None = None
    current_category: str | None = None
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
            i += 1
            continue

        if line.startswith("### Gameplay Flow "):
            if current_section is None:
                raise ValueError("Gameplay Flow metadata appears before a Production Asset section.")
            flow_title = line[len("### Gameplay Flow "):].strip()
            if not flow_title:
                raise ValueError("Gameplay Flow title cannot be empty.")
            flow = FlowDefinition(flow_title)
            i += 1
            list_mode: str | None = None
            while i < len(lines):
                meta = lines[i].rstrip()
                if meta.startswith(("## ", "### ", "#### ")):
                    break
                if meta.startswith("Trigger:"):
                    flow.trigger = meta.split(":", 1)[1].strip()
                    list_mode = None
                elif meta.startswith("Player Experience:"):
                    flow.experience = meta.split(":", 1)[1].strip()
                    list_mode = None
                elif meta.startswith("Uses:"):
                    raw = meta.split(":", 1)[1].strip()
                    flow.uses = [item.strip() for item in raw.split(";") if item.strip()]
                    list_mode = None
                elif meta.strip() == "Done When:":
                    list_mode = "done"
                elif list_mode == "done" and re.match(r"^\s*-\s+", meta):
                    flow.done_when.append(re.sub(r"^\s*-\s+", "", meta).strip())
                i += 1
            if not flow.trigger:
                raise ValueError(f"Gameplay Flow is missing Trigger: {current_section.title} / {flow_title}")
            if not flow.experience:
                raise ValueError(f"Gameplay Flow is missing Player Experience: {current_section.title} / {flow_title}")
            if not flow.done_when:
                raise ValueError(f"Gameplay Flow is missing Done When: {current_section.title} / {flow_title}")
            if flow_title in current_section.flows:
                raise ValueError(f"Duplicate Gameplay Flow in {current_section.title}: {flow_title}")
            current_section.flows[flow_title] = flow
            current_category = None
            continue

        if line.startswith("### "):
            if current_section is None:
                raise ValueError("Production Asset category appears before a section.")
            category = line[4:].strip()
            if category not in ASSET_CATEGORIES:
                raise ValueError(
                    f"Unsupported Production Asset category: {category}. "
                    f"Use one of: {', '.join(ASSET_CATEGORIES)}"
                )
            if category in current_section.categories:
                raise ValueError(
                    f"Duplicate Production Asset category in {current_section.title}: {category}"
                )
            current_section.categories[category] = []
            current_category = category
            i += 1
            continue

        if line.startswith("#### "):
            if current_section is None or current_category is None:
                raise ValueError("Production Asset entry appears before its section/category.")
            entry = AssetEntry(title=line[5:].strip(), category=current_category)
            if not entry.title:
                raise ValueError("Production Asset name cannot be empty.")

            i += 1
            while i < len(lines):
                meta = lines[i].rstrip()
                if meta.startswith(("## ", "### ", "#### ")):
                    break
                if meta.startswith("Flow:"):
                    entry.flow = meta.split(":", 1)[1].strip()
                elif meta.startswith("Requirement:"):
                    entry.requirement = meta.split(":", 1)[1].strip()
                elif meta.startswith("Usage:"):
                    entry.usage = meta.split(":", 1)[1].strip()
                elif meta.strip() == "Content:":
                    i += 1
                    if i >= len(lines) or not lines[i].strip().startswith("```"):
                        raise ValueError(
                            f"Production Asset Content for {entry.title} must use a fenced text block."
                        )
                    i += 1
                    body: list[str] = []
                    while i < len(lines) and lines[i].strip() != "```":
                        body.append(lines[i].rstrip())
                        i += 1
                    if i >= len(lines):
                        raise ValueError(f"Unclosed Content block for Production Asset: {entry.title}")
                    entry.content = "\n".join(body).strip()
                i += 1

            if not entry.flow:
                raise ValueError(f"Production Asset is missing Flow: {entry.title}")
            if not entry.requirement:
                raise ValueError(f"Production Asset is missing Requirement: {entry.title}")
            current_section.categories[current_category].append(entry)
            continue

        i += 1

    if not sections:
        raise ValueError("Production Asset requirements contain no sections.")

    seen: set[str] = set()
    total = 0
    for section in sections:
        key = voice._title_key(section.title)
        if key in seen:
            raise ValueError(f"Duplicate Production Asset section: {section.title}")
        seen.add(key)
        if not section.flows:
            raise ValueError(f"Production Asset section has no Gameplay Flow definitions: {section.title}")
        empty = [name for name, entries in section.categories.items() if not entries]
        if empty:
            raise ValueError(
                f"Production Asset section {section.title} contains empty categories: "
                + ", ".join(empty)
            )
        entries = [
            entry
            for category in ASSET_CATEGORIES
            for entry in section.categories.get(category, [])
        ]
        for entry in entries:
            if entry.flow not in section.flows:
                raise ValueError(
                    f"Production Asset Flow does not match a defined Gameplay Flow: "
                    f"{section.title} / {entry.title} / {entry.flow}"
                )
        total += len(entries)

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
            bi(
                "Reusable character and presentation assets referenced by multiple gameplay flows.",
                "Asset karakter dan presentasi reusable yang dipakai oleh beberapa flow gameplay.",
            ),
            bi(
                "Keep recurring character assets consistent and reusable across the journey.",
                "Jaga asset karakter berulang tetap konsisten dan reusable sepanjang perjalanan.",
            ),
            bi(
                "Every referenced gameplay flow can use the approved states without duplicating the asset.",
                "Setiap flow terkait dapat memakai state yang disetujui tanpa menduplikasi asset.",
            ),
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
                (
                    flow
                    for flow in flow_pages
                    if voice._title_key(txt(flow.get("title", ""))["en"]) == key
                ),
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

    raise ValueError(
        f"Production Asset section does not match an accepted PRD gameplay/journey section: {section_title}"
    )


def _ordered_titles(
    render_data: dict[str, Any],
    assets: AssetRequirements | None,
    voice_doc: voice.VoiceProduction | None,
) -> list[str]:
    asset_map = {
        voice._title_key(section.title): section.title
        for section in (assets.sections if assets else [])
    }
    voice_map = {
        voice._title_key(section.title): section.title
        for section in (voice_doc.sections if voice_doc else [])
    }
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
        raise ValueError(
            "Production Assets contain section(s) that do not map to accepted PRD order: "
            + ", ".join(names)
        )
    return ordered


def _asset_entries(section: AssetSection | None) -> list[AssetEntry]:
    if section is None:
        return []
    return [
        entry
        for category in ASSET_CATEGORIES
        for entry in section.categories.get(category, [])
    ]


def _flow_sort_key(label: str) -> tuple[int, str]:
    match = re.match(r"^\s*(\d+)", label)
    return (int(match.group(1)) if match else 9999, label.casefold())


def _copy_button(target_id: str, label: str) -> str:
    return (
        f'<button class="pa-copy-button" data-pa-copy="{esc(target_id)}" type="button">'
        f'<span class="pa-copy-label">{esc(label)}</span></button>'
    )


def _purpose_text(requirement: str) -> str:
    text = requirement.strip()
    text = re.sub(
        r"^(?:Create|Produce|Give|Build|Implement)\s+(?:or reuse\s+)?(?:one\s+)?",
        "",
        text,
        flags=re.I,
    )
    if text:
        text = text[0].upper() + text[1:]
    return text


def _asset_html(entry: AssetEntry, page_id: str) -> str:
    copy_id = f"{page_id}-asset-copy-{slug(entry.title)}"
    usage = (
        '<div class="pa-asset-row">'
        f'<span>{i18n(bi("Use / Trigger", "Penggunaan / Trigger"))}</span>'
        f'<p>{esc(entry.usage)}</p></div>'
        if entry.usage
        else ""
    )
    content = ""
    if entry.content:
        copy_label = "Player Text" if entry.category == "UI & Information" else "Copy-ready Text"
        content = (
            '<div class="pa-copy-block">'
            '<div class="pa-copy-head">'
            f'<span>{esc(copy_label)}</span>'
            f'{_copy_button(copy_id, "Copy Text")}</div>'
            f'<pre class="pa-content" id="{copy_id}">{esc(entry.content)}</pre>'
            '</div>'
        )
    return (
        '<article class="pa-asset-card">'
        '<div class="pa-asset-head">'
        f'<span class="pa-type-badge">{esc(entry.category)}</span>'
        f'<h4>{esc(entry.title)}</h4></div>'
        '<div class="pa-asset-body">'
        '<div class="pa-asset-row">'
        f'<span>{i18n(bi("Purpose", "Fungsi"))}</span>'
        f'<p>{esc(_purpose_text(entry.requirement))}</p></div>'
        f'{usage}{content}</div></article>'
    )


def _checklist_html(
    assets: list[AssetEntry],
    voices: list[voice.VoiceEntry],
    triggers: dict[str, str],
) -> str:
    items: list[str] = []
    for entry in assets:
        items.append(
            '<li><span class="pa-check">□</span><div>'
            f'<strong>{esc(entry.title)}</strong>'
            f'<small>{esc(entry.category)}</small>'
            f'<p>{esc(_purpose_text(entry.requirement))}</p></div></li>'
        )
    for entry in voices:
        trigger = triggers.get(entry.voice_id, "")
        items.append(
            '<li><span class="pa-check">□</span><div>'
            f'<strong>{esc(entry.title)}</strong>'
            f'<small>Voice · {esc(entry.speaker)}</small>'
            f'<p>{esc(trigger)}</p></div></li>'
        )
    if not items:
        return ""
    return (
        '<div class="pa-checklist"><h4>Implementation Checklist</h4>'
        '<ul>' + "".join(items) + '</ul></div>'
    )


def _done_html(items: list[str]) -> str:
    return (
        '<div class="pa-done"><h4>Done When</h4><ul>'
        + "".join(f'<li><span>✓</span>{esc(item)}</li>' for item in items)
        + '</ul></div>'
    )


def _pages_and_nav(
    render_data: dict[str, Any],
    assets: AssetRequirements | None,
    voice_doc: voice.VoiceProduction | None,
    triggers: dict[str, str],
    voice_flows: dict[str, str],
) -> tuple[str, str]:
    asset_map = {
        voice._title_key(section.title): section
        for section in (assets.sections if assets else [])
    }
    voice_map = {
        voice._title_key(section.title): section
        for section in (voice_doc.sections if voice_doc else [])
    }
    brand = render_data["document"].get("brand") or render_data["document"]["title"]
    pages: list[str] = []
    links: list[str] = []
    voice_number = 1

    for title in _ordered_titles(render_data, assets, voice_doc):
        key = voice._title_key(title)
        asset_section = asset_map.get(key)
        voice_section = voice_map.get(key)
        asset_entries = _asset_entries(asset_section)
        voice_entries = list(voice_section.entries) if voice_section else []
        if not asset_entries and not voice_entries:
            continue

        meta = _presentation(render_data, title)
        context = meta.context or bi(
            "Production requirements follow the accepted PRD.",
            "Requirement produksi mengikuti PRD yang diterima.",
        )

        grouped_assets: dict[str, list[AssetEntry]] = {}
        for entry in asset_entries:
            grouped_assets.setdefault(entry.flow, []).append(entry)

        grouped_voices: dict[str, list[voice.VoiceEntry]] = {}
        for entry in voice_entries:
            flow = voice_flows.get(entry.voice_id)
            if not flow:
                raise ValueError(f"Voice requirement Flow missing for canonical production entry: {entry.voice_id}")
            grouped_voices.setdefault(flow, []).append(entry)

        flow_defs = dict(asset_section.flows) if asset_section else {}
        flow_titles = sorted(
            set(flow_defs) | set(grouped_assets) | set(grouped_voices),
            key=_flow_sort_key,
        )
        for flow_title in flow_titles:
            if flow_title not in flow_defs:
                raise ValueError(
                    f"Gameplay Flow metadata missing for Production Assets section: {title} / {flow_title}"
                )

        body = (
            f'<header class="pa-shell {"voice-objective-shell" if voice_section else ""}">'
            '<small>Production Assets</small>'
            f'<h2>{esc(meta.title)}</h2><strong>{i18n(meta.package_label)}</strong>'
            f'<p class="pa-context">{i18n(context)}</p>'
            '<div class="pa-overview">'
            '<article><span>Player Goal</span>'
            f'<p>{i18n(meta.goal)}</p></article>'
            '<article><span>Completion</span>'
            f'<p>{i18n(meta.completion)}</p></article>'
            '</div></header>'
        )

        if voice_section and voice_doc:
            body += (
                f'<div class="voice-production-block pa-voice-setup-block" '
                f'data-voice-section="{esc(voice._title_key(voice_section.title))}">'
                + voice._section_setup_html(voice_doc, voice_section)
                + '</div>'
            )

        body += '<nav class="pa-flow-nav" aria-label="Gameplay flow quick jump">'
        for flow_title in flow_titles:
            flow_id = f"{meta.page_id}-flow-{slug(flow_title)}"
            body += f'<a href="#{flow_id}">{esc(flow_title)}</a>'
        body += '</nav>'

        voice_positions = {
            entry.voice_id: (index, len(voice_entries))
            for index, entry in enumerate(voice_entries, 1)
        }

        for flow_title in flow_titles:
            flow = flow_defs[flow_title]
            flow_assets = grouped_assets.get(flow_title, [])
            flow_voices = grouped_voices.get(flow_title, [])
            flow_id = f"{meta.page_id}-flow-{slug(flow_title)}"
            body += (
                f'<div class="pa-flow" id="{flow_id}">'
                '<div class="pa-flow-head">'
                '<span>Gameplay Flow</span>'
                f'<h3>{esc(flow_title)}</h3></div>'
                '<div class="pa-flow-brief">'
                '<article><span>Trigger</span>'
                f'<p>{esc(flow.trigger)}</p></article>'
                '<article><span>Player Experience</span>'
                f'<p>{esc(flow.experience)}</p></article>'
                '</div>'
            )
            if flow.uses:
                body += (
                    '<div class="pa-uses"><span>Uses</span>'
                    + "".join(f'<b>{esc(item)}</b>' for item in flow.uses)
                    + '</div>'
                )
            body += _checklist_html(flow_assets, flow_voices, triggers)
            body += '<div class="pa-assets">'
            for entry in flow_assets:
                body += _asset_html(entry, meta.page_id)
            for entry in flow_voices:
                trigger = triggers.get(entry.voice_id)
                if not trigger:
                    raise ValueError(
                        f"Voice requirement Trigger missing for canonical production entry: {entry.voice_id}"
                    )
                line_index, line_total = voice_positions[entry.voice_id]
                body += (
                    '<div class="pa-voice-inline">'
                    '<span class="pa-type-badge">Voice</span>'
                    + voice._entry_html(
                        entry,
                        voice_number,
                        line_index,
                        line_total,
                        meta.package_label,
                        trigger,
                    )
                    + '</div>'
                )
                voice_number += 1
            body += '</div>' + _done_html(flow.done_when) + '</div>'

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
        '<div class="nav-submenu">' + "".join(links) + "</div></div>"
    )
    return "".join(pages), nav


OBJECTIVE_STYLE = r'''<style id="production-assets-objective-style">
.pa-shell{margin:0 0 16px}
.pa-shell>small{display:block;margin-bottom:7px;color:var(--blue);font-size:.63rem;font-weight:800;letter-spacing:.09em;text-transform:uppercase}
.pa-shell h2{margin:0;color:var(--navy);font-size:1.9rem;line-height:1.12;letter-spacing:-.025em}
.pa-shell>strong{display:block;margin:6px 0 9px;color:var(--amber);font-size:.7rem;letter-spacing:.06em;text-transform:uppercase}
.pa-context{max-width:82ch;margin:0 0 12px;color:#52616a;font-size:.79rem;line-height:1.48}
.pa-overview{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.pa-overview article{padding:12px 15px 12px 0}
.pa-overview article+article{padding-left:15px;border-left:1px solid var(--line)}
.pa-overview span,.pa-flow-brief span,.pa-uses>span{display:block;margin-bottom:4px;color:var(--blue);font-size:.58rem;font-weight:850;letter-spacing:.07em;text-transform:uppercase}
.pa-overview p,.pa-flow-brief p{margin:0;color:var(--ink);font-size:.78rem;line-height:1.48}
.pa-flow-nav{display:flex;gap:7px;flex-wrap:wrap;margin:15px 0 3px}
.pa-flow-nav a{display:inline-flex;align-items:center;min-height:30px;padding:6px 9px;border:1px solid var(--line);border-radius:3px;background:var(--paper);color:var(--navy);font-size:.67rem;font-weight:750;text-decoration:none}
.pa-flow-nav a:hover,.pa-flow-nav a:focus-visible{border-color:var(--blue);color:var(--blue);outline:0}
.pa-flow{scroll-margin-top:74px;margin-top:22px;padding-top:3px}
.pa-flow+.pa-flow{padding-top:24px;border-top:2px solid var(--line)}
.pa-flow-head{margin-bottom:10px}
.pa-flow-head>span{display:block;margin-bottom:3px;color:var(--amber);font-size:.6rem;font-weight:850;letter-spacing:.08em;text-transform:uppercase}
.pa-flow-head h3{margin:0;color:var(--navy);font-size:1.14rem;line-height:1.25;letter-spacing:0;text-transform:none}
.pa-flow-brief{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);margin-bottom:10px;border:1px solid var(--line);background:var(--soft)}
.pa-flow-brief article{padding:11px 13px}
.pa-flow-brief article+article{border-left:1px solid var(--line)}
.pa-uses{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin:8px 0 12px}
.pa-uses>span{margin:0 4px 0 0}
.pa-uses b{padding:3px 7px;border:1px solid var(--line);border-radius:999px;background:var(--paper);color:var(--navy);font-size:.62rem}
.pa-checklist{margin:10px 0 12px;padding:12px 14px;border-left:3px solid var(--navy);background:#f8fafb}
.pa-checklist h4,.pa-done h4{margin:0 0 8px;color:var(--navy);font-size:.7rem;letter-spacing:.06em;text-transform:uppercase}
.pa-checklist ul,.pa-done ul{margin:0;padding:0;list-style:none}
.pa-checklist li{display:grid;grid-template-columns:22px minmax(0,1fr);gap:8px;padding:7px 0;border-top:1px solid var(--line)}
.pa-checklist li:first-child{border-top:0;padding-top:0}
.pa-check{color:var(--blue);font-size:1rem;line-height:1.25}
.pa-checklist strong{display:inline;color:var(--navy);font-size:.78rem}
.pa-checklist small{margin-left:7px;color:var(--muted);font-size:.58rem;text-transform:uppercase}
.pa-checklist p{margin:2px 0 0;color:#52616a;font-size:.71rem;line-height:1.4}
.pa-assets{display:grid;gap:10px}
.pa-asset-card{padding:13px 14px;border:1px solid #d8e1e5;border-radius:4px;background:var(--paper);break-inside:avoid}
.pa-asset-head{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.pa-type-badge{display:inline-block;padding:2px 6px;border-radius:2px;background:var(--soft);color:var(--blue);font-size:.57rem;font-weight:850;letter-spacing:.06em;text-transform:uppercase}
.pa-asset-head h4{margin:0;color:var(--navy);font-size:.96rem;line-height:1.3;text-transform:none}
.pa-asset-body{margin-top:9px;border-top:1px solid var(--line)}
.pa-asset-row{display:grid;grid-template-columns:95px minmax(0,1fr);gap:13px;padding:9px 0;border-bottom:1px solid var(--line)}
.pa-asset-row>span{padding-top:1px;color:var(--muted);font-size:.57rem;font-weight:850;letter-spacing:.06em;text-transform:uppercase}
.pa-asset-row p{max-width:78ch;margin:0;color:var(--ink);font-size:.77rem;line-height:1.48}
.pa-copy-block{padding-top:10px}
.pa-copy-head{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:5px}
.pa-copy-head>span{color:var(--blue);font-size:.58rem;font-weight:850;letter-spacing:.06em;text-transform:uppercase}
.pa-content{margin:0;padding:12px 13px;border:1px solid var(--line);border-left:3px solid var(--blue);border-radius:2px;background:#f8fafb;color:var(--navy);font:700 .8rem/1.55 var(--font);white-space:pre-wrap;overflow-wrap:anywhere}
.pa-copy-button{display:inline-flex;align-items:center;justify-content:center;min-height:30px;padding:7px 9px;border:1px solid var(--navy);border-radius:3px;background:var(--navy);color:#fff;font:800 .6rem/1 var(--font);letter-spacing:.045em;text-transform:uppercase;cursor:pointer;white-space:nowrap}
.pa-copy-button:hover,.pa-copy-button:focus-visible{border-color:var(--blue);background:var(--blue);outline:0}
.pa-copy-button.is-copied{border-color:var(--green);background:var(--green)}
.pa-voice-setup-block{margin:11px 0 0}
.pa-voice-inline>.pa-type-badge{margin:0 0 5px 1px}
.pa-voice-inline .voice-script-card{margin:0}
.pa-done{margin-top:12px;padding:12px 14px;border-left:3px solid var(--green);background:#eef6f2}
.pa-done li{display:grid;grid-template-columns:18px minmax(0,1fr);gap:6px;margin-top:5px;color:#365b50;font-size:.73rem;line-height:1.42}
.pa-done li:first-child{margin-top:0}
.pa-done li span{color:var(--green);font-weight:900}
body.theme-dark .pa-context,body.theme-dark .pa-flow-brief p,body.theme-dark .pa-checklist p{color:#c8d7dc}
body.theme-dark .pa-flow-brief,body.theme-dark .pa-checklist,body.theme-dark .pa-type-badge{background:#1d2f37}
body.theme-dark .pa-asset-card{border-color:#405761;background:#17262d}
body.theme-dark .pa-content{background:#1d2f37;color:#e8eff3}
body.theme-dark .pa-done{background:#193029}
@media(max-width:760px){
.pa-overview,.pa-flow-brief{grid-template-columns:1fr}
.pa-overview article+article,.pa-flow-brief article+article{padding-left:0;border-left:0;border-top:1px solid var(--line)}
.pa-asset-row{grid-template-columns:1fr;gap:3px}
.pa-copy-head{align-items:flex-start}
}
@media print{
.pa-flow-nav,.pa-copy-button{display:none!important}
.pa-asset-card,.pa-flow,.pa-done,.pa-checklist{break-inside:avoid}
}
</style>'''

OBJECTIVE_COPY_SCRIPT = r'''<script id="production-assets-flow-copy-script">(function(){
  function fallbackCopy(text){
    var area=document.createElement('textarea');
    area.value=text;area.setAttribute('readonly','');area.style.position='fixed';area.style.opacity='0';
    document.body.appendChild(area);area.select();
    try{document.execCommand('copy');}finally{document.body.removeChild(area);}
  }
  document.addEventListener('click',function(event){
    var button=event.target.closest('[data-pa-copy]');if(!button)return;
    var source=document.getElementById(button.getAttribute('data-pa-copy'));if(!source)return;
    var text=source.textContent||'';
    var label=button.querySelector('.pa-copy-label');
    var original=label?label.textContent:'Copy';
    var done=function(){
      button.classList.add('is-copied');
      if(label)label.textContent='Copied ✓';else button.textContent='Copied ✓';
      setTimeout(function(){button.classList.remove('is-copied');if(label)label.textContent=original;else button.textContent=original;},1400);
    };
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(done,function(){fallbackCopy(text);done();});}
    else{fallbackCopy(text);done();}
  });
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
    triggers = voice.parse_voice_requirement_triggers(requirements_path) if has_voice else {}
    voice_flows = voice.parse_voice_requirement_flows(requirements_path) if has_voice else {}
    source = output.read_text(encoding="utf-8")

    if voice.STYLE_MARKER in source or OBJECTIVE_STYLE_MARKER in source:
        raise ValueError("Production Assets extension already exists in rendered HTML.")

    pages, nav = _pages_and_nav(render_data, assets, voice_doc, triggers, voice_flows)
    nav_pattern = re.compile(r'(<nav class="sidebar-nav">)(.*?)(</nav>)', re.S)
    main_pattern = re.compile(r'(<main class="document-main">.*?)(</main>)', re.S)
    if len(nav_pattern.findall(source)) != 1:
        raise ValueError("Rendered HTML requires exactly one sidebar navigation container.")
    if len(main_pattern.findall(source)) != 1:
        raise ValueError("Rendered HTML requires exactly one document main container.")

    source = nav_pattern.sub(
        lambda match: match.group(1) + match.group(2) + nav + match.group(3),
        source,
        count=1,
    )
    source = main_pattern.sub(
        lambda match: match.group(1) + pages + match.group(2),
        source,
        count=1,
    )
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
