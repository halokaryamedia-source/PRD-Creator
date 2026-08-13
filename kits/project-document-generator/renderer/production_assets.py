from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from core import bi, esc, i18n, page

ENTRY_RE = re.compile(r"^###\s+([A-Za-z0-9][A-Za-z0-9-]*)\s+[—-]\s+(.+?)\s*$")
PLACEHOLDER_RE = re.compile(r"\b(?:TBD|TODO|FIXME)\b|\[OPEN\]", re.I)
PERFORMANCE_TAG_LINE_RE = re.compile(r"^(?:\[[^\[\]\r\n]+\]\s*)+$")
PERFORMANCE_TAG_RE = re.compile(r"\[[^\[\]\r\n]+\]")
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


def _has_initial_performance_tag(performance: str) -> bool:
    first = next((line.strip() for line in performance.splitlines() if line.strip()), "")
    return bool(first and PERFORMANCE_TAG_LINE_RE.fullmatch(first))


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


def _voice_for(cast: dict[str, str], speaker: str) -> str:
    speaker_key = speaker.casefold()
    for cast_speaker, voice in cast.items():
        if cast_speaker.casefold() == speaker_key:
            return voice
    return "Voice selection pending"


def _ordered_speakers(doc: VoiceProduction) -> list[str]:
    speakers: list[str] = []
    seen: set[str] = set()
    for section in doc.sections:
        for entry in section.entries:
            key = entry.speaker.casefold()
            if key not in seen:
                seen.add(key)
                speakers.append(entry.speaker)
    return speakers


def _cast_html(doc: VoiceProduction) -> str:
    rows = []
    for speaker in _ordered_speakers(doc):
        voice = _voice_for(doc.cast, speaker)
        rows.append(
            '<div class="voice-setup-row">'
            '<div class="voice-setup-field">'
            f'<span class="voice-setup-label">{i18n(bi("Speaker", "Speaker"))}</span>'
            f'<strong>{esc(speaker)}</strong>'
            '</div>'
            '<div class="voice-setup-field voice-setup-voice">'
            f'<span class="voice-setup-label">{i18n(bi("ElevenLabs Voice", "Voice ElevenLabs"))}</span>'
            f'<strong>{esc(voice)}</strong>'
            '</div>'
            '<div class="voice-setup-field voice-setup-model">'
            f'<span class="voice-setup-label">{i18n(bi("Model", "Model"))}</span>'
            '<strong>Eleven v3</strong>'
            '</div>'
            '</div>'
        )
    return (
        '<section class="voice-setup-block">'
        f'<h3 class="voice-setup-title">{i18n(bi("Voice Setup", "Setup Voice"))}</h3>'
        f'<div class="voice-setup-rows">{"".join(rows)}</div>'
        '</section>'
    )


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


def _entry_html(entry: VoiceEntry, sequence_no: int) -> str:
    prompt_id = f"voice-prompt-{esc(entry.voice_id.lower())}"
    return (
        '<article class="voice-script-card">'
        '<div class="voice-script-card-head">'
        '<div class="voice-script-identity">'
        f'<span class="voice-script-index">{sequence_no:02d}</span>'
        '<div class="voice-script-heading">'
        f'<h4>{esc(entry.title)}</h4>'
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


def voice_pages(render_data: dict, doc: VoiceProduction) -> list[str]:
    brand = render_data["document"].get("brand") or render_data["document"]["title"]
    base_code = 4 + len(render_data.get("packages", []))
    pages: list[str] = []
    sequence_no = 1
    intro = bi(
        "Choose the assigned ElevenLabs voice, then copy each prompt exactly in gameplay order.",
        "Gunakan voice ElevenLabs yang ditentukan, lalu copy setiap prompt secara tepat sesuai urutan gameplay.",
    )

    for section_index, section in enumerate(doc.sections):
        body = f'<p class="eyebrow">{i18n(bi("Production Assets · Voice", "Aset Produksi · Voice"))}</p>'
        if section_index == 0:
            body += (
                f'<h2 class="development-package-title">{i18n(bi("Voice Production", "Voice Production"))}</h2>'
                f'<p class="section-intro voice-production-intro">{i18n(intro)}</p>'
                + _cast_html(doc)
                + '<div class="voice-section-head">'
                + f'<span class="voice-section-label">{i18n(bi("Gameplay Order", "Urutan Gameplay"))}</span>'
                + f'<h3>{esc(section.title)}</h3>'
                + '</div>'
            )
        else:
            body += (
                f'<h2 class="voice-section-page-title">{esc(section.title)}</h2>'
                f'<p class="voice-section-page-subtitle">{i18n(bi("Voice Production", "Voice Production"))}</p>'
            )
        body += '<div class="voice-script-list">'
        for entry in section.entries:
            body += _entry_html(entry, sequence_no)
            sequence_no += 1
        body += "</div>"

        pages.append(
            page(
                f"production-assets-voice-{section_index + 1}",
                f"{base_code:02d}{chr(65 + section_index)}",
                bi("Voice Production", "Voice Production"),
                body,
                context=section.title,
                header=bi("Production Assets — Voice", "Aset Produksi — Voice"),
                footer_title=bi("Production Assets · Voice", "Aset Produksi · Voice"),
                brand=brand,
                role="production-assets",
                classes="sheet professional-only production-assets-page voice-production-page",
            )
        )
    return pages


def voice_navigation(render_data: dict, doc: VoiceProduction) -> str:
    base_code = 4 + len(render_data.get("packages", []))
    links = "".join(
        f'<a data-target="production-assets-voice-{index + 1}" href="#production-assets-voice-{index + 1}">'
        f'{i18n(bi("Voice", "Voice"))}<small>{esc(section.title)}</small></a>'
        for index, section in enumerate(doc.sections)
    )
    return (
        '<div class="nav-group is-open professional-nav production-assets-nav">'
        '<button aria-expanded="true" class="nav-group-toggle" type="button">'
        f'<span class="nav-index" data-full-index="{base_code:02d}" data-overview-index="">{base_code:02d}</span>'
        f'<span class="nav-copy">{i18n(bi("Production Assets", "Aset Produksi"))}</span>'
        '<span aria-hidden="true" class="group-chevron"></span></button>'
        f'<div class="nav-submenu">{links}</div></div>'
    )


VOICE_STYLE = r'''<style id="production-assets-style">
.production-assets-page .voice-production-intro{max-width:660px;margin-bottom:22px}
.voice-setup-block{margin:20px 0 32px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.voice-setup-title{margin:0;padding:12px 0 10px;color:var(--navy);font-size:.82rem;letter-spacing:.02em}
.voice-setup-rows{border-top:1px solid var(--line)}
.voice-setup-row{display:grid;grid-template-columns:minmax(150px,.85fr) minmax(280px,2fr) minmax(110px,.55fr);gap:24px;padding:14px 0}
.voice-setup-row+.voice-setup-row{border-top:1px solid var(--line)}
.voice-setup-field{min-width:0}
.voice-setup-label{display:block;margin-bottom:4px;color:var(--muted);font-size:.61rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase}
.voice-setup-field strong{display:block;color:var(--navy);font-size:.88rem;line-height:1.35}
.voice-setup-voice strong{font-size:1rem}
.voice-setup-model strong{color:var(--blue);font-size:.82rem}
.voice-section-head{display:flex;align-items:baseline;gap:15px;margin:0 0 13px;padding:0 0 10px;border-bottom:1px solid var(--line)}
.voice-section-label{color:var(--blue);font-size:.62rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase}
.voice-section-head h3{margin:0;color:var(--navy);font-size:1rem}
.voice-section-page-title{margin:6px 0 3px;color:var(--navy);font-size:1.55rem;line-height:1.15}
.voice-section-page-subtitle{margin:0 0 22px;color:var(--blue);font-size:.65rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase}
.voice-script-list{display:grid;gap:16px;margin-top:4px}
.voice-script-card{overflow:hidden;border:1px solid var(--line);border-radius:4px;background:var(--paper);break-inside:avoid}
.voice-script-card-head{display:flex;align-items:flex-start;justify-content:space-between;gap:20px;padding:15px 16px 12px}
.voice-script-identity{display:flex;gap:12px;align-items:flex-start;min-width:0}
.voice-script-index{min-width:24px;padding-top:2px;color:var(--amber);font-size:.69rem;font-weight:800;letter-spacing:.08em}
.voice-script-heading{min-width:0;flex:1}
.voice-script-heading h4{margin:0;color:var(--navy);font-size:.96rem;line-height:1.3;letter-spacing:.005em;text-transform:none}
.voice-script-meta{display:flex;gap:7px;align-items:center;flex-wrap:wrap;margin-top:5px;color:var(--muted);font-size:.7rem}
.voice-script-text{display:none}
.voice-script-display{padding:17px 18px 20px;border-top:1px solid var(--line);background:#fff}
.voice-script-line{max-width:74ch;color:var(--ink);font:500 .94rem/1.7 var(--font);overflow-wrap:anywhere}
.voice-script-gap{height:10px}
.voice-performance-cues{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 8px}
.voice-performance-tag{display:inline-flex;align-items:center;min-height:22px;padding:3px 7px;border:0;border-left:2px solid var(--blue);border-radius:2px;background:var(--soft);color:var(--blue);font-size:.64rem;font-weight:800;letter-spacing:.025em;text-transform:uppercase}
.voice-copy-button{display:inline-flex;align-items:center;justify-content:center;min-height:34px;padding:8px 12px;border:1px solid var(--navy);border-radius:3px;background:var(--navy);color:#fff;font:800 .65rem/1 var(--font);letter-spacing:.055em;text-transform:uppercase;cursor:pointer;white-space:nowrap}
.voice-copy-button:hover,.voice-copy-button:focus-visible{border-color:var(--blue);background:var(--blue);outline:0}
.voice-copy-button.is-copied{border-color:var(--green);background:var(--green);color:#fff}
.production-assets-nav .nav-submenu a small{display:block;margin-top:2px}
@media(max-width:760px){.voice-setup-row{grid-template-columns:1fr;gap:10px}.voice-script-card-head{gap:12px;padding:14px}.voice-script-display{padding:15px}.voice-copy-button{min-height:32px;padding:7px 9px}.voice-section-head{align-items:flex-start;flex-direction:column;gap:4px}}
@media print{.voice-copy-button{display:none!important}.voice-script-card{break-inside:avoid}}
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
    source = output.read_text(encoding="utf-8")

    if STYLE_MARKER in source or SCRIPT_MARKER in source:
        raise ValueError("Production Assets extension already exists in rendered HTML.")

    pages = "".join(voice_pages(render_data, doc))
    nav = voice_navigation(render_data, doc)

    nav_pattern = re.compile(r'(<nav class="sidebar-nav">.*?)(</nav>)', re.S)
    main_pattern = re.compile(r'(<main class="document-main">.*?)(</main>)', re.S)
    if len(nav_pattern.findall(source)) != 1:
        raise ValueError("Rendered HTML requires exactly one sidebar navigation container.")
    if len(main_pattern.findall(source)) != 1:
        raise ValueError("Rendered HTML requires exactly one document main container.")

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