# Flow 3 — Project Document / PRD Generation

Status: active durable policy

## Purpose

Turn Flow 2 `ready_for_prd` project meaning into canonical **PRD core 01–03** content and a deterministic Golden-based HTML projection.

Flow 3 does not own 04 Production Assets writing; required asset meaning already exists in the approved project model and is materialized through the separate 04 owner.

## Two contracts, one PRD

```text
kits/prd-creator/document/CONTENT-CONTRACT.md
→ semantic completeness / material conservation

kits/prd-creator/document/DESIGN-CONTRACT.md
→ approved page/component grammar / Golden presentation
```

Do not treat presentation counts from the reference project as project semantics.

## Authority chain

```text
Original Source + Current Instruction + Approved Decisions
→ Requirement State / ready_for_prd
→ work/content.md                 canonical PRD meaning
→ work/render-data.json           derived projection
→ DESIGN-CONTRACT + Golden runtime
→ output/v<document.version>/prd.html
```

Authority decreases downstream. Rendering cannot introduce project meaning.

## Flow 3 sequence

```text
read resolved requirement state
→ author complete semantic PRD content
→ preserve every material role-owned distinction
→ choose data-driven cardinality inside approved surfaces
→ bounded Humanize pass
→ derive render-data once
→ deterministic render
→ hand current revision to Flow 4
```

The target is **minimum complete production detail**, not minimal-looking output and not sample-count fidelity.

### Adaptive cardinality

Existing approved Flow / Note / Sequence component families may contain however many children current meaning requires.

```text
three real stages → three rendered stages
six real stages → six rendered stages
```

Do not create filler to reach four/five, and do not merge material stages merely to reduce to four/five.

Stable semantic/design questions remain stable where explicitly owned by the contracts—for example Overview facts, Gameplay Context/Main Objective/Result, Gameplay Information rows, table meanings, page family and navigation.

## Projection boundary

`render-data.json` is disposable projection data, not a semantic owner.

The renderer may:

- map semantic content into approved page/component families;
- preserve data-driven child counts;
- derive mechanical summaries already implied by canonical meaning.

It may not:

- decide unresolved product behavior;
- copy Golden sample facts;
- delete material distinctions for layout convenience;
- invent new component families without a design-contract change.

If authoring exposes a material unresolved project/design decision, return the affected requirement to Flow 2. If meaning is complete but the approved design cannot represent it clearly, the design/projection layer is the first wrong owner.

Production Asset briefs do not belong in `render-data.json`; they use `production-assets/CONTRACT.md`.

## Completion

Flow 3 completes when:

- Flow 2 truthfully remains `ready_for_prd`;
- `content.md` satisfies `CONTENT-CONTRACT.md`;
- the projection satisfies `DESIGN-CONTRACT.md` and renderer mechanics;
- no material product decision was silently made during authoring;
- semantic cardinality is conserved;
- current 01–03 HTML is rendered;
- no unresolved placeholder remains.

Flow 4—not renderer success—decides production readiness.

## Economy

Do not load full Golden HTML during ordinary authoring, recreate unchanged packages, add duplicate Golden checklists, move 04 rules into PRD core, or use word/row/sample-card counts as quality proxies.
