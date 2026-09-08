---
name: voice-production
description: Semantic/product-contract specialist for PRD-Creator Flow 5–7. Use when accepted PRD → Voice scope, communication intent, canonical Voice production meaning, natural spoken delivery, expression preservation, communication conservation, or Voice readiness/delivery semantics are the actual problem. Do not use as a generic renderer/validator wrapper when semantics are already correct.
---

# Voice Production

Own **semantic judgment** for Voice Flow 5–7. Detailed execution and Eleven v3 craft stay with the nearest package owner.

## Authority

```text
accepted project / PRD meaning
→ canonical Voice requirements
→ canonical Voice Production
→ Voice acceptance / delivery evidence
```

Project authority owns gameplay/story truth. Voice may interpret approved communication/performance needs but may not invent upstream facts.

## Use when

- deciding whether a Voice moment is justified;
- completing Flow 5 communication/context meaning;
- judging whether Flow 6 speech preserves both meaning and intended expression;
- diagnosing stiff, flat, over-directed, or emotionally ambiguous narration/dialogue;
- distinguishing Voice semantic/craft defects from renderer/validator defects;
- judging whether Flow 7 evidence truthfully supports readiness/delivery.

## Detailed owners

```text
Flow 5 scope/context
→ kits/prd-creator/voice/EXTRACTION.md

Flow 6 lifecycle/policy
→ docs/foundation/06-elevenlabs-script-production.md

Eleven v3 writing + expression + generation routing
→ kits/prd-creator/voice/PERFORMANCE-WRITING.md

Flow 7 validation/evidence
→ kits/prd-creator/voice/VALIDATION.md
```

## Flow 6 judgment

Canonical Voice Production owns final spoken wording and performance craft inside the approved Voice contract.

### Naturalness

Preserve approved meaning, not accidental PRD sentence syntax. Convert requirements into speech appropriate to Speaker, Trigger, Channel, and listener state.

Naturalness is register-specific; narrator, radio, tutorial, warning, and NPC dialogue do not share one casual style.

### Expression preservation

Audio Tags are a **first-class Eleven v3 acting control**.

Do not require a tag merely to satisfy formatting. Instead require **Expression Coverage**:

```text
no material acting state beyond voice/text baseline
→ zero-tag line may be correct

material emotion / subtext / projection / pacing / reaction / transition
→ explicit direction must be sufficient
→ use precise Audio Tag(s) when voice + wording + punctuation + context do not fully specify it
```

A material opening state should be anchored at the opening. A material state change should be directed near the transition. Reactions belong at their event point.

Do not treat `fewest tags` as the goal. The goal is complete expression coverage without redundant or conflicting direction.

### Generation continuity

Connected same-speaker narration may use adjacent text/request context without changing canonical `VO-...` wording. Each new TTS request may reset acting state; when a specific state must continue at the new clip opening, re-anchor it explicitly.

Response-dependent multi-speaker Voice IDs in the same Moment may use Text to Dialogue. Existing `VO-...` identities remain canonical.

## Flow 7 judgment

Mechanical parity does not prove naturalness, expression, visual quality, or generated-audio quality.

Preparation may establish:

- Communication Conservation;
- Naturalness;
- Expression Conservation;
- Voice Script Readiness.

Actual audio quality still requires heard evidence.

## Routing boundary

```text
Voice meaning / communication contract wrong
→ Voice semantic owner / Flow 5

meaning correct; wording stiff or expression under/over-directed
→ Flow 6 SoundMaker

Voice meaning correct; presentation / validator / CLI mechanics wrong
→ exact implementation owner

non-dialogue SFX
→ production-assets/SOUND-EFFECTS.md
```

## Proof economy

- recover current project/Voice context before asking;
- revise only invalidated scope;
- preserve meaning and acting intent, not document syntax;
- do not create duplicate expression schemas, scorecards, manifests, or approval layers;
- stop when current semantic/craft scope is correct and sufficiently proven.

## Boundary

This skill owns Voice Flow 5–7 **semantic judgment** only. Detailed procedure and executable mechanics stay with package owners.
