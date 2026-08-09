# Workflow

## Stage 1 — Intake

Follow `SOURCE-INTAKE.md`.

1. Resolve the active project package or create `workspace/active/<project-slug>/` when beginning a new repository-backed project.
2. Preserve supplied files as original source; do not rewrite them during intake.
3. Record each available source in `state/source-inventory.yaml`, including provenance, role, and whether it is current, superseded, reference-only, unreadable, or missing.
4. Inspect the Approved Template directly so required document coverage is known, but do not use template/sample-specific content as project fact.
5. Read every available authoritative and supporting Source file before asking detailed questions.

**Exit condition:** every available source is inventoried and inspected or explicitly marked unavailable/unreadable.

## Stage 2 — Requirement Recovery

Normalize material project facts, constraints, terminology, sequences, requirements, and open decisions into `state/requirement-register.yaml`. Every material entry must remain traceable to source evidence or an approved decision.

For each gap, use exactly one recovery class:

### Clarification
Use when the meaning already exists but needs clearer wording or fuller explanation.

### Completion
Use when missing content can be completed from strong contextual support without changing design intent.

### Proposal
Use when the addition changes or defines a design decision, including gameplay, mechanics, scoring logic, progression, learning objectives, win conditions, required quantities, or another material production choice.

### Blocked
Use when source evidence is insufficient or materially conflicting and a reliable decision cannot be recovered.

A source conflict is an evidence condition, not a fifth recovery class. Resolve it from explicit authority/supersession when possible; otherwise the affected requirement becomes Blocked.

Write/update `review.md` with concise entries containing:

- location / requirement ID;
- classification;
- issue;
- supporting source IDs;
- proposed text or required decision;
- impact when material.

Update `state/intake-state.yaml` with one current status and one next step.

**Exit condition:** every material requirement is traceable, and every identified gap has exactly one recovery class.

## Stage 3 — Approval

- Clarification and Completion are ready-to-apply when directly supported and non-design-changing.
- Present only unresolved high-impact Proposal and Blocked items that require user/creative-owner judgment.
- Apply user corrections and record approved material decisions.
- Do not proceed past unresolved Blocked items that affect required output.
- Do not force a discussion round when the source already supports a reliable completion.

**Exit condition:** all required design decisions are approved, explicitly deferred, or isolated outside the requested output.

## Stage 4 — Canonical Content

Create `content.md` from:

- supported Source content;
- approved Clarification;
- approved Completion;
- approved Proposal.

Keep the content aligned with the Approved Template's section hierarchy and Objective Package.

**Exit condition:** every required template section has approved content or an explicitly approved omission.

## Stage 5 — Render

1. Copy `template/approved-document.html` to the requested output path.
2. Replace project-specific content in the copy.
3. Duplicate the existing Objective Package when the objective count differs.
4. Update IDs, anchors, navigation, labels, and page numbering affected by duplicated objectives.
5. Preserve all unrelated HTML, CSS, JavaScript, classes, and components.

The renderer helper may be used for exact literal replacements. Dynamic objective editing must still reuse the existing Objective Package from the cloned template.

**Exit condition:** `final.html` opens with valid navigation, complete approved content, and the unchanged presentation system of the Approved Template.

## Stage 6 — Stop

Deliver the requested files. Do not continue redesigning or extending the document unless the user requests another revision.
