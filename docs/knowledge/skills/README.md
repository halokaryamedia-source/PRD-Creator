# Skill Catalog

Use this note for repository skill inventory, ownership, and lineage. Use `activation-matrix.md` for routing.

## Repository-Wide Skills

All canonical repository-wide agent skills live under:

`.agents/skills/`

Current frozen set after P0.2 re-audit:

| Skill | Canonical path | Function |
|---|---|---|
| `development-brief` | `.agents/skills/development-brief/SKILL.md` | mandatory Developing front door: goal/method/reference separation, execution channel, authority, Build/Acceptance POV, minimal scope, 2–5 criteria, proof budget, final contract gate |
| `project-document-production` | `.agents/skills/project-document-production/SKILL.md` | semantic/product-contract specialist for Flow 2–4: source recovery, canonical PRD meaning, render representation contract, PRD readiness/handoff |
| `voice-production` | `.agents/skills/voice-production/SKILL.md` | semantic/product-contract specialist for Flow 5–7: Voice scope, performance wording, artifact representation contract, Voice acceptance/delivery |

## Relationship To Production Kits

The root skill architecture and production kits are deliberately separate layers:

```text
AGENTS / development-brief / activation matrix
→ classify semantic/product contract vs executable mechanics
→ root semantic specialist only when useful
→ nearest kit procedure/AGENTS
→ exact implementation/project owner
```

### Project Document Generator

Detailed Flow 2–4 procedure and executable mechanics stay under:

`kits/project-document-generator/`

The root `project-document-production` specialist protects authority, representation meaning, readiness, and handoff contracts. Pure renderer/template/validator mechanics remain kit-local when those semantics are already correct.

### Voice Production Kit

Detailed Flow 5–7 procedure and executable mechanics stay under:

`kits/voice-production-kit/`

The root `voice-production` specialist protects accepted-PRD → Voice scope → wording → artifact meaning → acceptance authority. Pure DOCX builder/validator mechanics remain kit-local when those semantics are already correct.

## Repository Engineering Is Not A Production Skill

Shared executable engineering is owned by:

```text
requirements.lock.txt
tests/
tools/
.github/workflows/
```

Current responsibilities include:

- exact dependency verification environment;
- focused high-risk production contract regressions;
- static repository invariants;
- fail-closed `Production Verify` and `Repository Verify`.

These concerns are reusable repository engineering, but they do not form a production semantic specialist and do not consume the single-specialist slot.

## Consolidation Decisions

### Generic Developing front door

**Decision:** `RECOVER AS ROOT SKILL`.

Useful BuildIT behavior—goal/method separation, Build/Acceptance POV, execution-channel detection, development necessity, acceptance criteria, and proof budget—is domain-independent and was missing from PRD-Creator.

Result: `development-brief`.

### Project Document production capability

**Decision:** `KEEP KIT + KEEP ROOT SEMANTIC ROUTER`.

The existing Project Document Generator kit owns detailed Flow 2–4 production. The root specialist is retained for semantic/product-contract judgment, not as a generic renderer/validator debugger.

Result: `project-document-production` + existing kit.

### Voice Production capability

**Decision:** `KEEP KIT + KEEP ROOT SEMANTIC ROUTER`.

The existing Voice Production Kit owns detailed Flow 5–7 production. The root specialist is retained for Voice semantic/product-contract judgment, not as a generic DOCX/validator debugger.

Result: `voice-production` + existing kit.

### Renderer / validator / DOCX builder — P0.2 refinement

Earlier Phase 1 wording said these implementation surfaces were merged into their semantic owner. P0.2 refines that decision.

**Current decision:** `MOVE PURE MECHANICS TO MODULE-LOCAL; KEEP PRODUCT CONTRACT WITH SEMANTIC OWNER`.

- what PRD rendering/validation is required to represent → `project-document-production`;
- PRD renderer/template/validator executable mechanics → Project Document kit-local owner;
- what Voice script/DOCX/validation is required to represent → `voice-production`;
- Voice DOCX builder/validator executable mechanics → Voice kit-local owner;
- shared dependency/test/CI mechanics → repository engineering.

A root semantic specialist is not mandatory for pure technical Maintenance.

### Candidate production-tooling / Python / artifact-engineering skill

**Decision:** `DROP AS ROOT SKILL + MOVE TO MODULE-LOCAL / REPOSITORY ENGINEERING`.

P0.2 found no distinct cross-kit artifact/runtime contract beyond generic Python execution. PRD HTML and Voice DOCX mechanics have different module contracts, while dependency/test/CI already has a smaller shared owner.

Do not add such a skill merely to mirror BuildIT's TypeScript/Bun/runtime specialist inventory.

### Evidence gate

**Decision:** `MOVE TO ROOT AGENTS; NO SKILL`.

Evidence classification is baseline agent behavior and does not consume a specialist slot.

### Reference / Golden Sample handling

**Decision:** `KEEP AS FOUNDATION/KIT POLICY; NO SKILL`.

References demonstrate approved structure/quality but are not independent work owners.

## Skill Freeze Rule

The current three-skill root architecture was re-audited in P0.2 after real executable production verification and remains frozen.

Freeze meaning:

- root skills represent distinct reusable semantic/product-contract procedure;
- module-local executable ownership does not need a matching root skill;
- repository engineering does not become a production specialist merely because it is shared.

Do not add another root skill because:

- another file format appears;
- another validation/build script exists;
- a project has a unique content type;
- a one-off technical bug needs repair;
- Python/dependency/CI appears in the task;
- a global/user helper would be convenient to copy locally.

Add/rename/split a skill only when current repeated work proves a distinct reusable owner/procedure that cannot be represented by root policy, foundation policy, nearest kit procedure/AGENTS, repository engineering, or one current specialist.

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

Judge by actual trigger/function and ownership, not historical filename, implementation language, or technology.

## Non-Canonical / Retired Concepts

Do not create parallel repository skill roots under `kits/`, `docs/`, or project workspaces.

Kit-local `SKILL.md` / `AGENTS.md` files are production/contributor procedures, not alternate project-wide routing roots.

Do not recreate the retired generalized Production Document Builder skill architecture as a compatibility layer.

Do not create `renderer`, `docx-builder`, `python-tooling`, `artifact-engineering`, or `evidence-gate` root skills from current evidence.

## External Helpers

Global/user capabilities are not copied into the repository solely for availability. If an environment provides focused planning, review, research, testing, or diagnostic helpers, use them conditionally under root routing rules.

## Evidence

P0.2 audit:

`../reviews/technical-ownership-refinement-audit.md`

Durable decision:

`../decisions/technical-ownership-boundary.md`

## Parent

- [Activation Matrix](activation-matrix.md)
- [Work Routing](../work-routing.md)
- [Repository Ownership](../ownership.md)
