# Module Map

Updated: 2026-08-10

Use this note to identify the smallest current owner before creating, moving, or changing repository structure. It maps responsibilities; it does not duplicate implementation detail.

## Current Areas

```text
PRD-Creator/
├─ .agents/skills/                  repository-wide semantic routing specialists
├─ .github/workflows/               automated repository/production gates
├─ tests/                           focused high-risk generic production contracts
├─ tools/                           repository-wide verification utilities
├─ requirements.lock.txt            exact repository verification dependencies
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

Owns reusable repository-wide **work framing and semantic/product-contract judgment**, not every executable implementation surface.

Frozen canonical set after P0.2 re-audit:

```text
development-brief
project-document-production
voice-production
```

P0.2 explicitly separates semantic ownership from pure technical mechanics:

- PRD product/representation/readiness contract → `project-document-production`;
- Voice scope/wording/artifact/delivery contract → `voice-production`;
- pure renderer/validator/builder mechanics → nearest kit implementation owner;
- shared dependency/test/CI mechanics → repository engineering.

Do not create a root skill for renderer, validator, DOCX, Python, artifact engineering, research, evidence, or a file format merely because that surface exists.

### Repository engineering — `requirements.lock.txt`, `tests/`, `tools/`, `.github/workflows/`

Owns repeatable repository-wide engineering contracts.

Current gates:

```text
tools/verify_repository.py
→ .github/workflows/repository-verify.yml

requirements.lock.txt + tests/
→ .github/workflows/production-verify.yml
```

Current responsibilities:

- exact verification dependency environment;
- required owner/navigation/skill-freeze/retirement invariants;
- Python syntax/compile checks;
- focused PRD renderer/validator regression contracts;
- focused Voice builder/validator regression contracts;
- fail-closed CI aggregation.

Repository engineering does **not** own project meaning, PRD semantic readiness, Voice semantic acceptance, browser visual quality, DOCX rendered-page quality, or generated-audio quality.

Do not expand it into broad coverage or packaging machinery without a real repeatable failure/contract need.

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
- `operations/` — backlog, integration/acceptance evidence, boot baselines, ordered remediation;
- `skills/` — skill inventory/routing.

### `kits/project-document-generator/`

Owns actual Flow 2–4 production implementation.

Nearest `AGENTS.md` owns:

- Flow-local read/edit discipline;
- semantic-vs-technical handoff;
- renderer/template/validator contributor rules;
- exact verification commands;
- canonical-vs-derived edit boundary.

Pure renderer/template/validator mechanics remain here when the product/representation contract is already correct.

### `kits/voice-production-kit/`

Owns actual Flow 5–7 production implementation.

Nearest `AGENTS.md` owns:

- Flow-local read/edit discipline;
- semantic-vs-technical handoff;
- builder/validator contributor rules;
- dependency/build/verification commands;
- canonical-script-vs-derived-DOCX boundary.

Pure builder/validator mechanics remain here when Voice semantics/artifact contract are already correct.

### `workspace/`

Owns **project-specific** originals, normalized state, canonical PRD/Voice work, derived artifacts, and project-specific acceptance evidence.

Repository-wide policies/skills/tests must not be stored inside one project package.

## Technical Ownership Rule

```text
semantic/product contract wrong
→ matching root semantic specialist

semantic contract correct
+ executable mechanics wrong
→ nearest kit AGENTS + exact implementation owner

shared dependency/test/CI contract wrong
→ requirements.lock.txt / tests / tools / workflows
```

A pure technical Maintenance task may have **no root specialist**. That is intentional, not missing routing.

If one future repeated technical contract genuinely spans modules and requires reusable specialist procedure beyond repository engineering, re-audit the skill freeze before creating anything.

## Before Creating A New Module Or Note

Ask:

1. Does an existing owner already cover this responsibility?
2. Is it reusable semantic work-routing behavior (`.agents/skills`) or production implementation/procedure (`kits`)?
3. Is it a repeatable repository engineering invariant (`tests`/`tools`/workflow) or project-specific validation?
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
- [Technical Ownership Decision](../decisions/technical-ownership-boundary.md)
