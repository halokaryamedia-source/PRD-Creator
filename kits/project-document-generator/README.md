# Project Document Generator

**Version:** 1.0.0

A compact skill for completing project documentation and rendering it through an approved HTML template.

## Normal use

Provide the project sources and request a review.

The skill will:

1. preserve and inventory project sources;
2. recover traceable facts, requirements, gaps, and conflicts;
3. prepare Clarification and Completion;
4. separate Proposal and Blocked decisions for approval;
5. create approved canonical content;
6. clone the approved HTML template;
7. replace project-specific content and produce the final HTML.

## Package structure

```text
Project-Document-Generator/
├── SKILL.md
├── README.md
├── RULES.md
├── WORKFLOW.md
├── SOURCE-INTAKE.md
├── GLOSSARY.md
├── template/
│   └── approved-document.html
└── renderer/
    └── render.py
```

## Codex instruction

Point Codex to `SKILL.md` and provide the project source files. Codex must follow the review and approval stages before rendering when Proposal or Blocked items exist.

## Renderer

`renderer/render.py` is a minimal helper. It clones the approved template and applies exact literal replacements from a JSON file. It does not rebuild or redesign the HTML.
