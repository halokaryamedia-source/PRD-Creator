# Minecraft Bedrock delivery

Load only for an explicitly approved Bedrock target. This is an optional delivery reference, not a runtime exporter, new MCP tool or authority to edit a game repository.

Official reference checked 2026-09-09: [Creating and Adding Custom Sounds](https://learn.microsoft.com/en-us/minecraft/creator/documents/addcustomsounds?view=minecraft-bedrock-stable). The tutorial documents OGG assets, `sounds/sound_definitions.json`, event configuration through `sounds.json`, multiple alternatives, pitch/volume examples and `/playsound` testing. Its example fields are not a complete cross-version schema.

## Handoff, not invented engine behavior

Recover target Bedrock version, existing resource-pack owner, event namespace, playback mechanism and actual approved requirements. Map the existing AST to the project's sound event and file path; do not silently create gameplay triggers or export a replacement pack. Keep generation-specific metadata outside the engine schema.

For the chosen target, hand over selected/edited audio, identity mapping, one-shot/loop intent, trigger/contact alignment, needed state transitions, approved level/spatial intent, alternatives when justified, and target-test status. Do not label an asset integrated until that target has been tested.

## File and variation policy

Use the project's verified codec/container convention; the official tutorial uses OGG. Do not assume that every codec in an OGG container is supported, or that changing an extension performs conversion. Preserve the source master and verify the encoded derivative. Choose mono/stereo deliberately for the actual playback path; do not promise positional behavior based only on a prompt's word "mono" or a file extension.

Use existing multiple-sample/pitch/volume mechanisms where they preserve the required sound and are supported in the selected mapping. Do not copy fields between sound definitions, event mappings, animation configuration and scripts without checking the exact schema. Random selection does not guarantee a no-repeat rule. Generation of more samples is justified by observed repetition and required performance, not a fixed count.

Keep independently triggered startup, run and stop controllable. A generated loop is just audio: the game owner must implement starting, repetition, stopping, cleanup and any supported transitions. Avoid accidental overlapping loop instances. Do not infer gapless scheduling, dynamic reverb, occlusion, anti-repeat, streaming or a fixed simultaneous-voice limit without version-specific evidence.

## Target test order

First check file path/codec and sound-event mapping. Then audition through the actual approved event; `/playsound` can help isolate loading from trigger logic, but does not test the entire entity behavior. Next check contact timing, near/far behavior, start-stop cleanup, repeated playback, scene mix and overlapping actors on representative hardware.

Use ordinary minimum-content test scenes and the real resource pack; do not change unrelated world/gameplay data as part of SFX delivery. Playback issues usually belong to mapping/mix/runtime before another paid generation. Retain target version/build and evidence with the selected file. If runtime tests are not performed, report audio-prepared or audio-accepted only, not Bedrock-ready.
