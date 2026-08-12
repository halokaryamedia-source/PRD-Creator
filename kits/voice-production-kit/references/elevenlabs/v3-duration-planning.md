# Eleven v3 Duration Planning

Purpose: make duration a design input before script writing, while staying honest that normal Text to Speech duration is dynamic.

## 1. What ElevenLabs can and cannot guarantee

### Normal Text to Speech / Dynamic Duration

**OFFICIAL-CURRENT:** generated duration depends on the text and voice. Normal Speech Synthesis does not guarantee that a script will land on an exact second count.

An `Estimated Duration` in `work/voice-production.md` remains an expectation until actual audio exists.

### Voiceover Studio Fixed Duration

**OFFICIAL-PRODUCT-SPECIFIC:** Voiceover Studio supports **Fixed Duration**, which adjusts generated audio to fit a specified clip length.

Trade-off: ElevenLabs warns that forcing a clip far away from its natural duration can make speech sound unnaturally fast or slow.

Use Fixed Duration when exact synchronization is genuinely more important than fully natural pacing. It is not the default solution for ordinary game VO.

## 2. Duration must be planned before the final wording

When the user says:

```text
"maximum 10 seconds"
"around 15 seconds"
"must fit 30 seconds"
```

resolve the duration class first:

- **target range** — approximate timing, naturalness first;
- **hard maximum** — must stay below a cap;
- **fixed-sync** — must fill an externally defined timeline.

Do not finish a long script and then try to compress it using `[rushed]`, tag spam, or extreme playback/speed settings.

## 3. Word-budget formula

Use this planning formula:

```text
raw_words = target_seconds × planning_WPM / 60
```

For expressive speech, leave room for pauses, reactions, reveals, and strong landings:

```text
safe_words = raw_words × (1 - expressive_reserve)
```

The WPM values below are **production heuristics**, not ElevenLabs guarantees.

Suggested fallback planning classes when no project-calibrated audio exists:

| Performance | Planning range |
|---|---:|
| Slow / mysterious / emotional | 130–145 WPM |
| Clear cinematic | 140–155 WPM |
| Natural narration | 150–170 WPM |
| Energetic | 170–185 WPM |
| Very urgent | 185–200 WPM only when clarity remains safe |

For a hard duration cap, reserve roughly **10–15%** rather than filling the mathematical maximum. This is an internal safety heuristic, not an ElevenLabs feature.

## 4. Safe first-draft word budgets

Use these only as a starting point when no calibrated voice data exists:

| Target audio | Safe first draft |
|---:|---:|
| 5 sec | ~10–13 spoken words |
| 8 sec | ~16–20 |
| 10 sec | ~20–25 |
| 12 sec | ~24–30 |
| 15 sec | ~30–37 |
| 20 sec | ~40–50 |
| 30 sec | ~60–72 |
| 45 sec | ~90–110 |
| 60 sec | ~120–145 |

Use the lower side for more pauses/emotional movement. Use the upper side for clean energetic delivery with few pauses.

## 5. Examples

### Maximum 10 seconds

Natural/cinematic planning at 150 WPM:

```text
10 × 150 / 60 = 25 raw words
```

With expressive reserve, prefer roughly 20–23 words if the line includes hesitation, a reveal, or a strong final command.

### Around 15 seconds

```text
15 × 150 / 60 = 37.5 raw words
```

For expressive cinematic speech, roughly 30–35 spoken words is a safer first draft.

### Around 30 seconds

```text
30 × 160 / 60 = 80 raw words
```

For a narration with several emotional beats, roughly 65–72 spoken words is a safer first draft.

## 6. Project-calibrated duration is stronger than generic WPM

Once approved audio exists, calculate the actual effective speaking rate:

```text
calibrated_WPM = spoken_word_count / actual_seconds × 60
```

Example:

```text
42 spoken words
17.2 seconds
≈ 146.5 WPM
```

For the next line using the same voice/model/performance family, use that project rate instead of a generic internet average.

Do not assume one global rate for every performance. Maintain calibration by meaningful class when enough evidence exists:

```text
Voice X / v3
natural narration      ~ calibrated rate
mysterious / reflective ~ calibrated rate
urgent                  ~ calibrated rate
```

Only create these categories after actual approved audio exists. Do not populate fake values.

## 7. Hard maximum strategy

For `max N seconds`:

1. choose the performance class;
2. use calibrated WPM if available, otherwise fallback planning WPM;
3. calculate the raw word budget;
4. reserve 10–15% when the line needs expressive pauses/reactions;
5. write the script within the budget;
6. do not add filler merely to use the full duration;
7. actual audio remains the final duration evidence.

A `max 10 sec` line is healthier at 8.5–9.5 seconds than at 10.8 seconds.

## 8. Fixed-sync strategy

For exact external timing:

```text
write near the natural word budget
→ generate/review natural delivery
→ if exact sync is mandatory, use a product/workflow that supports fixed duration or downstream timing adjustment
```

Do not force a script that naturally needs 20 seconds into a 10-second slot. Rewrite the communication scope/wording first if the required meaning can be preserved.

## 9. Speed control caveat

Current ElevenLabs official documentation is internally inconsistent:

- one current Text to Speech product-guide section says Speed is not available for Eleven v3;
- an FAQ on current ElevenLabs documentation says Speed 0.7–1.2 is available for all voices/models.

Therefore status is **UNKNOWN / UI-DEPENDENT** for this repository's web v3 workflow.

Rules:

- do not make Speed a required v3 duration-control mechanism;
- use the actual current ElevenLabs UI as authority for whether the control is present;
- even when available, word budget and natural performance structure remain the primary duration tools;
- extreme speed changes may reduce quality according to ElevenLabs.

## 10. Duration evidence states

Use honest language:

- **Estimated Duration** — calculated/planned only;
- **Generated Duration** — actual file exists and duration was measured;
- **Approved Duration** — generated audio was heard/accepted for the production use case.

Never call a planned WPM estimate measured audio proof.
