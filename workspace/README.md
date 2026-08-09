# Project Workspace

This folder stores project-specific production packages. Reusable kit behavior belongs under `kits/`; durable workflow policy belongs under `docs/foundation/`.

## Lifecycle

```text
project is being worked on
→ workspace/active/<project>/

project is intentionally finalized/saved
→ workspace/saved/<project>/
```

## Active project package after Flow 3

```text
workspace/active/<project>/
├── README.md
├── source/
│   └── originals/                 immutable supplied source
├── state/
│   ├── source-inventory.yaml      provenance / source authority
│   ├── requirement-register.yaml  normalized requirements / gaps / decisions
│   └── intake-state.yaml          Flow 2 status (`ready_for_prd` gate)
├── work/
│   ├── review.md                  human-readable recovery review
│   ├── content.md                 canonical PRD content
│   └── render-data.json           derived rendering projection
└── output/
    └── final.html                  rendered PRD artifact
```

Use only files the current project actually needs. Flow 4 will define the development-readiness/handoff state; do not invent additional approval folders or packaging ceremony before that contract exists.

## Authority rule

```text
original source / approved decisions
→ requirement state
→ content.md
→ render-data.json
→ final.html
```

Downstream artifacts never silently outrank upstream authority.
