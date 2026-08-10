# Project Workspace

This folder stores project-specific production packages. Reusable behavior belongs under `kits/`; durable workflow policy belongs under `docs/foundation/`.

## Lifecycle

```text
active project → workspace/active/<project>/
saved project  → workspace/saved/<project>/
```

## Active project package after Flow 7

```text
workspace/active/<project>/
├── README.md
├── source/
│   └── originals/
├── state/
│   ├── source-inventory.yaml
│   ├── requirement-register.yaml
│   ├── intake-state.yaml
│   ├── handoff-state.yaml
│   └── voice-state.yaml
├── work/
│   ├── review.md
│   ├── content.md
│   ├── render-data.json
│   ├── acceptance.md
│   ├── voice-requirements.md       Flow 5 canonical voice scope
│   ├── voice-production.md         Flow 6 canonical spoken/performance text
│   └── voice-acceptance.md         Flow 7 current revision evidence/findings
└── output/
    ├── final.html
    ├── team-handoff.md
    └── Voice Production.docx       derived Voice production artifact
```

Actual generated audio files are project outputs/evidence only when the current task includes them. Do not invent a mandatory audio folder for script/DOCX-only projects.

## Authority rule

```text
original source / approved decisions
→ requirement state
→ canonical PRD
→ PRD acceptance
→ voice-requirements.md
→ voice-production.md
→ Voice Production.docx
→ voice-acceptance.md / voice-state delivery readiness
```

`state/voice-state.yaml` records lifecycle status/revision/paths; it does not replace canonical Voice content.

A DOCX may be regenerated from the canonical performance script. Do not patch the DOCX as source of truth. If audio exists, it does not replace the script/requirements as project authority.
