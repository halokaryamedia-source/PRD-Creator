# Next Action

## Current Status

`CLOCKWORK_BROWSER_VISUAL_QA_ACTIVE`

The unified `kits/prd-creator/` migration is complete. The user explicitly approved the next bounded task: prove the final current Clockwork project HTML visually in an actual browser.

## Active Boundary

Target repository/branch:

```text
halokaryamedia-source/PRD-Creator
Local
```

Pinned starting HEAD:

```text
4691af6013d552122e49eacc7ebc97f0469fa19b
```

Real-project acceptance sample:

```text
workspace/active/the-clockwork-vault/output/v1.0.0/prd.html
Git blob: dac955a4a482ad9dc2035f0c5714c87ae4de05c5
```

This task is visual QA / acceptance, not a renderer redesign or architecture cleanup.

## Goal

Establish truthful browser evidence for the final humanized Clockwork `prd.html`, especially the current objective-first / moment-first `04 Production Assets` presentation that is currently mechanically covered but browser-level `NOT PROVEN`.

## Browser acceptance scope

Render the exact current Clockwork `prd.html` in Chromium and inspect at minimum:

```text
1500 × 1000  desktop
1000 × 1000  laptop / narrower desktop
```

Check:

1. PRD core 01–03 remains visually intact;
2. sidebar/navigation activation and page switching work;
3. 04 Production Assets pages are readable and clearly grouped by gameplay moment;
4. MODEL / ITEM / UI-TEXT / AUDIO / PARTICLE resources remain distinguishable;
5. typography, spacing, alignment, hierarchy, and information density are usable;
6. no clipping, overlap, hidden content, broken sticky/sidebar state, or accidental horizontal page overflow;
7. Voice AUDIO cards remain readable, including Function, Voice Preset, ElevenLabs Model, Estimated Duration, and Prompt;
8. no visual claim is upgraded from static/CI evidence alone.

## Source-change gate

Do not change renderer, template, canonical PRD, Production Assets requirements, or current Clockwork output merely because visual QA is running.

If browser evidence finds a real defect:

```text
reproduce exact defect
→ identify first wrong owner
→ smallest complete source fix
→ regenerate only invalidated derived output
→ repeat only invalidated browser/mechanical proof
```

Do not hand-patch `prd.html`.

## Protected boundaries

Do not change during this task unless a reproduced visual defect requires the matching owner:

- gameplay/project meaning;
- Voice requirement/wording/performance;
- Golden contract for preference/cosmetic reasons;
- unified package architecture;
- tests/tools organization;
- export formats;
- conditional backlog items RQ-09/RQ-10/RQ-11/RQ-14.

## Completion rule

If both target viewports and representative navigation/pages pass without material visual defects, record the current evidence owner as:

```text
Project HTML Visual: PASS
```

with the exact Clockwork blob/viewport/evidence boundary, then return `next-action.md` to `STOP`.

If a defect is found, keep this task active and record only the reproduced defect + first wrong owner as the next step.

## Next Step

**Run actual Chromium visual QA on the exact Clockwork `prd.html` blob `dac955a4a482ad9dc2035f0c5714c87ae4de05c5` at 1500×1000 and 1000×1000, including representative PRD 01–03 pages, 04 Production Assets pages, sidebar/page navigation, and overflow/layout checks. Do not edit source unless a concrete browser defect is reproduced.**
