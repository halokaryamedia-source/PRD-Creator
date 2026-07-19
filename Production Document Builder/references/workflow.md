# Workflow

## Purpose

Defines the 12 operational phases, their gates, allowed transitions, and blocked
states for every Document Profile.

## Official Workflow

```text
Project Intake
→ Source Audit
→ Guided Discussion
→ Decision Consolidation
→ Structured Content Draft
→ Multi-Perspective Content Audit
→ Consistency Audit
→ User Approval
→ Content Freeze
→ HTML Generation
→ Final HTML Audit
→ Final Delivery
```

User Approval and Content Freeze are separate. Approval records user consent;
Content Freeze locks the approved content version for rendering.

## Phase 1 — Project Intake

**Objective:** understand project identity, source, intended readers, Action Mode,
Document Profile, scope, and output.

**Gate:** source read; Action Mode known; profile selected; intended readers and
scope clear; existing state/artifacts identified.

**Next:** Source Audit.

## Phase 2 — Source Audit

Classify source information as:

- Confirmed
- Needs Clarification
- Missing
- Conflict

Then provide a separate Recommendation, Priority, and Decision Required.
Prioritize structure, sequence, start/end conditions, handoff, scoring/timers,
interruption/reset, level requirements, production detail, then polish.

**Gate:** confirmed facts recorded; blockers/conflicts visible; discussion priority
ordered; one active flow selected.

## Phase 3 — Guided Discussion

Maintain one active flow. Ask three to five related decisions per normal round.
For packages use Gameplay → Level Design → Developer. Run a Mini Audit before
flow approval.

**Gate:** purpose clear; required data explicit; no blocking contradiction;
terminology defined; Mini Audit passed; user approved.

## Phase 4 — Decision Consolidation

Update Decision Log, Assumptions, Project State, affected sections, blockers, and
one `next_step`. Only approved decisions become final requirements.

**Gate:** decisions recorded; assumptions separate; replaced decisions preserved;
affected sections and next step set.

## Phase 5 — Structured Content Draft

Create/update `content/project-content.yaml` according to the active profile.
Unknown critical fields must be visibly open, never hidden placeholders.

**Gate:** required hierarchy exists; critical data explicit or open; scoring or
completion data exists; glossary references exist; approved decisions synchronized.

## Phase 6 — Multi-Perspective Content Audit

Audit as Player/New Reader, Level Designer, Developer, and Project Consistency.
Resolve Critical first, then Major. Product logic corrections require user
approval and Decision Log updates.

**Gate:** Critical=0; Major=0; blocking questions=0; changed dependencies re-audited.

## Phase 7 — Consistency Audit

Verify terminology, package order, quantities, start/end conditions, timers,
weights, handoffs, ownership, interruption, reset, and final result across pages.

**Gate:** no cross-page contradiction; no broken package dependency; critical
values consistent; scoring/result dependencies valid.

## Phase 8 — User Approval

Present reviewed scope and audit result with status:

```text
Content Status: Ready for Approval
```

**Gate:** explicit user approval with no hidden blocker.

## Phase 9 — Content Freeze

Mark approved sections `frozen`, record content/template/schema/Golden versions,
and set `content_frozen: true`.

**Gate:** approval exists; all required sections approved; Critical=0; Major=0;
blockers=0; scoring/completion/glossary/consistency validation passed.

## Phase 10 — HTML Generation

Render Frozen Structured Content through the selected profile and Golden Template.
Generate HTML, ZIP, render report, and status `audit_required`. Renderer may not
change product rules or fill open data.

## Phase 11 — Final HTML Audit

Audit content, hierarchy, navigation, visual parity, interactions, responsive,
and print behavior. Compare against Structured Content and the Golden Sample.

**Gate:** Critical HTML=0; Major HTML=0; interactions/responsive/print passed;
artifacts exist.

## Phase 12 — Final Delivery

Deliver final HTML, ZIP, and concise audit result. Mark status
`approved_for_delivery` only after the audit gate passes.

## Alternate Paths

### Continue

Load latest state, decisions, content, artifact, and resume `next_step`.

### Update

```text
Requested Change → Impact Analysis → Reopen Affected Sections → Update Decision
→ Update Content → Dependency Re-Audit → New Freeze → Re-render → HTML Audit
```

### Audit Only

Inspect without silently modifying source. Report findings and one next step.

### Visual Prototype

Allowed only by explicit request; labeled non-final; returns to normal content
workflow and cannot proceed directly to final delivery.

## Gate Enforcement

When a gate fails, stop. Explain failure, cause, impact, and one next action.
