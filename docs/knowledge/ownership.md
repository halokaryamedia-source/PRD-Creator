# Repository Ownership

Updated: 2026-08-30

Use this file only to answer **who owns what**. Exact contracts remain in the named owners.

## Root operating owners

| Boundary | Owner |
|---|---|
| Top-level boot, work modes, continuity, authority, skill budget | `AGENTS.md` |
| GitHub branch/ref, tool fit, write/commit/history, CI/API/safety | `GITHUB_RULES.md` |
| Stable product/repository orientation | `CONTEXT.md` |
| Contribution + branch-promotion procedure | `CONTRIBUTING.md` |
| Public-repository data handling | `SECURITY.md` |
| Active continuation / resume checkpoint | `docs/knowledge/next-action.md` |
| Detailed work-routing explanation | `docs/knowledge/work-routing.md` |
| Source/state precedence | `docs/knowledge/source-authority.md` |
| Current validation evidence | `docs/knowledge/reviews/current-validation.md` |
| Historical review evidence | `docs/knowledge/reviews/history/` |
| Durable decisions/rationale | `docs/knowledge/decisions/` |
| Future/non-active work | `docs/knowledge/operations/backlog.md` |

## Repository areas

| Area | Responsibility |
|---|---|
| `.agents/skills/` | reusable semantic judgment |
| `docs/foundation/` | durable Flow 1–7 production policy |
| `docs/knowledge/` | continuity, routing, ownership, decisions, evidence, backlog |
| `kits/prd-creator/` | categorized Flow 2–7 + bounded 04 procedure/implementation |
| `tests/`, `tools/`, `.github/`, `requirements.lock.txt` | repository engineering / verification / promotion gates |
| `workspace/active/` | ignored local/external current project-package mount point |
| `workspace/archive/` | ignored local/external retained project-package mount point |

The public system repository owns workspace **guidance**, not live project-package contents.

## Unified package root owners

| Boundary | Owner |
|---|---|
| Package orientation + Requirement Map | `kits/prd-creator/README.md` |
| Package technical/file routing | `kits/prd-creator/AGENTS.md` |
| End-to-end Flow 2–7 Production Execution router | `kits/prd-creator/SKILL.md` |

## PRD semantic and procedure owners

| Boundary | Owner |
|---|---|
| Reusable PRD/source/04/readiness semantic judgment | `.agents/skills/project-document-production/SKILL.md` |
| End-to-end production sequence | `docs/foundation/01-production-flow.md` |
| Flow 2 durable policy | `docs/foundation/02-source-intake-recovery.md` |
| Flow 2 detailed procedure | `kits/prd-creator/intake/SOURCE-INTAKE.md` |
| PRD-core 01–03 exact contract | `kits/prd-creator/document/CONTENT-CONTRACT.md` |
| non-Voice 04 exact contract | `kits/prd-creator/production-assets/CONTRACT.md` |
| Flow 4 durable policy | `docs/foundation/04-prd-validation-handoff.md` |
| Flow 4 detailed validation/handoff | `kits/prd-creator/document/VALIDATION.md` |

## PRD implementation owners

| Boundary | Owner |
|---|---|
| PRD-core + shared HTML composition contract | `kits/prd-creator/renderer/CONTRACT.md` |
| versioned delivery orchestration | `kits/prd-creator/renderer/delivery.py` |
| PRD-core page projection | `kits/prd-creator/renderer/pages.py` |
| lower-level HTML renderer orchestration | `kits/prd-creator/renderer/render.py` |
| reusable renderer primitives | `kits/prd-creator/renderer/core.py` |
| shared 04 compositor | `kits/prd-creator/renderer/production_assets_compositor.py` |
| Voice-specific 04 parsing/presentation primitives | `kits/prd-creator/renderer/production_assets.py` |
| canonical Golden bytes | `kits/prd-creator/template/golden-reference.html` |
| runtime Golden alias | `kits/prd-creator/template/runtime-template.html` |
| PRD mechanical validation | `kits/prd-creator/validator/_engine.py` + `kits/prd-creator/validator/validate.py` |
| PRD → Voice handoff consistency | `kits/prd-creator/validator/validate_handoff.py` |
| PRD regressions | `tests/test_prd_*` |

## Voice owners

| Boundary | Owner |
|---|---|
| Reusable Voice semantic judgment | `.agents/skills/voice-production/SKILL.md` |
| Flow 5 extraction | `kits/prd-creator/voice/EXTRACTION.md` |
| Flow 6 durable policy | `docs/foundation/06-elevenlabs-script-production.md` |
| Eleven v3 performance-writing craft | `kits/prd-creator/voice/PERFORMANCE-WRITING.md` |
| Flow 7 validation/evidence | `kits/prd-creator/voice/VALIDATION.md` |
| Voice mechanical validation | `kits/prd-creator/validator/validate_voice.py` |
| Voice regressions | `tests/test_voice_contracts.py` |

## Project package owners

The following paths are relative to whichever authorized project package is active locally/externally:

| Boundary | Owner |
|---|---|
| source/provenance + requirement state | project `state/` owners |
| canonical PRD-core meaning | `work/content.md` |
| derived PRD-core projection | `work/render-data.json` |
| canonical non-Voice 04 requirements | `work/asset-requirements.md` |
| PRD acceptance | `work/acceptance.md` |
| PRD handoff state | `state/handoff-state.yaml` |
| canonical Voice requirements | `work/voice-requirements.md` |
| canonical Voice production | `work/voice-production.md` |
| Voice acceptance/state | `work/voice-acceptance.md` + `state/voice-state.yaml` |
| stable handoff/resume navigator | `output/README.md` |
| human-facing project document | `output/v<document.version>/prd.html` |
| AI development-context projection | `output/v<document.version>/context.md` |
| compact AI navigation/line-range index | `output/v<document.version>/index.json` |

Derived delivery artifacts are never manually patched to reconcile owners; fix the canonical owner and regenerate.

## Ownership questions vs contract questions

```text
Who owns this?
→ ownership.md

What exactly must this owner produce/accept?
→ open the named owner

Which source/state outranks another?
→ source-authority.md
```

## New-owner rule

Create a new owner only when an existing owner cannot represent the responsibility without mixing unrelated jobs. Do not create a map, registry/framework, Flow/Kit, root skill, schema, compatibility layer, or workflow solely because a filename is inconvenient.
