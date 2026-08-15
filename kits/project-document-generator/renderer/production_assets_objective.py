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
    group: str = ""
    used: str = ""
    for_text: str = ""
    requirement: str = ""
    usage: str = ""
    content: str = ""


@dataclass
class FlowDefinition:
    title: str
    for_text: str = ""
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
                if meta.startswith("For:"):
                    flow.for_text = meta.split(":", 1)[1].strip()
                    list_mode = None
                elif meta.startswith("Trigger:"):
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
            if not flow.for_text:
                raise ValueError(f"Gameplay Flow is missing For: {current_section.title} / {flow_title}")
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
                elif meta.startswith("Group:"):
                    entry.group = meta.split(":", 1)[1].strip()
                elif meta.startswith("Used:"):
                    entry.used = meta.split(":", 1)[1].strip()
                elif meta.startswith("For:"):
                    entry.for_text = meta.split(":", 1)[1].strip()
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
            if not entry.group:
                entry.group = entry.flow
            if not entry.used:
                entry.used = entry.usage or entry.flow
            if not entry.for_text:
                raise ValueError(f"Production Asset is missing For: {entry.title}")
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


def _category_label(category: str, title: str = "") -> str:
    overrides = {
        "Custodian Vex": "MODEL / ANIMATION",
        "Gremlin": "MODEL / ANIMATION",
        "Wall Laser Sensor": "MODEL / VFX",
        "Laser Blocker Stone": "MODEL / ANIMATION",
        "Swinging Axe Trap": "MODEL / ANIMATION",
        "Floor Trap": "MODEL / PRESENTATION",
        "Power Generator": "MODEL / VFX",
        "90-Degree Rotator Junction": "MODEL / ANIMATION",
        "Orrery Ring": "MODEL / ANIMATION",
        "Pillar Lamp Feedback": "VFX",
        "Warden Hit Effects": "VFX",
        "Repair Gap Markers": "PRESENTATION",
        "Gremlin Path Collapse": "PRESENTATION",
        "Gremlin Route Swap": "PRESENTATION",
        "Gremlin First Rollback": "PRESENTATION",
        "Gremlin Second Rollback": "PRESENTATION",
    }
    if title in overrides:
        return overrides[title]
    return {
        "3D Models": "MODEL",
        "UI & Information": "UI / TEXT",
        "Audio": "SFX",
        "Visual Effects & Presentation": "PRESENTATION",
    }.get(category, category.upper())


def _asset_html(entry: AssetEntry, page_id: str) -> str:
    copy_id = f"{page_id}-asset-copy-{slug(entry.title)}"
    type_label = _category_label(entry.category, entry.title)
    actions = ""
    detail = ""
    if entry.content:
        actions = _copy_button(copy_id, "Copy Text")
        short_copy = len(entry.content) <= 320 and entry.content.count("\n") <= 7
        if short_copy:
            detail = (
                '<div class="pa-row-copy pa-row-copy-open">'
                f'<pre class="pa-content" id="{copy_id}">{esc(entry.content)}</pre>'
                '</div>'
            )
        else:
            detail = (
                '<details class="pa-row-details">'
                '<summary>View Text</summary>'
                f'<pre class="pa-content" id="{copy_id}">{esc(entry.content)}</pre>'
                '</details>'
            )
    return (
        '<article class="pa-row">'
        '<div class="pa-row-main">'
        f'<span class="pa-type">{esc(type_label)}</span>'
        '<div class="pa-row-info">'
        f'<h4>{esc(entry.title)}</h4>'
        f'<p class="pa-meta"><span>Used</span>{esc(entry.used)}</p>'
        f'<p class="pa-meta"><span>Purpose</span>{esc(entry.for_text)}</p>'
        '</div>'
        f'<div class="pa-row-actions">{actions}</div>'
        '</div>'
        f'{detail}'
        '</article>'
    )


def _voice_html(
    entry: voice.VoiceEntry,
    doc: voice.VoiceProduction,
    for_text: str,
    used_text: str,
) -> str:
    prompt_id = f"voice-prompt-{slug(entry.voice_id)}"
    selected_voice = voice._voice_for(doc.cast, entry.speaker)
    return (
        '<article class="pa-row pa-row-voice">'
        '<div class="pa-row-main">'
        '<span class="pa-type pa-type-voice">VOICE</span>'
        '<div class="pa-row-info">'
        f'<h4>{esc(entry.speaker)} — {esc(entry.title)}</h4>'
        f'<p class="pa-meta"><span>Used</span>{esc(used_text)}</p>'
        f'<p class="pa-meta"><span>Purpose</span>{esc(for_text)}</p>'
        f'<small>{esc(selected_voice)} · {esc(entry.duration)}</small>'
        '</div>'
        '<div class="pa-row-actions">'
        f'<button class="voice-copy-button" data-voice-copy="{esc(prompt_id)}" type="button">'
        '<span class="voice-copy-label">Copy Prompt</span></button>'
        '</div>'
        '</div>'
        '<details class="pa-row-details pa-voice-details">'
        '<summary>View Prompt</summary>'
        f'<pre class="voice-script-text" id="{esc(prompt_id)}">{esc(entry.performance)}</pre>'
        f'<div class="voice-script-display">{voice._performance_html(entry.performance)}</div>'
        '</details>'
        '</article>'
    )


def _shared_voice_cast_html(doc: voice.VoiceProduction | None) -> str:
    if doc is None or not doc.cast:
        return ""
    rows = []
    for speaker, selected in doc.cast.items():
        rows.append(
            '<div class="pa-cast-row">'
            f'<strong>{esc(speaker)}</strong>'
            f'<span>{esc(selected)}</span>'
            '<small>Eleven v3</small>'
            '</div>'
        )
    return (
        '<div class="pa-cast">'
        '<div class="pa-cast-head"><span>Voice Cast</span><p>Shared voice assignments for all Production Assets.</p></div>'
        '<div class="pa-cast-rows">' + ''.join(rows) + '</div>'
        '</div>'
    )


def _parse_voice_requirement_field(path: Path, label: str) -> dict[str, str]:
    values: dict[str, str] = {}
    current: str | None = None
    entry_re = re.compile(r"^###\s+([A-Za-z0-9][A-Za-z0-9-]*)\s+[—-]")
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        match = entry_re.match(line)
        if match:
            current = match.group(1)
            continue
        prefix = f"- {label}:"
        if current and line.startswith(prefix):
            value = line.split(":", 1)[1].strip()
            if value:
                values[current] = value
    return values


def _group_display(label: str) -> str:
    return re.sub(r"^\s*\d+\s*[—-]\s*", "", label).strip()


def _pages_and_nav(
    render_data: dict[str, Any],
    assets: AssetRequirements | None,
    voice_doc: voice.VoiceProduction | None,
    triggers: dict[str, str],
    voice_flows: dict[str, str],
    voice_for: dict[str, str],
    voice_groups: dict[str, str],
    voice_used: dict[str, str],
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

    for title in _ordered_titles(render_data, assets, voice_doc):
        key = voice._title_key(title)
        asset_section = asset_map.get(key)
        voice_section = voice_map.get(key)
        asset_entries = _asset_entries(asset_section)
        voice_entries = list(voice_section.entries) if voice_section else []
        if not asset_entries and not voice_entries:
            continue

        meta = _presentation(render_data, title)
        grouped_assets: dict[str, list[AssetEntry]] = {}
        for entry in asset_entries:
            grouped_assets.setdefault(entry.group, []).append(entry)

        grouped_voices: dict[str, list[voice.VoiceEntry]] = {}
        for entry in voice_entries:
            group = voice_groups.get(entry.voice_id)
            if not group:
                raise ValueError(f"Voice requirement Group missing for canonical production entry: {entry.voice_id}")
            grouped_voices.setdefault(group, []).append(entry)

        group_titles = sorted(set(grouped_assets) | set(grouped_voices), key=_flow_sort_key)

        body = (
            '<header class="pa-shell">'
            '<small>Production Assets</small>'
            f'<h2>{esc(meta.title)}</h2><strong>{i18n(meta.package_label)}</strong>'
            '<p class="pa-section-note">Concrete production assets and exact in-game copy. Mechanics stay in 03 Development.</p>'
            '</header>'
        )
        if key == voice._title_key(SHARED_SECTION):
            body += _shared_voice_cast_html(voice_doc)

        if len(group_titles) > 1:
            body += '<nav class="pa-group-nav" aria-label="Production groups"><span>Jump to</span>'
            for group_title in group_titles:
                group_id = f"{meta.page_id}-group-{slug(group_title)}"
                body += f'<a href="#{esc(group_id)}">{esc(_group_display(group_title))}</a>'
            body += '</nav>'

        for group_title in group_titles:
            group_id = f"{meta.page_id}-group-{slug(group_title)}"
            body += (
                f'<div class="pa-group" id="{esc(group_id)}">'
                f'<h3>{esc(_group_display(group_title))}</h3>'
                '<div class="pa-rows">'
            )
            for entry in grouped_assets.get(group_title, []):
                body += _asset_html(entry, meta.page_id)
            for entry in grouped_voices.get(group_title, []):
                for_text = voice_for.get(entry.voice_id)
                used_text = voice_used.get(entry.voice_id)
                if not for_text or not used_text:
                    raise ValueError(f"Voice requirement For/Used missing for canonical production entry: {entry.voice_id}")
                if voice_doc is None:
                    raise ValueError("Voice entry exists without Voice Production document.")
                body += _voice_html(entry, voice_doc, for_text, used_text)
            body += '</div></div>'

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
.pa-shell{margin:0 0 14px}
.pa-shell>small{display:block;margin-bottom:6px;color:var(--blue);font-size:.62rem;font-weight:800;letter-spacing:.09em;text-transform:uppercase}
.pa-shell h2{margin:0;color:var(--navy);font-size:1.9rem;line-height:1.12;letter-spacing:-.025em}
.pa-shell>strong{display:block;margin:5px 0 7px;color:var(--amber);font-size:.69rem;letter-spacing:.06em;text-transform:uppercase}
.pa-section-note{max-width:78ch;margin:0;color:var(--muted);font-size:.72rem;line-height:1.45}
.pa-cast{margin:14px 0 18px;border:1px solid var(--line);border-radius:5px;overflow:hidden}
.pa-cast-head{display:flex;align-items:baseline;gap:10px;padding:9px 12px;background:var(--soft);border-bottom:1px solid var(--line)}
.pa-cast-head span{color:var(--navy);font-size:.72rem;font-weight:850;text-transform:uppercase;letter-spacing:.06em}.pa-cast-head p{margin:0;color:var(--muted);font-size:.69rem}
.pa-cast-row{display:grid;grid-template-columns:minmax(120px,.8fr) minmax(0,2fr) auto;gap:12px;align-items:center;padding:9px 12px;border-top:1px solid var(--line);font-size:.72rem}.pa-cast-row:first-child{border-top:0}.pa-cast-row strong{color:var(--navy)}.pa-cast-row small{color:var(--muted)}
.pa-group-nav{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin:14px 0 2px;padding-bottom:10px;border-bottom:1px solid var(--line)}
.pa-group-nav>span{margin-right:3px;color:var(--muted);font-size:.61rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em}
.pa-group-nav a{display:inline-flex;padding:5px 8px;border:1px solid var(--line);border-radius:3px;color:var(--navy);background:var(--paper);font-size:.64rem;font-weight:750;text-decoration:none}.pa-group-nav a:hover,.pa-group-nav a:focus-visible{border-color:var(--blue);color:var(--blue);outline:0}
.pa-group{scroll-margin-top:72px;margin-top:22px}.pa-group+.pa-group{padding-top:18px;border-top:2px solid var(--line)}
.pa-group h3{margin:0 0 8px;color:var(--navy);font-size:1.04rem;line-height:1.25;text-transform:none}
.pa-rows{border-top:1px solid #cbd7dd}.pa-row{border-bottom:1px solid #cbd7dd;background:var(--paper)}
.pa-row-main{display:grid;grid-template-columns:122px minmax(0,1fr) auto;gap:13px;align-items:start;padding:12px 8px}
.pa-type{display:inline-flex;align-items:center;width:max-content;max-width:116px;padding:4px 7px;border-radius:3px;background:var(--soft);color:var(--blue);font-size:.59rem;font-weight:900;letter-spacing:.055em;line-height:1.25;text-transform:uppercase}.pa-type-voice{color:#9a5a0a;background:#fff5df}
.pa-row-info h4{margin:0 0 5px;color:var(--navy);font-size:.87rem;line-height:1.3;text-transform:none}.pa-row-info small{display:block;margin-top:5px;color:var(--muted);font-size:.62rem}
.pa-meta{display:grid;grid-template-columns:54px minmax(0,1fr);gap:7px;margin:2px 0;color:#52616a;font-size:.7rem;line-height:1.4}.pa-meta span{color:var(--blue);font-size:.56rem;font-weight:850;letter-spacing:.05em;text-transform:uppercase}
.pa-row-actions{display:flex;align-items:center;gap:6px;justify-content:flex-end;padding-top:1px}
.pa-copy-button,.pa-row .voice-copy-button{display:inline-flex;align-items:center;justify-content:center;min-height:28px;padding:6px 8px;border:1px solid var(--navy);border-radius:3px;background:var(--navy);color:#fff;font:800 .57rem/1 var(--font);letter-spacing:.04em;text-transform:uppercase;cursor:pointer;white-space:nowrap}.pa-copy-button:hover,.pa-copy-button:focus-visible,.pa-row .voice-copy-button:hover,.pa-row .voice-copy-button:focus-visible{background:var(--blue);border-color:var(--blue);outline:0}
.pa-row-copy,.pa-row-details{margin:0 8px 10px 143px}.pa-row-details{padding-top:0}.pa-row-details summary{display:inline-flex;cursor:pointer;color:var(--blue);font-size:.66rem;font-weight:800;margin:0 0 7px;user-select:none}
.pa-content,.pa-row .voice-script-text{margin:0;padding:10px 12px;border:1px solid var(--line);border-left:3px solid var(--blue);border-radius:3px;background:#f8fafb;color:var(--navy);font:700 .76rem/1.52 var(--font);white-space:pre-wrap;overflow-wrap:anywhere}.pa-row .voice-script-text{display:block!important;border-left-color:var(--amber)}
.pa-row .voice-script-display{margin-top:7px;padding:8px 0 0;border-top:1px solid var(--line)}.pa-row .voice-performance-tag{font-size:.57rem}.pa-row .voice-script-line{font-size:.75rem;line-height:1.5}.pa-row .voice-script-gap{height:6px}
body.theme-dark .pa-row{background:#17262d}body.theme-dark .pa-type{background:#1d2f37}.theme-dark .pa-type-voice{background:#3a2c14;color:#ffd488}body.theme-dark .pa-meta,body.theme-dark .pa-section-note{color:#c8d7dc}body.theme-dark .pa-content,body.theme-dark .pa-row .voice-script-text{background:#1d2f37;color:#e8eff3}
@media(max-width:760px){.pa-row-main{grid-template-columns:1fr auto}.pa-type{grid-column:1}.pa-row-info{grid-column:1/-1;grid-row:2}.pa-row-actions{grid-column:2;grid-row:1}.pa-row-copy,.pa-row-details{margin-left:8px}.pa-cast-row{grid-template-columns:1fr}.pa-meta{grid-template-columns:50px minmax(0,1fr)}}
@media print{.pa-group-nav,.pa-copy-button,.pa-row .voice-copy-button{display:none!important}.pa-row,.pa-group{break-inside:avoid}}
</style>'''

OBJECTIVE_COPY_SCRIPT = r'''<script id="production-assets-flow-copy-script">(function(){
  function fallbackCopy(text){var area=document.createElement('textarea');area.value=text;area.setAttribute('readonly','');area.style.position='fixed';area.style.opacity='0';document.body.appendChild(area);area.select();try{document.execCommand('copy');}finally{document.body.removeChild(area);}}
  document.addEventListener('click',function(event){var button=event.target.closest('[data-pa-copy]');if(!button)return;var source=document.getElementById(button.getAttribute('data-pa-copy'));if(!source)return;var text=source.textContent||'';var label=button.querySelector('.pa-copy-label');var original=label?label.textContent:'Copy';var done=function(){button.classList.add('is-copied');if(label)label.textContent='Copied ✓';else button.textContent='Copied ✓';setTimeout(function(){button.classList.remove('is-copied');if(label)label.textContent=original;else button.textContent=original;},1400);};if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(done,function(){fallbackCopy(text);done();});}else{fallbackCopy(text);done();}});
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
    voice_for = voice.parse_voice_requirement_for(requirements_path) if has_voice else {}
    voice_groups = _parse_voice_requirement_field(requirements_path, "Group") if has_voice else {}
    voice_used = _parse_voice_requirement_field(requirements_path, "Used") if has_voice else {}
    source = output.read_text(encoding="utf-8")

    if voice.STYLE_MARKER in source or OBJECTIVE_STYLE_MARKER in source:
        raise ValueError("Production Assets extension already exists in rendered HTML.")

    pages, nav = _pages_and_nav(render_data, assets, voice_doc, triggers, voice_flows, voice_for, voice_groups, voice_used)
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
