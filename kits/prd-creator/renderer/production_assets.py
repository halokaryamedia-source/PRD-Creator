from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT_ROOT = HERE.parent
if str(KIT_ROOT) not in sys.path:
    sys.path.insert(0, str(KIT_ROOT))

from core import esc
from shared.voice import (
    ENTRY_RE,
    PLACEHOLDER_RE,
    PERFORMANCE_TAG_LINE_RE,
    VoiceEntry,
    VoiceProduction,
    VoiceSection,
    has_initial_performance_tag,
    parse_production,
    plain_section_title,
    title_key,
)

PERFORMANCE_TAG_RE = re.compile(r"\[[^\[\]\r\n]+\]")
STYLE_MARKER = 'id="production-assets-style"'

parse_voice_production = parse_production
_has_initial_performance_tag = has_initial_performance_tag
_plain_section_title = plain_section_title
_title_key = title_key


def _voice_for(cast: dict[str, str], speaker: str) -> str:
    speaker_key = speaker.casefold()
    for cast_speaker, voice in cast.items():
        if cast_speaker.casefold() == speaker_key:
            return voice
    return "Voice selection pending"


def _performance_html(performance: str) -> str:
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

__all__ = [
    "ENTRY_RE",
    "PLACEHOLDER_RE",
    "PERFORMANCE_TAG_LINE_RE",
    "STYLE_MARKER",
    "VoiceEntry",
    "VoiceProduction",
    "VoiceSection",
    "parse_voice_production",
    "_has_initial_performance_tag",
    "_plain_section_title",
    "_title_key",
    "_voice_for",
    "_performance_html",
    "VOICE_STYLE",
    "VOICE_COPY_SCRIPT",
]
