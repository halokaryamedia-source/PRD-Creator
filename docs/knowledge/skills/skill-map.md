# Skill Map

Use this note for repository skill inventory, ownership, and lineage. Use `activation-matrix.md` for routing.

## Repository-Wide Skills

All canonical repository-wide agent skills live under:

`.agents/skills/`

Current frozen set:

| Skill | Canonical path | Function |
|---|---|---|
| `development-brief` | `.agents/skills/development-brief/SKILL.md` | mandatory Developing front door: goal/method/reference separation, execution channel, authority, Build/Acceptance POV, minimal scope, 2–5 criteria, proof budget, final contract gate |
| `project-document-production` | `.agents/skills/project-document-production/SKILL.md` | semantic specialist for Flow 2–4: source recovery, canonical PRD, renderer/template ownership, PRD validation/handoff |
| `voice-production` | `.agents/skills/voice-production/SKILL.md` | semantic specialist for Flow 5–7: Voice extraction, performance script, DOCX generation, Voice validation/delivery |

## Relationship To Production Kits

The root skill architecture and production kits are deliberately separate layers:

```text
AGENTS / development-brief / activation matrix
→ choose semantic owner and proof boundary
→ root specialist when useful
→ affected kit procedure
→ project source/state/canonical work/artifacts
```

### Project Document Generator

Detailed Flow 2–4 procedure stays under:

`kits/project-document-generator/`

The root `project-document-production` specialist does not duplicate every intake/content/render/validation rule. It protects routing, authority, root ownership, and acceptance boundaries.

### Voice Production Kit

Detailed Flow 5–7 procedure stays under:

`kits/voice-production-kit/`

The root `voice-production` specialist does not duplicate all extraction/script/DOCX/validation instructions. It protects the accepted-PRD → Voice scope → wording → derived artifact → acceptance authority chain.

## Phase 1 Consolidation Decisions

### Generic Developing front door

**Decision:** `RECOVER AS ROOT SKILL`.

Useful BuildIT behavior—goal/method separation, Build/Acceptance POV, execution-channel detection, development necessity, acceptance criteria, and proof budget—is domain-independent and was missing from PRD-Creator.

Result: `development-brief`.

### Project Document production capability

**Decision:** `KEEP KIT + ADD ROOT SEMANTIC ROUTER`.

The existing Project Document Generator kit already owns detailed Flow 2–4 production. It should not be moved wholesale into `.agents/skills/`. A root specialist is added only for semantic routing and agent judgment around that owner.

Result: `project-document-production` + existing kit.

### Voice Production capability

**Decision:** `KEEP KIT + ADD ROOT SEMANTIC ROUTER`.

The existing Voice Production Kit already owns detailed Flow 5–7 production. A root specialist is added for semantic routing, authority preservation, and acceptance boundaries without duplicating the kit.

Result: `voice-production` + existing kit.

### Renderer / validator / DOCX builder

**Decision:** `MERGE INTO SEMANTIC OWNER; NO ROOT SKILL`.

These are implementation surfaces, not independent semantic domains:

- PRD renderer/validator → `project-document-production`;
- Voice DOCX builder/validator → `voice-production`.

### Evidence gate

**Decision:** `MOVE TO ROOT AGENTS; NO SKILL`.

Evidence classification is baseline agent behavior and does not consume a specialist slot.

### Reference / Golden Sample handling

**Decision:** `KEEP AS FOUNDATION/KIT POLICY; NO SKILL`.

References demonstrate approved structure/quality but are not independent work owners.

## Skill Freeze Rule

The current three-skill root architecture is frozen after Phase 1.

Do not add another root skill because:

- another file format appears;
- another validation script exists;
- a project has a unique content type;
- a one-off bug needs repair;
- a global/user helper would be convenient to copy locally.

Add/rename/split a skill only when current repeated work proves a distinct reusable semantic owner that cannot be represented by root policy, foundation policy, an existing kit, or one current specialist.

## Capability Audit Vocabulary

Use:

```text
KEEP
RENAME
MERGE
MOVE
DROP
RECOVER
```

Judge by actual trigger/function and semantic ownership, not historical filename or technology.

## Non-Canonical / Retired Concepts

Do not create parallel repository skill roots under `kits/`, `docs/`, or project workspaces.

Kit-local `SKILL.md` files are production procedures, not alternate project-wide routing roots.

Do not recreate the retired generalized Production Document Builder skill architecture as a compatibility layer.

## External Helpers

Global/user capabilities are not copied into the repository solely for availability. If an environment provides focused planning, review, research, testing, or diagnostic helpers, use them conditionally under root routing rules.

## Parent

- [Activation Matrix](activation-matrix.md)
- [Agent Routing Flow](../flow.md)
- [Implementation Map](../implementation-map.md)
