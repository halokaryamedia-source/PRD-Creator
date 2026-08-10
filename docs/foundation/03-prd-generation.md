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
- derived render data passes structural renderer checks;
- `final.html` is generated through the approved Golden family;
- generated navigation resolves;
- no required placeholder remains.

Flow 4—not rendering success—decides development readiness.
