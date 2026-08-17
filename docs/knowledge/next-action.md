# Next Action

## Current Status

`CLOCKWORK_OVERVIEW_RESPONSIVE_FIX_READY`

The unified `kits/prd-creator/` migration is complete. The user explicitly approved final browser visual QA of the current Clockwork project HTML. Actual Chromium QA found one reproducible PRD-core responsive defect; the smallest source-first fix has been prepared and proven locally but is not yet committed to the repository.

## Active Boundary

Repository/branch:

```text
halokaryamedia-source/PRD-Creator
Local
```

Current committed Clockwork acceptance sample remains:

```text
workspace/active/the-clockwork-vault/output/v1.0.0/prd.html
Git blob: dac955a4a482ad9dc2035f0c5714c87ae4de05c5
```

Do not mark current Project HTML Visual PASS while that blob remains current.

## Reproduced browser defect

Actual browser:

```text
Chromium 144.0.7559.96
1500×1000
1000×1000
```

1500×1000 passed the requested representative visual checks.

At 1000×1000, `01 Overview → Complete Gameplay Journey` is materially clipped:

```text
.journey scrollWidth = 658
.journey clientWidth = 566
hidden overflow = 92 px
```

The sixth journey card is visibly cut by the page boundary.

No equivalent defect was found in current 04 Production Assets:

```text
7 Production Assets pages inspected
53 resource rows
19 Voice AUDIO rows
viewport overflow = 0
internal overflow = 0
page errors = 0
console warnings/errors = 0
```

Representative Overview / Gameplay Flow / Development / 04 navigation clicks all reached their intended section and active navigation state at both target viewports.

Current Clockwork contains real `MODEL`, `ITEM`, `UI / TEXT`, and `AUDIO` rows. It contains no current `PARTICLE` row, so do not claim a real-project PARTICLE browser sample from Clockwork.

## First wrong owner

This is a presentation-mechanics defect in the protected PRD-core Golden responsive CSS, not project/gameplay/Voice meaning.

Owner:

```text
kits/prd-creator/template/golden-reference.html
kits/prd-creator/template/runtime-template.html
```

The two template files must remain byte-identical.

Do not fix this in `prd.html`, Production Assets CSS, asset requirements, Voice content, or project data.

## Exact fix candidate

Add only this intermediate-width rule to the Golden CSS before the existing <=760px rule:

```css
@media(min-width:761px) and (max-width:1100px){
  .journey{grid-template-columns:repeat(3,1fr)}
  .journey article+article{border-left:0}
  .journey article:nth-child(3n+2),
  .journey article:nth-child(3n+3){border-left:1px solid var(--line)}
  .journey article:nth-child(n+4){border-top:1px solid var(--line)}
}
```

Behavior:

```text
>=1101 px  → existing six-column journey
761–1100   → three columns × two rows
<=760      → existing mobile rule remains unchanged
```

No content, page identity, DOM vocabulary, gameplay, Production Asset requirement, or Voice wording changes.

## Proven local candidate identity

Source-first local regeneration produced:

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

The exact candidate was produced by changing the template source and running the canonical renderer/delivery path. The generated `prd.html` was not hand-patched.

## Local candidate proof already completed

At 1500×1000 and 1000×1000 on Chromium 144.0.7559.96:

```text
document/body horizontal overflow = 0
1000px journey scrollWidth/clientWidth = 566/566
representative nav click + active state = PASS
all seven 04 pages viewport/internal overflow = 0
Voice AUDIO production fields readable = PASS
page/console errors = 0
```

Current Clockwork validation against that regenerated candidate:

```text
PRD validator = PASS
PRD → Voice handoff validator = PASS
Voice validator = PASS
```

## Files that must change together

One bounded logical delivery must include:

```text
kits/prd-creator/template/golden-reference.html
kits/prd-creator/template/runtime-template.html
kits/prd-creator/renderer/CONTRACT.md

docs/knowledge/decisions/golden-reference-fidelity.md

tests/test_prd_golden_reference.py

workspace/active/the-clockwork-vault/output/v1.0.0/prd.html

docs/knowledge/reviews/current-validation.md
docs/knowledge/next-action.md
```

Update current Golden SHA owners/test from:

```text
e1dccd77d7a5335213caea7a09d74ba78b2ae8e1
```

to the proven candidate:

```text
2050b965768489feda98373c2920bbee8c7093b3
```

Historical review/audit records that truthfully describe the former Golden blob must remain historical and must not be rewritten merely to erase the old hash.

## Required publish/proof sequence

Use a channel with a real local git workspace / safe patch-and-commit capability for the large tracked template/generated HTML files. Do **not** use GitHub Actions as a remote shell and do not full-reconstruct 795 KB/761 KB files through per-file connector replacement.

```text
pin current Local
→ apply exact Golden CSS fix to both byte-identical templates
→ update current Golden SHA owners + exact-Golden test
→ run canonical Clockwork delivery regeneration
→ confirm context.md/index.json unchanged
→ confirm regenerated prd.html Git blob = 3267b2f97e7335418a43edd6b0e81f6077aeeb51
→ run PRD/hand-off/Voice validation
→ run browser QA at 1500×1000 + 1000×1000
→ commit one coherent fix delivery
→ PRD Verify + Repository Verify
→ record Project HTML Visual: PASS
→ STOP
```

Voice Verify is not required unless the final diff unexpectedly touches Voice executable/canonical owners.

## Protected boundaries

Do not use this defect to change:

- project/gameplay meaning;
- Voice requirements/wording/performance;
- 04 Production Assets presentation that already passed both target viewports;
- page identities/navigation hierarchy;
- unified package architecture;
- tests/tools organization beyond the exact Golden identity update;
- RQ-09/RQ-10/RQ-11/RQ-14;
- export formats.

## Recovery

If a new session resumes here:

1. read this file after normal repository boot;
2. do not repeat the migration or broad visual audit;
3. current defect is already reproduced;
4. use the exact CSS and expected Git blobs above;
5. do not mark PASS until the fixed source + regenerated current output are actually committed and relevant proof is green.

## Next Step

**Apply the proven Golden responsive fix through a safe local/Codex git workspace, regenerate Clockwork from source, and publish the bounded fix only if the committed template/output identities and PRD/browser proof match the candidate above. Then change current browser evidence to `Project HTML Visual: PASS` and STOP.**
