from __future__ import annotations

import html
import re
from typing import Any


def esc(value: Any) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def present(value: Any) -> bool:
    return value not in (None, "", [], {})


def txt(value: Any) -> dict[str, str]:
    if isinstance(value, dict):
        return {
            "en": "" if value.get("en") is None else str(value["en"]),
            "id": "" if value.get("id") is None else str(value["id"]),
        }
    text = "" if value is None else str(value)
    return {"en": text, "id": text}


def bi(en: str, ind: str | None = None) -> dict[str, str]:
    return {"en": en, "id": ind or en}


def join_text(*values: Any, sep: str = " ") -> dict[str, str]:
    parts = [txt(value) for value in values if present(value)]
    return {
        "en": sep.join(part["en"] for part in parts if part["en"]),
        "id": sep.join(part["id"] for part in parts if part["id"]),
    }


def i18n(value: Any, tag: str = "span") -> str:
    text = txt(value)
    return f'<{tag} class="i18n-text" data-en="{esc(text["en"])}" data-id="{esc(text["id"])}">{esc(text["en"])}</{tag}>'


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "project"


def ul(items: list[Any], cls: str = "clean-list") -> str:
    if not items:
        return ""
    return f'<ul class="{esc(cls)}">' + "".join(f"<li>{i18n(item)}</li>" for item in items) + "</ul>"


def cell_html(value: Any) -> str:
    if isinstance(value, list):
        return ul(value, "compact-cell-list")
    return i18n(value) if present(value) else ""


def production_table(headers: list[Any], rows_html: list[str], cls: str) -> str:
    if not rows_html:
        return ""
    head = ""
    if headers:
        head = "<thead><tr>" + "".join(f"<th>{i18n(header)}</th>" for header in headers) + "</tr></thead>"
    return (
        f'<div class="production-table-wrap"><table class="production-table {esc(cls)}">'
        f"{head}<tbody>{''.join(rows_html)}</tbody></table></div>"
    )


def terms(items: list[dict[str, Any]], panel_id: str, *, glossary_enabled: bool = True) -> str:
    if not items:
        return ""
    rows = "".join(
        f'<div class="definition-item"><b>{i18n(item["label"])}</b><p>{i18n(item["definition"])}</p></div>'
        for item in items
    )
    definition_classes = "definition-list quarry-definition-list"
    if glossary_enabled:
        definition_classes += " glossary-definition-list"
    return (
        '<details class="terms-used-collapsible" data-terms-used=""><summary '
        f'aria-controls="{esc(panel_id)}" class="terms-used-summary">'
        f'<span class="terms-used-title">{i18n(bi("Terms Used", "Istilah yang Digunakan"))}</span>'
        '<span aria-hidden="true" class="terms-used-separator">—</span>'
        '<span class="terms-used-action">'
        f'<span class="terms-used-show-label">{i18n(bi("Show Details", "Tampilkan Detail"))}</span>'
        f'<span class="terms-used-hide-label">{i18n(bi("Hide Details", "Sembunyikan Detail"))}</span>'
        '<span aria-hidden="true" class="terms-used-chevron"></span></span></summary>'
        f'<div class="terms-used-panel" id="{esc(panel_id)}">'
        f'<div class="{definition_classes}">{rows}</div></div></details>'
    )


def cards(items: list[tuple[Any, Any]]) -> str:
    body = "".join(
        f"<article><b>{i18n(label)}</b><p>{i18n(value)}</p></article>" for label, value in items if present(value)
    )
    return f'<div class="phase-context-grid">{body}</div>' if body else ""


def context_block(label: Any, value: Any) -> str:
    if not present(value):
        return ""
    return f'<div class="context-block section-context"><b>{i18n(label)}</b><p>{i18n(value)}</p></div>'


def flow_cards(items: list[dict[str, Any]], cls: str) -> str:
    body = []
    for index, item in enumerate(items, 1):
        step = item.get("step", index)
        body.append(
            f"<article><b>{i18n(str(step).zfill(2))}</b>"
            f"<strong>{i18n(item['title'])}</strong>"
            f"<p>{i18n(item['description'])}</p></article>"
        )
    return f'<div class="flow {esc(cls)}">{"".join(body)}</div>' if body else ""


def sequence(items: list[dict[str, Any]]) -> str:
    body = []
    for item in items:
        text = join_text(item["action"], item["result"], sep=" — ")
        body.append(
            f'<div class="role-step"><div><strong>{i18n(item["title"])}</strong><p>{i18n(text)}</p></div></div>'
        )
    return f'<div class="role-sequence quarry-sequence">{"".join(body)}</div>' if body else ""


def note_grid(items: list[dict[str, Any]]) -> str:
    if not items:
        return ""
    body = "".join(
        f"<article><b>{i18n(item['title'])}</b><p>{i18n(item['description'])}</p></article>" for item in items
    )
    return f'<div class="outcome quarry-note-grid">{body}</div>'


def page(
    pid: str,
    code: str,
    title: Any,
    body: str,
    *,
    context: Any = "",
    classes: str = "sheet",
    phase: str = "",
    clean_target: str = "",
    role: str = "",
    brand: Any = "",
    header: Any = "",
    footer_title: Any = "",
) -> str:
    attrs = [f'class="{esc(classes)}"']
    if clean_target:
        attrs.append(f'data-clean-target="{esc(clean_target)}"')
    if role:
        attrs.append(f'data-page-role="{esc(role)}"')
    if phase:
        attrs.append(f'data-phase="{esc(phase)}"')
    attrs.append(f'id="{esc(pid)}"')
    header_value = header or bi(
        "Gameplay & Development Specification",
        "Spesifikasi Gameplay & Pengembangan",
    )
    footer_brand = brand or title
    footer_copy = footer_title or title
    return (
        f'<section {" ".join(attrs)}><div class="page-head">'
        f"<strong>{i18n(header_value)}</strong><span>{i18n(context)}</span></div>{body}"
        f'<div class="page-foot"><span class="footer-brand">{i18n(footer_brand)}</span>'
        f'<span class="footer-title">{i18n(footer_copy)}</span>'
        f'<span class="footer-code">{i18n(code)}</span></div></section>'
    )


def tabs(pid: str, active: str) -> str:
    items = [
        ("requirement", "1", bi("Gameplay Overview", "Gambaran Gameplay")),
        ("level", "2", bi("Level Design", "Level Design")),
        ("developer", "3", bi("Developer", "Developer")),
    ]
    links = []
    for key, code, label in items:
        target = f"dev-{pid}-{key}"
        current = ' aria-current="page"' if key == active else ""
        active_class = " is-active" if key == active else ""
        links.append(
            f'<a aria-label="Open {esc(txt(label)["en"])}" '
            f'class="section-tab section-tab-link{active_class}" '
            f'data-section-target="{esc(target)}" href="#{esc(target)}"{current}>'
            f"<b>{i18n(code)}</b><span>{i18n(label)}</span></a>"
        )
    return (
        '<div aria-label="Current gameplay development section" '
        'class="section-tabs package-tabs">' + "".join(links) + "</div>"
    )


def weight_text(value: Any) -> str:
    if value in (None, ""):
        return ""
    if isinstance(value, str) and value.strip().endswith("%"):
        return value.strip()
    return f"{value}%"


def _score_table(
    headers: list[Any],
    rows: list[str],
    classes: str = "score-table-wrap quarry-inline-score-table",
) -> str:
    if not rows:
        return ""
    head = "".join(f"<th>{i18n(value)}</th>" for value in headers)
    return (
        f'<div class="{esc(classes)}"><table class="score-table">'
        f"<thead><tr>{head}</tr></thead><tbody>{''.join(rows)}</tbody></table></div>"
    )


def _result_context(data: dict[str, Any]) -> str:
    rows = []
    for label, field in (
        (bi("Final Result", "Hasil Akhir"), "final_result_relationship"),
        (bi("Player-Facing Result", "Hasil yang Ditampilkan ke Player"), "player_facing_display"),
        (bi("Telemetry / Export", "Telemetry / Export"), "telemetry_export"),
    ):
        rows.append(join_text(label, data[field], sep=": "))
    return ul(rows, "compact-cell-list")


def score_html(data: dict[str, Any]) -> str:
    components = data.get("components", [])
    summary = f'<div class="quarry-score-summary"><strong>{i18n(data["score_name"])}</strong>'
    if data.get("scale"):
        summary += f"<span>{i18n(data['scale'])}</span>"
    formula = data.get("formula") or data.get("summary")
    if formula:
        summary += f"<p>{i18n(formula)}</p>"
    summary += "</div>"
    rows = [
        f"<tr><td><b>{i18n(item['name'])}</b></td>"
        f"<td><b>{i18n(weight_text(item['weight']))}</b></td>"
        f"<td>{i18n(item['rule'])}</td></tr>"
        for item in components
    ]
    extra = [
        join_text(bi("Timer Start", "Timer Mulai"), data["timer_start"], sep=": "),
        join_text(bi("Timer Stop", "Timer Berhenti"), data["timer_stop"], sep=": "),
        join_text(
            bi("No-Score Condition", "Kondisi Tanpa Score"),
            data["no_score_condition"],
            sep=": ",
        ),
        join_text(
            bi("Duplicate Prevention", "Pencegahan Duplikasi"),
            data["duplicate_prevention"],
            sep=": ",
        ),
    ]
    return (
        summary
        + _score_table(
            [
                bi("Component", "Komponen"),
                bi("Weight", "Bobot"),
                bi("Required Rule", "Aturan Wajib"),
            ],
            rows,
        )
        + ul(extra, "compact-cell-list")
        + _result_context(data)
    )


def completion_html(data: dict[str, Any]) -> str:
    summary_text = data.get("summary") or data["handoff_result"]
    summary = (
        f'<div class="quarry-score-summary phase-score-summary">'
        f"<strong>{i18n(data['completion_name'])}</strong>"
        f"<span>{i18n(bi('No Objective Score', 'Tanpa Objective Score'))}</span>"
        f"<p>{i18n(summary_text)}</p></div>"
    )
    mapping = [
        (
            bi("Completion", "Penyelesaian"),
            bi("Required", "Wajib"),
            data["valid_completion_condition"],
        ),
        (
            bi("Recorded Data", "Data yang Dicatat"),
            bi("Completion", "Penyelesaian"),
            data["recorded_data"],
        ),
        (
            bi("Incomplete Session", "Sesi Belum Selesai"),
            bi("No Result", "Tanpa Hasil"),
            data["interrupted_completion_behavior"],
        ),
        (
            bi("Duplicate Prevention", "Pencegahan Duplikasi"),
            bi("Required", "Wajib"),
            data["duplicate_prevention"],
        ),
    ]
    rows = [
        f"<tr><td><b>{i18n(component)}</b></td><td><b>{i18n(status)}</b></td><td>{i18n(rule)}</td></tr>"
        for component, status, rule in mapping
    ]
    return (
        summary
        + _score_table(
            [
                bi("Component", "Komponen"),
                bi("Status", "Status"),
                bi("Required Rule", "Aturan Wajib"),
            ],
            rows,
            "score-table-wrap quarry-inline-score-table phase-inline-score-table",
        )
        + _result_context(data)
    )
