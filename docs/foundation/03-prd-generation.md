# Flow 3 — Project Document / PRD Generation

Status: active durable policy

## Purpose

Turn a Flow 2 project marked `ready_for_prd` into canonical PRD meaning and a deterministic Golden-composed HTML presentation without reintroducing archived process ceremony.

## Authority chain

```text
Original Source + Approved Decisions
→ Requirement State / ready_for_prd
→ work/content.md                 canonical meaning
→ work/render-data.json           derived projection
→ Golden Sample renderer/template
→ output/final.html               derived presentation
```

Authority decreases downstream. Rendering cannot introduce project meaning.

## Canonical content

`work/content.md` is the Flow 3 source of truth. Detailed content/page-composition rules live in `kits/project-document-generator/CONTENT-CONTRACT.md`.

Required gameplay-document hierarchy:

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

Package/page counts follow the project. Golden authority means preserving hierarchy, information rhythm, component language, and presentation foundation—not copying Aftershock-specific facts/counts.

## Flow 2 intake boundary

Flow 3 receives resolved production meaning. It may organize and clarify that meaning, but it must not silently choose a material product rule that Flow 2 should own.

Return the affected requirement to Flow 2 when drafting exposes a material gap in any of these areas:

- topology, package order, global/local ownership, transition, or final result;
- mechanic lifecycle behavior;
- contradictory numeric/timing/count/scoring facts;
- wording so vague that materially different product behavior would still appear compliant;
- global/default rule conflicting with a package-specific exception;
- authoritative known project/platform/production constraint conflicting with requested behavior;
- missing Gameplay / Level Design / Developer implication;
- exclusion/removal or terminology ambiguity;
- another unresolved design/product choice.

Do not solve such a gap by inventing a metric, generic best practice, technical workaround, or renderer-friendly value. Qualitative direction may remain qualitative when it is intentionally so and production can proceed safely.

## Projection and rendering

`render-data.json` is a compact disposable projection. It contains only values required to reproduce canonical meaning through the Golden surfaces.

The active renderer:

- derives project metadata/navigation/pages/glossary from render data;
- preserves Golden hierarchy/page composition/component language;
- uses the approved Golden template as runtime presentation authority;
- keeps project-specific local-storage/language/grid behavior bounded;
- never treats the template/sample as project fact.

Normal production does not load the full Golden HTML into model context; renderer/validator consume large HTML directly at runtime.

## Intentionally not adopted

Do not restore archived schema registries, mandatory Guided Discussion/Content Freeze rounds, generic template profiles, release/ZIP/checksum packaging, or visual similarity scoring without a concrete current need.

## Flow 3 completion

Flow 3 completes when:

- Flow 2 is truthfully `ready_for_prd`;
- canonical content satisfies the content/Golden composition contract;
- no material Flow 2 intake issue was silently decided during drafting;
- derived render data passes structural renderer checks;
- `final.html` is generated through the approved Golden family;
- generated navigation resolves;
- no required placeholder remains.

Flow 4—not rendering success—decides development readiness.
