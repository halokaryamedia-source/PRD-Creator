from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from .issues import SourceParseError

ASSET_CATEGORIES = (
    "3D Models",
    "UI & Information",
    "Audio",
    "Visual Effects & Presentation",
)
CATEGORY_TYPE = {
    "3D Models": {"MODEL", "ITEM"},
    "UI & Information": {"UI / TEXT"},
    "Audio": {"AUDIO"},
    "Visual Effects & Presentation": {"PARTICLE"},
}
DEFAULT_TYPE = {
    "3D Models": "MODEL",
    "UI & Information": "UI / TEXT",
    "Audio": "AUDIO",
    "Visual Effects & Presentation": "PARTICLE",
}
ASSET_ID_RE = re.compile(r"^AST-[A-Z0-9]+(?:-[A-Z0-9]+)*$")
MOMENT_ID_RE = re.compile(r"^MOM-[A-Z0-9]+(?:-[A-Z0-9]+)*$")
OWNER_RE = re.compile(r"^Owner ID:\s*(\S+)\s*$", re.I)
PLACEHOLDER_RE = re.compile(r"\b(?:TBD|TODO|FIXME)\b|\[OPEN\]", re.I)
ALLOWED_FIELDS = {
    "ID",
    "Moment ID",
    "Moment",
    "Type",
    "Function",
    "Asset Brief",
    "Visual Brief",
    "Audio Brief",
    "Size",
}
RETIRED_FIELDS = {"Flow", "Create", "Used", "Includes", "Group", "For", "Requirement", "Usage"}


@dataclass(frozen=True)
class AssetEntry:
    asset_id: str
    title: str
    category: str
    type_label: str
    function_text: str
    moment_id: str
    moment: str
    asset_brief: str = ""
    size: str = ""
    content: str = ""
    order: int = 0


@dataclass
class AssetSection:
    owner_id: str
    title: str
    categories: dict[str, list[AssetEntry]] = field(default_factory=dict)
    moment_order: dict[str, int] = field(default_factory=dict)
    moment_titles: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class AssetRequirements:
    sections: tuple[AssetSection, ...]


def _error(path: Path, line: int | None, code: str, message: str, *, field: str = "") -> SourceParseError:
    return SourceParseError(
        code,
        "production_assets.source",
        message,
        path=path.as_posix(),
        line=line,
        field=field,
    )


def parse_asset_requirements(path: Path) -> AssetRequirements:
    text = path.read_text(encoding="utf-8")
    placeholder = PLACEHOLDER_RE.search(text)
    if placeholder:
        line = text.count("\n", 0, placeholder.start()) + 1
        raise _error(path, line, "ASSET_PLACEHOLDER", "Production Asset requirements contain an unresolved placeholder")

    sections: list[AssetSection] = []
    owner_ids: set[str] = set()
    asset_ids: set[str] = set()
    current_section: AssetSection | None = None
    current_section_line: int | None = None
    current_category: str | None = None
    lines = text.splitlines()
    i = 0

    while i < len(lines):
        line_number = i + 1
        line = lines[i].rstrip()
        if line.startswith("## "):
            if current_section is not None and not current_section.owner_id:
                raise _error(
                    path,
                    current_section_line,
                    "ASSET_OWNER_MISSING",
                    f"Production Asset section {current_section.title!r} requires Owner ID",
                    field="Owner ID",
                )
            title = line[3:].strip()
            if not title:
                raise _error(path, line_number, "ASSET_SECTION_EMPTY", "Production Asset section title cannot be empty")
            current_section = AssetSection("", title)
            current_section_line = line_number
            sections.append(current_section)
            current_category = None
            i += 1
            continue

        if current_section is not None and (match := OWNER_RE.match(line)):
            owner_id = match.group(1).strip()
            if current_section.owner_id:
                raise _error(
                    path,
                    line_number,
                    "ASSET_OWNER_DUPLICATE",
                    f"Duplicate Owner ID in Production Asset section {current_section.title!r}",
                    field="Owner ID",
                )
            if owner_id in owner_ids:
                raise _error(
                    path,
                    line_number,
                    "ASSET_OWNER_DUPLICATE",
                    f"Duplicate Production Asset Owner ID: {owner_id}",
                    field="Owner ID",
                )
            current_section.owner_id = owner_id
            owner_ids.add(owner_id)
            i += 1
            continue

        if line.startswith("### Gameplay Flow "):
            raise _error(
                path,
                line_number,
                "ASSET_LEGACY_FLOW",
                "Gameplay Flow metadata is retired; resource ordering must use stable Moment ID fields",
            )

        if line.startswith("### "):
            _require_section_owner(path, current_section, line_number, "Production Asset category")
            category = line[4:].strip()
            if category not in ASSET_CATEGORIES:
                raise _error(
                    path,
                    line_number,
                    "ASSET_CATEGORY_UNSUPPORTED",
                    f"Unsupported Production Asset category: {category}. Use one of: {', '.join(ASSET_CATEGORIES)}",
                )
            assert current_section is not None
            if category in current_section.categories:
                raise _error(
                    path,
                    line_number,
                    "ASSET_CATEGORY_DUPLICATE",
                    f"Duplicate Production Asset category in one section: {category}",
                )
            current_section.categories[category] = []
            current_category = category
            i += 1
            continue

        if line.startswith("#### "):
            if current_section is None or current_category is None:
                raise _error(
                    path,
                    line_number,
                    "ASSET_ENTRY_ORPHANED",
                    "Production Asset entry appears before its section/category",
                )
            entry_line = line_number
            title = line[5:].strip()
            if not title:
                raise _error(path, entry_line, "ASSET_TITLE_EMPTY", "Production Asset name cannot be empty")
            fields: dict[str, str] = {}
            field_lines: dict[str, int] = {}
            content = ""
            i += 1
            while i < len(lines):
                meta_line = i + 1
                meta = lines[i].rstrip()
                if meta.startswith(("## ", "### ", "#### ")):
                    break
                if meta.strip() == "Content:":
                    if content:
                        raise _error(
                            path,
                            meta_line,
                            "ASSET_CONTENT_DUPLICATE",
                            f"Duplicate Content block for Production Asset: {title}",
                            field="Content",
                        )
                    i += 1
                    if i >= len(lines) or not lines[i].strip().startswith("```"):
                        raise _error(
                            path,
                            meta_line,
                            "ASSET_CONTENT_FENCE",
                            f"Production Asset Content for {title} must use a fenced text block",
                            field="Content",
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
                            "ASSET_CONTENT_UNCLOSED",
                            f"Unclosed Content block for Production Asset: {title}",
                            field="Content",
                        )
                    content = "\n".join(body).strip()
                elif ":" in meta:
                    key, value = (part.strip() for part in meta.split(":", 1))
                    if key in RETIRED_FIELDS:
                        raise _error(
                            path,
                            meta_line,
                            "ASSET_FIELD_RETIRED",
                            f"Retired Production Asset field is not allowed: {key}",
                            field=key,
                        )
                    if key not in ALLOWED_FIELDS:
                        raise _error(
                            path,
                            meta_line,
                            "ASSET_FIELD_UNSUPPORTED",
                            f"Unsupported Production Asset field: {key}",
                            field=key,
                        )
                    if key in fields:
                        raise _error(
                            path,
                            meta_line,
                            "ASSET_FIELD_DUPLICATE",
                            f"Duplicate Production Asset field {key}: {title}",
                            field=key,
                        )
                    fields[key] = value
                    field_lines[key] = meta_line
                elif meta.strip():
                    raise _error(
                        path,
                        meta_line,
                        "ASSET_LINE_UNRECOGNIZED",
                        f"Unrecognized Production Asset line under {title}: {meta.strip()}",
                    )
                i += 1

            asset_id = fields.get("ID", "")
            if not ASSET_ID_RE.fullmatch(asset_id):
                raise _error(
                    path,
                    field_lines.get("ID", entry_line),
                    "ASSET_ID_INVALID",
                    f"Production Asset {title} requires stable ID in AST-... form",
                    field="ID",
                )
            if asset_id in asset_ids:
                raise _error(
                    path,
                    field_lines.get("ID", entry_line),
                    "ASSET_ID_DUPLICATE",
                    f"Duplicate Production Asset ID: {asset_id}",
                    field="ID",
                )
            asset_ids.add(asset_id)

            moment_id = fields.get("Moment ID", "")
            moment = fields.get("Moment", "")
            if not MOMENT_ID_RE.fullmatch(moment_id):
                raise _error(
                    path,
                    field_lines.get("Moment ID", entry_line),
                    "ASSET_MOMENT_ID_INVALID",
                    f"Production Asset {asset_id} requires stable Moment ID in MOM-... form",
                    field="Moment ID",
                )
            if not moment:
                raise _error(
                    path,
                    field_lines.get("Moment", entry_line),
                    "ASSET_MOMENT_MISSING",
                    f"Production Asset {asset_id} requires Moment",
                    field="Moment",
                )
            previous_title = current_section.moment_titles.get(moment_id)
            if previous_title is not None and previous_title != moment:
                raise _error(
                    path,
                    field_lines.get("Moment", entry_line),
                    "ASSET_MOMENT_CONFLICT",
                    f"Moment ID {moment_id} maps to conflicting titles {previous_title!r} and {moment!r}",
                    field="Moment",
                )
            if moment_id not in current_section.moment_order:
                current_section.moment_order[moment_id] = len(current_section.moment_order) + 1
                current_section.moment_titles[moment_id] = moment

            type_label = fields.get("Type") or DEFAULT_TYPE[current_category]
            if type_label not in CATEGORY_TYPE[current_category]:
                allowed = ", ".join(sorted(CATEGORY_TYPE[current_category]))
                raise _error(
                    path,
                    field_lines.get("Type", entry_line),
                    "ASSET_TYPE_INVALID",
                    f"Production Asset {asset_id} type {type_label!r} is invalid for {current_category}; expected {allowed}",
                    field="Type",
                )
            function_text = fields.get("Function", "")
            if not function_text:
                raise _error(
                    path,
                    field_lines.get("Function", entry_line),
                    "ASSET_FUNCTION_MISSING",
                    f"Production Asset {asset_id} requires Function",
                    field="Function",
                )
            brief = fields.get("Asset Brief") or fields.get("Visual Brief") or fields.get("Audio Brief") or ""
            if type_label == "UI / TEXT" and not content:
                raise _error(
                    path,
                    entry_line,
                    "ASSET_CONTENT_MISSING",
                    f"UI / TEXT Production Asset {asset_id} requires exact Content",
                    field="Content",
                )
            if type_label in {"MODEL", "ITEM", "PARTICLE", "AUDIO"} and not brief:
                raise _error(
                    path, entry_line, "ASSET_BRIEF_MISSING", f"Production Asset {asset_id} requires a production brief"
                )

            current_section.categories[current_category].append(
                AssetEntry(
                    asset_id=asset_id,
                    title=title,
                    category=current_category,
                    type_label=type_label,
                    function_text=function_text,
                    moment_id=moment_id,
                    moment=moment,
                    asset_brief=brief,
                    size=fields.get("Size", ""),
                    content=content,
                    order=len(asset_ids),
                )
            )
            continue
        i += 1

    if current_section is not None and not current_section.owner_id:
        raise _error(
            path,
            current_section_line,
            "ASSET_OWNER_MISSING",
            f"Production Asset section {current_section.title!r} requires Owner ID",
            field="Owner ID",
        )
    if not sections:
        raise _error(path, None, "ASSET_SECTION_MISSING", "Production Asset requirements contain no sections")
    if not asset_ids:
        raise _error(path, None, "ASSET_ENTRY_MISSING", "Production Asset requirements contain no asset entries")
    return AssetRequirements(tuple(sections))


def _require_section_owner(path: Path, section: AssetSection | None, line: int, context: str) -> None:
    if section is None or not section.owner_id:
        raise _error(
            path,
            line,
            "ASSET_OWNER_MISSING",
            f"{context} requires a Production Asset section with Owner ID",
            field="Owner ID",
        )
