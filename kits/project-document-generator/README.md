# Project Document Generator

**Version:** 1.1.0

A compact repository-backed system for recovering incomplete project direction, writing practical development-oriented PRD content, and rendering it through the approved HTML presentation shell.

## Normal use

```text
Project Source
→ Source Intake / Requirement Recovery
→ ready_for_prd
→ Canonical content.md
→ Derived render-data.json
→ Approved Template shell render
→ final.html
```

The skill will:

1. preserve and inventory project sources;
2. recover traceable facts, requirements, gaps, and conflicts;
3. resolve supported Clarification/Completion and isolate real Proposal/Blocked decisions;
4. write canonical PRD content using `CONTENT-CONTRACT.md`;
5. keep Gameplay, Level Design, and Developer responsibilities separate;
6. create a derived render projection without adding new meaning;
7. clone the approved HTML shell and regenerate project-owned navigation/pages deterministically;
8. stop before development-readiness/team-handoff approval, which belongs to Flow 4.

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
├── GLOSSARY.md
├── template/
│   └── approved-document.html
└── renderer/
    └── render.py
```

## Repository-backed project structure

```text
workspace/active/<project>/
├── README.md
├── source/originals/
├── state/
│   ├── source-inventory.yaml
│   ├── requirement-register.yaml
│   └── intake-state.yaml
├── work/
│   ├── review.md
│   ├── content.md
│   └── render-data.json
└── output/
    └── final.html
```

## Renderer

`renderer/render.py` preserves the Approved Template's shared presentation shell and replaces only project-owned brand metadata, navigation, document pages, and glossary data. It has no external Python dependencies.

The renderer does not validate whether the PRD is truly development-ready; Flow 4 owns that downstream acceptance decision.
