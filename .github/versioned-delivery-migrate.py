from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def replace_required(path: str, old: str, new: str, *, count: int | None = None) -> None:
    text = read(path)
    actual = text.count(old)
    if actual == 0:
        raise SystemExit(f"{path}: expected text not found: {old!r}")
    if count is not None and actual != count:
        raise SystemExit(f"{path}: expected {count} replacements for {old!r}, found {actual}")
    write(path, text.replace(old, new))


# Project Document Generator release metadata.
replace_required("kits/project-document-generator/SKILL.md", "version: 1.13.0", "version: 1.14.0", count=1)
replace_required("kits/project-document-generator/README.md", "**Version:** 1.13.0", "**Version:** 1.14.0", count=1)
replace_required("README.md", "Project Document Generator **v1.13.0**", "Project Document Generator **v1.14.0**", count=1)

# Current policy/owner docs only. Historical reviews/changelogs are intentionally untouched.
current_docs = [
    "AGENTS.md",
    "CONTEXT.md",
    "README.md",
    *[str(path.relative_to(ROOT)) for path in sorted((ROOT / "docs/foundation").glob("*.md"))],
    "kits/project-document-generator/AGENTS.md",
    "kits/project-document-generator/README.md",
    "kits/project-document-generator/RENDERING.md",
    "kits/project-document-generator/VALIDATION.md",
    "kits/voice-production-kit/AGENTS.md",
    "kits/voice-production-kit/README.md",
    "kits/voice-production-kit/VOICE-VALIDATION.md",
]
for path in current_docs:
    text = read(path).replace("output/final.html", "output/v<document.version>/prd.html")
    if path in {"AGENTS.md", "kits/project-document-generator/AGENTS.md", "kits/voice-production-kit/AGENTS.md"}:
        text = text.replace("`final.html`", "`prd.html`")
    write(path, text)

# Root README: short delivery tree and responsibilities.
root_readme = read("README.md")
old_output = """## Output

```text
output/v<document.version>/prd.html
├── 01 Overview
├── 02 Gameplay Flow
├── 03 Development
│   └── gameplay/objective sections
└── 04 Production Assets      # only when downstream assets exist
    ├── Global / Shared Assets   # only when needed
    └── <gameplay section> → <accepted PRD label>
```
"""
new_output = """## Output

```text
output/
├── README.md                  # navigator / resume entry point
└── v<document.version>/
    ├── prd.html               # human review
    ├── context.md             # AI semantic/development context
    └── index.json             # compact AI navigation + context line ranges
```

`prd.html` keeps the approved human-facing PRD presentation. `context.md` and `index.json` are derived side documents from the same accepted project truth; they are not a second PRD authority.
"""
if old_output not in root_readme:
    raise SystemExit("README.md: expected output block not found")
write("README.md", root_readme.replace(old_output, new_output, 1))

# Stable product context: side-doc meaning and semantic versioning.
context = read("CONTEXT.md")
marker = "PRD core and downstream asset production retain separate canonical owners and acceptance evidence even though humans see one consolidated HTML.\n\n"
addition = """PRD core and downstream asset production retain separate canonical owners and acceptance evidence even though humans see one consolidated HTML.

The same deterministic delivery pass also creates AI side documents beside the HTML:

```text
output/README.md
    navigator / resume entry point

output/v<document.version>/context.md
    reasoning-friendly accepted PRD + relevant Production Asset/Voice requirements

output/v<document.version>/index.json
    compact heading graph + exact context.md line ranges
```

These side documents are derived navigation/reading projections only. They do not create another product authority, and `index.json` must not duplicate the PRD prose as a second structured PRD.

"""
if marker not in context:
    raise SystemExit("CONTEXT.md: delivery insertion marker not found")
context = context.replace(marker, addition, 1)
version_marker = "`document.version` is PRD project/release metadata, not an edit counter."
if version_marker not in context:
    raise SystemExit("CONTEXT.md: version policy marker not found")
context = context.replace(
    version_marker,
    version_marker + " Accepted development handoff versions use semantic `X.Y.Z`; the folder adds the `v` prefix.",
    1,
)
write("CONTEXT.md", context)

# Rendering owner: one deterministic delivery pass and bounded AI reading route.
rendering = read("kits/project-document-generator/RENDERING.md")
insert_before = "## Exact Golden template identity\n"
delivery_section = """## Versioned delivery package

Normal handoff generation uses one deterministic command:

```bash
python kits/project-document-generator/renderer/delivery.py \\
  workspace/active/<project>/
```

It reads the current canonical project sources once and writes:

```text
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

Responsibilities stay narrow:

- `prd.html` is the only human-facing project document and keeps the approved Golden presentation;
- `context.md` is a reasoning-friendly development projection of accepted PRD meaning plus only existing downstream non-Voice/Voice requirements that are relevant to implementation;
- `index.json` is a compact navigation tree with `context.md` line ranges, not a prose copy, schema registry, dependency engine, or second PRD;
- `output/README.md` is the stable resume entry point that identifies the current version and reading route.

`document.version` must use semantic `X.Y.Z` for a handoff package. Version folders track PRD/project meaning; a downstream-only Production Assets refresh may regenerate files inside the same version when accepted PRD meaning did not change.

The AI reading path is intentionally bounded:

```text
output/README.md
→ current index.json
→ affected context.md range (+ directly relevant shared/global range)
→ current implementation
```

The side documents may reorganize already-owned canonical information for reading efficiency. They may not invent project facts, implementation architecture, dependencies, approval state, or compatibility requirements.

"""
if insert_before not in rendering:
    raise SystemExit("RENDERING.md: insertion marker not found")
rendering = rendering.replace(insert_before, delivery_section + insert_before, 1)
rendering = rendering.replace(
    "- `renderer/render.py` → deterministic base render + optional downstream composition orchestration",
    "- `renderer/render.py` → deterministic lower-level human HTML render + optional downstream composition orchestration\n- `renderer/delivery.py` → normal versioned handoff bundle (`prd.html` + AI side projections + navigator)",
)
write("kits/project-document-generator/RENDERING.md", rendering)

agents = read("kits/project-document-generator/AGENTS.md")
agents = agents.replace(
    "- `renderer/render.py` → deterministic base render + optional downstream composition orchestration",
    "- `renderer/render.py` → deterministic lower-level human HTML render + optional downstream composition orchestration\n- `renderer/delivery.py` → deterministic versioned handoff bundle and compact AI reading projections",
)
write("kits/project-document-generator/AGENTS.md", agents)

kit_readme = read("kits/project-document-generator/README.md")
kit_readme = kit_readme.replace(
    "→ exact Golden render\n→ output/v<document.version>/prd.html",
    "→ one deterministic delivery pass\n→ output/README.md\n→ output/v<document.version>/{prd.html, context.md, index.json}",
    1,
)
kit_readme = kit_readme.replace("│   ├── render.py", "│   ├── delivery.py\n│   ├── render.py", 1)
kit_readme = kit_readme.replace(
    "`production_assets_objective.py` composes objective-first mixed Production Assets.",
    "`delivery.py` is the normal handoff entry point and generates the human PRD plus compact AI side documents in one pass. `production_assets_objective.py` composes objective-first mixed Production Assets.",
    1,
)
kit_readme = kit_readme.replace(
    "All downstream content is rerendered into the same `output/v<document.version>/prd.html`.",
    "All current delivery surfaces are regenerated together from the same canonical project truth. The human PRD remains `prd.html`; `context.md` and `index.json` are derived AI reading aids only.",
    1,
)
write("kits/project-document-generator/README.md", kit_readme)

validation = read("kits/project-document-generator/VALIDATION.md")
old_handoff = """Handoff must point to the current canonical content, projection, rendered HTML, acceptance record, and handoff note; its accepted PRD version must match `render-data.document.version`.

Human-facing handoff notes should identify the current artifacts and material status. Do not duplicate checksum tables or internal validation transcripts when Git state and the validators already own those checks.
"""
new_handoff = """Handoff must point to the current canonical content/projection, acceptance record, `output/README.md`, and the matching versioned `prd.html` / `context.md` / `index.json` bundle. The accepted PRD version must use semantic `X.Y.Z` and match `render-data.document.version` plus the version declared by the side documents.

`output/README.md` is the human/AI resume navigator, not a second project-status database. It identifies the current artifact set and reading route; implementation progress remains owned by the implementation repository. Do not duplicate checksum tables or internal validation transcripts when Git state and the validators already own those checks.
"""
if old_handoff not in validation:
    raise SystemExit("VALIDATION.md: handoff paragraph not found")
write("kits/project-document-generator/VALIDATION.md", validation.replace(old_handoff, new_handoff, 1))

# Voice validator follows the explicit project_html state pointer; no legacy path fallback.
voice_validator = read("kits/voice-production-kit/validator/validate.py")
old = '    html_path=p/"output/final.html"; docx=p/"output/Voice Production.docx"\n'
new = '''    state_text=state.read_text(encoding="utf-8")
    html_match=re.search(r"(?m)^\\s*project_html:\\s*(.*?)\\s*$", state_text)
    html_ref=html_match.group(1).strip() if html_match else ""
    html_path=(p/html_ref) if html_ref else None
    docx=p/"output/Voice Production.docx"
'''
if old not in voice_validator:
    raise SystemExit("Voice validator: hardcoded HTML path not found")
voice_validator = voice_validator.replace(old, new, 1)
voice_validator = voice_validator.replace("if html_path.is_file():", "if html_path is not None and html_path.is_file():")
voice_validator = voice_validator.replace(
    'print("project_html="+("passed" if html_path.is_file() else "not_provided"))',
    'print("project_html="+("passed" if html_path is not None and html_path.is_file() else "not_provided"))',
)
write("kits/voice-production-kit/validator/validate.py", voice_validator)

voice_tests = read("tests/test_voice_contracts.py")
voice_tests = voice_tests.replace(
    '(project / "output").mkdir(parents=True)\n',
    '(project / "output").mkdir(parents=True)\n        (project / "output" / "v1.0.0").mkdir(parents=True)\n',
    1,
)
voice_tests = voice_tests.replace(
    '"status: voice_script_ready\\nrevision: contract-1\\n",',
    '"status: voice_script_ready\\nrevision: contract-1\\nproject_html: output/v1.0.0/prd.html\\n",',
    1,
)
voice_tests = voice_tests.replace("output/final.html", "output/v1.0.0/prd.html")
write("tests/test_voice_contracts.py", voice_tests)

voice_agents = read("kits/voice-production-kit/AGENTS.md")
old_command = """python kits/project-document-generator/renderer/render.py \\
  workspace/active/<project>/work/render-data.json \\
  workspace/active/<project>/output/v<document.version>/prd.html
"""
new_command = """python kits/project-document-generator/renderer/delivery.py \\
  workspace/active/<project>/
"""
if old_command not in voice_agents:
    raise SystemExit("Voice AGENTS: old render command not found")
voice_agents = voice_agents.replace(old_command, new_command, 1)
voice_agents = voice_agents.replace("when consolidated `prd.html` exists", "when the current versioned `prd.html` exists")
write("kits/voice-production-kit/AGENTS.md", voice_agents)

# First real migrated project: Clockwork accepted handoff becomes semantic v1.0.0.
replace_required("workspace/active/the-clockwork-vault/work/content.md", "- Version: Final Review", "- Version: 1.0.0", count=1)
replace_required("workspace/active/the-clockwork-vault/work/render-data.json", '"version": "Final Review"', '"version": "1.0.0"', count=1)
replace_required("workspace/active/the-clockwork-vault/work/voice-requirements.md", "Source PRD revision: Final Review", "Source PRD revision: 1.0.0", count=1)
replace_required(
    "workspace/active/the-clockwork-vault/work/voice-production.md",
    "Source Voice Requirements: Final Review / work/voice-requirements.md",
    "Source Voice Requirements: 1.0.0 / work/voice-requirements.md",
    count=1,
)

write(
    "workspace/active/the-clockwork-vault/state/handoff-state.yaml",
    """project: the-clockwork-vault
status: handoff_ready
accepted_prd_version: 1.0.0
content: work/content.md
render_data: work/render-data.json
html: output/v1.0.0/prd.html
context: output/v1.0.0/context.md
index: output/v1.0.0/index.json
acceptance: work/acceptance.md
handoff: output/README.md
""",
)
voice_state = read("workspace/active/the-clockwork-vault/state/voice-state.yaml")
voice_state = voice_state.replace("source_prd_revision: Final Review", "source_prd_revision: 1.0.0")
voice_state = voice_state.replace("project_html: output/final.html", "project_html: output/v1.0.0/prd.html")
write("workspace/active/the-clockwork-vault/state/voice-state.yaml", voice_state)

write(
    "docs/knowledge/next-action.md",
    """# Next Action

## Current Status

`VERSIONED_AI_HANDOFF_READY`

Project Document Generator v1.14.0 now produces one versioned delivery package from the same accepted project truth:

```text
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

`prd.html` remains the human-facing PRD. `context.md` is the AI reasoning surface. `index.json` is a compact heading graph with exact context line ranges, so an AI can locate scope before reading prose. `output/README.md` is the stable resume entry point for a project reopened later.

The design intentionally has no Obsidian/Graphify dependency, knowledge database, second PRD authority, duplicate JSON prose, compatibility alias, or extra workflow layer.

Clockwork is migrated as the first real package at PRD version `1.0.0`; Voice remains semantically unchanged and points to the versioned project HTML.

## Next Step

Use the versioned delivery bundle as the default handoff on the next new or revised real PRD, and adjust only if that real usage exposes a concrete navigation/context defect.
""",
)
