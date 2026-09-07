from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ENTRY_RE = re.compile(r"^###\s+([A-Za-z0-9][A-Za-z0-9-]*)\s+[—-]\s+(.+?)\s*$")
VOICE_ID_RE = re.compile(r"^VO-[A-Z0-9]+(?:-[A-Z0-9]+)*$")
MOMENT_ID_RE = re.compile(r"^MOM-[A-Z0-9]+(?:-[A-Z0-9]+)*$")
PLACEHOLDER_RE = re.compile(r"\b(?:TBD|TODO|FIXME)\b|\[OPEN\]", re.I)
PERFORMANCE_TAG_LINE_RE = re.compile(r"^(?:\[[^\[\]\r\n]+\]\s*)+$")
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


def has_initial_performance_tag(performance: str) -> bool:
    first = next((line.strip() for line in performance.splitlines() if line.strip()), "")
    return bool(first and PERFORMANCE_TAG_LINE_RE.fullmatch(first))


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
    if PLACEHOLDER_RE.search(text):
        raise ValueError("Voice requirements contain unresolved placeholders")

    out: dict[str, VoiceRequirement] = {}
    current_section = ""
    current_owner = ""
    seen_section_owners: dict[str, str] = {}
    moment_titles: dict[tuple[str, str], str] = {}
    current_id: str | None = None
    current_title = ""
    scalar: dict[str, str] = {}
    lists: dict[str, list[str]] = {key: [] for key in REQUIREMENT_LIST_FIELDS}
    active_list: str | None = None

    def flush() -> None:
        nonlocal current_id, current_title, scalar, lists, active_list
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
            raise ValueError(f"{current_id} missing requirement metadata: {', '.join(missing)}")
        if VOICE_ID_RE.fullmatch(current_id) is None:
            raise ValueError(f"Voice requirement ID must use VO-... stable identity: {current_id}")
        if scalar["Necessity"] not in {"required", "supporting"}:
            raise ValueError(f"{current_id} Necessity must be required or supporting")
        moment_id = scalar["Moment ID"]
        if MOMENT_ID_RE.fullmatch(moment_id) is None:
            raise ValueError(f"{current_id} Moment ID must use MOM-... stable identity")
        moment_key = (current_owner, moment_id)
        previous_moment = moment_titles.get(moment_key)
        if previous_moment is not None and previous_moment != scalar["Moment"]:
            raise ValueError(
                f"{current_id} Moment ID {moment_id} conflicts with existing title {previous_moment!r}"
            )
        moment_titles[moment_key] = scalar["Moment"]
        for list_field in REQUIREMENT_LIST_FIELDS:
            if not lists[list_field]:
                raise ValueError(f"{current_id} requires at least one {list_field} item")
        if current_id in out:
            raise ValueError(f"Duplicate Voice ID in requirements: {current_id}")
        if not current_owner:
            raise ValueError(f"Voice requirement section {current_section!r} requires Owner ID before entries")
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
        current_title = ""
        scalar = {}
        lists = {key: [] for key in REQUIREMENT_LIST_FIELDS}
        active_list = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("## "):
            flush()
            current_section = line[3:].strip()
            if not current_section:
                raise ValueError("Voice requirements section title cannot be empty")
            current_owner = ""
            continue
        if current_id is None and current_section and (owner_match := OWNER_RE.match(line)):
            if current_owner:
                raise ValueError(f"Duplicate Owner ID in Voice requirements section: {current_section}")
            owner_id = owner_match.group(1).strip()
            previous_section = seen_section_owners.get(owner_id)
            if previous_section is not None and previous_section != current_section:
                raise ValueError(
                    f"Duplicate Voice requirement Owner ID {owner_id} across sections {previous_section!r} and {current_section!r}"
                )
            current_owner = owner_id
            seen_section_owners[owner_id] = current_section
            continue
        match = ENTRY_RE.match(line)
        if match:
            flush()
            if not current_section:
                raise ValueError(f"Voice requirement {match.group(1)} appears before a gameplay section")
            if not current_owner:
                raise ValueError(f"Voice requirements section {current_section} requires Owner ID before entries")
            current_id = match.group(1)
            current_title = match.group(2).strip()
            continue
        if current_id is None:
            continue
        if line.startswith("- ") and line[2:].endswith(":"):
            key = line[2:-1].strip()
            if key not in REQUIREMENT_LIST_FIELDS:
                raise ValueError(f"Unsupported Voice requirement list field: {key}")
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
                raise ValueError(f"Unsupported Voice requirement field: {key}")
            if key in scalar:
                raise ValueError(f"Duplicate Voice requirement field {key}: {current_id}")
            scalar[key] = value
            active_list = None
            continue
        if line.strip():
            active_list = None
    flush()

    if not out:
        raise ValueError("No Voice IDs found in requirements")
    return out


def parse_production(path: Path) -> VoiceProduction:
    text = path.read_text(encoding="utf-8")
    if PLACEHOLDER_RE.search(text):
        raise ValueError("Voice Production contains an unresolved placeholder")
    lines = text.splitlines()
    cast: dict[str, str] = {}
    section_titles: list[str] = []
    section_owner: dict[str, str] = {}
    section_entries: dict[str, list[VoiceEntry]] = {}
    current_section: str | None = None
    in_cast = False
    seen_voice_ids: set[str] = set()
    seen_owners: set[str] = set()
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
                    raise ValueError("Voice Cast entries must use '- <Speaker>: <ElevenLabs voice>'")
                speaker, voice = (part.strip() for part in payload.split(":", 1))
                if not speaker or not voice:
                    raise ValueError("Voice Cast requires a non-empty Speaker and voice selection/profile")
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
                raise ValueError("Voice Production section title cannot be empty")
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
            if owner_id in seen_owners:
                raise ValueError(f"Duplicate Voice section Owner ID: {owner_id}")
            section_owner[current_section] = owner_id
            seen_owners.add(owner_id)
            i += 1
            continue

        match = ENTRY_RE.match(line)
        if match:
            if current_section is None:
                raise ValueError(f"Voice entry {match.group(1)} appears before a gameplay section")
            if not section_owner[current_section]:
                raise ValueError(f"Voice section {current_section} requires Owner ID before Voice entries")
            voice_id = match.group(1)
            if VOICE_ID_RE.fullmatch(voice_id) is None:
                raise ValueError(f"Voice Production ID must use VO-... stable identity: {voice_id}")
            if voice_id in seen_voice_ids:
                raise ValueError(f"Duplicate Voice ID exists in Voice Production: {voice_id}")
            seen_voice_ids.add(voice_id)
            title = match.group(2).strip()
            values: dict[str, str] = {}
            performance = ""
            i += 1
            while i < len(lines):
                meta = lines[i].rstrip()
                if meta.startswith(("## ", "### ")):
                    break
                if meta.strip() == "```performance":
                    if performance:
                        raise ValueError(f"Duplicate performance block for {voice_id}")
                    i += 1
                    body: list[str] = []
                    while i < len(lines) and lines[i].strip() != "```":
                        body.append(lines[i].rstrip())
                        i += 1
                    if i >= len(lines):
                        raise ValueError(f"Unclosed performance block for {voice_id}")
                    performance = "\n".join(body).strip()
                    i += 1
                    continue
                if ":" in meta:
                    key, value = (part.strip() for part in meta.split(":", 1))
                    if key not in {"Type", "Speaker", "Estimated Duration"}:
                        raise ValueError(f"Unsupported canonical Voice Production field: {key}")
                    if key in values:
                        raise ValueError(f"Duplicate Voice Production field {key}: {voice_id}")
                    values[key] = value
                elif meta.strip():
                    raise ValueError(f"Unrecognized Voice Production line for {voice_id}: {meta.strip()}")
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
                raise ValueError(f"{voice_id} is missing {', '.join(missing)}")
            if not has_initial_performance_tag(performance):
                raise ValueError(
                    f"{voice_id} performance must begin with at least one initial [performance direction] tag"
                )
            section_entries[current_section].append(
                VoiceEntry(
                    voice_id,
                    title,
                    values["Type"],
                    values["Speaker"],
                    values["Estimated Duration"],
                    performance,
                )
            )
            continue
        i += 1

    if not section_titles or not any(section_entries.values()):
        raise ValueError("Voice Production contains no gameplay-ordered Voice entries")
    empty = [title for title in section_titles if not section_entries[title]]
    if empty:
        raise ValueError("Voice section has no entries: " + ", ".join(empty))
    missing_owner = [title for title in section_titles if not section_owner[title]]
    if missing_owner:
        raise ValueError("Voice section requires Owner ID: " + ", ".join(missing_owner))
    return VoiceProduction(
        cast=cast,
        sections=tuple(
            VoiceSection(section_owner[title], title, tuple(section_entries[title]))
            for title in section_titles
        ),
    )
