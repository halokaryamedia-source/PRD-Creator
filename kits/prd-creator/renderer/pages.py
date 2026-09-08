from __future__ import annotations

from typing import Any, Literal

from shared.render_schema import (
    DeveloperData,
    DevelopmentRequirementGroupData,
    GameplayFlowData,
    GlobalDevelopmentData,
    LevelRequirementGroupData,
    PackageData,
    RenderData,
    TermData,
    TitleDescriptionData,
)

from .core import (
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
)

GOLDEN_GLOBAL_TITLES = {
    "development-overview": bi("Development Overview", "Development Overview"),
    "game-system": bi("Game System", "Game System"),
    "data-reset": bi("Data and Reset", "Data dan Reset"),
    "gameplay-development": bi("Gameplay Development", "Gameplay Development"),
}

GOLDEN_GLOBAL_PAGE_IDS = {
    "development-overview": "development-overview",
    "game-system": "shared-systems",
    "data-reset": "shared-data-reset",
    "gameplay-development": "phase-development",
}

PackageTab = Literal["requirement", "level", "developer"]


def _package_tabs(package_id: str, active: PackageTab) -> str:
    return tabs(package_id, active)


def heading(value: Any) -> str:
    return f'<h3 class="package-section-heading">{i18n(value)}</h3>'


def overview(data: RenderData) -> str:
    document = data["document"]
    overview_data = data["overview"]
    brand = document.get("brand") or document["title"]

    facts = overview_data["facts"]
    facts_html = "".join(
        f'<div class="fact"><b>{i18n(item["label"])}</b><span>{i18n(item["value"])}</span></div>' for item in facts
    )
    journey_items = overview_data["journey"]
    journey_html = "".join(
        f"<article><small>{index:02d}</small><strong>{i18n(item['title'])}</strong>"
        f"<p>{i18n(item['description'])}</p></article>"
        for index, item in enumerate(journey_items, 1)
    )
    journey_columns = max(1, min(len(journey_items), 6))
    journey_style = "" if len(journey_items) == 6 else f' style="grid-template-columns:repeat({journey_columns},1fr)"'

    body = (
        '<div class="cover-rule"></div>'
        f'<p class="eyebrow">{i18n(document["document_type"])}</p>'
        f"<h1>{i18n(document['title'])}</h1>"
        f'<p class="subtitle">{i18n(document.get("subtitle") or bi("Gameplay & Development Specification", "Spesifikasi Gameplay & Pengembangan"))}</p>'
        f'<p class="lead">{i18n(overview_data["project_context"])}</p>'
        f'<div class="facts three">{facts_html}</div>'
        f"<h3>{i18n(bi('Complete Gameplay Journey', 'Perjalanan Gameplay Lengkap'))}</h3>"
        f'<div class="journey"{journey_style}>{journey_html}</div>' + _summary_note(overview_data["main_systems"])
    )
    context = bi(
        f"Production Development Document · v{document['version']}",
        f"Dokumen Pengembangan Produksi · v{document['version']}",
    )
    return page(
        "summary",
        "01",
        bi("Overview", "Gambaran Umum"),
        body,
        context=context,
        classes="sheet clean-visible",
        brand=brand,
        footer_title=bi("Overview", "Gambaran Umum"),
    )


def _summary_note(items: list[TitleDescriptionData]) -> str:
    body = "".join(f"<li>{i18n(join_text(item['title'], item['description'], sep=' — '))}</li>" for item in items)
    return (
        '<div class="summary-note">'
        f"<strong>{i18n(bi('Global Gameplay Direction', 'Arah Gameplay Global'))}</strong>"
        f'<ul class="clean-list">{body}</ul></div>'
    )


def _story_flow(item: GameplayFlowData) -> str:
    body = ['<div class="story-flow">']
    for beat in item["beats"]:
        body.append(f"<h3>{i18n(beat['title'])}</h3>")
        description = beat["description"]
        if isinstance(description, list):
            body.extend(f"<p>{i18n(paragraph)}</p>" for paragraph in description)
        else:
            body.append(f"<p>{i18n(description)}</p>")
    body.append(
        '<div class="story-transition">'
        f"<b>{i18n(bi('Transition', 'Transisi'))}</b>"
        f"<p>{i18n(join_text(bi('Next:', 'Berikutnya:'), item['next_destination']))}</p></div>"
    )
    body.append("</div>")
    return "".join(body)


def flow_page_id(item: GameplayFlowData, index: int) -> str:
    return "flow-start" if index == 0 else f"flow-{item['id']}"


def flow_phase(item: GameplayFlowData, index: int) -> str:
    return "dev-flow" if index == 0 else f"dev-{item['id']}"


def flow_pages(data: RenderData) -> list[str]:
    pages: list[str] = []
    brand = data["document"].get("brand") or data["document"]["title"]
    packages = {package["id"]: package for package in data["packages"]}

    for index, item in enumerate(data["gameplay_flow"]):
        page_id = flow_page_id(item, index)
        body = f"<h2>{i18n(item['title'])}</h2>"
        if item.get("eyebrow"):
            body += f'<p class="eyebrow">{i18n(item["eyebrow"])}</p>'
        body += f'<p class="section-intro">{i18n(item["narrative_context"])}</p>'
        body += _story_flow(item)

        package = packages.get(item["id"])
        visible_terms = package.get("terms", []) if package is not None else item.get("terms", [])
        body += terms(visible_terms, f"{page_id}-terms-used-details", glossary_enabled=True)
        pages.append(
            page(
                page_id,
                f"02{chr(65 + index)}",
                item["title"],
                body,
                context=item["title"],
                header=bi("02 — Gameplay Flow", "02 — Alur Gameplay"),
                footer_title=join_text(
                    bi("Gameplay Flow", "Alur Gameplay"),
                    item["title"],
                    sep=" · ",
                ),
                brand=brand,
                phase=flow_phase(item, index),
                role="gameplay-flow",
                classes="sheet clean-visible story-page glossary-enabled-page",
            )
        )
    return pages


def _golden_global_title(item: GlobalDevelopmentData) -> Any:
    return GOLDEN_GLOBAL_TITLES[item["id"]]


def global_page_id(item: GlobalDevelopmentData) -> str:
    return GOLDEN_GLOBAL_PAGE_IDS[item["id"]]


def _global_tabs(items: list[GlobalDevelopmentData], active_id: str) -> str:
    links = []
    for index, item in enumerate(items, 1):
        target = global_page_id(item)
        active = item["id"] == active_id
        active_class = " is-active" if active else ""
        current = ' aria-current="page"' if active else ""
        title = _golden_global_title(item)
        links.append(
            f'<a aria-label="Open {esc(txt(title)["en"])}" class="section-tab section-tab-link{active_class}" '
            f'data-section-target="{esc(target)}" href="#{esc(target)}"{current}>'
            f"<b>{i18n(str(index))}</b><span>{i18n(title)}</span></a>"
        )
    return (
        '<div aria-label="Development section navigation" class="section-tabs package-tabs">'
        + "".join(links)
        + "</div>"
    )


def _development_requirement_rows(groups: list[DevelopmentRequirementGroupData]) -> list[str]:
    rows: list[str] = []
    for group_index, group in enumerate(groups, 1):
        rows.append(
            f'<tr class="quarry-group-row"><td><b>{group_index}</b></td>'
            f'<td colspan="3"><b>{i18n(group["title"])}</b></td></tr>'
        )
        for item_index, item in enumerate(group["items"]):
            code = item.get("code") or chr(65 + item_index)
            rows.append(
                f"<tr><td><b>{i18n(code)}</b></td><td><b>{i18n(item['title'])}</b></td>"
                f"<td>{cell_html(item['details'])}</td><td>{cell_html(item['result'])}</td></tr>"
            )
    return rows


def _dedupe_terms(items: list[TermData]) -> list[TermData]:
    output: list[TermData] = []
    seen: set[str] = set()
    for item in items:
        key = str(item["key"]).casefold()
        if key in seen:
            continue
        seen.add(key)
        output.append(item)
    return output


def _global_terms(items: list[GlobalDevelopmentData]) -> list[TermData]:
    output: list[TermData] = []
    for item in items:
        output.extend(item.get("terms", []))
    return _dedupe_terms(output)


def global_pages(data: RenderData) -> list[str]:
    pages: list[str] = []
    items = data["global_development"]
    brand = data["document"].get("brand") or data["document"]["title"]
    system_terms = _global_terms(items)

    for index, item in enumerate(items):
        page_id = global_page_id(item)
        title = _golden_global_title(item)
        body = (
            f'<h2 class="development-package-title">{i18n(title)}</h2>'
            f'<p class="development-package-subtitle">{i18n(item.get("subtitle") or bi("Project-wide development", "Pengembangan tingkat project"))}</p>'
            + _global_tabs(items, item["id"])
            + context_block(join_text(title, bi("Overview", "Gambaran Umum")), item["overview"])
            + heading(bi("Development Flow", "Alur Pengembangan"))
            + flow_cards(item["flow"], "quarry-development-flow")
            + heading(bi("Development Requirements", "Kebutuhan Pengembangan"))
            + production_table(
                [
                    bi("No.", "No."),
                    bi("Setup", "Setup"),
                    bi("Development Requirements", "Kebutuhan Pengembangan"),
                    bi("System Result", "Hasil Sistem"),
                ],
                _development_requirement_rows(item["requirements"]),
                "quarry-dev-table",
            )
            + heading(bi("Important Development Notes", "Catatan Pengembangan Penting"))
            + note_grid(item.get("notes", []))
            + terms(system_terms, f"{page_id}-terms-used-details", glossary_enabled=True)
        )
        pages.append(
            page(
                page_id,
                f"03{chr(65 + index)}",
                title,
                body,
                context=title,
                header=bi("03 — Development", "03 — Development"),
                footer_title=join_text(bi("Development", "Development"), title, sep=" · "),
                brand=brand,
                phase="dev-system",
                clean_target="summary",
                role="developer-overview",
                classes="sheet professional-only quarry-package-page phase-package-page global-development-page glossary-enabled-page",
            )
        )
    return pages


def _gameplay_info_rows(package: PackageData) -> list[str]:
    gameplay = package["gameplay"]
    result_model = gameplay["result_model"]
    result_label = (
        bi("Scoring Criteria", "Kriteria Scoring")
        if result_model["mode"] == "scored"
        else bi("Completion Criteria", "Kriteria Penyelesaian")
    )
    pairs = [
        (bi("Game Purpose", "Tujuan Gameplay"), gameplay["purpose"]),
        (bi("Gameplay Time", "Waktu Gameplay"), gameplay["gameplay_time"]),
        (bi("Starting Condition", "Kondisi Awal"), gameplay["start_condition"]),
        (bi("End Condition", "Kondisi Selesai"), gameplay["end_condition"]),
        (bi("Fail Condition", "Kondisi Gagal"), gameplay["blocked_or_fail_condition"]),
        (result_label, result_model["summary"]),
    ]
    return [f"<tr><td><b>{i18n(label)}</b></td><td>{cell_html(value)}</td></tr>" for label, value in pairs]


def _level_requirement_rows(groups: list[LevelRequirementGroupData]) -> list[str]:
    rows: list[str] = []
    number = 1
    multiple_groups = len(groups) > 1
    for group_index, group in enumerate(groups, 1):
        if multiple_groups:
            rows.append(
                f'<tr class="quarry-group-row"><td><b>{group_index}</b></td>'
                f'<td colspan="4"><b>{i18n(group["title"])}</b></td></tr>'
            )
        for item in group["items"]:
            code = item.get("code") or number
            number += 1
            subtitle = item.get("subtitle") or (group["title"] if not multiple_groups else "")
            object_cell = f"<b>{i18n(item['object'])}</b>"
            if present(subtitle):
                object_cell += f"<small>{i18n(subtitle)}</small>"
            rows.append(
                f"<tr><td><b>{i18n(code)}</b></td><td>{object_cell}</td>"
                f"<td>{cell_html(item['area_size'])}</td>"
                f"<td>{cell_html(item['build_and_visual'])}</td>"
                f"<td>{cell_html(item['gameplay_function'])}</td></tr>"
            )
            for child_index, child in enumerate(item.get("children", [])):
                child_code = child.get("code") or chr(65 + child_index)
                rows.append(
                    f'<tr class="quarry-child-row"><td><b>{i18n(child_code)}</b></td>'
                    f"<td><b>{i18n(child['object'])}</b></td>"
                    f"<td>{cell_html(child['area_size'])}</td>"
                    f"<td>{cell_html(child['build_and_visual'])}</td>"
                    f"<td>{cell_html(child['gameplay_function'])}</td></tr>"
                )
    return rows


def _developer_requirement_rows(developer: DeveloperData) -> list[str]:
    rows = _development_requirement_rows(developer["requirements"])
    group_number = len(developer["requirements"]) + 1

    scoring = developer.get("scoring")
    if scoring is not None:
        rows.append(
            f'<tr class="quarry-group-row"><td><b>{group_number}</b></td>'
            f'<td colspan="3"><b>{i18n(bi("Scoring Setup", "Setup Scoring"))}</b></td></tr>'
        )
        rows.append(
            f"<tr><td><b>A</b></td><td><b>{i18n(scoring['score_name'])}</b></td>"
            f"<td>{score_html(scoring)}</td>"
            f"<td>{cell_html(scoring['final_result_relationship'])}</td></tr>"
        )
        group_number += 1
    else:
        completion = developer.get("completion_data")
        if completion is None:
            raise ValueError("validated completion-only developer is missing completion_data")
        rows.append(
            f'<tr class="quarry-group-row"><td><b>{group_number}</b></td>'
            f'<td colspan="3"><b>{i18n(bi("Completion and Data", "Completion dan Data"))}</b></td></tr>'
        )
        rows.append(
            f"<tr><td><b>A</b></td><td><b>{i18n(completion['completion_name'])}</b></td>"
            f"<td>{completion_html(completion)}</td>"
            f"<td>{cell_html(completion['handoff_result'])}</td></tr>"
        )
        group_number += 1

    rows.append(
        f'<tr class="quarry-group-row"><td><b>{group_number}</b></td>'
        f'<td colspan="3"><b>{i18n(bi("Reset Setup", "Setup Reset"))}</b></td></tr>'
    )
    rows.append(
        f"<tr><td><b>A</b></td><td><b>{i18n(bi('Reset', 'Reset'))}</b></td>"
        f"<td>{cell_html(developer['reset'])}</td><td>{cell_html(developer['reset_result'])}</td></tr>"
    )
    return rows


def package_pages(data: RenderData) -> list[str]:
    pages: list[str] = []
    packages = data["packages"]
    brand = data["document"].get("brand") or data["document"]["title"]
    for package_index, package in enumerate(packages, 1):
        package_id = package["id"]
        package_label = package["package_label"]
        package_title = package["title"]
        gameplay = package["gameplay"]
        level = package["level_design"]
        developer = package["developer"]
        package_tabs = _package_tabs(package_id, "requirement")

        gameplay_body = (
            f'<h2 class="development-package-title">{i18n(package_title)}</h2>'
            f'<p class="development-package-subtitle">{i18n(package_label)}</p>'
            + package_tabs
            + context_block(bi("Gameplay Context", "Konteks Gameplay"), gameplay["context"])
            + cards(
                [
                    (bi("Main Objective", "Tujuan Utama"), gameplay["main_objective"]),
                    (bi("Result", "Hasil"), gameplay["result"]),
                ]
            )
            + heading(bi("Gameplay Information", "Informasi Gameplay"))
            + production_table(
                [bi("Category", "Kategori"), bi("Details", "Detail")],
                _gameplay_info_rows(package),
                "quarry-overview-table",
            )
            + heading(bi("Player Flow", "Alur Player"))
            + sequence(gameplay["player_flow"])
            + terms(
                package.get("terms", []),
                f"dev-{package_id}-requirement-terms-used-details",
                glossary_enabled=True,
            )
        )
        pages.append(
            page(
                f"dev-{package_id}-requirement",
                f"03{package_index}A",
                package_label,
                gameplay_body,
                context=package_title,
                header=bi("03 — Development", "03 — Development"),
                footer_title=join_text(bi("Gameplay Overview", "Gambaran Gameplay"), package_title, sep=" · "),
                brand=brand,
                phase=f"dev-{package_id}",
                role="gameplay-overview",
                classes="sheet professional-only quarry-package-page phase-package-page role-gameplay-overview glossary-enabled-page",
            )
        )

        level_body = (
            f'<h2 class="development-package-title">{i18n(package_title)}</h2>'
            f'<p class="development-package-subtitle">{i18n(package_label)}</p>'
            + _package_tabs(package_id, "level")
            + context_block(bi("Level Design Context", "Konteks Level Design"), level["overview"])
            + heading(bi("Level Design Flow", "Alur Level Design"))
            + flow_cards(level["flow"], "quarry-design-flow")
            + heading(bi("Build Requirements", "Kebutuhan Build"))
            + production_table(
                [
                    bi("No.", "No."),
                    bi("Object", "Objek"),
                    bi("Area Size", "Ukuran Area"),
                    bi("Build and Visual Requirements", "Kebutuhan Build dan Visual"),
                    bi("Gameplay Function", "Fungsi Gameplay"),
                ],
                _level_requirement_rows(level["requirements"]),
                "quarry-build-table",
            )
            + heading(bi("Important Build Notes", "Catatan Build Penting"))
            + note_grid(level.get("notes", []))
            + terms(package.get("terms", []), f"dev-{package_id}-level-terms-used-details", glossary_enabled=True)
        )
        pages.append(
            page(
                f"dev-{package_id}-level",
                f"03{package_index}B",
                package_label,
                level_body,
                context=package_title,
                header=bi("03 — Development", "03 — Development"),
                footer_title=join_text(bi("Level Design", "Level Design"), package_title, sep=" · "),
                brand=brand,
                phase=f"dev-{package_id}",
                role="level-design",
                classes="sheet professional-only quarry-package-page phase-package-page glossary-enabled-page",
            )
        )

        developer_body = (
            f'<h2 class="development-package-title">{i18n(package_title)}</h2>'
            f'<p class="development-package-subtitle">{i18n(package_label)}</p>'
            + _package_tabs(package_id, "developer")
            + context_block(bi("Developer Context", "Konteks Developer"), developer["overview"])
            + heading(bi("Development Flow", "Alur Pengembangan"))
            + flow_cards(developer["flow"], "quarry-development-flow")
            + heading(bi("Development Requirements", "Kebutuhan Pengembangan"))
            + production_table(
                [
                    bi("No.", "No."),
                    bi("Setup", "Setup"),
                    bi("Development Requirements", "Kebutuhan Pengembangan"),
                    bi("Gameplay Function", "Fungsi Gameplay"),
                ],
                _developer_requirement_rows(developer),
                "quarry-development-table",
            )
            + heading(bi("Important Development Notes", "Catatan Pengembangan Penting"))
            + note_grid(developer.get("notes", []))
            + terms(
                package.get("terms", []),
                f"dev-{package_id}-developer-terms-used-details",
                glossary_enabled=True,
            )
        )
        pages.append(
            page(
                f"dev-{package_id}-developer",
                f"03{package_index}C",
                package_label,
                developer_body,
                context=package_title,
                header=bi("03 — Development", "03 — Development"),
                footer_title=join_text(bi("Developer", "Developer"), package_title, sep=" · "),
                brand=brand,
                phase=f"dev-{package_id}",
                role="developer",
                classes="sheet professional-only quarry-package-page phase-package-page glossary-enabled-page",
            )
        )
    return pages


def glossary(data: RenderData) -> dict[str, dict[str, str]]:
    glossary_data: dict[str, dict[str, str]] = {}
    terms_by_role: dict[str, list[TermData]] = {
        "gameplay": [],
        "level_design": [],
        "developer": [],
    }
    for item in data["gameplay_flow"]:
        terms_data = item.get("terms", [])
        for term in terms_data:
            terms_by_role["gameplay"].append(term)
    for package in data["packages"]:
        for term in package.get("terms", []):
            roles = term.get("roles") or ["gameplay", "level_design", "developer"]
            for role in roles:
                terms_by_role[role].append(term)

    for items in terms_by_role.values():
        for term in _dedupe_terms(items):
            definition = txt(term["definition"])
            for language in ("en", "id"):
                aliases = term.get("aliases", [])
                if isinstance(aliases, dict):
                    aliases = aliases.get(language, [])
                for label in [txt(term["label"])[language], *aliases]:
                    if not label:
                        continue
                    glossary_data.setdefault(language, {})[label] = definition[language]
    return glossary_data


def navigation(data: RenderData) -> str:
    links: list[tuple[str, str, Any, Any]] = [
        (
            "summary",
            "01",
            bi("Overview", "Gambaran Umum"),
            "",
        )
    ]
    for index, item in enumerate(data["gameplay_flow"]):
        links.append(
            (
                flow_page_id(item, index),
                f"02{chr(65 + index)}",
                item["title"],
                bi("Gameplay Flow", "Alur Gameplay"),
            )
        )
    for index, item in enumerate(data["global_development"]):
        links.append(
            (
                global_page_id(item),
                f"03{chr(65 + index)}",
                _golden_global_title(item),
                bi("Development", "Development"),
            )
        )
    role_order = ("requirement", "level", "developer")
    for package_index, package in enumerate(data["packages"], 1):
        for role_suffix, role_label in (
            ("requirement", bi("Gameplay Overview", "Gambaran Gameplay")),
            ("level", bi("Level Design", "Level Design")),
            ("developer", bi("Developer", "Developer")),
        ):
            links.append(
                (
                    f"dev-{package['id']}-{role_suffix}",
                    f"03{package_index}{'ABC'[role_order.index(role_suffix)]}",
                    package["package_label"],
                    role_label,
                )
            )
    groups: list[str] = []
    for target, nav_index, label, small in links:
        groups.append(
            f'<a data-target="{esc(target)}" href="#{esc(target)}">'
            f'<span class="nav-index">{esc(nav_index)}</span>'
            f'<span class="nav-copy"><strong>{i18n(label)}</strong>'
            f"<small>{i18n(small)}</small></span></a>"
        )
    return "".join(groups)
