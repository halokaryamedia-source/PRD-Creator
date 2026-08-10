# Module Map

Updated: 2026-08-10

Use this note to identify the smallest current owner before creating, moving, or changing repository structure. It maps responsibilities; it does not duplicate implementation detail.

## Current Areas

```text
PRD-Creator/
├─ .agents/skills/                  repository-wide agent routing specialists
├─ .github/workflows/               narrow automated repository gates
├─ tools/                           repository-wide verification utilities
├─ docs/
│  ├─ foundation/                   durable production policy + proof matrix
│  └─ knowledge/                    memory, ownership, evidence, operations
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

### `.github/workflows/` + `tools/`

Own only **repeatable repository-wide engineering invariants** that are cheap and meaningful on every relevant commit.

Current gate:

```text
tools/verify_repository.py
→ .github/workflows/repository-verify.yml
```

It may enforce ownership/navigation/skill-freeze/retirement/Python-syntax contracts. It must not pretend to replace project semantic review, browser rendering, DOCX visual QA, or actual audio review.

Do not add another workflow/test framework unless a real repeatable failure proves a missing invariant.

### `docs/foundation/`

Owns durable product/production policy and the current validation/proof matrix. It does not own the active task or per-project state.

### `docs/knowledge/`

Owns repository memory:

- `next-action.md` — one active task snapshot;
- `decision-log.md` / `decisions/` — durable decisions and change thresholds;
- `implementation-map.md` / `modules/` — ownership;
- `sources/` — authority routing;
- `reviews/` — evidence/history and current review status;
- `maintenance/` — bug/regression/cleanup workflow;
- `operations/` — backlog, integration/acceptance evidence, boot baselines;
- `skills/` — skill inventory/routing.

### `kits/project-document-generator/`

Owns actual Flow 2–4 behavior. Its nearest `AGENTS.md` now owns Flow-local read/edit discipline because Phase 3 found a real broad-read defect in the old fixed kit reading order.

Renderer/template/validator remain implementation surfaces inside this semantic owner.

### `kits/voice-production-kit/`

Owns actual Flow 5–7 behavior. Existing nearest `AGENTS.md` remains the scoped Flow 5/6/7 routing rule; no additional nested owner is needed.

### `workspace/`

Owns **project-specific** originals, normalized state, canonical PRD/Voice work, derived artifacts, and project-specific acceptance evidence.

Repository-wide policies/skills must not be stored inside one project package.

## Before Creating A New Module Or Note

Ask:

1. Does an existing owner already cover this responsibility?
2. Is it reusable work-routing behavior (`.agents/skills`) or production procedure (`kits`)?
3. Is it a repeatable repository invariant (`tools`/workflow) or project-specific validation?
4. Is it durable policy (`foundation`) or working memory/evidence (`knowledge`)?
5. Is it project-specific data (`workspace`)?
6. Is a new file required now, or would extending the existing owner be smaller?
7. Would the new owner remain correct if the implementation file format/tool changed?

If ownership is still ambiguous, do not create the file yet. Resolve ownership first.

## Retired Boundary

`Production Document Builder/` is historical Git evidence only and must not be recreated as a compatibility owner.

## Related

- [Implementation Map](../implementation-map.md)
- [Source Map](../sources/source-map.md)
- [Skill Map](../skills/skill-map.md)
- [Operating Parity Acceptance](../operations/operating-parity-acceptance.md)
