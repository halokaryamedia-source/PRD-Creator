# Project Document Generator Agent Rules

Root `AGENTS.md` owns repository mode, continuity, authority, proof, and skill budget. Root `project-document-production` owns reusable PRD semantic judgment. This file owns **PRD kit routing, file/mechanical ownership, and context economy**.

Detailed normal Production Execution is `SKILL.md`. Exact Flow/representation contracts stay in their named owners; do not duplicate them here.

## Open only the active owner

| Need | Owner |
|---|---|
| Flow 2 source recovery/completion procedure | `SOURCE-INTAKE.md` |
| PRD core 01–03 semantic/visible contract | `CONTENT-CONTRACT.md` |
| non-Voice 04 Production Asset contract | `PRODUCTION-ASSETS.md` |
| render/projection/compositor contract | `RENDERING.md` |
| Flow 4 validation/handoff procedure | `VALIDATION.md` |
| kit terminology only when needed | `GLOSSARY.md` |
| end-to-end normal Production Execution | `SKILL.md` |

Do not broad-read the whole kit by default.

## Semantic vs technical boundary

```text
source / canonical PRD / non-Voice 04 / readiness meaning wrong
→ root project-document-production + smallest semantic owner

semantic contract correct; renderer/template/validator/compositor mechanics wrong
→ exact implementation owner below
```

A technical file does not automatically require the semantic specialist. Conversely, a technical change that would alter what the product/artifact must represent or accept must return to the semantic owner first.

## Implementation ownership

- `renderer/core.py` → reusable rendering helpers/primitives;
- `renderer/pages.py` → PRD render data → approved Golden PRD-core page composition;
- `renderer/render.py` → lower-level deterministic HTML render + downstream composition orchestration;
- `renderer/delivery.py` → versioned delivery bundle + AI reading projections;
- `renderer/production_assets_objective.py` → objective/moment-first mixed 04 composition;
- `renderer/production_assets.py` → Voice-specific parsing/presentation primitives reused by the shared 04 compositor;
- `template/golden-reference.html` → canonical approved Golden reference bytes;
- `template/runtime-template.html` → runtime alias; must remain byte-identical to Golden unless the Golden owner changes;
- `validator/_engine.py` + `validator/validate.py` → PRD mechanical validation;
- `validator/validate_handoff.py` → Flow 4 → Flow 5 handoff consistency.

Renderer/compositor code may organize already-owned canonical information; it may not invent project facts, asset requirements, Voice moments, actor voices, scripts, or decisions.

## Canonical source boundary

```text
approved project model
   ├─ work/content.md
   │  → work/render-data.json
   │  → project HTML 01–03
   └─ optional work/asset-requirements.md
      → project HTML 04 non-Voice resources

optional canonical Voice owners
→ project HTML 04 AUDIO presentation
```

Generated `prd.html`, `context.md`, and `index.json` are derived. Never patch them manually to hide an upstream defect.

Exact 01–03 contract belongs to `CONTENT-CONTRACT.md`. Exact non-Voice 04 contract belongs to `PRODUCTION-ASSETS.md`. Exact Voice semantics belong to the Voice Production owners.

## Context budget

Normal production/maintenance must not load large artifacts merely because they exist.

- canonical PRD-core meaning review → `work/content.md` / relevant requirement state;
- projection investigation → only affected `render-data.json` subtree when practical;
- non-Voice 04 meaning → project model + `work/asset-requirements.md` under `PRODUCTION-ASSETS.md`;
- Voice meaning → Voice canonical owners, not PRD render data;
- Golden/generated HTML → only for concrete template/DOM/runtime/visual evidence needs, in the smallest useful range;
- browser/visual claims → actual rendered/browser evidence.

The renderer/validator may read full large files at runtime; that does not require loading them fully into AI context.

## Bounded changes

For a concrete technical defect:

```text
observe/reproduce or inspect drift
→ confirm semantic contract is already correct
→ exact implementation owner
→ smallest complete fix
→ regenerate only invalidated derived output
→ cheapest proof that can falsify the fix
→ stop
```

Do not reread/rewrite unchanged gameplay sections, redesign adjacent PRD/04 content, or create compatibility layers merely because the current implementation is inconvenient.

## Verification routing

- repository/routing/docs-only changes → `Repository Verify` when its scope owns them;
- PRD renderer/template/validator/compositor/source-contract executable changes → `PRD Verify`;
- Voice canonical/validator behavior → `Voice Verify`;
- browser/visual PASS → actual browser/visual proof;
- generated-audio quality → actual audio evidence.

Do not rerun unrelated Golden/Voice/browser suites for ceremony.

## Anti-overdevelopment boundary

Do not create renderer profiles, generic Asset frameworks/schemas, separate Production Asset Flows/Kits, second HTML outputs, asset manifests, component registries, snapshot systems, template copies, debug artifacts, or new root skills without a concrete current need.

## Boundary

- this kit owns Flow 2–4 procedure/implementation plus bounded non-Voice 04 procedure/implementation;
- root semantic judgment stays in `project-document-production`;
- exact detailed contracts stay in their named kit owners;
- Voice semantics stay in `kits/voice-production-kit/`;
- shared dependencies/tests/CI stay with repository engineering.
