from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from core import bi, esc, i18n, page, txt
import production_assets as voice

ASSET_CATEGORIES = ("3D Models", "UI & Information", "Audio", "Visual Effects & Presentation")
SHARED_SECTION = "Global / Shared Assets"
OBJECTIVE_STYLE_MARKER = 'id="production-assets-objective-style"'


@dataclass
class AssetEntry:
    title: str
    requirement: str = ""
    usage: str = ""
    content: str = ""


@dataclass
class AssetSection:
    title: str
    categories: dict[str, list[AssetEntry]] = field(default_factory=dict)


@dataclass
class AssetRequirements:
    sections: list[AssetSection]


@dataclass
class SectionPresentation:
    title: str
    package_label: Any
    context: Any


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
            entry = AssetEntry(title=line[5:].strip())
            if not entry.title:
                raise ValueError("Production Asset name cannot be empty.")

            i += 1
            while i < len(lines):
                meta = lines[i].rstrip()
                if meta.startswith(("## ", "### ", "#### ")):
                    break
                if meta.startswith("Requirement:"):
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
        empty = [name for name, entries in section.categories.items() if not entries]
        if empty:
            raise ValueError(
                f"Production Asset section {section.title} contains empty categories: "
                + ", ".join(empty)
            )
        total += sum(len(entries) for entries in section.categories.values())

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
                "Assets reused across multiple gameplay sections.",
                "Asset yang digunakan ulang di beberapa bagian gameplay.",
            ),
        )

    for index, package in enumerate(render_data.get("packages", [])):
        if voice._title_key(txt(package.get("title", ""))["en"]) == key:
            return SectionPresentation(
                title,
                package.get("package_label", f"Gameplay {index + 1}"),
                package.get("gameplay", {}).get("context", ""),
            )

    journey = render_data.get("overview", {}).get("journey", [])
    for index, item in enumerate(journey):
        if voice._title_key(txt(item.get("title", ""))["en"]) == key:
            label = "Introduction" if index == 0 else "Ending" if index == len(journey) - 1 else "Journey"
            return SectionPresentation(title, bi(label, label), item.get("description", ""))

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


def _asset_html(entry: AssetEntry, number: int) -> str:
    usage = (
        f'<p class="pa-usage"><span>{i18n(bi("Usage", "Penggunaan"))}</span>{esc(entry.usage)}</p>'
        if entry.usage
        else ""
    )
    content = (
        f'<div class="pa-content"><span>{i18n(bi("Content", "Konten"))}</span>'
        f"<pre>{esc(entry.content)}</pre></div>"
        if entry.content
        else ""
    )
    return (
        '<article class="pa-card">'
        f'<div class="pa-card-head"><span>{number:02d}</span><h4>{esc(entry.title)}</h4></div>'
        f'<p class="pa-requirement">{esc(entry.requirement)}</p>'
        f"{usage}{content}</article>"
    )


def _voice_html(
    voice_doc: voice.VoiceProduction,
    section: voice.VoiceSection,
    label: Any,
    triggers: dict[str, str],
    number: int,
) -> tuple[str, int]:
    speakers = voice._section_speakers(section)
    primary = speakers[0] if len(speakers) == 1 else "Multiple speakers"
    body = (
        f'<div class="voice-production-block" data-voice-section="{esc(voice._title_key(section.title))}">'
        '<div class="pa-voice-head">'
        f'<strong>{i18n(bi("Voice Production", "Voice Production"))}</strong>'
        f'<span>{len(section.entries)} Voice Lines · {esc(primary)}</span></div>'
        + voice._section_setup_html(voice_doc, section)
        + '<div class="voice-script-list">'
    )
    for line_index, entry in enumerate(section.entries, 1):
        trigger = triggers.get(entry.voice_id)
        if not trigger:
            raise ValueError(f"Voice requirement Trigger missing for canonical production entry: {entry.voice_id}")
        body += voice._entry_html(entry, number, line_index, len(section.entries), label, trigger)
        number += 1
    return body + "</div></div>", number


def _counts(
    asset_section: AssetSection | None,
    voice_section: voice.VoiceSection | None,
) -> dict[str, int]:
    counts: dict[str, int] = {}
    for category in ASSET_CATEGORIES:
        count = len(asset_section.categories.get(category, [])) if asset_section else 0
        if category == "Audio" and voice_section:
            count += len(voice_section.entries)
        if count:
            counts[category] = count
    return counts


def _pages_and_nav(
    render_data: dict[str, Any],
    assets: AssetRequirements | None,
    voice_doc: voice.VoiceProduction | None,
    triggers: dict[str, str],
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
        counts = _counts(asset_section, voice_section)
        if not counts:
            continue

        meta = _presentation(render_data, title)
        total = sum(counts.values())
        context = meta.context or bi(
            "Production requirements follow the accepted PRD.",
            "Requirement produksi mengikuti PRD yang diterima.",
        )
        summary = (
            f'<div class="pa-summary"><strong>{total} Assets</strong>'
            + "".join(f"<span>{esc(category)} <b>{count}</b></span>" for category, count in counts.items())
            + "</div>"
        )
        shell_class = "pa-shell voice-objective-shell" if voice_section else "pa-shell"
        body = (
            f'<header class="{shell_class}"><small>Production Assets</small>'
            f"<h2>{esc(meta.title)}</h2><strong>{i18n(meta.package_label)}</strong>"
            f'<p class="pa-context">{i18n(context)}</p>{summary}</header>'
        )

        asset_number = 1
        for category, count in counts.items():
            body += (
                '<section class="pa-group"><div class="pa-group-head">'
                f"<h3>{esc(category)}</h3><span>{count} Assets</span></div>"
            )
            if asset_section:
                for entry in asset_section.categories.get(category, []):
                    body += _asset_html(entry, asset_number)
                    asset_number += 1
            if category == "Audio" and voice_section and voice_doc:
                block, voice_number = _voice_html(
                    voice_doc,
                    voice_section,
                    meta.package_label,
                    triggers,
                    voice_number,
                )
                body += block
            body += "</section>"

        index = len(pages)
        pid = f"production-assets-{index + 1}"
        pages.append(
            page(
                pid,
                f"04{chr(65 + index)}",
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
            f"<small>{i18n(meta.package_label)}</small></a>"
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
.pa-shell{margin:0 0 24px}
.pa-shell>small{display:block;margin-bottom:7px;color:var(--blue);font-size:.63rem;font-weight:800;letter-spacing:.09em;text-transform:uppercase}
.pa-shell h2{margin:0;color:var(--navy);font-size:1.9rem;line-height:1.12;letter-spacing:-.025em}
.pa-shell>strong{display:block;margin:6px 0 10px;color:var(--amber);font-size:.7rem;letter-spacing:.06em;text-transform:uppercase}
.pa-context{max-width:78ch;margin:0 0 16px;color:#52616a;font-size:.79rem;line-height:1.5}
.pa-summary{display:flex;align-items:center;gap:10px 20px;flex-wrap:wrap;padding:11px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);color:var(--muted);font-size:.68rem}
.pa-summary>strong,.pa-summary b{color:var(--navy)}
.pa-group{margin-top:22px}
.pa-group-head{display:flex;justify-content:space-between;align-items:baseline;gap:18px;margin-bottom:8px;padding-bottom:7px;border-bottom:1px solid var(--line)}
.pa-group-head h3{margin:0;color:var(--navy);font-size:.82rem;letter-spacing:.065em;text-transform:uppercase}
.pa-group-head span{color:var(--muted);font-size:.65rem}
.pa-card{padding:14px 0 15px;border-bottom:1px solid #d8e1e5;break-inside:avoid}
.pa-card-head{display:flex;gap:10px;align-items:flex-start}
.pa-card-head>span{min-width:24px;padding-top:2px;color:var(--amber);font-size:.69rem;font-weight:900;letter-spacing:.08em}
.pa-card h4{margin:0;color:var(--navy);font-size:.98rem;line-height:1.32;text-transform:none}
.pa-requirement,.pa-usage,.pa-content{max-width:82ch;margin-left:34px}
.pa-requirement{margin-top:7px;color:var(--ink);font-size:.82rem;line-height:1.58}
.pa-usage{margin-top:7px;color:#52616a;font-size:.75rem;line-height:1.5}
.pa-usage span,.pa-content>span{margin-right:7px;color:var(--muted);font-size:.6rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase}
.pa-content{margin-top:9px}
.pa-content>span{display:block;margin-bottom:5px}
.pa-content pre{margin:0;padding:10px 12px;border-left:3px solid var(--blue);background:#f8fafb;color:var(--navy);font:700 .78rem/1.5 var(--font);white-space:pre-wrap;overflow-wrap:anywhere}
.pa-voice-head{display:flex;justify-content:space-between;align-items:baseline;gap:16px;margin-bottom:9px}
.pa-voice-head strong{color:var(--navy);font-size:.79rem}
.pa-voice-head span{color:var(--muted);font-size:.65rem}
body.theme-dark .pa-context,body.theme-dark .pa-usage{color:#c8d7dc}
body.theme-dark .pa-content pre{background:#1d2f37;color:#e8eff3}
@media(max-width:760px){.pa-requirement,.pa-usage,.pa-content{margin-left:0}}
</style>'''


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
    triggers = (
        voice.parse_voice_requirement_triggers(voice_production_path.parent / "voice-requirements.md")
        if has_voice
        else {}
    )
    source = output.read_text(encoding="utf-8")

    if voice.STYLE_MARKER in source or OBJECTIVE_STYLE_MARKER in source:
        raise ValueError("Production Assets extension already exists in rendered HTML.")

    pages, nav = _pages_and_nav(render_data, assets, voice_doc, triggers)
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
    source = _insert(source, "</head>", voice.VOICE_STYLE + OBJECTIVE_STYLE, "head")
    if has_voice:
        source = _insert(source, "</body>", voice.VOICE_COPY_SCRIPT, "body")

    section_ids = set(re.findall(r'<section\b[^>]*\bid="([^"]+)"', source))
    targets = set(re.findall(r'data-target="([^"]+)"', nav))
    missing = sorted(targets - section_ids)
    if missing:
        raise ValueError(f"Production Assets navigation targets missing from generated pages: {missing}")

    output.write_text(source, encoding="utf-8")
