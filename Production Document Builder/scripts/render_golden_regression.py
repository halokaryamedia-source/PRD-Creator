#!/usr/bin/env python3
"""Render the locked AFTERSHOCK Golden Sample exactly, with structural inventory validation.

This is a regression renderer, not the semantic renderer used for new projects.
It proves that the approved V1.8/Golden Sample can be reproduced without any
visual, structural, content, CSS, JavaScript, or interaction changes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import yaml
from bs4 import BeautifulSoup


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_inventory(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise RuntimeError("Golden Sample inventory root must be an object.")
    return data


def validate_inventory(inventory: dict, html_bytes: bytes) -> dict:
    document = inventory.get("document", {})
    if document.get("id") != "aftershock":
        raise RuntimeError("Golden regression supports only document.id=aftershock.")
    if document.get("profile") != "complete_game_map":
        raise RuntimeError("Golden regression requires profile=complete_game_map.")
    if str(document.get("golden_sample_version")) != "1.0":
        raise RuntimeError("Golden regression requires golden_sample_version=1.0.")

    soup = BeautifulSoup(html_bytes.decode("utf-8"), "html.parser")
    actual_ids = [section.get("id") for section in soup.select("section.sheet[id]")]
    expected_ids = [page.get("id") for page in inventory.get("pages", [])]
    if actual_ids != expected_ids:
        raise RuntimeError(
            "Golden inventory page order does not match the locked HTML.\n"
            f"Expected: {expected_ids}\nActual: {actual_ids}"
        )

    hierarchy_ids: list[str] = []
    for group in inventory.get("hierarchy", []):
        hierarchy_ids.extend(group.get("page_ids", []))
    if hierarchy_ids != expected_ids:
        raise RuntimeError("Golden hierarchy page_ids do not match the page inventory order.")

    benchmark_ids = inventory.get("content_benchmark", {}).get("page_ids", [])
    missing_benchmark = [page_id for page_id in benchmark_ids if page_id not in actual_ids]
    if missing_benchmark:
        raise RuntimeError(f"Missing content benchmark pages: {missing_benchmark}")

    duplicate_ids = []
    all_ids = [node.get("id") for node in soup.select("[id]")]
    seen: set[str] = set()
    for node_id in all_ids:
        if node_id in seen and node_id not in duplicate_ids:
            duplicate_ids.append(node_id)
        seen.add(node_id)
    if duplicate_ids:
        raise RuntimeError(f"Locked Golden Sample contains duplicate IDs: {duplicate_ids}")

    return {
        "pages": len(actual_ids),
        "page_ids": actual_ids,
        "benchmark_pages": benchmark_ids,
        "sidebar_links": len(soup.select("#docSidebar a[href^='#']")),
        "terms_sections": len(soup.select("details.terms-used-collapsible")),
        "styles": len(soup.find_all("style")),
        "scripts": len(soup.find_all("script")),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    package_root = Path(__file__).resolve().parents[1]
    parser.add_argument(
        "--inventory",
        type=Path,
        default=package_root / "golden-sample" / "aftershock-content.yaml",
    )
    parser.add_argument(
        "--golden-html",
        type=Path,
        default=package_root / "golden-sample" / "aftershock-golden-sample-v1.0.html",
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    try:
        if not args.inventory.is_file():
            raise RuntimeError(f"Golden inventory not found: {args.inventory}")
        if not args.golden_html.is_file():
            raise RuntimeError(f"Locked Golden Sample not found: {args.golden_html}")

        inventory = load_inventory(args.inventory)
        source_bytes = args.golden_html.read_bytes()
        metrics = validate_inventory(inventory, source_bytes)

        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(source_bytes)

        output_bytes = args.output.read_bytes()
        source_hash = sha256_bytes(source_bytes)
        output_hash = sha256_bytes(output_bytes)
        if output_hash != source_hash or output_bytes != source_bytes:
            raise RuntimeError("Generated output is not byte-identical to the locked Golden Sample.")

        result = {
            "status": "passed",
            "mode": "golden_sample_exact_regression",
            "source": str(args.golden_html),
            "inventory": str(args.inventory),
            "output": str(args.output),
            "source_sha256": source_hash,
            "output_sha256": output_hash,
            "byte_identical": True,
            **metrics,
        }
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(yaml.safe_dump(result, sort_keys=False, allow_unicode=True), encoding="utf-8")
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, RuntimeError, UnicodeDecodeError, yaml.YAMLError) as exc:
        print(f"GOLDEN REGRESSION FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
