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


GOLDEN_GLOBAL_TITLES = {
    "development-overview": bi("Development Overview", "Development Overview"),
    "game-system": bi("Game System", "Game System"),
    "data-reset": bi("Data and Reset", "Data dan Reset"),
    "gameplay-development": bi("Gameplay Development", "Gameplay Development"),
}


def heading(value: Any) -> str:
    return f'<h3 class="package-section-heading">{i18n(value)}</h3>'


def _require_count(items: list[Any], expected: int, context: str) -> None:
    if len(items) != expected:
        raise ValueError(f"{context} must contain exactly {expected} items to match the Golden page prototype")


def _visible_package_terms(pkg: dict[str, Any], role: str) -> list[dict[str, Any]]:
    visible: list[dict[str, Any]] = []
    for term in pkg.get("terms", []):
        roles = term.get("roles")
        if roles is None or role in roles:
            visible.append(term)
    return visible


def _glossary_scope(package_id: str, role: str) -> str:
    return f"{package_id}-{role.replace('_', '-')}"


def _summary_note(items: Any) -> str:
    if not isinstance(items, list) or not items:
        return ""
    values: list[Any] = []
    for item in items:
        if isinstance(item, dict):
            title = item.get("title")
            description = item.get("description")
            if present(title) and present(description):
                values.append(join_text(title, description, sep=" — "))
            elif present(description):
                values.append(description)
        elif present(item):
            values.append(item)
    if not values:
        return ""
    body = "".join(f"<li>{i18n(value)}</li>" for value in values)
    return (
        '<div class="summary-note">'
        f'<strong>{i18n(bi("Global Gameplay Direction", "Arah Gameplay Global"))}</strong>'
        f'<ul class="clean-list">{body}</ul></div>'
    )


def overview(data: dict[str, Any]) -> str:
    document = data["document"]
    overview_data = data["overview"]
    brand = document.get("brand") or document["title"]

    facts = overview_data.get("facts", [])
    _require_count(facts, 3, "overview.facts")
    facts_html = "".join(
        f'<div class="fact"><b>{i18n(item.get("label", ""))}</b>'
        f'<span>{i18n(item.get("value", ""))}</span></div>'
        for item in facts
    )

    journey_items = overview_data.get("journey", [])
    journey_html = "".join(
        f'<article><small>{index:02d}</small><strong>{i18n(item.get("title", ""))}</strong>'
        f'<p>{i18n(item.get("description", ""))}</p></article>'
        for index, item in enumerate(journey_items, 1)
    )

    body = (
        '<div class="cover-rule"></div>'
        f'<p class="eyebrow">{i18n(document.get("map_type") or document.get("document_type") or bi("Adventure Map", "Adventure Map"))}</p>'
        f'<h1>{i18n(document["title"])}</h1>'
        f'<p class="subtitle">{i18n(document.get("subtitle") or bi("Gameplay & Development Specification", "Spesifikasi Gameplay & Pengembangan"))}</p>'
        f'<p class="lead">{i18n(overview_data.get("project_context", ""))}</p>'
        f'<div class="facts three">{facts_html}</div>'
        f'<h3>{i18n(bi("Complete Gameplay Journey", "Perjalanan Gameplay Lengkap"))}</h3>'
        f'<div class="journey" style="--prd-journey-columns:{min(len(journey_items), 6)}">{journey_html}</div>'
    )
    direction = overview_data.get("global_gameplay_direction") or overview_data.get("main_systems", [])
    body += _summary_note(direction)

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
        classes="sheet",
        brand=brand,
        footer_title=bi("Overview", "Gambaran Umum"),
    )


def _story_flow(item: dict[str, Any]) -> str:
    beats = [beat for beat in item.get("beats", []) if isinstance(beat, dict)]
    body: list[str] = ['<div class="story-flow">']
    for beat in beats:
        body.append(f'<h3>{i18n(beat.get("title", ""))}</h3>')
        description = beat.get("description") or beat.get("details") or ""
        if isinstance(description, list):
            for paragraph in description:
                body.append(f'<p>{i18n(paragraph)}</p>')
        elif present(description):
            body.append(f'<p>{i18n(description)}</p>')
    if item.get("next_destination"):
        body.append(
            '<div class="story-transition">'
            f'<b>{i18n(bi("Transition", "Transisi"))}</b>'
            f'<p>{i18n(join_text(bi("Next:", "Berikutnya:"), item["next_destination"]))}</p></div>'
        )
    body.append('</div>')
    return "".join(body)


def flow_pages(data: dict[str, Any]) -> list[str]:
    pages: list[str] = []
    brand = data["document"].get("brand") or data["document"]["title"]
    flow_items = data.get("gameplay_flow", [])
    packages = {pkg["id"]: pkg for pkg in data.get("packages", [])}

    for index, item in enumerate(flow_items):
        page_id = f'flow-{item["id"]}'
        pkg = packages.get(item["id"])
        body = f'<h2>{i18n(item.get("display_title") or item.get("title", ""))}</h2>'
        if item.get("eyebrow"):
            body += f'<p class="eyebrow">{i18n(item["eyebrow"])}</p>'
        if item.get("narrative_context"):
            body += f'<p class="section-intro">{i18n(item["narrative_context"])}</p>'
        body += _story_flow(item)

        if pkg is not None:
            visible_terms = _visible_package_terms(pkg, "gameplay")
            glossary_scope = _glossary_scope(pkg["id"], "gameplay")
            package_id = pkg["id"]
        else:
            visible_terms = item.get("terms", [])
            glossary_scope = f'{item["id"]}-opening' if visible_terms else ""
            package_id = ""
        body += terms(visible_terms, f"{page_id}-terms-used-details")

        context = item.get("context_label") or item.get("title", "")
        pages.append(
            page(
                page_id,
                f'02{chr(65 + index)}',
                item.get("title", ""),
                body,
                context=context,
                header=bi("02 — Gameplay Flow", "02 — Alur Gameplay"),
                footer_title=join_text(bi("Gameplay Flow", "Alur Gameplay"), item.get("title", ""), sep=" · "),
                brand=brand,
                package_id=package_id,
                glossary_scope=glossary_scope,
                role="gameplay-flow",
                classes="sheet gameplay-flow-page story-page glossary-enabled-page",
            )
        )
    return pages


def _golden_global_title(item: dict[str, Any]) -> Any:
    return GOLDEN_GLOBAL_TITLES.get(item.get("id"), item.get("title", ""))


def _global_tabs(items: list[dict[str, Any]], active_id: str) -> str:
    links = []
    for index, item in enumerate(items, 1):
        target = f'global-{item["id"]}'
        active = item["id"] == active_id
        active_class = " is-active" if active else ""
        current = ' aria-current="page"' if active else ""
        title = _golden_global_title(item)
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
        title = _golden_global_title(item)
        flow = [entry for entry in item.get("flow", []) if isinstance(entry, dict)]
        notes = item.get("notes", [])
        _require_count(flow, 4, f"global_development[{index}].flow")
        _require_count(notes, 4, f"global_development[{index}].notes")

        body = (
            f'<h2 class="package-title">{i18n(title)}</h2>'
            f'<p class="package-subtitle">{i18n(item.get("subtitle") or bi("Project-wide development", "Pengembangan tingkat project"))}</p>'
            + _global_tabs(items, item["id"])
            + context_block(join_text(title, bi("Overview", "Gambaran Umum")), item.get("overview", ""))
            + heading(bi("Development Flow", "Alur Pengembangan"))
            + flow_cards(flow, "development-flow-grid")
        )
        requirement_rows = _requirement_rows(item.get("requirements", []))
        if requirement_rows:
            body += heading(bi("Development Requirements", "Kebutuhan Pengembangan")) + production_table(
                [bi("No.", "No."), bi("Setup", "Setup"), bi("Development Requirements", "Kebutuhan Pengembangan"), bi("System Result", "Hasil Sistem")],
                requirement_rows,
                "development-requirements-table",
            )
        body += heading(bi("Important Development Notes", "Catatan Pengembangan Penting")) + note_grid(notes)
        body += terms(item.get("terms", []), f"{page_id}-terms-used-details")

        pages.append(
            page(
                page_id,
                f'03{chr(65 + index)}',
                title,
                body,
                context=title,
                header=bi("03 — Development", "03 — Development"),
                footer_title=join_text(bi("Development", "Development"), title, sep=" · "),
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
            name = txt(score.get("score_name", bi("Score", "Score")))
            parts_en = [f'{weight_text(item.get("weight"))} {txt(item.get("name", ""))["en"]}'.strip() for item in components]
            parts_id = [f'{weight_text(item.get("weight"))} {txt(item.get("name", ""))["id"]}'.strip() for item in components]
            scoring_model = {"en": f'{name["en"]}: ' + " + ".join(parts_en), "id": f'{name["id"]}: ' + " + ".join(parts_id)}
    elif not present(scoring_model) and developer.get("completion_data"):
        completion = developer["completion_data"]
        scoring_model = completion.get("summary") or completion.get("valid_completion_condition")

    pairs = [
        (bi("Game Purpose", "Tujuan Gameplay"), gameplay.get("purpose") or gameplay.get("game_purpose")),
        (bi("Gameplay Time", "Waktu Gameplay"), gameplay.get("gameplay_time") or gameplay.get("estimated_time") or gameplay.get("duration")),
        (bi("Starting Condition", "Kondisi Awal"), gameplay.get("start_condition")),
        (bi("End Condition", "Kondisi Selesai"), gameplay.get("end_condition")),
        (bi("Fail Condition", "Kondisi Gagal"), gameplay.get("blocked_or_fail_condition")),
        (bi("Scoring Criteria", "Kriteria Scoring"), scoring_model),
    ]
    return [f'<tr><td><b>{i18n(label)}</b></td><td>{cell_html(value)}</td></tr>' for label, value in pairs]


def _level_requirement_rows(groups: list[dict[str, Any]]) -> list[str]:
    rows: list[str] = []
    number = 1
    multiple_groups = len(groups) > 1
    for group_index, group in enumerate(groups, 1):
        items = group.get("items") or group.get("objects") or []
        group_title = group.get("title") or group.get("group_title") or ""
        if multiple_groups and present(group_title):
            rows.append(f'<tr class="requirement-group-row"><td><b>{group_index}</b></td><td colspan="4"><b>{i18n(group_title)}</b></td></tr>')
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
                rows.append(f'<tr class="requirement-child-row"><td><b>{i18n(child_code)}</b></td><td><b>{i18n(child_title)}</b></td><td>{cell_html(child_area)}</td><td>{cell_html(child_build)}</td><td>{cell_html(child_function)}</td></tr>')
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
            rows.append(f'<tr class="requirement-group-row"><td><b>{group_number}</b></td><td colspan="3"><b>{i18n(title)}</b></td></tr>')
        for item_index, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            code = item.get("code") or chr(65 + item_index)
            name = item.get("title") or item.get("requirement") or ""
            details = item.get("details") or item.get("requirements") or ""
            result = item.get("result") or item.get("expected_result") or item.get("gameplay_function") or ""
            rows.append(f'<tr><td><b>{i18n(code)}</b></td><td><b>{i18n(name)}</b></td><td>{cell_html(details)}</td><td>{cell_html(result)}</td></tr>')
        group_number += 1

    if developer.get("scoring"):
        scoring = developer["scoring"]
        rows.append(f'<tr class="requirement-group-row"><td><b>{group_number}</b></td><td colspan="3"><b>{i18n(bi("Scoring Setup", "Setup Scoring"))}</b></td></tr>')
        rows.append(f'<tr><td><b>A</b></td><td><b>{i18n(scoring.get("score_name", bi("Scoring", "Scoring")))}</b></td><td>{score_html(scoring)}</td><td>{cell_html(scoring.get("final_result_relationship", ""))}</td></tr>')
        group_number += 1
    elif developer.get("completion_data"):
        completion = developer["completion_data"]
        rows.append(f'<tr class="requirement-group-row"><td><b>{group_number}</b></td><td colspan="3"><b>{i18n(bi("Completion and Data", "Completion dan Data"))}</b></td></tr>')
        rows.append(f'<tr><td><b>A</b></td><td><b>{i18n(completion.get("completion_name", bi("Completion State", "Kondisi Selesai")))}</b></td><td>{completion_html(completion)}</td><td>{cell_html(completion.get("handoff_result", ""))}</td></tr>')
        group_number += 1

    if developer.get("reset"):
        rows.append(f'<tr class="requirement-group-row"><td><b>{group_number}</b></td><td colspan="3"><b>{i18n(bi("Reset Mechanic", "Reset Mechanic"))}</b></td></tr>')
        rows.append(f'<tr><td><b>A</b></td><td><b>{i18n(bi("Reset / Interruption", "Reset / Interupsi"))}</b></td><td>{cell_html(developer["reset"])}</td><td>{cell_html(developer.get("reset_result", ""))}</td></tr>')
    return rows


def package_pages(data: dict[str, Any]) -> list[str]:
    pages: list[str] = []
    flow_ids = {item["id"] for item in data.get("gameplay_flow", [])}
    brand = data["document"].get("brand") or data["document"]["title"]

    for index, pkg in enumerate(data.get("packages", [])):
        package_id = pkg["id"]
        code = 4 + index
        package_label = pkg.get("package_label", f"Package {index + 1}")
        title = pkg.get("title", package_id)
        journey_target = f"flow-{package_id}" if package_id in flow_ids else "summary"

        gameplay = pkg["gameplay"]
        player_flow = [entry for entry in gameplay.get("player_flow", []) if isinstance(entry, dict)]
        _require_count(player_flow, 5, f"packages[{index}].gameplay.player_flow")
        gameplay_body = (
            f'<h2 class="package-title">{i18n(title)}</h2>'
            f'<p class="package-subtitle">{i18n(join_text(package_label, bi("Gameplay Overview", "Gameplay Overview"), sep=" · "))}</p>'
            + tabs(package_id, "requirement")
            + cards([
                (bi("Gameplay Context", "Konteks Gameplay"), gameplay.get("context", gameplay.get("overview", ""))),
                (bi("Main Objective", "Tujuan Utama"), gameplay.get("main_objective")),
                (bi("Result", "Hasil"), gameplay.get("result")),
            ])
            + heading(bi("Gameplay Information", "Informasi Gameplay"))
            + production_table([], _gameplay_info_rows(pkg), "gameplay-info-table")
            + heading(bi("Gameplay Flow", "Alur Gameplay"))
            + sequence(player_flow)
            + terms(_visible_package_terms(pkg, "gameplay"), f"dev-{package_id}-requirement-terms-used-details")
        )
        pages.append(page(
            f"dev-{package_id}-requirement", f"{code:02d}A", title, gameplay_body,
            context=join_text(title, bi("Gameplay Overview", "Gameplay Overview"), sep=" · "),
            header=bi("Development — Gameplay", "Development — Gameplay"),
            footer_title=join_text(bi("Development", "Development"), title, bi("Gameplay Overview", "Gameplay Overview"), sep=" · "),
            brand=brand, package_id=package_id, glossary_scope=_glossary_scope(package_id, "gameplay"),
            journey_target=journey_target, role="gameplay-overview",
            classes="sheet production-only package-page role-gameplay-overview glossary-enabled-page",
        ))

        level = pkg["level_design"]
        level_flow = [entry for entry in level.get("flow", []) if isinstance(entry, dict)]
        level_notes = level.get("notes", [])
        _require_count(level_flow, 4, f"packages[{index}].level_design.flow")
        _require_count(level_notes, 4, f"packages[{index}].level_design.notes")
        level_body = (
            f'<h2 class="package-title">{i18n(title)}</h2>'
            f'<p class="package-subtitle">{i18n(join_text(package_label, bi("Level Design", "Level Design"), sep=" · "))}</p>'
            + tabs(package_id, "level")
            + context_block(bi("Level Design Overview", "Level Design Overview"), level.get("overview", ""))
            + heading(bi("Design Flow", "Design Flow"))
            + flow_cards(level_flow, "design-flow-grid")
            + heading(bi("Build Requirements", "Build Requirements"))
            + production_table([
                bi("No.", "No."), bi("Object", "Object"), bi("Area Size", "Area Size"),
                bi("Build and Visual Requirements", "Build and Visual Requirements"), bi("Gameplay Function", "Gameplay Function")
            ], _level_requirement_rows(level.get("requirements", [])), "build-requirements-table")
            + heading(bi("Important Build Notes", "Important Build Notes"))
            + note_grid(level_notes)
        )
        pages.append(page(
            f"dev-{package_id}-level", f"{code:02d}B", title, level_body,
            context=join_text(title, bi("Level Design", "Level Design"), sep=" · "),
            header=bi("Development — Gameplay", "Development — Gameplay"),
            footer_title=join_text(bi("Development", "Development"), title, bi("Level Design", "Level Design"), sep=" · "),
            brand=brand, package_id=package_id, glossary_scope=_glossary_scope(package_id, "level_design"),
            journey_target=journey_target, role="level-design",
            classes="sheet production-only package-page glossary-enabled-page",
        ))

        developer = pkg["developer"]
        developer_flow = [entry for entry in developer.get("flow", []) if isinstance(entry, dict)]
        developer_notes = developer.get("notes", [])
        _require_count(developer_flow, 4, f"packages[{index}].developer.flow")
        _require_count(developer_notes, 4, f"packages[{index}].developer.notes")
        developer_body = (
            f'<h2 class="package-title">{i18n(title)}</h2>'
            f'<p class="package-subtitle">{i18n(join_text(package_label, bi("Developer", "Developer"), sep=" · "))}</p>'
            + tabs(package_id, "developer")
            + context_block(bi("Developer Overview", "Developer Overview"), developer.get("overview", ""))
            + heading(bi("Development Flow", "Development Flow"))
            + flow_cards(developer_flow, "development-flow-grid")
            + heading(bi("Development Requirements", "Development Requirements"))
            + production_table([
                bi("No.", "No."), bi("Setup", "Setup"), bi("Development Requirements", "Development Requirements"), bi("Gameplay Function", "Gameplay Function")
            ], _developer_requirement_rows(developer), "development-requirements-table")
            + heading(bi("Important Development Notes", "Important Development Notes"))
            + note_grid(developer_notes)
        )
        pages.append(page(
            f"dev-{package_id}-developer", f"{code:02d}C", title, developer_body,
            context=join_text(title, bi("Developer", "Developer"), sep=" · "),
            header=bi("Development — Gameplay", "Development — Gameplay"),
            footer_title=join_text(bi("Development", "Development"), title, bi("Developer", "Developer"), sep=" · "),
            brand=brand, package_id=package_id, glossary_scope=_glossary_scope(package_id, "developer"),
            journey_target=journey_target, role="developer",
            classes="sheet production-only package-page glossary-enabled-page",
        ))
    return pages


def navigation(data: dict[str, Any]) -> str:
    navigation_items = [
        f'<a class="nav-link" data-target="summary" href="#summary"><span class="nav-index">01</span><span class="nav-copy">{i18n(bi("Overview", "Overview"))}</span></a>'
    ]
    flow = data.get("gameplay_flow", [])
    if flow:
        links = "".join(
            f'<a data-target="flow-{esc(item["id"])}" href="#flow-{esc(item["id"])}">{i18n(item.get("title", item["id"]))}</a>'
            for item in flow
        )
        navigation_items.append(
            '<div class="nav-group is-open"><button class="nav-group-toggle" aria-expanded="true">'
            f'<span class="nav-index">02</span><span class="nav-copy">{i18n(bi("Gameplay Flow", "Gameplay Flow"))}</span>'
            f'<span aria-hidden="true" class="group-chevron"></span></button><div class="nav-submenu">{links}</div></div>'
        )

    global_links = "".join(
        f'<a data-target="global-{esc(item["id"])}" href="#global-{esc(item["id"])}">{i18n(_golden_global_title(item))}</a>'
        for item in data.get("global_development", [])
    )
    package_links = []
    for index, pkg in enumerate(data.get("packages", [])):
        package_id, code = pkg["id"], 4 + index
        title = pkg.get("title", package_id)
        label = pkg.get("package_label", f"Package {index + 1}")
        subpages = "".join(
            f'<a class="package-page-link production-nav-item" data-target="dev-{package_id}-{key}" href="#dev-{package_id}-{key}"><span>{i18n(name)}</span></a>'
            for key, name in [("requirement", bi("Gameplay Overview", "Gameplay Overview")), ("level", bi("Level Design", "Level Design")), ("developer", bi("Developer", "Developer"))]
        )
        package_links.append(
            f'<div class="package-nav-item" data-package-nav="{esc(package_id)}">'
            f'<a class="package-nav-main" data-section-code="{code:02d}" data-target="dev-{package_id}-requirement" href="#dev-{package_id}-requirement">'
            f'<span>{i18n(title)}</span><small>{i18n(label)}</small></a><div class="package-page-list">{subpages}</div></div>'
        )
    if global_links or package_links:
        navigation_items.append(
            '<div class="nav-group is-open production-nav"><button class="nav-group-toggle" aria-expanded="true">'
            f'<span class="nav-index">03</span><span class="nav-copy">{i18n(bi("Development", "Development"))}</span>'
            f'<span aria-hidden="true" class="group-chevron"></span></button>'
            f'<div class="nav-submenu">{global_links}</div>'
            f'<div class="nav-submenu package-navigation'>{"".join(package_links)}</div></div>'
        )
    return "".join(navigation_items)


def _glossary_items(items: list[dict[str, Any]], scope: str) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for index, item in enumerate(items):
        label = txt(item.get("label") or item.get("term") or item.get("key", ""))
        aliases = item.get("aliases") or {"en": [label["en"]], "id": [label["id"]]}
        if isinstance(aliases, list):
            aliases = {"en": aliases, "id": aliases}
        output.append({
            "key": str(item.get("key") or f"{scope}-{index}"),
            "label": label,
            "definition": txt(item.get("definition", "")),
            "aliases": aliases,
        })
    return output


def glossary(data: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    output: dict[str, list[dict[str, Any]]] = {}
    for pkg in data.get("packages", []):
        package_id = pkg["id"]
        for role in ("gameplay", "level_design", "developer"):
            scope = _glossary_scope(package_id, role)
            output[scope] = _glossary_items(_visible_package_terms(pkg, role), scope)
    flow = data.get("gameplay_flow", [])
    if flow:
        opening = flow[0]
        opening_terms = opening.get("terms", [])
        if opening_terms:
            scope = f'{opening["id"]}-opening'
            output[scope] = _glossary_items(opening_terms, scope)
    return output
