# Project Document Generator

**Version:** 1.13.0

A compact repository-backed system for recovering uneven project direction, using the Golden fill map to identify what production detail must exist, completing missing or conflicting material meaning with explicit AI proposals, previewing the complete gameplay model in simple objective-based chat form for user approval, purifying/humanizing the approved model once, projecting that same model through the approved Golden Sample hierarchy/page composition, and validating the current revision with bounded AI/render/review cost.

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
→ one Content Purity + Humanize pass
→ Canonical content.md + direct render-data projection from the same approved model
→ one planned Golden Sample render
→ final.html
→ one mechanical/content-purity + one-read multi-lens review
→ targeted desktop visual sanity
→ development_ready
→ current handoff boundary
```

The skill will:

1. preserve and inventory project sources, including material user instructions that arrive without a file;
2. recover traceable facts, requirements, exclusions, topology, terminology, implications, gaps, and conflicts;
3. record enough source inspection coverage for resumability without rereading unchanged material;
4. use the Reverse-derived Golden fill map as a completeness guide for what each objective/global/role surface must eventually answer;
5. keep Golden project facts and Golden/document-process rules out of unrelated project content—the Golden supplies slot meaning and structure, not project mechanics or PRD-Creator narration;
6. complete missing material detail with one concrete project-consistent AI proposal instead of leaving the preview half-empty;
7. keep source-backed meaning and AI-proposed meaning distinct internally until preview approval;
8. select a coherent recommended default when source surfaces conflict or several plausible designs exist, while surfacing uncertainty only when it helps review;
9. reserve `Blocked` / direct user-only questions for cases where no responsible proposal can be formed;
10. propagate recovered/proposed decisions across affected Gameplay, Level Design, Developer, timing/scoring, transition, interruption and reset meaning before preview;
11. show one simple objective-by-objective Chat Preview before initial PRD generation so the user can correct or approve the complete proposed gameplay model without reading the full production document;
12. keep internal IDs/YAML/provenance/recovery jargon out of that preview; optionally show `Saran AI` only for material choices worth calling out;
13. treat approval of the complete preview as approval of the represented pending AI proposals unless the user explicitly corrects/rejects them;
14. run one Content Purity + Humanize pass after approval: remove process leakage, keep summary surfaces role-pure, use semantic titles, decompose multi-rule prose, and keep visible terminology consistent without deleting material meaning;
15. write `content.md` and derive compact `render-data.json` from the same purified approved model instead of asking AI to independently summarize the project a second time;
16. render approved project meaning through the Golden hierarchy without using HTML generation as the drafting loop;
17. keep initial preview chat-only, plan one full render after approval, and rerender again only after a concrete finding or later approved change;
18. keep revisions bounded: patch affected meaning/projection, rerender the full HTML mechanically once, then review only invalidated scope;
19. use the Golden fill map during normal authoring instead of repeatedly loading the large Golden HTML;
20. keep project language availability explicit instead of presenting an unavailable translation as supported;
21. run full mechanical validation plus one integrated semantic/content-purity review and representative desktop visual sanity for ordinary content-only generation;
22. escalate to full every-page/browser review only when template/CSS/runtime/page-composition changed, a global visual defect is suspected, or the user explicitly requests it;
23. block handoff on Critical/Major findings and return newly exposed missing material meaning to Flow 2 rather than hiding it downstream.

The Simple Chat Preview is not a new Flow or project artifact. Only material corrections, proposal/approval state, and decisions needed for continuity are persisted. Bounded revisions preview only the affected objective/global slice when interpretation changed.

## Content purity / Humanize

The final project PRD should read as though it was written directly for the project team.

Do not leak:

```text
Golden HTML / Golden Sample
PRD-Creator
content.md / render-data.json / final.html
page/template structure
"one Gameplay Overview / Level Design / Developer page"
three-page contract
content-lock / document-production workflow
```

Do not use generic filler labels such as `Global Rule 1` or `Important Note 2`. Name the actual rule.

Summary surfaces stay short because detailed material meaning is **relocated**, not deleted:

```text
Gameplay Result
= player/world state after completion

Developer
= telemetry, scoring formula, storage, interruption, reset
```

When one requirement contains several independent rules, render them as separate bullets/list items in the same owning requirement rather than one dense paragraph.

## Execution economy

```text
MODE A — Understand / Preview
Source → complete model → Chat Preview
No preview HTML, no render-data, no browser QA.

MODE B — Production Render
Approved preview → one purity/humanize pass
→ write content.md + direct render projection from the same model
→ one planned full final.html render
→ one mechanical validation
→ one integrated semantic review
→ representative visual sanity.

MODE C — Revision
Affected meaning only → affected preview if needed
→ purity/humanize affected slice
→ patch content/projection
→ one planned full rerender
→ one mechanical check
→ targeted review.
```

The full HTML file may be rewritten on every approved revision. That deterministic file write is cheaper and safer than adding partial-render/cache infrastructure. Optimize AI reading/reasoning/review scope instead.

The main efficiency gain is **one semantic model, one semantic write**:

```text
approved model
→ purity/humanize once
→ content.md
→ direct render-data projection
```

Do not reread `final.html` or ask the model to rewrite the same project from scratch merely to create rendering data.

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

Flow 3 core/derived — only after preview approval
work/content.md
work/render-data.json       # direct derived projection
output/final.html           # deterministic derived artifact

Flow 4 current handoff boundary
work/acceptance.md
state/handoff-state.yaml
output/team-handoff.md
```

Do not pre-create HTML/render artifacts during the initial chat preview loop. Do not pre-create Voice/downstream artifacts for a PRD-only project.

`handoff_ready` is a production-document readiness status, not client approval, implementation completion, QA completion, or release approval.
