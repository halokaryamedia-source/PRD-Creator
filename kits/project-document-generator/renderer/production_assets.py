from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from core import bi, esc, i18n, page, txt
from pages import flow_page_id, global_page_id

ENTRY_RE = re.compile(r"^###\s+([A-Za-z0-9][A-Za-z0-9-]*)\s+[—-]\s+(.+?)\s*$")
PLACEHOLDER_RE = re.compile(r"\b(?:TBD|TODO|FIXME)\b|\[OPEN\]", re.I)
PERFORMANCE_TAG_LINE_RE = re.compile(r"^(?:\[[^\[\]\r\n]+\]\s*)+$")
PERFORMANCE_TAG_RE = re.compile(r"\[[^\[\]\r\n]+\]")
SECTION_PREFIX_RE = re.compile(r"^\s*\d+\.\s*")
VOICE_CAST_LABEL = "Voice Cast:"
STYLE_MARKER = 'id="production-assets-style"'
SCRIPT_MARKER = 'id="production-assets-copy-script"'


@dataclass
class VoiceEntry:
    voice_id: str
    title: str
    speaker: str = ""
    duration: str = ""
    performance: str = ""


@dataclass
class VoiceSection:
    title: str
    entries: list[VoiceEntry] = field(default_factory=list)


@dataclass
class VoiceProduction:
    cast: dict[str, str]
    sections: list[VoiceSection]


@dataclass
class SectionPresentation:
    title: str
    page_code: int | None
    package_label: Any
    context: Any
    voice_count: int
    primary_speaker: str


def _has_initial_performance_tag(performance: str) -> bool:
    first = next((line.strip() for line in performance.splitlines() if line.strip()), "")
    return bool(first and PERFORMANCE_TAG_LINE_RE.fullmatch(first))


def _plain_section_title(value: str) -> str:
    return SECTION_PREFIX_RE.sub("", value).strip()


def _title_key(value: str) -> str:
    return (
        _plain_section_title(value)
        .replace("’", "'")
        .replace("`", "'")
        .casefold()
        .strip()
    )


def parse_voice_production(path: Path) -> VoiceProduction:
    text = path.read_text(encoding="utf-8")
    if PLACEHOLDER_RE.search(text):
        raise ValueError("Voice Production contains an unresolved placeholder.")

    lines = text.splitlines()
    cast: dict[str, str] = {}
    sections: list[VoiceSection] = []
    current_section: VoiceSection | None = None
    in_cast = False
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()

        if current_section is None and line.strip() == VOICE_CAST_LABEL:
            in_cast = True
            i += 1
            continue
        if current_section is None and in_cast:
            if line.startswith("- "):
                payload = line[2:].strip()
                if ":" not in payload:
                    raise ValueError("Voice Cast entries must use '- <Speaker>: <ElevenLabs voice>'.")
                speaker, voice = (part.strip() for part in payload.split(":", 1))
                if not speaker or not voice:
                    raise ValueError("Voice Cast requires a non-empty Speaker and ElevenLabs voice.")
                key = speaker.casefold()
                if any(existing.casefold() == key for existing in cast):
                    raise ValueError(f"Duplicate Voice Cast speaker: {speaker}")
                cast[speaker] = voice
                i += 1
                continue
            if line.strip():
                in_cast = False

        if line.startswith("## "):
            current_section = VoiceSection(line[3:].strip())
            if not current_section.title:
                raise ValueError("Voice Production section title cannot be empty.")
            sections.append(current_section)
            in_cast = False
            i += 1
            continue

        match = ENTRY_RE.match(line)
        if match:
            if current_section is None:
                raise ValueError(f"Voice entry {match.group(1)} appears before a gameplay section.")
            entry = VoiceEntry(match.group(1), match.group(2).strip())
            i += 1
            while i < len(lines):
                meta = lines[i].rstrip()
                if meta.startswith("Speaker:"):
                    entry.speaker = meta.split(":", 1)[1].strip()
                    i += 1
                    continue
                if meta.startswith("Estimated Duration:"):
                    entry.duration = meta.split(":", 1)[1].strip()
                    i += 1
                    continue
                if meta.strip() == "```performance":
                    i += 1
                    body: list[str] = []
                    while i < len(lines) and lines[i].strip() != "```":
                        body.append(lines[i].rstrip())
                        i += 1
                    if i >= len(lines):
                        raise ValueError(f"Unclosed performance block for {entry.voice_id}.")
                    entry.performance = "\n".join(body).strip()
                    i += 1
                    break
                if meta.startswith("### ") or meta.startswith("## "):
                    break
                i += 1

            for label, value in {
                "Speaker": entry.speaker,
                "Estimated Duration": entry.duration,
                "Performance Script": entry.performance,
            }.items():
                if not value:
                    raise ValueError(f"{entry.voice_id} is missing {label}.")
            if not _has_initial_performance_tag(entry.performance):
                raise ValueError(
                    f"{entry.voice_id} performance must begin with at least one initial [performance direction] tag."
                )
            current_section.entries.append(entry)
            continue

        i += 1

    if not sections or not any(section.entries for section in sections):
        raise ValueError("Voice Production contains no gameplay-ordered Voice entries.")
    empty = [section.title for section in sections if not section.entries]
    if empty:
        raise ValueError("Voice Production section has no entries: " + ", ".join(empty))
    ids = [entry.voice_id for section in sections for entry in section.entries]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate Voice IDs exist in Voice Production.")
    return VoiceProduction(cast=cast, sections=sections)


def parse_voice_requirement_triggers(path: Path) -> dict[str, str]:
    if not path.is_file():
        raise ValueError("Voice Production requires current work/voice-requirements.md for operator context.")

    triggers: dict[str, str] = {}
    current_id: str | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        match = ENTRY_RE.match(line)
        if match:
            current_id = match.group(1)
            continue
        if current_id and line.startswith("- Trigger:"):
            trigger = line.split(":", 1)[1].strip()
            if not trigger:
                raise ValueError(f"Voice requirement Trigger is empty for: {current_id}")
            triggers[current_id] = trigger

    if not triggers:
        raise ValueError("No Voice requirement Trigger values were found.")
    return triggers


def _voice_for(cast: dict[str, str], speaker: str) -> str:
    speaker_key = speaker.casefold()
    for cast_speaker, voice in cast.items():
        if cast_speaker.casefold() == speaker_key:
            return voice
    return "Voice selection pending"


def _section_speakers(section: VoiceSection) -> list[str]:
    speakers: list[str] = []
    seen: set[str] = set()
    for entry in section.entries:
        key = entry.speaker.casefold()
        if key not in seen:
            seen.add(key)
            speakers.append(entry.speaker)
    return speakers


def _section_metadata(render_data: dict[str, Any], section: VoiceSection) -> SectionPresentation:
    title = _plain_section_title(section.title)
    key = _title_key(title)

    packages = render_data.get("packages", [])
    for index, package in enumerate(packages):
        package_title = package.get("title", "")
        if _title_key(txt(package_title)["en"]) == key:
            speakers = _section_speakers(section)
            primary = speakers[0] if len(speakers) == 1 else "Multiple speakers"
            return SectionPresentation(
                title=title,
                page_code=5 + index,
                package_label=package.get("package_label", f"Gameplay {index + 1}"),
                context=package.get("gameplay", {}).get("context", ""),
                voice_count=len(section.entries),
                primary_speaker=primary,
            )

    for journey in render_data.get("overview", {}).get("journey", []):
        journey_title = journey.get("title", "")
        if _title_key(txt(journey_title)["en"]) == key:
            speakers = _section_speakers(section)
            primary = speakers[0] if len(speakers) == 1 else "Multiple speakers"
            return SectionPresentation(
                title=title,
                page_code=None,
                package_label="Journey",
                context=journey.get("description", ""),
                voice_count=len(section.entries),
                primary_speaker=primary,
            )

    speakers = _section_speakers(section)
    primary = speakers[0] if len(speakers) == 1 else "Multiple speakers"
    return SectionPresentation(
        title=title,
        page_code=None,
        package_label="Gameplay",
        context="",
        voice_count=len(section.entries),
        primary_speaker=primary,
    )


def _section_setup_html(doc: VoiceProduction, section: VoiceSection) -> str:
    rows = []
    for speaker in _section_speakers(section):
        rows.append(
            '<div class="voice-page-setup-row">'
            f'<span class="voice-page-setup-speaker">{esc(speaker)}</span>'
            '<span aria-hidden="true">·</span>'
            f'<strong>{esc(_voice_for(doc.cast, speaker))}</strong>'
            '<span aria-hidden="true">·</span>'
            '<span class="voice-page-setup-model">Eleven v3</span>'
            '</div>'
        )
    return (
        '<div class="voice-page-setup">'
        f'<span class="voice-page-setup-label">{i18n(bi("Voice Setup", "Setup Voice"))}</span>'
        '<div class="voice-page-setup-rows">' + "".join(rows) + '</div>'
        '</div>'
    )


def _section_shell_html(
    render_data: dict[str, Any],
    doc: VoiceProduction,
    section: VoiceSection,
) -> tuple[str, SectionPresentation]:
    meta = _section_metadata(render_data, section)
    number = f"{meta.page_code:02d}. " if meta.page_code is not None else ""
    context = meta.context or bi(
        "Gameplay context follows the accepted PRD.",
        "Konteks gameplay mengikuti PRD yang diterima.",
    )

    shell = (
        '<section class="voice-objective-shell">'
        f'<span class="voice-objective-kicker">{i18n(bi("Gameplay Order", "Urutan Gameplay"))}</span>'
        f'<h2 class="voice-objective-title">{esc(number)}{esc(meta.title)}</h2>'
        f'<p class="voice-objective-label">{i18n(meta.package_label)}</p>'
        '<div class="voice-objective-summary">'
        '<div class="voice-objective-summary-item voice-objective-context">'
        f'<span>{i18n(bi("Context", "Konteks"))}</span>'
        f'<p>{i18n(context)}</p>'
        '</div>'
        '<div class="voice-objective-summary-item">'
        f'<span>{i18n(bi("Voice Lines", "Voice Lines"))}</span>'
        f'<strong>{meta.voice_count}</strong>'
        '</div>'
        '<div class="voice-objective-summary-item">'
        f'<span>{i18n(bi("Primary Speaker", "Primary Speaker"))}</span>'
        f'<strong>{esc(meta.primary_speaker)}</strong>'
        '</div>'
        '</div>'
        + _section_setup_html(doc, section)
        + '</section>'
    )
    return shell, meta


def _performance_html(performance: str) -> str:
    parts: list[str] = []
    for raw in performance.splitlines():
        stripped = raw.strip()
        if not stripped:
            parts.append('<div class="voice-script-gap" aria-hidden="true"></div>')
            continue
        if PERFORMANCE_TAG_LINE_RE.fullmatch(stripped):
            tags = "".join(
                f'<span class="voice-performance-tag">{esc(tag)}</span>'
                for tag in PERFORMANCE_TAG_RE.findall(stripped)
            )
            parts.append(f'<div class="voice-performance-cues">{tags}</div>')
            continue
        parts.append(f'<div class="voice-script-line">{esc(raw)}</div>')
    return "".join(parts)


def _entry_html(
    entry: VoiceEntry,
    sequence_no: int,
    line_index: int,
    line_total: int,
    package_label: Any,
    trigger_context: str,
) -> str:
    prompt_id = f"voice-prompt-{esc(entry.voice_id.lower())}"
    return (
        '<article class="voice-script-card">'
        '<div class="voice-script-card-head">'
        '<div class="voice-script-identity">'
        f'<span class="voice-script-index">{sequence_no:02d}</span>'
        '<div class="voice-script-heading">'
        f'<h4>{esc(entry.title)}</h4>'
        f'<div class="voice-script-position">{i18n(package_label)} · {i18n(bi("Voice Line", "Voice Line"))} {line_index}/{line_total}</div>'
        f'<p class="voice-script-context"><span>{i18n(bi("Context", "Konteks"))}</span>{esc(trigger_context)}</p>'
        '<div class="voice-script-meta">'
        f'<span>{esc(entry.speaker)}</span>'
        '<span aria-hidden="true">·</span>'
        f'<span>{esc(entry.duration)}</span>'
        '</div>'
        '</div>'
        '</div>'
        f'<button class="voice-copy-button" data-voice-copy="{prompt_id}" type="button" title="Copy exact ElevenLabs prompt">'
        f'<span class="voice-copy-label">{i18n(bi("Copy Prompt", "Copy Prompt"))}</span>'
        '</button>'
        '</div>'
        f'<pre class="voice-script-text" id="{prompt_id}">{esc(entry.performance)}</pre>'
        f'<div class="voice-script-display">{_performance_html(entry.performance)}</div>'
        '</article>'
    )


def voice_pages(
    render_data: dict[str, Any],
    doc: VoiceProduction,
    requirement_triggers: dict[str, str],
) -> list[str]:
    brand = render_data["document"].get("brand") or render_data["document"]["title"]
    pages: list[str] = []
    sequence_no = 1

    for section_index, section in enumerate(doc.sections):
        shell, meta = _section_shell_html(render_data, doc, section)
        body = shell + '<div class="voice-script-list">'
        line_total = len(section.entries)

        for line_index, entry in enumerate(section.entries, 1):
            trigger = requirement_triggers.get(entry.voice_id)
            if not trigger:
                raise ValueError(
                    f"Voice requirement Trigger missing for canonical production entry: {entry.voice_id}"
                )
            body += _entry_html(
                entry,
                sequence_no,
                line_index,
                line_total,
                meta.package_label,
                trigger,
            )
            sequence_no += 1
        body += "</div>"

        pages.append(
            page(
                f"production-assets-voice-{section_index + 1}",
                f"04{chr(65 + section_index)}",
                bi("Voice Production", "Voice Production"),
                body,
                context=meta.title,
                header=bi("Production Assets — Voice", "Aset Produksi — Voice"),
                footer_title=bi("Production Assets · Voice", "Aset Produksi · Voice"),
                brand=brand,
                role="production-assets",
                classes="sheet professional-only production-assets-page voice-production-page",
            )
        )
    return pages


def _flow_navigation(render_data: dict[str, Any]) -> str:
    items = render_data.get("gameplay_flow", [])
    if not items:
        return ""
    links = "".join(
        f'<a data-target="{esc(flow_page_id(item, index))}" href="#{esc(flow_page_id(item, index))}">{i18n(item.get("title", item["id"]))}</a>'
        for index, item in enumerate(items)
    )
    return (
        '<div class="nav-group is-open">'
        '<button aria-expanded="true" class="nav-group-toggle" type="button">'
        f'<span class="nav-index" data-full-index="02" data-overview-index="02">{i18n("02")}</span>'
        f'<span class="nav-copy">{i18n(bi("Gameplay Flow", "Alur Gameplay"))}</span>'
        '<span aria-hidden="true" class="group-chevron"></span></button>'
        f'<div class="nav-submenu">{links}</div></div>'
    )


def _development_navigation(render_data: dict[str, Any]) -> str:
    links = "".join(
        f'<a data-target="{esc(global_page_id(item))}" href="#{esc(global_page_id(item))}">{i18n(item.get("title", item["id"]))}</a>'
        for item in render_data.get("global_development", [])
    )
    if not links:
        return ""
    return (
        '<div class="nav-group is-open professional-nav">'
        '<button aria-expanded="true" class="nav-group-toggle" type="button">'
        f'<span class="nav-index" data-full-index="03" data-overview-index="">{i18n("03")}</span>'
        f'<span class="nav-copy">{i18n(bi("Development", "Development"))}</span>'
        '<span aria-hidden="true" class="group-chevron"></span></button>'
        f'<div class="nav-submenu">{links}</div></div>'
    )


def _production_assets_navigation(doc: VoiceProduction) -> str:
    links = "".join(
        f'<a data-target="production-assets-voice-{index + 1}" href="#production-assets-voice-{index + 1}">'
        f'{i18n(bi("Voice", "Voice"))}<small>{esc(_plain_section_title(section.title))}</small></a>'
        for index, section in enumerate(doc.sections)
    )
    return (
        '<div class="nav-group is-open professional-nav production-assets-nav">'
        '<button aria-expanded="true" class="nav-group-toggle" type="button">'
        '<span class="nav-index" data-full-index="04" data-overview-index="">04</span>'
        f'<span class="nav-copy">{i18n(bi("Production Assets", "Aset Produksi"))}</span>'
        '<span aria-hidden="true" class="group-chevron"></span></button>'
        f'<div class="nav-submenu">{links}</div></div>'
    )


def _package_navigation(render_data: dict[str, Any]) -> str:
    groups = []
    for index, package in enumerate(render_data.get("packages", [])):
        package_id = package["id"]
        code = 5 + index
        title = package.get("title", package_id)
        label = package.get("package_label", f"Gameplay {index + 1}")
        subpages = "".join(
            f'<a data-target="dev-{package_id}-{key}" href="#dev-{package_id}-{key}">{i18n(name)}</a>'
            for key, name in (
                ("requirement", bi("Gameplay Overview", "Gameplay Overview")),
                ("level", bi("Level Design", "Level Design")),
                ("developer", bi("Developer", "Developer")),
            )
        )
        groups.append(
            '<div class="nav-group is-open professional-nav production-objective-nav">'
            '<button aria-expanded="true" class="nav-group-toggle" type="button">'
            f'<span class="nav-index" data-full-index="{code:02d}" data-overview-index="">{code:02d}</span>'
            f'<span class="nav-copy">{i18n(title)}</span>'
            '<span aria-hidden="true" class="group-chevron"></span></button>'
            f'<div class="nav-submenu"><div class="production-objective-label">{i18n(label)}</div>{subpages}</div></div>'
        )
    return "".join(groups)


def consolidated_navigation(render_data: dict[str, Any], doc: VoiceProduction) -> str:
    overview = (
        '<a class="nav-link" data-target="summary" href="#summary">'
        f'<span class="nav-index" data-full-index="01" data-overview-index="01">{i18n("01")}</span>'
        f'<span class="nav-copy">{i18n(bi("Overview", "Gambaran Umum"))}</span></a>'
    )
    return (
        overview
        + _flow_navigation(render_data)
        + _development_navigation(render_data)
        + _production_assets_navigation(doc)
        + _package_navigation(render_data)
    )


def _renumber_package_page_codes(source: str, render_data: dict[str, Any]) -> str:
    for index, _package in enumerate(render_data.get("packages", [])):
        old_base = 4 + index
        new_base = 5 + index
        for suffix in ("A", "B", "C"):
            old = f"{old_base:02d}{suffix}"
            new = f"{new_base:02d}{suffix}"
            source = source.replace(
                f'data-en="{old}" data-id="{old}">{old}</span>',
                f'data-en="{new}" data-id="{new}">{new}</span>',
            )
    return source


VOICE_STYLE = r'''<style id="production-assets-style">
.production-assets-page{--voice-panel:#f8fafb;--voice-line:#d8e1e5}
.voice-objective-shell{margin:0 0 22px}
.voice-objective-kicker{display:block;margin:0 0 7px;color:var(--blue);font-size:.63rem;font-weight:800;letter-spacing:.09em;text-transform:uppercase}
.voice-objective-title{margin:0;color:var(--navy);font-size:1.9rem;line-height:1.12;letter-spacing:-.025em}
.voice-objective-label{margin:6px 0 18px;color:var(--amber);font-size:.7rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase}
.voice-objective-summary{display:grid;grid-template-columns:minmax(0,1.65fr) minmax(120px,.45fr) minmax(180px,.65fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.voice-objective-summary-item{min-width:0;padding:13px 18px 14px 0}
.voice-objective-summary-item+.voice-objective-summary-item{padding-left:18px;border-left:1px solid var(--line)}
.voice-objective-summary-item>span{display:block;margin-bottom:5px;color:var(--muted);font-size:.61rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase}
.voice-objective-summary-item p{margin:0;color:#52616a;font-size:.78rem;line-height:1.5}
.voice-objective-summary-item strong{display:block;color:var(--navy);font-size:.88rem;line-height:1.4}
.voice-page-setup{display:flex;align-items:center;gap:14px;margin:12px 0 0;padding:10px 12px;border-left:3px solid var(--blue);background:var(--voice-panel)}
.voice-page-setup-label{flex:0 0 auto;color:var(--blue);font-size:.61rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase}
.voice-page-setup-rows{display:flex;min-width:0;flex-wrap:wrap;gap:7px 18px}
.voice-page-setup-row{display:flex;align-items:center;gap:7px;min-width:0;color:var(--muted);font-size:.7rem}
.voice-page-setup-row strong{color:var(--navy);font-size:.76rem}
.voice-page-setup-speaker{color:var(--ink);font-weight:700}
.voice-page-setup-model{color:var(--blue);font-weight:800}
.voice-script-list{display:grid;gap:16px;margin-top:4px}
.voice-script-card{overflow:hidden;border:1px solid var(--voice-line);border-radius:5px;background:var(--paper);break-inside:avoid}
.voice-script-card-head{display:flex;align-items:flex-start;justify-content:space-between;gap:20px;padding:16px 17px 13px}
.voice-script-identity{display:flex;gap:12px;align-items:flex-start;min-width:0}
.voice-script-index{min-width:24px;padding-top:2px;color:var(--amber);font-size:.69rem;font-weight:900;letter-spacing:.08em}
.voice-script-heading{min-width:0;flex:1}
.voice-script-heading h4{margin:0;color:var(--navy);font-size:.98rem;line-height:1.3;letter-spacing:.005em;text-transform:none}
.voice-script-position{margin-top:4px;color:var(--blue);font-size:.67rem;font-weight:800;letter-spacing:.02em}
.voice-script-context{max-width:780px;margin:7px 0 0;color:#52616a;font-size:.76rem;line-height:1.48}
.voice-script-context span{margin-right:6px;color:var(--muted);font-size:.61rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase}
.voice-script-meta{display:flex;gap:7px;align-items:center;flex-wrap:wrap;margin-top:7px;color:var(--muted);font-size:.69rem}
.voice-script-text{display:none}
.voice-script-display{padding:17px 18px 20px;border-top:1px solid var(--voice-line);background:#fff}
.voice-script-line{max-width:74ch;color:var(--ink);font:500 .94rem/1.7 var(--font);overflow-wrap:anywhere}
.voice-script-gap{height:10px}
.voice-performance-cues{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 8px}
.voice-performance-tag{display:inline-flex;align-items:center;min-height:22px;padding:3px 7px;border:0;border-left:2px solid var(--blue);border-radius:2px;background:var(--soft);color:var(--blue);font-size:.64rem;font-weight:800;letter-spacing:.025em;text-transform:uppercase}
.voice-copy-button{display:inline-flex;align-items:center;justify-content:center;min-height:36px;padding:9px 13px;border:1px solid var(--navy);border-radius:3px;background:var(--navy);color:#fff;font:800 .65rem/1 var(--font);letter-spacing:.055em;text-transform:uppercase;cursor:pointer;white-space:nowrap}
.voice-copy-button:hover,.voice-copy-button:focus-visible{border-color:var(--blue);background:var(--blue);outline:0}
.voice-copy-button.is-copied{border-color:var(--green);background:var(--green);color:#fff}
.production-assets-nav .nav-submenu a small{display:block;margin-top:2px}
.production-objective-label{padding:6px 10px 3px 14px;color:rgba(255,255,255,.42);font-size:.58rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase}
body.theme-dark .voice-objective-summary-item p,body.theme-dark .voice-script-context{color:#c8d7dc}
body.theme-dark .voice-page-setup{background:#1d2f37}
body.theme-dark .voice-script-card{border-color:#405761}
body.theme-dark .voice-script-display{background:#17262d;border-color:#405761}
body.theme-dark .voice-script-line{color:#e8eff3}
@media(max-width:760px){
.voice-objective-summary{grid-template-columns:1fr}
.voice-objective-summary-item+.voice-objective-summary-item{padding-left:0;border-left:0;border-top:1px solid var(--line)}
.voice-page-setup{align-items:flex-start;flex-direction:column;gap:7px}
.voice-script-card-head{gap:12px;padding:14px}
.voice-script-display{padding:15px}
.voice-copy-button{min-height:32px;padding:7px 9px}
}
@media print{
.voice-copy-button{display:none!important}
.voice-script-card,.voice-objective-shell{break-inside:avoid}
}
</style>'''

VOICE_COPY_SCRIPT = r'''<script id="production-assets-copy-script">(function(){
  function fallbackCopy(text){
    var area=document.createElement('textarea');
    area.value=text;area.setAttribute('readonly','');area.style.position='fixed';area.style.opacity='0';
    document.body.appendChild(area);area.select();
    try{document.execCommand('copy');}finally{document.body.removeChild(area);}
  }
  document.addEventListener('click',function(event){
    var button=event.target.closest('[data-voice-copy]');if(!button)return;
    var source=document.getElementById(button.getAttribute('data-voice-copy'));if(!source)return;
    var text=source.textContent||'';
    var label=button.querySelector('.voice-copy-label');
    var original=label?label.textContent:'Copy Prompt';
    var done=function(){
      button.classList.add('is-copied');
      if(label)label.textContent='Copied ✓';else button.textContent='Copied ✓';
      setTimeout(function(){button.classList.remove('is-copied');if(label)label.textContent=original;else button.textContent=original;},1400);
    };
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(done,function(){fallbackCopy(text);done();});}
    else{fallbackCopy(text);done();}
  });
})();</script>'''


def _insert_before_closing(source: str, closing: str, addition: str, label: str) -> str:
    if source.count(closing) != 1:
        raise ValueError(f"Rendered HTML requires exactly one {label} closing marker.")
    return source.replace(closing, addition + "\n" + closing, 1)


def augment_project_html(render_data_path: Path, output: Path, voice_production_path: Path) -> None:
    if not voice_production_path.is_file():
        return

    render_data = json.loads(render_data_path.read_text(encoding="utf-8"))
    doc = parse_voice_production(voice_production_path)
    requirement_triggers = parse_voice_requirement_triggers(
        voice_production_path.parent / "voice-requirements.md"
    )
    source = output.read_text(encoding="utf-8")

    if STYLE_MARKER in source or SCRIPT_MARKER in source:
        raise ValueError("Production Assets extension already exists in rendered HTML.")

    pages = "".join(voice_pages(render_data, doc, requirement_triggers))
    nav = consolidated_navigation(render_data, doc)

    nav_pattern = re.compile(r'(<nav class="sidebar-nav">).*?(</nav>)', re.S)
    main_pattern = re.compile(r'(<main class="document-main">.*?)(</main>)', re.S)
    if len(nav_pattern.findall(source)) != 1:
        raise ValueError("Rendered HTML requires exactly one sidebar navigation container.")
    if len(main_pattern.findall(source)) != 1:
        raise ValueError("Rendered HTML requires exactly one document main container.")

    source = _renumber_package_page_codes(source, render_data)
    source = nav_pattern.sub(lambda match: match.group(1) + nav + match.group(2), source, count=1)
    source = main_pattern.sub(lambda match: match.group(1) + pages + match.group(2), source, count=1)
    source = _insert_before_closing(source, "</head>", VOICE_STYLE, "head")
    source = _insert_before_closing(source, "</body>", VOICE_COPY_SCRIPT, "body")

    section_ids = set(re.findall(r'<section\b[^>]*\bid="([^"]+)"', source))
    targets = set(re.findall(r'data-target="([^"]+)"', nav))
    missing = sorted(targets - section_ids)
    if missing:
        raise ValueError(f"Production Assets navigation targets missing from generated pages: {missing}")

    output.write_text(source, encoding="utf-8")
