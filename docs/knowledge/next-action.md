# Next Action

Updated: 2026-08-13

## Current Status

`CLOCKWORK_VOICE_DIRECTED_UI_READY`

Working branch: **`Local` only**.

## Current state

Project Document Generator PRD core remains **v1.13.0**. Voice Production Kit is now **v1.11.0** and remains **Eleven v3 only**.

Clockwork continues to use the approved one-document architecture:

```text
accepted PRD
↓
12 justified Voice asset requirements
↓
Eleven v3 Voice Production
↓
same output/final.html
   PRD core
   + Production Assets → Voice
```

Voice remains a downstream development asset from the accepted PRD. Clockwork PRD canonical meaning/render-data was not changed by this Voice quality pass.

## Directed performance rule

Every standalone canonical `performance` block now begins with at least one initial Audio/Performance Direction Tag on its first non-blank line.

This is a **SoundMaker production rule** for intentionally directed Eleven v3 work, not a claim that Eleven v3 technically rejects untagged text.

Use:

```text
initial direction tag
→ required once per standalone Voice ID

transition tag
→ only when the scene creates a material audible state change
```

Tag stacking remains minimal. One initial tag is enough for a stable reminder; additional tags are not added merely to make the prompt look expressive.

Renderer and Voice validator now fail closed when a Voice Production entry has no initial performance direction.

## Clockwork Voice Production

Current canonical project files:

```text
work/voice-requirements.md
work/voice-production.md
work/voice-acceptance.md
state/voice-state.yaml
output/final.html
```

Current Voice Setup baseline:

```text
Custodian Vex → William Shanks - Rich and Deep
Model → Eleven v3
```

The commercial voice is selected for preparation/operator use but has **not** been audio-tested or audio-approved.

Exactly 12 justified Voice assets remain prepared in gameplay order across:

```text
The Antechamber
The Resonance Engine
The Broken Gallery
The Warden Halls
The Gremlin's Workshop
Vault Restored
```

All 12 now have explicit starting performance direction. Mid-script transition tags are used only where the delivery materially changes, for example the Antechamber reveal → reassurance, Workshop sabotage reaction → firm reroute instruction, and ending reflection → warm reward landing.

Voice was deliberately not added to every interaction/checkpoint/chime. Existing visual/local gameplay feedback remains primary where narration would only duplicate information.

## Production Assets HTML

`output/final.html` remains the single human-facing project document.

The Voice presentation has been simplified from nested grey cards into a lighter editorial production layout.

`Production Assets → Voice` now shows:

- **Voice Setup** once, with the selected ElevenLabs voice prominent;
- gameplay-ordered Voice title;
- Speaker + Estimated Duration as secondary metadata;
- one integrated **ElevenLabs Text** panel;
- performance-direction tags visually distinct from spoken text;
- **Copy** integrated into the script panel.

The visible spoken text uses regular/medium weight so CAPS, punctuation, and performance tags retain contrast.

The exact canonical `performance` payload remains hidden as the Copy source, so visual formatting does not change what is pasted into ElevenLabs.

Internal Flow 5 requirement metadata, source refs, SoundMaker reasoning, WPM math, QA, and acceptance state remain outside the visible page.

## Validation

Current non-audio Voice delivery state remains:

```text
Status: voice_delivery_ready
Mechanical: PASS
Voice Script Readiness: PASS
Communication Conservation: PASS
Project HTML Visual: PASS
Audio Evidence: not_provided
Critical: 0
Major: 0
```

Focused regression proof covers:

- renderer rejects a canonical Voice entry without an initial performance direction;
- Voice validator rejects the same defect;
- exact copied prompt parity remains intact;
- visible performance tags are derived from the canonical prompt;
- projects without Voice Production still receive no Production Assets extension.

Representative desktop browser inspection passed on the redesigned:

- Antechamber page with Voice Setup and two prompts;
- Gremlin's Workshop page with one baseline tag and one three-beat sabotage transition;
- Vault Restored page with reflective → warm performance movement.

No clipping, overlap, nested-card heaviness, or loss of PRD visual language was observed in those representative pages.

## Audio boundary

No ElevenLabs generation, listening, A/B comparison, measured-duration calibration, or generated-audio quality claim has been performed.

`voice_delivery_ready` still means the **non-audio script + consolidated project HTML** are production-ready. It does not mean the generated Voice assets or selected commercial voice are audio-approved.

## Overdevelopment guard

Do not add a generic Asset framework, second Voice HTML, asset manifest, new Flow, tag score, large tag library, SFX/Visual implementation, or more proof layers without a concrete production need.

## Next Step

**Keep Clockwork v1.11 as the non-audio directed-production baseline; enter SoundMaker Generation Mode only when the user explicitly asks to generate/test audio, or reopen only the affected Voice ID if content/performance wording is revised.**
