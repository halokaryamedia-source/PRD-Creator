# Project Workspace

This folder stores project-specific production packages. Reusable kit behavior belongs under `kits/`; durable workflow policy belongs under `docs/foundation/`.

## Lifecycle

```text
project is being worked on
→ workspace/active/<project>/

project is intentionally finalized/saved
→ workspace/saved/<project>/
```

## Active project package after Flow 5

```text
workspace/active/<project>/
├── README.md
├── source/
│   └── originals/                 immutable supplied source
├── state/
│   ├── source-inventory.yaml      provenance / source authority
│   ├── requirement-register.yaml  normalized requirements / gaps / decisions
│   ├── intake-state.yaml          Flow 2 readiness state
│   ├── handoff-state.yaml         Flow 4 accepted PRD revision/readiness
│   └── voice-state.yaml           Flow 5 voice extraction revision/status
├── work/
│   ├── review.md                  human-readable recovery review
│   ├── content.md                 canonical PRD meaning
│   ├── render-data.json           derived rendering projection
│   ├── acceptance.md              Flow 4 acceptance evidence/findings
│   └── voice-requirements.md      canonical justified voice moments
└── output/
    ├── final.html                  rendered PRD artifact
    └── team-handoff.md             concise production navigation aid
```

Flow 6 will add the production voice-script deliverable. Do not invent final voice-script/output paths before that contract is implemented.

## Authority rule

```text
original source / approved decisions
→ requirement state
→ content.md
→ render-data.json
→ final.html
→ PRD acceptance / handoff readiness
→ voice-requirements.md
→ Flow 6 performance script
```

Voice requirements define what communication is justified; they do not contain final spoken wording or ElevenLabs production decisions.
