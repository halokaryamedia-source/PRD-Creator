from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from shared.assets import ASSET_CATEGORIES, AssetEntry, AssetRequirements, AssetSection, parse_asset_requirements
from shared.lifecycle import load_voice_state
from shared.topology import ordered_owner_ids, require_owner
from shared.voice import VoiceProduction, VoiceRequirement, parse_production, parse_requirements, selected_voice

from .core import bi, esc, i18n, page, slug, txt
from .production_assets import (
    SCRIPT_MARKER,
    STYLE_MARKER,
    performance_html,
    production_assets_script,
    production_assets_style,
)
from .template_adapter import TemplateAdapter

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
    moment_id: str
    moment: str
    moment_order: int
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


def _copy_button(target_id: str, label: str) -> str:
    return (
        f'<button class="pa-copy-button" data-pa-copy="{esc(target_id)}" type="button">'
        f'<span class="pa-copy-label">{esc(label)}</span></button>'
    )


def _moment_registry(
    asset_section: AssetSection | None,
    requirements: dict[str, VoiceRequirement],
    owner_id: str,
) -> dict[str, tuple[str, int]]:
    registry: dict[str, tuple[str, int]] = {}
    if asset_section is not None:
        for moment_id, order in sorted(asset_section.moment_order.items(), key=lambda item: item[1]):
            registry[moment_id] = (asset_section.moment_titles[moment_id], order)

    next_order = max((order for _, order in registry.values()), default=0) + 1
    for requirement in requirements.values():
        if requirement.owner_id != owner_id:
            continue
        existing = registry.get(requirement.moment_id)
        if existing is not None:
            if existing[0] != requirement.moment:
                raise ValueError(
                    f"Moment ID {requirement.moment_id} has conflicting Asset/Voice titles: "
                    f"{existing[0]!r} vs {requirement.moment!r}"
                )
            continue
        registry[requirement.moment_id] = (requirement.moment, next_order)
        next_order += 1
    return registry


def _asset_to_item(entry: AssetEntry, page_id: str, registry: dict[str, tuple[str, int]]) -> ProductionItem:
    moment_title, moment_order = registry[entry.moment_id]
    return ProductionItem(
        item_id=f"{page_id}-build-{slug(entry.asset_id)}",
        title=entry.title,
        type_label=entry.type_label,
        function_text=entry.function_text,
        moment_id=entry.moment_id,
        moment=moment_title,
        moment_order=moment_order,
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
    registry: dict[str, tuple[str, int]],
    order: int,
) -> ProductionItem:
    moment_title, moment_order = registry[requirement.moment_id]
    return ProductionItem(
        item_id=f"{page_id}-build-{slug(entry.voice_id)}",
        title=f"{entry.speaker} — {entry.title}",
        type_label="AUDIO",
        function_text=" ".join(requirement.function.replace("_", " ").split()).capitalize(),
        moment_id=requirement.moment_id,
        moment=moment_title,
        moment_order=moment_order,
        sort_order=order,
        content=entry.performance,
        selected_voice=selected_voice(doc.cast, entry.speaker) or "Voice selection pending",
        duration=entry.duration,
        is_voice=True,
    )


def _item_sort_key(item: ProductionItem) -> tuple[int, int, str]:
    return TYPE_PRIORITY[item.type_label], item.sort_order, item.title.casefold()


def _reader_section_title(meta: SectionPresentation) -> str:
    label = txt(meta.package_label)["en"].strip()
    name = meta.title.strip()
    if label.casefold().startswith("objective"):
        short_name = re.sub(r"^The\s+", "", name, flags=re.I)
        return f"{label} · {short_name}"
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
                f"<span>Prompt</span>{_copy_button(target, 'Copy Prompt')}</div>"
                f'<pre class="voice-script-text" id="{esc(target)}">{esc(item.content)}</pre>'
                f'<div class="voice-script-display">{performance_html(item.content)}</div></div>'
            )
        else:
            target = f"{item.item_id}-copy"
            exact = (
                '<div class="pa-exact"><div class="pa-exact-head">'
                f"<span>Player Text</span>{_copy_button(target, 'Copy Text')}</div>"
                f'<pre class="pa-content" id="{esc(target)}">{esc(item.content)}</pre></div>'
            )
    meta = '<div class="pa-build-meta-row"><b>Function</b><span>' + esc(item.function_text) + "</span></div>"
    if item.is_voice:
        meta += '<div class="pa-build-meta-row"><b>Voice Preset</b><span>' + esc(item.selected_voice) + "</span></div>"
        meta += '<div class="pa-build-meta-row"><b>ElevenLabs Model</b><span>Eleven v3</span></div>'
        meta += '<div class="pa-build-meta-row"><b>Estimated Duration</b><span>' + esc(item.duration) + "</span></div>"
    elif item.asset_brief:
        brief_label = "Audio Brief" if item.type_label == "AUDIO" else "Visual Brief"
        meta += (
            '<div class="pa-build-meta-row"><b>' + brief_label + "</b><span>" + esc(item.asset_brief) + "</span></div>"
        )
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
        grouped.setdefault(item.moment_id, []).append(item)
    moment_ids = sorted(grouped, key=lambda key: min(item.moment_order for item in grouped[key]))
    out: list[str] = []
    for index, moment_id in enumerate(moment_ids, 1):
        moment_items = grouped[moment_id]
        titles = {item.moment for item in moment_items}
        if len(titles) != 1:
            raise ValueError(f"Moment ID {moment_id} has conflicting display titles")
        moment = next(iter(titles))
        children = "".join(_build_item_html(item) for item in sorted(moment_items, key=_item_sort_key))
        out.append(
            '<div class="pa-moment" data-moment-id="' + esc(moment_id) + '"><div class="pa-moment-head">'
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


def _assert_delivery_voice_cast(work: Path, voice_doc: VoiceProduction | None) -> None:
    if voice_doc is None:
        return
    state_path = work.parent / "state" / "voice-state.yaml"
    if not state_path.is_file():
        return
    state = load_voice_state(state_path)
    if state.status != "voice_delivery_ready":
        return
    speakers = sorted({entry.speaker for section in voice_doc.sections for entry in section.entries})
    missing = [speaker for speaker in speakers if not selected_voice(voice_doc.cast, speaker)]
    if missing:
        raise ValueError(
            "voice_delivery_ready cannot render unresolved Voice Cast selection/profile for: " + ", ".join(missing)
        )


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
        registry = _moment_registry(asset_section, requirements, owner_id)
        items = [_asset_to_item(entry, meta.page_id, registry) for entry in _asset_entries(asset_section)]
        if voice_section and voice_doc:
            section_ids = {entry.voice_id for entry in voice_section.entries}
            expected_ids = requirement_owners.get(owner_id, set())
            if section_ids != expected_ids:
                missing = sorted(expected_ids - section_ids)
                extra = sorted(section_ids - expected_ids)
                raise ValueError(f"Voice Owner ID parity mismatch for {owner_id}; missing={missing}, extra={extra}")
            for order, entry in enumerate(voice_section.entries, 1):
                requirement = requirements[entry.voice_id]
                if requirement.owner_id != owner_id:
                    raise ValueError(f"Voice requirement Owner ID mismatch for {entry.voice_id}")
                items.append(_voice_to_item(entry, voice_doc, meta.page_id, requirement, registry, order))
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
            f"<small>{i18n(meta.package_label)}</small></a>"
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
    _assert_delivery_voice_cast(work, voice_doc)

    source = output.read_text(encoding="utf-8")
    if STYLE_MARKER in source or SCRIPT_MARKER in source:
        raise ValueError("Production Assets extension already exists in rendered HTML")

    pages, nav = _pages_and_nav(render_data, assets, voice_doc, requirements_path)
    adapter = TemplateAdapter(source)
    adapter.append_navigation(nav)
    adapter.append_document_main(pages)

    head_additions = production_assets_style()
    if has_assets:
        asset_sha = hashlib.sha256(asset_path.read_bytes()).hexdigest()
        head_additions += f'\n<meta content="{asset_sha}" name="asset-requirements-sha256"/>'
    if has_voice:
        requirements_sha = hashlib.sha256(requirements_path.read_bytes()).hexdigest()
        production_sha = hashlib.sha256(voice_production_path.read_bytes()).hexdigest()
        head_additions += f'\n<meta content="{requirements_sha}" name="voice-requirements-sha256"/>'
        head_additions += f'\n<meta content="{production_sha}" name="voice-production-sha256"/>'
    adapter.inject_head(head_additions)
    adapter.inject_body(production_assets_script())

    source = adapter.source
    section_ids = set(re.findall(r'<section\b[^>]*\bid="([^"]+)"', source))
    targets = set(re.findall(r'data-target="([^"]+)"', nav))
    missing = sorted(targets - section_ids)
    if missing:
        raise ValueError(f"Production Assets navigation targets missing from generated pages: {missing}")
    output.write_text(source, encoding="utf-8")
