# Eleven v3 Voice Casting & Character Continuity

Last verified: **2026-09-09**

Purpose: keep one project Speaker recognizably the same actor across many Voice IDs while allowing moment-specific emotion, projection, pacing, and reactions. This is a craft reference for `../PERFORMANCE-WRITING.md`, not a new schema or cast database.

## Core principle

```text
approved Speaker identity
→ suitable ElevenLabs voice / target profile
→ stable actor baseline
→ moment-specific performance delta
→ expression direction
→ continuity review
```

A local emotion is a **delta from the actor baseline**, not permission to reinvent the character.

## 1. Actor Continuity Map

Reason internally over the dimensions that actually matter:

```text
Identity / Timbre
Native Cadence
Baseline Energy
Baseline Projection
Emotional Range
Projection Range
Language / Accent
Persona / Social Stance
No-Drift Boundary
Pronunciation Risk
```

Do not persist this map as another artifact. The canonical `Voice Cast` line remains compact.

## 2. Baseline vs local delta

Example:

```text
Speaker: Commander
Baseline: controlled, authoritative, measured, low emotional leakage
Range: calm → concerned → urgent
No-drift: cartoon aggression, constant shouting, trailer-announcer delivery

MOM-01 delta: restrained concern
MOM-02 delta: controlled urgency
MOM-03 delta: brief relief
```

Audio Tags then direct the **delta**:

```text
Commander baseline + [urgent]
```

not a new personality called `urgent`.

## 3. Voice-fit hierarchy

Current ElevenLabs v3 guidance makes voice selection the most important parameter. Before increasing direction complexity, verify:

```text
voice identity/timbre
→ language/accent fit
→ native cadence
→ required emotional range
→ required projection range
→ expected long-form stability
```

Internal result may remain:

```text
GOOD FIT
LIMITED FIT
RISKY FIT
UNKNOWN
```

A `LIMITED FIT` or `RISKY FIT` voice should not be rescued by tag stacking.

## 4. Cast selection rule

Prefer the voice that naturally covers the **largest required project envelope**, not merely the line that sounds best in isolation.

For a recurring Speaker, assess representative material that includes:

- ordinary baseline speech;
- the quietest required projection;
- the strongest required projection;
- at least one emotionally neutral line;
- at least one materially expressive line;
- the target language/accent;
- critical names/terms when pronunciation is a risk.

Preparation may establish a Target Voice Profile before final voice selection. Generation readiness requires the intended actual voice.

## 5. No-drift boundary

Every recurring Speaker should have a small internal negative boundary: what the actor should **not** become.

Examples:

```text
reserved scientist
→ do not drift into heroic announcer or comic panic

warm guide
→ do not drift into exaggerated childlike cheerfulness

field commander
→ do not turn every urgent line into shouting
```

Use this boundary during project-level Voice Script Readiness. Do not create a persisted `Do Not` schema.

## 6. Speaker continuity across many Voice IDs

Review the sequence as:

```text
Actor Baseline
→ MOM-01 Delta
→ MOM-02 Delta
→ MOM-03 Delta
→ return / evolution consistent with project context
```

A strong individual line still fails Character Continuity if its acting style belongs to a different character.

Continuity does **not** mean every line uses the same sentence structure, energy, tag, or pacing.

## 7. Narrator continuity

For narration, preserve both:

```text
Narrator Baseline
+ current narrative/emotional arc
```

A useful mental model:

```text
orientation
→ curiosity
→ reveal
→ unease
→ urgency
→ resolution
```

The narrator remains the same actor while local state changes. Use `v3-expression-direction.md` for state anchors/transitions and TTS previous/next context for prosodic continuity.

## 8. Multi-speaker contrast

Text to Dialogue should preserve intentional speaker contrast without pushing actors into caricature.

Check:

- distinct enough timbre/persona to identify speakers;
- compatible language/accent behavior;
- each actor remains inside their own range;
- reaction tags express the moment, not generic personality replacement;
- turn-to-turn escalation still sounds like the same people.

## 9. Voice identity for reproducibility

When actual generation begins, retain the **actual ElevenLabs `voice_id`** and voice source/type in generation evidence when useful. Display names are not sufficient production identity.

Current ElevenLabs Default voices are being replaced and are scheduled to expire on **2026-12-31**. Do not make a long-lived project reproducibility assumption based only on a Default voice display name. If a project uses one, plan re-casting before expiry and treat the replacement as a voice-fit decision rather than a name substitution.

## 10. Character Continuity Conservation

A recurring Speaker passes when:

- identity/timbre/persona remain recognizable;
- local emotion is plausible relative to the actor baseline;
- no line exceeds the actor range merely because a tag requests it;
- no-drift boundaries remain intact;
- language/accent behavior stays compatible;
- expressive variation does not collapse into one repetitive delivery template;
- narration/dialogue arcs evolve without unexplained character mutation.

This is part of integrated Voice Script Readiness, not a new acceptance field.

## Current official sources

- `https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices`
- `https://elevenlabs.io/docs/overview/capabilities/voices`
- `https://elevenlabs.io/docs/help-center/product/voices/my-voices/how-do-i-access-eleven-labs-default-voices`
- `https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-do-i-select-the-language-and-accent`
