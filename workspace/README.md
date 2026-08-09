# Project Workspace

This folder stores project-specific production packages. Reusable kit behavior belongs under `kits/`; durable workflow policy belongs under `docs/foundation/`.

## Lifecycle

```text
project is being worked on
→ workspace/active/<project>/

project is intentionally finalized/saved
→ workspace/saved/<project>/
```

## Active project package after Flow 4

```text
workspace/active/<project>/
├── README.md
├── source/
│   └── originals/                 immutable supplied source
├── state/
│   ├── source-inventory.yaml      provenance / source authority
│   ├── requirement-register.yaml  normalized requirements / gaps / decisions
│   ├── intake-state.yaml          Flow 2 readiness state
│   └── handoff-state.yaml         Flow 4 revision-specific readiness state
├── work/
│   ├── review.md                  human-readable recovery review
│   ├── content.md                 canonical PRD meaning
│   ├── render-data.json           derived rendering projection
│   └── acceptance.md              concise mechanical + role-based Flow 4 acceptance
└── output/
    ├── final.html                  rendered PRD artifact
    └── team-handoff.md             concise production navigation aid
```

Use only files the current project needs. `team-handoff.md` is not a second PRD and must not duplicate all requirements.

## Authority rule

```text
original source / approved decisions
→ requirement state
→ content.md
→ render-data.json
→ final.html
→ acceptance evidence / handoff readiness
```

Acceptance records usability of an exact revision; it never silently changes project meaning.
