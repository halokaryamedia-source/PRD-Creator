# Project Document Generator

**Version:** 1.13.0

Repository-backed system for turning uneven project direction into a development-ready gameplay PRD while preserving authority, approved project meaning, the exact Golden page prototype, and bounded proof cost.

## Normal use

```text
Project Source / Current Instruction
→ inventory + authority/relevance inspection
→ recover facts/rules/exclusions/topology/terminology
→ one integrated production-completeness pass
→ concrete Completion / Proposal for material missing or conflicting meaning
→ complete Simple Chat Preview
→ user correction / approval
→ ready_for_prd
→ one Content Purity + Humanize pass
→ content.md + direct render-data projection from the same approved model
→ one deterministic exact-Golden render
→ mechanical validation
→ integrated Semantic Readiness + Material Conservation
→ targeted desktop visual sanity
→ development_ready / handoff_ready
```

The system should solve before asking. Golden tells the agent what each required document surface must be able to answer, but never supplies another project's mechanics, counts, lore, scoring, timings, or implementation facts.

## Production principles

1. **Authority first.** Persist material source/instruction provenance before relying on it.
2. **Source retention is purposeful.** Keep originals in-repo when later direct inspection materially helps; otherwise external retention is allowed when exact identity/provenance is recorded and relevant meaning has already been recovered.
3. **Complete the model before drafting.** Use Completion when one answer is implied; use a concrete Proposal when AI must choose a material default; use Blocked only when no responsible proposal can be formed.
4. **Preview before initial PRD generation.** The Simple Chat Preview is an objective-based chat checkpoint, not another artifact.
5. **Approval promotes proposals.** Pending proposals represented in an approved preview become approved project meaning unless corrected/rejected.
6. **One semantic model, one semantic write.** Purify/humanize once, write `content.md`, and derive `render-data.json` directly from that same approved model.
7. **Golden is canonical presentation.** The visible page family/component language is fixed unless the user explicitly approves a Golden revision.
8. **Do not patch derived HTML.** Fix upstream meaning/projection/renderer ownership and regenerate.
9. **Review once through multiple semantic lenses.** Persist one `Semantic Readiness` result instead of duplicated role/consistency/acceptance PASS fields.
10. **Keep independent proof independent.** Mechanical, Semantic Readiness, Material Conservation, and Visual sanity answer different failure classes.
11. **Bound revisions.** Revisit only invalidated truth/content/projection/review scope; full HTML rerender remains deterministic and cheap.
12. **Stop when ready.** Do not add schemas, checksum registries, preview renderers, screenshot systems, quality scores, or parity machinery without a concrete need.

## Content Purity + Humanize

Run once before the planned render on the approved project model/canonical copy.

Keep visible project copy focused on the project itself. Do not leak PRD-Creator, Golden/template/page-production narration, internal IDs/YAML, or approval mechanics into the PRD.

Humanize by relocating/decomposing, not deleting:

```text
long player-facing Result
→ short readable Result
+ complete technical detail in Developer

one requirement with four independent actions
→ four readable list items in the same owning requirement
```

Material rules, values, exceptions, recovery, scoring, reset, build constraints, and observable results must remain conserved.

## Execution modes

```text
MODE A — Understand / Preview
Source → complete model → Simple Chat Preview
No preview HTML, render-data, or browser QA.

MODE B — Production Render
Approved preview → one purity/humanize pass
→ content.md + direct projection
→ one planned full render
→ one mechanical validation
→ one integrated semantic/material review
→ representative desktop visual sanity.

MODE C — Bounded Revision
Affected meaning only → affected preview if needed
→ affected purity/humanize + canonical/projection update
→ one full deterministic rerender
→ one mechanical check
→ targeted semantic/material/visual review.
```

Optimize AI reading/reasoning/review scope, not file-writing. Do not add partial-render/cache infrastructure merely to avoid rewriting `final.html`.

## Package structure

```text
kits/project-document-generator/
├── AGENTS.md
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
│   ├── golden-reference.html       # canonical approved reference bytes
│   └── runtime-template.html   # runtime alias; byte-identical
├── renderer/
│   ├── render.py
│   ├── _engine.py
│   ├── core.py
│   └── pages.py
└── validator/
    ├── validate.py
    ├── _engine.py
    └── validate_handoff.py
```

## Project artifact lifecycle through Flow 4

Create only what the active Flow actually needs.

```text
Flow 2 core
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml

Flow 2 conditional
source/originals/*            # only when in-repo retention materially helps
work/review.md                # only when a readable decision summary helps

Flow 2 chat checkpoint
Simple Chat Preview           # chat only; not a file artifact

Flow 3 canonical / derived
work/content.md
work/render-data.json
output/final.html

Flow 4 current handoff
work/acceptance.md
state/handoff-state.yaml
output/team-handoff.md
```

A file source retained externally should still be represented unambiguously in `state/source-inventory.yaml`; record filename/hash/retention when available and useful for exact continuity.

Do not pre-create Voice/downstream artifacts for a PRD-only project.

`handoff_ready` means the accepted PRD is usable as the current production reference. It does not mean client approval, implementation completion, gameplay QA, release approval, or Voice completion.
