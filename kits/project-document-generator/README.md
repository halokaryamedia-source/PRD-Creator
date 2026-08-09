# Project Document Generator

**Version:** 1.2.0

A compact repository-backed system for recovering incomplete project direction, writing practical development-oriented PRD content, rendering it through the approved HTML presentation shell, and validating whether that exact revision is ready for team handoff.

## Normal use

```text
Project Source
→ Source Intake / Requirement Recovery
→ ready_for_prd
→ Canonical content.md
→ Derived render-data.json
→ Approved Template shell render
→ final.html
→ Mechanical + 4-perspective acceptance
→ development_ready
→ team-handoff.md
→ handoff_ready
```

The skill will:

1. preserve and inventory project sources;
2. recover traceable facts, requirements, gaps, and conflicts;
3. resolve supported Clarification/Completion and isolate real Proposal/Blocked decisions;
4. write canonical PRD content using `CONTENT-CONTRACT.md`;
5. keep Gameplay, Level Design, and Developer responsibilities separate;
6. render through the approved presentation shell without adding new meaning;
7. run mechanical validation plus New Reader, Level Designer, Developer, and Project Consistency audits;
8. block handoff on Critical/Major findings;
9. produce a concise team handoff for an accepted revision.

## Package structure

```text
kits/project-document-generator/
├── SKILL.md
├── README.md
├── RULES.md
├── WORKFLOW.md
├── SOURCE-INTAKE.md
├── CONTENT-CONTRACT.md
├── RENDERING.md
├── VALIDATION.md
├── GLOSSARY.md
├── template/
│   └── approved-document.html
├── renderer/
│   ├── render.py
│   ├── core.py
│   └── pages.py
└── validator/
    └── validate.py
```

## Project output after Flow 4

```text
workspace/active/<project>/
├── source/originals/
├── state/
│   ├── source-inventory.yaml
│   ├── requirement-register.yaml
│   ├── intake-state.yaml
│   └── handoff-state.yaml
├── work/
│   ├── review.md
│   ├── content.md
│   ├── render-data.json
│   └── acceptance.md
└── output/
    ├── final.html
    └── team-handoff.md
```

`handoff_ready` is a production-document readiness status, not client approval, implementation completion, QA completion, or release approval.
