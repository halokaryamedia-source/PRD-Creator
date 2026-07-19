#!/usr/bin/env python3
"""Semantic HTML renderer for Production Document Builder v0.1."""
from __future__ import annotations

import hashlib
import html
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

import yaml

SUPPORTED_LANGS = ("en", "id")

PROFILE_LABELS: dict[str, dict[str, str]] = {
    "complete_game_map": {"en": "Production Specification", "id": "Spesifikasi Produksi"},
    "multi_stage_game": {"en": "Multi-Stage Production Specification", "id": "Spesifikasi Produksi Multi-Stage"},
    "single_gameplay": {"en": "Gameplay Specification", "id": "Spesifikasi Gameplay"},
    "game_system_module": {"en": "System Specification", "id": "Spesifikasi Sistem"},
    "specialized_document": {"en": "Specialized Production Document", "id": "Dokumen Produksi Khusus"},
}

SPECIALIZATION_LABELS: dict[str, dict[str, str]] = {
    "gameplay_design_only": {"en": "Gameplay Design", "id": "Desain Gameplay"},
    "level_design_only": {"en": "Level Design", "id": "Desain Level"},
    "developer_only": {"en": "Developer Specification", "id": "Spesifikasi Developer"},
    "scoring_and_data_only": {"en": "Scoring and Data", "id": "Scoring dan Data"},
    "audit_only": {"en": "Audit Report", "id": "Laporan Audit"},
}

PAGE_LABELS: dict[str, dict[str, str]] = {
    "overview": {"en": "Overview", "id": "Gambaran Umum"},
    "gameplay_flow": {"en": "Gameplay Flow", "id": "Alur Gameplay"},
    "development": {"en": "Development", "id": "Pengembangan"},
    "gameplay_overview": {"en": "Gameplay Overview", "id": "Gameplay Overview"},
    "level_design": {"en": "Level Design", "id": "Desain Level"},
    "developer": {"en": "Developer", "id": "Developer"},
    "system_overview": {"en": "System Overview", "id": "Gambaran Umum Sistem"},
    "system_flow": {"en": "System Flow", "id": "Alur Sistem"},
}

PACKAGE_TYPE_LABELS: dict[str, dict[str, str]] = {
    "introduction": {"en": "Introduction", "id": "Pendahuluan"},
    "objective": {"en": "Objective", "id": "Objektif"},
    "transition": {"en": "Transition", "id": "Transisi"},
    "ending": {"en": "Ending", "id": "Penutup"},
    "stage": {"en": "Stage", "id": "Stage"},
    "station": {"en": "Station", "id": "Station"},
    "standalone_gameplay": {"en": "Standalone Gameplay", "id": "Gameplay Mandiri"},
}

PLACEHOLDER_PATTERN = re.compile(
    r"\b(?:TBD|TODO|FIXME|INSERT\s+(?:TEXT|SCORE|VALUE)|USE\s+APPROVED\s+AMOUNT)\b",
    re.IGNORECASE,
)


def read_data(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        data = json.loads(text)
    else:
        data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise ValueError(f"Root value must be an object: {path}")
    return data


def write_yaml(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def canonical_data_hash(data: Any) -> str:
    payload = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def esc(value: Any) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def normalize_text(value: Any) -> dict[str, str]:
    if isinstance(value, dict):
        en = value.get("en")
        ind = value.get("id")
        if en is None and ind is not None:
            en = ind
        if ind is None and en is not None:
            ind = en
        return {"en": "" if en is None else str(en), "id": "" if ind is None else str(ind)}
    text = "" if value is None else str(value)
    return {"en": text, "id": text}


def i18n(value: Any, *, tag: str = "span", class_name: str = "i18n-text") -> str:
    text = normalize_text(value)
    return (
        f'<{tag} class="{esc(class_name)}" data-en="{esc(text["en"])}" '
        f'data-id="{esc(text["id"])}">{esc(text["en"])}</{tag}>'
    )


def i18n_text(value: Any) -> str:
    return i18n(value)


def localized_join(parts: Iterable[Any], separator: str = " · ") -> dict[str, str]:
    normalized = [normalize_text(part) for part in parts]
    return {
        lang: separator.join(item[lang] for item in normalized if item[lang])
        for lang in SUPPORTED_LANGS
    }


def bilingual_label(en: str, ind: str | None = None) -> dict[str, str]:
    return {"en": en, "id": ind if ind is not None else en}


def paragraphs(value: Any, class_name: str = "") -> str:
    text = normalize_text(value)
    classes = f' class="{esc(class_name)}"' if class_name else ""
    return f"<p{classes}>{i18n(text)}</p>"


def localized_list(items: list[Any], class_name: str = "clean-list") -> str:
    if not items:
        return ""
    return f'<ul class="{esc(class_name)}">' + "".join(f"<li>{i18n(item)}</li>" for item in items) + "</ul>"


def object_title(value: Any) -> dict[str, str]:
    if isinstance(value, dict):
        return normalize_text(value)
    return normalize_text(str(value).replace("_", " ").title())


def area_size_text(area: Any) -> dict[str, str]:
    if not isinstance(area, dict):
        return normalize_text(area)
    value = area.get("value")
    if value is None:
        return bilingual_label("Flexible", "Fleksibel")
    return normalize_text(value)


def requirement_list(items: list[Any]) -> str:
    return localized_list(items, "compact-cell-list")


def notes_from_text(items: list[Any]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for index, item in enumerate(items, 1):
        result.append(
            {
                "title": bilingual_label(f"Important Note {index}", f"Catatan Penting {index}"),
                "content": normalize_text(item),
            }
        )
    return result


def render_notes(items: list[Any]) -> str:
    notes = notes_from_text(items)
    if not notes:
        return ""
    articles = []
    for note in notes:
        articles.append(f"<article><b>{i18n(note['title'])}</b><p>{i18n(note['content'])}</p></article>")
    return '<div class="outcome quarry-note-grid">' + "".join(articles) + "</div>"


def render_flow(steps: list[dict[str, Any]], class_name: str = "flow") -> str:
    if not steps:
        return ""
    body: list[str] = []
    for step in steps:
        result = step.get("result")
        result_html = f'<p class="quiet">{i18n(result)}</p>' if result else ""
        body.append(
            "<article>"
            f'<span class="flow-number">{esc(step.get("number", ""))}</span>'
            f"<h4>{i18n(step.get('title', {}))}</h4>"
            f"<p>{i18n(step.get('description', {}))}</p>"
            f"{result_html}</article>"
        )
    return f'<div class="{esc(class_name)}">' + "".join(body) + "</div>"


def render_info_table(rows: list[tuple[dict[str, str], Any]]) -> str:
    if not rows:
        return ""
    body = "".join(f"<tr><th>{i18n(label)}</th><td>{i18n(value)}</td></tr>" for label, value in rows)
    return f'<div class="production-table-wrap"><table class="data-table"><tbody>{body}</tbody></table></div>'


def render_requirements(groups: list[dict[str, Any]]) -> str:
    if not groups:
        return ""
    rows: list[str] = []
    for group in groups:
        rows.append(
            '<tr class="quarry-group-row">'
            f'<td><b>{esc(group.get("number", ""))}</b></td>'
            f'<td colspan="3"><b>{i18n(group.get("title", {}))}</b></td></tr>'
        )
        for item in group.get("items", []):
            title = item.get("title", {})
            rows.append(
                "<tr>"
                f'<td><b>{esc(item.get("code", ""))}</b></td>'
                f"<td><b>{i18n(title)}</b></td>"
                f"<td>{requirement_list(item.get('requirements', []))}</td>"
                f"<td>{i18n(item.get('result') or bilingual_label('—', '—'))}</td>"
                "</tr>"
            )
    headings = [
        bilingual_label("No.", "No."),
        bilingual_label("Requirement", "Requirement"),
        bilingual_label("Details", "Detail"),
        bilingual_label("Expected Result", "Hasil yang Diharapkan"),
    ]
    head = "".join(f"<th>{i18n(item)}</th>" for item in headings)
    return (
        '<div class="production-table-wrap"><table class="quarry-development-table">'
        f"<thead><tr>{head}</tr></thead><tbody>{''.join(rows)}</tbody></table></div>"
    )


def render_build_requirements(groups: list[dict[str, Any]]) -> str:
    if not groups:
        return ""
    rows: list[str] = []
    for group in groups:
        rows.append(
            '<tr class="quarry-group-row">'
            f'<td><b>{esc(group.get("group_number", ""))}</b></td>'
            f'<td colspan="4"><b>{i18n(group.get("group_title", {}))}</b></td></tr>'
        )
        for item in group.get("objects", []):
            rows.append(
                "<tr>"
                f'<td><b>{esc(item.get("code", ""))}</b></td>'
                f"<td><b>{i18n(item.get('object', {}))}</b></td>"
                f"<td>{i18n(area_size_text(item.get('area_size')))}</td>"
                f"<td>{i18n(item.get('build_and_visual', {}))}</td>"
                f"<td>{i18n(item.get('gameplay_function', {}))}</td>"
                "</tr>"
            )
    headings = [
        bilingual_label("No.", "No."),
        bilingual_label("Object", "Objek"),
        bilingual_label("Area Size", "Ukuran Area"),
        bilingual_label("Build and Visual Requirements", "Kebutuhan Build dan Visual"),
        bilingual_label("Gameplay Function", "Fungsi Gameplay"),
    ]
    head = "".join(f"<th>{i18n(item)}</th>" for item in headings)
    return (
        '<div class="production-table-wrap"><table class="quarry-build-table">'
        f"<thead><tr>{head}</tr></thead><tbody>{''.join(rows)}</tbody></table></div>"
    )


def render_scoring(scoring: dict[str, Any]) -> str:
    if not scoring:
        return ""
    components: list[str] = []
    for component in scoring.get("components", []):
        components.append(
            "<tr>"
            f"<td><b>{i18n(component.get('name', {}))}</b></td>"
            f'<td><b>{esc(component.get("weight", ""))}%</b></td>'
            f"<td>{i18n(bilingual_label('Contributes to the final score.', 'Berkontribusi pada score akhir.'))}</td>"
            "</tr>"
        )
    comp_headings = [
        bilingual_label("Component", "Komponen"),
        bilingual_label("Weight", "Bobot"),
        bilingual_label("Rule", "Aturan"),
    ]
    component_head = "".join(f"<th>{i18n(item)}</th>" for item in comp_headings)
    scale = scoring.get("scale", {})
    detail_rows = [
        (bilingual_label("Score Scale", "Skala Score"), bilingual_label(f'{scale.get("minimum", "")}–{scale.get("maximum", "")}', f'{scale.get("minimum", "")}–{scale.get("maximum", "")}')),
        (bilingual_label("Standard or Target", "Standar atau Target"), scoring.get("standard_or_target", {})),
        (bilingual_label("Bonus Behavior", "Perilaku Bonus"), scoring.get("bonus_behavior", {})),
        (bilingual_label("Score Reduction", "Pengurangan Score"), scoring.get("reduction_behavior", {})),
        (bilingual_label("Timer Start", "Timer Mulai"), scoring.get("timer_start", {})),
        (bilingual_label("Timer Stop", "Timer Berhenti"), scoring.get("timer_stop", {})),
        (bilingual_label("No-Score Condition", "Kondisi Tanpa Score"), scoring.get("no_score_condition", {})),
        (bilingual_label("Duplicate Prevention", "Pencegahan Duplikasi"), scoring.get("duplicate_prevention", {})),
        (bilingual_label("Final Result Relationship", "Hubungan dengan Hasil Akhir"), scoring.get("final_result_relationship", {})),
    ]
    excluded = scoring.get("excluded_time", [])
    if excluded:
        detail_rows.insert(6, (bilingual_label("Excluded Time", "Waktu yang Tidak Dihitung"), localized_join(excluded, "; ")))
    recorded = scoring.get("recorded_data", [])
    if recorded:
        descriptions = [item.get("description", object_title(item.get("id", ""))) for item in recorded]
        detail_rows.append((bilingual_label("Recorded Data", "Data yang Dicatat"), localized_join(descriptions, "; ")))
    critical_inputs = scoring.get("critical_inputs", [])
    if critical_inputs:
        formatted = []
        for item in critical_inputs:
            formatted.append(bilingual_label(f'{item.get("id")}: {item.get("value")}', f'{item.get("id")}: {item.get("value")}'))
        detail_rows.append((bilingual_label("Critical Inputs", "Input Kritis"), localized_join(formatted, "; ")))
    return (
        '<section class="scoring-block">'
        f"<h3>{i18n(scoring.get('score_name', {}))}</h3>"
        '<div class="production-table-wrap"><table class="data-table">'
        f"<thead><tr>{component_head}</tr></thead><tbody>{''.join(components)}</tbody></table></div>"
        f"{render_info_table(detail_rows)}"
        "</section>"
    )


def render_completion_data(data: dict[str, Any]) -> str:
    if not data:
        return ""
    rows: list[tuple[dict[str, str], Any]] = [
        (bilingual_label("Produces Score", "Menghasilkan Score"), bilingual_label("No", "Tidak") if not data.get("produces_score") else bilingual_label("Yes", "Ya")),
        (bilingual_label("Valid Completion", "Penyelesaian Valid"), data.get("valid_completion_condition", {})),
        (bilingual_label("Interrupted Completion", "Penyelesaian yang Terinterupsi"), data.get("interrupted_completion_behavior", {})),
        (bilingual_label("Duplicate Prevention", "Pencegahan Duplikasi"), data.get("duplicate_prevention", {})),
        (bilingual_label("Handoff Result", "Hasil Handoff"), data.get("handoff_result", {})),
    ]
    recorded = data.get("recorded_data", [])
    if recorded:
        descriptions = [item.get("description", object_title(item.get("id", ""))) for item in recorded]
        rows.insert(2, (bilingual_label("Recorded Data", "Data yang Dicatat"), localized_join(descriptions, "; ")))
    return f"<h3>{i18n(bilingual_label('Completion Data', 'Data Penyelesaian'))}</h3>{render_info_table(rows)}"


@dataclass
class Page:
    page_id: str
    code: str
    header: dict[str, str]
    context: dict[str, str]
    title: dict[str, str]
    body: str
    footer_title: dict[str, str]
    classes: list[str] = field(default_factory=lambda: ["sheet"])
    page_role: str | None = None
    phase: str | None = None
    term_ids: list[str] = field(default_factory=list)
    tabs: list[dict[str, Any]] = field(default_factory=list)
    clean_target: str | None = None


class DocumentRenderer:
    def __init__(
        self,
        content: dict[str, Any],
        glossary: dict[str, Any] | None,
        template_dir: Path,
        *,
        template_version: str = "1.0",
        schema_version: str = "0.1",
        golden_sample_version: str = "aftershock-1.0",
        html_version: str = "1.0",
    ) -> None:
        self.content = content
        self.document = content["document"]
        self.profile = self.document["profile"]
        self.glossary_data = glossary or {"terms": []}
        self.glossary_by_id = {
            term["id"]: term
            for term in self.glossary_data.get("terms", [])
            if isinstance(term, dict) and term.get("id")
        }
        self.template_dir = template_dir
        self.template_version = template_version
        self.schema_version = schema_version
        self.golden_sample_version = golden_sample_version
        self.html_version = html_version
        self.content_hash = canonical_data_hash(content)
        self.pages: list[Page] = []
        self.navigation_html = ""
        self.page_glossary: dict[str, list[dict[str, Any]]] = {}
        self.missing_terms: list[tuple[str, str]] = []
        self._build()

    @property
    def title(self) -> str:
        return self.document["title"]

    @property
    def profile_label(self) -> dict[str, str]:
        if self.profile == "specialized_document":
            specialization = self.document.get("specialization")
            if specialization in SPECIALIZATION_LABELS:
                return SPECIALIZATION_LABELS[specialization]
        return PROFILE_LABELS.get(self.profile, bilingual_label("Production Document", "Dokumen Produksi"))

    def _build(self) -> None:
        builders = {
            "complete_game_map": self._build_complete_game_map,
            "multi_stage_game": self._build_multi_stage_game,
            "single_gameplay": self._build_single_gameplay,
            "game_system_module": self._build_game_system_module,
            "specialized_document": self._build_specialized_document,
        }
        try:
            builders[self.profile]()
        except KeyError as exc:
            raise ValueError(f"Unsupported document profile: {self.profile}") from exc
        self._resolve_page_glossary()

    def _page_header(self, number: str, label: dict[str, str]) -> dict[str, str]:
        label = normalize_text(label)
        return {lang: f"{number} — {label[lang]}" for lang in SUPPORTED_LANGS}

    def _overview_page(self, overview: dict[str, Any], *, page_id: str = "summary") -> Page:
        facts = overview.get("game_information", [])
        facts_html = ""
        if facts:
            cards = []
            for item in facts:
                cards.append(f'<div class="fact"><b>{i18n(item.get("label", {}))}</b><span>{i18n(item.get("value", {}))}</span></div>')
            facts_html = f'<div class="facts three">{"".join(cards)}</div>'

        flow_lookup = {
            item.get("id"): item
            for item in self.content.get("gameplay_flow", [])
            if isinstance(item, dict)
        }
        journey_cards: list[str] = []
        for index, item_id in enumerate(overview.get("journey_overview", []), 1):
            flow = flow_lookup.get(item_id, {})
            title = flow.get("title", object_title(item_id))
            description = flow.get("player_result") or flow.get("player_experience") or bilingual_label("Project stage", "Tahap project")
            journey_cards.append(
                "<article>"
                f"<small>{index:02d}</small>"
                f"<strong>{i18n(title)}</strong>"
                f"<p>{i18n(description)}</p>"
                "</article>"
            )
        journey_html = ""
        if journey_cards:
            journey_html = (
                f"<h3>{i18n(bilingual_label('Complete Gameplay Journey', 'Perjalanan Gameplay Lengkap'))}</h3>"
                f'<div class="journey">{"".join(journey_cards)}</div>'
            )

        systems = overview.get("main_systems", [])
        system_html = ""
        if systems:
            system_html = (
                '<div class="summary-note">'
                f"<strong>{i18n(bilingual_label('Main Systems', 'Sistem Utama'))}</strong>"
                '<ul class="clean-list">'
                + "".join(
                    f"<li><b>{i18n(item.get('title', {}))}</b> — {i18n(item.get('description', {}))}</li>"
                    for item in systems
                )
                + "</ul></div>"
            )

        body = (
            '<div class="cover-rule"></div>'
            f'<p class="eyebrow">{i18n(self.profile_label)}</p>'
            f"<h1>{i18n(bilingual_label(self.title, self.title))}</h1>"
            f'<p class="subtitle">{i18n(self.profile_label)}</p>'
            f'<p class="lead">{i18n(overview.get("project_context", {}))}</p>'
            f"<h3>{i18n(bilingual_label('Main Experience', 'Pengalaman Utama'))}</h3>"
            f"<p>{i18n(overview.get('main_experience', {}))}</p>"
            f"{facts_html}{journey_html}{system_html}"
        )
        return Page(
            page_id=page_id,
            code="01",
            header=bilingual_label("Gameplay & Development Specification", "Spesifikasi Gameplay & Pengembangan"),
            context={
                "en": f'Production Development Document · v{self.document.get("content_version", "1.0")}',
                "id": f'Dokumen Pengembangan Produksi · v{self.document.get("content_version", "1.0")}',
            },
            title=bilingual_label(self.title, self.title),
            body=body,
            footer_title=PAGE_LABELS["overview"],
            classes=["sheet", "clean-visible", "glossary-enabled-page"],
            page_role="overview",
            term_ids=list(overview.get("terms", [])),
        )

    def _gameplay_flow_pages(self, flow: list[dict[str, Any]], start_code: int = 2) -> list[Page]:
        pages: list[Page] = []
        for index, item in enumerate(flow):
            suffix = chr(ord("A") + index)
            page_id = f'flow-{item.get("id", index + 1)}'
            context_items = [item.get("title", {})]
            body = f"<h2>{i18n(item.get('title', {}))}</h2>"
            body += f'<p class="lead">{i18n(item.get("narrative_context", {}))}</p>'
            cards = [
                {"label": bilingual_label("Player Experience", "Pengalaman Player"), "content": item.get("player_experience", {})},
            ]
            if item.get("main_obstacle_or_change"):
                cards.append({"label": bilingual_label("Main Obstacle or Change", "Hambatan atau Perubahan Utama"), "content": item["main_obstacle_or_change"]})
            cards.append({"label": bilingual_label("Player Result", "Hasil Player"), "content": item.get("player_result", {})})
            body += '<div class="phase-context-grid">' + "".join(
                f"<article><b>{i18n(card['label'])}</b><p>{i18n(card['content'])}</p></article>" for card in cards
            ) + "</div>"
            if item.get("next_section"):
                body += (
                    '<div class="summary-note">'
                    f"<strong>{i18n(bilingual_label('Next Destination', 'Tujuan Berikutnya'))}</strong>"
                    f"<p>{i18n(object_title(item['next_section']))}</p></div>"
                )
            pages.append(
                Page(
                    page_id=page_id,
                    code=f"{start_code:02d}{suffix}",
                    header=self._page_header(f"{start_code:02d}", PAGE_LABELS["gameplay_flow"]),
                    context=localized_join(context_items),
                    title=normalize_text(item.get("title", {})),
                    body=body,
                    footer_title=localized_join([PAGE_LABELS["gameplay_flow"], item.get("title", {})]),
                    classes=["sheet", "clean-visible", "story-page", "glossary-enabled-page"],
                    page_role="gameplay-flow",
                    phase=f'dev-{item.get("id", index + 1)}',
                    term_ids=list(item.get("terms", [])),
                )
            )
        return pages

    def _global_page(self, key: str, data: dict[str, Any], code: str, *, header_number: str = "03") -> Page:
        title = data.get("title", object_title(key))
        body = f"<h2>{i18n(title)}</h2><p class=\"lead\">{i18n(data.get('overview', {}))}</p>"
        if data.get("flow"):
            body += f"<h3>{i18n(bilingual_label('Development Flow', 'Alur Pengembangan'))}</h3>{render_flow(data['flow'])}"
        if data.get("requirements"):
            body += f"<h3>{i18n(bilingual_label('Development Requirements', 'Kebutuhan Pengembangan'))}</h3>{render_requirements(data['requirements'])}"
        if data.get("important_notes"):
            body += f"<h3>{i18n(bilingual_label('Important Development Notes', 'Catatan Pengembangan Penting'))}</h3>{render_notes(data['important_notes'])}"
        return Page(
            page_id=key.replace("_", "-"),
            code=code,
            header=self._page_header(header_number, PAGE_LABELS["development"]),
            context=normalize_text(title),
            title=normalize_text(title),
            body=body,
            footer_title=normalize_text(title),
            classes=["sheet", "professional-only", "phase-package-page", "glossary-enabled-page"],
            page_role="development-global",
            phase=f"dev-global-{key.replace('_', '-')}",
            term_ids=list(data.get("terms", [])),
            clean_target="summary",
        )

    def _package_pages(self, package: dict[str, Any], section_number: int) -> list[Page]:
        package_id = package["id"]
        phase = f"dev-{package_id}"
        ids = {
            "gameplay": f"{phase}-gameplay",
            "level": f"{phase}-level",
            "developer": f"{phase}-developer",
        }
        tabs = [
            {"target": ids["gameplay"], "label": PAGE_LABELS["gameplay_overview"]},
            {"target": ids["level"], "label": PAGE_LABELS["level_design"]},
            {"target": ids["developer"], "label": PAGE_LABELS["developer"]},
        ]
        title = package.get("title", object_title(package_id))
        package_context = PACKAGE_TYPE_LABELS.get(package.get("type", ""), object_title(package.get("type", "Package")))
        if package.get("objective_number"):
            package_context = {
                "en": f'{package_context["en"]} {package["objective_number"]}',
                "id": f'{package_context["id"]} {package["objective_number"]}',
            }

        gameplay = package["gameplay_overview"]
        gameplay_body = self._render_tabs(tabs, ids["gameplay"])
        gameplay_body += f"<h2>{i18n(title)}</h2><p class=\"subtitle\">{i18n(PAGE_LABELS['gameplay_overview'])}</p>"
        gameplay_body += '<div class="phase-context-grid">' + "".join(
            [
                f"<article><b>{i18n(bilingual_label('Gameplay Context', 'Konteks Gameplay'))}</b><p>{i18n(gameplay.get('context', {}))}</p></article>",
                f"<article><b>{i18n(bilingual_label('Main Objective', 'Objektif Utama'))}</b><p>{i18n(gameplay.get('main_objective', {}))}</p></article>",
                f"<article><b>{i18n(bilingual_label('Result', 'Hasil'))}</b><p>{i18n(gameplay.get('result', {}))}</p></article>",
            ]
        ) + "</div>"
        info = gameplay.get("gameplay_information", {})
        info_rows = [
            (bilingual_label("Game Purpose", "Tujuan Gameplay"), info.get("game_purpose", {})),
            (bilingual_label("Estimated Time", "Estimasi Waktu"), info.get("estimated_time", {})),
            (bilingual_label("Starting Condition", "Kondisi Mulai"), info.get("starting_condition", {})),
            (bilingual_label("End Condition", "Kondisi Selesai"), info.get("end_condition", {})),
            (bilingual_label("Fail or Blocked Condition", "Kondisi Gagal atau Terblokir"), info.get("fail_or_blocked_condition", {})),
        ]
        if "scoring_criteria" in info:
            info_rows.append((bilingual_label("Scoring Criteria", "Kriteria Scoring"), info.get("scoring_criteria", {})))
        if "completion_criteria" in info:
            info_rows.append((bilingual_label("Completion Criteria", "Kriteria Penyelesaian"), info.get("completion_criteria", {})))
        gameplay_body += f"<h3>{i18n(bilingual_label('Gameplay Information', 'Informasi Gameplay'))}</h3>{render_info_table(info_rows)}"
        gameplay_body += f"<h3>{i18n(bilingual_label('Gameplay Flow', 'Alur Gameplay'))}</h3>{render_flow(gameplay.get('gameplay_flow', []))}"

        level = package["level_design"]
        level_body = self._render_tabs(tabs, ids["level"])
        level_body += f"<h2>{i18n(title)}</h2><p class=\"subtitle\">{i18n(PAGE_LABELS['level_design'])}</p>"
        level_body += f'<p class="lead">{i18n(level.get("overview", {}))}</p>'
        level_body += f"<h3>{i18n(bilingual_label('Design Flow', 'Alur Desain'))}</h3>{render_flow(level.get('design_flow', []))}"
        level_body += f"<h3>{i18n(bilingual_label('Build Requirements', 'Kebutuhan Build'))}</h3>{render_build_requirements(level.get('build_requirements', []))}"
        if level.get("important_notes"):
            level_body += f"<h3>{i18n(bilingual_label('Important Build Notes', 'Catatan Build Penting'))}</h3>{render_notes(level['important_notes'])}"

        developer = package["developer"]
        developer_body = self._render_tabs(tabs, ids["developer"])
        developer_body += f"<h2>{i18n(title)}</h2><p class=\"subtitle\">{i18n(PAGE_LABELS['developer'])}</p>"
        developer_body += '<div class="phase-context-grid">' + "".join(
            [
                f"<article><b>{i18n(bilingual_label('Developer Overview', 'Gambaran Developer'))}</b><p>{i18n(developer.get('overview', {}))}</p></article>",
                f"<article><b>{i18n(bilingual_label('Development Goal', 'Tujuan Pengembangan'))}</b><p>{i18n(developer.get('development_goal', {}))}</p></article>",
                f"<article><b>{i18n(bilingual_label('Expected Result', 'Hasil yang Diharapkan'))}</b><p>{i18n(developer.get('expected_result', {}))}</p></article>",
            ]
        ) + "</div>"
        developer_body += f"<h3>{i18n(bilingual_label('Development Flow', 'Alur Pengembangan'))}</h3>{render_flow(developer.get('development_flow', []))}"
        developer_body += f"<h3>{i18n(bilingual_label('Development Requirements', 'Kebutuhan Pengembangan'))}</h3>{render_requirements(developer.get('requirements', []))}"
        if developer.get("scoring"):
            developer_body += render_scoring(developer["scoring"])
        if developer.get("completion_data"):
            developer_body += render_completion_data(developer["completion_data"])
        if developer.get("important_notes"):
            developer_body += f"<h3>{i18n(bilingual_label('Important Development Notes', 'Catatan Pengembangan Penting'))}</h3>{render_notes(developer['important_notes'])}"

        pages = [
            Page(ids["gameplay"], f"{section_number:02d}A", self._page_header("03", PAGE_LABELS["development"]), localized_join([title, package_context]), title, gameplay_body, localized_join([title, PAGE_LABELS["gameplay_overview"]]), ["sheet", "professional-only", "phase-package-page", "glossary-enabled-page"], "gameplay-overview", phase, list(gameplay.get("terms", [])), tabs, "summary"),
            Page(ids["level"], f"{section_number:02d}B", self._page_header("03", PAGE_LABELS["development"]), localized_join([title, package_context]), title, level_body, localized_join([title, PAGE_LABELS["level_design"]]), ["sheet", "professional-only", "phase-package-page", "glossary-enabled-page"], "level-design", phase, list(level.get("terms", [])), tabs, "summary"),
            Page(ids["developer"], f"{section_number:02d}C", self._page_header("03", PAGE_LABELS["development"]), localized_join([title, package_context]), title, developer_body, localized_join([title, PAGE_LABELS["developer"]]), ["sheet", "professional-only", "phase-package-page", "glossary-enabled-page"], "developer", phase, list(developer.get("terms", [])), tabs, "summary"),
        ]
        return pages

    def _render_tabs(self, tabs: list[dict[str, Any]], active: str) -> str:
        links = []
        for tab in tabs:
            active_cls = " is-active" if tab["target"] == active else ""
            links.append(
                f'<a class="section-tab{active_cls}" data-section-target="{esc(tab["target"])}" href="#{esc(tab["target"])}">{i18n(tab["label"])}</a>'
            )
        return '<div class="section-tabs package-tabs" role="navigation" aria-label="Package pages">' + "".join(links) + "</div>"

    def _build_complete_game_map(self) -> None:
        self.pages.append(self._overview_page(self.content["overview"]))
        flow_pages = self._gameplay_flow_pages(self.content.get("gameplay_flow", []))
        self.pages.extend(flow_pages)
        globals_order = ["development_overview", "game_system", "data_and_reset", "gameplay_development"]
        global_pages = self.content["development"]["global_pages"]
        for index, key in enumerate(globals_order):
            self.pages.append(self._global_page(key, global_pages[key], f"03{chr(ord('A') + index)}"))
        packages = self.content["development"]["packages"]
        for index, package in enumerate(packages, 4):
            self.pages.extend(self._package_pages(package, index))
        self.navigation_html = self._nav_standard(flow_pages, [page for page in self.pages if page.page_role == "development-global"], packages, package_start=4)

    def _build_multi_stage_game(self) -> None:
        self.pages.append(self._overview_page(self.content["overview"]))
        flow_pages = self._gameplay_flow_pages(self.content.get("gameplay_flow", []))
        self.pages.extend(flow_pages)
        globals_order = ["session_system", "global_scoring", "data_and_leaderboard", "reset_system"]
        dev = self.content["development"]
        global_rendered = []
        for index, key in enumerate(globals_order):
            page = self._global_page(key, dev[key], f"03{chr(ord('A') + index)}")
            self.pages.append(page)
            global_rendered.append(page)
        packages = dev["stage_packages"]
        for index, package in enumerate(packages, 4):
            self.pages.extend(self._package_pages(package, index))
        self.navigation_html = self._nav_standard(flow_pages, global_rendered, packages, package_start=4)

    def _build_single_gameplay(self) -> None:
        self.pages.append(self._overview_page(self.content["overview"]))
        flow_pages = self._gameplay_flow_pages(self.content.get("gameplay_flow", []))
        self.pages.extend(flow_pages)
        package = self.content["development"]["gameplay_package"]
        self.pages.extend(self._package_pages(package, 3))
        self.navigation_html = self._nav_standard(flow_pages, [], [package], package_start=3)

    def _build_game_system_module(self) -> None:
        overview_data = self.content["system_overview"]
        overview_body = (
            '<div class="cover-rule"></div>'
            f'<p class="eyebrow">{i18n(self.profile_label)}</p>'
            f"<h1>{i18n(bilingual_label(self.title, self.title))}</h1>"
            f'<p class="subtitle">{i18n(PAGE_LABELS["system_overview"])}</p>'
            f'<p class="lead">{i18n(overview_data.get("overview", {}))}</p>'
            f"<h3>{i18n(bilingual_label('System Flow Summary', 'Ringkasan Alur Sistem'))}</h3>{render_flow(overview_data.get('flow', []))}"
            f"<h3>{i18n(bilingual_label('Core Requirements', 'Kebutuhan Utama'))}</h3>{render_requirements(overview_data.get('requirements', []))}"
            f"{render_notes(overview_data.get('important_notes', []))}"
        )
        overview_page = Page(
            "summary", "01", bilingual_label("System & Development Specification", "Spesifikasi Sistem & Pengembangan"),
            {"en": f'System Production Document · v{self.document.get("content_version", "1.0")}', "id": f'Dokumen Produksi Sistem · v{self.document.get("content_version", "1.0")}'},
            bilingual_label(self.title, self.title), overview_body, PAGE_LABELS["system_overview"],
            ["sheet", "clean-visible", "glossary-enabled-page"], "system-overview", "dev-system-overview", list(overview_data.get("terms", []))
        )
        self.pages.append(overview_page)
        flow_body = f"<h2>{i18n(PAGE_LABELS['system_flow'])}</h2>{render_flow(self.content.get('system_flow', []))}"
        flow_page = Page(
            "system-flow", "02", self._page_header("02", PAGE_LABELS["system_flow"]), self.profile_label,
            PAGE_LABELS["system_flow"], flow_body, PAGE_LABELS["system_flow"], ["sheet", "clean-visible", "story-page"], "system-flow"
        )
        self.pages.append(flow_page)
        order = ["architecture", "requirements", "configuration", "integration", "data_handling", "error_handling", "lifecycle", "usage_guide"]
        global_rendered: list[Page] = []
        for index, key in enumerate(order):
            page = self._global_page(key, self.content["development"][key], f"03{chr(ord('A') + index)}")
            self.pages.append(page)
            global_rendered.append(page)
        self.navigation_html = self._nav_module(flow_page, global_rendered)

    def _build_specialized_document(self) -> None:
        specialization = self.document["specialization"]
        source = self.content["specialized_content"]
        label = SPECIALIZATION_LABELS[specialization]
        term_ids: list[str] = []
        if specialization == "gameplay_design_only":
            data = source["gameplay_design"]
            term_ids = list(data.get("terms", []))
            body = f"<h1>{i18n(bilingual_label(self.title, self.title))}</h1><p class=\"subtitle\">{i18n(label)}</p>"
            body += '<div class="phase-context-grid">' + "".join(
                [
                    f"<article><b>{i18n(bilingual_label('Gameplay Context', 'Konteks Gameplay'))}</b><p>{i18n(data.get('context', {}))}</p></article>",
                    f"<article><b>{i18n(bilingual_label('Main Objective', 'Objektif Utama'))}</b><p>{i18n(data.get('main_objective', {}))}</p></article>",
                    f"<article><b>{i18n(bilingual_label('Result', 'Hasil'))}</b><p>{i18n(data.get('result', {}))}</p></article>",
                ]
            ) + "</div>"
            info = data.get("gameplay_information", {})
            rows = [(object_title(key), value) for key, value in info.items()]
            body += render_info_table(rows)
            body += f"<h3>{i18n(PAGE_LABELS['gameplay_flow'])}</h3>{render_flow(data.get('gameplay_flow', []))}"
        elif specialization == "level_design_only":
            data = source["level_design"]
            term_ids = list(data.get("terms", []))
            body = f"<h1>{i18n(bilingual_label(self.title, self.title))}</h1><p class=\"subtitle\">{i18n(label)}</p><p class=\"lead\">{i18n(data.get('overview', {}))}</p>"
            body += f"<h3>{i18n(bilingual_label('Design Flow', 'Alur Desain'))}</h3>{render_flow(data.get('design_flow', []))}"
            body += f"<h3>{i18n(bilingual_label('Build Requirements', 'Kebutuhan Build'))}</h3>{render_build_requirements(data.get('build_requirements', []))}"
            body += render_notes(data.get("important_notes", []))
        elif specialization == "developer_only":
            data = source["developer"]
            term_ids = list(data.get("terms", []))
            body = f"<h1>{i18n(bilingual_label(self.title, self.title))}</h1><p class=\"subtitle\">{i18n(label)}</p>"
            body += '<div class="phase-context-grid">' + "".join(
                [
                    f"<article><b>{i18n(bilingual_label('Developer Overview', 'Gambaran Developer'))}</b><p>{i18n(data.get('overview', {}))}</p></article>",
                    f"<article><b>{i18n(bilingual_label('Development Goal', 'Tujuan Pengembangan'))}</b><p>{i18n(data.get('development_goal', {}))}</p></article>",
                    f"<article><b>{i18n(bilingual_label('Expected Result', 'Hasil yang Diharapkan'))}</b><p>{i18n(data.get('expected_result', {}))}</p></article>",
                ]
            ) + "</div>"
            body += render_flow(data.get("development_flow", []))
            body += render_requirements(data.get("requirements", []))
            body += render_scoring(data.get("scoring", {}))
            body += render_completion_data(data.get("completion_data", {}))
            body += render_notes(data.get("important_notes", []))
        elif specialization == "scoring_and_data_only":
            data = source["scoring_and_data"]
            term_ids = list(data.get("terms", []))
            body = f"<h1>{i18n(data.get('title', label))}</h1><p class=\"subtitle\">{i18n(label)}</p>{render_scoring(data.get('scoring', {}))}"
        elif specialization == "audit_only":
            data = source["audit"]
            body = f"<h1>{i18n(bilingual_label(self.title, self.title))}</h1><p class=\"subtitle\">{i18n(label)}</p>"
            body += '<div class="phase-context-grid">' + "".join(
                [
                    f"<article><b>{i18n(bilingual_label('Audit Scope', 'Scope Audit'))}</b><p>{i18n(data.get('scope', {}))}</p></article>",
                    f"<article><b>{i18n(bilingual_label('Audit Method', 'Metode Audit'))}</b><p>{i18n(data.get('method', {}))}</p></article>",
                    f"<article><b>{i18n(bilingual_label('Next Step', 'Langkah Selanjutnya'))}</b><p>{i18n(data.get('next_step', {}))}</p></article>",
                ]
            ) + "</div>"
            if data.get("findings"):
                body += f"<h3>{i18n(bilingual_label('Findings', 'Temuan'))}</h3><ul class=\"clean-list\">" + "".join(f"<li>{esc(item)}</li>" for item in data["findings"]) + "</ul>"
        else:
            raise ValueError(f"Unsupported specialization: {specialization}")
        page = Page(
            "summary", "01", bilingual_label("Specialized Production Document", "Dokumen Produksi Khusus"), label,
            bilingual_label(self.title, self.title), body, label, ["sheet", "clean-visible", "phase-package-page", "glossary-enabled-page"], specialization, f"dev-{specialization}", term_ids
        )
        self.pages.append(page)
        self.navigation_html = self._single_nav(page)

    def _nav_link(self, page: Page, label: dict[str, str] | None = None, index: str | None = None, class_name: str = "nav-link") -> str:
        label = label or page.title
        index_html = f'<span class="nav-index" data-full-index="{esc(index or page.code)}" data-overview-index="{esc(index or page.code)}">{esc(index or page.code)}</span>' if class_name == "nav-link" else ""
        return f'<a class="{esc(class_name)}" data-target="{esc(page.page_id)}" href="#{esc(page.page_id)}">{index_html}<span class="nav-copy">{i18n(label)}</span></a>'

    def _nav_standard(self, flow_pages: list[Page], global_pages: list[Page], packages: list[dict[str, Any]], *, package_start: int) -> str:
        overview = self.pages[0]
        html_parts = [self._nav_link(overview, PAGE_LABELS["overview"], "01")]
        if flow_pages:
            submenu = "".join(f'<a data-target="{esc(page.page_id)}" href="#{esc(page.page_id)}">{i18n(page.title)}</a>' for page in flow_pages)
            html_parts.append(
                '<div class="nav-group is-open"><button aria-expanded="true" class="nav-group-toggle" type="button">'
                '<span class="nav-index" data-full-index="02" data-overview-index="02">02</span>'
                f'<span class="nav-copy">{i18n(PAGE_LABELS["gameplay_flow"])}</span><span aria-hidden="true" class="group-chevron"></span></button>'
                f'<div class="nav-submenu">{submenu}</div></div>'
            )
        global_submenu = "".join(f'<a data-target="{esc(page.page_id)}" href="#{esc(page.page_id)}">{i18n(page.title)}</a>' for page in global_pages)
        package_nav: list[str] = []
        page_map = {page.page_id: page for page in self.pages}
        for index, package in enumerate(packages, package_start):
            phase = f'dev-{package["id"]}'
            ids = [f"{phase}-gameplay", f"{phase}-level", f"{phase}-developer"]
            package_label = package.get("title", object_title(package["id"]))
            type_label = PACKAGE_TYPE_LABELS.get(package.get("type", ""), object_title(package.get("type", "Package")))
            if package.get("objective_number"):
                type_label = {"en": f'{type_label["en"]} {package["objective_number"]}', "id": f'{type_label["id"]} {package["objective_number"]}'}
            child_labels = [PAGE_LABELS["gameplay_overview"], PAGE_LABELS["level_design"], PAGE_LABELS["developer"]]
            children = "".join(
                f'<a class="phase-page-link professional-nav-item" data-phase-page-link="{esc(phase)}" data-target="{esc(page_id)}" href="#{esc(page_id)}"><span>{i18n(label)}</span></a>'
                for page_id, label in zip(ids, child_labels)
                if page_id in page_map
            )
            package_nav.append(
                f'<div class="phase-nav-item" data-phase-nav="{esc(phase)}">'
                f'<a class="phase-nav-main" data-phase-link="{esc(phase)}" data-section-code="{index:02d}" data-target="{esc(ids[0])}" href="#{esc(ids[0])}"><span>{i18n(package_label)}</span><small>{i18n(type_label)}</small></a>'
                f'<div class="phase-page-list">{children}</div></div>'
            )
        html_parts.append(
            '<div class="nav-group is-open professional-nav"><button aria-expanded="true" class="nav-group-toggle" type="button">'
            '<span class="nav-index" data-full-index="03" data-overview-index="">03</span>'
            f'<span class="nav-copy">{i18n(PAGE_LABELS["development"])}</span><span aria-hidden="true" class="group-chevron"></span></button>'
            f'<div class="nav-submenu">{global_submenu}</div><div class="nav-submenu phase-navigation">{"".join(package_nav)}</div></div>'
        )
        return "".join(html_parts)

    def _nav_module(self, flow_page: Page, global_pages: list[Page]) -> str:
        parts = [self._nav_link(self.pages[0], PAGE_LABELS["system_overview"], "01"), self._nav_link(flow_page, PAGE_LABELS["system_flow"], "02")]
        submenu = "".join(f'<a data-target="{esc(page.page_id)}" href="#{esc(page.page_id)}">{i18n(page.title)}</a>' for page in global_pages)
        parts.append(
            '<div class="nav-group is-open professional-nav"><button aria-expanded="true" class="nav-group-toggle" type="button">'
            '<span class="nav-index" data-full-index="03" data-overview-index="">03</span>'
            f'<span class="nav-copy">{i18n(PAGE_LABELS["development"])}</span><span aria-hidden="true" class="group-chevron"></span></button>'
            f'<div class="nav-submenu">{submenu}</div></div>'
        )
        return "".join(parts)

    def _single_nav(self, page: Page) -> str:
        return self._nav_link(page, self.profile_label, "01")

    def _resolve_page_glossary(self) -> None:
        for page in self.pages:
            terms: list[dict[str, Any]] = []
            for term_id in page.term_ids:
                term = self.glossary_by_id.get(term_id)
                if term is None:
                    self.missing_terms.append((page.page_id, term_id))
                    continue
                if term.get("status") == "deprecated":
                    continue
                terms.append(term)
            self.page_glossary[page.page_id] = terms

    def _terms_html(self, page: Page) -> str:
        terms = self.page_glossary.get(page.page_id, [])
        if not terms:
            return ""
        items = "".join(
            '<div class="definition-item">'
            f"<b>{i18n(term.get('term', {}))}</b>"
            f"<p>{i18n(term.get('definition', {}))}</p></div>"
            for term in terms
        )
        return (
            '<details class="terms-used-collapsible" data-terms-used>'
            '<summary class="terms-used-summary">'
            f'<span class="terms-used-title">{i18n(bilingual_label("Terms Used", "Istilah yang Digunakan"))}</span>'
            '<span aria-hidden="true" class="terms-used-separator">—</span>'
            '<span class="terms-used-action">'
            f'<span class="terms-used-show-label">{i18n(bilingual_label("Show Details", "Tampilkan Detail"))}</span>'
            f'<span class="terms-used-hide-label">{i18n(bilingual_label("Hide Details", "Sembunyikan Detail"))}</span>'
            '<span aria-hidden="true" class="terms-used-chevron"></span></span></summary>'
            f'<div class="terms-used-panel"><div class="definition-list quarry-definition-list glossary-definition-list">{items}</div></div></details>'
        )

    def _page_html(self, page: Page) -> str:
        attributes = [f'id="{esc(page.page_id)}"', f'class="{esc(" ".join(page.classes))}"']
        if page.page_role:
            attributes.append(f'data-page-role="{esc(page.page_role)}"')
        if page.phase:
            attributes.append(f'data-phase="{esc(page.phase)}"')
        if self.page_glossary.get(page.page_id):
            attributes.append(f'data-glossary-scope="{esc(page.page_id)}"')
        if page.clean_target:
            attributes.append(f'data-clean-target="{esc(page.clean_target)}"')
        head = (
            '<div class="page-head">'
            f"<strong>{i18n(page.header)}</strong>"
            f"<span>{i18n(page.context)}</span></div>"
        )
        footer = (
            '<div class="page-foot">'
            f'<span class="footer-brand">{esc(self.title)}</span>'
            f'<span class="footer-title">{i18n(page.footer_title)}</span>'
            f'<span class="footer-code">{esc(page.code)}</span></div>'
        )
        return f'<section {" ".join(attributes)}>{head}{page.body}{self._terms_html(page)}{footer}</section>'

    def _controls_html(self) -> str:
        languages = self.document.get("output_languages", [self.document.get("primary_language", "en")])
        language_panel = ""
        if set(languages) >= {"en", "id"}:
            language_panel = (
                '<div class="language-panel"><div aria-label="Select document language" class="language-control" data-language="en" id="languageSwitch" role="group">'
                '<span aria-hidden="true" class="language-slider"></span>'
                '<button aria-pressed="true" class="language-option is-active" data-language-option="en" type="button">EN</button>'
                '<button aria-pressed="false" class="language-option" data-language-option="id" type="button">ID</button>'
                "</div></div>"
            )
        return (
            '<div class="sidebar-settings"><div class="theme-setting-row">'
            '<button aria-checked="false" aria-label="Toggle light and dark appearance" class="header-theme-toggle moon-toggle-refined" id="themeModeSwitch" role="switch" type="button">'
            '<span aria-hidden="true" class="theme-icon theme-icon-moon">☾</span><span aria-hidden="true" class="theme-toggle-track"><span class="theme-toggle-thumb"></span></span></button>'
            f"</div>{language_panel}</div>"
        )

    def _view_mode_html(self) -> str:
        return (
            '<div class="view-mode-panel"><span class="view-mode-title">'
            f'{i18n(bilingual_label("View Mode", "Mode Tampilan"))}</span>'
            '<div aria-label="Document view" class="view-mode-control" data-mode="professional" id="viewModeSwitch" role="group">'
            '<span aria-hidden="true" class="view-mode-slider"></span>'
            f'<button aria-pressed="false" class="view-mode-option" data-mode-label="clean" type="button">{i18n(bilingual_label("Overview", "Ringkasan"))}</button>'
            f'<button aria-pressed="true" class="view-mode-option is-active" data-mode-label="professional" type="button">{i18n(bilingual_label("Full Detail", "Detail Lengkap"))}</button>'
            "</div></div>"
        )

    def _sidebar_html(self) -> str:
        brand_mark = re.sub(r"[^A-Za-z0-9]", "", self.title)[:1].upper() or "P"
        return (
            '<aside aria-label="Document navigation" class="doc-sidebar" id="docSidebar">'
            '<div class="sidebar-head">'
            f'<a aria-label="{esc(self.title)} overview" class="sidebar-brand" href="#summary"><span class="brand-mark">{esc(brand_mark)}</span>'
            f'<span class="brand-copy"><strong>{esc(self.title)}</strong><small>{i18n(self.profile_label)}</small></span></a>'
            '<button aria-controls="docSidebar" aria-expanded="true" aria-label="Collapse document navigation" class="sidebar-toggle" id="sidebarToggle" type="button"><span aria-hidden="true" class="toggle-lines"></span></button>'
            f"</div>{self._controls_html()}{self._view_mode_html()}<nav class=\"sidebar-nav\">{self.navigation_html}</nav></aside>"
        )

    def _glossary_runtime_data(self) -> dict[str, list[dict[str, Any]]]:
        result: dict[str, list[dict[str, Any]]] = {}
        for page_id, terms in self.page_glossary.items():
            result[page_id] = []
            for index, term in enumerate(terms):
                label = normalize_text(term.get("term", {}))
                definition = normalize_text(term.get("definition", {}))
                aliases_data = term.get("aliases", {}) or {}
                aliases = {
                    "en": list(dict.fromkeys([label["en"], *aliases_data.get("en", [])])),
                    "id": list(dict.fromkeys([label["id"], *aliases_data.get("id", [])])),
                }
                result[page_id].append(
                    {
                        "key": f"{page_id}-{index}",
                        "label": label,
                        "definition": definition,
                        "aliases": aliases,
                    }
                )
        return result

    def _document_controls_js(self) -> str:
        project_key = re.sub(r"[^a-z0-9_-]", "-", self.document["id"].lower())
        default_lang = self.document.get("primary_language", "en")
        return f"""
(function(){{
  const body = document.body;
  const modeControl = document.getElementById('viewModeSwitch');
  const themeControl = document.getElementById('themeModeSwitch');
  const modeLabels = Array.from(document.querySelectorAll('[data-mode-label]'));
  const groups = Array.from(document.querySelectorAll('.nav-group'));
  const navTargets = Array.from(document.querySelectorAll('[data-target]'));
  const phaseItems = Array.from(document.querySelectorAll('[data-phase-nav]'));
  const documentSheets = Array.from(document.querySelectorAll('section.sheet[id]'));
  const firstPageId = body.dataset.overviewPage || documentSheets[0]?.id || 'summary';
  const keyPrefix = 'production-document-{project_key}-';

  function updateThemeUI(theme){{
    const dark = theme === 'dark';
    body.classList.toggle('theme-dark', dark);
    body.classList.toggle('theme-normal', !dark);
    if (themeControl){{
      themeControl.dataset.theme = theme;
      themeControl.setAttribute('aria-checked', String(dark));
      themeControl.setAttribute('aria-label', dark ? 'Disable dark mode' : 'Enable dark mode');
    }}
    document.documentElement.style.colorScheme = dark ? 'dark' : 'light';
    try {{ localStorage.setItem(keyPrefix + 'theme', theme); }} catch(e) {{}}
  }}

  function updateModeUI(mode){{
    const professional = mode === 'professional';
    body.classList.toggle('view-clean', !professional);
    body.classList.toggle('view-professional', professional);
    if (modeControl) modeControl.dataset.mode = mode;
    document.querySelectorAll('.nav-index[data-full-index]').forEach(function(index){{
      index.textContent = professional ? index.dataset.fullIndex : index.dataset.overviewIndex;
    }});
    modeLabels.forEach(function(label){{
      const active = label.dataset.modeLabel === mode;
      label.classList.toggle('is-active', active);
      label.setAttribute('aria-pressed', String(active));
    }});
    try {{ localStorage.setItem(keyPrefix + 'view', mode); }} catch(e) {{}}
    if (!professional){{
      const currentHash = (location.hash || ('#' + firstPageId)).slice(1);
      const currentSection = document.getElementById(currentHash);
      if (currentSection && currentSection.classList.contains('professional-only')){{
        const cleanTarget = currentSection.dataset.cleanTarget || firstPageId;
        history.replaceState(null, '', '#' + cleanTarget);
        document.getElementById(cleanTarget)?.scrollIntoView({{behavior:'smooth', block:'start'}});
      }}
    }}
    requestAnimationFrame(updateActiveNavigation);
  }}

  modeLabels.forEach(label => label.addEventListener('click', () => updateModeUI(label.dataset.modeLabel)));
  themeControl?.addEventListener('click', () => updateThemeUI(body.classList.contains('theme-dark') ? 'normal' : 'dark'));
  groups.forEach(function(group){{
    const button = group.querySelector('.nav-group-toggle');
    button?.addEventListener('click', function(){{
      const open = group.classList.toggle('is-open');
      button.setAttribute('aria-expanded', String(open));
    }});
  }});

  function setActivePhase(phase, pageId){{
    const overviewMode = body.classList.contains('view-clean');
    phaseItems.forEach(function(item){{
      const current = item.dataset.phaseNav === phase;
      item.classList.toggle('is-current', current);
      item.querySelector('.phase-nav-main')?.classList.toggle('is-active', current);
      item.querySelectorAll('.phase-page-link').forEach(link => link.classList.toggle('is-active', !overviewMode && current && link.dataset.target === pageId));
    }});
  }}

  function activateSection(section){{
    if (!section) return;
    const id = section.id;
    const phase = section.dataset.phase || '';
    navTargets.forEach(function(link){{
      if (link.classList.contains('phase-nav-main') || link.classList.contains('phase-page-link')) return;
      link.classList.toggle('is-active', link.dataset.target === id);
    }});
    groups.forEach(function(group){{
      const activeChild = group.querySelector('[data-target="' + id + '"]');
      const gameplayChild = phase && group.querySelector('[data-phase-nav="' + phase + '"]');
      const active = Boolean(activeChild || gameplayChild);
      group.classList.toggle('has-active', active);
      if (active){{
        group.classList.add('is-open');
        group.querySelector('.nav-group-toggle')?.setAttribute('aria-expanded','true');
      }}
    }});
    if (phase) setActivePhase(phase, id);
    else phaseItems.forEach(item => {{ item.classList.remove('is-current'); item.querySelector('.phase-nav-main')?.classList.remove('is-active'); item.querySelectorAll('.phase-page-link').forEach(link => link.classList.remove('is-active')); }});
  }}

  function findCurrentSection(){{
    const visible = documentSheets.filter(section => section.offsetParent !== null);
    let current = null; let bestScore = Infinity;
    visible.forEach(function(section){{
      const rect = section.getBoundingClientRect();
      if (rect.bottom <= 92) return;
      const reference = 118;
      const score = rect.top <= reference ? Math.abs(rect.top-reference)*.35 : Math.abs(rect.top-reference);
      if (score < bestScore){{ current = section; bestScore = score; }}
    }});
    return current;
  }}
  function updateActiveNavigation(){{ activateSection(findCurrentSection()); }}
  navTargets.forEach(link => link.addEventListener('click', () => requestAnimationFrame(() => activateSection(document.getElementById(link.dataset.target)))));
  document.querySelectorAll('[data-section-target]').forEach(function(link){{
    link.addEventListener('click', function(event){{
      const target = document.getElementById(link.dataset.sectionTarget); if (!target) return;
      event.preventDefault();
      if (body.classList.contains('view-clean') && target.classList.contains('professional-only')) updateModeUI('professional');
      history.replaceState(null,'','#'+target.id); target.scrollIntoView({{behavior:'smooth',block:'start'}}); activateSection(target);
    }});
  }});
  window.addEventListener('scroll', updateActiveNavigation, {{passive:true}});
  window.addEventListener('resize', updateActiveNavigation);
  let savedMode='professional', savedTheme='normal';
  try {{ savedMode=localStorage.getItem(keyPrefix+'view')||'professional'; savedTheme=localStorage.getItem(keyPrefix+'theme')||'normal'; }} catch(e) {{}}
  updateThemeUI(savedTheme === 'dark' ? 'dark' : 'normal'); updateModeUI(savedMode === 'clean' ? 'clean' : 'professional');
  activateSection(document.getElementById((location.hash || ('#'+firstPageId)).slice(1)) || document.getElementById(firstPageId));

  const languageControl=document.getElementById('languageSwitch');
  const languageOptions=Array.from(document.querySelectorAll('[data-language-option]'));
  const i18nNodes=Array.from(document.querySelectorAll('.i18n-text'));
  function updateLanguage(language){{
    const selected=language === 'id' ? 'id' : 'en';
    document.documentElement.lang=selected; if (languageControl) languageControl.dataset.language=selected;
    languageOptions.forEach(button => {{ const active=button.dataset.languageOption===selected; button.classList.toggle('is-active',active); button.setAttribute('aria-pressed',String(active)); }});
    i18nNodes.forEach(node => {{ const value=selected==='id'?node.dataset.id:node.dataset.en; if(typeof value==='string') node.textContent=value; }});
    try {{ localStorage.setItem(keyPrefix+'language',selected); }} catch(e) {{}}
  }}
  languageOptions.forEach(button => button.addEventListener('click', () => updateLanguage(button.dataset.languageOption)));
  let savedLanguage={json.dumps(default_lang)}; try {{ savedLanguage=localStorage.getItem(keyPrefix+'language')||savedLanguage; }} catch(e) {{}}
  updateLanguage(savedLanguage);
}})();
"""

    def _glossary_js(self) -> str:
        glossary_json = json.dumps(self._glossary_runtime_data(), ensure_ascii=False, separators=(",", ":"))
        return f"""
(() => {{
  const glossary = {glossary_json};
  const tooltip=document.getElementById('globalGlossaryTooltip');
  const tooltipTerm=document.getElementById('globalGlossaryTooltipTerm');
  const tooltipDefinition=document.getElementById('globalGlossaryTooltipDefinition');
  let activeTarget=null, pinned=false, hideTimer=null;
  const isWordChar=(character)=>character?/\\p{{L}}|\\p{{N}}|_/u.test(character):false;
  function collectMatches(text,terms,language){{
    const locale=language==='id'?'id':'en'; const lower=text.toLocaleLowerCase(locale); const candidates=[];
    terms.forEach(term => (term.aliases[language]||term.aliases.en||[]).forEach(alias => {{
      const needle=alias.toLocaleLowerCase(locale); let from=0;
      while(needle && from<lower.length){{ const index=lower.indexOf(needle,from); if(index<0)break; const before=index>0?text[index-1]:''; const after=index+alias.length<text.length?text[index+alias.length]:''; if(!isWordChar(before)&&!isWordChar(after)) candidates.push({{start:index,end:index+alias.length,length:alias.length,term}}); from=index+Math.max(1,needle.length); }}
    }}));
    candidates.sort((a,b)=>a.start-b.start||b.length-a.length); const selected=[]; let cursor=-1;
    for(const candidate of candidates){{ if(candidate.start>=cursor){{selected.push(candidate);cursor=candidate.end;}} }} return selected;
  }}
  function shouldSkip(node){{ return Boolean(node.closest('script,style,#globalGlossaryTooltip,.doc-sidebar,.page-head,.page-foot,.section-tabs,a,button,.terms-used-collapsible')); }}
  function rebuildGlossaryTerms(){{
    hideTooltip(); const language=document.documentElement.lang==='id'?'id':'en';
    document.querySelectorAll('section[data-glossary-scope]').forEach(section => {{
      const terms=glossary[section.dataset.glossaryScope]; if(!terms?.length)return;
      section.querySelectorAll('.i18n-text').forEach(node => {{
        if(shouldSkip(node))return; const raw=language==='id'?node.dataset.id:node.dataset.en; if(typeof raw!=='string')return;
        node.textContent=raw; const matches=collectMatches(raw,terms,language); if(!matches.length)return;
        const fragment=document.createDocumentFragment(); let cursor=0;
        matches.forEach(match => {{ if(match.start>cursor)fragment.append(document.createTextNode(raw.slice(cursor,match.start))); const button=document.createElement('button'); button.type='button'; button.className='glossary-term'; button.dataset.glossaryScope=section.dataset.glossaryScope; button.dataset.glossaryKey=match.term.key; button.setAttribute('aria-expanded','false'); button.setAttribute('aria-describedby','globalGlossaryTooltip'); button.textContent=raw.slice(match.start,match.end); fragment.append(button); cursor=match.end; }});
        if(cursor<raw.length)fragment.append(document.createTextNode(raw.slice(cursor))); node.replaceChildren(fragment);
      }});
    }});
  }}
  function getTerm(target){{ return (glossary[target?.dataset.glossaryScope]||[]).find(term=>term.key===target?.dataset.glossaryKey)||null; }}
  function positionTooltip(target){{ if(!target||!tooltip.classList.contains('is-visible'))return; const rect=target.getBoundingClientRect(); if(window.matchMedia('(max-width:720px)').matches)return; const margin=12,gap=12,tipRect=tooltip.getBoundingClientRect(); const topPlace=rect.top>=tipRect.height+gap+margin; let top=topPlace?rect.top-tipRect.height-gap:rect.bottom+gap; top=Math.max(margin,Math.min(top,window.innerHeight-tipRect.height-margin)); let left=rect.left+rect.width/2-tipRect.width/2; left=Math.max(margin,Math.min(left,window.innerWidth-tipRect.width-margin)); tooltip.dataset.placement=topPlace?'top':'bottom'; tooltip.style.top=`${{Math.round(top)}}px`; tooltip.style.left=`${{Math.round(left)}}px`; }}
  function showTooltip(target,shouldPin=false){{ const term=getTerm(target); if(!term)return; clearTimeout(hideTimer); if(activeTarget&&activeTarget!==target)activeTarget.setAttribute('aria-expanded','false'); activeTarget=target;pinned=shouldPin; const language=document.documentElement.lang==='id'?'id':'en'; tooltipTerm.textContent=term.label[language]||term.label.en; tooltipDefinition.textContent=term.definition[language]||term.definition.en; tooltip.classList.add('is-visible'); tooltip.setAttribute('aria-hidden','false'); target.setAttribute('aria-expanded','true'); requestAnimationFrame(()=>positionTooltip(target)); }}
  function hideTooltip(force=true){{ clearTimeout(hideTimer); if(!force&&pinned)return; activeTarget?.setAttribute('aria-expanded','false'); activeTarget=null;pinned=false;tooltip.classList.remove('is-visible');tooltip.setAttribute('aria-hidden','true'); }}
  document.addEventListener('pointerover',event=>{{const target=event.target.closest?.('.glossary-term');if(target&&event.pointerType!=='touch'&&!pinned)showTooltip(target,false);}});
  document.addEventListener('pointerout',event=>{{const target=event.target.closest?.('.glossary-term');if(target&&!pinned)hideTimer=setTimeout(()=>hideTooltip(false),90);}});
  document.addEventListener('focusin',event=>{{const target=event.target.closest?.('.glossary-term');if(target)showTooltip(target,false);}});
  document.addEventListener('focusout',event=>{{if(event.target.closest?.('.glossary-term')&&!pinned)hideTooltip(true);}});
  document.addEventListener('click',event=>{{const target=event.target.closest?.('.glossary-term');if(target){{event.preventDefault();event.stopPropagation();if(activeTarget===target&&pinned)hideTooltip(true);else showTooltip(target,true);return;}}hideTooltip(true);}});
  document.addEventListener('keydown',event=>{{if(event.key==='Escape')hideTooltip(true);if((event.key==='Enter'||event.key===' ')&&event.target.closest?.('.glossary-term')){{event.preventDefault();event.target.click();}}}});
  window.addEventListener('scroll',()=>{{if(activeTarget&&pinned)positionTooltip(activeTarget);else hideTooltip(true);}},{{passive:true}}); window.addEventListener('resize',()=>activeTarget?positionTooltip(activeTarget):null); window.addEventListener('hashchange',()=>hideTooltip(true));
  const observer=new MutationObserver(mutations=>{{if(mutations.some(m=>m.type==='attributes'&&m.attributeName==='lang'))queueMicrotask(rebuildGlossaryTerms);}}); observer.observe(document.documentElement,{{attributes:true,attributeFilter:['lang']}});
  window.rebuildGlossaryTerms=rebuildGlossaryTerms; rebuildGlossaryTerms();
}})();
"""

    def render_html(self, *, standalone: bool = True) -> str:
        css = (self.template_dir / "styles" / "golden-sample.css").read_text(encoding="utf-8")
        css += """
/* Renderer v0.1 generic additions */
.sheet h2 + .subtitle{margin-top:-8px;margin-bottom:20px;color:var(--muted);font-weight:700}
.scoring-block{margin-top:28px;padding-top:4px}
.data-table thead th,.quarry-build-table thead th,.quarry-development-table thead th{text-align:left}
.audit-status{display:inline-flex;padding:4px 8px;border:1px solid var(--line);border-radius:999px;font-size:.72rem;font-weight:800}
@media(max-width:720px){.facts.three{grid-template-columns:1fr}.journey{grid-template-columns:1fr}.journey article+article{border-left:0;border-top:1px solid var(--line)}}
"""
        sidebar_js = (self.template_dir / "scripts" / "sidebar.js").read_text(encoding="utf-8")
        pages_html = "".join(self._page_html(page) for page in self.pages)
        body = (
            '<button aria-controls="docSidebar" aria-expanded="false" class="mobile-sidebar-button" id="mobileSidebarButton" type="button"><span aria-hidden="true">☰</span><span class="i18n-text" data-en="Menu" data-id="Menu">Menu</span></button>'
            '<button aria-label="Close document navigation" class="sidebar-scrim" hidden id="sidebarScrim" type="button"></button>'
            f"{self._sidebar_html()}<main class=\"document-main\">{pages_html}</main>"
            '<div aria-hidden="true" data-placement="top" id="globalGlossaryTooltip" role="tooltip"><span class="tooltip-term" id="globalGlossaryTooltipTerm"></span><span class="tooltip-definition" id="globalGlossaryTooltipDefinition"></span></div>'
        )
        meta = (
            f'<meta name="document-profile" content="{esc(self.profile)}">'
            f'<meta name="content-version" content="{esc(self.document.get("content_version", "1.0"))}">'
            f'<meta name="template-version" content="{esc(self.template_version)}">'
            f'<meta name="schema-version" content="{esc(self.schema_version)}">'
            f'<meta name="golden-sample" content="{esc(self.golden_sample_version)}">'
            f'<meta name="html-version" content="{esc(self.html_version)}">'
            f'<meta name="content-sha256" content="{esc(self.content_hash)}">'
        )
        style_block = f"<style>{css}</style>" if standalone else '<link rel="stylesheet" href="assets/golden-sample.css">'
        scripts = (
            f"<script>{self._document_controls_js()}</script>"
            f"<script>{self._glossary_js()}</script>"
            f"<script>{sidebar_js}</script>"
        ) if standalone else (
            '<script src="assets/document-controls.js"></script>'
            '<script src="assets/glossary-tooltip.js"></script>'
            '<script src="assets/sidebar.js"></script>'
        )
        primary = self.document.get("primary_language", "en")
        return (
            '<!doctype html><html lang="' + esc(primary) + '" data-default-language="' + esc(primary) + '"><head>'
            '<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            + meta
            + f"<title>{esc(self.title)} — {esc(self.profile_label['en'])}</title>{style_block}</head>"
            f'<body class="theme-normal view-professional" data-overview-page="{esc(self.pages[0].page_id)}">{body}{scripts}</body></html>'
        )

    def write_assets(self, output_dir: Path) -> None:
        assets = output_dir / "assets"
        assets.mkdir(parents=True, exist_ok=True)
        (assets / "golden-sample.css").write_text((self.template_dir / "styles" / "golden-sample.css").read_text(encoding="utf-8"), encoding="utf-8")
        (assets / "document-controls.js").write_text(self._document_controls_js(), encoding="utf-8")
        (assets / "glossary-tooltip.js").write_text(self._glossary_js(), encoding="utf-8")
        (assets / "sidebar.js").write_text((self.template_dir / "scripts" / "sidebar.js").read_text(encoding="utf-8"), encoding="utf-8")

    def render_metrics(self, html_text: str) -> dict[str, Any]:
        id_missing = html_text.count('data-id=""')
        en_missing = html_text.count('data-en=""')
        placeholders = len(PLACEHOLDER_PATTERN.findall(html_text))
        all_term_ids = set(self.glossary_by_id)
        used_term_ids = {term_id for page in self.pages for term_id in page.term_ids if term_id in all_term_ids}
        return {
            "pages": len(self.pages),
            "terms_defined": len(self.glossary_by_id),
            "unused_terms": len(all_term_ids - used_term_ids),
            "missing_term_refs": len(self.missing_terms),
            "id_missing": id_missing,
            "en_missing": en_missing,
            "placeholders": placeholders,
        }
