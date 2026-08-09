#!/usr/bin/env python3
"""Mechanical Flow 4 validation for a repository-backed PRD project.

This tool checks file presence, unresolved placeholders, render-data invariants,
scoring/completion exclusivity, generated page IDs, duplicate HTML IDs, and
fragment navigation reachability. It does not judge semantic development-readiness;
that remains the role-based Flow 4 audit recorded in work/acceptance.md.
"""
from __future__ import annotations

import argparse
import html as html_lib
import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPEN_RE = re.compile(r"\b(?:TBD|TODO|FIXME|INSERT\s+(?:TEXT|VALUE)|USE\s+APPROVED\s+AMOUNT)\b|\[OPEN\]", re.I)
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class HtmlFacts(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.fragment_hrefs: list[str] = []
        self.title_parts: list[str] = []
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if data.get("id"):
            self.ids.append(str(data["id"]))
        href = data.get("href")
        if isinstance(href, str) and href.startswith("#") and len(href) > 1:
            self.fragment_hrefs.append(href[1:])
        if tag.lower() == "title":
            self._in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_parts.append(data)


def text_en(value: Any) -> str:
    if isinstance(value, dict):
        value = value.get("en") or value.get("id") or ""
    return str(value or "")


def expected_page_ids(data: dict[str, Any]) -> list[str]:
    ids = ["summary"]
    ids += [f'flow-{item["id"]}' for item in data.get("gameplay_flow", [])]
    ids += [f'global-{item["id"]}' for item in data.get("global_development", [])]
    for pkg in data.get("packages", []):
        pid = pkg["id"]
        ids += [f"dev-{pid}-requirement", f"dev-{pid}-level", f"dev-{pid}-developer"]
    return ids


def validate(project: Path) -> dict[str, Any]:
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

    doc = data.get("document")
    check("document_object", isinstance(doc, dict), "render-data.document must be an object")
    title = text_en(doc.get("title")) if isinstance(doc, dict) else ""
    check("document_title", bool(title.strip()), "document title is present")

    packages = data.get("packages")
    check("packages_array", isinstance(packages, list) and len(packages) > 0, "at least one gameplay package is required for this template profile")
    packages = packages if isinstance(packages, list) else []

    seen_pkg: set[str] = set()
    for index, pkg in enumerate(packages, 1):
        if not isinstance(pkg, dict):
            errors.append(f"package_{index}: package must be an object")
            continue
        pid = pkg.get("id")
        if not isinstance(pid, str) or not ID_RE.fullmatch(pid):
            errors.append(f"package_{index}: invalid id {pid!r}")
            continue
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
            numeric_weights = [c.get("weight") for c in components if isinstance(c, dict) and isinstance(c.get("weight"), (int, float))]
            if numeric_weights and len(numeric_weights) == len(components):
                total = sum(numeric_weights)
                if abs(total - 100.0) > 1e-9:
                    errors.append(f"package_{pid}: numeric scoring weights total {total}, expected 100")

    html_text = html_path.read_text(encoding="utf-8")
    facts = HtmlFacts()
    try:
        facts.feed(html_text)
    except Exception as exc:
        errors.append(f"html_parse: {exc}")

    duplicates = sorted(k for k, count in Counter(facts.ids).items() if count > 1)
    check("html_ids_unique", not duplicates, f"duplicate ids: {duplicates}" if duplicates else "no duplicate HTML ids")

    id_set = set(facts.ids)
    expected = expected_page_ids(data)
    missing_expected = [page_id for page_id in expected if page_id not in id_set]
    check("expected_pages_present", not missing_expected, f"missing page ids: {missing_expected}" if missing_expected else f"{len(expected)} expected pages present")

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
