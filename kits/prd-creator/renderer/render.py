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
KIT_ROOT = HERE.parent
if __package__ in (None, ""):
    if str(KIT_ROOT) not in sys.path:
        sys.path.insert(0, str(KIT_ROOT))
    from renderer import prd_render_engine as engine
    from renderer import production_assets_compositor as production_assets
else:
    from . import prd_render_engine as engine
    from . import production_assets_compositor as production_assets

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


def _prepare_golden_template(template: Path, render_data: Path) -> str:
    source = template.read_text(encoding="utf-8")
    data = json.loads(render_data.read_text(encoding="utf-8"))
    title = engine.txt(data.get("document", {}).get("title", ""))["en"]
    namespace = engine.slug(title)

    for meta_name in SAMPLE_META_NAMES:
        source = re.sub(
            rf'<meta\b[^>]*\bname=["\']{re.escape(meta_name)}["\'][^>]*>\s*',
            "",
            source,
            flags=re.I,
        )
    for old_key, suffix in STORAGE_KEYS.items():
        source = source.replace(old_key, f"prd-{namespace}-{suffix}")
    return source


def _augment_production_assets(render_data: Path, output: Path) -> None:
    production_assets.augment_project_html(
        render_data,
        output,
        render_data.parent / "voice-production.md",
    )


def render(template: Path, render_data: Path, output: Path) -> None:
    source = template.read_text(encoding="utf-8")
    if engine.STORAGE_PREFIX_TOKEN in source:
        engine.render(template, render_data, output)
        _augment_production_assets(render_data, output)
        return

    prepared = _prepare_golden_template(template, render_data)
    if prepared.count(GOLDEN_SPEC_MARKER) != 1:
        raise ValueError("Approved Golden template must contain exactly one canonical specification marker")
    prepared = prepared.replace(GOLDEN_SPEC_MARKER, engine.STORAGE_PREFIX_TOKEN, 1)
    with tempfile.TemporaryDirectory(prefix="prd-golden-") as tmp:
        prepared_path = Path(tmp) / "runtime-template.html"
        prepared_path.write_text(prepared, encoding="utf-8")
        engine.render(prepared_path, render_data, output)
    _augment_production_assets(render_data, output)


def main() -> int:
    default_template = KIT_ROOT / "template" / "runtime-template.html"
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


validate = engine.validate


if __name__ == "__main__":
    raise SystemExit(main())
