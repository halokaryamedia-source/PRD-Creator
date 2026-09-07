# PRD Creator

**Version:** 2.0.0

PRD Creator turns project discussion/source into one approved project model, a development-ready PRD, required Production Assets, and optional downstream Voice Production in the same project delivery.

## Package version rule

```text
PATCH
→ backward-compatible bug fix

MINOR
→ additive capability or backward-compatible contract expansion

MAJOR
→ incompatible product/contract architecture change

NO BUMP
→ project-specific revision, documentation clarification, CI/repository hygiene, test-only change
```

Package 2.0 is a major contract change because machine identity and acceptance evidence are now explicit instead of being inferred from display titles/version labels.

Keep `SKILL.md`, this README, and current validation metadata aligned when a real package bump occurs.

## Product flow

```text
source + current instruction + approved decisions
→ requirement recovery + integrated cross-role synthesis
→ material Proposal review / approved project model
→ canonical PRD semantic content
→ deterministic projection through approved design grammar
→ 04 Production Assets when required
→ canonical mechanical validation + semantic reconciliation
→ exact-revision PRD/04 acceptance + handoff
→ Voice requirements / canonical Voice when required
→ one versioned project HTML + AI reading projections
```

## Model-readiness behavior

The package is model-agnostic but assumes a capable reasoning model can synthesize integrated project meaning rather than fill isolated fields.

- Start from the smallest authoritative owner/source that can settle the question.
- Expand context progressively when a material cross-cutting dependency requires it.
- Let the model handle reversible craft choices such as grouping, ordering, wording and decomposition.
- Material choices that change project behavior/scope remain explicit Proposals until approved.
- Before acceptance, reconcile meaning across approved source/requirements → canonical content → render projection → visible PRD.
- Keep mechanical validators deterministic; semantic review handles meaning loss/contradiction/invention.

## Semantic vs design separation

```text
document/CONTENT-CONTRACT.md
→ WHAT the PRD must communicate
→ semantic completeness + material conservation

document/DESIGN-CONTRACT.md
→ WHERE/HOW accepted meaning is presented
→ Golden page/component grammar + visual boundaries
```

The approved Golden artifact remains exact. Repeatable flow/note/sequence child counts follow project meaning rather than AFTERSHOCK sample counts.

## Package 2.0 engineering contract

The production system now uses explicit machine boundaries:

```text
real YAML state
→ shared/state.py

Voice requirements + Voice Production grammar
→ shared/voice.py

complete PRD validation
→ validator/api.py

Production Assets placement
→ stable Owner ID

non-Voice resource identity
→ stable AST-... ID

PRD acceptance
→ exact render-data SHA-256
```

Display titles are no longer machine join keys. Duplicate/missing/unknown IDs fail early. Handoff uses the same complete PRD validator as the normal validation CLI. Delivery is staged before replacing current output files.

## Package map

```text
kits/prd-creator/
├─ README.md
├─ AGENTS.md
├─ SKILL.md
├─ intake/
├─ document/
│  ├─ CONTENT-CONTRACT.md
│  ├─ DESIGN-CONTRACT.md
│  └─ VALIDATION.md
├─ production-assets/
├─ voice/
├─ shared/                    typed shared parser/state helpers
├─ renderer/
├─ validator/
└─ template/
```

## Requirement Map

| Requirement / canonical meaning | Project artifact | System owner |
|---|---|---|
| Project/gameplay requirement state | `state/requirement-register.yaml` | `intake/SOURCE-INTAKE.md` |
| Canonical PRD-core meaning | `work/content.md` | `document/CONTENT-CONTRACT.md` |
| PRD visible/page grammar | derived presentation | `document/DESIGN-CONTRACT.md` |
| PRD render projection | `work/render-data.json` | `renderer/CONTRACT.md` |
| Non-Voice Production Asset requirements | `work/asset-requirements.md` | `production-assets/CONTRACT.md` |
| Voice requirements | `work/voice-requirements.md` | `voice/EXTRACTION.md` |
| Canonical Voice production | `work/voice-production.md` | Flow 6 + `voice/PERFORMANCE-WRITING.md` |
| PRD acceptance / handoff | `work/acceptance.md` + `state/handoff-state.yaml` | `document/VALIDATION.md` + validators |
| Voice acceptance / state | `work/voice-acceptance.md` + `state/voice-state.yaml` | `voice/VALIDATION.md` + `validator/validate_voice.py` |

Do not create a generic `requirements/` folder merely for naming symmetry.

## Main domain owners

```text
intake/SOURCE-INTAKE.md
→ Flow 2 source recovery / integrated synthesis / preview

document/CONTENT-CONTRACT.md
→ PRD semantic completeness

document/DESIGN-CONTRACT.md
→ Golden page/component presentation contract

document/VALIDATION.md
→ Flow 4 readiness / reconciliation / exact-revision handoff

production-assets/CONTRACT.md
→ non-Voice 04 resource/writing/identity contract

voice/EXTRACTION.md
→ Flow 5 Voice scope/context extraction

voice/PERFORMANCE-WRITING.md
→ Eleven v3 craft

voice/VALIDATION.md
→ Flow 7 Voice identity/validation/evidence

renderer/CONTRACT.md
→ deterministic projection/compositor/delivery mechanics
```

## Canonical vs derived

Canonical project/Voice meaning lives under project `work/` and `state/` owners. Normal human-facing derived delivery is:

```text
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

`prd.html` is the single human-facing project document. Generated output never outranks canonical sources and must not be hand-patched to hide an upstream defect.

## Protected boundaries

- Golden/runtime template bytes remain protected and byte-identical.
- Page family, navigation and approved component vocabulary remain protected by `DESIGN-CONTRACT.md`.
- Adaptive cardinality applies inside approved flow/note/sequence component families; it does not authorize arbitrary new component types.
- Production Asset needs come from the approved project model, not a second design pass over generated PRD pages.
- Voice remains downstream from accepted project/PRD meaning.
- Machine-owned YAML is parsed as YAML, not line-oriented pseudo-YAML.
- Renderer/validator engine modules use domain-specific names; generic `_engine` collision paths are retired.
- Runtime and dev dependencies are separately pinned.
- The former DOCX export path remains retired.
- Browser visual claims and generated-audio quality require matching evidence.

For normal production start from `SKILL.md`. For a technical defect start from `AGENTS.md` and the smallest exact implementation owner.
