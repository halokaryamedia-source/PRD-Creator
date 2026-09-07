from __future__ import annotations

import re

from .core import esc
from shared.voice import PERFORMANCE_TAG_LINE_RE

PERFORMANCE_TAG_RE = re.compile(r"\[[^\[\]\r\n]+\]")
STYLE_MARKER = 'id="production-assets-style"'


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


VOICE_STYLE = r'''<style id="production-assets-style">
.production-assets-nav .nav-submenu a{min-width:0;white-space:normal;overflow-wrap:anywhere}
.production-assets-nav .nav-submenu a small{display:block;margin-top:2px;white-space:normal;overflow-wrap:anywhere}
.production-assets-objective-name{min-width:0;white-space:normal;overflow-wrap:anywhere}
.voice-performance-cues{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 8px}
</style>'''

VOICE_COPY_SCRIPT = ""

__all__ = ["STYLE_MARKER", "performance_html", "VOICE_STYLE", "VOICE_COPY_SCRIPT"]
