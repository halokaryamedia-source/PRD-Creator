#!/usr/bin/env python3
"""Validate rendered Production Document Builder HTML and write audit reports."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import threading
from contextlib import contextmanager
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from collections import Counter
from pathlib import Path
from typing import Any

import yaml
from bs4 import BeautifulSoup

from renderer_lib import PLACEHOLDER_PATTERN, canonical_data_hash, read_data, write_yaml


def expected_page_ids(content: dict[str, Any]) -> list[str]:
    profile = content.get("document", {}).get("profile")
    ids: list[str] = []
    if profile in {"complete_game_map", "multi_stage_game", "single_gameplay"}:
        ids.append("summary")
        ids.extend(f"flow-{item['id']}" for item in content.get("gameplay_flow", []) if isinstance(item, dict) and item.get("id"))
        dev = content.get("development", {})
        if profile == "complete_game_map":
            ids.extend(key.replace("_", "-") for key in ("development_overview", "game_system", "data_and_reset", "gameplay_development"))
            packages = dev.get("packages", [])
        elif profile == "multi_stage_game":
            ids.extend(key.replace("_", "-") for key in ("session_system", "global_scoring", "data_and_leaderboard", "reset_system"))
            packages = dev.get("stage_packages", [])
        else:
            packages = [dev.get("gameplay_package", {})]
        for package in packages:
            if isinstance(package, dict) and package.get("id"):
                phase = f"dev-{package['id']}"
                ids.extend([f"{phase}-gameplay", f"{phase}-level", f"{phase}-developer"])
    elif profile == "game_system_module":
        ids.extend(["summary", "system-flow"])
        ids.extend(key.replace("_", "-") for key in ("architecture", "requirements", "configuration", "integration", "data_handling", "error_handling", "lifecycle", "usage_guide"))
    elif profile == "specialized_document":
        ids.append("summary")
    return ids


def collect_term_refs(node: Any) -> set[str]:
    result: set[str] = set()
    if isinstance(node, dict):
        terms = node.get("terms")
        if isinstance(terms, list):
            result.update(item for item in terms if isinstance(item, str))
        for key, value in node.items():
            if key != "terms":
                result.update(collect_term_refs(value))
    elif isinstance(node, list):
        for value in node:
            result.update(collect_term_refs(value))
    return result


def static_audit(html_path: Path, content: dict[str, Any] | None, glossary: dict[str, Any] | None) -> tuple[dict[str, Any], list[str]]:
    text = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(text, "html.parser")
    notes: list[str] = []

    all_ids = [node.get("id") for node in soup.select("[id]") if node.get("id")]
    duplicates = sum(count - 1 for count in Counter(all_ids).values() if count > 1)
    page_nodes = soup.select("section.sheet[id]")
    page_ids = [node.get("id") for node in page_nodes]
    empty_pages = sum(1 for node in page_nodes if len(node.get_text(" ", strip=True)) < 30)

    link_targets: list[str] = []
    for node in soup.select('a[href^="#"], [data-target], [data-section-target]'):
        target = node.get("data-target") or node.get("data-section-target")
        if not target and node.get("href", "").startswith("#"):
            target = node.get("href")[1:]
        if target:
            link_targets.append(target)
    broken = sorted({target for target in link_targets if target not in set(all_ids)})
    reachable = set(link_targets)
    unreachable = [page_id for page_id in page_ids if page_id not in reachable]

    i18n_nodes = soup.select(".i18n-text")
    id_missing = sum(1 for node in i18n_nodes if not node.get("data-id"))
    en_missing = sum(1 for node in i18n_nodes if not node.get("data-en"))
    placeholders = len(PLACEHOLDER_PATTERN.findall(text))

    meta = {node.get("name"): node.get("content", "") for node in soup.select("meta[name]")}
    profile = meta.get("document-profile", "complete_game_map")
    expected = expected_page_ids(content) if content else page_ids
    missing_required = [page_id for page_id in expected if page_id not in page_ids]
    page_order_valid = [page_id for page_id in page_ids if page_id in expected] == [page_id for page_id in expected if page_id in page_ids]

    content_hash_matches = True
    if content:
        content_hash_matches = meta.get("content-sha256") == canonical_data_hash(content)
        if not content_hash_matches:
            notes.append("Rendered content hash does not match project-content input.")

    glossary_terms = glossary.get("terms", []) if glossary else []
    glossary_ids = {item.get("id") for item in glossary_terms if isinstance(item, dict) and item.get("id")}
    used_terms = collect_term_refs(content) if content else set()
    unused_terms = glossary_ids - used_terms
    missing_term_refs = used_terms - glossary_ids

    if duplicates:
        notes.append(f"Duplicate element IDs: {duplicates}")
    if broken:
        notes.append(f"Broken navigation targets: {', '.join(broken)}")
    if unreachable:
        notes.append(f"Unreachable pages: {', '.join(unreachable)}")
    if empty_pages:
        notes.append(f"Empty pages: {empty_pages}")
    if missing_required:
        notes.append(f"Missing required pages: {', '.join(missing_required)}")
    if placeholders:
        notes.append(f"Unresolved placeholders: {placeholders}")
    if id_missing or en_missing:
        notes.append(f"Missing translations in rendered nodes: ID={id_missing}, EN={en_missing}")
    if missing_term_refs:
        notes.append(f"Unknown glossary references: {', '.join(sorted(missing_term_refs))}")

    return {
        "meta": meta,
        "profile": profile,
        "pages_created": len(page_nodes),
        "sidebar_links": len(soup.select('.doc-sidebar a[data-target], .doc-sidebar a[href^="#"]')),
        "empty_pages": empty_pages,
        "missing_required_sections": len(missing_required),
        "unresolved_placeholders": placeholders,
        "content_hash_matches": content_hash_matches,
        "id_missing": id_missing,
        "en_missing": en_missing,
        "terms_defined": len(glossary_ids),
        "unused_terms": len(unused_terms),
        "unmatched_critical_terms": len(missing_term_refs),
        "duplicate_ids": duplicates,
        "broken_links": len(broken),
        "unreachable_pages": len(unreachable),
        "page_order_valid": page_order_valid,
        "page_ids": page_ids,
    }, notes




@contextmanager
def local_file_server(directory: Path):
    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self, format: str, *args: Any) -> None:
            return

    handler = lambda *args, **kwargs: QuietHandler(*args, directory=str(directory), **kwargs)
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_address[1]}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def browser_audit(html_path: Path, screenshots_dir: Path | None = None) -> tuple[dict[str, Any], list[str], dict[str, Any]]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise RuntimeError("Playwright is not installed.") from exc

    statuses = {
        "desktop_16_9": "not_run",
        "laptop": "not_run",
        "tablet": "not_run",
        "mobile": "not_run",
        "zoom_125": "not_run",
        "zoom_150": "not_run",
    }
    print_result = {"status": "not_run", "terms_expanded": False, "controls_hidden": False}
    notes: list[str] = []
    details: dict[str, Any] = {"console_errors": [], "interactions": {}}
    html_source = html_path.read_text(encoding="utf-8")

    if screenshots_dir:
        screenshots_dir.mkdir(parents=True, exist_ok=True)

    def overflow_ok(page) -> bool:
        return bool(page.evaluate("document.documentElement.scrollWidth <= document.documentElement.clientWidth + 2"))

    with sync_playwright() as p:
        chromium_path = os.environ.get("CHROMIUM_PATH") or shutil.which("chromium") or shutil.which("chromium-browser")
        launch_args: dict[str, Any] = {
            "headless": True,
            "args": ["--no-sandbox", "--disable-dev-shm-usage"],
        }
        if chromium_path:
            launch_args["executable_path"] = chromium_path
        browser = p.chromium.launch(**launch_args)
        viewports = {
            "desktop_16_9": {"width": 1920, "height": 1080},
            "laptop": {"width": 1366, "height": 768},
            "tablet": {"width": 1024, "height": 768},
            "mobile": {"width": 390, "height": 844},
        }
        for key, viewport in viewports.items():
            context = browser.new_context(viewport=viewport)
            page = context.new_page()
            page.on("console", lambda msg: details["console_errors"].append(msg.text) if msg.type == "error" else None)
            page.set_content(html_source, wait_until="load")
            page.wait_for_timeout(250)
            statuses[key] = "passed" if overflow_ok(page) else "failed"
            if screenshots_dir and key in {"desktop_16_9", "mobile"}:
                page.screenshot(path=str(screenshots_dir / f"{key}.png"), full_page=False)
            context.close()

        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()
        page.on("console", lambda msg: details["console_errors"].append(msg.text) if msg.type == "error" else None)
        page.set_content(html_source, wait_until="load")
        page.wait_for_timeout(300)

        if page.locator('[data-language-option="id"]').count():
            page.locator('[data-language-option="id"]').click()
            details["interactions"]["language_id"] = page.locator("html").get_attribute("lang") == "id"
            page.locator('[data-language-option="en"]').click()
            details["interactions"]["language_en"] = page.locator("html").get_attribute("lang") == "en"
        else:
            details["interactions"]["language_switch"] = "not_applicable"

        if page.locator("#themeModeSwitch").count():
            page.locator("#themeModeSwitch").click()
            details["interactions"]["theme"] = page.locator("body").evaluate("el => el.classList.contains('theme-dark')")

        if page.locator('[data-mode-label="clean"]').count():
            page.locator('[data-mode-label="clean"]').click()
            clean_ok = page.locator("body").evaluate("el => el.classList.contains('view-clean')")
            page.locator('[data-mode-label="professional"]').click()
            professional_ok = page.locator("body").evaluate("el => el.classList.contains('view-professional')")
            details["interactions"]["view_mode"] = clean_ok and professional_ok

        if page.locator("#sidebarToggle").count():
            page.locator("#sidebarToggle").click()
            details["interactions"]["sidebar_collapse"] = page.locator("body").evaluate("el => el.classList.contains('sidebar-collapsed')")
            page.locator("#sidebarToggle").click()

        if page.locator("details[data-terms-used]").count():
            detail = page.locator("details[data-terms-used]").first
            detail.locator("summary").click()
            details["interactions"]["terms_used"] = detail.evaluate("el => el.open")

        page.wait_for_timeout(250)
        tooltip_instances = page.locator(".glossary-term").count()
        details["tooltip_instances"] = tooltip_instances
        if tooltip_instances:
            term = page.locator(".glossary-term").first
            term.click()
            details["interactions"]["tooltip"] = page.locator("#globalGlossaryTooltip").evaluate("el => el.classList.contains('is-visible')")

        for zoom_key, factor in (("zoom_125", 1.25), ("zoom_150", 1.5)):
            page.evaluate(f"document.body.style.zoom='{factor}'")
            page.wait_for_timeout(100)
            statuses[zoom_key] = "passed" if overflow_ok(page) else "failed"
        page.evaluate("document.body.style.zoom='1'")

        page.emulate_media(media="print")
        page.wait_for_timeout(100)
        terms_expanded = True
        if page.locator(".terms-used-panel").count():
            terms_expanded = page.locator(".terms-used-panel").first.evaluate("el => getComputedStyle(el).display !== 'none'")
        controls_hidden = True
        if page.locator(".doc-sidebar").count():
            controls_hidden = page.locator(".doc-sidebar").evaluate("el => getComputedStyle(el).display === 'none'")
        print_result = {"status": "passed" if terms_expanded and controls_hidden else "failed", "terms_expanded": terms_expanded, "controls_hidden": controls_hidden}
        context.close()

        context = browser.new_context(viewport={"width": 390, "height": 844})
        page = context.new_page()
        page.set_content(html_source, wait_until="load")
        if page.locator("#mobileSidebarButton").count():
            page.locator("#mobileSidebarButton").click()
            opened = page.locator("body").evaluate("el => el.classList.contains('sidebar-mobile-open')")
            page.keyboard.press("Escape")
            closed = not page.locator("body").evaluate("el => el.classList.contains('sidebar-mobile-open')")
            details["interactions"]["mobile_drawer"] = opened and closed
        context.close()
        browser.close()

    if details["console_errors"]:
        notes.append(f"Browser console errors: {len(details['console_errors'])}")
    for key, status in statuses.items():
        if status == "failed":
            notes.append(f"Responsive check failed: {key}")
    if print_result["status"] == "failed":
        notes.append("Print validation failed.")
    failed_interactions = [key for key, value in details["interactions"].items() if value is False]
    if failed_interactions:
        notes.append(f"Interaction checks failed: {', '.join(failed_interactions)}")
    return statuses, notes, {"print": print_result, **details}


def report_status(
    static: dict[str, Any],
    responsive: dict[str, str],
    print_data: dict[str, Any],
    browser_details: dict[str, Any],
    equivalence_audit: str,
) -> str:
    blocking_static = any(
        [
            static["empty_pages"],
            static["missing_required_sections"],
            static["unresolved_placeholders"],
            static["id_missing"],
            static["en_missing"],
            static["unmatched_critical_terms"],
            static["duplicate_ids"],
            static["broken_links"],
            static["unreachable_pages"],
            not static["page_order_valid"],
            not static["content_hash_matches"],
        ]
    )
    browser_failed = any(value == "failed" for value in responsive.values()) or print_data.get("status") == "failed"
    browser_failed = browser_failed or bool(browser_details.get("console_errors")) or any(value is False for value in browser_details.get("interactions", {}).values())
    language_blocked = equivalence_audit != "passed"
    return "needs_revision" if blocking_static or browser_failed or language_blocked else "success"


def audit_markdown(html_path: Path, report: dict[str, Any], notes: list[str], browser_details: dict[str, Any]) -> str:
    status = report["render"]["status"]
    lines = [
        "# Final HTML Audit",
        "",
        f"- **Artifact:** `{html_path.name}`",
        f"- **Status:** `{status}`",
        f"- **Profile:** `{report['render']['profile']}`",
        f"- **Pages:** {report['render']['pages_created']}",
        f"- **Critical structural blockers:** {0 if status == 'success' else len(notes)}",
        "",
        "## Structural Results",
        "",
        f"- Duplicate IDs: {report['structure']['duplicate_ids']}",
        f"- Broken links: {report['structure']['broken_links']}",
        f"- Unreachable pages: {report['structure']['unreachable_pages']}",
        f"- Empty pages: {report['render']['empty_pages']}",
        f"- Unresolved placeholders: {report['content']['unresolved_placeholders']}",
        f"- Missing EN values: {report['languages']['en_missing']}",
        f"- Missing ID values: {report['languages']['id_missing']}",
        f"- Translation equivalence audit: {report['languages']['equivalence_audit']}",
        "",
        "## Browser Results",
        "",
    ]
    lines.extend(f"- {key}: {value}" for key, value in report["responsive"].items())
    lines.extend(
        [
            f"- Print: {report['print']['status']}",
            f"- Tooltip instances: {report['glossary']['tooltip_instances']}",
            f"- Console errors: {len(browser_details.get('console_errors', []))}",
            "",
            "## Interaction Checks",
            "",
        ]
    )
    for key, value in browser_details.get("interactions", {}).items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Findings", ""])
    if notes:
        lines.extend(f"- {note}" for note in notes)
    else:
        lines.append("- No Critical or Major HTML findings.")
    lines.extend(["", "## Delivery Gate", ""])
    lines.append("Passed." if status == "success" else "Blocked until the findings above are resolved.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path)
    parser.add_argument("--content", type=Path)
    parser.add_argument("--glossary", type=Path)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--audit-md", type=Path)
    parser.add_argument("--browser", action="store_true")
    parser.add_argument("--screenshots-dir", type=Path)
    parser.add_argument(
        "--equivalence-audit",
        choices=("not_run", "passed", "failed"),
        default="not_run",
        help="Result of a separate semantic EN/ID equivalence review. Presence checks alone do not prove equivalent meaning.",
    )
    args = parser.parse_args()

    try:
        content = read_data(args.content) if args.content else None
        glossary = read_data(args.glossary) if args.glossary else {"terms": []}
        static, notes = static_audit(args.html, content, glossary)
        responsive = {key: "not_run" for key in ("desktop_16_9", "laptop", "tablet", "mobile", "zoom_125", "zoom_150")}
        browser_details: dict[str, Any] = {"console_errors": [], "interactions": {}, "tooltip_instances": 0}
        print_data = {"status": "not_run", "terms_expanded": False, "controls_hidden": False}
        if args.browser:
            responsive, browser_notes, result = browser_audit(args.html, args.screenshots_dir)
            notes.extend(browser_notes)
            print_data = result.pop("print")
            browser_details = result

        status = report_status(static, responsive, print_data, browser_details, args.equivalence_audit)
        meta = static["meta"]
        report = {
            "render": {
                "status": status,
                "profile": static["profile"],
                "pages_created": static["pages_created"],
                "sidebar_links": static["sidebar_links"],
                "empty_pages": static["empty_pages"],
                "output_html": str(args.html),
            },
            "content": {
                "missing_required_sections": static["missing_required_sections"],
                "unresolved_placeholders": static["unresolved_placeholders"],
                "content_hash_matches": static["content_hash_matches"],
            },
            "languages": {
                "id_missing": static["id_missing"],
                "en_missing": static["en_missing"],
                "equivalence_audit": args.equivalence_audit if not static["id_missing"] and not static["en_missing"] else "failed",
            },
            "glossary": {
                "terms_defined": static["terms_defined"],
                "tooltip_instances": int(browser_details.get("tooltip_instances", 0)),
                "unused_terms": static["unused_terms"],
                "unmatched_critical_terms": static["unmatched_critical_terms"],
            },
            "structure": {
                "duplicate_ids": static["duplicate_ids"],
                "broken_links": static["broken_links"],
                "unreachable_pages": static["unreachable_pages"],
                "page_order_valid": static["page_order_valid"],
            },
            "responsive": responsive,
            "print": print_data,
            "versions": {
                "content": meta.get("content-version", "0.0"),
                "template": meta.get("template-version", "0.0"),
                "schema": meta.get("schema-version", "0.0"),
                "golden_sample": meta.get("golden-sample", "aftershock-1.0"),
                "html": meta.get("html-version", "0.0"),
            },
        }
        write_yaml(args.report, report)
        audit_path = args.audit_md or args.report.with_name("html-audit.md")
        audit_path.write_text(audit_markdown(args.html, report, notes, browser_details), encoding="utf-8")
        print(json.dumps({"status": status, "report": str(args.report), "audit": str(audit_path), "findings": notes}, ensure_ascii=False, indent=2))
        return 0 if status == "success" else 1
    except (OSError, RuntimeError, ValueError, yaml.YAMLError) as exc:
        print(f"HTML AUDIT FAILED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
