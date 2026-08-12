# Project Document Generator

**Version:** 1.11.0

A compact repository-backed system for recovering uneven project direction, using the Golden fill map to identify what production detail must exist, completing missing or conflicting material meaning with explicit AI proposals, previewing the complete gameplay model in simple objective-based chat form for user approval, writing practical development-oriented PRD content, projecting it through the approved Golden Sample hierarchy/page composition, and validating whether the current revision is ready for team handoff.

## Normal use

```text
Project Source
→ inventory + authority/relevance inspection
→ explicit facts/rules/exclusions
→ topology + terminology + cross-role implications
→ production coverage + lifecycle + quantitative/clarity/coherence checks
→ Golden fill-map completeness pass
→ concrete AI proposals for missing/conflicting material detail
→ complete Simple Chat Preview
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
4. use the Reverse-derived Golden fill map as a completeness guide for what each objective/global/role surface must eventually answer;
5. keep Golden project facts out of unrelated projects—the Golden supplies slot meaning and structure, not Aftershock mechanics/numbers;
6. complete missing material detail with one concrete project-consistent AI proposal instead of leaving the preview half-empty;
7. keep source-backed meaning and AI-proposed meaning distinct internally until preview approval;
8. select a coherent recommended default when source surfaces conflict or several plausible designs exist, while surfacing uncertainty only when it helps review;
9. reserve `Blocked` / direct user-only questions for cases where no responsible proposal can be formed;
10. propagate recovered/proposed decisions across affected Gameplay, Level Design, Developer, timing/scoring, transition, interruption and reset meaning before preview;
11. show one simple objective-by-objective Chat Preview before initial PRD generation so the user can correct or approve the complete proposed gameplay model without reading the full production document;
12. keep internal IDs/YAML/provenance/recovery jargon out of that preview; optionally show `Saran AI` only for material choices worth calling out;
13. treat approval of the complete preview as approval of the represented pending AI proposals unless the user explicitly corrects/rejects them;
14. write canonical PRD content using `CONTENT-CONTRACT.md` only after the preview-approved Flow 2 boundary, keeping Gameplay, Level Design, and Developer responsibilities separate;
15. render approved project meaning through the Golden hierarchy, component composition, and presentation foundation without adding new meaning during Flow 3;
16. keep project language availability explicit instead of presenting an unavailable translation as supported;
17. run mechanical validation plus one-read New Reader / Level Designer / Developer / Project Consistency review;
18. block handoff on Critical/Major findings and return newly exposed missing material meaning to Flow 2 rather than hiding it downstream.

The Simple Chat Preview is not a new Flow or project artifact. Only material corrections, proposal/approval state, and decisions needed for continuity are persisted. Bounded revisions preview only the affected objective/global slice when interpretation changed.

Cross-project rendering keeps the Golden visual language while allowing content-driven variation: project/package count and data-driven requirement density may vary, while the approved Golden page family, component composition, labels, reading pattern, and slot responsibilities remain fixed.

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
