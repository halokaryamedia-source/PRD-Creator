# Workflow

Project Document Generator has three macro steps. This file is a sequencing reference only; detailed rules live in each Flow owner.

```text
1. UNDERSTAND — Flow 2
2. BUILD PRD  — Flow 3
3. REVIEW     — Flow 4
```

Normal PRD work is **Production Execution**, not repository Developing.

## 1. UNDERSTAND

Owner: `SOURCE-INTAKE.md`.

```text
inventory + inspect material source
→ explicit facts/rules/exclusions
→ topology + terminology
→ cross-role implications
→ production coverage
→ mechanic lifecycle + quantitative coherence
→ problem framing + Resolution Ladder
→ propagate the resolution
→ grouped humanized decisions only if needed
```

Flow 2 should solve supported gaps before questioning the user. If a real choice remains, present one clear recommendation with reason/impact and only meaningful alternatives. Flow 3 must not have to invent package order/global ownership/transitions, lifecycle behavior, numeric corrections, required role implications, removed behavior, terminology, or another material product rule.

Exit: `ready_for_prd`, `needs_decision`, or `blocked`.

## 2. BUILD PRD

Owners: `CONTENT-CONTRACT.md`; `RENDERING.md` only for projection/HTML mechanics.

```text
content.md
→ compact render-data.json
→ deterministic renderer
→ Golden Sample
→ final.html
```

Canonical meaning is completed before the main projection. Do not hand-write HTML, load the full Golden source into model context, or rebuild unchanged projection/packages during bounded revisions.

If drafting discovers a material requirement-recovery gap, return it to Flow 2 instead of making a hidden design choice.

## 3. REVIEW

Owner: `VALIDATION.md`.

```text
mechanical validation
+ one-read multi-lens semantic review
+ actual visual sanity when available
→ fix real findings
→ re-review only invalidated scope
```

The model reviews canonical meaning; the validator handles full HTML mechanics. A package/document slice should be read once and assessed for New Reader, Level Designer, Developer, and Consistency together rather than reread four times.

## Revision fast path

```text
approved bounded change
→ persist authoritative instruction when needed
→ affected requirements + topology/terminology/exclusion/implication checks
→ lifecycle/quantitative/impact checks where invalidated
→ affected content/projection
→ rerender
→ one mechanical check
→ targeted review
```

Do not replay unchanged intake, decisions, packages, or evidence.

## Delivery

Default user delivery is the final PRD plus material adjustments and any real remaining attention item. Internal state/render data/validator output stays internal unless needed.

Do not add stages, template profiles, quality scores, screenshot/pixel systems, or HTML frameworks merely to make the process look rigorous.
