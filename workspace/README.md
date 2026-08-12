# Project Workspace

This folder stores project-specific production packages. Reusable behavior belongs under `kits/`; durable workflow policy belongs under `docs/foundation/`.

## Lifecycle

```text
active project → workspace/active/<project>/
saved project  → workspace/saved/<project>/
```

Project packages grow **by Flow**, not by pre-creating the final folder tree.

## Artifact classes

### Core

Create when the owning Flow actually needs the artifact.

Flow 2:

```text
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml
```

Flow 3:

```text
work/content.md              canonical PRD meaning
```

Flow 4/current handoff boundary:

```text
work/acceptance.md
state/handoff-state.yaml
output/team-handoff.md       concise current handoff navigation/status
```

### Conditional source retention

`source/originals/` is **not a folder-shape requirement**.

Keep a supplied original in-repo when later direct inspection/reproduction materially benefits from the bytes being present. A large/static source may remain externally retained when duplicating it adds no production value, provided:

- relevant authority has been inspected to sufficient depth;
- `state/source-inventory.yaml` records unambiguous identity/provenance and the retention boundary;
- file sources record filename and SHA-256 when available/useful for exact continuity;
- current recovered/approved project meaning is persisted in requirement/canonical state.

External retention is not permission to throw away unread authority or replace it with generated output.

### Other conditional artifacts

Create only when the condition exists:

```text
README.md                    project-specific navigation/context only when useful
work/review.md               readable decision/recovery summary only when useful
actual audio/evidence files  only when current scope supplies or produces them
```

Do not create empty placeholder files to make project packages look uniform.

### Derived

Generate from canonical/current state; never hand-edit as authority:

```text
work/render-data.json        derived from canonical PRD
output/final.html            deterministic exact-Golden PRD
output/Voice Production.docx derived from canonical Voice Production script
```

### Downstream

Do not create until the downstream Flow is requested/entered:

```text
state/voice-state.yaml
work/voice-requirements.md
work/voice-production.md
work/voice-acceptance.md
output/Voice Production.docx
```

A PRD-only project does not need Voice files merely because the repository supports Voice later.

## Typical package after Flow 7

A project that actually used the complete PRD + Voice sequence may eventually contain:

```text
workspace/active/<project>/
├── source/originals/             # only if source is retained in-repo
├── state/
│   ├── source-inventory.yaml
│   ├── requirement-register.yaml
│   ├── intake-state.yaml
│   ├── handoff-state.yaml
│   └── voice-state.yaml
├── work/
│   ├── review.md                 # only if useful
│   ├── content.md
│   ├── render-data.json
│   ├── acceptance.md
│   ├── voice-requirements.md
│   ├── voice-production.md
│   └── voice-acceptance.md
└── output/
    ├── final.html
    ├── team-handoff.md
    └── Voice Production.docx
```

This is an **eventual example**, not a bootstrap checklist.

## Authority rule

```text
source evidence + current user instruction + approved decisions
→ requirement state
→ canonical PRD
→ PRD acceptance
→ voice-requirements.md
→ voice-production.md
→ Voice Production.docx
→ voice-acceptance.md / voice-state
```

A source's physical storage location does not change its authority; provenance/status/current user instruction do.

Derived artifacts may be regenerated. Do not patch `final.html` or DOCX as source of truth. Generated audio, when present, is evidence/output and does not replace canonical requirements or script meaning.
