# Workspace Context

Last verified: 2026-08-10
Stability: stable
Owner: workspace

## Purpose

This workspace supports a two-stage production system:

1. turn incomplete/uneven project direction into documentation that developers, level designers, and the wider production team can use;
2. derive validated ElevenLabs-ready Voice Production from accepted project/gameplay/story documentation without inventing upstream design.

The production pipeline and the agent operating layer are separate:

```text
Agent Operating Layer
Plan / Developing / Maintenance
→ semantic owner + proof boundary

Production Layer
Flow 2 → Flow 3 → Flow 4 → Flow 5 → Flow 6 → Flow 7
```

## Agent Operating Layer

Canonical repository-wide skills live only under `.agents/skills/`:

- `development-brief` — mandatory front door for non-trivial Developing work;
- `project-document-production` — semantic specialist for Flow 2–4;
- `voice-production` — semantic specialist for Flow 5–7.

Detailed routing/ownership is owned by:

- `docs/knowledge/flow.md` — Plan / Developing / Maintenance route;
- `docs/knowledge/skills/activation-matrix.md` — skill selection;
- `docs/knowledge/skills/skill-map.md` — skill inventory/lineage/freeze;
- `docs/knowledge/modules/module-map.md` — repository-area ownership;
- `docs/knowledge/sources/source-map.md` — authority/source routing;
- `docs/knowledge/maintenance/maintenance-flow.md` — bug/regression/cleanup route;
- `docs/knowledge/reviews/review-graph.md` — current meaning of historical review evidence;
- `docs/knowledge/decisions/change-decision-guide.md` — durable decision / cross-owner change threshold.

The root skill architecture is intentionally small and frozen. Detailed production procedure remains inside the existing kits rather than being duplicated into root skills.

## Project Document Generator

Current owner: `kits/project-document-generator/`.

```text
project source
→ requirement recovery
→ ready_for_prd
→ canonical content.md
→ rendered final.html
→ PRD acceptance
→ handoff_ready
```

## Voice Production Kit

Current owner: `kits/voice-production-kit/`.

```text
handoff_ready PRD
→ Flow 5 voice-requirements.md
→ voice_requirements_ready
→ Flow 6 voice-production.md
→ Voice Production.docx
→ voice_script_ready
→ Flow 7 voice-acceptance.md
→ voice_delivery_ready
```

Flow 5 owns **which communications exist and what they must communicate**. Flow 6 owns **final spoken wording/performance notation**. Flow 7 owns **revision-specific script/DOCX validation and delivery readiness**.

## Stable Terms

**Development Brief** — pre-implementation contract that separates goal/method/reference, selects authority/POVs/scope, defines 2–5 acceptance criteria, and sets the minimum proof budget.

**Build POV** — semantic expert/owner responsible for making the active change correctly.

**Acceptance POV** — downstream reader/operator/consumer who determines whether the result is actually useful.

**Review Graph** — current-status index for historical review/audit evidence; review bodies remain time-captured.

**Maintenance Flow** — root-cause-first route for bugs/regressions/cleanup that does not automatically invoke `development-brief`.

**Source Authority Map** — routing note that identifies which current owner can support a claim without becoming another source of truth.

**Canonical PRD Content** — `work/content.md`; accepted project meaning used by downstream production.

**Voice Requirement** — justified player-facing communication moment with approved speaker/channel/trigger/purpose/required facts.

**Voice Requirements** — `work/voice-requirements.md`; canonical Flow 5 voice-scope owner.

**Voice Production Script** — `work/voice-production.md`; canonical Flow 6 final spoken/performance wording.

**Voice Production DOCX** — `output/Voice Production.docx`; derived presentation artifact.

**Voice Acceptance** — `work/voice-acceptance.md`; Flow 7 evidence/findings for an exact script/DOCX revision.

**Voice State** — `state/voice-state.yaml`; lifecycle/status owner across Flow 5–7.

**Voice Delivery Ready** — script + DOCX scope has passed current Flow 7 gates. It does not imply generated audio was reviewed unless audio evidence explicitly says so.

**Performance Direction** — concise square-bracket delivery direction; never a new project fact/event.

**Estimated Duration** — expected spoken-duration range; not measured audio proof.

**Audio Evidence** — explicit record of whether actual generated audio was supplied/reviewed (`not_provided`, `partial_review`, `reviewed_passed`, `reviewed_with_findings`).

**Golden Sample / Approved Reference** — demonstrated structure/presentation/performance-quality reference; never automatic project fact or quota.

## Reference State

`kits/voice-production-kit/REFERENCE/Aftershock/README.md` records the audited original Aftershock Voice Production reference contract and source SHA-256. The active builder/validator does not depend on that binary at runtime.

The old paired Aftershock Gameplay HTML V1.2 is not active factual authority; current accepted project PRDs own upstream facts.

## Retired Historical Package

`Production Document Builder/` v0.2.0 has been removed from the live `Local` tree after real-project integration proof and final retirement audit. Its Golden Sample is preserved byte-identically by the active approved template, and Git history is the recovery path for old implementation details.

## Stable Structure

- `.agents/skills/` — canonical repository-wide agent skill root.
- `docs/foundation/` — durable production policy and current proof matrix.
- `docs/knowledge/` — continuity, routing, skills, ownership, sources, maintenance, reviews, decisions, operations.
- `kits/project-document-generator/` — active PRD Flow 2–4 production owner.
- `kits/voice-production-kit/` — active Voice Flow 5–7 production owner.
- `workspace/active/` — active project packages.
- `workspace/saved/` — retained project packages.

## Architecture Principle

```text
Source ≠ Requirement State ≠ Canonical PRD ≠ PRD Acceptance ≠ Voice Requirements ≠ Voice Production Script ≠ DOCX ≠ Voice Acceptance ≠ Audio
```

A successful tool/artifact never silently becomes higher authority than the canonical work/evidence that produced it.

## Current Development State

Production Flow 1–7, The Clockwork Vault real-project integration proof, and retirement of the old Production Document Builder are complete.

BuildIT-style operating parity is a separate improvement track:

- **Phase 1 — Agent Routing + Skill Architecture:** implemented;
- **Phase 2 — Ownership + Review + Maintenance + Proof Infrastructure:** implemented in repository architecture;
- representative boot/routing/Maintenance scenarios still need to be exercised before final operating-parity acceptance.

Production behavior itself is not reopened unless parity acceptance exposes a concrete conflict or missing capability.
