# PRD Creator

**Version:** 3.0.0

PRD Creator turns project evidence/discussion into one revision-bound approved project model, canonical PRD, required Production Assets, and optional Voice Production in one versioned delivery.

## Version rule

```text
PATCH  backward-compatible fix
MINOR  additive backward-compatible capability
MAJOR  incompatible product/machine contract change
NO BUMP project-only revision, clarification, CI/repository hygiene, test-only work
```

Package 3.0 is MAJOR because current machine formats intentionally reject older readiness aliases, title-based moment ordering, implicit result modeling, and acceptance records that do not bind all current canonical bytes.

## Product flow

```text
sources
→ strict provenance + requirement recovery
→ integrated cross-role model
→ Simple Chat Preview
→ exact requirement-revision approval
→ canonical content.md
→ strict render-data projection + content SHA
→ deterministic PRD core
→ non-Voice 04 when required
→ exact-byte PRD/04 acceptance + handoff
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
Flow 2 approval
requirement-register bytes → approved_requirement_sha256

PRD projection
content.md bytes → render-data.canonical_content_sha256

PRD acceptance
Accepted Render Data SHA256
Accepted Asset Requirements SHA256

04 identity
Owner ID → Moment ID → AST/VO ID

Voice production
voice-production → exact Voice Requirements SHA

Voice acceptance
Accepted Voice Production SHA256
```

Persisted state paths are normalized project-relative POSIX refs only.

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
└─ template/
```

## Canonical owners

| Meaning | Artifact | Owner |
|---|---|---|
| source / requirement approval | `state/source-inventory.yaml`, `requirement-register.yaml`, `intake-state.yaml` | `intake/SOURCE-INTAKE.md` |
| PRD semantic meaning | `work/content.md` | `document/CONTENT-CONTRACT.md` |
| strict render projection | `work/render-data.json` | `shared/render_schema.py` + `renderer/CONTRACT.md` |
| Golden grammar | derived presentation | `document/DESIGN-CONTRACT.md` |
| non-Voice 04 | `work/asset-requirements.md` | `production-assets/CONTRACT.md` |
| PRD acceptance/handoff | `work/acceptance.md`, `state/handoff-state.yaml` | `document/VALIDATION.md` |
| Voice requirements | `work/voice-requirements.md` | `voice/EXTRACTION.md` |
| Voice wording/performance | `work/voice-production.md` | `voice/PERFORMANCE-WRITING.md` |
| Voice acceptance | `work/voice-acceptance.md`, `state/voice-state.yaml` | `voice/VALIDATION.md` |

Do not create parallel schemas or generic registries for these owners.

## Renderer boundaries

- `render-data.json` accepts one field vocabulary; unknown/legacy keys fail.
- Gameplay result mode is explicit: `scored | completion_only`.
- Renderer never infers missing semantic meaning from another role.
- `TemplateAdapter` is the only owner of Golden shell mutation/reference compatibility.
- Production Assets CSS/JS live in `renderer/static/` and are inlined at render time.
- 04 joins only through stable Owner/Moment/Resource identity.
- Delivery publishes complete version directories transactionally with rollback.

## Model behavior

The package is model-agnostic and expects capable reasoning without forcing unnecessary approval loops.

- Start from the smallest authoritative owner/source.
- Expand context only for material dependencies.
- Let the model choose reversible wording/grouping/decomposition craft.
- Keep product/design/runtime choices as explicit Proposals until approved.
- Use strict machine contracts to fail early rather than guess compatibility.
- Fix the first wrong owner rather than polishing downstream symptoms.

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
- Machine YAML uses the shared duplicate-safe YAML loader.
- Generic `_engine.py` imports and title-based machine joins are retired.
- Browser visual PASS requires browser evidence.
- Generated-audio quality requires audio evidence.

For production use start from `SKILL.md`. For implementation defects start from `AGENTS.md` and the smallest exact technical owner.
