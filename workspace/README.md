# Project Workspace

This folder stores project-specific production packages. Reusable behavior belongs under `kits/`; durable workflow policy belongs under `docs/foundation/`.

## Lifecycle

```text
active project → workspace/active/<project>/
saved project  → workspace/archive/<project>/
```

Project packages grow only when the current production stage needs an artifact. Do not pre-create a full folder tree.

## Core PRD artifacts

```text
Flow 2
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml

Flow 3
work/content.md              canonical PRD meaning
work/render-data.json        deterministic PRD projection
output/final.html            PRD core at this stage

Flow 4
work/acceptance.md
state/handoff-state.yaml
output/team-handoff.md
```

`source/originals/`, project `README.md`, and `work/review.md` are conditional. Keep them only when they provide real continuity/production value.

## Downstream Production Assets

After the PRD is accepted, non-Voice Production Asset requirements may be added only when real asset production needs them:

```text
work/asset-requirements.md
```

This optional file contains objective-first actionable requirements using only the current categories that actually have assets:

```text
3D Models
UI & Information
Audio
Visual Effects & Presentation
```

A generic entry uses:

```text
Asset Name
Requirement     mandatory
Usage           optional
Content         optional exact player-facing content
```

Do not create component inventories, empty categories, duplicate shared assets, or a second HTML output.

## Downstream Voice

Create only after entering Voice Flow 5–7:

```text
state/voice-state.yaml
work/voice-requirements.md
work/voice-production.md
work/voice-acceptance.md
```

Voice remains canonical in those files and is not duplicated into `asset-requirements.md`.

When any downstream Production Assets exist, the normal PRD renderer rerenders the same project document:

```text
output/final.html
= accepted PRD core
+ 04 Production Assets
```

Production Assets navigation is objective-first:

```text
04 Production Assets
   Global / Shared Assets      # only when present
   <gameplay section title>
      <accepted PRD label>
```

Categories appear inside each page only when non-zero. Voice appears inside the matching gameplay page's `Audio → Voice Production` block.

Gameplay/objective PRD sections remain under `03 Development`; downstream composition does not renumber accepted PRD page identities.

## Optional derived exports

```text
output/Voice Production.docx
```

DOCX is produced only when a portable Voice export is requested or useful. It does not replace canonical Voice Production.

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
    ├── final.html
    ├── team-handoff.md
    └── Voice Production.docx     # optional
```

This is an eventual example, not a bootstrap checklist.

## Authority rule

```text
source evidence + current user instruction + approved decisions
→ requirement state
→ canonical PRD
→ PRD acceptance
→ optional non-Voice asset requirements
→ optional Voice requirements + canonical Voice Production
→ consolidated final.html presentation
→ downstream acceptance/state where applicable
```

Derived artifacts may be regenerated. Never patch `final.html` or DOCX as source of truth.
