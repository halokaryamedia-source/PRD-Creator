# Production Document Builder v0.2.0

This is the complete archival package for **Production Document Builder**.
It is built around the approved **AFTERSHOCK V1.8 / Golden Sample v1.0**.

## Approved Golden Sample

Canonical file:

```text
golden-sample/aftershock-golden-sample-v1.0.html
```

Required SHA-256:

```text
6af765b1c40100728b126fe219c88e5f0f734816f6c9a596d1cd90292c380901
```

The approved file contains the 30-page hierarchy, visual system, navigation,
EN/ID switching, Light/Dark mode, View Mode, global glossary tooltip,
collapsible Terms Used, responsive behavior, and print behavior.

## Package Contents

- Root `SKILL.md`
- Eight workflow reference guides
- JSON Schemas and semantic validator
- Locked Golden Sample and manifest
- Golden Template components, CSS, and scripts
- Renderer and HTML validator v0.2
- Complete Game/Map, Multi-Stage, Single Gameplay, System Module, and Specialized profile support
- Valid and invalid schema fixtures
- Renderer, Golden regression, and end-to-end acceptance tests
- Installation, archive, and Golden Sample contract documentation

## Important Distinction

Two render paths are intentionally different:

1. **Golden exact regression** reproduces the approved AFTERSHOCK Golden Sample
   byte-for-byte and must match its SHA-256.
2. **Semantic project rendering** uses the same visual, hierarchy, component,
   and interaction contracts for new project content. New projects naturally
   have different text and may have different page counts.

Generic fixtures are technical tests and must never be presented as Golden
Sample parity. Pre-generated generic HTML outputs are intentionally excluded
from this archive to avoid that confusion.

## Installation

Copy the entire `production-document-builder/` folder as one Skill directory.
Keep `SKILL.md` at the folder root.

Install dependencies:

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Verification

Run the full acceptance suite:

```bash
python tests/run_acceptance_tests.py
```

Run only the exact Golden Sample regression:

```bash
python tests/run_golden_regression_test.py
```

Expected automated results:

```text
Schema and semantic tests: 27/27
Renderer regression tests: 11/11
Golden exact regression: byte-identical
End-to-end acceptance: passed
```

## Rendering a Frozen Workspace

```bash
python scripts/run_pipeline.py <workspace-folder> \
  --html-version 1.0 \
  --equivalence-audit passed
```

Final HTML remains blocked until Structured Content is Frozen and the required
audit gates have passed.

## Trial Status

The DAIGON Circuit real-project trial was paused by the user before the Guided
Discussion phase was approved. It is not included as part of the Skill core and
does not affect the package's automated acceptance status.

## Versions

- Skill: 0.2.0
- Renderer: 0.2
- Template: 1.0
- Schema: 0.1
- Golden Sample: aftershock-1.0
