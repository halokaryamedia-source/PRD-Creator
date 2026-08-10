# Project Production Workspace

A repository-first production workspace for turning incomplete project direction into development-ready project documentation, then deriving validated ElevenLabs-ready Voice Production deliverables.

The repository is project memory. Chat history is supporting context, not the authority for current state.

## Branch Model

- `Local` — permanent working/development authority.
- `main` — stable baseline; change only when explicitly requested.
- routine per-flow/per-task branches and PRs are not used.

## Two Architecture Layers

PRD-Creator separates **how the agent works** from **how the product is produced**.

```text
Agent Operating Layer
Plan / Developing / Maintenance
→ development-brief for Developing
→ at most one semantic specialist
→ ownership/source routing
→ minimum useful proof + Acceptance POV

Product Production Layer
Flow 2 → Flow 3 → Flow 4 → Flow 5 → Flow 6 → Flow 7
```

## Agent Operating Layer

Canonical repository-wide skills live under `.agents/skills/`:

```text
development-brief
project-document-production
voice-production
```

- `development-brief` is mandatory for non-trivial Developing tasks.
- Developing may add **at most one** semantic specialist.
- `project-document-production` owns agent judgment/routing around Flow 2–4.
- `voice-production` owns agent judgment/routing around Flow 5–7.
- Maintenance is root-cause-first and does not automatically invoke `development-brief`.
- detailed production procedures remain inside `kits/`; root skills do not duplicate them.

Operating owners:

- `docs/knowledge/flow.md` — agent work-routing map;
- `docs/knowledge/flows/development-flow.md` — Developing contract;
- `docs/knowledge/maintenance/maintenance-flow.md` — Maintenance contract;
- `docs/knowledge/skills/activation-matrix.md` — skill selection;
- `docs/knowledge/skills/skill-map.md` — inventory/lineage/freeze rules;
- `docs/knowledge/modules/module-map.md` — repository-area ownership;
- `docs/knowledge/sources/source-map.md` — source/authority routing;
- `docs/knowledge/reviews/review-graph.md` — current meaning of historical review evidence;
- `docs/knowledge/decisions/change-decision-guide.md` — durable decision / cross-owner change threshold;
- `docs/knowledge/operations/context-boot-baseline.md` — expected efficient boot/routing scenarios.

## Production Flow

```text
Flow 1 — Repository Boot & Project Memory             ✓ implemented
    ↓
Flow 2 — Source Intake & Requirement Recovery         ✓ implemented
    ↓
Flow 3 — Project Document / PRD Generation            ✓ implemented
    ↓
Flow 4 — PRD Validation & Team Handoff                ✓ implemented
    ↓
Flow 5 — Voice Requirement Extraction                 ✓ implemented
    ↓
Flow 6 — ElevenLabs Performance Script Production     ✓ implemented
    ↓
Flow 7 — Voice Validation & Delivery                  ✓ implemented
```

Project Document Generator owns Flow 2–4 under `kits/project-document-generator/`.

Voice Production Kit owns Flow 5–7 under `kits/voice-production-kit/`: accepted PRD → traceable Voice requirements → canonical performance script → derived `Voice Production.docx` → final script/DOCX acceptance.

The replacement Flow 2–7 pipeline passed real-project integration proof using **The Clockwork Vault**, including a real DOCX defect → root fix → rebuild → revalidation cycle.

## Mandatory Session Boot

1. read `AGENTS.md`;
2. read `CONTEXT.md`;
3. read `docs/knowledge/next-action.md`;
4. open only the smallest relevant foundation/source/kit owner;
5. use module/source maps only when ownership/authority is unclear;
6. open the activation matrix only when skill selection is needed.

Do not load the task board, review history, every kit, or saved projects during normal boot unless the active boundary requires them.

## Repository Map

- `AGENTS.md` — repository-wide work modes, authority, independent judgment, root-cause/proof/anti-slop baseline.
- `CONTEXT.md` — stable purpose, terminology, architecture boundaries.
- `.agents/skills/` — canonical repository-wide routing/judgment skills.
- `docs/foundation/` — durable production policy + current proof matrix.
- `docs/knowledge/` — current state, routing, ownership, sources, skills, decisions, maintenance, reviews, operations.
- `kits/project-document-generator/` — detailed PRD intake/generation/validation procedure and implementation.
- `kits/voice-production-kit/` — detailed Voice extraction/script/DOCX/final acceptance procedure and implementation.
- `workspace/active/` — active project packages.
- `workspace/saved/` — retained project packages.

## Core Authority Rule

```text
Source ≠ Requirement State ≠ Canonical PRD ≠ PRD Acceptance ≠ Voice Requirements ≠ Voice Production Script ≠ DOCX ≠ Voice Acceptance ≠ Audio
```

Generated artifacts and successful tooling never silently become higher authority than the canonical work/evidence that produced them.

## Current Proof / Parity State

- Product Flow 1–7: implemented.
- Real-project Flow 2–7 integration: verified on The Clockwork Vault.
- Retired Production Document Builder migration: complete.
- BuildIT-style operating parity Phase 1 — Agent Routing + Skill Architecture: implemented.
- BuildIT-style operating parity Phase 2 — Ownership + Review + Maintenance + Proof Infrastructure: implemented in repository architecture.

Final operating-parity acceptance still requires representative boot/routing/Maintenance scenarios and a final owner/link/proof audit. Do not add CI or another framework merely to mimic BuildIT; add an engineering gate only if current failure evidence justifies it.
