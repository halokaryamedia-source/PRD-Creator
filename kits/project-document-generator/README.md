# Project Document Generator

**Version:** 1.5.0

A compact repository-backed system for recovering incomplete project direction, writing practical development-oriented PRD content, projecting it through the approved Golden Sample hierarchy and page composition, and validating whether the current revision is ready for team handoff.

## Normal use

```text
Project Source
→ Source Intake / Requirement Recovery
→ ready_for_prd
→ Canonical content.md
→ Derived render-data.json
→ Golden Sample projection / render
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
6. render project facts through the approved Golden hierarchy, component composition, and presentation foundation without adding new meaning;
7. keep project language availability explicit instead of presenting an unavailable translation as supported;
8. run mechanical validation plus New Reader, Level Designer, Developer, and Project Consistency audits;
9. block handoff on Critical/Major findings;
10. produce a concise team handoff for an accepted revision.

Cross-project rendering keeps the Golden visual language while allowing content-driven variation: journey/flow grids use the available Golden width instead of assuming Aftershock's exact item count, and package Terms Used remain role-specific rather than repeating automatically on every role page.

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
