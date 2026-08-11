#!/usr/bin/env python3
"""Render PRD data through the exact approved Golden presentation shell."""
from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _engine  # noqa: E402

GOLDEN_SPEC_MARKER = "aftershock-v0.2"
SAMPLE_META_NAMES = (
    "golden-sample-id",
    "golden-sample-version",
    "source-document",
    "template-extraction-version",
)
STORAGE_KEYS = {
    "aftershock-document-theme": "document-theme",
    "aftershock-document-view": "document-view",
    "aftershock-document-language": "document-language",
    "aftershock-sidebar-collapsed": "sidebar-collapsed",
}


def _prepare_golden_template(template: Path, render_data: Path) -> tuple[str, str]:
    source = template.read_text(encoding="utf-8")
    data = json.loads(render_data.read_text(encoding="utf-8"))
    title = _engine.txt(data.get("document", {}).get("title", ""))["en"]
    namespace = _engine.slug(title)

    for meta_name in SAMPLE_META_NAMES:
        source = re.sub(
            rf'<meta\b[^>]*\bname=["\']{re.escape(meta_name)}["\'][^>]*>\s*',
            "",
            source,
            flags=re.I,
        )

    for old_key, suffix in STORAGE_KEYS.items():
        source = source.replace(old_key, f"prd-{namespace}-{suffix}")
    return source, namespace


def render(template: Path, render_data: Path, output: Path) -> None:
    source = template.read_text(encoding="utf-8")
    if _engine.STORAGE_PREFIX_TOKEN in source:
        _engine.render(template, render_data, output)
        return

    prepared, _namespace = _prepare_golden_template(template, render_data)
    if prepared.count(GOLDEN_SPEC_MARKER) != 1:
        raise ValueError(
            "Approved Golden template must contain exactly one canonical specification marker"
        )

    previous_marker = _engine.STORAGE_PREFIX_TOKEN
    try:
        _engine.STORAGE_PREFIX_TOKEN = GOLDEN_SPEC_MARKER
        with tempfile.TemporaryDirectory(prefix="prd-golden-") as tmp:
            prepared_path = Path(tmp) / "approved-document.html"
            prepared_path.write_text(prepared, encoding="utf-8")
            _engine.render(prepared_path, render_data, output)
    finally:
        _engine.STORAGE_PREFIX_TOKEN = previous_marker


def main() -> int:
    default_template = HERE.parent / "template" / "approved-document.html"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("render_data", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--template", type=Path, default=default_template)
    args = parser.parse_args()
    try:
        render(args.template, args.render_data, args.output)
        print(args.output)
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"PRD RENDER FAILED: {exc}", file=sys.stderr)
        return 2


validate = _engine.validate
apply_result_summaries = _engine.apply_result_summaries


if __name__ == "__main__":
    raise SystemExit(main())
