# PRD Creator

**Version:** 1.14.0

PRD Creator is the single production kit for turning project discussion/source into one approved project model, a development-ready PRD, required Production Assets, and optional downstream Voice Production in the same project delivery.

## Product flow

```text
source + current instruction + approved decisions
→ requirement recovery / approved project model
→ PRD core 01–03
→ 04 Production Assets when required
→ Voice requirements when required
→ canonical Voice Production
→ one versioned project HTML
→ acceptance / delivery evidence
```

The kit is one package, but its domains remain separate. Project/PRD meaning, Production Asset requirements, and Voice meaning keep their own owners.

## Package map

```text
kits/prd-creator/
├─ README.md                  package navigation + Requirement Map
├─ AGENTS.md                  technical/file routing + context economy
├─ SKILL.md                   end-to-end Flow 2–7 Production Execution router
├─ intake/                    source intake + requirement recovery procedure
├─ document/                  PRD core 01–03 content/validation contracts
├─ production-assets/         non-Voice 04 resource contract
├─ voice/                     Voice requirement/craft/validation owners + references
├─ renderer/                  deterministic PRD + 04 composition and delivery
├─ validator/                 PRD, handoff, and Voice mechanical validators
└─ template/                  approved Golden/runtime template bytes
```

Open only the domain that owns the current task. Detailed contracts stay in those folders rather than being duplicated at package root.

## Requirement Map

| Requirement / canonical meaning | Project artifact | System owner |
|---|---|---|
| Project/gameplay requirement state | `state/requirement-register.yaml` | `intake/SOURCE-INTAKE.md` + Flow 2 policy |
| Canonical PRD-core meaning | `work/content.md` | `document/CONTENT-CONTRACT.md` |
| PRD render projection | `work/render-data.json` | `renderer/CONTRACT.md` |
| Non-Voice Production Asset requirements | `work/asset-requirements.md` | `production-assets/CONTRACT.md` |
| Voice requirements | `work/voice-requirements.md` | `voice/EXTRACTION.md` |
| Canonical Voice production | `work/voice-production.md` | Flow 6 policy + `voice/SOUNDMAKER.md` |
| PRD acceptance / handoff | `work/acceptance.md` + `state/handoff-state.yaml` | `document/VALIDATION.md` + validators |
| Voice acceptance / state | `work/voice-acceptance.md` + `state/voice-state.yaml` | `voice/VALIDATION.md` + `validator/validate_voice.py` |

Do not create a generic `requirements/` folder merely for naming symmetry. Requirement instances remain project artifacts; system contracts remain with the domain that owns them.

## Main domain owners

```text
intake/SOURCE-INTAKE.md
→ Flow 2 source recovery / completion / Simple Chat Preview

document/CONTENT-CONTRACT.md
→ exact PRD core 01–03 semantic + visible-composition contract

document/VALIDATION.md
→ Flow 4 semantic readiness / handoff procedure

production-assets/CONTRACT.md
→ exact non-Voice 04 resource/writing/readiness contract

voice/EXTRACTION.md
→ Flow 5 Voice scope/context extraction

voice/SOUNDMAKER.md
→ Eleven v3 performance-writing craft

voice/VALIDATION.md
→ Flow 7 Voice validation/evidence

renderer/CONTRACT.md
→ deterministic projection/compositor/delivery contract
```

Durable Flow policy remains under `docs/foundation/`.

## Canonical vs derived

Canonical project/Voice meaning lives under the project `work/` and `state/` owners. The normal human-facing derived delivery is:

```text
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

`prd.html` is the single human-facing project document. It contains the protected PRD core 01–03 and, when required, additive 04 Production Assets. Canonical Voice is presented there as `AUDIO` inside the matching gameplay moment; it is not duplicated into a second Voice HTML.

Generated output never outranks canonical sources and must not be hand-patched to hide an upstream defect.

## Protected boundaries

- Golden/runtime template bytes and approved PRD-core 01–03 composition remain protected.
- Production Asset needs come from the same approved project model, not a second design pass over generated 01–03.
- Voice Production is downstream from accepted project/PRD meaning and may not invent upstream facts.
- The former DOCX export path is retired.
- Generated-audio quality requires actual audio evidence.
- Root `tests/`, `tools/`, `.agents/skills/`, and `docs/foundation/` remain repository-level owners outside this package.

For normal production start from `SKILL.md`. For a technical defect start from `AGENTS.md` and the smallest exact implementation owner.