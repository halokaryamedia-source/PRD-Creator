# PRD Creator

**Version:** 3.0.0

PRD Creator turns project evidence/discussion into one revision-bound project model, canonical PRD, required Production Assets, and optional Voice Production in one versioned delivery.

## Version rule

```text
PATCH  backward-compatible fix
MINOR  additive backward-compatible capability
MAJOR  incompatible product/machine contract change
NO BUMP project-only revision, clarification, CI/repository hygiene, test-only work
```

Package 3.0 is MAJOR because current machine formats intentionally reject older readiness aliases, title-based moment ordering, implicit result modeling, redundant handoff path state, and acceptance records that do not bind all current canonical bytes.

## Product flow

```text
sources
→ strict provenance + material requirement recovery
→ integrated cross-role model
→ material Proposal/conflict?
   yes → compact Simple Chat Preview → approval/correction
   no  → continue automatically
→ exact requirement-revision binding
→ canonical content.md
→ strict render-data projection + approved-requirement SHA + content SHA
→ deterministic PRD core
→ non-Voice 04 when required
→ exact-byte PRD/04 acceptance
→ minimal handoff revision state
→ Flow 5 Voice requirements when justified
→ Flow 6 Voice production
→ exact-byte Flow 7 acceptance
→ one current project HTML
```

## Package 3 engineering shape

```text
single truth
→ stable identity
→ strict schema
→ exact revision binding
→ deterministic projection
→ transactional publication
```

Key contracts:

```text
Flow 2 revision
requirement-register bytes → approved_requirement_sha256
Simple Chat Preview approval → required only for material AI Proposals

PRD projection
Flow 2 requirement SHA → render-data.approved_requirement_sha256
content.md bytes → render-data.canonical_content_sha256

PRD acceptance
Accepted Render Data SHA256
Accepted Asset Requirements SHA256

Handoff state
status + accepted_prd_version
(canonical work/output paths are derived, not persisted)

04 identity
Owner ID → Moment ID → AST/VO ID

Voice production
voice-production → exact Voice Requirements SHA

Voice acceptance
Accepted Voice Production SHA256
```

Where state does persist path references, they are normalized project-relative POSIX refs only.

## Package map

```text
kits/prd-creator/
├─ SKILL.md
├─ AGENTS.md
├─ README.md
├─ intake/
├─ document/
├─ production-assets/
├─ voice/
├─ shared/
│  ├─ intake.py
│  ├─ state.py
│  ├─ paths.py
│  ├─ handoff.py
│  ├─ acceptance.py
│  ├─ render_schema.py
│  ├─ localization.py
│  ├─ assets.py
│  ├─ voice.py
│  ├─ lifecycle.py
│  ├─ topology.py
│  └─ issues.py
├─ renderer/
│  ├─ template_adapter.py
│  └─ static/
├─ validator/
│  ├─ prd_validation_engine.py
│  ├─ html_contract.py
│  ├─ voice_validation.py
│  ├─ validate.py
│  ├─ validate_handoff.py
│  └─ validate_voice.py
└─ template/
```

## Canonical owners

| Meaning | Artifact | Owner |
|---|---|---|
| source / requirement revision + conditional approval | `state/source-inventory.yaml`, `requirement-register.yaml`, `intake-state.yaml` | `intake/SOURCE-INTAKE.md` |
| PRD semantic meaning | `work/content.md` | `document/CONTENT-CONTRACT.md` |
| strict render projection | `work/render-data.json` | `shared/render_schema.py` + `renderer/CONTRACT.md` |
| Golden grammar | derived presentation | `document/DESIGN-CONTRACT.md` |
| non-Voice 04 | `work/asset-requirements.md` | `production-assets/CONTRACT.md` |
| PRD acceptance/handoff | `work/acceptance.md`, minimal `state/handoff-state.yaml` | `document/VALIDATION.md` |
| Voice requirements | `work/voice-requirements.md` | `voice/EXTRACTION.md` |
| Voice wording/performance | `work/voice-production.md` | `voice/PERFORMANCE-WRITING.md` |
| Voice acceptance | `work/voice-acceptance.md`, `state/voice-state.yaml` | `voice/VALIDATION.md` |

Do not create parallel schemas or generic registries for these owners.

## Implementation boundaries

- `shared/acceptance.py` owns reusable acceptance label/SHA parsing primitives; semantic acceptance meaning remains with Flow 4/7 owners.
- `shared/handoff.py` owns only handoff status + accepted revision identity; artifact locations are deterministic and are not duplicated into handoff state.
- `validator/prd_validation_engine.py` orchestrates PRD source/projection/business checks.
- `validator/html_contract.py` owns derived HTML freshness/composition/navigation checks.
- `validator/validate_handoff.py` derives canonical artifact paths from the accepted PRD version and proves current artifact/delivery/acceptance parity.
- `validator/voice_validation.py` owns Flow 5–7 mechanical domain validation.
- `validator/validate_voice.py` is only the Voice CLI/public entrypoint.

## Renderer boundaries

- `render-data.json` accepts one field vocabulary; unknown/legacy keys fail.
- Projection binds both the exact Flow 2 requirement revision and exact current `content.md` bytes.
- Gameplay result mode is explicit: `scored | completion_only`.
- Renderer never infers missing semantic meaning from another role.
- `TemplateAdapter` is the only owner of Golden shell mutation/reference compatibility, including additive 04 insertion.
- Production Assets CSS/JS live in `renderer/static/` and are inlined at render time.
- 04 joins only through stable Owner/Moment/Resource identity.
- Preparation Mode may show pending Voice selection; `voice_delivery_ready` may not render unresolved cast selection/profile.
- Delivery publishes complete version directories transactionally with rollback.

## Model behavior

The package is model-agnostic and expects capable reasoning without forcing unnecessary approval loops.

- Start from the smallest authoritative owner/source.
- Expand context only for material dependencies.
- Let the model choose reversible wording/grouping/decomposition craft.
- Keep product/design/runtime choices as explicit Proposals until approved.
- Skip the preview checkpoint when current authority already settles all material choices.
- Use strict machine contracts to fail early rather than guess compatibility.
- Fix the first wrong owner rather than polishing downstream symptoms.

## Operator CLI

Use the thin operator facade for routine mechanical execution instead of remembering individual renderer/validator script paths:

```bash
python tools/prd.py status workspace/active/<project>/
python tools/prd.py build workspace/active/<project>/
python tools/prd.py validate workspace/active/<project>/
python tools/prd.py handoff workspace/active/<project>/
python tools/prd.py voice workspace/active/<project>/
```

`status` is intentionally compact and mechanical. It reports the current PRD / handoff / Voice validation state, the first structured issue/owner when blocked, and the smallest next repair target. Use `--json` for agent/machine consumption.

The facade does not create another authority, schema, validator, or lifecycle. It delegates to the existing canonical delivery and validation owners. A clear mechanical status does not establish semantic readiness, browser visual quality, audio quality, or user approval.

## Derived delivery

```text
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

`prd.html` is the single human-facing project document. Derived files never outrank canonical `work/`/`state/` sources and should never be hand-patched to hide an upstream defect.

## Protected boundaries

- Golden reference/runtime bytes stay protected and byte-identical unless an explicit design-contract change is approved.
- Adaptive cardinality is allowed only inside approved component families.
- Machine YAML uses the shared duplicate-safe YAML loader and reports parse-line location when available.
- Generic `_engine.py` imports and title-based machine joins are retired.
- Browser visual PASS requires browser evidence.
- Generated-audio quality requires audio evidence.

For production use start from `SKILL.md`. For implementation defects start from `AGENTS.md` and the smallest exact technical owner.
