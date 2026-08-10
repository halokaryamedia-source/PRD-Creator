# Project Workspace

This folder stores project-specific production packages. Reusable behavior belongs under `kits/`; durable workflow policy belongs under `docs/foundation/`.

## Lifecycle

```text
active project → workspace/active/<project>/
saved project  → workspace/saved/<project>/
```

## Active project package after Flow 6

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
│   └── voice-production.md         Flow 6 canonical spoken/performance text
└── output/
    ├── final.html
    ├── team-handoff.md
    └── Voice Production.docx       Flow 6 derived production artifact
```

Use only files the current project actually needs.

## Authority rule

```text
original source / approved decisions
→ requirement state
→ canonical PRD
→ PRD acceptance
→ voice-requirements.md
→ voice-production.md
→ Voice Production.docx
→ Flow 7 delivery state
```

`state/voice-state.yaml` is the downstream lifecycle owner across Flow 5–7. It records status/revision/paths; it does not replace canonical voice content.

A DOCX may be regenerated at any time from the canonical performance script. Do not patch the DOCX as the source of truth.
