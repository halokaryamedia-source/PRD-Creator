#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from docx import Document

PLACEHOLDER_RE = re.compile(r"\b(?:TBD|TODO|FIXME)\b|\[OPEN\]", re.I)
ENTRY_RE = re.compile(r"^###\s+([A-Za-z0-9][A-Za-z0-9-]*)\s+[—-]\s+(.+?)\s*$")
VOICE_ID_RE = re.compile(r"\bVO-[A-Z0-9][A-Z0-9-]*\b")
DOCX_ENTRY_RE = re.compile(r"^(VO-[A-Z0-9][A-Z0-9-]*)\s+-\s+(.+?)\s*$")
STATUS_RE = re.compile(r"^\s*status:\s*([A-Za-z0-9_-]+)\s*$", re.M)
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")


@dataclass
class Requirement:
    voice_id: str
    title: str
    voice_type: str = ""
    speaker: str = ""
    channel: str = ""
    trigger: str = ""
    must_communicate: list[str] = field(default_factory=list)


@dataclass
class ScriptEntry:
    voice_id: str
    title: str
    voice_type: str = ""
    duration: str = ""
    performance: str = ""
    section: str = ""


@dataclass
class DocxEntry:
    voice_id: str
    title: str
    voice_type: str
    duration: str
    performance: str
    section: str


def norm(s: str) -> str:
    return " ".join(s.split())


def text_fingerprint(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def docx_revision_identifier(requirements_sha256: str, script_sha256: str) -> str:
    return (
        f"voice-requirements-sha256={requirements_sha256};"
        f"voice-script-sha256={script_sha256}"
    )


def parse_requirements(path: Path) -> dict[str, Requirement]:
    text = path.read_text(encoding="utf-8")
    if PLACEHOLDER_RE.search(text):
        raise ValueError("Voice requirements contain unresolved placeholders")
    lines = text.splitlines()
    out: dict[str, Requirement] = {}
    current: Requirement | None = None
    list_mode: str | None = None
    for raw in lines:
        line = raw.rstrip()
        m = ENTRY_RE.match(line)
        if m:
            vid = m.group(1)
            if vid in out:
                raise ValueError(f"Duplicate Voice ID in requirements: {vid}")
            current = Requirement(vid, m.group(2).strip())
            out[vid] = current
            list_mode = None
            continue
        if current is None:
            continue
        if line.startswith("- Type:"):
            current.voice_type = line.split(":", 1)[1].strip()
            list_mode = None
        elif line.startswith("- Speaker:"):
            current.speaker = line.split(":", 1)[1].strip()
            list_mode = None
        elif line.startswith("- Channel:"):
            current.channel = line.split(":", 1)[1].strip()
            list_mode = None
        elif line.startswith("- Trigger:"):
            current.trigger = line.split(":", 1)[1].strip()
            list_mode = None
        elif line.startswith("- Must communicate:"):
            list_mode = "must"
        elif line.startswith("- Must not add/repeat:") or line.startswith("- Source refs:"):
            list_mode = None
        elif list_mode == "must" and re.match(r"^\s{2,}-\s+", line):
            current.must_communicate.append(re.sub(r"^\s{2,}-\s+", "", line).strip())
    if not out:
        raise ValueError("No Voice IDs found in requirements")
    for requirement in out.values():
        missing = [
            key
            for key, value in {
                "Type": requirement.voice_type,
                "Speaker": requirement.speaker,
                "Channel": requirement.channel,
                "Trigger": requirement.trigger,
            }.items()
            if not value
        ]
        if missing:
            raise ValueError(
                f"{requirement.voice_id} missing requirement metadata: {', '.join(missing)}"
            )
    return out


def parse_script(path: Path) -> tuple[list[str], dict[str, ScriptEntry], str]:
    text = path.read_text(encoding="utf-8")
    if PLACEHOLDER_RE.search(text):
        raise ValueError("Voice script contains unresolved placeholders")
    lines = text.splitlines()
    sections: list[str] = []
    current_section = ""
    source_requirements_sha256 = ""
    out: dict[str, ScriptEntry] = {}
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if line.startswith("Source Voice Requirements SHA-256:"):
            if source_requirements_sha256:
                raise ValueError("Voice script contains duplicate Voice Requirements SHA-256 metadata")
            source_requirements_sha256 = line.split(":", 1)[1].strip().lower()
            if not SHA256_RE.fullmatch(source_requirements_sha256):
                raise ValueError("Source Voice Requirements SHA-256 must be exactly 64 hexadecimal characters")
            i += 1
            continue
        if line.startswith("## "):
            current_section = line[3:].strip()
            sections.append(current_section)
            i += 1
            continue
        m = ENTRY_RE.match(line)
        if not m:
            i += 1
            continue
        vid = m.group(1)
        if vid in out:
            raise ValueError(f"Duplicate Voice ID in script: {vid}")
        entry = ScriptEntry(vid, m.group(2).strip(), section=current_section)
        i += 1
        while i < len(lines):
            meta = lines[i].rstrip()
            if meta.startswith("Type:"):
                entry.voice_type = meta.split(":", 1)[1].strip()
                i += 1
                continue
            if meta.startswith("Estimated Duration:"):
                entry.duration = meta.split(":", 1)[1].strip()
                i += 1
                continue
            if meta.strip() == "```performance":
                i += 1
                body: list[str] = []
                while i < len(lines) and lines[i].strip() != "```":
                    body.append(lines[i].rstrip())
                    i += 1
                if i >= len(lines):
                    raise ValueError(f"Unclosed performance block for {vid}")
                entry.performance = "\n".join(body).strip()
                i += 1
                break
            if meta.startswith("### ") or meta.startswith("## "):
                break
            i += 1
        if not current_section:
            raise ValueError(f"{vid} appears before a section")
        for key, value in {
            "Type": entry.voice_type,
            "Estimated Duration": entry.duration,
            "Performance Script": entry.performance,
        }.items():
            if not value:
                raise ValueError(f"{vid} missing {key}")
        out[vid] = entry
    if not out:
        raise ValueError("No Voice IDs found in script")
    if not source_requirements_sha256:
        raise ValueError("Voice script missing Source Voice Requirements SHA-256 metadata")
    return sections, out, source_requirements_sha256


def validate_state(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = STATUS_RE.search(text)
    if not match:
        raise ValueError("voice-state.yaml missing status")
    status = match.group(1)
    allowed = {"voice_script_ready", "voice_validation", "needs_revision", "voice_delivery_ready"}
    if status not in allowed:
        raise ValueError(
            f"Flow 7 cannot validate status {status}; expected one of: {', '.join(sorted(allowed))}"
        )
    return status


def previous_nonempty(paragraphs, index: int) -> str:
    for pos in range(index - 1, -1, -1):
        text = paragraphs[pos].text.strip()
        if text:
            return text
    return ""


def next_nonempty_index(paragraphs, index: int) -> int | None:
    for pos in range(index + 1, len(paragraphs)):
        if paragraphs[pos].text.strip():
            return pos
    return None


def parse_docx_entries(doc: Document) -> tuple[list[str], list[str], dict[str, DocxEntry], list[str]]:
    paragraphs = doc.paragraphs
    sections: list[str] = []
    order: list[str] = []
    entries: dict[str, DocxEntry] = {}
    issues: list[str] = []
    current_section = ""

    for index, paragraph in enumerate(paragraphs):
        text = paragraph.text.strip()
        style_name = paragraph.style.name if paragraph.style is not None else ""
        if style_name == "Heading 1":
            current_section = text
            sections.append(current_section)
            continue

        match = DOCX_ENTRY_RE.fullmatch(text)
        if not match:
            continue

        voice_id, title = match.group(1), match.group(2).strip()
        if voice_id in entries:
            issues.append(f"DOCX contains duplicate entry heading for {voice_id}")
            continue

        voice_type = previous_nonempty(paragraphs, index)
        duration_index = next_nonempty_index(paragraphs, index)
        duration_line = paragraphs[duration_index].text.strip() if duration_index is not None else ""
        performance_index = (
            next_nonempty_index(paragraphs, duration_index)
            if duration_index is not None
            else None
        )
        performance = paragraphs[performance_index].text.strip() if performance_index is not None else ""

        duration = ""
        if duration_line.startswith("Estimated Duration:"):
            duration = duration_line.split(":", 1)[1].strip()
        else:
            issues.append(f"DOCX entry {voice_id} is missing its bound Estimated Duration paragraph")

        entries[voice_id] = DocxEntry(
            voice_id=voice_id,
            title=title,
            voice_type=voice_type,
            duration=duration,
            performance=performance,
            section=current_section,
        )
        order.append(voice_id)

    return sections, order, entries, issues


def validate_docx(
    path: Path,
    sections: list[str],
    script: dict[str, ScriptEntry],
    requirements_sha256: str,
    script_sha256: str,
) -> list[str]:
    doc = Document(path)
    paragraphs = doc.paragraphs
    full = "\n".join(paragraph.text for paragraph in paragraphs)
    issues: list[str] = []

    expected_identifier = docx_revision_identifier(requirements_sha256, script_sha256)
    actual_identifier = (doc.core_properties.identifier or "").strip()
    if actual_identifier != expected_identifier:
        issues.append(
            "DOCX revision identifier mismatch: "
            f"expected {expected_identifier}, found {actual_identifier or '<missing>'}"
        )

    actual_sections, actual_order, docx_entries, structural_issues = parse_docx_entries(doc)
    issues.extend(structural_issues)

    expected_sections = [section for section in sections if section]
    if [norm(section) for section in actual_sections] != [norm(section) for section in expected_sections]:
        issues.append(
            "DOCX section order differs from canonical script: "
            f"expected {expected_sections}, found {actual_sections}"
        )

    expected_order = list(script)
    if actual_order != expected_order:
        issues.append(
            "DOCX Voice entry order differs from canonical script: "
            f"expected {expected_order}, found {actual_order}"
        )

    expected_ids = set(script)
    actual_ids = set(docx_entries)
    if actual_ids != expected_ids:
        missing = sorted(expected_ids - actual_ids)
        extra = sorted(actual_ids - expected_ids)
        if missing:
            issues.append("DOCX missing Voice entry blocks: " + ", ".join(missing))
        if extra:
            issues.append("DOCX has extra Voice entry blocks: " + ", ".join(extra))

    global_ids = set(VOICE_ID_RE.findall(full))
    if global_ids != expected_ids:
        missing = sorted(expected_ids - global_ids)
        extra = sorted(global_ids - expected_ids)
        if missing:
            issues.append("DOCX missing Voice ID tokens: " + ", ".join(missing))
        if extra:
            issues.append("DOCX has unexpected Voice ID tokens: " + ", ".join(extra))

    for voice_id in expected_order:
        expected = script[voice_id]
        actual = docx_entries.get(voice_id)
        if actual is None:
            continue
        if norm(actual.section) != norm(expected.section):
            issues.append(
                f"DOCX section binding differs for {voice_id}: expected {expected.section}, found {actual.section}"
            )
        if actual.voice_type.casefold() != expected.voice_type.casefold():
            issues.append(
                f"DOCX Type differs for {voice_id}: expected {expected.voice_type}, found {actual.voice_type}"
            )
        if norm(actual.title) != norm(expected.title):
            issues.append(
                f"DOCX title differs for {voice_id}: expected {expected.title}, found {actual.title}"
            )
        if norm(actual.duration) != norm(expected.duration):
            issues.append(
                f"DOCX duration differs for {voice_id}: expected {expected.duration}, found {actual.duration or '<missing>'}"
            )
        if norm(actual.performance) != norm(expected.performance):
            issues.append(f"DOCX performance text differs for {voice_id}")

    section = doc.sections[0]
    width = round(section.page_width.inches, 2)
    height = round(section.page_height.inches, 2)
    if (width, height) != (8.5, 11.0):
        issues.append(f"DOCX page size expected Letter 8.5x11, got {width}x{height}")
    if not paragraphs:
        issues.append("DOCX contains no paragraphs")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Mechanically validate the current Flow 7 Voice requirements/script/DOCX package."
    )
    parser.add_argument("project", type=Path, help="workspace/active/<project> directory")
    args = parser.parse_args()
    project = args.project
    requirements_path = project / "work/voice-requirements.md"
    script_path = project / "work/voice-production.md"
    docx_path = project / "output/Voice Production.docx"
    state_path = project / "state/voice-state.yaml"
    missing = [
        str(path.relative_to(project))
        for path in (requirements_path, script_path, docx_path, state_path)
        if not path.is_file()
    ]
    if missing:
        print("VOICE VALIDATION FAILED: missing files: " + ", ".join(missing), file=sys.stderr)
        return 2

    try:
        validate_state(state_path)
        requirements = parse_requirements(requirements_path)
        sections, script, declared_requirements_sha256 = parse_script(script_path)
        current_requirements_sha256 = text_fingerprint(requirements_path)
        current_script_sha256 = text_fingerprint(script_path)
        issues: list[str] = []

        if declared_requirements_sha256.casefold() != current_requirements_sha256.casefold():
            issues.append(
                "Script Voice Requirements revision mismatch: "
                f"expected {current_requirements_sha256}, found {declared_requirements_sha256}"
            )

        if set(requirements) != set(script):
            missing_script = sorted(set(requirements) - set(script))
            extra_script = sorted(set(script) - set(requirements))
            if missing_script:
                issues.append("Script missing Voice IDs: " + ", ".join(missing_script))
            if extra_script:
                issues.append("Script has extra Voice IDs: " + ", ".join(extra_script))

        for voice_id in sorted(set(requirements) & set(script)):
            if requirements[voice_id].voice_type.casefold() != script[voice_id].voice_type.casefold():
                issues.append(f"Type mismatch for {voice_id}")

        issues.extend(
            validate_docx(
                docx_path,
                sections,
                script,
                current_requirements_sha256,
                current_script_sha256,
            )
        )

        if issues:
            print("VOICE VALIDATION FAILED")
            for issue in issues:
                print("- " + issue)
            return 1

        print("VOICE VALIDATION PASS")
        print(
            f"requirements={len(requirements)} script_entries={len(script)} sections={len(sections)}"
        )
        print("revision_integrity=passed")
        print("docx_entry_binding=passed")
        print("semantic_and_visual_review=required")
        return 0
    except (OSError, ValueError) as exc:
        print(f"VOICE VALIDATION FAILED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
