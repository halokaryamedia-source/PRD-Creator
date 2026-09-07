from __future__ import annotations

import re
from pathlib import Path

from .core import esc
from shared.voice import PERFORMANCE_TAG_LINE_RE

PERFORMANCE_TAG_RE = re.compile(r"\[[^\[\]\r\n]+\]")
STYLE_MARKER = 'id="production-assets-style"'
SCRIPT_MARKER = 'id="production-assets-script"'
STATIC_ROOT = Path(__file__).resolve().parent / "static"


def performance_html(performance: str) -> str:
    parts: list[str] = []
    for raw in performance.splitlines():
        stripped = raw.strip()
        if not stripped:
            parts.append('<div class="voice-script-gap" aria-hidden="true"></div>')
            continue
        if PERFORMANCE_TAG_LINE_RE.fullmatch(stripped):
            tags = "".join(
                f'<span class="voice-performance-tag">{esc(tag)}</span>'
                for tag in PERFORMANCE_TAG_RE.findall(stripped)
            )
            parts.append(f'<div class="voice-performance-cues">{tags}</div>')
            continue
        parts.append(f'<div class="voice-script-line">{esc(raw)}</div>')
    return "".join(parts)


def production_assets_style() -> str:
    css = _static_text("production-assets.css")
    return f'<style id="production-assets-style">\n{css}</style>'


def production_assets_script() -> str:
    script = _static_text("production-assets.js")
    return f'<script id="production-assets-script">\n{script}</script>'


def _static_text(name: str) -> str:
    path = STATIC_ROOT / name
    if not path.is_file():
        raise ValueError(f"missing renderer static resource: {path}")
    return path.read_text(encoding="utf-8").rstrip() + "\n"


__all__ = [
    "STYLE_MARKER",
    "SCRIPT_MARKER",
    "performance_html",
    "production_assets_style",
    "production_assets_script",
]
