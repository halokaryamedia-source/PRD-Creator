# Workflow

## Stage 1 — Intake

Follow `SOURCE-INTAKE.md`. Preserve supplied source, record provenance/authority, and inspect available authoritative/supporting material.

**Exit:** sources inventoried and inspected or explicitly unavailable/unreadable.

## Stage 2 — Requirement Recovery

Normalize material facts, constraints, terminology, sequences, requirements, and decisions into `state/requirement-register.yaml`.

Use exactly one gap class: Clarification, Completion, Proposal, or Blocked.

Update `work/review.md` and `state/intake-state.yaml`.

**Exit:** material requirements are traceable and identified gaps are classified.

## Stage 3 — Decision Resolution

Apply supported Clarification/Completion. Ask only unresolved high-impact Proposal/Blocked decisions. Record approved material decisions.

**Exit:** `state/intake-state.yaml` = `ready_for_prd`.

## Stage 4 — Canonical PRD Content

Read `CONTENT-CONTRACT.md`. Create/update `work/content.md` from authoritative source, recovered requirements, supported recovery, and approved decisions.

Use the canonical hierarchy:

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

If canonical drafting exposes a real unresolved design decision, return it to Flow 2 rather than guessing.

**Exit:** required canonical sections are complete with no unresolved required design decision/placeholder.

## Stage 5 — Rendering Projection

Read `RENDERING.md`. Create/update `work/render-data.json` strictly as a structured projection of `content.md`.

**Exit:** projection contains no new meaning and passes renderer input checks.

## Stage 6 — Render

Run:

```bash
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

**Exit:** current `output/final.html` is generated structurally without changing project meaning.

## Stage 7 — Mechanical Flow 4 Validation

Read `VALIDATION.md`, then run:

```bash
python kits/project-document-generator/validator/validate.py \
  workspace/active/<project>/
```

Mechanical failure means the PRD cannot enter semantic acceptance yet. Fix the canonical owner, projection, renderer, or template according to the actual cause.

**Exit:** mechanical status = `pass`.

## Stage 8 — Four-Perspective Acceptance

Audit the same current revision from:

1. New Reader / Player Context;
2. Level Designer;
3. Developer;
4. Project Consistency.

Record concise evidence/findings in `work/acceptance.md` using Critical/Major/Minor/Suggestion severity.

- Critical or Major → status `needs_revision` and fix the canonical owner.
- If meaning changes, regenerate render-data and rerender before re-audit.
- A real missing product decision returns to Flow 2.

**Exit:** all four perspectives pass, Critical=0, Major=0.

## Stage 9 — Development-Ready Gate

Set `state/handoff-state.yaml` to `development_ready` only when:

- mechanical validation passed;
- all four perspectives passed;
- Critical=0;
- Major=0;
- no unresolved Proposal/Blocked item affects handed-off scope;
- requested language coverage is usable;
- any remaining Minor is intentionally accepted and does not change meaning.

**Exit:** `development_ready`.

## Stage 10 — Team Handoff

Create `output/team-handoff.md` as a concise navigation aid containing accepted revision/paths, project scope, role reading routes, package inventory, global systems, and any accepted non-blocking caveat.

Do not copy the PRD into the handoff file.

Set `state/handoff-state.yaml` to `handoff_ready` and point it to the accepted content, HTML, acceptance report, and handoff file.

**Exit:** `handoff_ready`.

## Stage 11 — Flow 4 Stop Gate

Flow 4 ends at team-handoff readiness.

Do **not** claim:

- client sign-off;
- implementation completed;
- QA completed;
- release approved;
- Voice Production requirements already extracted.

If canonical meaning changes later, reopen Flow 4 to `pending_review`, rerender, and re-audit the affected dependencies.
