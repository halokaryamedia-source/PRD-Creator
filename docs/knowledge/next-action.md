# Next Action

## Current Status

`PRD_SCOPE_BOUNDARY_HARDENING_IMPLEMENTED`

The six-map Map Composition Audit is complete and its approved product conclusion has been translated into a bounded PRD-Creator semantic hardening. The work does **not** redesign the Golden document, renderer, Production Assets presentation, Voice, repository architecture, or accepted Clockwork output.

## Evidence Completed

The official six-map development sample set was successfully extracted and inspected in the 2026-08-18 session:

```text
3#Angry bird.zip
6#Avatar_Legends.zip
16#Ice Age.zip
23#Sherlock Holmes.zip
24#Minions DLC.zip
29#NinjaWeaponAcademy.zip
```

The audit compared finished-map world/BP/RP structure, readable functions/scripts/configuration, entities/interactables, assets, UI/audio, progression/state/reset patterns, and world/session configuration where accessible. Ice Age provided valid structural/world/pack evidence, but much of its internal non-manifest pack payload was not readable as normal plaintext; no unsupported gameplay meaning was inferred from filenames or IP/theme knowledge.

The audit showed that PRD-Creator already covers most professional map concerns through existing Gameplay, Level Design, Developer, lifecycle, quantitative coherence, known constraints, reset/data, and Production Assets owners. The main reusable gap was narrower: technical/as-built source evidence could be mistaken for canonical PRD meaning unless the PRD scope boundary is explicit.

## Accepted Product Decision

Canonical PRD is a **pre-build production specification**, not a forensic/as-built implementation document.

Preserve when material:

- gameplay/product requirements;
- build and production requirements;
- approved dimensions, counts, timing, capacities, spatial relationships, route/boundary intent, relative/functional placement, visibility/readability, and other design-owned constraints;
- explicit approved technical constraints that production must obey.

Do not promote by default:

- exact world coordinates or map-instance locators, including final spawn/teleport/checkpoint/trigger/ticking-area/bounding coordinates;
- incidental scoreboard names, tags, function paths, runtime IDs, UUIDs, pack/file identifiers, debug/setup residue, or other details that only describe how one finished implementation happened to realize the requirement.

Source evidence is not deleted. When technical/as-built evidence contains useful meaning, recover the underlying production requirement while retaining the source for provenance.

The boundary is semantic, not vocabulary-based. A technical detail becomes a legitimate PRD constraint when the user/client explicitly requires it or another approved system materially depends on it. Spatial design remains valid even though exact world coordinates are excluded.

## Implementation Boundary

The approved hardening is owned by:

```text
docs/foundation/02-source-intake-recovery.md
→ durable canonical PRD-scope policy

kits/prd-creator/intake/SOURCE-INTAKE.md
→ operational recovery of requirement meaning vs implementation evidence

kits/prd-creator/document/CONTENT-CONTRACT.md
→ Material Conservation applies to resolved PRD-scope meaning and must not reintroduce excluded as-built residue

kits/prd-creator/document/VALIDATION.md
→ existing Semantic Readiness / Material Conservation lenses verify the boundary without a new PASS surface
```

No new schema, requirement taxonomy, keyword blacklist, coordinate detector, compatibility framework, validator subsystem, Flow, Skill, visible panel, or acceptance section is introduced.

## 01–04 Result

```text
01 Overview
→ no direct contract redesign; receives cleaner upstream project meaning.

02 Gameplay Flow
→ no direct contract redesign; existing player-readable situation → action → response → recovery → result → transition contract remains authoritative.

03 Development
→ existing structure remains; Material Conservation is clarified so complete production behavior survives without forcing incidental as-built identifiers/coordinates into the PRD.

04 Production Assets
→ no contract change required; existing MODEL / ITEM / UI-TEXT / AUDIO / PARTICLE boundary and anti-speculative rules remain authoritative.
```

## Protected Baseline

Do not reopen these as a consequence of this hardening unless new concrete evidence proves a separate defect:

- Golden/template visible composition;
- renderer/compositor behavior;
- PRD page family or labels;
- `kits/prd-creator/production-assets/CONTRACT.md`;
- Voice requirements, wording, production, or validation;
- accepted Clockwork canonical/project output;
- repository architecture or root Skill set.

Clockwork remains useful regression evidence because its approved requirement state already demonstrates the intended boundary: technical Objective 4 grid coordinates stay outside the PRD while gameplay/spatial production meaning remains documented.

## Review / Proof Standard

Use semantic adversarial cases rather than a keyword blacklist:

```text
finished teleport coordinate
→ preserve transition meaning; do not promote coordinate

approved 30×30 arena size
→ preserve

machine centered in chamber / visible from entrance
→ preserve

explicit Minecraft Education compatibility requirement
→ preserve

observed tag/scoreboard/function identifier only
→ do not promote unless explicitly required as a technical constraint
```

A good existing PRD should remain materially unchanged. The expected effect is better source judgment, not more document sections or more prose.

## Next Step

**Use the hardened scope boundary on the next real new/revised PRD production and treat only a concrete misclassification/regression as evidence for further bounded change; do not proactively redesign 01–04 or extend this audit into new frameworks.**
