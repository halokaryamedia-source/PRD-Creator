# Project Document Generator

**Version:** 1.13.0

Project Document Generator produces the accepted Golden PRD core and can append bounded downstream Production Assets to the same project HTML.

## PRD core

```text
source + approved decisions
→ content.md
→ render-data.json
→ exact Golden render
→ output/final.html
```

The PRD core remains `6 + 4N` pages for `N` gameplay sections. Golden template bytes remain unchanged by downstream composition.

## Downstream Production Assets

Optional non-Voice requirements use:

```text
work/asset-requirements.md
```

Contract owner:

```text
PRODUCTION-ASSETS.md
```

Current categories are:

```text
3D Models
UI & Information
Audio
Visual Effects & Presentation
```

Production Assets is objective-first. Sidebar links identify the gameplay/shared section and accepted PRD label; categories appear inside the page only when they contain assets.

Voice remains canonical in the Voice Production Kit and is merged into the matching page's `Audio → Voice Production` block.

## Package structure

```text
kits/project-document-generator/
├── CONTENT-CONTRACT.md
├── PRODUCTION-ASSETS.md
├── RENDERING.md
├── SOURCE-INTAKE.md
├── VALIDATION.md
├── renderer/
│   ├── render.py
│   ├── production_assets_objective.py
│   ├── production_assets.py
│   ├── core.py
│   └── pages.py
└── template/
    ├── golden-reference.html
    └── runtime-template.html
```

`production_assets_objective.py` composes objective-first mixed Production Assets. `production_assets.py` supplies the existing Voice-specific parsing/presentation primitives.

## Artifact lifecycle

PRD-only projects need no downstream asset files. After PRD handoff, projects may add only the downstream sources they actually use:

```text
work/asset-requirements.md     optional non-Voice requirements
work/voice-requirements.md     Voice only
work/voice-production.md       Voice only
work/voice-acceptance.md       Voice only
state/voice-state.yaml         Voice only
```

All downstream content is rerendered into the same `output/final.html`.

The objective-first compositor has contract coverage for generic asset-only, Voice-only, mixed asset + Voice, zero-category omission, source mapping, and no-downstream no-op behavior.
