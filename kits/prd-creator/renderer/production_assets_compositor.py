from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
KIT_ROOT = HERE.parent
if str(KIT_ROOT) not in sys.path:
    sys.path.insert(0, str(KIT_ROOT))

from core import bi, esc, i18n, page, slug, txt
import production_assets as voice
from shared.voice import VoiceRequirement, parse_requirements

ASSET_CATEGORIES = ("3D Models", "UI & Information", "Audio", "Visual Effects & Presentation")
OBJECTIVE_STYLE_MARKER = 'id="production-assets-objective-style"'
OWNER_RE = re.compile(r"^(?:Owner ID|Owner):\s*(\S+)\s*$", re.I)
ASSET_ID_RE = re.compile(r"^[A-Z][A-Z0-9]*-[A-Z0-9-]+$")

TYPE_PRIORITY = {"MODEL": 10, "ITEM": 20, "UI / TEXT": 30, "AUDIO": 40, "PARTICLE": 50}


@dataclass(frozen=True)
class AssetEntry:
    asset_id: str
    title: str
    category: str
    type_label: str
    function_text: str
    moment: str
    flow: str = ""
    asset_brief: str = ""
    size: str = ""
    content: str = ""
    order: int = 0


@dataclass
class AssetSection:
    owner_id: str
    title: str
    categories: dict[str, list[AssetEntry]] = field(default_factory=dict)
    flow_order: dict[str, int] = field(default_factory=dict)


@dataclass(frozen=True)
class AssetRequirements:
    sections: tuple[AssetSection, ...]


@dataclass(frozen=True)
class SectionPresentation:
    owner_id: str
    title: str
    package_label: Any
    page_id: str


@dataclass(frozen=True)
class ProductionItem:
    item_id: str
    title: str
    type_label: str
    function_text: str
    moment: str
    flow_order: int
    sort_order: int
    asset_brief: str = ""
    size: str = ""
    content: str = ""
    speaker: str = ""
    selected_voice: str = ""
    duration: str = ""
    is_voice: bool = False


def _default_type(category: str) -> str:
    return {
        "3D Models": "MODEL",
        "UI & Information": "UI / TEXT",
        "Audio": "AUDIO",
        "Visual Effects & Presentation": "PARTICLE",
    }.get(category, category.upper())


def parse_asset_requirements(path: Path) -> AssetRequirements:
    text = path.read_text(encoding="utf-8")
    if voice.PLACEHOLDER_RE.search(text):
        raise ValueError("Production Asset requirements contain an unresolved placeholder.")

    sections: list[AssetSection] = []
    current_section: AssetSection | None = None
    current_category: str | None = None
    owner_ids: set[str] = set()
    asset_ids: set[str] = set()
    lines = text.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()
        if line.startswith("## "):
            if current_section is not None and not current_section.owner_id:
                raise ValueError(f"Production Asset section {current_section.title} requires Owner ID")
            title = line[3:].strip()
            if not title:
                raise ValueError("Production Asset section title cannot be empty.")
            current_section = AssetSection("", title)
            sections.append(current_section)
            current_category = None
            i += 1
            continue

        if current_section is not None and (owner_match := OWNER_RE.match(line)):
            owner_id = owner_match.group(1).strip()
            if current_section.owner_id:
                raise ValueError(f"Duplicate Owner ID in Production Asset section: {current_section.title}")
            if owner_id in owner_ids:
                raise ValueError(f"Duplicate Production Asset Owner ID: {owner_id}")
            current_section.owner_id = owner_id
            owner_ids.add(owner_id)
            i += 1
            continue

        if line.startswith("### Gameplay Flow "):
            if current_section is None or not current_section.owner_id:
                raise ValueError("Gameplay Flow metadata requires a Production Asset section with Owner ID.")
            flow_title = line[len("### Gameplay Flow ") :].strip()
            if not flow_title:
                raise ValueError("Gameplay Flow title cannot be empty.")
            current_section.flow_order.setdefault(flow_title, len(current_section.flow_order) + 1)
            current_category = None
            i += 1
            continue

        if line.startswith("### "):
            if current_section is None or not current_section.owner_id:
                raise ValueError("Production Asset category requires a section with Owner ID.")
            category = line[4:].strip()
            if category not in ASSET_CATEGORIES:
                raise ValueError(f"Unsupported Production Asset category: {category}. Use one of: {', '.join(ASSET_CATEGORIES)}")
            current_section.categories.setdefault(category, [])
            current_category = category
            i += 1
            continue

        if line.startswith("#### "):
            if current_section is None or current_category is None:
                raise ValueError("Production Asset entry appears before its section/category.")
            title = line[5:].strip()
            if not title:
                raise ValueError("Production Asset name cannot be empty.")
            fields: dict[str, str] = {}
            content = ""
            i += 1
            while i < len(lines):
                meta = lines[i].rstrip()
                if meta.startswith(("## ", "### ", "#### ")):
                    break
                if meta.strip() == "Content:":
                    i += 1
                    if i >= len(lines) or not lines[i].strip().startswith("```"):
                        raise ValueError(f"Production Asset Content for {title} must use a fenced text block.")
                    i += 1
                    body: list[str] = []
                    while i < len(lines) and lines[i].strip() != "```":
                        body.append(lines[i].rstrip())
                        i += 1
                    if i >= len(lines):
                        raise ValueError(f"Unclosed Content block for Production Asset: {title}")
                    content = "\n".join(body).strip()
                elif ":" in meta:
                    key, value = meta.split(":", 1)
                    fields[key.strip()] = value.strip()
                i += 1

            asset_id = fields.get("ID", "")
            if not ASSET_ID_RE.fullmatch(asset_id):
                raise ValueError(f"Production Asset {title} requires stable ID such as AST-CORE-CONSOLE")
            if asset_id in asset_ids:
                raise ValueError(f"Duplicate Production Asset ID: {asset_id}")
            asset_ids.add(asset_id)
            function_text = fields.get("Function", "")
            moment = fields.get("Moment", "")
            if not function_text:
                raise ValueError(f"Production Asset {asset_id} requires Function")
            if not moment:
                raise ValueError(f"Production Asset {asset_id} requires Moment")
            flow = fields.get("Flow", "")
            if flow and current_section.flow_order and flow not in current_section.flow_order:
                raise ValueError(f"Production Asset Flow does not match a defined Gameplay Flow: {current_section.owner_id} / {asset_id} / {flow}")
            entry = AssetEntry(
                asset_id=asset_id,
                title=title,
                category=current_category,
                type_label=fields.get("Type") or _default_type(current_category),
                function_text=function_text,
                moment=moment,
                flow=flow,
                asset_brief=fields.get("Asset Brief") or fields.get("Visual Brief") or fields.get("Audio Brief") or "",
                size=fields.get("Size", ""),
                content=content,
                order=len(asset_ids),
            )
            current_section.categories[current_category].append(entry)
            continue
        i += 1

    if current_section is not None and not current_section.owner_id:
        raise ValueError(f"Production Asset section {current_section.title} requires Owner ID")
    if not sections:
        raise ValueError("Production Asset requirements contain no sections.")
    if not asset_ids:
        raise ValueError("Production Asset requirements contain no asset entries.")
    return AssetRequirements(tuple(sections))


def _presentation(render_data: dict[str, Any], owner_id: str, display_title: str) -> SectionPresentation:
    if owner_id == "shared":
        return SectionPresentation(owner_id, "Global / Shared Assets", bi("Shared", "Shared"), "production-assets-global-shared")
    if owner_id.startswith("package:"):
        package_id = owner_id.split(":", 1)[1]
        for index, package in enumerate(render_data.get("packages", [])):
            if str(package.get("id")) == package_id:
                title = txt(package.get("title", display_title))["en"]
                return SectionPresentation(owner_id, title, package.get("package_label", f"Gameplay {index + 1}"), f"production-assets-{slug(package_id)}")
        raise ValueError(f"Production Asset owner does not match an accepted package: {owner_id}")
    if owner_id.startswith("journey:"):
        flow_id = owner_id.split(":", 1)[1]
        flow_items = render_data.get("gameplay_flow", [])
        for index, item in enumerate(flow_items):
            if str(item.get("id")) == flow_id:
                title = txt(item.get("title", display_title))["en"]
                label = "Introduction" if index == 0 else "Ending" if index == len(flow_items) - 1 else "Journey"
                return SectionPresentation(owner_id, title, bi(label, label), f"production-assets-journey-{slug(flow_id)}")
        raise ValueError(f"Production Asset owner does not match an accepted journey flow: {owner_id}")
    raise ValueError(f"Unsupported Production Asset Owner ID: {owner_id}")


def _ordered_owner_ids(render_data: dict[str, Any], owners: set[str]) -> list[str]:
    ordered: list[str] = []
    remaining = set(owners)
    if "shared" in remaining:
        ordered.append("shared")
        remaining.remove("shared")
    for item in render_data.get("gameplay_flow", []):
        owner = f"journey:{item.get('id')}"
        if owner in remaining:
            ordered.append(owner)
            remaining.remove(owner)
    for package in render_data.get("packages", []):
        owner = f"package:{package.get('id')}"
        if owner in remaining:
            ordered.append(owner)
            remaining.remove(owner)
    if remaining:
        raise ValueError("Production Assets contain Owner ID(s) outside accepted PRD topology: " + ", ".join(sorted(remaining)))
    return ordered


def _asset_entries(section: AssetSection | None) -> list[AssetEntry]:
    if section is None:
        return []
    return [entry for category in ASSET_CATEGORIES for entry in section.categories.get(category, [])]


def _flow_order(section: AssetSection | None, flow: str) -> int:
    if not flow:
        return 999
    if section and flow in section.flow_order:
        return section.flow_order[flow]
    match = re.match(r"^\s*(\d+)", flow)
    return int(match.group(1)) if match else 999


def _copy_button(target_id: str, label: str) -> str:
    return f'<button class="pa-copy-button" data-pa-copy="{esc(target_id)}" type="button"><span class="pa-copy-label">{esc(label)}</span></button>'


def _asset_to_item(entry: AssetEntry, section: AssetSection | None, page_id: str) -> ProductionItem:
    return ProductionItem(
        item_id=f"{page_id}-build-{slug(entry.asset_id)}",
        title=entry.title,
        type_label=entry.type_label,
        function_text=entry.function_text,
        moment=entry.moment,
        flow_order=_flow_order(section, entry.flow),
        sort_order=entry.order,
        asset_brief=entry.asset_brief,
        size=entry.size,
        content=entry.content,
    )


def _voice_to_item(entry: voice.VoiceEntry, doc: voice.VoiceProduction, page_id: str, requirement: VoiceRequirement, order: int) -> ProductionItem:
    return ProductionItem(
        item_id=f"{page_id}-build-{slug(entry.voice_id)}",
        title=f"{entry.speaker} — {entry.title}",
        type_label="AUDIO",
        function_text=" ".join(requirement.function.replace("_", " ").split()).capitalize(),
        moment=entry.title,
        flow_order=999,
        sort_order=order,
        content=entry.performance,
        speaker=entry.speaker,
        selected_voice=voice._voice_for(doc.cast, entry.speaker),
        duration=entry.duration,
        is_voice=True,
    )


def _item_sort_key(item: ProductionItem) -> tuple[int, int, int, str]:
    return TYPE_PRIORITY.get(item.type_label.upper(), 500), item.flow_order, item.sort_order, item.title.casefold()


def _reader_section_title(meta: SectionPresentation) -> str:
    label = txt(meta.package_label)["en"].strip()
    name = meta.title.strip()
    if label.casefold().startswith("objective"):
        return f"{label} · {re.sub(r'^The\s+', '', name, flags=re.I)}"
    if label.casefold() == "introduction":
        return f"Introduction · {name}"
    if label.casefold() == "ending":
        return f"Ending · {name}"
    if label.casefold() == "shared":
        return "Shared Assets"
    return f"{label} · {name}" if label else name


def _build_item_html(item: ProductionItem) -> str:
    exact = ""
    if item.content:
        if item.is_voice:
            target = "voice-prompt-" + item.item_id.split("-build-")[-1]
            exact = '<div class="pa-exact pa-audio-prompt"><div class="pa-exact-head">' + f'<span>Prompt</span>{_copy_button(target, "Copy Prompt")}</div>' + f'<pre class="voice-script-text" id="{esc(target)}">{esc(item.content)}</pre>' + f'<div class="voice-script-display">{voice._performance_html(item.content)}</div></div>'
        else:
            target = f"{item.item_id}-copy"
            exact = '<div class="pa-exact"><div class="pa-exact-head">' + f'<span>Player Text</span>{_copy_button(target, "Copy Text")}</div>' + f'<pre class="pa-content" id="{esc(target)}">{esc(item.content)}</pre></div>'
    meta = '<div class="pa-build-meta-row"><b>Function</b><span>' + esc(item.function_text) + '</span></div>'
    if item.is_voice:
        meta += '<div class="pa-build-meta-row"><b>Voice Preset</b><span>' + esc(item.selected_voice) + '</span></div>'
        meta += '<div class="pa-build-meta-row"><b>ElevenLabs Model</b><span>Eleven v3</span></div>'
        meta += '<div class="pa-build-meta-row"><b>Estimated Duration</b><span>' + esc(item.duration) + '</span></div>'
    elif item.asset_brief:
        brief_label = "Audio Brief" if item.type_label.upper() == "AUDIO" else "Visual Brief"
        meta += '<div class="pa-build-meta-row"><b>' + brief_label + '</b><span>' + esc(item.asset_brief) + '</span></div>'
        if item.size:
            meta += '<div class="pa-build-meta-row"><b>Size</b><span>' + esc(item.size) + '</span></div>'
    type_class = "pa-type-" + slug(item.type_label)
    cls = "pa-row pa-row-voice" if item.is_voice else "pa-build-row pa-row"
    return f'<article class="{cls}" id="{esc(item.item_id)}"><div class="pa-build-head"><span class="pa-type {type_class}">{esc(item.type_label)}</span><h4>{esc(item.title)}</h4></div><div class="pa-build-meta">{meta}</div>{exact}</article>'


def _moment_html(items: list[ProductionItem]) -> str:
    grouped: dict[str, list[ProductionItem]] = {}
    for item in items:
        grouped.setdefault(item.moment, []).append(item)
    moments = sorted(grouped, key=lambda moment: (min(x.flow_order for x in grouped[moment]), min(x.sort_order for x in grouped[moment])))
    out: list[str] = []
    for index, moment in enumerate(moments, 1):
        out.append('<div class="pa-moment"><div class="pa-moment-head">' + f'<span>{index:02d}</span><h3>{esc(moment)}</h3></div><div class="pa-build-list">' + ''.join(_build_item_html(item) for item in sorted(grouped[moment], key=_item_sort_key)) + '</div></div>')
    return ''.join(out)


def _pages_and_nav(render_data: dict[str, Any], assets: AssetRequirements | None, voice_doc: voice.VoiceProduction | None, requirements_path: Path) -> tuple[str, str]:
    asset_map = {section.owner_id: section for section in (assets.sections if assets else ())}
    voice_map = {section.owner_id: section for section in (voice_doc.sections if voice_doc else ())}
    owners = set(asset_map) | set(voice_map)
    requirements = parse_requirements(requirements_path) if voice_doc else {}
    brand = render_data["document"].get("brand") or render_data["document"]["title"]
    pages: list[str] = []
    links: list[str] = []

    for owner_id in _ordered_owner_ids(render_data, owners):
        asset_section = asset_map.get(owner_id)
        voice_section = voice_map.get(owner_id)
        display_title = asset_section.title if asset_section else voice_section.title if voice_section else owner_id
        meta = _presentation(render_data, owner_id, display_title)
        items = [_asset_to_item(entry, asset_section, meta.page_id) for entry in _asset_entries(asset_section)]
        if voice_section and voice_doc:
            for order, entry in enumerate(voice_section.entries, 1):
                requirement = requirements.get(entry.voice_id)
                if requirement is None:
                    raise ValueError(f"Voice Production entry is missing current Voice requirement: {entry.voice_id}")
                items.append(_voice_to_item(entry, voice_doc, meta.page_id, requirement, order))
        if not items:
            continue
        body = '<header class="pa-shell">' + f'<h2>{esc(_reader_section_title(meta))}</h2></header><div class="pa-moments">{_moment_html(items)}</div>'
        pages.append(page(meta.page_id, f"PA-{len(pages) + 1:02d}", bi("Production Assets", "Aset Produksi"), body, context=meta.title, header=bi("Production Assets", "Aset Produksi"), footer_title=bi("Production Assets", "Aset Produksi"), brand=brand, role="production-assets", classes="sheet professional-only production-assets-page"))
        links.append(f'<a data-target="{meta.page_id}" href="#{meta.page_id}"><span class="production-assets-objective-name">{esc(meta.title)}</span><small>{i18n(meta.package_label)}</small></a>')

    if not pages:
        raise ValueError("Production Assets contain no renderable accepted sections.")
    nav = '<div class="nav-group is-open professional-nav production-assets-nav"><button aria-expanded="true" class="nav-group-toggle" type="button"><span class="nav-index" data-full-index="04" data-overview-index="">04</span>' + f'<span class="nav-copy">{i18n(bi("Production Assets", "Aset Produksi"))}</span><span aria-hidden="true" class="group-chevron"></span></button><div class="nav-submenu">' + ''.join(links) + '</div></div>'
    return ''.join(pages), nav


OBJECTIVE_STYLE = r'''<style id="production-assets-objective-style">
.pa-shell{margin:0 0 18px}.pa-shell h2{margin:0;color:var(--navy);font-size:1.72rem;line-height:1.14;letter-spacing:-.02em}.pa-moments{display:grid;gap:22px}.pa-moment+.pa-moment{padding-top:20px;border-top:1px solid var(--line)}.pa-moment-head{display:flex;align-items:baseline;gap:9px;margin-bottom:8px}.pa-moment-head>span{color:var(--amber);font-size:.62rem;font-weight:900}.pa-moment-head h3{margin:0;color:var(--navy);font-size:1.07rem;text-transform:none}.pa-build-list{border-top:1px solid #cbd7dd}.pa-build-row,.pa-row-voice{padding:13px 10px;border-bottom:1px solid #cbd7dd;background:var(--paper);break-inside:avoid}.pa-build-head{display:flex;flex-direction:column;align-items:flex-start;gap:5px}.pa-type{display:inline-flex;padding:4px 8px;border-radius:3px;background:var(--soft);color:var(--blue);font-size:.64rem;font-weight:900;letter-spacing:.06em;text-transform:uppercase}.pa-type-audio{background:#fff3dc;color:#8a4e00}.pa-type-ui-text{background:#eaf4fb;color:#145d83}.pa-type-model{background:#eaf6ef;color:#2d6847}.pa-type-item{background:#f0effa;color:#51458c}.pa-type-particle{background:#f5edf8;color:#74457e}.pa-build-head h4{margin:0;color:var(--navy);font-size:.94rem;line-height:1.3;text-transform:none}.pa-build-meta{display:grid;gap:8px;margin-top:10px}.pa-build-meta-row{display:block;color:#52616a;font-size:.74rem;line-height:1.48}.pa-build-meta-row b{display:block;margin-bottom:2px;color:var(--navy);font-size:.61rem;font-weight:900;letter-spacing:.035em;text-transform:uppercase}.pa-exact{margin-top:10px}.pa-exact-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:5px}.pa-exact-head>span{color:var(--blue);font-size:.61rem;font-weight:900;text-transform:uppercase}.pa-audio-prompt .pa-exact-head>span{color:#9a5a0a}.pa-copy-button{min-height:27px;padding:5px 8px;border:1px solid var(--navy);border-radius:3px;background:var(--navy);color:#fff;font:800 .56rem/1 var(--font);text-transform:uppercase}.pa-content{margin:0;padding:10px 12px;border:1px solid var(--line);border-left:3px solid var(--blue);border-radius:3px;background:#f8fafb;color:var(--navy);font:700 .76rem/1.52 var(--font);white-space:pre-wrap}.pa-row-voice .voice-script-text{display:none!important}.pa-row-voice .voice-script-display{margin:0;padding:10px 12px;border:1px solid var(--line);border-left:3px solid var(--amber);border-radius:3px;background:#f8fafb}.pa-row-voice .voice-performance-tag{display:inline-flex;margin:0 0 5px;padding:2px 6px;border-radius:3px;background:#fff0d2;color:#965700;font-size:.65rem;font-weight:900}.pa-row-voice .voice-script-line{color:var(--navy);font-size:.76rem;line-height:1.55}.pa-row-voice .voice-script-gap{height:6px}body.theme-dark .pa-build-row,body.theme-dark .pa-row-voice{background:#17262d}body.theme-dark .pa-build-meta-row{color:#c8d7dc}body.theme-dark .pa-row-voice .voice-script-display,body.theme-dark .pa-content{background:#1d2f37;color:#e8eff3}body.theme-dark .pa-type-audio{background:#3b2c13;color:#ffd284}@media print{.pa-copy-button{display:none!important}}
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
    source = _insert(source, "</body>", OBJECTIVE_COPY_SCRIPT + ("\n" + voice.VOICE_COPY_SCRIPT if has_voice else ""), "body")
    section_ids = set(re.findall(r'<section\b[^>]*\bid="([^"]+)"', source))
    targets = set(re.findall(r'data-target="([^"]+)"', nav))
    missing = sorted(targets - section_ids)
    if missing:
        raise ValueError(f"Production Assets navigation targets missing from generated pages: {missing}")
    output.write_text(source, encoding="utf-8")
