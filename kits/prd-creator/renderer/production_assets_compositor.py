from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .core import bi, esc, i18n, page, slug, txt
from .production_assets import STYLE_MARKER, VOICE_COPY_SCRIPT, VOICE_STYLE, performance_html
from shared.assets import ASSET_CATEGORIES, AssetEntry, AssetRequirements, AssetSection, parse_asset_requirements
from shared.topology import ordered_owner_ids, require_owner
from shared.voice import VoiceProduction, VoiceRequirement, parse_production, parse_requirements, selected_voice

OBJECTIVE_STYLE_MARKER = 'id="production-assets-objective-style"'
TYPE_PRIORITY = {"MODEL": 10, "ITEM": 20, "UI / TEXT": 30, "AUDIO": 40, "PARTICLE": 50}


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
    selected_voice: str = ""
    duration: str = ""
    is_voice: bool = False


def _presentation(render_data: dict[str, Any], owner_id: str) -> SectionPresentation:
    target = require_owner(render_data, owner_id)
    if target.kind == "shared":
        page_id = "production-assets-global-shared"
    elif target.kind == "package":
        page_id = f"production-assets-{slug(target.stable_id)}"
    else:
        page_id = f"production-assets-journey-{slug(target.stable_id)}"
    return SectionPresentation(target.owner_id, target.title, target.label, page_id)


def _asset_entries(section: AssetSection | None) -> list[AssetEntry]:
    if section is None:
        return []
    return [entry for category in ASSET_CATEGORIES for entry in section.categories.get(category, [])]


def _flow_order(section: AssetSection | None, flow: str) -> int:
    if not flow:
        return 999
    if section and flow in section.flow_order:
        return section.flow_order[flow]
    return 999


def _copy_button(target_id: str, label: str) -> str:
    return (
        f'<button class="pa-copy-button" data-pa-copy="{esc(target_id)}" type="button">'
        f'<span class="pa-copy-label">{esc(label)}</span></button>'
    )


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


def _voice_to_item(
    entry: Any,
    doc: VoiceProduction,
    page_id: str,
    requirement: VoiceRequirement,
    order: int,
) -> ProductionItem:
    return ProductionItem(
        item_id=f"{page_id}-build-{slug(entry.voice_id)}",
        title=f"{entry.speaker} — {entry.title}",
        type_label="AUDIO",
        function_text=" ".join(requirement.function.replace("_", " ").split()).capitalize(),
        moment=requirement.moment,
        flow_order=999,
        sort_order=order,
        content=entry.performance,
        selected_voice=selected_voice(doc.cast, entry.speaker) or "Voice selection pending",
        duration=entry.duration,
        is_voice=True,
    )


def _item_sort_key(item: ProductionItem) -> tuple[int, int, int, str]:
    return TYPE_PRIORITY[item.type_label], item.flow_order, item.sort_order, item.title.casefold()


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
            exact = (
                '<div class="pa-exact pa-audio-prompt"><div class="pa-exact-head">'
                f'<span>Prompt</span>{_copy_button(target, "Copy Prompt")}</div>'
                f'<pre class="voice-script-text" id="{esc(target)}">{esc(item.content)}</pre>'
                f'<div class="voice-script-display">{performance_html(item.content)}</div></div>'
            )
        else:
            target = f"{item.item_id}-copy"
            exact = (
                '<div class="pa-exact"><div class="pa-exact-head">'
                f'<span>Player Text</span>{_copy_button(target, "Copy Text")}</div>'
                f'<pre class="pa-content" id="{esc(target)}">{esc(item.content)}</pre></div>'
            )
    meta = '<div class="pa-build-meta-row"><b>Function</b><span>' + esc(item.function_text) + "</span></div>"
    if item.is_voice:
        meta += '<div class="pa-build-meta-row"><b>Voice Preset</b><span>' + esc(item.selected_voice) + "</span></div>"
        meta += '<div class="pa-build-meta-row"><b>ElevenLabs Model</b><span>Eleven v3</span></div>'
        meta += '<div class="pa-build-meta-row"><b>Estimated Duration</b><span>' + esc(item.duration) + "</span></div>"
    elif item.asset_brief:
        brief_label = "Audio Brief" if item.type_label == "AUDIO" else "Visual Brief"
        meta += '<div class="pa-build-meta-row"><b>' + brief_label + "</b><span>" + esc(item.asset_brief) + "</span></div>"
        if item.size:
            meta += '<div class="pa-build-meta-row"><b>Size</b><span>' + esc(item.size) + "</span></div>"
    type_class = "pa-type-" + slug(item.type_label)
    cls = "pa-row pa-row-voice" if item.is_voice else "pa-build-row pa-row"
    return (
        f'<article class="{cls}" id="{esc(item.item_id)}"><div class="pa-build-head">'
        f'<span class="pa-type {type_class}">{esc(item.type_label)}</span><h4>{esc(item.title)}</h4></div>'
        f'<div class="pa-build-meta">{meta}</div>{exact}</article>'
    )


def _moment_html(items: list[ProductionItem]) -> str:
    grouped: dict[str, list[ProductionItem]] = {}
    for item in items:
        grouped.setdefault(item.moment, []).append(item)
    moments = sorted(
        grouped,
        key=lambda moment: (
            min(item.flow_order for item in grouped[moment]),
            min(item.sort_order for item in grouped[moment]),
        ),
    )
    out: list[str] = []
    for index, moment in enumerate(moments, 1):
        children = "".join(_build_item_html(item) for item in sorted(grouped[moment], key=_item_sort_key))
        out.append(
            '<div class="pa-moment"><div class="pa-moment-head">'
            f'<span>{index:02d}</span><h3>{esc(moment)}</h3></div><div class="pa-build-list">{children}</div></div>'
        )
    return "".join(out)


def _voice_owner_map(voice_doc: VoiceProduction) -> dict[str, Any]:
    return {section.owner_id: section for section in voice_doc.sections}


def _requirements_by_owner(requirements: dict[str, VoiceRequirement]) -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    for requirement in requirements.values():
        result.setdefault(requirement.owner_id, set()).add(requirement.voice_id)
    return result


def _pages_and_nav(
    render_data: dict[str, Any],
    assets: AssetRequirements | None,
    voice_doc: VoiceProduction | None,
    requirements_path: Path,
) -> tuple[str, str]:
    asset_map = {section.owner_id: section for section in (assets.sections if assets else ())}
    voice_map = _voice_owner_map(voice_doc) if voice_doc else {}
    owners = set(asset_map) | set(voice_map)
    requirements = parse_requirements(requirements_path) if voice_doc else {}
    requirement_owners = _requirements_by_owner(requirements)
    brand = render_data["document"].get("brand") or render_data["document"]["title"]
    pages: list[str] = []
    links: list[str] = []

    for owner_id in ordered_owner_ids(render_data, owners):
        meta = _presentation(render_data, owner_id)
        asset_section = asset_map.get(owner_id)
        voice_section = voice_map.get(owner_id)
        items = [_asset_to_item(entry, asset_section, meta.page_id) for entry in _asset_entries(asset_section)]
        if voice_section and voice_doc:
            section_ids = {entry.voice_id for entry in voice_section.entries}
            expected_ids = requirement_owners.get(owner_id, set())
            if section_ids != expected_ids:
                missing = sorted(expected_ids - section_ids)
                extra = sorted(section_ids - expected_ids)
                raise ValueError(
                    f"Voice Owner ID parity mismatch for {owner_id}; missing={missing}, extra={extra}"
                )
            for order, entry in enumerate(voice_section.entries, 1):
                requirement = requirements[entry.voice_id]
                if requirement.owner_id != owner_id:
                    raise ValueError(f"Voice requirement Owner ID mismatch for {entry.voice_id}")
                items.append(_voice_to_item(entry, voice_doc, meta.page_id, requirement, order))
        if not items:
            continue
        body = (
            '<header class="pa-shell">'
            f'<h2>{esc(_reader_section_title(meta))}</h2></header><div class="pa-moments">{_moment_html(items)}</div>'
        )
        pages.append(
            page(
                meta.page_id,
                f"PA-{len(pages) + 1:02d}",
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
            f'<a data-target="{meta.page_id}" href="#{meta.page_id}">'
            f'<span class="production-assets-objective-name">{esc(meta.title)}</span>'
            f'<small>{i18n(meta.package_label)}</small></a>'
        )

    if not pages:
        raise ValueError("Production Assets contain no renderable accepted sections")
    nav = (
        '<div class="nav-group is-open professional-nav production-assets-nav">'
        '<button aria-expanded="true" class="nav-group-toggle" type="button">'
        '<span class="nav-index" data-full-index="04" data-overview-index="">04</span>'
        f'<span class="nav-copy">{i18n(bi("Production Assets", "Aset Produksi"))}</span>'
        '<span aria-hidden="true" class="group-chevron"></span></button><div class="nav-submenu">'
        + "".join(links)
        + "</div></div>"
    )
    return "".join(pages), nav


OBJECTIVE_STYLE = r'''<style id="production-assets-objective-style">
.pa-shell{margin:0 0 18px}.pa-shell h2{margin:0;color:var(--navy);font-size:1.72rem;line-height:1.14;letter-spacing:-.02em}.pa-moments{display:grid;gap:22px}.pa-moment+.pa-moment{padding-top:20px;border-top:1px solid var(--line)}.pa-moment-head{display:flex;align-items:baseline;gap:9px;margin-bottom:8px}.pa-moment-head>span{color:var(--amber);font-size:.62rem;font-weight:900}.pa-moment-head h3{margin:0;color:var(--navy);font-size:1.07rem;text-transform:none}.pa-build-list{border-top:1px solid #cbd7dd}.pa-build-row,.pa-row-voice{padding:13px 10px;border-bottom:1px solid #cbd7dd;background:var(--paper);break-inside:avoid}.pa-build-head{display:flex;flex-direction:column;align-items:flex-start;gap:5px}.pa-type{display:inline-flex;padding:4px 8px;border-radius:3px;background:var(--soft);color:var(--blue);font-size:.64rem;font-weight:900;letter-spacing:.06em;text-transform:uppercase}.pa-type-audio{background:#fff3dc;color:#8a4e00}.pa-type-ui-text{background:#eaf4fb;color:#145d83}.pa-type-model{background:#eaf6ef;color:#2d6847}.pa-type-item{background:#f0effa;color:#51458c}.pa-type-particle{background:#f5edf8;color:#74457e}.pa-build-head h4{margin:0;color:var(--navy);font-size:.94rem;line-height:1.3;text-transform:none}.pa-build-meta{display:grid;gap:8px;margin-top:10px}.pa-build-meta-row{display:block;color:#52616a;font-size:.74rem;line-height:1.48}.pa-build-meta-row b{display:block;margin-bottom:2px;color:var(--navy);font-size:.61rem;font-weight:900;letter-spacing:.035em;text-transform:uppercase}.pa-exact{margin-top:10px}.pa-exact-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:5px}.pa-exact-head>span{color:var(--blue);font-size:.61rem;font-weight:900;text-transform:uppercase}.pa-audio-prompt .pa-exact-head>span{color:#9a5a0a}.pa-copy-button{min-height:27px;padding:5px 8px;border:1px solid var(--navy);border-radius:3px;background:var(--navy);color:#fff;font:800 .56rem/1 var(--font);text-transform:uppercase}.pa-content{margin:0;padding:10px 12px;border:1px solid var(--line);border-left:3px solid var(--blue);border-radius:3px;background:#f8fafb;color:var(--navy);font:700 .76rem/1.52 var(--font);white-space:pre-wrap}.pa-row-voice .voice-script-text{display:none!important}.pa-row-voice .voice-script-display{margin:0;padding:10px 12px;border:1px solid var(--line);border-left:3px solid var(--amber);border-radius:3px;background:#f8fafb}.pa-row-voice .voice-performance-tag{display:inline-flex;margin:0 0 5px;padding:2px 6px;border-radius:3px;background:#fff0d2;color:#965700;font-size:.65rem;font-weight:900}.pa-row-voice .voice-script-line{color:var(--navy);font-size:.76rem;line-height:1.55}.pa-row-voice .voice-script-gap{height:6px}body.theme-dark .pa-build-row,body.theme-dark .pa-row-voice{background:#17262d}body.theme-dark .pa-build-meta-row{color:#c8d7dc}body.theme-dark .pa-row-voice .voice-script-display,body.theme-dark .pa-content{background:#1d2f37;color:#e8eff3}body.theme-dark .pa-type-audio{background:#3b2c13;color:#ffd284}@media print{.pa-copy-button{display:none!important}}
</style>'''

OBJECTIVE_COPY_SCRIPT = r'''<script id="production-assets-flow-copy-script">(function(){
  function fallbackCopy(text){var area=document.createElement('textarea');area.value=text;area.setAttribute('readonly','');area.style.position='fixed';area.style.opacity='0';document.body.appendChild(area);area.select();try{document.execCommand('copy');}finally{document.body.removeChild(area);}}
  document.addEventListener('click',function(event){var button=event.target.closest('[data-pa-copy]');if(!button)return;var source=document.getElementById(button.getAttribute('data-pa-copy'));if(!source)return;var text=source.textContent||'';var label=button.querySelector('.pa-copy-label');var original=label?label.textContent:'Copy';var done=function(){button.classList.add('is-copied');if(label)label.textContent='Copied ✓';setTimeout(function(){button.classList.remove('is-copied');if(label)label.textContent=original;},1400);};if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(done,function(){fallbackCopy(text);done();});}else{fallbackCopy(text);done();}});
})();</script>'''


def _insert(source: str, closing: str, addition: str, label: str) -> str:
    if source.count(closing) != 1:
        raise ValueError(f"Rendered HTML requires exactly one {label} closing marker")
    return source.replace(closing, addition + "\n" + closing, 1)


def augment_project_html(render_data_path: Path, output: Path, voice_production_path: Path) -> None:
    work = voice_production_path.parent
    asset_path = work / "asset-requirements.md"
    requirements_path = work / "voice-requirements.md"
    has_assets = asset_path.is_file()
    has_voice = voice_production_path.is_file()
    if not has_assets and not has_voice:
        return
    if has_voice and not requirements_path.is_file():
        raise ValueError("Voice Production requires current work/voice-requirements.md")

    render_data = json.loads(render_data_path.read_text(encoding="utf-8"))
    assets = parse_asset_requirements(asset_path) if has_assets else None
    voice_doc = parse_production(voice_production_path) if has_voice else None
    source = output.read_text(encoding="utf-8")
    if STYLE_MARKER in source or OBJECTIVE_STYLE_MARKER in source:
        raise ValueError("Production Assets extension already exists in rendered HTML")

    pages, nav = _pages_and_nav(render_data, assets, voice_doc, requirements_path)
    nav_pattern = re.compile(r'(<nav class="sidebar-nav">)(.*?)(</nav>)', re.S)
    main_pattern = re.compile(r'(<main class="document-main">.*?)(</main>)', re.S)
    if len(nav_pattern.findall(source)) != 1:
        raise ValueError("Rendered HTML requires exactly one sidebar navigation container")
    if len(main_pattern.findall(source)) != 1:
        raise ValueError("Rendered HTML requires exactly one document main container")
    source = nav_pattern.sub(lambda match: match.group(1) + match.group(2) + nav + match.group(3), source, count=1)
    source = main_pattern.sub(lambda match: match.group(1) + pages + match.group(2), source, count=1)

    head_additions = VOICE_STYLE + OBJECTIVE_STYLE
    if has_assets:
        asset_sha = hashlib.sha256(asset_path.read_bytes()).hexdigest()
        head_additions += f'\n<meta content="{asset_sha}" name="asset-requirements-sha256"/>'
    if has_voice:
        requirements_sha = hashlib.sha256(requirements_path.read_bytes()).hexdigest()
        production_sha = hashlib.sha256(voice_production_path.read_bytes()).hexdigest()
        head_additions += f'\n<meta content="{requirements_sha}" name="voice-requirements-sha256"/>'
        head_additions += f'\n<meta content="{production_sha}" name="voice-production-sha256"/>'
    source = _insert(source, "</head>", head_additions, "head")
    source = _insert(
        source,
        "</body>",
        OBJECTIVE_COPY_SCRIPT + ("\n" + VOICE_COPY_SCRIPT if has_voice else ""),
        "body",
    )

    section_ids = set(re.findall(r'<section\b[^>]*\bid="([^"]+)"', source))
    targets = set(re.findall(r'data-target="([^"]+)"', nav))
    missing = sorted(targets - section_ids)
    if missing:
        raise ValueError(f"Production Assets navigation targets missing from generated pages: {missing}")
    output.write_text(source, encoding="utf-8")
