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
    weight_text,
)


def heading(value: Any) -> str:
    return f'<h3 class="package-section-heading">{i18n(value)}</h3>'


def _visible_package_terms(pkg: dict[str, Any], role: str) -> list[dict[str, Any]]:
    visible: list[dict[str, Any]] = []
    for term in pkg.get("terms", []):
        roles = term.get("roles")
        if roles is None:
            roles = ["gameplay"]
        if role in roles:
            visible.append(term)
    return visible


def _document_control(document: dict[str, Any], overview_data: dict[str, Any]) -> str:
    items = [
        (bi("Version", "Versi"), str(document.get("version", "1.0"))),
        (bi("Scope", "Cakupan"), overview_data.get("document_scope")),
        (bi("Intended Use", "Tujuan Penggunaan"), overview_data.get("intended_use")),
    ]
    cells = "".join(
        f'<article><b>{i18n(label)}</b><p>{i18n(value)}</p></article>'
        for label, value in items
        if present(value)
    )
    return (
        '<div class="document-control-block">'
        f'<span class="document-control-title">{i18n(bi("Document Control", "Kontrol Dokumen"))}</span>'
        f'<div class="document-control-strip">{cells}</div></div>'
    )


def _main_systems(items: list[dict[str, Any]]) -> str:
    visible = [
        item
        for item in items
        if isinstance(item, dict) and (present(item.get("title")) or present(item.get("description")))
    ]
    if not visible:
        return ""
    body = "".join(
        f'<article><b>{i18n(item.get("title", ""))}</b>'
        f'<p>{i18n(item.get("description", ""))}</p></article>'
        for item in visible
    )
    return f'<h3>{i18n(bi("Main Systems", "Sistem Utama"))}</h3><div class="main-system-grid">{body}</div>'


def overview(data: dict[str, Any]) -> str:
    document, overview_data = data["document"], data["overview"]
    brand = document.get("brand") or document["title"]
    facts = "".join(
        f'<div class="fact"><b>{i18n(item.get("label", ""))}</b>'
        f'<span>{i18n(item.get("value", ""))}</span></div>'
        for item in overview_data.get("facts", [])
    )
    journey_items = overview_data.get("journey") or [
        {"title": item.get("title", item["id"]), "description": item.get("player_result", "")}
        for item in data.get("gameplay_flow", [])
    ]
    journey = "".join(
        f'<article><small>{index:02d}</small><strong>{i18n(item.get("title", ""))}</strong>'
        f'<p>{i18n(item.get("description", ""))}</p></article>'
        for index, item in enumerate(journey_items, 1)
    )

    body = (
        '<div class="cover-rule"></div>'
        f'<p class="eyebrow">{i18n(document.get("document_type", bi("Production Specification", "Spesifikasi Produksi")))}</p>'
        f'<h1>{i18n(document["title"])}</h1>'
        f'<p class="subtitle">{i18n(document.get("subtitle", bi("Gameplay & Development Specification", "Spesifikasi Gameplay & Pengembangan")))}</p>'
        f'<p class="lead">{i18n(overview_data.get("project_context", ""))}</p>'
    )
    if overview_data.get("main_experience"):
        body += f'<h3>{i18n(bi("Main Experience", "Pengalaman Utama"))}</h3><p>{i18n(overview_data["main_experience"])}</p>'
    body += _document_control(document, overview_data)
    if facts:
        body += f'<div class="facts{" three" if len(overview_data.get("facts", [])) == 3 else ""}">{facts}</div>'
    if journey:
        columns = min(len(journey_items), 6)
        body += (
            f'<h3>{i18n(bi("Complete Gameplay Journey", "Perjalanan Gameplay Lengkap"))}</h3>'
            f'<div class="journey" style="--prd-journey-columns:{columns}">{journey}</div>'
        )
    body += _main_systems(overview_data.get("main_systems", []))
    body += terms(overview_data.get("terms", []), "summary-terms-used-details")

    context = bi(
        f'Production Development Document · v{document.get("version", "1.0")}',
        f'Dokumen Pengembangan Produksi · v{document.get("version", "1.0")}',
    )
    return page(
        "summary",
        "01",
        bi("Overview", "Gambaran Umum"),
        body,
        context=context,
        classes="sheet glossary-enabled-page",
        brand=brand,
        footer_title=bi("Overview", "Gambaran Umum"),
    )


def _narrative_beats(item: dict[str, Any]) -> list[dict[str, Any]]:
    explicit = item.get("beats")
    if isinstance(explicit, list) and explicit:
        return [beat for beat in explicit if isinstance(beat, dict)]
    beats: list[dict[str, Any]] = []
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


def _flow_orientation(item: dict[str, Any], pkg: dict[str, Any], previous_title: Any) -> str:
    gameplay = pkg["gameplay"]
    fields = [
        (bi("Player Goal", "Tujuan Player"), gameplay.get("main_objective")),
        (bi("Arrives From", "Datang Dari"), previous_title),
        (bi("Continues To", "Berlanjut Ke"), item.get("next_destination")),
    ]
    body = "".join(
        f'<article><b>{i18n(label)}</b><p>{i18n(value)}</p></article>'
        for label, value in fields
        if present(value)
    )
    return f'<div class="flow-orientation">{body}</div>' if body else ""


def flow_pages(data: dict[str, Any]) -> list[str]:
    pages: list[str] = []
    brand = data["document"].get("brand") or data["document"]["title"]
    flow_items = data.get("gameplay_flow", [])
    packages = {pkg["id"]: pkg for pkg in data.get("packages", [])}

    for index, item in enumerate(flow_items):
        page_id = f'flow-{item["id"]}'
        pkg = packages.get(item["id"])
        beats = _narrative_beats(item)
        beat_html = "".join(
            f'<div class="narrative-beat"><div class="narrative-index">{beat_index:02d}</div>'
            f'<div class="narrative-copy"><strong>{i18n(beat.get("title", ""))}</strong>'
            f'<p>{i18n(beat.get("description", beat.get("details", "")))}</p></div></div>'
            for beat_index, beat in enumerate(beats, 1)
        )

        body = f'<h2>{i18n(item.get("title", ""))}</h2>'
        if pkg is not None:
            previous_title = flow_items[index - 1].get("title", "") if index > 0 else ""
            body += _flow_orientation(item, pkg, previous_title)
        if item.get("narrative_context"):
            body += f'<p class="section-intro">{i18n(item["narrative_context"])}</p>'
        body += f'<div class="narrative-sequence">{beat_html}</div>'
        if item.get("next_destination"):
            body += (
                '<div class="story-transition">'
                f'<b>{i18n(bi("Transition", "Transisi"))}</b>'
                f'<p>{i18n(join_text(bi("Next:", "Berikutnya:"), item["next_destination"]))}</p></div>'
            )

        if pkg is not None:
            visible_terms = _visible_package_terms(pkg, "gameplay")
            glossary_scope = pkg["id"]
            package_id = pkg["id"]
        else:
            visible_terms = item.get("terms", [])
            glossary_scope = item["id"] if visible_terms else ""
            package_id = ""
        body += terms(visible_terms, f"{page_id}-terms-used-details")

        pages.append(
            page(
                page_id,
                f'02{chr(65 + index)}',
                item.get("title", ""),
                body,
                context=item.get("title", ""),
                header=bi("02 — Gameplay Flow", "02 — Alur Gameplay"),
                footer_title=join_text(bi("Gameplay Flow", "Alur Gameplay"), item.get("title", ""), sep=" · "),
                brand=brand,
                package_id=package_id,
                glossary_scope=glossary_scope,
                role="gameplay-flow",
                classes="sheet gameplay-flow-page narrative-page glossary-enabled-page",
            )
        )
    return pages


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
            rows.append(
                f'<tr class="requirement-group-row"><td><b>{group_index}</b></td>'
                f'<td colspan="3"><b>{i18n(group_title)}</b></td></tr>'
            )
        for item_index, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            code = item.get("code") or chr(65 + item_index)
            title = item.get("title") or item.get("requirement") or item.get("object") or ""
            details = item.get("details", item.get("requirements", ""))
            result = item.get("result", item.get("expected_result", item.get("gameplay_function", "")))
            rows.append(
                f'<tr><td><b>{i18n(code)}</b></td><td><b>{i18n(title)}</b></td>'
                f'<td>{cell_html(details)}</td><td>{cell_html(result)}</td></tr>'
            )
    return rows


def global_pages(data: dict[str, Any]) -> list[str]:
    pages: list[str] = []
    items = data.get("global_development", [])
    brand = data["document"].get("brand") or data["document"]["title"]

    for index, item in enumerate(items):
        page_id = f'global-{item["id"]}'
        body = (
            f'<h2 class="package-title">{i18n(item.get("title", ""))}</h2>'
            f'<p class="package-subtitle">{i18n(item.get("subtitle") or bi("Project-wide development", "Pengembangan tingkat project"))}</p>'
            + _global_tabs(items, item["id"])
            + context_block(join_text(item.get("title", ""), bi("Overview", "Gambaran Umum")), item.get("overview", ""))
        )
        flow = [entry for entry in item.get("flow", []) if isinstance(entry, dict)]
        if flow:
            body += heading(bi("Development Flow", "Alur Pengembangan")) + flow_cards(flow, "development-flow-grid")
        requirement_rows = _requirement_rows(item.get("requirements", []))
        if requirement_rows:
            body += heading(bi("Development Requirements", "Kebutuhan Pengembangan")) + production_table(
                [
                    bi("No.", "No."),
                    bi("Setup", "Setup"),
                    bi("Development Requirements", "Kebutuhan Pengembangan"),
                    bi("Expected System Result", "Hasil Sistem yang Diharapkan"),
                ],
                requirement_rows,
                "development-requirements-table",
            )
        if item.get("notes"):
            body += heading(bi("Critical Constraints & Notes", "Batasan & Catatan Kritis")) + note_grid(item["notes"])
        body += terms(item.get("terms", []), f"{page_id}-terms-used-details")

        pages.append(
            page(
                page_id,
                f'03{chr(65 + index)}',
                item.get("title", ""),
                body,
                context=item.get("title", ""),
                header=bi("03 — Development", "03 — Pengembangan"),
                footer_title=join_text(bi("Development", "Pengembangan"), item.get("title", ""), sep=" · "),
                brand=brand,
                journey_target="summary",
                role="global-development",
                classes="sheet production-only global-development-page glossary-enabled-page",
            )
        )
    return pages


def _gameplay_info_rows(pkg: dict[str, Any]) -> list[str]:
    gameplay = pkg["gameplay"]
    developer = pkg["developer"]
    scoring_model = gameplay.get("scoring_criteria") or gameplay.get("scoring_summary")

    if not present(scoring_model) and developer.get("scoring"):
        score = developer["scoring"]
        components = [item for item in score.get("components", []) if isinstance(item, dict)]
        explicit_summary = score.get("formula") or score.get("summary")
        if present(explicit_summary):
            scoring_model = explicit_summary
        elif components:
            score_name = txt(score.get("score_name", bi("Score", "Score")))
            raw_weights = [item.get("weight") for item in components]
            if all(weight not in (None, "") for weight in raw_weights):
                en_formula = " + ".join(
                    f'{weight_text(item.get("weight"))} {txt(item.get("name", ""))["en"]}' for item in components
                )
                id_formula = " + ".join(
                    f'{weight_text(item.get("weight"))} {txt(item.get("name", ""))["id"]}' for item in components
                )
                scoring_model = {
                    "en": f'{score_name["en"]}: {en_formula}',
                    "id": f'{score_name["id"]}: {id_formula}',
                }
            else:
                scoring_model = {
                    "en": f'{score_name["en"]} uses ' + ", ".join(txt(item.get("name", ""))["en"] for item in components),
                    "id": f'{score_name["id"]} menggunakan ' + ", ".join(txt(item.get("name", ""))["id"] for item in components),
                }
    elif not present(scoring_model) and developer.get("completion_data"):
        completion = developer["completion_data"]
        scoring_model = completion.get("summary") or completion.get("valid_completion_condition")

    pairs = [
        (bi("Game Purpose", "Tujuan Gameplay"), gameplay.get("purpose") or gameplay.get("game_purpose")),
        (bi("Gameplay Time", "Waktu Gameplay"), gameplay.get("gameplay_time") or gameplay.get("estimated_time") or gameplay.get("duration")),
        (bi("Starting Condition", "Kondisi Awal"), gameplay.get("start_condition")),
        (bi("End Condition", "Kondisi Selesai"), gameplay.get("end_condition")),
        (bi("Failure / Retry / Recovery", "Gagal / Ulang / Pemulihan"), gameplay.get("blocked_or_fail_condition")),
        (bi("Result / Scoring Model", "Model Hasil / Scoring"), scoring_model),
    ]
    return [
        f'<tr><td><b>{i18n(label)}</b></td><td>{cell_html(value)}</td></tr>'
        for label, value in pairs
        if present(value)
    ]


def _level_requirement_rows(groups: list[dict[str, Any]]) -> list[str]:
    rows: list[str] = []
    number = 1
    multiple_groups = len(groups) > 1

    for group_index, group in enumerate(groups, 1):
        items = group.get("items") or group.get("objects") or []
        group_title = group.get("title") or group.get("group_title") or ""
        if multiple_groups and present(group_title):
            rows.append(
                f'<tr class="requirement-group-row"><td><b>{group_index}</b></td>'
                f'<td colspan="4"><b>{i18n(group_title)}</b></td></tr>'
            )
        for item in items:
            if not isinstance(item, dict):
                continue
            code = item.get("no") or item.get("number") or number
            number += 1
            title = item.get("object") or item.get("title") or ""
            subtitle = item.get("subtitle") or (group_title if not multiple_groups else "")
            object_cell = f'<b>{i18n(title)}</b>' + (
                f'<small>{i18n(subtitle)}</small>' if present(subtitle) else ""
            )
            area = item.get("area_size") or item.get("size") or item.get("dimensions") or "—"
            build = item.get("build_and_visual") or item.get("requirements") or item.get("details") or ""
            function = item.get("gameplay_function") or item.get("result") or ""
            rows.append(
                f'<tr><td><b>{i18n(code)}</b></td><td>{object_cell}</td><td>{cell_html(area)}</td>'
                f'<td>{cell_html(build)}</td><td>{cell_html(function)}</td></tr>'
            )
            for child_index, child in enumerate(item.get("children", [])):
                if not isinstance(child, dict):
                    continue
                child_code = child.get("code") or chr(65 + child_index)
                child_title = child.get("object") or child.get("title") or ""
                child_area = child.get("area_size") or child.get("size") or "—"
                child_build = child.get("build_and_visual") or child.get("requirements") or child.get("details") or ""
                child_function = child.get("gameplay_function") or child.get("result") or ""
                rows.append(
                    f'<tr class="requirement-child-row"><td><b>{i18n(child_code)}</b></td>'
                    f'<td><b>{i18n(child_title)}</b></td><td>{cell_html(child_area)}</td>'
                    f'<td>{cell_html(child_build)}</td><td>{cell_html(child_function)}</td></tr>'
                )
    return rows


def _developer_requirement_rows(developer: dict[str, Any]) -> list[str]:
    rows: list[str] = []
    group_number = 1

    for group in developer.get("requirements", []):
        if not isinstance(group, dict):
            continue
        title = group.get("title") or group.get("group_title") or ""
        items = group.get("items") or group.get("objects") or []
        if present(title):
            rows.append(
                f'<tr class="requirement-group-row"><td><b>{group_number}</b></td>'
                f'<td colspan="3"><b>{i18n(title)}</b></td></tr>'
            )
        for item_index, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            code = item.get("code") or chr(65 + item_index)
            name = item.get("title") or item.get("requirement") or ""
            details = item.get("details") or item.get("requirements") or ""
            result = item.get("result") or item.get("expected_result") or item.get("gameplay_function") or ""
            rows.append(
                f'<tr><td><b>{i18n(code)}</b></td><td><b>{i18n(name)}</b></td>'
                f'<td>{cell_html(details)}</td><td>{cell_html(result)}</td></tr>'
            )
        group_number += 1

    if developer.get("scoring"):
        scoring = developer["scoring"]
        rows.append(
            f'<tr class="requirement-group-row"><td><b>{group_number}</b></td>'
            f'<td colspan="3"><b>{i18n(bi("Scoring / Result", "Scoring / Hasil"))}</b></td></tr>'
        )
        rows.append(
            f'<tr><td><b>A</b></td><td><b>{i18n(scoring.get("score_name", bi("Scoring", "Scoring")))}</b></td>'
            f'<td>{score_html(scoring)}</td><td>{cell_html(scoring.get("final_result_relationship", ""))}</td></tr>'
        )
        group_number += 1
    elif developer.get("completion_data"):
        completion = developer["completion_data"]
        rows.append(
            f'<tr class="requirement-group-row"><td><b>{group_number}</b></td>'
            f'<td colspan="3"><b>{i18n(bi("Completion / Result", "Penyelesaian / Hasil"))}</b></td></tr>'
        )
        rows.append(
            f'<tr><td><b>A</b></td><td><b>{i18n(completion.get("completion_name", bi("Completion State", "Kondisi Selesai")))}</b></td>'
            f'<td>{completion_html(completion)}</td><td>{cell_html(completion.get("handoff_result", ""))}</td></tr>'
        )
        group_number += 1

    if developer.get("reset"):
        rows.append(
            f'<tr class="requirement-group-row"><td><b>{group_number}</b></td>'
            f'<td colspan="3"><b>{i18n(bi("Reset / Interruption", "Reset / Interupsi"))}</b></td></tr>'
        )
        rows.append(
            f'<tr><td><b>A</b></td><td><b>{i18n(bi("Reset and Recovery", "Reset dan Pemulihan"))}</b></td>'
            f'<td>{cell_html(developer["reset"])}</td><td>{cell_html(developer.get("reset_result", ""))}</td></tr>'
        )
    return rows


def _developer_flow(items: list[dict[str, Any]]) -> str:
    body: list[str] = []
    for index, entry in enumerate(items, 1):
        if not isinstance(entry, dict):
            continue
        step = entry.get("step", index)
        trigger = entry.get("trigger")
        title = entry.get("title") or entry.get("stage") or trigger or bi("Development Step", "Tahap Pengembangan")
        behavior = entry.get("behavior") or entry.get("details") or entry.get("description") or ""
        fields = []
        for label, value in [
            (bi("Trigger", "Pemicu"), trigger),
            (bi("System Behavior", "Perilaku Sistem"), behavior),
            (bi("Data", "Data"), entry.get("data")),
            (bi("Expected Result", "Hasil yang Diharapkan"), entry.get("result")),
        ]:
            if present(value):
                fields.append(f'<div><dt>{i18n(label)}</dt><dd>{i18n(value)}</dd></div>')
        body.append(
            '<article class="developer-flow-step">'
            f'<header><span>{i18n(str(step).zfill(2))}</span><strong>{i18n(title)}</strong></header>'
            f'<dl>{"".join(fields)}</dl></article>'
        )
    return f'<div class="developer-flow">{"".join(body)}</div>' if body else ""


def _acceptance_block(items: list[Any]) -> str:
    return (
        '<div class="acceptance">'
        f'<h3>{i18n(bi("Acceptance & Verification", "Penerimaan & Verifikasi"))}</h3>'
        f'<ul class="acceptance-list">{"".join(f"<li>{i18n(item)}</li>" for item in items)}</ul>'
        '</div>'
    )


def package_pages(data: dict[str, Any]) -> list[str]:
    pages: list[str] = []
    flow_ids = {item["id"] for item in data.get("gameplay_flow", [])}
    brand = data["document"].get("brand") or data["document"]["title"]

    for index, pkg in enumerate(data.get("packages", [])):
        package_id, code = pkg["id"], 4 + index
        package_label = pkg.get("package_label", f"Package {index + 1}")
        title = pkg.get("title", package_id)
        journey_target = f"flow-{package_id}" if package_id in flow_ids else "summary"

        gameplay = pkg["gameplay"]
        gameplay_context = gameplay.get("context", gameplay.get("overview", ""))
        gameplay_body = (
            f'<h2 class="package-title">{i18n(title)}</h2>'
            f'<p class="package-subtitle">{i18n(join_text(package_label, bi("Gameplay Overview", "Gambaran Gameplay"), sep=" · "))}</p>'
            + tabs(package_id, "requirement")
            + cards([
                (bi("Gameplay Context", "Konteks Gameplay"), gameplay_context),
                (bi("Main Objective", "Tujuan Utama"), gameplay.get("main_objective")),
                (bi("Result", "Hasil"), gameplay.get("result")),
            ])
        )
        info_rows = _gameplay_info_rows(pkg)
        if info_rows:
            gameplay_body += heading(bi("Gameplay Information", "Informasi Gameplay")) + production_table(
                [], info_rows, "gameplay-info-table"
            )
        player_flow = [entry for entry in gameplay.get("player_flow", []) if isinstance(entry, dict)]
        if player_flow:
            gameplay_body += heading(bi("Objective Sequence", "Urutan Objective")) + sequence(player_flow)
        gameplay_body += terms(
            _visible_package_terms(pkg, "gameplay"),
            f"dev-{package_id}-requirement-terms-used-details",
        )
        pages.append(
            page(
                f"dev-{package_id}-requirement",
                f"{code:02d}A",
                title,
                gameplay_body,
                context=join_text(title, bi("Gameplay Overview", "Gambaran Gameplay"), sep=" · "),
                header=bi("Development — Gameplay", "Pengembangan — Gameplay"),
                footer_title=join_text(bi("Development", "Pengembangan"), title, bi("Gameplay Overview", "Gambaran Gameplay"), sep=" · "),
                brand=brand,
                package_id=package_id,
                glossary_scope=package_id,
                journey_target=journey_target,
                role="gameplay-overview",
                classes="sheet production-only package-page role-gameplay-overview glossary-enabled-page",
            )
        )

        level = pkg["level_design"]
        level_body = (
            f'<h2 class="package-title">{i18n(title)}</h2>'
            f'<p class="package-subtitle">{i18n(join_text(package_label, bi("Level Design", "Level Design"), sep=" · "))}</p>'
            + tabs(package_id, "level")
            + context_block(bi("Level Design Overview", "Ringkasan Level Design"), level.get("overview", ""))
        )
        level_flow = [entry for entry in level.get("flow", []) if isinstance(entry, dict)]
        if level_flow:
            level_body += heading(bi("Design Flow", "Alur Desain")) + flow_cards(level_flow, "design-flow-grid")
        level_rows = _level_requirement_rows(level.get("requirements", []))
        if level_rows:
            level_body += heading(bi("Build Requirements", "Kebutuhan Build")) + production_table(
                [
                    bi("No.", "No."),
                    bi("Object", "Objek"),
                    bi("Area / Spatial Constraint", "Area / Batasan Spasial"),
                    bi("Build and Visual Requirements", "Kebutuhan Build dan Visual"),
                    bi("Gameplay Function", "Fungsi Gameplay"),
                ],
                level_rows,
                "build-requirements-table",
            )
        if level.get("notes"):
            level_body += heading(bi("Critical Constraints & Notes", "Batasan & Catatan Kritis")) + note_grid(level["notes"])
        level_body += terms(
            _visible_package_terms(pkg, "level_design"),
            f"dev-{package_id}-level-terms-used-details",
        )
        pages.append(
            page(
                f"dev-{package_id}-level",
                f"{code:02d}B",
                title,
                level_body,
                context=join_text(title, bi("Level Design", "Level Design"), sep=" · "),
                header=bi("Development — Gameplay", "Pengembangan — Gameplay"),
                footer_title=join_text(bi("Development", "Pengembangan"), title, bi("Level Design", "Level Design"), sep=" · "),
                brand=brand,
                package_id=package_id,
                glossary_scope=package_id,
                journey_target=journey_target,
                role="level-design",
                classes="sheet production-only package-page glossary-enabled-page",
            )
        )

        developer = pkg["developer"]
        developer_body = (
            f'<h2 class="package-title">{i18n(title)}</h2>'
            f'<p class="package-subtitle">{i18n(join_text(package_label, bi("Developer", "Developer"), sep=" · "))}</p>'
            + tabs(package_id, "developer")
            + context_block(bi("Developer Overview", "Ringkasan Developer"), developer.get("overview", ""))
        )
        developer_flow = [entry for entry in developer.get("flow", []) if isinstance(entry, dict)]
        if developer_flow:
            developer_body += heading(bi("Development Flow", "Alur Pengembangan")) + _developer_flow(developer_flow)
        developer_rows = _developer_requirement_rows(developer)
        if developer_rows:
            developer_body += heading(bi("Development Requirements", "Kebutuhan Pengembangan")) + production_table(
                [
                    bi("No.", "No."),
                    bi("Setup", "Setup"),
                    bi("Development Requirements", "Kebutuhan Pengembangan"),
                    bi("Expected System Result", "Hasil Sistem yang Diharapkan"),
                ],
                developer_rows,
                "development-requirements-table",
            )
        if developer.get("notes"):
            developer_body += heading(bi("Critical Constraints & Notes", "Batasan & Catatan Kritis")) + note_grid(developer["notes"])
        developer_body += _acceptance_block(pkg.get("acceptance", []))
        developer_body += terms(
            _visible_package_terms(pkg, "developer"),
            f"dev-{package_id}-developer-terms-used-details",
        )
        pages.append(
            page(
                f"dev-{package_id}-developer",
                f"{code:02d}C",
                title,
                developer_body,
                context=join_text(title, bi("Developer", "Developer"), sep=" · "),
                header=bi("Development — Gameplay", "Pengembangan — Gameplay"),
                footer_title=join_text(bi("Development", "Pengembangan"), title, bi("Developer", "Developer"), sep=" · "),
                brand=brand,
                package_id=package_id,
                glossary_scope=package_id,
                journey_target=journey_target,
                role="developer",
                classes="sheet production-only package-page glossary-enabled-page",
            )
        )
    return pages


def navigation(data: dict[str, Any]) -> str:
    navigation_items = [
        f'<a class="nav-link" data-target="summary" href="#summary">'
        f'<span class="nav-index">01</span><span class="nav-copy">{i18n(bi("Overview", "Gambaran Umum"))}</span></a>'
    ]

    flow = data.get("gameplay_flow", [])
    if flow:
        links = "".join(
            f'<a data-target="flow-{esc(item["id"])}" href="#flow-{esc(item["id"])}">'
            f'{i18n(item.get("title", item["id"]))}</a>'
            for item in flow
        )
        navigation_items.append(
            '<div class="nav-group is-open"><button class="nav-group-toggle" aria-expanded="true">'
            f'<span class="nav-index">02</span><span class="nav-copy">{i18n(bi("Gameplay Flow", "Alur Gameplay"))}</span>'
            f'<span aria-hidden="true" class="group-chevron"></span></button><div class="nav-submenu">{links}</div></div>'
        )

    global_links = "".join(
        f'<a data-target="global-{esc(item["id"])}" href="#global-{esc(item["id"])}">'
        f'{i18n(item.get("title", item["id"]))}</a>'
        for item in data.get("global_development", [])
    )
    package_links = []
    for index, pkg in enumerate(data.get("packages", [])):
        package_id, code = pkg["id"], 4 + index
        title = pkg.get("title", package_id)
        label = pkg.get("package_label", f"Package {index + 1}")
        subpages = "".join(
            f'<a class="package-page-link production-nav-item" data-target="dev-{package_id}-{key}" '
            f'href="#dev-{package_id}-{key}"><span>{i18n(name)}</span></a>'
            for key, name in [
                ("requirement", bi("Gameplay Overview", "Gambaran Gameplay")),
                ("level", bi("Level Design", "Level Design")),
                ("developer", bi("Developer", "Developer")),
            ]
        )
        package_links.append(
            f'<div class="package-nav-item" data-package-nav="{esc(package_id)}">'
            f'<a class="package-nav-main" data-section-code="{code:02d}" '
            f'data-target="dev-{package_id}-requirement" href="#dev-{package_id}-requirement">'
            f'<span>{i18n(title)}</span><small>{i18n(label)}</small></a>'
            f'<div class="package-page-list">{subpages}</div></div>'
        )

    if global_links or package_links:
        navigation_items.append(
            '<div class="nav-group is-open production-nav"><button class="nav-group-toggle" aria-expanded="true">'
            f'<span class="nav-index">03</span><span class="nav-copy">{i18n(bi("Development", "Pengembangan"))}</span>'
            f'<span aria-hidden="true" class="group-chevron"></span></button>'
            f'<div class="nav-submenu">{global_links}</div>'
            f'<div class="nav-submenu package-navigation">{"".join(package_links)}</div></div>'
        )
    return "".join(navigation_items)


def _glossary_items(items: list[dict[str, Any]], scope: str) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for index, item in enumerate(items):
        label = txt(item.get("label") or item.get("term") or item.get("key", ""))
        aliases = item.get("aliases") or {"en": [label["en"]], "id": [label["id"]]}
        if isinstance(aliases, list):
            aliases = {"en": aliases, "id": aliases}
        output.append(
            {
                "key": str(item.get("key") or f"{scope}-{index}"),
                "label": label,
                "definition": txt(item.get("definition", "")),
                "aliases": aliases,
            }
        )
    return output


def glossary(data: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    output: dict[str, list[dict[str, Any]]] = {}
    for pkg in data.get("packages", []):
        output[pkg["id"]] = _glossary_items(pkg.get("terms", []), pkg["id"])

    flow = data.get("gameplay_flow", [])
    if flow:
        opening = flow[0]
        opening_terms = opening.get("terms", [])
        if opening_terms:
            output[opening["id"]] = _glossary_items(opening_terms, opening["id"])
    return output
