from __future__ import annotations
import html, re
from typing import Any


def esc(v: Any) -> str:
    return html.escape("" if v is None else str(v), quote=True)


def txt(v: Any) -> dict[str, str]:
    if isinstance(v, dict):
        en, ind = v.get("en"), v.get("id")
        en = ind if en is None else en
        ind = en if ind is None else ind
        return {"en": "" if en is None else str(en), "id": "" if ind is None else str(ind)}
    s = "" if v is None else str(v)
    return {"en": s, "id": s}


def bi(en: str, ind: str | None = None) -> dict[str, str]:
    return {"en": en, "id": ind or en}


def i18n(v: Any, tag: str = "span") -> str:
    t = txt(v)
    return f'<{tag} class="i18n-text" data-en="{esc(t["en"])}" data-id="{esc(t["id"])}">{esc(t["en"])}</{tag}>'


def slug(v: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", v.lower()).strip("-") or "project"


def ul(items: list[Any]) -> str:
    return '<ul class="clean-list">' + "".join(f"<li>{i18n(x)}</li>" for x in items) + "</ul>" if items else ""


def table(headers: list[Any], rows: list[list[Any]], cls: str = "role-spec-table") -> str:
    if not rows: return ""
    h = "".join(f"<th>{i18n(x)}</th>" for x in headers)
    b = "".join("<tr>" + "".join(f"<td>{i18n(x)}</td>" for x in row) + "</tr>" for row in rows)
    return f'<div class="role-table-wrap"><table class="{esc(cls)}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def terms(items: list[dict[str, Any]]) -> str:
    if not items: return ""
    rows = "".join(f'<div class="definition-item"><dt>{i18n(x.get("label") or x.get("term") or x.get("key", ""))}</dt><dd>{i18n(x.get("definition", ""))}</dd></div>' for x in items)
    return ('<details class="terms-used-collapsible"><summary class="terms-used-summary">'
            f'<span class="terms-used-title">{i18n(bi("Terms Used", "Istilah yang Digunakan"))}</span>'
            f'<span class="terms-used-action">{i18n(bi("Show / hide definitions", "Tampilkan / sembunyikan definisi"))}</span>'
            f'</summary><div class="terms-used-panel"><dl class="definition-list">{rows}</dl></div></details>')


def cards(items: list[tuple[Any, Any]]) -> str:
    body = "".join(f'<article><b>{i18n(k)}</b><p>{i18n(v)}</p></article>' for k, v in items if v not in (None, "", [], {}))
    return f'<div class="phase-context-grid">{body}</div>' if body else ""


def page(pid: str, code: str, title: Any, body: str, *, context: Any = "", classes: str = "sheet", phase: str = "", clean: str = "") -> str:
    attrs = [f'class="{esc(classes)}"', f'id="{esc(pid)}"']
    if phase: attrs.append(f'data-phase="{esc(phase)}"')
    if clean: attrs.append(f'data-clean-target="{esc(clean)}"')
    header = i18n(bi("Gameplay & Development Specification", "Spesifikasi Gameplay & Pengembangan"))
    return (f'<section {" ".join(attrs)}><div class="page-head"><strong>{header}</strong><span>{i18n(context)}</span></div>{body}'
            f'<div class="page-foot"><span class="footer-brand">MIVUBI</span><span class="footer-title">{i18n(title)}</span><span class="footer-code">{esc(code)}</span></div></section>')


def tabs(pid: str, active: str) -> str:
    items = [("requirement", "A", "Gameplay Overview"), ("level", "B", "Level Design"), ("developer", "C", "Developer")]
    return '<nav class="section-tabs">' + "".join(f'<a class="section-tab section-tab-link{" is-active" if key == active else ""}" data-target="dev-{esc(pid)}-{key}" href="#dev-{esc(pid)}-{key}"><b>{code}</b>{i18n(label)}</a>' for key, code, label in items) + '</nav>'


def requirement_rows(groups: list[dict[str, Any]], level: bool = False) -> list[list[Any]]:
    rows = []
    for group in groups:
        title = group.get("title") or group.get("group_title") or ""
        for item in group.get("items") or group.get("objects") or []:
            if level:
                rows.append([title, item.get("object", item.get("title", "")), item.get("build_and_visual", item.get("requirements", "")), item.get("gameplay_function", item.get("result", ""))])
            else:
                rows.append([title, item.get("title", item.get("requirement", "")), item.get("details", item.get("requirements", "")), item.get("result", item.get("expected_result", ""))])
    return rows


def score_html(data: dict[str, Any]) -> str:
    if not data: return ""
    rows = [[x.get("name", ""), f'{x.get("weight", "")}%', x.get("rule", bi("Contributes to final score", "Berkontribusi pada score akhir"))] for x in data.get("components", [])]
    info = [[bi("Timer Start", "Timer Mulai"), data.get("timer_start", "")], [bi("Timer Stop", "Timer Berhenti"), data.get("timer_stop", "")], [bi("No-Score Condition", "Kondisi Tanpa Score"), data.get("no_score_condition", "")], [bi("Duplicate Prevention", "Pencegahan Duplikasi"), data.get("duplicate_prevention", "")], [bi("Final Result", "Hasil Akhir"), data.get("final_result_relationship", "")]]
    return f'<h3>{i18n(data.get("score_name", bi("Scoring", "Scoring")))}</h3>' + table(["Component", "Weight", "Rule"], rows) + table(["Rule", "Definition"], [x for x in info if x[1] not in (None, "", [], {})])


def completion_html(data: dict[str, Any]) -> str:
    if not data: return ""
    rows = [[bi("Produces Score", "Menghasilkan Score"), bi("Yes", "Ya") if data.get("produces_score") else bi("No", "Tidak")], [bi("Valid Completion", "Penyelesaian Valid"), data.get("valid_completion_condition", "")], [bi("Recorded Data", "Data yang Dicatat"), data.get("recorded_data", "")], [bi("Interruption", "Interupsi"), data.get("interrupted_completion_behavior", "")], [bi("Duplicate Prevention", "Pencegahan Duplikasi"), data.get("duplicate_prevention", "")], [bi("Handoff Result", "Hasil Handoff"), data.get("handoff_result", "")]]
    return f'<h3>{i18n(bi("Completion Data", "Data Penyelesaian"))}</h3>' + table(["Rule", "Definition"], [x for x in rows if x[1] not in (None, "", [], {})])
