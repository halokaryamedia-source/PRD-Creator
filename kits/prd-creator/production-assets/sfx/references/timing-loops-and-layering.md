# Timing, loops and layering

Read only the relevant section. This is repository craft policy; documented capabilities are scoped in [contracts](elevenlabs-contracts-and-sources.md).

## Timing is not one number

Separate authoritative sync/deadline, requested file duration, event onset, event body, and tail. A production duration recommendation is reversible and must not become upstream gameplay timing. Manual duration can be justified by editability or bounded exposure even when the project has no exact timing constraint. Auto is a choice, not a mandatory cheap mode.

For a sub-minimum final cue, request a valid-length source and edit a useful event if feasible; do not ask the API for an invalid duration. For an attack contact synchronized to an animation, identify the audible contact and align that point downstream. More timestamp prose cannot replace an unavailable exact-time control. Leave useful attack/tail handles; excessive cropping or aggressive fades can damage the cue.

For fixed sequences, ordered words may direct progression. For independently triggered actions, use separately controllable assets. A startup inside a repeated run loop will restart on every repetition; keep startup/run/stop apart when required. Generation duration does not implement the engine's loop lifecycle.

## Loop types

| Type | Direct | Listen for |
|---|---|---|
| Steady bed | Continuous rain, wind or room texture | Level/timbre continuity, no unrequested entrance/exit |
| Cyclic mechanism | Motor rotation or repeated mechanical cycle | Stable cycle and plausible load |
| Evolving bed | Slow bounded movement within sustained texture | Audible reset or drift that cannot repeat |
| Rhythmic loop | Wheel/rail or timed mechanism | Cycle timing; missing/doubled pulse at join |
| Bed plus spots | Bed separate from distinctive independent events | Obvious repeated foreground event; masking |

A continuous sound is not automatically intended to loop. A long finite ambience can remain non-looping. Enable loop only for repeat playback; this does not prove that any candidate or target codec is seamless.

Review consecutive repetitions, including the join in context. Check discontinuity/click, short silence, level dip, spectral/color change, cycle mismatch and distinctive recurring spots. A waveform match alone cannot prove a convincing perceptual loop.

## Editing before another generation

Preserve the original. Try a suitable edit region, trim unintended silence, or a short crossfade only when it preserves the sound's job. Do not crossfade a rhythmic contact into a doubled hit. Stereo channels must remain coherent; mono downmix needs a listening check for cancellation or loss of character.

[Audacity's zero-crossing guidance](https://manual.audacityteam.org/man/select_menu_at_zero_crossings.html) explains why near-zero cuts reduce clicks and why stereo may not share matching crossing points. Use that as an editing aid, not a seam guarantee. Listen to the exported target file again; a good editor loop is not proof of target playback.

A badly distorted source, wrong identity or missing event may not be worth salvaging. Avoid endless editing just to avoid a justified new take, but keep any paid retry inside the approved budget.

## Layering anatomy

Consider dominant onset, body/resonance, useful detail and tail. They are listening roles, not four mandatory generation requests.

| Effect | Possible distinct roles | Reason to separate |
|---|---|---|
| Heavy impact | Contact, body, fragments, decay | Independent control or reused debris |
| Machinery | Motor, movement, air, load-dependent rattle | State-dependent activation or level |
| Eruption | Pressure bed, main blast, debris, environmental tail | Independent cues or unreadable combined result |
| Moving vehicle | Drive source, rolling contact, wind | Different playback dependencies |

Prefer a coherent single generation when that satisfies the job. Split when independence matters or a combined approach cannot meet the brief cleanly. Do not demand paid failure first when the approved design already requires independent components. Conversely, do not add a sub-bass layer merely because a cinematic recipe lists one.

Review layers separately and together at intended levels. Check attacks, low-frequency competition, clutter and cumulative level. Do not normalize every layer to the same loudness and then sum blindly. For a fixed composite, retain a composite derivative when useful; independently controlled runtime layers require a real playback plan and concurrency review.

## Source versus playback space

A mobile positional source usually benefits from an adaptable recording perspective rather than baked distant pass-by or cave reverb. A fixed cinematic may intentionally include location/trajectory. A UI cue may be listener-relative. An ambience may intentionally contain a spatial field. These are project choices, not claims that every engine supplies reverb, occlusion or seamless crossfading.

Keep source sound, playback distance/attenuation, spatialization, environment and triggering ownership separate. Recover actual target capabilities before promising an effect. Do not spend generation budget trying to fix a wrong event mapping, playback level or distance configuration.

Studio is an optional timeline editor for placement and layers; it is not required for local edits and does not make generation/free-regeneration offers interchangeable across media. See [execution](execution-and-cost-control.md) before any action that might invoke paid generation.
