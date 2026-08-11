from __future__ import annotations
import html, re
from typing import Any


def esc(v: Any) -> str:
    return html.escape("" if v is None else str(v), quote=True)


def present(v: Any) -> bool:
    return v not in (None, "", [], {})


def txt(v: Any) -> dict[str, str]:
    if isinstance(v, dict):
        en, ind = v.get("en"), v.get("id")
        return {"en": "" if en is None else str(en), "id": "" if ind is None else str(ind)}
    s = "" if v is None else str(v)
    return {"en": s, "id": s}


def bi(en: str, ind: str | None = None) -> dict[str, str]:
    return {"en": en, "id": ind or en}


def join_text(*values: Any, sep: str = " ") -> dict[str, str]:
    parts = [txt(value) for value in values if present(value)]
    return {
        "en": sep.join(part["en"] for part in parts if part["en"]),
        "id": sep.join(part["id"] for part in parts if part["id"]),
    }


def i18n(v: Any, tag: str = "span") -> str:
    t = txt(v)
    return f'<{tag} class="i18n-text" data-en="{esc(t["en"])}" data-id="{esc(t["id"])}">{esc(t["en"])}</{tag}>'


def slug(v: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", v.lower()).strip("-") or "project"


def ul(items: list[Any], cls: str = "clean-list") -> str:
    return f'<ul class="{esc(cls)}">' + "".join(f"<li>{i18n(x)}</li>" for x in items) + "</ul>" if items else ""


def cell_html(value: Any) -> str:
    if isinstance(value, list):
        return ul(value, "compact-cell-list")
    return i18n(value) if present(value) else ""


def table(headers: list[Any], rows: list[list[Any]], cls: str = "role-spec-table") -> str:
    if not rows:
        return ""
    h = "".join(f"<th>{i18n(x)}</th>" for x in headers)
    b = "".join("<tr>" + "".join(f"<td>{cell_html(x)}</td>" for x in row) + "</tr>" for row in rows)
    return f'<div class="role-table-wrap"><table class="{esc(cls)}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def production_table(headers: list[Any], rows_html: list[str], cls: str) -> str:
    if not rows_html:
        return ""
    head = ""
    if headers:
        head = '<thead><tr>' + "".join(f"<th>{i18n(x)}</th>" for x in headers) + "</tr></thead>"
    return f'<div class="production-table-wrap"><table class="production-table {esc(cls)}">{head}<tbody>{"".join(rows_html)}</tbody></table></div>'


def terms(items: list[dict[str, Any]], panel_id: str) -> str:
    if not items:
        return ""
    rows = "".join(
        f'<div class="definition-item"><b>{i18n(x.get("label") or x.get("term") or x.get("key", ""))}</b><p>{i18n(x.get("definition", ""))}</p></div>'
        for x in items
    )
    return (
        '<details class="terms-used-collapsible" data-terms-used=""><summary '
        f'aria-controls="{esc(panel_id)}" class="terms-used-summary">'
        f'<span class="terms-used-title">{i18n(bi("Terms Used", "Istilah yang Digunakan"))}</span>'
        '<span aria-hidden="true" class="terms-used-separator">—</span>'
        '<span class="terms-used-action">'
        f'<span class="terms-used-show-label">{i18n(bi("Show Details", "Tampilkan Detail"))}</span>'
        f'<span class="terms-used-hide-label">{i18n(bi("Hide Details", "Sembunyikan Detail"))}</span>'
        '<span aria-hidden="true" class="terms-used-chevron"></span></span></summary>'
        f'<div class="terms-used-panel" id="{esc(panel_id)}"><div class="definition-list quarry-definition-list glossary-definition-list">{rows}</div></div></details>'
    )


def cards(items: list[tuple[Any, Any]]) -> str:
    body = "".join(
        f'<article><b>{i18n(k)}</b><p>{i18n(v)}</p></article>'
        for k, v in items if present(v)
    )
    return f'<div class="phase-context-grid">{body}</div>' if body else ""


def context_block(label: Any, value: Any) -> str:
    if not present(value):
        return ""
    return f'<div class="context-block section-context"><b>{i18n(label)}</b><p>{i18n(value)}</p></div>'


def flow_cards(items: list[dict[str, Any]], cls: str) -> str:
    if not items:
        return ""
    body = []
    for index, item in enumerate(items, 1):
        step = item.get("step", index)
        title = item.get("title") or item.get("stage") or item.get("trigger") or ""
        description = item.get("description") or item.get("details") or item.get("action") or item.get("behavior") or ""
        body.append(f'<article><b>{i18n(str(step).zfill(2))}</b><strong>{i18n(title)}</strong><p>{i18n(description)}</p></article>')
    columns = min(len(body), 4)
    return f'<div class="flow {esc(cls)}" style="--prd-flow-columns:{columns}">{"".join(body)}</div>'


def sequence(items: list[dict[str, Any]]) -> str:
    if not items:
        return ""
    body = []
    for item in items:
        title = item.get("title") or item.get("stage") or ""
        description = item.get("description") or item.get("action") or item.get("details") or ""
        result = item.get("result")
        text = join_text(description, result, sep=" — ") if present(result) else description
        body.append(f'<div class="role-step"><div><strong>{i18n(title)}</strong><p>{i18n(text)}</p></div></div>')
    return f'<div class="role-sequence quarry-sequence">{"".join(body)}</div>'


def note_grid(items: list[Any]) -> str:
    if not items:
        return ""
    body = []
    for item in items:
        if isinstance(item, dict):
            title = item.get("title") or item.get("label") or bi("Important Note", "Catatan Penting")
            description = item.get("description") or item.get("details") or item.get("note") or ""
        else:
            title = bi("Important Note", "Catatan Penting")
            description = item
        body.append(f'<article><b>{i18n(title)}</b><p>{i18n(description)}</p></article>')
    return f'<div class="outcome quarry-note-grid">{"".join(body)}</div>'


def page(
    pid: str,
    code: str,
    title: Any,
    body: str,
    *,
    context: Any = "",
    classes: str = "sheet",
    phase: str = "",
    clean: str = "",
    role: str = "",
    brand: Any = "",
    header: Any = "",
    footer_title: Any = "",
) -> str:
    attrs = [f'class="{esc(classes)}"', f'id="{esc(pid)}"']
    if phase:
        attrs.append(f'data-phase="{esc(phase)}"')
    if clean:
        attrs.append(f'data-clean-target="{esc(clean)}"')
    if role:
        attrs.append(f'data-page-role="{esc(role)}"')
    header_value = header or bi("Gameplay & Development Specification", "Spesifikasi Gameplay & Pengembangan")
    footer_brand = brand or title
    footer_copy = footer_title or title
    return (
        f'<section {" ".join(attrs)}><div class="page-head"><strong>{i18n(header_value)}</strong><span>{i18n(context)}</span></div>{body}'
        f'<div class="page-foot"><span class="footer-brand">{i18n(footer_brand)}</span><span class="footer-title">{i18n(footer_copy)}</span><span class="footer-code">{i18n(code)}</span></div></section>'
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
        active_attrs = ' aria-current="page"' if key == active else ""
        active_class = " is-active" if key == active else ""
        links.append(
            f'<a aria-label="Open {esc(txt(label)["en"])}" class="section-tab section-tab-link{active_class}" data-section-target="{esc(target)}" href="#{esc(target)}"{active_attrs}>'
            f'<b>{i18n(code)}</b><span>{i18n(label)}</span></a>'
        )
    return '<div aria-label="Current gameplay development section" class="section-tabs package-tabs">' + "".join(links) + "</div>"


def weight_text(value: Any) -> str:
    if value in (None, ""):
        return ""
    if isinstance(value, str) and value.strip().endswith("%"):
        return value.strip()
    return f"{value}%"


def _score_table(headers: list[Any], rows: list[str]) -> str:
    if not rows:
        return ""
    head = "".join(f"<th>{i18n(value)}</th>" for value in headers)
    return (
        '<div class="score-table-wrap quarry-inline-score-table phase-inline-score-table">'
        f'<table class="score-table"><thead><tr>{head}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'
    )


def _result_context(data: dict[str, Any]) -> str:
    rows = []
    for label, value in [
        (bi("Final Result", "Hasil Akhir"), data.get("final_result_relationship")),
        (bi("Player-Facing Result", "Hasil yang Ditampilkan ke Player"), data.get("player_facing_display")),
        (bi("Telemetry / Export", "Telemetry / Export"), data.get("telemetry_export")),
    ]:
        if present(value):
            rows.append(join_text(label, value, sep=": "))
    return ul(rows, "compact-cell-list") if rows else ""


def score_html(data: dict[str, Any]) -> str:
    if not data:
        return ""
    components = [item for item in data.get("components", []) if isinstance(item, dict)]
    score_name = data.get("score_name", bi("Score", "Score"))
    scale = data.get("scale") or data.get("score_scale") or ""
    formula = data.get("formula") or data.get("summary")
    if not present(formula) and components:
        en_parts = [f'{weight_text(item.get("weight"))} {txt(item.get("name", ""))["en"]}'.strip() for item in components]
        id_parts = [f'{weight_text(item.get("weight"))} {txt(item.get("name", ""))["id"]}'.strip() for item in components]
        formula = {"en": " + ".join(en_parts), "id": " + ".join(id_parts)}
    summary = f'<div class="quarry-score-summary phase-score-summary"><strong>{i18n(score_name)}</strong>'
    if present(scale):
        summary += f'<span>{i18n(scale)}</span>'
    if present(formula):
        summary += f'<p>{i18n(formula)}</p>'
    summary += "</div>"
    rows = [
        f'<tr><td><b>{i18n(item.get("name", ""))}</b></td><td><b>{i18n(weight_text(item.get("weight")))}</b></td><td>{i18n(item.get("rule", ""))}</td></tr>'
        for item in components
    ]
    extra = []
    for label, value in [
        (bi("Timer Start", "Timer Mulai"), data.get("timer_start")),
        (bi("Timer Stop", "Timer Berhenti"), data.get("timer_stop")),
        (bi("No-Score Condition", "Kondisi Tanpa Score"), data.get("no_score_condition")),
        (bi("Duplicate Prevention", "Pencegahan Duplikasi"), data.get("duplicate_prevention")),
    ]:
        if present(value):
            extra.append(join_text(label, value, sep=": "))
    return summary + _score_table(
        [bi("Component", "Komponen"), bi("Weight", "Bobot"), bi("Required Rule", "Aturan Wajib")],
        rows,
    ) + (ul(extra, "compact-cell-list") if extra else "") + _result_context(data)


def completion_html(data: dict[str, Any]) -> str:
    if not data:
        return ""
    name = data.get("completion_name", bi("Completion", "Penyelesaian"))
    status = bi("Produces Score", "Menghasilkan Score") if data.get("produces_score") else bi("No Objective Score", "Tanpa Objective Score")
    summary = (
        f'<div class="quarry-score-summary phase-score-summary"><strong>{i18n(name)}</strong><span>{i18n(status)}</span>'
        f'<p>{i18n(data.get("summary") or data.get("handoff_result") or "")}</p></div>'
    )
    rows = []
    mapping = [
        (bi("Completion", "Penyelesaian"), bi("Required", "Wajib"), data.get("valid_completion_condition")),
        (bi("Recorded Data", "Data yang Dicatat"), bi("Completion", "Penyelesaian"), data.get("recorded_data")),
        (bi("Incomplete Session", "Sesi Belum Selesai"), bi("No Result", "Tanpa Hasil"), data.get("interrupted_completion_behavior")),
        (bi("Duplicate Prevention", "Pencegahan Duplikasi"), bi("Required", "Wajib"), data.get("duplicate_prevention")),
    ]
    for component, row_status, rule in mapping:
        if present(rule):
            rows.append(f'<tr><td><b>{i18n(component)}</b></td><td><b>{i18n(row_status)}</b></td><td>{i18n(rule)}</td></tr>')
    return summary + _score_table(
        [bi("Component", "Komponen"), bi("Status", "Status"), bi("Required Rule", "Aturan Wajib")],
        rows,
    ) + _result_context(data)
