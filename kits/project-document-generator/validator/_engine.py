#!/usr/bin/env python3
"""Mechanical Flow 4 validation for a repository-backed PRD project."""
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
FLOW2_REQUIRED_STATE = {"source-inventory.yaml": "SRC", "requirement-register.yaml": "REQ"}
FLOW2_EXPLICIT_BLOCKERS = {
    "requirement-register.yaml": {"approval_status": {"pending"}, "recovery_class": {"blocked"}},
    "source-inventory.yaml": {"inspection": {"blocked"}},
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


def _clean_state_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1].strip()
    return value


def _flow2_state_entries(path: Path, prefix: str) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        candidate = line[1:].lstrip() if line.startswith("-") else line
        if ":" not in candidate:
            continue
        key, raw_value = candidate.split(":", 1)
        key = key.strip()
        value = _clean_state_scalar(raw_value)
        if key == "id" and re.fullmatch(rf"{re.escape(prefix)}-\d+", value):
            current = {"id": value, "line": lineno, "fields": {}}
            entries.append(current)
            continue
        if current is not None:
            current["fields"][key] = (value, lineno)
    return entries


def flow2_persisted_state_consistency(project: Path) -> tuple[bool, str]:
    findings: list[str] = []
    parsed: dict[str, list[dict[str, Any]]] = {}
    for filename, prefix in FLOW2_REQUIRED_STATE.items():
        path = project / "state" / filename
        if not path.is_file():
            findings.append(f"missing required Flow 2 persisted state: state/{filename}")
            parsed[filename] = []
            continue
        entries = _flow2_state_entries(path, prefix)
        parsed[filename] = entries
        if not entries:
            findings.append(f"{filename} must contain at least one {prefix}-### entry before ready_for_prd")

    for filename, rules in FLOW2_EXPLICIT_BLOCKERS.items():
        for entry in parsed.get(filename, []):
            fields: dict[str, tuple[str, int]] = entry["fields"]
            if filename == "source-inventory.yaml":
                source_status = fields.get("status", ("current", entry["line"]))[0].casefold()
                if source_status == "superseded":
                    continue
            for key, blocked_values in rules.items():
                field = fields.get(key)
                if field is None:
                    continue
                value, lineno = field
                if value.casefold() in blocked_values:
                    findings.append(f"{filename}:{lineno} {entry['id']} {key}={value!r}")

    if findings:
        return False, "Flow 2 persisted-state contradiction(s): " + "; ".join(findings)
    return True, "required Flow 2 state is present and no unambiguous current blocker contradicts ready_for_prd"


def _has_text(value: Any) -> bool:
    return bool(text_en(value).strip())


def _has_dict_entry(value: Any) -> bool:
    return isinstance(value, list) and any(isinstance(item, dict) for item in value)


def _has_requirement_rows(groups: Any) -> bool:
    if not isinstance(groups, list):
        return False
    for group in groups:
        if not isinstance(group, dict):
            continue
        items = group.get("items") or group.get("objects") or []
        if any(isinstance(item, dict) for item in items):
            return True
    return False


def _has_narrative_beat(item: dict[str, Any]) -> bool:
    explicit = item.get("beats")
    if isinstance(explicit, list):
        for beat in explicit:
            if isinstance(beat, dict) and (_has_text(beat.get("description")) or _has_text(beat.get("details"))):
                return True
    return any(
        _has_text(item.get(key))
        for key in ("player_experience", "main_obstacle_or_change", "player_result", "narrative_context")
    )


def required_content_errors(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    for item in data.get("gameplay_flow", []):
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            continue
        flow_id = item["id"]
        if not _has_text(item.get("title")):
            failures.append(f"flow-{flow_id}: title is required")
        if not _has_narrative_beat(item):
            failures.append(f"flow-{flow_id}: at least one narrative beat/context is required")

    for item in data.get("global_development", []):
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            continue
        global_id = item["id"]
        if not _has_text(item.get("overview")):
            failures.append(f"global-{global_id}: overview is required")
        if not _has_requirement_rows(item.get("requirements")):
            failures.append(f"global-{global_id}: at least one Development Requirement row is required")

    for pkg in data.get("packages", []):
        if not isinstance(pkg, dict) or not isinstance(pkg.get("id"), str):
            continue
        package_id = pkg["id"]
        gameplay = pkg.get("gameplay") if isinstance(pkg.get("gameplay"), dict) else {}
        level = pkg.get("level_design") if isinstance(pkg.get("level_design"), dict) else {}
        developer = pkg.get("developer") if isinstance(pkg.get("developer"), dict) else {}
        if not (_has_text(gameplay.get("context")) or _has_text(gameplay.get("overview"))):
            failures.append(f"package-{package_id}: Gameplay Context is required")
        if not _has_text(gameplay.get("main_objective")):
            failures.append(f"package-{package_id}: Main Objective is required")
        if not _has_text(gameplay.get("result")):
            failures.append(f"package-{package_id}: Result is required")
        if not _has_dict_entry(gameplay.get("player_flow")):
            failures.append(f"package-{package_id}: at least one player_flow step is required")
        if not _has_text(level.get("overview")):
            failures.append(f"package-{package_id}: Level Design overview is required")
        if not _has_requirement_rows(level.get("requirements")):
            failures.append(f"package-{package_id}: at least one Build Requirement row is required")
        if not _has_text(developer.get("overview")):
            failures.append(f"package-{package_id}: Developer overview is required")
    return failures


def expected_page_ids(data: dict[str, Any]) -> list[str]:
    ids = ["summary"]
    ids += [f'flow-{item["id"]}' for item in data.get("gameplay_flow", [])]
    ids += [f'global-{item["id"]}' for item in data.get("global_development", [])]
    for pkg in data.get("packages", []):
        package_id = pkg["id"]
        ids += [
            f"dev-{package_id}-requirement",
            f"dev-{package_id}-level",
            f"dev-{package_id}-developer",
        ]
    return ids


def document_composition_errors(data: dict[str, Any], facts: HtmlFacts) -> list[str]:
    """Check only the deterministic Golden prototype markers rendered on each page."""
    failures: list[str] = []

    def require(section_id: str, required: set[str]) -> None:
        available = facts.section_classes.get(section_id, set())
        missing = sorted(required - available)
        if missing:
            failures.append(f"{section_id} missing {missing}")

    for item in data.get("gameplay_flow", []):
        require(f'flow-{item["id"]}', {"story-page", "story-flow"})

    for item in data.get("global_development", []):
        require(
            f'global-{item["id"]}',
            {"package-tabs", "section-context", "development-flow-grid", "development-requirements-table", "note-grid"},
        )

    for pkg in data.get("packages", []):
        package_id = pkg["id"]
        require(
            f"dev-{package_id}-requirement",
            {"package-tabs", "package-context-grid", "gameplay-info-table", "objective-sequence"},
        )
        require(
            f"dev-{package_id}-level",
            {"package-tabs", "section-context", "design-flow-grid", "build-requirements-table", "note-grid"},
        )
        require(
            f"dev-{package_id}-developer",
            {"package-tabs", "section-context", "development-flow-grid", "development-requirements-table", "result-summary", "note-grid"},
        )

    return failures


def validate(project: Path) -> dict[str, Any]:
    intake_path = project / "state" / "intake-state.yaml"
    content_path = project / "work" / "content.md"
    data_path = project / "work" / "render-data.json"
    html_path: Path | None = None
    errors: list[str] = []
    warnings: list[str] = []
    checks: list[dict[str, str]] = []

    def check(name: str, ok: bool, detail: str) -> None:
        checks.append({"check": name, "status": "pass" if ok else "fail", "detail": detail})
        if not ok:
            errors.append(f"{name}: {detail}")

    ready, ready_detail = flow2_readiness(intake_path)
    check("flow2_ready_for_prd", ready, ready_detail)
    if ready:
        consistent, consistency_detail = flow2_persisted_state_consistency(project)
        check("flow2_persisted_state_consistent", consistent, consistency_detail)
    check("canonical_content_exists", content_path.is_file(), str(content_path))
    check("render_data_exists", data_path.is_file(), str(data_path))
    if errors:
        return {"status": "fail", "errors": errors, "warnings": warnings, "checks": checks}

    content = content_path.read_text(encoding="utf-8")
    check(
        "canonical_content_has_no_open_placeholders",
        OPEN_RE.search(content) is None,
        "content.md contains no unresolved placeholder token",
    )

    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"render_data_json: {exc}")
        return {"status": "fail", "errors": errors, "warnings": warnings, "checks": checks}
    if not isinstance(data, dict):
        errors.append("render_data_root: render-data must be an object")
        return {"status": "fail", "errors": errors, "warnings": warnings, "checks": checks}

    document_meta = data.get("document")
    current_version = (
        text_en(document_meta.get("version")).strip()
        if isinstance(document_meta, dict)
        else ""
    )
    html_path = (
        project / "output" / f"v{current_version}" / "prd.html"
        if current_version
        else project / "output" / "v<missing-version>" / "prd.html"
    )
    check(
        "rendered_html_exists",
        bool(current_version) and html_path.is_file(),
        str(html_path) if current_version else "render-data.document.version is required to resolve the versioned prd.html",
    )
    if errors:
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

    document = data.get("document")
    check("document_object", isinstance(document, dict), "render-data.document must be an object")
    title = text_en(document.get("title")) if isinstance(document, dict) else ""
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

    gameplay_flow = collections["gameplay_flow"]
    global_development = collections["global_development"]
    packages = collections["packages"]
    check("gameplay_flow_array", len(gameplay_flow) > 0, "at least one Gameplay Flow page is required")
    check("global_development_array", len(global_development) > 0, "at least one Global Development page is required")
    check("packages_array", len(packages) > 0, "at least one gameplay package is required")

    seen_packages: set[str] = set()
    for pkg in packages:
        package_id = pkg["id"]
        if package_id in seen_packages:
            errors.append(f"package_{package_id}: duplicate package id")
        seen_packages.add(package_id)
        for role in ("gameplay", "level_design", "developer"):
            if not isinstance(pkg.get(role), dict):
                errors.append(f"package_{package_id}: missing {role} object")
        developer = pkg.get("developer") if isinstance(pkg.get("developer"), dict) else {}
        has_score = isinstance(developer.get("scoring"), dict) and bool(developer.get("scoring"))
        has_completion = isinstance(developer.get("completion_data"), dict) and bool(developer.get("completion_data"))
        if has_score == has_completion:
            errors.append(f"package_{package_id}: developer must define exactly one of scoring or completion_data")
        if has_score:
            components = developer["scoring"].get("components", [])
            if isinstance(components, list):
                raw_weights = [item.get("weight") if isinstance(item, dict) else None for item in components]
                if any(weight not in (None, "") for weight in raw_weights):
                    parsed = []
                    for index, weight in enumerate(raw_weights):
                        current = scoring_weight(weight)
                        if current is None:
                            errors.append(
                                f"package_{package_id}: scoring component {index} weight must be numeric or a numeric percentage string"
                            )
                        else:
                            parsed.append(current)
                    if len(parsed) == len(raw_weights) and abs(sum(parsed) - 100.0) > 1e-9:
                        errors.append(f"package_{package_id}: scoring weights total {sum(parsed):g}, expected 100")

    if structure_ok:
        required_content = required_content_errors(data)
        check(
            "required_content",
            not required_content,
            "required content slots are populated" if not required_content else "; ".join(required_content),
        )
    if not structure_ok:
        return {"status": "fail", "errors": errors, "warnings": warnings, "checks": checks}

    assert html_path is not None
    html_text = html_path.read_text(encoding="utf-8")
    facts = HtmlFacts()
    try:
        facts.feed(html_text)
    except Exception as exc:
        errors.append(f"html_parse: {exc}")

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
        html_binding_detail = "rendered HTML is stale relative to work/render-data.json; rerender the current versioned prd.html"
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
        if not asset_bindings:
            asset_binding_detail = "rendered HTML is missing asset-requirements-sha256 binding"
        elif len(asset_bindings) != 1:
            asset_binding_detail = (
                "rendered HTML must contain exactly one asset-requirements-sha256 binding; "
                f"found {len(asset_bindings)}"
            )
        elif SHA256_RE.fullmatch(asset_bindings[0]) is None:
            asset_binding_detail = "rendered HTML asset-requirements-sha256 binding is invalid"
        elif asset_bindings[0] != actual_asset_sha:
            asset_binding_detail = (
                "rendered HTML is stale relative to work/asset-requirements.md; "
                "rerender the current versioned prd.html"
            )
        else:
            asset_binding_detail = "rendered HTML is bound to the current non-Voice Production Asset requirements"
    else:
        asset_binding_ok = not asset_bindings
        asset_binding_detail = (
            "no non-Voice Production Asset requirement source or stale binding is present"
            if asset_binding_ok
            else "rendered HTML still carries an asset-requirements binding but work/asset-requirements.md is absent; rerender"
        )
    check(
        "html_matches_current_asset_requirements",
        asset_binding_ok,
        asset_binding_detail,
    )

    duplicates = sorted(key for key, count in Counter(facts.ids).items() if count > 1)
    check("html_ids_unique", not duplicates, f"duplicate ids: {duplicates}" if duplicates else "no duplicate HTML ids")

    expected = expected_page_ids(data)
    actual_pages = facts.document_section_ids
    core_pages = actual_pages[: len(expected)]
    downstream_pages = actual_pages[len(expected) :]
    core_exact = core_pages == expected
    invalid_downstream = [
        section_id
        for section_id in downstream_pages
        if "production-assets-page" not in facts.section_classes.get(section_id, set())
    ]
    page_set_ok = core_exact and not invalid_downstream
    if page_set_ok and downstream_pages:
        page_detail = (
            f"PRD core matches expected order/set: {len(expected)} pages; "
            f"valid additive Production Assets pages: {len(downstream_pages)}"
        )
    elif page_set_ok:
        page_detail = f"PRD core matches expected order/set: {len(expected)} pages; no downstream pages"
    else:
        page_detail = (
            f"expected PRD core {expected}; actual prefix {core_pages}; "
            f"invalid downstream pages {invalid_downstream}; actual pages {actual_pages}"
        )
    check(
        "generated_page_set_matches_current_render_data",
        page_set_ok,
        page_detail,
    )

    composition = document_composition_errors(data, facts)
    check(
        "document_page_composition",
        not composition,
        "required Golden prototype markers are present" if not composition else "; ".join(composition),
    )

    id_set = set(facts.ids)
    broken = sorted(set(target for target in facts.fragment_hrefs if target not in id_set))
    check("fragment_navigation_reachable", not broken, f"broken targets: {broken}" if broken else "all fragment links resolve")

    browser_title = "".join(facts.title_parts).strip()
    check(
        "browser_title_matches_project",
        bool(title) and title.lower() in html_lib.unescape(browser_title).lower(),
        f"browser title: {browser_title!r}",
    )

    status = "pass" if not errors else "fail"
    return {
        "status": status,
        "errors": errors,
        "warnings": warnings,
        "checks": checks,
        "expected_pages": expected,
    }


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
