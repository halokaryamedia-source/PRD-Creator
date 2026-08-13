# Project Document Generator Agent Rules

Root `AGENTS.md` owns repository mode, proof, skill budget, continuity, and semantic-vs-technical routing. This file owns PRD kit routing/mechanics plus the narrow **same-HTML Production Assets composition mechanics**.

## Open only the active owner

- Flow 2 → `SOURCE-INTAKE.md`
- Flow 3 content → `CONTENT-CONTRACT.md`
- Flow 3 projection/HTML → `RENDERING.md` only when needed
- Flow 4 → `VALIDATION.md`
- downstream Production Assets HTML composition defect → `RENDERING.md` + `renderer/production_assets.py`
- `WORKFLOW.md` → sequence only when the active Flow is unclear
- `GLOSSARY.md` / `RULES.md` → only for a specific terminology/kit-wide invariant question

Do not broad-read the whole kit by default.

## HTML context budget

Normal production must not load `template/runtime-template.html`, `template/golden-reference.html`, or generated `final.html` in full into model context.

- renderer/validator may read large files directly at runtime;
- canonical PRD meaning review uses `content.md`;
- projection investigation uses only the affected `render-data.json` subtree;
- downstream Voice meaning stays in Voice canonical sources, not in PRD render-data;
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
accepted downstream canonical production source
→ deterministic Production Assets compositor
→ appended professional-only pages in the same final.html
```

For Voice, the compositor reads `work/voice-production.md`; it does **not** own Voice requirements, actor decisions, or wording.

Never patch `final.html` manually to hide an upstream PRD or Voice defect.

## Implementation ownership

- `renderer/core.py` → reusable PRD rendering helpers/primitives
- `renderer/pages.py` → PRD render data → approved Golden PRD-core page composition
- `renderer/render.py` → deterministic base render + optional downstream composition orchestration
- `renderer/production_assets.py` → concrete downstream Production Assets presentation; currently Voice only
- `template/golden-reference.html` → canonical approved Golden reference bytes
- `template/runtime-template.html` → runtime template alias; must remain byte-identical to Golden
- `validator/validate.py` → mechanical Flow 4 PRD checks
- `validator/validate_handoff.py` → narrow Flow 4 → Flow 5 PRD handoff consistency

Renderer/compositor code may organize already-owned canonical information; it may not invent project facts, Voice moments, actor voices, scripts, or decisions.

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

A downstream Voice-only update may rerender the same HTML without reopening PRD acceptance when `content.md` and `render-data.json` are unchanged. Voice workflow owns Voice acceptance.

## Efficient production

Initial PRD build:

```text
complete + approve Flow 2 model
→ one purity/humanize pass
→ content.md + direct projection
→ render once
→ validate/review PRD core
```

Downstream Voice preparation:

```text
accepted PRD
→ Voice Flow 5–6 canonical sources
→ rerender same final.html
→ Production Assets → Voice appended
→ Voice validation on affected scope
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

Do not create renderer profiles, generic Asset frameworks/schemas, second Voice HTML, asset manifests, snapshot systems, template copies, debug artifacts, or new skills without a concrete current need.

## Boundary

- this kit owns semantic Flow 2–4;
- Voice semantics belong to `kits/voice-production-kit/`;
- this kit additionally owns the narrow mechanical composition of accepted downstream production content into the shared project HTML;
- current Production Assets compositor is Voice-specific and must not be generalized to other asset domains without an approved concrete need;
- shared dependencies/tests/CI belong to repository engineering.
