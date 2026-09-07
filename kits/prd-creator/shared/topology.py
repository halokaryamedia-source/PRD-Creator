from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class OwnerTarget:
    owner_id: str
    title: str
    label: Any
    kind: str
    stable_id: str


def owner_targets(render_data: dict[str, Any]) -> dict[str, OwnerTarget]:
    """Return the one canonical owner topology used by 04 and Voice.

    `journey:<id>` is reserved for gameplay-flow entries that are not package-owned.
    A package and its matching gameplay-flow page use only `package:<id>`. This removes
    the former ambiguity where one package could be addressed through two Owner IDs.
    """

    targets: dict[str, OwnerTarget] = {
        "shared": OwnerTarget(
            "shared",
            "Global / Shared Assets",
            {"en": "Shared", "id": "Shared"},
            "shared",
            "shared",
        )
    }
    packages = [item for item in render_data.get("packages", []) if isinstance(item, dict)]
    package_ids = {str(item.get("id") or "") for item in packages}

    flow_items = [item for item in render_data.get("gameplay_flow", []) if isinstance(item, dict)]
    for index, flow in enumerate(flow_items):
        flow_id = str(flow.get("id") or "")
        if not flow_id or flow_id in package_ids:
            continue
        label = (
            {"en": "Introduction", "id": "Introduction"}
            if index == 0
            else {"en": "Journey", "id": "Journey"}
        )
        targets[f"journey:{flow_id}"] = OwnerTarget(
            f"journey:{flow_id}",
            _text_en(flow.get("title")) or flow_id,
            label,
            "journey",
            flow_id,
        )

    for index, package in enumerate(packages, 1):
        package_id = str(package.get("id") or "")
        if not package_id:
            continue
        targets[f"package:{package_id}"] = OwnerTarget(
            f"package:{package_id}",
            _text_en(package.get("title")) or package_id,
            package.get("package_label")
            or {"en": f"Gameplay {index}", "id": f"Gameplay {index}"},
            "package",
            package_id,
        )
    return targets


def require_owner(render_data: dict[str, Any], owner_id: str) -> OwnerTarget:
    target = owner_targets(render_data).get(owner_id)
    if target is None:
        raise ValueError(f"Owner ID does not match accepted PRD topology: {owner_id}")
    return target


def production_page_id(render_data: dict[str, Any], owner_id: str) -> str:
    target = require_owner(render_data, owner_id)
    if target.kind == "shared":
        return "production-assets-global-shared"
    if target.kind == "package":
        return f"production-assets-{_slug(target.stable_id)}"
    return f"production-assets-journey-{_slug(target.stable_id)}"


def ordered_owner_ids(render_data: dict[str, Any], owners: set[str]) -> list[str]:
    targets = owner_targets(render_data)
    unknown = sorted(owners - set(targets))
    if unknown:
        raise ValueError("Owner ID(s) outside accepted PRD topology: " + ", ".join(unknown))

    order: list[str] = []
    if "shared" in owners:
        order.append("shared")
    for flow in render_data.get("gameplay_flow", []):
        if not isinstance(flow, dict):
            continue
        owner_id = f"journey:{flow.get('id')}"
        if owner_id in owners and owner_id in targets:
            order.append(owner_id)
    for package in render_data.get("packages", []):
        if not isinstance(package, dict):
            continue
        owner_id = f"package:{package.get('id')}"
        if owner_id in owners:
            order.append(owner_id)
    return order


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-") or "section"


def _text_en(value: Any) -> str:
    if isinstance(value, dict):
        value = value.get("en") or value.get("id") or ""
    return str(value or "").strip()
