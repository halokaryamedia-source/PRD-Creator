# Current Validation Status

Updated: 2026-08-17

This file records the **current evidence state only**. Historical debugging, earlier category-dashboard/browser proof, and superseded review detail remain in historical review files and Git history.

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

`kits/prd-creator/production-assets/CONTRACT.md` owns one integrated 04 readiness gate covering:

- coverage;
- authority;
- actionability;
- correct gameplay moment/context;
- content purity;
- exact known facts/copy;
- reader usability;
- duplication/shared-resource economy;
- PRD-core 01–03 protection.

`kits/prd-creator/document/VALIDATION.md` applies that gate inside the existing Flow 4 `Semantic Readiness` result. There is no separate Production Assets PASS field, workflow, schema, or approval document.

Mechanical validation/source freshness does not by itself prove that an asset brief is professionally actionable.

## Current regression evidence

The current PRD Creator 04 regression covers:

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

## Current browser visual evidence

Actual Chromium QA was run on the exact currently committed Clockwork project document:

```text
workspace/active/the-clockwork-vault/output/v1.0.0/prd.html
Git blob: dac955a4a482ad9dc2035f0c5714c87ae4de05c5
Chromium: 144.0.7559.96
Viewports: 1500×1000 and 1000×1000
```

Current result:

```text
Project HTML Visual: FAIL — one reproducible responsive defect
```

Evidence:

- 1500×1000: representative Overview, Gameplay Flow, Development, sidebar/navigation, 04 Production Assets, and Voice AUDIO presentation are visually usable with no document-level horizontal overflow;
- 1000×1000: all seven 04 Production Assets pages show zero viewport/internal overflow, 53 production rows and 19 Voice rows remain readable, and representative sidebar/page navigation reaches the intended target with the correct active state;
- current Clockwork visibly exercises `MODEL`, `ITEM`, `UI / TEXT`, and `AUDIO`; it contains no `PARTICLE` row, so current-project browser evidence does not claim a real Clockwork PARTICLE sample;
- no Chromium page error or console warning/error was observed at either target viewport;
- one material defect remains in `01 Overview`: the six-column `Complete Gameplay Journey` grid is wider than its readable content area at 1000×1000. Measured `.journey` width is `scrollWidth=658` vs `clientWidth=566`, leaving 92 px of hidden/clipped content and visibly truncating the sixth journey card.

The defect is presentation mechanics, not project/content meaning. Its first wrong owner is the Golden responsive CSS used by `template/golden-reference.html` and byte-identical `template/runtime-template.html`.

### Proven local fix candidate — not yet current repository state

A source-first local candidate was tested without hand-patching generated HTML:

```css
@media(min-width:761px) and (max-width:1100px){
  .journey{grid-template-columns:repeat(3,1fr)}
  .journey article+article{border-left:0}
  .journey article:nth-child(3n+2),
  .journey article:nth-child(3n+3){border-left:1px solid var(--line)}
  .journey article:nth-child(n+4){border-top:1px solid var(--line)}
}
```

The candidate preserves six columns above 1100 px and the existing <=760 px mobile rule. It changes only the intermediate-width Overview journey layout.

Local proof of that exact candidate:

```text
Golden/runtime candidate Git blob
2050b965768489feda98373c2920bbee8c7093b3

regenerated Clockwork prd.html candidate Git blob
3267b2f97e7335418a43edd6b0e81f6077aeeb51

context.md unchanged
003cc0068505339b8406b445601b7350bffa70a5

index.json unchanged
c205422dc0d639b5d0bf9081364321c318e23d22
```

After source-first regeneration, actual Chromium proof at both 1500×1000 and 1000×1000 showed:

- document/body horizontal overflow: 0;
- 1000 px Overview journey: `scrollWidth=566`, `clientWidth=566`;
- all representative navigation clicks: PASS;
- all seven 04 pages: zero viewport/internal overflow;
- Voice production fields remain readable;
- page/console errors: 0.

The regenerated candidate also passed the current Clockwork PRD validator, PRD→Voice handoff validator, and Voice validator locally.

This candidate is **not** upgraded to current `Project HTML Visual: PASS` until the Golden source change and regenerated project HTML are safely committed to `Local` and the current proof gates are re-confirmed.

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