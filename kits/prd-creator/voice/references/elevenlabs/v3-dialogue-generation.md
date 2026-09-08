# Eleven v3 Text to Dialogue Generation

Last verified: **2026-09-08**

Purpose: generate conversationally dependent multi-speaker Voice moments while preserving canonical `VO-...` identity and turn-specific expression.

## 1. When to use Text to Dialogue

Use when multiple speakers participate in the same approved Moment and later delivery materially depends on preceding turns.

Examples:

- question → answer;
- interruption/overlap;
- tension/reaction/escalation;
- conversational timing that isolated TTS would lose.

Standalone lines remain normal TTS.

## 2. Canonical identity

No persistent Dialogue ID or duplicate script.

```text
MOM-...
├─ VO-A-01
├─ VO-B-01
├─ VO-A-02
└─ VO-B-02
        ↓ generation only
ordered Text to Dialogue inputs
```

Each turn derives from one canonical Voice entry:

```text
voice_id ← selected ElevenLabs voice for Speaker
text     ← exact canonical performance payload for that VO ID
```

## 3. Current API facts

Current Text to Dialogue:

- uses Eleven v3;
- accepts ordered `text` + `voice_id` inputs;
- supports Audio Tags inside each turn's text;
- is nondeterministic;
- supports optional seed as best-effort consistency;
- supports language/pronunciation/normalization controls on current API surfaces;
- should keep total input text around current reliable request guidance (roughly 2,000 characters);
- currently supports up to 10 unique voice IDs per request.

Split large scenes only at semantic/conversational boundaries.

## 4. Expression Coverage per turn

Do not reduce Dialogue direction to `minimal tags`. Each turn must preserve its material acting intent.

For every turn, review:

```text
Emotion
Attitude / Subtext
Projection
Pace / Rhythm
Intensity
Reaction
Transition from prior turn
Landing into next turn
```

Policy:

```text
baseline response with no material special acting
→ zero tag may be valid

material response state
→ explicit direction when needed

interruption / overlap / whisper / reaction / state shift
→ tag near the affected beat
```

Examples:

```text
[annoyed] You knew about this?
[defensive] I only found out this morning.
[interrupting] Then why didn't you tell me?
```

Tags stay inside the turn they affect. Do not create a Dialogue-level direction schema.

## 5. Conversational expression arc

Review the exchange as one performance, not isolated lines.

```text
Speaker A state
→ Speaker B reacts
→ A changes/holds state
→ B escalates/releases
```

A later turn should not mechanically repeat the same opening tag if its state has changed. Conversely, do not omit a critical reaction merely because the preceding turn provides context.

Text to Dialogue context helps interaction, but explicit acting cues are still appropriate when a turn must land in a specific way.

## 6. Candidate generation

Several generations may be needed.

```text
reviewed canonical turns + voices/settings
→ generate candidate
→ acceptable?
   yes → continue review
   no  → compare same-content candidate/regeneration first
→ same defect repeats?
   yes → diagnose Expression Coverage / tag placement / settings / voice fit
```

Do not churn canonical wording because one nondeterministic take is weaker.

## 7. Dialogue review

Evaluate:

- required meaning/intelligibility;
- speaker identity/voice fit;
- turn-to-turn reaction/timing;
- expression accuracy per turn;
- emotional progression;
- interruption/overlap when intended;
- pronunciation;
- pacing/landing;
- artifacts/drift;
- authoritative timing compatibility.

A strong overall conversation does not excuse a constituent line losing required meaning or expression.

## 8. Timestamps

Use the current timestamps endpoint when timing materially helps subtitles, animation, scripted events, or measurement.

Generated segment/character timing is evidence for that take, not source-level timing authority.

## 9. Generation identity

When approval/reproducibility matters, retain useful operator/evidence context:

```text
Moment ID
ordered VO IDs
model_id
voice_id per Speaker
surface / endpoint
Stability/settings
language/pronunciation/normalization when used
seed when used
selected candidate/take
actual duration/timestamps when measured
```

Do not add these as mandatory canonical line fields.

## 10. Failure routing

```text
wrong fact / turn meaning
→ Flow 5 / project authority

correct meaning but weak wording/expression
→ Flow 6 SoundMaker

individual turns good but interaction disconnected
→ Dialogue surface / candidate / voice-fit review

repeated ignored expression
→ voice fit + Stability + tag placement before more tag stacking

timing evidence needed
→ timestamps generation

non-dialogue environmental sound
→ production-assets/SOUND-EFFECTS.md
```

## Official sources

- `https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue`
- `https://elevenlabs.io/docs/eleven-api/guides/cookbooks/text-to-dialogue`
- `https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert`
- `https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert-with-timestamps`
- `https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices`
