# Project Document Generator

**Version:** 1.10.0

A compact repository-backed system for recovering uneven project direction, solving material documentation/design gaps without inventing product decisions, previewing the recovered gameplay in simple objective-based chat form for user approval, writing practical development-oriented PRD content, projecting it through the approved Golden Sample hierarchy/page composition, and validating whether the current revision is ready for team handoff.

## Normal use

```text
Project Source
→ inventory + authority/relevance inspection
→ explicit facts/rules/exclusions
→ topology + terminology + cross-role implications
→ production coverage + lifecycle + quantitative/clarity/coherence checks
→ problem framing + Resolution Ladder
→ humanized grouped decisions only if needed
→ Simple Chat Preview
→ user correction / approval
→ ready_for_prd
→ Canonical content.md
→ Derived render-data.json
→ Golden Sample projection / render
→ final.html
→ mechanical + one-read multi-lens review
→ development_ready
→ current handoff boundary
```

The skill will:

1. preserve and inventory project sources, including material user instructions that arrive without a file;
2. recover traceable facts, requirements, exclusions, topology, terminology, implications, gaps, and conflicts;
3. record enough source inspection coverage for resumability without rereading unchanged material;
4. check relevant mechanic lifecycle, related numeric consistency, materially vague wording, global/local rule coherence, and authoritative known constraints before drafting;
5. resolve supported Clarification/Completion automatically and use the Resolution Ladder before escalating Proposal/Blocked decisions;
6. recommend one option only when evidence/goals/constraints actually favor it, otherwise present a concise balanced tradeoff;
7. show one simple objective-by-objective Chat Preview before initial PRD generation so the user can correct or approve the recovered gameplay without reading the full production document;
8. keep internal IDs/YAML/provenance/recovery jargon out of that preview and show `Perlu Konfirmasi` only for unresolved material meaning;
9. write canonical PRD content using `CONTENT-CONTRACT.md` only after the preview-approved Flow 2 boundary, keeping Gameplay, Level Design, and Developer responsibilities separate;
10. render project facts through the approved Golden hierarchy, component composition, and presentation foundation without adding new meaning;
11. keep project language availability explicit instead of presenting an unavailable translation as supported;
12. run mechanical validation plus one-read New Reader / Level Designer / Developer / Project Consistency review;
13. block handoff on Critical/Major findings and return missed product/design gaps to Flow 2 rather than hiding them downstream.

The Simple Chat Preview is not a new Flow or project artifact. Only material corrections/approval needed for continuity are persisted. Bounded revisions preview only the affected objective/global slice when interpretation changed.

Cross-project rendering keeps the Golden visual language while allowing content-driven variation: project/package count and data-driven requirement density may vary, while the approved Golden page family, component composition, labels, and reading pattern remain fixed.

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

## Project artifact lifecycle through Flow 4

Create only what the active Flow needs.

```text
Flow 2 core
source/originals/
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml

Flow 2 conditional
work/review.md              # only when a user-facing decision/recovery summary adds value

Flow 2 chat checkpoint
Simple Chat Preview         # user-facing chat only; not a file artifact

Flow 3 core/derived
work/content.md
work/render-data.json       # derived
output/final.html           # derived

Flow 4 current handoff boundary
work/acceptance.md
state/handoff-state.yaml
output/team-handoff.md
```

Do not pre-create Voice/downstream artifacts for a PRD-only project.

`handoff_ready` is a production-document readiness status, not client approval, implementation completion, QA completion, or release approval.
