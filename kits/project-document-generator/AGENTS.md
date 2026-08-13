# Project Document Generator Agent Rules

Root `AGENTS.md` owns repository mode, proof, skill budget, continuity, and semantic-vs-technical routing. This file owns PRD kit routing/mechanics plus the narrow **same-HTML Production Assets composition mechanics**.

## Open only the active owner

- Flow 2 → `SOURCE-INTAKE.md`
- Flow 3 content → `CONTENT-CONTRACT.md`
- Flow 3 projection/HTML → `RENDERING.md` only when needed
- Flow 4 → `VALIDATION.md`
- non-Voice Production Asset requirement contract → `PRODUCTION-ASSETS.md`
- downstream Production Assets HTML composition defect → `RENDERING.md` + `renderer/production_assets_objective.py`
- Voice-specific parsing/presentation primitive defect → `renderer/production_assets.py` only when the shared compositor source is otherwise correct
- `WORKFLOW.md` → sequence only when the active Flow is unclear
- `GLOSSARY.md` / `RULES.md` → only for a specific terminology/kit-wide invariant question

Do not broad-read the whole kit by default.

## HTML context budget

Normal production must not load `template/runtime-template.html`, `template/golden-reference.html`, or generated `final.html` in full into model context.

- renderer/validator may read large files directly at runtime;
- canonical PRD meaning review uses `content.md`;
- projection investigation uses only the affected `render-data.json` subtree;
- non-Voice Production Asset requirements stay in project `work/asset-requirements.md`;
- downstream Voice meaning stays in Voice canonical sources, not in PRD render-data or `asset-requirements.md`;
- Golden/HTML source is inspected only for a concrete component/marker/runtime defect or explicit Golden regression audit, in the smallest useful range;
- visual claims require actual rendered/browser/page evidence.

## Canonical boundary

PRD core:

```text
source evidence + current user instruction + approved decisions
→ requirement state
→ content.md
→ render-data.json
→ PRD core in final.html
→ PRD acceptance / handoff evidence
```

Optional downstream production presentation:

```text
accepted PRD
→ optional work/asset-requirements.md
→ optional downstream Voice canonical production source
→ objective-first Production Assets compositor
→ appended professional-only pages in the same final.html
```

`work/asset-requirements.md` owns actionable non-Voice Production Asset requirements only. Voice continues to use `work/voice-requirements.md` / `work/voice-production.md`; the compositor does **not** own Voice requirements, actor decisions, or wording.

Never patch `final.html` manually to hide an upstream PRD, asset-requirement, or Voice defect.

## Implementation ownership

- `PRODUCTION-ASSETS.md` → compact objective-first non-Voice Production Asset requirement contract
- `renderer/core.py` → reusable PRD rendering helpers/primitives
- `renderer/pages.py` → PRD render data → approved Golden PRD-core page composition
- `renderer/render.py` → deterministic base render + optional downstream composition orchestration
- `renderer/production_assets_objective.py` → objective-first Production Assets composition, category omission, shared/non-shared page mapping, and Voice/non-Voice merge
- `renderer/production_assets.py` → Voice-specific parsing and presentation primitives reused by the objective-first compositor
- `template/golden-reference.html` → canonical approved Golden reference bytes
- `template/runtime-template.html` → runtime template alias; must remain byte-identical to Golden
- `validator/validate.py` → mechanical Flow 4 PRD checks
- `validator/validate_handoff.py` → narrow Flow 4 → Flow 5 PRD handoff consistency

Renderer/compositor code may organize already-owned canonical information; it may not invent project facts, asset requirements, Voice moments, actor voices, scripts, or decisions.

## PRD core vs Production Assets

The approved Golden PRD core remains unchanged:

```text
Overview
Gameplay Flow
Development
Gameplay sections → Gameplay Overview / Level Design / Developer
```

For `N` gameplay sections, `6 + 4N` remains the PRD-core page count.

`Production Assets` is downstream professional-only content appended after the PRD core. It is not a new PRD semantic page family and does not alter Golden template bytes.

Current human-facing navigation is objective-first:

```text
04 Production Assets
   <gameplay/shared section title>
      <accepted PRD label>
```

Asset categories are shown **inside** the matching page only:

```text
3D Models
UI & Information
Audio
Cinematic & Presentation
```

A zero-count category is omitted. Voice appears inside the matching gameplay page's `Audio` section and retains its canonical detailed Voice cards.

A downstream-only update may rerender the same HTML without reopening PRD acceptance when `content.md` and `render-data.json` are unchanged. Voice workflow still owns Voice acceptance.

## Efficient production

Initial PRD build:

```text
complete + approve Flow 2 model
→ one purity/humanize pass
→ content.md + direct projection
→ render once
→ validate/review PRD core
```

Downstream Production Assets preparation:

```text
accepted PRD
→ optional actionable non-Voice asset requirements
→ optional Voice Flow 5–6 canonical sources
→ rerender same final.html
→ objective-first Production Assets pages
→ validate only affected downstream scope
```

Bounded PRD revision:

```text
approved PRD delta
→ affected content + cross-references
→ affected projection
→ full deterministic rerender
→ targeted PRD review
```

Do not reread/rewrite unchanged gameplay sections. English-only data should not be duplicated into fake bilingual objects.

## Semantic vs technical

- PRD source/canonical/representation/readiness meaning wrong → root `project-document-production` + smallest semantic owner;
- non-Voice asset requirement wrong → accepted PRD authority + `PRODUCTION-ASSETS.md` contract;
- Voice scope/wording/actor selection wrong → Voice Production owners, not this renderer;
- semantic sources correct but PRD renderer/compositor mechanics wrong → exact implementation owner here.

Do not load a semantic specialist solely as an HTML/Python wrapper.

## Verification and maintenance

For a concrete defect:

```text
observe failure
→ identify first wrong owner
→ smallest complete fix
→ regenerate invalidated derived output
→ cheapest proof that can falsify the fix
→ stop
```

`PRD Verify` is the canonical CI gate for affected PRD/render/compositor contracts. Voice canonical/validator behavior uses `Voice Verify`.

Browser/visual PASS still requires actual browser/visual evidence.

Do not create renderer profiles, generic Asset frameworks/schemas, separate Production Asset Flows/Kits, second HTML outputs, asset manifests, component registries, snapshot systems, template copies, debug artifacts, or new skills without a concrete current need.

## Boundary

- this kit owns semantic Flow 2–4;
- Voice semantics belong to `kits/voice-production-kit/`;
- this kit additionally owns the narrow contract/mechanical composition of accepted downstream production content into the shared project HTML;
- the current non-Voice extension is intentionally limited to objective-first actionable requirements, not a generic asset-management framework;
- shared dependencies/tests/CI belong to repository engineering.
