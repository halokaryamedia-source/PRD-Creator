from __future__ import annotations

import hashlib
import html as html_lib
import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from shared.assets import parse_asset_requirements
from shared.intake import validate_flow2_state
from shared.issues import Issue
from shared.render_schema import ProjectionError, validate_projection_schema
from shared.topology import require_owner

OPEN_RE = re.compile(r"\b(?:TBD|TODO|FIXME|INSERT\s+(?:TEXT|VALUE)|USE\s+APPROVED\s+AMOUNT)\b|\[OPEN\]", re.I)
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
WEIGHT_RE = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*%?\s*$")

GOLDEN_GLOBAL_PAGE_IDS = {
    "development-overview": "development-overview",
    "game-system": "shared-systems",
    "data-reset": "shared-data-reset",
    "gameplay-development": "phase-development",
}


class HtmlFacts(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.fragment_hrefs: list[str] = []
        self.title_parts: list[str] = []
        self.document_section_ids: list[str] = []
        self.section_classes: dict[str, set[str]] = {}
        self.render_data_sha256: list[str] = []
        self.asset_requirements_sha256: list[str] = []
        self._in_title = False
        self._in_document_main = False
        self._current_document_section: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        classes = set(str(data.get("class") or "").split())
        tag_name = tag.lower()
        if tag_name == "main" and "document-main" in classes:
            self._in_document_main = True
        if data.get("id"):
            self.ids.append(str(data["id"]))
        if tag_name == "section" and self._in_document_main and data.get("id"):
            section_id = str(data["id"])
            self.document_section_ids.append(section_id)
            self._current_document_section = section_id
            self.section_classes.setdefault(section_id, set()).update(classes)
        elif self._current_document_section:
            self.section_classes.setdefault(self._current_document_section, set()).update(classes)
        if tag_name == "meta" and str(data.get("name") or "").casefold() == "render-data-sha256":
            self.render_data_sha256.append(str(data.get("content") or ""))
        if tag_name == "meta" and str(data.get("name") or "").casefold() == "asset-requirements-sha256":
            self.asset_requirements_sha256.append(str(data.get("content") or ""))
        href = data.get("href")
        if isinstance(href, str) and href.startswith("#") and len(href) > 1:
            self.fragment_hrefs.append(href[1:])
        if tag_name == "title":
            self._in_title = True

    def handle_endtag(self, tag: str) -> None:
        tag_name = tag.lower()
        if tag_name == "title":
            self._in_title = False
        if tag_name == "section" and self._current_document_section:
            self._current_document_section = None
        if tag_name == "main" and self._in_document_main:
            self._in_document_main = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_parts.append(data)


def text_en(value: Any) -> str:
    if isinstance(value, dict):
        value = value.get("en") or value.get("id") or ""
    return str(value or "")


def scoring_weight(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        match = WEIGHT_RE.fullmatch(value)
        if match:
            return float(match.group(1))
    return None


def _global_page_id(item: dict[str, Any]) -> str:
    return GOLDEN_GLOBAL_PAGE_IDS.get(item.get("id"), f'global-{item.get("id", "section")}')


def expected_page_ids(data: dict[str, Any]) -> list[str]:
    ids = ["summary"]
    for index, item in enumerate(data.get("gameplay_flow", [])):
        ids.append("flow-start" if index == 0 else f'flow-{item["id"]}')
    ids += [_global_page_id(item) for item in data.get("global_development", [])]
    for package in data.get("packages", []):
        package_id = package["id"]
        ids += [
            f"dev-{package_id}-requirement",
            f"dev-{package_id}-level",
            f"dev-{package_id}-developer",
        ]
    return ids


def document_composition_errors(data: dict[str, Any], facts: HtmlFacts) -> list[str]:
    failures: list[str] = []
    packages = {package["id"]: package for package in data.get("packages", [])}

    def require(section_id: str, required: set[str]) -> None:
        available = facts.section_classes.get(section_id, set())
        missing = sorted(required - available)
        if missing:
            failures.append(f"{section_id} missing {missing}")

    for index, item in enumerate(data.get("gameplay_flow", [])):
        section_id = "flow-start" if index == 0 else f'flow-{item["id"]}'
        required = {"clean-visible", "story-page", "story-flow"}
        source_terms = (
            item.get("terms", [])
            if index == 0
            else packages.get(item["id"], {}).get("terms", [])
        )
        if source_terms:
            required.add("quarry-definition-list")
        require(section_id, required)
    for item in data.get("global_development", []):
        require(
            _global_page_id(item),
            {
                "professional-only",
                "quarry-package-page",
                "phase-package-page",
                "global-development-page",
                "package-tabs",
                "section-context",
                "quarry-development-flow",
                "quarry-dev-table",
                "quarry-note-grid",
            },
        )
    for package in data.get("packages", []):
        package_id = package["id"]
        require(
            f"dev-{package_id}-requirement",
            {
                "professional-only",
                "quarry-package-page",
                "phase-package-page",
                "role-gameplay-overview",
                "package-tabs",
                "phase-context-grid",
                "quarry-overview-table",
                "quarry-sequence",
            },
        )
        require(
            f"dev-{package_id}-level",
            {
                "professional-only",
                "quarry-package-page",
                "phase-package-page",
                "package-tabs",
                "section-context",
                "quarry-design-flow",
                "quarry-build-table",
                "quarry-note-grid",
            },
        )
        require(
            f"dev-{package_id}-developer",
            {
                "professional-only",
                "quarry-package-page",
                "phase-package-page",
                "package-tabs",
                "section-context",
                "quarry-development-flow",
                "quarry-development-table",
                "quarry-score-summary",
                "quarry-note-grid",
            },
        )
    return failures


def _scoring_weight_errors(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for package in data.get("packages", []):
        package_id = package["id"]
        developer = package["developer"]
        scoring = developer.get("scoring")
        if not isinstance(scoring, dict):
            continue
        components = scoring.get("components", [])
        if not isinstance(components, list) or not components:
            continue
        parsed: list[float] = []
        for index, component in enumerate(components):
            weight = scoring_weight(component.get("weight") if isinstance(component, dict) else None)
            if weight is None:
                errors.append(
                    f"package_{package_id}: scoring component {index} weight must be numeric or a numeric percentage string"
                )
            else:
                parsed.append(weight)
        if len(parsed) == len(components) and abs(sum(parsed) - 100.0) > 1e-9:
            errors.append(f"package_{package_id}: scoring weights total {sum(parsed):g}, expected 100")
    return errors


def _asset_source_errors(project: Path, data: dict[str, Any]) -> list[str]:
    path = project / "work" / "asset-requirements.md"
    if not path.is_file():
        return []
    try:
        assets = parse_asset_requirements(path)
        for section in assets.sections:
            require_owner(data, section.owner_id)
    except (OSError, ValueError) as exc:
        return [str(exc)]
    return []


def validate(project: Path) -> dict[str, Any]:
    project = project.resolve()
    content_path = project / "work" / "content.md"
    data_path = project / "work" / "render-data.json"
    errors: list[str] = []
    warnings: list[str] = []
    checks: list[dict[str, str]] = []
    structured: list[Issue] = []

    def check(name: str, ok: bool, detail: str, issue: Issue | None = None) -> None:
        checks.append({"check": name, "status": "pass" if ok else "fail", "detail": detail})
        if not ok:
            errors.append(f"{name}: {detail}")
            if issue is not None:
                structured.append(issue)

    flow2_issues = validate_flow2_state(project)
    check(
        "flow2_state_current",
        not flow2_issues,
        "Flow 2 approval is bound to the current requirement-register revision"
        if not flow2_issues
        else "; ".join(str(issue) for issue in flow2_issues),
    )
    structured.extend(flow2_issues)
    check("canonical_content_exists", content_path.is_file(), str(content_path))
    check("render_data_exists", data_path.is_file(), str(data_path))
    if errors:
        return _result(errors, warnings, checks, structured)

    content = content_path.read_text(encoding="utf-8")
    check(
        "canonical_content_has_no_open_placeholders",
        OPEN_RE.search(content) is None,
        "content.md contains no unresolved placeholder token",
        Issue(
            "PRD_CONTENT_PLACEHOLDER",
            "flow3.content",
            "canonical content contains an unresolved placeholder",
            path="work/content.md",
        ),
    )

    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"render_data_json: {exc}")
        structured.append(
            Issue(
                "PRD_PROJECTION_JSON_INVALID",
                "flow3.projection",
                str(exc),
                path="work/render-data.json",
                line=exc.lineno,
            )
        )
        return _result(errors, warnings, checks, structured)
    if not isinstance(data, dict):
        errors.append("render_data_root: render-data must be an object")
        structured.append(
            Issue(
                "PRD_PROJECTION_ROOT_INVALID",
                "flow3.projection",
                "render-data root must be an object",
                path="work/render-data.json",
            )
        )
        return _result(errors, warnings, checks, structured)

    try:
        validate_projection_schema(data)
    except ProjectionError as exc:
        check(
            "projection_schema",
            False,
            str(exc),
            Issue(
                "PRD_PROJECTION_SCHEMA_INVALID",
                "flow3.projection",
                str(exc),
                path="work/render-data.json",
            ),
        )
        return _result(errors, warnings, checks, structured)
    check("projection_schema", True, "render-data uses the one canonical projection field shape")

    actual_content_sha = hashlib.sha256(content_path.read_bytes()).hexdigest()
    declared_content_sha = str(data["canonical_content_sha256"])
    check(
        "render_data_matches_canonical_content",
        declared_content_sha == actual_content_sha,
        "render-data is bound to the current canonical content revision"
        if declared_content_sha == actual_content_sha
        else "render-data projection is stale relative to work/content.md",
        Issue(
            "PRD_PROJECTION_STALE",
            "flow3.projection",
            "render-data canonical_content_sha256 does not match current content.md bytes",
            path="work/render-data.json",
            field="canonical_content_sha256",
        ),
    )

    weight_errors = _scoring_weight_errors(data)
    check(
        "scoring_weights",
        not weight_errors,
        "scoring weights are coherent" if not weight_errors else "; ".join(weight_errors),
    )

    asset_errors = _asset_source_errors(project, data)
    check(
        "asset_requirements_source",
        not asset_errors,
        "non-Voice Production Asset source is valid against accepted topology"
        if not asset_errors
        else "; ".join(asset_errors),
    )

    document = data["document"]
    current_version = text_en(document["version"]).strip()
    check(
        "document_version_semantic",
        SEMVER_RE.fullmatch(current_version) is not None,
        f"document.version={current_version!r}",
    )
    html_path = project / "output" / f"v{current_version}" / "prd.html"
    check("rendered_html_exists", html_path.is_file(), str(html_path))
    if errors:
        return _result(errors, warnings, checks, structured)

    html_text = html_path.read_text(encoding="utf-8")
    facts = HtmlFacts()
    try:
        facts.feed(html_text)
    except Exception as exc:
        errors.append(f"html_parse: {exc}")
        structured.append(
            Issue(
                "PRD_HTML_PARSE_FAILED",
                "flow3.renderer",
                str(exc),
                path=f"output/v{current_version}/prd.html",
            )
        )

    actual_render_data_sha = hashlib.sha256(data_path.read_bytes()).hexdigest()
    bindings = facts.render_data_sha256
    binding_ok = (
        len(bindings) == 1
        and SHA256_RE.fullmatch(bindings[0]) is not None
        and bindings[0] == actual_render_data_sha
    )
    if not bindings:
        html_binding_detail = "rendered HTML is missing render-data-sha256 revision binding"
    elif len(bindings) != 1:
        html_binding_detail = f"rendered HTML must contain exactly one render-data-sha256 binding; found {len(bindings)}"
    elif SHA256_RE.fullmatch(bindings[0]) is None:
        html_binding_detail = "rendered HTML render-data-sha256 binding is invalid"
    elif bindings[0] != actual_render_data_sha:
        html_binding_detail = "rendered HTML is stale relative to work/render-data.json"
    else:
        html_binding_detail = "rendered HTML is bound to the current render-data revision"
    check("html_matches_current_render_data", binding_ok, html_binding_detail)

    asset_path = project / "work" / "asset-requirements.md"
    asset_bindings = facts.asset_requirements_sha256
    if asset_path.is_file():
        actual_asset_sha = hashlib.sha256(asset_path.read_bytes()).hexdigest()
        asset_binding_ok = (
            len(asset_bindings) == 1
            and SHA256_RE.fullmatch(asset_bindings[0]) is not None
            and asset_bindings[0] == actual_asset_sha
        )
        asset_binding_detail = (
            "rendered HTML is bound to current non-Voice Production Asset requirements"
            if asset_binding_ok
            else "rendered HTML asset-requirements binding is missing, invalid, duplicated, or stale"
        )
    else:
        asset_binding_ok = not asset_bindings
        asset_binding_detail = (
            "no non-Voice Production Asset source or stale binding is present"
            if asset_binding_ok
            else "rendered HTML carries an asset binding but work/asset-requirements.md is absent"
        )
    check("html_matches_current_asset_requirements", asset_binding_ok, asset_binding_detail)

    duplicates = sorted(key for key, count in Counter(facts.ids).items() if count > 1)
    check("html_ids_unique", not duplicates, f"duplicate ids: {duplicates}" if duplicates else "no duplicate HTML ids")

    expected = expected_page_ids(data)
    actual_pages = facts.document_section_ids
    core_pages = actual_pages[: len(expected)]
    downstream_pages = actual_pages[len(expected) :]
    invalid_downstream = [
        section_id
        for section_id in downstream_pages
        if "production-assets-page" not in facts.section_classes.get(section_id, set())
    ]
    page_set_ok = core_pages == expected and not invalid_downstream
    check(
        "generated_page_set_matches_current_render_data",
        page_set_ok,
        f"PRD core matches expected order/set: {len(expected)} pages; additive Production Assets pages: {len(downstream_pages)}"
        if page_set_ok
        else f"expected core {expected}; actual prefix {core_pages}; invalid downstream {invalid_downstream}",
    )

    composition = document_composition_errors(data, facts)
    check(
        "document_page_composition",
        not composition,
        "required Golden prototype markers are present" if not composition else "; ".join(composition),
    )

    id_set = set(facts.ids)
    broken = sorted(set(target for target in facts.fragment_hrefs if target not in id_set))
    check(
        "fragment_navigation_reachable",
        not broken,
        f"broken targets: {broken}" if broken else "all fragment links resolve",
    )

    browser_title = "".join(facts.title_parts).strip()
    title = text_en(document["title"])
    check(
        "browser_title_matches_project",
        bool(title) and title.lower() in html_lib.unescape(browser_title).lower(),
        f"browser title: {browser_title!r}",
    )

    return _result(errors, warnings, checks, structured, expected_pages=expected)


def _result(
    errors: list[str],
    warnings: list[str],
    checks: list[dict[str, str]],
    issues: list[Issue],
    *,
    expected_pages: list[str] | None = None,
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "warnings": warnings,
        "checks": checks,
        "issues": [issue.as_dict() for issue in issues],
    }
    if expected_pages is not None:
        result["expected_pages"] = expected_pages
    return result
