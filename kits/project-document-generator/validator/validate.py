#!/usr/bin/env python3
"""Mechanical Flow 4 validation for a repository-backed PRD project.

Checks current artifact structure, render-data invariants, navigation, and a small
set of Golden Sample composition markers. It does not judge semantic or visual
quality; those remain part of the Flow 4 review.
"""
from __future__ import annotations

import argparse
import hashlib
import html as html_lib
import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPEN_RE = re.compile(r"\b(?:TBD|TODO|FIXME|INSERT\s+(?:TEXT|VALUE)|USE\s+APPROVED\s+AMOUNT)\b|\[OPEN\]", re.I)
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
WEIGHT_RE = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*%?\s*$")
INTAKE_STATUS_RE = re.compile(r"(?m)^\s*status:\s*([A-Za-z0-9_-]+)\s*(?:#.*)?$")
INTAKE_READY_RE = re.compile(r"(?mi)^\s*ready_for_prd:\s*(true|false)\s*(?:#.*)?$")
FLOW2_EXPLICIT_BLOCKERS = {
    "requirement-register.yaml": {
        "approval_status": {"pending"},
        "recovery_class": {"blocked"},
    },
    "source-inventory.yaml": {
        "inspection": {"blocked"},
    },
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


def flow2_readiness(path: Path) -> tuple[bool, str]:
    if not path.is_file():
        return False, f"missing Flow 2 intake state: {path}"

    text = path.read_text(encoding="utf-8")
    statuses = INTAKE_STATUS_RE.findall(text)
    readiness = INTAKE_READY_RE.findall(text)
    if len(statuses) != 1 or len(readiness) != 1:
        return False, "intake-state.yaml must define exactly one status and one ready_for_prd boolean"

    status = statuses[0]
    ready = readiness[0].lower() == "true"
    if status != "ready_for_prd" or not ready:
        return False, f"Flow 2 is not ready: status={status!r}, ready_for_prd={ready}"
    return True, "Flow 2 intake state explicitly reports ready_for_prd"


def flow2_persisted_state_consistency(project: Path) -> tuple[bool, str]:
    findings: list[str] = []

    for filename, rules in FLOW2_EXPLICIT_BLOCKERS.items():
        path = project / "state" / filename
        if not path.is_file():
            continue
        for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = raw.split("#", 1)[0].strip()
            if not line or ":" not in line:
                continue
            if line.startswith("-"):
                line = line[1:].lstrip()
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
                value = value[1:-1].strip()
            normalized = value.casefold()
            if key in rules and normalized in rules[key]:
                findings.append(f"{filename}:{lineno} {key}={value!r}")

    if findings:
        return False, "explicit persisted Flow 2 blocker(s): " + "; ".join(findings)
    return True, "no explicit persisted Flow 2 blocker marker contradicts ready_for_prd"


def expected_page_ids(data: dict[str, Any]) -> list[str]:
    ids = ["summary"]
    ids += [f'flow-{item["id"]}' for item in data.get("gameplay_flow", [])]
    ids += [f'global-{item["id"]}' for item in data.get("global_development", [])]
    for pkg in data.get("packages", []):
        pid = pkg["id"]
        ids += [f"dev-{pid}-requirement", f"dev-{pid}-level", f"dev-{pid}-developer"]
    return ids


def golden_composition_errors(data: dict[str, Any], facts: HtmlFacts) -> list[str]:
    failures: list[str] = []

    def require(section_id: str, required: set[str]) -> None:
        available = facts.section_classes.get(section_id, set())
        missing = sorted(required - available)
        if missing:
            failures.append(f"{section_id} missing {missing}")

    for item in data.get("gameplay_flow", []):
        require(f'flow-{item["id"]}', {"narrative-page", "narrative-sequence"})

    for item in data.get("global_development", []):
        section_id = f'global-{item["id"]}'
        required = {"package-tabs", "section-context"}
        if item.get("flow"):
            required.add("quarry-development-flow")
        if item.get("requirements"):
            required.add("production-table")
        require(section_id, required)

    for pkg in data.get("packages", []):
        pid = pkg["id"]
        gameplay = pkg.get("gameplay") if isinstance(pkg.get("gameplay"), dict) else {}
        level = pkg.get("level_design") if isinstance(pkg.get("level_design"), dict) else {}
        developer = pkg.get("developer") if isinstance(pkg.get("developer"), dict) else {}

        gameplay_required = {"package-tabs", "phase-context-grid", "phase-overview-table"}
        if gameplay.get("player_flow"):
            gameplay_required.add("role-sequence")
        require(f"dev-{pid}-requirement", gameplay_required)

        level_required = {"package-tabs", "section-context"}
        if level.get("flow"):
            level_required.add("quarry-design-flow")
        if level.get("requirements"):
            level_required.add("quarry-build-table")
        if level.get("notes"):
            level_required.add("quarry-note-grid")
        require(f"dev-{pid}-level", level_required)

        developer_required = {"package-tabs", "section-context", "quarry-development-table", "quarry-score-summary"}
        if developer.get("flow"):
            developer_required.add("quarry-development-flow")
        if developer.get("notes"):
            developer_required.add("quarry-note-grid")
        require(f"dev-{pid}-developer", developer_required)

    return failures


def validate(project: Path) -> dict[str, Any]:
    intake_path = project / "state" / "intake-state.yaml"
    content_path = project / "work" / "content.md"
    data_path = project / "work" / "render-data.json"
    html_path = project / "output" / "final.html"

    errors: list[str] = []
    warnings: list[str] = []
    checks: list[dict[str, str]] = []

    def check(name: str, ok: bool, detail: str) -> None:
        checks.append({"check": name, "status": "pass" if ok else "fail", "detail": detail})
        if not ok:
            errors.append(f"{name}: {detail}")

    flow2_ready, flow2_detail = flow2_readiness(intake_path)
    check("flow2_ready_for_prd", flow2_ready, flow2_detail)
    if flow2_ready:
        flow2_consistent, flow2_consistency_detail = flow2_persisted_state_consistency(project)
        check("flow2_persisted_state_consistent", flow2_consistent, flow2_consistency_detail)
    check("canonical_content_exists", content_path.is_file(), str(content_path))
    check("render_data_exists", data_path.is_file(), str(data_path))
    check("rendered_html_exists", html_path.is_file(), str(html_path))
    if errors:
        return {"status": "fail", "errors": errors, "warnings": warnings, "checks": checks}

    content = content_path.read_text(encoding="utf-8")
    check("canonical_content_has_no_open_placeholders", OPEN_RE.search(content) is None, "content.md contains no unresolved placeholder token")

    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"render_data_json: {exc}")
        return {"status": "fail", "errors": errors, "warnings": warnings, "checks": checks}

    if not isinstance(data, dict):
        errors.append("render_data_root: render-data must be an object")
        return {"status": "fail", "errors": errors, "warnings": warnings, "checks": checks}

    actual_content_sha = hashlib.sha256(content_path.read_bytes()).hexdigest()
    declared_content_sha = data.get("canonical_content_sha256")
    binding_valid = (
        isinstance(declared_content_sha, str)
        and SHA256_RE.fullmatch(declared_content_sha) is not None
        and declared_content_sha == actual_content_sha
    )
    if not isinstance(declared_content_sha, str) or SHA256_RE.fullmatch(declared_content_sha) is None:
        binding_detail = "render-data canonical_content_sha256 is missing or invalid"
    elif declared_content_sha != actual_content_sha:
        binding_detail = "render-data projection is stale relative to work/content.md; regenerate the affected projection"
    else:
        binding_detail = "render-data is bound to the current canonical content revision"
    check("render_data_matches_canonical_content", binding_valid, binding_detail)

    doc = data.get("document")
    check("document_object", isinstance(doc, dict), "render-data.document must be an object")
    title = text_en(doc.get("title")) if isinstance(doc, dict) else ""
    check("document_title", bool(title.strip()), "document title is present")
    check("overview_object", isinstance(data.get("overview"), dict), "render-data.overview must be an object")

    structure_ok = True
    collections: dict[str, list[dict[str, Any]]] = {}
    for key in ("gameplay_flow", "global_development", "packages"):
        value = data.get(key, [])
        if not isinstance(value, list):
            errors.append(f"{key}: must be an array")
            structure_ok = False
            collections[key] = []
            continue
        typed: list[dict[str, Any]] = []
        for index, item in enumerate(value):
            if not isinstance(item, dict):
                errors.append(f"{key}[{index}]: item must be an object")
                structure_ok = False
                continue
            item_id = item.get("id")
            if not isinstance(item_id, str) or not ID_RE.fullmatch(item_id):
                errors.append(f"{key}[{index}]: invalid stable id {item_id!r}")
                structure_ok = False
                continue
            typed.append(item)
        collections[key] = typed

    packages = collections["packages"]
    check("packages_array", len(packages) > 0, "at least one gameplay package is required for this template profile")

    seen_pkg: set[str] = set()
    for pkg in packages:
        pid = pkg["id"]
        if pid in seen_pkg:
            errors.append(f"package_{pid}: duplicate package id")
        seen_pkg.add(pid)
        for role in ("gameplay", "level_design", "developer"):
            if not isinstance(pkg.get(role), dict):
                errors.append(f"package_{pid}: missing {role} object")
        dev = pkg.get("developer") if isinstance(pkg.get("developer"), dict) else {}
        has_score = isinstance(dev.get("scoring"), dict) and bool(dev.get("scoring"))
        has_completion = isinstance(dev.get("completion_data"), dict) and bool(dev.get("completion_data"))
        if has_score == has_completion:
            errors.append(f"package_{pid}: developer must define exactly one of scoring or completion_data")
        if has_score:
            components = dev["scoring"].get("components", [])
            if isinstance(components, list):
                raw_weights = [
                    component.get("weight") if isinstance(component, dict) else None
                    for component in components
                ]
                has_weighted_scoring = any(weight not in (None, "") for weight in raw_weights)
                if has_weighted_scoring:
                    parsed_weights: list[float] = []
                    for index, weight in enumerate(raw_weights):
                        parsed = scoring_weight(weight)
                        if parsed is None:
                            errors.append(
                                f"package_{pid}: scoring component {index} weight must be numeric or a numeric percentage string"
                            )
                        else:
                            parsed_weights.append(parsed)
                    if len(parsed_weights) == len(raw_weights):
                        total = sum(parsed_weights)
                        if abs(total - 100.0) > 1e-9:
                            errors.append(f"package_{pid}: scoring weights total {total:g}, expected 100")

    if not structure_ok:
        return {"status": "fail", "errors": errors, "warnings": warnings, "checks": checks}

    html_text = html_path.read_text(encoding="utf-8")
    facts = HtmlFacts()
    try:
        facts.feed(html_text)
    except Exception as exc:
        errors.append(f"html_parse: {exc}")

    actual_render_data_sha = hashlib.sha256(data_path.read_bytes()).hexdigest()
    html_bindings = facts.render_data_sha256
    html_binding_valid = (
        len(html_bindings) == 1
        and SHA256_RE.fullmatch(html_bindings[0]) is not None
        and html_bindings[0] == actual_render_data_sha
    )
    if not html_bindings:
        html_binding_detail = "rendered HTML is missing render-data-sha256 revision binding"
    elif len(html_bindings) != 1:
        html_binding_detail = f"rendered HTML must contain exactly one render-data-sha256 binding; found {len(html_bindings)}"
    elif SHA256_RE.fullmatch(html_bindings[0]) is None:
        html_binding_detail = "rendered HTML render-data-sha256 binding is invalid"
    elif html_bindings[0] != actual_render_data_sha:
        html_binding_detail = "rendered HTML is stale relative to work/render-data.json; rerender final.html"
    else:
        html_binding_detail = "rendered HTML is bound to the current render-data revision"
    check("html_matches_current_render_data", html_binding_valid, html_binding_detail)

    duplicates = sorted(k for k, count in Counter(facts.ids).items() if count > 1)
    check("html_ids_unique", not duplicates, f"duplicate ids: {duplicates}" if duplicates else "no duplicate HTML ids")

    expected = expected_page_ids(data)
    actual_pages = facts.document_section_ids
    missing_expected = [page_id for page_id in expected if page_id not in actual_pages]
    extra_generated = [page_id for page_id in actual_pages if page_id not in expected]
    exact_pages = actual_pages == expected
    check(
        "generated_page_set_matches_current_render_data",
        exact_pages,
        f"generated pages match expected order/set: {len(expected)} pages"
        if exact_pages
        else f"expected {expected}; actual {actual_pages}; missing {missing_expected}; extra {extra_generated}",
    )

    composition = golden_composition_errors(data, facts)
    check(
        "golden_page_composition",
        not composition,
        "Golden Sample composition markers present on generated pages" if not composition else "; ".join(composition),
    )

    id_set = set(facts.ids)
    broken = sorted(set(target for target in facts.fragment_hrefs if target not in id_set))
    check("fragment_navigation_reachable", not broken, f"broken targets: {broken}" if broken else "all fragment links resolve")

    browser_title = "".join(facts.title_parts).strip()
    check("browser_title_matches_project", bool(title) and title.lower() in html_lib.unescape(browser_title).lower(), f"browser title: {browser_title!r}")

    if not data.get("gameplay_flow"):
        warnings.append("No gameplay_flow entries; confirm this is intentional for the selected document profile.")
    if not data.get("global_development"):
        warnings.append("No global_development pages; confirm the project has no shared global system requiring its own page.")

    status = "pass" if not errors else "fail"
    return {"status": status, "errors": errors, "warnings": warnings, "checks": checks, "expected_pages": expected}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="workspace/active/<project> directory")
    parser.add_argument("--output", type=Path, help="optional JSON result path")
    args = parser.parse_args()
    result = validate(args.project)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
