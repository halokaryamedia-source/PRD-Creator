# Workflow

Project Document Generator has three production steps. This file owns **sequence only**; detailed behavior stays in each owner.

```text
Flow 2  UNDERSTAND
Flow 3  BUILD PRD
Flow 4  REVIEW & HANDOFF
```

Normal project creation/revision is Production Execution, not repository Developing.

## Flow 2 — UNDERSTAND

Owner: `SOURCE-INTAKE.md`.

```text
source authority
→ requirement truth
→ one integrated production-readiness pass
→ resolve only material gaps
→ propagate approved meaning
→ ready_for_prd | needs_decision | blocked
```

Exit rule: Flow 3 must not need to invent package order, shared/local ownership, transitions, material role behavior, scoring/result meaning, or another product decision.

Once ready, stop Flow 2. Optional redesign ideas are not part of intake.

## Flow 3 — BUILD PRD

Semantic owner: `CONTENT-CONTRACT.md`.
Projection mechanics: `RENDERING.md` only when needed.

```text
ready requirement state
→ work/content.md
→ bounded Humanize pass
→ work/render-data.json
→ generic approved PRD template + renderer
→ output/final.html
```

`content.md` owns meaning. Projection and HTML are derived.

If authoring exposes a material unresolved decision, return that issue to Flow 2. Do not hide it with prose or renderer-friendly defaults.

## Flow 4 — REVIEW & HANDOFF

Owner: `VALIDATION.md`.

```text
mechanical validation
+ one integrated semantic review
+ targeted desktop visual sanity when actually required/available
→ fix first wrong owner
→ development_ready | handoff_ready
```

Mechanical PASS is not semantic or visual approval.

Review the affected document/package once through the relevant reader lenses rather than rereading it separately for each role.

## Bounded revision

```text
approved change
→ affected Flow 2 truth only
→ affected canonical content/projection
→ rerender
→ one mechanical check
→ targeted semantic/visual review of invalidated scope
→ stop
```

Do not replay unchanged intake, packages, evidence, mobile QA, or downstream Voice work.

## Delivery

Default user delivery is the requested PRD plus material changes/attention items. Internal source inventory, requirement state, render projection, and validator details stay internal unless needed.

Do not add workflow stages, template profiles, quality scores, screenshot systems, or HTML frameworks merely to make the process look more rigorous.
