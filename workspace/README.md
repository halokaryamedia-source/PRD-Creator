# Project Workspace

This folder stores project-specific production packages. Reusable kit behavior belongs under `kits/`; durable workflow policy belongs under `docs/foundation/`.

## Lifecycle

```text
project is being worked on
→ workspace/active/<project-slug>/

project is intentionally finalized/saved
→ workspace/saved/<project-slug>/
```

## Flow 2 Project Package

When a real project begins intake, create only the directories/files it needs:

```text
workspace/active/<project-slug>/
├── README.md
├── source/
│   └── originals/
├── state/
│   ├── source-inventory.yaml
│   ├── requirement-register.yaml
│   └── intake-state.yaml
└── work/
    └── review.md
```

Rules:

- `source/originals/` preserves supplied project files unchanged;
- state files are maintained by the active Project Document Generator intake workflow;
- `work/review.md` is a concise human-readable view of gaps/decisions;
- Flow 3 may add canonical content/rendering files later;
- do not place final deliverables in `source/`;
- do not pre-create empty process files that a project does not need.

Field details live in `../kits/project-document-generator/SOURCE-INTAKE.md`.
