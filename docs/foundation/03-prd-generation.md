# Flow 3 — Project Document / PRD Generation

Status: active durable policy

## Purpose

Turn the exact preview-approved Flow 2 requirement revision into canonical **PRD core 01–03** meaning, one strict render projection, and deterministic Golden-based HTML.

Flow 3 does not invent 04 resource meaning. Required non-Voice assets come from the same approved project model and are materialized through the 04 owner.

## Contracts

```text
CONTENT-CONTRACT.md
→ semantic completeness / material conservation / strict projection meaning

DESIGN-CONTRACT.md
→ approved page/component grammar / Golden presentation
```

The executable render-data field contract lives in `shared/render_schema.py`; documentation must not create a second schema.

## Authority chain

```text
current sources + instruction + approved decisions
→ exact approved requirement-register bytes
→ work/content.md                         canonical PRD meaning
→ work/render-data.json                   strict projection + content SHA
→ DESIGN-CONTRACT + Golden runtime
→ output/v<document.version>/prd.html
```

Authority decreases downstream. Rendering cannot introduce project meaning.

## Sequence

```text
verify current Flow 2 approval hash
→ author complete content.md
→ preserve material role distinctions
→ bounded Humanize pass
→ derive one strict render-data projection
→ bind canonical_content_sha256
→ deterministic render
→ hand current revision to Flow 4
```

The target is minimum **complete** production detail, not minimal-looking output or sample-count fidelity.

## Adaptive cardinality

Existing approved Flow / Note / Sequence component families use however many children current meaning requires.

```text
three real stages → three rendered stages
six real stages → six rendered stages
```

Do not create filler and do not merge independent meaning for layout convenience.

Stable semantic questions remain stable where explicitly owned by the contracts, including Overview facts, Gameplay Context/Main Objective/Result, Gameplay Information questions, table meanings, and page/navigation families.

## Strict projection boundary

`render-data.json` is disposable projection data with **one supported vocabulary**.

It must:

- contain `canonical_content_sha256` for exact current `content.md` bytes;
- satisfy `shared/render_schema.py` without unknown/legacy aliases;
- carry explicit package/result topology, including `gameplay.result_model`;
- use explicit bilingual values when bilingual mode is enabled;
- preserve material numeric/percentage/stable-ID invariants across languages.

The renderer may only map, order, escape, wrap, localize, and mechanically present already-resolved data.

It may **not**:

- infer a missing semantic field from another role;
- recover historical aliases;
- synthesize Gameplay scoring/completion meaning from Developer data;
- decide unresolved behavior;
- copy Golden sample facts;
- delete distinctions for layout convenience.

If authoring exposes an unresolved material decision, return the affected requirement to Flow 2. If the meaning is correct but the approved design cannot represent it, the design/projection layer is the first wrong owner.

Production Asset briefs remain outside render-data and use `production-assets/CONTRACT.md`.

## Completion

Flow 3 completes only when:

- Flow 2 approval still matches exact current requirement-register bytes;
- `content.md` satisfies `CONTENT-CONTRACT.md`;
- `render-data.json` is a current strict projection of that content;
- semantic cardinality is conserved;
- current 01–03 HTML is rendered from the exact projection;
- no material product decision was silently made during authoring;
- no unresolved placeholder remains.

Flow 4—not renderer success—decides accepted production readiness.

## Economy

Do not load full Golden HTML during ordinary authoring, maintain compatibility aliases, recreate unchanged packages, duplicate validation schemas in prose, move 04 rules into PRD core, or use word/card counts as quality proxies.
