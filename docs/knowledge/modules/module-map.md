# Module Map

Updated: 2026-08-10

Use this note to identify the smallest current owner before creating, moving, or changing repository structure. It maps responsibilities; it does not duplicate implementation detail.

## Current Areas

```text
PRD-Creator/
├─ .agents/skills/                  repository-wide agent routing specialists
├─ docs/
│  ├─ foundation/                   durable production policy
│  └─ knowledge/                    repository memory, ownership, evidence, operations
├─ kits/
│  ├─ project-document-generator/   Flow 2–4 production implementation
│  └─ voice-production-kit/         Flow 5–7 production implementation
└─ workspace/
   ├─ active/                       active project packages
   └─ saved/                        retained project packages
```

## Boundary Rules

### `.agents/skills/`

Owns reusable repository-wide **work framing/routing judgment**, not detailed production procedure.

Frozen canonical set:

```text
development-brief
project-document-production
voice-production
```

Do not create a new root skill for renderer, validator, DOCX, research, evidence, or a file format merely because that surface exists.

### `docs/foundation/`

Owns durable product/production policy:

- product boundaries;
- Flow 1–7 production contracts;
- validation/proof status that is stable enough to guide future work.

It does not own the current task or per-project state.

### `docs/knowledge/`

Owns repository memory:

- `next-action.md` — one active task snapshot;
- `decision-log.md` / `decisions/` — durable decisions and change thresholds;
- `implementation-map.md` / `modules/` — ownership;
- `sources/` — authority routing;
- `reviews/` — evidence/history and current review status;
- `maintenance/` — bug/regression/cleanup workflow;
- `operations/` — backlog, integration proof, retirement/audit notes, boot baselines;
- `skills/` — skill inventory/routing.

### `kits/project-document-generator/`

Owns actual Flow 2–4 behavior:

- source intake/recovery;
- canonical PRD generation;
- approved-shell rendering;
- PRD mechanical/semantic validation and handoff.

Renderer/template/validator are implementation surfaces inside this semantic owner, not separate top-level modules.

### `kits/voice-production-kit/`

Owns actual Flow 5–7 behavior:

- Voice Requirement Extraction;
- final performance wording;
- deterministic DOCX generation;
- Voice validation/delivery.

Builder/validator/reference contracts remain inside this semantic owner.

### `workspace/`

Owns **project-specific** material only:

- original inputs;
- normalized state;
- canonical PRD/Voice work;
- derived artifacts;
- project-specific acceptance evidence.

Repository-wide policies/skills must not be stored inside one project package.

## Before Creating A New Module Or Note

Ask:

1. Does an existing owner already cover this responsibility?
2. Is it reusable work-routing behavior (`.agents/skills`) or production procedure (`kits`)?
3. Is it durable policy (`foundation`) or working memory/evidence (`knowledge`)?
4. Is it project-specific data (`workspace`)?
5. Is a new file required now, or would extending the existing owner be smaller?
6. Would the new owner remain correct if the implementation file format/tool changed?

If ownership is still ambiguous, do not create the file yet. Resolve ownership first.

## Retired Boundary

`Production Document Builder/` is historical Git evidence only and must not be recreated as a compatibility owner.

## Related

- [Implementation Map](../implementation-map.md)
- [Source Map](../sources/source-map.md)
- [Skill Map](../skills/skill-map.md)
- [Workspace Map](../workspace-map.md)
