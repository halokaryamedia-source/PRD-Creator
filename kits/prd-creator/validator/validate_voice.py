#!/usr/bin/env python3
"""CLI for the canonical Voice lifecycle validator."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT_ROOT = HERE.parent
if __package__ in (None, ""):
    if str(KIT_ROOT) not in sys.path:
        sys.path.insert(0, str(KIT_ROOT))
    from validator.voice_validation import validate
else:
    from .voice_validation import validate

__all__ = ["validate"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="workspace/active/<project> directory")
    args = parser.parse_args()
    result = validate(args.project)
    if result["status"] == "fail":
        print("VOICE VALIDATION FAILED")
        for issue in result["errors"]:
            print("- " + str(issue))
        return 1
    print("VOICE VALIDATION PASS")
    print(
        f"status={result['voice_status']} requirements={result['requirements']} "
        f"script_entries={result['script_entries']} sections={result['sections']}"
    )
    print(f"project_html={result['project_html']}")
    print("semantic_and_visual_review=required")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
