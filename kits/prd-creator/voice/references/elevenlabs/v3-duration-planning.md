# Eleven v3 Duration Planning

Purpose: make duration a design input before script writing while staying honest that normal Eleven v3 TTS/Dialogue duration is dynamic.

## 1. Duration classes

Resolve timing before final wording:

- **target range** — approximate; naturalness first;
- **hard maximum** — must remain below a cap;
- **fixed-sync** — must fit an externally fixed timeline.

Standard Eleven v3 generation does not guarantee exact seconds from text alone. The former Voiceover Studio exposed a legacy Fixed Duration workflow, but that product was sunset on 2026-05-15; do not depend on that legacy control as current production policy.

For current production, plan the script near the natural target first, generate/measure the actual take, then use current supported surface controls only when they genuinely help without degrading naturalness.

## 2. Evidence hierarchy

Use the strongest available evidence in this order:

```text
nearest approved same-project sample
(same voice + similar performance + similar words/beats)
        ↓
project-calibrated performance-class rate
        ↓
generic planning WPM
```

Do not fabricate calibration when no approved audio exists.

### Preparation Mode with no audio evidence

This is valid and does not block script preparation.

Use generic planning WPM + a safety reserve and label the result only as **Estimated Duration**.

### When approved audio exists later

Prefer a nearby approved sample over one global project WPM because two lines with the same word count can differ materially when beat count, pauses, reactions, or delivery style differ.

Compare approximately:

```text
same voice
+ similar performance family
+ similar spoken-word count
+ similar beat/pause density
```

Use the closest useful evidence rather than forcing every line into one average.

## 3. Generic fallback formula

When no project calibration exists:

```text
raw_words = target_seconds × planning_WPM / 60
safe_words = raw_words × (1 - expressive_reserve)
```

These are planning heuristics, not ElevenLabs guarantees.

| Performance | Fallback planning range |
|---|---:|
| Slow / mysterious / emotional | 130–145 WPM |
| Clear cinematic | 140–155 WPM |
| Natural narration | 150–170 WPM |
| Energetic | 170–185 WPM |
| Very urgent | 185–200 WPM only when clarity remains safe |

For a hard cap, reserve roughly **10–15%** when pauses, reactions, reveal beats, or a strong landing are expected.

## 4. Safe first-draft budgets

Use only as a no-calibration starting point:

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

Use the lower side for heavier emotional movement/pause density; use the upper side for clean energetic delivery with few pauses.

## 5. Beat-aware planning

Word count alone is not enough.

Before finalizing a timed line, note whether it contains:

- many short beat boundaries;
- deliberate ellipses / dramatic pivots;
- vocal reactions;
- repeated words / hesitation;
- a slow reveal;
- a strong isolated ending.

More of these usually requires more timing reserve. Do not invent an exact seconds-per-pause formula.

For a same-Moment Text to Dialogue group, also reserve for turn-taking, reactions, interruption/overlap behavior, and the fact that each turn influences the surrounding conversational rhythm.

## 6. Practical examples

### Maximum 10 seconds

At 150 WPM:

```text
10 × 150 / 60 = 25 raw words
```

For an expressive line, roughly 20–23 spoken words is a safer first draft.

### Around 15 seconds

```text
15 × 150 / 60 = 37.5 raw words
```

For expressive cinematic speech, roughly 30–35 spoken words is a safer starting point.

### Around 30 seconds

```text
30 × 160 / 60 = 80 raw words
```

For several emotional beats, roughly 65–72 spoken words is a safer starting point.

## 7. Calibration when audio exists

A simple calibrated rate can be computed as:

```text
calibrated_WPM = spoken_word_count / actual_seconds × 60
```

Use it only for reasonably similar voice/performance conditions.

If enough evidence eventually exists, keep meaningful performance classes such as:

```text
natural narration
mysterious / reflective
urgent / warning
```

Do not populate categories with guessed values.

For Text to Dialogue, prefer generated segment/take timing from actual audio or the current `with-timestamps` endpoint over inferring each speaker's timing from a project-wide WPM.

## 8. Hard maximum strategy

For `max N seconds`:

1. choose the performance family;
2. use nearest approved evidence if available;
3. otherwise use calibrated class rate;
4. otherwise use fallback WPM;
5. reserve expressive margin;
6. write within the resulting spoken-word budget;
7. preserve required meaning and landing;
8. generate and measure when the hard cap matters operationally;
9. do not add filler merely to use the full slot.

A line safely under the cap is preferable to one that only fits if the model rushes unnaturally.

## 9. Fixed-sync strategy

For exact external timing:

```text
write near natural word budget
→ preserve required meaning
→ choose correct generation surface
→ generate
→ measure actual take / use timestamps when available
→ revise wording first if materially off target
→ use current supported speed/timeline controls only when appropriate
```

Do not force a line that naturally needs much longer into a short slot. Rewrite the communication load first when possible.

Generated timestamps are evidence for that take, not upstream timing authority.

## 10. Speed caveat

Current official ElevenLabs guidance is surface-dependent and has changed over time. Current consolidated Best Practices describes a Text to Speech/API Speed setting with `1.0` as unchanged, while older/surface-specific v3 pages may differ.

Repository rules:

- use the **active current surface/API** as authority for whether Speed is available;
- when exposed, keep `1.0` / unchanged as the natural baseline;
- word budget + natural spoken architecture remain primary;
- use only small bounded Speed changes after the wording already fits the intended duration reasonably well;
- current guidance warns extreme Speed values can reduce quality;
- do not make Speed a required mechanism or invent it on a surface that does not expose it;
- Speed is never a substitute for correctly sized, naturally phrased speech.

## 11. Evidence labels

Use truthful labels:

- **Estimated Duration** — planning only; no audio required;
- **Generated Duration** — actual generated file/take duration measured;
- **Approved Duration** — generated audio reviewed/accepted for its use case.

Preparation Mode can stop at Estimated Duration. Never promote an estimate to generated/approved evidence without actual audio.