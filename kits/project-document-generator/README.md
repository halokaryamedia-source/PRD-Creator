# Project Document Generator

**Version:** 1.14.0

Project Document Generator turns project discussion + source into the approved PRD core and can complete 04 Production Assets from the same approved project model in the same project HTML.

## PRD core 01–03

```text
source + approved decisions
→ content.md
→ render-data.json
→ one deterministic delivery pass
→ output/README.md
→ output/v<document.version>/{prd.html, context.md, index.json}
```

The PRD core remains `6 + 4N` pages for `N` gameplay sections. Golden template bytes and the existing 01–03 structure/style remain unchanged by 04 composition.

## 04 Production Assets

Concrete Production Asset needs are recovered while the project is understood from discussion/source. They are not normally discovered by rereading generated 01–03 and brainstorming extra assets afterward.

Optional non-Voice requirements use:

```text
work/asset-requirements.md
```

Contract owner:

```text
PRODUCTION-ASSETS.md
```

04 is objective/moment-first. Visible resource types are:

```text
MODEL
ITEM
UI / TEXT
AUDIO
PARTICLE
```

Only resources that actually need to be created/prepared are included. Visual resources use short Function + literal Visual Brief + optional real approved Size. UI / TEXT carries exact player copy. Non-dialogue AUDIO uses a short Audio Brief. Gameplay behavior and generic sequences are not assets.

Voice remains canonical in the Voice Production Kit and is merged into the matching 04 moment as `AUDIO`.

## Package structure

```text
kits/project-document-generator/
├── CONTENT-CONTRACT.md
├── PRODUCTION-ASSETS.md
├── RENDERING.md
├── SOURCE-INTAKE.md
├── VALIDATION.md
├── renderer/
│   ├── delivery.py
│   ├── render.py
│   ├── production_assets_objective.py
│   ├── production_assets.py
│   ├── core.py
│   └── pages.py
└── template/
    ├── golden-reference.html
    └── runtime-template.html
```

`delivery.py` is the normal handoff entry point and generates the human PRD plus compact AI side documents in one pass. `production_assets_objective.py` composes objective/moment-first mixed Production Assets. `production_assets.py` supplies the existing Voice-specific parsing/presentation primitives.

## Artifact lifecycle

Projects use only the sources they need:

```text
work/content.md                canonical PRD-core meaning
work/render-data.json          derived PRD-core projection
work/asset-requirements.md     optional non-Voice 04 requirements
work/voice-requirements.md     Voice only
work/voice-production.md       Voice only
work/voice-acceptance.md       Voice only
state/voice-state.yaml         Voice only
```

All current delivery surfaces are regenerated from their canonical sources into the same project document. The human PRD remains `prd.html`; `context.md` and `index.json` are derived AI reading aids only.

The 04 compositor has contract coverage for generic asset-only, Voice-only, mixed asset + Voice, source mapping, and no-downstream no-op behavior.
