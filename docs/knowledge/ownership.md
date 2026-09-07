# Repository Ownership

Updated: 2026-09-07

Use this file only to answer **who owns what**. Exact contracts remain in the named owners.

## Root operating owners

| Boundary | Owner |
|---|---|
| Top-level boot, work modes, continuity, authority, skill budget | `AGENTS.md` |
| GitHub branch/ref, tool fit, write/commit/history, CI/API/safety | `GITHUB_RULES.md` |
| Stable product/repository orientation | `CONTEXT.md` |
| Contribution + branch-promotion procedure | `CONTRIBUTING.md` |
| Public-repository data handling | `SECURITY.md` |
| Active continuation | `docs/knowledge/next-action.md` |
| Source/state precedence | `docs/knowledge/source-authority.md` |
| Current validation evidence | `docs/knowledge/reviews/current-validation.md` |
| Durable decisions/rationale | `docs/knowledge/decisions/` |
| Future/non-active work | `docs/knowledge/operations/backlog.md` |

## Repository areas

| Area | Responsibility |
|---|---|
| `.agents/skills/` | reusable semantic judgment |
| `docs/foundation/` | durable Flow 1–7 production policy |
| `docs/knowledge/` | continuity, routing, ownership, decisions, evidence, backlog |
| `kits/prd-creator/` | categorized Flow 2–7 + bounded 04 procedure/implementation |
| `tests/`, `tools/`, `.github/`, root dependency locks | repository engineering / verification / promotion gates |
| `workspace/active/` | ignored local/external current project-package mount point |
| `workspace/archive/` | ignored local/external retained project-package mount point |

The public system repository owns workspace guidance, not live project-package contents.

## Unified package root owners

| Boundary | Owner |
|---|---|
| Package orientation + Requirement Map | `kits/prd-creator/README.md` |
| Package technical/file routing | `kits/prd-creator/AGENTS.md` |
| End-to-end Flow 2–7 execution router | `kits/prd-creator/SKILL.md` |

## PRD semantic / design / procedure owners

| Boundary | Owner |
|---|---|
| Reusable PRD/source/04/readiness semantic judgment | `.agents/skills/project-document-production/SKILL.md` |
| End-to-end production sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 durable policy | `docs/foundation/02-source-intake-recovery.md` |
| Flow 2 detailed procedure | `kits/prd-creator/intake/SOURCE-INTAKE.md` |
| PRD-core 01–03 semantic completeness + material conservation | `kits/prd-creator/document/CONTENT-CONTRACT.md` |
| PRD-core 01–03 Golden page/component design grammar | `kits/prd-creator/document/DESIGN-CONTRACT.md` |
| non-Voice 04 exact contract | `kits/prd-creator/production-assets/CONTRACT.md` |
| Flow 4 durable policy | `docs/foundation/04-prd-validation-handoff.md` |
| Flow 4 validation/handoff | `kits/prd-creator/document/VALIDATION.md` |

`CONTENT-CONTRACT.md` answers **what meaning must survive**. `DESIGN-CONTRACT.md` answers **where/how accepted meaning is presented**. Sample card/step counts do not become semantic ownership merely because the Golden example contains them.

## Shared implementation owners

| Boundary | Owner |
|---|---|
| real YAML machine-state parsing | `kits/prd-creator/shared/state.py` |
| typed canonical Voice requirements/production parsing | `kits/prd-creator/shared/voice.py` |

These shared parsers are implementation primitives only; they do not own project/Voice meaning.

## PRD implementation owners

| Boundary | Owner |
|---|---|
| PRD-core + shared HTML projection contract | `kits/prd-creator/renderer/CONTRACT.md` |
| staged versioned delivery orchestration | `kits/prd-creator/renderer/delivery.py` |
| PRD-core page projection / adaptive child cardinality | `kits/prd-creator/renderer/pages.py` |
| render CLI/orchestration | `kits/prd-creator/renderer/render.py` |
| lower-level PRD render engine | `kits/prd-creator/renderer/prd_render_engine.py` |
| reusable renderer primitives | `kits/prd-creator/renderer/core.py` |
| stable-ID shared 04 compositor | `kits/prd-creator/renderer/production_assets_compositor.py` |
| Voice-specific 04 presentation primitives | `kits/prd-creator/renderer/production_assets.py` |
| canonical Golden bytes | `kits/prd-creator/template/golden-reference.html` |
| runtime Golden alias | `kits/prd-creator/template/runtime-template.html` |
| lower-level PRD mechanical checks | `kits/prd-creator/validator/prd_validation_engine.py` |
| canonical complete PRD validation API | `kits/prd-creator/validator/api.py` |
| PRD validation CLI | `kits/prd-creator/validator/validate.py` |
| PRD → Voice handoff consistency + exact acceptance binding | `kits/prd-creator/validator/validate_handoff.py` |
| PRD regressions | `tests/test_prd_*` |

Generic renderer/validator `_engine.py` names are retired; domain-specific engine names prevent import-cache collisions.

## Voice owners

| Boundary | Owner |
|---|---|
| Reusable Voice semantic judgment | `.agents/skills/voice-production/SKILL.md` |
| Flow 5 extraction | `kits/prd-creator/voice/EXTRACTION.md` |
| Flow 6 durable policy | `docs/foundation/06-elevenlabs-script-production.md` |
| Eleven v3 performance craft | `kits/prd-creator/voice/PERFORMANCE-WRITING.md` |
| Flow 7 validation/evidence + section Owner-ID contract | `kits/prd-creator/voice/VALIDATION.md` |
| Voice mechanical validation | `kits/prd-creator/validator/validate_voice.py` |
| Voice regressions | `tests/test_voice_contracts.py` |

## Project package owners

Paths below are relative to the authorized active project package:

| Boundary | Owner |
|---|---|
| source/provenance + requirement state | project `state/` owners |
| canonical PRD-core meaning | `work/content.md` |
| derived PRD-core projection | `work/render-data.json` |
| canonical non-Voice 04 requirements + stable Asset/Owner IDs | `work/asset-requirements.md` |
| PRD acceptance + exact render-data SHA binding | `work/acceptance.md` |
| PRD handoff state | `state/handoff-state.yaml` |
| canonical Voice requirements | `work/voice-requirements.md` |
| canonical Voice production + section Owner IDs | `work/voice-production.md` |
| Voice acceptance/state | `work/voice-acceptance.md` + `state/voice-state.yaml` |
| stable handoff/resume navigator | `output/README.md` |
| human-facing project document | `output/v<document.version>/prd.html` |
| AI development-context projection | `output/v<document.version>/context.md` |
| compact AI navigation/line-range index | `output/v<document.version>/index.json` |

Derived delivery is never manually patched to reconcile owners; fix the canonical/contract owner and regenerate.

## Ownership questions vs contract questions

```text
Who owns this?
→ ownership.md

What meaning must be present?
→ CONTENT-CONTRACT / matching semantic owner

How must it be presented?
→ DESIGN-CONTRACT / renderer contract

Which source/state outranks another?
→ source-authority.md
```

## New-owner rule

Create a new owner only when responsibilities are genuinely different. Shared implementation modules do not create new semantic/product ownership; they centralize parsing/mechanical behavior that previously drifted across multiple implementations.
