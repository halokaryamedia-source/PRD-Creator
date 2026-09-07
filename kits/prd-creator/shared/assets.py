from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

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
OWNER_RE = re.compile(r"^Owner ID:\s*(\S+)\s*$", re.I)
PLACEHOLDER_RE = re.compile(r"\b(?:TBD|TODO|FIXME)\b|\[OPEN\]", re.I)
ALLOWED_FIELDS = {
    "ID",
    "Flow",
    "Moment",
    "Type",
    "Function",
    "Asset Brief",
    "Visual Brief",
    "Audio Brief",
    "Size",
}
RETIRED_FIELDS = {"Create", "Used", "Includes", "Group", "For", "Requirement", "Usage"}


@dataclass(frozen=True)
class AssetEntry:
    asset_id: str
    title: str
    category: str
    type_label: str
    function_text: str
    moment: str
    flow: str = ""
    asset_brief: str = ""
    size: str = ""
    content: str = ""
    order: int = 0


@dataclass
class AssetSection:
    owner_id: str
    title: str
    categories: dict[str, list[AssetEntry]] = field(default_factory=dict)
    flow_order: dict[str, int] = field(default_factory=dict)


@dataclass(frozen=True)
class AssetRequirements:
    sections: tuple[AssetSection, ...]


def parse_asset_requirements(path: Path) -> AssetRequirements:
    text = path.read_text(encoding="utf-8")
    if PLACEHOLDER_RE.search(text):
        raise ValueError("Production Asset requirements contain an unresolved placeholder")

    sections: list[AssetSection] = []
    owner_ids: set[str] = set()
    asset_ids: set[str] = set()
    current_section: AssetSection | None = None
    current_category: str | None = None
    lines = text.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()
        if line.startswith("## "):
            if current_section is not None and not current_section.owner_id:
                raise ValueError(f"Production Asset section {current_section.title} requires Owner ID")
            title = line[3:].strip()
            if not title:
                raise ValueError("Production Asset section title cannot be empty")
            current_section = AssetSection("", title)
            sections.append(current_section)
            current_category = None
            i += 1
            continue

        if current_section is not None and (match := OWNER_RE.match(line)):
            owner_id = match.group(1).strip()
            if current_section.owner_id:
                raise ValueError(f"Duplicate Owner ID in Production Asset section: {current_section.title}")
            if owner_id in owner_ids:
                raise ValueError(f"Duplicate Production Asset Owner ID: {owner_id}")
            current_section.owner_id = owner_id
            owner_ids.add(owner_id)
            i += 1
            continue

        if line.startswith("### Gameplay Flow "):
            _require_section_owner(current_section, "Gameplay Flow metadata")
            flow_title = line[len("### Gameplay Flow ") :].strip()
            if not flow_title:
                raise ValueError("Gameplay Flow title cannot be empty")
            assert current_section is not None
            if flow_title in current_section.flow_order:
                raise ValueError(f"Duplicate Gameplay Flow label in Production Assets: {flow_title}")
            current_section.flow_order[flow_title] = len(current_section.flow_order) + 1
            current_category = None
            i += 1
            continue

        if line.startswith("### "):
            _require_section_owner(current_section, "Production Asset category")
            category = line[4:].strip()
            if category not in ASSET_CATEGORIES:
                raise ValueError(
                    f"Unsupported Production Asset category: {category}. Use one of: {', '.join(ASSET_CATEGORIES)}"
                )
            assert current_section is not None
            if category in current_section.categories:
                raise ValueError(f"Duplicate Production Asset category in one section: {category}")
            current_section.categories[category] = []
            current_category = category
            i += 1
            continue

        if line.startswith("#### "):
            if current_section is None or current_category is None:
                raise ValueError("Production Asset entry appears before its section/category")
            title = line[5:].strip()
            if not title:
                raise ValueError("Production Asset name cannot be empty")
            fields: dict[str, str] = {}
            content = ""
            i += 1
            while i < len(lines):
                meta = lines[i].rstrip()
                if meta.startswith(("## ", "### ", "#### ")):
                    break
                if meta.strip() == "Content:":
                    if content:
                        raise ValueError(f"Duplicate Content block for Production Asset: {title}")
                    i += 1
                    if i >= len(lines) or not lines[i].strip().startswith("```"):
                        raise ValueError(f"Production Asset Content for {title} must use a fenced text block")
                    i += 1
                    body: list[str] = []
                    while i < len(lines) and lines[i].strip() != "```":
                        body.append(lines[i].rstrip())
                        i += 1
                    if i >= len(lines):
                        raise ValueError(f"Unclosed Content block for Production Asset: {title}")
                    content = "\n".join(body).strip()
                elif ":" in meta:
                    key, value = (part.strip() for part in meta.split(":", 1))
                    if key in RETIRED_FIELDS:
                        raise ValueError(f"Retired Production Asset field is not allowed: {key}")
                    if key not in ALLOWED_FIELDS:
                        raise ValueError(f"Unsupported Production Asset field: {key}")
                    if key in fields:
                        raise ValueError(f"Duplicate Production Asset field {key}: {title}")
                    fields[key] = value
                elif meta.strip():
                    raise ValueError(f"Unrecognized Production Asset line under {title}: {meta.strip()}")
                i += 1

            asset_id = fields.get("ID", "")
            if not ASSET_ID_RE.fullmatch(asset_id):
                raise ValueError(f"Production Asset {title} requires stable ID in AST-... form")
            if asset_id in asset_ids:
                raise ValueError(f"Duplicate Production Asset ID: {asset_id}")
            asset_ids.add(asset_id)

            type_label = fields.get("Type") or DEFAULT_TYPE[current_category]
            if type_label not in CATEGORY_TYPE[current_category]:
                allowed = ", ".join(sorted(CATEGORY_TYPE[current_category]))
                raise ValueError(
                    f"Production Asset {asset_id} type {type_label!r} is invalid for {current_category}; expected {allowed}"
                )
            function_text = fields.get("Function", "")
            moment = fields.get("Moment", "")
            if not function_text:
                raise ValueError(f"Production Asset {asset_id} requires Function")
            if not moment:
                raise ValueError(f"Production Asset {asset_id} requires Moment")
            flow = fields.get("Flow", "")
            if flow and current_section.flow_order and flow not in current_section.flow_order:
                raise ValueError(
                    f"Production Asset Flow does not match a defined Gameplay Flow: {current_section.owner_id} / {asset_id} / {flow}"
                )
            brief = fields.get("Asset Brief") or fields.get("Visual Brief") or fields.get("Audio Brief") or ""
            if type_label == "UI / TEXT" and not content:
                raise ValueError(f"UI / TEXT Production Asset {asset_id} requires exact Content")
            if type_label in {"MODEL", "ITEM", "PARTICLE", "AUDIO"} and not brief:
                raise ValueError(f"Production Asset {asset_id} requires a production brief")

            current_section.categories[current_category].append(
                AssetEntry(
                    asset_id=asset_id,
                    title=title,
                    category=current_category,
                    type_label=type_label,
                    function_text=function_text,
                    moment=moment,
                    flow=flow,
                    asset_brief=brief,
                    size=fields.get("Size", ""),
                    content=content,
                    order=len(asset_ids),
                )
            )
            continue
        i += 1

    if current_section is not None and not current_section.owner_id:
        raise ValueError(f"Production Asset section {current_section.title} requires Owner ID")
    if not sections:
        raise ValueError("Production Asset requirements contain no sections")
    if not asset_ids:
        raise ValueError("Production Asset requirements contain no asset entries")
    return AssetRequirements(tuple(sections))


def _require_section_owner(section: AssetSection | None, context: str) -> None:
    if section is None or not section.owner_id:
        raise ValueError(f"{context} requires a Production Asset section with Owner ID")
