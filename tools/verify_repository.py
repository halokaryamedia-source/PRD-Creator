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
    ".github/workflows/prd-verify.yml",
    ".github/workflows/voice-verify.yml",
    "AGENTS.md",
    "CONTEXT.md",
    "requirements.lock.txt",
    "tests/test_prd_contracts.py",
    "tests/test_prd_content_purity.py",
    "tests/test_prd_delivery.py",
    "tests/test_voice_contracts.py",
    "docs/knowledge/README.md",
    "docs/knowledge/next-action.md",
    "docs/knowledge/work-routing.md",
    "docs/knowledge/workflows/development.md",
    "docs/knowledge/workflows/maintenance.md",
    "docs/knowledge/workflows/maintenance-note-template.md",
    "docs/knowledge/ownership.md",
    "docs/knowledge/source-authority.md",
    "docs/knowledge/reviews/README.md",
    "docs/knowledge/reviews/current-validation.md",
    "docs/knowledge/decisions/README.md",
    "docs/knowledge/decisions/recording-policy.md",
    "docs/knowledge/skills/activation-matrix.md",
    "docs/knowledge/skills/README.md",
    "docs/knowledge/operations/boot-baseline.md",
    "docs/knowledge/operations/backlog.md",
    "kits/project-document-generator/AGENTS.md",
    "kits/project-document-generator/SKILL.md",
    "kits/project-document-generator/renderer/delivery.py",
    "kits/voice-production-kit/AGENTS.md",
    "kits/voice-production-kit/SKILL.md",
    "kits/voice-production-kit/requirements.txt",
    "kits/voice-production-kit/references/aftershock/README.md",
    "workspace/README.md",
    "workspace/archive/README.md",
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

CURRENT_DELIVERY_OWNER_PATHS = [
    "CONTEXT.md",
    "docs/foundation/03-prd-generation.md",
    "docs/foundation/04-prd-validation-handoff.md",
    "docs/foundation/06-elevenlabs-script-production.md",
    "docs/foundation/07-voice-validation-delivery.md",
    "docs/knowledge/ownership.md",
    "docs/knowledge/reviews/current-validation.md",
    "kits/project-document-generator/AGENTS.md",
    "kits/project-document-generator/RENDERING.md",
    "kits/voice-production-kit/AGENTS.md",
    "kits/voice-production-kit/VOICE-VALIDATION.md",
    "workspace/README.md",
    "docs/knowledge/decisions/recording-policy.md",
    ".agents/skills/project-document-production/SKILL.md",
    ".agents/skills/voice-production/SKILL.md",
    "kits/project-document-generator/SKILL.md",
    "kits/project-document-generator/WORKFLOW.md",
    "kits/project-document-generator/RULES.md",
    "kits/project-document-generator/CONTENT-CONTRACT.md",
    "kits/voice-production-kit/SKILL.md",
]

RETIRED_CURRENT_DELIVERY_TERMS = (
    "output/final.html",
    "final.html",
    "output/team-handoff.md",
    "Cinematic & Presentation",
)

AGENT_REQUIRED_HEADINGS = {
    "## Execution channel",
    "## User-facing communication",
    "## Product boundaries",
}

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
PIN_RE = re.compile(r"^([A-Za-z0-9_.-]+)==([^\s=]+)$")
SKILL_VERSION_RE = re.compile(r"(?m)^version:\s*([^\s]+)\s*$")
README_VERSION_RE = re.compile(r"(?m)^\*\*Version:\*\*\s*([^\s]+)\s*$")


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
    retired = [
        "Production Document Builder",
        ".github/workflows/production-verify.yml",
        "docs/knowledge/index.md",
        "docs/knowledge/minimal-nav.md",
        "docs/knowledge/workspace-map.md",
        "docs/knowledge/flow.md",
        "docs/knowledge/flows",
        "docs/knowledge/maintenance",
        "docs/knowledge/modules",
        "docs/knowledge/sources",
        "docs/knowledge/implementation-map.md",
        "docs/knowledge/decision-log.md",
        "docs/knowledge/decisions/change-decision-guide.md",
        "docs/knowledge/reviews/review-graph.md",
        "docs/knowledge/reviews/review-template.md",
        "docs/knowledge/operations/context-boot-baseline.md",
        "docs/knowledge/operations/task-board.md",
        "docs/foundation/validation-report.md",
        "workspace/saved",
        "kits/voice-production-kit/REFERENCE",
        "kits/voice-production-kit/INSTRUCTIONS.md",
    ]
    for rel in retired:
        if (ROOT / rel).exists():
            fail(errors, f"retired repository path must not return: {rel}")


def check_current_delivery_routing(errors: list[str]) -> None:
    for rel in CURRENT_DELIVERY_OWNER_PATHS:
        path = ROOT / rel
        if not path.is_file():
            fail(errors, f"missing current delivery owner: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for retired in RETIRED_CURRENT_DELIVERY_TERMS:
            if retired in text:
                fail(errors, f"stale current delivery reference in {rel}: {retired}")

    ownership = ROOT / "docs" / "knowledge" / "ownership.md"
    if ownership.is_file():
        text = ownership.read_text(encoding="utf-8")
        required_markers = (
            "renderer/delivery.py",
            "output/README.md",
            "output/v<document.version>/prd.html",
            "output/v<document.version>/context.md",
            "output/v<document.version>/index.json",
            "Visual Effects & Presentation",
        )
        for marker in required_markers:
            if marker not in text:
                fail(errors, f"ownership.md missing current delivery routing marker: {marker}")

    workspace = ROOT / "workspace" / "README.md"
    if workspace.is_file():
        text = workspace.read_text(encoding="utf-8")
        required_markers = (
            "renderer/delivery.py",
            "output/README.md",
            "output/v<document.version>/prd.html",
            "output/v<document.version>/context.md",
            "output/v<document.version>/index.json",
        )
        for marker in required_markers:
            if marker not in text:
                fail(errors, f"workspace/README.md missing current delivery marker: {marker}")

    current_validation = ROOT / "docs" / "knowledge" / "reviews" / "current-validation.md"
    skill_path = ROOT / "kits" / "project-document-generator" / "SKILL.md"
    if current_validation.is_file():
        text = current_validation.read_text(encoding="utf-8")
        required_markers = (
            "output/README.md",
            "output/v<document.version>/prd.html",
            "output/v<document.version>/context.md",
            "output/v<document.version>/index.json",
        )
        for marker in required_markers:
            if marker not in text:
                fail(errors, f"current-validation.md missing current delivery marker: {marker}")

        if skill_path.is_file():
            version_match = SKILL_VERSION_RE.search(skill_path.read_text(encoding="utf-8"))
            if version_match:
                expected = f"Project Document Generator remains **v{version_match.group(1)}**"
                if expected not in text:
                    fail(
                        errors,
                        "current-validation.md Project Document Generator version does not match current SKILL version",
                    )

    voice_docs = [
        ROOT / "docs" / "foundation" / "06-elevenlabs-script-production.md",
        ROOT / "docs" / "foundation" / "07-voice-validation-delivery.md",
        ROOT / "kits" / "voice-production-kit" / "AGENTS.md",
        ROOT / "kits" / "voice-production-kit" / "VOICE-VALIDATION.md",
    ]
    retired_voice_nav = "04 Production Assets\n   VOICE"
    for path in voice_docs:
        if path.is_file() and retired_voice_nav in path.read_text(encoding="utf-8"):
            fail(
                errors,
                f"stale Voice sidebar category routing in {path.relative_to(ROOT)}",
            )


    decision_policy = ROOT / "docs" / "knowledge" / "decisions" / "recording-policy.md"
    if decision_policy.is_file():
        policy_text = decision_policy.read_text(encoding="utf-8")
        for retired in ("implementation-map.md", "`modules/`"):
            if retired in policy_text:
                fail(errors, f"stale current decision-routing reference in recording-policy.md: {retired}")


def check_next_action(errors: list[str]) -> None:
    path = ROOT / "docs" / "knowledge" / "next-action.md"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    if text.count("## Next Step") != 1:
        fail(errors, "next-action.md must contain exactly one '## Next Step'")
    if "## Current Status" not in text:
        fail(errors, "next-action.md is missing '## Current Status'")


def check_agent_contract(errors: list[str]) -> None:
    path = ROOT / "AGENTS.md"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    for heading in sorted(AGENT_REQUIRED_HEADINGS):
        if heading not in text:
            fail(errors, f"AGENTS.md missing required section: {heading}")


def check_project_document_version(errors: list[str]) -> None:
    skill_path = ROOT / "kits" / "project-document-generator" / "SKILL.md"
    readme_path = ROOT / "kits" / "project-document-generator" / "README.md"
    if not skill_path.is_file() or not readme_path.is_file():
        return

    skill_match = SKILL_VERSION_RE.search(skill_path.read_text(encoding="utf-8"))
    readme_match = README_VERSION_RE.search(readme_path.read_text(encoding="utf-8"))
    if not skill_match:
        fail(errors, "Project Document SKILL.md is missing version front matter")
        return
    if not readme_match:
        fail(errors, "Project Document README.md is missing Version")
        return
    if skill_match.group(1) != readme_match.group(1):
        fail(
            errors,
            "Project Document version drift: "
            f"SKILL {skill_match.group(1)} != README {readme_match.group(1)}",
        )


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
    check_current_delivery_routing(errors)
    check_next_action(errors)
    check_agent_contract(errors)
    check_project_document_version(errors)
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
    print("- root AGENTS contract sections: present")
    print("- Project Document skill/README version: aligned")
    print("- current versioned delivery routing: aligned")
    print("- workspace/current-validation delivery routing: aligned")
    print("- relative navigation: valid")
    print("- dependency lock/direct pins: exact and aligned")
    print("- Python kits/tools/tests: syntax valid")
    print("- retired builder boundary: preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
