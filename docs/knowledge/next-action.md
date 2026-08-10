# Next Action

Updated: 2026-08-10

This is the single active-task snapshot.

## Active Goal

Bring PRD-Creator's **agent operating architecture** to the same level of discipline as BuildIT while preserving PRD-Creator's own domain boundaries and completed Flow 1–7 production pipeline.

## Current Status

`OPERATING_PARITY_PHASE_1_AGENT_ROUTING_SKILLS_IMPLEMENTED`

## Completed — Phase 1

Implemented:

- explicit work modes: Plan / Developing / Maintenance;
- root independent-judgment rule: user owns the goal, agent owns method quality;
- mandatory non-trivial Developing front door: `.agents/skills/development-brief/SKILL.md`;
- Build POV + Acceptance POV contract;
- 2–5 acceptance criteria + minimum-proof budget before implementation;
- root-cause/edit gate;
- ChatGPT→GitHub vs Local/Codex-style execution-channel distinction;
- BuildIT-style minimum useful proof and evidence escalation adapted to this product;
- canonical root skill set:
  - `development-brief`;
  - `project-document-production`;
  - `voice-production`;
- Developing skill budget: `development-brief` + at most one specialist;
- `docs/knowledge/skills/activation-matrix.md` routing rules;
- `docs/knowledge/skills/skill-map.md` ownership/lineage/freeze rules;
- `docs/knowledge/flow.md` agent routing map, explicitly separate from product Flow 2–7;
- `docs/knowledge/flows/development-flow.md` dual Build/Acceptance validation route.

## Preserved Boundaries

Phase 1 does **not**:

- replace or duplicate the detailed `kits/*/SKILL.md` production procedures;
- create renderer/validator/DOCX/evidence skills;
- reopen completed product Flow 1–7;
- recreate retired generic schema/profile/freeze architecture;
- add a large generic skill catalog merely to resemble BuildIT by file count.

## Current Skill Architecture

```text
Developing task
→ development-brief
→ at most one semantic specialist
   ├─ project-document-production  (Flow 2–4)
   └─ voice-production             (Flow 5–7)
→ affected kit/project owner
→ minimum useful proof
→ Acceptance POV gate
```

## Remaining Operating-Parity Gaps

Still not yet at BuildIT parity:

- formal module/ownership map beyond the current implementation map;
- explicit source-authority map;
- dedicated Maintenance workflow + template;
- review evidence lifecycle / `review-graph`;
- durable decision-note threshold / lightweight OpenSpec-style guide;
- context-boot efficiency baseline;
- proof/validation status matrix updated around the new operating layer.

## Next Step

Implement **Phase 2 — Ownership + Review + Maintenance + Proof Infrastructure**: add module/source ownership routing, Maintenance flow, review evidence lifecycle, lightweight durable-decision threshold, and proof/boot baseline without changing production semantics unless a concrete inconsistency is discovered.
