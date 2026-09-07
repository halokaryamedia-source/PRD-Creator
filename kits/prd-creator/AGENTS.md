# PRD Creator Kit Agent Rules

Root `AGENTS.md` owns repository mode, continuity, authority, proof, and skill budget. This file owns **package file/mechanical routing and context economy**. Detailed normal Production Execution is `SKILL.md`; semantic and design contracts stay in their named owners.

## Open the active owner

| Need | Owner |
|---|---|
| Flow 2 source recovery/completion | `intake/SOURCE-INTAKE.md` |
| PRD core 01–03 semantic completeness | `document/CONTENT-CONTRACT.md` |
| PRD core 01–03 Golden visual/component grammar | `document/DESIGN-CONTRACT.md` |
| PRD terminology when needed | `document/GLOSSARY.md` |
| Flow 4 validation/handoff | `document/VALIDATION.md` |
| non-Voice 04 Production Asset meaning | `production-assets/CONTRACT.md` |
| render/projection/compositor/delivery mechanics | `renderer/CONTRACT.md` |
| Flow 5 Voice extraction | `voice/EXTRACTION.md` |
| Flow 6 durable Voice policy | `docs/foundation/06-elevenlabs-script-production.md` |
| Eleven v3 craft | `voice/PERFORMANCE-WRITING.md` |
| Flow 7 Voice validation | `voice/VALIDATION.md` |
| end-to-end Flow 2–7 execution | `SKILL.md` |

Do not broad-read the whole kit. Start with the smallest owner that can settle the current question, then expand only when a material cross-owner dependency or contradiction requires it.

## Semantic vs design vs technical boundary

```text
project/source meaning wrong or incomplete
→ project-document-production + CONTENT-CONTRACT / Flow 2 owner

meaning correct but wrong approved visible placement/component family
→ DESIGN-CONTRACT

semantic + design contracts correct; renderer/template/validator/compositor mechanics wrong
→ exact implementation owner

Voice scope/communication meaning wrong
→ voice-production + nearest Voice owner
```

Do not change project meaning to work around a presentation defect. Do not change the design contract to work around an implementation defect.

## Implementation ownership

- `shared/state.py` → real YAML parsing and common machine-state scalar/list access;
- `shared/voice.py` → one typed Voice requirements/production grammar used by renderer and validator;
- `renderer/core.py` → reusable rendering primitives;
- `renderer/pages.py` → render-data into approved page/component grammar, including data-driven child cardinality;
- `renderer/render.py` → thin render CLI/orchestration wrapper;
- `renderer/prd_render_engine.py` → deterministic PRD-core render validation/orchestration;
- `renderer/delivery.py` → staged/transactional versioned delivery + AI projections;
- `renderer/production_assets_compositor.py` → stable-ID shared 04 composition;
- `renderer/production_assets.py` → Voice-specific 04 presentation primitives backed by `shared/voice.py`;
- `validator/prd_validation_engine.py` → lower-level deterministic PRD checks;
- `validator/api.py` → canonical complete PRD validation API, including content purity;
- `validator/validate.py` → thin PRD validation CLI;
- `validator/validate_handoff.py` → Flow 4 → Flow 5 consistency + exact acceptance revision binding;
- `validator/validate_voice.py` → Voice mechanical validation using shared typed parsers.

There is no generic top-level `_engine` module contract. Engine modules use domain-specific names so renderer and validator can coexist in one Python process without import-cache collision.

Renderer/validator code may organize or check already-owned information. It may not invent project facts, material asset requirements, Voice moments, resource ownership, or product decisions.

## Machine data boundary

Machine-owned YAML state must be parsed as YAML through `shared/state.py`; do not reintroduce regex/line-splitting pseudo-YAML parsers.

Production presentation identity is stable-ID based:

```text
Production Assets section → Owner ID
non-Voice resource        → Asset ID
Voice line                → VO-... ID
```

Display titles are not identity and must not be used as silent join keys.

## Canonical source boundary

```text
approved project model
├─ work/content.md                       semantic PRD truth
│  → work/render-data.json               derived projection
│  → DESIGN-CONTRACT component grammar
│  → project HTML 01–03
├─ optional work/asset-requirements.md
│  → project HTML 04 non-Voice resources
└─ accepted downstream Voice
   → work/voice-requirements.md
   → work/voice-production.md
   → project HTML 04 AUDIO presentation
```

Generated `prd.html`, `context.md`, and `index.json` are derived. Never patch them manually to hide an upstream defect.

## Adaptive composition boundary

Golden fixes the page/component grammar described by `document/DESIGN-CONTRACT.md`. It does **not** require new projects to copy AFTERSHOCK's number of flow cards, note cards, or compact sequence steps.

```text
material semantic distinctions
→ data-driven child count
→ existing approved component family
```

No filler to hit a sample count. No destructive merging to reduce to a sample count. New component families still require an explicit design change.

## Context economy

Use progressive expansion:

```text
smallest current owner/source
→ unresolved material question?
→ open the smallest adjacent owner/source that can answer it
→ repeat only while the decision can materially change
```

Large Golden/generated HTML is opened only for concrete DOM/runtime/visual evidence needs. Deep Voice references are opened only for the active Voice craft/evidence question.

## Bounded technical changes

```text
observe/reproduce drift
→ confirm which semantic/design/technical owner is first wrong
→ smallest complete fix
→ regenerate only invalidated derived output
→ cheapest proof that can falsify the fix
→ stop
```

PRD-only mechanics do not reopen Voice. Voice-only mechanics do not reopen accepted PRD meaning when upstream meaning is unchanged.

## Verification routing

- repository/routing/docs-only changes → Repository Verify;
- PRD renderer/template/validator/source-contract executable changes → PRD Verify;
- Voice validator/canonical contract changes → Voice Verify;
- shared parser/state changes → affected targeted gate + Local promotion full regression;
- shared 04 compositor behavior → PRD Verify plus Voice proof when Voice behavior changes;
- visual PASS → actual browser/render evidence;
- generated-audio quality → actual audio evidence.

Static source quality is enforced by locked dev tooling (`ruff`, `mypy`, `coverage`) in CI. Runtime dependencies stay separately pinned in `requirements.lock.txt`.

## Anti-overdevelopment

Do not create compatibility copies, generic requirement/schema/manifest/registry frameworks, separate PRD/asset flows, alternate PRD HTML exports, renderer profiles, snapshot systems, settings databases, or scoring systems merely because a stronger model can populate them.

The former DOCX export path remains retired.

## Boundary

- `project-document-production` owns reusable project/PRD/04 semantic judgment;
- `document/CONTENT-CONTRACT.md` owns PRD semantic completeness;
- `document/DESIGN-CONTRACT.md` owns approved PRD visual/component grammar;
- `voice-production` owns Voice semantic judgment;
- implementation owners project those contracts deterministically;
- shared dependencies/tests/CI remain repository engineering owners.
