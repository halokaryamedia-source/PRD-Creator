# PRD Creator Kit Agent Rules

Root `AGENTS.md` owns repository mode, continuity, authority, proof, and skill budget. The root semantic specialists remain separate:

```text
.agents/skills/project-document-production/
.agents/skills/voice-production/
```

This file owns **unified kit file/mechanical routing and context economy**. Detailed normal Production Execution is `SKILL.md`; exact domain contracts stay in their named owners.

## Open only the active owner

| Need | Owner |
|---|---|
| Flow 2 source recovery/completion | `intake/SOURCE-INTAKE.md` |
| PRD core 01–03 semantic/visible contract | `document/CONTENT-CONTRACT.md` |
| PRD terminology when needed | `document/GLOSSARY.md` |
| Flow 4 validation/handoff procedure | `document/VALIDATION.md` |
| non-Voice 04 Production Asset contract | `production-assets/CONTRACT.md` |
| render/projection/compositor/delivery contract | `renderer/CONTRACT.md` |
| Flow 5 Voice scope/context extraction | `voice/EXTRACTION.md` |
| Flow 6 durable lifecycle/output policy | `docs/foundation/06-elevenlabs-script-production.md` |
| Eleven v3 performance-writing craft | `voice/PERFORMANCE-WRITING.md` |
| Flow 7 Voice validation/evidence | `voice/VALIDATION.md` |
| end-to-end normal Flow 2–7 Production Execution | `SKILL.md` |
| package orientation / Requirement Map | `README.md` |

Do not broad-read the whole kit. Deep Voice references are opened only when the current craft/evidence question needs them.

## Semantic vs technical boundary

```text
source / project model / canonical PRD / non-Voice 04 / PRD readiness meaning wrong
→ root project-document-production + smallest semantic owner

Voice scope / Speaker / Channel / Trigger / Purpose / wording / Voice readiness meaning wrong
→ root voice-production + smallest Voice owner

semantic contracts correct; renderer/template/validator/compositor mechanics wrong
→ exact implementation owner below
```

A technical file does not automatically require a semantic specialist. Conversely, a technical change that would alter what the product/artifact is required to represent or accept must return to the matching semantic owner first.

## Implementation ownership

### Renderer

- `renderer/core.py` → reusable rendering helpers/primitives;
- `renderer/pages.py` → PRD render data → approved Golden PRD-core page composition;
- `renderer/render.py` → lower-level deterministic HTML render + downstream composition orchestration;
- `renderer/delivery.py` → versioned delivery bundle + AI reading projections;
- `renderer/production_assets_compositor.py` → objective/moment-first mixed 04 composition;
- `renderer/production_assets.py` → Voice-specific parsing/presentation primitives reused by the shared 04 compositor;
- `renderer/_engine.py` → lower-level PRD rendering engine used by the renderer family.

### Template

- `template/golden-reference.html` → canonical approved Golden reference bytes;
- `template/runtime-template.html` → runtime alias; remains byte-identical to Golden unless the Golden owner changes.

### Validators

- `validator/_engine.py` + `validator/validate.py` → PRD mechanical validation;
- `validator/validate_handoff.py` → Flow 4 → Flow 5 handoff consistency;
- `validator/validate_voice.py` → Voice revision/parity/project-HTML mechanical validation.

Renderer/compositor/validator code may organize or check already-owned canonical information. It may not invent project facts, resource requirements, Voice moments, actor voices, scripts, or product decisions.

## Canonical source boundary

```text
approved project model
├─ work/content.md
│  → work/render-data.json
│  → project HTML 01–03
├─ optional work/asset-requirements.md
│  → project HTML 04 non-Voice resources
└─ accepted downstream Voice
   → work/voice-requirements.md
   → work/voice-production.md
   → project HTML 04 AUDIO presentation
```

Generated `prd.html`, `context.md`, and `index.json` are derived. Never patch them manually to hide an upstream defect.

Exact PRD-core semantics belong to `document/CONTENT-CONTRACT.md`. Exact non-Voice 04 semantics belong to `production-assets/CONTRACT.md`. Exact Voice semantics remain under the Voice owners.

## Context economy

Normal production/maintenance must not load large artifacts merely because they exist.

- source/project-model recovery → only material source + intake/requirement state;
- canonical PRD-core review → `work/content.md` / relevant requirement state;
- projection investigation → only affected `render-data.json` subtree when practical;
- non-Voice 04 meaning → approved project model + `work/asset-requirements.md`;
- Voice meaning → Voice canonical owners, not PRD render data;
- Golden/generated HTML → only for concrete template/DOM/runtime/visual evidence needs, in the smallest useful range;
- deep Eleven reference material → only for the active Voice craft/evidence question;
- browser/visual claims → actual rendered/browser evidence;
- generated-audio claims → actual audio evidence.

Runtime code may read full files. That does not require loading those full files into AI context.

## Bounded technical changes

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

Do not reread/rewrite unchanged gameplay sections, redesign adjacent PRD/04/Voice content, or create compatibility layers merely because the implementation is inconvenient.

PRD-only mechanics do not reopen Voice work. Voice-only mechanics do not reopen PRD-core acceptance when upstream PRD meaning is unchanged.

## Verification routing

- repository/routing/docs-only changes → `Repository Verify` when owned by its paths;
- PRD renderer/template/validator/compositor/source-contract executable changes → `PRD Verify`;
- Voice validator/canonical contract changes → `Voice Verify`;
- shared 04 compositor behavior → `PRD Verify` and Voice proof only when Voice behavior is materially touched;
- project HTML visual PASS → actual browser/render evidence;
- generated-audio quality → actual audio evidence.

Do not rerun unrelated Golden/Voice/browser/audio suites for ceremony.

## Anti-overdevelopment boundary

Do not create:

- compatibility copies of the retired kit roots;
- generic requirement/parser/schema/manifest/registry frameworks;
- separate Production Asset flows/kits;
- second Voice HTML or other replacement export surface;
- renderer profiles or template copies;
- asset manifests/component registries/snapshot systems;
- settings databases or scoring systems for Voice;
- new root skills merely because implementation technology differs.

The former DOCX export path remains retired and must not return without a new explicit product requirement.

## Boundary

- this unified kit owns detailed Flow 2–7 production procedure/implementation;
- `project-document-production` owns reusable Project/PRD/04 semantic judgment;
- `voice-production` owns reusable Voice semantic judgment;
- exact contracts remain in the smallest categorized domain owner;
- shared dependencies/tests/CI remain repository engineering owners;
- root `tests/`, `tools/`, `.agents/skills/`, and `docs/foundation/` stay outside the kit.
