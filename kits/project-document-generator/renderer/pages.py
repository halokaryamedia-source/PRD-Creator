from __future__ import annotations
from typing import Any
from core import (
    bi,
    cards,
    cell_html,
    completion_html,
    context_block,
    esc,
    flow_cards,
    i18n,
    join_text,
    note_grid,
    page,
    present,
    production_table,
    score_html,
    sequence,
    tabs,
    terms,
    txt,
    ul,
)


def heading(value: Any) -> str:
    return f'<h3 class="package-section-heading">{i18n(value)}</h3>'


def overview(data: dict[str, Any]) -> str:
    d, o = data["document"], data["overview"]
    brand = d.get("brand") or d["title"]
    facts = "".join(
        f'<div class="fact"><b>{i18n(x.get("label", ""))}</b><span>{i18n(x.get("value", ""))}</span></div>'
        for x in o.get("facts", [])
    )
    journey_src = o.get("journey") or [
        {"title": x.get("title", x["id"]), "description": x.get("player_result", "")}
        for x in data.get("gameplay_flow", [])
    ]
    journey = "".join(
        f'<article><small>{n:02d}</small><strong>{i18n(x.get("title", ""))}</strong><p>{i18n(x.get("description", ""))}</p></article>'
        for n, x in enumerate(journey_src, 1)
    )
    systems = [
        join_text(x.get("title"), x.get("description"), sep=" — ")
        for x in o.get("main_systems", [])
        if present(x.get("title")) or present(x.get("description"))
    ]
    body = (
        '<div class="cover-rule"></div>'
        f'<p class="eyebrow">{i18n(d.get("document_type", bi("Production Specification", "Spesifikasi Produksi")))}</p>'
        f'<h1>{i18n(d["title"])}</h1>'
        f'<p class="subtitle">{i18n(d.get("subtitle", bi("Gameplay & Development Specification", "Spesifikasi Gameplay & Pengembangan")))}</p>'
        f'<p class="lead">{i18n(o.get("project_context", ""))}</p>'
    )
    if o.get("main_experience"):
        body += f'<h3>{i18n(bi("Main Experience", "Pengalaman Utama"))}</h3><p>{i18n(o["main_experience"])}</p>'
    if facts:
        body += f'<div class="facts{" three" if len(o.get("facts", [])) == 3 else ""}">{facts}</div>'
    if journey:
        body += f'<h3>{i18n(bi("Complete Gameplay Journey", "Perjalanan Gameplay Lengkap"))}</h3><div class="journey">{journey}</div>'
    if systems:
        body += f'<div class="summary-note"><strong>{i18n(bi("Main Systems", "Sistem Utama"))}</strong>{ul(systems)}</div>'
    body += terms(o.get("terms", []), "summary-terms-used-details")
    ctx = bi(
        f'Production Development Document · v{d.get("version", "1.0")}',
        f'Dokumen Pengembangan Produksi · v{d.get("version", "1.0")}',
    )
    return page(
        "summary",
        "01",
        bi("Overview", "Gambaran Umum"),
        body,
        context=ctx,
        classes="sheet clean-visible glossary-enabled-page",
        brand=brand,
        footer_title=bi("Overview", "Gambaran Umum"),
    )


def _narrative_beats(item: dict[str, Any]) -> list[dict[str, Any]]:
    explicit = item.get("beats")
    if isinstance(explicit, list) and explicit:
        return [beat for beat in explicit if isinstance(beat, dict)]
    beats = []
    for title, value in [
        (bi("Player Experience", "Pengalaman Player"), item.get("player_experience")),
        (bi("Main Obstacle or Change", "Hambatan atau Perubahan Utama"), item.get("main_obstacle_or_change")),
        (bi("Player Result", "Hasil Player"), item.get("player_result")),
    ]:
        if present(value):
            beats.append({"title": title, "description": value})
    if not beats and present(item.get("narrative_context")):
        beats.append({"title": item.get("title", ""), "description": item.get("narrative_context")})
    return beats


def flow_pages(data: dict[str, Any]) -> list[str]:
    out = []
    brand = data["document"].get("brand") or data["document"]["title"]
    for n, item in enumerate(data.get("gameplay_flow", [])):
        pid = f'flow-{item["id"]}'
        beats = _narrative_beats(item)
        beat_html = "".join(
            f'<div class="narrative-beat"><div class="narrative-index">{index:02d}</div>'
            f'<div class="narrative-copy"><strong>{i18n(beat.get("title", ""))}</strong><p>{i18n(beat.get("description", beat.get("details", "")))}</p></div></div>'
            for index, beat in enumerate(beats, 1)
        )
        body = f'<h2>{i18n(item.get("title", ""))}</h2>'
        if item.get("narrative_context"):
            body += f'<p class="section-intro">{i18n(item["narrative_context"])}</p>'
        body += f'<div class="narrative-sequence">{beat_html}</div>'
        if item.get("next_destination"):
            body += f'<div class="story-transition"><p>{i18n(join_text(bi("Next:", "Berikutnya:"), item["next_destination"]))}</p></div>'
        body += terms(item.get("terms", []), f"{pid}-terms-used-details")
        out.append(
            page(
                pid,
                f'02{chr(65+n)}',
                item.get("title", ""),
                body,
                context=item.get("title", ""),
                header=bi("02 — Gameplay Flow", "02 — Alur Gameplay"),
                footer_title=join_text(bi("Gameplay Flow", "Alur Gameplay"), item.get("title", ""), sep=" · "),
                brand=brand,
                classes="sheet clean-visible story-page narrative-page glossary-enabled-page",
            )
        )
    return out


def _global_tabs(items: list[dict[str, Any]], active_id: str) -> str:
    links = []
    for index, item in enumerate(items, 1):
        target = f'global-{item["id"]}'
        active = item["id"] == active_id
        active_class = " is-active" if active else ""
        current = ' aria-current="page"' if active else ""
        title = item.get("title", item["id"])
        links.append(
            f'<a aria-label="Open {esc(txt(title)["en"])}" class="section-tab section-tab-link{active_class}" '
            f'data-section-target="{esc(target)}" href="#{esc(target)}"{current}>'
            f'<b>{i18n(str(index))}</b><span>{i18n(title)}</span></a>'
        )
    return '<div aria-label="Development section navigation" class="section-tabs package-tabs">' + "".join(links) + "</div>"


def _requirement_rows(groups: list[dict[str, Any]]) -> list[str]:
    rows: list[str] = []
    for group_index, group in enumerate(groups, 1):
        items = group.get("items") or group.get("objects") or []
        group_title = group.get("title") or group.get("group_title") or ""
        if present(group_title):
            rows.append(f'<tr class="quarry-group-row"><td><b>{group_index}</b></td><td colspan="3"><b>{i18n(group_title)}</b></td></tr>')
        for item_index, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            code = item.get("code") or chr(65 + item_index)
            title = item.get("title") or item.get("requirement") or item.get("object") or ""
            details = item.get("details", item.get("requirements", ""))
            result = item.get("result", item.get("expected_result", item.get("gameplay_function", "")))
            rows.append(f'<tr><td><b>{i18n(code)}</b></td><td><b>{i18n(title)}</b></td><td>{cell_html(details)}</td><td>{cell_html(result)}</td></tr>')
    return rows


def global_pages(data: dict[str, Any]) -> list[str]:
    out = []
    items = data.get("global_development", [])
    brand = data["document"].get("brand") or data["document"]["title"]
    for n, item in enumerate(items):
        pid = f'global-{item["id"]}'
        body = (
            f'<h2 class="development-package-title">{i18n(item.get("title", ""))}</h2>'
            f'<p class="development-package-subtitle">{i18n(item.get("subtitle") or bi("Project-wide development", "Development seluruh project"))}</p>'
            + _global_tabs(items, item["id"])
            + context_block(join_text(item.get("title", ""), bi("Overview", "Overview")), item.get("overview", ""))
        )
        flow = [entry for entry in item.get("flow", []) if isinstance(entry, dict)]
        if flow:
            body += heading(bi("Development Flow", "Alur Development")) + flow_cards(flow, "quarry-development-flow")
        req_rows = _requirement_rows(item.get("requirements", []))
        if req_rows:
            body += heading(bi("Development Requirements", "Kebutuhan Development")) + production_table(
                [bi("No.", "No."), bi("Setup", "Setup"), bi("Development Requirements", "Kebutuhan Development"), bi("System Result", "Hasil Sistem")],
                req_rows,
                "quarry-dev-table",
            )
        if item.get("notes"):
            body += heading(bi("Important Development Notes", "Catatan Development Penting")) + note_grid(item["notes"])
        body += terms(item.get("terms", []), f"{pid}-terms-used-details")
        out.append(
            page(
                pid,
                f'03{chr(65+n)}',
                item.get("title", ""),
                body,
                context=item.get("title", ""),
                header=bi("03 — Development", "03 — Development"),
                footer_title=join_text(bi("Development", "Development"), item.get("title", ""), sep=" · "),
                brand=brand,
                phase="dev-system",
                clean="summary",
                role="developer-overview",
                classes="sheet professional-only quarry-package-page phase-package-page global-development-page glossary-enabled-page",
            )
        )
    return out


def _gameplay_info_rows(pkg: dict[str, Any]) -> list[str]:
    gp = pkg["gameplay"]
    dev = pkg["developer"]
    scoring_criteria = gp.get("scoring_criteria") or gp.get("scoring_summary")
    if not present(scoring_criteria) and dev.get("scoring"):
        score = dev["scoring"]
        components = [item for item in score.get("components", []) if isinstance(item, dict)]
        if components:
            en_formula = " + ".join(f'{item.get("weight", "")}% {txt(item.get("name", ""))["en"]}' for item in components)
            id_formula = " + ".join(f'{item.get("weight", "")}% {txt(item.get("name", ""))["id"]}' for item in components)
            score_name = txt(score.get("score_name", bi("Score", "Score")))
            scoring_criteria = {"en": f'{score_name["en"]}: {en_formula}', "id": f'{score_name["id"]}: {id_formula}'}
    elif not present(scoring_criteria) and dev.get("completion_data"):
        scoring_criteria = dev["completion_data"].get("summary") or dev["completion_data"].get("valid_completion_condition")
    pairs = [
        (bi("Game Purpose", "Tujuan Gameplay"), gp.get("purpose") or gp.get("game_purpose")),
        (bi("Gameplay Time", "Waktu Gameplay"), gp.get("gameplay_time") or gp.get("estimated_time") or gp.get("duration")),
        (bi("Starting Condition", "Kondisi Awal"), gp.get("start_condition")),
        (bi("End Condition", "Kondisi Selesai"), gp.get("end_condition")),
        (bi("Fail Condition", "Kondisi Gagal"), gp.get("blocked_or_fail_condition")),
        (bi("Scoring Criteria", "Kriteria Scoring"), scoring_criteria),
    ]
    return [f'<tr><td><b>{i18n(label)}</b></td><td>{cell_html(value)}</td></tr>' for label, value in pairs if present(value)]


def _level_requirement_rows(groups: list[dict[str, Any]]) -> list[str]:
    rows: list[str] = []
    number = 1
    multiple_groups = len(groups) > 1
    for group_index, group in enumerate(groups, 1):
        items = group.get("items") or group.get("objects") or []
        group_title = group.get("title") or group.get("group_title") or ""
        if multiple_groups and present(group_title):
            rows.append(f'<tr class="quarry-group-row"><td><b>{group_index}</b></td><td colspan="4"><b>{i18n(group_title)}</b></td></tr>')
        for item in items:
            if not isinstance(item, dict):
                continue
            code = item.get("no") or item.get("number") or number
            number += 1
            title = item.get("object") or item.get("title") or ""
            subtitle = item.get("subtitle") or (group_title if not multiple_groups else "")
            object_cell = f'<b>{i18n(title)}</b>' + (f'<small>{i18n(subtitle)}</small>' if present(subtitle) else "")
            area = item.get("area_size") or item.get("size") or item.get("dimensions") or "—"
            build = item.get("build_and_visual") or item.get("requirements") or item.get("details") or ""
            function = item.get("gameplay_function") or item.get("result") or ""
            rows.append(f'<tr><td><b>{i18n(code)}</b></td><td>{object_cell}</td><td>{cell_html(area)}</td><td>{cell_html(build)}</td><td>{cell_html(function)}</td></tr>')
            for child_index, child in enumerate(item.get("children", [])):
                if not isinstance(child, dict):
                    continue
                child_code = child.get("code") or chr(65 + child_index)
                child_title = child.get("object") or child.get("title") or ""
                child_area = child.get("area_size") or child.get("size") or "—"
                child_build = child.get("build_and_visual") or child.get("requirements") or child.get("details") or ""
                child_function = child.get("gameplay_function") or child.get("result") or ""
                rows.append(
                    f'<tr class="quarry-child-row"><td><b>{i18n(child_code)}</b></td><td><b>{i18n(child_title)}</b></td>'
                    f'<td>{cell_html(child_area)}</td><td>{cell_html(child_build)}</td><td>{cell_html(child_function)}</td></tr>'
                )
    return rows


def _developer_requirement_rows(dev: dict[str, Any]) -> list[str]:
    rows: list[str] = []
    group_number = 1
    for group in dev.get("requirements", []):
        if not isinstance(group, dict):
            continue
        title = group.get("title") or group.get("group_title") or ""
        items = group.get("items") or group.get("objects") or []
        if present(title):
            rows.append(f'<tr class="quarry-group-row"><td><b>{group_number}</b></td><td colspan="3"><b>{i18n(title)}</b></td></tr>')
        for item_index, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            code = item.get("code") or chr(65 + item_index)
            name = item.get("title") or item.get("requirement") or ""
            details = item.get("details") or item.get("requirements") or ""
            result = item.get("result") or item.get("expected_result") or item.get("gameplay_function") or ""
            rows.append(f'<tr><td><b>{i18n(code)}</b></td><td><b>{i18n(name)}</b></td><td>{cell_html(details)}</td><td>{cell_html(result)}</td></tr>')
        group_number += 1
    if dev.get("scoring"):
        scoring = dev["scoring"]
        rows.append(f'<tr class="quarry-group-row"><td><b>{group_number}</b></td><td colspan="3"><b>{i18n(bi("Scoring Setup", "Scoring Setup"))}</b></td></tr>')
        rows.append(
            f'<tr><td><b>A</b></td><td><b>{i18n(scoring.get("score_name", bi("Scoring", "Scoring")))}</b></td>'
            f'<td>{score_html(scoring)}</td><td>{cell_html(scoring.get("final_result_relationship", ""))}</td></tr>'
        )
        group_number += 1
    elif dev.get("completion_data"):
        completion = dev["completion_data"]
        rows.append(f'<tr class="quarry-group-row"><td><b>{group_number}</b></td><td colspan="3"><b>{i18n(bi("Completion and Data", "Penyelesaian dan Data"))}</b></td></tr>')
        rows.append(
            f'<tr><td><b>A</b></td><td><b>{i18n(completion.get("completion_name", bi("Completion State", "Kondisi Selesai")))}</b></td>'
            f'<td>{completion_html(completion)}</td><td>{cell_html(completion.get("handoff_result", ""))}</td></tr>'
        )
        group_number += 1
    if dev.get("reset"):
        rows.append(f'<tr class="quarry-group-row"><td><b>{group_number}</b></td><td colspan="3"><b>{i18n(bi("Reset Mechanic", "Reset Mechanic"))}</b></td></tr>')
        rows.append(
            f'<tr><td><b>A</b></td><td><b>{i18n(bi("Reset / Interruption", "Reset / Interupsi"))}</b></td>'
            f'<td>{cell_html(dev["reset"])}</td><td>{cell_html(dev.get("reset_result", ""))}</td></tr>'
        )
    return rows


def package_pages(data: dict[str, Any]) -> list[str]:
    out, flow_ids = [], {x["id"] for x in data.get("gameplay_flow", [])}
    brand = data["document"].get("brand") or data["document"]["title"]
    for n, pkg in enumerate(data.get("packages", [])):
        pid, code = pkg["id"], 4 + n
        label, title = pkg.get("package_label", f"Package {n+1}"), pkg.get("title", pid)
        clean, phase = (f"flow-{pid}" if pid in flow_ids else "summary"), f"dev-{pid}"

        gp = pkg["gameplay"]
        gp_context = gp.get("context", gp.get("overview", ""))
        gp_body = (
            f'<h2 class="development-package-title">{i18n(title)}</h2>'
            f'<p class="development-package-subtitle">{i18n(join_text(label, bi("Gameplay Overview", "Gameplay Overview"), sep=" · "))}</p>'
            + tabs(pid, "requirement")
            + cards([
                (bi("Gameplay Context", "Konteks Gameplay"), gp_context),
                (bi("Main Objective", "Tujuan Utama"), gp.get("main_objective")),
                (bi("Result", "Hasil"), gp.get("result")),
            ])
        )
        info_rows = _gameplay_info_rows(pkg)
        if info_rows:
            gp_body += heading(bi("Gameplay Information", "Informasi Gameplay")) + production_table([], info_rows, "phase-overview-table quarry-overview-table")
        gp_flow = [entry for entry in gp.get("player_flow", []) if isinstance(entry, dict)]
        if gp_flow:
            gp_body += heading(bi("Gameplay Flow", "Alur Gameplay")) + sequence(gp_flow)
        gp_body += terms(pkg.get("terms", []), f"dev-{pid}-requirement-terms-used-details")
        out.append(
            page(
                f"dev-{pid}-requirement",
                f"{code:02d}A",
                title,
                gp_body,
                context=join_text(title, bi("Gameplay Overview", "Gameplay Overview"), sep=" · "),
                header=bi("Development — Gameplay", "Pengembangan — Gameplay"),
                footer_title=join_text(bi("Development", "Pengembangan"), title, bi("Gameplay Overview", "Gameplay Overview"), sep=" · "),
                brand=brand,
                phase=phase,
                clean=clean,
                role="gameplay-overview",
                classes="sheet professional-only quarry-package-page phase-package-page role-gameplay-overview glossary-enabled-page",
            )
        )

        ld = pkg["level_design"]
        ld_body = (
            f'<h2 class="development-package-title">{i18n(title)}</h2>'
            f'<p class="development-package-subtitle">{i18n(join_text(label, bi("Level Design", "Level Design"), sep=" · "))}</p>'
            + tabs(pid, "level")
            + context_block(bi("Level Design Overview", "Ringkasan Level Design"), ld.get("overview", ""))
        )
        ld_flow = [entry for entry in ld.get("flow", []) if isinstance(entry, dict)]
        if ld_flow:
            ld_body += heading(bi("Design Flow", "Alur Design")) + flow_cards(ld_flow, "quarry-design-flow")
        ld_rows = _level_requirement_rows(ld.get("requirements", []))
        if ld_rows:
            ld_body += heading(bi("Build Requirements", "Kebutuhan Build")) + production_table(
                [bi("No.", "No."), bi("Object", "Objek"), bi("Area Size", "Ukuran Area"), bi("Build and Visual Requirements", "Kebutuhan Build dan Visual"), bi("Gameplay Function", "Fungsi Gameplay")],
                ld_rows,
                "quarry-build-table",
            )
        if ld.get("notes"):
            ld_body += heading(bi("Important Build Notes", "Catatan Build Penting")) + note_grid(ld["notes"])
        ld_body += terms(pkg.get("terms", []), f"dev-{pid}-level-terms-used-details")
        out.append(
            page(
                f"dev-{pid}-level",
                f"{code:02d}B",
                title,
                ld_body,
                context=join_text(title, bi("Level Design", "Level Design"), sep=" · "),
                header=bi("Development — Gameplay", "Pengembangan — Gameplay"),
                footer_title=join_text(bi("Development", "Pengembangan"), title, bi("Level Design", "Level Design"), sep=" · "),
                brand=brand,
                phase=phase,
                clean=clean,
                classes="sheet professional-only quarry-package-page phase-package-page glossary-enabled-page",
            )
        )

        dev = pkg["developer"]
        dev_body = (
            f'<h2 class="development-package-title">{i18n(title)}</h2>'
            f'<p class="development-package-subtitle">{i18n(join_text(label, bi("Developer", "Developer"), sep=" · "))}</p>'
            + tabs(pid, "developer")
            + context_block(bi("Developer Overview", "Ringkasan Developer"), dev.get("overview", ""))
        )
        dev_flow = []
        for entry in dev.get("flow", []):
            if not isinstance(entry, dict):
                continue
            description = entry.get("behavior") or entry.get("details") or entry.get("description") or ""
            extras = []
            if present(entry.get("data")):
                extras.append(join_text(bi("Data", "Data"), entry["data"], sep=": "))
            if present(entry.get("result")):
                extras.append(join_text(bi("Result", "Hasil"), entry["result"], sep=": "))
            if extras:
                description = join_text(description, *extras, sep=" · ")
            dev_flow.append({"step": entry.get("step", len(dev_flow) + 1), "title": entry.get("title") or entry.get("trigger") or entry.get("stage") or "", "description": description})
        if dev_flow:
            dev_body += heading(bi("Development Flow", "Alur Development")) + flow_cards(dev_flow, "quarry-development-flow")
        dev_rows = _developer_requirement_rows(dev)
        if dev_rows:
            dev_body += heading(bi("Development Requirements", "Kebutuhan Development")) + production_table(
                [bi("No.", "No."), bi("Setup", "Setup"), bi("Development Requirements", "Kebutuhan Development"), bi("Gameplay Function", "Fungsi Gameplay")],
                dev_rows,
                "quarry-development-table",
            )
        if dev.get("notes"):
            dev_body += heading(bi("Important Development Notes", "Catatan Development Penting")) + note_grid(dev["notes"])
        dev_body += terms(pkg.get("terms", []), f"dev-{pid}-developer-terms-used-details")
        out.append(
            page(
                f"dev-{pid}-developer",
                f"{code:02d}C",
                title,
                dev_body,
                context=join_text(title, bi("Developer", "Developer"), sep=" · "),
                header=bi("Development — Gameplay", "Pengembangan — Gameplay"),
                footer_title=join_text(bi("Development", "Pengembangan"), title, bi("Developer", "Developer"), sep=" · "),
                brand=brand,
                phase=phase,
                clean=clean,
                classes="sheet professional-only quarry-package-page phase-package-page glossary-enabled-page",
            )
        )
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
        pid, code = pkg["id"], 4 + n
        title, label = pkg.get("title", pid), pkg.get("package_label", f"Package {n+1}")
        sub = "".join(
            f'<a class="phase-page-link professional-nav-item" data-target="dev-{pid}-{key}" href="#dev-{pid}-{key}"><span>{i18n(name)}</span></a>'
            for key, name in [("requirement", "Gameplay Overview"), ("level", "Level Design"), ("developer", "Developer")]
        )
        plinks.append(
            f'<div class="phase-nav-item" data-phase-nav="dev-{pid}"><a class="phase-nav-main" data-section-code="{code:02d}" data-target="dev-{pid}-requirement" href="#dev-{pid}-requirement">'
            f'<span>{i18n(title)}</span><small>{i18n(label)}</small></a><div class="phase-page-list">{sub}</div></div>'
        )
    if glinks or plinks:
        nav.append(
            f'<div class="nav-group is-open professional-nav"><button class="nav-group-toggle" aria-expanded="true"><span class="nav-index">03</span><span class="nav-copy">{i18n(bi("Development", "Pengembangan"))}</span></button>'
            f'<div class="nav-submenu">{glinks}</div><div class="nav-submenu phase-navigation">{"".join(plinks)}</div></div>'
        )
    return "".join(nav)


def glossary(data: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    out = {}
    for pkg in data.get("packages", []):
        items = []
        for n, item in enumerate(pkg.get("terms", [])):
            label = txt(item.get("label") or item.get("term") or item.get("key", ""))
            aliases = item.get("aliases") or {"en": [label["en"]], "id": [label["id"]]}
            if isinstance(aliases, list):
                aliases = {"en": aliases, "id": aliases}
            items.append({"key": str(item.get("key") or f'{pkg["id"]}-{n}'), "label": label, "definition": txt(item.get("definition", "")), "aliases": aliases})
        out[pkg["id"]] = items
    return out
