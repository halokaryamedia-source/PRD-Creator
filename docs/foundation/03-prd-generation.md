# Flow 3 — Project Document / PRD Generation

Status: active durable policy

## Purpose

Turn a Flow 2 project marked `ready_for_prd` into canonical production documentation and the derived Golden HTML artifact.

## Single content owner

The gameplay PRD's mandatory blueprint, mandatory-slot states, Scoring / Result behavior, role completeness, and Humanize rules are owned only by:

```text
kits/project-document-generator/CONTENT-CONTRACT.md
```

This foundation page does not maintain a second Golden checklist.

## Authority chain

```text
Original Source + Current Instruction + Approved Decisions
→ Requirement State / ready_for_prd
→ work/content.md                 canonical meaning
→ work/render-data.json           derived projection
→ Golden renderer/template
→ output/final.html               derived presentation
```

Authority decreases downstream. Rendering cannot introduce project meaning.

## Flow 3 work sequence

```text
read resolved requirement state
→ fill the fixed Golden mandatory shell
→ preserve all material role-owned meaning
→ apply one bounded Humanize pass
→ derive render-data once
→ render HTML
→ hand current revision to Flow 4
```

The target is **minimum complete production detail**, not minimal-looking output.

If drafting exposes a material unresolved project/design decision, return the affected requirement to Flow 2. Do not hide the gap with generic prose, guessed values, Golden example facts, or renderer-friendly defaults.

## Projection boundary

`render-data.json` is a disposable projection of current canonical meaning. It must satisfy the deterministic shell rules in `RENDERING.md` but is not a second semantic owner.

The renderer may organize approved meaning into the Golden surfaces. It may not decide whether a mandatory concern is applicable, invent project facts, or repair incomplete Flow 2 recovery.

## Completion

Flow 3 completes when:

- Flow 2 truthfully remains `ready_for_prd`;
- `content.md` satisfies `CONTENT-CONTRACT.md`;
- no material product decision was silently made during authoring;
- render data satisfies the deterministic Golden shell;
- `final.html` is generated from the current projection;
- no unresolved placeholder remains.

Flow 4—not renderer success—decides production readiness.

## Economy

Do not load full Golden HTML during normal authoring, recreate unchanged packages, add duplicate Golden checklists, or use word/row counts as quality proxies.
