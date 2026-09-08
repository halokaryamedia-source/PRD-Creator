# Eleven v3 Text to Dialogue Generation

Last verified: **2026-09-08**

Purpose: current production reference for generating conversationally dependent multi-speaker Voice moments without changing PRD-Creator's canonical `VO-...` identity model.

## 1. When to use Text to Dialogue

Use Eleven v3 Text to Dialogue when **multiple speakers participate in the same approved Moment and the delivery of later turns materially depends on the preceding turns**.

Examples:

- question → answer;
- interruption or overlap;
- tension/reaction/escalation between characters;
- conversational timing where generating each line independently would lose context.

Prefer normal Text to Speech when a Voice ID is effectively standalone even if other speakers exist elsewhere in the project.

```text
same speaker / independent line
→ TTS

multiple speakers + same Moment + response dependency
→ Text to Dialogue
```

Do not route to Dialogue merely because two Voice IDs are adjacent in a document.

## 2. Canonical identity stays unchanged

PRD-Creator does not create a persistent Dialogue ID or duplicate Dialogue script.

```text
MOM-...
├─ VO-A-01
├─ VO-B-01
├─ VO-A-02
└─ VO-B-02
        ↓ generation only
ordered Text to Dialogue inputs
```

Each `inputs[]` turn is derived from one existing canonical Voice entry:

```text
voice_id ← intentionally selected ElevenLabs voice for that Speaker
text     ← exact reviewed performance payload for that VO ID
```

The ordered generation group is temporary operator context. If wording changes after review, update the affected canonical `VO-...` entry first.

## 3. Current API facts

Text to Dialogue:

- uses Eleven v3;
- accepts ordered inputs containing `text` + `voice_id`;
- supports Audio Tags inside each turn's text;
- is nondeterministic;
- supports optional `seed` as best-effort consistency, not guaranteed determinism;
- supports `language_code`, pronunciation dictionaries, and text-normalization controls on current API surfaces;
- should keep total `inputs[].text` at or below roughly 2,000 characters per request for reliable generation;
- the current API endpoint accepts at most 10 unique voice IDs per request.

If a scene exceeds current request limits, split only at semantic/conversational boundaries. Do not cut inside one important response beat merely to equalize chunk size.

## 4. Audio Tags inside Dialogue

Keep the same SoundMaker discipline used by standalone Voice:

```text
spoken wording
→ beat structure
→ punctuation / line structure
→ selective emphasis
→ minimal Audio Tags
```

Tags belong inside the turn they should affect. Do not add a global tag cluster outside the turn list and do not use environmental SFX instructions as a substitute for the separate SFX lane.

## 5. Candidate generation

ElevenLabs explicitly notes that several Dialogue generations may be needed to get the desired result.

Production rule:

```text
reviewed canonical turns + selected voices/settings
→ generate candidate
→ first result clearly acceptable?
   yes → continue review/approval
   no  → compare available same-content candidate/regeneration first
→ same defect repeats?
   yes → diagnose prompt/settings/voice/surface
   no  → prefer best take without unnecessary rewrite
```

Do not churn canonical wording because one nondeterministic take was merely weaker.

## 6. Dialogue review

Evaluate the complete exchange and each constituent VO ID:

- required meaning/intelligibility;
- speaker identity and voice fit;
- turn-to-turn reaction/timing;
- emotional progression;
- interruption/overlap behavior when intended;
- pronunciation;
- pacing and landing;
- artifacts or unintended drift;
- compatibility with any authoritative timing constraint.

A strong overall conversation does not excuse a constituent line dropping required communication.

## 7. Timestamps

Use `POST /v1/text-to-dialogue/with-timestamps` when generated timing materially helps subtitles, animation, scripted events, or measurement.

Current response evidence may include:

- `voice_segments` with `voice_id`, start/end times, and dialogue input index;
- character-level alignment;
- normalized alignment when available.

Use generated timestamps as evidence of **that take**. Do not treat them as a source-level timing requirement, and do not persist them into canonical Voice wording unless another owner genuinely needs generated implementation data.

## 8. Generation identity

When audio approval/reproducibility matters, retain enough operator/evidence context to identify the selected take:

```text
Moment ID
ordered constituent VO IDs
model_id
actual ElevenLabs voice_id per Speaker
surface / endpoint
Stability/settings
language_code when used
pronunciation dictionary version(s) when used
text-normalization mode when material
seed when used
selected candidate/take
actual generated duration/timestamps when measured
```

Do not add these as mandatory fields to every `voice-production.md` line. Canonical script stays compact; generation identity belongs to actual generation evidence/operator context.

## 9. Failure routing

```text
wrong fact / wrong turn meaning
→ Flow 5 / upstream project authority

correct meaning but weak spoken performance
→ Flow 6 canonical prompt

individual turns good but interaction flat/unnatural
→ Dialogue surface + candidate/settings/voice-fit review

one speaker repeatedly ignores required range
→ voice fit before tag stacking

timing evidence needed
→ with-timestamps generation

non-dialogue environmental sound needed
→ production-assets/SOUND-EFFECTS.md
```

## 10. Current official sources

- `https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue`
- `https://elevenlabs.io/docs/eleven-api/guides/cookbooks/text-to-dialogue`
- `https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert`
- `https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert-with-timestamps`
- `https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices`

Re-check when live/API behavior conflicts with this reference or when request limits/settings change materially.
