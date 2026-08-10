# Workflow

The Project Document Generator uses three macro steps. Internal files and checks support these steps; they are not separate user-facing approval stages.

```text
1. UNDERSTAND   — Flow 2
2. BUILD PRD    — Flow 3
3. REVIEW       — Flow 4
```

The normal user experience should stay close to:

```text
project source
→ inspect/recover
→ one grouped decision review only if needed
→ build PRD
→ review/fix
→ final accepted PRD
```

Do not turn the internal artifact chain into an 11-step ceremony.

## 1. UNDERSTAND — Flow 2

Follow `SOURCE-INTAKE.md`.

### Internal work

- preserve supplied source and provenance;
- inspect all available authoritative/supporting material before questioning the user;
- register only production-relevant requirements, constraints, conflicts, and decisions;
- classify real gaps as Clarification, Completion, Proposal, or Blocked;
- apply supported Clarification/Completion without unnecessary approval rounds;
- after source inspection is complete, batch remaining high-impact Proposal/Blocked items into one concise decision review when possible.

Detailed state may use:

- `state/source-inventory.yaml`;
- `state/requirement-register.yaml`;
- `state/intake-state.yaml`;
- `work/review.md` only when a human-facing decision/recovery summary is useful.

Do not make the user approve a separate intake report when no material decision is waiting.

**Exit:** `state/intake-state.yaml` truthfully reaches `ready_for_prd`. A material unresolved Proposal/Blocked item prevents this status.

---

## 2. BUILD PRD — Flow 3

Read `CONTENT-CONTRACT.md`. Create/update canonical `work/content.md` from authoritative source, supported recovery, and approved decisions.

The Golden Sample is the approved output authority. Preserve its document foundation and production structure:

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

The goal is **not** to simplify the final document by removing this structure. Efficiency comes from producing the same kind of document with less internal ceremony and less filler.

### Content rule

Use minimum sufficient detail inside the fixed structure:

- keep information that helps a reader understand, build, implement, validate, or avoid guessing;
- do not invent extra mechanics, objects, dimensions, architecture, scoring detail, or narrative just to fill a page;
- when one role has little package-specific work, keep that role page concise and reference the relevant shared/global rule rather than manufacturing detail;
- preserve plain, concrete PRD prose and stable terminology.

### Internal rendering

Treat projection + rendering as implementation details of the same BUILD step:

```text
work/content.md
→ derive work/render-data.json
→ render through Golden Sample template
→ output/final.html
```

Read `RENDERING.md` when projection/rendering is in scope.

`work/render-data.json` is derived. It is not another project-meaning approval stage.

If canonical drafting exposes a real unresolved design decision, return that decision to Flow 2 instead of guessing.

**Exit:** current canonical content is complete, current HTML is rendered through the approved Golden Sample foundation, generated navigation resolves, and no required placeholder remains.

---

## 3. REVIEW — Flow 4

Read `VALIDATION.md`.

### Mechanical check

Run:

```bash
python kits/project-document-generator/validator/validate.py \
  workspace/active/<project>/
```

Mechanical failure means the current PRD cannot be accepted yet. Fix the actual owner: canonical content, projection, renderer, or template mechanics.

### Integrated semantic review

Review the same current revision once through four lenses:

1. New Reader / Player Context;
2. Level Designer;
3. Developer;
4. Project Consistency.

These are four perspectives inside **one review pass**, not four separate reporting ceremonies.

Record each finding once in `work/acceptance.md` with the relevant lens, severity, owner, location, and resolution status.

- Critical or Major → `needs_revision`;
- fix the owning source/content boundary;
- regenerate only invalidated derived output;
- re-review the affected scope;
- a real missing product decision returns to Flow 2.

Writing quality and information density are checked inside these same perspectives. Do not create a separate AI-writing, brevity, or quality-score gate.

**Exit:** mechanical validation passes, all four lenses pass, Critical=0, Major=0, and no unresolved Proposal/Blocked item affects the handed-off scope.

Set `development_ready` only at that point.

## Team Handoff

For the current canonical sequence, `output/team-handoff.md` remains a concise navigation aid after acceptance and `handoff_ready` remains the downstream boundary used by the repository.

Do not treat handoff generation as another content-writing phase and do not copy the PRD into it. It should only point the team to the accepted document and relevant reading route.

## Stop Gate

Flow 4 ends at accepted PRD/team-handoff readiness.

Do **not** claim:

- client sign-off;
- implementation completed;
- QA completed;
- release approved;
- Voice Production requirements already extracted.

If canonical meaning changes later, reopen the affected review boundary, regenerate derived artifacts, and re-audit only what the change invalidated.
