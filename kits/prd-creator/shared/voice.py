from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .issues import SourceParseError

ENTRY_RE = re.compile(r"^###\s+([A-Za-z0-9][A-Za-z0-9-]*)\s+[—-]\s+(.+?)\s*$")
VOICE_ID_RE = re.compile(r"^VO-[A-Z0-9]+(?:-[A-Z0-9]+)*$")
MOMENT_ID_RE = re.compile(r"^MOM-[A-Z0-9]+(?:-[A-Z0-9]+)*$")
PLACEHOLDER_RE = re.compile(r"\b(?:TBD|TODO|FIXME)\b|\[OPEN\]", re.I)
SECTION_PREFIX_RE = re.compile(r"^\s*\d+\.\s*")
OWNER_RE = re.compile(r"^Owner ID:\s*(\S+)\s*$", re.I)
REQUIREMENT_LIST_FIELDS = {"Must communicate", "Must not add/repeat", "Source refs"}
REQUIREMENT_SCALAR_FIELDS = {
    "Type",
    "Function",
    "Necessity",
    "Speaker",
    "Channel",
    "Trigger",
    "Purpose",
    "Moment ID",
    "Moment",
    "Timing Constraint",
}


@dataclass(frozen=True)
class VoiceRequirement:
    voice_id: str
    owner_id: str
    section_title: str
    title: str
    voice_type: str
    function: str
    necessity: str
    speaker: str
    channel: str
    trigger: str
    purpose: str
    moment_id: str
    moment: str
    timing_constraint: str
    must_communicate: tuple[str, ...]
    must_not_add_repeat: tuple[str, ...]
    source_refs: tuple[str, ...]


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


def _error(path: Path, line: int | None, code: str, owner: str, message: str, *, field: str = "") -> SourceParseError:
    return SourceParseError(code, owner, message, path=path.as_posix(), line=line, field=field)


def plain_section_title(value: str) -> str:
    return SECTION_PREFIX_RE.sub("", value).strip()


def selected_voice(cast: dict[str, str], speaker: str) -> str:
    speaker_key = speaker.casefold()
    for cast_speaker, voice in cast.items():
        if cast_speaker.casefold() == speaker_key:
            return voice
    return ""


def parse_requirements(path: Path) -> dict[str, VoiceRequirement]:
    text = path.read_text(encoding="utf-8")
    placeholder = PLACEHOLDER_RE.search(text)
    if placeholder:
        placeholder_line = text.count("\n", 0, placeholder.start()) + 1
        raise _error(
            path,
            placeholder_line,
            "VOICE_REQUIREMENT_PLACEHOLDER",
            "flow5.voice_requirement",
            "Voice requirements contain unresolved placeholders",
        )

    out: dict[str, VoiceRequirement] = {}
    current_section = ""
    current_owner = ""
    current_section_line: int | None = None
    seen_section_owners: dict[str, str] = {}
    moment_titles: dict[tuple[str, str], str] = {}
    current_id: str | None = None
    current_id_line: int | None = None
    current_title = ""
    scalar: dict[str, str] = {}
    scalar_lines: dict[str, int] = {}
    lists: dict[str, list[str]] = {key: [] for key in REQUIREMENT_LIST_FIELDS}
    active_list: str | None = None

    def flush() -> None:
        nonlocal current_id, current_id_line, current_title, scalar, scalar_lines, lists, active_list
        if current_id is None:
            return
        required_scalar = (
            "Type",
            "Function",
            "Necessity",
            "Speaker",
            "Channel",
            "Trigger",
            "Purpose",
            "Moment ID",
            "Moment",
        )
        missing = [key for key in required_scalar if not scalar.get(key)]
        if missing:
            raise _error(
                path,
                current_id_line,
                "VOICE_REQUIREMENT_FIELD_MISSING",
                "flow5.voice_requirement",
                f"{current_id} missing requirement metadata: {', '.join(missing)}",
                field=missing[0],
            )
        if VOICE_ID_RE.fullmatch(current_id) is None:
            raise _error(
                path,
                current_id_line,
                "VOICE_ID_INVALID",
                "flow5.voice_requirement",
                f"Voice requirement ID must use VO-... stable identity: {current_id}",
                field="Voice ID",
            )
        if scalar["Necessity"] not in {"required", "supporting"}:
            raise _error(
                path,
                scalar_lines.get("Necessity", current_id_line),
                "VOICE_NECESSITY_INVALID",
                "flow5.voice_requirement",
                f"{current_id} Necessity must be required or supporting",
                field="Necessity",
            )
        moment_id = scalar["Moment ID"]
        if MOMENT_ID_RE.fullmatch(moment_id) is None:
            raise _error(
                path,
                scalar_lines.get("Moment ID", current_id_line),
                "VOICE_MOMENT_ID_INVALID",
                "flow5.voice_requirement",
                f"{current_id} Moment ID must use MOM-... stable identity",
                field="Moment ID",
            )
        moment_key = (current_owner, moment_id)
        previous_moment = moment_titles.get(moment_key)
        if previous_moment is not None and previous_moment != scalar["Moment"]:
            raise _error(
                path,
                scalar_lines.get("Moment", current_id_line),
                "VOICE_MOMENT_CONFLICT",
                "flow5.voice_requirement",
                f"{current_id} Moment ID {moment_id} conflicts with existing title {previous_moment!r}",
                field="Moment",
            )
        moment_titles[moment_key] = scalar["Moment"]
        for list_field in REQUIREMENT_LIST_FIELDS:
            if not lists[list_field]:
                raise _error(
                    path,
                    current_id_line,
                    "VOICE_REQUIREMENT_LIST_MISSING",
                    "flow5.voice_requirement",
                    f"{current_id} requires at least one {list_field} item",
                    field=list_field,
                )
        if current_id in out:
            raise _error(
                path,
                current_id_line,
                "VOICE_ID_DUPLICATE",
                "flow5.voice_requirement",
                f"Duplicate Voice ID in requirements: {current_id}",
                field="Voice ID",
            )
        if not current_owner:
            raise _error(
                path,
                current_section_line,
                "VOICE_OWNER_MISSING",
                "flow5.voice_requirement",
                f"Voice requirement section {current_section!r} requires Owner ID before entries",
                field="Owner ID",
            )
        out[current_id] = VoiceRequirement(
            voice_id=current_id,
            owner_id=current_owner,
            section_title=current_section,
            title=current_title,
            voice_type=scalar["Type"],
            function=scalar["Function"],
            necessity=scalar["Necessity"],
            speaker=scalar["Speaker"],
            channel=scalar["Channel"],
            trigger=scalar["Trigger"],
            purpose=scalar["Purpose"],
            moment_id=moment_id,
            moment=scalar["Moment"],
            timing_constraint=scalar.get("Timing Constraint", ""),
            must_communicate=tuple(lists["Must communicate"]),
            must_not_add_repeat=tuple(lists["Must not add/repeat"]),
            source_refs=tuple(lists["Source refs"]),
        )
        current_id = None
        current_id_line = None
        current_title = ""
        scalar = {}
        scalar_lines = {}
        lists = {key: [] for key in REQUIREMENT_LIST_FIELDS}
        active_list = None

    for index, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip()
        if line.startswith("## "):
            flush()
            current_section = line[3:].strip()
            current_section_line = index
            if not current_section:
                raise _error(
                    path,
                    index,
                    "VOICE_SECTION_EMPTY",
                    "flow5.voice_requirement",
                    "Voice requirements section title cannot be empty",
                )
            current_owner = ""
            continue
        if current_id is None and current_section and (owner_match := OWNER_RE.match(line)):
            if current_owner:
                raise _error(
                    path,
                    index,
                    "VOICE_OWNER_DUPLICATE",
                    "flow5.voice_requirement",
                    f"Duplicate Owner ID in Voice requirements section: {current_section}",
                    field="Owner ID",
                )
            owner_id = owner_match.group(1).strip()
            previous_section = seen_section_owners.get(owner_id)
            if previous_section is not None and previous_section != current_section:
                raise _error(
                    path,
                    index,
                    "VOICE_OWNER_DUPLICATE",
                    "flow5.voice_requirement",
                    f"Duplicate Voice requirement Owner ID {owner_id} across sections {previous_section!r} and {current_section!r}",
                    field="Owner ID",
                )
            current_owner = owner_id
            seen_section_owners[owner_id] = current_section
            continue
        match = ENTRY_RE.match(line)
        if match:
            flush()
            if not current_section:
                raise _error(
                    path,
                    index,
                    "VOICE_ENTRY_ORPHANED",
                    "flow5.voice_requirement",
                    f"Voice requirement {match.group(1)} appears before a gameplay section",
                )
            if not current_owner:
                raise _error(
                    path,
                    index,
                    "VOICE_OWNER_MISSING",
                    "flow5.voice_requirement",
                    f"Voice requirements section {current_section} requires Owner ID before entries",
                    field="Owner ID",
                )
            current_id = match.group(1)
            current_id_line = index
            current_title = match.group(2).strip()
            continue
        if current_id is None:
            continue
        if line.startswith("- ") and line[2:].endswith(":"):
            key = line[2:-1].strip()
            if key not in REQUIREMENT_LIST_FIELDS:
                raise _error(
                    path,
                    index,
                    "VOICE_REQUIREMENT_FIELD_UNSUPPORTED",
                    "flow5.voice_requirement",
                    f"Unsupported Voice requirement list field: {key}",
                    field=key,
                )
            active_list = key
            continue
        if active_list and re.match(r"^\s{2,}-\s+", line):
            value = re.sub(r"^\s{2,}-\s+", "", line).strip()
            if value:
                lists[active_list].append(value)
            continue
        if line.startswith("- ") and ":" in line:
            key, value = (part.strip() for part in line[2:].split(":", 1))
            if key not in REQUIREMENT_SCALAR_FIELDS:
                raise _error(
                    path,
                    index,
                    "VOICE_REQUIREMENT_FIELD_UNSUPPORTED",
                    "flow5.voice_requirement",
                    f"Unsupported Voice requirement field: {key}",
                    field=key,
                )
            if key in scalar:
                raise _error(
                    path,
                    index,
                    "VOICE_REQUIREMENT_FIELD_DUPLICATE",
                    "flow5.voice_requirement",
                    f"Duplicate Voice requirement field {key}: {current_id}",
                    field=key,
                )
            scalar[key] = value
            scalar_lines[key] = index
            active_list = None
            continue
        if line.strip():
            active_list = None
    flush()
    if not out:
        raise _error(
            path, None, "VOICE_REQUIREMENT_MISSING", "flow5.voice_requirement", "No Voice IDs found in requirements"
        )
    return out


def parse_production(path: Path) -> VoiceProduction:
    text = path.read_text(encoding="utf-8")
    placeholder = PLACEHOLDER_RE.search(text)
    if placeholder:
        placeholder_line = text.count("\n", 0, placeholder.start()) + 1
        raise _error(
            path,
            placeholder_line,
            "VOICE_PRODUCTION_PLACEHOLDER",
            "flow6.voice_production",
            "Voice Production contains an unresolved placeholder",
        )
    lines = text.splitlines()
    cast: dict[str, str] = {}
    section_titles: list[str] = []
    section_owner: dict[str, str] = {}
    section_entries: dict[str, list[VoiceEntry]] = {}
    current_section: str | None = None
    current_section_line: int | None = None
    in_cast = False
    seen_voice_ids: set[str] = set()
    seen_owners: set[str] = set()
    i = 0

    while i < len(lines):
        line_number = i + 1
        line = lines[i].rstrip()
        if current_section is None and line.strip() == "Voice Cast:":
            in_cast = True
            i += 1
            continue
        if current_section is None and in_cast:
            if line.startswith("- "):
                payload = line[2:].strip()
                if ":" not in payload:
                    raise _error(
                        path,
                        line_number,
                        "VOICE_CAST_FORMAT",
                        "flow6.voice_production",
                        "Voice Cast entries must use '- <Speaker>: <ElevenLabs voice>'",
                    )
                speaker, voice = (part.strip() for part in payload.split(":", 1))
                if not speaker or not voice:
                    raise _error(
                        path,
                        line_number,
                        "VOICE_CAST_EMPTY",
                        "flow6.voice_production",
                        "Voice Cast requires a non-empty Speaker and voice selection/profile",
                    )
                if any(existing.casefold() == speaker.casefold() for existing in cast):
                    raise _error(
                        path,
                        line_number,
                        "VOICE_CAST_DUPLICATE",
                        "flow6.voice_production",
                        f"Duplicate Voice Cast speaker: {speaker}",
                        field="Speaker",
                    )
                cast[speaker] = voice
                i += 1
                continue
            if line.strip():
                in_cast = False

        if line.startswith("## "):
            current_section = line[3:].strip()
            current_section_line = line_number
            if not current_section:
                raise _error(
                    path,
                    line_number,
                    "VOICE_SECTION_EMPTY",
                    "flow6.voice_production",
                    "Voice Production section title cannot be empty",
                )
            if current_section in section_entries:
                raise _error(
                    path,
                    line_number,
                    "VOICE_SECTION_DUPLICATE",
                    "flow6.voice_production",
                    f"Duplicate Voice Production section: {current_section}",
                )
            section_titles.append(current_section)
            section_entries[current_section] = []
            section_owner[current_section] = ""
            in_cast = False
            i += 1
            continue

        if current_section is not None and (owner_match := OWNER_RE.match(line)):
            owner_id = owner_match.group(1).strip()
            if section_entries[current_section]:
                raise _error(
                    path,
                    line_number,
                    "VOICE_OWNER_POSITION",
                    "flow6.voice_production",
                    f"Owner ID for Voice section {current_section} must appear before Voice entries",
                    field="Owner ID",
                )
            if section_owner[current_section]:
                raise _error(
                    path,
                    line_number,
                    "VOICE_OWNER_DUPLICATE",
                    "flow6.voice_production",
                    f"Duplicate Owner ID in Voice section: {current_section}",
                    field="Owner ID",
                )
            if owner_id in seen_owners:
                raise _error(
                    path,
                    line_number,
                    "VOICE_OWNER_DUPLICATE",
                    "flow6.voice_production",
                    f"Duplicate Voice section Owner ID: {owner_id}",
                    field="Owner ID",
                )
            section_owner[current_section] = owner_id
            seen_owners.add(owner_id)
            i += 1
            continue

        match = ENTRY_RE.match(line)
        if match:
            entry_line = line_number
            if current_section is None:
                raise _error(
                    path,
                    entry_line,
                    "VOICE_ENTRY_ORPHANED",
                    "flow6.voice_production",
                    f"Voice entry {match.group(1)} appears before a gameplay section",
                )
            if not section_owner[current_section]:
                raise _error(
                    path,
                    entry_line,
                    "VOICE_OWNER_MISSING",
                    "flow6.voice_production",
                    f"Voice section {current_section} requires Owner ID before Voice entries",
                    field="Owner ID",
                )
            voice_id = match.group(1)
            if VOICE_ID_RE.fullmatch(voice_id) is None:
                raise _error(
                    path,
                    entry_line,
                    "VOICE_ID_INVALID",
                    "flow6.voice_production",
                    f"Voice Production ID must use VO-... stable identity: {voice_id}",
                    field="Voice ID",
                )
            if voice_id in seen_voice_ids:
                raise _error(
                    path,
                    entry_line,
                    "VOICE_ID_DUPLICATE",
                    "flow6.voice_production",
                    f"Duplicate Voice ID exists in Voice Production: {voice_id}",
                    field="Voice ID",
                )
            seen_voice_ids.add(voice_id)
            title = match.group(2).strip()
            values: dict[str, str] = {}
            value_lines: dict[str, int] = {}
            performance = ""
            i += 1
            while i < len(lines):
                meta_line = i + 1
                meta = lines[i].rstrip()
                if meta.startswith(("## ", "### ")):
                    break
                if meta.strip() == "```performance":
                    if performance:
                        raise _error(
                            path,
                            meta_line,
                            "VOICE_PERFORMANCE_DUPLICATE",
                            "flow6.voice_production",
                            f"Duplicate performance block for {voice_id}",
                            field="Performance Script",
                        )
                    i += 1
                    body: list[str] = []
                    while i < len(lines) and lines[i].strip() != "```":
                        body.append(lines[i].rstrip())
                        i += 1
                    if i >= len(lines):
                        raise _error(
                            path,
                            meta_line,
                            "VOICE_PERFORMANCE_UNCLOSED",
                            "flow6.voice_production",
                            f"Unclosed performance block for {voice_id}",
                            field="Performance Script",
                        )
                    performance = "\n".join(body).strip()
                    i += 1
                    continue
                if ":" in meta:
                    key, value = (part.strip() for part in meta.split(":", 1))
                    if key not in {"Type", "Speaker", "Estimated Duration"}:
                        raise _error(
                            path,
                            meta_line,
                            "VOICE_PRODUCTION_FIELD_UNSUPPORTED",
                            "flow6.voice_production",
                            f"Unsupported canonical Voice Production field: {key}",
                            field=key,
                        )
                    if key in values:
                        raise _error(
                            path,
                            meta_line,
                            "VOICE_PRODUCTION_FIELD_DUPLICATE",
                            "flow6.voice_production",
                            f"Duplicate Voice Production field {key}: {voice_id}",
                            field=key,
                        )
                    values[key] = value
                    value_lines[key] = meta_line
                elif meta.strip():
                    raise _error(
                        path,
                        meta_line,
                        "VOICE_PRODUCTION_LINE_UNRECOGNIZED",
                        "flow6.voice_production",
                        f"Unrecognized Voice Production line for {voice_id}: {meta.strip()}",
                    )
                i += 1
            missing = [
                label
                for label, value in {
                    "Type": values.get("Type", ""),
                    "Speaker": values.get("Speaker", ""),
                    "Estimated Duration": values.get("Estimated Duration", ""),
                    "Performance Script": performance,
                }.items()
                if not value
            ]
            if missing:
                raise _error(
                    path,
                    entry_line,
                    "VOICE_PRODUCTION_FIELD_MISSING",
                    "flow6.voice_production",
                    f"{voice_id} is missing {', '.join(missing)}",
                    field=missing[0],
                )
            section_entries[current_section].append(
                VoiceEntry(
                    voice_id, title, values["Type"], values["Speaker"], values["Estimated Duration"], performance
                )
            )
            continue
        i += 1

    if not section_titles or not any(section_entries.values()):
        raise _error(
            path,
            None,
            "VOICE_PRODUCTION_EMPTY",
            "flow6.voice_production",
            "Voice Production contains no gameplay-ordered Voice entries",
        )
    empty = [title for title in section_titles if not section_entries[title]]
    if empty:
        raise _error(
            path,
            None,
            "VOICE_SECTION_EMPTY",
            "flow6.voice_production",
            "Voice section has no entries: " + ", ".join(empty),
        )
    missing_owner = [title for title in section_titles if not section_owner[title]]
    if missing_owner:
        raise _error(
            path,
            current_section_line,
            "VOICE_OWNER_MISSING",
            "flow6.voice_production",
            "Voice section requires Owner ID: " + ", ".join(missing_owner),
            field="Owner ID",
        )
    return VoiceProduction(
        cast=cast,
        sections=tuple(
            VoiceSection(section_owner[title], title, tuple(section_entries[title])) for title in section_titles
        ),
    )
