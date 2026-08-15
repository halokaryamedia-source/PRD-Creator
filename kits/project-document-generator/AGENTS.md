# Project Document Generator Agent Rules

Root `AGENTS.md` owns repository mode, proof, skill budget, continuity, and semantic-vs-technical routing. This file owns PRD kit routing/mechanics plus the narrow **same-HTML 04 Production Assets composition mechanics**.

## Open only the active owner

- Flow 2 → `SOURCE-INTAKE.md`
- Flow 3 PRD-core content → `CONTENT-CONTRACT.md`
- Flow 3 PRD-core projection/HTML → `RENDERING.md` only when needed
- Flow 4 → `VALIDATION.md`
- non-Voice 04 Production Asset requirement/writing contract → `PRODUCTION-ASSETS.md`
- downstream 04 HTML composition defect → `RENDERING.md` + `renderer/production_assets_objective.py`
- Voice-specific parsing/presentation primitive defect → `renderer/production_assets.py` only when the shared compositor source is otherwise correct
- `WORKFLOW.md` → sequence only when the active Flow is unclear
- `GLOSSARY.md` / `RULES.md` → only for a specific terminology/kit-wide invariant question

Do not broad-read the whole kit by default.

## HTML context budget

Normal production must not load `template/runtime-template.html`, `template/golden-reference.html`, or generated `prd.html` in full into model context.

- renderer/validator may read large files directly at runtime;
- canonical PRD-core meaning review uses `content.md`;
- projection investigation uses only the affected `render-data.json` subtree;
- non-Voice 04 requirements stay in project `work/asset-requirements.md`;
- downstream Voice meaning stays in Voice canonical sources, not in PRD render-data or `asset-requirements.md`;
- Golden/HTML source is inspected only for a concrete component/marker/runtime defect or explicit Golden regression audit, in the smallest useful range;
- visual claims require actual rendered/browser/page evidence.

## Canonical boundary

The same approved project model can feed two separate canonical surfaces:

```text
source evidence + current user instruction + approved decisions
→ approved project model
   ├─ content.md
   │  → render-data.json
   │  → PRD core 01–03 in output/v<document.version>/prd.html
   └─ optional work/asset-requirements.md
      → 04 Production Assets in the same prd.html
```

Concrete Production Asset needs should be recovered with the project model from discussion/source. Do not use generated 01–03 as the normal discovery source for 04.

Optional canonical Voice Production may be merged into matching 04 moments from the existing Voice owners. `work/asset-requirements.md` owns actionable non-Voice Production Asset requirements only. Voice continues to use `work/voice-requirements.md` / `work/voice-production.md`; the compositor does **not** own Voice requirements, actor decisions, or wording.

Never patch `prd.html` manually to hide an upstream PRD, asset-requirement, or Voice defect.

## Implementation ownership

- `CONTENT-CONTRACT.md` → approved PRD-core 01–03 semantic/visible-composition contract
- `PRODUCTION-ASSETS.md` → bounded moment-first non-Voice 04 Production Asset requirement/writing contract
- `renderer/core.py` → reusable PRD rendering helpers/primitives
- `renderer/pages.py` → PRD render data → approved Golden PRD-core page composition
- `renderer/render.py` → deterministic lower-level human HTML render + optional downstream composition orchestration
- `renderer/delivery.py` → deterministic versioned handoff bundle and compact AI reading projections
- `renderer/production_assets_objective.py` → objective/moment-first 04 composition, section mapping, resource rendering, and Voice/non-Voice merge
- `renderer/production_assets.py` → Voice-specific parsing and presentation primitives reused by the objective-first compositor
- `template/golden-reference.html` → canonical approved Golden reference bytes
- `template/runtime-template.html` → runtime template alias; must remain byte-identical to Golden
- `validator/validate.py` → mechanical Flow 4 PRD checks
- `validator/validate_handoff.py` → narrow Flow 4 → Flow 5 PRD handoff consistency

Renderer/compositor code may organize already-owned canonical information; it may not invent project facts, asset requirements, Voice moments, actor voices, scripts, or decisions.

## Protected PRD core vs 04 Production Assets

The approved 01–03 baseline remains unchanged:

```text
01 Overview
02 Gameplay Flow
03 Development
   Gameplay sections → Gameplay Overview / Level Design / Developer
```

For `N` gameplay sections, `6 + 4N` remains the PRD-core page count.

`04 Production Assets` is an additive professional production surface. It must not alter Golden template bytes, PRD-core page identities, 01–03 navigation, or PRD-core authoring rules.

Current human-facing 04 navigation is objective-first:

```text
04 Production Assets
   <gameplay/shared section title>
      <accepted PRD label>
```

Inside each matching page, content is **moment-first**, for example:

```text
Objective 3 · Warden Halls

01 · Throughout the Warden Halls
   MODEL
   Swinging Axe Trap
   ...

02 · Entering the Warden Halls
   UI / TEXT
   ...
   AUDIO
   ...
```

Visible resource types are:

```text
MODEL
ITEM
UI / TEXT
AUDIO
PARTICLE
```

Do not expose the internal markdown storage headings as a visible category dashboard. Do not render empty type/category sections.

Voice dialogue is rendered as `AUDIO` inside the matching moment from canonical Voice sources. Its visible production fields are Function, Voice Preset, ElevenLabs Model, Estimated Duration, and exact Prompt; actor/script ownership remains in the Voice system.

A downstream-only 04 update may rerender the same versioned HTML without reopening PRD-core acceptance when `content.md` and `render-data.json` are unchanged. Voice workflow still owns Voice acceptance.

## Efficient production

Initial project build:

```text
source/discussion
→ complete + approve Flow 2 model
   including real Production Asset needs
→ one PRD-core purity/humanize pass
→ content.md + direct projection
→ render/validate/review existing 01–03
→ materialize non-Voice asset-requirements.md from the same approved model
→ merge canonical Voice only when it exists
→ rerender consolidated 04
→ validate only affected downstream scope
```

The artifact sequence does **not** mean 04 is designed from finished 01–03. Its resource requirements come from the same approved project model.

Bounded PRD revision:

```text
approved PRD delta
→ affected project model meaning
→ affected PRD-core and/or 04 canonical source only
→ full deterministic rerender
→ targeted review
```

Do not reread/rewrite unchanged gameplay sections. English-only data should not be duplicated into fake bilingual objects.

## 04 authoring discipline

Use `PRODUCTION-ASSETS.md` as the single detailed owner.

Key rules:

- only concrete resources that really need to be prepared belong in 04;
- gameplay behavior, reset logic, route logic, thresholds, and generic sequences are not assets;
- MODEL / ITEM / PARTICLE use short Function + literal Visual Brief + optional real approved Size;
- UI / TEXT uses Function + exact player-facing copy;
- non-dialogue AUDIO uses Function + short Audio Brief;
- generic `States / Position / Orientation / Reuse / Used At / Build Specs` metadata is not part of new visible authoring;
- do not invent visual style, lore, dimensions, animation, VFX, or sound that project authority does not support;
- when a detail changes project meaning, return it to the existing project approval boundary instead of deciding it in 04;
- use plain human production notes, not polished filler prose.

## Semantic vs technical

- PRD source/canonical/representation/readiness meaning wrong → root `project-document-production` + smallest semantic owner;
- non-Voice 04 requirement wrong → approved project model + `PRODUCTION-ASSETS.md` contract;
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

For changes limited to 04 instructions/contracts, prove that 01–03 owners/renderer/template were not changed. Do not rerun unrelated Golden/Voice/browser suites for ceremony.

`PRD Verify` is the canonical CI gate for affected PRD/render/compositor contracts. Voice canonical/validator behavior uses `Voice Verify`.

Browser/visual PASS still requires actual browser/visual evidence.

Do not create renderer profiles, generic Asset frameworks/schemas, separate Production Asset Flows/Kits, second HTML outputs, asset manifests, component registries, snapshot systems, template copies, debug artifacts, or new skills without a concrete current need.

## Boundary

- this kit owns semantic Flow 2–4 plus the bounded non-Voice 04 contract/composition path;
- 01–03 remain protected by their existing Golden/content owners;
- Voice semantics belong to `kits/voice-production-kit/`;
- 04 is a normal capability of the same Project Document Generator, not a new numbered Flow or separate product;
- shared dependencies/tests/CI belong to repository engineering.
