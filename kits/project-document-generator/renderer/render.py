#!/usr/bin/env python3
"""Clone the approved HTML template and apply exact literal replacements.

This helper intentionally does not reconstruct HTML. Dynamic objective packages must be
edited by duplicating the existing package inside the cloned template.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any


def load_replacements(path: Path) -> list[tuple[str, str]]:
    data: Any = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("replacements"), list):
        raise ValueError('Replacement JSON must contain a "replacements" array.')

    replacements: list[tuple[str, str]] = []
    for index, item in enumerate(data["replacements"], start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Replacement #{index} must be an object.")
        old = item.get("old")
        new = item.get("new")
        if not isinstance(old, str) or not isinstance(new, str):
            raise ValueError(f'Replacement #{index} requires string fields "old" and "new".')
        if old == "":
            raise ValueError(f"Replacement #{index} has an empty old value.")
        replacements.append((old, new))
    return replacements


def render(template: Path, output: Path, replacements_path: Path | None) -> None:
    if not template.is_file():
        raise FileNotFoundError(f"Approved template not found: {template}")

    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(template, output)

    if replacements_path is None:
        return

    replacements = load_replacements(replacements_path)
    html = output.read_text(encoding="utf-8")

    for index, (old, new) in enumerate(replacements, start=1):
        count = html.count(old)
        if count == 0:
            raise ValueError(f"Replacement #{index} did not match the cloned template.")
        html = html.replace(old, new)

    output.write_text(html, encoding="utf-8")


def main() -> None:
    default_template = Path(__file__).resolve().parents[1] / "template" / "approved-document.html"

    parser = argparse.ArgumentParser(
        description="Clone the approved HTML template and apply exact literal replacements."
    )
    parser.add_argument("output", type=Path, help="Destination HTML path.")
    parser.add_argument(
        "--template",
        type=Path,
        default=default_template,
        help="Approved template path.",
    )
    parser.add_argument(
        "--replacements",
        type=Path,
        help='Optional JSON file containing {"replacements":[{"old":"...","new":"..."}]}.',
    )
    args = parser.parse_args()

    render(args.template, args.output, args.replacements)
    print(args.output)


if __name__ == "__main__":
    main()
