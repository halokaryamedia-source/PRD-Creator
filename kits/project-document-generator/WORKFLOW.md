# Workflow

## Stage 1 — Intake

Follow `SOURCE-INTAKE.md`.

1. Resolve/create `workspace/active/<project-slug>/`.
2. Preserve supplied files as original source.
3. Record source provenance/authority in `state/source-inventory.yaml`.
4. Inspect the Approved Template to understand required coverage without promoting sample content into project facts.
5. Read available authoritative/supporting source before detailed questions.

**Exit:** available sources inventoried and inspected or explicitly unavailable/unreadable.

## Stage 2 — Requirement Recovery

Normalize material facts, constraints, terminology, sequences, requirements, and decisions into `state/requirement-register.yaml`.

Use exactly one recovery class for each gap:

- **Clarification** — meaning exists; wording/explanation is weak.
- **Completion** — missing detail can be recovered safely from strong context.
- **Proposal** — a material design decision would be introduced/changed.
- **Blocked** — evidence is insufficient/conflicting for a reliable answer.

Update `work/review.md` and `state/intake-state.yaml`.

**Exit:** material requirements are traceable and identified gaps are classified.

## Stage 3 — Decision Resolution

- Apply supported Clarification/Completion.
- Ask only unresolved high-impact Proposal/Blocked decisions.
- Record approved material decisions.
- Do not force a discussion round when evidence already supports a reliable answer.

Set intake status to `ready_for_prd` only when required blockers are resolved or explicitly outside requested scope.

**Exit:** `state/intake-state.yaml` = `ready_for_prd`.

## Stage 4 — Canonical PRD Content

Read `CONTENT-CONTRACT.md`.

Create/update `work/content.md` from:

- authoritative Source;
- recovered requirement register;
- supported Clarification/Completion;
- approved project decisions.

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

Critical information must be explicit. A package that does not score uses Completion Data instead of an artificial score.

If writing the canonical PRD exposes a real unresolved design decision, return that requirement to Flow 2 rather than guessing inside Flow 3.

**Exit:** required canonical sections are complete and contain no unresolved required design decision/placeholder.

## Stage 5 — Rendering Projection

Read `RENDERING.md`.

Create/update `work/render-data.json` as a structured projection of `content.md`.

Rules:

- projection may reorganize but not reinterpret content;
- stable IDs are lowercase kebab-case;
- package IDs are unique;
- each rendered package contains Gameplay, Level Design, and Developer objects;
- Developer uses scoring or completion data as appropriate;
- project terms/aliases are included only when they exist in canonical content.

**Exit:** render-data contains no meaning absent from `content.md` and passes renderer input checks.

## Stage 6 — Render

Run:

```bash
python kits/project-document-generator/renderer/render.py \
  workspace/active/<project>/work/render-data.json \
  workspace/active/<project>/output/final.html
```

The renderer:

1. reads the approved HTML shell;
2. preserves shared styles/scripts/controls;
3. replaces project brand metadata;
4. regenerates navigation from the current project structure;
5. generates overview/flow/global/package pages using approved component classes;
6. injects project glossary data;
7. blocks invalid IDs, missing package role objects, missing scoring/completion behavior, unresolved placeholders, broken nav targets, or missing template markers.

**Exit:** `output/final.html` is generated structurally without changing project meaning.

## Stage 7 — Flow 3 Stop Gate

Flow 3 is complete when canonical content and rendered HTML exist and the renderer's structural checks pass.

Do **not** claim:

- development-ready;
- team-handoff approved;
- final delivery approved;
- Voice Production ready.

Those downstream claims belong to Flow 4+.
