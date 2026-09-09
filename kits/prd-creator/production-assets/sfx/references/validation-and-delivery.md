# Validation and delivery

Read for candidate review, diagnosis or handoff. This is repository acceptance policy, not a new persisted status schema. Product/export facts: [contracts](elevenlabs-contracts-and-sources.md). Paid actions: [execution](execution-and-cost-control.md).

## Separate proof levels

| Evidence level | What may be concluded | What may not be concluded |
|---|---|---|
| Prepared | Brief conserved; prompt/settings and operator plan are usable | Audio quality, exact duration, seamless loop, spend permission |
| Generated, unreviewed | A real file/response was obtained | Audible correctness or family continuity |
| Audio accepted | Identified file was heard and accepted against the brief | In-game timing, mix or spatial behavior without target evidence |
| Target verified | Identified build/export was tested in the actual target context | Other builds, codecs or future regenerated takes are identical |

Retain the existing conceptual **SFX Production Readiness: PASS / FAIL** for preparation. It is not permission to spend. Do not add statuses to Voice lifecycle or acceptance parsers. Report the strongest evidenced level and explicit gaps.

## Preparation review

Check source/event and gameplay information, exclusions, approved timing, smallest sufficient composition, family strategy when relevant, documented parameters, intended export/playback route and review criteria. State assumptions as reversible craft choices; unresolved material project meaning goes upstream. A static parameter/link test cannot approve a prompt's acoustic performance.

## Heard review and diagnosis

Listen at comfortable comparable levels; do not prefer a louder candidate solely because it appears more impressive. Check identity/material, the required state difference, onset/body/tail, unwanted speech/music/events, usable dynamic range, perspective and editability. Evaluate family members against the retained anchor, not memory alone.

| Defect | First owner/action |
|---|---|
| Requirement is wrong or materially ambiguous | Production Assets / approved source |
| Correct requirement, prompt describes another event | Smallest prompt correction |
| Correct brief/prompt, isolated deviant take | Available candidate comparison; no automatic rewrite |
| Important descriptor repeatedly absent | Wording clarity, then a justified settings experiment |
| Good source, excess silence/level/edit-point issue | Non-destructive edit and recheck before new generation |
| Tail/transient clipped or required event absent | Evaluate recoverability; bounded new take if necessary |
| Family identity drifts | Baseline and state delta, then only invalidated members |
| Loop click or perceptual reset | Join/cycle review and feasible edit; regenerate only if needed |
| Sound works alone but masks important gameplay | Playback mix/density first; not automatically a new prompt |
| No output in game | Asset path/event/target integration before blaming generation |

Do not require repeated paid evidence for an obvious prompt or parameter error. One better take after a change is a useful candidate, not proof of causality. Prefer a brief reasoned selection over a numerical scorecard.

## Asset QA

Inspect the actual file when tools allow: decodability, codec/container, channels, sample rate, measured duration, empty/truncated content, unwanted silence, clipping/distortion and intended head/tail. A nonzero file is not proof of successful complete audio. No universal LUFS, peak or silence threshold applies to all clicks, ambiences and impacts; use project-approved targets and listen in context.

Keep the original selected bytes. Edit copies; identify source and derivative clearly. Raw PCM requires known sample format/channel/rate and proper container writing, not renaming to WAV. Upsampling/transcoding a compressed source does not recover lost information. Choose the best available authorized source for the downstream job without silently upgrading plans. Inspect target encoding rather than choosing by extension alone.

The [Voice Isolator documentation](https://elevenlabs.io/docs/overview/capabilities/voice-isolator) describes speech extraction. Therefore this policy does not use it automatically for non-speech SFX; it may remove the desired material. Any deliberate cleanup must be compared to the retained original.

## Target QA

Check event trigger and timing, loop lifecycle/start-stop, distances/spatial behavior actually supported, scene mix, repetition fatigue, overlapping sources and unintended stacking. A fixed render must contain the intended SFX tracks; verify the chosen export path supports them. For explicit Bedrock work use [Bedrock delivery](minecraft-bedrock-delivery.md), not generic engine assumptions.

Listen to the exported target file and then its real playback. A clean master loop is insufficient if decoding or scheduling creates a gap. Tests that only parse JSON, check names or compile scripts cannot prove audible target quality.

## Minimal evidence / approval lock

Use existing project execution notes, not another production database. Preserve AST linkage, exact prompt/model/surface/settings, selected file/take, relevant source and derivative identity, measured duration only if measured, review decision and budget usage/uncertainties. Useful file hashes can identify accepted bytes, but do not create a global cache/index solely for this purpose.

User edits to a prompt/settings must be retained with the take they produced. Approval binds that file and reviewed behavior; it does not guarantee a regenerated clone. Preserve same-project calibration and avoid promoting it into general model policy. Do not rewrite `work/asset-requirements.md` unless approved required meaning changed.

## Small calibration plan, only when authorized

No benchmark generation runs in CI. Choose the smallest cases relevant to the project, not this entire list by default.

| Case | Falsifiable listening question |
|---|---|
| Single impact | Correct contact/material, without extra repeated hits? |
| Foot/contact | Surface and weight readable, reusable onset intact? |
| Continuous loop | Join and level stable on repeat? |
| Rhythmic loop | No doubled/missing pulse at the join? |
| Related state pair | Same identity with the required audible difference? |
| Ordered sequence | Correct progression; what editing is still needed? |
| UI cue | Information clear in its actual mix? |

Freeze configuration for candidate comparisons. Test language, phrase length or influence as separate hypotheses when a real defect warrants it. Record accept/reject, reason, exact setup, edits and verified spend. Do not publish fake readiness percentages, guaranteed savings or acoustic PASS from static checks.
