from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ENTRY_RE = re.compile(r"^###\s+([A-Za-z0-9][A-Za-z0-9-]*)\s+[—-]\s+(.+?)\s*$")
PLACEHOLDER_RE = re.compile(r"\b(?:TBD|TODO|FIXME)\b|\[OPEN\]", re.I)
PERFORMANCE_TAG_LINE_RE = re.compile(r"^(?:\[[^\[\]\r\n]+\]\s*)+$")
SECTION_PREFIX_RE = re.compile(r"^\s*\d+\.\s*")
OWNER_RE = re.compile(r"^(?:Owner ID|Owner):\s*(\S+)\s*$", re.I)


@dataclass(frozen=True)
class VoiceRequirement:
    voice_id: str
    title: str
    voice_type: str
    function: str
    speaker: str
    channel: str
    trigger: str
    must_communicate: tuple[str, ...] = ()


@dataclass(frozen=True)
class VoiceEntry:
    voice_id: str
    title: str
    voice_type: str
    speaker: str
    duration: str
    performance: str


@dataclass(frozen=True)
class VoiceSection:
    owner_id: str
    title: str
    entries: tuple[VoiceEntry, ...]


@dataclass(frozen=True)
class VoiceProduction:
    cast: dict[str, str]
    sections: tuple[VoiceSection, ...]


def has_initial_performance_tag(performance: str) -> bool:
    first = next((line.strip() for line in performance.splitlines() if line.strip()), "")
    return bool(first and PERFORMANCE_TAG_LINE_RE.fullmatch(first))


def plain_section_title(value: str) -> str:
    return SECTION_PREFIX_RE.sub("", value).strip()


def title_key(value: str) -> str:
    return plain_section_title(value).replace("’", "'").replace("`", "'").casefold().strip()


def _requirement_blocks(path: Path) -> list[tuple[str, str, dict[str, str], tuple[str, ...]]]:
    text = path.read_text(encoding="utf-8")
    if PLACEHOLDER_RE.search(text):
        raise ValueError("Voice requirements contain unresolved placeholders")
    result: list[tuple[str, str, dict[str, str], tuple[str, ...]]] = []
    current_id: str | None = None
    current_title = ""
    fields: dict[str, str] = {}
    must: list[str] = []
    list_mode: str | None = None

    def flush() -> None:
        nonlocal current_id, current_title, fields, must, list_mode
        if current_id is not None:
            result.append((current_id, current_title, fields, tuple(must)))
        current_id = None
        current_title = ""
        fields = {}
        must = []
        list_mode = None

    for raw in text.splitlines():
        line = raw.rstrip()
        match = ENTRY_RE.match(line)
        if match:
            flush()
            current_id = match.group(1)
            current_title = match.group(2).strip()
            continue
        if current_id is None:
            continue
        if line.startswith("- Must communicate:"):
            list_mode = "must"
            continue
        if line.startswith("- Must not add/repeat:") or line.startswith("- Source refs:"):
            list_mode = None
            continue
        if list_mode == "must" and re.match(r"^\s{2,}-\s+", line):
            must.append(re.sub(r"^\s{2,}-\s+", "", line).strip())
            continue
        if line.startswith("- ") and ":" in line:
            key, value = line[2:].split(":", 1)
            fields[key.strip()] = value.strip()
            list_mode = None
    flush()
    if not result:
        raise ValueError("No Voice IDs found in requirements")
    ids = [voice_id for voice_id, _, _, _ in result]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate Voice ID in requirements")
    return result


def parse_requirement_functions(path: Path) -> dict[str, str]:
    functions: dict[str, str] = {}
    for voice_id, _, fields, _ in _requirement_blocks(path):
        function = fields.get("Function", "").strip()
        if not function:
            raise ValueError(
                f"Voice requirement Function is required for Production Assets presentation: {voice_id}"
            )
        functions[voice_id] = function
    return functions


def parse_requirements(path: Path, *, require_trigger: bool = False) -> dict[str, VoiceRequirement]:
    out: dict[str, VoiceRequirement] = {}
    for voice_id, title, fields, must in _requirement_blocks(path):
        required = {
            "Type": fields.get("Type", ""),
            "Function": fields.get("Function", ""),
            "Speaker": fields.get("Speaker", ""),
            "Channel": fields.get("Channel", ""),
        }
        if require_trigger:
            required["Trigger"] = fields.get("Trigger", "")
        missing = [key for key, value in required.items() if not value]
        if missing:
            raise ValueError(f"{voice_id} missing requirement metadata: {', '.join(missing)}")
        out[voice_id] = VoiceRequirement(
            voice_id=voice_id,
            title=title,
            voice_type=required["Type"],
            function=required["Function"],
            speaker=required["Speaker"],
            channel=required["Channel"],
            trigger=fields.get("Trigger", ""),
            must_communicate=must,
        )
    return out


def parse_production(path: Path) -> VoiceProduction:
    text = path.read_text(encoding="utf-8")
    if PLACEHOLDER_RE.search(text):
        raise ValueError("Voice Production contains an unresolved placeholder.")
    lines = text.splitlines()
    cast: dict[str, str] = {}
    section_titles: list[str] = []
    section_owner: dict[str, str] = {}
    section_entries: dict[str, list[VoiceEntry]] = {}
    current_section: str | None = None
    in_cast = False
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()
        if current_section is None and line.strip() == "Voice Cast:":
            in_cast = True
            i += 1
            continue
        if current_section is None and in_cast:
            if line.startswith("- "):
                payload = line[2:].strip()
                if ":" not in payload:
                    raise ValueError("Voice Cast entries must use '- <Speaker>: <ElevenLabs voice>'.")
                speaker, voice = (part.strip() for part in payload.split(":", 1))
                if not speaker or not voice:
                    raise ValueError("Voice Cast requires a non-empty Speaker and ElevenLabs voice.")
                if any(existing.casefold() == speaker.casefold() for existing in cast):
                    raise ValueError(f"Duplicate Voice Cast speaker: {speaker}")
                cast[speaker] = voice
                i += 1
                continue
            if line.strip():
                in_cast = False

        if line.startswith("## "):
            current_section = line[3:].strip()
            if not current_section:
                raise ValueError("Voice Production section title cannot be empty.")
            if current_section in section_entries:
                raise ValueError(f"Duplicate Voice Production section: {current_section}")
            section_titles.append(current_section)
            section_entries[current_section] = []
            section_owner[current_section] = ""
            in_cast = False
            i += 1
            continue

        if current_section is not None and (owner_match := OWNER_RE.match(line)):
            owner_id = owner_match.group(1).strip()
            if section_entries[current_section]:
                raise ValueError(f"Owner ID for Voice section {current_section} must appear before Voice entries")
            if section_owner[current_section]:
                raise ValueError(f"Duplicate Owner ID in Voice section: {current_section}")
            section_owner[current_section] = owner_id
            i += 1
            continue

        match = ENTRY_RE.match(line)
        if match:
            if current_section is None:
                raise ValueError(f"Voice entry {match.group(1)} appears before a gameplay section.")
            if not section_owner[current_section]:
                raise ValueError(f"Voice section {current_section} requires Owner ID before Voice entries")
            voice_id = match.group(1)
            title = match.group(2).strip()
            voice_type = speaker = duration = performance = ""
            i += 1
            while i < len(lines):
                meta = lines[i].rstrip()
                if meta.startswith("Type:"):
                    voice_type = meta.split(":", 1)[1].strip()
                    i += 1
                    continue
                if meta.startswith("Speaker:"):
                    speaker = meta.split(":", 1)[1].strip()
                    i += 1
                    continue
                if meta.startswith("Estimated Duration:"):
                    duration = meta.split(":", 1)[1].strip()
                    i += 1
                    continue
                if meta.strip() == "```performance":
                    i += 1
                    body: list[str] = []
                    while i < len(lines) and lines[i].strip() != "```":
                        body.append(lines[i].rstrip())
                        i += 1
                    if i >= len(lines):
                        raise ValueError(f"Unclosed performance block for {voice_id}.")
                    performance = "\n".join(body).strip()
                    i += 1
                    break
                if meta.startswith("### ") or meta.startswith("## "):
                    break
                i += 1
            missing = [
                label
                for label, value in {
                    "Type": voice_type,
                    "Speaker": speaker,
                    "Estimated Duration": duration,
                    "Performance Script": performance,
                }.items()
                if not value
            ]
            if missing:
                raise ValueError(f"{voice_id} is missing {', '.join(missing)}.")
            if not has_initial_performance_tag(performance):
                raise ValueError(
                    f"{voice_id} performance must begin with at least one initial [performance direction] tag."
                )
            if any(entry.voice_id == voice_id for entries in section_entries.values() for entry in entries):
                raise ValueError(f"Duplicate Voice ID exists in Voice Production: {voice_id}")
            section_entries[current_section].append(
                VoiceEntry(voice_id, title, voice_type, speaker, duration, performance)
            )
            continue
        i += 1

    if not section_titles or not any(section_entries.values()):
        raise ValueError("Voice Production contains no gameplay-ordered Voice entries.")
    empty = [title for title in section_titles if not section_entries[title]]
    if empty:
        raise ValueError("Voice section has no entries: " + ", ".join(empty))
    owners = [section_owner[title] for title in section_titles]
    if len(owners) != len(set(owners)):
        raise ValueError("Duplicate Voice section Owner ID exists")
    return VoiceProduction(
        cast=cast,
        sections=tuple(
            VoiceSection(section_owner[title], title, tuple(section_entries[title]))
            for title in section_titles
        ),
    )
