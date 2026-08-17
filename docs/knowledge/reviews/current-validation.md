# Current Validation Status

Updated: 2026-08-18

This file records the **current evidence state only**. Historical debugging, superseded visual failures, and earlier review detail remain in Git history and historical review files.

## Current system state

Working branch: `Local`.

PRD Creator package remains **v1.14.0**. Voice production scope remains **Eleven v3** inside the unified package.

Current project-document authority shape:

```text
project discussion + original source + approved decisions
→ complete approved project model
   ├─ PRD core 01–03
   │  → work/content.md
   │  → work/render-data.json
   └─ justified non-Voice 04 Production Assets
      → work/asset-requirements.md
→ one deterministic versioned delivery
→ output/README.md
→ output/v<document.version>/prd.html
→ output/v<document.version>/context.md
→ output/v<document.version>/index.json
```

Production Asset needs are recovered with the same project model during Flow 2. Finished/generated 01–03 is not the normal discovery authority for 04.

01–03 remain protected by the Golden/content/renderer contract. The bounded responsive Golden correction recorded below changes presentation mechanics only; it does not change accepted PRD meaning or page identities.

## Current 04 contract

04 navigation is objective-first and each page body is moment-first.

Visible resource types are:

```text
MODEL
ITEM
UI / TEXT
AUDIO
PARTICLE
```

Current reader-first fields:

```text
MODEL / ITEM / PARTICLE
→ Function
→ Visual Brief
→ optional real approved Size

UI / TEXT
→ Function
→ exact Player Text

standalone non-dialogue AUDIO
→ Function
→ Audio Brief

dialogue AUDIO
→ Function
→ Voice Preset
→ ElevenLabs Model = Eleven v3
→ Estimated Duration
→ exact Prompt
```

Internal parser headings (`3D Models`, `UI & Information`, `Audio`, `Visual Effects & Presentation`) remain backward-compatibility source grouping only. They are not visible taxonomy/dashboard requirements.

Generic visible `Requirement / Usage / States / Position / Orientation / Reuse / Used At / Build Specs`, fake gameplay SEQUENCE assets, line-count/Primary-Speaker Voice summaries, Flow 5 Context rows, and separate visible Speaker rows are not part of the current reader-first 04 contract.

## Readiness proof boundary

`kits/prd-creator/production-assets/CONTRACT.md` owns one integrated 04 readiness gate covering coverage, authority, actionability, correct gameplay moment/context, content purity, exact known facts/copy, reader usability, duplication/shared-resource economy, and PRD-core 01–03 protection.

`kits/prd-creator/document/VALIDATION.md` applies that gate inside the existing Flow 4 `Semantic Readiness` result. There is no separate Production Assets PASS field, workflow, schema, or approval document.

Mechanical validation/source freshness does not by itself prove that an asset brief is professionally actionable.

## Current regression evidence

The current PRD Creator 04 regression covers objective-first navigation, moment-first page bodies, current resource-type rendering, reader-first fields, Voice/non-Voice merge, retired-presentation absence, integrated readiness ownership, and stable semantic 04 page IDs.

Repository-wide and PRD contract verification remain the repeatable mechanical proof owners for repository/04 synchronization. Voice Verify remains the Voice semantic/validator proof owner when those executable contracts change.

## Current browser visual evidence

Actual Chromium QA was run on the exact source-first Clockwork candidate that is now committed byte-for-byte as current repository state:

```text
workspace/active/the-clockwork-vault/output/v1.0.0/prd.html
Git blob: 3267b2f97e7335418a43edd6b0e81f6077aeeb51
Golden/runtime Git blob: 2050b965768489feda98373c2920bbee8c7093b3
Chromium: 144.0.7559.96
Viewports: 1500×1000 and 1000×1000
```

Current result:

```text
Project HTML Visual: PASS
```

Evidence:

- document/body horizontal overflow = 0 at both target viewports;
- at 1000px, `Complete Gameplay Journey` is no longer clipped: `.journey scrollWidth=566`, `clientWidth=566`;
- representative Overview, Gameplay Flow, Development, sidebar/page navigation, and active-state behavior = PASS;
- all seven 04 Production Assets pages show zero viewport/internal overflow;
- 53 production rows and 19 Voice AUDIO rows remain readable;
- Voice AUDIO fields including Function, Voice Preset, ElevenLabs Model, Estimated Duration, and Prompt remain readable;
- current Clockwork visibly exercises `MODEL`, `ITEM`, `UI / TEXT`, and `AUDIO`; it contains no current `PARTICLE` row, so this real-project browser proof does not claim a Clockwork PARTICLE sample;
- Chromium page errors and console warnings/errors = 0.

The intermediate-width Golden correction is limited to `761–1100px`, where the Overview journey becomes three columns × two rows. Widths above `1100px` retain the existing six-column layout, and the existing `<=760px` mobile rule is unchanged.

The exact regenerated candidate also passed the current Clockwork PRD validator, PRD→Voice handoff validator, and Voice validator before publication. `context.md` and `index.json` remained unchanged:

```text
context.md  003cc0068505339b8406b445601b7350bffa70a5
index.json   c205422dc0d639b5d0bf9081364321c318e23d22
```

Because the committed Golden/runtime and `prd.html` blobs exactly match that proven candidate, the browser evidence applies to current repository state.

## Current Voice presentation

Voice remains canonical in:

```text
work/voice-requirements.md
→ work/voice-production.md
```

The consolidated project HTML presents each line as an `AUDIO` resource in the matching natural gameplay moment. Flow 5 Trigger/Purpose/source refs remain in Voice owners and are not visible 04 metadata.

Generated-audio quality remains unproven unless actual audio exists and is reviewed.

## Current continuation

Current continuation is owned by `docs/knowledge/next-action.md`.
