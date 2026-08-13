# Next Action

Updated: 2026-08-13

## Current Status

`CLOCKWORK_VOICE_OBJECTIVE_UI_READY`

Working branch: **`Local` only**.

## Current state

Project Document Generator PRD core remains **v1.13.0**. Voice Production Kit is **v1.11.1** and remains **Eleven v3 only**.

Clockwork continues to use one human-facing project document:

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

Clockwork PRD meaning, `work/render-data.json`, Voice wording, performance tags, Voice asset count, and actor selection were not changed by the v1.11.1 UI refinement.

## Directed performance baseline

Every standalone canonical `performance` block begins with at least one deliberate initial Audio/Performance Direction Tag. Transition tags remain conditional on real audible state changes.

Current Voice Setup baseline:

```text
Custodian Vex → William Shanks - Rich and Deep
Model → Eleven v3
```

The commercial voice is selected for preparation/operator use but has **not** been audio-tested or audio-approved.

## Production Assets → Voice v1.11.1

All gameplay Voice pages now use the same objective shell, including short sections such as The Antechamber.

The section shell derives from accepted project data:

```text
Gameplay Order / objective title
→ PRD package label + gameplay context
→ Voice line count + Primary Speaker
→ compact Voice Setup
```

Each Voice entry derives implementation-facing placement without adding a new canonical field:

```text
title
→ <PRD package label> · Voice Line X/Y
→ Context = exact Flow 5 Trigger
→ Speaker · Estimated Duration
→ exact Eleven v3 prompt
→ Copy Prompt
```

Examples now visible in Gremlin's Workshop:

```text
Build One Live Network
Objective 4 · Voice Line 1/3
Context: The player enters the Workshop and conduit interaction becomes active on the unsabotaged 3×3 grid.

Gremlin Sabotage Reaction
Objective 4 · Voice Line 2/3
Context: About 20 seconds after Ring 2 stabilizes, the scripted Gremlin event visibly breaks one authored active connection and input is briefly locked.

Highlight-Only Assist
Objective 4 · Voice Line 3/3
Context: The configured Workshop assist threshold is reached and Vex highlights one useful node, connection, or region without changing the board.
```

The exact Flow 5 Trigger remains owned by `work/voice-requirements.md`; it is only projected into HTML for developer setup. `work/voice-production.md` remains minimal and unchanged.

`Copy Prompt` still copies only the exact hidden canonical `performance` payload.

## Consolidated navigation

When Production Assets exists, professional navigation is now:

```text
01 Overview
02 Gameplay Flow
03 Development
04 Production Assets
05+ gameplay/objective packages
```

The package number shift is presentation-only in the consolidated HTML. A PRD with no Production Assets keeps its original PRD-core navigation/page numbering.

## Validation

Current non-audio delivery remains:

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

Proof completed for v1.11.1:

- full PRD contract suite passed;
- Voice contract suite passed with the new project-HTML objective/context contract;
- Clockwork rerender passed from canonical source;
- Clockwork Voice mechanical validator passed;
- consolidated navigation asserts passed (`04 Production Assets`, packages `05+`);
- exact Flow 5 Trigger context was verified in rendered Gremlin entries;
- actual desktop browser capture passed for The Antechamber and The Gremlin's Workshop;
- no clipping/overlap was observed in those representative pages;
- temporary review workflows self-removed after use.

## Audio boundary

No ElevenLabs generation, listening, A/B comparison, measured-duration calibration, or generated-audio quality claim has been performed.

`voice_delivery_ready` means the **non-audio script + consolidated project HTML** are production-ready. It does not mean the generated Voice assets or selected commercial voice are audio-approved.

## Overdevelopment guard

Do not add a generic Asset framework, second Voice HTML, duplicate Context field, asset manifest, new Flow, tag score, large tag library, SFX/Visual implementation, or more proof layers without a concrete production need.

## Next Step

**Keep Clockwork v1.11.1 as the non-audio production baseline. Enter SoundMaker Generation Mode only when the user explicitly asks to generate/test audio, or reopen only affected Voice IDs when content/performance requirements change.**
