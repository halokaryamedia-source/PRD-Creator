# Project Workspace

This folder stores project-specific production packages. Reusable behavior belongs under `kits/`; durable workflow policy belongs under `docs/foundation/`.

## Lifecycle

```text
active project → workspace/active/<project>/
saved project  → workspace/archive/<project>/
```

Project packages grow only when the current production stage needs an artifact. Do not pre-create a full folder tree.

## Core project artifacts

```text
Flow 2
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml

Flow 3 — PRD core 01–03
work/content.md              canonical PRD-core meaning
work/render-data.json        deterministic PRD-core projection

Bounded 04 Production Assets, when justified
work/asset-requirements.md   canonical non-Voice 04 resource requirements

Flow 4
work/acceptance.md
state/handoff-state.yaml

Versioned delivery
output/README.md                         stable handoff / resume navigator
output/v<document.version>/prd.html      human-facing project document
output/v<document.version>/context.md    AI development context
output/v<document.version>/index.json    compact AI navigation + context line ranges
```

The normal delivery entry point is:

```bash
python kits/project-document-generator/renderer/delivery.py \
  workspace/active/<project>/
```

`source/originals/`, project-level notes, and other supporting files are conditional. Keep them only when they provide real continuity or production value.

## Version rule

`document.version` is project/PRD release metadata, not an edit counter. The delivery folder adds the `v` prefix:

```text
document.version: 1.0.0
→ output/v1.0.0/
```

A downstream-only Production Assets refresh may regenerate the current version folder when accepted project/PRD meaning did not change.

## 04 Production Assets

Production Asset needs are recovered while the project is understood from discussion/source. They are **not** normally discovered by rereading finished 01–03 and brainstorming extra assets afterward.

The approved project model can feed both:

```text
approved project model
├─ work/content.md → 01–03
└─ work/asset-requirements.md → non-Voice 04
```

Create `work/asset-requirements.md` only when the project has real non-Voice production resources that must be prepared.

The current visible 04 resource types are:

```text
MODEL
ITEM
UI / TEXT
AUDIO
PARTICLE
```

Visible authoring is reader-first and moment-first:

- MODEL / ITEM / PARTICLE → `Function` + literal `Visual Brief` + optional real approved numeric/block `Size`;
- UI / TEXT → `Function` + exact player-facing `Player Text`;
- standalone non-dialogue AUDIO → `Function` + short `Audio Brief`;
- dialogue AUDIO → canonical Voice data from the Voice Production owners.

Do not create gameplay logic, reset/route/threshold behavior, generic sequences, empty categories, duplicate shared assets, speculative decoration, placeholder sizes, or generic metadata such as `States`, `Position`, `Orientation`, `Reuse`, `Used At`, or `Build Specs`.

The current parser still accepts internal source-group headings for backward compatibility:

```text
3D Models
UI & Information
Audio
Visual Effects & Presentation
```

Those headings are **internal storage only**. They are not the visible 04 taxonomy or page dashboard.

When 04 exists, the normal delivery pass regenerates the same current versioned project document:

```text
output/v<document.version>/prd.html
= approved PRD core 01–03
+ 04 Production Assets
```

Production Assets navigation is objective-first and page bodies are moment-first:

```text
04 Production Assets
   Global / Shared Assets      # only when real shared resources exist
   <gameplay section title>
      <accepted PRD label>

page body
→ 01 · <natural gameplay moment>
   → TYPE
   → Resource Name
   → resource-specific fields
```

Gameplay/objective PRD sections remain under `03 Development`; downstream composition does not renumber or rewrite accepted 01–03 page identities.

## Downstream Voice

Create Voice artifacts only after entering Voice Flow 5–7:

```text
state/voice-state.yaml
work/voice-requirements.md
work/voice-production.md
work/voice-acceptance.md
```

Voice remains canonical in those files and is not duplicated into `asset-requirements.md`. Its derived 04 presentation appears as an `AUDIO` resource inside the matching gameplay moment:

```text
AUDIO
<Character> — <Line Title>

Function
...

Voice Preset
...

ElevenLabs Model
Eleven v3

Estimated Duration
...

Prompt
<exact canonical performance payload>
```

Flow 5 Trigger/Purpose/source refs remain in Voice owners and are not visible Production Asset metadata.

## Optional derived exports

```text
output/Voice Production.docx
```

DOCX is produced only when a portable Voice export is requested or useful. It does not replace canonical Voice Production or the versioned project delivery bundle.

## Typical package

A project may eventually contain:

```text
workspace/active/<project>/
├── source/originals/             # conditional
├── state/
│   ├── source-inventory.yaml
│   ├── requirement-register.yaml
│   ├── intake-state.yaml
│   ├── handoff-state.yaml
│   └── voice-state.yaml          # only when Voice is used
├── work/
│   ├── content.md
│   ├── render-data.json
│   ├── acceptance.md
│   ├── asset-requirements.md     # optional non-Voice Production Assets
│   ├── voice-requirements.md     # only when Voice is used
│   ├── voice-production.md       # only when Voice is used
│   └── voice-acceptance.md       # only when Voice is used
└── output/
    ├── README.md
    ├── v<document.version>/
    │   ├── prd.html
    │   ├── context.md
    │   └── index.json
    └── Voice Production.docx     # optional
```

This is an eventual example, not a bootstrap checklist.

## Authority rule

```text
source evidence + current user instruction + approved decisions
→ approved project model
   ├─ canonical PRD core
   └─ optional non-Voice 04 requirements
→ PRD/04 acceptance
→ optional Voice requirements + canonical Voice Production
→ versioned derived delivery surfaces
→ downstream acceptance/state where applicable
```

Derived delivery artifacts may be regenerated. Never patch `prd.html`, `context.md`, `index.json`, or DOCX as a source of truth; fix the canonical owner and regenerate the affected projection.
