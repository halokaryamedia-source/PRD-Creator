from __future__ import annotations
from typing import Any
from core import bi, cards, completion_html, esc, i18n, page, requirement_rows, score_html, table, tabs, terms, txt, ul


def overview(data: dict[str, Any]) -> str:
    d, o = data["document"], data["overview"]
    facts = "".join(f'<div class="fact"><b>{i18n(x.get("label", ""))}</b><span>{i18n(x.get("value", ""))}</span></div>' for x in o.get("facts", []))
    journey_src = o.get("journey") or [{"title": x.get("title", x["id"]), "description": x.get("player_result", "")} for x in data.get("gameplay_flow", [])]
    journey = "".join(f'<article><small>{n:02d}</small><strong>{i18n(x.get("title", ""))}</strong><p>{i18n(x.get("description", ""))}</p></article>' for n, x in enumerate(journey_src, 1))
    systems = [bi(f'{txt(x.get("title"))["en"]} — {txt(x.get("description"))["en"]}', f'{txt(x.get("title"))["id"]} — {txt(x.get("description"))["id"]}') for x in o.get("main_systems", [])]
    body = '<div class="cover-rule"></div>' + f'<p class="eyebrow">{i18n(d.get("document_type", bi("Production Specification", "Spesifikasi Produksi")))}</p><h1>{i18n(d["title"])}</h1><p class="subtitle">{i18n(d.get("subtitle", bi("Gameplay & Development Specification", "Spesifikasi Gameplay & Pengembangan")))}</p><p class="lead">{i18n(o.get("project_context", ""))}</p>'
    if o.get("main_experience"): body += f'<h3>{i18n(bi("Main Experience", "Pengalaman Utama"))}</h3><p>{i18n(o["main_experience"])}</p>'
    if facts: body += f'<div class="facts{" three" if len(o.get("facts", [])) == 3 else ""}">{facts}</div>'
    if journey: body += f'<h3>{i18n(bi("Complete Gameplay Journey", "Perjalanan Gameplay Lengkap"))}</h3><div class="journey">{journey}</div>'
    if systems: body += f'<div class="summary-note"><strong>{i18n(bi("Main Systems", "Sistem Utama"))}</strong>{ul(systems)}</div>'
    body += terms(o.get("terms", []))
    ctx = bi(f'Production Development Document · v{d.get("version", "1.0")}', f'Dokumen Pengembangan Produksi · v{d.get("version", "1.0")}')
    return page("summary", "01", bi("Overview", "Gambaran Umum"), body, context=ctx, classes="sheet clean-visible glossary-enabled-page")


def flow_pages(data: dict[str, Any]) -> list[str]:
    out = []
    for n, item in enumerate(data.get("gameplay_flow", [])):
        body = f'<h2>{i18n(item.get("title", ""))}</h2><p class="lead">{i18n(item.get("narrative_context", ""))}</p>'
        body += cards([(bi("Player Experience", "Pengalaman Player"), item.get("player_experience")), (bi("Main Obstacle or Change", "Hambatan atau Perubahan Utama"), item.get("main_obstacle_or_change")), (bi("Player Result", "Hasil Player"), item.get("player_result"))])
        if item.get("next_destination"): body += f'<div class="summary-note"><strong>{i18n(bi("Next Destination", "Tujuan Berikutnya"))}</strong><p>{i18n(item["next_destination"])}</p></div>'
        body += terms(item.get("terms", []))
        out.append(page(f'flow-{item["id"]}', f'02{chr(65+n)}', item.get("title", ""), body, context=item.get("title", ""), classes="sheet clean-visible story-page glossary-enabled-page"))
    return out


def global_pages(data: dict[str, Any]) -> list[str]:
    out = []
    for n, item in enumerate(data.get("global_development", [])):
        flow = [[x.get("step", i), x.get("title", x.get("stage", "")), x.get("description", x.get("details", "")), x.get("result", "")] for i, x in enumerate(item.get("flow", []), 1)]
        body = f'<h2>{i18n(item.get("title", ""))}</h2><p class="lead">{i18n(item.get("overview", ""))}</p>'
        if flow: body += f'<h3>{i18n(bi("Development Flow", "Alur Pengembangan"))}</h3>' + table(["Step", "Stage", "Details", "Result"], flow, "development-flow-table")
        req = requirement_rows(item.get("requirements", []))
        if req: body += f'<h3>{i18n(bi("Development Requirements", "Kebutuhan Pengembangan"))}</h3>' + table(["Group", "Requirement", "Details", "Expected Result"], req, "role-spec-table development-spec-table")
        if item.get("notes"): body += f'<div class="summary-note"><strong>{i18n(bi("Important Notes", "Catatan Penting"))}</strong>{ul(item["notes"])}</div>'
        body += terms(item.get("terms", []))
        out.append(page(f'global-{item["id"]}', f'03{chr(65+n)}', item.get("title", ""), body, context=bi("Global Development", "Pengembangan Global"), classes="sheet professional-only global-development-page glossary-enabled-page"))
    return out


def package_pages(data: dict[str, Any]) -> list[str]:
    out, flow_ids = [], {x["id"] for x in data.get("gameplay_flow", [])}
    for n, pkg in enumerate(data.get("packages", [])):
        pid, code = pkg["id"], 4+n
        label, title = pkg.get("package_label", f"Package {n+1}"), pkg.get("title", pid)
        clean, phase = (f"flow-{pid}" if pid in flow_ids else "summary"), f"dev-{pid}"
        gp = pkg["gameplay"]
        gp_rows = [[x.get("step", i), x.get("title", x.get("stage", "")), x.get("action", x.get("details", "")), x.get("result", "")] for i, x in enumerate(gp.get("player_flow", []), 1)]
        body = tabs(pid, "requirement") + f'<p class="eyebrow">{i18n(label)}</p><h2>{i18n(title)}</h2><p class="lead">{i18n(gp.get("context", gp.get("overview", "")))}</p>'
        if gp.get("main_objective"): body += f'<div class="goal objective-copy"><b>{i18n(bi("Main Objective", "Objektif Utama"))}</b><p>{i18n(gp["main_objective"])}</p></div>'
        body += cards([(bi("Starting Condition", "Kondisi Mulai"), gp.get("start_condition")), (bi("End Condition", "Kondisi Selesai"), gp.get("end_condition")), (bi("Blocked / Fail Condition", "Kondisi Terblokir / Gagal"), gp.get("blocked_or_fail_condition"))])
        if gp_rows: body += f'<h3>{i18n(bi("Player Flow", "Alur Player"))}</h3>' + table(["Step", "Stage", "Player Action", "Result"], gp_rows, "integrated-gameplay-flow-table")
        if gp.get("result"): body += f'<div class="acceptance"><h3>{i18n(bi("Gameplay Result", "Hasil Gameplay"))}</h3><p>{i18n(gp["result"])}</p></div>'
        body += terms(pkg.get("terms", []))
        out.append(page(f"dev-{pid}-requirement", f"{code:02d}A", title, body, context=label, phase=phase, clean=clean, classes="sheet professional-only phase-package-page glossary-enabled-page"))

        ld = pkg["level_design"]
        ld_flow = [[x.get("step", i), x.get("title", x.get("stage", "")), x.get("details", x.get("description", ""))] for i, x in enumerate(ld.get("flow", []), 1)]
        body = tabs(pid, "level") + f'<p class="eyebrow">{i18n(label)}</p><h2>{i18n(title)}</h2><p class="lead">{i18n(ld.get("overview", ""))}</p>'
        if ld_flow: body += f'<h3>{i18n(bi("Level Design Flow", "Alur Level Design"))}</h3>' + table(["Step", "Stage", "Details"], ld_flow, "level-flow-table")
        req = requirement_rows(ld.get("requirements", []), True)
        if req: body += f'<h3>{i18n(bi("Build Requirements", "Kebutuhan Build"))}</h3>' + table(["Group", "Object", "Build & Visual", "Gameplay Function"], req, "role-spec-table level-spec-table")
        if ld.get("notes"): body += f'<div class="summary-note"><strong>{i18n(bi("Important Build Notes", "Catatan Build Penting"))}</strong>{ul(ld["notes"])}</div>'
        body += terms(pkg.get("terms", []))
        out.append(page(f"dev-{pid}-level", f"{code:02d}B", title, body, context=label, phase=phase, clean=clean, classes="sheet professional-only phase-package-page glossary-enabled-page"))

        dev = pkg["developer"]
        dev_flow = [[x.get("step", i), x.get("trigger", x.get("stage", "")), x.get("behavior", x.get("details", "")), x.get("data", ""), x.get("result", "")] for i, x in enumerate(dev.get("flow", []), 1)]
        body = tabs(pid, "developer") + f'<p class="eyebrow">{i18n(label)}</p><h2>{i18n(title)}</h2><p class="lead">{i18n(dev.get("overview", ""))}</p>'
        if dev_flow: body += f'<h3>{i18n(bi("Development Flow", "Alur Development"))}</h3>' + table(["Step", "Trigger", "Behavior", "Data", "Result"], dev_flow, "development-flow-table")
        req = requirement_rows(dev.get("requirements", []))
        if req: body += f'<h3>{i18n(bi("Developer Requirements", "Kebutuhan Developer"))}</h3>' + table(["Group", "Requirement", "Details", "Expected Result"], req, "role-spec-table development-spec-table")
        body += score_html(dev.get("scoring", {})) + completion_html(dev.get("completion_data", {}))
        if dev.get("reset"): body += f'<div class="role-rule-box"><h4>{i18n(bi("Reset / Interruption", "Reset / Interupsi"))}</h4>{ul(dev["reset"])}</div>'
        if dev.get("notes"): body += f'<div class="summary-note"><strong>{i18n(bi("Important Development Notes", "Catatan Development Penting"))}</strong>{ul(dev["notes"])}</div>'
        body += terms(pkg.get("terms", []))
        out.append(page(f"dev-{pid}-developer", f"{code:02d}C", title, body, context=label, phase=phase, clean=clean, classes="sheet professional-only phase-package-page glossary-enabled-page"))
    return out


def navigation(data: dict[str, Any]) -> str:
    nav = [f'<a class="nav-link" data-target="summary" href="#summary"><span class="nav-index">01</span><span class="nav-copy">{i18n(bi("Overview", "Gambaran Umum"))}</span></a>']
    flow = data.get("gameplay_flow", [])
    if flow:
        links = "".join(f'<a data-target="flow-{esc(x["id"])}" href="#flow-{esc(x["id"])}">{i18n(x.get("title", x["id"]))}</a>' for x in flow)
        nav.append(f'<div class="nav-group is-open"><button class="nav-group-toggle" aria-expanded="true"><span class="nav-index">02</span><span class="nav-copy">{i18n(bi("Gameplay Flow", "Alur Gameplay"))}</span></button><div class="nav-submenu">{links}</div></div>')
    glinks = "".join(f'<a data-target="global-{esc(x["id"])}" href="#global-{esc(x["id"])}">{i18n(x.get("title", x["id"]))}</a>' for x in data.get("global_development", []))
    plinks = []
    for n, pkg in enumerate(data.get("packages", [])):
        pid, code = pkg["id"], 4+n
        title, label = pkg.get("title", pid), pkg.get("package_label", f"Package {n+1}")
        sub = "".join(f'<a class="phase-page-link professional-nav-item" data-target="dev-{pid}-{key}" href="#dev-{pid}-{key}"><span>{i18n(name)}</span></a>' for key, name in [("requirement", "Gameplay Overview"), ("level", "Level Design"), ("developer", "Developer")])
        plinks.append(f'<div class="phase-nav-item" data-phase-nav="dev-{pid}"><a class="phase-nav-main" data-section-code="{code:02d}" data-target="dev-{pid}-requirement" href="#dev-{pid}-requirement"><span>{i18n(title)}</span><small>{i18n(label)}</small></a><div class="phase-page-list">{sub}</div></div>')
    if glinks or plinks:
        nav.append(f'<div class="nav-group is-open professional-nav"><button class="nav-group-toggle" aria-expanded="true"><span class="nav-index">03</span><span class="nav-copy">{i18n(bi("Development", "Pengembangan"))}</span></button><div class="nav-submenu">{glinks}</div><div class="nav-submenu phase-navigation">{"".join(plinks)}</div></div>')
    return "".join(nav)


def glossary(data: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    out = {}
    for pkg in data.get("packages", []):
        items = []
        for n, item in enumerate(pkg.get("terms", [])):
            label = txt(item.get("label") or item.get("term") or item.get("key", ""))
            aliases = item.get("aliases") or {"en": [label["en"]], "id": [label["id"]]}
            if isinstance(aliases, list): aliases = {"en": aliases, "id": aliases}
            items.append({"key": str(item.get("key") or f'{pkg["id"]}-{n}'), "label": label, "definition": txt(item.get("definition", "")), "aliases": aliases})
        out[pkg["id"]] = items
    return out
