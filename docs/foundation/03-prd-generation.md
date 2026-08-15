# Flow 3 — Project Document / PRD Generation

Status: active durable policy

## Purpose

Turn a Flow 2 project marked `ready_for_prd` into canonical **PRD core 01–03** content and the derived Golden HTML artifact.

Flow 3 does not own the 04 Production Assets writing contract. Real Production Asset needs have already been preserved in the approved project model during Flow 2 and are materialized later through the bounded 04 owner without redesigning 01–03.

## Single content owner

The gameplay PRD core's mandatory blueprint, mandatory-slot states, Scoring / Result behavior, role completeness, and Humanize rules are owned only by:

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

This foundation page does not maintain a second Golden checklist.

## PRD-core authority chain

```text
Original Source + Current Instruction + Approved Decisions
→ Requirement State / ready_for_prd
→ work/content.md                 canonical PRD-core meaning
→ work/render-data.json           derived PRD-core projection
→ Golden renderer/template
→ output/v<document.version>/prd.html → 01–03 derived presentation
```

Authority decreases downstream. Rendering cannot introduce project meaning.

The same approved project model may also feed `work/asset-requirements.md` through `PRODUCTION-ASSETS.md`; that parallel 04 source does not change `content.md`, Golden bytes, or 01–03 authoring rules.

## Flow 3 work sequence

```text
read resolved requirement state
→ fill the fixed Golden mandatory shell
→ preserve all material role-owned meaning
→ apply one bounded Humanize pass
→ derive render-data once
→ render 01–03
→ hand current revision to Flow 4
```

The target is **minimum complete production detail**, not minimal-looking output.

If drafting exposes a material unresolved project/design decision, return the affected requirement to Flow 2. Do not hide the gap with generic prose, guessed values, Golden example facts, renderer-friendly defaults, or downstream asset invention.

## Projection boundary

`render-data.json` is a disposable projection of current canonical PRD-core meaning. It must satisfy the deterministic shell rules in `RENDERING.md` but is not a second semantic owner.

The renderer may organize approved meaning into the Golden surfaces. It may not decide whether a mandatory concern is applicable, invent project facts, or repair incomplete Flow 2 recovery.

Production Asset briefs do not belong in `render-data.json`; they use the separate bounded 04 source owned by `PRODUCTION-ASSETS.md`.

## Completion

Flow 3 completes when:

- Flow 2 truthfully remains `ready_for_prd`;
- `content.md` satisfies `CONTENT-CONTRACT.md`;
- no material product decision was silently made during authoring;
- render data satisfies the deterministic Golden shell;
- `output/v<document.version>/prd.html` contains the current 01–03 projection;
- no unresolved placeholder remains.

Flow 4—not renderer success—decides production readiness.

## Economy

Do not load full Golden HTML during normal authoring, recreate unchanged packages, add duplicate Golden checklists, move 04 rules into the PRD-core contract, or use word/row counts as quality proxies.
