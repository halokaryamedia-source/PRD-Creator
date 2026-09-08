---
name: voice-production
description: Semantic/product-contract specialist for PRD-Creator Flow 5–7. Use when accepted PRD → Voice scope, communication intent, canonical Voice production meaning, natural spoken delivery, actor continuity, expression preservation, pronunciation/language control, or Voice readiness/delivery semantics are the actual problem. Do not use as a generic renderer/validator wrapper when semantics are already correct.
---

# Voice Production

Own **semantic judgment** for Voice Flow 5–7. Detailed Eleven v3 craft stays with the nearest package owner.

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
- judging whether Flow 6 speech preserves meaning, actor identity, expression, and critical pronunciation;
- diagnosing stiff, flat, over-directed, emotionally ambiguous, character-drifting, or language/pronunciation-risky narration/dialogue;
- distinguishing semantic/craft defects from renderer/validator defects;
- judging whether Flow 7 evidence truthfully supports readiness/delivery.

## Detailed owners

```text
Flow 5 scope/context
→ kits/prd-creator/voice/EXTRACTION.md

Flow 6 lifecycle/policy
→ docs/foundation/06-elevenlabs-script-production.md

Eleven v3 writing + actor + expression + pronunciation + generation routing
→ kits/prd-creator/voice/PERFORMANCE-WRITING.md

Flow 7 validation/evidence
→ kits/prd-creator/voice/VALIDATION.md
```

## Flow 6 judgment

Canonical Voice Production owns final spoken wording and reversible performance craft inside the approved Voice contract.

### Naturalness

Preserve approved meaning, not accidental PRD syntax. Naturalness is register-specific; narrator, radio, tutorial, warning, and NPC dialogue do not share one casual style.

### Actor / Character Continuity

For recurring Speakers, local emotion is a performance **delta from a stable actor baseline**. Voice fit should cover required identity/timbre, cadence, energy, emotional/projection range, language/accent, and no-drift boundaries.

Do not use Audio Tags to force a voice outside its practical envelope or to reinvent a character between Moments.

### Expression preservation

Audio Tags are first-class Eleven v3 acting controls. Do not require a tag for formatting; require **Expression Coverage**.

```text
no material acting state beyond actor/text baseline
→ zero-tag line may be correct

material emotion / subtext / projection / pacing / reaction / transition
→ explicit direction must be sufficient
```

Opening states, transitions, and reactions should be directed where they actually occur.

### Language / Pronunciation

Critical names, project terminology, acronyms, numbers/dates/symbols, and code-switched terms require an intentional spoken strategy when materially risky. Prefer language/accent-compatible voices; use explicit spoken forms, IPA/phoneme control, or pronunciation dictionaries only where needed.

Preparation identifies risk; heard evidence is required for pronunciation approval.

### Generation continuity / variance

Connected same-speaker narration may use adjacent text/request context without changing canonical `VO-...` wording. Each new TTS request may reset acting state; re-anchor a required state when needed.

Response-dependent multi-speaker Voice IDs in the same Moment may use Text to Dialogue. Existing `VO-...` identities remain canonical.

One weak nondeterministic take does not prove a prompt defect. Compare same-content candidates/regenerations first; after a repeated defect is established, change one variable class at a time.

## Flow 7 judgment

Mechanical parity does not prove naturalness, actor continuity, expression, pronunciation, visual quality, or generated-audio quality.

Preparation may establish:

- Communication Conservation;
- Expression Conservation;
- Character Continuity Conservation when applicable;
- Pronunciation Conservation;
- Voice Script Readiness.

Actual audio quality and pronunciation approval still require heard evidence.

## Routing boundary

```text
Voice meaning / communication contract wrong
→ Voice semantic owner / Flow 5

meaning correct; wording/actor/expression/pronunciation strategy wrong
→ Flow 6 SoundMaker

one weak take only
→ candidate variance review before canonical rewrite

Voice meaning correct; presentation / validator / CLI mechanics wrong
→ exact implementation owner

non-dialogue SFX
→ production-assets/SOUND-EFFECTS.md
```

## Proof economy

- recover current project/Voice context before asking;
- revise only invalidated scope;
- preserve meaning, actor identity, and acting intent;
- do not create duplicate cast databases, pronunciation manifests, candidate scorecards, or approval layers;
- stop when current semantic/craft scope is correct and sufficiently proven.

## Boundary

This skill owns Voice Flow 5–7 **semantic judgment** only. Detailed procedure and executable mechanics stay with package owners.
