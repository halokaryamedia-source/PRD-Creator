# Operating Architecture Parity Audit

Captured: 2026-08-10
Scope: compare PRD-Creator `Local` operating discipline against BuildIT `Local` by **working method**, not domain content.
Current owner/source: root repository policy and `docs/knowledge/` operating architecture.

## Question

Was PRD-Creator already as strict and operationally disciplined as BuildIT after Flow 1–7 and migration completion?

## Evidence Observed

BuildIT demonstrated additional repository operating mechanisms beyond its product workflow:

- explicit Plan / Developing / Maintenance routing;
- mandatory Developing front door;
- goal vs suggested-method separation;
- Build POV + Acceptance POV;
- 2–5 acceptance criteria and proof budget before implementation;
- semantic specialist budget and activation matrix;
- skill inventory/lineage/freeze rules;
- root-cause/edit gate;
- execution-channel distinction;
- evidence-status escalation;
- agent work-routing flow separate from product flow;
- dedicated Maintenance route;
- module/source ownership maps;
- review evidence lifecycle;
- durable-decision / cross-cutting-change threshold;
- context-boot efficiency baseline.

At capture time PRD-Creator already had strong production semantics, repository continuity, anti-slop rules, Flow-specific validation, and real-project proof, but several of the operating mechanisms above were missing or only implicit.

## Gap Classification At Capture

| Mechanism | State at audit capture |
|---|---|
| Repository memory / boot / one next action | strong |
| Production Flow 2–7 | strong and real-project verified |
| Root work modes | missing |
| Mandatory development front door | missing |
| Semantic root skill architecture | missing |
| Activation matrix / skill lineage / freeze | missing |
| Build POV / Acceptance POV | missing |
| Root-cause / proof economy | partial |
| Module/source ownership routing | partial |
| Dedicated Maintenance workflow | missing |
| Review lifecycle/index | missing |
| Durable-decision/change threshold | missing |
| Context-boot baseline | missing |

## Main Finding

Production completion did **not** equal operating-architecture parity.

The correct target is:

```text
agent operating layer
→ chooses mode / owner / skill / proof

production layer
→ Flow 2–7 procedures inside the correct semantic owner
```

BuildIT's MCP/Blockbench skill names, source tree, CI stack, and domain policies are not requirements for PRD-Creator.

## Recommended Implementation Order

### Phase 1 — Agent Routing + Skill Architecture

- work modes;
- independent judgment;
- development-brief;
- Build/Acceptance POVs;
- semantic specialist budget;
- canonical `.agents/skills/`;
- activation matrix + skill map;
- agent flow + Developing flow.

### Phase 2 — Ownership + Review + Maintenance + Proof Infrastructure

- module/source maps;
- Maintenance flow;
- review graph;
- durable-decision threshold;
- context-boot baseline;
- operating proof matrix.

### Final Acceptance

After the two architecture phases, exercise routing/maintenance against real repository scenarios and audit whether nearest-owner rules or an engineering gate are actually needed. Do not add CI/tests/frameworks only to resemble BuildIT.

## What Could Disprove This

This audit would be superseded if current `Local` already contained equivalent owner/routing/proof mechanisms under other canonical names and real task evidence showed they worked consistently.

At capture time it did not.

## Current Interpretation

Do not use this body as current status. Current implementation meaning is owned by:

- `docs/knowledge/reviews/README.md`;
- `docs/knowledge/next-action.md`;
- current source/docs.
