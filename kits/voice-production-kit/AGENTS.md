# Voice Production Kit Agent Rules

Root `AGENTS.md` owns work mode, continuity, authority, proof, and skill budget. Root `voice-production` owns reusable Voice semantic judgment. This file owns **Voice kit routing, file/mechanical ownership, and context economy**.

Detailed normal Flow 5–7 Production Execution is `SKILL.md`. Do not duplicate exact Flow/presentation contracts here.

## Active owners

| Need | Owner |
|---|---|
| Flow 5 Voice scope/context extraction | `VOICE-EXTRACTION.md` |
| Flow 6 durable lifecycle/output policy | `docs/foundation/06-elevenlabs-script-production.md` |
| Flow 6 end-to-end kit procedure | `SKILL.md` |
| Eleven v3 performance-writing craft | `SOUNDMAKER.md` |
| Flow 7 validation/evidence | `VOICE-VALIDATION.md` |
| optional DOCX presentation | `DOCX-FORMAT.md` |
| package overview/navigation | `README.md` |

Do not broad-read every Voice/reference file by default. Deep Eleven v3 references are opened only when the current writing/evidence question needs them.

## Semantic vs technical boundary

```text
Voice scope / Speaker / Channel / Trigger / Purpose / wording / readiness meaning wrong
→ root voice-production + smallest semantic owner

Voice semantics correct; builder/validator/presentation mechanics wrong
→ exact implementation owner below
```

A technical file does not automatically require the semantic specialist. A technical change that would alter the required Voice/product contract must return to the semantic owner first.

## Implementation ownership

- project 04 objective/moment-first composition/navigation → `kits/project-document-generator/renderer/production_assets_objective.py`;
- Voice-specific 04 parsing/presentation primitives → `kits/project-document-generator/renderer/production_assets.py`;
- optional DOCX generation/pagination → `builder/build_docx.py`;
- optional DOCX presentation contract → `DOCX-FORMAT.md`;
- Voice mechanical parity/derived-output validation → `validator/validate.py`;
- shared dependency/test/CI → repository-engineering owners.

Exact reader-facing 04 resource fields/layout are owned by `kits/project-document-generator/PRODUCTION-ASSETS.md` plus the current shared compositor contract. Do not maintain another Voice HTML schema here.

## Canonical source boundary

```text
accepted project / PRD meaning
→ work/voice-requirements.md
→ work/voice-production.md
→ Voice acceptance/state
```

Project HTML and optional DOCX are derived presentation/export surfaces. Never hand-edit them as the source fix.

Flow 5 requirements own Voice scope/communication context. `work/voice-production.md` owns canonical production wording/performance. Presentation code may organize that data but may not create new Voice moments, project facts, actor decisions, or wording.

## Context economy

- recover current project/Voice canonical state before asking the user;
- use the smallest current Flow owner rather than loading all Voice docs;
- open deep Eleven/reference material only for the current evidence/craft question;
- do not load generated project HTML/DOCX merely to reason about canonical Voice meaning;
- visual claims require actual render/browser/page evidence;
- generated-audio claims require actual audio evidence.

## Bounded technical changes

```text
observe/reproduce or inspect concrete defect
→ confirm semantic contract is already correct
→ exact implementation owner
→ smallest complete fix
→ regenerate only invalidated derived output
→ cheapest relevant proof
→ stop
```

Voice-only production/mechanical changes do not reopen PRD-core acceptance when upstream PRD meaning is unchanged.

## Verification routing

- repository/docs/routing-only changes → `Repository Verify` when owned by its paths;
- Voice builder/validator/test/dependency changes → `Voice Verify`;
- shared Project Document 04 compositor changes → `PRD Verify`;
- project HTML visual PASS → actual browser/render evidence;
- optional DOCX visual PASS → rendered-page evidence;
- audio quality → actual audio evidence.

Do not run unrelated verification for ceremony.

## Boundaries

- kit owns detailed Flow 5–7 procedure/implementation;
- root `voice-production` owns reusable semantic judgment;
- Project Document Generator owns shared 04 composition mechanics and non-Voice 04 requirements;
- upstream project/PRD authority owns gameplay/story truth;
- DOCX remains optional export;
- do not add a second Voice HTML, generic asset framework, new root skill, or extra workflow layer without a concrete need.
