# Current Validation Status

Updated: 2026-08-16

This file records the **current evidence state only**. Historical debugging, earlier category-dashboard/browser proof, and superseded review detail remain in historical review files and Git history.

## Current system state

Working branch: `Local`.

Project Document Generator remains **v1.14.0**. Voice Production Kit remains **v1.11.2**.

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

01–03 remain protected by the existing Golden/content/renderer contract. The 04 work does not change Golden bytes, accepted PRD-core page identities, or the 01–03 style/structure.

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

`PRODUCTION-ASSETS.md` owns one integrated 04 readiness gate covering:

- coverage;
- authority;
- actionability;
- correct gameplay moment/context;
- content purity;
- exact known facts/copy;
- reader usability;
- duplication/shared-resource economy;
- PRD-core 01–03 protection.

`VALIDATION.md` applies that gate inside the existing Flow 4 `Semantic Readiness` result. There is no separate Production Assets PASS field, workflow, schema, or approval document.

Mechanical validation/source freshness does not by itself prove that an asset brief is professionally actionable.

## Current regression evidence

The current Project Document 04 regression covers:

- objective-first navigation;
- moment-first page bodies;
- MODEL / UI / TEXT / AUDIO / PARTICLE rendering;
- Function + Visual Brief / exact Player Text / AUDIO production fields;
- Voice Preset + ElevenLabs Model + Estimated Duration + exact Prompt;
- absence of retired visible Requirement / Usage / category-count/dashboard presentation;
- absence of visible Flow 5 Trigger Context and separate Speaker metadata;
- Voice/non-Voice merge on the same 04 page;
- asset-only, Voice-only, mixed, and no-downstream behavior;
- integrated 04 readiness-owner presence;
- stable semantic 04 page IDs.

Repository-wide and PRD contract verification remain the repeatable mechanical proof owners for repository/04 synchronization. Voice Verify remains the Voice semantic/validator proof owner when those executable contracts change.

## Visual evidence boundary

Earlier browser proof for the pre-humanized objective/category presentation is historical evidence only and must not be reused as a visual PASS for the current humanized moment-first 04 layout.

The latest 04 renderer/output has user-approved content/presentation direction and mechanical contract coverage, but **current browser-level visual proof for the final humanized layout is NOT PROVEN in this evidence owner** unless a later review records actual browser evidence.

Do not infer visual PASS from static HTML, CI, or an older layout proof.

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
