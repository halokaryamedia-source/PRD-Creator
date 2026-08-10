#!/usr/bin/env python3
"""Static repository contract checks for PRD-Creator.

This gate checks stable repository invariants that are useful on every commit.
It does not replace production contract execution, project semantic validation,
HTML/DOCX visual QA, or generated-audio review.
"""
from __future__ import annotations

import py_compile
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

CANONICAL_SKILLS = {
    "development-brief",
    "project-document-production",
    "voice-production",
}

REQUIRED_PATHS = [
    ".github/workflows/repository-verify.yml",
    ".github/workflows/production-verify.yml",
    "AGENTS.md",
    "CONTEXT.md",
    "requirements.lock.txt",
    "tests/test_prd_contracts.py",
    "tests/test_voice_contracts.py",
    "docs/knowledge/next-action.md",
    "docs/knowledge/flow.md",
    "docs/knowledge/flows/development-flow.md",
    "docs/knowledge/maintenance/maintenance-flow.md",
    "docs/knowledge/modules/module-map.md",
    "docs/knowledge/sources/source-map.md",
    "docs/knowledge/reviews/review-graph.md",
    "docs/knowledge/decisions/change-decision-guide.md",
    "docs/knowledge/skills/activation-matrix.md",
    "docs/knowledge/skills/skill-map.md",
    "kits/project-document-generator/AGENTS.md",
    "kits/project-document-generator/SKILL.md",
    "kits/voice-production-kit/AGENTS.md",
    "kits/voice-production-kit/SKILL.md",
    "kits/voice-production-kit/requirements.txt",
]

MARKDOWN_ROOTS = [
    ROOT / "AGENTS.md",
    ROOT / "CONTEXT.md",
    ROOT / "README.md",
    ROOT / "docs" / "foundation",
    ROOT / "docs" / "knowledge",
    ROOT / "kits" / "project-document-generator",
    ROOT / "kits" / "voice-production-kit",
]

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
PIN_RE = re.compile(r"^([A-Za-z0-9_.-]+)==([^\s=]+)$")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for item in MARKDOWN_ROOTS:
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            files.extend(item.rglob("*.md"))
    return sorted(set(files))


def check_required_paths(errors: list[str]) -> None:
    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            fail(errors, f"missing required owner: {rel}")


def check_skill_root(errors: list[str]) -> None:
    skill_root = ROOT / ".agents" / "skills"
    if not skill_root.is_dir():
        fail(errors, "missing canonical .agents/skills root")
        return

    actual = {
        path.name
        for path in skill_root.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    }
    if actual != CANONICAL_SKILLS:
        fail(
            errors,
            "canonical skill set drift: "
            f"expected {sorted(CANONICAL_SKILLS)}, got {sorted(actual)}",
        )

    for skill in sorted(CANONICAL_SKILLS):
        if not (skill_root / skill / "SKILL.md").is_file():
            fail(errors, f"missing SKILL.md for canonical skill: {skill}")

    nested = (
        list((ROOT / "kits").glob("**/.agents/skills"))
        if (ROOT / "kits").exists()
        else []
    )
    for path in nested:
        fail(errors, f"unexpected nested repository skill root: {path.relative_to(ROOT)}")


def check_retired_boundaries(errors: list[str]) -> None:
    if (ROOT / "Production Document Builder").exists():
        fail(errors, "retired Production Document Builder/ must not return to live tree")


def check_next_action(errors: list[str]) -> None:
    path = ROOT / "docs" / "knowledge" / "next-action.md"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    if text.count("## Next Step") != 1:
        fail(errors, "next-action.md must contain exactly one '## Next Step'")
    if "## Current Status" not in text:
        fail(errors, "next-action.md is missing '## Current Status'")


def requirement_pins(path: Path, errors: list[str]) -> dict[str, str]:
    pins: dict[str, str] = {}
    if not path.is_file():
        return pins
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        match = PIN_RE.fullmatch(line)
        if not match:
            fail(
                errors,
                f"{path.relative_to(ROOT)}:{lineno} must use an exact 'name==version' pin",
            )
            continue
        name = match.group(1).replace("_", "-").lower()
        if name in pins:
            fail(errors, f"duplicate dependency pin in {path.relative_to(ROOT)}: {name}")
        pins[name] = match.group(2)
    return pins


def check_dependency_lock(errors: list[str]) -> None:
    lock = requirement_pins(ROOT / "requirements.lock.txt", errors)
    direct = requirement_pins(
        ROOT / "kits" / "voice-production-kit" / "requirements.txt", errors
    )
    if not lock:
        fail(errors, "requirements.lock.txt must contain exact dependency pins")
        return
    if not direct:
        fail(errors, "Voice requirements.txt must contain at least one exact direct pin")
        return
    for name, version in direct.items():
        if lock.get(name) != version:
            fail(
                errors,
                "direct dependency must match lock exactly: "
                f"{name}=={version}, lock has {lock.get(name)!r}",
            )


def normalize_link_target(source: Path, raw: str) -> Path | None:
    target = raw.strip().strip("<>")
    if not target:
        return None

    lower = target.lower()
    if (
        target.startswith("#")
        or "://" in target
        or lower.startswith(("mailto:", "tel:", "data:", "skills:", "sandbox:"))
    ):
        return None

    target = unquote(target.split("#", 1)[0].split("?", 1)[0]).strip()
    if not target:
        return None

    if target.startswith("/"):
        return ROOT / target.lstrip("/")
    return source.parent / target


def check_markdown_links(errors: list[str]) -> None:
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = normalize_link_target(path, raw)
            if target is None:
                continue
            try:
                exists = target.resolve().exists()
            except OSError:
                exists = target.exists()
            if not exists:
                rel_source = path.relative_to(ROOT)
                fail(errors, f"broken relative link in {rel_source}: {raw}")


def check_python_syntax(errors: list[str]) -> None:
    roots = [ROOT / "kits", ROOT / "tools", ROOT / "tests"]
    for root in roots:
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("*.py")):
            try:
                py_compile.compile(str(path), doraise=True)
            except py_compile.PyCompileError as exc:
                fail(errors, f"python syntax error in {path.relative_to(ROOT)}: {exc.msg}")


def main() -> int:
    errors: list[str] = []

    check_required_paths(errors)
    check_skill_root(errors)
    check_retired_boundaries(errors)
    check_next_action(errors)
    check_dependency_lock(errors)
    check_markdown_links(errors)
    check_python_syntax(errors)

    if errors:
        print("REPOSITORY VERIFY FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("REPOSITORY VERIFY PASSED")
    print(f"- canonical skills: {', '.join(sorted(CANONICAL_SKILLS))}")
    print(f"- markdown files checked: {len(iter_markdown_files())}")
    print("- relative navigation: valid")
    print("- dependency lock/direct pins: exact and aligned")
    print("- Python kits/tools/tests: syntax valid")
    print("- retired builder boundary: preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
