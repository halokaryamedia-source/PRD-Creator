#!/usr/bin/env python3
"""Package a rendered Production Document Builder output as a ZIP."""
from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

import yaml


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--zip", dest="zip_path", type=Path, required=True)
    parser.add_argument("--screenshots-dir", type=Path)
    parser.add_argument("--root-name")
    args = parser.parse_args()

    for path in (args.html, args.report, args.audit):
        if not path.is_file():
            raise SystemExit(f"Missing package input: {path}")

    report = yaml.safe_load(args.report.read_text(encoding="utf-8"))
    report.setdefault("render", {})["output_html"] = args.html.name
    report["render"]["output_zip"] = args.zip_path.name
    args.report.write_text(yaml.safe_dump(report, sort_keys=False, allow_unicode=True), encoding="utf-8")

    args.zip_path.parent.mkdir(parents=True, exist_ok=True)
    root = args.root_name or args.html.stem
    entries: list[tuple[Path, str]] = [
        (args.html, f"{root}/{args.html.name}"),
        (args.report, f"{root}/{args.report.name}"),
        (args.audit, f"{root}/{args.audit.name}"),
    ]
    if args.screenshots_dir and args.screenshots_dir.is_dir():
        for path in sorted(args.screenshots_dir.rglob("*")):
            if path.is_file():
                entries.append((path, f"{root}/screenshots/{path.relative_to(args.screenshots_dir).as_posix()}"))

    with zipfile.ZipFile(args.zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source, target in entries:
            archive.write(source, target)

    result = {
        "zip": str(args.zip_path),
        "sha256": sha256(args.zip_path),
        "files": len(entries),
        "root": root,
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
