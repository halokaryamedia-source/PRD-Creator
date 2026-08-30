# Development Workflow

Updated: 2026-08-17

This file is the human-readable lifecycle overview for **repository/system Developing**. The canonical implementation procedure is `.agents/skills/development-brief/SKILL.md`; do not duplicate that procedure here.

Normal project Production Execution does **not** use this workflow.

## Entry

Non-trivial Developing begins only after repository continuity is recovered:

```text
AGENTS.md
→ GITHUB_RULES.md Core Rules
→ CONTEXT.md
→ docs/knowledge/next-action.md
→ development-brief
```

`CONTEXT.md` protects stable repository/product boundaries. `next-action.md` protects cross-session continuation. They are mandatory for non-trivial Developing even though later investigation should remain read-minimal.

A read-only `amati / inspect / understand / recover context` request stops after context recovery/reporting and does not enter implementation.

## Lifecycle

```text
recover current context
→ development-brief grounds goal / method / authority / scope / proof
→ development needed?
   ├─ no → explain/reuse + minimum proof → STOP
   └─ yes
      → at most one useful semantic specialist
      → smallest relevant owner/source
      → smallest complete implementation
      → cheapest relevant proof
      → Acceptance POV + original-scope check
      → update only continuity/decision owner whose state actually changed
      → STOP
```

## Owner selection

Use `development-brief` alone when another specialist adds no semantic value.

```text
PRD/source/04/handoff system meaning
→ project-document-production

Voice scope/production/delivery system meaning
→ voice-production

pure technical mechanics with correct semantics
→ nearest kit AGENTS + exact implementation owner

shared dependency/test/CI mechanics
→ repository engineering owner
```

If investigation reveals a second independent problem, finish/reframe the first boundary before switching. Do not stack specialists because the full product eventually contains both PRD and Voice.

## Execution channel

GitHub mechanics, commit/history quality, retries, and GitHub proof boundaries are canonical in root `GITHUB_RULES.md`.

This workflow only adds the Developing selection principle:

```text
bounded repository change fitting current GitHub capability
→ GitHub-capable channel

coordinated multi-file / patch-semantic / local build-runtime need
→ Local or Codex-style workspace with required capability

browser / audio / runtime acceptance claim
→ actual matching capability
```

Do not create temporary Actions, helper architecture, or extra repository files to emulate a missing capability.

## Continuity reconciliation

If `next-action.md` conflicts materially with current source/state:

```text
verify exact current owner
→ determine which record is stale
→ reconcile that owner
→ continue from actual current state
```

Do not implement a stale next step twice. Do not select a nearby TODO/audit finding as replacement work without explicit current authority.

## Completion

Before `Selesai`, re-check:

- original goal and out-of-scope boundary;
- 2–5 acceptance criteria from `development-brief`;
- whether actual proof supports the claimed status;
- whether any current continuity/decision owner truly changed.

Distinguish `implemented` from `verified` when browser/audio/runtime proof remains unavailable.

Do not create a planning note per task. `next-action.md` changes only when the active continuation meaningfully changes; durable decision records require the threshold in `../decisions/recording-policy.md`.

## Related

- [Work Routing](../work-routing.md)
- [Maintenance Workflow](maintenance.md)
- [Decision Recording Policy](../decisions/recording-policy.md)
